# Claude Code on the Web 活用ガイド v2.0

## 概要

本ガイドは、ブラウザベースの「Claude Code on the Web」を最大限活用するための手順書です。Anthropicハッカソン優勝者の設定テンプレート「everything-claude-code」から**Web版でも応用可能な概念**を抽出し、EDA（探索的データ分析）やその他の開発タスクを効率化します。

**参考資料**:
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code) - Anthropicハッカソン優勝者のテンプレート集
- [公式ドキュメント](https://code.claude.com/docs/ja/claude-code-on-the-web)

---

## CLI版 vs Web版：機能対応表

| 機能 | CLI版 | Web版 | 備考 |
|------|-------|-------|------|
| CLAUDE.md | ✅ | ✅ | 完全対応 |
| Hooks (SessionStart) | ✅ | ✅ | 完全対応 |
| Agents | ✅ | ⚠️ | 手動で文脈切り替え |
| Commands (/tdd等) | ✅ | ⚠️ | CLAUDE.mdに記載して参照 |
| Contexts (dev/research) | ✅ | ⚠️ | CLAUDE.mdで切り替え |
| MCP Servers | ✅ | 🔒 | 自動接続のみ（設定不可） |
| Plugins | ✅ | ❌ | 非対応 |

**凡例**: ✅完全対応 ⚠️工夫で代替可能 🔒制限あり ❌非対応

---

## 前提条件

| 項目 | 要件 |
|------|------|
| Claudeプラン | Pro または Max |
| GitHub | アカウント必須、プライベートリポジトリ作成可能 |
| ローカルPC | gitインストール済み |
| データ | GitHubリポジトリに配置可能なもの（100MB/ファイル以下） |

---

## プロジェクト構成：推奨ディレクトリ

CLI版のベストプラクティスをWeb版向けにカスタマイズ：

```
project-name/
├── CLAUDE.md                    # プロジェクト指示書（最重要）
├── README.md                    # プロジェクト概要
├── requirements.txt             # Python依存パッケージ
│
├── .claude/
│   ├── settings.json            # フック設定
│   └── contexts/                # コンテキストモード定義（Web版独自）
│       ├── dev.md               # 開発モード
│       ├── research.md          # 調査モード
│       └── review.md            # レビューモード
│
├── rules/                       # モジュール化されたルール
│   ├── security.md              # セキュリティチェック
│   ├── coding-style.md          # コーディング規約
│   └── testing.md               # テスト方針
│
├── skills/                      # ドメイン知識・ワークフロー定義
│   ├── eda-workflow.md          # EDA標準フロー
│   ├── domain-knowledge.md      # 業界知識
│   └── patterns.md              # 実装パターン
│
├── data/
│   ├── raw/                     # 元データ（編集禁止）
│   └── processed/               # 加工済みデータ
│
├── experiments/                 # 1実験1ディレクトリ
│   └── exp001_baseline/
│       ├── main.py
│       ├── outputs/
│       └── log.md               # 実験ログ
│
├── src/                         # 共通コード
│   ├── data/
│   ├── features/
│   ├── visualization/
│   └── utils/
│
└── outputs/                     # 最終成果物
    ├── reports/
    └── figures/
```

---

## CLAUDE.md 強化版テンプレート

CLI版の `user-CLAUDE.md` と `project-CLAUDE.md` の知見を統合：

```markdown
# CLAUDE.md

## プロジェクト概要
- **目的**: [分析の目的を記載]
- **データ**: [データの概要]
- **評価指標**: [成功の定義]

---

## Core Philosophy（基本原則）

### 1. Plan Before Execute（計画先行）
複雑な作業は計画から始める。いきなりコードを書かない。

### 2. Test-Driven（テスト駆動）
可能な限り、テストを先に書く。

### 3. Security-First（セキュリティ優先）
ハードコードされたシークレット禁止。入力バリデーション必須。

### 4. Many Small Files（ファイル分割）
大きなファイルより、小さなファイル複数を優先。

### 5. Immutability（不変性）
data/raw/ のデータは絶対に変更しない。

---

## Critical Rules（絶対ルール）

コミット前の必須チェック:
- [ ] ハードコードされたシークレット（APIキー、パスワード）がないこと
- [ ] すべてのユーザー入力がバリデーションされていること
- [ ] data/raw/ 配下のファイルを編集していないこと
- [ ] 型ヒントとdocstringが記載されていること

---

## データセット情報

### 学習データ (data/raw/train.csv)
| カラム名 | 型 | 説明 | 備考 |
|----------|-----|------|------|
| id | int | 一意識別子 | |
| feature_1 | float | 特徴量1 | 欠損あり |
| target | int | 目的変数 | 0/1の二値 |

### テストデータ (data/raw/test.csv)
[同様に記載]

---

## Available Commands（利用可能なコマンド）

※ Web版ではスラッシュコマンドは使えないため、以下のキーワードで呼び出し

| キーワード | 内容 | 使い方 |
|-----------|------|--------|
| `EDAを実行` | 標準EDAワークフロー実行 | 「data/raw/xxx.csv のEDAを実行して」 |
| `計画を作成` | 実装計画書の作成 | 「○○の計画を作成して」 |
| `レビューして` | コード品質チェック | 「src/xxx.py をレビューして」 |
| `テストを書いて` | TDDワークフロー | 「○○のテストを書いて」 |
| `リファクタして` | コード改善 | 「src/xxx.py をリファクタして」 |

---

## Context Modes（コンテキストモード）

### 開発モード（デフォルト）
```
「開発モードで進めて」
```
- コード優先、動くものを素早く作る
- 完璧より進捗を重視

### 調査モード
```
「調査モードで進めて」
```
- 理解優先、コードを書く前に徹底調査
- 既存コードとドキュメントを精読してから行動

### レビューモード
```
「レビューモードで進めて」
```
- 品質チェック重視
- セキュリティ、パフォーマンス、可読性を厳しくチェック

---

## 技術スタック

- Python 3.x（環境にプリインストール済み）
- pandas, numpy, matplotlib, seaborn（要インストール）
- scikit-learn（要インストール）

---

## ディレクトリルール

1. **data/raw/** - 元データ格納、**絶対に編集しない**
2. **data/processed/** - 加工済みデータ
3. **experiments/expXXX_[説明]/** - 各実験は独立ディレクトリ
4. **outputs/** - 最終成果物

---

## コーディング規約

- 型ヒント必須
- docstring必須（Google形式）
- インデント: スペース4つ
- f-string優先
- print文でなくlogger使用

---

## EDA標準フロー（skills/eda-workflow.md を参照）

1. データ読み込み・基本統計量確認
2. 欠損値・異常値の確認
3. 目的変数の分布確認
4. 特徴量ごとの分布・目的変数との関係
5. 特徴量間の相関分析
6. 結果をMarkdownレポートにまとめる

---

## ドメイン知識

[プロジェクト固有の業界知識をここに記載]
```

---

## モジュール化されたルール管理

CLI版の `rules/` ディレクトリ概念をWeb版でも活用：

### rules/security.md
```markdown
# Security Rules

## コミット前チェック

- [ ] ハードコードされたシークレットがない
  - APIキー、パスワード、トークン
- [ ] すべてのユーザー入力がバリデーションされている
- [ ] SQLインジェクション対策（パラメータ化クエリ）
- [ ] XSS対策（HTMLサニタイズ）

## 禁止事項

- .env ファイルのコミット
- 平文でのパスワード保存
- eval() の使用
```

### rules/coding-style.md
```markdown
# Coding Style Rules

## Python

- 型ヒント必須
- docstring必須（Google形式）
- インデント: スペース4つ
- 1関数80行以下
- 1ファイル500行以下

## 命名規則

- 変数/関数: snake_case
- クラス: PascalCase
- 定数: UPPER_SNAKE_CASE

## インポート順序

1. 標準ライブラリ
2. サードパーティ
3. ローカルモジュール
```

### rules/testing.md
```markdown
# Testing Rules

## TDDワークフロー

1. **RED** - 失敗するテストを先に書く
2. **GREEN** - テストを通す最小限のコードを実装
3. **REFACTOR** - テストを維持しながらコード改善

## カバレッジ要件

- 新規コード: 80%以上
- 重要ロジック: 90%以上

## テストファイル命名

- test_[モジュール名].py
- tests/unit/
- tests/integration/
```

---

## Skills（スキル）：ワークフロー定義

### skills/eda-workflow.md
```markdown
# EDA Workflow Skill

## 標準フロー

### Step 1: データ読み込み・基本統計量
```python
df = pd.read_csv('data/raw/xxx.csv')
print(df.shape)
print(df.dtypes)
print(df.describe())
```

### Step 2: 欠損値確認
```python
print(df.isnull().sum())
print(df.isnull().sum() / len(df) * 100)  # 欠損率
```

### Step 3: 目的変数分布
```python
df['target'].value_counts(normalize=True)
```

### Step 4: 特徴量探索
数値型: ヒストグラム
カテゴリ型: カーディナリティ、クロス集計

### Step 5: 相関分析
```python
corr_matrix = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr_matrix, annot=True)
```

### Step 6: レポート作成
Markdownで experiments/expXXX/outputs/eda_report.md に出力

## 出力物

- experiments/expXXX/outputs/eda_report.md
- experiments/expXXX/outputs/figures/*.png
```

