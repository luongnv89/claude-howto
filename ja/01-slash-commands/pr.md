<!-- i18n-source: 01-slash-commands/pr.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
description: コードを整え、変更をステージングし、プルリクエストを準備する
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# プルリクエスト準備チェックリスト

PR を作成する前に、以下のステップを実行する:

1. リンタ実行: `prettier --write .`
2. テスト実行: `npm test`
3. git 差分のレビュー: `git diff HEAD`
4. 変更をステージング: `git add .`
5. Conventional Commits に従ったコミットメッセージを作成する:
   - `fix:` バグ修正
   - `feat:` 新機能
   - `docs:` ドキュメント
   - `refactor:` コード再構成
   - `test:` テスト追加
   - `chore:` メンテナンス

6. PR サマリを生成する。次の項目を含める:
   - 何を変更したか
   - なぜ変更したか
   - 実施したテスト
   - 想定される影響

---
**Last Updated**: April 9, 2026
