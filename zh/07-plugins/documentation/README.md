---
name: 文档生成插件
description: 为文档编写、同步和校验提供完整工作流
tags: plugins, documentation, automation
---

# 文档生成插件

这个插件把文档相关的命令、subagents、模板和 MCP 服务器打包在一起，帮助你生成、同步和校验文档。

## 特性

✅ 生成 API 文档
✅ 创建和更新 README
✅ 同步文档
✅ 改进代码注释
✅ 生成示例

## 包含内容

### 命令

插件命令以 `plugin.json` 中的插件 `name` 作为命名空间：

- `/documentation:generate-api-docs`（[commands/generate-api-docs.md](commands/generate-api-docs.md)）- 生成 API 文档
- `/documentation:generate-readme`（[commands/generate-readme.md](commands/generate-readme.md)）- 生成 README
- `/documentation:sync-docs`（[commands/sync-docs.md](commands/sync-docs.md)）- 同步文档
- `/documentation:validate-docs`（[commands/validate-docs.md](commands/validate-docs.md)）- 校验文档

### Subagents
- [agents/api-documenter.md](agents/api-documenter.md) - API 文档 subagent
- [agents/code-commentator.md](agents/code-commentator.md) - 代码注释 subagent
- [agents/example-generator.md](agents/example-generator.md) - 示例生成 subagent

### 模板
- [templates/adr-template.md](templates/adr-template.md) - ADR 模板
- [templates/api-endpoint.md](templates/api-endpoint.md) - API 端点模板
- [templates/function-docs.md](templates/function-docs.md) - 函数文档模板

### MCP 服务器

`.mcp.json` 声明了一个服务器 `github`：GitHub 官方 MCP 服务器（`ghcr.io/github/github-mcp-server`），通过 Docker 以只读模式运行。镜像固定在 [v2.1.0 版本](https://github.com/github/github-mcp-server/releases/tag/v2.1.0)；如需升级，请修改 `.mcp.json` 中的标签。它在 `/mcp` 中显示为 `plugin:documentation:github`。

## 安装

```bash
claude --plugin-dir ./07-plugins/documentation
```

加载插件之前先检查它：

```bash
claude plugin validate ./07-plugins/documentation
```

## 使用方式

### 生成 API 文档
```text
/documentation:generate-api-docs
```

### 创建 README
```text
/documentation:generate-readme
```

### 同步文档
```text
/documentation:sync-docs
```

### 校验文档
```text
/documentation:validate-docs
```

## 适用场景

- 想标准化项目文档产出
- 想自动生成 README、API 文档和示例
- 想同步多个文档之间的一致性
- 想维护代码注释和示例质量

## 需求

- Claude Code 2.1+
- Docker 和 GitHub personal access token（可选，用于 GitHub MCP 服务器）

## 示例工作流

```text
用户：/documentation:generate-api-docs

Claude：
1. 扫描 /src/api/ 下的所有 API 端点
2. 委派给 api-documenter subagent
3. 提取函数签名和 JSDoc
4. 按模块 / 端点组织内容
5. 使用 api-endpoint.md 模板
6. 生成完整的 Markdown 文档
7. 包含 curl、JavaScript 和 Python 示例

结果：
✅ API 文档已生成
📄 已创建文件：
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 覆盖率：23/23 个端点已文档化
```

## 模板用途

### API 端点模板
用于编写带完整示例的 REST API 文档。

### 函数文档模板
用于编写单个函数或方法的说明文档。

### ADR 模板
用于记录架构决策。

## 配置

为文档同步设置 GitHub token：
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` 会把它作为 `GITHUB_PERSONAL_ACCESS_TOKEN`（服务器读取的变量）传给服务器。运行 `/mcp` 检查 `plugin:documentation:github` 是否已连接。没有 token 时，这些命令仍然可以处理本地文件。

## 最佳实践

- 文档尽量贴近代码
- 随着代码变化同步更新文档
- 提供可直接执行的示例
- 定期校验文档有效性
- 使用模板保持一致性

---

**最后更新**: 2026 年 10 月 18 日
**Claude Code 版本**: 2.1.302
**来源**:
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
