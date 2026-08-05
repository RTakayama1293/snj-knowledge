# 仕入先情報 Google Drive ディレクトリ構造

## 出典情報

- **取得日**: 2026-08-05
- **ルートフォルダ名**: 照合用見積置き場
- **ルートフォルダURL**: https://drive.google.com/drive/folders/1dFGh6VSyxHhpenaip-e7C08fS3WOu0Yc
- **取得方法**: Google Drive MCPコネクタ（`search_files`、`parentId`指定で再帰列挙）
- **所有者**: Googleドライブ上の高山さんアカウント（`ryota.takayama1293@gmail.com`）

## 概要

高山さんが仕入先の見積・規格書・やり取り記録を集約したGoogle Driveフォルダ「照合用見積置き場」のディレクトリ構造を記録する。見積照合・仕入先参照時に「どこを見ればよいか」を示すためのナレッジ。

**重要な注記（範囲の限界）**: このフォルダは想定以上に規模が大きく、特に「●生産者・メーカー別ファイル」（仕入先ごとのフォルダが約100件）と「お蔵入りの生産者」（約33件）の配下は、1仕入先フォルダあたり数件〜90件超のファイル（見積書・規格書・メール・写真・動画等）を含む。今回のセッションでは以下の範囲まで列挙した。

- **全階層のフォルダ名・ID・URLを列挙完了**（フォルダ構造は全件確定）
- **ファイル一覧（ファイル名・種別）まで確認できたのは以下のみ**:
  - ★2026新EEZOフォルダ、★2026船上ニセコメロン、★はまなす催事、★仕入先開拓依頼、★鹿肉サンプル、★ヤマト運輸、雪貯蔵フォルダ（直下のファイル）
  - ●生産者・メーカー別ファイル配下の約100フォルダのうち、51フォルダ分
- **ファイル一覧が未確認（フォルダ名のみ確認）の部分**:
  - ●生産者・メーカー別ファイル配下の残り約49フォルダ
  - お蔵入りの生産者配下の33フォルダ全件
  - ★2026新EEZOフォルダ配下の19サブフォルダ全件
  - ★はまなす催事配下の4サブフォルダ全件
  - ★仕入先開拓依頼配下の3サブフォルダ全件
  - ★鹿肉サンプル配下の1サブフォルダ（2026 06月請求書）
  - ★2026船上ニセコメロン配下の1サブフォルダ（★2025船上ニセコメロン）
  - 一部の生産者フォルダ内に見つかったさらに深い階層のサブフォルダ（後述）

未確認部分は「未確認」と明記し、ファイル数・ファイル名を推測で埋めていない。追加調査が必要な場合は同じ手順（`search_files` を対象フォルダIDに対して`parentId = '<ID>'`で実行）で再列挙すること。

## ディレクトリツリー

フォルダ名の横に判明している範囲でのフォルダ数・ファイル数を付記する。`（未確認）`は今回セッションでファイル一覧を取得していないことを示す。

```
照合用見積置き場/
└ ●仕入/
  ├ 1. ●生産者・メーカー別ファイル/ （フォルダ100・ファイル0）
  │   ※ 100フォルダの内訳は「フォルダ別詳細」参照。51フォルダはファイル内容確認済み、残り49フォルダは未確認
  │
  ├ 2. ★2026新EEZOフォルダ/ （フォルダ19・ファイル11）
  │   └ 19サブフォルダ（すべて未確認：EC26xx案件フォルダ群）
  │
  ├ 3. ★2026船上ニセコメロン/ （フォルダ1・ファイル21）
  │   └ ★2025船上ニセコメロン/ （未確認）
  │
  ├ 4. ★はまなす催事/ （フォルダ4・ファイル6）
  │   ├ 発注書/ （未確認）
  │   ├ 後で削除/ （未確認）
  │   ├ 請求書　（ 納品書）/ （未確認）
  │   └ 配置・服装・ポップ/ （未確認）
  │
  ├ 5. お蔵入りの生産者/ （フォルダ33・ファイル0）
  │   ※ 33フォルダすべて未確認（フォルダ名のみ確認。「フォルダ別詳細」参照）
  │
  ├ 6. ★仕入先開拓依頼/ （フォルダ3・ファイル5）
  │   ├ 回答書/ （未確認）
  │   ├ 依頼書/ （未確認）
  │   └ old/ （未確認）
  │
  ├ 7. ★鹿肉サンプル/ （フォルダ1・ファイル2）
  │   └ 2026　06月請求書/ （未確認）
  │
  ├ 8. ★ヤマト運輸/ （フォルダ0・ファイル16）※末端フォルダ・確認完了
  │
  └ 9. 雪貯蔵フォルダ　　　　　　　　【美唄市・他】/ （フォルダ0・ファイル5）※末端フォルダ・確認完了
```

