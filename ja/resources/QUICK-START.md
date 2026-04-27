<!-- i18n-source: resources/QUICK-START.md -->
<!-- i18n-source-sha: 20779db -->
<!-- i18n-date: 2026-04-27 -->
# クイックスタート — ブランドアセット

## アセットをプロジェクトにコピーする

```bash
# すべてのリソースを Web プロジェクトにコピー
cp -r resources/ /path/to/your/website/

# Web 用 favicon のみをコピー
cp resources/favicons/* /path/to/your/website/public/
```

## HTML へ追加（コピー＆ペースト）

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## Markdown／ドキュメントで使う

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## 推奨サイズ

| 用途 | サイズ | ファイル |
|---------|------|------|
| Web サイトヘッダー | 520×120 | `logos/claude-howto-logo.svg` |
| アプリアイコン | 256×256 | `icons/claude-howto-icon.svg` |
| ブラウザタブ | 32×32 | `favicons/favicon-32.svg` |
| モバイルホーム画面 | 128×128 | `favicons/favicon-128.svg` |
| デスクトップアプリ | 256×256 | `favicons/favicon-256.svg` |
| 小さなアバター | 64×64 | `favicons/favicon-64.svg` |

## カラーコード

```css
/* CSS でこれらを使用 */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## アイコンデザインの意味

**コードブラケット付きコンパス**:
- コンパスリング ＝ ナビゲーション、体系的な学習経路
- 緑の北針 ＝ 方向、進捗、ガイダンス
- 黒の南針 ＝ 基盤、揺るぎない土台
- `>` ブラケット ＝ ターミナルプロンプト、コード、CLI コンテキスト
- 目盛り ＝ 精度、体系的なステップ

「明確なガイダンスでコードを進む道を見つける」を象徴している。

## どこで何を使うか

### Web サイト
- **ヘッダー**: ロゴ（`logos/claude-howto-logo.svg`）
- **Favicon**: 32px（`favicons/favicon-32.svg`）
- **ソーシャルプレビュー**: アイコン（`icons/claude-howto-icon.svg`）

### GitHub
- **README バッジ**: アイコン（`icons/claude-howto-icon.svg`）64〜128px
- **リポジトリアバター**: アイコン（`icons/claude-howto-icon.svg`）

### ソーシャルメディア
- **プロフィール画像**: アイコン（`icons/claude-howto-icon.svg`）
- **バナー**: ロゴ（`logos/claude-howto-logo.svg`）
- **サムネイル**: 256×256px のアイコン

### ドキュメント
- **章ヘッダー**: ロゴまたはアイコン（適切にスケール）
- **ナビゲーションアイコン**: Favicon（32〜64px）

---

完全なドキュメントは [README.md](README.md) を参照。
