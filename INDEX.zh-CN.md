<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例总索引（Complete Index）

本文档按功能类别整理了全部示例文件的完整索引。

## 统计摘要

- **文件总数**：100+ files
- **类别数量**：10 feature categories
- **插件数量**：3 complete plugins
- **技能数量**：6 complete skills
- **Hooks 数量**：8 example hooks
- **可直接使用**：All examples

---

## 01. Slash Commands（10 files）

用户触发的常见工作流快捷命令。

| File | Description | Use Case |
|------|-------------|----------|
| `optimize.md` | 代码优化分析器 | 查找性能问题 |
| `pr.md` | Pull Request 准备 | PR 流程自动化 |
| `generate-api-docs.md` | API 文档生成器 | 生成 API 文档 |
| `commit.md` | Commit 消息助手 | 统一提交规范 |
| `setup-ci-cd.md` | CI/CD 流水线初始化 | DevOps 自动化 |
| `push-all.md` | 推送全部变更 | 快速推送工作流 |
| `unit-test-expand.md` | 扩展单元测试覆盖 | 测试自动化 |
| `doc-refactor.md` | 文档重构 | 文档改进 |
| `pr-slash-command.png` | 示例截图 | 可视化参考 |
| `README.md` | 文档说明 | 安装与使用指南 |

**Installation Path**: `.claude/commands/`

**Usage**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Memory（6 files）

持久化上下文与项目规范。

| File | Description | Scope | Location |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | 团队项目规范 | Project-wide | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 目录专属规则 | Directory | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 个人偏好 | User | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 截图：memory saved | - | 可视化参考 |
| `memory-ask-claude.png` | 截图：ask Claude | - | 可视化参考 |
| `README.md` | 文档说明 | - | 参考资料 |

**Installation**: Copy to appropriate location

**Usage**: Automatically loaded by Claude

---

## 03. Skills（28 files）

可自动触发的能力模块（含脚本和模板）。

### Code Review Skill（5 files）
```text
code-review/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-metrics.py            # Code metrics analyzer
│   └── compare-complexity.py         # Complexity comparison
└── templates/
    ├── review-checklist.md           # Review checklist
    └── finding-template.md           # Finding documentation
```

**Purpose**: 含安全、性能与质量分析的综合代码评审

**Auto-invoked**: 代码评审时

---

### Brand Voice Skill（4 files）
```text
brand-voice/
├── SKILL.md                          # Skill definition
├── templates/
│   ├── email-template.txt            # Email format
│   └── social-post-template.txt      # Social media format
└── tone-examples.md                  # Example messages
```

**Purpose**: 保持沟通中的品牌语气一致

**Auto-invoked**: 生成营销文案时

---

### Documentation Generator Skill（2 files）
```text
doc-generator/
├── SKILL.md                          # Skill definition
└── generate-docs.py                  # Python doc extractor
```

**Purpose**: 从源码生成完整 API 文档

**Auto-invoked**: 创建/更新 API 文档时

---

### Refactor Skill（5 files）
```text
refactor/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-complexity.py         # Complexity analyzer
│   └── detect-smells.py              # Code smell detector
├── references/
│   ├── code-smells.md                # Code smells catalog
│   └── refactoring-catalog.md        # Refactoring patterns
└── templates/
    └── refactoring-plan.md           # Refactoring plan template
```

**Purpose**: 基于复杂度分析的系统化代码重构

**Auto-invoked**: 重构代码时

---

### Claude MD Skill（1 file）
```text
claude-md/
└── SKILL.md                          # Skill definition
```

**Purpose**: 管理与优化 CLAUDE.md 文件

---

### Blog Draft Skill（3 files）
```text
blog-draft/
├── SKILL.md                          # Skill definition
└── templates/
    ├── draft-template.md             # Blog draft template
    └── outline-template.md           # Blog outline template
```

**Purpose**: 以统一结构起草博客

**Plus**: `README.md` - Skills 总览与使用指南