## フォルダ別詳細

### 1. ●生産者・メーカー別ファイル

- **ID**: `1-GKzk9O3--_nevXy3mbvfBtCotRDZfVZ`
- **URL**: https://drive.google.com/drive/folders/1-GKzk9O3--_nevXy3mbvfBtCotRDZfVZ
- 直下はフォルダのみ100件（ファイルなし）。仕入先ごとに1フォルダの構成。フォルダ名の頭の数字は商材カテゴリ番号（01鹿肉／02精肉／03水産／04野菜／06チーズ／20飲料／50菓子／60食品）と見られる。

以下、ファイル内容を確認できた51フォルダを列挙する（フォルダ名・ID・URL・ファイル件数・種別）。件数はメール(.eml)・PDF・Excel・画像・動画等すべての合計。

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
| 02精肉　GOODGOOD（1億9400万）【大阪府】 | `1vpjVoD1W704qd3yqAPaBE-nEdaWhsKPJ` | 8＋サブフォルダ1（OLD、未確認） | PDF、Word |
| 01鹿肉　食美樂　　　　　　　　【新冠町】 | `1SGsx-AFFs2gn_SFX3siPPbv76WfuPsCy` | 2 | Word、PDF |
| 02精肉　エスフーズ | `1TEH9fll5BhCxdresONm_GQwuCGVDdZN4` | 2 | Excel |
| 02精肉　美瑛ファーム　美瑛放牧酪農場　【美瑛町】 | `1G-_p81wnU6jCeNEzG6WF04zz8zfP8sfA` | 3 | メール、PDF |
| 02精肉　サカモト食品　　　　　【幕別町】　matsu | `1WDsvBlu0tOkseTbMcaRvyAiuqOglEQan` | 4＋サブフォルダ1（サカモト食品さんからもらった画像EC掲載OK、未確認） | PDF、メール、Word |
| 02精肉　ファームズ千代田　　　　【美瑛町】　kuro | `1cPYisi3vHqBKuneYVHwJDj9uG6Qu6sBW` | 約43 | 画像多数、PDF、メール |
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
| 03水産　小樽水産加工業協同組合　【小樽市】　matsu | `1StlWFP8BgqTXgZeer3KYFmfOozA3kWxf` | 約35＋サブフォルダ5（【商品写真】かね丁鍛冶、かね丁鍛冶見積202507最新、ホリ商店（ほっけ）、参考資料、井原水産hp／すべて未確認） | PDF、Excel、画像多数 |
| 03水産　丸恭水産 | `1Z2M3rXSogjiMuB3dNs2pjbga54vBRpH2` | 2 | Excel、メール |
| 04野菜　ニセコビュープラザ 直売会協同組合　【ニセコ町】　matsu | `1tAD8sOy8cq4W1DDzJ_vRrFArZJgJKRmy` | 9＋サブフォルダ5（メロン、干し芋、＿削除だが一旦保存、野菜セット、恋するじゃが（熟＆新じゃがセット）／すべて未確認） | Excel、PDF |
| 03水産　知床工房吉野　　　【斜里町・知床】 | `1z_b4L2P32IIyE2ebEm4xQpHnJZpStgbz` | 13 | 画像、メール、Excel、PDF |
| 04野菜　原田産業　原田さん　※見積なし　【倶知安町】 | `1kCrSKA2U3L9WUTGR0gjk-4FUKJVhV8yW` | 20 | 動画、画像、PowerPoint、Word、PDF |
| 03水産　福島町役場　陸上養殖あわび　【福島町】 | `1RRWtQ9ALNeZzRw3mPntqq-9UcL_Vn7Sv` | 5＋サブフォルダ1（福島町から画像データ（20260106）、未確認） | メール、Word、Excel、画像 |
| 03水産　東しゃこたん漁協　　　　【古平町】 | `1RvdPFAASGiks8ZQ4Is344b_3V4rT5GrB` | 5 | PDF、メール、Excel |
| 03水産　山下水産　　　　　【寿都町】　kuro | `1FjunPozso4h4qacQzLkDJVhyprnUR0wD` | 7 | PDF、メール、Word |
| 04野菜　シニック（紫蘇）　　　【蘭越町】 | `1TV5RgNFPpCyCn9XOoTwMyADmsNEboqyk` | 5＋サブフォルダ1（20260706蘭越視察写真門永、未確認） | 動画、Word、メール、Excel |
| 03水産　王子サーモン | `1Y6CcoNvEgyrTrXuzRZi2Ar0lV2jTZufa` | 3 | PDF |
| 04野菜　ベジタブルワークス　　　　　　【真狩村】 | `1HtZVodh2dRY3L2vWSLJIlAe8-zm_9gFt` | 約60 | PDF多数、画像多数、Excel |
| 03水産　藤田水産　　　　　　　　　【小平町】 | `1H1VWEUdhC3L1EGU5EsTim0NnuhLZAF85` | 1 | Excel |
| 03水産　落石漁港協同組合　　　　　　【根室市】 | `1zAHeFxJ2l9AxXCE0zolZr7lSMOcycjyk` | 3 | PDF |
| 03水産　龍王水産　札幌　　　　　　　【札幌】 | `1V0RhHgzAtCbFxywWOYv8sxvdSuRfFVul` | 4 | PDF、Word、画像 |
| 04野菜　リストファーム　※見積なし　　【倶知安】 | `1Eo8wMjo2IwZalHFWXSDoi2UgE0BIRcEq` | 4 | PDF |
| 04野菜　水戸青果　　　　　　　【札幌市】 | `18yuCnOY8PewkfzpQa11bX3dLJ5NqYIwm` | 8 | PDF、PowerPoint |
| 04野菜　中野ファーム　トマト（ジュース）　【余市町】 | `1MTP421x4IDKlY4jUkNG3QS7ztC_3pf7j` | 11 | メール、画像、PDF |

