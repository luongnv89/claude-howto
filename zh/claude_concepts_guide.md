<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Concepts 完整指南

这是一份全面的参考指南，覆盖 Slash Commands、Subagents、Memory、MCP Protocol、Agent Skills、Plugins、Hooks、Checkpoints、Advanced Features 等 Claude Code 核心概念，并配有表格、图示和实践示例。

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

Slash commands 是由用户手动触发的快捷命令，以 Markdown 文件形式保存，Claude Code 可以读取并执行。它们非常适合把高频提示词与工作流标准化，方便团队复用。

### 架构

```mermaid
graph TD
    A["用户输入: /command-name"] -->|触发| B["搜索 .claude/commands/"]
    B -->|找到| C["command-name.md"]
    C -->|加载| D["Markdown 内容"]
    D -->|执行| E["Claude 处理提示"]
    E -->|返回| F["上下文中的结果"]
```

### 文件结构

```mermaid
graph LR
    A["项目根目录"] -->|包含| B[".claude/commands/"]
    B -->|包含| C["optimize.md"]
    B -->|包含| D["test.md"]
    B -->|包含| E["docs/"]
    E -->|包含| F["generate-api-docs.md"]
    E -->|包含| G["generate-readme.md"]
```

### 命令组织表

| 位置 | 作用域 | 可用范围 | 适用场景 | Git 跟踪 |
|------|--------|----------|----------|-----------|
| `.claude/commands/` | 项目级 | 团队成员 | 团队工作流、共享标准 | ✅ 是 |
| `~/.claude/commands/` | 个人级 | 当前用户 | 跨项目的个人快捷命令 | ❌ 否 |
| 子目录 | 命名空间 | 取决于父目录 | 按类别组织命令 | ✅ 是 |

### 功能与能力

| 功能 | 示例 | 是否支持 |
|------|------|----------|
| Shell 脚本执行 | `bash scripts/deploy.sh` | ✅ 是 |
| 文件引用 | `@path/to/file.js` | ✅ 是 |
| Bash 集成 | `$(git log --oneline)` | ✅ 是 |
| 参数 | `/pr --verbose` | ✅ 是 |
| MCP 命令 | `/mcp__github__list_prs` | ✅ 是 |

### 实践示例

#### 示例 1：代码优化命令

**文件：** `.claude/commands/optimize.md`

```markdown
---
name: 代码优化
description: 分析代码中的性能问题并给出优化建议
tags: performance, analysis
---

# 代码优化

请按以下优先级顺序审查给定代码中的问题：

1. **性能瓶颈** - 识别 O(n²) 操作、低效循环
2. **内存泄漏** - 查找未释放资源、循环引用
3. **算法改进** - 建议更优算法或数据结构
4. **缓存机会** - 识别重复计算
5. **并发问题** - 查找竞态条件或线程问题

请按以下格式输出：
- 问题严重级别（Critical/High/Medium/Low）
- 代码位置
- 解释说明
- 带代码示例的修复建议
```

**使用方式：**
```bash
# 用户在 Claude Code 中输入
/optimize

# Claude 加载提示并等待代码输入
```

#### 示例 2：Pull Request 辅助命令

**文件：** `.claude/commands/pr.md`

```markdown
---
name: 准备 Pull Request
description: 清理代码、暂存改动并准备一个 Pull Request
tags: git, workflow
---

# Pull Request 准备清单

在创建 PR 前，执行以下步骤：

1. 运行 lint：`prettier --write .`
2. 运行测试：`npm test`
3. 查看 git diff：`git diff HEAD`
4. 暂存改动：`git add .`
5. 按 conventional commits 规则编写提交信息：
   - `fix:` 用于 bug 修复
   - `feat:` 用于新功能
   - `docs:` 用于文档更新
   - `refactor:` 用于代码重构
   - `test:` 用于补充测试
   - `chore:` 用于维护性工作

6. 生成 PR 摘要，包括：
   - 改了什么
   - 为什么改
   - 做了哪些测试
   - 可能的影响
```

**使用方式：**
```bash
/pr

# Claude 按清单逐项检查并准备 PR
```

#### 示例 3：分层式文档生成器

**文件：** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: 生成 API 文档
description: 基于源代码生成完整 API 文档
tags: documentation, api
---

# API 文档生成器

通过以下步骤生成 API 文档：

1. 扫描 `/src/api/` 下的所有文件
2. 提取函数签名和 JSDoc 注释
3. 按 endpoint / module 组织结构
4. 生成带示例的 Markdown
5. 包含请求 / 响应 schema
6. 补充错误文档

输出格式：
- 输出 Markdown 文件到 `/docs/api.md`
- 为所有端点包含 curl 示例
- 补充 TypeScript 类型
```

### 命令生命周期图

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: 输入 /optimize
    Claude->>FS: 搜索 .claude/commands/
    FS-->>Claude: 返回 optimize.md
    Claude->>Claude: 加载 Markdown 内容
    Claude->>User: 显示提示上下文
    User->>Claude: 提供待分析代码
    Claude->>CLI: （可能执行脚本）
    CLI-->>Claude: 返回结果
    Claude->>User: 输出分析
```

