<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Slash Commands

## 概览

Slash commands 是在交互式会话中控制 Claude 行为的快捷命令，主要分为以下几类：

- **Built-in commands**：Claude Code 内置命令（`/help`、`/clear`、`/model`）
- **Skills**：以 `SKILL.md` 文件定义的用户命令（`/optimize`、`/pr`）
- **Plugin commands**：来自已安装插件的命令（`/frontend-design:frontend-design`）
- **MCP prompts**：来自 MCP servers 的命令（`/mcp__github__list_prs`）

> **Note**：自定义 slash commands 已并入 skills。`.claude/commands/` 下的文件仍可用，但现在推荐使用 skills（`.claude/skills/`）。两种方式都会创建 `/command-name` 快捷命令。完整说明见 [Skills Guide](../03-skills/README.zh-CN.md)。

## Built-in Commands 参考

Built-in commands 是常见操作的快捷入口。目前可用 **55+ built-in commands** 与 **5 bundled skills**。在 Claude Code 输入 `/` 可查看完整列表，输入 `/` 后接任意字母可筛选。

| Command | Purpose |
|---------|---------|
| `/add-dir <path>` | 添加工作目录 |
| `/agents` | 管理 agent 配置 |
| `/branch [name]` | 将当前对话分叉为新会话（别名：`/fork`）。注意：`/fork` 在 v2.1.77 重命名为 `/branch` |
| `/btw <question>` | 提问侧向问题，不写入主对话历史 |
| `/chrome` | 配置 Chrome 浏览器集成 |
| `/clear` | 清空对话（别名：`/reset`、`/new`） |
| `/color [color\|default]` | 设置提示栏颜色 |
| `/compact [instructions]` | 压缩对话，可附带聚焦说明 |
| `/config` | 打开设置（别名：`/settings`） |
| `/context` | 以彩色网格可视化上下文使用情况 |
| `/copy [N]` | 复制助手回复到剪贴板；`w` 可写入文件 |
| `/cost` | 显示 token 使用统计 |
| `/desktop` | 在 Desktop 应用中继续（别名：`/app`） |
| `/diff` | 交互式 diff 查看器（针对未提交改动） |
| `/doctor` | 诊断安装健康状态 |
| `/effort [low\|medium\|high\|max\|auto]` | 设置推理强度。`max` 需要 Opus 4.6 |
| `/exit` | 退出 REPL（别名：`/quit`） |
| `/export [filename]` | 将当前会话导出到文件或剪贴板 |
| `/extra-usage` | 配置额外用量额度（速率限制相关） |
| `/fast [on\|off]` | 切换 fast mode |
| `/feedback` | 提交反馈（别名：`/bug`） |
| `/help` | 显示帮助 |
| `/hooks` | 查看 hook 配置 |
| `/ide` | 管理 IDE 集成 |
| `/init` | 初始化 `CLAUDE.md`。设置 `CLAUDE_CODE_NEW_INIT=true` 可启用交互流程 |
| `/insights` | 生成会话分析报告 |
| `/install-github-app` | 配置 GitHub Actions app |
| `/install-slack-app` | 安装 Slack app |
| `/keybindings` | 打开快捷键配置 |
| `/login` | 切换 Anthropic 账号 |
| `/logout` | 退出 Anthropic 账号 |
| `/mcp` | 管理 MCP servers 和 OAuth |
| `/memory` | 编辑 `CLAUDE.md`，切换 auto-memory |
| `/mobile` | 生成移动端二维码（别名：`/ios`、`/android`） |
| `/model [model]` | 选择模型，可用左右方向键切换 effort |
| `/passes` | 分享 Claude Code 免费周 |
| `/permissions` | 查看/更新权限（别名：`/allowed-tools`） |
| `/plan [description]` | 进入 plan mode |
| `/plugin` | 管理插件 |
| `/pr-comments [PR]` | 获取 GitHub PR 评论 |
| `/privacy-settings` | 隐私设置（仅 Pro/Max） |
| `/release-notes` | 查看更新日志 |
| `/reload-plugins` | 重载已激活插件 |
| `/remote-control` | 从 claude.ai 远程控制（别名：`/rc`） |
| `/remote-env` | 配置默认远程环境 |
| `/rename [name]` | 重命名会话 |
| `/resume [session]` | 恢复会话（别名：`/continue`） |
| `/review` | **Deprecated** —— 请改用 `code-review` 插件 |
| `/rewind` | 回退对话和/或代码（别名：`/checkpoint`） |
| `/sandbox` | 切换 sandbox mode |
| `/schedule [description]` | 创建/管理计划任务 |
| `/security-review` | 扫描当前分支的安全漏洞 |
| `/skills` | 列出可用 skills |
| `/stats` | 可视化每日用量、会话数、连续使用天数 |
| `/status` | 显示版本、模型、账号 |
| `/statusline` | 配置状态栏 |
| `/tasks` | 列出/管理后台任务 |
| `/terminal-setup` | 配置终端快捷键 |
| `/theme` | 更换配色主题 |
| `/vim` | 切换 Vim/Normal 模式 |
| `/voice` | 切换按住说话语音输入 |

