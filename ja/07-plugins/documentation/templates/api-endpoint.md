<!-- i18n-source: 07-plugins/documentation/templates/api-endpoint.md -->
<!-- i18n-source-sha: 5caeff2 -->
<!-- i18n-date: 2026-04-27 -->

# [METHOD] /api/v1/[endpoint]

## 説明
このエンドポイントの動作の簡単な説明。

## 認証
必要な認証方式（例：Bearer トークン）。

## パラメータ

### Path Parameters
| Name | Type | Required | 説明 |
|------|------|----------|-----|
| id | string | Yes | リソース ID |

### Query Parameters
| Name | Type | Required | 説明 |
|------|------|----------|-----|
| page | integer | No | ページ番号（デフォルト: 1） |
| limit | integer | No | 1 ページあたりの件数（デフォルト: 20） |

### Request Body
```json
{
  "field": "value"
}
```

## レスポンス

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

## サンプル

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

## レート制限
- 認証済みユーザーは 1 時間あたり 1000 リクエスト
- 公開エンドポイントは 1 時間あたり 100 リクエスト

## 関連エンドポイント
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)
