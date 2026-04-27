<!-- i18n-source: CLAUDE.md -->
<!-- i18n-source-sha: a70777e -->
<!-- i18n-date: 2026-04-27 -->

# CLAUDE.md

このファイルは、本リポジトリ内のコードを扱う際の Claude Code（claude.ai/code）向けガイドである。

## プロジェクト概要

Claude How To は Claude Code 機能のチュートリアルリポジトリである。これは **ドキュメント・アズ・コード** であり、主な成果物は実行可能アプリケーションではなく、番号付きの学習モジュールに整理された Markdown ファイルである。

**アーキテクチャ：** 各モジュール（01〜10）は Claude Code の特定の機能を、コピー＆ペースト可能なテンプレート、Mermaid 図、サンプルとともに解説する。ビルドシステムはドキュメントの品質を検証し、EPUB 電子書籍を生成する。

## よく使うコマンド

### pre-commit 品質チェック

すべてのドキュメントは、コミット前に 4 つの品質チェックを通過しなければならない（pre-commit フックで自動実行される）：

```bash
# pre-commit フックをインストール（毎コミットで実行）
pre-commit install

# 全チェックを手動で実行
pre-commit run --all-files
```

4 つのチェックは以下のとおり：
1. **markdown-lint** — `markdownlint` による Markdown 構造とフォーマット
2. **cross-references** — 内部リンク、アンカー、コードフェンスの構文（Python スクリプト）
3. **mermaid-syntax** — すべての Mermaid 図が正しくパースされるかを検証（Python スクリプト）
4. **link-check** — 外部 URL が到達可能か（Python スクリプト）
5. **build-epub** — EPUB がエラーなく生成されるか（`.md` 変更時）

### 開発環境のセットアップ

```bash
# uv（Python パッケージマネージャ）をインストール
pip install uv

# 仮想環境を作成して Python 依存関係をインストール
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Node.js ツール（Markdown リンタと Mermaid バリデータ）をインストール
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli

# pre-commit フックをインストール
uv pip install pre-commit
pre-commit install
```

### テスト

`scripts/` 内の Python スクリプトはユニットテストを持つ：

```bash
# 全テストを実行
pytest scripts/tests/ -v

# カバレッジ付きで実行
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 特定のテストを実行
pytest scripts/tests/test_build_epub.py -v
```

### コード品質

```bash
# Python コードをリント・整形
ruff check scripts/
ruff format scripts/

# セキュリティスキャン
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# 型チェック
mypy scripts/ --ignore-missing-imports
```

### EPUB ビルド

```bash
# 電子書籍を生成（Mermaid 図を Kroki.io API でレンダリング）
uv run scripts/build_epub.py

# オプション付き
uv run scripts/build_epub.py --verbose --output custom-name.epub --max-concurrent 5
```

## ディレクトリ構造

```
├── 01-slash-commands/      # ユーザーが起動するショートカット
├── 02-memory/              # 永続コンテキストの例
├── 03-skills/              # 再利用可能な能力
├── 04-subagents/           # 専門 AI アシスタント
├── 05-mcp/                 # Model Context Protocol の例
├── 06-hooks/               # イベント駆動の自動化
├── 07-plugins/             # バンドル機能
├── 08-checkpoints/         # セッションのスナップショット
├── 09-advanced-features/   # プランニング、シンキング、バックグラウンド
├── 10-cli/                 # CLI リファレンス
├── scripts/
│   ├── build_epub.py           # EPUB ジェネレータ（Mermaid を Kroki API でレンダリング）
│   ├── check_cross_references.py   # 内部リンクを検証
│   ├── check_links.py          # 外部 URL を検証
│   ├── check_mermaid.py        # Mermaid 構文を検証
│   └── tests/                  # スクリプトのユニットテスト
├── .pre-commit-config.yaml    # 品質チェック定義
└── README.md               # メインガイド（モジュール索引も兼ねる）
```

## コンテンツ作成ガイド

### モジュール構造
番号付きフォルダはいずれも以下のパターンに従う：
- **README.md** — 機能の概要と例
- **サンプルファイル** — コピー＆ペースト可能なテンプレート（コマンドは `.md`、設定は `.json`、フックは `.sh`）
- ファイルは機能の複雑さと依存関係に従って整理されている

### Mermaid 図
- すべての図は正常にパースできること（pre-commit フックで検査）
- EPUB ビルドは Kroki.io API で図をレンダリングする（インターネット接続が必要）
- フローチャート、シーケンス図、アーキテクチャ可視化に Mermaid を使用する

### 相互参照
- 内部リンクは相対パスを使う（例：`(01-slash-commands/README.md)`）
- コードフェンスは言語指定が必須（例：` ```bash `、` ```python `）
- アンカーリンクは `#heading-name` 形式

### リンク検証
- 外部 URL は到達可能であること（pre-commit フックで検査）
- 一時的なコンテンツへのリンクは避ける
- 可能な限りパーマリンクを使用する

## 主要なアーキテクチャ上のポイント

1. **番号付きフォルダは学習順序を示す** — 01〜10 のプレフィックスは Claude Code 機能の推奨学習順序を表す。この番号付けは意図的なものなので、アルファベット順に並べ替えてはならない。

2. **スクリプトはユーティリティであり製品ではない** — `scripts/` の Python スクリプトはドキュメント品質と EPUB 生成を支援するものである。実際のコンテンツは番号付きモジュールフォルダにある。

3. **pre-commit がゲートキーパー** — PR が承認される前に 4 つの品質チェックがすべて通過しなければならない。CI パイプラインは同じチェックを 2 回目のパスとして実行する。

4. **Mermaid のレンダリングにはネットワークが必要** — EPUB ビルドは図のレンダリングに Kroki.io API を呼び出す。ここでビルドが失敗する場合は、ネットワーク問題か Mermaid 構文エラーが典型的な原因である。

5. **これはチュートリアルでありライブラリではない** — コンテンツを追加する際は、明快な解説、コピー＆ペースト可能な例、視覚的な図を重視する。価値は概念を教えることにあり、再利用可能なコードを提供することではない。

## コミット規約

Conventional Commits 形式に従う：
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`
- `refactor(hooks): Simplify hook configuration examples`

スコープは該当するフォルダ名に合わせる。