### Bundled Skills

这些 skills 随 Claude Code 一起提供，调用方式与 slash commands 相同：

| Skill | Purpose |
|-------|---------|
| `/batch <instruction>` | 使用 worktrees 编排大规模并行改动 |
| `/claude-api` | 加载当前项目语言对应的 Claude API 参考 |
| `/debug [description]` | 启用调试日志 |
| `/loop [interval] <prompt>` | 按设定间隔重复执行 prompt |
| `/simplify [focus]` | 评审改动文件的代码质量 |

### Deprecated Commands

| Command | Status |
|---------|--------|
| `/review` | Deprecated —— 已由 `code-review` 插件替代 |
| `/output-style` | v2.1.73 起弃用 |
| `/fork` | 重命名为 `/branch`（别名仍可用，v2.1.77） |

### Recent Changes

- `/fork` 重命名为 `/branch`，并保留 `/fork` 作为别名（v2.1.77）
- `/output-style` 弃用（v2.1.73）
- `/review` 弃用，改用 `code-review` 插件
- 新增 `/effort` 命令，`max` 级别需要 Opus 4.6
- 新增 `/voice` 命令，用于按住说话语音输入
- 新增 `/schedule` 命令，用于创建/管理计划任务
- 新增 `/color` 命令，用于自定义提示栏颜色
- `/model` 选择器现在显示人类可读标签（如 “Sonnet 4.6”），而非原始模型 ID
- `/resume` 支持 `/continue` 别名
- MCP prompts 可作为 `/mcp__<server>__<prompt>` 命令使用（见 [MCP Prompts as Commands](#mcp-prompts-as-commands)）

## Custom Commands (Now Skills)

自定义 slash commands 已**并入 skills**。两种方式都会创建可通过 `/command-name` 调用的命令：

| Approach | Location | Status |
|----------|----------|--------|
| **Skills (Recommended)** | `.claude/skills/<name>/SKILL.md` | 当前标准 |
| **Legacy Commands** | `.claude/commands/<name>.md` | 仍可使用 |

如果 skill 与 command 同名，**skill 优先级更高**。例如同时存在 `.claude/commands/review.md` 和 `.claude/skills/review/SKILL.md` 时，会使用 skill 版本。

### Migration Path

现有 `.claude/commands/` 文件无需修改即可继续使用。迁移到 skills 的路径如下：

**Before (Command):**
```text
.claude/commands/optimize.md
```

**After (Skill):**
```text
.claude/skills/optimize/SKILL.md
```

### Why Skills?

相比 legacy commands，skills 提供更多能力：

- **Directory structure**：可打包脚本、模板和参考文件
- **Auto-invocation**：Claude 可在匹配场景下自动触发 skills
- **Invocation control**：可控制由用户触发、Claude 触发，或二者都可
- **Subagent execution**：通过 `context: fork` 在隔离上下文中执行
- **Progressive disclosure**：按需加载附加文件

### Creating a Custom Command as a Skill

创建包含 `SKILL.md` 的目录：

```bash
mkdir -p .claude/skills/my-command
```

**File:** `.claude/skills/my-command/SKILL.md`

```yaml
---
name: my-command
description: What this command does and when to use it
---

# My Command

Instructions for Claude to follow when this command is invoked.

1. First step
2. Second step
3. Third step
```

### Frontmatter Reference

| Field | Purpose | Default |
|-------|---------|---------|
| `name` | 命令名（会变成 `/name`） | 目录名 |
| `description` | 简短描述（帮助 Claude 判断触发时机） | 第一段 |
| `argument-hint` | 参数自动补全提示 | None |
| `allowed-tools` | 命令可免确认使用的工具 | Inherits |
| `model` | 指定使用模型 | Inherits |
| `disable-model-invocation` | 若为 `true`，仅用户可触发（Claude 不能自动触发） | `false` |
| `user-invocable` | 若为 `false`，在 `/` 菜单隐藏 | `true` |
| `context` | 设为 `fork` 时在隔离 subagent 运行 | None |
| `agent` | 使用 `context: fork` 时的 agent 类型 | `general-purpose` |
| `hooks` | skill 级 hooks（PreToolUse、PostToolUse、Stop） | None |

### Arguments

命令支持接收参数：

**所有参数使用 `$ARGUMENTS`：**

```yaml
---
name: fix-issue
description: Fix a GitHub issue by number
---

Fix issue #$ARGUMENTS following our coding standards
```

Usage: `/fix-issue 123` → `$ARGUMENTS` 为 `"123"`

**按位置使用 `$0`、`$1` 等：**

```yaml
---
name: review-pr
description: Review a PR with priority
---

Review PR #$0 with priority $1
```

Usage: `/review-pr 456 high` → `$0`=`"456"`，`$1`=`"high"`

### Dynamic Context with Shell Commands

可在 prompt 前通过 `` !`command` `` 执行 bash 命令：

```yaml
---
name: commit
description: Create a git commit with context
allowed-tools: Bash(git *)
---

## Context

- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`

## Your task

Based on the above changes, create a single git commit.
```

### File References

使用 `@` 引入文件内容：

```markdown
Review the implementation in @src/utils/helpers.js
Compare @src/old-version.js with @src/new-version.js
```

## Plugin Commands

插件可提供自定义命令：

```text
/plugin-name:command-name
```

如果没有命名冲突，也可直接使用 `/command-name`。

**Examples:**
```bash
/frontend-design:frontend-design
/commit-commands:commit
```

## MCP Prompts as Commands

MCP servers 可将 prompts 暴露为 slash commands：

```text
/mcp__<server-name>__<prompt-name> [arguments]
```

**Examples:**
```bash
/mcp__github__list_prs
/mcp__github__pr_review 456
/mcp__jira__create_issue "Bug title" high
```

### MCP Permission Syntax

可在权限中控制 MCP server 访问范围：

- `mcp__github` - 访问整个 GitHub MCP server
- `mcp__github__*` - 通配访问所有工具
- `mcp__github__get_issue` - 仅访问特定工具

## Command Architecture

```mermaid
graph TD
    A["User Input: /command-name"] --> B{"Command Type?"}
    B -->|Built-in| C["Execute Built-in"]
    B -->|Skill| D["Load SKILL.md"]
    B -->|Plugin| E["Load Plugin Command"]
    B -->|MCP| F["Execute MCP Prompt"]

    D --> G["Parse Frontmatter"]
    G --> H["Substitute Variables"]
    H --> I["Execute Shell Commands"]
    I --> J["Send to Claude"]
    J --> K["Return Results"]
```

## Command Lifecycle

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: Types /optimize
    Claude->>FS: Searches .claude/skills/ and .claude/commands/
    FS-->>Claude: Returns optimize/SKILL.md
    Claude->>Claude: Parses frontmatter
    Claude->>CLI: Executes !`command` substitutions
    CLI-->>Claude: Command outputs
    Claude->>Claude: Substitutes $ARGUMENTS
    Claude->>User: Processes prompt
    Claude->>User: Returns results
```

## Available Commands in This Folder

这些示例命令可安装为 skills 或 legacy commands。

### 1. `/optimize` - Code Optimization

分析代码中的性能瓶颈、内存泄漏与优化机会。

**Usage:**
```text
/optimize
[Paste your code]
```

### 2. `/pr` - Pull Request Preparation

引导你完成 PR 准备清单，包括 lint、测试与 commit 格式。

**Usage:**
```text
/pr
```

**Screenshot:**
![/pr](pr-slash-command.png)

### 3. `/generate-api-docs` - API Documentation Generator

从源码生成完整 API 文档。

**Usage:**
```text
/generate-api-docs
```

### 4. `/commit` - Git Commit with Context

基于仓库动态上下文生成 git commit。

**Usage:**
```text
/commit [optional message]
```

### 5. `/push-all` - Stage, Commit, and Push

暂存全部改动、创建 commit，并在安全检查后推送到远端。

**Usage:**
```text
/push-all
```

**Safety Checks:**
- Secrets: `.env*`、`*.key`、`*.pem`、`credentials.json`
- API Keys: 检测真实 key 与占位符
- Large files: 未使用 Git LFS 且 `>10MB`
- Build artifacts: `node_modules/`、`dist/`、`__pycache__/`

### 6. `/doc-refactor` - Documentation Restructuring

重构项目文档结构，提升清晰度与可访问性。

**Usage:**
```text
/doc-refactor
```

### 7. `/setup-ci-cd` - CI/CD Pipeline Setup

搭建 pre-commit hooks 与 GitHub Actions 质量保障流程。

**Usage:**
```text
/setup-ci-cd
```

### 8. `/unit-test-expand` - Test Coverage Expansion

通过补齐未覆盖分支与边界场景提升测试覆盖率。

**Usage:**
```text
/unit-test-expand
```

## Installation

### As Skills (Recommended)

复制到你的 skills 目录：

```bash
# Create skills directory
mkdir -p .claude/skills

# For each command file, create a skill directory
for cmd in optimize pr commit; do
  mkdir -p .claude/skills/$cmd
  cp 01-slash-commands/$cmd.md .claude/skills/$cmd/SKILL.md
done
```

### As Legacy Commands

复制到你的 commands 目录：

```bash
# Project-wide (team)
mkdir -p .claude/commands
cp 01-slash-commands/*.md .claude/commands/

# Personal use
mkdir -p ~/.claude/commands
cp 01-slash-commands/*.md ~/.claude/commands/
```

## Creating Your Own Commands

### Skill Template (Recommended)

创建 `.claude/skills/my-command/SKILL.md`：

```yaml
---
name: my-command
description: What this command does. Use when [trigger conditions].
argument-hint: [optional-args]
allowed-tools: Bash(npm *), Read, Grep
---

# Command Title

## Context

- Current branch: !`git branch --show-current`
- Related files: @package.json

## Instructions

1. First step
2. Second step with argument: $ARGUMENTS
3. Third step

## Output Format

- How to format the response
- What to include
```

### User-Only Command (No Auto-Invocation)

对于有副作用、不应被 Claude 自动触发的命令：

```yaml
---
name: deploy
description: Deploy to production
disable-model-invocation: true
allowed-tools: Bash(npm *), Bash(git *)
---

Deploy the application to production:

1. Run tests
2. Build application
3. Push to deployment target
4. Verify deployment
```

## Best Practices

| Do | Don't |
|------|---------|
| 使用清晰、动作导向的命令名 | 为一次性任务创建命令 |
| 在 `description` 里写明触发条件 | 在命令里堆砌复杂逻辑 |
| 让命令聚焦单一任务 | 硬编码敏感信息 |
| 对副作用命令启用 `disable-model-invocation` | 省略 description 字段 |
| 使用 `!` 前缀注入动态上下文 | 假设 Claude 自动知道当前状态 |
| 将关联资源放进 skill 目录组织 | 把所有内容都塞进一个文件 |

## Troubleshooting

### Command Not Found

**Solutions:**
- 检查文件是否位于 `.claude/skills/<name>/SKILL.md` 或 `.claude/commands/<name>.md`
- 确认 frontmatter 里的 `name` 与预期命令名一致
- 重启 Claude Code 会话
- 运行 `/help` 查看可用命令

### Command Not Executing as Expected

**Solutions:**
- 提供更明确、具体的指令
- 在 skill 文件里加入示例
- 如使用 bash，检查 `allowed-tools`
- 先用简单输入测试

### Skill vs Command Conflict

若同名 skill 与 command 并存，**skill 优先**。请删除其一或重命名。

## Related Guides

- **[Skills](../03-skills/README.zh-CN.md)** - skills 完整参考（可自动触发能力）
- **[Memory](../02-memory/README.zh-CN.md)** - 通过 `CLAUDE.md` 持久化上下文
- **[Subagents](../04-subagents/README.zh-CN.md)** - 委派式 AI agents
- **[Plugins](../07-plugins/README.zh-CN.md)** - 打包命令集合
- **[Hooks](../06-hooks/README.zh-CN.md)** - 事件驱动自动化

## Additional Resources

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode) - Built-in commands 参考
- [Official Skills Documentation](https://code.claude.com/docs/en/skills) - skills 完整参考
- [CLI Reference](https://code.claude.com/docs/en/cli-reference) - 命令行选项

---

*Part of the [Claude How To](../README.zh-CN.md) guide series*
