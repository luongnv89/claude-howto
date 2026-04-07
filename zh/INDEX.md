<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例 - 完整索引

这份文档是仓库里所有示例文件的完整索引，按功能类型整理，方便你快速定位需要的内容。

## 概览统计

- **总文件数**：100+ 文件
- **分类数**：10 个功能分类
- **插件**：3 个完整插件
- **Skills**：6 个完整 skills
- **Hooks**：8 个示例 hook
- **可直接使用**：所有示例都可直接拿来用

---

## 01. Slash Commands（10 个文件）

用于常见工作流的用户触发快捷命令。

| 文件 | 说明 | 使用场景 |
|------|------|----------|
| `optimize.md` | 代码优化分析器 | 查找性能问题 |
| `pr.md` | Pull Request 准备 | PR 工作流自动化 |
| `generate-api-docs.md` | API 文档生成器 | 生成 API 文档 |
| `commit.md` | 提交信息助手 | 统一提交风格 |
| `setup-ci-cd.md` | CI/CD 流水线设置 | DevOps 自动化 |
| `push-all.md` | 推送所有变更 | 快速推送工作流 |
| `unit-test-expand.md` | 扩展单元测试覆盖率 | 测试自动化 |
| `doc-refactor.md` | 文档重构 | 文档优化 |
| `pr-slash-command.png` | 截图示例 | 视觉参考 |
| `README.md` | 文档 | 安装与使用指南 |

**安装路径**：`.claude/commands/`

**使用方式**：`/optimize`、`/pr`、`/generate-api-docs`、`/commit`、`/setup-ci-cd`、`/push-all`、`/unit-test-expand`、`/doc-refactor`

---

## 02. Memory（6 个文件）

持久化上下文和项目规范。

| 文件 | 说明 | 范围 | 位置 |
|------|------|------|------|
| `project-CLAUDE.md` | 团队项目规范 | 整个项目 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 专用规则 | 目录级 | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 个人偏好 | 用户级 | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 截图：记忆已保存 | - | 视觉参考 |
| `memory-ask-claude.png` | 截图：询问 Claude | - | 视觉参考 |
| `README.md` | 文档 | - | 参考说明 |

**安装方式**：复制到对应位置

**使用方式**：Claude 会自动加载

---

## 03. Skills（28 个文件）

带脚本和模板的自动触发能力。

### 代码审查 Skill（5 个文件）

```text
code-review/
├── SKILL.md                     # Skill 定义
├── scripts/
│   ├── analyze-metrics.py          # 代码指标分析器
│   └── compare-complexity.py       # 复杂度对比
└── templates/
    ├── review-checklist.md      # 审查清单
    └── finding-template.md      # 问题记录模板
```

**用途**：结合安全、性能和质量分析的完整代码审查

**自动触发**：在审查代码时

### 品牌语气 Skill（4 个文件）

```text
brand-voice/
├── SKILL.md                     # Skill 定义
├── templates/
│   ├── email-template.txt          # 邮件格式
│   └── social-post-template.txt    # 社交媒体格式
└── tone-examples.md             # 示例消息
```

**用途**：确保对外沟通中的品牌语气一致

**自动触发**：在编写营销文案时

### 文档生成 Skill（2 个文件）

```text
doc-generator/
├── SKILL.md                     # Skill 定义
└── generate-docs.py                 # Python 文档提取器
```

**用途**：从源代码生成完整的 API 文档

**自动触发**：在创建或更新 API 文档时

### 重构 Skill（5 个文件）

```text
refactor/
├── SKILL.md                     # Skill 定义
├── scripts/
│   ├── analyze-complexity.py       # 复杂度分析器
│   └── detect-smells.py            # 代码异味检测器
├── references/
│   ├── code-smells.md           # 代码异味目录
│   └── refactoring-catalog.md   # 重构模式目录
└── templates/
    └── refactoring-plan.md      # 重构计划模板
```

**用途**：结合复杂度分析进行系统化代码重构

**自动触发**：在重构代码时

### Claude MD Skill（1 个文件）

```text
claude-md/
└── SKILL.md                     # Skill 定义
```

**用途**：管理和优化 `CLAUDE.md` 文件

### 博客草稿 Skill（3 个文件）

```text
blog-draft/
├── SKILL.md                     # Skill 定义
└── templates/
    ├── draft-template.md        # 博客草稿模板
    └── outline-template.md      # 博客大纲模板
```

