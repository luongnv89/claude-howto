<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude 核心概念完整指南

一份全面的参考指南，涵盖 Slash Commands（斜杠命令）、Subagents（子代理）、Memory（记忆）、MCP Protocol（MCP 协议）以及 Agent Skills（代理技能），包含表格、图表和实用示例。

---

## 目录

1. [Slash Commands（斜杠命令）](#slash-commands)
2. [Subagents（子代理）](#subagents)
3. [Memory（记忆）](#memory)
4. [MCP Protocol（MCP 协议）](#mcp-protocol)
5. [Agent Skills（代理技能）](#agent-skills)
6. [Plugins（插件）](#plugins)
7. [Hooks（钩子）](#hooks)
8. [Checkpoints and Rewind（检查点与回退）](#checkpoints-and-rewind)
9. [Advanced Features（高级功能）](#advanced-features)
10. [Comparison & Integration（比较与集成）](#comparison--integration)

---

## Slash Commands（斜杠命令）

### 概述

Slash Commands 是以 Markdown 文件形式存储的用户调用快捷方式，Claude Code 可以执行这些命令。它们帮助团队将常用提示词和工作流程标准化。

### 架构

```mermaid
graph TD
    A["用户输入：/command-name"] -->|触发| B["搜索 .claude/commands/"]
    B -->|找到| C["command-name.md"]
    C -->|加载| D["Markdown 内容"]
    D -->|执行| E["Claude 处理提示词"]
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

### 命令组织对照表

| 位置 | 作用域 | 可用范围 | 使用场景 | Git 跟踪 |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | 项目专用 | 团队成员 | 团队工作流、共享规范 | ✅ 是 |
| `~/.claude/commands/` | 个人 | 当前用户 | 跨项目个人快捷方式 | ❌ 否 |
| 子目录 | 命名空间化 | 基于父目录 | 按类别组织 | ✅ 是 |

### 功能与能力

| 功能 | 示例 | 是否支持 |
|---------|---------|-----------|
| Shell 脚本执行 | `bash scripts/deploy.sh` | ✅ 是 |
| 文件引用 | `@path/to/file.js` | ✅ 是 |
| Bash 集成 | `$(git log --oneline)` | ✅ 是 |
| 参数传递 | `/pr --verbose` | ✅ 是 |
| MCP 命令 | `/mcp__github__list_prs` | ✅ 是 |

### 实用示例

#### 示例 1：代码优化命令

**文件：** `.claude/commands/optimize.md`

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

**用法：**
```bash
# 用户在 Claude Code 中输入
/optimize

# Claude 加载提示词并等待代码输入
```

#### 示例 2：Pull Request 助手命令

**文件：** `.claude/commands/pr.md`

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

**用法：**
```bash
/pr

# Claude 按照清单执行并准备 PR
```

#### 示例 3：层级文档生成器

**文件：** `.claude/commands/docs/generate-api-docs.md`

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

### 命令生命周期图

```mermaid
sequenceDiagram
    participant User as 用户
    participant Claude as Claude Code
    participant FS as 文件系统
    participant CLI as Shell/Bash

    User->>Claude: 输入 /optimize
    Claude->>FS: 搜索 .claude/commands/
    FS-->>Claude: 返回 optimize.md
    Claude->>Claude: 加载 Markdown 内容
    Claude->>User: 显示提示词上下文
    User->>Claude: 提供待分析的代码
    Claude->>CLI: （可能执行脚本）
    CLI-->>Claude: 结果
    Claude->>User: 返回分析结果
```

### 最佳实践

| ✅ 应该做 | ❌ 不应该做 |
|------|---------|
| 使用清晰、以动作为导向的命名 | 为一次性任务创建命令 |
| 在描述中记录触发关键词 | 在命令中构建复杂逻辑 |
| 保持命令专注于单一任务 | 创建冗余命令 |
| 对项目命令进行版本控制 | 硬编码敏感信息 |
| 在子目录中分类组织 | 创建过长的命令列表 |
| 使用简洁易读的提示词 | 使用缩写或晦涩的表述 |

---

## Subagents（子代理）

### 概述

Subagents 是具有独立上下文窗口和自定义系统提示词的专用 AI 助手。它们支持委托任务执行，同时保持关注点的清晰分离。

### 架构图

```mermaid
graph TB
    User["👤 用户"]
    Main["🎯 主代理<br/>（协调者）"]
    Reviewer["🔍 代码审查员<br/>子代理"]
    Tester["✅ 测试工程师<br/>子代理"]
    Docs["📝 文档编写者<br/>子代理"]

    User -->|请求| Main
    Main -->|委派| Reviewer
    Main -->|委派| Tester
    Main -->|委派| Docs
    Reviewer -->|返回结果| Main
    Tester -->|返回结果| Main
    Docs -->|返回结果| Main
    Main -->|综合| User
```

### 子代理生命周期

```mermaid
sequenceDiagram
    participant User as 用户
    participant MainAgent as 主代理
    participant CodeReviewer as 代码审查员<br/>子代理
    participant Context as 独立<br/>上下文窗口

    User->>MainAgent: "构建新的认证功能"
    MainAgent->>MainAgent: 分析任务
    MainAgent->>CodeReviewer: "审查这段代码"
    CodeReviewer->>Context: 初始化干净上下文
    Context->>CodeReviewer: 加载审查员指令
    CodeReviewer->>CodeReviewer: 执行审查
    CodeReviewer-->>MainAgent: 返回发现结果
    MainAgent->>MainAgent: 整合结果
    MainAgent-->>User: 提供综合回复
```

### 子代理配置对照表

| 配置项 | 类型 | 用途 | 示例 |
|---------------|------|---------|---------|
| `name` | 字符串 | 代理标识符 | `code-reviewer` |
| `description` | 字符串 | 用途与触发关键词 | `Comprehensive code quality analysis` |
| `tools` | 列表/字符串 | 允许的能力 | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | 行为指令 | 自定义指南 |

### 工具访问层级

```mermaid
graph TD
    A["子代理配置"] -->|选项 1| B["继承主线程<br/>的所有工具"]
    A -->|选项 2| C["指定单独工具"]
    B -->|包含| B1["文件操作"]
    B -->|包含| B2["Shell 命令"]
    B -->|包含| B3["MCP 工具"]
    C -->|显式列表| C1["read, grep, diff"]
    C -->|显式列表| C2["Bash(npm:*), Bash(test:*)"]
```

### 实用示例

#### 示例 1：完整的子代理配置

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

For each issue:
- **Severity**: Critical / High / Medium / Low
- **Category**: Security / Performance / Quality / Testing / Design
- **Location**: File path and line number
- **Issue Description**: What's wrong and why
- **Suggested Fix**: Code example
- **Impact**: How this affects the system

## Example Review

### Issue: N+1 Query Problem
- **Severity**: High
- **Category**: Performance
- **Location**: src/user-service.ts:45
- **Issue**: Loop executes database query in each iteration
- **Fix**: Use JOIN or batch query
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

## Testing Strategy

1. **Unit Tests** - Individual functions/methods
2. **Integration Tests** - Component interactions
3. **End-to-End Tests** - Complete workflows
4. **Edge Cases** - Boundary conditions
5. **Error Scenarios** - Failure handling

## Test Output Requirements

- Use Jest for JavaScript/TypeScript
- Include setup/teardown for each test
- Mock external dependencies
- Document test purpose
- Include performance assertions when relevant

## Coverage Requirements

- Minimum 80% code coverage
- 100% for critical paths
- Report missing coverage areas
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

## Documentation Standards

1. **Clarity** - Use simple, clear language
2. **Examples** - Include practical code examples
3. **Completeness** - Cover all parameters and returns
4. **Structure** - Use consistent formatting
5. **Accuracy** - Verify against actual code

## Documentation Sections

### For APIs
- Description
- Parameters (with types)
- Returns (with types)
- Throws (possible errors)
- Examples (curl, JavaScript, Python)
- Related endpoints

### For Features
- Overview
- Prerequisites
- Step-by-step instructions
- Expected outcomes
- Troubleshooting
- Related topics
```

#### 示例 2：子代理委派的实际运作

```markdown
# 场景：构建支付功能

## 用户请求
"构建一个与 Stripe 集成的安全支付处理功能"

## 主代理流程

1. **规划阶段**
   - 理解需求
   - 确定所需任务
   - 规划架构

2. **委派给代码审查员子代理**
   - 任务："审查支付处理实现的安全性"
   - 上下文：认证、API 密钥、令牌处理
   - 审查内容：SQL 注入、密钥泄露、HTTPS 强制执行

3. **委派给测试工程师子代理**
   - 任务："为支付流程创建全面的测试"
   - 上下文：成功场景、失败场景、边界情况
   - 创建测试：有效支付、拒付、网络故障、Webhook

4. **委派给文档编写者子代理**
   - 任务："记录支付 API 端点文档"
   - 上下文：请求/响应模式
   - 产出：带有 curl 示例和错误码的 API 文档

5. **综合阶段**
   - 主代理收集所有输出
   - 整合各方发现
   - 向用户返回完整解决方案
```

#### 示例 3：工具权限范围控制

**限制型配置——仅限特定命令**

```yaml
---
name: secure-reviewer
description: Security-focused code review with minimal permissions
tools: read, grep
---

# Secure Code Reviewer

Reviews code for security vulnerabilities only.

This agent:
- ✅ Reads files to analyze
- ✅ Searches for patterns
- ❌ Cannot execute code
- ❌ Cannot modify files
- ❌ Cannot run tests

This ensures the reviewer doesn't accidentally break anything.
```

**扩展型配置——拥有完整实现能力**

```yaml
---
name: implementation-agent
description: Full implementation capabilities for feature development
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

Builds features from specifications.

This agent:
- ✅ Reads specifications
- ✅ Writes new code files
- ✅ Runs build commands
- ✅ Searches codebase
- ✅ Edits existing files
- ✅ Finds files matching patterns

Full capabilities for independent feature development.
```

### 子代理上下文管理

```mermaid
graph TB
    A["主代理上下文<br/>50,000 tokens"]
    B["子代理 1 上下文<br/>20,000 tokens"]
    C["子代理 2 上下文<br/>20,000 tokens"]
    D["子代理 3 上下文<br/>20,000 tokens"]

    A -->|干净的新上下文| B
    A -->|干净的新上下文| C
    A -->|干净的新上下文| D

    B -->|仅返回结果| A
    C -->|仅返回结果| A
    D -->|仅返回结果| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### 何时使用子代理

| 场景 | 是否使用子代理 | 原因 |
|----------|--------------|-----|
| 包含多个步骤的复杂功能 | ✅ 是 | 分离关注点，防止上下文污染 |
| 快速代码审查 | ❌ 否 | 引入不必要的开销 |
| 并行任务执行 | ✅ 是 | 每个子代理拥有独立上下文 |
| 需要专业领域知识 | ✅ 是 | 可使用自定义系统提示词 |
| 长时间运行的分析 | ✅ 是 | 防止主上下文耗尽 |
| 单一任务 | ❌ 否 | 会不必要地增加延迟 |

### Agent Teams（代理团队）

Agent Teams 协调多个代理共同完成相关任务。与每次只委派给单个子代理不同，Agent Teams 允许主代理编排一组相互协作的代理，这些代理可以共享中间结果，共同朝着同一目标努力。这对于大规模任务（如全栈功能开发）非常有用，在这类任务中，前端代理、后端代理和测试代理可以并行工作。

---

## Memory（记忆）

### 概述

Memory 使 Claude 能够在不同会话和对话之间保留上下文。它有两种形式：在 claude.ai 中的自动综合，以及在 Claude Code 中基于文件系统的 CLAUDE.md。

### 记忆架构

```mermaid
graph TB
    A["Claude 会话"]
    B["用户输入"]
    C["记忆系统"]
    D["记忆存储"]

    B -->|用户提供信息| C
    C -->|每 24 小时综合一次| D
    D -->|自动加载| A
    A -->|使用上下文| C
```

### Claude Code 中的记忆层级（7 个层级）

Claude Code 从 7 个层级加载记忆，优先级从高到低排列：

```mermaid
graph TD
    A["1. 托管策略<br/>企业管理员策略"] --> B["2. 项目记忆<br/>./CLAUDE.md"]
    B --> C["3. 项目规则<br/>.claude/rules/*.md"]
    C --> D["4. 用户记忆<br/>~/.claude/CLAUDE.md"]
    D --> E["5. 用户规则<br/>~/.claude/rules/*.md"]
    E --> F["6. 本地记忆<br/>.claude/local/CLAUDE.md"]
    F --> G["7. 自动记忆<br/>自动捕获的偏好设置"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### 记忆位置对照表

| 层级 | 位置 | 作用域 | 优先级 | 是否共享 | 最适用于 |
|------|----------|-------|----------|--------|----------|
| 1. 托管策略 | 企业管理员 | 组织 | 最高 | 所有组织用户 | 合规性、安全策略 |
| 2. 项目 | `./CLAUDE.md` | 项目 | 高 | 团队（Git）| 团队规范、架构 |
| 3. 项目规则 | `.claude/rules/*.md` | 项目 | 高 | 团队（Git）| 模块化项目约定 |
| 4. 用户 | `~/.claude/CLAUDE.md` | 个人 | 中 | 个人 | 个人偏好 |
| 5. 用户规则 | `~/.claude/rules/*.md` | 个人 | 中 | 个人 | 个人规则模块 |
| 6. 本地 | `.claude/local/CLAUDE.md` | 本地 | 低 | 不共享 | 特定机器的设置 |
| 7. 自动记忆 | 自动 | 会话 | 最低 | 个人 | 学习到的偏好、模式 |

### 自动记忆（Auto Memory）

Auto Memory 会自动捕获用户在会话期间观察到的偏好和使用模式。Claude 会从你的交互中学习并记住：

- 代码风格偏好
- 你常做的更正
- 框架和工具的选择
- 沟通风格偏好

Auto Memory 在后台运行，无需手动配置。

### 记忆更新生命周期

```mermaid
sequenceDiagram
    participant User as 用户
    participant Claude as Claude Code
    participant Editor as 文件系统
    participant Memory as CLAUDE.md

    User->>Claude: "记住：使用 async/await"
    Claude->>User: "要写入哪个记忆文件？"
    User->>Claude: "项目记忆"
    Claude->>Editor: 打开 ~/.claude/settings.json
    Claude->>Memory: 写入 ./CLAUDE.md
    Memory-->>Claude: 文件已保存
    Claude->>Claude: 加载更新后的记忆
    Claude-->>User: "记忆已保存！"
```

### 实用示例

#### 示例 1：项目记忆结构

**文件：** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

#### 示例 2：目录级别的记忆

**文件：** `./src/api/CLAUDE.md`

~~~~markdown
# API Module Standards

This file overrides root CLAUDE.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

### Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
~~~~

#### 示例 3：个人记忆

**文件：** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
## 关于我
- **经验水平**：8 年全栈开发经验
- **偏好语言**：TypeScript、Python
- **沟通风格**：直接，附带示例
- **学习方式**：图表配合代码

## 代码偏好

### 错误处理
我偏好使用 try-catch 块进行显式错误处理，并提供有意义的错误信息。
避免泛型错误，始终记录错误日志以便调试。

### 注释
注释说明"为什么"，而不是"做什么"。代码应当自文档化。
注释应解释业务逻辑或不显而易见的决策。

### 测试
我偏好 TDD（测试驱动开发）。
先写测试，再写实现。
关注行为，而非实现细节。

### 架构
我偏好模块化、松耦合的设计。
使用依赖注入以提高可测试性。
关注点分离（Controllers、Services、Repositories）。

## 调试偏好
- 使用带前缀的 console.log：`[DEBUG]`
- 包含上下文：函数名、相关变量
- 有堆栈跟踪时使用堆栈跟踪
- 日志中始终包含时间戳

## 沟通
- 用图表解释复杂概念
- 先展示具体示例，再解释理论
- 包含修改前后的代码片段
- 在末尾总结要点

## 项目组织
我的项目组织如下：
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## 工具链
- **IDE**：VS Code（带 vim 键位绑定）
- **终端**：Zsh + Oh-My-Zsh
- **格式化**：Prettier（100 字符行宽）
- **Linter**：ESLint（airbnb 配置）
- **测试框架**：Jest + React Testing Library
~~~~

#### 示例 4：会话期间更新记忆

**会话交互：**

```markdown
用户：记住我偏好在所有新组件中使用 React hooks，而不是 class 组件。

Claude：我来把这条信息加入你的记忆。应该存入哪个记忆文件？
        1. 项目记忆 (./CLAUDE.md)
        2. 个人记忆 (~/.claude/CLAUDE.md)

用户：项目记忆

Claude：✅ 记忆已保存！

已添加到 ./CLAUDE.md：
---

### 组件开发
- 使用带 React Hooks 的函数式组件
- 偏好 hooks 而非 class 组件
- 使用自定义 hooks 实现可复用逻辑
- 为事件处理函数使用 useCallback
- 为复杂计算使用 useMemo
```

### Claude Web/Desktop 中的记忆

#### 记忆合成时间线

```mermaid
graph LR
    A["第 1 天：用户<br/>对话"] -->|24 小时| B["第 2 天：记忆<br/>合成"]
    B -->|自动| C["记忆已更新<br/>已摘要"]
    C -->|加载到| D["第 2～N 天：<br/>新对话"]
    D -->|添加到| E["记忆"]
    E -->|24 小时后| F["记忆刷新"]
```

**示例记忆摘要：**

```markdown
## Claude 对用户的记忆

### 职业背景
- 拥有 8 年经验的高级全栈开发者
- 专注于 TypeScript/Node.js 后端和 React 前端
- 活跃的开源贡献者
- 对 AI 和机器学习感兴趣

### 项目上下文
- 当前正在构建电商平台
- 技术栈：Node.js、PostgreSQL、React 18、Docker
- 与 5 人开发团队协作
- 使用 CI/CD 和蓝绿部署

### 沟通偏好
- 偏好直接、简洁的解释
- 喜欢可视化图表和示例
- 欣赏代码片段
- 在注释中解释业务逻辑

### 当前目标
- 提升 API 性能
- 将测试覆盖率提升至 90%
- 实现缓存策略
- 记录架构文档
```

### 记忆功能对比

| 功能 | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| 自动合成 | ✅ 每 24 小时 | ❌ 手动 |
| 跨项目 | ✅ 共享 | ❌ 项目专属 |
| 团队访问 | ✅ 共享项目 | ✅ Git 追踪 |
| 可搜索 | ✅ 内置 | ✅ 通过 `/memory` |
| 可编辑 | ✅ 对话中 | ✅ 直接编辑文件 |
| 导入/导出 | ✅ 是 | ✅ 复制/粘贴 |
| 持久化 | ✅ 24 小时以上 | ✅ 无限期 |

---

## MCP 协议

### 概述

MCP（Model Context Protocol）是一种标准化的方式，让 Claude 能够访问外部工具、API 和实时数据源。与记忆（Memory）不同，MCP 提供对动态数据的实时访问。

### MCP 架构

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["外部服务"]

    A -->|请求：list_issues| B
    B -->|查询| C
    C -->|数据| B
    B -->|响应| A

    A -->|请求：create_issue| B
    B -->|操作| C
    C -->|结果| B
    B -->|响应| A
```

### MCP 生态系统

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|文件 I/O| G["本地文件"]
    C -->|API| H["GitHub 仓库"]
    D -->|查询| I["PostgreSQL/MySQL"]
    E -->|消息| J["Slack 工作区"]
    F -->|文档| K["Google Drive"]
```

### MCP 配置流程

```mermaid
sequenceDiagram
    participant User as 用户
    participant Claude as Claude Code
    participant Config as 配置文件
    participant Service as 外部服务

    User->>Claude: 输入 /mcp
    Claude->>Claude: 列出可用的 MCP 服务器
    Claude->>User: 显示选项
    User->>Claude: 选择 GitHub MCP
    Claude->>Config: 更新配置
    Config->>Claude: 激活连接
    Claude->>Service: 测试连接
    Service-->>Claude: 认证成功
    Claude->>User: ✅ MCP 已连接！
```

### 可用 MCP 服务器列表

| MCP 服务器 | 用途 | 常用工具 | 认证方式 | 实时 |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 文件操作 | read、write、delete | OS 权限 | ✅ 是 |
| **GitHub** | 仓库管理 | list_prs、create_issue、push | OAuth | ✅ 是 |
| **Slack** | 团队沟通 | send_message、list_channels | Token | ✅ 是 |
| **Database** | SQL 查询 | query、insert、update | 凭据 | ✅ 是 |
| **Google Docs** | 文档访问 | read、write、share | OAuth | ✅ 是 |
| **Asana** | 项目管理 | create_task、update_status | API Key | ✅ 是 |
| **Stripe** | 支付数据 | list_charges、create_invoice | API Key | ✅ 是 |
| **Memory** | 持久化记忆 | store、retrieve、delete | 本地 | ❌ 否 |

### 实际示例

#### 示例 1：GitHub MCP 配置

**文件：** `.mcp.json`（项目范围）或 `~/.claude.json`（用户范围）

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

**可用的 GitHub MCP 工具：**

~~~~markdown
# GitHub MCP 工具

## Pull Request 管理
- `list_prs` - 列出仓库中所有 PR
- `get_pr` - 获取 PR 详情（含 diff）
- `create_pr` - 创建新 PR
- `update_pr` - 更新 PR 描述/标题
- `merge_pr` - 将 PR 合并到主分支
- `review_pr` - 添加审查评论

示例请求：
```
/mcp__github__get_pr 456

# 返回：
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue 管理
- `list_issues` - 列出所有 Issue
- `get_issue` - 获取 Issue 详情
- `create_issue` - 创建新 Issue
- `close_issue` - 关闭 Issue
- `add_comment` - 为 Issue 添加评论

## 仓库信息
- `get_repo_info` - 仓库详情
- `list_files` - 文件树结构
- `get_file_content` - 读取文件内容
- `search_code` - 在代码库中搜索

## 提交操作
- `list_commits` - 提交历史
- `get_commit` - 特定提交详情
- `create_commit` - 创建新提交
~~~~

#### 示例 2：Database MCP 配置

**配置：**

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

**使用示例：**

```markdown
用户：查找所有订单数超过 10 的用户

Claude：我将查询你的数据库以获取该信息。

# 使用 MCP database 工具：
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# 结果：
- Alice：15 笔订单
- Bob：12 笔订单
- Charlie：11 笔订单
```

#### 示例 3：多 MCP 工作流

**场景：日报生成**

```markdown
# 使用多个 MCP 的日报工作流

## 配置
1. GitHub MCP - 获取 PR 指标
2. Database MCP - 查询销售数据
3. Slack MCP - 发布报告
4. Filesystem MCP - 保存报告

## 工作流

### 第一步：获取 GitHub 数据
/mcp__github__list_prs completed:true last:7days

输出：
- PR 总数：42
- 平均合并时间：2.3 小时
- 审查周转时间：1.1 小时

### 第二步：查询数据库
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

输出：
- 销量：247
- 收入：$12,450

### 第三步：生成报告
将数据合并为 HTML 报告

### 第四步：保存到文件系统
将 report.html 写入 /reports/

### 第五步：发布到 Slack
将摘要发送到 #daily-reports 频道

最终输出：
✅ 报告已生成并发布
📊 本周合并 47 个 PR
💰 当日销售额 $12,450
```

#### 示例 4：Filesystem MCP 操作

**配置：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**可用操作：**

| 操作 | 命令 | 用途 |
|-----------|---------|---------|
| 列出文件 | `ls ~/projects` | 显示目录内容 |
| 读取文件 | `cat src/main.ts` | 读取文件内容 |
| 写入文件 | `create docs/api.md` | 创建新文件 |
| 编辑文件 | `edit src/app.ts` | 修改文件 |
| 搜索 | `grep "async function"` | 在文件中搜索 |
| 删除 | `rm old-file.js` | 删除文件 |

### MCP 与 Memory 的决策矩阵

```mermaid
graph TD
    A["需要外部数据？"]
    A -->|否| B["使用 Memory"]
    A -->|是| C["数据是否频繁变化？"]
    C -->|否/偶尔| B
    C -->|是/经常| D["使用 MCP"]

    B -->|存储| E["偏好<br/>上下文<br/>历史"]
    D -->|访问| F["实时 API<br/>数据库<br/>服务"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### 请求/响应模式

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as 数据库

    App->>MCP: 请求："SELECT * FROM users WHERE id=1"
    MCP->>DB: 执行查询
    DB-->>MCP: 结果集
    MCP-->>App: 返回解析后的数据
    App->>App: 处理结果
    App->>App: 继续任务

    Note over MCP,DB: 实时访问<br/>无缓存
```

---

## Agent Skills（智能体技能）

### 概述

Agent Skills 是以文件夹形式封装的可复用、模型可调用的能力，包含指令、脚本和资源。Claude 会自动检测并使用相关技能。

### Skill 架构

```mermaid
graph TB
    A["Skill 目录"]
    B["SKILL.md"]
    C["YAML 元数据"]
    D["指令"]
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
    participant User as 用户
    participant Claude as Claude
    participant System as 系统
    participant Skill as Skill

    User->>Claude: "创建 Excel 报告"
    Claude->>System: 扫描可用技能
    System->>System: 加载技能元数据
    Claude->>Claude: 将用户请求与技能匹配
    Claude->>Skill: 加载 xlsx skill SKILL.md
    Skill-->>Claude: 返回指令 + 工具
    Claude->>Claude: 执行技能
    Claude->>User: 生成 Excel 文件
```

### Skill 类型与位置对照表

| 类型 | 位置 | 范围 | 共享 | 同步 | 最适用于 |
|------|----------|-------|--------|------|----------|
| 预置 | 内置 | 全局 | 所有用户 | 自动 | 文档创建 |
| 个人 | `~/.claude/skills/` | 个人 | 否 | 手动 | 个人自动化 |
| 项目 | `.claude/skills/` | 团队 | 是 | Git | 团队规范 |
| 插件 | 通过插件安装 | 视情况 | 视情况 | 自动 | 集成功能 |

### 预置技能

```mermaid
graph TB
    A["预置技能"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["创建演示文稿"]
    B --> B2["编辑幻灯片"]
    C --> C1["创建电子表格"]
    C --> C2["分析数据"]
    D --> D1["创建文档"]
    D --> D2["格式化文本"]
    E --> E1["生成 PDF"]
    E --> E2["填写表单"]
```

### 内置技能

Claude Code 现已内置 5 个开箱即用的技能：

| 技能 | 命令 | 用途 |
|-------|---------|---------|
| **Simplify** | `/simplify` | 简化复杂代码或解释 |
| **Batch** | `/batch` | 对多个文件或条目批量执行操作 |
| **Debug** | `/debug` | 系统化调试问题并进行根因分析 |
| **Loop** | `/loop` | 按定时器调度重复任务 |
| **Claude API** | `/claude-api` | 直接与 Anthropic API 交互 |

这些内置技能始终可用，无需安装或配置。

### 实际示例

#### 示例 1：自定义代码审查技能

**目录结构：**

```
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
when_to_use: When users ask to review code, analyze code quality, or evaluate pull requests
effort: high
shell: bash
---

# 代码审查技能

本技能提供全面的代码审查能力，重点关注：

1. **安全分析**
   - 认证/授权问题
   - 数据暴露风险
   - 注入漏洞
   - 加密弱点
   - 敏感数据日志记录

2. **性能审查**
   - 算法效率（Big O 分析）
   - 内存优化
   - 数据库查询优化
   - 缓存机会
   - 并发问题

3. **代码质量**
   - SOLID 原则
   - 设计模式
   - 命名规范
   - 文档
   - 测试覆盖率

4. **可维护性**
   - 代码可读性
   - 函数大小（应 < 50 行）
   - 圈复杂度
   - 依赖管理
   - 类型安全

## 审查模板

对每段审查的代码，提供以下内容：

### 摘要
- 整体质量评分（1-5）
- 关键发现数量
- 建议优先处理的领域

### 严重问题（如有）
- **问题**：清晰描述
- **位置**：文件和行号
- **影响**：说明重要性
- **严重程度**：严重/高/中
- **修复**：代码示例

### 按分类的发现

#### 安全（如发现问题）
列出安全漏洞及示例

#### 性能（如发现问题）
列出性能问题及复杂度分析

#### 质量（如发现问题）
列出代码质量问题及重构建议

#### 可维护性（如发现问题）
列出可维护性问题及改进建议
```
## Python 脚本：analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """分析代码的常见指标。"""

    # 统计函数数量
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # 统计类数量
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # 平均行长度
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # 估算复杂度
    complexity = len(re.findall(r'\b(if|elif|else|for|while|and|or)\b', code))

    return {
        'functions': functions,
        'classes': classes,
        'avg_line_length': avg_length,
        'complexity_score': complexity
    }

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
```

## Python 脚本：compare-complexity.py

```python
#!/usr/bin/env python3
"""
比较修改前后代码的圈复杂度。
帮助识别重构是否真正简化了代码结构。
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """分析代码复杂度指标。"""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        使用 McCabe 方法计算圈复杂度。
        统计决策点：if、elif、else、for、while、except、and、or
        """
        complexity = 1  # 基础复杂度

        # 统计决策点
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b(?!$)',
            r'\bor\b(?!$)'
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        计算认知复杂度——代码有多难理解？
        基于嵌套深度和控制流。
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # 追踪嵌套深度
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # 反缩进时减少嵌套
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        可维护性指数范围 0-100。
        > 85：优秀
        > 65：良好
        > 50：一般
        < 50：较差
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # 简化版 MI 计算
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """生成综合复杂度报告。"""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """比较两个代码版本之间的复杂度指标。"""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("代码复杂度对比")
    print("=" * 60)

    print("\n修改前：")
    print(f"  圈复杂度：    {before_metrics['cyclomatic_complexity']}")
    print(f"  认知复杂度：  {before_metrics['cognitive_complexity']}")
    print(f"  可维护性指数：{before_metrics['maintainability_index']}")
    print(f"  代码行数：    {before_metrics['lines_of_code']}")
    print(f"  平均行长度：  {before_metrics['avg_line_length']}")

    print("\n修改后：")
    print(f"  圈复杂度：    {after_metrics['cyclomatic_complexity']}")
    print(f"  认知复杂度：  {after_metrics['cognitive_complexity']}")
    print(f"  可维护性指数：{after_metrics['maintainability_index']}")
    print(f"  代码行数：    {after_metrics['lines_of_code']}")
    print(f"  平均行长度：  {after_metrics['avg_line_length']}")

    print("\n变化：")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  圈复杂度：    {cyclomatic_change:+d}")
    print(f"  认知复杂度：  {cognitive_change:+d}")
    print(f"  可维护性指数：{mi_change:+.2f}")
    print(f"  代码行数：    {loc_change:+d}")

    print("\n评估：")
    if mi_change > 0:
        print("  ✅ 代码可维护性提升")
    elif mi_change < 0:
        print("  ⚠️  代码可维护性下降")
    else:
```
    print("  ➡️  Maintainability unchanged")

    if cyclomatic_change < 0:
        print("  ✅ Complexity DECREASED")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexity INCREASED")
    else:
        print("  ➡️  Complexity unchanged")

    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
```

## 模板：review-checklist.md

```markdown
# 代码审查清单

## 安全清单
- [ ] 没有硬编码的凭证或密钥
- [ ] 对所有用户输入进行验证
- [ ] 防止 SQL 注入（使用参数化查询）
- [ ] 对状态变更操作进行 CSRF 防护
- [ ] 通过适当转义防止 XSS
- [ ] 在受保护的端点上进行身份验证检查
- [ ] 对资源进行授权检查
- [ ] 使用安全的密码哈希算法（bcrypt、argon2）
- [ ] 日志中不含敏感数据
- [ ] 强制使用 HTTPS

## 性能清单
- [ ] 没有 N+1 查询
- [ ] 适当使用索引
- [ ] 在有收益的地方实现缓存
- [ ] 主线程上没有阻塞操作
- [ ] async/await 使用正确
- [ ] 大型数据集已分页处理
- [ ] 数据库连接使用连接池
- [ ] 正则表达式已优化
- [ ] 没有不必要的对象创建
- [ ] 防止内存泄漏

## 质量清单
- [ ] 函数少于 50 行
- [ ] 变量命名清晰
- [ ] 没有重复代码
- [ ] 正确处理错误
- [ ] 注释解释"为什么"，而不是"是什么"
- [ ] 生产环境中没有 console.logs
- [ ] 类型检查（TypeScript/JSDoc）
- [ ] 遵循 SOLID 原则
- [ ] 正确应用设计模式
- [ ] 代码自文档化

## 测试清单
- [ ] 已编写单元测试
- [ ] 覆盖边界情况
- [ ] 已测试错误场景
- [ ] 存在集成测试
- [ ] 覆盖率 > 80%
- [ ] 没有不稳定的测试
- [ ] 已 Mock 外部依赖
- [ ] 测试名称清晰
```

## 模板：finding-template.md

~~~~markdown
# 代码审查问题模板

在代码审查期间，使用此模板记录发现的每个问题。

---

## 问题：[标题]

### 严重程度
- [ ] 严重（阻止部署）
- [ ] 高（合并前必须修复）
- [ ] 中（应尽快修复）
- [ ] 低（有则更好）

### 分类
- [ ] 安全
- [ ] 性能
- [ ] 代码质量
- [ ] 可维护性
- [ ] 测试
- [ ] 设计模式
- [ ] 文档

### 位置
**文件：** `src/components/UserCard.tsx`

**行数：** 45-52

**函数/方法：** `renderUserDetails()`

### 问题描述

**是什么：** 描述问题所在。

**为何重要：** 解释影响以及为什么需要修复。

**当前行为：** 展示有问题的代码或行为。

**期望行为：** 描述应该发生什么。

### 代码示例

#### 当前（有问题的）

```typescript
// 展示 N+1 查询问题
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // 每个用户一次查询！
  renderUserPosts(posts);
});
```

#### 建议修复

```typescript
// 使用 JOIN 查询优化
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 影响分析

| 方面 | 影响 | 严重程度 |
|--------|--------|----------|
| 性能 | 20 个用户产生 100+ 次查询 | 高 |
| 用户体验 | 页面加载缓慢 | 高 |
| 可扩展性 | 规模化后崩溃 | 严重 |
| 可维护性 | 难以调试 | 中 |

### 相关问题

- `AdminUserList.tsx` 第 120 行存在类似问题
- 相关 PR：#456
- 相关 Issue：#789

### 其他资源

- [N+1 查询问题](https://en.wikipedia.org/wiki/N%2B1_problem)
- [数据库 Join 文档](https://docs.example.com/joins)
- [性能优化指南](./docs/performance.md)

### 审查者备注

- 这是该代码库中的常见模式
- 考虑将其加入代码风格指南
- 可能值得创建一个辅助函数

### 作者回复（用于反馈）

*由代码作者填写：*

- [ ] 已在提交中实现修复：`abc123`
- [ ] 修复状态：完成 / 进行中 / 需要讨论
- [ ] 疑问或顾虑：（描述）

---

## 问题统计（供审查者使用）

审查多个问题时，进行跟踪：

- **发现问题总数：** X
- **严重：** X
- **高：** X
- **中：** X
- **低：** X

**建议：** ✅ 批准 / ⚠️ 请求更改 / 🔄 需要讨论

**整体代码质量：** 1-5 星
~~~~

## 使用示例

~~~~markdown
用户：审查这段 React 组件代码

Claude：我将使用我的代码审查 Skill 进行全面的代码审查。

[加载 SKILL.md]
[根据清单分析代码]
[运行 Python 指标脚本]
[应用模板]

## 代码审查结果

### 摘要
质量评分：3.5/5
主要发现：7 项
优先领域：性能优化、错误处理

### 严重问题：1 项

**问题**：N+1 查询问题
**位置**：UserComponent.tsx，第 45-52 行
**影响**：渲染 20 个用户列表时产生 100+ 次数据库查询
**严重程度**：高
**修复**：
```javascript
// 之前：N+1 次查询
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ 次查询

// 之后：单次 JOIN 查询
const users = fetchUsersWithPosts(); // 1 次查询
```

### 性能发现
- 大列表缺少分页
- 建议：对列表项使用 React.memo()
- 数据库查询：可通过索引优化

### 质量发现
- 第 20 行的函数有 127 行（最大值：50）
- 缺少错误边界
- Props 应具有 TypeScript 类型
~~~~

#### 示例 2：品牌声音 Skill

**目录结构：**

```
.claude/skills/brand-voice/
├── SKILL.md
├── brand-guidelines.md
├── tone-examples.md
└── templates/
    ├── email-template.txt
    ├── social-post-template.txt
    └── blog-post-template.md
```

**文件：** `.claude/skills/brand-voice/SKILL.md`

```yaml
---
name: Brand Voice Consistency
description: Ensure all communication matches brand voice and tone guidelines
tags:
  - brand
  - writing
  - consistency
when_to_use: When creating marketing copy, customer communications, or public-facing content
---

# 品牌声音 Skill

## 概述
此 Skill 确保所有通信维持一致的品牌声音、语气和信息传递。

## 品牌标识

### 使命
帮助团队通过 AI 自动化开发工作流程

### 价值观
- **简洁**：让复杂的事情变简单
- **可靠**：稳如磐石的执行
- **赋能**：激发人类创造力

### 语气
- **友好而专业** —— 平易近人，但不随意
- **清晰简洁** —— 避免行话，用简单语言解释技术概念
- **自信** —— 我们知道自己在做什么
- **有同理心** —— 理解用户需求和痛点

## 写作指南

### 应做 ✅
- 称呼读者时使用"你"
- 使用主动语态："Claude 生成报告"，而非"报告由 Claude 生成"
- 从价值主张开始
- 使用具体示例
- 句子保持在 20 字以内
- 使用列表提升清晰度
- 包含号召性用语

### 不应做 ❌
- 不使用企业行话
- 不要居高临下或过于简化
- 不使用"我们相信"或"我们认为"
- 除强调外不使用全大写
- 不要制造大段文字墙
- 不要假定对方有技术知识

## 词汇

### ✅ 首选术语
- Claude（不用"the Claude AI"）
- 代码生成（不用"auto-coding"）
- Agent（不用"bot"）
- 流程化（不用"革命化"）
- 集成（不用"协同"）

### ❌ 避免使用的术语
- "前沿"（过度使用）
- "游戏规则改变者"（含糊）
- "杠杆"（企业腔）
- "利用"（用"使用"）
- "范式转变"（不清晰）
```
## 示例

### ✅ 好的示例
"Claude 自动化您的代码审查流程。无需手动检查每个 PR，Claude 审查安全性、性能和质量——每周为您的团队节省数小时。"

为什么有效：价值清晰、收益具体、以行动为导向

### ❌ 差的示例
"Claude 利用前沿 AI 提供全面的软件开发解决方案。"

为什么无效：含糊、企业行话、没有具体价值

## 模板：邮件

```
主题：[清晰、以收益为导向的主题]

你好 [姓名]，

[开头：对他们有什么价值]

[正文：如何运作 / 他们将获得什么]

[具体示例或收益]

[号召行动：清晰的下一步]

此致，
[姓名]
```

## 模板：社交媒体

```
[钩子：第一行抓住注意力]
[2-3 行：价值或有趣的事实]
[号召行动：链接、问题或互动]
[表情符号：最多 1-2 个，增添视觉趣味]
```

## 文件：tone-examples.md
```
令人振奋的公告：
"每周节省 8 小时的代码审查时间。Claude 自动审查您的 PR。"

富有同理心的支持：
"我们知道部署可能令人紧张。Claude 处理测试，让您无需担忧。"

自信的产品功能：
"Claude 不只是建议代码，它理解您的架构并保持一致性。"

教育性博客文章：
"让我们探索 Agent 如何改善代码审查工作流程。以下是我们学到的内容..."
```

#### 示例 3：文档生成器 Skill

**文件：** `.claude/skills/doc-generator/SKILL.md`

~~~~yaml
---
name: API Documentation Generator
description: Generate comprehensive, accurate API documentation from source code
version: "1.0.0"
tags:
  - documentation
  - api
  - automation
when_to_use: When creating or updating API documentation
---

# API 文档生成器 Skill

## 生成内容

- OpenAPI/Swagger 规范
- API 端点文档
- SDK 使用示例
- 集成指南
- 错误代码参考
- 认证指南

## 文档结构

### 每个端点的格式

```markdown
## GET /api/v1/users/:id

### 描述
对此端点功能的简短说明

### 参数

| 名称 | 类型 | 是否必需 | 描述 |
|------|------|----------|-------------|
| id | string | 是 | 用户 ID |

### 响应

**200 成功**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 未找到**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### 示例

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```

## Python 脚本：generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """从 Python 源代码中提取 API 文档。"""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """提取函数文档。"""
        if node.name.startswith('get_') or node.name.startswith('post_'):
            doc = ast.get_docstring(node)
            endpoint = {
                'name': node.name,
                'docstring': doc,
                'params': [arg.arg for arg in node.args.args],
                'returns': self._extract_return_type(node)
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """从函数注解中提取返回类型。"""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """从端点生成 Markdown 文档。"""
    docs = "# API 文档\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**参数**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**返回**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
~~~~

### Skill 发现与调用

```mermaid
graph TD
    A["用户请求"] --> B["Claude 分析"]
    B -->|扫描| C["可用 Skills"]
    C -->|元数据检查| D["Skill 描述匹配？"]
    D -->|是| E["加载 SKILL.md"]
    D -->|否| F["尝试下一个 Skill"]
    F -->|还有更多 Skills？| D
    F -->|没有更多| G["使用通用知识"]
    E --> H["提取指令"]
    H --> I["执行 Skill"]
    I --> J["返回结果"]
```

### Skill 与其他功能的对比

```mermaid
graph TB
    A["扩展 Claude"]
    B["斜杠命令"]
    C["子 Agent"]
    D["记忆"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B -->|用户调用| G["快捷方式"]
    C -->|自动委托| H["隔离上下文"]
    D -->|持久化| I["跨会话上下文"]
    E -->|实时| J["外部数据访问"]
    F -->|自动调用| K["自主执行"]
```

---

## Claude Code 插件

### 概述

Claude Code 插件是定制化内容的打包集合（斜杠命令、子 Agent、MCP 服务器和钩子），可通过单条命令完成安装。它们代表最高级别的扩展机制——将多个功能组合成具有内聚性的、可分享的包。

### 架构

```mermaid
graph TB
    A["插件"]
    B["斜杠命令"]
    C["子 Agent"]
    D["MCP 服务器"]
    E["钩子"]
    F["配置"]

    A -->|包含| B
    A -->|包含| C
    A -->|包含| D
    A -->|包含| E
    A -->|包含| F
```

### 插件加载流程

```mermaid
sequenceDiagram
    participant User as 用户
    participant Claude as Claude Code
    participant Plugin as 插件市场
    participant Install as 安装程序
    participant SlashCmds as 斜杠命令
    participant Subagents as 子 Agent
    participant MCPServers as MCP 服务器
    participant Hooks as 钩子
    participant Tools as 已配置工具

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: 下载插件清单
    Plugin-->>Claude: 返回插件定义
    Claude->>Install: 提取组件
    Install->>SlashCmds: 配置
    Install->>Subagents: 配置
    Install->>MCPServers: 配置
    Install->>Hooks: 配置
    SlashCmds-->>Tools: 就绪可用
    Subagents-->>Tools: 就绪可用
    MCPServers-->>Tools: 就绪可用
    Hooks-->>Tools: 就绪可用
    Tools-->>Claude: 插件已安装 ✅
```

### 插件类型与分发

| 类型 | 范围 | 共享对象 | 权威来源 | 示例 |
|------|-------|--------|-----------|----------|
| 官方 | 全局 | 所有用户 | Anthropic | PR 审查、安全指导 |
| 社区 | 公开 | 所有用户 | 社区 | DevOps、数据科学 |
| 组织 | 内部 | 团队成员 | 公司 | 内部标准、工具 |
| 个人 | 个人 | 单个用户 | 开发者 | 自定义工作流程 |

### 插件定义结构

```yaml
---
name: plugin-name
version: "1.0.0"
description: "此插件的功能"
author: "您的姓名"
license: MIT

# 插件元数据
tags:
  - category
  - use-case

# 依赖要求
requires:
  - claude-code: ">=1.0.0"

# 打包的组件
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# 配置
config:
  auto_load: true
  enabled_by_default: true
---
```

### 插件结构

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### 实际示例

#### 示例 1：PR 审查插件

**文件：** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "license": "MIT"
}
```

**文件：** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR 审查

此命令启动完整的拉取请求审查，包括：

1. 安全分析
2. 测试覆盖率验证
3. 文档更新
4. 代码质量检查
5. 性能影响评估
```

**文件：** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: read, grep, diff
---

# 安全审查员

专注于发现安全漏洞：
- 身份验证/授权问题
- 数据泄露
- 注入攻击
- 安全配置
```

**安装方式：**

```bash
/plugin install pr-review

# 结果：
# ✅ 已安装 3 个斜杠命令
# ✅ 已配置 3 个子 Agent
# ✅ 已连接 2 个 MCP 服务器
# ✅ 已注册 4 个钩子
# ✅ 准备就绪！
```

#### 示例 2：DevOps 插件

**组件：**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

#### 示例 3：文档插件

**打包组件：**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
```
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

### 插件市场

```mermaid
graph TB
    A["插件市场"]
    B["官方<br/>Anthropic"]
    C["社区<br/>市场"]
    D["企业<br/>注册表"]

    A --> B
    A --> C
    A --> D

    B -->|分类| B1["开发"]
    B -->|分类| B2["DevOps"]
    B -->|分类| B3["文档"]

    C -->|搜索| C1["DevOps 自动化"]
    C -->|搜索| C2["移动开发"]
    C -->|搜索| C3["数据科学"]

    D -->|内部| D1["公司标准"]
    D -->|内部| D2["遗留系统"]
    D -->|内部| D3["合规"]
```

### 插件安装与生命周期

```mermaid
graph LR
    A["发现"] -->|浏览| B["市场"]
    B -->|选择| C["插件页面"]
    C -->|查看| D["组件"]
    D -->|安装| E["/plugin install"]
    E -->|解压| F["配置"]
    F -->|激活| G["使用"]
    G -->|检查| H["更新"]
    H -->|可用| G
    G -->|完成| I["禁用"]
    I -->|稍后| J["启用"]
    J -->|返回| G
```

### 插件功能对比

| 功能 | 斜杠命令 | Skill | 子代理 | 插件 |
|------|----------|-------|--------|------|
| **安装方式** | 手动复制 | 手动复制 | 手动配置 | 一条命令 |
| **配置时间** | 5 分钟 | 10 分钟 | 15 分钟 | 2 分钟 |
| **打包方式** | 单文件 | 单文件 | 单文件 | 多文件 |
| **版本管理** | 手动 | 手动 | 手动 | 自动 |
| **团队共享** | 复制文件 | 复制文件 | 复制文件 | 安装 ID |
| **更新方式** | 手动 | 手动 | 手动 | 自动可用 |
| **依赖关系** | 无 | 无 | 无 | 可能包含 |
| **市场上架** | 否 | 否 | 否 | 是 |
| **分发方式** | 代码仓库 | 代码仓库 | 代码仓库 | 市场 |

### 插件使用场景

| 使用场景 | 推荐方案 | 原因 |
|----------|----------|------|
| **团队入职** | ✅ 使用插件 | 即时配置，包含所有设置 |
| **框架搭建** | ✅ 使用插件 | 打包框架专属命令 |
| **企业标准** | ✅ 使用插件 | 集中分发，版本控制 |
| **快速任务自动化** | ❌ 使用命令 | 插件过于复杂 |
| **单领域专长** | ❌ 使用 Skill | 插件太重，改用 Skill |
| **专项分析** | ❌ 使用子代理 | 手动创建或使用 Skill |
| **实时数据访问** | ❌ 使用 MCP | 独立使用，不要打包 |

### 何时创建插件

```mermaid
graph TD
    A["需要创建插件吗？"]
    A -->|需要多个组件| B{"需要多个命令<br/>或子代理<br/>或 MCP？"}
    B -->|是| C["✅ 创建插件"]
    B -->|否| D["使用单一功能"]
    A -->|团队工作流| E{"与团队<br/>共享？"}
    E -->|是| C
    E -->|否| F["保持本地配置"]
    A -->|配置复杂| G{"需要自动<br/>配置？"}
    G -->|是| C
    G -->|否| D
```

### 发布插件

**发布步骤：**

1. 创建包含所有组件的插件结构
2. 编写 `.claude-plugin/plugin.json` 清单文件
3. 创建 `README.md` 文档
4. 使用 `/plugin install ./my-plugin` 在本地测试
5. 提交至插件市场
6. 经过审核并获批准
7. 在市场上发布
8. 用户通过一条命令即可安装

**提交示例：**

~~~~markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 slash commands for different review types
- 3 specialized subagents
- GitHub and CodeQL MCP integration
- Automated security scanning hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 1.0+
- GitHub access
- CodeQL (optional)
~~~~

### 插件与手动配置对比

**手动配置（2 小时以上）：**
- 逐一安装斜杠命令
- 单独创建子代理
- 分别配置 MCP
- 手动设置 Hooks
- 记录所有内容
- 与团队共享（但愿他们能正确配置）

**使用插件（2 分钟）：**
```bash
/plugin install pr-review
# ✅ 所有内容已安装并配置完毕
# ✅ 立即可用
# ✅ 团队可复现完全相同的配置
```

---

## 对比与集成

### 功能对比矩阵

| 功能 | 调用方式 | 持久性 | 作用范围 | 使用场景 |
|------|----------|--------|----------|----------|
| **斜杠命令** | 手动（`/cmd`） | 仅当前会话 | 单条命令 | 快速快捷方式 |
| **子代理** | 自动委派 | 隔离上下文 | 专项任务 | 任务分发 |
| **Memory** | 自动加载 | 跨会话 | 用户/团队上下文 | 长期学习 |
| **MCP 协议** | 自动查询 | 实时外部 | 实时数据访问 | 动态信息 |
| **Skills** | 自动调用 | 文件系统 | 可复用专长 | 自动化工作流 |

### 交互时间线

```mermaid
graph LR
    A["会话开始"] -->|加载| B["Memory（CLAUDE.md）"]
    B -->|发现| C["可用 Skills"]
    C -->|注册| D["斜杠命令"]
    D -->|连接| E["MCP 服务器"]
    E -->|就绪| F["用户交互"]

    F -->|输入 /cmd| G["斜杠命令"]
    F -->|请求| H["Skill 自动调用"]
    F -->|查询| I["MCP 数据"]
    F -->|复杂任务| J["委派给子代理"]

    G -->|使用| B
    H -->|使用| B
    I -->|使用| B
    J -->|使用| B
```

### 实际集成案例：客服自动化

#### 架构

```mermaid
graph TB
    User["客户邮件"] -->|接收| Router["支持路由器"]

    Router -->|分析| Memory["Memory<br/>客户历史"]
    Router -->|查询| MCP1["MCP: 客户数据库<br/>历史工单"]
    Router -->|检查| MCP2["MCP: Slack<br/>团队状态"]

    Router -->|路由复杂问题| Sub1["子代理：技术支持<br/>上下文：技术问题"]
    Router -->|路由简单问题| Sub2["子代理：账单<br/>上下文：付款问题"]
    Router -->|路由紧急问题| Sub3["子代理：升级<br/>上下文：优先级处理"]

    Sub1 -->|格式化| Skill1["Skill：回复生成器<br/>保持品牌风格"]
    Sub2 -->|格式化| Skill2["Skill：回复生成器"]
    Sub3 -->|格式化| Skill3["Skill：回复生成器"]

    Skill1 -->|生成| Output["格式化回复"]
    Skill2 -->|生成| Output
    Skill3 -->|生成| Output

    Output -->|发布| MCP3["MCP: Slack<br/>通知团队"]
    Output -->|发送| Reply["客户回复"]
```

#### 请求流程

```markdown
## 客服请求处理流程

### 1. 收到邮件
"我在上传文件时遇到了 500 错误，这严重影响了我的工作！"

### 2. Memory 查询
- 加载包含支持标准的 CLAUDE.md
- 检查客户历史：VIP 客户，本月第 3 次事故

### 3. MCP 查询
- GitHub MCP：列出未解决的 issue（找到相关 bug 报告）
- 数据库 MCP：检查系统状态（未报告宕机）
- Slack MCP：检查工程团队是否已知晓

### 4. Skill 检测与加载
- 请求匹配"技术支持" Skill
- 从 Skill 加载支持回复模板

### 5. 子代理委派
- 路由至技术支持子代理
- 提供上下文：客户历史、错误详情、已知问题
- 子代理拥有完整权限：read、bash、grep 工具

### 6. 子代理处理
技术支持子代理：
- 在代码库中搜索文件上传的 500 错误
- 在提交 8f4a2c 中发现最近的变更
- 创建临时解决方案文档

### 7. Skill 执行
回复生成器 Skill：
- 使用品牌声音指南
- 以同理心格式化回复
- 包含临时解决步骤
- 链接相关文档

### 8. MCP 输出
- 向 #support Slack 频道发布更新
- @提及工程团队
- 在 Jira MCP 中更新工单

### 9. 回复
客户收到：
- 有同理心的确认
- 问题原因说明
- 即时临时解决方案
- 永久修复时间线
- 相关 issue 链接
```

### 完整功能编排

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP 服务器
    participant Skills as Skills
    participant SubAgent as 子代理

    User->>Claude: 请求："构建认证系统"
    Claude->>Memory: 加载项目标准
    Memory-->>Claude: 认证标准、团队实践
    Claude->>MCP: 在 GitHub 查询类似实现
    MCP-->>Claude: 代码示例、最佳实践
    Claude->>Skills: 检测匹配的 Skills
    Skills-->>Claude: 安全审查 Skill + 测试 Skill
    Claude->>SubAgent: 委派实现
    SubAgent->>SubAgent: 构建功能
    Claude->>Skills: 应用安全审查 Skill
    Skills-->>Claude: 安全检查清单结果
    Claude->>SubAgent: 委派测试
    SubAgent-->>Claude: 测试结果
    Claude->>User: 交付完整系统
```

### 各功能使用时机

```mermaid
graph TD
    A["新任务"] --> B{任务类型？}

    B -->|重复工作流| C["斜杠命令"]
    B -->|需要实时数据| D["MCP 协议"]
    B -->|下次需要记住| E["Memory"]
    B -->|专项子任务| F["子代理"]
    B -->|领域专项工作| G["Skill"]

    C --> C1["✅ 团队快捷方式"]
    D --> D1["✅ 实时 API 访问"]
    E --> E1["✅ 持久上下文"]
    F --> F1["✅ 并行执行"]
    G --> G1["✅ 自动调用专长"]
```

### 选择决策树

```mermaid
graph TD
    Start["需要扩展 Claude？"]

    Start -->|快速重复任务| A{"手动还是自动？"}
    A -->|手动| B["斜杠命令"]
    A -->|自动| C["Skill"]

    Start -->|需要外部数据| D{"实时性？"}
    D -->|是| E["MCP 协议"]
    D -->|否/跨会话| F["Memory"]

    Start -->|复杂项目| G{"多个角色？"}
    G -->|是| H["子代理"]
    G -->|否| I["Skills + Memory"]

    Start -->|长期上下文| J["Memory"]
    Start -->|团队工作流| K["斜杠命令 +<br/>Memory"]
    Start -->|完全自动化| L["Skills +<br/>子代理 +<br/>MCP"]
```

---

## 总结表

| 方面 | 斜杠命令 | 子代理 | Memory | MCP | Skills | 插件 |
|------|----------|--------|--------|-----|--------|------|
| **配置难度** | 简单 | 中等 | 简单 | 中等 | 中等 | 简单 |
| **学习曲线** | 低 | 中等 | 低 | 中等 | 中等 | 低 |
| **团队价值** | 高 | 高 | 中等 | 高 | 高 | 非常高 |
| **自动化程度** | 低 | 高 | 中等 | 高 | 高 | 非常高 |
| **上下文管理** | 单会话 | 隔离 | 持久 | 实时 | 持久 | 全功能 |
| **维护负担** | 低 | 中等 | 低 | 中等 | 中等 | 低 |
| **可扩展性** | 良好 | 优秀 | 良好 | 优秀 | 优秀 | 优秀 |
| **可共享性** | 一般 | 一般 | 良好 | 良好 | 良好 | 优秀 |
| **版本管理** | 手动 | 手动 | 手动 | 手动 | 手动 | 自动 |
| **安装方式** | 手动复制 | 手动配置 | 不适用 | 手动配置 | 手动复制 | 一条命令 |

---

## 快速入门指南

### 第 1 周：从简单开始
- 为常用任务创建 2-3 个斜杠命令
- 在设置中启用 Memory
- 在 CLAUDE.md 中记录团队标准

### 第 2 周：添加实时访问
- 配置 1 个 MCP（GitHub 或数据库）
- 使用 `/mcp` 进行配置
- 在工作流中查询实时数据

### 第 3 周：分发工作
- 为特定角色创建第一个子代理
- 使用 `/agents` 命令
- 用简单任务测试委派功能

### 第 4 周：全面自动化
- 为重复自动化创建第一个 Skill
- 使用 Skill 市场或自定义构建
- 组合所有功能实现完整工作流

### 持续优化
- 每月回顾并更新 Memory
- 发现模式时添加新 Skills
- 优化 MCP 查询
- 精炼子代理提示词

---

## Hooks

### 概述

Hooks 是事件驱动的 Shell 命令，会在响应 Claude Code 事件时自动执行。它们无需手动干预即可实现自动化、验证和自定义工作流。

### Hook 事件

Claude Code 支持跨四种 Hook 类型（command、http、prompt、agent）的 **25 个 Hook 事件**：

| Hook 事件 | 触发时机 | 使用场景 |
|-----------|----------|----------|
| **SessionStart** | 会话开始/恢复/清除/压缩 | 环境设置、初始化 |
| **InstructionsLoaded** | 加载 CLAUDE.md 或规则文件 | 验证、转换、增强 |
| **UserPromptSubmit** | 用户提交提示词 | 输入验证、提示词过滤 |
| **PreToolUse** | 任意工具运行前 | 验证、审批门控、日志记录 |
| **PermissionRequest** | 显示权限对话框 | 自动批准/拒绝流程 |
| **PostToolUse** | 工具成功执行后 | 自动格式化、通知、清理 |
| **PostToolUseFailure** | 工具执行失败 | 错误处理、日志记录 |
| **Notification** | 发送通知 | 告警、外部集成 |
| **SubagentStart** | 子代理启动 | 上下文注入、初始化 |
| **SubagentStop** | 子代理结束 | 结果验证、日志记录 |
| **Stop** | Claude 完成响应 | 摘要生成、清理任务 |
| **StopFailure** | API 错误结束轮次 | 错误恢复、日志记录 |
| **TeammateIdle** | 代理团队成员空闲 | 工作分配、协调 |
| **TaskCompleted** | 任务标记为完成 | 任务后处理 |
| **TaskCreated** | 通过 TaskCreate 创建任务 | 任务跟踪、日志记录 |
| **ConfigChange** | 配置文件变更 | 验证、传播 |
| **CwdChanged** | 工作目录变更 | 目录专属设置 |
| **FileChanged** | 监听的文件发生变更 | 文件监控、触发重建 |
| **PreCompact** | 上下文压缩前 | 状态保存 |
| **PostCompact** | 压缩完成后 | 压缩后操作 |
| **WorktreeCreate** | 正在创建 Worktree | 环境设置、依赖安装 |
| **WorktreeRemove** | 正在移除 Worktree | 清理、资源释放 |
| **Elicitation** | MCP 服务器请求用户输入 | 输入验证 |
| **ElicitationResult** | 用户响应 Elicitation | 响应处理 |
| **SessionEnd** | 会话终止 | 清理、最终日志记录 |

### 常用 Hooks

Hooks 配置在 `~/.claude/settings.json`（用户级）或 `.claude/settings.json`（项目级）：

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

### Hook 环境变量

- `$CLAUDE_FILE_PATH` - 正在编辑/写入的文件路径
- `$CLAUDE_TOOL_NAME` - 正在使用的工具名称
- `$CLAUDE_SESSION_ID` - 当前会话标识符
- `$CLAUDE_PROJECT_DIR` - 项目目录路径

### 最佳实践

✅ **应该做：**
- 保持 Hooks 快速执行（< 1 秒）
- 将 Hooks 用于验证和自动化
- 优雅地处理错误
- 使用绝对路径

❌ **不应该做：**
- 使 Hooks 具有交互性
- 将 Hooks 用于长时间运行的任务
- 硬编码凭证

**参见**：[06-hooks/](06-hooks/) 获取详细示例

---

## 检查点与回滚

### 概述

检查点允许你保存对话状态并回滚到之前的节点，从而实现安全的实验和多方案探索。

### 核心概念

| 概念 | 说明 |
|------|------|
| **检查点（Checkpoint）** | 对话状态的快照，包含消息、文件和上下文 |
| **回滚（Rewind）** | 返回到之前的检查点，丢弃后续更改 |
| **分支点（Branch Point）** | 从该检查点出发探索多种方案 |

### 访问检查点

检查点在每次用户提交提示词时自动创建。执行回滚：

```bash
# 连按两次 Esc 打开检查点浏览器
Esc + Esc

# 或使用 /rewind 命令
/rewind
```

选择检查点后，你有五个选项：
1. **恢复代码和对话** —— 同时回滚到该节点
2. **恢复对话** —— 回滚消息，保留当前代码
3. **恢复代码** —— 回滚文件，保留对话
4. **从此处摘要** —— 将对话压缩为摘要
5. **取消** —— 不做操作

### 使用场景

| 场景 | 工作流 |
|------|--------|
| **探索多种方案** | 保存 → 尝试方案 A → 保存 → 回滚 → 尝试方案 B → 对比 |
| **安全重构** | 保存 → 重构 → 测试 → 失败则回滚 |
| **A/B 测试** | 保存 → 设计 A → 保存 → 回滚 → 设计 B → 对比 |
| **错误恢复** | 发现问题 → 回滚到上一个良好状态 |

### 配置

```json
{
  "autoCheckpoint": true
}
```

**参见**：[08-checkpoints/](08-checkpoints/) 获取详细示例

---

## 高级功能

### 规划模式

在编码前创建详细的实现计划。

**激活方式：**
```bash
/plan Implement user authentication system
```

**优势：**
- 包含时间估算的清晰路线图
- 风险评估
- 系统化任务拆解
- 可供审查和修改的机会

### 扩展思考

针对复杂问题进行深度推理。

**激活方式：**
- 会话中按 `Alt+T`（macOS 上为 `Option+T`）切换
- 通过设置 `MAX_THINKING_TOKENS` 环境变量进行编程控制

```bash
# 通过环境变量启用扩展思考
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**优势：**
- 深入分析权衡取舍
- 更优的架构决策
- 考虑边缘情况
- 系统化评估

### 后台任务

在不阻塞对话的情况下运行长时间操作。

**用法：**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # 显示所有任务
/task status bg-1234 # 检查进度
/task show bg-1234   # 查看输出
/task cancel bg-1234 # 取消任务
```

### 权限模式

控制 Claude 的操作权限。

| 模式 | 说明 | 使用场景 |
|------|------|----------|
| **default** | 标准权限，敏感操作时提示确认 | 一般开发 |
| **acceptEdits** | 自动接受文件编辑，无需确认 | 可信的编辑工作流 |
| **plan** | 仅分析和规划，不修改文件 | 代码审查、架构规划 |
| **auto** | 自动批准安全操作，仅对高风险操作提示 | 兼顾自主性与安全性 |
| **dontAsk** | 执行所有操作无需确认提示 | 经验丰富的用户、自动化 |
| **bypassPermissions** | 完全不受限制访问，无安全检查 | CI/CD 流水线、可信脚本 |

**用法：**
```bash
claude --permission-mode plan          # 只读分析
claude --permission-mode acceptEdits   # 自动接受编辑
claude --permission-mode auto          # 自动批准安全操作
claude --permission-mode dontAsk       # 无确认提示
```

### 无头模式（打印模式）

使用 `-p`（print）标志在无交互输入的情况下运行 Claude Code，适用于自动化和 CI/CD。

**用法：**
```bash
# 运行特定任务
claude -p "Run all tests"

# 管道输入进行分析
cat error.log | claude -p "explain this error"

# CI/CD 集成（GitHub Actions）
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# JSON 输出用于脚本处理
claude -p --output-format json "list all functions in src/"
```

### 定时任务

使用 `/loop` 命令按重复计划运行任务。

**用法：**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

定时任务在后台运行，完成后报告结果。适用于持续监控、定期检查和自动化维护工作流。

### Chrome 集成

Claude Code 可与 Chrome 浏览器集成，执行 Web 自动化任务。这使你能够直接在开发工作流中实现页面导航、表单填写、截图和从网站提取数据等功能。

### 会话管理

管理多个工作会话。

**命令：**
```bash
/resume                # 恢复之前的对话
/rename "Feature"      # 为当前会话命名
/fork                  # 分叉出新会话
claude -c              # 继续最近的对话
claude -r "Feature"    # 按名称/ID 恢复会话
```

### 交互功能

**键盘快捷键：**
- `Ctrl + R` - 搜索命令历史
- `Tab` - 自动补全
- `↑ / ↓` - 命令历史
- `Ctrl + L` - 清屏

**多行输入：**
```bash
User: \
> 长而复杂的提示词
> 跨越多行
> \end
```

### 配置

完整配置示例：

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
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

**参见**：[09-advanced-features/](09-advanced-features/) 获取全面指南

---

## 资源

- [Claude Code 文档](https://code.claude.com/docs/en/overview)
- [Anthropic 文档](https://docs.anthropic.com)
- [MCP GitHub 服务器](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*最后更新：2026 年 3 月*
*适用于 Claude Haiku 4.5、Sonnet 4.6 和 Opus 4.6*
*现已包含：Hooks、检查点、规划模式、扩展思考、后台任务、权限模式（6 种）、无头模式、会话管理、自动 Memory、代理团队、定时任务、Chrome 集成、频道、语音听写和打包 Skills*
