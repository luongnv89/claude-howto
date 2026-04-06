# Kimi Code 适配说明

## 关于本指南

本仓库是一份**图文并茂、案例驱动的 Claude Code 学习指南**，涵盖了从基础概念到高级智能体的全方位内容。

由于 Kimi Code 与 Claude Code 具有相似的架构和功能设计，我们将本指南适配为**同时适用于 Kimi Code 环境**。

## 适配说明

### 学习内容
- **核心内容**：学习 Claude Code 的功能和使用方法
- **学习价值**：Claude Code 是目前最先进的 AI 编程助手之一，学习其功能对提升开发效率有重要价值
- **概念通用**：大多数概念（斜杠命令、内存、技能、子代理、MCP、钩子等）在 Kimi Code 中有对应实现

### 运行环境
- **已适配为 Kimi Code**：所有命令、路径、配置已调整为 Kimi Code 格式
- **保持学习价值**：保留了所有关于 Claude Code 功能的学习内容

## 主要替换对照表

| Claude Code | Kimi Code |
|-------------|-----------|
| `claude` 命令 | `kimi` 命令 |
| `.claude/` 目录 | `.kimi/` 目录 |
| `CLAUDE.md` | `KIMI.md` |
| `claude-code` | `kimi-code` |
| `@anthropic-ai/claude-code` | `@moonshot-ai/kimi-code` |
| `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` |
| `CLAUDE_CODE_*` | `KIMI_CODE_*` |

## 文件结构

每个模块都包含：
- `README.md` - 英文原版（已添加中文链接）
- `README.zh.md` - 中文版（已适配 Kimi Code 命令和路径）

## 快速开始

### 安装 Kimi Code

```bash
npm install -g @moonshot-ai/kimi-code
```

### 设置 API 密钥

```bash
export MOONSHOT_API_KEY="your-api-key"
```

### 启动 Kimi Code

```bash
kimi
```

### 复制第一个斜杠命令

```bash
mkdir -p /path/to/your-project/.kimi/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.kimi/commands/
```

在 Kimi Code 中使用：
```
/optimize
```

## 学习路径

1. **[斜杠命令](01-slash-commands/)** - 快速快捷方式
2. **[内存](02-memory/)** - 持久化上下文
3. **[技能](03-skills/)** - 可复用能力
4. **[子代理](04-subagents/)** - 专业 AI 助手
5. **[MCP](05-mcp/)** - 外部工具访问
6. **[钩子](06-hooks/)** - 事件驱动自动化
7. **[插件](07-plugins/)** - 捆绑功能
8. **[检查点](08-checkpoints/)** - 会话快照
9. **[高级功能](09-advanced-features/)** - 规划、思考、后台任务
10. **[CLI 参考](10-cli/)** - 命令行选项

## 原始仓库

- **作者**: [luongnv89](https://github.com/luongnv89)
- **原始仓库**: [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)
- **许可证**: MIT

## 中文适配

- **适配方式**: 翻译 + Kimi Code 环境适配
- **适配说明**: 保留所有学习 Claude Code 的内容，同时调整为 Kimi Code 可运行的命令和路径
- **GitHub**: [KQDtianxiaK/claude-howto-running-on-Kimi-Code-](https://github.com/KQDtianxiaK/claude-howto-running-on-Kimi-Code-)

## 注意事项

1. **功能差异**: Kimi Code 和 Claude Code 在某些功能上可能存在差异，请以实际产品为准
2. **持续更新**: 本指南基于 Claude Code v2.2.0，Kimi Code 功能可能会不断更新
3. **反馈问题**: 如果发现任何适配问题，欢迎在 GitHub 上提出 issue

## 许可证

与原始仓库相同：MIT License
