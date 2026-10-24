---
name: doc-generator
description: Generate comprehensive, accurate API documentation from source code. Use when creating or updating API documentation, generating OpenAPI specs, or when users mention API docs, endpoints, or documentation.
---

# مولد مستندات API (API Documentation Generator Skill)

## تولید می‌کند

- مشخصات OpenAPI/Swagger
- مستندات endpointهای API
- مثال‌های استفاده از SDK
- راهنماهای یکپارچه‌سازی
- مرجع کدهای خطا
- راهنماهای احراز هویت

## ساختار مستندات

### برای هر endpoint

````markdown
## GET /api/v1/users/:id

### توضیحات

توضیح کوتاهی از آنچه این endpoint انجام می‌دهد

### پارامترها

| نام | نوع | الزامی | توضیحات |
|------|------|----------|-------------|
| id | string | بله | شناسه کاربر |

### پاسخ

**200 موفق**
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

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
