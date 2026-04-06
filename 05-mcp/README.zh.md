# MCP (Model Context Protocol)

一个视觉指南，了解 AI 代理如何连接外部工具和数据源。

> 📚 **关于本指南**
> 
> 本模块介绍 **Claude Code** 的 MCP 功能。
> 
> Kimi Code 用户可参考 **Kimi Code 适配**部分了解对应配置。

---

## 快速对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `claude mcp` 命令 | `kimi mcp` 命令 |
| `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` |
| `.claude/` 配置 | `.kimi/` 配置 |

---

## 概览

MCP（Model Context Protocol）让 Claude Code 和 Kimi Code 能够连接外部工具、API 和数据源。

```
┌─────────────────────────────────────────────────────────────┐
│                     MCP 架构                                 │
├─────────────────────────────────────────────────────────────┤
│                                                            │
│                   Claude Code / Kimi Code                   │
│                         │                                   │
│                         ▼                                   │
│              ┌─────────────────────┐                       │
│              │    MCP 客户端       │                       │
│              │  (内置在 CLI 中)    │                       │
│              └──────────┬──────────┘                       │
│                         │                                   │
│         ┌───────────────┼───────────────┐                  │
│         │               │               │                  │
│         ▼               ▼               ▼                  │
│    ┌─────────┐    ┌─────────┐    ┌─────────┐             │
│    │ GitHub  │    │Slack    │    │Database │             │
│    │ Server  │    │ Server  │    │ Server  │             │
│    └────┬────┘    └────┬────┘    └────┬────┘             │
│         │              │              │                    │
│         ▼              ▼              ▼                    │
│    ┌─────────────────────────────────────┐                │
│    │         外部服务                     │                │
│    │  GitHub    Slack    PostgreSQL      │                │
│    └─────────────────────────────────────┘                │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

### 工作流程

```
用户询问 ──▶ MCP 客户端 ──▶ 查询合适的服务器 ──▶ 获取数据 ──▶ 回复用户
```

---

## 安装

**Claude Code:**
```bash
# 添加 MCP 服务器
export GITHUB_TOKEN="your-token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 列出已配置的服务器
claude mcp list
```

**Kimi Code 适配:**
```bash
# 添加 MCP 服务器
export GITHUB_TOKEN="your-token"
kimi mcp add github -- npx -y @modelcontextprotocol/server-github

# 列出已配置的服务器
kimi mcp list
```

---

## 工作原理

### MCP 连接流程

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP 连接流程                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                │
│   1. 配置服务器                                                 │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │  claude mcp add │ 或 kimmi mcp add                          │
│   │  <name> <cmd>   │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   2. 存储配置                                                   │
│            │                                                    │
│            ├─▶ ~/.claude/mcp.json 或 ~/.kimi/mcp.json           │
│            │                                                    │
│            ▼                                                    │
│   3. 会话启动                                                   │
│            │                                                    │
│            ├─▶ 读取 mcp.json                                    │
│            │                                                    │
│            ▼                                                    │
│   4. 启动服务器进程                                             │
│            │                                                    │
│            ├─▶ 为每个服务器启动子进程                           │
│            │                                                    │
│            ▼                                                    │
│   5. 能力发现                                                   │
│            │                                                    │
│            ├─▶ 查询每个服务器的能力                             │
│            │      - 可用工具                                     │
│            │      - 资源类型                                     │
│            │      - 提示词模板                                   │
│            │                                                    │
│            ▼                                                    │
│   6. 运行时查询                                                 │
│            │                                                    │
│            ├─▶ 用户: "列出我的 GitHub issues"                   │
│            │                                                    │
│            ├─▶ Claude / Kimi 识别需要 GitHub 服务器             │
│            │                                                    │
│            ├─▶ 发送 JSON-RPC 请求到 GitHub 服务器               │
│            │                                                    │
│            ├─▶ 服务器查询 GitHub API                            │
│            │                                                    │
│            ├─▶ 返回结构化数据                                   │
│            │                                                    │
│            ▼                                                    │
│   7. 响应用户                                                   │
│            │                                                    │
│            └─▶ 格式化并呈现结果                                 │
│                                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 常用 MCP 服务器

| 服务器 | 用途 | 安装 |
|--------|------|------|
| **GitHub** | 仓库、issues、PR 管理 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Slack** | 消息发送和频道管理 | `claude mcp add slack -- npx -y @modelcontextprotocol/server-slack` |
| **PostgreSQL** | 数据库查询 | `claude mcp add postgres -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 文件系统访问 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |

---

## Kimi Code 适配

### 配置路径

| 配置项 | Claude Code | Kimi Code |
|--------|-------------|-----------|
| CLI 命令 | `claude mcp` | `kimi mcp` |
| 配置文件 | `~/.claude/mcp.json` | `~/.kimi/mcp.json` |
| 环境变量 | `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` |
| 服务器支持 | 标准 MCP 服务器 | 标准 MCP 服务器 |

### 快速迁移

```bash
# 1. 复制 MCP 配置
cp ~/.claude/mcp.json ~/.kimi/mcp.json

# 2. 使用 Kimi Code CLI 管理
kimi mcp list
kimi mcp add <name> <command>
kimi mcp remove <name>
```

### 注意事项

- MCP 是开放协议，服务器可以通用
- 大多数 MCP 服务器同时支持 Claude Code 和 Kimi Code
- API 密钥根据服务不同而不同（GitHub Token、Slack Token 等）
- 配置格式相同，可以共享配置文件

---

## 最佳实践

| 实践 | 原因 | 示例 |
|------|------|------|
| **使用最小权限** | 安全 | 只授予必要的权限 |
| **保护令牌** | 防止泄露 | 使用环境变量 |
| **命名规范** | 清晰识别 | `github-personal` 而非 `gh` |
| **文档化用途** | 团队协作 | 注释每个服务器的用途 |
| **定期审查** | 清理无用服务器 | 删除不用的配置 |

---

## 故障排除

| 问题 | 检查 | 解决方案 |
|------|------|---------|
| 服务器未连接 | 配置 | 检查 `mcp.json` 格式 |
| 认证失败 | 令牌 | 验证 API 令牌有效 |
| 命令未找到 | 包安装 | 确保 npx 可以访问包 |
| 权限错误 | 范围 | 检查令牌权限 |

---

## 下一步

- [学习钩子 →](../06-hooks/)
- [探索插件 →](../07-plugins/)
