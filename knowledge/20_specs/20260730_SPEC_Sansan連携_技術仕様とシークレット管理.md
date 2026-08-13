# Sansan連携 技術仕様・シークレット管理（Claude Code共有用）

**作成日**: 2026-07-30
**対象読者**: Claude Code / CCWセッション（前提知識ゼロで読める自己完結ドキュメント）
**スコープ**: Sansan Open APIの確定仕様、LINE配信botの実装、シークレットの管理ルール
**正本の置き場**: 本ドキュメントの正本はsnj-knowledgeに置く（このファイルはCoworkで作成したドラフト。repoへのコミットは高山がCCWで実施）

---

## 1. システム全体像

```
Sansan（営業全員がスマホでコンタクト登録。3類型テンプレート運用）
   │  GET /v6.0/reports（日次ポーリング）
   ▼
Google Apps Script「Sansan商談ダイジェストbot」 ← ★本番ランタイム。コード正本もGAS
   │  POST https://api.line.me/v2/bot/message/push
   ▼
LINEグループ（蜂巣・高山・田嶋・杉田・エディ＋bot）… 平日18時台に日次ダイジェスト
```

- **GASが本番ランタイム**。リポジトリ側にデプロイパイプラインはない。コードを変更する場合はGASエディタに貼って保存する（clasp等は未導入）
- 関連する既存基盤: 週次のコンタクトCSV→台帳転記（高山・手動）、ナレフル案件整理アシスタント。botはこれらと独立で、読み取り専用

## 2. Sansan Open API 確定仕様（2026-07-30実機確認済み）

### 2.1 認証・共通

| 項目 | 値 |
|------|-----|
| ベースURL | `https://api.sansan.com` |
| 認証 | リクエストヘッダー `X-Sansan-Api-Key: {APIキー}` |
| APIキー | Sansan管理画面から**ユーザー単位**で発行。現行キーは高山ユーザーに紐づく |
| レート制限 | 300リクエスト/分（429で超過通知） |
| アクセス範囲 | 自社が保有するコンタクト情報のみ（他社データは参照不可） |
| 公式リファレンス | https://docs.ap.sansan.com/ja/api/openapi/index.html ※**機械取得不可（robots制限）**。仕様確認はブラウザで行うこと |

### 2.2 コンタクトAPI（商談・活動記録）★重要

**エンドポイントは `/reports`。`/contacts` ではない**（ここで一度ハマった。v3.2〜v2.4の `/contacts` は全て404）。

#### コンタクトSet取得

```
GET https://api.sansan.com/v6.0/reports
```

| パラメータ | 必須 | 内容 |
|-----------|------|------|
| updatedFrom | **必須** | コンタクト更新日時 `YYYY-MM-DDThh:mm:ssTZD` 形式（例: `2026-07-30T00:00:00+09:00`）。**`+`はURLエンコード必須（%2B）** |
| updatedTo | **必須** | 同上 |
| range | 任意 | `me`（デフォルト）／`all`。**全社分を取るには明示的に `all` が必要** |
| type | 任意 | 区分での絞り込み。配列形式 `type[]=Meeting&type[]=Call` |
| limit | 任意 | 1〜300（デフォルト100） |
| nextPageToken | 任意 | ページング。レスポンスの `hasMore: true` の間、返却トークンを次リクエストに渡す |
| orderBy / orderDirection | 任意 | `registeredAt`／`updatedAt`（デフォルト）、`asc`／`desc`（デフォルト） |

#### レスポンス（1件あたりの主要フィールド）

| フィールド | 内容 |
|-----------|------|
| id | コンタクトID |
| registeredTime / updatedTime | 登録／更新日時（+09:00付きISO） |
| startDate / endDate | 面談日（面会系で入る。BizCardExchangeでは日付、その他ではnullのことあり） |
| startTime / endTime | 開始・終了日時（BizCardExchangeではnull） |
| owner | `{id, name, email}` 登録者 |
| externalAttendees | `[{id, personId, companyName, lastName, firstName}]` 社外出席者 |
| internalAttendees | `[{id, name, departmentName}]` 社内出席者 |
| type | 区分: `Meeting`(面会) `Visit`(訪問) `MeetingAtOffice`(来訪) `Call`／`OutboundCall`／`InboundCall`(電話系) `Email`／`SentEmail`／`ReceivedEmail`(メール系) `OnlineMeeting`(オンライン会議) `BizCardExchange`(名刺交換・自動) |
| title / location / memo | タイトル・場所・メモ（メモ上限20,000字。テンプレ本文が入る） |
| categories | `[{name, value}]` カスタムカテゴリ |

#### コンタクトデータ登録（未使用だが利用可能）

```
POST https://api.sansan.com/v6.0/reports
```
必須: `startTime`・`endTime`（秒は00のみ）・`externalAttendees`（会社名/姓/名のいずれか必須。新規名刺として作成される）・`type`。任意: `internalAttendeeUserIds`・`title`・`location`・`memo`。
→ 将来「Claude Codeが整理した議事録をSansanに書き戻す」用途に使える。

### 2.3 その他のAPI（今回未使用・存在確認のみ）

名刺API（`/v3.1/bizCards` 等）・人物・組織・タグAPIが存在。バージョンはAPIごとに異なる（名刺はv3系、コンタクトはv6.0）。パラメータ不足時は400を返す（=404が出たらパスが違うと判断してよい）。

## 3. LINE Messaging API 要点

