<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# 用一个周末掌握 Claude Code

从输入 `claude` 开始，到编排 agents、hooks、skills 和 MCP servers，全程配有可视化教程、可直接复制粘贴的模板，以及循序渐进的学习路径。

**[15 分钟快速上手](#15-分钟快速上手)** | **[找到适合你的起点](#不知道从哪里开始)** | **[浏览功能目录](CATALOG.md)**

---

## 目录

- [问题在哪里](#问题在哪里)
- [Claude How To 如何解决这些问题](#claude-how-to-如何解决这些问题)
- [它是如何工作的](#它是如何工作的)
- [不知道从哪里开始？](#不知道从哪里开始)
- [15 分钟快速上手](#15-分钟快速上手)
- [你能用它做什么？](#你能用它做什么)
- [常见问题](#常见问题)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

---

## 问题在哪里

你已经安装了 Claude Code。也试着跑了几个提示词。然后呢？

- **官方文档会介绍功能，但不会告诉你如何把它们组合起来。** 你知道 slash commands 存在，但不知道怎样把它们和 hooks、memory、subagents 串起来，形成一个真正能节省数小时的工作流。
- **没有清晰的学习路径。** 应该先学 MCP 还是 hooks？先学 skills 还是 subagents？结果往往是每样都看了一点，但没有一个真正掌握。
- **示例太基础。** 一个 “hello world” 级别的 slash command，并不能帮你构建一个可用于生产环境的代码审查流水线，也无法让它结合 memory、委派给专门 agent、并自动执行安全扫描。

你实际上只用上了 Claude Code 10% 的能力，而剩下的 90% 你甚至不知道自己错过了什么。

---

## Claude How To 如何解决这些问题

这不是另一份功能参考手册，而是一份**结构化、可视化、以示例驱动的指南**。它会教你如何使用 Claude Code 的每一项功能，并提供今天就能复制到项目里的真实场景模板。

| | 官方文档 | 本指南 |
|--|---------------|------------|
| **形式** | 参考文档 | 带 Mermaid 图表的可视化教程 |
| **深度** | 功能说明 | 底层工作原理解析 |
| **示例** | 基础代码片段 | 可立即上手的生产级模板 |
| **结构** | 按功能组织 | 递进式学习路径（从入门到高级） |
| **上手方式** | 自主摸索 | 带时间预估的引导式路线图 |
| **自我评估** | 没有 | 交互式测验，帮你找出短板并生成个性化路径 |

### 你将获得：

- **10 个教程模块**，覆盖 Claude Code 的所有核心功能，从 slash commands 到自定义 agent 团队
- **可复制粘贴的配置**，包括 slash commands、`CLAUDE.md` 模板、hook 脚本、MCP 配置、subagent 定义，以及完整 plugin 打包
- **Mermaid 图表**，展示每个功能的内部工作机制，让你不仅知道“怎么做”，还知道“为什么这么做”
- **一条引导式学习路径**，帮助你在 11 到 13 小时内从初学者成长为高级用户
- **内置自测能力**，可以直接在 Claude Code 中运行 `/self-assessment` 或 `/lesson-quiz hooks` 找出知识盲点

**[开始学习路线  ->](LEARNING-ROADMAP.md)**

---

## 它是如何工作的

### 1. 先找到你的水平

完成[自我评估测验](LEARNING-ROADMAP.md#find-your-level)，或者在 Claude Code 中运行 `/self-assessment`。系统会根据你已经掌握的内容，生成一份个性化学习路线。

### 2. 按引导路径学习

按照顺序学习 10 个模块，每个模块都建立在前一个模块的基础上。你可以一边学，一边把模板直接复制到自己的项目中。

### 3. 把多个功能组合成工作流

真正的威力来自功能组合。你会学到如何把 slash commands、memory、subagents 和 hooks 连接成自动化流水线，用于代码审查、部署和文档生成等任务。

### 4. 测试你的理解程度

每学完一个模块后运行 `/lesson-quiz [topic]`。测验会精准指出你漏掉的知识点，让你快速补齐短板。

**[15 分钟快速上手](#15-分钟快速上手)**

---

## 已被 5,900+ 开发者信赖

- **5,900+ GitHub stars**，来自每天都在使用 Claude Code 的开发者
- **690+ forks**，许多团队已将这份指南改造成自己的工作流版本
- **持续维护中**，会与每次 Claude Code 发布保持同步（最新版本：v2.2.0，2026 年 3 月）
- **社区驱动**，贡献者会分享他们在真实工作中的配置和经验

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不知道从哪里开始？

先做自我评估，或者直接按你的水平开始：

| Level | 你可以…… | 从这里开始 | 时间 |
|-------|-----------|------------|------|
| **Beginner** | 启动 Claude Code 并进行对话 | [Slash Commands](01-slash-commands/README.md) | 约 2.5 小时 |
| **Intermediate** | 使用 `CLAUDE.md` 和自定义命令 | [Skills](03-skills/README.md) | 约 3.5 小时 |
| **Advanced** | 配置 MCP servers 和 hooks | [Advanced Features](09-advanced-features/README.md) | 约 5 小时 |

**完整学习路径，共 10 个模块：**

| 顺序 | 模块 | 水平 | 时间 |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/README.md) | 初学者 | 30 分钟 |
| 2 | [Memory](02-memory/README.md) | 初学者+ | 45 分钟 |
| 3 | [Checkpoints](08-checkpoints/README.md) | 中级 | 45 分钟 |
| 4 | [CLI Basics](10-cli/README.md) | 初学者+ | 30 分钟 |
| 5 | [Skills](03-skills/README.md) | 中级 | 1 小时 |
| 6 | [Hooks](06-hooks/README.md) | 中级 | 1 小时 |
| 7 | [MCP](05-mcp/README.md) | 中级+ | 1 小时 |
| 8 | [Subagents](04-subagents/README.md) | 中级+ | 1.5 小时 |
| 9 | [Advanced Features](09-advanced-features/README.md) | 高级 | 2 到 3 小时 |
| 10 | [Plugins](07-plugins/README.md) | 高级 | 2 小时 |

**[完整学习路线图 ->](LEARNING-ROADMAP.md)**

---

## 15 分钟快速上手

```bash
# 1. 克隆这份指南
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 复制你的第一个 slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 试试看：在 Claude Code 中输入
# /optimize

# 4. 想更进一步？设置项目记忆：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安装一个 skill：
cp -r 03-skills/code-review ~/.claude/skills/
```

如果你想完成更完整的基础配置，这里有一个**1 小时的关键配置方案**：

```bash
# Slash commands（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 项目记忆（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安装一个 skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 周末目标：继续添加 hooks、subagents、MCP 和 plugins
# 按学习路径逐步完成配置
```

**[查看完整安装参考](#15-分钟快速上手)**

---

## 你能用它做什么？

| 使用场景 | 你会组合使用的功能 |
|----------|------------------------|
| **自动化代码审查** | Slash Commands + Subagents + Memory + MCP |
| **团队入职培训** | Memory + Slash Commands + Plugins |
| **CI/CD 自动化** | CLI Reference + Hooks + Background Tasks |
| **文档生成** | Skills + Subagents + Plugins |
| **安全审计** | Subagents + Skills + Hooks（只读模式） |
| **DevOps 流水线** | Plugins + MCP + Hooks + Background Tasks |
| **复杂重构** | Checkpoints + Planning Mode + Hooks |

---

## 常见问题

**这是免费的吗？**
是的。MIT 许可证，永久免费。你可以将它用于个人项目、工作项目或团队中，唯一要求只是保留许可证声明。

**它有人维护吗？**
是的，而且持续维护。该指南会与每次 Claude Code 发布同步。当前版本是 v2.2.0（2026 年 3 月），兼容 Claude Code 2.1+。

**它和官方文档有什么不同？**
官方文档是功能参考手册；这份指南则是教程，包含图示、生产级模板和渐进式学习路径。两者是互补关系，建议先用本指南学习，再在需要具体细节时查官方文档。

**完整学完需要多久？**
完整路径大约需要 11 到 13 小时。但你在 15 分钟内就能获得直接收益，只要复制一个 slash command 模板并试用即可。

**我可以搭配 Claude Sonnet / Haiku / Opus 使用吗？**
可以。所有模板都适用于 Claude Sonnet 4.6、Claude Opus 4.6 和 Claude Haiku 4.5。

**我可以参与贡献吗？**
当然可以。请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献规范。我们欢迎新的示例、bug 修复、文档改进以及社区模板。

**我可以离线阅读吗？**
可以。运行 `uv run scripts/build_epub.py`，即可生成包含全部内容和渲染后 Mermaid 图表的 EPUB 电子书。

---

## 今天就开始掌握 Claude Code

你已经安装好了 Claude Code。你和 10 倍生产力之间，差的只是知道该怎么正确使用它。这份指南会提供结构化路径、可视化解释和可直接复制的模板，帮助你真正掌握它。

MIT 许可证，永久免费。克隆它、fork 它、改造成适合你自己的版本。

**[开始学习路线 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15 分钟快速上手](#15-分钟快速上手)**

---

<details>
<summary>快速导航：全部功能</summary>

| 功能 | 说明 | 文件夹 |
|---------|-------------|--------|
| **功能目录** | 包含安装命令的完整参考 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 用户手动触发的快捷命令 | [01-slash-commands/README.md](01-slash-commands/README.md) |
| **Memory** | 持久上下文 | [02-memory/README.md](02-memory/README.md) |
| **Skills** | 可复用能力 | [03-skills/README.md](03-skills/README.md) |
| **Subagents** | 专门化 AI 助手 | [04-subagents/README.md](04-subagents/README.md) |
| **MCP Protocol** | 访问外部工具 | [05-mcp/README.md](05-mcp/README.md) |
| **Hooks** | 事件驱动自动化 | [06-hooks/README.md](06-hooks/README.md) |
| **Plugins** | 打包后的功能集合 | [07-plugins/README.md](07-plugins/README.md) |
| **Checkpoints** | 会话快照与回退 | [08-checkpoints/README.md](08-checkpoints/README.md) |
| **Advanced Features** | 规划、思考、后台任务 | [09-advanced-features/README.md](09-advanced-features/README.md) |
| **CLI Reference** | 命令、参数与选项 | [10-cli/README.md](10-cli/README.md) |
| **博客文章** | 真实使用案例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 调用方式 | 持久性 | 最适合 |
|---------|-----------|------------|----------|
| **Slash Commands** | 手动（`/cmd`） | 仅当前会话 | 快速快捷操作 |
| **Memory** | 自动加载 | 跨会话 | 长期记忆与学习 |
| **Skills** | 自动触发 | 文件系统级 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务拆分 |
| **MCP Protocol** | 自动查询 | 实时 | 获取实时数据 |
| **Hooks** | 事件触发 | 已配置 | 自动化与校验 |
| **Plugins** | 一条命令 | 全功能打包 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 会话级 | 安全试验 |
| **Planning Mode** | 手动/自动 | 规划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务持续期间 | 长时间运行的操作 |
| **CLI Reference** | 终端命令 | 会话/脚本级 | 自动化与脚本开发 |

</details>

<details>
<summary>安装速查表</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints（默认自动开启，可在设置中配置）
# 参见 08-checkpoints/README.md

# Advanced Features（在设置中配置）
# 参见 09-advanced-features/config-examples.json

# CLI Reference（无需安装）
# 使用示例见 10-cli/README.md
```

</details>

<details>
<summary>01. Slash Commands</summary>

**位置**: [01-slash-commands/README.md](01-slash-commands/README.md)

**是什么**: 以 Markdown 文件形式存储、由用户手动触发的快捷命令

**示例**:
- `optimize.md` - 代码优化分析
- `pr.md` - Pull Request 准备
- `generate-api-docs.md` - API 文档生成器

**安装**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使用方法**:
```
/optimize
/pr
/generate-api-docs
```

**了解更多**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**位置**: [02-memory/README.md](02-memory/README.md)

**是什么**: 跨会话持久化的上下文

**示例**:
- `project-CLAUDE.md` - 团队共享的项目规范
- `directory-api-CLAUDE.md` - 目录级规则
- `personal-CLAUDE.md` - 个人偏好

**安装**:
```bash
# 项目记忆
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录记忆
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人记忆
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用方法**: Claude 会自动加载

</details>

<details>
<summary>03. Skills</summary>

**位置**: [03-skills/README.md](03-skills/README.md)

**是什么**: 可复用、会在合适时自动触发的能力包，包含说明和脚本

**示例**:
- `code-review/` - 带脚本的完整代码审查能力
- `brand-voice/` - 品牌语气一致性检查
- `doc-generator/` - API 文档生成器

**安装**:
```bash
# 个人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使用方法**: 在相关场景下自动触发

</details>

<details>
<summary>04. Subagents</summary>

**位置**: [04-subagents/README.md](04-subagents/README.md)

**是什么**: 拥有隔离上下文和自定义提示词的专门化 AI 助手

**示例**:
- `code-reviewer.md` - 全面代码质量分析
- `test-engineer.md` - 测试策略与覆盖率
- `documentation-writer.md` - 技术文档编写
- `secure-reviewer.md` - 面向安全的审查（只读）
- `implementation-agent.md` - 完整功能实现

**安装**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用方法**: 由主 agent 自动委派

</details>

<details>
<summary>05. MCP Protocol</summary>

**位置**: [05-mcp/README.md](05-mcp/README.md)

**是什么**: 用于访问外部工具和 API 的 Model Context Protocol

**示例**:
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件操作
- `multi-mcp.json` - 多个 MCP servers 配置

**安装**:
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP server
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动添加到项目 .mcp.json（参见 [05-mcp/README.md](05-mcp/README.md) 中的示例）
```

**使用方法**: 配置完成后，Claude 会自动获得 MCP 工具能力

</details>

<details>
<summary>06. Hooks</summary>

**位置**: [06-hooks/README.md](06-hooks/README.md)

**是什么**: 基于事件触发的 shell 命令，会在 Claude Code 事件发生时自动执行

**示例**:
- `format-code.sh` - 写入前自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 扫描安全问题
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 校验用户提示词
- `notify-team.sh` - 事件发生时发送通知

**安装**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 hooks：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**使用方法**: hooks 会在事件发生时自动执行

**Hook 类型**（4 类，25 个事件）:
- **工具 Hook**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **会话 Hook**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **任务 Hook**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **生命周期 Hook**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**位置**: [07-plugins/README.md](07-plugins/README.md)

**是什么**: 把 commands、agents、MCP 和 hooks 打包在一起的功能集合

**示例**:
- `pr-review/` - 完整的 PR 审查工作流
- `devops-automation/` - 部署与监控
- `documentation/` - 文档生成

**安装**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使用方法**: 使用其中打包好的 slash commands 和功能

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**位置**: [08-checkpoints/README.md](08-checkpoints/README.md)

**是什么**: 保存对话状态，并回退到之前的时间点，以探索不同方案

**核心概念**:
- **Checkpoint**: 对话状态快照
- **Rewind**: 回到之前的 checkpoint
- **Branch Point**: 从同一个 checkpoint 分叉出多种方案

**使用方法**:
```
# 每次用户提示后都会自动创建 checkpoint
# 如需回退，按两次 Esc，或者使用：
/rewind

# 然后从以下五个选项中选择：
# 1. 恢复代码和对话
# 2. 恢复对话
# 3. 恢复代码
# 4. 从这里开始总结
# 5. 算了
```

**使用场景**:
- 尝试不同实现方式
- 从错误中恢复
- 安全试验
- 比较不同备选方案
- 对不同设计做 A/B 测试

</details>

<details>
<summary>09. Advanced Features</summary>

**位置**: [09-advanced-features/README.md](09-advanced-features/README.md)

**是什么**: 面向复杂工作流和自动化的高级能力

**包括**:
- **Planning Mode**：编码前先创建详细实现计划
- **Extended Thinking**：用于复杂问题的深度推理（用 `Alt+T` / `Option+T` 切换）
- **Background Tasks**：运行长时间操作且不阻塞当前会话
- **Permission Modes**：`default`、`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions`
- **Headless Mode**：在 CI/CD 中运行 Claude Code：`claude -p "Run tests and generate report"`
- **Session Management**：`/resume`、`/rename`、`/fork`、`claude -c`、`claude -r`
- **Configuration**：在 `~/.claude/settings.json` 中自定义行为

完整配置请参见 [config-examples.json](09-advanced-features/config-examples.json)。

</details>

<details>
<summary>10. CLI Reference</summary>

**位置**: [10-cli/README.md](10-cli/README.md)

**是什么**: Claude Code 的完整命令行接口参考

**快速示例**:
```bash
# 交互模式
claude "explain this project"

# 输出模式（非交互）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# 为脚本输出 JSON
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**使用场景**: CI/CD 流水线集成、脚本自动化、批处理、多会话工作流、自定义 agent 配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码审查工作流

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

用户：/review-pr

Claude：
1. 加载项目 memory（编码规范）
2. 通过 GitHub MCP 获取 PR
3. 委派给 code-reviewer subagent
4. 委派给 test-engineer subagent
5. 汇总发现
6. 提供完整审查结果
```

### 自动化文档生成

```markdown
# 使用：Skills + Subagents + Memory

用户："为 auth 模块生成 API 文档"

Claude：
1. 加载项目 memory（文档规范）
2. 识别出文档生成请求
3. 自动触发 doc-generator skill
4. 委派给 api-documenter subagent
5. 生成带示例的完整文档
```

### DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

用户：/deploy production

Claude：
1. 运行部署前 hook（校验环境）
2. 委派给 deployment-specialist subagent
3. 通过 Kubernetes MCP 执行部署
4. 监控进度
5. 运行部署后 hook（健康检查）
6. 报告状态
```

</details>

<details>
<summary>目录结构</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md（本文件）
```

</details>

<details>
<summary>最佳实践</summary>

### 应该做的
- 从简单的 slash commands 开始
- 逐步增加功能
- 用 memory 保存团队规范
- 先在本地测试配置
- 为自定义实现写文档
- 对项目配置做版本控制
- 和团队共享 plugins

### 不应该做的
- 不要创建重复功能
- 不要硬编码凭据
- 不要跳过文档
- 不要把简单任务过度复杂化
- 不要忽视安全最佳实践
- 不要提交敏感数据

</details>

<details>
<summary>故障排查</summary>

### 功能没有加载
1. 检查文件位置和命名
2. 验证 YAML frontmatter 语法
3. 检查文件权限
4. 查看 Claude Code 版本兼容性

### MCP 连接失败
1. 检查环境变量
2. 检查 MCP server 是否正确安装
3. 测试凭据
4. 检查网络连通性

### Subagent 没有发生委派
1. 检查工具权限
2. 确认 agent 描述是否清晰
3. 查看任务复杂度
4. 单独测试 agent

</details>

<details>
<summary>测试</summary>

本项目包含完整的自动化测试：

- **单元测试**：基于 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**：使用 Ruff 做 lint 和格式化检查
- **安全**：使用 Bandit 做漏洞扫描
- **类型检查**：使用 mypy 做静态类型分析
- **构建验证**：测试 EPUB 生成功能
- **覆盖率跟踪**：集成 Codecov

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行全部单元测试
pytest scripts/tests/ -v

# 运行带覆盖率报告的测试
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行代码质量检查
ruff check scripts/
ruff format --check scripts/

# 运行安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 运行类型检查
mypy scripts/ --ignore-missing-imports
```

每次 push 到 `main` / `develop`，以及每次向 `main` 提交 PR 时，测试都会自动运行。详情见 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读这份指南？你可以生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

这会生成包含全部内容与 Mermaid 渲染图表的 `claude-howto-guide.epub`。

更多选项见 [scripts/README.md](scripts/README.md)。

</details>

<details>
<summary>参与贡献</summary>

发现问题，或者想贡献一个示例？非常欢迎你的帮助。

**请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，了解以下详细规范：**
- 可贡献的内容类型（示例、文档、功能、bug、反馈）
- 如何搭建开发环境
- 目录结构以及如何添加内容
- 编写规范与最佳实践
- Commit 和 PR 流程

**我们的社区标准：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我们如何彼此相处
- [SECURITY.md](SECURITY.md) - 安全政策与漏洞报告方式

### 报告安全问题

如果你发现了安全漏洞，请负责任地报告：

1. **使用 GitHub 私密漏洞报告功能**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或者阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **不要**公开提交安全漏洞 issue

快速开始：
1. Fork 并克隆仓库
2. 创建一个清晰描述用途的分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按规范进行修改
4. 提交一个说明清楚的 Pull Request

**需要帮助？** 打开一个 issue 或 discussion，我们会引导你完成整个过程。

</details>

<details>
<summary>更多资源</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 可直接使用的 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的创造者分享了他系统化的工作流：并行 agents、共享 `CLAUDE.md`、Plan mode、slash commands、subagents，以及用于长时间自主会话的验证 hooks。

</details>

---

## 参与贡献

欢迎贡献内容。如何开始请查看我们的[贡献指南](CONTRIBUTING.md)。

## 贡献者

感谢所有为本项目做出贡献的人。

| 贡献者 | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 许可证

MIT 许可证，详见 [LICENSE](LICENSE)。你可以自由使用、修改和分发，唯一要求是保留许可证声明。

---

**最后更新**：2026 年 3 月
**Claude Code 版本**：2.1+
**兼容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
