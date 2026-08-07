# 仕入先情報 Google Drive ディレクトリ構造

## 出典情報

- **取得日**: 2026-08-05（●仕入配下）／2026-08-07（永井さん仕入れ担当分を追記）
- **ルートフォルダ名**: 照合用見積置き場
- **ルートフォルダURL**: https://drive.google.com/drive/folders/1dFGh6VSyxHhpenaip-e7C08fS3WOu0Yc
- **取得方法**: Google Drive MCPコネクタ（`search_files`、`parentId`指定で再帰列挙）
- **所有者**: Googleドライブ上の高山さんアカウント（`ryota.takayama1293@gmail.com`）

## 概要

高山さんが仕入先の見積・規格書・やり取り記録を集約したGoogle Driveフォルダ「照合用見積置き場」のディレクトリ構造を記録する。見積照合・仕入先参照時に「どこを見ればよいか」を示すためのナレッジ。

**照合用見積置き場の直下構成**: 2026-08-05時点では「●仕入」の1フォルダのみだったが、2026-08-07付で「永井さん仕入れ担当分」（ID: `1kCcsF3A9F3sLVSRidFpDm9QYqjDx1rQT`）が新設され、直下は「●仕入」「永井さん仕入れ担当分」の2フォルダとなった。永井さん仕入れ担当分は、北海道貿易開発の永井取締役が持っていた酒などの仕入先データ（2026-08-07 高山さんより）。詳細は「フォルダ別詳細」の10節を参照。

**重要な注記（範囲の限界）**: このフォルダは想定以上に規模が大きく、特に「●生産者・メーカー別ファイル」（仕入先ごとのフォルダ123件）と「お蔵入りの生産者」（33件）の配下は、1仕入先フォルダあたり数件〜90件超のファイル（見積書・規格書・メール・写真・動画等）を含む。

**フォルダ構造は全階層確定（2026-08-05時点）**。2026-08-05の3ラウンド目のセッションで、第1・第2ラウンドで「未確認」としていた孫・曾孫階層のサブフォルダすべてにファイル件数・主な種別の確認を広げ、**未確認は残っていない**。

- **全階層のフォルダ名・ID・URLを列挙完了**（フォルダ構造は全件確定。ページネーション異常も検証済み・後述）
- **ファイル件数・主な種別まで確認できた範囲**:
  - ★2026新EEZOフォルダ、★2026船上ニセコメロン、★はまなす催事、★仕入先開拓依頼、★鹿肉サンプル、★ヤマト運輸、雪貯蔵フォルダ（直下のファイルおよび全サブフォルダ、孫階層まで）
  - ●生産者・メーカー別ファイル配下の123フォルダ全件（直下ファイルの件数・種別）、および見つかった孫サブフォルダ全件（ナオバンズ2件、梅屋2件、シャルキュトリーアカイシ2件、ニキヒルズ1件、わらく堂1件、三海幸1件、丸市岡田商店1件、うんがぷらす1件、サザエ食品1件、ベターデイズ1件、京樽1件、フジ1件、野菜田1件、北海道美女物語1件、フェリーサービス1件）
  - お蔵入りの生産者配下の33フォルダ全件（直下ファイルの件数・種別）
  - 「90社内GRP　オーセントホテル小樽」フォルダの直下ファイル155件を`pageSize=200`で完走・確定（サブフォルダなし。後述）
  - ★2026新EEZOフォルダ配下EC2606「シャルキュトリーアカイシ」「江戸屋」の孫・曾孫サブフォルダ、EC2607「採用検討中・ボツ」配下10件のEC候補案件フォルダとその内側のサブフォルダまで確認済み
  - ★2025船上ニセコメロン配下「旧」、★はまなす催事「請求書（納品書）」配下「納品書」を確認済み
- **個別ファイル名までは記載していない**: 本文書はフォルダ単位の「件数＋主な種別」に集約している（既存の表形式を踏襲）。個別ファイル名の全件記載は行っていない
- **未確認として残る部分**: **2026-08-05時点で未確認は残っていない**。フォルダ構造・直下ファイルの件数・種別はすべてのフォルダで確認済み

追加調査が必要な場合は同じ手順（`search_files` を対象フォルダIDに対して`parentId = '<ID>'`で実行）で再列挙すること。

## ディレクトリツリー

フォルダ名の横にフォルダ数・ファイル数を付記する。●仕入配下は2026-08-05時点、永井さん仕入れ担当分は2026-08-07時点で確定。孫階層まで含め、未確認は残っていない（詳細は「フォルダ別詳細」参照）。

```
照合用見積置き場/
├ ●仕入/
│  ├ 1. ●生産者・メーカー別ファイル/ （フォルダ123・ファイル0）
│  │   ※ 123フォルダ全件、直下ファイルの件数・種別を確認済み。「フォルダ別詳細」参照
│  │   ※ 一部フォルダ配下に孫階層のサブフォルダあり（個別に注記、件数・種別確認済み）
│  │
│  ├ 2. ★2026新EEZOフォルダ/ （フォルダ19・ファイル11）
│  │   └ 19サブフォルダ（EC26xx案件フォルダ群。件数・種別確認済み。うち2件はさらに孫サブフォルダあり・確認済み）
│  │
│  ├ 3. ★2026船上ニセコメロン/ （フォルダ1・ファイル21）
│  │   └ ★2025船上ニセコメロン/ （フォルダ1・ファイル35、確認済み。配下の「旧」も確認済み・7件）
│  │
│  ├ 4. ★はまなす催事/ （フォルダ4・ファイル6）
│  │   ├ 発注書/ （ファイル15、確認済み）
│  │   ├ 後で削除/ （ファイル7、確認済み）
│  │   ├ 請求書　（ 納品書）/ （ファイル7、確認済み。配下の「納品書」も確認済み・1件）
│  │   └ 配置・服装・ポップ/ （ファイル5、確認済み）
│  │
│  ├ 5. お蔵入りの生産者/ （フォルダ33・ファイル0）
│  │   ※ 33フォルダ全件、直下ファイルの件数・種別を確認済み。「フォルダ別詳細」参照
│  │
│  ├ 6. ★仕入先開拓依頼/ （フォルダ3・ファイル5）
│  │   ├ 回答書/ （ファイル52、確認済み）
│  │   ├ 依頼書/ （ファイル18、確認済み）
│  │   └ old/ （ファイル1、確認済み）
│  │
│  ├ 7. ★鹿肉サンプル/ （フォルダ1・ファイル2）
│  │   └ 2026　06月請求書/ （ファイル7、確認済み）
│  │
│  ├ 8. ★ヤマト運輸/ （フォルダ0・ファイル16）※末端フォルダ・確認完了
│  │
│  └ 9. 雪貯蔵フォルダ　　　　　　　　【美唄市・他】/ （フォルダ0・ファイル5）※末端フォルダ・確認完了
│
└ 永井さん仕入れ担当分/ （フォルダ4・ファイル2、2026-08-07新設。北海道貿易開発の永井取締役の仕入先データ）
   ├ メモ/ （フォルダ0・ファイル1）※末端フォルダ
   ├ 2.カタログ/ （フォルダ1・ファイル5）
   │   └ OLD/ （フォルダ0・ファイル12）※末端フォルダ
   ├ 3.データまとめ/ （フォルダ0・ファイル4）※末端フォルダ
   └ 1.メーカー/ （フォルダ8・ファイル0）
       ├ 醤油/ （フォルダ1・ファイル0）
       │   └ 湯浅醤油/ （フォルダ7・ファイル3、配下7フォルダはいずれも末端）
       ├ 梅酒/ （フォルダ4・ファイル1）※4蔵元いずれも末端
       ├ 日本酒/ （フォルダ14・ファイル1）
       │   └ （うち会津は5蔵元グループ。榮川配下が最深＝銘柄別9フォルダまで展開。詳細は「フォルダ別詳細」10節参照）
       ├ 焼酎/ （フォルダ1・ファイル0）
       │   └ 五島列島酒造/ （フォルダ0・ファイル1）※末端フォルダ
       ├ 会津漆器/ （フォルダ0・ファイル0）※空フォルダ
       ├ お茶/ （フォルダ3・ファイル0）
       ├ ウイスキー/ （フォルダ1・ファイル1）
       │   └ サンフーズ/ （フォルダ0・ファイル2）※末端フォルダ
       └ ボンド商会/ （フォルダ0・ファイル2）※末端フォルダ
```

## フォルダ別詳細

### 1. ●生産者・メーカー別ファイル

- **ID**: `1-GKzk9O3--_nevXy3mbvfBtCotRDZfVZ`
- **URL**: https://drive.google.com/drive/folders/1-GKzk9O3--_nevXy3mbvfBtCotRDZfVZ
- 直下はフォルダのみ**123件確定**（ファイルなし）。仕入先ごとに1フォルダの構成。フォルダ名の頭の数字は商材カテゴリ番号（01鹿肉／02精肉／03水産／04野菜／06チーズ／20飲料／50菓子／60食品／70精油／71化粧品／75キャビア／90社内GRP）と見られる。第1ラウンドでは「約100件」としていたが、`pageSize=200`で再列挙し123件で確定した（後述の注記参照）。

以下、123フォルダ全件を列挙する（フォルダ名・ID・ファイル件数・種別）。件数はメール(.eml)・PDF・Excel・画像・動画等すべての合計。「＋サブフォルダN（…）」は当該フォルダ配下にさらにサブフォルダがあることを示し、件数・主な種別を付記した（2026-08-05時点で全件確認済み）。

| フォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| 01鹿肉　Co-Wild　　　　　　【厚真町】 | `11_Vj_FmcTz74ZOUIwtKAYk0e1-Df0hiC` | 1 | PDF |
| 01鹿肉　MOMIJI　　　　　　【北斗市】 | `19lur1P7d2fhXXz-Ey7nfln_FNMCC4IqF` | 1 | Excel |
| 01鹿肉　Ezo Momiji  エゾモミジ  【恵庭市】 | `1wFZQcsjTEzwA0660xr2P6n4rbt6H6Nrz` | 3 | PDF、メール(eml) |
| 01鹿肉　あぷかの森　　　　　【恵庭市】 | `1d2xJbIAzjGa-8QgBpkXXnKrhfnjcn8ut` | 14 | 動画(MP4)多数、画像、PDF、メール |
| 01鹿肉　エゾの杜　　　  　　【十勝　池田町】 | `1QqTpPS6yTjUK2Ibds75nYD9iKIVdBEcS` | 5 | PDF、メール |
| 01鹿肉　ジビエ工房　　　　　【当別町】 | `1-NAofK4huIlmTT_QuIb_79QxXhtsiKUn` | 2 | Word、PDF |
| 01鹿肉　ソヴァージュド函館　　　【函館】 | `1CaFFmU3uvmrWxMZraYPmaCXGCG3fLFYv` | 11 | PDF、Excel、Word、画像、メール |
| 01鹿肉　ユック　　　　　　　　【根室】 | `1ONy0rt0Up_Mz809TS0Fh_I_3FW7YwXrZ` | 2 | メール、PDF |
| 01鹿肉　上田精肉店　　　　　【新得町】 | `16ZysO9a4uMSlJ4jqCIBmY03JHcZEOdKO` | 3 | メール、PDF |
| 01鹿肉　阿寒グリーンファーム　　　【釧路市】 | `1o44tc38LHoWoJTZTgat-YjnEvPNsPWFw` | 1 | PDF |
| 01鹿肉　水戸青果　　　　　　【札幌】 | `1q1MB4QAojllH-ak4h28_BnBcWSLk36fd` | 3 | PDF、PowerPoint |
| 01鹿肉　北鹿舎　　　　　　【白老・苫小牧】 | `1HdeZE7EqHB33-4ZCz3U_9ImnNC7uIHUE` | 3 | PDF、メール、Excel |
| 01鹿肉　狩人の蔵　　　　【帯広市】 | `19Vc1nobMpImd2OKdILix3SNkE4YC-Rgl` | 13 | メール、画像多数、Word |
| 01鹿肉　株式会社　North innovation | `1Zi6pKpMHDspzGcYDATTfHVUrSEk8TpNw` | 2 | PDF |
| 01鹿肉　北海道エゾ鹿ファクトリー　【白糠町】 | `17AvSDFKxjq6JrKHIGtQySVBro7JAbq_k` | 1 | PDF |
| 01鹿肉　熟成エゾ鹿肉　シクヌ　　【訓子府町】 | `1NeEfjatD8cNoxGfPH8JOpf4I0d1sFr9z` | 1 | PDF |
| 01鹿肉　知床エゾジカファーム　　　【斜里町・知床】 | `1HeRmG6uMdjZfPcUM5bf559q1eIgKg4zw` | 15 | PDF、メール、画像多数 |
| 02精肉　GOODGOOD（1億9400万）【大阪府】 | `1vpjVoD1W704qd3yqAPaBE-nEdaWhsKPJ` | 8＋サブフォルダ1（OLD：1件、PDF） | PDF、Word |
| 01鹿肉　食美樂　　　　　　　　【新冠町】 | `1SGsx-AFFs2gn_SFX3siPPbv76WfuPsCy` | 2 | Word、PDF |
| 02精肉　エスフーズ | `1TEH9fll5BhCxdresONm_GQwuCGVDdZN4` | 2 | Excel |
| 02精肉　美瑛ファーム　美瑛放牧酪農場　【美瑛町】 | `1G-_p81wnU6jCeNEzG6WF04zz8zfP8sfA` | 3 | メール、PDF |
| 02精肉　サカモト食品　　　　　【幕別町】　matsu | `1WDsvBlu0tOkseTbMcaRvyAiuqOglEQan` | 4＋サブフォルダ1（サカモト食品さんからもらった画像EC掲載OK：10件、Thumbs.db・画像(png)多数） | PDF、メール、Word |
| 02精肉　ファームズ千代田　　　　【美瑛町】　kuro | `1cPYisi3vHqBKuneYVHwJDj9uG6Qu6sBW` | 41 | 画像多数、PDF、メール |
| 02精肉　北一ミート　　　　　　【札幌市】 | `18Tr91cmsVGOn3mXvg9FmxKPg-__q7vwA` | 2 | メール、PDF |
| 03水産　ヤマニ野口水産　　　　【留萌】 | `1tKL6Sv-VIt6f_dCO_LjiVjT7wGWy4DrO` | 9 | PDF、画像 |
| 03水産　マルホン小西漁業　　　【寿都町】 | `17722SXVBput3knrw3oe6sG15YTIe11UO` | 3 | メール、PDF |
| 03水産　NSニッセイ　　　　　【小樽市】　matsu | `1pQMICmmvQnLLvvaYHuKTz6n-9fl2uJht` | 20 | Excel、画像多数、PDF |
| 03水産　カネシン水産　生ウニ　　【札幌市】 | `1rEpfscDGnExdXzA96KKPvr6u2FFR2f5-` | 3 | 画像、Excel |
| 03水産　ナチュラルシー（天然サクラマスフィレ）【横浜市】 | `1HbOzes9Qh5Jagw8O4LY_kDBG8HPtQFYr` | 2 | メール、PDF |
| 03水産　まるひら商店　　　　　【札幌市】 | `1fIiuPTb-mVC5B4f8bl6TEb6zBQPNsSBe` | 4 | PDF、メール |
| 03水産　エビコー　　　　　　【札幌市】　EEZO✖ | `1gvvxoYg1VSmJzvMPh6GCwvJZ7B9Iq33a` | 6 | PDF、メール |
| 03水産　マルトシ吉野商店　　　【寿都町】　matsu | `15RY1FxKqOTp6vLbo7aaIPzTWDOV3p1zP` | 3 | メール、PDF |
| 03水産　佐藤水産　　　　【札幌市・石狩】　kuro | `1EWzwmZR5XSrjo-qTJb94bxGLfbY56rUr` | 4 | PDF、メール |
| 03水産　小樽水産加工業協同組合　【小樽市】　matsu | `1StlWFP8BgqTXgZeer3KYFmfOozA3kWxf` | 48＋サブフォルダ5（【商品写真】かね丁鍛冶13件、かね丁鍛冶見積202507最新4件、ホリ商店（ほっけ）1件、参考資料1件、井原水産hp21件） | PDF、Excel、画像多数 |
| 03水産　丸恭水産 | `1Z2M3rXSogjiMuB3dNs2pjbga54vBRpH2` | 2 | Excel、メール |
| 04野菜　ニセコビュープラザ 直売会協同組合　【ニセコ町】　matsu | `1tAD8sOy8cq4W1DDzJ_vRrFArZJgJKRmy` | 7＋サブフォルダ5（メロン18件、干し芋17件、＿削除だが一旦保存2件、野菜セット24件、恋するじゃが（熟＆新じゃがセット）6件） | Excel、PDF |
| 03水産　知床工房吉野　　　【斜里町・知床】 | `1z_b4L2P32IIyE2ebEm4xQpHnJZpStgbz` | 13 | 画像、メール、Excel、PDF |
| 04野菜　原田産業　原田さん　※見積なし　【倶知安町】 | `1kCrSKA2U3L9WUTGR0gjk-4FUKJVhV8yW` | 20 | 動画、画像、PowerPoint、Word、PDF |
| 03水産　福島町役場　陸上養殖あわび　【福島町】 | `1RRWtQ9ALNeZzRw3mPntqq-9UcL_Vn7Sv` | 5＋サブフォルダ1（福島町から画像データ（20260106）：5件、Thumbs.db・画像） | メール、Word、Excel、画像 |
| 03水産　東しゃこたん漁協　　　　【古平町】 | `1RvdPFAASGiks8ZQ4Is344b_3V4rT5GrB` | 5 | PDF、メール、Excel |
| 03水産　山下水産　　　　　【寿都町】　kuro | `1FjunPozso4h4qacQzLkDJVhyprnUR0wD` | 7 | PDF、メール、Word |
| 04野菜　シニック（紫蘇）　　　【蘭越町】 | `1TV5RgNFPpCyCn9XOoTwMyADmsNEboqyk` | 5＋サブフォルダ1（20260706蘭越視察写真門永：16件、画像多数・Thumbs.db） | 動画、Word、メール、Excel |
| 03水産　王子サーモン | `1Y6CcoNvEgyrTrXuzRZi2Ar0lV2jTZufa` | 3 | PDF |
| 04野菜　ベジタブルワークス　　　　　　【真狩村】 | `1HtZVodh2dRY3L2vWSLJIlAe8-zm_9gFt` | 65 | PDF多数、画像多数、Excel |
| 03水産　藤田水産　　　　　　　　　【小平町】 | `1H1VWEUdhC3L1EGU5EsTim0NnuhLZAF85` | 1 | Excel |
| 03水産　落石漁港協同組合　　　　　　【根室市】 | `1zAHeFxJ2l9AxXCE0zolZr7lSMOcycjyk` | 3 | PDF |
| 03水産　龍王水産　札幌　　　　　　　【札幌】 | `1V0RhHgzAtCbFxywWOYv8sxvdSuRfFVul` | 4 | PDF、Word、画像 |
| 04野菜　リストファーム　※見積なし　　【倶知安】 | `1Eo8wMjo2IwZalHFWXSDoi2UgE0BIRcEq` | 4 | PDF |
| 04野菜　水戸青果　　　　　　　【札幌市】 | `18yuCnOY8PewkfzpQa11bX3dLJ5NqYIwm` | 8 | PDF、PowerPoint |
| 04野菜　中野ファーム　トマト（ジュース）　【余市町】 | `1MTP421x4IDKlY4jUkNG3QS7ztC_3pf7j` | 11 | メール、画像、PDF |
| 十勝グランナッツ（落花生）【芽室町・士幌町】 | `1bViyXlUxkMdI7T4grHFgaIIlFzcxvZx0` | 3 | PDF、メール |
| チーズダム CHEESEDOM（eezo未公開）【せたな町】 | `1Pwy4oGGXlA31kZlb-0qBfEsAbUGrolFw` | 2 | メール、PDF |
| 長福ファーム　※見積なし【倶知安町】 | `1V8cDrXP-DwOrV9D2DyETdbwvdfCP_4m5` | 4 | メール、画像、Thumbs.db |
| カミカワキッチン（1000万）eezo未公開【上川町】 | `1LOdn5JX_WiXLREPbTEsvfO1J17OILbTX` | 3 | PDF、メール |
| しあわせチーズ工房（eezo未公開）【足寄町】 | `1WXCwpnDaT99AduPjvPyOxOnVvRw662-T` | 9 | PDF、メール、Thumbs.db |
| トワ・ヴェール（フジタCo）【黒松内町・札幌】 | `1iiLnLcKkbBfvb671BRnMyrDZ8_XIbRNj` | 2＋サブフォルダ1（2023過去分：2件、Thumbs.db・PDF） | メール、PDF |
| ニセコチーズ工房（eezo未公開）【ニセコ町】 | `1anuX75Ymf0OukdcQnqyIUTovHrNj7wBh` | 16 | PDF多数、メール、Excel、画像、Thumbs.db |
| 十勝野フォロマージュ　見積もらえてない【中札内村】 | `11gD3CJ0hLY4rU4gmXQPqhTU7E9_IAX8j` | 1 | メール |
| CHISE GARDEN チセガーデン【ニセコ】 | `12_FclYoJOiZP-e7P2PcqE-Sca_ba5tZS` | 1 | PDF |
| アップルランド山の駅おとえ　シードル【深川市】 | `1MXUjzy8BudS52QNdX5n0Yq65wlpBVrAb` | 4 | 画像(png)、Excel、Word、PDF |
| キリンビバレッジ【札幌】 | `17roKmYHAOY_piNBR5NJD7EVtYJYN25Hz` | 1 | PDF |
| トカプコーヒー【中札内村】kuro | `1yXAJw0mcj6rF9KsPxfbkwAIrgnP32RLQ` | 9 | メール、画像、PDF、odt、テキスト |
| ハリカ桑名園【富良野市】kuro | `1eJKtzdYF7nSNR5K-s3afhnSDnA5dZxV7` | 9 | PDF、Thumbs.db、メール、画像、Excel、Word |
| ニキヒルズ NIKI HILLS【仁木町】kuro | `1wPdcVjIBWlRhnWtxCm_wbnOI1lQYebZQ` | 12＋サブフォルダ1（20250905ニキヒルズ提供ワイン画像：4件、Thumbs.db・ワイン画像jpg3） | PDF多数、Thumbs.db、Word(doc)、メール、Excel |
| 網走ビール（網走市） | `1wedE1qcuO-sRqYh7K7QyQQlopjIrE9OH` | 5 | PDF多数、Excel |
| ナオバンズ Nao-buns【倶知安町】matsu | `17BrWOd6FY1JSFp2ya6Hmd9-wBjz-C9oh` | 73＋サブフォルダ2（クッキー缶凹み：7件、Thumbs.db・画像jpg/JPEG6／旧タリフ：4件、送料見積PDF4） | 画像多数(jpg/png/avif/webp)、PDF、Excel多数、PowerPoint、zip、メール、Thumbs.db |
| 奥尻ワイナリー【奥尻町】 | `1E5J02NIj-O4Zdc8qci5XmgVabpVoVJD0` | 2 | メール、Excel |
| 北王よいち【余市町】kuro | `1kwQegrAe2lzZyfctFIk6dYXJg13wexBS` | 12 | PDF多数、メール、Thumbs.db、画像、Word |
| わらく堂【札幌市】matsu | `10F8k3FCitQ4-W6LLw3Id3CwsHqdGu3jP` | 15＋サブフォルダ1（わらく堂からいただいた写真データ（オーケストラデュオ）：6件、Thumbs.db・画像jpg/JPG5） | メール、Word、PDF、Thumbs.db、画像 |
| 積丹スピリット【積丹町】 | `1SYehNxgriHf2l93dUpoh6keE1e61gdg3` | 8 | メール、PDF多数、Word、画像 |
| ほんま　月寒あんぱん本舗（3600万）【恵庭市】matsu | `1Vm_pTH39GyOZj3n5H2ZycxQ-veetH8eH` | 11 | Excel(xls)多数、zip、メール、PDF |
| 三海幸【函館市】matsu | `1V_tW3g40y-7vdBt9Ezj6i5Vy_LFv_Hnd` | 21＋サブフォルダ1（2025年2月1日ご納品分よりｇ変更：2件、PDF2〔規格変更商品一覧・お知らせ〕） | PDF多数、メール、画像、zip |
| 丸市岡田商店【札幌市】matsu | `1mtPdmNHeFpSV-mNvWot5fJF23Db8FuWp` | 26＋サブフォルダ1（新規見積り　eezo登録未：3件、PDF1・Excel1・チラシPDF1） | メール、Thumbs.db、Excel、画像(jpg/webp)多数、PDF |
| 北海道名販【室蘭市】matsu | `1LTys4JNQJY8os2JqDHtnuRwD-egUjBHX` | 4 | メール、テキスト、Word、PDF |
| 北海道デイリーライス（小樽市）高級おはぎ | `1ETnFxPvDjuufmoDzpJH2vp_U6sT-nqv5` | 10 | Thumbs.db、Word、画像、PDF多数、メール |
| 厚真観光協会・SNF苫小牧【厚真町】 | `1c_dsatstskEC7Rg6wwHMKzkk9AmlvEZp` | 18 | Thumbs.db、Excel、画像多数、PDF |
| にんにく種蔵【札幌市】matsu | `1rxMomeVOrN1hUYTDveYD-9uvy_ipSAQa` | 34 | PDF多数、Thumbs.db、メール、画像多数、テキスト、Word |
| 山栄食品工業　※前精算【函館市】 | `16is2_yGr4mP2TAwuJWpylAnTnfXySjUD` | 5 | Excel、メール、PDF |
| 昭和製菓　※前精算【函館市】前精算の為EEZO NG | `1of5KQas-JbBrIXt06zvVbS8g2Q6ovO2I` | 6 | Thumbs.db、Excel多数、PDF |
| 谷田製菓(きびだんご)【夕張市】matsu | `1gajXS1Hm6IMwiGEXoPsd6Xde7A8n7fjx` | 7 | Thumbs.db、Excel多数、PowerPoint |
| Atta（フリーズドライアスパラ他）【札幌市】 | `1uXt8ofKr5hnYF5LpUMdfXKQZcBQGxoQi` | 3 | メール、PDF |
| うんがぷらす㈱【小樽市】kuro | `1zWVd_3WcUE8LVX3NDrCou3XklodlHH2l` | 13＋サブフォルダ1（北前吟撰＿パンフレット＿価格表：2件、パンフレットPDF・価格表PDF） | zip、メール、PDF多数 |
| 梅屋 UMEYA【旭川市】kuro | `1pj-DHtOqabmouRgYkruh4CfLc4OCs86W` | 35＋サブフォルダ2（20260305最新画像：6件、Thumbs.db・画像jpeg/JPG5／梅屋さんから画像データ：5件、Thumbs.db・画像jpg4） | PDF多数、Excel(xls)多数、画像多数、メール |
| からくさ Han's Marine（札幌市）※海鮮キムチ | `1JqGEif9CPz4nCO2-VtrsY14s4al-788W` | 6 | メール、PDF |
| サンマルコ食品　冷凍コロッケ【関西支店が窓口】 | `1GkzSjl3A7RF2nIsQDKda49PaJyQkv7FI` | 7 | Thumbs.db、Excel、画像、PDF、メール |
| アベファーム ABE FARM【赤井川村】kuro | `1yy_vwVDaqgbNP3eezeLIbf4LzOEHJRdT` | 7 | メール、PDF、Word |
| サザエ食品【札幌市】matsu | `1GSj7fF05gzuqSIt-GzRJcbXN7zOm-ClB` | 25＋サブフォルダ1（サザエ食品提供画像：17件、Thumbs.db・画像jpg多数） | PowerPoint、PDF多数、Thumbs.db、画像多数、メール、Word |
| エーデルワイスファーム（ベーコン節）【北広島市】 | `1rEkgFxyK8m-f3pv3d2MzRI2t2DOUccQW` | 3 | メール、PDF |
| シャルキュトリーアカイシ【ニセコ町】kuro | `1vAwOyXwcNU8dKpnHcrEOPrEyd1R7jfNa` | 4＋サブフォルダ2（画像：4件、Thumbs.db・生ハム等商品画像jpg3／過去見積：1件、PDF） | PDF、Thumbs.db、メール |
| ジョー・エンタープライズ【札幌市】matsu | `1H5Bv4eUc3BbedeHPFgPyvJfZ4jVSBY3L` | 13 | Thumbs.db、画像、メール、PDF多数 |
| ノベルズ食品【上士幌町】kuro | `1UsTZ6hcJVoH4a4CtJXz72L0mMdw-Md27` | 19 | PDF多数、メール、Word |
| ベターデイズ（札幌市）※豚まん | `15vw62hThUXdHv283JDpk8CqPKEydVFhb` | 22＋サブフォルダ1（20251028ベターデイズからいただいた画像：15件、PDF4・Thumbs.db・商品画像jpg10） | PDF多数、Thumbs.db、画像多数、メール |
| ノースファームストック（ジャムなど）【岩見沢】 | `1MVtC5KLhiF9_DPbx3eQnO3XKpDBxWQTf` | 6 | Thumbs.db、Excel、Word |
| ノースボート　利尻昆布ラーメン【札幌市】matsu | `1tEodPf192qLLYLXMjOwCeQ9bnspKaVT3` | 24 | PDF多数、Thumbs.db、画像多数、メール |
| 京樽 | `1uan2lGjicAp4Zq8eXzrJLDIZkxXjLuSO` | 1＋サブフォルダ1（【新日本海商事株式会社様】価格改定見積一式：2件、価格改定見積PDF2） | PDF |
| ハンズマリン　海鮮キムチ【札幌】 | `1DXjY5yEdx4iDblOLYnoNLyi0OoxhxE3v` | 6 | Thumbs.db、画像、Excel |
| リージョナルデザイン Regional Design INC【長沼町】eezo返信なし | `1NRvsPnDLMRoZkkJBF3ysppL-1BuF5O8M` | 26 | メール、Thumbs.db、PDF、画像多数、Excel |
| フジ FUJI【札幌市】matsu | `1fs3KfnfaVA6aqXmAalxbCXXVeiYfbc05` | 32＋サブフォルダ1（2025.7　トウモロコシ予約販売案内：3件、Excel1・PDF2〔チラシ表裏〕） | PDF多数、Excel多数、Word、画像、Thumbs.db、xlsb |
| 丸一大西食品【札幌市】kuro | `1V6rxGUn0xoeM3h_uABamR21CT6sVIHan` | 26 | PDF多数、Excel(xls/xlsm)多数、メール、画像多数、テキスト、PowerPoint |
| 佃善（札幌）豚じゃが・餃子 | `13YFcDJn11ynxyDpSKT4d-l0rmB2rWwfb` | 5 | メール、PDF多数 |
| 五洋物産（札幌）　じゃがもっち | `1djcSGy7hFgEChCQcdJg-AdyrEXIvONjR` | 6 | Excel多数、メール、PDF多数 |
| 北海道バイオインダストリー【札幌】matsu | `11qrTuv7uTuVeICYbRKSfAt0RDB2SxjS9` | 9 | Thumbs.db、PDF多数、メール、画像 |
| 北武フーズ | `1GZ5203I10i9p2tOJ7S9B4h8EVDnnQUpE` | 1 | Excel |
| 北海道国際流通機構【札幌市】 | `1yTe1i5AAXjpJd-6XT-AycGzXcjUo_cKH` | 6 | メール、Thumbs.db、画像、Excel、PDF |
| 十勝しんむら牧場 | `1fYVQ3iaAFXU7VXGc0VT2LmdFP6ZzDIyB` | 7 | Thumbs.db、画像多数、Excel |
| 福島町町づくり工房【福島町】 | `1i6OZKlxal82GrUqY5G7nroSL8FhoGcWh` | 4 | Word、Excel |
| 医食同源（がごめ昆布の食品・化粧品）【函館】 | `1SQPYeKBBwreY2455Gac01qXiGzKXw2wy` | 2 | メール、Excel |
| 南華園【札幌市】matsu | `1h8LqoWkhOqypz3w5C_j4VD9cPPX5v43j` | 6 | メール多数、Excel、PDF |
| 道の駅 　みそぎの郷きこない【木古内町】 | `1YpkTA_KBKtD22HxKATW1L224AB7xW002` | 10 | テキスト、画像多数、Excel、Word |
| 小林食品【興部町・おこっぺ】matsu | `1LKHMJfK9Rla0rlmLWclGsgc_gxYfHupR` | 11 | Thumbs.db、画像多数、メール、PDF、Word |
| 秀明ナチュラルファーム【久遠郡】 | `12-tAB0VOluDSxUcFQqO3yeX8q4QPZVUi` | 3 | メール、PDF |
| 野菜田【富良野市】kuro | `1xsZtP14ZVoVnO1s2nxzYf502sAwnG8vV` | 11＋サブフォルダ1（野菜田さんからもらった写真データ：13件、Thumbs.db・商品画像jpg多数） | Thumbs.db、画像多数、メール、PDF、Word |
| 谷口農場【旭川市】 | `1Zd4DRbcrJUWu8JE8Z7maFU-tz06uZoIk` | 2 | メール、PDF |
| 旭川食品 | `1KJfM0hJ9TdxNKNtA70TZ0WvJIYvxu_DQ` | 1 | PDF |
| 郊楽苑【釧路】 | `16P13O_NLv__C4GPT5SmsjsSXfn0VuB-8` | 2 | PDF、Excel |
| 雪屋媚山商店（雪貯蔵）【美唄市】 | `1668PqH2OM8xvIHLU0Zb-Gv1QXZdsWJb7` | 3 | メール、PDF |
| 北見ハッカ通商　（1000万）【北見市・札幌】 | `16eFZdMMpEjJEzH02yJzkjbn6bWqQiteU` | 8 | PDF多数、メール、Word |
| フプの森（エッセンシャルオイル）【下川町】eezo NG | `1B-ziG7hGFVMaRCHP9tXaCbXc7XPpJJ0z` | 4 | メール、Excel、PDF |
| 北海道美女物語【函館・大阪】matsu | `1ZtT_tXbCPryDiqJk2K_S7i1ANzuTgeRC` | 16＋サブフォルダ1（ソワレさんからもらった写真画像 EC掲載ok：25件、Thumbs.db・商品画像png/jpg多数） | PDF多数、Thumbs.db、画像、Excel、メール、Word |
| 75キャビア　鹿追町役場（鹿追町） | `1dsUalDzTQSuLlt-5cmsViJOOOI16Nvk_` | 1 | メール |
| 90社内GRP　ノーザンデリカ　※見積等なし【小樽市】 | `1m9bl61X8D9ntecOpWg5TAEm0K8iOah31` | 1 | PDF |
| 90社内GRP　オーセントホテル小樽【小樽市】 | `1qBUrpLMjLXt5ZmmA7_xLw1tG7tQ8uNfA` | **155件で確定**（`pageSize=200`で1回のレスポンスで全件取得。`nextPageToken`なし。サブフォルダなし） | 画像133（jpg等）、PDF15、Word(docx)2、Excel(xlsx)1、PowerPoint(pptx)1、zip1、Thumbs.db1、ai1 |
| 90社内GRP　フェリーサービス　※見積等なし【小樽市】 | `1z3it1Ipumg-aUpR2qfgUxeSq6bjBx5Jr` | 15＋サブフォルダ1（小樽パッケージ　商品写真：66件、Thumbs.db・商品画像jpg/webp/png多数） | Thumbs.db、画像、Excel多数、PDF |

