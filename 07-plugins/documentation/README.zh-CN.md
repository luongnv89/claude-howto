<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation Plugin

用于项目文档生成与维护的一体化插件。

## Features

✅ API 文档自动生成  
✅ README 创建与更新  
✅ 文档与代码同步  
✅ 代码注释优化  
✅ 示例代码生成

## Installation

```bash
/plugin install documentation
```

## What's Included

### Slash Commands
- `/generate-api-docs` - 生成 API 文档
- `/generate-readme` - 创建或更新 README
- `/sync-docs` - 将文档与代码变更同步
- `/validate-docs` - 校验文档完整性

### Subagents
- `api-documenter` - API 文档专家
- `code-commentator` - 注释改进专家
- `example-generator` - 示例代码生成专家

### Templates
- `api-endpoint.md` - API 接口文档模板
- `function-docs.md` - 函数文档模板
- `adr-template.md` - 架构决策记录（ADR）模板

### MCP Servers
- GitHub 集成（用于文档同步）

## Usage

### Generate API Documentation

```text
/generate-api-docs
```

### Create README

```text
/generate-readme
```

### Sync Documentation

```text
/sync-docs
```

### Validate Documentation

```text
/validate-docs
```

## Requirements

- Claude Code 1.0+
- GitHub 访问权限（可选）

## Example Workflow

```text
User: /generate-api-docs

Claude:
1. 扫描 /src/api/ 下全部接口
2. 委派给 api-documenter subagent
3. 提取函数签名与 JSDoc
4. 按模块/端点归类
5. 套用 api-endpoint.md 模板
6. 生成完整 markdown 文档
7. 附带 curl、JavaScript、Python 示例

Result:
✅ API documentation generated
📄 Files created:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Coverage: 23/23 endpoints documented
```

## Templates Usage

### API Endpoint Template
用于记录 REST API 端点并附完整调用示例。

### Function Documentation Template
用于记录单个函数/方法。

### ADR Template
用于记录架构决策过程与结论。

## Configuration

如需启用 GitHub 文档同步，请设置 token：

```bash
export GITHUB_TOKEN="your_github_token"
```

## Best Practices

- 文档尽量贴近代码维护
- 代码变更时同步更新文档
- 文档中加入可运行示例
- 定期执行文档校验
- 使用模板保证一致性
