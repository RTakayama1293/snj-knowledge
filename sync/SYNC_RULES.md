# SYNC_RULES — タッチポイント同期ルール v1

**作成日**: 2026-07-20
**正本**: このrepo（GitHub: snj-knowledge）。ここに無い版は正本ではない。

## 1. タッチポイントと役割

| タッチポイント | 役割 | 同期方法 | 方向 |
|---|---|---|---|
| GitHub snj-knowledge | **正本** | — | — |
| ローカルClaude Code（nucbox） | 編集・作業拠点 | git pull / push | 双方向 |
| CCW（Claude Code on the Web） | 編集・作業拠点 | repo直結（PR/commit） | 双方向 |
| claude.aiプロジェクト「食材卸の事業計画」 | RAG用配布コピー | Coworkセッションに「プロジェクト同期して」と依頼 | repo→project 一方向 |
| ナレフルチャット参照ファイル | 配布コピー | 手動アップロード（Notionタスクで管理） | repo→ナレフル 一方向 |

## 2. 更新フロー

### 2.1 正本の編集（ローカルCC / CCW / Cowork）
1. 編集 → コミット → push（CCWはPRマージ）
2. `knowledge/10_rules/` を変えた場合: **即時**、配布コピー差し替えタスクをNotionに起票
3. それ以外: 次回同期でまとめて反映

### 2.2 チャット（webプロジェクト会話）で成果物が生まれた場合
1. 従来どおりプロジェクトに保存してよい（会話の流れを止めない）
2. 週次で「inboxの取り込みして」とCowork/ローカルCCに依頼
   → プロジェクト側の新規ファイルを `_inbox/` に取り込み→カテゴリ振り分け→コミット
3. 振り分け後、プロジェクト側はそのまま（配布コピーとして残る）

### 2.3 webプロジェクトへの同期（repo→project）
- トリガー: 正本にまとまった変更が入ったとき／最低でも月次
- 手順（Coworkセッションが実行）:
  1. repoをclone
  2. `sync/project_manifest.md` とプロジェクトの実態を突合
  3. 差分のみ project_write（同名置換）／manifest外のファイルは project_delete
  4. 完了報告に反映件数を記載

## 3. 禁止事項

- 配布コピー（プロジェクト／ナレフル参照ファイル）の直接編集
- `archive/` 配下の編集・削除
- 正本を経由しないタッチポイント間の直接コピー（差分の温床になる）

## 4. 定期メンテナンス

| 頻度 | 作業 |
|---|---|
| 週次（月曜ルーチンに追加） | _inbox取り込み・振り分け |
| 月次 | repo→project同期、KNOWLEDGE_MAP更新確認 |
| 四半期 | 30_plansの棚卸し（旧版化したものをarchiveへ） |

## 5. 既知の非対象

- Excel実体（SENDO・案件管理PT・EEZO販管）: OneDrive/ローカル運用のまま。仕様書のみ本repoで管理
- Sansan・Notion・Shopify内のデータ: 各ツールが本籍地
- 25-05-27_snj_concept.pdf: バイナリのためプロジェクト側のみに存在。必要ならユーザーが原本をrepoに追加
