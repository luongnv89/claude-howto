---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 基于上下文创建 git commit
---

## 上下文

- 当前 git 状态: !`git status`
- 当前 git diff: !`git diff HEAD`
- 当前分支: !`git branch --show-current`
- 最近提交: !`git log --oneline -10`

## 你的任务

基于上述变更，创建一个单独的 git commit。

如果通过参数提供了消息，请使用它：$ARGUMENTS

否则请分析变更，并按 conventional commits 格式生成合适的 commit message：
- `feat:` 用于新功能
- `fix:` 用于 bug 修复
- `docs:` 用于文档变更
- `refactor:` 用于代码重构
- `test:` 用于新增测试
- `chore:` 用于维护性任务
