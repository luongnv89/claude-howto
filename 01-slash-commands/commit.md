---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 使用上下文建立 git commit
---

## 上下文資訊

- 目前 git 狀態：!`git status`
- 目前 git 差異：!`git diff HEAD`
- 目前分支：!`git branch --show-current`
- 最近的提交紀錄：!`git log --oneline -10`

## 你的任務

根據以上變更，建立一個 git commit。

如果透過參數提供了訊息，請使用它：$ARGUMENTS

否則，請分析變更並依照 conventional commits 格式建立適當的提交訊息：
- `feat:` 用於新功能
- `fix:` 用於修復錯誤
- `docs:` 用於文件變更
- `refactor:` 用於程式碼重構
- `test:` 用於新增測試
- `chore:` 用於維護任務