### 最佳实践

| ✅ 建议 | ❌ 不建议 |
|------|---------|
| 使用清晰、面向动作的命名 | 为一次性任务创建命令 |
| 在描述中写清触发场景 | 在命令里堆复杂逻辑 |
| 保持命令聚焦单一任务 | 创建重复命令 |
| 将项目命令纳入版本控制 | 硬编码敏感信息 |
| 使用子目录组织分类 | 做过长的命令列表 |
| 使用简单、可读的提示词 | 使用晦涩或过度缩写的措辞 |

---

## Subagents

### 概览

Subagents 是带有隔离上下文窗口和自定义系统提示词的专门化 AI 助手。它们让 Claude 能够把复杂任务拆分并委派出去，同时保持关注点清晰分离。

### 架构图

```mermaid
graph TB
    User["👤 用户"]
    Main["🎯 主 Agent<br/>(协调者)"]
    Reviewer["🔍 代码审查<br/>Subagent"]
    Tester["✅ 测试工程师<br/>Subagent"]
    Docs["📝 文档编写<br/>Subagent"]

    User -->|提出请求| Main
    Main -->|委派| Reviewer
    Main -->|委派| Tester
    Main -->|委派| Docs
    Reviewer -->|返回结果| Main
    Tester -->|返回结果| Main
    Docs -->|返回结果| Main
    Main -->|汇总| User
```

### Subagent 生命周期

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as 主 Agent
    participant CodeReviewer as 代码审查<br/>Subagent
    participant Context as 独立的<br/>上下文窗口

    User->>MainAgent: “构建新的认证功能”
    MainAgent->>MainAgent: 分析任务
    MainAgent->>CodeReviewer: “审查这段代码”
    CodeReviewer->>Context: 初始化干净上下文
    Context->>CodeReviewer: 加载审查规则
    CodeReviewer->>CodeReviewer: 执行审查
    CodeReviewer-->>MainAgent: 返回发现
    MainAgent->>MainAgent: 融合结果
    MainAgent-->>User: 输出综合结论
```

### Subagent 配置表

| 配置项 | 类型 | 作用 | 示例 |
|--------|------|------|------|
| `name` | String | Agent 标识符 | `code-reviewer` |
| `description` | String | 用途与触发词 | `Comprehensive code quality analysis` |
| `tools` | List/String | 允许的能力 | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | 行为指令 | 自定义规范 |

### 工具访问层级

```mermaid
graph TD
    A["Subagent 配置"] -->|选项 1| B["继承主线程的全部工具"]
    A -->|选项 2| C["显式指定工具"]
    B -->|包含| B1["文件操作"]
    B -->|包含| B2["Shell 命令"]
    B -->|包含| B3["MCP 工具"]
    C -->|显式列表| C1["read, grep, diff"]
    C -->|显式列表| C2["Bash(npm:*), Bash(test:*)"]
```

### 实践示例

#### 示例 1：完整 Subagent 配置

**文件：** `.claude/agents/code-reviewer.md`

```yaml
---
name: code-reviewer
description: Comprehensive code quality and maintainability analysis
tools: read, grep, diff, lint_runner
---

# Code Reviewer Agent

You are an expert code reviewer specializing in:
- Performance optimization
- Security vulnerabilities
- Code maintainability
- Testing coverage
- Design patterns

## Review Priorities (in order)

1. **Security Issues** - Authentication, authorization, data exposure
2. **Performance Problems** - O(n²) operations, memory leaks, inefficient queries
3. **Code Quality** - Readability, naming, documentation
4. **Test Coverage** - Missing tests, edge cases
5. **Design Patterns** - SOLID principles, architecture

## Review Output Format

针对每个问题：
- **Severity**: Critical / High / Medium / Low
- **Category**: Security / Performance / Quality / Testing / Design
- **Location**: File path and line number
- **Issue Description**: What's wrong and why
- **Suggested Fix**: Code example
- **Impact**: How this affects the system
```

**文件：** `.claude/agents/test-engineer.md`

```yaml
---
name: test-engineer
description: Test strategy, coverage analysis, and automated testing
tools: read, write, bash, grep
---

# Test Engineer Agent

You are expert at:
- Writing comprehensive test suites
- Ensuring high code coverage (>80%)
- Testing edge cases and error scenarios
- Performance benchmarking
- Integration testing
```

**文件：** `.claude/agents/documentation-writer.md`

```yaml
---
name: documentation-writer
description: Technical documentation, API docs, and user guides
tools: read, write, grep
---

# Documentation Writer Agent

You create:
- API documentation with examples
- User guides and tutorials
- Architecture documentation
- Changelog entries
- Code comment improvements
```

#### 示例 2：Subagent 委派流程

```markdown
# 场景：构建支付功能