### 2. ★2026新EEZOフォルダ

- **ID**: `1Z_SEgizUQrEBehJ5vFnYOaqneJXZq-nu`
- **URL**: https://drive.google.com/drive/folders/1Z_SEgizUQrEBehJ5vFnYOaqneJXZq-nu

直下のファイル（11件、内容確認済み）:

| ファイル名 | 種別 |
|---|---|
| 26-06-11商品撮影詳細.xlsx | Excel |
| 26-04-15_撮影進行台本_EEZOギフト（ラフ）.xlsx - ショートカット.lnk | ショートカット(.lnk) |
| EEZOについて.docx | Word |
| 26-05-20_EEZO（エエゾ）について_仕入先依頼用.txt | テキスト |
| ギフトようにせずに各商品をひとつずつということですね.docx | Word |
| 現在レザンガレット.docx | Word |
| 26-04-15_撮影進行台本_EEZOギフト（ラフ）.xlsx | Excel |
| 26-04-06_EEZOセット商品仕入先候補.xlsx | Excel |
| 納品書　まな板 Amazon .pdf | PDF |
| 納品書　ナオバンズ撮影用商品　.pdf | PDF |
| オーセントスイーツ　見積pdf.pdf | PDF |

直下のサブフォルダ（19件。EC受注案件ごとに1フォルダの構成）。件数・種別を確認済み。「＋サブフォルダN」はさらに孫階層があることを示す:

| フォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| EC2604 ニセコビュープラザ（4セット商品） | `1mF02sjl9BnJu66hgWPwHopaTdAkX1hF_` | 6 | Thumbs.db、画像、PDF、Excel |
| EC2606 オーセントホテル | `1PTBIOgaVz8jW8E-0VeG_3BW9VFfDs_E6` | 2 | Excel |
| EC2604 梅屋 | `1u7vMDUnQ7ikssxa-c2eA0D12mbquuOIT` | 5 | Excel、PDF |
| EC2604 ナオバンズ（2セット） | `1rWExBGMtLS9v9E7Pv-1AUJDuDHKcM0MQ` | 1 | Excel |
| EC2604 トワヴェール・フジタCo（11セット商品） | `1I4rQgPrguKvW2qhECTp60x70ijyx9V50` | 3 | Word、PDF、Excel |
| EC2604 ニキヒルズワイナリー（3セット商品） | `1M89TYb22iSrgE3tnagddVhyDUOzbPy3w` | 2 | Word、PDF |
| EC2604 小樽水産加工業組合（6セット） | `1LxRkGxGSGufvV9XM7taQ1iWNORfZkW5Q` | 5 | Excel、PDF多数 |
| EC2606 ㈱六美 | `1gD-PKmuNkD15etdYh4G3FDzUOXxebiBe` | 11 | 画像、Excel、Word、Thumbs.db、メール |
| EC2606 トワヴェール・フジタ（清涼・アイスクリーム） | `1Z-Z6p6t-Pi47l-0prmknUPMH3bzeLksU` | 4 | PDF、メール、Word |
| EC2606 シャルキュトリーアカイシ（清涼・肉ハム） | `1IGO7HYK5iuxuvqa0rN3rfrkFZXeuKjnk` | 2＋サブフォルダ1（シャルキュトリー簡易撮影分：16件、Thumbs.db・商品画像JPEG多数） | メール、PDF |
| EC2606 上川大雪（清涼・日本酒） | `1nfABjvmIE96__JQIcPwyTrVfdXMc_q4W` | 9 | Thumbs.db、画像、メール、Word、PDF |
| EC2606 みにとまとん（オモシロ焼き菓子） | `1BwQXrujm7s_cesRhhbbsHpyA3kDSwB6l` | 3 | メール、Excel、Word |
| EC2606 ニキヒルズワイナリー（ノンアルコール NEIRO） | `12Rrdr2Z_AyZ2f6qX0x5SvwwlJfqlAwrX` | 6 | PDF多数、メール |
| EC2606 北王よいち（ぶどう・林檎・トマトジュース） | `1zJ1Dt-pig2HZXu1ICRPZZZeLPImQJOmp` | 3 | メール、PDF |
| EC2606 小樽水産加工業協同組合 | `1vYANBGESBOuFEyTKBxyrgN-P8Me9jDsF` | 1 | Excel |
| EC2606 江戸屋（清涼・アイス・ジェラート） | `1Xy79pL9LkSyW769Bb6QQkCqo3HQJBvXd` | 7＋サブフォルダ2（110501 doyell 夜を愉しむアイス3種10個：直下4件〔Thumbs.db・商品画像jpg3〕＋孫サブフォルダ2〔mini4件・rename3件、いずれも画像〕／江戸屋からもらった画像：直下0件＋孫サブフォルダ1「440310 doyellシュシュフラン４種６個」8件〔Thumbs.db・商品画像jpg7〕＋さらに曾孫サブフォルダ2〔mini3件・rename5件、いずれも画像〕） | メール、Excel、PDF、Word |
| EC2607 採用検討中・ボツ | `12LS3L-9Ons_mSZa7NankGKQwBYAOeiKe` | 1＋サブフォルダ10（EC候補案件フォルダ群。件数・種別を確認済み。詳細は本節末尾の補足表を参照） | Word |
| EC2606撮影用　請求書＆納品書 | `1suGnn0I5Za6GbrJ0hv5wm1UFfzX5pdLb` | 2 | PDF |
| EC260X ベターデイズ（まん10個選択可） | `1HPpTRXvRaL7-Bc09ZQxUWk45uxfmWtH6` | 4 | Word、PDF |

