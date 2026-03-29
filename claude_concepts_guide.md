<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude 概念完整指南

涵蓋斜線指令、子代理、記憶體、MCP 協定和 Agent 技能的完整參考指南，附表格、圖表和實際範例。

---

## 目錄

1. [斜線指令](#斜線指令)
2. [子代理](#子代理)
3. [記憶體](#記憶體)
4. [MCP 協定](#mcp-協定)
5. [Agent 技能](#agent-技能)
6. [外掛套件](#外掛套件)
7. [Hooks](#hooks)
8. [檢查點與倒轉](#檢查點與倒轉)
9. [進階功能](#進階功能)
10. [比較與整合](#比較與整合)

---

## 斜線指令

### 概覽

斜線指令是以 Markdown 檔案儲存的使用者呼叫快捷方式，Claude Code 可以執行。它們讓團隊能夠標準化常用的提示和工作流程。

### 架構

```mermaid
graph TD
    A["User Input: /command-name"] -->|Triggers| B["Search .claude/commands/"]
    B -->|Finds| C["command-name.md"]
    C -->|Loads| D["Markdown Content"]
    D -->|Executes| E["Claude Processes Prompt"]
    E -->|Returns| F["Result in Context"]
```

### 檔案結構

```mermaid
graph LR
    A["Project Root"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### 指令組織表

| 位置 | 範圍 | 可用性 | 使用案例 | Git 追蹤 |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | 專案專屬 | 團隊成員 | 團隊工作流程、共享標準 | ✅ 是 |
| `~/.claude/commands/` | 個人 | 個別使用者 | 跨專案的個人快捷方式 | ❌ 否 |
| 子目錄 | 命名空間 | 基於父層 | 按類別組織 | ✅ 是 |

### 功能與能力

| 功能 | 範例 | 支援 |
|---------|---------|-----------|
| Shell 腳本執行 | `bash scripts/deploy.sh` | ✅ 是 |
| 檔案引用 | `@path/to/file.js` | ✅ 是 |
| Bash 整合 | `$(git log --oneline)` | ✅ 是 |
| 引數 | `/pr --verbose` | ✅ 是 |
| MCP 指令 | `/mcp__github__list_prs` | ✅ 是 |

### 實際範例

#### 範例 1：程式碼最佳化指令

**檔案：** `.claude/commands/optimize.md`

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

**使用方式：**
```bash
# 使用者在 Claude Code 中輸入
/optimize

# Claude 載入提示並等待程式碼輸入
```

#### 範例 2：Pull Request 輔助指令

**檔案：** `.claude/commands/pr.md`

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

**使用方式：**
```bash
/pr

# Claude 執行檢查清單並準備 PR
```

#### 範例 3：階層式文件產生器

**檔案：** `.claude/commands/docs/generate-api-docs.md`

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

### 指令生命週期圖

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

### 最佳實務

| ✅ 應做 | ❌ 不應做 |
|------|---------|
| 使用清晰、以動作為導向的名稱 | 為一次性任務建立指令 |
| 在描述中記錄觸發詞 | 在指令中建構複雜邏輯 |
| 保持指令專注於單一任務 | 建立冗餘指令 |
| 版本控制專案指令 | 硬編碼敏感資訊 |
| 在子目錄中組織 | 建立過長的指令清單 |
| 使用簡單、可讀的提示 | 使用縮寫或隱晦的措辭 |

---

## 子代理

### 概覽

子代理是具有隔離上下文視窗和自訂系統提示的專門化 AI 助手。它們實現委派的任務執行，同時維持清晰的關注點分離。

### 架構圖

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

### 子代理生命週期

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

### 子代理配置表

| 配置 | 類型 | 用途 | 範例 |
|---------------|------|---------|---------|
| `name` | String | Agent 識別碼 | `code-reviewer` |
| `description` | String | 用途和觸發詞 | `Comprehensive code quality analysis` |
| `tools` | List/String | 允許的能力 | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | 行為指令 | 自訂指南 |

### 工具存取層級

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

### 實際範例

#### 範例 1：完整的子代理設定

**檔案：** `.claude/agents/code-reviewer.md`

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

**檔案：** `.claude/agents/test-engineer.md`

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

**檔案：** `.claude/agents/documentation-writer.md`

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

#### 範例 2：子代理委派實例

```markdown
# 情境：建構支付功能

## 使用者請求
"Build a secure payment processing feature that integrates with Stripe"

## 主代理流程

1. **規劃階段**
   - 理解需求
   - 確定所需任務
   - 規劃架構

2. **委派給 Code Reviewer 子代理**
   - 任務："Review the payment processing implementation for security"
   - 上下文：Auth、API 金鑰、token 處理
   - 審查項目：SQL injection、金鑰洩露、HTTPS 強制

3. **委派給 Test Engineer 子代理**
   - 任務："Create comprehensive tests for payment flows"
   - 上下文：成功情境、失敗、邊界情況
   - 建立測試：有效支付、拒絕的卡片、網路故障、webhooks

4. **委派給 Documentation Writer 子代理**
   - 任務："Document the payment API endpoints"
   - 上下文：Request/Response schemas
   - 產出：附 curl 範例的 API 文件、錯誤碼

5. **綜合**
   - 主代理收集所有輸出
   - 整合結果
   - 向使用者回傳完整方案
```

#### 範例 3：工具權限範圍設定

**限制性設定 - 僅限特定指令**

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

**擴展設定 - 用於實作的所有工具**

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
    A["Main Agent Context<br/>50,000 tokens"]
    B["Subagent 1 Context<br/>20,000 tokens"]
    C["Subagent 2 Context<br/>20,000 tokens"]
    D["Subagent 3 Context<br/>20,000 tokens"]

    A -->|Clean slate| B
    A -->|Clean slate| C
    A -->|Clean slate| D

    B -->|Results only| A
    C -->|Results only| A
    D -->|Results only| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### 何時使用子代理

| 情境 | 使用子代理 | 原因 |
|----------|--------------|-----|
| 包含許多步驟的複雜功能 | ✅ 是 | 分離關注點，防止上下文污染 |
| 快速程式碼審查 | ❌ 否 | 不必要的開銷 |
| 並行任務執行 | ✅ 是 | 每個子代理有自己的上下文 |
| 需要專業知識 | ✅ 是 | 自訂系統提示 |
| 長時間運行的分析 | ✅ 是 | 防止主上下文耗盡 |
| 單一任務 | ❌ 否 | 不必要地增加延遲 |

### Agent Teams

Agent Teams 協調多個代理處理相關任務。Agent Teams 不是一次委派給一個子代理，而是讓主代理協調一組代理進行協作、共享中間結果，並朝共同目標努力。這對於大型任務非常有用，例如全端功能開發，其中前端代理、後端代理和測試代理並行工作。

---

## 記憶體

### 概覽

記憶體使 Claude 能夠在工作階段和對話之間保留上下文。它以兩種形式存在：claude.ai 中的自動合成，以及 Claude Code 中基於檔案系統的 CLAUDE.md。

### 記憶體架構

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

### Claude Code 中的記憶體層級（7 層）

Claude Code 從 7 層載入記憶體，按優先順序從高到低列出：

```mermaid
graph TD
    A["1. Managed Policy<br/>Enterprise admin policies"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>Automatically captured preferences"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### 記憶體位置表

| 層級 | 位置 | 範圍 | 優先順序 | 共享 | 最適合 |
|------|----------|-------|----------|--------|----------|
| 1. 託管政策 | 企業管理員 | 組織 | 最高 | 所有組織使用者 | 合規、安全政策 |
| 2. 專案 | `./CLAUDE.md` | 專案 | 高 | 團隊（Git） | 團隊標準、架構 |
| 3. 專案規則 | `.claude/rules/*.md` | 專案 | 高 | 團隊（Git） | 模組化的專案慣例 |
| 4. 使用者 | `~/.claude/CLAUDE.md` | 個人 | 中 | 個人 | 個人偏好 |
| 5. 使用者規則 | `~/.claude/rules/*.md` | 個人 | 中 | 個人 | 個人規則模組 |
| 6. 本機 | `.claude/local/CLAUDE.md` | 本機 | 低 | 不共享 | 機器專屬設定 |
| 7. 自動記憶 | 自動 | 工作階段 | 最低 | 個人 | 學習到的偏好、模式 |

### 自動記憶

自動記憶在工作階段期間自動擷取使用者的偏好和觀察到的模式。Claude 從您的互動中學習並記住：

- 編碼風格偏好
- 您常做的更正
- 框架和工具選擇
- 溝通風格偏好

自動記憶在背景運作，不需要手動配置。

### 記憶體更新生命週期

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: "Remember: use async/await"
    Claude->>User: "Which memory file?"
    User->>Claude: "Project memory"
    Claude->>Editor: Open ~/.claude/settings.json
    Claude->>Memory: Write to ./CLAUDE.md
    Memory-->>Claude: File saved
    Claude->>Claude: Load updated memory
    Claude-->>User: "Memory saved!"
```

### 實際範例

#### 範例 1：專案記憶體結構

**檔案：** `./CLAUDE.md`

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

#### 範例 2：目錄專屬記憶體

**檔案：** `./src/api/CLAUDE.md`

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

#### 範例 3：個人記憶體

**檔案：** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:
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

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
~~~~

#### 範例 4：工作階段中的記憶體更新

**工作階段互動：**

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

### Claude Web/Desktop 中的記憶體

#### 記憶體合成時間線

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**記憶體摘要範例：**

```markdown
## Claude's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

### 記憶體功能比較

| 功能 | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| 自動合成 | ✅ 每 24 小時 | ❌ 手動 |
| 跨專案 | ✅ 共享 | ❌ 專案專屬 |
| 團隊存取 | ✅ 共享專案 | ✅ Git 追蹤 |
| 可搜尋 | ✅ 內建 | ✅ 透過 `/memory` |
| 可編輯 | ✅ 在聊天中 | ✅ 直接編輯檔案 |
| 匯入/匯出 | ✅ 是 | ✅ 複製/貼上 |
| 持久性 | ✅ 24 小時+ | ✅ 無限期 |

---

## MCP 協定

### 概覽

MCP（Model Context Protocol）是 Claude 存取外部工具、API 和即時資料來源的標準化方式。與記憶體不同，MCP 提供對變動資料的即時存取。

### MCP 架構

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

### MCP 生態系統

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

### MCP 設定流程

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

### 可用的 MCP 伺服器表

| MCP 伺服器 | 用途 | 常用工具 | 驗證 | 即時 |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 檔案操作 | read, write, delete | 作業系統權限 | ✅ 是 |
| **GitHub** | 倉庫管理 | list_prs, create_issue, push | OAuth | ✅ 是 |
| **Slack** | 團隊溝通 | send_message, list_channels | Token | ✅ 是 |
| **Database** | SQL 查詢 | query, insert, update | 憑證 | ✅ 是 |
| **Google Docs** | 文件存取 | read, write, share | OAuth | ✅ 是 |
| **Asana** | 專案管理 | create_task, update_status | API Key | ✅ 是 |
| **Stripe** | 支付資料 | list_charges, create_invoice | API Key | ✅ 是 |
| **Memory** | 持久記憶 | store, retrieve, delete | 本機 | ❌ 否 |

### 實際範例

#### 範例 1：GitHub MCP 配置

**檔案：** `.mcp.json`（專案範圍）或 `~/.claude.json`（使用者範圍）

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
# GitHub MCP Tools

## Pull Request Management
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `update_pr` - Update PR description/title
- `merge_pr` - Merge PR to main branch
- `review_pr` - Add review comments

Example request:
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue Management
- `list_issues` - List all issues
- `get_issue` - Get issue details
- `create_issue` - Create new issue
- `close_issue` - Close issue
- `add_comment` - Add comment to issue

## Repository Information
- `get_repo_info` - Repository details
- `list_files` - File tree structure
- `get_file_content` - Read file contents
- `search_code` - Search across codebase

## Commit Operations
- `list_commits` - Commit history
- `get_commit` - Specific commit details
- `create_commit` - Create new commit
~~~~

#### 範例 2：Database MCP 設定

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

**使用範例：**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

#### 範例 3：多 MCP 工作流程

**情境：每日報表產生**

```markdown
# 使用多個 MCP 的每日報表工作流程

## 設定
1. GitHub MCP - 取得 PR 指標
2. Database MCP - 查詢銷售資料
3. Slack MCP - 發佈報表
4. Filesystem MCP - 儲存報表

## 工作流程

### 步驟 1：取得 GitHub 資料
/mcp__github__list_prs completed:true last:7days

輸出：
- 總 PR 數：42
- 平均合併時間：2.3 小時
- 審查週轉時間：1.1 小時

### 步驟 2：查詢資料庫
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

輸出：
- 銷售量：247
- 營收：$12,450

### 步驟 3：產生報表
將資料組合成 HTML 報表

### 步驟 4：儲存到檔案系統
將 report.html 寫入 /reports/

### 步驟 5：發佈到 Slack
將摘要傳送到 #daily-reports 頻道

最終輸出：
✅ 報表已產生並發佈
📊 本週合併了 47 個 PR
💰 每日銷售額 $12,450
```

#### 範例 4：Filesystem MCP 操作

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

| 操作 | 指令 | 用途 |
|-----------|---------|---------|
| 列出檔案 | `ls ~/projects` | 顯示目錄內容 |
| 讀取檔案 | `cat src/main.ts` | 讀取檔案內容 |
| 寫入檔案 | `create docs/api.md` | 建立新檔案 |
| 編輯檔案 | `edit src/app.ts` | 修改檔案 |
| 搜尋 | `grep "async function"` | 搜尋檔案 |
| 刪除 | `rm old-file.js` | 刪除檔案 |

### MCP vs 記憶體：決策矩陣

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### Request/Response 模式

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

---

## Agent 技能

### 概覽

Agent 技能是可重複使用的、由模型觸發的能力，打包為包含指令、腳本和資源的資料夾。Claude 會自動偵測並使用相關的技能。

### 技能架構

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

### 技能載入流程

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

### 技能類型與位置表

| 類型 | 位置 | 範圍 | 共享 | 同步 | 最適合 |
|------|----------|-------|--------|------|----------|
| 預建 | 內建 | 全域 | 所有使用者 | 自動 | 文件建立 |
| 個人 | `~/.claude/skills/` | 個人 | 否 | 手動 | 個人自動化 |
| 專案 | `.claude/skills/` | 團隊 | 是 | Git | 團隊標準 |
| 外掛 | 透過外掛安裝 | 視情況 | 視情況 | 自動 | 整合功能 |

### 預建技能

```mermaid
graph TB
    A["Pre-built Skills"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["Create presentations"]
    B --> B2["Edit slides"]
    C --> C1["Create spreadsheets"]
    C --> C2["Analyze data"]
    D --> D1["Create documents"]
    D --> D2["Format text"]
    E --> E1["Generate PDFs"]
    E --> E2["Fill forms"]
```

### 內建技能

Claude Code 現在包含 5 個開箱即用的內建技能：

| 技能 | 指令 | 用途 |
|-------|---------|---------|
| **Simplify** | `/simplify` | 簡化複雜的程式碼或說明 |
| **Batch** | `/batch` | 跨多個檔案或項目執行操作 |
| **Debug** | `/debug` | 系統性除錯問題，附根因分析 |
| **Loop** | `/loop` | 在計時器上排程重複任務 |
| **Claude API** | `/claude-api` | 直接與 Anthropic API 互動 |

這些內建技能始終可用，不需要安裝或配置。

### 實際範例

#### 範例 1：自訂程式碼審查技能

**目錄結構：**

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

**檔案：** `~/.claude/skills/code-review/SKILL.md`

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

# Code Review Skill

This skill provides comprehensive code review capabilities focusing on:

1. **Security Analysis**
   - Authentication/authorization issues
   - Data exposure risks
   - Injection vulnerabilities
   - Cryptographic weaknesses
   - Sensitive data logging

2. **Performance Review**
   - Algorithm efficiency (Big O analysis)
   - Memory optimization
   - Database query optimization
   - Caching opportunities
   - Concurrency issues

3. **Code Quality**
   - SOLID principles
   - Design patterns
   - Naming conventions
   - Documentation
   - Test coverage

4. **Maintainability**
   - Code readability
   - Function size (should be < 50 lines)
   - Cyclomatic complexity
   - Dependency management
   - Type safety

## Review Template

For each piece of code reviewed, provide:

### Summary
- Overall quality assessment (1-5)
- Key findings count
- Recommended priority areas

### Critical Issues (if any)
- **Issue**: Clear description
- **Location**: File and line number
- **Impact**: Why this matters
- **Severity**: Critical/High/Medium
- **Fix**: Code example

### Findings by Category

#### Security (if issues found)
List security vulnerabilities with examples

#### Performance (if issues found)
List performance problems with complexity analysis

#### Quality (if issues found)
List code quality issues with refactoring suggestions

#### Maintainability (if issues found)
List maintainability problems with improvements
```
## Python Script: analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """Analyze code for common metrics."""

    # Count functions
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # Count classes
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # Average line length
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # Estimate complexity
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

## Python Script: compare-complexity.py

```python
#!/usr/bin/env python3
"""
Compare cyclomatic complexity of code before and after changes.
Helps identify if refactoring actually simplifies code structure.
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """Analyze code complexity metrics."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calculate cyclomatic complexity using McCabe's method.
        Count decision points: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Base complexity

        # Count decision points
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
        Calculate cognitive complexity - how hard is it to understand?
        Based on nesting depth and control flow.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Track nesting depth
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # Reduce nesting when unindenting
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Maintainability Index ranges from 0-100.
        > 85: Excellent
        > 65: Good
        > 50: Fair
        < 50: Poor
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Simplified MI calculation
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """Generate comprehensive complexity report."""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compare complexity metrics between two code versions."""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("CODE COMPLEXITY COMPARISON")
    print("=" * 60)

    print("\nBEFORE:")
    print(f"  Cyclomatic Complexity:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {before_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {before_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {before_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {before_metrics['avg_line_length']}")

    print("\nAFTER:")
    print(f"  Cyclomatic Complexity:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {after_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {after_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {after_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {after_metrics['avg_line_length']}")

    print("\nCHANGES:")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  Cyclomatic Complexity:    {cyclomatic_change:+d}")
    print(f"  Cognitive Complexity:     {cognitive_change:+d}")
    print(f"  Maintainability Index:    {mi_change:+.2f}")
    print(f"  Lines of Code:            {loc_change:+d}")

    print("\nASSESSMENT:")
    if mi_change > 0:
        print("  ✅ Code is MORE maintainable")
    elif mi_change < 0:
        print("  ⚠️  Code is LESS maintainable")
    else:
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

## Template: review-checklist.md

```markdown
# Code Review Checklist

## Security Checklist
- [ ] No hardcoded credentials or secrets
- [ ] Input validation on all user inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection on state-changing operations
- [ ] XSS prevention with proper escaping
- [ ] Authentication checks on protected endpoints
- [ ] Authorization checks on resources
- [ ] Secure password hashing (bcrypt, argon2)
- [ ] No sensitive data in logs
- [ ] HTTPS enforced

## Performance Checklist
- [ ] No N+1 queries
- [ ] Appropriate use of indexes
- [ ] Caching implemented where beneficial
- [ ] No blocking operations on main thread
- [ ] Async/await used correctly
- [ ] Large datasets paginated
- [ ] Database connections pooled
- [ ] Regular expressions optimized
- [ ] No unnecessary object creation
- [ ] Memory leaks prevented

## Quality Checklist
- [ ] Functions < 50 lines
- [ ] Clear variable naming
- [ ] No duplicate code
- [ ] Proper error handling
- [ ] Comments explain WHY, not WHAT
- [ ] No console.logs in production
- [ ] Type checking (TypeScript/JSDoc)
- [ ] SOLID principles followed
- [ ] Design patterns applied correctly
- [ ] Self-documenting code

## Testing Checklist
- [ ] Unit tests written
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Integration tests present
- [ ] Coverage > 80%
- [ ] No flaky tests
- [ ] Mock external dependencies
- [ ] Clear test names
```

## Template: finding-template.md

~~~~markdown
# Code Review Finding Template

Use this template when documenting each issue found during code review.

---

## Issue: [TITLE]

### Severity
- [ ] Critical (blocks deployment)
- [ ] High (should fix before merge)
- [ ] Medium (should fix soon)
- [ ] Low (nice to have)

### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### Issue Description

**What:** Describe what the issue is.

**Why it matters:** Explain the impact and why this needs to be fixed.

**Current behavior:** Show the problematic code or behavior.

**Expected behavior:** Describe what should happen instead.

### Code Example

#### Current (Problematic)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 100+ queries for 20 users | High |
| User Experience | Slow page load | High |
| Scalability | Breaks at scale | Critical |
| Maintainability | Hard to debug | Medium |

### Related Issues

- Similar issue in `AdminUserList.tsx` line 120
- Related PR: #456
- Related issue: #789

### Additional Resources

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)
- [Performance Optimization Guide](./docs/performance.md)

### Reviewer Notes

- This is a common pattern in this codebase
- Consider adding this to the code style guide
- Might be worth creating a helper function

### Author Response (for feedback)

*To be filled by the code author:*

- [ ] Fix implemented in commit: `abc123`
- [ ] Fix status: Complete / In Progress / Needs Discussion
- [ ] Questions or concerns: (describe)

---

## Finding Statistics (for Reviewer)

When reviewing multiple findings, track:

- **Total Issues Found:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**Recommendation:** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality:** 1-5 stars
~~~~

## 使用範例

~~~~markdown
User: Review this React component code

Claude: I'll conduct a comprehensive code review using my Code Review Skill.

[Loads SKILL.md]
[Analyzes code against checklist]
[Runs Python metrics script]
[Applies templates]

## Code Review Results

### Summary
Quality Score: 3.5/5
Key Findings: 7 items
Priority Areas: Performance optimization, error handling

### Critical Issues: 1

**Issue**: N+1 Query Problem
**Location**: UserComponent.tsx, lines 45-52
**Impact**: Renders 100+ database queries for list of 20 users
**Severity**: High
**Fix**:
```javascript
// Before: N+1 queries
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ queries

// After: Single query with JOIN
const users = fetchUsersWithPosts(); // 1 query
```

### Performance Findings
- Missing pagination on large lists
- Recommendation: Use React.memo() for items
- Database query: Could be optimized with index

### Quality Findings
- Function in line 20 is 127 lines (max: 50)
- Missing error boundary
- Props should have TypeScript types
~~~~

#### 範例 2：品牌語調技能

**目錄結構：**

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

**檔案：** `.claude/skills/brand-voice/SKILL.md`

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

# Brand Voice Skill

## Overview
This skill ensures all communications maintain consistent brand voice, tone, and messaging.

## Brand Identity

### Mission
Help teams automate their development workflows with AI

### Values
- **Simplicity**: Make complex things simple
- **Reliability**: Rock-solid execution
- **Empowerment**: Enable human creativity

### Tone of Voice
- **Friendly but professional** - approachable without being casual
- **Clear and concise** - avoid jargon, explain technical concepts simply
- **Confident** - we know what we're doing
- **Empathetic** - understand user needs and pain points

## Writing Guidelines

### Do's ✅
- Use "you" when addressing readers
- Use active voice: "Claude generates reports" not "Reports are generated by Claude"
- Start with value proposition
- Use concrete examples
- Keep sentences under 20 words
- Use lists for clarity
- Include calls-to-action

### Don'ts ❌
- Don't use corporate jargon
- Don't patronize or oversimplify
- Don't use "we believe" or "we think"
- Don't use ALL CAPS except for emphasis
- Don't create walls of text
- Don't assume technical knowledge

## Vocabulary

### ✅ Preferred Terms
- Claude (not "the Claude AI")
- Code generation (not "auto-coding")
- Agent (not "bot")
- Streamline (not "revolutionize")
- Integrate (not "synergize")

### ❌ Avoid Terms
- "Cutting-edge" (overused)
- "Game-changer" (vague)
- "Leverage" (corporate-speak)
- "Utilize" (use "use")
- "Paradigm shift" (unclear)
```
## 範例

### ✅ 好的範例
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

為什麼有效：清晰的價值、具體的好處、以行動為導向

### ❌ 不好的範例
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

為什麼無效：模糊、企業術語、沒有具體價值

## Template: Email

```
Subject: [Clear, benefit-driven subject]

Hi [Name],

[Opening: What's the value for them]

[Body: How it works / What they'll get]

[Specific example or benefit]

[Call to action: Clear next step]

Best regards,
[Name]
```

## Template: Social Media

```
[Hook: Grab attention in first line]
[2-3 lines: Value or interesting fact]
[Call to action: Link, question, or engagement]
[Emoji: 1-2 max for visual interest]
```

## File: tone-examples.md
```
Exciting announcement:
"Save 8 hours per week on code reviews. Claude reviews your PRs automatically."

Empathetic support:
"We know deployments can be stressful. Claude handles testing so you don't have to worry."

Confident product feature:
"Claude doesn't just suggest code. It understands your architecture and maintains consistency."

Educational blog post:
"Let's explore how agents improve code review workflows. Here's what we learned..."
```

#### 範例 3：文件產生器技能

**檔案：** `.claude/skills/doc-generator/SKILL.md`

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

# API Documentation Generator Skill

## Generates

- OpenAPI/Swagger specifications
- API endpoint documentation
- SDK usage examples
- Integration guides
- Error code references
- Authentication guides

## Documentation Structure

### For Each Endpoint

```markdown
## GET /api/v1/users/:id

### Description
Brief explanation of what this endpoint does

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### Examples

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

## Python Script: generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
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
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
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
### 技能發現與觸發

```mermaid
graph TD
    A["User Request"] --> B["Claude Analyzes"]
    B -->|Scans| C["Available Skills"]
    C -->|Metadata check| D["Skill Description Match?"]
    D -->|Yes| E["Load SKILL.md"]
    D -->|No| F["Try next skill"]
    F -->|More skills?| D
    F -->|No more| G["Use general knowledge"]
    E --> H["Extract Instructions"]
    H --> I["Execute Skill"]
    I --> J["Return Results"]
```

### 技能 vs 其他功能

```mermaid
graph TB
    A["Extending Claude"]
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

    B -->|User-invoked| G["Quick shortcuts"]
    C -->|Auto-delegated| H["Isolated contexts"]
    D -->|Persistent| I["Cross-session context"]
    E -->|Real-time| J["External data access"]
    F -->|Auto-invoked| K["Autonomous execution"]
```

---

## Claude Code 外掛套件

### 概覽

Claude Code 外掛套件是斜線指令、子代理、MCP 伺服器和 hooks 的整合集合，可用單一指令安裝。它們代表最高級別的擴展機制 — 將多個功能組合成有凝聚力、可共享的套件。

### 架構

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

### 外掛載入流程

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
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: Download plugin manifest
    Plugin-->>Claude: Return plugin definition
    Claude->>Install: Extract components
    Install->>SlashCmds: Configure
    Install->>Subagents: Configure
    Install->>MCPServers: Configure
    Install->>Hooks: Configure
    SlashCmds-->>Tools: Ready to use
    Subagents-->>Tools: Ready to use
    MCPServers-->>Tools: Ready to use
    Hooks-->>Tools: Ready to use
    Tools-->>Claude: Plugin installed ✅
```

### 外掛類型與分發

| 類型 | 範圍 | 共享 | 權限 | 範例 |
|------|-------|--------|-----------|----------|
| 官方 | 全域 | 所有使用者 | Anthropic | PR Review、Security Guidance |
| 社群 | 公開 | 所有使用者 | 社群 | DevOps、Data Science |
| 組織 | 內部 | 團隊成員 | 公司 | 內部標準、工具 |
| 個人 | 個人 | 單一使用者 | 開發者 | 自訂工作流程 |

### 外掛定義結構

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT

# Plugin metadata
tags:
  - category
  - use-case

# Requirements
requires:
  - claude-code: ">=1.0.0"

# Components bundled
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# Configuration
config:
  auto_load: true
  enabled_by_default: true
---
```

### 外掛結構

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

### 實際範例

#### 範例 1：PR Review 外掛

**檔案：** `.claude-plugin/plugin.json`

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

**檔案：** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR Review

This command initiates a complete pull request review including:

1. Security analysis
2. Test coverage verification
3. Documentation updates
4. Code quality checks
5. Performance impact assessment
```

**檔案：** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: read, grep, diff
---

# Security Reviewer

Specializes in finding security vulnerabilities:
- Authentication/authorization issues
- Data exposure
- Injection attacks
- Secure configuration
```

**安裝：**

```bash
/plugin install pr-review

# 結果：
# ✅ 已安裝 3 個斜線指令
# ✅ 已配置 3 個子代理
# ✅ 已連接 2 個 MCP 伺服器
# ✅ 已註冊 4 個 hooks
# ✅ 準備就緒！
```

#### 範例 2：DevOps 外掛

**元件：**

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

#### 範例 3：文件外掛

**整合元件：**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
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

### 外掛市集

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>Anthropic"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Registry"]

    A --> B
    A --> C
    A --> D

    B -->|Categories| B1["Development"]
    B -->|Categories| B2["DevOps"]
    B -->|Categories| B3["Documentation"]

    C -->|Search| C1["DevOps Automation"]
    C -->|Search| C2["Mobile Dev"]
    C -->|Search| C3["Data Science"]

    D -->|Internal| D1["Company Standards"]
    D -->|Internal| D2["Legacy Systems"]
    D -->|Internal| D3["Compliance"]
```

### 外掛安裝與生命週期

```mermaid
graph LR
    A["Discover"] -->|Browse| B["Marketplace"]
    B -->|Select| C["Plugin Page"]
    C -->|View| D["Components"]
    D -->|Install| E["/plugin install"]
    E -->|Extract| F["Configure"]
    F -->|Activate| G["Use"]
    G -->|Check| H["Update"]
    H -->|Available| G
    G -->|Done| I["Disable"]
    I -->|Later| J["Enable"]
    J -->|Back| G
```

### 外掛功能比較

| 功能 | 斜線指令 | 技能 | 子代理 | 外掛 |
|---------|---------------|-------|----------|--------|
| **安裝** | 手動複製 | 手動複製 | 手動配置 | 一個指令 |
| **設定時間** | 5 分鐘 | 10 分鐘 | 15 分鐘 | 2 分鐘 |
| **打包** | 單一檔案 | 單一檔案 | 單一檔案 | 多個 |
| **版本控制** | 手動 | 手動 | 手動 | 自動 |
| **團隊共享** | 複製檔案 | 複製檔案 | 複製檔案 | 安裝 ID |
| **更新** | 手動 | 手動 | 手動 | 自動提供 |
| **依賴項** | 無 | 無 | 無 | 可能包含 |
| **市集** | 否 | 否 | 否 | 是 |
| **分發** | 倉庫 | 倉庫 | 倉庫 | 市集 |

### 外掛使用案例

| 使用案例 | 建議 | 原因 |
|----------|-----------------|-----|
| **團隊入職** | ✅ 使用外掛 | 即時設定，所有配置 |
| **框架設定** | ✅ 使用外掛 | 打包框架專屬指令 |
| **企業標準** | ✅ 使用外掛 | 集中分發，版本控制 |
| **快速任務自動化** | ❌ 使用指令 | 過度複雜 |
| **單一領域專業** | ❌ 使用技能 | 太重，改用技能 |
| **專門化分析** | ❌ 使用子代理 | 手動建立或使用技能 |
| **即時資料存取** | ❌ 使用 MCP | 獨立的，不需打包 |

### 何時建立外掛

```mermaid
graph TD
    A["Should I create a plugin?"]
    A -->|Need multiple components| B{"Multiple commands<br/>or subagents<br/>or MCPs?"}
    B -->|Yes| C["✅ Create Plugin"]
    B -->|No| D["Use Individual Feature"]
    A -->|Team workflow| E{"Share with<br/>team?"}
    E -->|Yes| C
    E -->|No| F["Keep as Local Setup"]
    A -->|Complex setup| G{"Needs auto<br/>configuration?"}
    G -->|Yes| C
    G -->|No| D
```

### 發布外掛

**發布步驟：**

1. 建立包含所有元件的外掛結構
2. 撰寫 `.claude-plugin/plugin.json` manifest
3. 建立附文件的 `README.md`
4. 在本機使用 `/plugin install ./my-plugin` 測試
5. 提交到外掛市集
6. 獲得審查和核准
7. 在市集上發布
8. 使用者可以用一個指令安裝

**提交範例：**

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

### 外掛 vs 手動配置

**手動設定（2+ 小時）：**
- 逐一安裝斜線指令
- 個別建立子代理
- 分別配置 MCP
- 手動設定 hooks
- 記錄所有內容
- 與團隊共享（希望他們能正確配置）

**使用外掛（2 分鐘）：**
```bash
/plugin install pr-review
# ✅ 一切已安裝並配置
# ✅ 立即可用
# ✅ 團隊可以複製完全相同的設定
```

---

## 比較與整合

### 功能比較矩陣

| 功能 | 觸發方式 | 持久性 | 範圍 | 使用案例 |
|---------|-----------|------------|-------|----------|
| **斜線指令** | 手動（`/cmd`） | 僅限工作階段 | 單一指令 | 快速捷徑 |
| **子代理** | 自動委派 | 隔離上下文 | 專門化任務 | 任務分配 |
| **記憶體** | 自動載入 | 跨工作階段 | 使用者/團隊上下文 | 長期學習 |
| **MCP 協定** | 自動查詢 | 即時外部 | 即時資料存取 | 動態資訊 |
| **技能** | 自動觸發 | 基於檔案系統 | 可重複使用的專業 | 自動化工作流程 |

### 互動時間線

```mermaid
graph LR
    A["Session Start"] -->|Load| B["Memory (CLAUDE.md)"]
    B -->|Discover| C["Available Skills"]
    C -->|Register| D["Slash Commands"]
    D -->|Connect| E["MCP Servers"]
    E -->|Ready| F["User Interaction"]

    F -->|Type /cmd| G["Slash Command"]
    F -->|Request| H["Skill Auto-Invoke"]
    F -->|Query| I["MCP Data"]
    F -->|Complex task| J["Delegate to Subagent"]

    G -->|Uses| B
    H -->|Uses| B
    I -->|Uses| B
    J -->|Uses| B
```

### 實際整合範例：客戶支援自動化

#### 架構

```mermaid
graph TB
    User["Customer Email"] -->|Receives| Router["Support Router"]

    Router -->|Analyze| Memory["Memory<br/>Customer history"]
    Router -->|Lookup| MCP1["MCP: Customer DB<br/>Previous tickets"]
    Router -->|Check| MCP2["MCP: Slack<br/>Team status"]

    Router -->|Route Complex| Sub1["Subagent: Tech Support<br/>Context: Technical issues"]
    Router -->|Route Simple| Sub2["Subagent: Billing<br/>Context: Payment issues"]
    Router -->|Route Urgent| Sub3["Subagent: Escalation<br/>Context: Priority handling"]

    Sub1 -->|Format| Skill1["Skill: Response Generator<br/>Brand voice maintained"]
    Sub2 -->|Format| Skill2["Skill: Response Generator"]
    Sub3 -->|Format| Skill3["Skill: Response Generator"]

    Skill1 -->|Generate| Output["Formatted Response"]
    Skill2 -->|Generate| Output
    Skill3 -->|Generate| Output

    Output -->|Post| MCP3["MCP: Slack<br/>Notify team"]
    Output -->|Send| Reply["Customer Reply"]
```

#### 請求流程

```markdown
## 客戶支援請求流程

### 1. 傳入的電子郵件
"I'm getting error 500 when trying to upload files. This is blocking my workflow!"

### 2. 記憶體查詢
- 載入包含支援標準的 CLAUDE.md
- 查看客戶歷史：VIP 客戶，本月第 3 次事件

### 3. MCP 查詢
- GitHub MCP：列出開放的 issue（找到相關的錯誤報告）
- Database MCP：檢查系統狀態（沒有報告中斷）
- Slack MCP：檢查工程部門是否已知

### 4. 技能偵測與載入
- 請求匹配「Technical Support」技能
- 從技能載入支援回應模板

### 5. 子代理委派
- 路由到 Tech Support 子代理
- 提供上下文：客戶歷史、錯誤詳情、已知問題
- 子代理有完整存取權限：read、bash、grep 工具

### 6. 子代理處理
Tech Support 子代理：
- 在程式碼庫中搜尋檔案上傳中的 500 錯誤
- 在 commit 8f4a2c 中找到最近的變更
- 建立解決方法文件

### 7. 技能執行
Response Generator 技能：
- 使用品牌語調指南
- 以同理心格式化回應
- 包含解決方法步驟
- 連結相關文件

### 8. MCP 輸出
- 發佈更新到 #support Slack 頻道
- 標記工程團隊
- 在 Jira MCP 中更新工單

### 9. 回應
客戶收到：
- 同理心的確認
- 原因說明
- 即時解決方法
- 永久修復的時間表
- 相關問題的連結
```

### 完整的功能協調

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: Request: "Build auth system"
    Claude->>Memory: Load project standards
    Memory-->>Claude: Auth standards, team practices
    Claude->>MCP: Query GitHub for similar implementations
    MCP-->>Claude: Code examples, best practices
    Claude->>Skills: Detect matching Skills
    Skills-->>Claude: Security Review Skill + Testing Skill
    Claude->>SubAgent: Delegate implementation
    SubAgent->>SubAgent: Build feature
    Claude->>Skills: Apply Security Review Skill
    Skills-->>Claude: Security checklist results
    Claude->>SubAgent: Delegate testing
    SubAgent-->>Claude: Test results
    Claude->>User: Complete system delivered
```

### 何時使用每個功能

```mermaid
graph TD
    A["New Task"] --> B{Type of Task?}

    B -->|Repeated workflow| C["Slash Command"]
    B -->|Need real-time data| D["MCP Protocol"]
    B -->|Remember for next time| E["Memory"]
    B -->|Specialized subtask| F["Subagent"]
    B -->|Domain-specific work| G["Skill"]

    C --> C1["✅ Team shortcut"]
    D --> D1["✅ Live API access"]
    E --> E1["✅ Persistent context"]
    F --> F1["✅ Parallel execution"]
    G --> G1["✅ Auto-invoked expertise"]
```

### 選擇決策樹

```mermaid
graph TD
    Start["Need to extend Claude?"]

    Start -->|Quick repeated task| A{"Manual or Auto?"}
    A -->|Manual| B["Slash Command"]
    A -->|Auto| C["Skill"]

    Start -->|Need external data| D{"Real-time?"}
    D -->|Yes| E["MCP Protocol"]
    D -->|No/Cross-session| F["Memory"]

    Start -->|Complex project| G{"Multiple roles?"}
    G -->|Yes| H["Subagents"]
    G -->|No| I["Skills + Memory"]

    Start -->|Long-term context| J["Memory"]
    Start -->|Team workflow| K["Slash Command +<br/>Memory"]
    Start -->|Full automation| L["Skills +<br/>Subagents +<br/>MCP"]
```

---

## 摘要表

| 面向 | 斜線指令 | 子代理 | 記憶體 | MCP | 技能 | 外掛 |
|--------|---|---|---|---|---|---|
| **設定難度** | 簡單 | 中等 | 簡單 | 中等 | 中等 | 簡單 |
| **學習曲線** | 低 | 中 | 低 | 中 | 中 | 低 |
| **團隊效益** | 高 | 高 | 中 | 高 | 高 | 非常高 |
| **自動化程度** | 低 | 高 | 中 | 高 | 高 | 非常高 |
| **上下文管理** | 單一工作階段 | 隔離 | 持久 | 即時 | 持久 | 所有功能 |
| **維護負擔** | 低 | 中 | 低 | 中 | 中 | 低 |
| **可擴展性** | 良好 | 優秀 | 良好 | 優秀 | 優秀 | 優秀 |
| **可共享性** | 尚可 | 尚可 | 良好 | 良好 | 良好 | 優秀 |
| **版本控制** | 手動 | 手動 | 手動 | 手動 | 手動 | 自動 |
| **安裝** | 手動複製 | 手動配置 | 不適用 | 手動配置 | 手動複製 | 一個指令 |

---

## 快速入門指南

### 第 1 週：從簡單開始
- 為常見任務建立 2-3 個斜線指令
- 在設定中啟用記憶體
- 在 CLAUDE.md 中記錄團隊標準

### 第 2 週：新增即時存取
- 設定 1 個 MCP（GitHub 或 Database）
- 使用 `/mcp` 進行配置
- 在工作流程中查詢即時資料

### 第 3 週：分配工作
- 為特定角色建立第一個子代理
- 使用 `/agents` 指令
- 用簡單任務測試委派

### 第 4 週：全面自動化
- 為重複自動化建立第一個技能
- 使用技能市集或建構自訂技能
- 結合所有功能以建立完整的工作流程

### 持續進行
- 每月審查和更新記憶體
- 在模式出現時新增新技能
- 最佳化 MCP 查詢
- 精煉子代理提示

---

## Hooks

### 概覽

Hooks 是回應 Claude Code 事件時自動執行的事件驅動 shell 指令。它們實現自動化、驗證和自訂工作流程，無需手動介入。

### Hook 事件

Claude Code 支援 **25 個 hook 事件**，分為四種 hook 類型（command、http、prompt、agent）：

| Hook 事件 | 觸發條件 | 使用案例 |
|------------|---------|-----------|
| **SessionStart** | 工作階段開始/恢復/清除/壓縮 | 環境設定、初始化 |
| **InstructionsLoaded** | CLAUDE.md 或規則檔案載入 | 驗證、轉換、擴充 |
| **UserPromptSubmit** | 使用者提交提示 | 輸入驗證、提示過濾 |
| **PreToolUse** | 任何工具執行前 | 驗證、核准關卡、記錄 |
| **PermissionRequest** | 權限對話框顯示 | 自動核准/拒絕流程 |
| **PostToolUse** | 工具成功後 | 自動格式化、通知、清理 |
| **PostToolUseFailure** | 工具執行失敗 | 錯誤處理、記錄 |
| **Notification** | 傳送通知 | 警報、外部整合 |
| **SubagentStart** | 子代理啟動 | 上下文注入、初始化 |
| **SubagentStop** | 子代理完成 | 結果驗證、記錄 |
| **Stop** | Claude 完成回應 | 摘要產生、清理任務 |
| **StopFailure** | API 錯誤結束回合 | 錯誤恢復、記錄 |
| **TeammateIdle** | Agent Team 隊友閒置 | 工作分配、協調 |
| **TaskCompleted** | 任務標記為完成 | 任務後處理 |
| **TaskCreated** | 透過 TaskCreate 建立任務 | 任務追蹤、記錄 |
| **ConfigChange** | 配置檔案變更 | 驗證、傳播 |
| **CwdChanged** | 工作目錄變更 | 目錄專屬設定 |
| **FileChanged** | 監控的檔案變更 | 檔案監控、重建觸發 |
| **PreCompact** | 上下文壓縮前 | 狀態保存 |
| **PostCompact** | 壓縮完成後 | 壓縮後操作 |
| **WorktreeCreate** | 正在建立 Worktree | 環境設定、依賴安裝 |
| **WorktreeRemove** | 正在移除 Worktree | 清理、資源釋放 |
| **Elicitation** | MCP 伺服器請求使用者輸入 | 輸入驗證 |
| **ElicitationResult** | 使用者回應徵詢 | 回應處理 |
| **SessionEnd** | 工作階段終止 | 清理、最終記錄 |

### 常見 Hooks

Hooks 配置在 `~/.claude/settings.json`（使用者級別）或 `.claude/settings.json`（專案級別）中：

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

### Hook 環境變數

- `$CLAUDE_FILE_PATH` - 正在編輯/寫入的檔案路徑
- `$CLAUDE_TOOL_NAME` - 正在使用的工具名稱
- `$CLAUDE_SESSION_ID` - 當前工作階段識別碼
- `$CLAUDE_PROJECT_DIR` - 專案目錄路徑

### 最佳實務

✅ **應做：**
- 保持 hooks 快速（< 1 秒）
- 使用 hooks 進行驗證和自動化
- 優雅地處理錯誤
- 使用絕對路徑

❌ **不應做：**
- 不要讓 hooks 具有互動性
- 不要將 hooks 用於長時間運行的任務
- 不要硬編碼憑證

**參見**：[06-hooks/](06-hooks/) 以獲取詳細範例

---

## 檢查點與倒轉

### 概覽

檢查點允許您儲存對話狀態並倒轉到先前的時間點，實現安全的實驗和探索多種方法。

### 關鍵概念

| 概念 | 說明 |
|---------|-------------|
| **檢查點** | 對話狀態的快照，包括訊息、檔案和上下文 |
| **倒轉** | 返回到先前的檢查點，捨棄後續的變更 |
| **分支點** | 從中探索多種方法的檢查點 |

### 存取檢查點

檢查點會在每次使用者提示時自動建立。要倒轉：

```bash
# 按兩次 Esc 開啟檢查點瀏覽器
Esc + Esc

# 或使用 /rewind 指令
/rewind
```

當您選擇一個檢查點時，您可以從五個選項中選擇：
1. **還原程式碼和對話** -- 將兩者都倒轉到該時間點
2. **還原對話** -- 倒轉訊息，保留當前程式碼
3. **還原程式碼** -- 倒轉檔案，保留對話
4. **從此處摘要** -- 將對話壓縮為摘要
5. **取消** -- 取消

### 使用案例

| 情境 | 工作流程 |
|----------|----------|
| **探索方法** | 儲存 → 嘗試 A → 儲存 → 倒轉 → 嘗試 B → 比較 |
| **安全重構** | 儲存 → 重構 → 測試 → 如果失敗：倒轉 |
| **A/B 測試** | 儲存 → 設計 A → 儲存 → 倒轉 → 設計 B → 比較 |
| **錯誤恢復** | 發現問題 → 倒轉到上一個正常狀態 |

### 配置

```json
{
  "autoCheckpoint": true
}
```

**參見**：[08-checkpoints/](08-checkpoints/) 以獲取詳細範例

---

## 進階功能

### 規劃模式

在編碼之前建立詳細的實作計畫。

**啟動方式：**
```bash
/plan Implement user authentication system
```

**優點：**
- 附時間估算的清晰路線圖
- 風險評估
- 系統性任務分解
- 審查和修改的機會

### 延伸思考

針對複雜問題的深度推理。

**啟動方式：**
- 在工作階段中使用 `Alt+T`（或 macOS 上的 `Option+T`）切換
- 設定 `MAX_THINKING_TOKENS` 環境變數以進行程式化控制

```bash
# 透過環境變數啟用延伸思考
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**優點：**
- 全面的權衡分析
- 更好的架構決策
- 邊界情況的考慮
- 系統性評估

### 背景任務

在不阻塞對話的情況下執行長時間操作。

**使用方式：**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # 顯示所有任務
/task status bg-1234 # 檢查進度
/task show bg-1234   # 查看輸出
/task cancel bg-1234 # 取消任務
```

### 權限模式

控制 Claude 可以做什麼。

| 模式 | 說明 | 使用案例 |
|------|-------------|----------|
| **default** | 帶敏感操作提示的標準權限 | 一般開發 |
| **acceptEdits** | 不需確認自動接受檔案編輯 | 受信任的編輯工作流程 |
| **plan** | 僅分析和規劃，不修改檔案 | 程式碼審查、架構規劃 |
| **auto** | 自動核准安全操作，僅對風險操作提示 | 平衡的自主性與安全性 |
| **dontAsk** | 不需確認提示即執行所有操作 | 有經驗的使用者、自動化 |
| **bypassPermissions** | 完全不受限制的存取，無安全檢查 | CI/CD 管道、受信任的腳本 |

**使用方式：**
```bash
claude --permission-mode plan          # 唯讀分析
claude --permission-mode acceptEdits   # 自動接受編輯
claude --permission-mode auto          # 自動核准安全操作
claude --permission-mode dontAsk       # 無確認提示
```

### Headless 模式（列印模式）

使用 `-p`（列印）旗標在沒有互動輸入的情況下執行 Claude Code，用於自動化和 CI/CD。

**使用方式：**
```bash
# 執行特定任務
claude -p "Run all tests"

# 管道輸入進行分析
cat error.log | claude -p "explain this error"

# CI/CD 整合（GitHub Actions）
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# 用於腳本編寫的 JSON 輸出
claude -p --output-format json "list all functions in src/"
```

### 排程任務

使用 `/loop` 指令按重複排程執行任務。

**使用方式：**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

排程任務在背景執行，完成後報告結果。它們適用於持續監控、定期檢查和自動化維護工作流程。

### Chrome 整合

Claude Code 可以與 Chrome 瀏覽器整合，進行 Web 自動化任務。這使得在開發工作流程中可以直接瀏覽網頁、填寫表單、截取螢幕截圖和從網站擷取資料等功能。

### 工作階段管理

管理多個工作階段。

**指令：**
```bash
/resume                # 恢復先前的對話
/rename "Feature"      # 命名當前工作階段
/fork                  # 分叉為新的工作階段
claude -c              # 繼續最近的對話
claude -r "Feature"    # 按名稱/ID 恢復工作階段
```

### 互動功能

**鍵盤快捷鍵：**
- `Ctrl + R` - 搜尋指令歷史
- `Tab` - 自動完成
- `↑ / ↓` - 指令歷史
- `Ctrl + L` - 清除螢幕

**多行輸入：**
```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

### 配置

完整配置範例：

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

**參見**：[09-advanced-features/](09-advanced-features/) 以獲取完整指南

---

## 資源

- [Claude Code 文件](https://code.claude.com/docs/en/overview)
- [Anthropic 文件](https://docs.anthropic.com)
- [MCP GitHub 伺服器](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*最後更新：2026 年 3 月*
*適用於 Claude Haiku 4.5、Sonnet 4.6 和 Opus 4.6*
*現在包含：Hooks、檢查點、規劃模式、延伸思考、背景任務、權限模式（6 種模式）、Headless 模式、工作階段管理、自動記憶、Agent Teams、排程任務、Chrome 整合、頻道、語音輸入和內建技能*
