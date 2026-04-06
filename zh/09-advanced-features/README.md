<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# 高级功能

这是一份关于 Claude Code 高级能力的完整指南，涵盖 planning mode、extended thinking、auto mode、后台任务、权限模式、打印模式（非交互）、会话管理、交互功能、消息通道（Channels）、语音输入、远程控制、网页会话、桌面应用、任务列表、提示词建议、Git 工作树、沙盒、受管设置和配置。

## 目录

1. [概览](#概览)
2. [规划模式](#规划模式)
3. [扩展思考](#扩展思考)
4. [自动模式](#自动模式)
5. [后台任务](#后台任务)
6. [定时任务](#定时任务)
7. [权限模式](#权限模式)
8. [无头模式](#无头模式)
9. [会话管理](#会话管理)
10. [交互功能](#交互功能)
11. [语音输入](#语音输入)
12. [消息通道（Channels）](#消息通道channels)
13. [Chrome 集成](#chrome-集成)
14. [远程控制](#远程控制)
15. [网页会话](#网页会话)
16. [桌面应用](#桌面应用)
17. [任务列表](#任务列表)
18. [提示词建议](#提示词建议)
19. [Git 工作树（Git Worktrees）](#git-工作树git-worktrees)
20. [沙盒](#沙盒)
21. [企业受管设置](#企业受管设置)
22. [配置与设置](#配置与设置)
23. [最佳实践](#最佳实践)
24. [更多资源](#更多资源)

---

<a id="overview"></a>
## 概览

Claude Code 的高级功能把基础能力扩展到了规划、推理、自动化和控制层面。它们能支持更复杂的开发任务、代码审查、自动化流程以及多会话管理。

**核心高级功能包括：**
- **Planning Mode**：先写详细实现计划，再开始编码
- **Extended Thinking**：对复杂问题进行更深入的推理
- **Auto Mode**：由后台安全分类器在每一步执行前进行审查（Research Preview）
- **Background Tasks**：长时间任务不阻塞对话
- **Permission Modes**：控制 Claude 可以做什么（`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`）
- **Print Mode**：非交互式运行，适合自动化和 CI/CD（`claude -p`）
- **Session Management**：管理多个会话
- **Interactive Features**：快捷键、多行输入、历史记录
- **Voice Dictation**：按住说话，支持 20 种语言的语音识别
- **Channels**：消息通道，允许 MCP server 向运行中的会话推送消息（Research Preview）
- **Remote Control**：从 Claude.ai 或 Claude app 控制本地会话
- **Web Sessions**：在浏览器中运行 Claude Code
- **Desktop App**：支持可视化 diff 审查和多会话的独立应用
- **Task List**：跨 context compaction 持久跟踪任务
- **Prompt Suggestions**：根据上下文智能推荐命令
- **Git 工作树（Git Worktrees）**：隔离的 worktree 分支，适合并行工作
- **Sandboxing**：操作系统级文件系统和网络隔离
- **Managed Settings**：通过 plist、Registry 或受管文件进行企业部署
- **Configuration**：用 JSON 配置文件定制行为

<a id="planning-mode"></a>
## 规划模式

更多规划示例见 [planning-mode-examples.md](planning-mode-examples.md)。

Planning mode 允许 Claude 在真正实现前先梳理复杂任务，生成一份你可以审阅并批准的详细计划。

### 什么是 Planning Mode？

Planning mode 是一个两阶段流程：
1. **规划阶段**：Claude 分析任务并生成详细实现计划
2. **实现阶段**：在你批准后，Claude 执行计划

### 什么时候使用 Planning Mode

✅ 适合：
- 复杂的多文件重构
- 新功能开发
- 架构调整
- 数据库迁移
- 大型 API 重设计

❌ 不建议：
- 简单 bug 修复
- 格式化修改
- 单文件编辑
- 快速查询

### 如何启动 Planning Mode

**Slash command：**
```bash
/plan Implement user authentication system
```

**CLI 参数：**
```bash
claude --permission-mode plan
```

**设为默认：**
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**快捷键：**
- `Shift + Tab` - 切换权限模式（包括 plan）
- `Alt + M` - 切换权限模式（Windows/Linux）

### Planning Mode 的好处

- **结构化实施方式**：把实现步骤拆得更清楚
- **审阅和批准**：先看计划，再执行
- **风险识别**：先发现潜在问题
- **阶段清晰**：有明确的里程碑和阶段划分

### 示例：功能实现

```text
User: /plan Add a real-time notification system

Claude: 我会为实时通知系统制定计划。

## 实现计划

### 阶段 1：基础设施
1. 安装 WebSocket 库（socket.io）
2. 搭建 WebSocket server
3. 配置连接管理

### 阶段 2：后端
4. 创建通知服务
5. 实现通知队列
6. 为通知添加数据库 schema
7. 创建 API 端点

### 阶段 3：前端
8. 搭建 WebSocket client
9. 创建通知 UI 组件
10. 实现通知状态管理
11. 添加通知权限

### 阶段 4：测试与发布
12. 编写单元测试
13. 编写集成测试
14. 更新文档
15. 部署到 staging

预计时间：3-4 小时
需要修改的文件：12 个
需要创建的新文件：8 个

准备继续吗？（yes/no/modify plan）
```

### 计划修改

```text
User: 修改计划 - 先跳过队列，后面再加

Claude: 已更新计划：
[展示删除队列后的计划]

User: 看起来不错，继续

Claude: [按修改后的计划开始实现]
```

### Planning Mode 配置

你可以通过 CLI 参数或 slash command 启用 planning mode：

```bash
# 通过 CLI 启用 plan mode
claude --permission-mode plan

# 或在 REPL 里使用 /plan
/plan Implement user authentication system
```

**规划专用模型别名**：使用 `opusplan`，规划用 Opus，执行用 Sonnet：

```bash
claude --model opusplan "design and implement the new API"
```

**外部编辑计划**：按 `Ctrl+G` 可以把当前计划打开到外部编辑器里进行更详细的修改。

<a id="extended-thinking"></a>
## 扩展思考

Extended thinking 让 Claude 在给出解决方案前，花更多时间进行复杂推理。

### 什么是 Extended Thinking？

这是一个有意识的、分步骤的推理过程，Claude 会：
- 拆解复杂问题
- 比较多种方案
- 评估权衡
- 推导边界情况

### 如何启用

**快捷键：**
- `Option + T`（macOS）/ `Alt + T`（Windows/Linux）- 切换 extended thinking

**自动启用：**
- 对所有模型默认开启（Opus 4.6、Sonnet 4.6、Haiku 4.5）
- Opus 4.6 支持自适应推理，effort 等级为 `low`（○）、`medium`（◐）、`high`（●）、`max`（仅 Opus 4.6）

### 好处

- 更适合复杂问题
- 更容易发现边界条件
- 便于比较多个方案
- 输出通常更稳健

### 示例：架构决策

```text
Context Analysis
Approach 1: Microservices
Approach 2: Monolith
Decision Factors
Recommendation
```

### 配置

```json
{
  "thinking": {
    "enabled": true,
    "effort": "high"
  }
}
```

<a id="auto-mode"></a>
## 自动模式

Auto mode 是一个研究预览功能。它会在每个动作执行前，用后台安全分类器评估风险，帮助你在自动化和安全之间取得平衡。

### 需求

- 支持 auto mode 的 Claude Code 版本
- 合适的权限和配置

### 启用方式

```bash
# 用 CLI 解锁 auto mode
claude --enable-auto-mode

# 然后在 REPL 中用 Shift+Tab 切换到它
```

### 分类器如何工作

在执行工具前，后台分类器会判断这个动作是否安全、是否需要提示、是否应该被阻止。

### 默认阻止的动作

- 明显危险的文件操作
- 高风险 shell 命令
- 可能泄露凭据的操作

### 默认允许的动作

- 只读检查
- 常规分析
- 低风险修改

### 配置 Auto Mode

Auto mode 可以在设置中进一步约束、放宽或与权限模式结合使用。

### 回退行为

如果分类器无法判定，Claude 会回退到更保守的权限处理方式。

### 预置一份类似 Auto-Mode 的保守权限基线

```bash
# 先预览将要添加的权限（不会写入）

# 应用保守基线

# 只有在需要时再逐步增加能力
```

<a id="background-tasks"></a>
## 后台任务

后台任务允许 Claude 在不阻塞对话的情况下运行长时间操作。

### 什么是后台任务？

后台任务适合长时间运行的工作，例如构建、测试、下载、扫描或并行分析。你可以把它们交给 Claude，让对话继续保持响应。

### 启动后台任务

你可以从命令、计划或工具链中启动后台任务，让 Claude 在后台继续工作。

### 管理后台任务

- 查看任务状态
- 中止任务
- 等待任务完成
- 从结果中恢复上下文

### 示例：并行开发

```text
任务 A：运行测试
任务 B：生成文档
任务 C：执行安全扫描
```

### 配置

后台任务的超时、并发和通知行为都可以在设置中调整。

<a id="scheduled-tasks"></a>
## 定时任务

Scheduled tasks 让 Claude 按计划重复执行某些提示词或任务。

### `/loop` 命令

```bash
# 显式间隔
/loop 10m Run tests and report failures

# 自然语言
/loop every day at 9am check release notes
```

### 一次性提醒

```bash
/schedule "remind me to review the PR in 30 minutes"
```

### 管理定时任务

- 查看任务列表
- 修改执行频率
- 暂停或取消任务

### 行为细节

定时任务会遵循当前会话与权限配置，并按计划触发执行。

### 云端定时任务

部分场景可以在云端环境中运行调度任务。

### 禁用定时任务

如果你不希望自动触发，关闭相关设置即可。

### 示例：监控部署

```text
每 5 分钟检查一次部署状态，直到 health check 通过。
```

<a id="permission-modes"></a>
## 权限模式

Permission modes 决定 Claude 可以直接执行哪些操作。

### 可用模式

- `default`
- `acceptEdits`
- `plan`
- `auto`
- `dontAsk`
- `bypassPermissions`

### 启用方式

可以通过命令行、设置或会话中的快捷操作切换权限模式。

### 示例

#### Default Mode

默认的平衡模式，必要时会询问权限。

#### Plan Mode

只做规划，不直接执行高风险改动。

#### Accept Edits Mode

更偏向自动接受编辑，适合受控环境。

### 使用场景

- 代码审查
- 自动化重构
- CI/CD
- 高风险操作前的审批流程

<a id="headless-mode"></a>
## 无头模式

Headless mode 指非交互式运行 Claude Code，常用于自动化和 CI/CD。

### 什么是 Print Mode？

Print mode 就是 `claude -p`：给一个任务，输出结果，然后退出。

### 在 Print Mode 中运行

```bash
# 运行指定任务
claude -p "run tests and summarize failures"

# 处理管道内容
cat logs.txt | claude -p "find the root cause"

# CI/CD 集成
claude -p "review this diff and return JSON"
```

### 其他示例

```bash
# 捕获输出
claude -p "analyze this code" > report.txt

# 结构化输出
claude -p --output-format json "list files"

# 标准输入
echo "hello" | claude -p "translate to Chinese"
```

### CI/CD 示例

```yaml
# .github/workflows/code-review.yml
```

### Print Mode 配置

- 限制自主回合数
- 使用结构化 JSON 输出
- 启用 schema 验证
- 禁用会话持久化

<a id="session-management"></a>
## 会话管理

会话管理用于在多个会话之间恢复、重命名、分叉和持续工作。

### 常用命令

- `/resume`
- `/rename`
- `/fork`
- `claude -c`
- `claude -r`

### 恢复会话

```bash
# 继续最后一次对话
claude -c

# 恢复指定名称或 ID 的会话
claude -r "feature-auth"
```

### 分叉会话

```bash
# 恢复并分叉，适合实验
claude -r "feature-auth" --fork
```

### 会话持久化

你可以选择保留、继续或重建会话上下文。

<a id="interactive-features"></a>
## 交互功能

交互功能包括快捷键、多行输入、历史记录、Vim 模式和 Bash 模式等。

### 快捷键

常用快捷键用于切换模式、编辑输入、查看历史和控制输出。

### 自定义快捷键

你可以在设置中绑定自己的按键组合。

### 可用上下文

不同上下文会影响快捷键的可用性和行为。

### Chord 支持

支持组合按键触发复杂操作。

### 保留键与冲突键

某些按键会被系统或终端占用，需要避免冲突。

### Tab 补全

输入命令、参数或路径时会提供补全建议。

### 命令历史

Claude 会保留历史记录，方便你快速重用之前的输入。

### 多行输入

```text
第一行
第二行
第三行
```

### 行内编辑

支持在输入过程中编辑中间内容。

### Vim 模式

如果你熟悉 Vim，可以启用类似的编辑体验。

### Bash 模式

可在会话中直接进入更偏 shell 风格的操作方式。

<a id="voice-dictation"></a>
## 语音输入

语音输入支持按住说话和多语言识别，适合快速记录想法或在不方便键盘输入时使用。

### 如何启用

在设置中打开语音输入即可。

### 特性

- 支持按住说话
- 支持 20 种语言的语音识别
- 适合快速口述任务

### 配置

可在 settings 中控制灵敏度、语言和输入行为。

<a id="channels"></a>
## 消息通道（Channels）

消息通道允许 MCP servers 向正在运行的会话推送消息。

### 订阅 channels

```bash
# 启动时订阅 channel 插件
```

### 支持的集成

- Discord
- Telegram
- 其他 channel 型集成

### 配置

通过 MCP 配置或 settings 订阅相应 channel。

### 工作方式

外部系统可以把消息推送进 Claude 的当前会话里，让你在一个会话中接收通知或事件。

<a id="chrome-integration"></a>
## Chrome 集成

Chrome 集成让 Claude 可以协助浏览器自动化和站点级操作。

### 启用 Chrome 集成

开启相关开关后，Claude 就可以与浏览器协作。

### 能力

- 浏览器自动化
- 页面操作
- 网站级交互

### 站点级权限

你可以对站点设置更细粒度的访问权限。

### 工作方式

Claude 通过浏览器连接与页面交互。

### 已知限制

- 某些站点会限制自动化
- 复杂页面可能需要更多权限

<a id="remote-control"></a>
## 远程控制

Remote Control 可以让你从 Claude.ai 或 Claude app 远程控制本地 Claude Code 会话。

### 启动 Remote Control

```bash
# 使用默认会话名启动
claude --remote-control

# 使用自定义名称
claude --remote-control --name my-session
```

### 连接到会话

你可以在远程端连接到已经启动的本地会话，继续同一个上下文。

### 安全性

远程控制会牵涉到会话和权限，因此建议只在可信环境中使用。

### Remote Control vs Claude Code on the web

Remote Control 是控制本地会话；web 版则是在浏览器中直接运行。

### 局限

- 网络可用性依赖更高
- 某些本地资源可能不可远程访问

### 使用场景

- 在手机上查看并接管会话
- 远程继续长期任务

<a id="web-sessions"></a>
## 网页会话

Web Sessions 允许你直接在浏览器里创建和恢复 Claude Code 会话。

### 创建 Web Session

```bash
# 从 CLI 创建新的 web session
claude --remote "implement API"
```

### 在本地恢复 Web Session

```bash
# 在本地终端恢复 web session
claude --teleport
```

### 使用场景

- 浏览器里快速开始任务
- 在本地和网页之间切换
- 远程继续工作

<a id="desktop-app"></a>
## 桌面应用

桌面应用提供独立界面，适合视觉化 diff 审查和多会话管理。

### 安装

按照桌面应用的安装说明安装即可。

### 从 CLI 接力

你可以把 CLI 会话交给桌面应用继续处理。

### 核心功能

- 可视化 diff
- 多会话
- 更直观的审查体验

### App 预览配置

可以调整预览、布局和视觉呈现方式。

### Connectors

桌面应用可以连接到不同的工作环境。

### 远程和 SSH 会话

桌面应用也支持远程或 SSH 场景下的接力。

### Desktop 中的权限模式

Desktop 里同样可以使用不同的权限模式。

### 企业功能

企业部署下可使用更多受管和合规相关能力。

<a id="task-list"></a>
## 任务列表

Task List 用于跨 context compaction 持久保存任务进度。

### 切换任务列表

在设置里打开或关闭任务列表显示。

### 持久任务

任务会保留，即使上下文被压缩，也能继续跟踪。

### 命名任务目录

你可以给任务分组或目录命名，方便管理。

<a id="prompt-suggestions"></a>
## 提示词建议

Prompt suggestions 会根据当前上下文智能推荐下一步命令或提示词。

### 工作方式

系统会结合你的历史、当前任务和上下文给出建议。

### 禁用建议

如果你不想看到建议，可以在设置里关闭。

<a id="git-worktrees"></a>
## Git 工作树（Git Worktrees）

Git worktrees 让你在隔离的目录里并行工作，非常适合实验和分支开发。

### 从 worktree 启动

```bash
# 在隔离 worktree 中启动 Claude Code
claude -w
```

### Worktree 位置

你可以控制 worktree 的放置位置，保持主工作区整洁。

### Monorepo 的 sparse checkout

在大型 monorepo 中，可配合 sparse checkout 只加载需要的部分。

### Worktree 工具和 Hooks

worktree 场景下依然可以配合工具和 hooks 自动化流程。

### 自动清理

不需要的 worktree 可以自动清理。

### 使用场景

- 并行尝试多个方案
- 隔离高风险重构
- 保持主分支整洁

<a id="sandboxing"></a>
## 沙盒

沙盒提供文件系统和网络层面的隔离，能显著降低自动化操作的风险。

### 启用沙盒

开启后，Claude 的很多操作都会在受控环境里执行。

### 配置项

你可以配置允许访问的目录、网络行为和例外列表。

### 示例配置

```json
{
  "sandbox": {
    "enabled": true
  }
}
```

### 工作方式

沙盒会限制 Claude 可触达的文件和网络边界。

### 使用场景

- 低风险自动化
- 在不完全信任的输入上执行任务
- 受控环境中的批处理

<a id="managed-settings-enterprise"></a>
## 企业受管设置

企业可以通过受管设置统一分发 Claude Code 配置。

### 部署方式

- plist
- Registry
- 受管文件

### 受管配置片段

通过受管配置片段，可以给团队统一推送策略。

### 可用的受管设置

- 权限模式
- 功能开关
- MCP / hooks / 插件约束

### macOS plist 示例

```xml
<!-- 示例略 -->
```

<a id="configuration-and-settings"></a>
## 配置与设置

### 配置文件位置

- `~/.claude/settings.json`
- `.claude/settings.json`
- `.claude/settings.local.json`

### 完整配置示例

```json
{
  "permissions": {
    "defaultMode": "plan"
  },
  "thinking": {
    "enabled": true,
    "effort": "high"
  },
  "autoCheckpoint": true
}
```

### 环境变量

#### 模型选择

- `ANTHROPIC_API_KEY`
- `CLAUDE_MODEL`

#### API 配置

- `ANTHROPIC_API_KEY`

#### Thinking 配置

- `CLAUDE_EFFORT`

#### 功能开关

- `CLAUDE_ENABLE_AUTO_MODE`

#### MCP 配置

- `CLAUDE_MCP_CONFIG`

#### 任务管理

- `CLAUDE_TASK_LIST`

#### Agent team（实验性）

- `CLAUDE_TEAM_MODE`

#### Subagent 和 plugin 配置

- `CLAUDE_PLUGIN_DATA`

#### 子进程和流式处理

- `CLAUDE_OUTPUT_FORMAT`

### 配置管理命令

你可以用命令查看或更新当前配置，并把它们落到 settings 中。

### 每个项目的配置

推荐把项目专用设置放进项目内的 `.claude/settings.json`，这样能跟代码一起版本化。

<a id="best-practices"></a>
## 最佳实践

### Planning Mode

- 复杂任务先规划，再实现
- 计划要可审阅

### Extended Thinking

- 留给复杂问题
- 不要在简单任务上过度使用

### Background Tasks

- 用于长时间、可并行的任务
- 记得设置超时和可见性

### Permissions

- 默认最小权限
- 只在必要时放宽

### Sessions

- 为重要会话命名
- 必要时分叉，而不是硬改

<a id="additional-resources"></a>
## 更多资源

- [根目录中文指南](../README.md)
- [Slash Commands 中文参考](../01-slash-commands/README.md)
- [Checkpoints 中文指南](../08-checkpoints/README.md)
- [Plugins 中文指南](../07-plugins/README.md)
- [CLI 中文参考](../10-cli/README.md)
