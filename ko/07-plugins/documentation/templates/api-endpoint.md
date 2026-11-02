# [METHOD] /api/v1/[endpoint]

## 설명
해당 엔드포인트가 수행하는 작업에 대한 간단한 설명입니다.

## 인증(Authentication)
필요한 인증 방식 (예: Bearer 토큰)

## 파라미터

### Path 파라미터
| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|----------|------|
| id | string | 예 | 리소스 ID |

### Query 파라미터
| 이름 | 타입 | 필수 여부 | 설명 |
|------|------|----------|------|
| page | integer | 아니오 | 페이지 번호 (기본값: 1) |
| limit | integer | 아니오 | 페이지당 항목 수 (기본값: 20) |

### 요청 본문(Request Body)
```json
{
  "field": "value"
}
```

## 응답(Response)

### 200 OK
```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "예시"
  }
}
```

### 400 Bad Request
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "잘못된 입력입니다"
  }
}
```

### 404 Not Found
```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "리소스를 찾을 수 없습니다"
  }
}
```

## 예제(Examples)

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

## 속도 제한(Rate Limits)
- 인증 사용자: 시간당 1000 요청
- 공개 엔드포인트: 시간당 100 요청

## 관련 엔드포인트
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)
