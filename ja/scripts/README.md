<!-- i18n-source: scripts/README.md -->
<!-- i18n-source-sha: 58e586f -->
<!-- i18n-date: 2026-04-27 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB ビルダースクリプト

Claude How-To の Markdown ファイル群から EPUB 形式の電子書籍をビルドするスクリプト。

## 特徴

- フォルダ構成（01-slash-commands、02-memory など）に沿って章を整理する
- Mermaid 図を [Pele](https://github.com/obsidianmd/pele)（Node.js で実行する固定バージョンのバンドル）で SVG 画像としてレンダリングする。CSS 変数は白背景上の通常の色に置き換えるため、どの EPUB リーダーでも表示できる
- 同一の図をキャッシュし、ユニークな図は一度だけレンダリングする
- プロジェクトロゴから表紙画像を生成する
- 内部 Markdown リンクを EPUB の章参照へ変換する
- 厳格モード — レンダリング不能な図があればビルドを失敗させる

## 必要環境

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Mermaid 図レンダリング用に `PATH` 上の Node.js >= 20。固定バージョンの Pele バンドルは初回実行時にダウンロードされ（ネットワークが必要なのは一度だけ）、sha256 で検証して `scripts/.vendor-cache/pele/` にキャッシュされる

## クイックスタート

```bash
# 最も簡単な方法 — uv がすべてを処理する
uv run scripts/build_epub.py
```

## 開発環境セットアップ

```bash
# 仮想環境を作成
uv venv

# 有効化して依存関係をインストール
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# テストを実行
pytest scripts/tests/ -v

# スクリプトを実行
python scripts/build_epub.py
```

## コマンドラインオプション

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--lang {en,vi,zh,ja,ko,fa}]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --lang {en,vi,zh,ja,ko,fa}  Language to build (default: en)
```

## 使用例

```bash
# 詳細ログ付きでビルド
uv run scripts/build_epub.py --verbose

# 出力先をカスタマイズ
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 日本語版をビルド
uv run scripts/build_epub.py --lang ja
```

## 出力

リポジトリのルートディレクトリに `claude-howto-guide.epub` を生成する。

EPUB には次が含まれる：
- プロジェクトロゴ付きの表紙画像
- ネストされた目次
- すべての Markdown コンテンツを EPUB 互換 HTML に変換したもの
- SVG 画像としてレンダリングされた Mermaid 図

## テストの実行

```bash
# 仮想環境を使う場合
source .venv/bin/activate
pytest scripts/tests/ -v

# または uv で直接実行
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with pillow \
    pytest scripts/tests/ -v
```

## 依存関係

PEP 723 のインラインスクリプトメタデータで管理する：

| パッケージ | 用途 |
|---------|---------|
| `ebooklib` | EPUB 生成 |
| `markdown` | Markdown から HTML への変換 |
| `beautifulsoup4` | HTML パース |
| `pillow` | 表紙画像生成 |

## トラブルシューティング

**`Pele is unavailable` でビルドが失敗する**: Node.js >= 20 をインストールし、`node` が `PATH` 上にあることを確認する（`node --version`）。

**Pele バンドルのダウンロードまたはチェックサムの失敗**: 初回ビルドは固定バージョンの Pele バンドルを cdn.jsdelivr.net からダウンロードし、各ファイルの sha256 を検証する。オフラインやプロキシ環境では、ネットワークに接続した状態で一度ビルドすれば、以降は `scripts/.vendor-cache/pele/<version>/` のキャッシュを使う。チェックサムの不一致はダウンロードが改変または途中で切れたことを意味するので、そのフォルダを削除して再度ビルドする。

**ロゴが見つからない**: `claude-howto-logo.png` が見つからない場合、スクリプトはテキストのみの表紙を生成する。
