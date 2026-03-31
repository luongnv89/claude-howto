<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例 - 完整索引

本文档提供了按功能类型整理的所有示例文件的完整索引。

## 统计摘要

- **文件总数**：100+ 个文件
- **分类数量**：10 个功能类别
- **插件数量**：3 个完整插件
- **技能数量**：6 个完整技能
- **Hook 数量**：8 个示例 Hook
- **可直接使用**：所有示例

---

## 01. Slash Commands（10 个文件）

用户主动调用的常见工作流快捷方式。

| 文件 | 描述 | 使用场景 |
|------|-------------|----------|
| `optimize.md` | 代码优化分析器 | 发现性能问题 |
| `pr.md` | Pull Request 准备 | PR 工作流自动化 |
| `generate-api-docs.md` | API 文档生成器 | 生成 API 文档 |
| `commit.md` | 提交信息助手 | 规范化提交 |
| `setup-ci-cd.md` | CI/CD 流水线配置 | DevOps 自动化 |
| `push-all.md` | 推送所有更改 | 快速推送工作流 |
| `unit-test-expand.md` | 扩展单元测试覆盖率 | 测试自动化 |
| `doc-refactor.md` | 文档重构 | 文档改进 |
| `pr-slash-command.png` | 截图示例 | 视觉参考 |
| `README.md` | 文档说明 | 配置与使用指南 |

**安装路径**：`.claude/commands/`

**使用方式**：`/optimize`、`/pr`、`/generate-api-docs`、`/commit`、`/setup-ci-cd`、`/push-all`、`/unit-test-expand`、`/doc-refactor`

---

## 02. Memory（6 个文件）

持久化上下文与项目规范。

| 文件 | 描述 | 作用范围 | 位置 |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | 团队项目规范 | 项目级 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 专属规则 | 目录级 | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 个人偏好设置 | 用户级 | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 截图：记忆已保存 | - | 视觉参考 |
| `memory-ask-claude.png` | 截图：询问 Claude | - | 视觉参考 |
| `README.md` | 文档说明 | - | 参考资料 |

**安装方式**：复制到对应位置

**使用方式**：由 Claude 自动加载

---

## 03. Skills（28 个文件）

自动调用的能力，包含脚本和模板。

### 代码审查技能（5 个文件）
```
code-review/
├── SKILL.md                          # 技能定义
├── scripts/
│   ├── analyze-metrics.py            # 代码指标分析器
│   └── compare-complexity.py         # 复杂度比较工具
└── templates/
    ├── review-checklist.md           # 审查清单
    └── finding-template.md           # 问题记录模板
```

**用途**：包含安全、性能和质量分析的全面代码审查

**自动触发**：审查代码时

---

### 品牌声音技能（4 个文件）
```
brand-voice/
├── SKILL.md                          # 技能定义
├── templates/
│   ├── email-template.txt            # 邮件格式模板
│   └── social-post-template.txt      # 社交媒体格式模板
└── tone-examples.md                  # 示例消息
```

**用途**：确保沟通中品牌声音的一致性

**自动触发**：创建营销文案时

---

### 文档生成器技能（2 个文件）
```
doc-generator/
├── SKILL.md                          # 技能定义
└── generate-docs.py                  # Python 文档提取器
```

**用途**：从源代码生成完整的 API 文档

**自动触发**：创建/更新 API 文档时

---

### 重构技能（5 个文件）
```
refactor/
├── SKILL.md                          # 技能定义
├── scripts/
│   ├── analyze-complexity.py         # 复杂度分析器
│   └── detect-smells.py              # 代码坏味道检测器
├── references/
│   ├── code-smells.md                # 代码坏味道目录
│   └── refactoring-catalog.md        # 重构模式目录
└── templates/
    └── refactoring-plan.md           # 重构计划模板
```

**用途**：包含复杂度分析的系统化代码重构

**自动触发**：重构代码时

---

### CLAUDE.md 技能（1 个文件）
```
claude-md/
└── SKILL.md                          # 技能定义
```

**用途**：管理和优化 CLAUDE.md 文件

---

### 博客草稿技能（3 个文件）
```
blog-draft/
├── SKILL.md                          # 技能定义
└── templates/
    ├── draft-template.md             # 博客草稿模板
    └── outline-template.md           # 博客大纲模板
```

