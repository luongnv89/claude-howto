<!-- i18n-source: 07-plugins/pr-review/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review プラグイン

セキュリティ、テスト、ドキュメントのチェックを伴う完全な PR レビューワークフロー。

## 機能

✅ セキュリティ解析
✅ テストカバレッジのチェック
✅ ドキュメントの検証
✅ コード品質の評価
✅ パフォーマンス影響の解析

## インストール

```bash
claude --plugin-dir ./07-plugins/pr-review
```

読み込む前にプラグインをチェックする：

```bash
claude plugin validate ./07-plugins/pr-review
```

## 同梱内容

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### スラッシュコマンド

プラグインのコマンドは、`plugin.json` のプラグイン `name` で名前空間が付く：

- `/pr-review:review-pr` — 包括的な PR レビュー
- `/pr-review:check-security` — セキュリティ観点のレビュー
- `/pr-review:check-tests` — テストカバレッジ解析

### サブエージェント
- `security-reviewer` — セキュリティ脆弱性の検出
- `test-checker` — テストカバレッジ解析
- `performance-analyzer` — パフォーマンス影響の評価

### MCP サーバー

`.mcp.json` は `github` という 1 つのサーバーを宣言する。GitHub 公式の MCP サーバー（`ghcr.io/github/github-mcp-server`）を Docker で読み取り専用モードで実行する。`/mcp` では `plugin:pr-review:github` として表示される。

### フック

`hooks/hooks.json` は `pre-review.js` を `UserPromptExpansion` イベントに登録し、上記 3 つのコマンドに一致する matcher を設定する。いずれかのコマンドを入力すると、フックは次のように動作する：

- カレントディレクトリが git リポジトリでない場合、コマンドをブロックする（終了コード 2）
- それ以外の場合、現在のブランチと、未コミットの変更に関する注記を Claude のコンテキストに追加する

## 使い方

### 基本的な PR レビュー
```text
/pr-review:review-pr
```

### セキュリティチェックのみ
```text
/pr-review:check-security
```

### テストカバレッジチェック
```text
/pr-review:check-tests
```

## 必要要件

- Claude Code 1.0 以上
- Node.js（フックスクリプトの実行用）
- Docker（GitHub MCP サーバーの実行用）
- GitHub の personal access token
- Git リポジトリ

## 設定

Claude Code を起動する前に GitHub トークンを設定する：
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` はこれを、サーバーが読み取る変数である `GITHUB_PERSONAL_ACCESS_TOKEN` としてサーバーに渡す。`/mcp` を実行して `plugin:pr-review:github` が接続されていることを確認する。

## ワークフロー例

```text
User: /pr-review:review-pr

Claude:
1. pre-review hook checks the git repository and adds the branch to context
2. Fetches PR data via GitHub MCP
3. Delegates security review to security-reviewer subagent
4. Delegates testing to test-checker subagent
5. Delegates performance to performance-analyzer subagent
6. Synthesizes all findings
7. Provides comprehensive review report

Result:
✅ Security: No critical issues found
⚠️  Testing: Coverage is 65%, recommend 80%+
✅ Performance: No significant impact
📝 Recommendations: Add tests for edge cases
```

---

**最終更新**: 2026 年 10 月 18 日
**Claude Code バージョン**: 2.1.302
**出典**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**対応モデル**: Claude Fable 5.2、Claude Fable 5.1、Claude Fable 5、Claude Opus 5.5、Claude Opus 5、Claude Sonnet 5.5、Claude Sonnet 5、Claude Sonnet 4.6、Claude Opus 4.8、Claude Haiku 5.5、Claude Haiku 4.5
