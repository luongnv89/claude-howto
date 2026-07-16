<!-- i18n-source: 07-plugins/documentation/templates/api-endpoint.md -->
<!-- i18n-date: 2026-05-09 -->
# [METHOD] /api/v1/[endpoint]

## คำอธิบาย
คำอธิบายสั้น ๆ ว่า endpoint นี้ทำอะไร

## การยืนยันตัวตน
วิธีการยืนยันตัวตนที่จำเป็น (เช่น Bearer token)

## พารามิเตอร์

### Path Parameters
| ชื่อ | ประเภท | จำเป็น | คำอธิบาย |
|------|------|----------|-------------|
| id | string | ใช่ | Resource ID |

### Query Parameters
| ชื่อ | ประเภท | จำเป็น | คำอธิบาย |
|------|------|----------|-------------|
| page | integer | ไม่ | หมายเลขหน้า (ค่าเริ่มต้น: 1) |
| limit | integer | ไม่ | รายการต่อหน้า (ค่าเริ่มต้น: 20) |

### Request Body
```json
{
  "field": "value"
}
```

## การตอบสนอง

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

## ตัวอย่าง

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

## Rate Limits
- 1000 requests ต่อชั่วโมงสำหรับผู้ใช้ที่ยืนยันตัวตน
- 100 requests ต่อชั่วโมงสำหรับ endpoint สาธารณะ

## Endpoint ที่เกี่ยวข้อง
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)
