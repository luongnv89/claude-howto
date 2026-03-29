---
description: 從原始碼建立完整的 API 文件
---

# API 文件產生器

透過以下步驟產生 API 文件：

1. 掃描 `/src/api/` 中的所有檔案
2. 擷取函式簽名與 JSDoc 註解
3. 依端點/模組組織
4. 建立包含範例的 markdown
5. 包含請求/回應 schema
6. 加入錯誤文件

輸出格式：
- Markdown 檔案放置於 `/docs/api.md`
- 所有端點包含 curl 範例
- 加入 TypeScript 型別