## 用户请求
"构建一个与 Stripe 集成的安全支付处理功能"

## 主 Agent 工作流

1. **规划阶段**
   - 理解需求
   - 确定所需任务
   - 规划架构

2. **委派给 Code Reviewer Subagent**
   - 任务："审查支付处理实现中的安全问题"
   - 上下文：认证、API 密钥、token 处理
   - 重点：SQL 注入、密钥泄露、HTTPS 强制

3. **委派给 Test Engineer Subagent**
   - 任务："为支付流程创建完整测试"
   - 上下文：成功场景、失败场景、边界情况
   - 输出：有效支付、拒付、网络故障、webhook 测试

4. **委派给 Documentation Writer Subagent**
   - 任务："为支付 API 端点编写文档"
   - 上下文：请求 / 响应 schema
   - 产出：带 curl 示例和错误码的 API 文档

5. **综合**
   - 主 Agent 汇总所有输出
   - 整合发现
   - 返回完整方案给用户
```

#### 示例 3：工具权限范围

**受限配置：只允许特定能力**

```yaml
---
name: secure-reviewer
description: Security-focused code review with minimal permissions
tools: read, grep
---

# Secure Code Reviewer

Reviews code for security vulnerabilities only.
```

**扩展配置：为实现任务开放全部工具**

```yaml
---
name: implementation-agent
description: Full implementation capabilities for feature development
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

Builds features from specifications.
```

### Subagent 上下文管理

```mermaid
graph TB
    A["主 Agent 上下文<br/>50,000 tokens"]
    B["Subagent 1 上下文<br/>20,000 tokens"]
    C["Subagent 2 上下文<br/>20,000 tokens"]
    D["Subagent 3 上下文<br/>20,000 tokens"]

    A -->|干净上下文| B
    A -->|干净上下文| C
    A -->|干净上下文| D

    B -->|仅返回结果| A
    C -->|仅返回结果| A
    D -->|仅返回结果| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### 何时使用 Subagents

| 场景 | 是否使用 Subagent | 原因 |
|------|------------------|------|
| 多步骤复杂功能 | ✅ 是 | 分离关注点，防止上下文污染 |
| 快速代码审查 | ❌ 否 | 开销不值得 |
| 并行任务执行 | ✅ 是 | 每个 subagent 都有自己的上下文 |
| 需要专业化角色 | ✅ 是 | 可以用自定义系统提示词 |
| 长时间分析任务 | ✅ 是 | 防止主上下文耗尽 |
| 单一步骤任务 | ❌ 否 | 只会增加延迟 |

### Agent Teams

Agent Teams 用于协调多个 agent 围绕一个共同目标协作。与一次只委派一个 subagent 不同，Agent Teams 允许主 agent 编排一组协作代理，在共享中间结果的同时并行推进大任务，例如由前端 agent、后端 agent、测试 agent 一起完成一个全栈功能。

---

## Memory

### 概览

Memory 让 Claude 能够在不同会话和对话之间保留上下文。它主要有两种形态：Claude Web/Desktop 中的自动记忆综合，以及 Claude Code 中基于文件系统的 `CLAUDE.md`。

### Memory 架构

```mermaid
graph TB
    A["Claude 会话"]
    B["用户输入"]
    C["记忆系统"]
    D["记忆存储"]

    B -->|用户提供信息| C
    C -->|每 24 小时综合| D
    D -->|自动加载| A
    A -->|使用上下文| C
```

### Claude Code 中的 7 层记忆层级

Claude Code 会按优先级从高到低加载 7 层记忆：

```mermaid
graph TD
    A["1. Managed Policy<br/>企业管理员策略"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>自动捕获的偏好"]
```

### Memory 位置表

| 层级 | 位置 | 作用域 | 优先级 | 是否共享 | 最适合 |
|------|------|--------|--------|----------|--------|
| 1. Managed Policy | 企业管理员 | 组织级 | 最高 | 全组织用户 | 合规、安全策略 |
| 2. Project | `./CLAUDE.md` | 项目级 | 高 | 团队（Git） | 团队标准、架构 |
| 3. Project Rules | `.claude/rules/*.md` | 项目级 | 高 | 团队（Git） | 模块化项目约定 |
| 4. User | `~/.claude/CLAUDE.md` | 个人级 | 中 | 个人 | 个人偏好 |
| 5. User Rules | `~/.claude/rules/*.md` | 个人级 | 中 | 个人 | 个人规则模块 |
| 6. Local | `.claude/local/CLAUDE.md` | 本地 | 低 | 不共享 | 机器相关设置 |
| 7. Auto Memory | 自动生成 | 会话级 | 最低 | 个人 | 学到的偏好与模式 |

### Auto Memory

Auto Memory 会在会话中自动捕获用户偏好与行为模式。Claude 会记住：