**補足: EC2607「採用検討中・ボツ」配下10サブフォルダの詳細**（親ID `12LS3L-9Ons_mSZa7NankGKQwBYAOeiKe`。直下ファイル1件「採用検討中商品について.docx」＋以下10フォルダ）

| フォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| EC　シミック（紫蘇）　※画像・送料依頼中 | `1rWm02Wgo4p9J3gHd6YDaU34MzWNdzYOQ` | 4＋サブフォルダ1（資料：4件、商品ラインナップPDF・パンフPDF・お取引先台帳PDF・包装箱画像jpeg） | xlsx、eml、lnk、pdf |
| EC　しもかわ森のブルワリー　※set依頼中 | `1QaDzkm62KNDd0C_p5zfJWNd5TPdtwln-` | 3 | ブローシャーPDF、eml、商品詳細PDF |
| EC　Otaru arch オタルアーチ　※見積依頼中 | `1de8uIpH9nkJVFs4jARL-3k0Bm4rtStWe` | 9 | 報告書docx、eml、商品画像jpeg5、Ginブローシャー/プレスリリースPDF2 |
| EC　ル・カレン　※WEB出荷が必要 | `14vgA1hVHvQyBFlTBrbjpewZ8zoZd63ho` | 2 | 商品案内PDF、eml |
| EC　ユートピア知床㈱　※set依頼中 | `1uryJmmNJ_f0yeOAYTcS0y8ltwp1apKDv` | 3 | 商品ガイドPDF、見積書PDF、サンプル送付状PDF |
| ★EC　きまぐれ牧場　※準備OK | `1U0xCb-KvocdQuxhdzG-Ouw3fQSjKq6aP` | 4＋サブフォルダ2（資料（初期見積等）：4件、見積・提案・宣材PDF／画像　気まぐれ牧場様より：11件、Thumbs.db・商品画像jpg10） | eml、xlsx、pdf |
| ★EC　エゾの杜　※準備OK | `1FXcd0S3YCUYIuGrc27ubiUxYbsB_Ysyx` | 2＋サブフォルダ2（画像①エゾの杜提供掲載OK　新日本海商事㈱イメージ：12件、Thumbs.db・商品画像JPG/jpg11／画像②同パッケージ：20件、Thumbs.db・商品画像jpg/JPG19） | eml、xlsx |
| ★EC　ニセコビュープラザ　※準備OK | `1-rzjv5WLXeHQ0lZS8PzW1YABJlLSiD9L` | 3＋サブフォルダ1（画像　びゅーぷら提供分、船上撮影分：14件、Thumbs.db・商品画像JPEG/jpg/png多数） | eml、lnk |
| ★EC　円甘味(まるあまみ)　※準備OK | `1xUOtI8Fe_HW717Pe_phKTky5AEJfWLkV` | 3＋サブフォルダ2（画像　円甘味提供：5件、Thumbs.db・商品画像jpg/png／資料：3件、商品PDF2・見積xlsx1） | xlsx、eml、Thumbs.db |
| 不採用 | `1j7jjqUVs45pUWZmugMeOF4QeLqWjV6Qe` | 0＋サブフォルダ1（EC　ココ　㈱COCO　※未着手(EEZO合わない)：2件、eml・見積PDF） | （直下ファイルなし） |

### 3. ★2026船上ニセコメロン

- **ID**: `1xxF91R1AH1zTpfA-UGxbGykvcAxNO-2V`
- **URL**: https://drive.google.com/drive/folders/1xxF91R1AH1zTpfA-UGxbGykvcAxNO-2V

サブフォルダ: ★2025船上ニセコメロン (`1DEJYkas3-aqfugCwptJiFVCNHEuqW6gj`) — ファイル35件、確認済み（Thumbs.db、Word、PDF、PowerPoint、画像多数、動画(MP4)、Excel、png）。配下にさらにサブフォルダ「旧」(`16DyMLL4JDE0bdFZlwACmeqh8UKiA2SKv`) があり、直下ファイル7件（すべてWord docx。船内イベント「海の上のニセコ野菜直売所」「海の上のニセコメロン試食会」関連の企画書）を確認済み

直下のファイル（21件、内容確認済み）:

| ファイル名 | 種別 |
|---|---|
| 7月分　請求書詳細（メロン試食会）　.xlsx | Excel |
| VEニセコメロン販売状況.xlsx | Excel |
| IMG_3219.HEIC〜IMG_3212.HEIC（7点） | 画像 |
| Thumbs.db | その他（Thumbs.db） |
| 北海道の旬を楽しむ船内イベント.pptx | PowerPoint |
| 旅客部制作　船の産直ポップ.pptx | PowerPoint |
| 20260721_船の産直_ニセコメロン.pptx | PowerPoint |
| 船の産直企画 ニセコメロン販売 実施のお願い（安井課長　門永課長宛）.docx | Word |
| 船の産直企画 ニセコメロン販売 実施のお願い.docx | Word |
| 船内ポップ.pptx | PowerPoint |
| ショップ　レジ販売価格　.docx | Word |
| 船内アナウンス.docx | Word |
| 2026海の上のニセコメロン試食会 ver.2 .docx | Word |
| 2026海の上のニセコメロン試食会 ver.1 .docx | Word |
| 仕入収支表　.xlsx - ショートカット.lnk | ショートカット(.lnk) |

### 4. ★はまなす催事

