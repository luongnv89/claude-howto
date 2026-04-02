---
description: 从源码生成完整 API 文档
---

# API Documentation Generator

按以下步骤生成 API 文档：

1. 扫描 `/src/api/` 下所有文件
2. 提取函数签名与 JSDoc 注释
3. 按 endpoint/module 组织内容
4. 生成包含示例的 Markdown
5. 包含 request/response schema
6. 补充错误文档

输出格式：
- 在 `/docs/api.md` 生成 Markdown 文件
- 为所有 endpoint 提供 curl 示例
- 补充 TypeScript 类型