- 代码风格偏好
- 你常做的纠正
- 框架和工具选择
- 沟通方式偏好

它在后台工作，不需要手动配置。

### Memory 更新生命周期

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: “记住：统一使用 async/await”
    Claude->>User: “写入哪个记忆文件？”
    User->>Claude: “项目记忆”
    Claude->>Editor: 打开 ~/.claude/settings.json
    Claude->>Memory: 写入 ./CLAUDE.md
    Memory-->>Claude: 文件已保存
    Claude->>Claude: 重新加载记忆
    Claude-->>User: “记忆已保存！”
```

### 实践示例

#### 示例 1：项目级记忆结构

**文件：** `./CLAUDE.md`

```markdown
# 项目配置

## 项目概览
- **名称**：电商平台
- **技术栈**：Node.js、PostgreSQL、React 18、Docker
- **团队规模**：5 名开发者
- **截止时间**：2025 年第 4 季度

## 架构
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## 开发标准

### Code Style
- 使用 Prettier 格式化
- 使用 ESLint + airbnb config
- 最大行宽 100 字符
- 使用 2 空格缩进

### Naming Conventions
- **文件**：kebab-case
- **类**：PascalCase
- **函数/变量**：camelCase
- **常量**：UPPER_SNAKE_CASE
- **数据库表**：snake_case
```

#### 示例 2：目录级记忆

**文件：** `./src/api/CLAUDE.md`

~~~~markdown
# API 模块标准

该文件会覆盖根目录 `CLAUDE.md` 中对 `/src/api/` 的规则。

## API 专属标准

### Request Validation
- 使用 Zod 做 schema 校验
- 所有输入都必须校验
- 校验失败时返回 400
- 包含字段级错误详情

### Authentication
- 所有端点都要求 JWT token
- Token 通过 Authorization header 传递
- Token 24 小时过期
- 实现 refresh token 机制
~~~~

#### 示例 3：个人记忆

**文件：** `~/.claude/CLAUDE.md`

~~~~markdown
# 我的开发偏好

## About Me
- **经验水平**：8 年全栈开发
- **偏好语言**：TypeScript、Python
- **沟通风格**：直接、配示例
- **学习风格**：喜欢图示和代码配合

## Code Preferences

### Error Handling
我偏好显式的 try-catch 和清晰的错误信息。
避免泛化错误，调试时始终记录日志。
~~~~

#### 示例 4：会话中更新记忆

```markdown
User: 记住：所有新组件都优先使用 React hooks，不用 class components。

Claude: 我会把它加入记忆。你希望写入哪个记忆文件？
        1. 项目记忆（./CLAUDE.md）
        2. 个人记忆（~/.claude/CLAUDE.md）

User: 项目记忆

Claude: ✅ 记忆已保存！
```

### Claude Web/Desktop 中的记忆综合

#### 记忆综合时间线

```mermaid
graph LR
    A["第 1 天：用户对话"] -->|24 小时| B["第 2 天：记忆综合"]
    B -->|自动| C["记忆更新并摘要化"]
    C -->|加载到| D["第 2-N 天：新对话"]
```

### Memory 功能对比

| 功能 | Claude Web/Desktop | Claude Code (`CLAUDE.md`) |
|------|--------------------|---------------------------|
| 自动综合 | ✅ 每 24 小时 | ❌ 手动 |
| 跨项目 | ✅ 共享 | ❌ 项目级 |
| 团队访问 | ✅ 共享项目 | ✅ Git 跟踪 |
| 可搜索 | ✅ 内建 | ✅ 通过 `/memory` |
| 可编辑 | ✅ 聊天中 | ✅ 直接改文件 |
| 导入/导出 | ✅ 支持 | ✅ 复制粘贴 |
| 持久性 | ✅ 24h+ | ✅ 长期 |

---

## MCP Protocol

### 概览

MCP（Model Context Protocol）是 Claude 访问外部工具、API 与实时数据源的标准方式。与 Memory 不同，MCP 提供的是对持续变化数据的实时访问。

### MCP 架构

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["外部服务"]

    A -->|请求| B
    B -->|查询| C
    C -->|数据| B
    B -->|响应| A
```

### MCP 生态

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]
```

### MCP 设置流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as 配置文件
    participant Service as 外部服务

    User->>Claude: 输入 /mcp
    Claude->>Claude: 列出可用 MCP server
    Claude->>User: 展示选项
    User->>Claude: 选择 GitHub MCP
    Claude->>Config: 更新配置
    Config->>Claude: 激活连接
    Claude->>Service: 测试连接
    Service-->>Claude: 认证成功
    Claude->>User: ✅ MCP 已连接
```

### 可用 MCP Server 表