- **ID**: `1RLo0BDpR-mKL1v-xurzfEP9-aHg4hmqN`
- **URL**: https://drive.google.com/drive/folders/1RLo0BDpR-mKL1v-xurzfEP9-aHg4hmqN

サブフォルダ（4件、確認済み）:

| フォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| 発注書 | `1zstAF-g9KlzGmuIRUIdDX_btB7ZtKzmT` | 15 | PDF多数、Excel |
| 後で削除 | `1ugBDNNPuvOjE7FtZR82oMmy4YoIP8r41` | 7 | Excel多数 |
| 請求書　（ 納品書） | `1U2wRvd5SEqpmCi9k_Y8FMVMaqGgkAfJk` | 7＋サブフォルダ1（納品書：1件、PDF「納品書 0627はまなす催事　小樽水産加工業組合.pdf」） | PDF多数 |
| 配置・服装・ポップ | `18vjUG9RCWzNE1iKdeFPR4Egd7WIjmb-b` | 5 | PowerPoint、Excel、Word、PDF |

直下のファイル（6件、内容確認済み）:

| ファイル名 | 種別 |
|---|---|
| 販売詳細表　（はまなす一般公開0601）7月〆請求　.xlsx | Excel |
| 販売詳細表　（はまなす一般公開0601）.xlsx | Excel |
| 0713 Pケーキ・干し芋 販売レポ（廣岡さん）.pdf | PDF |
| マリネックス.xlsx | Excel |
| Thumbs.db | その他（Thumbs.db） |
| 一般公開イベント案内（04.30作成）※神原さん.pdf | PDF |

### 5. お蔵入りの生産者

- **ID**: `1wt-KARilZS4kxPVdAUJAOAwImZfU4K5C`
- **URL**: https://drive.google.com/drive/folders/1wt-KARilZS4kxPVdAUJAOAwImZfU4K5C

直下はフォルダのみ**33件確定**（ファイルなし。`pageSize=200`で再列挙し件数一致・新規発見なしを確認）。33フォルダ全件、直下ファイルの件数・種別を確認済み。

| フォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| ♪KYOWA　　水産・水産加工（EC卸）　　【札幌】 | `1cKsnkO18o3SoHarFGE8Qz94yAPw6xO19` | 3 | PDF |
| YKフーズ　（どら焼き）　　　　　　【千歳市】 | `1fkbAG7r0l52ulBXKE1XIFemBNbgg9crc` | 3 | Thumbs.db、画像、PDF |
| ♪飴谷製菓　　　菓子（バター飴）　　　【小樽】 | `1Gg7fE6FFv3s2s3XwXt5BF226a7aTLpBG` | 3 | PDF |
| エビジン　EBIJIN　　　　　　　　　　【余市町】 | `1afosCtAeggN0ERL4v4uLs1RswvCnDeUl` | 1 | Thumbs.db |
| エコみらい　（無添加トマトジュース）　【当麻町】eezo返信なし | `1TL7miWPK1wYH1ZKVtW8kr2Doer5CEAsx` | 2 | PDF |
| あまとう　　　　　　　　　　　　　【小樽市】 | `1yZ0PpYUqLT95r0w14EmdJ0Ya4vE1mgZN` | 2 | PDF |
| しおかぜ牧場　　　　　　　　　　　【積丹町】 | `1YR9Lbn-iUf87m5OvGRSmoD0QF9um5wKK` | 7 | Thumbs.db、画像 |
| エーデルワイスファーム (ベーコン節）　　【北広島市】eezo NG | `168y9tx2l8OAQVt3rKTzwXzFzMKFUsdQ0` | 2 | PDF、Word |
| やせいのおにくや　　　　　　　　　　【足寄町】eezo返信なし | `1vVaw0-up_KzCo9vos1XX2uLyMf8uK6sw` | 3 | PDF、Word |
| アプロディーテ　（ニセコ解離水）　　　【札幌市】 | `1gGg36NfT1nGHkl6qmR5zQw5-EX2SkkMG` | 1 | PDF |
| カネキタ北島農場（肉業者経由じゃないといけない）【余市町】 | `1j9mmQYscwvhCenA6wvNHdaCR7pZR6G96` | 1 | Thumbs.db |
| カネサ漁業　　　　　　　　　　　　　【寿都町】 | `1yqrKOhxN7xyxJiYlhBnT_ijovFqm-w1_` | 7 | Thumbs.db、画像、PDF |
| チーズ工房タカラ　　　　　　　【喜茂別町】取引NG | `1SHsn6QqL48BGSlAlgRURaRv9a6relYUy` | 1 | メール |
| ケイプ　ハートランドフェリー　　【稚内市】 | `1viRKFPEVnbic4QTrpSUwJWsa-WYvzh63` | 1 | PDF |
| ニセコ蒸留所　　　　　　　　　　【ニセコ町】 | `1moATrcFGM3tFVI7yncNusJ6kpmXI4Ijv` | 2 | PDF |
| 小嶋屋（へぎそば）　　　　　　　　【新潟市】 | `1So08h-DS3Aun8d-R4PaEhEuXvnSIBzK9` | 4 | Thumbs.db、画像、PDF |
| 兼由　KANEYOSHI　　　　　　　　【根室市】 | `1PvGLgUT2MMN2hhvZzJ9CnDgfT--DDrsx` | 3 | PDF |
| ネコ酒　Kカンパニー　　　　　　　　【札幌市】 | `1PPSONATiNAoLcsOrbzTZQRJqfs4uCisO` | 9 | Thumbs.db、画像多数、PDF |
| フルゥール　　　　　　　　　　　　　【秋田市】 | `1KMRzmNq2elJ3a3txPRqPq04kMb7DvJ6u` | 2 | Excel、PDF |
| 丸い遠藤商店　　　　　　　　　　【小樽市】 | `1IRV9ZtpJQpCS_yNJ-1nQjfm5vUhCYWRi` | 18 | Thumbs.db、画像多数、PDF |
| 江崎グリコ　（キャラメルキッチン）　【大阪市】 | `1si7bX1wT_OVK7VYzifFB-VxFoM5PJ7CV` | 1 | PDF |
| 北海道ケンソ（日高根昆布だし）　　【札幌市】 | `1uDxp3aTOtlTj2aPxfW7cUIxJMFQd9PD-` | 2 | PDF、Excel |
| 北島製パン　　　　　　　　　　　【木古内町】 | `1lrszkymUOJej3uMt_jeM0AZr1QNzjMDN` | 4 | PDF |
| 円甘味（まるあまみ）小樽石蔵バウム　【小樽】 | `1-4VGLD_ON4dtqBsghUyDgV-szdBhj-IW` | 2 | メール、PDF |
| 松原農園　　　　　　　　　　　　　【蘭越町】 | `1MbeTmyws8AsooLa3bnP1Y5F46b61Zfzu` | 6 | PDF、Thumbs.db、画像、メール |
| 北海道貿易開発㈱　永井取締役　　【小樽市】 | `1QpdH5bk4t48mLTB5MXuEgoKxGGyRAmLo` | 1 | PDF |
| 海商　　　　　　　　　　　　【大阪市】 | `1av0v8jLI6A05ZVJosg0KdW9M4-aYcPK_` | 3 | PDF |
| 焼尻島　めん羊　　　　　　【羽幌町】 | `1OmjaiyDR4SppO3lfkwSXZqOeiZrGSxmv` | 2 | Word、doc |
| 海洋養殖サーモン　　　　　【岩内町・泊村】 | `1Ra22voy8LwCvmJF90SBHSmBJs9-QtFU7` | 12 | Thumbs.db、画像多数 |
| 熊鹿庁　　　　　　　　　　　【木古内町】 | `12RFsHZ7A2PcJ8pKmdJT2fQLVP3gqrBy5` | 5 | Thumbs.db、画像、Word |
| 秋田県物産振興会　　　　　【秋田市】 | `1TkdKKALgOuyYpewB_8z2sLqve9EJVYhX` | 1 | PDF |
| 竹中罐詰㈱　　　　　　　　　【舞鶴市】 | `1blx6ooUAumdW6CTNPsw1WE4aX0De1ntD` | 1 | PDF |
| 胆振提案 | `1h9Pyt2MgfxN1zagywVE_YzPydzOwWDV_` | 7 | PDF |

### 6. ★仕入先開拓依頼

- **ID**: `1VTzu33pTQcVdQm25oISHNwzE1iU2w2_U`
- **URL**: https://drive.google.com/drive/folders/1VTzu33pTQcVdQm25oISHNwzE1iU2w2_U

サブフォルダ（3件、確認済み）:

| フォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| 回答書 | `1VR-B28cyQZ410IfjV5uT-ZBAjRC3F_2U` | 52 | Excel（仕入先開拓の依頼案件別シート）多数 |
| 依頼書 | `1JWBrIVAfrtyVsjWhbKVhueS1aJBKPV-Y` | 18 | Excel（依頼案件別シート）多数 |
| old | `17acqpJxaKz5aotBeMMEmFi3rSHJLCdhV` | 1 | Excel |

直下のファイル（5件、内容確認済み）:

| ファイル名 | 種別 |
|---|---|
| 26-08-04_SUP_TS_0019_焼きトウモロコシ_NISSHAビジネスサービス株式会社.xlsx | Excel |
| 依頼一覧.xlsx | Excel |
| 新規仕入先リスト.xlsx | Excel |
| YY-MM-DD_依頼番号_品目名_顧客名.xlsx（テンプレートと見られる） | Excel |
| 25-10-23_依頼番号_品目名_顧客名.xlsx | Excel |

### 7. ★鹿肉サンプル

- **ID**: `1SJqueXf4MqnePLT7Sj5VjLQOWXP4UJaG`
- **URL**: https://drive.google.com/drive/folders/1SJqueXf4MqnePLT7Sj5VjLQOWXP4UJaG

サブフォルダ: 2026　06月請求書 (`1UECuTmblzfkh4Hw3u8h9VgJEWEgcAinb`) — ファイル7件、確認済み（PDF。上田精肉店・ユック・函館・クイージ（食美樂）・知床エゾシカファーム等の仕入先別6月分請求書）

直下のファイル（2件、内容確認済み）:

| ファイル名 | 種別 |
|---|---|
| ~$鹿肉仕入＆サンプル.xlsx（Excelの一時ロックファイル） | Excel |
| 鹿肉仕入＆サンプル.xlsx | Excel |

### 8. ★ヤマト運輸

- **ID**: `1uj-ntmHKfZj9BH9neMeT1JfvTrJyPiBT`
- **URL**: https://drive.google.com/drive/folders/1uj-ntmHKfZj9BH9neMeT1JfvTrJyPiBT
- サブフォルダなし（末端フォルダ）。直下のファイル16件、すべて確認完了。

| ファイル名 | 種別 |
|---|---|
| 【Web出荷】利用申込書_産直.xlsx | Excel |
| 【Web出荷】利用規約_産直_2503.pdf | PDF |
| Thumbs.db | その他（Thumbs.db） |
| 普通運賃HP抜粋.jpg | 画像 |
| 新日本海商事様【Web出荷】サービス提案書（産直）.pdf - ショートカット.lnk | ショートカット(.lnk) |
| 運賃■■■お見積書20260629（新日本海商事）.pdf - ショートカット.lnk | ショートカット(.lnk) |
| 運賃■■■お見積書20260629（新日本海商事）.pdf | PDF |
| 新日本海商事様【Web出荷】サービス提案書（産直）.pdf | PDF |
| ③EEZO EC事業拡大に向けたヤマトグループ総合提案.pdf | PDF |
| 【Web出荷】データ交換規約_CSV版.pdf | PDF |
| 産直引取サービス提供に関する覚書.pdf | PDF |
| ②レジュメ　仮説課題と解決方法.pdf | PDF |
| ６月１７日ヤマト運輸打合せまとめ.docx | Word |
| ④チラシ　クロネコ掛け払い.pdf | PDF |
| ②レジュメ　EEZO EC拡大に向けたヤマトGRP総合提案.pdf | PDF |
| ①名刺　山谷・伊原さん.pdf | PDF |

### 9. 雪貯蔵フォルダ　　　　　　　　【美唄市・他】

- **ID**: `1r7SdQt_YwjXVtMfnZ-1T-bc48FiUNlzH`
- **URL**: https://drive.google.com/drive/folders/1r7SdQt_YwjXVtMfnZ-1T-bc48FiUNlzH
- サブフォルダなし（末端フォルダ）。直下のファイル5件、すべて確認完了。

| ファイル名 | 種別 |
|---|---|
| ニセコ雪長蔵（雑誌）.pdf - ショートカット.lnk | ショートカット(.lnk) |
| 美唄ホワイトデータ構想プレゼン.pdf - ショートカット.lnk | ショートカット(.lnk) |
| 美唄ホワイトデータ構想プレゼン.pdf | PDF |
| ニセコ雪長蔵（雑誌）.pdf | PDF |
| クールエナジー美唄市（パンフ）.pdf | PDF |

### 10. 永井さん仕入れ担当分

- **ID**: `1kCcsF3A9F3sLVSRidFpDm9QYqjDx1rQT`
- **URL**: https://drive.google.com/drive/folders/1kCcsF3A9F3sLVSRidFpDm9QYqjDx1rQT
- **作成日**: 2026-08-07（Google Drive上の`createdTime`で確認。「照合用見積置き場」直下に「●仕入」と同階層で新設）
- **由来**: 北海道貿易開発の永井取締役が持っていた酒などの仕入先データ（2026-08-07 高山さんより）
- **確認範囲**: 直下から全階層（最深で8階層目＝ルートから7階層下）まで再帰的に列挙し、2026-08-07時点で未確認は残っていない

直下のファイル（2件、内容確認済み）:

| ファイル名 | 種別 |
|---|---|
| コピードメチャン出荷銘柄特徴.xlsx | Excel |
| ドメチャン出荷分説明.xlsx | Excel |

直下のサブフォルダ（4件）:

| フォルダ名 | ID | ファイル件数（配下合計） | 内容 |
|---|---|---|---|
| メモ | `11Nm0htqKCLgrfzEKXnxUUtkuEsPjRR6i` | 1 | 沖田さん.docx のみ（末端フォルダ） |
| 2.カタログ | `16V8N4FA5IXGeMcfsg0NtPN_xU-HhUkGU` | 17 | 直下5件＋サブフォルダ「OLD」12件（末端） |
| 3.データまとめ | `1touNGIHR4U210Wnn7fE2B_niclUX7g8C` | 4 | 日本酒データ・商品リスト・茶価格調査（末端フォルダ） |
| 1.メーカー | `1gdCmsLS77sPP4UhC3pY3GvM9oy57qghH` | 267 | 醤油・梅酒・日本酒・焼酎・会津漆器・お茶・ウイスキー・ボンド商会の8カテゴリ、最深で7階層下（銘柄別フォルダ）まで展開 |

以下、4サブフォルダの内訳。

**10.1 メモ**

末端フォルダ。直下ファイル1件（沖田さん.docx、Word）。

**10.2 2.カタログ**

直下ファイル5件（Thumbs.db、「25-09-30_新日本海商事_酒ラインナップ」「25-09-22_Sake collection-Selected ver」のpptx・pdf各1）。

サブフォルダ「OLD」(`1SDVPrXfTR4hJZOa6BeyfOOncDznquSCv`) は末端フォルダ、ファイル12件（Thumbs.db、25-09-09〜25-07-24の酒ラインナップ・日本酒カタログ・Sake collectionのpptx/pdf群）。

**10.3 3.データまとめ**

末端フォルダ。直下ファイル4件（日本酒データまとめ.xlsx、ダルマ向け商品リスト.xlsx、~$日本酒データまとめ.xlsx〔Excelの一時ロックファイル〕、茶店頭価格調査.xlsx）。

**10.4 1.メーカー**

直下はフォルダのみ8件確定（ファイルなし）。仕入先カテゴリ別の構成。

| カテゴリ | ID | 配下ファイル合計 | 内容 |
|---|---|---|---|
| 醤油 | `1JsFif9r1y57qF38Crj-nRpj0aNDPifB5` | 25 | 湯浅醤油1社、7階層下まで展開（見積書・商品企画書・ラベル関連・サプライヤー証明書・原材料仕入書・製造工程フロー図・原材料一覧） |
| 梅酒 | `1IURMG0SkqXpic9NDlqieFksjP1rL3bjU` | 22 | 紀の司酒造・中野BC・加賀梅酒・CHOYAの4社（いずれも末端） |
| 日本酒 | `17h7yWaNGIV4Go0IKs4pz5u2dHh2Lu9R_` | 200 | 14蔵元。うち会津は5蔵元（榮川・曙酒造・会津ほまれ・大和川・名倉山）のグループで、榮川配下が最深（銘柄別9フォルダ） |
| 焼酎 | `1wn9xP63Cmo-oIfhdDeTQSMtFUeARKaM8` | 1 | 五島列島酒造1社（末端） |
| 会津漆器 | `1DUc8kqguNEZG6Ioipxp69X8LnqHTGsds` | 0 | 空フォルダ（サブフォルダ・ファイルともになし、確認済み） |
| お茶 | `1xnKxKaA5cH6Dc0QMxUbULMfgnKlU0Lr5` | 14 | 丸七製茶・協栄製茶・ロイヤルブルーティージャパンの3社 |
| ウイスキー | `1bStYn9TQ-Oz0j9wrXNIOsaDvQRt2PVU6` | 3 | 直下ファイル1件＋サンフーズ1社 |
| ボンド商会 | `1VhfLKNfkpe7Zpa0lLfRMGN5i3DbkNd7L` | 2 | 直下ファイル2件（見積・商品リスト、末端） |

以下、8カテゴリの内訳。

*醤油 → 湯浅醤油*

湯浅醤油 (`1iTpstpfb8QIWG_-WRPki9-ghDBzOOdbM`): 直下ファイル3件（産地証明取得用zip・提出書類zip・Thumbs.db）＋サブフォルダ7件（いずれも末端）。

| サブフォルダ名 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| 見積書 | `12hdZqWrGekRo6YJ8T52BZzDZSt7zxY9B` | 1 | 見積書PDF |
| 商品企画書 | `18zBCRu0dH09pR0kdJeCChB0aK5i639Lx` | 4 | 商品規格書PDF |
| ラベル関連 | `1YlC-x7G4Aqm2Xt538emljNx9hHQ8GiS5` | 5 | 画像（heic/png）、貼付見本 |
| ④サプライヤー証明書 | `1Zw4XCZO_1ohCbSAyD6KsoDVnMi-6ancO` | 2 | 産地証明書PDF |
| ③原材料の仕入書 | `1keoXS-7j9yZ-vJdKBNxww2BrqS4dt8ke` | 2 | PDF（産地証明書） |
| ①製造工程フロー図 | `15qi9TJ2Ba28kma6RXYSemCdonIYMpddM` | 2 | 製造工程図PDF |
| ②原材料一覧（成分表） | `12hIIL1jFDFuzuTqVXR-Ax8zCjV-XUtNk` | 6 | 原材料配合表・栄養成分分析表PDF（和文・英文） |

*梅酒*

直下ファイル1件（梅酒仕入れ候補リスト.xlsx、Excel）。

| 蔵元 | ID | ファイル件数 | 主な種別 |
|---|---|---|---|
| 紀の司酒造 | `1i8qfZWt15Cpz0oXMjJJSR4lBdgPBwOeC` | 2 | 商品企画書docx、商品規格書PDF |
| 中野BC | `1vQoh-5or3ixk6C6VAdgPXh4Xp7Xvogvm` | 6 | 見積書PDF、Thumbs.db、商品画像jpg、梅酒利点説明PDF |
| 加賀梅酒 | `17sX3XarcnQL-mHRp6Ab0A7tkITb5Muem` | 2 | 見積書PDF×2 |
| CHOYA | `1mNZEIdATw2zDu3jUDX9jDlSZhofaKLeK` | 11 | 酒ラインナップpptx/PDF、商品画像png/jpg、見積書PDF、Thumbs.db |

*日本酒*

直下ファイル1件（Thumbs.db）。14蔵元のフォルダ。

| 蔵元 | ID | ファイル件数（配下合計） | 備考 |
|---|---|---|---|
| 長州酒造 | `1aNu-mxMIXRGD6nWCK3LBzc48Mv8nC_0-` | 2 | 末端（Thumbs.db、資料pptx） |
| 稲見酒造 | `1xvC16qaYCIrr6DtyaKxu74Rux3qDNtxN` | 7 | 見積1＋写真6（サブフォルダ2、いずれも末端） |
| 若鶴酒造 | `1jpKC73unDrTJ38SGvbTn6Ir8rne08n8z` | 6 | 資料4＋見積2（サブフォルダ2、いずれも末端） |
| 近藤酒造 | `13txLn_SMwEN1zSBOrc83exeQVBL0cOr2` | 6 | 写真4＋見積2（サブフォルダ2、いずれも末端） |
| 梅ヶ枝 | `1X_o1NlNkAX-ShoGZxBRYCZaV0EP1vbsB` | 27 | 写真20＋見積7（サブフォルダ2、いずれも末端） |
| 小浜酒造 | `13OvukWGF-MBd55ckwfY4-81Ft7pthf8u` | 31 | 見積1＋写真30（サブフォルダ2、いずれも末端） |
| 小山本家酒造 | `1SPV1-REY1lx2RAOBrCkZgWceF6XNQfCk` | 4 | 末端（規格書・見積xlsx/PDF、輸出向け含む） |
| 光武酒造 | `1-sxayXxIiqm7cxdn5POa7KfZHVk1HPsm` | 1 | 末端（docx） |
| 名手酒蔵店 | `157h3EFVc82nwMTBKyZGkfumtN6p-yfZt` | 3 | 末端（pptx、PDF、見積xlsx） |
| 太田酒造 | `1h-1YrcQ_MPRpnYlTOlLtZEs3zX8BPYv4` | 1 | 末端（提案書PDF） |
| 会津 | `1ECu-GJAj9P-Ox21VyJL6uKSA6Mkb957Q` | 91 | 5蔵元グループ（榮川・曙酒造・会津ほまれ・大和川・名倉山）。詳細は次表 |
| 上川大雪酒造 | `1xyDmUoDKsQtno4qztV2pNBHxhYdDpOq_` | 1 | 末端（仕様書PDF） |
| 下関酒造 | `1Od61qWoHNCgIoHL6Gm_5hLvVKFn10Hna` | 1 | 末端（standard products PDF） |
| 佐々木酒造 | `1mxPhZqXaVQqfXbuxxEAQoo3TyU7jpnsp` | 18 | 直下3＋見積5（サブフォルダOLD含む）＋写真10（サブフォルダZIP含む） |

会津（5蔵元、配下合計91件）の内訳:

| 蔵元 | ID | ファイル件数（配下合計） | 備考 |
|---|---|---|---|
| 榮川 | `1leatQAqMYqvXMh7M4ApaMttMMdVSC5hH` | 47 | 見積3＋榮川資料44（Thumbs.db1・銘柄34・イメージ9）。銘柄配下はさらに9フォルダ（純米酒　辛口／純米酒／純米吟醸 GO BEYOND／純米大吟醸／純米吟醸／本醸造／特別純米酒／榮四郎　純米大吟醸／榮四郎　大吟醸、いずれも商品画像中心の末端フォルダ） |
| 曙酒造 | `1jxuDzxKvgIvaCdwE31Hy8sK4M8GPj3PP` | 5 | 末端（国内用・輸出用の商品一覧PDF、見積PDF、docx） |
| 会津ほまれ | `1_IoualuqBMp-CBHRcz9zVtrKpse4A_V5` | 7 | 見積3＋写真4（サブフォルダ2、いずれも末端） |
| 大和川 | `1in4K4Yr_ZKTgvR4x1kABx5KZVRzQIwWP` | 25 | 写真22（サブフォルダ「コンセプト写真（LIYU展開用）」6件・「商品写真」15件・Thumbs.db1）＋見積3（サブフォルダ「国内」1件含む） |
| 名倉山 | `1_Dg6yz7vT5D-e4iGJ-OnjUhxzYpq3OG2` | 7 | 写真5＋見積2（サブフォルダ2、いずれも末端） |

*焼酎 → 五島列島酒造*

五島列島酒造 (`1VF-GwxhZCM0RTuDtuxXbSbl-RHtWNqVI`): 末端フォルダ、ファイル1件（PDF）。

*会津漆器*

空フォルダ（サブフォルダ・ファイルともになし、確認済み）。

*お茶*

| 会社 | ID | ファイル件数（配下合計） | 備考 |
|---|---|---|---|
| 丸七製茶 | `1KNzRdsaapDpCbto-R1Kq1xLcIt20SHNK` | 1 | 末端（PDF） |
| 協栄製茶 | `18GqU774J3rjt8sqvnvEnsln8dxj_HstU` | 11 | 見積3＋写真8（サブフォルダ2、いずれも末端） |
| ロイヤルブルーティージャパン | `1R_t2avkcGaFlXeSUPV0SwTHiMa9XZ48b` | 2 | 末端（提案書PDF×2） |

*ウイスキー → サンフーズ*

直下ファイル1件（KEVIN向けウイスキー仕入れ候補リスト.xlsx）。サンフーズ (`1eEujTuxD9YSllHnlMLwd3XYeXNKkrycD`) は末端フォルダ、ファイル2件（瓶一覧xlsx、見積書PDF）。

*ボンド商会*

末端フォルダ。直下ファイル2件（【御見積】251217ビール.pdf、ボンド商会.xlsx）。

## 注記

この文書はDriveの実態のスナップショットであり、Drive側の変更で古くなる。更新時は同じ手順で再列挙して上書きする。

**ページネーション異常の検証結果（2026-08-05、2ラウンド目）**: 第1ラウンドでは「●生産者・メーカー別ファイル」で`pageSize=100`のまま`nextPageToken`を辿ると同一の1ページ目が返り続ける挙動が見られ、直下フォルダ数が「約100件」で確定できなかった。2ラウンド目で`pageSize=200`に上げて1回で列挙し直した結果、**123件で確定**した（`nextPageToken`は返却されず、1回のレスポンスで全件取得できた）。第1ラウンドで確認済みだった50フォルダ（文書内では「51フォルダ分」と記載されていたが、実際に表に記載されていたのは50件）との突合でも欠落・重複はなく、123件のうち50件が第1ラウンド確認済み、残り73件が今回新たに確認できたフォルダで、合計がちょうど123件と一致した。同様に「お蔵入りの生産者」も`pageSize=200`で再列挙し、**33件で確定**（第1ラウンドの33件と完全一致、新規発見・消失なし）。以上より、この異常は「直下フォルダ数がpageSizeの初期値100件に近く、100件を境にAPIが正しくページングしない」ことが原因だった可能性が高い。100件超のフォルダを列挙する際は、はじめから`pageSize`を200程度に上げて1回で取得するのが安全である。

**「90社内GRP　オーセントホテル小樽」の完走結果（2026-08-05、3ラウンド目）**: 直下ファイルが100件を超えるため2ラウンド目では完走できなかったが、`pageSize=200`で再実行した結果、**155件で確定**（`nextPageToken`は返却されず、1回のレスポンスで全件取得。サブフォルダなし）。上記の「約100件を境にページングが不安定になる」という仮説と整合する結果であり、100件超のフォルダは`pageSize=200`で一発列挙するのが安全という見立てを補強した。

再列挙の手順:

1. `mcp__Google_Drive__search_files` を `query: "parentId = '<フォルダID>'"`、`pageSize: 200`（直下件数が多い、または不明なフォルダは100ではなく200を推奨）、`excludeContentSnippets: true` で実行する
2. `nextPageToken` が返る場合はページネーションする
3. 返却された各フォルダについて同様に再帰する
4. 2026-08-05時点で本文書に「未確認」マークは残っていない。今後Drive側の変更を追う場合は、変更が想定されるフォルダから優先的に再列挙する