**用途**：生成结构统一的博客草稿

**补充**：`README.md` - Skills 总览与使用指南

**安装路径**：`~/.claude/skills/` 或 `.claude/skills/`

---

## 04. Subagents（9 个文件）

带自定义能力的专门化 AI 助手。

| 文件 | 说明 | 工具 | 使用场景 |
|------|------|------|----------|
| `code-reviewer.md` | 代码质量分析 | read, grep, diff, lint_runner | 完整审查 |
| `test-engineer.md` | 测试覆盖分析 | read, write, bash, grep | 测试自动化 |
| `documentation-writer.md` | 文档创建 | read, write, grep | 文档生成 |
| `secure-reviewer.md` | 安全审查（只读） | read, grep | 安全审计 |
| `implementation-agent.md` | 完整实现 | read, write, bash, grep, edit, glob | 功能开发 |
| `debugger.md` | 调试专家 | read, bash, grep | Bug 排查 |
| `data-scientist.md` | 数据分析专家 | read, write, bash | 数据工作流 |
| `clean-code-reviewer.md` | 代码整洁性规范 | read, grep | 代码质量 |
| `README.md` | 文档 | - | 安装与使用指南 |

**安装路径**：`.claude/agents/`

**使用方式**：由主 agent 自动委派

---

## 05. MCP Protocol（5 个文件）

外部工具和 API 集成。

| 文件 | 说明 | 集成对象 | 使用场景 |
|------|------|----------|----------|
| `github-mcp.json` | GitHub 集成 | GitHub API | PR / issue 管理 |
| `database-mcp.json` | 数据库查询 | PostgreSQL / MySQL | 实时数据查询 |
| `filesystem-mcp.json` | 文件操作 | 本地文件系统 | 文件管理 |
| `multi-mcp.json` | 多服务器配置 | GitHub + DB + Slack | 完整集成 |
| `README.md` | 文档 | - | 安装与使用指南 |

**安装路径**：项目级 `.mcp.json` 或用户级 `~/.claude.json`

**使用方式**：例如 `/mcp__github__list_prs`

---

## 06. Hooks（9 个文件）

事件驱动的自动化脚本，会自动执行。

| 文件 | 说明 | 事件 | 使用场景 |
|------|------|------|----------|
| `format-code.sh` | 自动格式化代码 | `PreToolUse:Write` | 代码格式化 |
| `pre-commit.sh` | 提交前运行测试 | `PreToolUse:Bash` | 测试自动化 |
| `security-scan.sh` | 安全扫描 | `PostToolUse:Write` | 安全检查 |
| `log-bash.sh` | 记录 bash 命令 | `PostToolUse:Bash` | 命令日志 |
| `validate-prompt.sh` | 验证提示词 | `PreToolUse` | 输入校验 |
| `notify-team.sh` | 发送通知 | `Notification` | 团队通知 |
| `context-tracker.py` | 跟踪上下文窗口使用量 | `PostToolUse` | 上下文监控 |
| `context-tracker-tiktoken.py` | 基于 token 的上下文跟踪 | `PostToolUse` | 精确 token 统计 |
| `README.md` | 文档 | - | 安装与使用指南 |

**安装路径**：在 `~/.claude/settings.json` 中配置

**使用方式**：在设置中配置后自动执行

**Hook 类型**（4 类，25 个事件）：
- 工具 Hook：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`PermissionRequest`
- 会话 Hook：`SessionStart`、`SessionEnd`、`Stop`、`StopFailure`、`SubagentStart`、`SubagentStop`
- 任务 Hook：`UserPromptSubmit`、`TaskCompleted`、`TaskCreated`、`TeammateIdle`
- 生命周期 Hook：`ConfigChange`、`CwdChanged`、`FileChanged`、`PreCompact`、`PostCompact`、`WorktreeCreate`、`WorktreeRemove`、`Notification`、`InstructionsLoaded`、`Elicitation`、`ElicitationResult`

---

## 07. Plugins（3 个完整插件，40 个文件）

打包好的功能集合。