| MCP Server | 用途 | 常见工具 | 认证 | 实时 |
|------------|------|----------|------|------|
| Filesystem | 文件操作 | read, write, delete | 操作系统权限 | ✅ 是 |
| GitHub | 仓库管理 | list_prs, create_issue, push | OAuth | ✅ 是 |
| Slack | 团队沟通 | send_message, list_channels | Token | ✅ 是 |
| Database | SQL 查询 | query, insert, update | 凭据 | ✅ 是 |
| Google Docs | 文档访问 | read, write, share | OAuth | ✅ 是 |
| Asana | 项目管理 | create_task, update_status | API Key | ✅ 是 |
| Stripe | 支付数据 | list_charges, create_invoice | API Key | ✅ 是 |
| Memory | 持久记忆 | store, retrieve, delete | Local | ❌ 否 |

### 实践示例

#### 示例 1：GitHub MCP 配置

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

#### 示例 2：Database MCP 配置

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

#### 示例 3：多 MCP 工作流

```markdown
# 使用多个 MCP 的日报工作流

## 设置
1. GitHub MCP - 获取 PR 指标
2. Database MCP - 查询销售数据
3. Slack MCP - 发送报告
4. Filesystem MCP - 保存报告
```

#### 示例 4：Filesystem MCP 操作

| 操作 | 命令 | 作用 |
|------|------|------|
| 列出文件 | `ls ~/projects` | 查看目录内容 |
| 读取文件 | `cat src/main.ts` | 读取文件内容 |
| 写入文件 | `create docs/api.md` | 创建新文件 |
| 编辑文件 | `edit src/app.ts` | 修改文件 |
| 搜索 | `grep "async function"` | 在文件中搜索 |
| 删除 | `rm old-file.js` | 删除文件 |

### MCP vs Memory：决策矩阵

```mermaid
graph TD
    A["需要外部数据吗？"]
    A -->|否| B["使用 Memory"]
    A -->|是| C["数据是否频繁变化？"]
    C -->|否/很少| B
    C -->|是/经常| D["使用 MCP"]
```

### 请求 / 响应模式

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
```

---

## Agent Skills

### 概览

Agent Skills 是可复用、由模型自动调用的能力包。它们以目录形式存在，通常包含说明、脚本和资源文件。Claude 会在合适时自动发现并使用它们。

### Skill 架构

```mermaid
graph TB
    A["Skill 目录"]
    B["SKILL.md"]
    C["YAML 元数据"]
    D["说明"]
    E["脚本"]
    F["模板"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### Skill 加载流程

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

| 类型 | 位置 | 作用域 | 是否共享 | 同步方式 | 最适合 |
|------|------|--------|----------|----------|--------|
| 内置 | Built-in | 全局 | 全部用户 | 自动 | 文档生成 |
| 个人 | `~/.claude/skills/` | 个人 | 否 | 手动 | 个人自动化 |
| 项目 | `.claude/skills/` | 团队 | 是 | Git | 团队标准 |
| 插件 | 通过 plugin 安装 | 视情况而定 | 视情况而定 | 自动 | 集成能力 |

### 预构建 Skills

Claude Code 现在内置了 5 个 bundled skills，可直接使用：

| Skill | 命令 | 用途 |
|-------|------|------|
| Simplify | `/simplify` | 简化复杂代码或解释 |
| Batch | `/batch` | 批量对多个文件或对象执行操作 |
| Debug | `/debug` | 系统化调试并做根因分析 |
| Loop | `/loop` | 按定时计划重复执行任务 |
| Claude API | `/claude-api` | 直接与 Anthropic API 交互 |

### 实践示例

#### 示例 1：自定义代码审查 Skill

**目录结构：**

```text
~/.claude/skills/code-review/
├── SKILL.md
├── templates/
│   ├── review-checklist.md
│   └── finding-template.md
└── scripts/
    ├── analyze-metrics.py
    └── compare-complexity.py
```

**文件：** `~/.claude/skills/code-review/SKILL.md`

```yaml
---
name: Code Review Specialist
description: Comprehensive code review with security, performance, and quality analysis
version: "1.0.0"
tags:
  - code-review
  - quality
  - security
when_to_use: 当用户希望审查代码、分析代码质量或评估 pull request 时
effort: high
shell: bash
---

# 代码审查 Skill

这个 skill 提供全面的代码审查能力，重点关注：

1. **安全分析**
2. **性能审查**
3. **代码质量**
4. **可维护性**
```

相关 Python 脚本和模板可直接沿用原始实现；脚本逻辑本身无需翻译即可使用。

#### 示例 2：Brand Voice Skill

这个 skill 用于统一品牌语气、用词风格和外部沟通表达。它通常包含品牌使命、价值观、推荐用词、避免用词，以及邮件 / 社交媒体等模板。

#### 示例 3：Documentation Generator Skill

这个 skill 用于从源码生成 API 文档，常见产物包括：

- OpenAPI/Swagger 规范
- API 端点文档
- SDK 使用示例
- 集成指南
- 错误码说明
- 认证说明

### Skill 发现与调用

```mermaid
graph TD
    A["用户请求"] --> B["Claude 分析"]
    B -->|扫描| C["可用 Skills"]
    C -->|元数据匹配| D["Skill 描述是否匹配？"]
    D -->|是| E["加载 SKILL.md"]
    D -->|否| F["尝试下一个 Skill"]
    E --> H["提取指令"]
    H --> I["执行 Skill"]
    I --> J["返回结果"]
```

### Skill 与其他功能的区别

```mermaid
graph TB
    A["扩展 Claude"]
    B["Slash Commands"]
    C["Subagents"]
    D["Memory"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
```

---

## Claude Code Plugins

### 概览

Claude Code Plugins 是把多种能力打包在一起的一体化扩展机制，通常包含 slash commands、subagents、MCP servers、hooks 以及相关配置。它们可以通过一条命令完成安装。

### 架构

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|打包| B
    A -->|打包| C
    A -->|打包| D
    A -->|打包| E
    A -->|打包| F
```

### Plugin 加载流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: 下载插件清单
    Plugin-->>Claude: 返回插件定义
    Claude->>Install: 解包组件
    Install->>SlashCmds: 配置
    Install->>Subagents: 配置
    Install->>MCPServers: 配置
    Install->>Hooks: 配置
```

### Plugin 类型与分发

| 类型 | 作用域 | 是否共享 | 权威来源 | 示例 |
|------|--------|----------|----------|------|
| Official | 全局 | 全部用户 | Anthropic | PR Review、Security Guidance |
| Community | 公开 | 全部用户 | 社区 | DevOps、Data Science |
| Organization | 内部 | 团队成员 | 公司 | 内部标准、工具 |
| Personal | 个人 | 单用户 | 开发者 | 自定义工作流 |

### Plugin 定义结构

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT
---
```

### Plugin 结构

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
├── agents/
├── skills/
├── hooks/
├── .mcp.json
├── templates/
├── scripts/
├── docs/
└── tests/
```

### 实践示例

#### 示例 1：PR Review Plugin

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs"
}
```

#### 示例 2：DevOps Plugin

```text
devops-automation/
├── commands/
├── agents/
├── mcp/
├── hooks/
└── scripts/
```

#### 示例 3：Documentation Plugin

```text
documentation/
├── commands/
├── agents/
├── mcp/
└── templates/
```

### Plugin Marketplace

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official"]
    C["Community"]
    D["Enterprise"]
```

