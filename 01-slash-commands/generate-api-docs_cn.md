---
description: 从源代码生成全面的 API 文档
---

# API 文档生成器

通过以下方式生成 API 文档：

1. 扫描 `/src/api/` 中的所有文件
2. 提取函数签名和 JSDoc 注释
3. 按端点/模块组织
4. 创建带示例的 Markdown 文档
5. 包含请求/响应模式
6. 添加错误文档

输出格式：
- `/docs/api.md` 中的 Markdown 文件
- 包含所有端点的 curl 示例
- 添加 TypeScript 类型