### PR Review 插件（10 个文件）

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json                  # 插件清单
├── commands/
│   ├── review-pr.md              # 综合审查
│   ├── check-security.md         # 安全检查
│   └── check-tests.md            # 测试覆盖检查
├── agents/
│   ├── security-reviewer.md      # 安全专家
│   ├── test-checker.md           # 测试专家
│   └── performance-analyzer.md   # 性能专家
├── mcp/
│   └── github-config.json           # GitHub 集成
├── hooks/
│   └── pre-review.js                # 审查前校验
└── README.md                     # 插件文档
```

**功能**：安全分析、测试覆盖、性能影响

**命令**：`/review-pr`、`/check-security`、`/check-tests`

**安装**：`/plugin install pr-review`

### DevOps Automation 插件（15 个文件）

```text
devops-automation/
├── .claude-plugin/
│   └── plugin.json                  # 插件清单
├── commands/
│   ├── deploy.md                 # 部署
│   ├── rollback.md               # 回滚
│   ├── status.md                 # 系统状态
│   └── incident.md               # 事件响应
├── agents/
│   ├── deployment-specialist.md  # 部署专家
│   ├── incident-commander.md     # 事件协调
│   └── alert-analyzer.md         # 告警分析
├── mcp/
│   └── kubernetes-config.json       # Kubernetes 集成
├── hooks/
│   ├── pre-deploy.js                # 部署前检查
│   └── post-deploy.js               # 部署后任务
├── scripts/
│   ├── deploy.sh                    # 部署自动化
│   ├── rollback.sh                  # 回滚自动化
│   └── health-check.sh              # 健康检查
└── README.md                     # 插件文档
```

**功能**：Kubernetes 部署、回滚、监控、事件响应

**命令**：`/deploy`、`/rollback`、`/status`、`/incident`

**安装**：`/plugin install devops-automation`

### Documentation 插件（14 个文件）

```text
documentation/
├── .claude-plugin/
│   └── plugin.json                  # 插件清单
├── commands/
│   ├── generate-api-docs.md      # API 文档生成
│   ├── generate-readme.md        # README 创建
│   ├── sync-docs.md              # 文档同步
│   └── validate-docs.md          # 文档校验
├── agents/
│   ├── api-documenter.md         # API 文档专家
│   ├── code-commentator.md       # 代码注释专家
│   └── example-generator.md      # 示例生成器
├── mcp/
│   └── github-docs-config.json      # GitHub 集成
├── templates/
│   ├── api-endpoint.md           # API 端点模板
│   ├── function-docs.md          # 函数文档模板
│   └── adr-template.md           # ADR 模板
└── README.md                     # 插件文档
```

**功能**：API 文档、README 生成、文档同步、文档校验

**命令**：`/generate-api-docs`、`/generate-readme`、`/sync-docs`、`/validate-docs`

**安装**：`/plugin install documentation`

**补充**：`README.md` - 插件总览与使用指南

---

## 08. Checkpoints and Rewind（2 个文件）

保存会话状态，并探索替代方案。

| 文件 | 说明 | 内容 |
|------|------|------|
| `README.md` | 文档 | 完整的 checkpoint 指南 |
| `checkpoint-examples.md` | 真实示例 | 数据库迁移、性能优化、UI 迭代、调试 |

**核心概念**：
- **Checkpoint**：会话状态快照
- **Rewind**：回到之前的 checkpoint
- **Branch Point**：探索多种方案

**使用方式**：

```bash
# 每次用户提示后都会自动创建 checkpoint
# 如需回退，按两次 Esc，或使用：
/rewind
# 然后选择：恢复代码和对话、恢复对话、
# 恢复代码、从这里开始总结，或算了
```

**使用场景**：
- 尝试不同实现方式
- 从错误中恢复
- 安全试验
- 比较不同方案
- A/B 测试

---

## 09. Advanced Features（3 个文件）

复杂工作流下的高级能力。

| 文件 | 说明 | 功能 |
|------|------|------|
| `README.md` | 完整指南 | 全部高级功能说明 |
| `config-examples.json` | 配置示例 | 10+ 个场景化配置 |
| `planning-mode-examples.md` | 规划示例 | REST API、数据库迁移、重构 |

**扩展功能**：
- Scheduled Tasks：使用 `/loop` 和 cron 工具的周期任务
- Chrome Integration：通过无头 Chromium 做浏览器自动化
- Remote Control（扩展版）：连接方式、安全性、对比表
- Keyboard Customization：自定义快捷键、组合键支持、上下文
- Desktop App（扩展版）：连接器、`launch.json`、企业功能

### 已覆盖的高级功能

#### Planning Mode
- 编写详细实现计划
- 时间预估与风险评估
- 系统化拆解任务

#### Extended Thinking
- 面向复杂问题的深度推理
- 架构决策分析
- 权衡取舍评估

#### Background Tasks
- 长时间运行且不阻塞当前会话
- 并行开发工作流
- 任务管理与监控

#### Permission Modes
- **default**：风险操作需要审批
- **acceptEdits**：自动接受文件编辑，其他操作仍需审批
- **plan**：只读分析，不做修改
- **auto**：自动批准安全操作，风险操作仍提示
- **dontAsk**：除危险操作外全部接受
- **bypassPermissions**：全部接受（需要 `--dangerously-skip-permissions`）

#### Headless Mode（`claude -p`）
- CI/CD 集成
- 自动化任务执行
- 批处理

#### Session Management
- 多会话管理
- 会话切换与保存
- 会话持久化

#### 交互功能
- 键盘快捷键
- 命令历史
- Tab 补全
- 多行输入

#### 配置
- 完整设置管理
- 环境相关配置
- 按项目定制

#### Scheduled Tasks
- 使用 `/loop` 创建周期任务
- Cron 工具：`CronCreate`、`CronList`、`CronDelete`
- 自动化的重复工作流

#### Chrome Integration
- 通过无头 Chromium 进行浏览器自动化
- 页面测试与抓取能力
- 页面交互与数据提取

#### Remote Control（扩展版）
- 连接方式与协议
- 安全注意事项与最佳实践
- 远程访问方案对比表

#### Keyboard Customization
- 自定义按键绑定配置
- 支持多键组合快捷键
- 基于上下文的按键激活

#### Desktop App（扩展版）
- 用于 IDE 集成的连接器
- `launch.json` 配置
- 企业功能与部署

---

## 10. CLI Usage（1 个文件）

命令行界面使用方式与参考。

| 文件 | 说明 | 内容 |
|------|------|------|
| `README.md` | CLI 文档 | 参数、选项与使用模式 |

**核心 CLI 功能**：
- `claude` - 启动交互式会话
- `claude -p "prompt"` - 无头/非交互模式
- `claude web` - 打开 Web 会话
- `claude --model` - 选择模型（Sonnet 4.6、Opus 4.6）
- `claude --permission-mode` - 设置权限模式
- `claude --remote` - 通过 WebSocket 启用远程控制

---

## 文档文件（13 个文件）

| 文件 | 位置 | 说明 |
|------|------|------|
| `README.md` | `/` | 主总览 |
| `INDEX.md` | `/` | 本完整索引 |
| `QUICK_REFERENCE.md` | `/` | 速查卡片 |
| `README.md` | `/01-slash-commands/` | Slash Commands 指南 |
| `README.md` | `/02-memory/` | Memory 指南 |
| `README.md` | `/03-skills/` | Skills 指南 |
| `README.md` | `/04-subagents/` | Subagents 指南 |
| `README.md` | `/05-mcp/` | MCP 指南 |
| `README.md` | `/06-hooks/` | Hooks 指南 |
| `README.md` | `/07-plugins/` | Plugins 指南 |
| `README.md` | `/08-checkpoints/` | Checkpoints 指南 |
| `README.md` | `/09-advanced-features/` | Advanced Features 指南 |
| `README.md` | `/10-cli/` | CLI 指南 |

---

## 完整文件树

```text
claude-howto/
├── README.md                                  # 主总览
├── INDEX.md                                   # 本文件
├── QUICK_REFERENCE.md                         # 速查卡片
├── claude_concepts_guide.md                   # 原始指南
│
├── 01-slash-commands/                            # Slash Commands
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
├── 02-memory/                                    # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                    # Skills
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
├── 04-subagents/                                 # Subagents
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
├── 05-mcp/                                       # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                     # Hooks
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
├── 07-plugins/                                   # Plugins
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
├── 08-checkpoints/                               # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                         # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                       # CLI 使用
    └── README.md