### Plugin 安装与生命周期

```mermaid
graph LR
    A["发现"] --> B["浏览 Marketplace"]
    B --> C["查看插件页"]
    C --> D["查看组件"]
    D --> E["/plugin install"]
    E --> F["配置"]
    F --> G["启用"]
```

### Plugin 功能对比

| 功能 | Slash Command | Skill | Subagent | Plugin |
|------|---------------|-------|----------|--------|
| 安装 | 手动复制 | 手动复制 | 手动配置 | 一条命令 |
| 搭建时间 | 5 分钟 | 10 分钟 | 15 分钟 | 2 分钟 |
| 打包能力 | 单文件 | 单文件 | 单文件 | 多组件 |
| 团队共享 | 复制文件 | 复制文件 | 复制文件 | 通过安装 ID |
| 更新方式 | 手动 | 手动 | 手动 | 市场可用 / 更易分发 |

### 何时创建 Plugin

- 当你需要一次分发多个命令、subagents、MCP servers 或 hooks 时
- 当这是团队级工作流，需要统一安装和复制时
- 当你希望自动化配置过程并减少手工步骤时

### 发布 Plugin

1. 创建完整的插件结构
2. 编写 `.claude-plugin/plugin.json`
3. 编写 `README.md`
4. 本地测试
5. 提交到 marketplace
6. 审核通过
7. 发布

### Plugin vs 手动配置

**手动配置：**
- 一个个复制 slash commands
- 单独创建 subagents
- 分别配置 MCP
- 手动设置 hooks

**使用 Plugin：**
```bash
/plugin install pr-review
# ✅ 一次安装完成
# ✅ 即刻可用
# ✅ 团队可复现
```

---

## Comparison & Integration

### 功能对比矩阵

| 功能 | 调用方式 | 持久性 | 作用域 | 适用场景 |
|------|----------|--------|--------|----------|
| Slash Commands | 手动 (`/cmd`) | 仅当前会话 | 单个命令 | 快捷操作 |
| Subagents | 自动委派 | 隔离上下文 | 专门任务 | 任务拆分 |
| Memory | 自动加载 | 跨会话 | 用户 / 团队上下文 | 长期记忆 |
| MCP Protocol | 自动查询 | 实时外部数据 | 动态访问 | 外部数据接入 |
| Skills | 自动触发 | 文件系统级 | 可复用专长 | 自动化工作流 |
| Plugins | 一键安装 | 全套组合 | 团队 / 市场分发 | 完整方案打包 |

### 交互时间线

