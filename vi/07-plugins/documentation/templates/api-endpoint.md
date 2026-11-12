# [METHOD] /api/v1/[endpoint]

## Mô Tả
Giải thích ngắn gọn endpoint này làm gì.

## Xác Thực
Phương thức xác thực bắt buộc (ví dụ: Bearer token).

## Tham Số

### Tham Số Path
| Tên | Kiểu | Bắt Buộc | Mô Tả |
|------|------|----------|-------------|
| id | string | Có | ID tài nguyên |

### Tham Số Query
| Tên | Kiểu | Bắt Buộc | Mô Tả |
|------|------|----------|-------------|
| page | integer | Không | Số trang (mặc định: 1) |
| limit | integer | Không | Số mục mỗi trang (mặc định: 20) |

### Request Body
```json
{
  "field": "value"
}
```

## Response

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

## Ví Dụ

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

## Giới Hạn Tần Suất
- 1000 request mỗi giờ cho người dùng đã xác thực
- 100 request mỗi giờ cho endpoint công khai

## Endpoint Liên Quan
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)

---

**Cập Nhật Lần Cuối**: Ngày 4 tháng 8 năm 2026
**Phiên Bản Claude Code**: 2.1.220
**Nguồn**:
- https://code.claude.com/docs/en/plugins
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