**Installation Path**: `~/.claude/skills/` or `.claude/skills/`

---

## 04. Subagents（9 files）

具备定制能力的专用 AI 助手。

| File | Description | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | 代码质量分析 | read, grep, diff, lint_runner | 综合评审 |
| `test-engineer.md` | 测试覆盖分析 | read, write, bash, grep | 测试自动化 |
| `documentation-writer.md` | 文档创建 | read, write, grep | 文档生成 |
| `secure-reviewer.md` | 安全评审（只读） | read, grep | 安全审计 |
| `implementation-agent.md` | 全流程实现 | read, write, bash, grep, edit, glob | 功能开发 |
| `debugger.md` | 调试专员 | read, bash, grep | 问题定位 |
| `data-scientist.md` | 数据分析专员 | read, write, bash | 数据工作流 |
| `clean-code-reviewer.md` | Clean Code 标准审查 | read, grep | 代码质量 |
| `README.md` | 文档说明 | - | 安装与使用指南 |

**Installation Path**: `.claude/agents/`

**Usage**: Automatically delegated by main agent

---

## 05. MCP Protocol（5 files）

外部工具与 API 集成。

| File | Description | Integrates With | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub 集成 | GitHub API | PR/Issue 管理 |
| `database-mcp.json` | 数据库查询 | PostgreSQL/MySQL | 在线数据查询 |
| `filesystem-mcp.json` | 文件操作 | Local filesystem | 文件管理 |
| `multi-mcp.json` | 多服务器组合 | GitHub + DB + Slack | 完整集成 |
| `README.md` | 文档说明 | - | 安装与使用指南 |

**Installation Path**: `.mcp.json` (project scope) or `~/.claude.json` (user scope)

**Usage**: `/mcp__github__list_prs`, etc.

---

## 06. Hooks（9 files）

事件驱动自动化脚本（自动执行）。

| File | Description | Event | Use Case |
|------|-------------|-------|----------|
| `format-code.sh` | 自动格式化代码 | PreToolUse:Write | 代码格式化 |
| `pre-commit.sh` | 提交前跑测试 | PreToolUse:Bash | 测试自动化 |
| `security-scan.sh` | 安全扫描 | PostToolUse:Write | 安全校验 |
| `log-bash.sh` | 记录 bash 命令 | PostToolUse:Bash | 命令审计 |
| `validate-prompt.sh` | 校验 prompt | PreToolUse | 输入校验 |
| `notify-team.sh` | 发送通知 | Notification | 团队通知 |
| `context-tracker.py` | 追踪上下文窗口占用 | PostToolUse | 上下文监控 |
| `context-tracker-tiktoken.py` | 基于 token 的上下文追踪 | PostToolUse | 精准 token 统计 |
| `README.md` | 文档说明 | - | 安装与使用指南 |

**Installation Path**: Configure in `~/.claude/settings.json`

**Usage**: Configured in settings, executed automatically

**Hook Types** (4 types, 25 events):
- Tool Hooks: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Session Hooks: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Task Hooks: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Lifecycle Hooks: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Plugins（3 complete plugins, 40 files）

打包化能力集合。

### PR Review Plugin（10 files）
```text
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── review-pr.md                  # Comprehensive review
│   ├── check-security.md             # Security check
│   └── check-tests.md                # Test coverage check
├── agents/
│   ├── security-reviewer.md          # Security specialist
│   ├── test-checker.md               # Test specialist
│   └── performance-analyzer.md       # Performance specialist
├── mcp/
│   └── github-config.json            # GitHub integration
├── hooks/
│   └── pre-review.js                 # Pre-review validation
└── README.md                         # Plugin documentation
```

**Features**: 安全分析、测试覆盖、性能影响评估

**Commands**: `/review-pr`, `/check-security`, `/check-tests`

**Installation**: `/plugin install pr-review`

---

