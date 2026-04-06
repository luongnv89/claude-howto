---
description: 根据源代码生成完整的 API 文档
---

# API 文档生成器

按以下步骤生成 API 文档：

1. 扫描 `/src/api/` 下的所有文件
2. 提取函数签名和 JSDoc 注释
3. 按端点/模块进行组织
4. 生成带示例的 Markdown
5. 包含请求/响应 Schema
6. 添加错误文档

输出格式：
- 输出为 `/docs/api.md` 中的 Markdown 文件
- 为所有端点加入 curl 示例
- 添加 TypeScript 类型
