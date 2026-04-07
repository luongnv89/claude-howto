---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 创建带上下文的 Git 提交
---

## 上下文

- 当前 git 状态: !`git status`
- 当前 git diff: !`git diff HEAD`
- 当前分支: !`git branch --show-current`
- 最近的提交: !`git log --oneline -10`

## 你的任务

根据上面的变更创建一个单独的 Git 提交。

如果通过参数传入了 message，就直接使用它：$ARGUMENTS

否则，分析这些变更，并按照 conventional commits 格式生成合适的提交信息：
- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档变更
- `refactor:` 代码重构
- `test:` 新增测试
- `chore:` 维护任务
