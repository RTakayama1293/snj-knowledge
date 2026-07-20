# Metaショップ データフィード入力ガイド（EEZO版）

**作成日**: 2025年11月10日  
**対象**: 新日本海商事 EEZO Instagram/Facebookショップ

---

## 📋 項目一覧と優先度

### 🔴 必須項目（9項目）- これがないと登録できない

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 1 | **id** | 商品の一意なID<br>SKU番号を推奨<br>※CS-Cartの商品IDでOK | `EZOSHIKA_MOMO_2KG`<br>`AKAGYU_SIROIN_300G` |
| 2 | **title** | 商品タイトル<br>200文字以内<br>検索されるキーワードを含める | `【北海道産】エゾシカもも肉 2kg 真空パック 業務用`<br>`熊本あか牛 サーロイン 300g A4等級` |
| 3 | **description** | 商品説明<br>9999文字以内<br>特徴、調理法、規格を記載 | `北海道の大自然で育ったエゾシカのもも肉です。低脂肪・高たんぱくで健康志向の方におすすめ。脂肪含有率2%、鉄分は牛肉の3倍。真空パックで鮮度を保ち、フェリー輸送でお届けします。推奨調理法：55℃30分の低温調理でロゼに仕上げ、赤ワインソースと合わせてください。` |
| 4 | **availability** | 在庫状況<br>2択のみ | `in stock` (在庫あり)<br>`out of stock` (在庫なし) |
| 5 | **condition** | 商品状態<br>2択のみ | `new` (新品) ※食品は基本これ<br>`used` (中古) |
| 6 | **price** | 価格<br>数字 + 半角スペース + 通貨コード<br>小数点は `.` を使用 | `5000 JPY`<br>`8500.00 JPY`<br>※カンマ不可 |
| 7 | **link** | 商品ページURL<br>CS-CartのURL | `https://eezo.jp/products/ezoshika-momo-2kg`<br>※実際のCS-Cart商品URL |
| 8 | **image_link** | 商品メイン画像URL<br>500×500px以上<br>JPG/PNG/GIF | `https://eezo.jp/images/ezoshika_momo_main.jpg`<br>※CS-Cartにアップロード済みの画像URL |
| 9 | **brand** | ブランド名<br>100文字以内 | `EEZO`<br>`現代の北前船`<br>`GOODGOOD農場`（生産者名でもOK） |

---

## 🟡 重要な任意項目（優先度高）

