# [METHOD] /api/v1/[endpoint]

## توضیح
توضیح مختصری از اینکه این endpoint چه کاری انجام می‌دهد.

## احراز هویت
روش احراز هویت مورد نیاز (مثلاً Bearer token).

## پارامترها

### پارامترهای مسیر
| نام | نوع | الزامی | توضیح |
|------|------|----------|-------------|
| id | string | بله | شناسه منبع |

### پارامترهای query
| نام | نوع | الزامی | توضیح |
|------|------|----------|-------------|
| page | integer | خیر | شماره صفحه (پیش‌فرض: ۱) |
| limit | integer | خیر | موارد در هر صفحه (پیش‌فرض: ۲۰) |

### بدنه درخواست
```json
{
  "field": "value"
}
```

## پاسخ‌ها

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

## نمونه‌ها

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

## محدودیت‌های نرخ
- ۱۰۰۰ درخواست در ساعت برای کاربران احراز هویت‌شده
- ۱۰۰ درخواست در ساعت برای endpoint‌های عمومی

## endpoint‌های مرتبط
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)

---

**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: 2.1.220
**منابع**:
- https://code.claude.com/docs/en/plugins
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
