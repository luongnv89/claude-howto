<!-- i18n-source: 07-plugins/pr-review/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
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
/plugin install pr-review
```

## 同梱内容

### スラッシュコマンド
- `/review-pr` — 包括的な PR レビュー
- `/check-security` — セキュリティ観点のレビュー
- `/check-tests` — テストカバレッジ解析

### サブエージェント
- `security-reviewer` — セキュリティ脆弱性の検出
- `test-checker` — テストカバレッジ解析
- `performance-analyzer` — パフォーマンス影響の評価

### MCP サーバー
- PR データ取得のための GitHub 連携

### フック
- `pre-review.js` — レビュー前検証

## 使い方

### 基本的な PR レビュー
```
/review-pr
```

### セキュリティチェックのみ
```
/check-security
```

### テストカバレッジチェック
```
/check-tests
```

## 必要要件

- Claude Code 1.0 以上
- GitHub アクセス
- Git リポジトリ

## 設定

GitHub トークンを設定する：
```bash
export GITHUB_TOKEN="your_github_token"
```

## ワークフロー例

```
User: /review-pr

Claude:
1. Runs pre-review hook (validates git repo)
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

**最終更新**: 2026 年 4 月 24 日
**Claude Code バージョン**: 2.1.119
**出典**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**対応モデル**: Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