**未確認（フォルダ名のみ確認）の残り49フォルダ**（ファイル一覧は取得していない）:

十勝グランナッツ（落花生）【芽室町・士幌町】(`1bViyXlUxkMdI7T4grHFgaIIlFzcxvZx0`)、チーズダム CHEESEDOM（eezo未公開）【せたな町】(`1Pwy4oGGXlA31kZlb-0qBfEsAbUGrolFw`)、長福ファーム　※見積なし【倶知安町】(`1V8cDrXP-DwOrV9D2DyETdbwvdfCP_4m5`)、カミカワキッチン（1000万）eezo未公開【上川町】(`1LOdn5JX_WiXLREPbTEsvfO1J17OILbTX`)、しあわせチーズ工房（eezo未公開）【足寄町】(`1WXCwpnDaT99AduPjvPyOxOnVvRw662-T`)、トワ・ヴェール（フジタCo）【黒松内町・札幌】(`1iiLnLcKkbBfvb671BRnMyrDZ8_XIbRNj`)、ニセコチーズ工房（eezo未公開）【ニセコ町】(`1anuX75Ymf0OukdcQnqyIUTovHrNj7wBh`)、十勝野フォロマージュ　見積もらえてない【中札内村】(`11gD3CJ0hLY4rU4gmXQPqhTU7E9_IAX8j`)、CHISE GARDEN チセガーデン【ニセコ】(`12_FclYoJOiZP-e7P2PcqE-Sca_ba5tZS`)、アップルランド山の駅おとえ　シードル【深川市】(`1MXUjzy8BudS52QNdX5n0Yq65wlpBVrAb`)、キリンビバレッジ【札幌】(`17roKmYHAOY_piNBR5NJD7EVtYJYN25Hz`)、トカプコーヒー【中札内村】kuro(`1yXAJw0mcj6rF9KsPxfbkwAIrgnP32RLQ`)、ハリカ桑名園【富良野市】kuro(`1eJKtzdYF7nSNR5K-s3afhnSDnA5dZxV7`)、ニキヒルズ NIKI HILLS【仁木町】kuro(`1wPdcVjIBWlRhnWtxCm_wbnOI1lQYebZQ`)、網走ビール（網走市）(`1wedE1qcuO-sRqYh7K7QyQQlopjIrE9OH`)、ナオバンズ Nao-buns【倶知安町】matsu(`17BrWOd6FY1JSFp2ya6Hmd9-wBjz-C9oh`)、奥尻ワイナリー【奥尻町】(`1E5J02NIj-O4Zdc8qci5XmgVabpVoVJD0`)、北王よいち【余市町】kuro(`1kwQegrAe2lzZyfctFIk6dYXJg13wexBS`)、わらく堂【札幌市】matsu(`10F8k3FCitQ4-W6LLw3Id3CwsHqdGu3jP`)、積丹スピリット【積丹町】(`1SYehNxgriHf2l93dUpoh6keE1e61gdg3`)、ほんま　月寒あんぱん本舗（3600万）【恵庭市】matsu(`1Vm_pTH39GyOZj3n5H2ZycxQ-veetH8eH`)、三海幸【函館市】matsu(`1V_tW3g40y-7vdBt9Ezj6i5Vy_LFv_Hnd`)、丸市岡田商店【札幌市】matsu(`1mtPdmNHeFpSV-mNvWot5fJF23Db8FuWp`)、北海道名販【室蘭市】matsu(`1LTys4JNQJY8os2JqDHtnuRwD-egUjBHX`)、北海道デイリーライス（小樽市）高級おはぎ(`1ETnFxPvDjuufmoDzpJH2vp_U6sT-nqv5`)、厚真観光協会・SNF苫小牧【厚真町】(`1c_dsatstskEC7Rg6wwHMKzkk9AmlvEZp`)、にんにく種蔵【札幌市】matsu(`1rxMomeVOrN1hUYTDveYD-9uvy_ipSAQa`)、山栄食品工業　※前精算【函館市】(`16is2_yGr4mP2TAwuJWpylAnTnfXySjUD`)、昭和製菓　※前精算【函館市】前精算の為EEZO NG(`1of5KQas-JbBrIXt06zvVbS8g2Q6ovO2I`)、谷田製菓(きびだんご)【夕張市】matsu(`1gajXS1Hm6IMwiGEXoPsd6Xde7A8n7fjx`)、Atta（フリーズドライアスパラ他）【札幌市】(`1uXt8ofKr5hnYF5LpUMdfXKQZcBQGxoQi`)、うんがぷらす㈱【小樽市】kuro(`1zWVd_3WcUE8LVX3NDrCou3XklodlHH2l`)、梅屋 UMEYA【旭川市】kuro(`1pj-DHtOqabmouRgYkruh4CfLc4OCs86W`)、からくさ Han's Marine（札幌市）※海鮮キムチ(`1JqGEif9CPz4nCO2-VtrsY14s4al-788W`)、サンマルコ食品　冷凍コロッケ【関西支店が窓口】(`1GkzSjl3A7RF2nIsQDKda49PaJyQkv7FI`)、アベファーム ABE FARM【赤井川村】kuro(`1yy_vwVDaqgbNP3eezeLIbf4LzOEHJRdT`)、サザエ食品【札幌市】matsu(`1GSj7fF05gzuqSIt-GzRJcbXN7zOm-ClB`)、エーデルワイスファーム（ベーコン節）【北広島市】(`1rEkgFxyK8m-f3pv3d2MzRI2t2DOUccQW`)、シャルキュトリーアカイシ【ニセコ町】kuro(`1vAwOyXwcNU8dKpnHcrEOPrEyd1R7jfNa`)、ジョー・エンタープライズ【札幌市】matsu(`1H5Bv4eUc3BbedeHPFgPyvJfZ4jVSBY3L`)、ノベルズ食品【上士幌町】kuro(`1UsTZ6hcJVoH4a4CtJXz72L0mMdw-Md27`)、ベターデイズ（札幌市）※豚まん(`15vw62hThUXdHv283JDpk8CqPKEydVFhb`)、ノースファームストック（ジャムなど）【岩見沢】(`1MVtC5KLhiF9_DPbx3eQnO3XKpDBxWQTf`)、ノースボート　利尻昆布ラーメン【札幌市】matsu(`1tEodPf192qLLYLXMjOwCeQ9bnspKaVT3`)、京樽(`1uan2lGjicAp4Zq8eXzrJLDIZkxXjLuSO`)、ハンズマリン　海鮮キムチ【札幌】(`1DXjY5yEdx4iDblOLYnoNLyi0OoxhxE3v`)、リージョナルデザイン Regional Design INC【長沼町】eezo返信なし(`1NRvsPnDLMRoZkkJBF3ysppL-1BuF5O8M`)、フジ FUJI【札幌市】matsu(`1fs3KfnfaVA6aqXmAalxbCXXVeiYfbc05`)、丸一大西食品【札幌市】kuro(`1V6rxGUn0xoeM3h_uABamR21CT6sVIHan`)、佃善（札幌）豚じゃが・餃子(`13YFcDJn11ynxyDpSKT4d-l0rmB2rWwfb`)

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