**用途**：以一致的结构起草博客文章

**附加说明**：`README.md` - Skills 概述与使用指南

**安装路径**：`~/.claude/skills/` 或 `.claude/skills/`

---

## 04. Subagents（9 个文件）

具备自定义能力的专用 AI 助手。

| 文件 | 描述 | 工具 | 使用场景 |
|------|-------------|-------|----------|
| `code-reviewer.md` | 代码质量分析 | read, grep, diff, lint_runner | 全面代码审查 |
| `test-engineer.md` | 测试覆盖率分析 | read, write, bash, grep | 测试自动化 |
| `documentation-writer.md` | 文档创建 | read, write, grep | 文档生成 |
| `secure-reviewer.md` | 安全审查（只读） | read, grep | 安全审计 |
| `implementation-agent.md` | 完整功能实现 | read, write, bash, grep, edit, glob | 功能开发 |
| `debugger.md` | 调试专家 | read, bash, grep | 问题排查 |
| `data-scientist.md` | 数据分析专家 | read, write, bash | 数据工作流 |
| `clean-code-reviewer.md` | 整洁代码规范 | read, grep | 代码质量 |
| `README.md` | 文档说明 | - | 配置与使用指南 |

**安装路径**：`.claude/agents/`

**使用方式**：由主代理自动委派

---

## 05. MCP 协议（5 个文件）

外部工具与 API 集成。

| 文件 | 描述 | 集成对象 | 使用场景 |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub 集成 | GitHub API | PR/Issue 管理 |
| `database-mcp.json` | 数据库查询 | PostgreSQL/MySQL | 实时数据查询 |
| `filesystem-mcp.json` | 文件操作 | 本地文件系统 | 文件管理 |
| `multi-mcp.json` | 多服务器配置 | GitHub + DB + Slack | 完整集成方案 |
| `README.md` | 文档说明 | - | 配置与使用指南 |

**安装路径**：`.mcp.json`（项目范围）或 `~/.claude.json`（用户范围）

**使用方式**：`/mcp__github__list_prs` 等

---

## 06. Hooks（9 个文件）

自动执行的事件驱动自动化脚本。

| 文件 | 描述 | 事件 | 使用场景 |
|------|-------------|-------|----------|
| `format-code.sh` | 自动格式化代码 | PreToolUse:Write | 代码格式化 |
| `pre-commit.sh` | 提交前运行测试 | PreToolUse:Bash | 测试自动化 |
| `security-scan.sh` | 安全扫描 | PostToolUse:Write | 安全检查 |
| `log-bash.sh` | 记录 Bash 命令日志 | PostToolUse:Bash | 命令日志记录 |
| `validate-prompt.sh` | 验证提示词 | PreToolUse | 输入验证 |
| `notify-team.sh` | 发送通知 | Notification | 团队通知 |
| `context-tracker.py` | 跟踪上下文窗口使用情况 | PostToolUse | 上下文监控 |
| `context-tracker-tiktoken.py` | 基于 Token 的上下文跟踪 | PostToolUse | 精确 Token 计数 |
| `README.md` | 文档说明 | - | 配置与使用指南 |

**安装路径**：在 `~/.claude/settings.json` 中配置

**使用方式**：在设置中配置，自动执行

**Hook 类型**（4 种类型，25 个事件）：
- 工具 Hooks：PreToolUse、PostToolUse、PostToolUseFailure、PermissionRequest
- 会话 Hooks：SessionStart、SessionEnd、Stop、StopFailure、SubagentStart、SubagentStop
- 任务 Hooks：UserPromptSubmit、TaskCompleted、TaskCreated、TeammateIdle
- 生命周期 Hooks：ConfigChange、CwdChanged、FileChanged、PreCompact、PostCompact、WorktreeCreate、WorktreeRemove、Notification、InstructionsLoaded、Elicitation、ElicitationResult

---

## 07. Plugins（3 个完整插件，40 个文件）

功能集合打包。

