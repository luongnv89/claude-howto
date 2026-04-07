<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP（Model Context Protocol）

## 概览

MCP 是 Claude Code 访问外部工具、服务和 API 的标准协议。你可以把 GitHub、数据库、文件系统、聊天系统等都接到 Claude 里。

## MCP 架构

MCP 通常由三部分构成：

1. Claude Code
2. MCP server
3. 外部工具或数据源

Claude 会通过 MCP 协议向 server 发起工具调用，并把结果带回当前会话。

## MCP 生态

- GitHub 集成
- 数据库集成
- 文件系统集成
- 组织内部工具
- 第三方服务

## 安装方式

### HTTP 传输（推荐）

```bash
# Basic HTTP connection

# HTTP with authentication header
```

### Stdio 传输（本地）

```bash
# Local Node.js server

# With environment variables
```

### SSE 传输（已弃用）

旧版本中可能仍能见到 SSE 方式，但新配置一般优先考虑 HTTP 或 stdio。

### WebSocket 传输

适用于需要实时双向通信的场景。

### Windows 说明

在 Windows 上配置本地 server 时，要注意 shell、环境变量和路径写法。

### OAuth 2.0 认证

对于支持 OAuth 的 MCP server，Claude 可以通过交互式流程或预配置凭据完成认证。

## MCP 设置流程

1. 确认你要接入的服务
2. 选择 transport
3. 配置环境变量或认证
4. 在 Claude Code 中添加 server
5. 验证工具是否可用

## MCP 工具搜索

Claude 会根据当前上下文自动查找可用工具。

## 动态工具更新

当 MCP server 增加或移除工具时，Claude 可以在运行时感知变化。

## MCP 提示补充（Elicitation）

有些 MCP server 会在需要用户补充信息时触发 elicitation，Claude 再把问题转给用户。

## 工具描述与指令上限

每个 MCP 工具都应该有清晰的描述，帮助 Claude 选择正确的工具。

## 把 MCP Prompts 暴露成 Slash Commands

```text
/mcp__<server-name>__<prompt-name> [arguments]
```

例如：

```bash
/mcp__github__list_prs
/mcp__github__pr_review 456
/mcp__jira__create_issue "Bug title" high
```

## Server 去重

如果多个配置都指向同一个 server，Claude 会尽量避免重复加载。

## 通过 `@` 提及使用 MCP 资源

你可以把某些资源当作引用对象，在 prompt 中直接提及。

## MCP 作用域

MCP 配置通常有不同作用域，例如项目级和用户级。

### 使用项目作用域

适合把团队共享的 server 配置写进项目内。

## MCP 配置管理

### 添加 MCP server

```bash
# Add HTTP-based server

# Add local stdio server

# List all MCP servers

# Get details on specific server

# Remove an MCP server

# Reset project-specific approval choices

# Import from Claude Desktop
```

## 可用 MCP Server 表

你可以在配置中维护一张 server 清单，记录用途、认证方式和安装命令。

## 实战示例

### 示例 1：GitHub MCP 配置

你可以用 GitHub MCP 做这些事：

- PR 管理
- Issue 管理
- 仓库信息查询
- commit 操作

### 环境变量展开

在配置中可以使用环境变量，让同一份配置适配不同环境。

### 示例 2：数据库 MCP

```bash
# Using MCP database tool:

# Results:
```

### 示例 3：多 MCP 工作流

适合日常报告、跨系统同步和自动化文档生成。

### 示例 4：文件系统 MCP 操作

可用于读写文件、批量整理、生成报告或导出结果。

## MCP vs Memory：决策矩阵

- **Memory**：适合长期规则、偏好和上下文
- **MCP**：适合实时工具访问和外部数据

## 请求 / 响应模式

MCP 一般遵循：

1. Claude 发起请求
2. Server 处理
3. 返回结构化结果

## 环境变量

常见环境变量包括：

- API token
- 数据库地址
- 服务端口
- 认证信息

## Claude 作为 MCP Server（`claude mcp serve`）

```bash
# Start Claude Code as an MCP server on stdio
```

## 受管 MCP 配置（企业）

企业可通过受管设置统一分发 MCP 配置。

## 插件提供的 MCP Servers

插件可以把自己的 MCP server 一起打包分发。

## Subagent 作用域 MCP

某些 MCP 只允许特定 subagent 使用。

## MCP 输出限制

如果输出过大，可以限制 token 数或分页获取。

### 增大最大输出

```bash
# Increase the max output to 50,000 tokens
```

## 用代码执行解决上下文膨胀

当重复把大量数据回传给 Claude 会浪费 token 时，可以把 MCP 当作代码 API 来用，减少来回传输。

### 问题

- 两个信息源都在耗 token
- 大数据集不适合全量塞进上下文

### 方案

- 用 MCP 工具做实时查询
- 只把必要结果传给 Claude

#### 工作方式

Claude 通过工具调用从外部系统取回需要的数据，而不是把所有数据先写进上下文。

### 好处

- 更少 token 浪费
- 更清晰的数据边界
- 更适合大规模查询

#### 示例：过滤大数据集

#### 示例：循环而不做 round-trip

### 取舍

- 实现复杂度更高
- 需要维护 server
- 但扩展性更好

### MCPorter：MCP 工具组合运行时

这是更高级的工具编排思路，可以把多个 MCP 工具串成一个流程。

## 最佳实践

### 安全注意事项

#### 应该做的

- 只授权必要的工具
- 优先使用最小权限
- 检查输出是否可信

#### 不要做的

- 不要把高风险 token 写死在仓库里
- 不要默认开放所有工具
- 不要忽视网络和认证风险

### 配置建议

- 给每个 server 写清楚用途
- 用环境变量存认证信息
- 把项目级配置版本化

### 性能建议

- 避免一次性拉回过多数据
- 优先做过滤和分页
- 只返回 Claude 真正需要的结果

## 安装说明

### 前置条件

- Claude Code
- 对应的 MCP server
- 必要的认证信息

### 分步设置

1. 安装 server
2. 设置环境变量
3. 添加到 Claude
4. 测试工具

### 特定服务的安装

不同服务会有不同的安装命令和认证方式。

## 故障排查

### 找不到 MCP Server

- 检查是否安装
- 检查路径
- 检查配置是否正确

### 认证失败

- 检查环境变量是否设置
- 确认 token 权限正确
- 重新导出变量后再试

### 连接超时

- 检查网络
- 检查 server 是否可用

### MCP Server 崩溃

- 查看 server 日志
- 降低并发
- 简化请求

## 相关概念

- [Memory 中文指南](../02-memory/README.md)
- [Subagents 中文参考](../04-subagents/README.md)
- [Plugins 中文指南](../07-plugins/README.md)

## 更多资源

- [根目录中文指南](../README.md)
- [MCP 规范](https://modelcontextprotocol.io)
