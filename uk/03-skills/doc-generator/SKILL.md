---
name: doc-generator
description: Генерація вичерпної, точної документації API з вихідного коду. Використовуйте при створенні або оновленні документації API, генерації специфікацій OpenAPI, або коли користувачі згадують документацію API, ендпоінти чи документацію.
---

# Навичка генерації документації API

## Генерує

- Специфікації OpenAPI/Swagger
- Документацію ендпоінтів API
- Приклади використання SDK
- Посібники з інтеграції
- Довідники кодів помилок
- Посібники з автентифікації

## Структура документації

### Для кожного ендпоінту

````markdown
## GET /api/v1/users/:id

### Опис
Короткий опис призначення цього ендпоінту

### Параметри

| Назва | Тип | Обовʼязковий | Опис |
|-------|-----|-------------|------|
| id | string | Так | ID користувача |

### Відповідь

**200 Успіх**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Не знайдено**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "Користувач не існує"
}
```

### Приклади

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