### PR Review 插件（10 个文件）
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # 插件清单
├── commands/
│   ├── review-pr.md                  # 全面审查
│   ├── check-security.md             # 安全检查
│   └── check-tests.md                # 测试覆盖率检查
├── agents/
│   ├── security-reviewer.md          # 安全专家
│   ├── test-checker.md               # 测试专家
│   └── performance-analyzer.md       # 性能专家
├── mcp/
│   └── github-config.json            # GitHub 集成配置
├── hooks/
│   └── pre-review.js                 # 审查前验证
└── README.md                         # 插件文档
```

**功能**：安全分析、测试覆盖率、性能影响

**命令**：`/review-pr`、`/check-security`、`/check-tests`

**安装方式**：`/plugin install pr-review`

---

### DevOps 自动化插件（15 个文件）
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # 插件清单
├── commands/
│   ├── deploy.md                     # 部署
│   ├── rollback.md                   # 回滚
│   ├── status.md                     # 系统状态
│   └── incident.md                   # 故障响应
├── agents/
│   ├── deployment-specialist.md      # 部署专家
│   ├── incident-commander.md         # 故障指挥官
│   └── alert-analyzer.md             # 告警分析器
├── mcp/
│   └── kubernetes-config.json        # Kubernetes 集成配置
├── hooks/
│   ├── pre-deploy.js                 # 部署前检查
│   └── post-deploy.js                # 部署后任务
├── scripts/
│   ├── deploy.sh                     # 部署自动化脚本
│   ├── rollback.sh                   # 回滚自动化脚本
│   └── health-check.sh               # 健康检查脚本
└── README.md                         # 插件文档
```

**功能**：Kubernetes 部署、回滚、监控、故障响应

**命令**：`/deploy`、`/rollback`、`/status`、`/incident`

**安装方式**：`/plugin install devops-automation`

---