### skills/domain-knowledge.md（例：北海道食材商社）
```markdown
# Domain Knowledge - 北海道食材商社

## 商品カテゴリ
- 水産物: カニ、ウニ、サケ、タコ（主力）
- 畜産物: エゾシカ、あか牛（高単価）
- 農産物: じゃがいも、ゆり根、アスパラ、メロン
- 酒類: 日本酒、焼酎、ワイン

## 販売チャネル
- toB（法人）: ホテル・外食・小売 → 高単価、安定
- toC（個人）: EEZO EC → 注文数多いが単価低い

## 季節性
- 12月: 年末需要でピーク
- 8月: お中元需要
- 4月: 年度切替で法人需要減

## 重要KPI
- 粗利率: 目標30%以上
- リピート率: toB顧客の継続取引
- CAC: 顧客獲得コスト
```

---

## フック設定（.claude/settings.json）

### 基本設定：依存関係の自動インストール
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "pip install pandas numpy matplotlib seaborn scikit-learn openpyxl japanize-matplotlib"
          }
        ]
      }
    ]
  }
}
```

### 拡張設定：TypeScriptプロジェクト向け
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "npm install"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\.(ts|tsx)$\"",
        "description": "TypeScriptファイル編集後に型チェック",
        "hooks": [
          {
            "type": "command",
            "command": "npx tsc --noEmit --pretty false 2>&1 | head -20"
          }
        ]
      }
    ]
  }
}
```