```

---

## 按使用场景快速开始

### 代码质量与审查

```bash
# 安装 slash command
cp 01-slash-commands/optimize.md .claude/commands/

# 安装 subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# 安装 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 或直接安装完整插件
/plugin install pr-review
```

### DevOps 与部署

```bash
# 安装插件（包含全部功能）
/plugin install devops-automation
```

### 文档

```bash
# 安装 slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 安装 subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# 安装 skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# 或直接安装完整插件
/plugin install documentation
```

### 团队规范

```bash
# 设置项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 根据团队规范调整内容
```

### 外部集成

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
# 参见 06-hooks/README.md
```

### 安全实验

```bash
# 每次用户提示后都会自动创建 checkpoint
# 回退：按 Esc 两次或使用 /rewind
# 然后选择要从回退菜单中恢复的内容

# 参见 08-checkpoints/README.md 的示例
```

### 高级工作流

```bash
# 配置高级功能
# 参见 09-advanced-features/config-examples.json

# 使用 planning mode
/plan 实现功能 X

# 使用权限模式
claude --permission-mode plan          # 用于代码审查（只读）
claude --permission-mode acceptEdits   # 自动接受编辑
claude --permission-mode auto          # 自动批准安全操作

# 以 headless 模式运行 CI/CD
claude -p "Run tests and report results"

# 运行后台任务
在后台运行测试

# 参见 09-advanced-features/README.md 获取完整指南
```

