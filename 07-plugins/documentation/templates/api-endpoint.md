# [METHOD] /api/v1/[endpoint]

## 說明
簡要說明此端點的功能。

## 認證
所需的認證方法（例如 Bearer token）。

## 參數

### 路徑參數
| 名稱 | 類型 | 必填 | 說明 |
|------|------|----------|-------------|
| id | string | 是 | 資源 ID |

### 查詢參數
| 名稱 | 類型 | 必填 | 說明 |
|------|------|----------|-------------|
| page | integer | 否 | 頁碼（預設：1） |
| limit | integer | 否 | 每頁項目數（預設：20） |

### 請求主體
```json
{
  "field": "value"
}
```

## 回應

### 200 OK
```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "Example"
  }
}
```

### 400 Bad Request
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input"
  }
}
```

### 404 Not Found
```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found"
  }
}
```

## 範例

### cURL
```bash
curl -X GET "https://api.example.com/api/v1/endpoint" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

### JavaScript
```javascript
const response = await fetch('/api/v1/endpoint', {
  headers: {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json'
  }
});
const data = await response.json();
```

### Python
```python
import requests

response = requests.get(
    'https://api.example.com/api/v1/endpoint',
    headers={'Authorization': 'Bearer token'}
)
data = response.json()
```

## 速率限制
- 已認證使用者每小時 1000 個請求
- 公開端點每小時 100 個請求

## 相關端點
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)
