<!-- i18n-source: resources/README.md -->
<!-- i18n-source-sha: 20779db -->
<!-- i18n-date: 2026-04-27 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Claude How To — ブランドアセット

Claude How To プロジェクトのロゴ・アイコン・favicon の完全コレクション。すべて V3.0 デザインを使用：コードブラケット（`>`）付きコンパスシンボルで、コードを進む案内付きナビゲーションを表現する。ブラック／ホワイト／グレーのパレットにブライトグリーン（#22C55E）のアクセントを加えている。

## ディレクトリ構造

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # Main logo - Light mode (520×120px)
│   └── claude-howto-logo-dark.svg  # Main logo - Dark mode (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # App icon - Light mode (256×256px)
│   └── claude-howto-icon-dark.svg  # App icon - Dark mode (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px (primary)
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 内の追加アセット：
```
assets/logo/
├── logo-full.svg       # Mark + wordmark (horizontal)
├── logo-mark.svg       # Compass symbol only (120×120px)
├── logo-wordmark.svg   # Text only
├── logo-icon.svg       # App icon (512×512, rounded)
├── favicon.svg         # 16×16 optimized
├── logo-white.svg      # White version for dark backgrounds
└── logo-black.svg      # Black monochrome version
```

## アセット概要

### デザインコンセプト（V3.0）

**コードブラケット付きコンパス** — ガイダンスとコードの融合：
- **コンパスリング** ＝ ナビゲーション、進路を見つける
- **北針（グリーン）** ＝ 方向、学習経路の進捗
- **南針（ブラック）** ＝ 基盤、揺るぎない土台
- **`>` ブラケット** ＝ ターミナルプロンプト、コード、CLI コンテキスト
- **目盛り** ＝ 精度、体系的な学習

### ロゴ

**ファイル**:
- `logos/claude-howto-logo.svg`（ライトモード）
- `logos/claude-howto-logo-dark.svg`（ダークモード）

**仕様**:
- **サイズ**: 520×120 px
- **用途**: ワードマーク付きのメインヘッダー／ブランディングロゴ
- **使用箇所**:
  - Web サイトのヘッダー
  - README バッジ
  - マーケティング素材
  - 印刷物
- **形式**: SVG（完全にスケーラブル）
- **モード**: ライト（白背景）とダーク（#0A0A0A 背景）

### アイコン

**ファイル**:
- `icons/claude-howto-icon.svg`（ライトモード）
- `icons/claude-howto-icon-dark.svg`（ダークモード）

**仕様**:
- **サイズ**: 256×256 px
- **用途**: アプリケーションアイコン、アバター、サムネイル
- **使用箇所**:
  - アプリアイコン
  - プロフィールアバター
  - ソーシャルメディアサムネイル
  - ドキュメントヘッダー
- **形式**: SVG（完全にスケーラブル）
- **モード**: ライト（白背景）とダーク（#0A0A0A 背景）

**デザイン要素**:
- 主要方位および中間方位の目盛り付きコンパスリング
- 緑の北針（方向／ガイダンス）
- 黒の南針（基盤）
- 中央の `>` コードブラケット（ターミナル／CLI）
- 緑の中央ドットアクセント

### Favicon

Web 利用向けに複数サイズで最適化されたバージョン：

| ファイル | サイズ | DPI | 用途 |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | ブラウザタブ（旧ブラウザ） |
| `favicon-32.svg` | 32×32 px | 1x | 標準ブラウザ favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI ディスプレイ |
| `favicon-128.svg` | 128×128 px | 2x | Apple touch icon、ブックマーク |
| `favicon-256.svg` | 256×256 px | 4x | 近代ブラウザ、PWA アイコン |

**最適化ノート**:
- 16px: 最小限のジオメトリ — リング、針、シェブロンのみ
- 32px: 主要方位の目盛りを追加
- 64px 以上: 中間方位の目盛りを含むフルディテール
- すべてメインアイコンとビジュアル一貫性を保つ
- SVG 形式により任意のサイズで鮮明に表示

## HTML 統合

### 基本的な favicon セットアップ

```html
<!-- Browser favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch icon (mobile home screen) -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA & modern browsers -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完全セットアップ

```html
<head>
  <!-- Primary favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple touch icon -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA icons -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest reference (if using manifest.json) -->
  <meta name="theme-color" content="#000000">
</head>
```

## カラーパレット

### プライマリカラー
- **ブラック**: `#000000`（メインテキスト、ストローク、南針）
- **ホワイト**: `#FFFFFF`（ライト背景）
- **グレー**: `#6B7280`（補助テキスト、補助目盛り）

### アクセントカラー
- **ブライトグリーン**: `#22C55E`（北針、中央ドット、アクセント線 — ハイライト専用、背景には使わない）

### ダークモード
- **背景**: `#0A0A0A`（ニアブラック）

### CSS 変数
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 設定
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 使用ガイドライン
- メインテキストと構造要素にはブラックを使う
- 補助・サポート要素にはグレーを使う
- グリーンは **ハイライト専用** — 針、ドット、アクセント線
- グリーンを背景色には使わない
- WCAG AA コントラスト（最低 4.5:1）を維持する

## デザインガイドライン

### ロゴの使い方
- 白またはダーク（#0A0A0A）背景に使用する
- 比率を保ってスケールする
- ロゴ周りに余白を確保する（最低: ロゴ高さの半分）
- 背景に応じて提供されているライト／ダークバリアントを使う

### アイコンの使い方
- 標準サイズで使う: 16、32、64、128、256px
- コンパスのプロポーションを維持する
- 比率を保ってスケールする

### Favicon の使い方
- 文脈に応じた適切なサイズを使う
- 16〜32px: ブラウザタブ、ブックマーク
- 64px: サイトアイコン
- 128px 以上: Apple／Android のホーム画面

## SVG 最適化

すべての SVG ファイルはグラデーションやフィルターのないフラットデザイン：
- ストロークベースのクリーンなジオメトリ
- 埋め込みラスター画像なし
- 最適化されたパス
- レスポンシブ viewBox

Web 最適化用：
```bash
# 品質を保ちながら SVG を圧縮
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## PNG 変換

旧ブラウザ対応のため SVG を PNG に変換するには：

```bash
# ImageMagick を使う
convert -density 300 -background none favicon-256.svg favicon-256.png

# Inkscape を使う
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## アクセシビリティ

- 高コントラスト比（WCAG AA 準拠 — 最低 4.5:1）
- どのサイズでも認識できるクリーンな幾何学形状
- スケーラブルなベクター形式
- アイコン内にテキストを含まない（テキストはワードマークで別途追加）
- 意味伝達における赤緑の色依存なし

## 帰属

これらのアセットは Claude How To プロジェクトの一部である。

**ライセンス**: MIT（プロジェクトの LICENSE ファイルを参照）

## バージョン履歴

- **v3.0**（2026 年 2 月）: ブラック／ホワイト／グレー＋グリーンアクセントのパレットによるコンパス・ブラケットデザイン
- **v2.0**（2026 年 1 月）: エメラルドパレットの 12 光線スターバーストデザイン（Claude にインスパイアされたもの）
- **v1.0**（2026 年 1 月）: ヘキサゴンベースの進捗アイコンの初期デザイン

---

**最終更新**: 2026 年 2 月
**現バージョン**: 3.0（コンパス・ブラケット）
**全アセット**: 本番利用可能な SVG、完全スケーラブル、WCAG AA 準拠
