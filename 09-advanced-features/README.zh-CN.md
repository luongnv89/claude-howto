<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Advanced Features

本指南系统介绍 Claude Code 的高级能力，包括：规划模式、深度思考、自动模式、后台任务、权限模式、非交互打印模式、会话管理、交互能力、Channels、语音听写、远程控制、Web 会话、桌面应用、任务列表、提示建议、Git Worktrees、沙箱、企业托管设置与配置管理。

## 目录

1. [Overview](#overview)
2. [Planning Mode](#planning-mode)
3. [Extended Thinking](#extended-thinking)
4. [Auto Mode](#auto-mode)
5. [Background Tasks](#background-tasks)
6. [Scheduled Tasks](#scheduled-tasks)
7. [Permission Modes](#permission-modes)
8. [Headless Mode](#headless-mode)
9. [Session Management](#session-management)
10. [Interactive Features](#interactive-features)
11. [Voice Dictation](#voice-dictation)
12. [Channels](#channels)
13. [Chrome Integration](#chrome-integration)
14. [Remote Control](#remote-control)
15. [Web Sessions](#web-sessions)
16. [Desktop App](#desktop-app)
17. [Task List](#task-list)
18. [Prompt Suggestions](#prompt-suggestions)
19. [Git Worktrees](#git-worktrees)
20. [Sandboxing](#sandboxing)
21. [Managed Settings (Enterprise)](#managed-settings-enterprise)
22. [Configuration and Settings](#configuration-and-settings)
23. [Best Practices](#best-practices)
24. [Additional Resources](#additional-resources)

---

## Overview

Claude Code 的高级能力在基础编码功能上增加了更强的规划、推理、自动化与控制机制，适合复杂开发任务、代码评审、自动化流水线与多会话协作。

**关键高级能力包括：**
- **Planning Mode**：编码前先生成可评审的实现计划
- **Extended Thinking**：针对复杂问题进行深度推理
- **Auto Mode**：后台安全分类器在每次动作执行前进行审查（Research Preview）
- **Background Tasks**：长任务后台运行，不阻塞当前对话
- **Permission Modes**：控制 Claude 的可执行范围（`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`）
- **Print Mode**：非交互运行 Claude Code，适用于自动化和 CI/CD（`claude -p`）
- **Session Management**：管理和切换多个会话
- **Interactive Features**：快捷键、多行输入、历史记录
- **Voice Dictation**：按键说话输入，支持 20 种语言 STT
- **Channels**：MCP 服务器向运行中的会话推送消息（Research Preview）
- **Remote Control**：通过 Claude.ai 或 Claude App 远程控制本地 Claude Code
- **Web Sessions**：在浏览器（claude.ai/code）中运行 Claude Code
- **Desktop App**：桌面独立应用，支持可视化 diff 与多会话
- **Task List**：上下文压缩后仍保留的任务追踪
- **Prompt Suggestions**：基于上下文的智能命令建议
- **Git Worktrees**：隔离工作树并行开发
- **Sandboxing**：操作系统级文件与网络隔离
- **Managed Settings**：企业通过 plist/Registry/托管文件集中配置
- **Configuration**：通过 JSON 配置文件定制行为

---

## Planning Mode

规划模式允许 Claude 在真正动手实现之前先完成任务分析与实施计划，并由你确认后执行。

### What is Planning Mode?

规划模式分为两阶段：
1. **Planning Phase**：Claude 分析任务并生成详细实现计划
2. **Implementation Phase**：计划获批后按计划执行

### When to Use Planning Mode

✅ 适用场景：
- 多文件复杂重构
- 新功能完整实现
- 架构级调整
- 数据库迁移
- 重大 API 重设计

❌ 不建议用于：
- 简单 bug 修复
- 纯格式化改动
- 单文件小改
- 快速问答

### Activating Planning Mode

**Slash command**:
```bash
/plan Implement user authentication system
```

**CLI flag**:
```bash
claude --permission-mode plan
```

**Set as default**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Keyboard shortcut**:
- `Shift + Tab` - 切换权限模式（含 plan）
- `Alt + M` - 切换权限模式（Windows/Linux）

### Benefits of Planning Mode

- **结构化实施**：先拆分步骤再执行
- **可审阅可调整**：先审计划再改代码
- **风险前置识别**：提前发现潜在问题
- **阶段清晰**：里程碑与执行边界明确

### Example: Feature Implementation

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### Plan Modifications

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Planning Mode Configuration

规划模式可通过 CLI 或斜杠命令启用：

```bash
# Activate plan mode via CLI
claude --permission-mode plan

# Or use the /plan slash command inside the REPL
/plan Implement user authentication system
```

**Model alias for planning**：可使用 `opusplan`（Opus 负责规划，Sonnet 负责执行）：

```bash
claude --model opusplan "design and implement the new API"
```

**Edit plan externally**：按 `Ctrl+G` 可在外部编辑器中修改当前计划。

---

## Extended Thinking

深度思考让 Claude 在输出答案前投入更多推理时间与推理预算，以获得更稳健的结论。

### What is Extended Thinking?

深度思考是一种逐步推理过程，Claude 会：
- 拆解复杂问题
- 对比多种方案
- 评估权衡
- 推演边界情况

### Activating Extended Thinking

**Keyboard shortcut**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - 切换深度思考

**Automatic activation**:
- 所有模型默认启用（Opus 4.6、Sonnet 4.6、Haiku 4.5）
- Opus 4.6 支持自适应推理强度：`low` (○)、`medium` (◐)、`high` (●)、`max`（仅 Opus 4.6）
- 其他模型使用固定预算，最多 31,999 tokens

**Configuration methods**:
- 切换：`Alt+T` / `Option+T`，或通过 `/config`
- 查看推理：`Ctrl+O`（verbose 模式）
- 设置强度：`/effort` 命令或 `--effort` 参数

**Custom budget**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Effort level** (Opus 4.6 only):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), or max (Opus 4.6 only)
```

**CLI flag**:
```bash
claude --effort high "complex architectural review"
```

**Slash command**:
```
/effort high
```

> **Note:** 在提示词中使用 `ultrathink` 会触发更深推理模式。`low`/`medium`/`high`/`max` 决定推理投入。

### Benefits of Extended Thinking

- **更深层推理**：复杂问题决策更稳
- **更好的架构判断**：权衡更完整
- **边界场景覆盖更充分**
- **复杂问题分析更系统**

### Example: Architectural Decision

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### Extended Thinking Configuration

深度思考可通过环境变量、快捷键和 CLI 参数控制：

```bash
# Set thinking token budget
export MAX_THINKING_TOKENS=16000

# Set effort level (Opus 4.6 only): low (○), medium (◐), high (●), or max (Opus 4.6 only)
export CLAUDE_CODE_EFFORT_LEVEL=high
```

会话中可用 `Alt+T` / `Option+T` 切换，用 `/effort` 设置强度，或通过 `/config` 调整。

---

## Auto Mode

自动模式（Research Preview，2026 年 3 月）会在后台使用安全分类器审查每次动作。它允许 Claude 在较高自治下工作，同时默认拦截危险操作。

### Requirements

- **Plan**: Team plan（Enterprise 与 API 方案逐步开放）
- **Model**: Claude Sonnet 4.6 或 Opus 4.6
- **Classifier**: 分类器运行于 Claude Sonnet 4.6（会增加 token 成本）

### Enabling Auto Mode

```bash
# Unlock auto mode with CLI flag
claude --enable-auto-mode

# Then cycle to it with Shift+Tab in the REPL
```

也可直接设为默认权限模式：

```bash
claude --permission-mode auto
```

通过配置设定：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### How the Classifier Works

后台分类器按以下顺序决策：

1. **Allow/deny rules** -- 先检查显式许可规则
2. **Read-only/edits auto-approved** -- 文件读取与编辑自动通过
3. **Classifier** -- 分类器审查动作安全性
4. **Fallback** -- 连续 3 次或累计 20 次拦截后回退为人工确认

### Default Blocked Actions

自动模式默认拦截：

| Blocked Action | Example |
|----------------|---------|
| Pipe-to-shell installs | `curl \| bash` |
| Sending sensitive data externally | API keys, credentials over network |
| Production deploys | Deploy commands targeting production |
| Mass deletion | `rm -rf` on large directories |
| IAM changes | Permission and role modifications |
| Force push to main | `git push --force origin main` |

### Default Allowed Actions

| Allowed Action | Example |
|----------------|---------|
| Local file operations | Read, write, edit project files |
| Declared dependency installs | `npm install`, `pip install` from manifest |
| Read-only HTTP | `curl` for fetching documentation |
| Pushing to current branch | `git push origin feature-branch` |

### Configuring Auto Mode

**Print default rules as JSON**:
```bash
claude auto-mode defaults
```

企业可通过 `autoMode.environment` 托管设置配置“可信基础设施”范围。

### Fallback Behavior

当分类器无法稳定判断时，自动模式会回退为人工确认：
- 连续 **3 次** 分类器拦截
- 会话累计 **20 次** 分类器拦截

这样可以确保在高不确定场景下用户仍保有最终控制权。

### Seeding Auto-Mode-Equivalent Permissions (No Team Plan Required)

如果没有 Team plan，或希望不启用后台分类器，也可以通过保守规则初始化 `~/.claude/settings.json`，获得近似 auto mode 的权限体验。

**File:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added (no changes written)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply the conservative baseline
python3 09-advanced-features/setup-auto-mode-permissions.py

# Add more capability only when you need it
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

脚本会按类别写入权限规则：

| Category | Examples |
|----------|---------|
| Core read-only tools | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| Local inspection | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| Optional edits | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| Optional test/build | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| Optional git writes | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git (local write) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Package managers | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build & test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Common shell | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

危险操作（如 `rm -rf`、`sudo`、force push、`DROP TABLE`、`terraform destroy` 等）会被有意排除。脚本是幂等的，重复执行不会产生重复规则。

---

## Background Tasks

后台任务可以在不打断当前对话的前提下执行耗时操作。

### What Are Background Tasks?

后台任务异步执行，你可以继续处理其它工作：
- 长时间测试套件
- 构建流程
- 数据库迁移
- 部署脚本
- 分析型任务

**Basic Usage:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Starting Background Tasks

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### Managing Background Tasks

**List active tasks**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**Check task status**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**View task output**:
```
User: /task show bg-1234

[Shows live output from the test run]
```

**Cancel task**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### Example: Parallel Development

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### Configuration

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Scheduled Tasks

定时任务允许你按周期或一次性提醒自动运行 prompt。该功能为会话级（session-scoped）：仅在 Claude Code 运行期间有效，会话结束后清空。可用于 v2.1.72+。

### The `/loop` command

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

也支持标准 5 字段 cron 表达式。

### One-time reminders

你可以设置一次性提醒：

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Managing scheduled tasks

| Tool | Description |
|------|-------------|
| `CronCreate` | 创建定时任务 |
| `CronList` | 列出活动定时任务 |
| `CronDelete` | 删除定时任务 |

**限制与行为：**
- 每个会话最多 **50** 个定时任务
- 会话结束后全部清空
- 周期任务会在 **3 天**后自动过期
- Claude Code 不运行时不会补执行错过触发

### Behavior details

| Aspect | Detail |
|--------|--------|
| **Recurring jitter** | 间隔抖动最高 10%（最多 15 分钟） |
| **One-shot jitter** | 在 :00/:30 边界时最多 90 秒抖动 |
| **Missed fires** | 不补执行；未运行期间触发将跳过 |
| **Persistence** | 重启后不持久化 |

### Cloud Scheduled Tasks

使用 `/schedule` 创建云端定时任务（运行在 Anthropic 基础设施）：

```
/schedule daily at 9am run the test suite and report failures
```

云定时任务可跨重启保留，不依赖本地 Claude Code 常驻。

### Disabling scheduled tasks

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### Example: monitoring a deployment

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Tip**: 本地定时任务是会话级。如果你需要可跨重启持久执行的自动化，请使用 CI/CD、GitHub Actions 或 Desktop App 的调度能力。

---

## Permission Modes

权限模式定义了 Claude 在无需你逐次确认时可以执行的操作范围。

### Available Permission Modes

| Mode | Behavior |
|---|---|
| `default` | 仅读文件；其他操作需确认 |
| `acceptEdits` | 读写文件自动通过；命令仍需确认 |
| `plan` | 仅读（研究模式，不执行修改） |
| `auto` | 可执行全部动作，但每步由后台分类器审查（Research Preview） |
| `bypassPermissions` | 全部动作放行，不做权限检查（高风险） |
| `dontAsk` | 仅允许预批准工具，其余全部拒绝 |

可在 CLI 中用 `Shift+Tab` 循环切换，也可通过 `--permission-mode` 或 `permissions.defaultMode` 设置默认。

### Activation Methods

**Keyboard shortcut**:
```bash
Shift + Tab  # Cycle through all 6 modes
```

**Slash command**:
```bash
/plan                  # Enter plan mode
```

**CLI flag**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Setting**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Permission Mode Examples

#### Default Mode
Claude 会在重要操作前请求确认：

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Plan Mode
先出计划再执行：

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### Accept Edits Mode
自动接受文件修改：

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### Use Cases

**Code Review**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Pair Programming**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Automated Tasks**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## Headless Mode

打印模式（`claude -p`）允许 Claude Code 在无交互输入的情况下运行，适合自动化和 CI/CD。它是当前的非交互模式，替代了旧的 `--headless` 参数。

### What is Print Mode?

打印模式可用于：
- 自动化脚本执行
- CI/CD 集成
- 批处理任务
- 定时运行

### Running in Print Mode (Non-Interactive)

```bash
# Run specific task
claude -p "Run all tests"

# Process piped content
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Additional Print Mode Usage Examples

```bash
# Run a specific task with output capture
claude -p "Run all tests and generate coverage report"

# With structured output
claude -p --output-format json "Analyze code quality"

# With input from stdin
echo "Analyze code quality" | claude -p "explain this"
```

### Example: CI/CD Integration

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Print Mode Configuration

打印模式（`claude -p`）支持多个自动化参数：

```bash
# Limit autonomous turns
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# With schema validation
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Disable session persistence
claude -p --no-session-persistence "one-off analysis"
```

---

## Session Management

高效管理多个 Claude Code 会话。

### Session Management Commands

| Command | Description |
|---------|-------------|
| `/resume` | 按 ID 或名称恢复会话 |
| `/rename` | 为当前会话命名 |
| `/fork` | 从当前会话分叉新分支 |
| `claude -c` | 继续最近一次会话 |
| `claude -r "session"` | 按名称或 ID 恢复会话 |

### Resuming Sessions

**Continue last conversation**:
```bash
claude -c
```

**Resume a named session**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Rename the current session** (inside the REPL):
```
/rename auth-refactor
```

### Forking Sessions

从现有会话分叉，以便尝试替代方案且不影响原会话：

```
/fork
```

或在 CLI 中：
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Session Persistence

会话会自动保存并可恢复：

```bash
# Continue last conversation
claude -c

# Resume specific session by name or ID
claude -r "auth-refactor"

# Resume and fork for experimentation
claude --resume auth-refactor --fork-session "alternative approach"
```

---

## Interactive Features

### Keyboard Shortcuts

Claude Code 支持大量快捷键提升效率：

| Shortcut | Description |
|----------|-------------|
| `Ctrl+C` | 取消当前输入/生成 |
| `Ctrl+D` | 退出 Claude Code |
| `Ctrl+G` | 在外部编辑器编辑计划 |
| `Ctrl+L` | 清空终端显示 |
| `Ctrl+O` | 切换详细输出（查看推理） |
| `Ctrl+R` | 反向搜索历史 |
| `Ctrl+T` | 切换任务列表视图 |
| `Ctrl+B` | 将运行任务转后台 |
| `Esc+Esc` | 回退代码/对话（rewind） |
| `Shift+Tab` / `Alt+M` | 切换权限模式 |
| `Option+P` / `Alt+P` | 切换模型 |
| `Option+T` / `Alt+T` | 切换深度思考 |

**Line Editing (standard readline shortcuts):**

| Shortcut | Action |
|----------|--------|
| `Ctrl + A` | 光标移至行首 |
| `Ctrl + E` | 光标移至行尾 |
| `Ctrl + K` | 剪切到行尾 |
| `Ctrl + U` | 剪切到行首 |
| `Ctrl + W` | 向后删除一个词 |
| `Ctrl + Y` | 粘贴（yank） |
| `Tab` | 自动补全 |
| `↑ / ↓` | 历史命令 |

### Customizing keybindings

运行 `/keybindings` 可编辑 `~/.claude/keybindings.json`（v2.1.18+）来自定义快捷键。

**Configuration format**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

将绑定设为 `null` 可取消默认快捷键。

### Available contexts

快捷键按 UI 上下文生效：

| Context | Key Actions |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | 设置页导航动作 |
| **Tabs** | 标签页切换与管理 |
| **Help** | 帮助面板导航 |

共 18 个上下文，此外还包括 `Transcript`、`Task`、`ThemePicker`、`Attachments`、`Footer`、`MessageSelector`、`DiffDialog`、`ModelPicker`、`Select` 等。

### Chord support

支持组合按键序列（Chord）：

```
"ctrl+k ctrl+s"   → 两段按键：先 ctrl+k，再 ctrl+s
"ctrl+shift+p"    → 同时按下修饰键组合
```

**Keystroke syntax**:
- **Modifiers**：`ctrl`、`alt`（或 `opt`）、`shift`、`meta`（或 `cmd`）
- **大写即包含 Shift**：`K` 等价于 `shift+k`
- **特殊键**：`escape`、`enter`、`return`、`tab`、`space`、`backspace`、`delete`、方向键

### Reserved and conflicting keys

| Key | Status | Notes |
|-----|--------|-------|
| `Ctrl+C` | Reserved | 不可重绑定（中断） |
| `Ctrl+D` | Reserved | 不可重绑定（退出） |
| `Ctrl+B` | Terminal conflict | 可能与 tmux 前缀冲突 |
| `Ctrl+A` | Terminal conflict | 可能与 GNU Screen 前缀冲突 |
| `Ctrl+Z` | Terminal conflict | 进程挂起快捷键 |

> **Tip**: 若快捷键无效，请先检查终端模拟器或多路复用器（tmux/screen）冲突。

### Tab Completion

Claude Code 支持智能 Tab 补全：

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### Command History

可快速调用历史命令：

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### Multi-line Input

复杂输入可使用多行模式：

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Example:**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### Inline Editing

发送前可在输入框内原地编辑：

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Vim Mode

启用 Vi/Vim 键位输入模式：

**Activation**:
- 通过 `/vim` 或 `/config` 启用
- `Esc` 进入 NORMAL，`i/a/o` 进入 INSERT

**Navigation keys**:
- `h` / `l` - 左右移动
- `j` / `k` - 上下移动
- `w` / `b` / `e` - 按词移动
- `0` / `$` - 行首/行尾
- `gg` / `G` - 文本开头/结尾

**Text objects**:
- `iw` / `aw` - 词内/词周围
- `i"` / `a"` - 引号内/引号周围
- `i(` / `a(` - 括号内/括号周围

### Bash Mode

使用 `!` 前缀可直接执行 shell 命令：

```bash
! npm test
! git status
! cat src/index.js
```

适合在当前会话中快速执行终端命令，无需切换上下文。

---

## Voice Dictation

语音听写支持按键说话输入（push-to-talk），你可以通过语音向 Claude Code 发出指令。

### Activating Voice Dictation

```
/voice
```

### Features

| Feature | Description |
|---------|-------------|
| **Push-to-talk** | 按住录音，松开发送 |
| **20 languages** | 语音转文本支持 20 种语言 |
| **Custom keybinding** | 可通过 `/keybindings` 自定义按键 |
| **Account requirement** | 需要 Claude.ai 账号用于 STT 处理 |

### Configuration

可在 `/keybindings` 对应文件中配置按键。语音转文本由 Claude.ai 账号侧处理。

---

## Channels

Channels（Research Preview）允许 MCP 服务器将外部消息主动推送到运行中的 Claude Code 会话，实现实时集成。

### Subscribing to Channels

```bash
# Subscribe to channel plugins at startup
claude --channels discord,telegram
```

### Supported Integrations

| Integration | Description |
|-------------|-------------|
| **Discord** | 在会话内接收并回复 Discord 消息 |
| **Telegram** | 在会话内接收并回复 Telegram 消息 |

### Configuration

**Managed setting**（企业托管配置）：

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

`allowedChannelPlugins` 控制组织内允许使用的 channel 插件。

### How It Works

1. MCP 服务器作为 channel 插件连接外部服务
2. 外部消息被推送到当前 Claude Code 会话
3. Claude 在会话上下文中读取并响应消息
4. 插件需通过 `allowedChannelPlugins` 托管设置批准

---

## Chrome Integration

Chrome Integration 可将 Claude Code 连接到 Chrome 或 Microsoft Edge，用于实时网页自动化与调试。该功能为 beta，v2.0.73+ 可用（Edge 支持自 v1.0.36+）。

### Enabling Chrome Integration

**At startup**:

```bash
claude --chrome      # Enable Chrome connection
claude --no-chrome   # Disable Chrome connection
```

**Within a session**:

```
/chrome
```

选择“Enabled by default”后，未来会话默认启用浏览器集成。Claude Code 会共享你浏览器的登录状态，因此可操作已登录网页应用。

### Capabilities

| Capability | Description |
|------------|-------------|
| **Live debugging** | 实时读取控制台日志、检查 DOM、调试 JavaScript |
| **Design verification** | 对照设计稿验证页面渲染 |
| **Form validation** | 测试表单提交流程、输入校验与报错 |
| **Web app testing** | 交互式测试已登录应用（Gmail、Google Docs、Notion 等） |
| **Data extraction** | 页面内容抓取与处理 |
| **Session recording** | 录制浏览器交互为 GIF |

### Site-level permissions

Chrome 扩展按站点管理访问权限。你可随时在扩展面板中授权或撤销指定站点访问，Claude Code 仅能操作你明确允许的网站。

### How it works

Claude Code 在可见浏览器窗口中执行操作，你可实时观察。遇到登录页或 CAPTCHA 时，Claude 会暂停并等待你手动处理后继续。

### Known limitations

- **Browser support**: 仅支持 Chrome 与 Edge，不支持 Brave、Arc 等其他 Chromium 发行版
- **WSL**: 不支持 Windows Subsystem for Linux
- **Third-party providers**: 不支持 Bedrock、Vertex、Foundry 提供商
- **Service worker idle**: Chrome 扩展 service worker 在长会话中可能进入空闲

> **Tip**: 该功能目前是 beta，后续版本可能扩展浏览器支持范围。

---

## Remote Control

Remote Control 允许你在手机、平板或任意浏览器中继续控制本地运行中的 Claude Code 会话。执行仍发生在你的本机，不会迁移到云端。支持 Pro、Max、Team、Enterprise（v2.1.51+）。

### Starting Remote Control

**From the CLI**:

```bash
# Start with default session name
claude remote-control

# Start with a custom name
claude remote-control --name "Auth Refactor"
```

**From within a session**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Available flags**:

| Flag | Description |
|------|-------------|
| `--name "title"` | 自定义会话标题，便于识别 |
| `--verbose` | 输出详细连接日志 |
| `--sandbox` | 启用文件与网络隔离 |
| `--no-sandbox` | 禁用沙箱（默认） |

### Connecting to a session

可通过三种方式在其它设备连接：

1. **Session URL** — 启动时终端会输出可直接访问的 URL
2. **QR code** — 启动后按 `spacebar` 显示二维码
3. **Find by name** — 在 claude.ai/code 或 Claude 移动端按名称查找会话

### Security

- **不开放入站端口**
- **仅出站 HTTPS/TLS**
- **作用域凭证**：短时且权限受限的 token
- **会话隔离**：每个远程会话相互独立

### Remote Control vs Claude Code on the web

| Aspect | Remote Control | Claude Code on Web |
|--------|---------------|-------------------|
| **Execution** | 在你的机器执行 | 在 Anthropic 云端执行 |
| **Local tools** | 可用本地 MCP、文件、CLI | 无本地依赖 |
| **Use case** | 异地继续本地任务 | 从任意浏览器快速开始 |

### Limitations

- 每个 Claude Code 实例仅支持一个远程会话
- 宿主机终端必须保持打开
- 网络不可达约 10 分钟后会话超时

### Use cases

- 离开工位后用手机/平板继续控制 Claude Code
- 利用 claude.ai 更丰富 UI，同时保留本地工具执行
- 在移动端进行快速代码审阅

---

## Web Sessions

Web Sessions 允许你直接在 claude.ai/code 中运行 Claude Code，也可以从 CLI 创建 Web 会话。

### Creating a Web Session

```bash
# Create a new web session from the CLI
claude --remote "implement the new API endpoints"
```

该命令会在 claude.ai 启动一个 Claude Code 会话，你可在任意浏览器访问。

### Resuming Web Sessions Locally

若会话起于 Web，想迁回本地终端继续：

```bash
# Resume a web session in the local terminal
claude --teleport
```

或在交互会话中：
```
/teleport
```

### Use Cases

- 在一台机器开始，另一台机器继续
- 将会话 URL 分享给团队成员
- 在网页 UI 查看 diff，再回终端执行落地

---

## Desktop App

Claude Code Desktop App 是独立桌面应用，提供可视化 diff、并行会话与连接器集成。支持 macOS 与 Windows（Pro、Max、Team、Enterprise）。

### Installation

从 [claude.ai](https://claude.ai) 下载：
- **macOS**：Universal（Apple Silicon + Intel）
- **Windows**：x64 与 ARM64 安装包

安装参考：[Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart)

### Handing off from CLI

将当前 CLI 会话交接到桌面应用：

```
/desktop
```

### Core features

| Feature | Description |
|---------|-------------|
| **Diff view** | 文件级可视化审查，支持内联评论，Claude 可读取评论并修正 |
| **App preview** | 自动启动开发服务器并内嵌浏览器预览 |
| **PR monitoring** | 集成 GitHub CLI，自动修复 CI 失败并在检查通过后自动合并 |
| **Parallel sessions** | 侧栏多会话，并自动使用 Git worktree 隔离 |
| **Scheduled tasks** | 支持小时/每日/工作日/每周定时任务（应用运行期间） |
| **Rich rendering** | 代码、Markdown、图表高亮渲染 |

### App preview configuration

可在 `.claude/launch.json` 中配置预览服务：

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### Connectors

连接外部服务可提供更丰富上下文：

| Connector | Capability |
|-----------|------------|
| **GitHub** | PR 监控、Issue 跟踪、代码评审 |
| **Slack** | 通知与频道上下文 |
| **Linear** | Issue 与迭代管理 |
| **Notion** | 文档与知识库访问 |
| **Asana** | 任务与项目管理 |
| **Calendar** | 日程感知与会议上下文 |

> **Note**: 连接器不适用于远程（云端）会话。

### Remote and SSH sessions

- **Remote sessions**：运行在 Anthropic 云基础设施，应用关闭后仍可继续；可在 claude.ai/code 与移动端访问
- **SSH sessions**：通过 SSH 连接远端机器，访问远程文件系统与工具（远端需安装 Claude Code）

### Permission modes in Desktop

桌面应用支持与 CLI 一致的 4 种权限模式：

| Mode | Behavior |
|------|----------|
| **Ask permissions** (default) | 每次编辑与命令均需审批 |
| **Auto accept edits** | 文件编辑自动通过；命令仍需人工审批 |
| **Plan mode** | 先审查方案，再允许变更 |
| **Bypass permissions** | 自动执行（仅限沙箱模式，且由管理员管控） |

### Enterprise features

- **Admin console**：组织级控制 Code 标签页与权限策略
- **MDM deployment**：macOS 通过 MDM、Windows 通过 MSIX 部署
- **SSO integration**：组织成员强制单点登录
- **Managed settings**：集中管理团队配置与可用模型

---

## Task List

Task List 提供可持久保留的任务追踪，即使会话发生上下文压缩（历史被裁剪）也不会丢失。

### Toggling the Task List

会话中按 `Ctrl+T` 可显示/隐藏任务列表。

### Persistent Tasks

任务可跨上下文压缩保留，适合多步骤长期任务。

### Named Task Directories

可通过 `CLAUDE_CODE_TASK_LIST_ID` 为任务列表指定命名目录，并在多会话间共享：

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

---

## Prompt Suggestions

Prompt Suggestions 会基于 git 历史与当前上下文，在输入框下显示灰色建议命令。

### How It Works

- 建议以灰色文本显示在输入框下方
- 按 `Tab` 接受建议
- 按 `Enter` 可直接接受并提交
- 建议会根据上下文动态变化

### Disabling Prompt Suggestions

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktrees

Git Worktrees 允许在隔离工作树中启动 Claude Code，实现不同分支并行开发，无需频繁 stash/switch。

### Starting in a Worktree

```bash
# Start Claude Code in an isolated worktree
claude --worktree
# or
claude -w
```

### Worktree Location

工作树默认创建于：
```
<repo>/.claude/worktrees/<name>
```

### Sparse Checkout for Monorepos

对于 monorepo，可通过 `worktree.sparsePaths` 开启稀疏检出，减少磁盘占用与初始化时间：

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Worktree Tools and Hooks

| Item | Description |
|------|-------------|
| `ExitWorktree` | 退出并清理当前 worktree |
| `WorktreeCreate` | 创建 worktree 时触发的 Hook 事件 |
| `WorktreeRemove` | 删除 worktree 时触发的 Hook 事件 |

### Auto-Cleanup

若 worktree 无改动，会话结束时会自动清理。

### Use Cases

- 在不影响主分支的情况下开发功能分支
- 在隔离环境中运行测试
- 在可丢弃环境中实验改动
- monorepo 下只检出必要目录以加快启动

---

## Sandboxing

沙箱为 Claude Code 执行 Bash 命令提供操作系统级文件系统与网络隔离。它与权限规则互补，形成更强安全防护。

### Enabling Sandboxing

**Slash command**:
```
/sandbox
```

**CLI flags**:
```bash
claude --sandbox       # Enable sandboxing
claude --no-sandbox    # Disable sandboxing
```

### Configuration Settings

| Setting | Description |
|---------|-------------|
| `sandbox.enabled` | 启用或禁用沙箱 |
| `sandbox.failIfUnavailable` | 若无法启用沙箱则直接失败 |
| `sandbox.filesystem.allowWrite` | 允许写入路径 |
| `sandbox.filesystem.allowRead` | 允许读取路径 |
| `sandbox.filesystem.denyRead` | 禁止读取路径 |
| `sandbox.enableWeakerNetworkIsolation` | 在 macOS 启用较弱网络隔离 |

### Example Configuration

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### How It Works

- Bash 命令在受限沙箱环境中执行
- 可限制网络访问，避免意外外联
- 与 permission rules 叠加形成纵深防御
- 在 macOS 上建议通过 `sandbox.enableWeakerNetworkIsolation` 启用网络限制（macOS 无完整网络隔离）

### Use Cases

- 更安全地运行不可信或自动生成代码
- 防止误改项目目录外文件
- 在自动化任务中限制网络访问

---

## Managed Settings (Enterprise)

托管设置允许企业管理员通过平台原生管理工具，在组织范围集中部署 Claude Code 配置。

### Deployment Methods

| Platform | Method | Since |
|----------|--------|-------|
| macOS | Managed plist files (MDM) | v2.1.51+ |
| Windows | Windows Registry | v2.1.51+ |
| Cross-platform | Managed configuration files | v2.1.51+ |
| Cross-platform | Managed drop-ins (`managed-settings.d/` directory) | v2.1.83+ |

### Managed Drop-ins

从 v2.1.83 起，管理员可在 `managed-settings.d/` 目录投放多个托管配置文件，按字母顺序合并，便于分层策略管理：

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Available Managed Settings

| Setting | Description |
|---------|-------------|
| `disableBypassPermissionsMode` | 禁止用户启用 bypass permissions |
| `availableModels` | 限制可选模型范围 |
| `allowedChannelPlugins` | 控制允许的 channel 插件 |
| `autoMode.environment` | 配置 auto mode 的可信基础设施 |
| Custom policies | 组织自定义权限与工具策略 |

### Example: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Configuration and Settings

### Configuration File Locations

1. **Global config**: `~/.claude/config.json`
2. **Project config**: `./.claude/config.json`
3. **User config**: `~/.config/claude-code/settings.json`

### Complete Configuration Example

**Core advanced features configuration:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**Extended configuration example:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Environment Variables

可通过环境变量覆盖配置：

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=true

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### Configuration Management Commands

```
User: /config
[Opens interactive configuration menu]
```

`/config` 提供交互菜单，可切换：
- 深度思考开关
- 详细输出
- 权限模式
- 模型选择

### Per-Project Configuration

在项目内创建 `.claude/config.json`：

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Best Practices

### Planning Mode
- ✅ 用于复杂多步骤任务
- ✅ 执行前先审计划
- ✅ 必要时修改计划
- ❌ 简单任务不必使用

### Extended Thinking
- ✅ 用于架构决策
- ✅ 用于复杂问题求解
- ✅ 关注推理过程
- ❌ 简单查询不必开启高强度推理

### Background Tasks
- ✅ 用于耗时任务
- ✅ 持续监控进度
- ✅ 妥善处理失败任务
- ❌ 避免并发任务过多

### Permissions
- ✅ `plan` 适合只读评审
- ✅ `default` 适合互动开发
- ✅ `acceptEdits` 适合自动化编辑流
- ✅ `auto` 适合带安全护栏的自治执行
- ❌ 非必要不要使用 `bypassPermissions`

### Sessions
- ✅ 不同任务分不同会话
- ✅ 保留重要会话状态
- ✅ 定期清理旧会话
- ❌ 不要把无关任务混在同一会话

---

## Additional Resources

更多信息可参考：

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode)
- [Official Headless Mode Documentation](https://code.claude.com/docs/en/headless)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Checkpoints Guide](../08-checkpoints/) - Session management and rewinding
- [Slash Commands](../01-slash-commands/) - Command reference
- [Memory Guide](../02-memory/) - Persistent context
- [Skills Guide](../03-skills/) - Autonomous capabilities
- [Subagents Guide](../04-subagents/) - Delegated task execution
- [MCP Guide](../05-mcp/) - External data access
- [Hooks Guide](../06-hooks/) - Event-driven automation
- [Plugins Guide](../07-plugins/) - Bundled extensions
- [Official Scheduled Tasks Documentation](https://code.claude.com/docs/en/scheduled-tasks)
- [Official Chrome Integration Documentation](https://code.claude.com/docs/en/chrome)
- [Official Remote Control Documentation](https://code.claude.com/docs/en/remote-control)
- [Official Keybindings Documentation](https://code.claude.com/docs/en/keybindings)
- [Official Desktop App Documentation](https://code.claude.com/docs/en/desktop)
