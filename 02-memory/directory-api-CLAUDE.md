# API 模組標準

此檔案覆寫 /src/api/ 中所有內容的根目錄 CLAUDE.md

## API 特定標準

### 請求驗證
- 使用 Zod 進行 schema 驗證
- 始終驗證輸入
- 驗證錯誤時回傳 400
- 包含欄位層級的錯誤詳細資訊

### 認證
- 所有端點需要 JWT token
- Token 放在 Authorization header 中
- Token 在 24 小時後過期
- 實作 refresh token 機制

### 回應格式

所有回應必須遵循此結構：

```json
{
  "success": true,
  "data": { /* 實際資料 */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

錯誤回應：
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* 欄位錯誤 */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### 分頁
- 使用基於游標的分頁（非偏移量）
- 包含 `hasMore` 布林值
- 最大頁面大小限制為 100
- 預設頁面大小：20

### 速率限制
- 已認證使用者每小時 1000 個請求
- 公開端點每小時 100 個請求
- 超過時回傳 429
- 包含 retry-after header

### 快取
- 使用 Redis 進行工作階段快取
- 預設快取時長：5 分鐘
- 寫入操作時使快取失效
- 以資源類型標記快取金鑰