### DevOps Automation Plugin（15 files）
```text
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── deploy.md                     # Deployment
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # System status
│   └── incident.md                   # Incident response
├── agents/
│   ├── deployment-specialist.md      # Deployment expert
│   ├── incident-commander.md         # Incident coordinator
│   └── alert-analyzer.md             # Alert analyzer
├── mcp/
│   └── kubernetes-config.json        # Kubernetes integration
├── hooks/
│   ├── pre-deploy.js                 # Pre-deployment checks
│   └── post-deploy.js                # Post-deployment tasks
├── scripts/
│   ├── deploy.sh                     # Deployment automation
│   ├── rollback.sh                   # Rollback automation
│   └── health-check.sh               # Health checks
└── README.md                         # Plugin documentation
```

**Features**: Kubernetes 部署、回滚、监控、故障响应

**Commands**: `/deploy`, `/rollback`, `/status`, `/incident`

**Installation**: `/plugin install devops-automation`

---

### Documentation Plugin（14 files）
```text
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── generate-api-docs.md          # API docs generation
│   ├── generate-readme.md            # README creation
│   ├── sync-docs.md                  # Doc synchronization
│   └── validate-docs.md              # Doc validation
├── agents/
│   ├── api-documenter.md             # API doc specialist
│   ├── code-commentator.md           # Code comment specialist
│   └── example-generator.md          # Example creator
├── mcp/
│   └── github-docs-config.json       # GitHub integration
├── templates/
│   ├── api-endpoint.md               # API endpoint template
│   ├── function-docs.md              # Function doc template
│   └── adr-template.md               # ADR template
└── README.md                         # Plugin documentation
```

**Features**: API 文档、README 生成、文档同步与校验

**Commands**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Installation**: `/plugin install documentation`

**Plus**: `README.md` - Plugins 总览与使用指南

---

## 08. Checkpoints and Rewind（2 files）

保存会话状态并探索替代实现路径。

| File | Description | Content |
|------|-------------|---------|
| `README.md` | 文档说明 | 完整 checkpoint 指南 |
| `checkpoint-examples.md` | 真实案例 | 数据迁移、性能优化、UI 迭代、调试 |
| | | |

**Key Concepts**:
- **Checkpoint**: Snapshot of conversation state
- **Rewind**: Return to previous checkpoint
- **Branch Point**: Explore multiple approaches

**Usage**:
```text
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind
# Then choose: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, or Never mind
```

**Use Cases**:
- Try different implementations
- Recover from mistakes
- Safe experimentation
- Compare solutions
- A/B testing

---

## 09. Advanced Features（3 files）

面向复杂工作流的高级能力。

| File | Description | Features |
|------|-------------|----------|
| `README.md` | 完整指南 | 全部高级能力文档 |
| `config-examples.json` | 配置示例 | 10+ 场景配置模板 |
| `planning-mode-examples.md` | 规划示例 | REST API、数据库迁移、重构 |
| Scheduled Tasks | 使用 `/loop` 与 cron 工具执行周期任务 | 自动化周期工作流 |
| Chrome Integration | 基于 headless Chromium 的浏览器自动化 | Web 测试与抓取 |
| Remote Control (expanded) | 连接方式、安全注意、对比表 | 远程会话管理 |
| Keyboard Customization | 自定义快捷键、组合键、上下文激活 | 个性化操作 |
| Desktop App (expanded) | Connectors、launch.json、企业能力 | 桌面集成 |
| | | |

**Advanced Features Covered**:

### Planning Mode
- 制定详细实现计划
- 时间预估与风险评估
- 结构化任务拆解

### Extended Thinking
- 复杂问题深度推理
- 架构决策分析
- 方案取舍评估

### Background Tasks
- 长任务不阻塞主流程
- 并行开发工作流
- 任务管理与监控

### Permission Modes
- **default**: 高风险操作前询问
- **acceptEdits**: 自动接受编辑，其他操作询问
- **plan**: 只读分析，不改动
- **auto**: 安全操作自动通过，风险操作询问
- **dontAsk**: 接受除高风险外的操作
- **bypassPermissions**: 全部通过（需 `--dangerously-skip-permissions`）

