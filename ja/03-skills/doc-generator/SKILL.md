<!-- i18n-source: 03-skills/doc-generator/SKILL.md -->
<!-- i18n-source-sha: a6380d8 -->
<!-- i18n-date: 2026-04-27 -->

---
name: api-documentation-generator
description: ソースコードから包括的かつ正確な API ドキュメントを生成する。API ドキュメントの作成・更新、OpenAPI 仕様の生成時、または API ドキュメント、エンドポイント、ドキュメントについて言及がある場合に使用する。
---

# API ドキュメント生成スキル

## 生成するもの

- OpenAPI/Swagger 仕様
- API エンドポイントのドキュメント
- SDK 利用例
- 統合ガイド
- エラーコード・リファレンス
- 認証ガイド

## ドキュメント構造

### 各エンドポイントごと

```markdown
## GET /api/v1/users/:id

### Description
このエンドポイントの動作を簡潔に説明

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

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

### Examples

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
