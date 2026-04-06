# CLI 参考

Claude Code 和 Kimi Code 的命令、标志和选项完整参考。

> 📚 **关于本指南**
> 
> 本模块介绍 **Claude Code** 的 CLI 功能。
> 
> Kimi Code 用户可参考 **Kimi Code 适配**部分了解对应命令。

---

## 快速对照

| Claude Code | Kimi Code | 说明 |
|-------------|-----------|------|
| `claude` | `kimi` | 启动命令 |
| `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` | API 密钥 |
| `@anthropic-ai/claude-code` | `@moonshot-ai/kimi-code` | npm 包 |

---

## 全局选项

| 选项 | Claude Code | Kimi Code | 说明 |
|------|-------------|-----------|------|
| `-p, --print` | `claude -p` | `kimi -p` | 打印模式，非交互 |
| `-c, --continue` | `claude -c` | `kimi -c` | 继续上次会话 |
| `-r, --read-only` | `claude -r` | `kimi -r` | 只读模式 |
| `--plan` | `claude --plan` | `kimi --plan` | 规划模式 |
| `--resume` | `claude --resume` | `kimi --resume` | 恢复后台任务 |
| `-v, --version` | `claude -v` | `kimi -v` | 显示版本 |
| `-h, --help` | `claude -h` | `kimi -h` | 显示帮助 |

---

## 命令

### 核心命令

```bash
# Claude Code
claude [options] [prompt]     # 启动交互式会话
claude -p "your prompt"       # 打印模式
claude -c                     # 继续会话
claude -r                     # 只读模式
claude --plan                 # 规划模式
claude --resume               # 恢复后台任务

# Kimi Code
kimi [options] [prompt]       # 启动交互式会话
kimi -p "your prompt"         # 打印模式
kimi -c                       # 继续会话
kimi -r                       # 只读模式
kimi --plan                   # 规划模式
kimi --resume                 # 恢复后台任务
```

### 代理管理

```bash
# Claude Code
claude agents list            # 列出代理
claude agents add <name>      # 添加代理
claude agents remove <name>   # 移除代理

# Kimi Code
kimi agents list              # 列出代理
kimi agents add <name>        # 添加代理
kimi agents remove <name>     # 移除代理
```

### MCP 管理

```bash
# Claude Code
claude mcp list               # 列出 MCP 服务器
claude mcp add <name> <cmd>   # 添加 MCP 服务器
claude mcp remove <name>      # 移除 MCP 服务器

# Kimi Code
kimi mcp list                 # 列出 MCP 服务器
kimi mcp add <name> <cmd>     # 添加 MCP 服务器
kimi mcp remove <name>        # 移除 MCP 服务器
```

### 插件管理

```bash
# Claude Code
claude plugin list            # 列出插件
claude plugin install <name>  # 安装插件
claude plugin uninstall <name># 卸载插件

# Kimi Code
kimi plugin list              # 列出插件
kimi plugin install <name>    # 安装插件
kimi plugin uninstall <name>  # 卸载插件
```

---

## 环境变量

| 变量 | Claude Code | Kimi Code | 说明 |
|------|-------------|-----------|------|
| `ANTHROPIC_API_KEY` | ✅ | ❌ | Anthropic API 密钥 |
| `MOONSHOT_API_KEY` | ❌ | ✅ | Moonshot AI API 密钥 |
| `CLAUDE_CODE_DEBUG` | ✅ | ❌ | 调试模式 |
| `KIMI_CODE_DEBUG` | ❌ | ✅ | 调试模式 |
| `CLAUDE_CODE_CONFIG` | ✅ | ❌ | 自定义配置路径 |
| `KIMI_CODE_CONFIG` | ❌ | ✅ | 自定义配置路径 |

---

## 配置文件

### Claude Code

```
~/.claude/
├── config.json          # 用户配置
├── mcp.json            # MCP 服务器配置
├── commands/           # 全局斜杠命令
├── skills/             # 全局技能
├── agents/             # 代理定义
└── hooks/              # 钩子脚本
```

### Kimi Code

```
~/.kimi/
├── config.json          # 用户配置
├── mcp.json            # MCP 服务器配置
├── commands/           # 全局斜杠命令
├── skills/             # 全局技能
├── agents/             # 代理定义
└── hooks/              # 钩子脚本
```

### 项目级配置

```bash
# Claude Code
./.claude/
├── commands/           # 项目斜杠命令
└── plugins/            # 项目插件

./CLAUDE.md             # 项目内存
./CLAUDE.local.md       # 本地内存（不提交）

# Kimi Code
./.kimi/
├── commands/           # 项目斜杠命令
└── plugins/            # 项目插件

./KIMI.md               # 项目内存
./KIMI.local.md         # 本地内存（不提交）
```

---

## Kimi Code 适配

### 命令对照表

| 功能 | Claude Code | Kimi Code |
|------|-------------|-----------|
| 启动 | `claude` | `kimi` |
| 打印模式 | `claude -p` | `kimi -p` |
| 继续会话 | `claude -c` | `kimi -c` |
| 只读模式 | `claude -r` | `kimi -r` |
| 规划模式 | `claude --plan` | `kimi --plan` |
| 恢复任务 | `claude --resume` | `kimi --resume` |
| 代理管理 | `claude agents` | `kimi agents` |
| MCP 管理 | `claude mcp` | `kimi mcp` |
| 插件管理 | `claude plugin` | `kimi plugin` |

### 路径对照表

| 类型 | Claude Code | Kimi Code |
|------|-------------|-----------|
| 用户配置 | `~/.claude/` | `~/.kimi/` |
| 项目配置 | `./.claude/` | `./.kimi/` |
| 内存文件 | `CLAUDE.md` | `KIMI.md` |
| 本地内存 | `CLAUDE.local.md` | `KIMI.local.md` |

### 环境变量对照表

| Claude Code | Kimi Code | 用途 |
|-------------|-----------|------|
| `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` | API 密钥 |
| `CLAUDE_CODE_DEBUG` | `KIMI_CODE_DEBUG` | 调试模式 |
| `CLAUDE_CODE_CONFIG` | `KIMI_CODE_CONFIG` | 配置路径 |

---

## 最佳实践

| 实践 | 原因 | 示例 |
|------|------|------|
| **使用别名** | 快速访问 | `alias cld='claude'` |
| **环境变量** | 安全密钥 | 在 `.bashrc` 中设置 |
| **项目配置** | 团队协作 | 提交 `.claude/commands/` |
| **本地配置忽略** | 保护敏感信息 | `.gitignore` 添加 `CLAUDE.local.md` / `KIMI.local.md` |

---

## 故障排除

| 问题 | 检查 | 解决方案 |
|------|------|---------|
| 命令未找到 | PATH | 确保安装目录在 PATH 中 |
| 认证失败 | API 密钥 | 检查环境变量 |
| 配置未加载 | 路径 | 验证配置文件位置 |
| 权限错误 | 文件权限 | 检查 `~/.claude/` 或 `~/.kimi/` 权限 |

---

## 下一步

- [回到主指南 →](../README.zh.md)