### リモート環境限定実行（推奨）

scripts/setup.sh:
```bash
#!/bin/bash

# リモート環境（Claude Code）でのみ実行
if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  exit 0
fi

# Python環境セットアップ
pip install -r requirements.txt

# 日本語フォント設定（matplotlibで必要な場合）
pip install japanize-matplotlib

exit 0
```

.claude/settings.json:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "bash scripts/setup.sh"
          }
        ]
      }
    ]
  }
}
```

---

## 実践的な使い方

### 1. セッション開始時

```
プロジェクトの構造を確認して、CLAUDE.md と rules/ 配下のルールを読んで
```

### 2. EDA実行

```
data/raw/sales.csv のEDAを実行して。skills/eda-workflow.md のフローに従って
```

### 3. コンテキストモード切り替え

```
調査モードで進めて。既存のsrc/以下のコードを精読してから、新機能の設計を考えて
```

### 4. コードレビュー

```
レビューモードで src/features/create_features.py をレビューして。
rules/security.md と rules/coding-style.md のルールに従って
```

### 5. 計画作成

```
新機能「顧客セグメント分析」の実装計画を作成して。
1. 要件分析
2. 設計
3. 実装ステップ
4. テスト計画
を含めて
```

---

## コンテキスト管理のベストプラクティス

CLI版から学ぶ、Web版でのコンテキスト節約術：

### 1. 参照ファイルを明示する
```
❌ 悪い例: 「コードをレビューして」
✅ 良い例: 「src/features/create_features.py をレビューして」
```

### 2. 不要な情報を読み込まない
```
❌ 悪い例: 「プロジェクト全体を確認して」
✅ 良い例: 「src/data/以下のファイル一覧を見せて」
```

### 3. 段階的に進める
```
❌ 悪い例: 「全部やって」
✅ 良い例: 「まずStep 1のデータ読み込みと基本統計量を確認して」
```

### 4. 結果を保存してから次へ
```
「現在の分析結果を experiments/exp001_baseline/outputs/step1.md に保存して」
「次に Step 2 の欠損値分析に進んで」
```

---

## 新日本海商事での活用例

### 例1: 販売データEDA

CLAUDE.md に追記:
```markdown
## ドメイン知識
- 商品カテゴリ: 水産物（カニ、ウニ、サケ）、畜産物（エゾシカ）、農産物
- 販売チャネル: toB（ホテル・外食・小売）、toC（EEZO EC）
- 季節性: 年末年始、お中元時期に需要増
```

指示例:
```
data/raw/sales_2024.csv のEDAを実行して。
skills/eda-workflow.md のフローに従い、特にドメイン知識を踏まえて
- 商品カテゴリ別の売上推移
- 顧客セグメント別の購買傾向
- 季節性の分析
を重点的に
```

### 例2: 展示会リード分析

```
展示会で獲得した111件のリードデータを分析して。
- リードスコアの分布
- 業種・地域別の傾向
- 成約確度の予測に使えそうな特徴量
を特定して
```

---

## トラブルシューティング

### Q: CLAUDE.md が読み込まれていない気がする

確認方法:
```
CLAUDE.md の内容を要約して
```
正しく読み込まれていれば、記載した内容が要約されます。

### Q: フック設定が効かない

確認事項:
1. `.claude/settings.json` のJSONが正しい形式か
2. `matcher` の値が正しいか（SessionStartは `"startup"`）
3. シェルスクリプトに実行権限があるか（`chmod +x scripts/setup.sh`）

### Q: 大きなファイルがプッシュできない

対処:
- 100MB以下に分割
- Git LFS の利用を検討
- サンプルデータで分析

### Q: 日本語が文字化けする

対処:
```python
pip install japanize-matplotlib
import japanize_matplotlib
```

---

## まとめ：Web版で使えるCLI版の知見

| CLI版の概念 | Web版での実現方法 |
|------------|-----------------|
| CLAUDE.md | そのまま使用可能 |
| rules/ | ディレクトリ作成してCLAUDE.mdから参照 |
| skills/ | ディレクトリ作成してCLAUDE.mdから参照 |
| contexts/ | CLAUDE.mdに記載、指示で切り替え |
| Hooks | .claude/settings.json で設定 |
| Agents | 手動で「○○モードで」と切り替え |
| Commands | 「○○を実行して」とキーワードで呼び出し |

**核心的な学び**:
1. **CLAUDE.mdに文脈を書いておく** → 毎回の説明が不要
2. **ルールとスキルをモジュール化** → 再利用性向上
3. **コンテキストモードで切り替え** → 状況に応じた振る舞い
4. **フックで自動化** → 環境セットアップを省略

---

## 参考リンク

- [everything-claude-code](https://github.com/affaan-m/everything-claude-code) - Anthropicハッカソン優勝者のテンプレート
- [Claude Code on the Web 公式ドキュメント](https://code.claude.com/docs/ja/claude-code-on-the-web)
- [Claude Code フック設定](https://code.claude.com/docs/ja/hooks)

---

*作成日: 2025-12-29*
*更新日: 2026-01-23（v2.0 - CLI版知見統合）*
*対象: Claude Code on the Web（リサーチプレビュー）*
*新日本海商事 データ分析業務効率化プロジェクト用*