```mermaid
graph LR
    A["Session Start"] -->|Load| B["Memory (CLAUDE.md)"]
    B -->|Discover| C["Available Skills"]
    C -->|Register| D["Slash Commands"]
    D -->|Connect| E["MCP Servers"]
    E -->|Ready| F["User Interaction"]
```

### 集成示例：客户支持自动化

#### 架构

```mermaid
graph TB
    User["客户邮件"] -->|进入| Router["支持路由器"]
    Router -->|分析| Memory["Memory<br/>客户历史"]
    Router -->|查询| MCP1["MCP: 客户数据库"]
    Router -->|检查| MCP2["MCP: Slack"]
    Router -->|复杂问题| Sub1["Subagent: 技术支持"]
    Router -->|简单问题| Sub2["Subagent: 计费支持"]
```

#### 请求流

```markdown
1. 用户发来报错邮件
2. 读取记忆和历史上下文
3. 通过多个 MCP 查询系统状态
4. 自动识别适合的 Skill
5. 委派给对应 Subagent
6. Subagent 处理问题
7. Skill 负责按统一语气生成回复
8. MCP 将结果同步到外部系统
9. 返回给客户
```

### 完整功能编排

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: "Build auth system"
    Claude->>Memory: 加载项目标准
    Claude->>MCP: 查询相似实现
    Claude->>Skills: 检测匹配 Skill
    Claude->>SubAgent: 委派实现
```

### 何时使用哪种功能

```mermaid
graph TD
    A["新任务"] --> B{任务类型？}

    B -->|重复工作流| C["Slash Command"]
    B -->|需要实时数据| D["MCP Protocol"]
    B -->|希望下次记住| E["Memory"]
    B -->|需要专业子任务| F["Subagent"]
    B -->|领域型自动化| G["Skill"]
```

### 选择决策树

```mermaid
graph TD
    Start["需要扩展 Claude 吗？"]
    Start -->|快速重复任务| A{"手动还是自动？"}
    A -->|手动| B["Slash Command"]
    A -->|自动| C["Skill"]
    Start -->|需要外部数据| D{"是否实时？"}
    D -->|是| E["MCP Protocol"]
    D -->|否| F["Memory"]
    Start -->|复杂项目| G{"是否多角色协作？"}
    G -->|是| H["Subagents"]
```

---

## Summary Table

| 维度 | Slash Commands | Subagents | Memory | MCP | Skills | Plugins |
|------|----------------|-----------|--------|-----|--------|---------|
| 搭建难度 | 简单 | 中等 | 简单 | 中等 | 中等 | 简单 |
| 学习曲线 | 低 | 中 | 低 | 中 | 中 | 低 |
| 团队价值 | 高 | 高 | 中 | 高 | 高 | 很高 |
| 自动化程度 | 低 | 高 | 中 | 高 | 高 | 很高 |
| 上下文管理 | 单会话 | 隔离 | 持久 | 实时 | 持久 | 全部整合 |
| 可扩展性 | 好 | 极佳 | 好 | 极佳 | 极佳 | 极佳 |
| 共享性 | 一般 | 一般 | 好 | 好 | 好 | 极佳 |
| 安装方式 | 手动复制 | 手动配置 | N/A | 手动配置 | 手动复制 | 一条命令 |

---

## Quick Start Guide

### 第 1 周：先从简单的开始
- 为常见任务做 2-3 个 slash commands
- 在设置里开启 Memory
- 在 `CLAUDE.md` 里写明团队标准

### 第 2 周：接入实时数据
- 先配置 1 个 MCP（GitHub 或 Database）
- 通过 `/mcp` 配置
- 在工作流中查询实时数据

### 第 3 周：分发工作
- 创建第一个针对角色的 Subagent
- 使用 `/agents`
- 用简单任务测试委派

### 第 4 周：全面自动化
- 创建第一个 Skill
- 使用市场里的 Skill 或自建
- 组合多个功能做完整工作流

### 持续优化
- 每月回顾并更新 Memory
- 当重复模式出现时新增 Skill
- 优化 MCP 查询
- 持续打磨 Subagent 提示词

---

## Hooks

### 概览

Hooks 是事件驱动的 shell 命令，会在 Claude Code 的特定事件发生时自动执行，可用于自动化、校验、通知和自定义工作流。

### Hook 事件

Claude Code 支持 **25 个 hook 事件**，分布在四类钩子中：

| Hook 事件 | 触发时机 | 常见用途 |
|-----------|----------|----------|
| SessionStart | 会话开始 / 恢复 / 清空 / compact | 环境初始化 |
| InstructionsLoaded | 加载 `CLAUDE.md` 或 rules | 校验、增强 |
| UserPromptSubmit | 用户提交提示词 | 输入校验 |
| PreToolUse | 工具执行前 | 审批、校验、日志 |
| PermissionRequest | 弹出权限请求时 | 自动批准 / 拒绝 |
| PostToolUse | 工具执行成功后 | 自动格式化、通知、清理 |
| PostToolUseFailure | 工具失败后 | 错误处理 |
| Notification | 通知发送时 | 外部联动 |
| SubagentStart | 启动 subagent 时 | 注入上下文 |
| SubagentStop | subagent 结束时 | 结果校验 |
| Stop | Claude 响应完成时 | 总结、清理 |
| SessionEnd | 会话结束时 | 收尾处理 |

### 常见 Hook 配置

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
    ]
  }
}
```

