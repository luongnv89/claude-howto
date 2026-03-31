<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude How To

> 一份可视化、示例驱动的 Claude Code 使用指南——从基础概念到高级 Agent，包含可立即带来价值的复制即用模板。

## 为什么需要这份指南？

本项目以不同的方式补充了 [Anthropic 官方文档](https://code.claude.com/docs/en/overview)：

| | 官方文档 | 本指南 |
|--|---------------|------------|
| **格式** | 参考文档 | 带有图表的可视化教程 |
| **深度** | 功能描述 | 底层工作原理 |
| **示例** | 基础代码片段 | 可立即使用的生产级模板 |
| **结构** | 按功能组织 | 渐进式学习路径（入门 → 进阶） |
| **引导方式** | 自主探索 | 附有时间估算的引导学习路线 |
| **自我评估** | 无 | 交互式测验，帮助识别技能差距并构建个性化学习路径 |

**你将在这里找到：**
- 解释每个功能工作原理的 Mermaid 图表
- 可直接复制到项目中的即用配置
- 带有背景说明和最佳实践的真实案例
- 从 `/help` 到构建自定义 Agent 的清晰进阶路径
- 基于常见问题的故障排查指南

---

## 目录

- [为什么需要这份指南？](#为什么需要这份指南)
- [功能目录](#-功能目录)
- [快速导航](#快速导航)
- [学习路径](#-学习路径)
- [快速参考](#-快速参考选择你的功能)
- [快速入门](#-快速入门)
- **功能介绍**
  - [01. Slash Commands](#01-slash-commands)
  - [02. Memory](#02-memory)
  - [03. Skills](#03-skills)
  - [04. Subagents](#04-subagents)
  - [05. MCP Protocol](#05-mcp-protocol)
  - [06. Hooks](#06-hooks)
  - [07. Plugins](#07-plugins)
  - [08. Checkpoints](#08-checkpoints-与回溯)
  - [09. 高级功能](#09-高级功能)
  - [10. CLI 参考](#10-cli-参考)
- [目录结构](#目录结构)
- [安装快速参考](#安装快速参考)
- [工作流示例](#工作流示例)
- [最佳实践](#最佳实践)
- [故障排查](#故障排查)
- [测试](#测试)
- [更多资源](#更多资源)
- [贡献](#贡献)
- [EPUB 生成](#epub-生成)
- [贡献者](#贡献者)
- [Star 历史](#star-历史)

---

## 功能目录

**需要快速参考？** 查看我们全面的 **[功能目录](CATALOG.md)**，包含：

- 所有 slash commands（内置和自定义）及其说明
- Sub-agents 及其能力
- Skills 及自动调用触发条件
- Plugins 及其组件和安装命令
- 用于外部集成的 MCP 服务器
- 用于事件驱动自动化的 Hooks
- 每项功能的一键安装命令

**[查看完整目录](CATALOG.md)**

---

## 快速导航

| 功能 | 描述 | 文件夹 |
|---------|-------------|--------|
| **功能目录** | 包含安装命令的完整参考 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 用户调用的快捷方式 | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 持久化上下文 | [02-memory/](02-memory/) |
| **Skills** | 可复用能力 | [03-skills/](03-skills/) |
| **Subagents** | 专业化 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP Protocol** | 外部工具访问 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驱动自动化 | [06-hooks/](06-hooks/) |
| **Plugins** | 功能集合包 | [07-plugins/](07-plugins/) |
| **Checkpoints** | 会话快照与回溯 | [08-checkpoints/](08-checkpoints/) |
| **高级功能** | 规划、思考、后台任务 | [09-advanced-features/](09-advanced-features/) |
| **CLI 参考** | 命令、标志和选项 | [10-cli/](10-cli/) |
| **博客文章** | 真实使用案例 | [博客文章](https://medium.com/@luongnv89) |

---

## 📚 学习路径

**不知道从哪里开始？** 参加 [自我评估测验](LEARNING-ROADMAP.md#-find-your-level) 找到适合你的推荐路径，或在 Claude Code 中运行 `/self-assessment` 进行交互式版本评估。

> **内置 Skills**：本仓库包含两个可在 Claude Code 中直接使用的交互式 Skills：
> - `/self-assessment` — 评估你对 Claude Code 的整体熟练程度，获取个性化学习路径
> - `/lesson-quiz [lesson]` — 测试你对任意具体课程的理解（例如 `/lesson-quiz hooks`）

| 顺序 | 功能 | 级别 | 时间 | 适合人群 |
|-------|---------|-------|------|-----------------|
| **1** | [Slash Commands](01-slash-commands/) | ⭐ 入门 | 30 分钟 | 第 1 级起点 |
| **2** | [Memory](02-memory/) | ⭐⭐ 入门+ | 45 分钟 | 第 1 级 |
| **3** | [Checkpoints](08-checkpoints/) | ⭐⭐ 中级 | 45 分钟 | 第 1 级 |
| **4** | [CLI 基础](10-cli/) | ⭐⭐ 入门+ | 30 分钟 | 第 1 级 |
| **5** | [Skills](03-skills/) | ⭐⭐ 中级 | 1 小时 | 第 2 级起点 |
| **6** | [Hooks](06-hooks/) | ⭐⭐ 中级 | 1 小时 | 第 2 级 |
| **7** | [MCP](05-mcp/) | ⭐⭐⭐ 中级+ | 1 小时 | 第 2 级 |
| **8** | [Subagents](04-subagents/) | ⭐⭐⭐ 中级+ | 1.5 小时 | 第 2 级 |
| **9** | [高级功能](09-advanced-features/) | ⭐⭐⭐⭐⭐ 进阶 | 2-3 小时 | 第 3 级起点 |
| **10** | [Plugins](07-plugins/) | ⭐⭐⭐⭐ 进阶 | 2 小时 | 第 3 级 |
| **11** | [CLI 精通](10-cli/) | ⭐⭐⭐ 进阶 | 1 小时 | 第 3 级 |

**总计**：约 11-13 小时 | 📖 **[完整学习路线 →](LEARNING-ROADMAP.md)**

---

## 🎯 快速参考：选择你的功能

### 功能对比

| 功能 | 调用方式 | 持久性 | 最适合 |
|---------|-----------|------------|----------|
| **Slash Commands** | 手动（`/cmd`） | 仅限当前会话 | 快速快捷方式 |
| **Memory** | 自动加载 | 跨会话 | 长期学习记忆 |
| **Skills** | 自动调用 | 文件系统 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务分发 |
| **MCP Protocol** | 自动查询 | 实时 | 访问实时数据 |
| **Hooks** | 事件触发 | 配置化 | 自动化与验证 |
| **Plugins** | 一条命令 | 全部功能 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 基于会话 | 安全实验 |
| **Planning Mode** | 手动/自动 | 规划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务持续期间 | 长时间运行的操作 |
| **CLI Reference** | 终端命令 | 会话/脚本 | 自动化与脚本编写 |

### 使用场景矩阵

| 使用场景 | 推荐功能 |
|----------|---------------------|
| **团队入职** | Memory + Slash Commands + Plugins |
| **代码质量** | Subagents + Skills + Memory + Hooks |
| **文档生成** | Skills + Subagents + Plugins |
| **DevOps** | Plugins + MCP + Hooks + Background Tasks |
| **安全审查** | Subagents + Skills + Hooks（只读模式） |
| **API 集成** | MCP + Memory |
| **快速任务** | Slash Commands |
| **复杂项目** | 全部功能 + Planning Mode |
| **重构** | Checkpoints + Planning Mode + Hooks |
| **学习/实验** | Checkpoints + Extended Thinking + Permission Mode |
| **CI/CD 自动化** | CLI Reference + Hooks + Background Tasks |
| **性能优化** | Planning Mode + Checkpoints + Background Tasks |
| **脚本自动化** | CLI Reference + Hooks + MCP |
| **批量处理** | CLI Reference + Background Tasks |

---

## ⚡ 快速入门

### 15 分钟——第一步
```bash
# 复制你的第一个 slash command
cp 01-slash-commands/optimize.md .claude/commands/

# 试试它！
# 在 Claude Code 中输入：/optimize
```

### 1 小时——基础配置
```bash
# 1. Slash commands（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 2. 项目 Memory（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 3. 安装一个 Skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 4. 组合使用（15 分钟）
# 看看它们如何协同工作！
```

### 周末——完整配置
- **第 1 天**：Slash Commands、Memory、Skills、Hooks
- **第 2 天**：Subagents、MCP 集成、Plugins
- **成果**：完整的 Claude Code 高级用户配置

📖 **[详细里程碑和练习 →](LEARNING-ROADMAP.md)**

---

## 01. Slash Commands

**位置**：[01-slash-commands/](01-slash-commands/)

**是什么**：以 Markdown 文件形式存储的用户调用快捷方式

**示例**：
- `optimize.md` — 代码优化分析
- `pr.md` — Pull Request 准备
- `generate-api-docs.md` — API 文档生成器

**安装**：
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使用**：
```
/optimize
/pr
/generate-api-docs
```

**深入了解**：[发现 Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

---

## 02. Memory

**位置**：[02-memory/](02-memory/)

**是什么**：跨会话的持久化上下文

**示例**：
- `project-CLAUDE.md` — 团队级项目规范
- `directory-api-CLAUDE.md` — 目录级规则
- `personal-CLAUDE.md` — 个人偏好设置

**安装**：
```bash
# 项目 Memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录 Memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人 Memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用**：由 Claude 自动加载

---

## 03. Skills

**位置**：[03-skills/](03-skills/)

**是什么**：带有指令和脚本的可复用、自动调用能力

**示例**：
- `code-review/` — 带有脚本的全面代码审查
- `brand-voice/` — 品牌语调一致性检查器
- `doc-generator/` — API 文档生成器

**安装**：
```bash
# 个人 Skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 Skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使用**：在相关时自动调用

---

## 04. Subagents

**位置**：[04-subagents/](04-subagents/)

**是什么**：具有隔离上下文和自定义提示词的专业化 AI 助手

**示例**：
- `code-reviewer.md` — 全面的代码质量分析
- `test-engineer.md` — 测试策略与覆盖率
- `documentation-writer.md` — 技术文档编写
- `secure-reviewer.md` — 安全聚焦审查（只读）
- `implementation-agent.md` — 完整功能实现

**安装**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用**：由主 Agent 自动委派

---

## 05. MCP Protocol

**位置**：[05-mcp/](05-mcp/)

**是什么**：Model Context Protocol，用于访问外部工具和 API

**示例**：
- `github-mcp.json` — GitHub 集成
- `database-mcp.json` — 数据库查询
- `filesystem-mcp.json` — 文件操作
- `multi-mcp.json` — 多个 MCP 服务器

**安装**：
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP 服务器
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动添加到项目的 .mcp.json（参见 05-mcp/ 中的示例）
```

**使用**：配置后，MCP 工具可自动被 Claude 使用

---

## 06. Hooks

**位置**：[06-hooks/](06-hooks/)

**是什么**：事件驱动的 Shell 命令，在响应 Claude Code 事件时自动执行

**示例**：
- `format-code.sh` — 写入前自动格式化代码
- `pre-commit.sh` — 提交前运行测试
- `security-scan.sh` — 扫描安全问题
- `log-bash.sh` — 记录所有 Bash 命令
- `validate-prompt.sh` — 验证用户提示词
- `notify-team.sh` — 在事件发生时发送通知

**安装**：
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 Hooks：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**使用**：Hooks 在事件触发时自动执行

**Hook 类型**：
- **工具 Hooks**：`PreToolUse:*`、`PostToolUse:*`
- **会话 Hooks**：`Stop`、`SubagentStop`、`SubagentStart`
- **生命周期 Hooks**：`Notification`、`ConfigChange`、`WorktreeCreate`、`WorktreeRemove`

---

## 07. Plugins

**位置**：[07-plugins/](07-plugins/)

**是什么**：命令、Agent、MCP 和 Hooks 的集合包

**示例**：
- `pr-review/` — 完整的 PR 审查工作流
- `devops-automation/` — 部署与监控
- `documentation/` — 文档生成

**安装**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使用**：使用集合包中的 slash commands 和功能

---

## 08. Checkpoints 与回溯

**位置**：[08-checkpoints/](08-checkpoints/)

**是什么**：保存对话状态并回溯到之前的节点，以探索不同的解决方案

**核心概念**：
- **Checkpoint**：对话状态的快照
- **Rewind**：回到之前的 Checkpoint
- **Branch Point**：从同一 Checkpoint 探索多种方案

**使用**：
```
# Checkpoints 随每次用户提示自动创建
# 回溯时，按两次 Esc 或使用：
/rewind

# 然后从五个选项中选择：
# 1. 恢复代码和对话
# 2. 仅恢复对话
# 3. 仅恢复代码
# 4. 从此处开始总结
# 5. 不需要了
```

**使用场景**：
- 尝试不同的实现方案
- 从错误中恢复
- 安全实验
- 比较备选方案
- A/B 测试不同设计

**工作流示例**：
```
1. 正常工作（Checkpoints 自动创建）
2. 尝试实验性方案
3. 如果成功：继续
4. 如果失败：按 Esc+Esc 或使用 /rewind 回溯
```

---

## 09. 高级功能

**位置**：[09-advanced-features/](09-advanced-features/)

**是什么**：用于复杂工作流和自动化的高级能力

### Planning Mode（规划模式）

在编码前创建详细的实现计划：
```
用户：/plan 实现用户认证系统

Claude：[创建全面的分步计划]

用户：批准并继续
```

**优势**：清晰的路线图、时间估算、风险评估

### Extended Thinking（扩展思考）

对复杂问题进行深度推理。按 `Alt+T` / `Option+T` 切换，或设置 `MAX_THINKING_TOKENS` 环境变量：
```bash
# 会话内切换：按 Alt+T（macOS 上为 Option+T）

# 或通过环境变量设置
MAX_THINKING_TOKENS=10000 claude

# 然后提问复杂问题
用户：我们应该使用微服务还是单体架构？
Claude：[通过扩展推理系统性地分析权衡]
```

**优势**：更好的架构决策、全面的分析

### Background Tasks（后台任务）

在不阻塞当前工作的情况下运行长时间操作：
```
用户：在后台运行测试

Claude：已启动 bg-1234，你可以继续工作

[稍后] 测试结果：245 通过，3 失败
```

**优势**：并行开发，无需等待

### Permission Modes（权限模式）

控制 Claude 可以执行的操作：
- **`default`**：带有确认提示的标准权限
- **`acceptEdits`**：自动接受文件编辑，其他操作需确认
- **`plan`**：仅分析和规划，不做任何修改
- **`dontAsk`**：无需确认接受所有操作
- **`bypassPermissions`**：跳过所有权限检查（危险）

```bash
claude --permission-mode plan          # 代码审查模式
claude --permission-mode acceptEdits   # 学习模式
claude --permission-mode default       # 标准模式
```

### Headless Mode（无界面模式）

在 CI/CD 和自动化中运行 Claude Code：
```bash
claude -p "运行测试并生成报告"
```

**使用场景**：CI/CD、自动审查、批量处理

### Session Management（会话管理）

管理多个工作会话：
```bash
/resume                          # 交互式恢复之前的会话
/rename                          # 重命名当前会话
/fork                            # 派生当前会话
claude -c                        # 继续最近的会话
claude -r "session"              # 恢复匹配查询的会话
```

### 交互功能

**键盘快捷键**：Ctrl+R（搜索）、Tab（补全）、↑/↓（历史记录）

**命令历史**：访问之前的命令

**多行输入**：跨多行输入的复杂提示词

### 配置

在 `~/.claude/settings.json` 中自定义 Claude Code 行为：
```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Bash(git *)"],
    "deny": ["Bash(rm -rf *)"]
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }]
  },
  "env": {
    "MAX_THINKING_TOKENS": "10000"
  }
}
```

完整配置参见 [config-examples.json](09-advanced-features/config-examples.json)。

---

## 10. CLI 参考

**位置**：[10-cli/](10-cli/)

**是什么**：Claude Code 的完整命令行界面参考

**核心内容**：
- CLI 命令（`claude`、`claude -p`、`claude -c`、`claude -r`）
- 核心标志（打印模式、继续、恢复、版本）
- 模型与配置（`--model`、`--agents`）
- 系统提示词自定义
- 工具与权限管理
- 输出格式（text、JSON、stream-JSON）
- MCP 配置
- 会话管理

**快速示例**：
```bash
# 交互模式
claude "解释这个项目"

# 打印模式（非交互）
claude -p "审查这段代码"

# 处理文件内容
cat error.log | claude -p "解释这个错误"

# 为脚本输出 JSON
claude -p --output-format json "列出所有函数"

# 恢复会话
claude -r "feature-auth" "继续实现"
```

**使用场景**：
- CI/CD 流水线集成
- 脚本自动化与管道操作
- 批量处理
- 多会话工作流
- 自定义 Agent 配置

---

## 目录结构

```

├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md（本文件）
```

---

## 安装快速参考

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints（自动启用，在 settings 中配置）
# 参见 08-checkpoints/README.md

# 高级功能（在 settings 中配置）
# 参见 09-advanced-features/config-examples.json

# CLI 参考（无需安装）
# 参见 10-cli/README.md 中的使用示例
```

---

## 工作流示例

### 1. 完整代码审查工作流

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

用户：/review-pr

Claude：
1. 加载项目 Memory（编码规范）
2. 通过 GitHub MCP 获取 PR
3. 委派给 code-reviewer subagent
4. 委派给 test-engineer subagent
5. 综合发现结果
6. 提供全面的审查报告
```

### 2. 自动化文档生成

```markdown
# 使用：Skills + Subagents + Memory

用户："为 auth 模块生成 API 文档"

Claude：
1. 加载项目 Memory（文档规范）
2. 检测到文档生成请求
3. 自动调用 doc-generator skill
4. 委派给 api-documenter subagent
5. 创建带示例的全面文档
```

### 3. DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

用户：/deploy production

Claude：
1. 运行 pre-deploy hook（验证环境）
2. 委派给 deployment-specialist subagent
3. 通过 Kubernetes MCP 执行部署
4. 监控进度
5. 运行 post-deploy hook（健康检查）
6. 报告状态
```

---

## 最佳实践

### 建议做 ✅
- 从 slash commands 简单开始
- 逐步添加功能
- 使用 Memory 记录团队规范
- 先在本地测试配置
- 为自定义实现编写文档
- 对项目配置进行版本控制
- 与团队共享 Plugins

### 避免做 ❌
- 不要创建冗余功能
- 不要硬编码凭证
- 不要跳过文档
- 不要将简单任务过度复杂化
- 不要忽视安全最佳实践
- 不要提交敏感数据

---

## 故障排查

### 功能未加载
1. 检查文件位置和命名
2. 验证 YAML frontmatter 语法
3. 检查文件权限
4. 确认 Claude Code 版本兼容性

### MCP 连接失败
1. 验证环境变量
2. 检查 MCP 服务器安装
3. 测试凭证有效性
4. 检查网络连接

### Subagent 未委派
1. 检查工具权限
2. 验证 Agent 描述的清晰度
3. 检查任务复杂度
6. 独立测试 Agent

---

## 测试

本项目包含全面的自动化测试，以确保代码质量和可靠性。

### 测试概览

- **单元测试**：使用 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**：使用 Ruff 进行代码检查和格式化
- **安全性**：使用 Bandit 进行漏洞扫描
- **类型检查**：使用 mypy 进行静态类型分析
- **构建验证**：EPUB 生成测试
- **覆盖率追踪**：Codecov 集成

### 本地运行测试

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行所有单元测试
pytest scripts/tests/ -v

# 运行测试并生成覆盖率报告
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行代码质量检查
ruff check scripts/
ruff format --check scripts/

# 运行安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 运行类型检查
mypy scripts/ --ignore-missing-imports
```

### GitHub 自动化测试

测试在以下情况自动运行：
- 每次向 `main` 或 `develop` 分支推送
- 每次向 `main` 发起 Pull Request

在 GitHub Actions 标签页查看测试结果，或查看 [TESTING.md](.github/TESTING.md) 获取详细信息。

### 编写测试

贡献代码时，请为新功能添加测试：

1. 在 `scripts/tests/test_*.py` 中**编写测试**
2. **在本地运行测试**验证是否通过
3. 使用 `pytest --cov=scripts` **检查覆盖率**
4. **随 PR 一起提交** — 所有贡献均需要测试

详细测试指南请参见 [TESTING.md](.github/TESTING.md)。

---

## 更多资源

- [Claude Code 官方文档](https://code.claude.com/docs/en/overview)
- [MCP Protocol 规范](https://modelcontextprotocol.io)
- [Skills 仓库](https://github.com/luongnv89/skills) — 即用型 Skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny 的 Claude Code 工作流](https://x.com/bcherny/status/2007179832300581177) — Claude Code 创始人分享了他的系统化工作流：并行 Agent、共享 CLAUDE.md、Plan 模式、slash commands、subagents 以及用于自主长期运行会话的验证 Hooks。核心见解包括将重复工作流转化为可复用命令，以及将 Claude 接入团队工具（GitHub、Slack、BigQuery、Sentry）实现带反馈循环的端到端工作。

---

## 贡献

发现了问题或想要贡献示例？我们非常欢迎你的参与！

**请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南，包括：**
- 贡献类型（示例、文档、功能、Bug、反馈）
- 如何配置开发环境
- 目录结构及如何添加内容
- 写作规范和最佳实践
- 提交和 PR 流程

**社区规范：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — 社区相处方式
- [SECURITY.md](SECURITY.md) — 安全政策与漏洞报告

### 报告安全问题

如果发现安全漏洞，请负责任地报告：

1. **使用 GitHub 私有漏洞报告**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **请勿**为安全漏洞提交公开 Issue

安全问题将被认真对待并及时处理。完整安全政策请参见 [SECURITY.md](SECURITY.md)。

快速开始：
1. Fork 并克隆仓库
2. 创建描述性分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按照指南进行更改
4. 提交带有清晰描述的 Pull Request

**需要帮助？** 提交 Issue 或讨论，我们会引导你完成整个流程。

---

## 许可证

本项目采用 MIT 许可证——详情请参见 [LICENSE](LICENSE) 文件。

你可以自由地：
- 在你的项目中使用本指南和示例
- 修改和改编内容
- 分享和传播
- 用于商业目的

唯一的要求是包含一份许可证和版权声明副本。

---

## EPUB 生成

想要离线阅读本指南？生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

这将创建包含所有内容（含渲染后的 Mermaid 图表）的 `claude-howto-guide.epub`。

更多选项请参见 [scripts/README.md](scripts/README.md)。

---

## 贡献者

感谢所有为本项目做出贡献的人！

| 贡献者 | PR |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - 添加 EPUB 创建工具](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): 在概念指南的嵌套代码块中使用波浪线围栏](https://github.com/luongnv89/claude-howto/pull/7) |

---

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

**最后更新**：2026 年 3 月
**Claude Code 版本**：2.1+
**兼容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