### カテゴリ・分類

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 10 | **google_product_category** | Google商品カテゴリ<br>[カテゴリ一覧](https://www.facebook.com/business/help/526764014610932) | `Food, Beverages & Tobacco > Food Items > Meat & Seafood`<br>`Food, Beverages & Tobacco > Food Items > Fruits & Vegetables` |
| 11 | **fb_product_category** | Facebook商品カテゴリ<br>Facebookの分類 | `Food & Grocery`<br>`Alcoholic Beverages` |

**EEZO向けカテゴリ対応表**
```
畜産物（エゾシカ・あか牛）
→ Google: Food, Beverages & Tobacco > Food Items > Meat & Seafood
→ FB: Food & Grocery

水産物（カニ・ウニ・サケ）
→ Google: Food, Beverages & Tobacco > Food Items > Meat & Seafood
→ FB: Food & Grocery

農産物（じゃがいも・アスパラ・メロン）
→ Google: Food, Beverages & Tobacco > Food Items > Fruits & Vegetables
→ FB: Food & Grocery

酒類（日本酒・焼酎・ワイン）
→ Google: Food, Beverages & Tobacco > Beverages > Alcoholic Beverages
→ FB: Alcoholic Beverages
```

### 価格・販売

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 12 | **quantity_to_sell_on_facebook** | 販売可能数量<br>※Instagram/FBでの直販用<br>※EEZOは外部サイト誘導なので不要 | 空欄でOK |
| 13 | **sale_price** | セール価格<br>期間限定セール時のみ | `4500 JPY` (通常5000円→セール4500円) |
| 14 | **sale_price_effective_date** | セール期間<br>開始日時/終了日時 | `2025-11-15T00:00+09:00/2025-11-30T23:59+09:00`<br>※日本時間は+09:00 |

### バリエーション管理

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 15 | **item_group_id** | 同一商品のバリエーション<br>グループID<br>※サイズ違い・色違い等をまとめる | `EZOSHIKA_MOMO`<br>（2kg版も500g版も同じID） |
| 17 | **color** | 色<br>200文字以内 | 食品なので通常空欄<br>野菜なら：`緑` `赤` |
| 18 | **size** | サイズ<br>200文字以内 | `2kg`<br>`300g`<br>`1箱（約5kg）` |

**バリエーション例：エゾシカもも肉**
```
商品A: id=EZOSHIKA_MOMO_2KG, item_group_id=EZOSHIKA_MOMO, size=2kg
商品B: id=EZOSHIKA_MOMO_500G, item_group_id=EZOSHIKA_MOMO, size=500g
→ Instagram上で「サイズを選択」として表示される
```

### 商品属性

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 16 | **gender** | 対象性別<br>※食品では通常不要 | 空欄 |
| 19 | **age_group** | 対象年齢層<br>※食品では通常不要 | 空欄（またはadult） |
| 20 | **material** | 素材<br>200文字以内 | 食品には不適切、空欄でOK |
| 21 | **pattern** | 模様・柄<br>100文字以内 | 食品には不適切、空欄でOK |

---

## 🟢 あれば便利な任意項目（優先度中）

### 配送・重量

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 22 | **shipping** | 配送料金<br>フォーマット：国:地域:方法:料金 | `JP::Ferry:1500 JPY`<br>`JP:Kanto:Ground:1800 JPY;JP:Kansai:Ferry:1500 JPY`<br>※複数地域はセミコロン区切り |
| 23 | **shipping_weight** | 配送重量<br>単位必須(kg/g/lb/oz) | `2 kg`<br>`500 g` |

**EEZOの配送料設定例**
```
フェリー航路沿い（小樽・舞鶴・新潟）:
JP:Hokkaido:Ferry:1200 JPY;JP:Kansai:Ferry:1500 JPY;JP:Niigata:Ferry:1300 JPY

それ以外:
JP::Ground:1800 JPY
```

### 動画・メディア

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 24 | **video[0].url** | 商品動画URL<br>直接動画ファイルのURL | `https://eezo.jp/videos/ezoshika_cooking.mp4`<br>※YouTubeリンク不可、直接ファイル必須 |
| 25 | **video[0].tag[0]** | 動画タグ | `調理方法`<br>`下処理`<br>`ジビエ` |

### 識別コード・タグ

| 列番号 | 項目名 | 説明 | EEZO記入例 |
|--------|--------|------|------------|
| 26 | **gtin** | 国際取引商品番号<br>バーコード番号<br>※食品で持っている場合のみ | `4901234567890` (13桁JANコード)<br>なければ空欄 |
| 27-28 | **product_tags[0]**<br>**product_tags[1]** | 商品タグ<br>110文字/タグ<br>最大5000タグ<br>※フィルタリング用 | `北海道産`<br>`業務用`<br>`真空パック`<br>`ジビエ`<br>`低脂肪` |
| 29 | **style[0]** | スタイル<br>※食品では不要 | 空欄 |

---

## 🎯 EEZO商品別 入力見本

### 見本1: エゾシカもも肉 2kg

```csv
id,title,description,availability,condition,price,link,image_link,brand,google_product_category,fb_product_category,quantity_to_sell_on_facebook,sale_price,sale_price_effective_date,item_group_id,gender,color,size,age_group,material,pattern,shipping,shipping_weight,video[0].url,video[0].tag[0],gtin,product_tags[0],product_tags[1],style[0]
EZOSHIKA_MOMO_2KG,【北海道産】エゾシカもも肉 2kg 真空パック 業務用,北海道の大自然で育ったエゾシカのもも肉です。低脂肪・高たんぱくで健康志向の方におすすめ。脂肪含有率2%、鉄分は牛肉の3倍。真空パックで鮮度を保ち、フェリー輸送でお届けします。推奨調理法：55℃30分の低温調理でロゼに仕上げ、赤ワインソースと合わせてください。楽水山・オーセントホテル小樽でも採用されています。,in stock,new,5000 JPY,https://eezo.jp/ezoshika-momo-2kg,https://eezo.jp/images/ezoshika_momo_2kg.jpg,EEZO,Food Beverages & Tobacco > Food Items > Meat & Seafood,Food & Grocery,,,,,,,2kg,,,,,2 kg,,,北海道産,ジビエ,
```

### 見本2: 熊本あか牛サーロイン 300g

```csv
AKAGYU_SIROIN_300G,熊本あか牛 サーロイン 300g A4等級 国産和牛,阿蘇の大自然で育った熊本あか牛のサーロインです。低カロリー・高たんぱくで、健康志向のお客様に人気の赤身和牛。A4等級の高品質で、柔らかくジューシーな味わい。真空パックでお届けします。,in stock,new,8500 JPY,https://eezo.jp/akagyu-siroin-300g,https://eezo.jp/images/akagyu_siroin.jpg,GOODGOOD農場,Food Beverages & Tobacco > Food Items > Meat & Seafood,Food & Grocery,,,AKAGYU_SIROIN,,,300g,,,JP:Kansai:Ferry:1500 JPY,300 g,,,熊本産,和牛,
```

### 見本3: 活毛ガニ 500g

```csv
KEGANI_500G,【北海道産】活毛ガニ 500g 産地直送,北海道近海で獲れた新鮮な活毛ガニです。身入りが良く、濃厚なカニ味噌が自慢。現代の北前船のフェリー輸送で鮮度を保ったままお届けします。到着後すぐに茹でてお召し上がりください。,in stock,new,4500 JPY,https://eezo.jp/kegani-500g,https://eezo.jp/images/kegani_live.jpg,EEZO,Food Beverages & Tobacco > Food Items > Meat & Seafood,Food & Grocery,,,,,,500g,,,JP::Ferry:2000 JPY,500 g,,,北海道産,海鮮,
```

### 見本4: 大七 純米生酛 720ml

```csv
DAISHICHI_KIMOTO_720,大七酒造 純米生酛 720ml 福島県,350年の伝統を誇る大七酒造の代表銘柄。生酛造りによる深い味わいと、なめらかな口当たりが特徴。常温からぬる燗まで幅広く楽しめます。海外輸出実績も豊富な日本酒です。,in stock,new,2800 JPY,https://eezo.jp/daishichi-kimoto-720,https://eezo.jp/images/daishichi_720.jpg,大七酒造,Food Beverages & Tobacco > Beverages > Alcoholic Beverages,Alcoholic Beverages,,,,,,720ml,,,JP::Ground:1200 JPY,1.5 kg,,,福島県,日本酒,
```

---

## 📊 CS-Cartからのデータ変換マッピング

### CS-Cartフィールド → Metaフィールド対応表

| CS-Cart項目 | Meta項目 | 変換ルール |
|-------------|----------|-----------|
| Product Code (商品コード) | id | そのまま使用（英数字のみ推奨） |
| Product Name (商品名) | title | そのまま使用（200文字以内に調整） |
| Full Description (詳細説明) | description | HTMLタグを除去してプレーンテキストに |
| In Stock (在庫数) | availability | 1以上→`in stock`、0→`out of stock` |
| Price (価格) | price | 数字 + ` JPY` を追加 |
| Product URL | link | 完全なURL（https://含む） |
| Main Image URL | image_link | 完全なURL（https://含む） |
| Brand/Manufacturer | brand | メーカー名またはEEZO |
| Weight (重量) | shipping_weight | 数字 + ` kg` または ` g` |

### CS-Cartエクスポート→Meta変換の手順

```
【ステップ1】CS-Cartから商品データをエクスポート
- 管理画面 → 商品 → エクスポート
- CSV形式でダウンロード

【ステップ2】Excelで変換作業
1. CS-CartのCSVを開く
2. Metaテンプレートを別シートで開く
3. 対応表に従ってVLOOKUPまたは手作業でマッピング
4. 必須9項目を最優先で埋める
5. 任意項目は段階的に追加

【ステップ3】データクリーニング
- HTMLタグの除去（description）
- 価格形式の統一（5000円→5000 JPY）
- 在庫状況の変換（数字→in stock/out of stock）
- URL の完全形式確認（https://から始まる）
- 画像URLの確認（500x500px以上）

【ステップ4】アップロード
- コマースマネージャーでCSVアップロード
- エラーチェック
- 問題があれば修正して再アップロード
```

---

## ⚠️ よくあるエラーと対処法

### エラー1: 「Invalid price format」
```
原因: 価格フォーマットが間違っている
NG例: 5,000円、¥5000、5000
OK例: 5000 JPY、5000.00 JPY
```

### エラー2: 「Image URL not accessible」
```
原因: 画像URLにアクセスできない
確認:
- URLが正しいか（https://で始まる）
- 画像が実際にアップロードされているか
- 画像サイズが500x500px以上か
- ファイル形式がJPG/PNG/GIFか
```

### エラー3: 「Missing required field」
```
原因: 必須項目が空欄
対処: 9つの必須項目すべてに値を入力
特にbrandとconditionを忘れがち
```

### エラー4: 「Duplicate ID」
```
原因: idが重複している
対処: 各商品のidは必ずユニークに
CS-Cartの商品コードをそのまま使えばOK
```

---

## 🚀 実装ステップ

### Phase 1: テスト商品（今日）
```
□ 代表商品5点を手作業で入力
  - エゾシカもも肉
  - あか牛サーロイン
  - 活毛ガニ
  - アスパラガス
  - 日本酒（大七）
□ 必須9項目のみ入力
□ コマースマネージャーにアップロード
□ エラーがないか確認
```

### Phase 2: 全商品データ準備（今週）
```
□ CS-Cartから商品データをエクスポート
□ Excelで変換シート作成
□ 必須9項目をマッピング
□ データクリーニング
□ 50商品程度でテストアップロード
```

### Phase 3: 全商品アップロード（来週）
```
□ 残り450商品をアップロード
□ 任意項目の追加（カテゴリ、タグ等）
□ 画像の最適化
□ エラー修正
```

### Phase 4: 自動化検討（1ヶ月後）
```
□ Pintaアドオン等で自動フィード生成
□ 毎日自動同期の設定
□ 在庫・価格の自動更新
```

---

## 💡 EEZOならではの注意点

### 1. ブランド戦略
```
推奨: brandは「EEZO」で統一
理由:
- ブランド認知の統一
- 検索結果での一貫性
- 生産者名は description に記載
```

### 2. 価格表示
```
注意: Instagram上の価格は参考価格
- 実際の購入はCS-Cartサイトへ遷移
- サイト側の価格と必ず一致させる
- セール時は両方で更新
```

### 3. 在庫管理
```
課題: Metaカタログ ⇔ CS-Cart の在庫同期
短期: 手動更新（週1回）
中期: データフィード定期更新（毎日）
長期: API連携で完全自動化
```

### 4. 501商品の優先順位
```
優先度A（先にアップロード）:
- 看板商品（エゾシカ、あか牛、カニ、ウニ）
- 高単価商品（利益率高い）
- Instagram映えする商品

優先度B（Phase2で追加）:
- 定番商品
- 通年販売商品

優先度C（Phase3で追加）:
- 季節限定商品
- 在庫不安定商品
```

---

**次のステップ**: まず5商品を手動入力して、フォーマットに慣れましょう！

**作成者**: ミナト  
**更新日**: 2025年11月10日
