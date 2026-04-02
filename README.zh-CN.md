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

<p align="right">
  <strong>语言：</strong>
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a>
</p>

> 中文入口： [快速参考](QUICK_REFERENCE.zh-CN.md) · [功能目录](CATALOG.zh-CN.md) · [学习路线图](LEARNING-ROADMAP.zh-CN.md) · [索引](INDEX.zh-CN.md)

# 用一个周末掌握 Claude Code

从只会输入 `claude`，到能编排 agents、hooks、skills 和 MCP servers —— 通过可视化教程、可直接复制的模板，以及循序渐进的学习路径。

**[15 分钟快速上手](#15-分钟快速上手)** | **[不确定从哪里开始？](#不确定从哪里开始)** | **[浏览功能目录](CATALOG.zh-CN.md)**

---

## 目录

- [你遇到的问题](#你遇到的问题)
- [Claude How To 如何解决这些问题](#claude-how-to-如何解决这些问题)
- [它是如何工作的](#它是如何工作的)
- [不确定从哪里开始？](#不确定从哪里开始)
- [15 分钟快速上手](#15-分钟快速上手)
- [你可以用它构建什么？](#你可以用它构建什么)
- [常见问题](#常见问题)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

---

## 你遇到的问题

你已经安装了 Claude Code，跑了几个 prompt。然后呢？

- **官方文档介绍了功能，但没有告诉你如何组合它们。** 你知道有 slash commands，但不知道如何把它和 hooks、memory、subagents 串成一个真正省时的工作流。
- **缺少清晰的学习路径。** 应该先学 MCP 还是 hooks？先学 skills 还是 subagents？结果就是每个都看了一点，却没有真正掌握。
- **示例太基础。** 一个 "hello world" slash command 并不能帮你搭建生产级代码评审流水线（用 memory、委派给专用 agents、自动跑安全扫描）。

你实际上只用了 Claude Code 10% 的能力，而且你并不知道自己还不知道什么。

---

## Claude How To 如何解决这些问题

这不是另一本功能索引手册，而是一份**结构化、可视化、示例驱动**的指南，教你用真实场景模板掌握 Claude Code 的每个核心功能，而且今天就能复制到你的项目里。

| | 官方文档 | 本指南 |
|--|---------|--------|
| **形式** | 参考手册 | 带 Mermaid 图的可视化教程 |
| **深度** | 功能说明 | 解释底层如何工作 |
| **示例** | 基础片段 | 可立即使用的生产级模板 |
| **结构** | 按功能组织 | 渐进式学习路径（从初级到高级） |
| **上手方式** | 自主摸索 | 带时间预估的引导式路线图 |
| **自测能力** | 无 | 交互式测验，定位短板并生成个性化路径 |

### 你将获得：

- **10 个教程模块**，覆盖 Claude Code 全部关键能力（从 slash commands 到自定义 agent 团队）
- **可复制配置**：slash commands、CLAUDE.md 模板、hook 脚本、MCP 配置、subagent 定义、完整 plugin 套件
- **Mermaid 架构图**：展示每个能力的内部机制，帮你理解 *为什么*，而不仅仅是 *怎么做*
- **引导式学习路径**：11-13 小时从新手到高阶用户
- **内置自测**：直接在 Claude Code 运行 `/self-assessment` 或 `/lesson-quiz hooks` 来定位知识缺口

**[开始学习路径  ->](LEARNING-ROADMAP.zh-CN.md)**

---

## 它是如何工作的

### 1）先定位你的水平

完成 [自测问卷](LEARNING-ROADMAP.zh-CN.md#-先定位你的水平)，或在 Claude Code 中运行 `/self-assessment`。你会得到基于当前能力的个性化路线图。

### 2）按引导路径学习

按顺序完成 10 个模块。每个模块都建立在前一个模块之上，且可边学边复制模板到项目中。

### 3）把功能组合成工作流

真正的威力来自组合。你会学到如何把 slash commands + memory + subagents + hooks 组装成自动化流水线，用于代码评审、部署、文档生成等场景。

### 4）测试你的理解程度

每个模块后运行 `/lesson-quiz [topic]`。测验会指出你漏掉的点，帮助你快速补齐。

**[15 分钟快速上手](#15-分钟快速上手)**

---

## 被 5,900+ 开发者使用

- **5,900+ GitHub stars**：来自日常使用 Claude Code 的开发者
- **690+ forks**：团队基于该指南定制自有工作流
- **持续维护**：每次 Claude Code 发布都会同步更新（最新：v2.2.0，2026 年 3 月）
- **社区驱动**：由真实开发者贡献配置与实践经验

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不确定从哪里开始？

先做自测，或者直接按等级选择入口：

| 等级 | 你目前可以… | 从这里开始 | 预计时间 |
|------|--------------|-----------|---------|
| **初学者** | 启动 Claude Code 并对话 | [Slash Commands](01-slash-commands/README.zh-CN.md) | ~2.5 小时 |
| **中级** | 使用 CLAUDE.md 和自定义命令 | [Skills](03-skills/README.zh-CN.md) | ~3.5 小时 |
| **高级** | 配置 MCP servers 和 hooks | [Advanced Features](09-advanced-features/README.zh-CN.md) | ~5 小时 |

**包含全部 10 个模块的完整学习路径：**

| 顺序 | 模块 | 等级 | 时间 |
|------|------|------|------|
| 1 | [Slash Commands](01-slash-commands/README.zh-CN.md) | Beginner | 30 min |
| 2 | [Memory](02-memory/README.zh-CN.md) | Beginner+ | 45 min |
| 3 | [Checkpoints](08-checkpoints/README.zh-CN.md) | Intermediate | 45 min |
| 4 | [CLI Basics](10-cli/README.zh-CN.md) | Beginner+ | 30 min |
| 5 | [Skills](03-skills/README.zh-CN.md) | Intermediate | 1 hour |
| 6 | [Hooks](06-hooks/README.zh-CN.md) | Intermediate | 1 hour |
| 7 | [MCP](05-mcp/README.zh-CN.md) | Intermediate+ | 1 hour |
| 8 | [Subagents](04-subagents/README.zh-CN.md) | Intermediate+ | 1.5 hours |
| 9 | [Advanced Features](09-advanced-features/README.zh-CN.md) | Advanced | 2-3 hours |
| 10 | [Plugins](07-plugins/README.zh-CN.md) | Advanced | 2 hours |

**[完整学习路线图 ->](LEARNING-ROADMAP.zh-CN.md)**

---

## 15 分钟快速上手

```bash
# 1. 克隆本指南
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 复制你的第一个 slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 在 Claude Code 里尝试：
# /optimize

# 4. 准备继续？先配置项目 memory：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安装一个 skill：
cp -r 03-skills/code-review ~/.claude/skills/
```

如果你想一步到位，这里有**1 小时核心配置**：

```bash
# Slash commands（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 项目 memory（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安装一个 skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 周末目标：补齐 hooks、subagents、MCP、plugins
# 按学习路径逐步配置
```

**[查看完整安装参考](#15-分钟快速上手)**

---

## 你可以用它构建什么？

| 使用场景 | 组合能力 |
|----------|---------|
| **自动化代码评审** | Slash Commands + Subagents + Memory + MCP |
| **团队入职标准化** | Memory + Slash Commands + Plugins |
| **CI/CD 自动化** | CLI Reference + Hooks + Background Tasks |
| **文档自动生成** | Skills + Subagents + Plugins |
| **安全审计** | Subagents + Skills + Hooks（只读模式） |
| **DevOps 流水线** | Plugins + MCP + Hooks + Background Tasks |
| **复杂重构** | Checkpoints + Planning Mode + Hooks |

---

## 常见问题

**这个项目免费吗？**  
是。MIT 许可证，永久免费。你可以在个人、公司、团队场景使用，唯一要求是保留许可证声明。

**这个项目有持续维护吗？**  
有。会随 Claude Code 每次发布同步更新。当前版本 v2.2.0（2026 年 3 月），兼容 Claude Code 2.1+。

**和官方文档有什么区别？**  
官方文档是功能参考；本指南是教程，包含图示、生产模板和渐进学习路径。两者互补：先在这里掌握方法，再回官方文档查细节。

**完整学完要多久？**  
完整路径约 11-13 小时。但你 15 分钟就能得到直接收益：复制一个 slash command 模板并跑起来。

**能用于 Claude Sonnet / Haiku / Opus 吗？**  
可以。模板适配 Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5。

**可以贡献内容吗？**  
非常欢迎。请看 [CONTRIBUTING.md](CONTRIBUTING.zh-CN.md) 获取贡献规范。我们欢迎新示例、bug 修复、文档改进和社区模板。

**可以离线阅读吗？**  
可以。运行 `uv run scripts/build_epub.py` 生成带图表渲染的 EPUB 电子书。

---

## 现在就开始掌握 Claude Code

你已经安装了 Claude Code。你与 10x 生产力之间的差距，只是“是否知道如何系统使用它”。本指南提供结构化路径、可视化解释与可复制模板，帮助你快速抵达。

MIT 许可，永久免费。克隆它、fork 它、把它变成你的工作系统。

**[开始学习路径 ->](LEARNING-ROADMAP.zh-CN.md)** | **[浏览功能目录](CATALOG.zh-CN.md)** | **[15 分钟快速上手](#15-分钟快速上手)**

---

<details>
<summary>快速导航——全部功能</summary>

| 功能 | 说明 | 目录 |
|------|------|------|
| **Feature Catalog** | 含安装命令的完整参考 | [CATALOG.md](CATALOG.zh-CN.md) |
| **Slash Commands** | 用户手动触发的快捷命令 | [01-slash-commands/](01-slash-commands/README.zh-CN.md) |
| **Memory** | 跨会话持久上下文 | [02-memory/](02-memory/README.zh-CN.md) |
| **Skills** | 可复用能力模块 | [03-skills/](03-skills/README.zh-CN.md) |
| **Subagents** | 专用 AI 助手 | [04-subagents/](04-subagents/README.zh-CN.md) |
| **MCP Protocol** | 外部工具访问 | [05-mcp/](05-mcp/README.zh-CN.md) |
| **Hooks** | 事件驱动自动化 | [06-hooks/](06-hooks/README.zh-CN.md) |
| **Plugins** | 打包化能力集合 | [07-plugins/](07-plugins/README.zh-CN.md) |
| **Checkpoints** | 会话快照与回退 | [08-checkpoints/](08-checkpoints/README.zh-CN.md) |
| **Advanced Features** | 规划、思考、后台任务 | [09-advanced-features/](09-advanced-features/README.zh-CN.md) |
| **CLI Reference** | 命令、参数与选项 | [10-cli/](10-cli/README.zh-CN.md) |
| **Blog Posts** | 真实使用案例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 触发方式 | 持久性 | 最适合 |
|------|---------|-------|--------|
| **Slash Commands** | 手动（`/cmd`） | 仅会话内 | 快速快捷操作 |
| **Memory** | 自动加载 | 跨会话 | 长期记忆 |
| **Skills** | 自动调用 | 文件系统 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务分工 |
| **MCP Protocol** | 自动查询 | 实时 | 实时数据访问 |
| **Hooks** | 事件触发 | 配置持久 | 自动化与校验 |
| **Plugins** | 一条命令安装 | 全能力打包 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 基于会话 | 安全试验 |
| **Planning Mode** | 手动/自动 | 计划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务期间 | 长耗时操作 |
| **CLI Reference** | 终端命令 | 会话/脚本 | 自动化与脚本化 |

</details>

<details>
<summary>安装速查</summary>

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

# Checkpoints（默认已启用，可在 settings 配置）
# 详见 08-checkpoints/README.md

# Advanced Features（在 settings 中配置）
# 详见 09-advanced-features/config-examples.json

# CLI Reference（无需安装）
# 详见 10-cli/README.md
```

</details>

<details>
<summary>01. Slash Commands</summary>

**位置**： [01-slash-commands/](01-slash-commands/README.zh-CN.md)

**定义**：存储为 Markdown 的用户触发快捷命令

**示例**：
- `optimize.md` - 代码优化分析
- `pr.md` - Pull Request 准备
- `generate-api-docs.md` - API 文档生成

**安装**：
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使用**：
```
/optimize
/pr
/generate-api-docs
```

**延伸阅读**： [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**位置**： [02-memory/](02-memory/README.zh-CN.md)

**定义**：跨会话持久化上下文

**示例**：
- `project-CLAUDE.md` - 团队级项目规范
- `directory-api-CLAUDE.md` - 目录级规则
- `personal-CLAUDE.md` - 个人偏好

**安装**：
```bash
# 项目记忆
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录记忆
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人记忆
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用**：由 Claude 自动加载

</details>

<details>
<summary>03. Skills</summary>

**位置**： [03-skills/](03-skills/README.zh-CN.md)

**定义**：可复用、可自动触发的能力模块（含说明与脚本）

**示例**：
- `code-review/` - 含脚本的综合代码审查
- `brand-voice/` - 品牌语气一致性
- `doc-generator/` - API 文档生成

**安装**：
```bash
# 个人技能
cp -r 03-skills/code-review ~/.claude/skills/

# 项目技能
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使用**：在相关场景下自动触发

</details>

<details>
<summary>04. Subagents</summary>

**位置**： [04-subagents/](04-subagents/README.zh-CN.md)

**定义**：具备隔离上下文和定制提示词的专用 AI 助手

**示例**：
- `code-reviewer.md` - 综合代码质量审查
- `test-engineer.md` - 测试策略与覆盖
- `documentation-writer.md` - 技术文档撰写
- `secure-reviewer.md` - 安全专项评审（只读）
- `implementation-agent.md` - 全流程功能实现

**安装**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用**：由主 agent 自动委派

</details>

<details>
<summary>05. MCP Protocol</summary>

**位置**： [05-mcp/](05-mcp/README.zh-CN.md)

**定义**：Model Context Protocol，用于连接外部工具和 API

**示例**：
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件系统操作
- `multi-mcp.json` - 多 MCP server 组合

**安装**：
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# CLI 添加 MCP server
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动写入项目 .mcp.json（见 05-mcp/ 示例）
```

**使用**：配置完成后，MCP 工具会自动可用

</details>

<details>
<summary>06. Hooks</summary>

**位置**： [06-hooks/](06-hooks/README.zh-CN.md)

**定义**：事件驱动 shell 命令，在 Claude Code 事件发生时自动执行

**示例**：
- `format-code.sh` - 写入前自动格式化
- `pre-commit.sh` - 提交前自动跑测试
- `security-scan.sh` - 安全扫描
- `log-bash.sh` - 记录 Bash 命令
- `validate-prompt.sh` - 校验用户输入
- `notify-team.sh` - 事件通知团队

**安装**：
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置：
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

**使用**：按事件自动执行

**Hook 类型**（4 类、25 事件）：
- **Tool Hooks**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **Session Hooks**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **Task Hooks**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **Lifecycle Hooks**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**位置**： [07-plugins/](07-plugins/README.zh-CN.md)

**定义**：commands、agents、MCP、hooks 的打包集合

**示例**：
- `pr-review/` - 完整 PR 评审流程
- `devops-automation/` - 部署与监控
- `documentation/` - 文档自动化生成

**安装**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使用**：直接使用插件打包命令与能力

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**位置**： [08-checkpoints/](08-checkpoints/README.zh-CN.md)

**定义**：保存会话状态并回退到历史点，探索不同实现路径

**核心概念**：
- **Checkpoint**：会话状态快照
- **Rewind**：回到历史 checkpoint
- **Branch Point**：从同一 checkpoint 分叉多种方案

**使用**：
```
# 每次用户 prompt 都会自动创建 checkpoint
# 回退方式：按两次 Esc 或使用：
/rewind

# 然后从 5 个选项中选择：
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Never mind
```

**适用场景**：
- 尝试不同实现方案
- 从错误中恢复
- 安全试验
- 对比替代方案
- A/B 设计实验

</details>

<details>
<summary>09. Advanced Features</summary>

**位置**： [09-advanced-features/](09-advanced-features/README.zh-CN.md)

**定义**：面向复杂工作流与自动化的高级能力

**包含**：
- **Planning Mode** —— 编码前先形成详细实现计划
- **Extended Thinking** —— 复杂问题深度推理（`Alt+T` / `Option+T` 切换）
- **Background Tasks** —— 长任务后台执行，不阻塞主流程
- **Permission Modes** —— `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** —— CI/CD 中运行：`claude -p "Run tests and generate report"`
- **Session Management** —— `/resume`, `/rename`, `/fork`, `claude -c`, `claude -r`
- **Configuration** —— 在 `~/.claude/settings.json` 中定制行为

完整配置见 [config-examples.json](09-advanced-features/config-examples.json)。

</details>

<details>
<summary>10. CLI Reference</summary>

**位置**： [10-cli/](10-cli/README.zh-CN.md)

**定义**：Claude Code 命令行接口完整参考

**快速示例**：
```bash
# 交互模式
claude "explain this project"

# 打印模式（非交互）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# 脚本场景的 JSON 输出
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**使用场景**：CI/CD 集成、脚本自动化、批处理、多会话流程、自定义 agent 配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码评审工作流

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### 自动化文档生成

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Claude:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### DevOps 部署工作流

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Claude:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

</details>

<details>
<summary>目录结构</summary>

```text
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
└── README.md (this file)
```

</details>

<details>
<summary>最佳实践</summary>

### 建议做法
- 从最简单的 slash commands 开始
- 逐步叠加能力，不要一次加太多
- 用 memory 固化团队规范
- 先在本地验证配置
- 为自定义实现补齐文档
- 项目配置纳入版本控制
- 通过 plugins 在团队共享能力

### 不建议
- 不要重复造已有能力
- 不要硬编码凭证
- 不要跳过文档
- 不要把简单问题复杂化
- 不要忽略安全最佳实践
- 不要提交敏感数据

</details>

<details>
<summary>故障排查</summary>

### 功能未加载
1. 检查文件位置和命名
2. 验证 YAML frontmatter 语法
3. 检查文件权限
4. 确认 Claude Code 版本兼容性

### MCP 连接失败
1. 检查环境变量
2. 检查 MCP server 安装
3. 测试认证凭据
4. 检查网络连通性

### Subagent 未被委派
1. 检查工具权限配置
2. 检查 agent 描述是否清晰
3. 评估任务复杂度是否匹配
4. 独立测试 agent

</details>

<details>
<summary>测试</summary>

该项目包含完整自动化测试体系：

- **Unit Tests**：基于 pytest（Python 3.10、3.11、3.12）
- **Code Quality**：Ruff lint 与格式检查
- **Security**：Bandit 漏洞扫描
- **Type Checking**：mypy 静态类型分析
- **Build Verification**：EPUB 生成验证
- **Coverage Tracking**：Codecov 覆盖率追踪

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行全部单元测试
pytest scripts/tests/ -v

# 运行测试并生成覆盖率报告
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行代码质量检查
ruff check scripts/
ruff format --check scripts/

# 运行安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 运行类型检查
mypy scripts/ --ignore-missing-imports
```

测试会在每次 push 到 `main`/`develop` 以及每次向 `main` 提交 PR 时自动执行。详见 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读本指南？可以生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

会生成 `claude-howto-guide.epub`，包含全部内容以及已渲染的 Mermaid 图。

更多选项见 [scripts/README.md](scripts/README.zh-CN.md)。

</details>

<details>
<summary>参与贡献</summary>

发现问题，或希望贡献示例？非常欢迎！

**请先阅读 [CONTRIBUTING.md](CONTRIBUTING.zh-CN.md)，其中包括：**
- 贡献类型（示例、文档、功能、修复、反馈）
- 开发环境搭建方式
- 目录结构与内容添加方式
- 编写规范与最佳实践
- Commit / PR 流程

**社区规范：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.zh-CN.md) - 社区行为准则
- [SECURITY.md](SECURITY.zh-CN.md) - 安全策略与漏洞上报

### 安全问题上报

如果你发现安全漏洞，请按负责任方式报告：

1. **使用 GitHub 私有漏洞上报**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **不要**将安全漏洞公开为普通 issue

快速流程：
1. Fork 并 clone 仓库
2. 创建清晰分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按规范完成变更
4. 提交包含清晰说明的 PR

**需要帮助？** 直接开 issue 或 discussion，我们会协助你推进。

</details>

<details>
<summary>更多资源</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 可直接使用的 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 创建者分享的系统化方法：并行 agents、共享 CLAUDE.md、Plan mode、slash commands、subagents、验证 hooks，用于长时自治会话。

</details>

---

## 参与贡献

欢迎贡献！请查看 [Contributing Guide](CONTRIBUTING.zh-CN.md)。

## Contributors

感谢所有贡献者！

| Contributor | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 许可证

MIT License，详见 [LICENSE](LICENSE)。允许自由使用、修改、分发；唯一要求是保留许可证声明。

---

**Last Updated**: March 2026  
**Claude Code Version**: 2.1+  
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
