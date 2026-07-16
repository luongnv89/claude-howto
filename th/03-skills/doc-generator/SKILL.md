<!-- i18n-source: 03-skills/doc-generator/SKILL.md -->
<!-- i18n-date: 2026-05-09 -->
---
name: api-documentation-generator
description: Generate comprehensive, accurate API documentation from source code. Use when creating or updating API documentation, generating OpenAPI specs, or when users mention API docs, endpoints, or documentation.
---

# API Documentation Generator Skill

## สิ่งที่สร้างได้

- OpenAPI/Swagger specification
- เอกสาร API endpoint
- ตัวอย่างการใช้งาน SDK
- คู่มือการ integrate
- เอกสารอ้างอิง error code
- คู่มือ authentication

## โครงสร้างเอกสาร

### สำหรับแต่ละ Endpoint

```markdown
## GET /api/v1/users/:id

### คำอธิบาย
คำอธิบายสั้นๆ ว่า endpoint นี้ทำอะไร

### Parameter

| ชื่อ | ประเภท | จำเป็น | คำอธิบาย |
|------|------|----------|-------------|
| id | string | ใช่ | User ID |

### การตอบกลับ

**200 สำเร็จ**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 ไม่พบ**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "ไม่พบผู้ใช้"
}
```

### ตัวอย่าง

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
```
