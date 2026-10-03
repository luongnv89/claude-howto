---
name: api-documentation-generator
description: 소스 코드로부터 포괄적이고 정확한 API 문서를 생성합니다. API 문서를 생성하거나 업데이트할 때, OpenAPI 사양을 생성할 때, 또는 사용자가 API 문서, 엔드포인트, 문서를 언급할 때 사용합니다.
---

# API 문서 생성기 기능

## 생성 항목

- OpenAPI/Swagger 사양
- API 엔드포인트 문서
- SDK 사용 예제
- 통합 가이드
- 오류 코드 참조
- 인증 가이드


## 문서 구조

### 각 엔드포인트별


```markdown
## GET /api/v1/users/:id

### 설명
이 엔드포인트가 수행하는 작업에 대한 간단한 설명

### 매개변수

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### 응답

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### 예제

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