| 項目 | 値 |
|------|-----|
| プッシュ | `POST https://api.line.me/v2/bot/message/push`、`Authorization: Bearer {チャネルアクセストークン}` |
| 宛先 | `to` にグループID。グループIDはWebhookイベント `source.groupId` から採取（bot招待→発言→doPostで記録） |
| 通数カウント | **送信先人数分**（5人グループへ1プッシュ＝5通）。1プッシュに**メッセージオブジェクト5個まで**載せてもカウントは人数分のみ |
| 無料枠 | コミュニケーションプラン 月200通。日次1配信×5人×22営業日≒110通/月で枠内 |
| 1メッセージ上限 | テキスト5,000字 |
| 備考 | LINE Notifyは2025年3月終了。Messaging API一択 |

## 4. GAS bot実装仕様（v0.8）

コード正本: GASプロジェクト「Sansan商談ダイジェストbot」（配布コピー: プロジェクト知識 `claude/20260730_CODE_LINE配信bot_GAS_v08.gs`）

### 抽出・配信ロジック

1. `dailyDigest`（平日18時台トリガー）: `LAST_RUN`（前回実行時刻）〜now を `updatedFrom/To` で取得し、`registeredTime >= LAST_RUN` の**新規登録のみ**に絞る（過去分の編集は流さない）
2. 配信対象フィルタ: **区分が商談系**（Meeting/Visit/MeetingAtOffice/Call/OutboundCall/InboundCall/OnlineMeeting）**かつメモ非空**。タグ有無は問わない（名刺交換・メール自動記録はここで落ちる）
   - 既知の観察: 区分Emailのコンタクトが配信された事例あり（2026-07-30）。メール商談報告を拾いたい場合は `DELIVER_TYPES` にEmail系を追加する（自動取込メールがメモ持ちで混入しないか要観察）
3. 表示: `▼n. [類型] タイトル｜先方社名（M/d面談・登録者・区分）`＋メモ全文（1行目の類型タグ行のみ除去）。類型ラベルはメモ内の【販売商談】【仕入先商談】【関連業者商談】から判定、なければラベルなし。並び順は面談日（startTime>startDate>registeredTime）昇順
4. 分割: コンタクト境界で4,900字以内に分割し、最大5メッセージを1プッシュで送信。0件の日は送信しない
5. 送信成功後に `LAST_RUN` を更新（増分方式）

### ユーティリティ関数

`testSansan`（疎通＋絞り込み結果）／`testDigest`（本番同一ロジックのdry-run）／`testLinePush`／`showCapturedGroups`（Webhookで採取したグループID一覧）／`resetLastRun`（LAST_RUN削除→次回は過去24時間対象）

### 運用上の既知のハマりどころ

- **トリガーの「実行するデプロイ」は必ずHead**。バージョン番号を選ぶとその時点のコードに固定され、以後の修正が反映されない（2026-07-30に実際に発生）
- dailyDigestは実行のたびにLAST_RUNが進む。再テストは `resetLastRun` を挟む（グループに重複配信されるので注意）
- GASのトリガーは「保存済み」コードを実行する。エディタ未保存の変更は走らない

## 5. シークレット管理

### 5.1 正本: GASスクリプトプロパティ（本番ランタイム）

| キー | 内容 | 備考 |
|------|------|------|
| SANSAN_API_KEY | Sansan Open APIキー | ユーザー単位発行。チャット経由で共有された初代キーは**再発行済み（旧キー無効）** |
| LINE_TOKEN | Messaging APIチャネルアクセストークン（長期） | LINE Developersコンソールで発行 |
| LINE_GROUP_ID | 配信先グループID | Webhook採取。本番グループ切替時に差し替え |
| LAST_RUN / CAPTURED_GROUPS | bot内部状態 | 自動管理。手動編集不要 |

### 5.2 GitHub Secrets（リポジトリでSansanを扱う場合）

Claude Code（CCW含む）でSansan APIを叩くコード・分析を書く場合は、以下の命名でリポジトリのSecrets（Settings > Secrets and variables > Actions）に登録して参照する：

| Secret名 | 内容 |
|----------|------|
| `SANSAN_API_KEY` | Sansan Open APIキー |
| `LINE_CHANNEL_ACCESS_TOKEN` | LINEチャネルアクセストークン |
| `LINE_GROUP_ID` | 配信先グループID |

**Claude Codeが守るルール**:
1. キー・トークンの値を**コード・ドキュメント・コミットに直書きしない**。`process.env.SANSAN_API_KEY`／`os.environ["SANSAN_API_KEY"]` で参照する
2. ログ・標準出力・エラーメッセージにキーを出さない（デバッグ出力にヘッダーを含めない）
3. `.env` を使う場合は `.gitignore` 済みであることを確認してから書く
4. 値そのものが必要な場面（GASプロパティへの再設定等）は高山に依頼し、Claude Codeは扱わない
5. 漏えい・混入に気づいたら即報告。無効化はSansan管理画面（APIキー再発行）／LINE Developers（トークン再発行）で高山が行う

### 5.3 ローテーション履歴

| 日付 | 対応 |
|------|------|
| 2026-07-30 | 初代Sansanキーがチャット経由で共有されたため再発行。以降のキーはGASプロパティのみに保存 |

## 6. 残タスク・発展余地

- 本番5人グループへの切り替え（bot招待→showCapturedGroups→LINE_GROUP_ID差し替え）※完了していれば消す
- メール区分（Email/SentEmail/ReceivedEmail）を配信対象に含めるかの判断（4章の観察事項）
- POST /v6.0/reports を使った書き戻し自動化（議事録整理→Sansan登録）
- 週次CSV吸い出しの置き換え: 本APIで台帳転記の前処理を自動化できる可能性（ナレフル入力の自動生成）
- タグ別出し分け・ネクストアクション期限リマインドなどの配信拡張