### 文档插件（14 个文件）
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # 插件清单
├── commands/
│   ├── generate-api-docs.md          # API 文档生成
│   ├── generate-readme.md            # README 创建
│   ├── sync-docs.md                  # 文档同步
│   └── validate-docs.md              # 文档验证
├── agents/
│   ├── api-documenter.md             # API 文档专家
│   ├── code-commentator.md           # 代码注释专家
│   └── example-generator.md          # 示例创建专家
├── mcp/
│   └── github-docs-config.json       # GitHub 集成配置
├── templates/
│   ├── api-endpoint.md               # API 端点模板
│   ├── function-docs.md              # 函数文档模板
│   └── adr-template.md               # ADR 模板
└── README.md                         # 插件文档
```

**功能**：API 文档、README 生成、文档同步、文档验证

**命令**：`/generate-api-docs`、`/generate-readme`、`/sync-docs`、`/validate-docs`

**安装方式**：`/plugin install documentation`

**附加说明**：`README.md` - Plugins 概述与使用指南

---

## 08. 检查点与回退（2 个文件）

保存对话状态并探索不同实现方案。

| 文件 | 描述 | 内容 |
|------|-------------|---------|
| `README.md` | 文档说明 | 全面的检查点使用指南 |
| `checkpoint-examples.md` | 真实案例 | 数据库迁移、性能优化、UI 迭代、调试排错 |
| | | |

**核心概念**：
- **Checkpoint（检查点）**：对话状态快照
- **Rewind（回退）**：返回到之前的检查点
- **Branch Point（分支点）**：探索多种实现方案

**使用方式**：
```
# 每次用户发送提示时自动创建检查点
# 回退方式：连按两次 Esc 或使用：
/rewind
# 然后选择：恢复代码和对话、恢复对话、
# 恢复代码、从此处生成摘要，或取消
```

**适用场景**：
- 尝试不同实现方案
- 从错误中恢复
- 安全地进行实验
- 比较不同解决方案
- A/B 测试

---

## 09. 高级功能（3 个文件）

复杂工作流所需的高级能力。

| 文件 | 描述 | 功能 |
|------|-------------|----------|
| `README.md` | 完整指南 | 所有高级功能文档 |
| `config-examples.json` | 配置示例 | 10+ 个特定场景配置 |
| `planning-mode-examples.md` | 规划示例 | REST API、数据库迁移、代码重构 |
| 定时任务 | 使用 `/loop` 和 cron 工具执行周期性任务 | 自动化周期性工作流 |
| Chrome 集成 | 通过无头 Chromium 实现浏览器自动化 | Web 测试与数据抓取 |
| 远程控制（扩展） | 连接方式、安全性、对比表格 | 远程会话管理 |
| 键盘自定义 | 自定义快捷键、和弦键支持、上下文感知 | 个性化快捷键 |
| 桌面应用（扩展） | 连接器、launch.json、企业功能 | 桌面集成 |
| | | |

**涵盖的高级功能**：

### 规划模式
- 创建详细的实现计划
- 时间估算与风险评估
- 系统化任务分解

### 扩展思考
- 对复杂问题进行深度推理
- 架构决策分析
- 权衡取舍评估

### 后台任务
- 长时间运行的操作不阻塞前台
- 并行开发工作流
- 任务管理与监控

### 权限模式
- **default**：对风险操作请求批准
- **acceptEdits**：自动接受文件编辑，其他操作需询问
- **plan**：只读分析，不做任何修改
- **auto**：自动批准安全操作，风险操作需提示
- **dontAsk**：接受所有操作（风险操作除外）
- **bypassPermissions**：接受所有操作（需要 `--dangerously-skip-permissions`）

### 无头模式（`claude -p`）
- CI/CD 集成
- 自动化任务执行
- 批量处理

### 会话管理
- 多工作会话
- 会话切换与保存
- 会话持久化

### 交互功能
- 键盘快捷键
- 命令历史记录
- Tab 补全
- 多行输入

### 配置管理
- 全面的设置管理
- 特定环境配置
- 按项目自定义

### 定时任务
- 使用 `/loop` 命令执行周期性任务
- Cron 工具：CronCreate、CronList、CronDelete
- 自动化周期性工作流

### Chrome 集成
- 通过无头 Chromium 实现浏览器自动化
- Web 测试与数据抓取能力
- 页面交互与数据提取

### 远程控制（扩展）
- 连接方式与协议
- 安全注意事项与最佳实践
- 远程访问方式对比表格

### 键盘自定义
- 自定义快捷键配置
- 多键组合的和弦键支持
- 上下文感知的快捷键激活

### 桌面应用（扩展）
- IDE 集成连接器
- launch.json 配置
- 企业功能与部署

---

## 10. CLI 使用（1 个文件）

命令行界面使用模式与参考文档。

| 文件 | 描述 | 内容 |
|------|-------------|---------|
| `README.md` | CLI 文档 | 标志、选项与使用模式 |

**核心 CLI 功能**：
- `claude` - 启动交互式会话
- `claude -p "prompt"` - 无头/非交互模式
- `claude web` - 启动 Web 会话
- `claude --model` - 选择模型（Sonnet 4.6、Opus 4.6）
- `claude --permission-mode` - 设置权限模式
- `claude --remote` - 通过 WebSocket 启用远程控制

---

## 文档文件（13 个文件）

| 文件 | 位置 | 描述 |
|------|----------|-------------|
| `README.md` | `/` | 示例主概述 |
| `INDEX.md` | `/` | 完整索引（本文件） |
| `QUICK_REFERENCE.md` | `/` | 快速参考卡片 |
| `README.md` | `/01-slash-commands/` | Slash Commands 指南 |
| `README.md` | `/02-memory/` | Memory 指南 |
| `README.md` | `/03-skills/` | Skills 指南 |
| `README.md` | `/04-subagents/` | Subagents 指南 |
| `README.md` | `/05-mcp/` | MCP 指南 |
| `README.md` | `/06-hooks/` | Hooks 指南 |
| `README.md` | `/07-plugins/` | Plugins 指南 |
| `README.md` | `/08-checkpoints/` | 检查点指南 |
| `README.md` | `/09-advanced-features/` | 高级功能指南 |
| `README.md` | `/10-cli/` | CLI 指南 |

---

## 完整文件目录

```
claude-howto/
├── README.md                                    # 主概述
├── INDEX.md                                     # 本文件
├── QUICK_REFERENCE.md                           # 快速参考卡片
├── claude_concepts_guide.md                     # 原始指南
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
├── 05-mcp/                                      # MCP 协议
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
├── 08-checkpoints/                              # 检查点
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # 高级功能
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI 使用
    └── README.md
```

---

## 按使用场景快速开始

### 代码质量与审查
```bash
# 安装 Slash Command
cp 01-slash-commands/optimize.md .claude/commands/

# 安装 Subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# 安装 Skill
cp -r 03-skills/code-review ~/.claude/skills/