直下のサブフォルダ（19件・**すべて未確認**。EC受注案件ごとに1フォルダの構成と見られる）:

EC2604 ニセコビュープラザ　（4セット商品）(`1mF02sjl9BnJu66hgWPwHopaTdAkX1hF_`)、EC2606 オーセントホテル(`1PTBIOgaVz8jW8E-0VeG_3BW9VFfDs_E6`)、EC2604 梅屋(`1u7vMDUnQ7ikssxa-c2eA0D12mbquuOIT`)、EC2604 ナオバンズ　(2セット）(`1rWExBGMtLS9v9E7Pv-1AUJDuDHKcM0MQ`)、EC2604 トワヴェール・フジタCo, （11セット商品）(`1I4rQgPrguKvW2qhECTp60x70ijyx9V50`)、EC2604 ニキヒルズワイナリー（3セット商品）(`1M89TYb22iSrgE3tnagddVhyDUOzbPy3w`)、EC2604 小樽水産加工業組合 （6セット）(`1LxRkGxGSGufvV9XM7taQ1iWNORfZkW5Q`)、EC2606 ㈱六美(`1gD-PKmuNkD15etdYh4G3FDzUOXxebiBe`)、EC2606 トワヴェール・フジタ（清涼・アイスクリーム）(`1Z-Z6p6t-Pi47l-0prmknUPMH3bzeLksU`)、EC2606 シャルキュトリーアカイシ　（清涼・肉ハム）(`1IGO7HYK5iuxuvqa0rN3rfrkFZXeuKjnk`)、EC2606 上川大雪　（清涼・日本酒）(`1nfABjvmIE96__JQIcPwyTrVfdXMc_q4W`)、EC2606 みにとまとん　（オモシロ焼き菓子）(`1BwQXrujm7s_cesRhhbbsHpyA3kDSwB6l`)、EC2606 ニキヒルズワイナリー（ノンアルコール NEIRO）(`12Rrdr2Z_AyZ2f6qX0x5SvwwlJfqlAwrX`)、EC2606 北王よいち　　（ぶどう・林檎・トマトジュース）(`1zJ1Dt-pig2HZXu1ICRPZZZeLPImQJOmp`)、EC2606 小樽水産加工業協同組合(`1vYANBGESBOuFEyTKBxyrgN-P8Me9jDsF`)、EC2606 江戸屋　（清涼・アイス・ジェラート）(`1Xy79pL9LkSyW769Bb6QQkCqo3HQJBvXd`)、EC2607 採用検討中 ・ ボツ(`12LS3L-9Ons_mSZa7NankGKQwBYAOeiKe`)、EC2606撮影用　請求書＆納品書(`1suGnn0I5Za6GbrJ0hv5wm1UFfzX5pdLb`)、EC260X ベターデイズ　（まん10個選択可）(`1HPpTRXvRaL7-Bc09ZQxUWk45uxfmWtH6`)

### 3. ★2026船上ニセコメロン

- **ID**: `1xxF91R1AH1zTpfA-UGxbGykvcAxNO-2V`
- **URL**: https://drive.google.com/drive/folders/1xxF91R1AH1zTpfA-UGxbGykvcAxNO-2V

サブフォルダ: ★2025船上ニセコメロン (`1DEJYkas3-aqfugCwptJiFVCNHEuqW6gj`) ※未確認

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

サブフォルダ（4件・**すべて未確認**）: 発注書(`1zstAF-g9KlzGmuIRUIdDX_btB7ZtKzmT`)、後で削除(`1ugBDNNPuvOjE7FtZR82oMmy4YoIP8r41`)、請求書　（ 納品書）(`1U2wRvd5SEqpmCi9k_Y8FMVMaqGgkAfJk`)、配置・服装・ポップ(`18vjUG9RCWzNE1iKdeFPR4Egd7WIjmb-b`)

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

直下はフォルダのみ33件（ファイルなし）。**すべて未確認**（フォルダ名のみ）。

♪KYOWA　　水産・水産加工（EC卸）　　【札幌】(`1cKsnkO18o3SoHarFGE8Qz94yAPw6xO19`)、YKフーズ　（どら焼き）　　　　　　【千歳市】(`1fkbAG7r0l52ulBXKE1XIFemBNbgg9crc`)、♪飴谷製菓　　　菓子（バター飴）　　　【小樽】(`1Gg7fE6FFv3s2s3XwXt5BF226a7aTLpBG`)、エビジン　EBIJIN　　　　　　　　　　【余市町】(`1afosCtAeggN0ERL4v4uLs1RswvCnDeUl`)、エコみらい　（無添加トマトジュース）　【当麻町】eezo返信なし(`1TL7miWPK1wYH1ZKVtW8kr2Doer5CEAsx`)、あまとう　　　　　　　　　　　　　【小樽市】(`1yZ0PpYUqLT95r0w14EmdJ0Ya4vE1mgZN`)、しおかぜ牧場　　　　　　　　　　　【積丹町】(`1YR9Lbn-iUf87m5OvGRSmoD0QF9um5wKK`)、エーデルワイスファーム (ベーコン節）　　【北広島市】eezo NG(`168y9tx2l8OAQVt3rKTzwXzFzMKFUsdQ0`)、やせいのおにくや　　　　　　　　　　【足寄町】eezo返信なし(`1vVaw0-up_KzCo9vos1XX2uLyMf8uK6sw`)、アプロディーテ　（ニセコ解離水）　　　【札幌市】(`1gGg36NfT1nGHkl6qmR5zQw5-EX2SkkMG`)、カネキタ北島農場（肉業者経由じゃないといけない）【余市町】(`1j9mmQYscwvhCenA6wvNHdaCR7pZR6G96`)、カネサ漁業　　　　　　　　　　　　　【寿都町】(`1yqrKOhxN7xyxJiYlhBnT_ijovFqm-w1_`)、チーズ工房タカラ　　　　　　　【喜茂別町】取引NG(`1SHsn6QqL48BGSlAlgRURaRv9a6relYUy`)、ケイプ　ハートランドフェリー　　【稚内市】(`1viRKFPEVnbic4QTrpSUwJWsa-WYvzh63`)、ニセコ蒸留所　　　　　　　　　　【ニセコ町】(`1moATrcFGM3tFVI7yncNusJ6kpmXI4Ijv`)、小嶋屋（へぎそば）　　　　　　　　【新潟市】(`1So08h-DS3Aun8d-R4PaEhEuXvnSIBzK9`)、兼由　KANEYOSHI　　　　　　【根室市】(`1PvGLgUT2MMN2hhvZzJ9CnDgfT--DDrsx`)、ネコ酒　Kカンパニー　　　　　　　【札幌市】(`1PPSONATiNAoLcsOrbzTZQRJqfs4uCisO`)、フルゥール　　　　　　　　　　【秋田市】(`1KMRzmNq2elJ3a3txPRqPq04kMb7DvJ6u`)、丸い遠藤商店　　　　　　　　　　【小樽市】(`1IRV9ZtpJQpCS_yNJ-1nQjfm5vUhCYWRi`)、江崎グリコ　（キャラメルキッチン）　【大阪市】(`1si7bX1wT_OVK7VYzifFB-VxFoM5PJ7CV`)、北海道ケンソ（日高根昆布だし）　　【札幌市】(`1uDxp3aTOtlTj2aPxfW7cUIxJMFQd9PD-`)、北島製パン　　　　　　　　　【木古内町】(`1lrszkymUOJej3uMt_jeM0AZr1QNzjMDN`)、円甘味（まるあまみ）小樽石蔵バウム　【小樽】(`1-4VGLD_ON4dtqBsghUyDgV-szdBhj-IW`)、松原農園　　　　　　　　　　　【蘭越町】(`1MbeTmyws8AsooLa3bnP1Y5F46b61Zfzu`)、北海道貿易開発㈱　永井取締役　　【小樽市】(`1QpdH5bk4t48mLTB5MXuEgoKxGGyRAmLo`)、海商　　　　　　　　　　　　【大阪市】(`1av0v8jLI6A05ZVJosg0KdW9M4-aYcPK_`)、焼尻島　めん羊　　　　　　【羽幌町】(`1OmjaiyDR4SppO3lfkwSXZqOeiZrGSxmv`)、海洋養殖サーモン　　　　　【岩内町・泊村】(`1Ra22voy8LwCvmJF90SBHSmBJs9-QtFU7`)、熊鹿庁　　　　　　　　　　　【木古内町】(`12RFsHZ7A2PcJ8pKmdJT2fQLVP3gqrBy5`)、秋田県物産振興会　　　　　【秋田市】(`1TkdKKALgOuyYpewB_8z2sLqve9EJVYhX`)、竹中罐詰㈱　　　　　　　　　【舞鶴市】(`1blx6ooUAumdW6CTNPsw1WE4aX0De1ntD`)、胆振提案(`1h9Pyt2MgfxN1zagywVE_YzPydzOwWDV_`)

### 6. ★仕入先開拓依頼

- **ID**: `1VTzu33pTQcVdQm25oISHNwzE1iU2w2_U`
- **URL**: https://drive.google.com/drive/folders/1VTzu33pTQcVdQm25oISHNwzE1iU2w2_U

サブフォルダ（3件・**すべて未確認**）: 回答書(`1VR-B28cyQZ410IfjV5uT-ZBAjRC3F_2U`)、依頼書(`1JWBrIVAfrtyVsjWhbKVhueS1aJBKPV-Y`)、old(`17acqpJxaKz5aotBeMMEmFi3rSHJLCdhV`)

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

サブフォルダ: 2026　06月請求書 (`1UECuTmblzfkh4Hw3u8h9VgJEWEgcAinb`) ※未確認

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

## 注記

この文書はDriveの実態のスナップショットであり、Drive側の変更で古くなる。更新時は同じ手順で再列挙して上書きする。

再列挙の手順:

1. `mcp__Google_Drive__search_files` を `query: "parentId = '<フォルダID>'"`、`pageSize: 100`、`excludeContentSnippets: true` で実行する
2. `nextPageToken` が返る場合はページネーションする（ただし2026-08-05取得時、「●生産者・メーカー別ファイル」ではページトークンを使っても同一の1ページ目が返る挙動が確認された。件数が想定と食い違う場合はこの挙動を疑うこと）
3. 返却された各フォルダについて同様に再帰する
4. 本文書の「未確認」マークがついたフォルダから優先的に着手する

**未確認部分の再列挙が必要な優先度（提案）**: 見積照合で頻繁に参照する仕入先が「●生産者・メーカー別ファイル」の未確認49フォルダに含まれる場合はそこを先に。「お蔵入りの生産者」は名称からして現在非アクティブな仕入先の可能性が高く、優先度は低いと考えられる（高山さんに確認要）。
