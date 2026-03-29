---
description: 清理程式碼、暫存變更並準備 pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request 準備檢查清單

在建立 PR 之前，執行以下步驟：

1. 執行格式檢查：`prettier --write .`
2. 執行測試：`npm test`
3. 審查 git 差異：`git diff HEAD`
4. 暫存變更：`git add .`
5. 依照 conventional commits 格式建立提交訊息：
   - `fix:` 用於修復錯誤
   - `feat:` 用於新功能
   - `docs:` 用於文件
   - `refactor:` 用於程式碼重構
   - `test:` 用於新增測試
   - `chore:` 用於維護

6. 產生 PR 摘要，包含：
   - 變更了什麼
   - 為什麼變更
   - 執行了哪些測試
   - 潛在影響
