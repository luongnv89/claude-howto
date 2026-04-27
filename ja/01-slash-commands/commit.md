<!-- i18n-source: 01-slash-commands/commit.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: コンテキスト付きで git コミットを作成する
---

## コンテキスト

- 現在の git ステータス: !`git status`
- 現在の git 差分: !`git diff HEAD`
- 現在のブランチ: !`git branch --show-current`
- 直近のコミット: !`git log --oneline -10`

## タスク

上記の変更内容に基づいて、単一の git コミットを作成する。

引数でメッセージが指定された場合はそれを使う: $ARGUMENTS

そうでない場合は、変更内容を分析し、Conventional Commits 形式に従って適切なコミットメッセージを作成する:
- `feat:` 新機能
- `fix:` バグ修正
- `docs:` ドキュメント変更
- `refactor:` コードのリファクタリング
- `test:` テスト追加
- `chore:` メンテナンスタスク

---
**Last Updated**: April 9, 2026