# 或安装完整插件
/plugin install pr-review
```

### DevOps 与部署
```bash
# 安装插件（包含所有功能）
/plugin install devops-automation
```

### 文档
```bash
# 安装 Slash Command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 安装 Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# 安装 Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# 或安装完整插件
/plugin install documentation
```

### 团队规范
```bash
# 配置项目记忆
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 编辑以匹配团队规范
```

### 外部集成
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装 MCP 配置（项目范围）
cp 05-mcp/multi-mcp.json .mcp.json
```

### 自动化与验证
```bash
# 安装 Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在设置中配置 Hooks（~/.claude/settings.json）
# 参见 06-hooks/README.md
```

### 安全实验
```bash
# 每次用户发送提示时自动创建检查点
# 回退方式：按 Esc+Esc 或使用 /rewind
# 然后从回退菜单中选择要恢复的内容

# 参见 08-checkpoints/README.md 查看示例
```

### 高级工作流
```bash
# 配置高级功能
# 参见 09-advanced-features/config-examples.json

# 使用规划模式
/plan Implement feature X

# 使用权限模式
claude --permission-mode plan          # 用于代码审查（只读）
claude --permission-mode acceptEdits   # 自动接受编辑
claude --permission-mode auto          # 自动批准安全操作

# 以无头模式运行用于 CI/CD
claude -p "Run tests and report results"

# 运行后台任务
Run tests in background

# 参见 09-advanced-features/README.md 查看完整指南
```

---

## 功能覆盖矩阵

| 分类 | 命令 | 代理 | MCP | Hooks | 脚本 | 模板 | 文档 | 图片 | 合计 |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagents** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 检查点** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 高级功能** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## 学习路径

### 初级（第 1 周）
1. ✅ 阅读 `README.md`
2. ✅ 安装 1-2 个 Slash Commands
3. ✅ 创建项目记忆文件
4. ✅ 尝试基本命令

### 中级（第 2-3 周）
1. ✅ 配置 GitHub MCP
2. ✅ 安装一个 Subagent
3. ✅ 尝试委派任务
4. ✅ 安装一个 Skill

### 高级（第 4 周及以后）
1. ✅ 安装完整插件
2. ✅ 创建自定义 Slash Commands
3. ✅ 创建自定义 Subagent
4. ✅ 创建自定义 Skill
5. ✅ 构建自己的插件

### 专家（第 5 周及以后）
1. ✅ 配置 Hooks 实现自动化
2. ✅ 使用检查点进行实验
3. ✅ 配置规划模式
4. ✅ 有效使用权限模式
5. ✅ 配置无头模式用于 CI/CD
6. ✅ 掌握会话管理

---

## 按关键词搜索

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
- `04-subagents/documentation-writer.md` - 文档写作代理
- `03-skills/doc-generator/` - 文档生成技能
- `07-plugins/documentation/` - 完整文档插件

### 部署
- `07-plugins/devops-automation/` - 完整 DevOps 解决方案

### 自动化
- `06-hooks/` - 事件驱动自动化
- `06-hooks/pre-commit.sh` - 提交前自动化
- `06-hooks/format-code.sh` - 自动格式化
- `09-advanced-features/` - 用于 CI/CD 的无头模式

### 验证
- `06-hooks/security-scan.sh` - 安全验证
- `06-hooks/validate-prompt.sh` - 提示词验证

### 实验
- `08-checkpoints/` - 使用回退功能进行安全实验
- `08-checkpoints/checkpoint-examples.md` - 真实案例

### 规划
- `09-advanced-features/planning-mode-examples.md` - 规划模式示例
- `09-advanced-features/README.md` - 扩展思考

### 配置
- `09-advanced-features/config-examples.json` - 配置示例

---

## 注意事项

- 所有示例均可直接使用
- 请根据实际需求进行修改
- 示例遵循 Claude Code 最佳实践
- 每个类别都有专属 README 提供详细说明
- 脚本包含适当的错误处理
- 模板支持自定义

---

## 贡献指南

想要添加更多示例？请遵循以下结构：
1. 创建合适的子目录
2. 包含说明用法的 README.md
3. 遵循命名规范
4. 充分测试
5. 更新本索引

---

**最后更新**：2026 年 3 月
**示例总数**：100+ 个文件
**分类数量**：10 个功能
**Hooks 数量**：8 个自动化脚本
**配置示例**：10+ 个场景
**可直接使用**：所有示例
