<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude 核心概念完整指南（中文）

> 进度说明：本文件为中文转译进行中版本。当前已完成 **Slash Commands / Subagents / Memory** 三个章节，后续章节将继续分批补齐。

一份覆盖 Slash Commands、Subagents、Memory、MCP Protocol、Agent Skills 等能力的综合参考指南，包含表格、架构图与实战示例。

---

## 目录

1. [Slash Commands](#slash-commands)
2. [Subagents](#subagents)
3. [Memory](#memory)
4. [MCP Protocol](#mcp-protocol)
5. [Agent Skills](#agent-skills)
6. [Plugins](#claude-code-plugins)
7. [Hooks](#hooks)
8. [Checkpoints and Rewind](#checkpoints-and-rewind)
9. [Advanced Features](#advanced-features)
10. [Comparison & Integration](#comparison--integration)

---

## Slash Commands

### 概览

Slash commands 是由用户手动触发的快捷指令，以 Markdown 文件形式保存并由 Claude Code 执行。它能帮助团队标准化高频提示词与工作流。

### 架构

```mermaid
graph TD
    A["User Input: /command-name"] -->|Triggers| B["Search .claude/commands/"]
    B -->|Finds| C["command-name.md"]
    C -->|Loads| D["Markdown Content"]
    D -->|Executes| E["Claude Processes Prompt"]
    E -->|Returns| F["Result in Context"]
```

### 文件结构

```mermaid
graph LR
    A["Project Root"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### 命令组织表

| Location | Scope | Availability | Use Case | Git Tracked |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | Project-specific | Team members | Team workflows, shared standards | ✅ Yes |
| `~/.claude/commands/` | Personal | Individual user | Personal shortcuts across projects | ❌ No |
| Subdirectories | Namespaced | Based on parent | Organize by category | ✅ Yes |

### 能力与特性

| Feature | Example | Supported |
|---------|---------|-----------|
| Shell script execution | `bash scripts/deploy.sh` | ✅ Yes |
| File references | `@path/to/file.js` | ✅ Yes |
| Bash integration | `$(git log --oneline)` | ✅ Yes |
| Arguments | `/pr --verbose` | ✅ Yes |
| MCP commands | `/mcp__github__list_prs` | ✅ Yes |

### 实战示例

#### 示例 1：代码优化命令

**File:** `.claude/commands/optimize.md`

```markdown
---
name: Code Optimization
description: Analyze code for performance issues and suggest optimizations
tags: performance, analysis
---

# Code Optimization

Review the provided code for the following issues in order of priority:

1. **Performance bottlenecks** - identify O(n²) operations, inefficient loops
2. **Memory leaks** - find unreleased resources, circular references
3. **Algorithm improvements** - suggest better algorithms or data structures
4. **Caching opportunities** - identify repeated computations
5. **Concurrency issues** - find race conditions or threading problems

Format your response with:
- Issue severity (Critical/High/Medium/Low)
- Location in code
- Explanation
- Recommended fix with code example
```

**Usage:**
```bash
# User types in Claude Code
/optimize

# Claude loads the prompt and waits for code input
```

#### 示例 2：PR 辅助命令

**File:** `.claude/commands/pr.md`

```markdown
---
name: Prepare Pull Request
description: Clean up code, stage changes, and prepare a pull request
tags: git, workflow
---

# Pull Request Preparation Checklist

Before creating a PR, execute these steps:

1. Run linting: `prettier --write .`
2. Run tests: `npm test`
3. Review git diff: `git diff HEAD`
4. Stage changes: `git add .`
5. Create commit message following conventional commits:
   - `fix:` for bug fixes
   - `feat:` for new features
   - `docs:` for documentation
   - `refactor:` for code restructuring
   - `test:` for test additions
   - `chore:` for maintenance

6. Generate PR summary including:
   - What changed
   - Why it changed
   - Testing performed
   - Potential impacts
```

#### 示例 3：分层文档生成命令

**File:** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: Generate API Documentation
description: Create comprehensive API documentation from source code
tags: documentation, api
---

# API Documentation Generator

Generate API documentation by:

1. Scanning all files in `/src/api/`
2. Extracting function signatures and JSDoc comments
3. Organizing by endpoint/module
4. Creating markdown with examples
5. Including request/response schemas
6. Adding error documentation

Output format:
- Markdown file in `/docs/api.md`
- Include curl examples for all endpoints
- Add TypeScript types
```

### 命令生命周期

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: Types /optimize
    Claude->>FS: Searches .claude/commands/
    FS-->>Claude: Returns optimize.md
    Claude->>Claude: Loads Markdown content
    Claude->>User: Displays prompt context
    User->>Claude: Provides code to analyze
    Claude->>CLI: (May execute scripts)
    CLI-->>Claude: Results
    Claude->>User: Returns analysis
```

### 最佳实践

| ✅ Do | ❌ Don't |
|------|---------|
| 使用清晰、动作导向的命名 | 为一次性任务创建命令 |
| 在 description 中写清触发词 | 把复杂逻辑塞进命令文件 |
| 一个命令聚焦一个任务 | 创建重复命令 |
| 项目命令纳入版本控制 | 硬编码敏感信息 |
| 通过子目录组织命令 | 做冗长命令清单 |
| 提示词尽量简洁可读 | 使用晦涩缩写表达 |

---

## Subagents

### 概览

Subagents 是具备独立上下文窗口和定制系统提示词的专用 AI 助手。它支持将任务委派给不同角色，同时保持关注点分离。

### 架构图

```mermaid
graph TB
    User["👤 User"]
    Main["🎯 Main Agent<br/>(Coordinator)"]
    Reviewer["🔍 Code Reviewer<br/>Subagent"]
    Tester["✅ Test Engineer<br/>Subagent"]
    Docs["📝 Documentation<br/>Subagent"]

    User -->|asks| Main
    Main -->|delegates| Reviewer
    Main -->|delegates| Tester
    Main -->|delegates| Docs
    Reviewer -->|returns result| Main
    Tester -->|returns result| Main
    Docs -->|returns result| Main
    Main -->|synthesizes| User
```

### Subagent 生命周期

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Separate<br/>Context Window

    User->>MainAgent: "Build new auth feature"
    MainAgent->>MainAgent: Analyze task
    MainAgent->>CodeReviewer: "Review this code"
    CodeReviewer->>Context: Initialize clean context
    Context->>CodeReviewer: Load reviewer instructions
    CodeReviewer->>CodeReviewer: Perform review
    CodeReviewer-->>MainAgent: Return findings
    MainAgent->>MainAgent: Incorporate results
    MainAgent-->>User: Provide synthesis
```

### 配置字段

| Configuration | Type | Purpose | Example |
|---------------|------|---------|---------|
| `name` | String | Agent identifier | `code-reviewer` |
| `description` | String | Purpose & trigger terms | `Comprehensive code quality analysis` |
| `tools` | List/String | Allowed capabilities | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | Behavioral instructions | Custom guidelines |

### 工具权限层级

```mermaid
graph TD
    A["Subagent Configuration"] -->|Option 1| B["Inherit All Tools<br/>from Main Thread"]
    A -->|Option 2| C["Specify Individual Tools"]
    B -->|Includes| B1["File Operations"]
    B -->|Includes| B2["Shell Commands"]
    B -->|Includes| B3["MCP Tools"]
    C -->|Explicit List| C1["read, grep, diff"]
    C -->|Explicit List| C2["Bash(npm:*), Bash(test:*)"]
```

### 何时使用 Subagents

| Scenario | Use Subagent | Why |
|----------|--------------|-----|
| 复杂功能含多个步骤 | ✅ Yes | 关注点分离，避免上下文污染 |
| 快速小型 code review | ❌ No | 额外开销不划算 |
| 并行任务执行 | ✅ Yes | 每个子代理拥有独立上下文 |
| 需要专项能力 | ✅ Yes | 可通过 system prompt 定制 |
| 长时间分析任务 | ✅ Yes | 避免主上下文耗尽 |
| 单一步骤任务 | ❌ No | 增加不必要延迟 |

### Agent Teams

Agent Teams 用于编排多个代理协同完成同一目标。与“逐个委派单个 subagent”不同，Agent Teams 更适合大规模任务（例如前后端并行开发 + 测试并行验证）。

---

## Memory

### 概览

Memory 让 Claude 能跨会话保留上下文。主要有两种形态：
- claude.ai 的自动摘要记忆
- Claude Code 基于文件系统的 `CLAUDE.md`

### Memory 架构

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|User provides info| C
    C -->|Synthesizes every 24h| D
    D -->|Loads automatically| A
    A -->|Uses context| C
```

### Claude Code 的 Memory 层级（7 层）

Claude Code 会按优先级从高到低加载 7 层记忆：

```mermaid
graph TD
    A["1. Managed Policy<br/>Enterprise admin policies"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>Automatically captured preferences"]
```

### Memory 位置对照

| Tier | Location | Scope | Priority | Shared | Best For |
|------|----------|-------|----------|--------|----------|
| 1. Managed Policy | Enterprise admin | Organization | Highest | All org users | 合规与安全策略 |
| 2. Project | `./CLAUDE.md` | Project | High | Team (Git) | 团队标准、架构约定 |
| 3. Project Rules | `.claude/rules/*.md` | Project | High | Team (Git) | 模块化项目规则 |
| 4. User | `~/.claude/CLAUDE.md` | Personal | Medium | Individual | 个人偏好 |
| 5. User Rules | `~/.claude/rules/*.md` | Personal | Medium | Individual | 个人规则模块 |
| 6. Local | `.claude/local/CLAUDE.md` | Local | Low | Not shared | 本机特定设置 |
| 7. Auto Memory | Automatic | Session | Lowest | Individual | 学习到的偏好与模式 |

### Auto Memory

Auto Memory 会在会话中自动学习并记住：
- 代码风格偏好
- 你常做的纠正
- 常用框架与工具选择
- 沟通表达偏好

### Memory 功能对比

| Feature | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| Auto-synthesis | ✅ Every 24h | ❌ Manual |
| Cross-project | ✅ Shared | ❌ Project-specific |
| Team access | ✅ Shared projects | ✅ Git-tracked |
| Searchable | ✅ Built-in | ✅ Through `/memory` |
| Editable | ✅ In-chat | ✅ Direct file edit |
| Import/Export | ✅ Yes | ✅ Copy/paste |
| Persistent | ✅ 24h+ | ✅ Indefinite |

---

## MCP Protocol

### 概览

MCP（Model Context Protocol）是 Claude 访问外部工具、API 与实时数据源的标准协议。与 Memory 不同，MCP 提供的是**实时变化数据**访问能力。

### MCP 架构

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A
```

### MCP 生态

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]
```

### MCP 配置流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

### 常见 MCP Server

| MCP Server | Purpose | Common Tools | Auth | Real-time |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 文件操作 | read, write, delete | OS permissions | ✅ Yes |
| **GitHub** | 仓库管理 | list_prs, create_issue, push | OAuth | ✅ Yes |
| **Slack** | 团队沟通 | send_message, list_channels | Token | ✅ Yes |
| **Database** | SQL 查询 | query, insert, update | Credentials | ✅ Yes |
| **Google Docs** | 文档访问 | read, write, share | OAuth | ✅ Yes |
| **Asana** | 项目管理 | create_task, update_status | API Key | ✅ Yes |
| **Stripe** | 支付数据 | list_charges, create_invoice | API Key | ✅ Yes |
| **Memory** | 持久存储 | store, retrieve, delete | Local | ❌ No |

### 实战示例

#### 示例 1：GitHub MCP 配置

**File:** `.mcp.json`（项目级）或 `~/.claude.json`（用户级）

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

#### 示例 2：Database MCP

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.
```

#### 示例 3：多 MCP 串联工作流

场景：日报生成（GitHub + Database + Slack + Filesystem）

1. 从 GitHub 拉取 PR 指标
2. 从数据库查询业务数据
3. 生成报告并写入文件
4. 推送摘要到 Slack

### MCP 与 Memory 选型

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]
```

---

## Agent Skills

### 概览

Agent Skills 是可复用、由模型自动调用的能力包。通常以目录形式组织，包含说明、脚本和模板资源。

### Skill 架构

```mermaid
graph TB
    A["Skill Directory"]
    B["SKILL.md"]
    C["YAML Metadata"]
    D["Instructions"]
    E["Scripts"]
    F["Templates"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### 加载流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude
    participant System as System
    participant Skill as Skill

    User->>Claude: "Create Excel report"
    Claude->>System: Scan available skills
    System->>System: Load skill metadata
    Claude->>Claude: Match user request to skills
    Claude->>Skill: Load xlsx skill SKILL.md
    Skill-->>Claude: Return instructions + tools
    Claude->>Claude: Execute skill
    Claude->>User: Generate Excel file
```

### Skill 类型与位置

| Type | Location | Scope | Shared | Sync | Best For |
|------|----------|-------|--------|------|----------|
| Pre-built | Built-in | Global | All users | Auto | 文档生成等通用能力 |
| Personal | `~/.claude/skills/` | Individual | No | Manual | 个人自动化 |
| Project | `.claude/skills/` | Team | Yes | Git | 团队规范与流程 |
| Plugin | Via plugin install | Varies | Depends | Auto | 组合式能力包 |

### Bundled Skills（内置）

Claude Code 当前包含 5 个内置技能：

| Skill | Command | Purpose |
|-------|---------|---------|
| **Simplify** | `/simplify` | 简化复杂代码或说明 |
| **Batch** | `/batch` | 批量处理多个文件/对象 |
| **Debug** | `/debug` | 系统化根因分析 |
| **Loop** | `/loop` | 定时循环任务 |
| **Claude API** | `/claude-api` | 直接调用 Anthropic API |

### 何时用 Skill

- 同类任务重复出现
- 需要固定流程/模板
- 需要“自动触发”而不是手动输入命令

---

## Claude Code Plugins

### 概览

Plugins 是更高层级的扩展机制：把 slash commands、subagents、MCP servers、hooks 等能力打包后一次安装。

### 架构

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|bundles| B
    A -->|bundles| C
    A -->|bundles| D
    A -->|bundles| E
    A -->|bundles| F
```

### 插件安装流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: Download plugin manifest
    Plugin-->>Claude: Return plugin definition
    Claude->>Install: Extract components
    Install-->>Claude: Plugin installed ✅
```

### 插件类型

| Type | Scope | Shared | Authority | Examples |
|------|-------|--------|-----------|----------|
| Official | Global | All users | Anthropic | PR Review, Security Guidance |
| Community | Public | All users | Community | DevOps, Data Science |
| Organization | Internal | Team members | Company | Internal standards, tools |
| Personal | Individual | Single user | Developer | 自定义工作流 |

### Plugin 与其他能力对比

| Feature | Slash Command | Skill | Subagent | Plugin |
|---------|---------------|-------|----------|--------|
| 安装方式 | 手动复制 | 手动复制 | 手动配置 | 一条命令 |
| 配置时间 | 低 | 中 | 中 | 最低 |
| 组件打包 | 单文件 | 单文件 | 单文件 | 多组件 |
| 更新机制 | 手动 | 手动 | 手动 | 集中更新 |
| 团队分发 | 一般 | 一般 | 一般 | 最佳 |

### 何时应该做成插件

- 需要组合多种能力（commands + agents + MCP + hooks）
- 需要团队快速一致安装
- 需要版本化分发和持续更新

---

## Hooks

### 概览

Hooks 是事件驱动的自动命令。Claude Code 在特定事件触发时执行对应 hook，可用于自动化、校验、通知与治理。

### Hook 事件（25 个）

Claude Code 当前支持 **25 个 Hook 事件**，覆盖 command/http/prompt/agent 四类。

常见事件包括：`SessionStart`、`UserPromptSubmit`、`PreToolUse`、`PostToolUse`、`SubagentStart`、`Stop`、`TaskCreated`、`TaskCompleted`、`ConfigChange`、`FileChanged`、`SessionEnd` 等。

### 配置示例

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "eslint $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### 常用环境变量

- `$CLAUDE_FILE_PATH`：正在写入/编辑的文件路径
- `$CLAUDE_TOOL_NAME`：当前工具名
- `$CLAUDE_SESSION_ID`：会话 ID
- `$CLAUDE_PROJECT_DIR`：项目目录

### 最佳实践

✅ 建议：
- Hook 保持快速（建议 < 1 秒）
- 用于校验和自动化收尾动作
- 做好错误容错
- 使用绝对路径

❌ 不建议：
- 在 Hook 中做人机交互
- 在 Hook 内跑超长任务
- 硬编码密钥

---

## Checkpoints and Rewind

### 概览

Checkpoint 可以保存当前会话状态，并在需要时回退（rewind）到历史节点，适合安全试错和方案分支探索。

### 核心概念

| Concept | Description |
|---------|-------------|
| **Checkpoint** | 会话快照（消息、文件、上下文） |
| **Rewind** | 回到旧快照并丢弃之后的改动 |
| **Branch Point** | 用于分叉探索不同方案的关键节点 |

### 如何使用

```bash
Esc + Esc
# 或
/rewind
```

回退时可选：
1. Restore code and conversation
2. Restore conversation
3. Restore code
4. Summarize from here
5. Never mind

### 典型场景

- 大重构前先打点，失败即回滚
- A/B 两种实现方案并行试验
- 出现误改后快速恢复到可用状态

---

## Advanced Features

### Planning Mode

先规划后执行，适合复杂任务。

```bash
/plan Implement user authentication system
```

### Extended Thinking

在复杂问题上使用更深推理：

- `Option+T`（macOS）/ `Alt+T`（Windows/Linux）切换
- 也可通过 `MAX_THINKING_TOKENS` 调整预算

### Background Tasks

后台执行长任务，不阻塞当前对话：

```bash
/task list
/task status <id>
/task show <id>
/task cancel <id>
```

### Permission Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| `default` | 标准权限，敏感操作会询问 | 日常开发 |
| `acceptEdits` | 自动接受文件编辑 | 可信编辑流 |
| `plan` | 只分析和规划，不改文件 | 评审/设计 |
| `auto` | 自动放行安全动作，风险动作再问 | 平衡型 |
| `dontAsk` | 尽量不询问直接执行 | 自动化场景 |
| `bypassPermissions` | 完全放开权限 | 受控 CI 场景 |

### Headless / Print Mode

```bash
claude -p "Run all tests"
cat error.log | claude -p "explain this error"
claude -p --output-format json "list all functions in src/"
```

### Scheduled Tasks

```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

### Session Management

```bash
/resume
/rename "Feature"
/fork
claude -c
claude -r "Feature"
```

---

## Comparison & Integration

### 能力对比矩阵

| Feature | Invocation | Persistence | Scope | Use Case |
|---------|-----------|------------|-------|----------|
| **Slash Commands** | Manual (`/cmd`) | Session only | 单命令 | 快捷触发 |
| **Subagents** | Auto-delegated | Isolated context | 专项任务 | 任务分工 |
| **Memory** | Auto-loaded | Cross-session | 用户/团队上下文 | 长期记忆 |
| **MCP Protocol** | Auto-queried | Real-time external | 实时外部数据 | 动态信息 |
| **Skills** | Auto-invoked | Filesystem-based | 可复用能力 | 自动化流程 |
| **Plugins** | Install once | 组合能力 | 团队级分发 | 标准化落地 |

### 组合建议

- **快速启动**：Slash Commands + Memory
- **团队自动化**：Skills + Hooks + MCP
- **复杂工程**：Subagents + Planning Mode + Checkpoints
- **企业治理**：Plugins + Managed Settings + Hook 审计

### 选择决策（简化）

```mermaid
graph TD
    A["Need to extend Claude?"] --> B{"Task type"}
    B -->|Repeated manual task| C["Slash Command"]
    B -->|Auto reusable capability| D["Skill"]
    B -->|Need live external data| E["MCP"]
    B -->|Need cross-session context| F["Memory"]
    B -->|Multi-role complex task| G["Subagents"]
    B -->|Team-wide packaged workflow| H["Plugin"]
```

---

## Resources

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Anthropic Documentation](https://docs.anthropic.com)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*Last updated: March 2026*
*For Claude Haiku 4.5, Sonnet 4.6, and Opus 4.6*
