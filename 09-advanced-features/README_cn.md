<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# 高级功能

Claude Code 高级功能综合指南，包括规划模式、扩展思考、自动模式、后台任务、权限模式、打印模式（非交互式）、会话管理、交互功能、频道、语音听写、远程控制、Web 会话、桌面应用、任务列表、提示建议、git worktree、沙箱、托管设置和配置。

## 目录

1. [概述](#概述)
2. [规划模式](#规划模式)
3. [扩展思考](#扩展思考)
4. [自动模式](#自动模式)
5. [后台任务](#后台任务)
6. [计划任务](#计划任务)
7. [权限模式](#权限模式)
8. [无头模式](#无头模式)
9. [会话管理](#会话管理)
10. [交互功能](#交互功能)
11. [语音听写](#语音听写)
12. [频道](#频道)
13. [Chrome 集成](#chrome-集成)
14. [远程控制](#远程控制)
15. [Web 会话](#web-会话)
16. [桌面应用](#桌面应用)
17. [任务列表](#任务列表)
18. [提示建议](#提示建议)
19. [Git Worktree](#git-worktree)
20. [沙箱](#沙箱)
21. [托管设置（企业版）](#托管设置企业版)
22. [配置和设置](#配置和设置)
23. [最佳实践](#最佳实践)
24. [相关概念](#相关概念)

---

## 概述

Claude Code 的高级功能通过规划、推理、自动化和控制机制扩展了核心功能。这些功能为复杂开发任务、代码审查、自动化和多会话管理提供了复杂的工作流。

**主要高级功能包括：**
- **规划模式**：在编码前创建详细的实现计划
- **扩展思考**：对复杂问题进行深度推理
- **自动模式**：后台安全分类器在执行前审查每个动作（研究预览版）
- **后台任务**：运行长时间操作而不阻塞对话
- **权限模式**：控制 Claude 可以做什么（`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`）
- **打印模式**：以非交互方式运行 Claude Code，用于自动化和 CI/CD（`claude -p`）
- **会话管理**：管理多个工作会话
- **交互功能**：键盘快捷键、多行输入和命令历史
- **语音听写**：支持 20 种语言 STT 的按键通话语音输入
- **频道**：MCP 服务器将消息推送到运行中的会话（研究预览版）
- **远程控制**：从 Claude.ai 或 Claude 应用控制 Claude Code
- **Web 会话**：在 claude.ai/code 浏览器中运行 Claude Code
- **桌面应用**：用于视觉 diff 审查和多个会话的独立应用
- **任务列表**：跨上下文压缩的持久任务跟踪
- **提示建议**：基于上下文的智能命令建议
- **Git Worktree**：用于并行工作的隔离 worktree 分支
- **沙箱**：OS 级文件系统和网络隔离
- **托管设置**：通过 plist、Registry 或托管文件进行企业部署
- **配置**：用 JSON 配置文件自定义行为

---

## 规划模式

规划模式允许 Claude 在实现复杂任务前先思考，创建你可以审查和批准的详细计划。

### 什么是规划模式？

规划模式是一种两阶段方法：
1. **规划阶段**：Claude 分析任务并创建详细的实现计划
2. **实现阶段**：获得批准后，Claude 执行计划

### 何时使用规划模式

✅ 使用规划模式于：
- 复杂的多文件重构
- 新功能实现
- 架构更改
- 数据库迁移
- 主要 API 重新设计

❌ 不要使用规划模式于：
- 简单的 bug 修复
- 格式更改
- 单文件编辑
- 快速查询

### 激活规划模式

**斜杠命令**：
```bash
/plan 实现用户认证系统
```

**CLI 标志**：
```bash
claude --permission-mode plan
```

**设置为默认**：
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**键盘快捷键**：
- `Shift + Tab` - 切换权限模式（包括规划）
- `Alt + M` - 切换权限模式（Windows/Linux）

### 规划模式的好处

- **结构化实现方法**：实现步骤的详细分解
- **审查和批准**：执行前批准或调整计划
- **风险识别**：实现前识别潜在问题
- **清晰的阶段**：有组织的实现阶段和里程碑

### 示例：功能实现

```
用户：/plan 添加实时通知系统

Claude：我来创建实现实时通知的计划。

## 实现计划

### 第一阶段：基础设施设置
1. 安装 WebSocket 库（socket.io）
2. 设置 WebSocket 服务器
3. 配置连接管理

### 第二阶段：后端实现
4. 创建通知服务
5. 实现通知队列
6. 为通知添加数据库 Schema
7. 创建 API 端点

### 第三阶段：前端集成
8. 设置 WebSocket 客户端
9. 创建通知 UI 组件
10. 实现通知状态管理
11. 添加通知权限

### 第四阶段：测试与部署
12. 编写单元测试
13. 编写集成测试
14. 更新文档
15. 部署到预发布环境

预计时间：3-4 小时
要修改的文件：12
要创建的新文件：8

准备好继续吗？（是/否/修改计划）

用户：是

Claude：[开始按计划实现]
```

### 计划修改

```
用户：修改计划 - 现在跳过队列，我们稍后添加

Claude：更新的计划：
[显示删除队列的修改计划]

用户：看起来不错，继续

Claude：[实现修改后的计划]
```

### 规划模式配置

规划模式通过 CLI 标志或斜杠命令激活：

```bash
# 通过 CLI 激活规划模式
claude --permission-mode plan

# 或在 REPL 内使用 /plan 斜杠命令
/plan 实现用户认证系统
```

**规划的模型别名**：使用 `opusplan` 作为模型别名，用 Opus 进行规划，用 Sonnet 进行执行：

```bash
claude --model opusplan "设计并实现新的 API"
```

**外部编辑计划**：按 `Ctrl+G` 在外部编辑器中打开当前计划进行详细修改。

---

## 扩展思考

扩展思考允许 Claude 在提供解决方案之前花更多时间推理复杂问题。

### 什么是扩展思考？

扩展思考是一个蓄意的逐步推理过程，Claude 在其中：
- 分解复杂问题
- 考虑多种方法
- 评估权衡
- 推理边缘情况

### 激活扩展思考

**键盘快捷键**：
- `Option + T`（macOS）/ `Alt + T`（Windows/Linux）- 切换扩展思考

**自动激活**：
- 默认为所有模型启用（Opus 4.6、Sonnet 4.6、Haiku 4.5）
- Opus 4.6：具有努力级别的自适应推理：`low`（○）、`medium`（◐）、`high`（●）、`max`（仅 Opus 4.6）
- 其他模型：固定预算最多 31,999 个 token

**配置方法**：
- 切换：`Alt+T` / `Option+T`，或通过 `/config`
- 查看推理：`Ctrl+O`（详细模式）
- 设置努力：`/effort` 命令或 `--effort` 标志

**自定义预算**：
```bash
export MAX_THINKING_TOKENS=1024
```

**努力级别**（仅 Opus 4.6）：
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○)、medium (◐)、high (●) 或 max（仅 Opus 4.6）
```

**CLI 标志**：
```bash
claude --effort high "复杂架构审查"
```

**斜杠命令**：
```
/effort high
```

> **注意：** 提示中的关键词"ultrathink"会激活深度推理模式。努力级别 `low`、`medium`、`high` 和 `max`（仅 Opus 4.6）控制 Claude 执行多少推理。

### 扩展思考的好处

- **深度推理**：对复杂问题花更多时间思考
- **更好的架构决策**：通过全面评估做出明智选择
- **考虑边缘情况**：思考潜在问题和场景
- **彻底分析**：对复杂问题解决的结构化方法

### 扩展思考配置

扩展思考通过环境变量、键盘快捷键和 CLI 标志控制：

```bash
# 设置思考 token 预算
export MAX_THINKING_TOKENS=16000

# 设置努力级别（仅 Opus 4.6）：low (○)、medium (◐)、high (●) 或 max（仅 Opus 4.6）
export CLAUDE_CODE_EFFORT_LEVEL=high
```

在会话中使用 `Alt+T` / `Option+T` 切换，使用 `/effort` 设置努力，或通过 `/config` 配置。

---

## 自动模式

自动模式是一个研究预览版权限模式（2026 年 3 月），使用后台安全分类器在执行前审查每个动作。它允许 Claude 自主工作，同时阻止危险操作。

### 要求

- **计划**：团队计划（企业版和 API 正在推出）
- **模型**：Claude Sonnet 4.6 或 Opus 4.6
- **分类器**：在 Claude Sonnet 4.6 上运行（增加额外 token 成本）

### 启用自动模式

```bash
# 使用 CLI 标志解锁自动模式
claude --enable-auto-mode

# 然后在 REPL 中用 Shift+Tab 切换到它
```

或将其设置为默认权限模式：

```bash
claude --permission-mode auto
```

通过配置设置：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 分类器如何工作

后台分类器按以下决策顺序评估每个动作：

1. **允许/拒绝规则** -- 首先检查明确的权限规则
2. **只读/编辑自动批准** -- 文件读取和编辑自动通过
3. **分类器** -- 后台分类器审查该动作
4. **回退** -- 连续 3 次或总计 20 次阻止后回退到提示

### 默认阻止的动作

自动模式默认阻止以下内容：

| 阻止的动作 | 示例 |
|-----------|------|
| 管道到 shell 安装 | `curl \| bash` |
| 向外部发送敏感数据 | API 密钥、凭据通过网络 |
| 生产部署 | 针对生产的部署命令 |
| 大规模删除 | `rm -rf` 大目录 |
| IAM 更改 | 权限和角色修改 |
| 强制推送到主分支 | `git push --force origin main` |

### 默认允许的动作

| 允许的动作 | 示例 |
|-----------|------|
| 本地文件操作 | 读取、写入、编辑项目文件 |
| 声明的依赖安装 | `npm install`、来自清单的 `pip install` |
| 只读 HTTP | `curl` 获取文档 |
| 推送到当前分支 | `git push origin feature-branch` |

### 配置自动模式

**以 JSON 打印默认规则**：
```bash
claude auto-mode defaults
```

**通过 `autoMode.environment` 托管设置配置受信任的基础设施**，用于企业部署。这允许管理员定义受信任的 CI/CD 环境、部署目标和基础设施模式。

### 回退行为

当分类器不确定时，自动模式回退到提示用户：
- **连续 3 次**分类器阻止后
- 会话中**总计 20 次**分类器阻止后

这确保当分类器无法自信地批准动作时，用户始终保持控制。

### 无需团队计划的等效权限种子（不需要团队计划）

如果你没有团队计划或希望一种不需要后台分类器的更简单方法，可以用一个保守的安全权限规则基准种子 `~/.claude/settings.json`。该脚本从只读和本地检查规则开始，然后让你只在需要时选择性加入编辑、测试、本地 git 写入、包安装和 GitHub 写入动作。

**文件：** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 预览将添加的内容（不写入更改）
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 应用保守基准
python3 09-advanced-features/setup-auto-mode-permissions.py

# 只在需要时添加更多能力
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

该脚本在这些类别中添加规则：

| 类别 | 示例 |
|------|------|
| 核心只读工具 | `Read(*)`、`Glob(*)`、`Grep(*)`、`Agent(*)`、`WebSearch(*)`、`WebFetch(*)` |
| 本地检查 | `Bash(git status:*)`、`Bash(git log:*)`、`Bash(git diff:*)`、`Bash(cat:*)` |
| 可选编辑 | `Edit(*)`、`Write(*)`、`NotebookEdit(*)` |
| 可选测试/构建 | `Bash(pytest:*)`、`Bash(python3 -m pytest:*)`、`Bash(cargo test:*)` |
| 可选 git 写入 | `Bash(git add:*)`、`Bash(git commit:*)`、`Bash(git stash:*)` |
| 包管理器 | `Bash(npm install:*)`、`Bash(pip install:*)`、`Bash(cargo build:*)` |
| 构建和测试 | `Bash(make:*)`、`Bash(pytest:*)`、`Bash(go test:*)` |
| 常用 shell | `Bash(ls:*)`、`Bash(cat:*)`、`Bash(find:*)`、`Bash(cp:*)`、`Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`、`Bash(gh pr create:*)`、`Bash(gh issue list:*)` |

危险操作（`rm -rf`、`sudo`、强制推送、`DROP TABLE`、`terraform destroy` 等）被有意排除。该脚本是幂等的——运行两次不会重复规则。

---

## 后台任务

后台任务允许长时间运行的操作在不阻塞对话的情况下执行。

### 什么是后台任务？

后台任务在你继续工作时异步运行：
- 长测试套件
- 构建过程
- 数据库迁移
- 部署脚本
- 分析工具

**基本用法：**
```bash
用户：在后台运行测试

Claude：已启动任务 bg-1234

/task list           # 显示所有任务
/task status bg-1234 # 检查进度
/task show bg-1234   # 查看输出
/task cancel bg-1234 # 取消任务
```

---

## 计划任务

计划任务让你在定期计划或一次性提醒上自动运行提示。任务是会话范围的——它们在 Claude Code 激活时运行，并在会话结束时清除。自 v2.1.72+ 起可用。

### `/loop` 命令

```bash
# 明确的时间间隔
/loop 5m 检查部署是否完成

# 自然语言
/loop 每 30 分钟检查构建状态
```

也支持标准 5 字段 cron 表达式进行精确调度。

### 一次性提醒

设置在特定时间触发一次的提醒：

```
提醒我在下午 3 点推送发布分支
45 分钟后，运行集成测试
```

### 管理计划任务

| 工具 | 描述 |
|------|------|
| `CronCreate` | 创建新计划任务 |
| `CronList` | 列出所有活动的计划任务 |
| `CronDelete` | 删除计划任务 |

**限制和行为**：
- 每个会话最多 **50 个计划任务**
- 会话范围——会话结束时清除
- 定期任务在 **3 天**后自动过期
- 任务只在 Claude Code 运行时触发——没有错过触发的补偿

### 云端计划任务

使用 `/schedule` 创建在 Anthropic 基础设施上运行的云端计划任务：

```
/schedule 每天上午 9 点运行测试套件并报告失败
```

云端计划任务在重启后仍然存在，不需要 Claude Code 在本地运行。

### 禁用计划任务

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

---

## 权限模式

权限模式控制 Claude 可以在不需要明确批准的情况下采取哪些动作。

### 可用权限模式

| 模式 | 行为 |
|------|------|
| `default` | 仅读取文件；提示所有其他动作 |
| `acceptEdits` | 读取和编辑文件；提示命令 |
| `plan` | 仅读取文件（研究模式，无编辑） |
| `auto` | 所有动作，带后台安全分类器检查（研究预览版） |
| `bypassPermissions` | 所有动作，无权限检查（危险） |
| `dontAsk` | 只有预批准的工具执行；其他所有都被拒绝 |

在 CLI 中用 `Shift+Tab` 循环切换模式。用 `--permission-mode` 标志或 `permissions.defaultMode` 设置默认。

### 激活方法

**键盘快捷键**：
```bash
Shift + Tab  # 循环所有 6 种模式
```

**斜杠命令**：
```bash
/plan                  # 进入规划模式
```

**CLI 标志**：
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**设置**：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

---

## 无头模式

打印模式（`claude -p`）允许 Claude Code 在不需要交互输入的情况下运行，非常适合自动化和 CI/CD。这是非交互模式，替代了旧的 `--headless` 标志。

### 在打印模式下运行

```bash
# 运行特定任务
claude -p "运行所有测试"

# 处理管道内容
cat error.log | claude -p "分析这些错误"

# CI/CD 集成（GitHub Actions）
- name: AI 代码审查
  run: claude -p "审查 PR"
```

### 打印模式配置

打印模式（`claude -p`）支持多个自动化标志：

```bash
# 限制自主轮次
claude -p --max-turns 5 "重构这个模块"

# 结构化 JSON 输出
claude -p --output-format json "分析这个代码库"

# 禁用会话持久化
claude -p --no-session-persistence "一次性分析"
```

---

## 会话管理

有效管理多个 Claude Code 会话。

### 会话管理命令

| 命令 | 描述 |
|------|------|
| `/resume` | 通过 ID 或名称恢复对话 |
| `/rename` | 命名当前会话 |
| `/fork` | 将当前会话分叉为新分支 |
| `claude -c` | 继续最近的对话 |
| `claude -r "session"` | 通过名称或 ID 恢复会话 |

### 恢复会话

**继续最后的对话**：
```bash
claude -c
```

**恢复命名的会话**：
```bash
claude -r "auth-refactor" "完成这个 PR"
```

**重命名当前会话**（在 REPL 内）：
```
/rename auth-refactor
```

### 会话分叉

分叉会话以尝试替代方法而不失去原始：

```
/fork
```

或从 CLI：
```bash
claude --resume auth-refactor --fork-session "试试 OAuth"
```

---

## 交互功能

### 键盘快捷键

Claude Code 支持键盘快捷键以提高效率。以下是官方文档中的完整参考：

| 快捷键 | 描述 |
|--------|------|
| `Ctrl+C` | 取消当前输入/生成 |
| `Ctrl+D` | 退出 Claude Code |
| `Ctrl+G` | 在外部编辑器中编辑计划 |
| `Ctrl+L` | 清除终端屏幕 |
| `Ctrl+O` | 切换详细输出（查看推理） |
| `Ctrl+R` | 反向搜索历史 |
| `Ctrl+T` | 切换任务列表视图 |
| `Ctrl+B` | 后台运行的任务 |
| `Esc+Esc` | 回退代码/对话 |
| `Shift+Tab` / `Alt+M` | 切换权限模式 |
| `Option+P` / `Alt+P` | 切换模型 |
| `Option+T` / `Alt+T` | 切换扩展思考 |

**行编辑（标准 readline 快捷键）：**

| 快捷键 | 动作 |
|--------|------|
| `Ctrl + A` | 移到行首 |
| `Ctrl + E` | 移到行尾 |
| `Ctrl + K` | 剪切到行尾 |
| `Ctrl + U` | 剪切到行首 |
| `Ctrl + W` | 向后删除单词 |
| `Ctrl + Y` | 粘贴（yank） |
| `Tab` | 自动补全 |
| `↑ / ↓` | 命令历史 |

### 自定义键绑定

通过运行 `/keybindings` 创建自定义键盘快捷键，它会打开 `~/.claude/keybindings.json` 进行编辑（v2.1.18+）。

**配置格式**：

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

将绑定设置为 `null` 可解绑默认快捷键。

### Vim 模式

启用文本编辑的 Vi/Vim 键绑定：

**激活**：
- 使用 `/vim` 命令或 `/config` 启用
- 使用 `Esc` 切换到普通模式，`i/a/o` 切换到插入模式

### Bash 模式

使用 `!` 前缀直接执行 shell 命令：

```bash
! npm test
! git status
! cat src/index.js
```

---

## 语音听写

语音听写为 Claude Code 提供按键通话语音输入，允许你说出提示而不是键入。

### 激活语音听写

```
/voice
```

### 功能

| 功能 | 描述 |
|------|------|
| **按键通话** | 按住键录音，松开发送 |
| **20 种语言** | 语音转文字支持 20 种语言 |
| **自定义键绑定** | 通过 `/keybindings` 配置按键通话键 |
| **账号要求** | 需要 Claude.ai 账号进行 STT 处理 |

---

## 频道

频道（研究预览版）允许 MCP 服务器将消息推送到运行中的 Claude Code 会话，支持与外部服务的实时集成。

### 订阅频道

```bash
# 启动时订阅频道插件
claude --channels discord,telegram
```

### 支持的集成

| 集成 | 描述 |
|------|------|
| **Discord** | 在你的会话中接收和响应 Discord 消息 |
| **Telegram** | 在你的会话中接收和响应 Telegram 消息 |

### 配置

**企业部署的托管设置**：

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

`allowedChannelPlugins` 托管设置控制整个组织允许哪些频道插件。

---

## Chrome 集成

Chrome 集成将 Claude Code 连接到你的 Chrome 或 Microsoft Edge 浏览器，进行实时 Web 自动化和调试。这是自 v2.0.73+ 起可用的 beta 功能（Edge 支持在 v1.0.36+ 中添加）。

### 启用 Chrome 集成

**启动时**：

```bash
claude --chrome      # 启用 Chrome 连接
claude --no-chrome   # 禁用 Chrome 连接
```

**在会话中**：

```
/chrome
```

### 功能

| 功能 | 描述 |
|------|------|
| **实时调试** | 实时读取控制台日志、检查 DOM 元素、调试 JavaScript |
| **设计验证** | 对照设计模型比较渲染的页面 |
| **表单验证** | 测试表单提交、输入验证和错误处理 |
| **Web 应用测试** | 与已认证的应用（Gmail、Google Docs、Notion 等）交互 |
| **数据提取** | 从 Web 页面抓取和处理内容 |
| **会话录制** | 将浏览器交互录制为 GIF 文件 |

---

## 远程控制

远程控制让你从手机、平板电脑或任何浏览器继续本地运行的 Claude Code 会话。你的本地会话继续在你的机器上运行——没有任何内容移到云端。可在 Pro、Max、团队和企业计划上使用（v2.1.51+）。

### 启动远程控制

**从 CLI**：

```bash
# 使用默认会话名称启动
claude remote-control

# 使用自定义名称启动
claude remote-control --name "Auth Refactor"
```

**在会话中**：

```
/remote-control
/remote-control "Auth Refactor"
```

### 连接到会话

从另一台设备连接的三种方式：

1. **会话 URL** — 会话启动时打印到终端；在任何浏览器中打开
2. **二维码** — 启动后按 `空格键` 显示可扫描的二维码
3. **按名称查找** — 在 claude.ai/code 或 Claude 移动应用（iOS/Android）中浏览你的会话

### 安全

- 在你的机器上**不打开入站端口**
- 仅**通过 TLS 的出站 HTTPS**
- **范围凭据** — 多个短期的、范围有限的 token
- **会话隔离** — 每个远程会话是独立的

---

## Web 会话

Web 会话允许你直接在 claude.ai/code 浏览器中运行 Claude Code，或从 CLI 创建 Web 会话。

### 创建 Web 会话

```bash
# 从 CLI 创建新 Web 会话
claude --remote "实现新的 API 端点"
```

### 在本地恢复 Web 会话

```bash
# 在本地终端恢复 Web 会话
claude --teleport
```

或在交互式 REPL 中：
```
/teleport
```

---

## 桌面应用

Claude Code 桌面应用提供独立应用程序，具有视觉 diff 审查、并行会话和集成连接器。可在 macOS 和 Windows 上使用（Pro、Max、团队和企业计划）。

### 安装

从 [claude.ai](https://claude.ai) 下载适合你平台的版本：
- **macOS**：通用构建（Apple Silicon 和 Intel）
- **Windows**：x64 和 ARM64 安装程序可用

### 从 CLI 移交

将当前 CLI 会话转移到桌面应用：

```
/desktop
```

### 核心功能

| 功能 | 描述 |
|------|------|
| **Diff 视图** | 带内联注释的逐文件视觉审查；Claude 读取注释并修改 |
| **应用预览** | 自动启动带嵌入式浏览器的开发服务器进行实时验证 |
| **PR 监控** | GitHub CLI 集成，自动修复 CI 失败，检查通过时自动合并 |
| **并行会话** | 侧边栏中有自动 Git worktree 隔离的多个会话 |
| **计划任务** | 应用打开时运行的定期任务（每小时、每天、工作日、每周） |
| **富渲染** | 带语法高亮的代码、Markdown 和图表渲染 |

### 企业功能

- **管理控制台**：控制组织的 Code 选项卡访问和权限设置
- **MDM 部署**：在 macOS 上通过 MDM 或在 Windows 上通过 MSIX 部署
- **SSO 集成**：要求组织成员使用单点登录
- **托管设置**：集中管理团队配置和模型可用性

---

## 任务列表

任务列表功能提供持久任务跟踪，在上下文压缩（对话历史被修剪以适应上下文窗口时）后仍然存在。

### 切换任务列表

在会话中按 `Ctrl+T` 切换任务列表视图。

### 命名任务目录

使用 `CLAUDE_CODE_TASK_LIST_ID` 环境变量创建跨会话共享的命名任务目录：

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

这允许多个会话共享同一任务列表，对团队工作流或多会话项目很有用。

---

## 提示建议

提示建议显示基于你的 git 历史和当前对话上下文的灰色示例命令。

### 工作原理

- 建议显示为输入提示下方的灰色文本
- 按 `Tab` 接受建议
- 按 `Enter` 接受并立即提交
- 建议是上下文感知的，从 git 历史和对话状态中提取

### 禁用提示建议

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktree

Git Worktree 允许你在隔离的 worktree 中启动 Claude Code，支持在不同分支上并行工作而无需暂存或切换。

### 在 Worktree 中启动

```bash
# 在隔离的 worktree 中启动 Claude Code
claude --worktree
# 或
claude -w
```

### Worktree 位置

Worktree 创建于：
```
<repo>/.claude/worktrees/<name>
```

### 用于 Monorepo 的稀疏检出

使用 `worktree.sparsePaths` 设置在 monorepo 中执行稀疏检出，减少磁盘使用和克隆时间：

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### 自动清理

如果在 worktree 中没有进行更改，会话结束时会自动清理。

---

## 沙箱

沙箱为 Claude Code 执行的 Bash 命令提供 OS 级文件系统和网络隔离。这是对权限规则的补充，提供额外的安全层。

### 启用沙箱

**斜杠命令**：
```
/sandbox
```

**CLI 标志**：
```bash
claude --sandbox       # 启用沙箱
claude --no-sandbox    # 禁用沙箱
```

### 配置设置

| 设置 | 描述 |
|------|------|
| `sandbox.enabled` | 启用或禁用沙箱 |
| `sandbox.failIfUnavailable` | 如果无法激活沙箱则失败 |
| `sandbox.filesystem.allowWrite` | 允许写入访问的路径 |
| `sandbox.filesystem.allowRead` | 允许读取访问的路径 |
| `sandbox.filesystem.denyRead` | 拒绝读取访问的路径 |
| `sandbox.enableWeakerNetworkIsolation` | 在 macOS 上启用较弱的网络隔离 |

### 示例配置

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

---

## 托管设置（企业版）

托管设置使企业管理员能够使用平台原生管理工具在整个组织中部署 Claude Code 配置。

### 部署方法

| 平台 | 方法 | 自从 |
|------|------|------|
| macOS | 托管 plist 文件（MDM） | v2.1.51+ |
| Windows | Windows 注册表 | v2.1.51+ |
| 跨平台 | 托管配置文件 | v2.1.51+ |
| 跨平台 | 托管 drop-in（`managed-settings.d/` 目录） | v2.1.83+ |

### 可用托管设置

| 设置 | 描述 |
|------|------|
| `disableBypassPermissionsMode` | 防止用户启用绕过权限 |
| `availableModels` | 限制用户可以选择的模型 |
| `allowedChannelPlugins` | 控制允许哪些频道插件 |
| `autoMode.environment` | 为自动模式配置受信任的基础设施 |
| 自定义策略 | 组织特定的权限和工具策略 |

---

## 配置和设置

### 配置文件位置

1. **全局配置**：`~/.claude/config.json`
2. **项目配置**：`./.claude/config.json`
3. **用户配置**：`~/.config/claude-code/settings.json`

### 环境变量

用环境变量覆盖配置：

```bash
# 模型选择
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API 配置
export ANTHROPIC_API_KEY=sk-ant-...

# 思考配置
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# 功能切换
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # 由 --bare 标志设置

# MCP 配置
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# 任务管理
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# 代理团队（实验性）
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true

# 子代理和插件配置
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=true

# 子进程和流
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### 配置管理命令

```
用户：/config
[打开交互式配置菜单]
```

---

## 最佳实践

### 规划模式
- ✅ 用于复杂的多步骤任务
- ✅ 批准前审查计划
- ✅ 需要时修改计划
- ❌ 不用于简单任务

### 扩展思考
- ✅ 用于架构决策
- ✅ 用于复杂问题解决
- ✅ 审查思考过程
- ❌ 不用于简单查询

### 后台任务
- ✅ 用于长时间运行的操作
- ✅ 监控任务进度
- ✅ 优雅地处理任务失败
- ❌ 不要启动太多并发任务

### 权限
- ✅ 用 `plan` 进行代码审查（只读）
- ✅ 用 `default` 进行交互式开发
- ✅ 用 `acceptEdits` 进行自动化工作流
- ✅ 用 `auto` 进行带安全防护的自主工作
- ❌ 除非绝对必要，不要使用 `bypassPermissions`

### 会话
- ✅ 为不同任务使用单独的会话
- ✅ 保存重要的会话状态
- ✅ 清理旧会话
- ❌ 不要在一个会话中混合不相关的工作

---

## 附加资源

- [官方交互模式文档](https://code.claude.com/docs/en/interactive-mode)
- [官方无头模式文档](https://code.claude.com/docs/en/headless)
- [CLI 参考](https://code.claude.com/docs/en/cli-reference)
- [检查点指南](../08-checkpoints/) - 会话管理和回退
- [斜杠命令](../01-slash-commands/) - 命令参考
- [内存指南](../02-memory/) - 持久上下文
- [技能指南](../03-skills/) - 自主功能
- [子代理指南](../04-subagents/) - 委托任务执行
- [MCP 指南](../05-mcp/) - 外部数据访问
- [钩子指南](../06-hooks/) - 事件驱动自动化
- [插件指南](../07-plugins/) - 捆绑扩展
- [官方计划任务文档](https://code.claude.com/docs/en/scheduled-tasks)
- [官方 Chrome 集成文档](https://code.claude.com/docs/en/chrome)
- [官方远程控制文档](https://code.claude.com/docs/en/remote-control)
- [官方键绑定文档](https://code.claude.com/docs/en/keybindings)
- [官方桌面应用文档](https://code.claude.com/docs/en/desktop)