### Headless Mode (`claude -p`)
- CI/CD 集成
- 自动化任务执行
- 批处理流程

### Session Management
- 多会话并行
- 会话切换与保存
- 会话持久化

### Interactive Features
- 快捷键
- 命令历史
- Tab 补全
- 多行输入

### Configuration
- 全面 settings 管理
- 环境差异化配置
- 按项目定制

### Scheduled Tasks
- 使用 `/loop` 进行周期任务
- cron 工具：CronCreate、CronList、CronDelete
- 自动化重复工作

### Chrome Integration
- headless Chromium 自动化
- Web 测试与抓取
- 页面交互与数据提取

### Remote Control（expanded）
- 连接方式与协议
- 安全注意事项与最佳实践
- 远程接入方案对比

### Keyboard Customization
- 自定义快捷键配置
- 组合键（chord）支持
- 基于上下文的键位激活

### Desktop App（expanded）
- IDE 连接器
- launch.json 配置
- 企业级部署能力

---

## 10. CLI Usage（1 file）

命令行使用模式与参考。

| File | Description | Content |
|------|-------------|---------|
| `README.md` | CLI 文档 | 参数、选项与使用模式 |

**Key CLI Features**:
- `claude` - 启动交互会话
- `claude -p "prompt"` - 无头/非交互模式
- `claude web` - 启动 Web 会话
- `claude --model` - 选择模型（Sonnet 4.6, Opus 4.6）
- `claude --permission-mode` - 设置权限模式
- `claude --remote` - 通过 WebSocket 启用远程控制

---

## 文档文件（13 files）

| File | Location | Description |
|------|----------|-------------|
| `README.md` | `/` | 主入口总览 |
| `INDEX.md` | `/` | 本完整索引 |
| `QUICK_REFERENCE.md` | `/` | 快速参考卡 |
| `README.md` | `/01-slash-commands/` | Slash commands 指南 |
| `README.md` | `/02-memory/` | Memory 指南 |
| `README.md` | `/03-skills/` | Skills 指南 |
| `README.md` | `/04-subagents/` | Subagents 指南 |
| `README.md` | `/05-mcp/` | MCP 指南 |
| `README.md` | `/06-hooks/` | Hooks 指南 |
| `README.md` | `/07-plugins/` | Plugins 指南 |
| `README.md` | `/08-checkpoints/` | Checkpoints 指南 |
| `README.md` | `/09-advanced-features/` | Advanced features 指南 |
| `README.md` | `/10-cli/` | CLI 指南 |

---

## 完整文件树

```text
claude-howto/
├── README.md                                    # Main overview
├── INDEX.md                                     # This file
├── QUICK_REFERENCE.md                           # Quick reference card
├── claude_concepts_guide.md                     # Original guide
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI Usage
    └── README.md
```

---

## 按使用场景快速开始

### 代码质量与评审
```bash
# 安装 slash command
cp 01-slash-commands/optimize.md .claude/commands/

# 安装 subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# 安装 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 或直接安装完整 plugin
/plugin install pr-review
```

### DevOps 与部署
```bash
# 安装插件（包含完整能力）
/plugin install devops-automation
```

### 文档自动化
```bash
# 安装 slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 安装 subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# 安装 skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# 或安装完整插件
/plugin install documentation
```

### 团队标准
```bash
# 配置项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 按团队规范修改内容
```

### 外部系统集成
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装 MCP 配置（项目级）
cp 05-mcp/multi-mcp.json .mcp.json
```

### 自动化与校验
```bash
# 安装 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在 settings 中配置 hooks（~/.claude/settings.json）
# 详见 06-hooks/README.md
```

### 安全实验
```bash
# Checkpoints are created automatically with every user prompt
# To rewind: press Esc+Esc or use /rewind
# Then choose what to restore from the rewind menu

