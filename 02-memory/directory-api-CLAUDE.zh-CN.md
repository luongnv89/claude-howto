# API Module Standards

此文件会覆盖根级 CLAUDE.md 中对 `/src/api/` 目录的规则。

## API-Specific Standards

### Request Validation
- 使用 Zod 进行 schema 校验
- 所有输入必须校验
- 校验失败返回 400
- 返回字段级错误详情

### Authentication
- 所有 endpoint 都要求 JWT token
- token 放在 Authorization header
- token 24 小时过期
- 实现 refresh token 机制

### Response Format

所有成功响应必须遵循以下结构：

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

错误响应：
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- 使用 cursor 分页（不要使用 offset）
- 返回 `hasMore` 布尔值
- 单页最大 100
- 默认每页 20

### Rate Limiting
- 认证用户：1000 次/小时
- 公开接口：100 次/小时
- 超限返回 429
- 返回 `retry-after` header

### Caching
- 使用 Redis 做会话缓存
- 默认缓存 5 分钟
- 写操作后失效缓存
- 缓存 key 需带资源类型标签