### Hook 环境变量

- `$CLAUDE_FILE_PATH`：当前被写入 / 编辑的文件
- `$CLAUDE_TOOL_NAME`：正在使用的工具名
- `$CLAUDE_SESSION_ID`：当前会话 ID
- `$CLAUDE_PROJECT_DIR`：项目目录路径

### 最佳实践

✅ 建议：
- 让 hooks 尽量快（最好 < 1 秒）
- 用 hooks 做校验和自动化
- 优雅处理错误
- 使用绝对路径

❌ 不建议：
- 让 hooks 进入交互式流程
- 把长时间任务放在 hooks 里
- 硬编码凭据

**详见：** [06-hooks/README.md](06-hooks/README.md)

---

## Checkpoints and Rewind

### 概览

Checkpoints 可以保存会话状态，并在需要时回退到之前的节点，从而安全地尝试不同方案。

### 核心概念

| 概念 | 说明 |
|------|------|
| Checkpoint | 对消息、文件和上下文的快照 |
| Rewind | 回到某个历史 checkpoint，并丢弃之后的变化 |
| Branch Point | 从同一个 checkpoint 分叉出多种方案 |

### 如何访问 Checkpoints

```bash
# 按两次 Esc 打开 checkpoint 浏览器
Esc + Esc

# 或使用 /rewind
/rewind
```

选择 checkpoint 后有五个选项：
1. 恢复代码和对话
2. 恢复对话
3. 恢复代码
4. 从这里开始总结
5. 取消

### 常见场景

| 场景 | 工作流 |
|------|--------|
| 探索不同方案 | 保存 → 尝试 A → 保存 → 回退 → 尝试 B |
| 安全重构 | 保存 → 重构 → 测试 → 失败就回退 |
| A/B 测试 | 保存 → 设计 A → 保存 → 回退 → 设计 B |
| 误操作恢复 | 发现问题 → 回退到最近稳定状态 |

### 配置

```json
{
  "autoCheckpoint": true
}
```

**详见：** [08-checkpoints/README.md](08-checkpoints/README.md)

---

## Advanced Features

### Planning Mode

在编码前先生成详细实现计划。

```bash
/plan Implement user authentication system
```

优势：
- 清晰路线图
- 时间预估
- 风险评估
- 可审查、可修改

### Extended Thinking

适合复杂问题的深度推理。

```bash
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

### Background Tasks

后台执行长任务而不阻塞当前对话。

```bash
/task list
/task status bg-1234
/task show bg-1234
/task cancel bg-1234
```

### Permission Modes

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| `default` | 标准权限模式 | 通用开发 |
| `acceptEdits` | 自动接受文件编辑 | 信任编辑工作流 |
| `plan` | 只分析不改文件 | 审查、规划 |
| `auto` | 自动批准安全操作 | 平衡自治与安全 |
| `dontAsk` | 不再提示确认 | 资深用户 / 自动化 |
| `bypassPermissions` | 完全不受限 | CI/CD、可信脚本 |

### Headless Mode（Print Mode）

使用 `-p` 标志在无交互模式下运行 Claude Code，适合自动化和 CI/CD。

```bash
claude -p "Run all tests"
cat error.log | claude -p "explain this error"
claude -p --output-format json "list all functions in src/"
```

### Scheduled Tasks

通过 `/loop` 按计划周期性运行任务：

```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

### Chrome Integration

Claude Code 可以与 Chrome 浏览器集成，用于网页自动化，如导航页面、填写表单、截图和提取页面数据。

### Session Management

```bash
/resume
/rename "Feature"
/fork
claude -c
claude -r "Feature"
```

### Interactive Features

- `Ctrl + R`：搜索命令历史
- `Tab`：自动补全
- `↑ / ↓`：浏览历史
- `Ctrl + L`：清屏

### 配置

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "default"
  }
}
```

**详见：** [09-advanced-features/README.md](09-advanced-features/README.md)

---

## Resources

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Anthropic Documentation](https://docs.anthropic.com)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*最后更新：2026 年 3 月*
*适用于 Claude Haiku 4.5、Sonnet 4.6、Opus 4.6*
*现已覆盖：Hooks、Checkpoints、Planning Mode、Extended Thinking、Background Tasks、Permission Modes、Headless Mode、Session Management、Auto Memory、Agent Teams、Scheduled Tasks、Chrome Integration、Bundled Skills 等概念。*
