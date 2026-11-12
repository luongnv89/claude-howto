<!-- i18n-source: 07-plugins/documentation/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation プラグイン

プロジェクトのドキュメント生成と保守を包括的に行うプラグイン。

## 機能

✅ API ドキュメント生成
✅ README の作成と更新
✅ ドキュメント同期
✅ コードコメントの改善
✅ サンプルコード生成

## インストール

```bash
claude --plugin-dir ./07-plugins/documentation
```

読み込む前にプラグインをチェックする：

```bash
claude plugin validate ./07-plugins/documentation
```

## 同梱内容

### スラッシュコマンド

プラグインのコマンドは、`plugin.json` のプラグイン `name` で名前空間が付く：

- `/documentation:generate-api-docs` — API ドキュメントを生成
- `/documentation:generate-readme` — README を作成または更新
- `/documentation:sync-docs` — コード変更にドキュメントを同期
- `/documentation:validate-docs` — ドキュメントを検証

### サブエージェント
- `api-documenter` — API ドキュメンテーションのスペシャリスト
- `code-commentator` — コードコメントの改善
- `example-generator` — コード例の作成

### テンプレート
- `api-endpoint.md` — API エンドポイントのドキュメントテンプレート
- `function-docs.md` — 関数ドキュメントのテンプレート
- `adr-template.md` — Architecture Decision Record（ADR）テンプレート

### MCP サーバー

`.mcp.json` は `github` という 1 つのサーバーを宣言する。GitHub 公式の MCP サーバー（`ghcr.io/github/github-mcp-server`）を Docker で読み取り専用モードで実行する。`/mcp` では `plugin:documentation:github` として表示される。

## 使い方

### API ドキュメントを生成
```text
/documentation:generate-api-docs
```

### README を作成
```text
/documentation:generate-readme
```

### ドキュメントを同期
```text
/documentation:sync-docs
```

### ドキュメントを検証
```text
/documentation:validate-docs
```

## 必要要件

- Claude Code 1.0 以上
- Docker と GitHub の personal access token（任意。GitHub MCP サーバー用）

## ワークフロー例

```text
User: /documentation:generate-api-docs

Claude:
1. Scans all API endpoints in /src/api/
2. Delegates to api-documenter subagent
3. Extracts function signatures and JSDoc
4. Organizes by module/endpoint
5. Uses api-endpoint.md template
6. Generates comprehensive markdown docs
7. Includes curl, JavaScript, and Python examples

Result:
✅ API documentation generated
📄 Files created:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Coverage: 23/23 endpoints documented
```

## テンプレートの使い方

### API Endpoint テンプレート
REST API エンドポイントを完全な例つきでドキュメント化する。

### Function Documentation テンプレート
個々の関数 / メソッドのドキュメント化に使う。

### ADR テンプレート
アーキテクチャ判断のドキュメント化に使う。

## 設定

ドキュメント同期用の GitHub トークンを設定する：
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` はこれを、サーバーが読み取る変数である `GITHUB_PERSONAL_ACCESS_TOKEN` としてサーバーに渡す。`/mcp` を実行して `plugin:documentation:github` が接続されていることを確認する。トークンがなくても、コマンドはローカルファイルに対しては動作する。

## ベストプラクティス

- ドキュメントはコードの近くに置く
- コード変更とともにドキュメントも更新する
- 実用的な例を含める
- 定期的に検証する
- 一貫性のためにテンプレートを使う

---

**最終更新**: 2026 年 10 月 18 日
**Claude Code バージョン**: 2.1.302
**出典**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**対応モデル**: Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
