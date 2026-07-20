# EEZOS 引き算プロンプト設計書 v4

**作成日**: 2026年2月26日
**更新**: v3の「石の彫刻」路線から「紋章型」への構造転換
**ツール**: Google Gemini
**用途**: 2/27堀田MTG用の仮絵生成

---

## v3→v4 構造転換の経緯

### v3までの問題

v1-v3は「ええぞすは何でできているか」（石？陶器？ブロンズ？）を追いかけていた。しかし:

1. **設計判断が「紋章型」なのに、3D構造物を作ろうとしていた矛盾**。グレンフィディックの鹿紋は「何の素材か」ではなく「色面の構成」で成立している
2. **堀田さんのカラーパレットとズレていた**。原案ではDeep Navy / Blue Gray / Goldの3色体系。v3のcool gray（weathered stone）はこのパレットの外にある
3. **堀田さんの紋章アート**（ネイビー地にゴールドライン）が示していたのは、物質感ではなくグラフィックとしての存在

### 転換の核心

**ええぞすは物質ではない。色面の構成として存在するエンブレム**。

ユーザーの直感: 「実体化する前のジャーヴィス」。情報と意思の集積が形を取りかけているが、まだ物質ではない。裏設定の「願いの集積体」と整合する。

### v4の設計方針

- Blue grayの雫型シルエット（目と手つき）が、Deep navyのローブを纏っている
- 全体として見ると「エンブレムのようだが、目と手があるので存在感がある」
- 石・陶器・ブロンズ等の物質的記述を全廃
- 質感ではなく**色の関係性**で成立させる
- 堀田さんのカラーパレットと完全整合

---

## v4 Layer 1: 紋章型ええぞす

### Positive

```
A single front-facing character on a pure white background. Completely still.

This is a teardrop-shaped spirit wearing a robe. It looks like a heraldic emblem that has gentle presence — NOT a 3D object, NOT a stone sculpture, NOT a plush toy.

THE SPIRIT: A smooth teardrop silhouette in flat blue-gray. The entire form is one uniform blue-gray tone — like the shadow color of a luxury navy brand. The face is simply two tiny dark navy dots for eyes placed on the upper portion. No mouth. The eyes are very small, approximately 1/20th of the width. No eye highlights, no reflections. The expression is unreadable but calm. The shape narrows gently toward a rounded top — NOT sharply pointed, but softly tapered.

THE ROBE: A deep navy hoodless robe draped over the lower two-thirds, as if the spirit is wearing it. Shallow V-neck. The robe follows the silhouette without creating shoulders. No legs visible below. Small abstract ellipsoid hands in the same blue-gray peek out slightly from the sleeve openings. One small antique gold compass emblem on the upper left chest, like a lapel pin. This is the ONLY gold element.

SILHOUETTE: Continuous teardrop form. Softly tapered at the top, gently widening toward the bottom. No neck. No shoulders. No waist. Head-to-robe ratio approximately 1:2.5. Width-to-height approximately 1:1.8. The character floats a few centimeters above the ground with a soft shadow below.

COLOR PALETTE — STRICT:
- Spirit body: blue-gray (muted, desaturated blue-gray)
- Robe: deep navy (darker than the body)
- Compass emblem: antique gold (the ONLY warm color)
- Background: pure white

FEELING: An emblem given quiet life. A brand symbol that breathes. The stillness of a crest on a coat of arms, but with the faintest sense that something ancient and wise lives within.

Style: Flat 2D illustration. Minimal shading. Clean edges. Matte throughout. NO texture, NO stone grain, NO fabric weave visible. Color and shape only.
```

### Negative

```
3D render, realistic, photograph, oil painting. Stone, granite, ceramic, bronze, metal, clay, rubber, plastic. Visible texture, fabric texture, stone grain, surface roughness. Shoulders, neck, collarbone, human silhouette, human proportions. Head separate from body. Cute, kawaii, chibi, baby proportions, plush toy, stuffed animal. Ghost, monster, Kaonashi, grim reaper, skeleton, hooded figure. Golem, robot, humanoid, action figure. Legs, feet, shoes, visible fingers. Eye highlights, eye shine, sparkle, expressive eyes, large eyes. White face, pale face different from body color, mask. Open mouth, teeth, smile. Glow, light effects, aura, bloom, neon, emissive. Pattern, decoration, embroidery, ornate trim. Hood, cowl. Sharply pointed top. Dramatic lighting, heavy shadow, strong contrast. Tribal, runes, markings. Large centered emblem.
```

---

## v4 Layer 2: 金継ぎ光の再検討

### 金継ぎ光の方向性転換

v3までは「石の継ぎ目から光が漏れる」エミッシブ表現を検討していた。v4では物質感を廃止したため、光の意味も変わる。

**新しい解釈**: ローブと精霊の境界（V-neck縁、裾、袖口）に走るゴールドのライン。「光が漏れている」のではなく、堀田さんの紋章アートと同様に「刻まれた金の線」。紋章の縁取りのように、2つの色面の境界を金で区切る。

### Layer 2 Positive（Layer 1に追加する差分）

THE ROBEの記述を以下に差し替え:

```
THE ROBE: A deep navy hoodless robe draped over the lower two-thirds, as if the spirit is wearing it. Shallow V-neck. The robe follows the silhouette without creating shoulders. No legs visible below. Small abstract ellipsoid hands in the same blue-gray peek out slightly from the sleeve openings. One small antique gold compass emblem on the upper left chest, like a lapel pin. A thin antique gold line — like gold leaf applied to the edge — traces where the robe meets the spirit: along the V-neck edge, the hem, and the sleeve openings. These gold lines are flat and graphic, NOT glowing, NOT emissive. They are decorative borders, like on a heraldic crest.
```

### 見るべきポイント

- ゴールドラインが「光っている」ではなく「描かれている」に見えるか
- 紋章的な格が上がるか、それとも装飾過多になるか
- Layer 1（コンパスのみ）と比較して、どちらが堀田さんの "Silence creates authority. One emblem tells the whole story." に合致するか

---

## 堀田原案との照合結果

### 整合している点

| 堀田原案の記述 | v4での対応 |
|--------------|-----------|
| 「かわいさ」を排し「信頼・格式・品格」を最優先 | 紋章型の設計思想 |
| 点の目（顔幅1/20、ハイライトなし） | 同一 |
| 口は原則なし | 同一 |
| 足無し（浮遊型）構造 | 同一 |
| 重心をやや下寄りに | 下部が広がるteardrop型で実現 |
| 指のない楕円体の手、袖口から少しだけ | 同一 |
| フード無しロングローブ、浅いV字襟 | 同一 |
| 装飾ゼロ、コンパス紋章のみ | 同一 |
| Deep Navy / Blue Gray / Gold の3色 | **v4で完全整合**（v3まではcool grayでズレていた） |
| 完全マット、テクスチャ禁止 | **v4でフラット化により解決**（v3は石の質感でズレていた） |

### 明日確認が必要な点

| 論点 | 堀田原案 | v4の現状 | 確認事項 |
|------|---------|---------|---------|
| 頭頂の形状 | 「上が細く」= やや尖る雫型 | 「softly tapered」= やや絞るが丸い | どこまで絞るか。尖りすぎるとお化け化する経緯を説明の上で合意 |
| 直線と曲線の比率 | 直6：曲4 | 現状は曲線寄り | 堀田さんの意図する「直線」がどこに入るか |
| テクスチャ禁止の範囲 | 3D制作指示として記述 | v4は2Dフラットで対応 | 2Dでも質感表現は不可か、それともフラットでOKか |
| 金継ぎ的ゴールドライン | 紋章アートにはある、ローブ仕様には「装飾ゼロ」 | Layer 2で検証可能 | 堀田さんの紋章アートのラインをキャラクターにも適用してよいか |

---

## 確立済みの不変要素（v4時点）

| 要素 | 確定値 | 経緯 |
|------|--------|------|
| 形状語 | **teardrop（softly tapered）** | bell→丸すぎ。teardrop→尖る。中間の「softly tapered teardrop」で両立 |
| **体色** | **Blue gray** | **v4で変更。堀田パレット準拠。物質の色ではなくブランドカラー** |
| **ローブ色** | **Deep navy** | **v4で明示。堀田パレット準拠** |
| **アクセント** | **Antique gold（コンパスのみ）** | **v4で明示。堀田パレット準拠** |
| **質感** | **フラット・テクスチャなし** | **v4で変更。石・陶器等の物質感を全廃** |
| 顔と体の色差 | なし（統一） | v2で確定 |
| 肩 | なし（明示禁止） | v2で確定 |
| 脚 | なし | 初期から不変 |
| 指 | なし（楕円手） | 初期から不変 |
| 目のサイズ | 幅の1/20 | 初期から不変 |
| 目のハイライト | なし | 初期から不変 |
| 口 | なし | 初期から不変 |
| 頭身比 | 1:2.5 | v3で確定 |
| 幅高比 | 1:1.8 | 初期から不変 |

---

## 試行の全経緯（v1→v4）

```
v1 Layer 1: 3素材テスト（暗い体＋白い顔＋ネイビーローブ）
  → 肩＋白い顔 = 人体構造＋仮面感 → NG

v2 Layer 1-R: 雫型精霊（teardrop、色統一）
  → 頭頂が尖る＋ずんぐりkawaii → 部分NG

v3 Layer 1-R: bell型（丸い頭頂、クールグレー、石質感）
  → 構造は成立。石質感も出た。コンパス追加もOK
  → だが「石の彫刻」= 3D構造物を作ろうとしていた

v4: 紋章型への転換
  → 物質感を全廃。Blue gray + Deep navy + Gold
  → 堀田パレット完全準拠。「エンブレムに命が宿った」存在
  → 堀田原案との照合で整合性を確認
  → ★現在ここ。Gemini出力の検証待ち
```

---

## 堀田MTGでの見せ方（v4更新）

### ストーリーライン

1. **v1-v3の試行経緯**: 素材感を追いかけた結果、石の彫刻＝3D構造物になっていた
2. **転換点**: 堀田さんの紋章アートとカラーパレットを照合し、「物質ではなく色面の構成」に気づいた
3. **v4の方向性**: Blue gray + Deep navy + Gold。エンブレムに命が宿った存在
4. **堀田原案との整合**: カラーパレット・テクスチャ禁止・装飾ゼロすべて準拠
5. **確認事項**: 頭頂の絞り具合、直6：曲4の解釈、ゴールドラインの適用範囲

---

*作成: ミナト*
*v1→v2→v3→v4の試行結果と堀田原案照合を統合*