# See 08-checkpoints/README.md for examples
```

### 高级工作流
```bash
# 配置高级能力
# See 09-advanced-features/config-examples.json

# 使用 planning mode
/plan Implement feature X

# 使用权限模式
claude --permission-mode plan          # For code review (read-only)
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions

# 在 CI/CD 使用无头模式
claude -p "Run tests and report results"

# 运行后台任务
Run tests in background

# See 09-advanced-features/README.md for complete guide
```

---

## 功能覆盖矩阵

| Category | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Images | Total |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagents** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## 学习路径

### Beginner（Week 1）
1. ✅ 阅读 `README.md`
2. ✅ 安装 1-2 个 slash commands
3. ✅ 创建项目 memory 文件
4. ✅ 体验基础命令

### Intermediate（Week 2-3）
1. ✅ 配置 GitHub MCP
2. ✅ 安装一个 subagent
3. ✅ 体验委派任务
4. ✅ 安装一个 skill

### Advanced（Week 4+）
1. ✅ 安装完整 plugin
2. ✅ 创建自定义 slash commands
3. ✅ 创建自定义 subagent
4. ✅ 创建自定义 skill
5. ✅ 构建自定义 plugin

### Expert（Week 5+）
1. ✅ 用 hooks 做自动化
2. ✅ 用 checkpoints 做安全实验
3. ✅ 配置 planning mode
4. ✅ 熟练使用 permission modes
5. ✅ 在 CI/CD 中使用 headless mode
6. ✅ 熟练管理会话

---

## 按关键词检索

### Performance
- `01-slash-commands/optimize.md` - 性能分析
- `04-subagents/code-reviewer.md` - 性能评审
- `03-skills/code-review/` - 性能指标
- `07-plugins/pr-review/agents/performance-analyzer.md` - 性能专员

### Security
- `04-subagents/secure-reviewer.md` - 安全评审
- `03-skills/code-review/` - 安全分析
- `07-plugins/pr-review/` - 安全检查

### Testing
- `04-subagents/test-engineer.md` - 测试工程师
- `07-plugins/pr-review/commands/check-tests.md` - 覆盖率检查

### Documentation
- `01-slash-commands/generate-api-docs.md` - API 文档命令
- `04-subagents/documentation-writer.md` - 文档 agent
- `03-skills/doc-generator/` - 文档 skill
- `07-plugins/documentation/` - 完整文档插件

### Deployment
- `07-plugins/devops-automation/` - 完整 DevOps 方案

### Automation
- `06-hooks/` - 事件驱动自动化
- `06-hooks/pre-commit.sh` - 提交前自动化
- `06-hooks/format-code.sh` - 自动格式化
- `09-advanced-features/` - CI/CD 无头模式

### Validation
- `06-hooks/security-scan.sh` - 安全校验
- `06-hooks/validate-prompt.sh` - prompt 校验

### Experimentation
- `08-checkpoints/` - 回退式安全实验
- `08-checkpoints/checkpoint-examples.md` - 真实案例

### Planning
- `09-advanced-features/planning-mode-examples.md` - 规划示例
- `09-advanced-features/README.md` - Extended Thinking

### Configuration
- `09-advanced-features/config-examples.json` - 配置示例

---

## 说明

- 全部示例都可直接使用
- 请根据实际场景按需改造
- 示例遵循 Claude Code 最佳实践
- 每个类别都配有 README 详细说明
- 脚本包含基础错误处理
- 模板可按需定制

---

## 贡献

如果想补充更多示例，请遵循：
1. 创建对应子目录
2. 提供 README.md 说明用法
3. 遵循命名规范
4. 充分测试
5. 更新本索引

---

**Last Updated**: March 2026
**Total Examples**: 100+ files
**Categories**: 10 features
**Hooks**: 8 automation scripts
**Configuration Examples**: 10+ scenarios
**Ready to Use**: All examples
