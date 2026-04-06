# API 模块规范

本文件会覆盖 `/src/api/` 下所有内容对应的根目录 `CLAUDE.md`。

## API 专属规范

### 请求校验
- 使用 Zod 做 schema 校验
- 始终校验输入
- 校验失败时返回 400
- 提供字段级别的错误详情

### 认证
- 所有端点都需要 JWT token
- token 放在 `Authorization` header 中
- token 24 小时后过期
- 实现 refresh token 机制

### 响应格式

所有响应都必须遵循下面的结构：

```json
{
  "success": true,
  "data": { /* 实际数据 */ },
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
    "message": "用户可读消息",
    "details": { /* 字段错误 */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### 分页
- 使用基于 cursor 的分页，而不是 offset
- 包含 `hasMore` 布尔值
- 单页最大数量限制为 100
- 默认页大小：20

### 限流
- 已认证用户每小时 1000 次请求
- 公开端点每小时 100 次请求
- 超出时返回 429
- 包含 `retry-after` header

### 缓存
- 使用 Redis 做会话缓存
- 缓存时长默认 5 分钟
- 写操作时失效缓存
- 用资源类型给缓存键打标签