---

## 功能覆盖矩阵

| 分类 | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Images | 总计 |
|------|----------|--------|-----|-------|---------|-----------|------|--------|------|
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

### 入门（第 1 周）

1. ✅ 阅读 `README.md`
2. ✅ 安装 1 到 2 个 slash command
3. ✅ 创建项目 memory 文件
4. ✅ 试用基础命令

### 中级（第 2-3 周）

1. ✅ 搭建 GitHub MCP
2. ✅ 安装一个 subagent
3. ✅ 尝试委派任务
4. ✅ 安装一个 skill

### 高级（第 4 周及以后）

1. ✅ 安装完整插件
2. ✅ 创建自定义 slash command
3. ✅ 创建自定义 subagent
4. ✅ 创建自定义 skill
5. ✅ 构建自己的插件

### 专家（第 5 周及以后）

1. ✅ 配置 hooks 做自动化
2. ✅ 用 checkpoints 做实验
3. ✅ 配置 planning mode
4. ✅ 充分利用权限模式
5. ✅ 为 CI/CD 配置 headless mode
6. ✅ 熟练掌握会话管理

---

## 按关键词查找

### 性能

- `01-slash-commands/optimize.md` - 性能分析
- `04-subagents/code-reviewer.md` - 性能审查
- `03-skills/code-review/` - 性能指标
- `07-plugins/pr-review/agents/performance-analyzer.md` - 性能专家

### 安全

- `04-subagents/secure-reviewer.md` - 安全审查
- `03-skills/code-review/` - 安全分析
- `07-plugins/pr-review/` - 安全检查

### 测试

- `04-subagents/test-engineer.md` - 测试工程师
- `07-plugins/pr-review/commands/check-tests.md` - 测试覆盖率

### 文档

- `01-slash-commands/generate-api-docs.md` - API 文档命令
- `04-subagents/documentation-writer.md` - 文档编写 agent
- `03-skills/doc-generator/` - 文档生成 skill
- `07-plugins/documentation/` - 完整文档插件

### 部署

- `07-plugins/devops-automation/` - 完整 DevOps 方案

### 自动化

- `06-hooks/` - 事件驱动自动化
- `06-hooks/pre-commit.sh` - 提交前自动化
- `06-hooks/format-code.sh` - 自动格式化
- `09-advanced-features/` - headless 模式用于 CI/CD

### 校验

- `06-hooks/security-scan.sh` - 安全校验
- `06-hooks/validate-prompt.sh` - 提示词校验

### 实验

- `08-checkpoints/` - 使用 rewind 做安全实验
- `08-checkpoints/checkpoint-examples.md` - 真实示例

### 规划

- `09-advanced-features/planning-mode-examples.md` - 规划模式示例
- `09-advanced-features/README.md` - 深度思考

### 配置

- `09-advanced-features/config-examples.json` - 配置示例

---

## 说明

- 所有示例都可直接使用
- 按需修改以适配你的项目
- 示例遵循 Claude Code 最佳实践
- 每个分类都有自己的 README，包含详细说明
- 脚本包含正确的错误处理
- 模板都可自定义

---

## 参与贡献

如果你想增加更多示例，可以按照下面的结构：
1. 创建合适的子目录
2. 包含带使用说明的 README.md
3. 遵循命名规范
4. 充分测试
5. 更新这个索引

---

**最后更新**：2026 年 3 月
**总示例数**：100+ 文件
**分类数**：10 个功能
**Hooks**：8 个自动化脚本
**配置示例**：10+ 个场景
**可直接使用**：所有示例
