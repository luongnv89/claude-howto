---
name: doc-generator
description: تولید مستندات جامع و دقیق API از کد منبع. برای ایجاد یا به‌روزرسانی مستندات API، تولید مشخصات OpenAPI، یا وقتی کاربر از مستندات API، endpointها یا مستندسازی حرف می‌زند استفاده کنید.
---

# مهارت تولید مستندات API

## چه چیزی تولید می‌کند

- مشخصات OpenAPI/Swagger
- مستندات endpointهای API
- مثال‌های استفاده از SDK
- راهنماهای یکپارچه‌سازی
- مراجع کدهای خطا
- راهنماهای احراز هویت

## ساختار مستندات

### برای هر endpoint

````markdown
## GET /api/v1/users/:id

### توضیح
توضیح کوتاهی از کاری که این endpoint انجام می‌دهد

### پارامترها

| نام | نوع | الزامی | توضیح |
|------|------|----------|-------------|
| id | string | بله | شناسه کاربر |

### پاسخ

**200 موفقیت**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 یافت نشد**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### مثال‌ها

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```
````

---

**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: 2.1.220
**منابع**:
- https://code.claude.com/docs/en/skills
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
