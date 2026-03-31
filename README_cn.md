<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# 一个周末掌握 Claude Code

从输入 `claude` 到编排智能体、hooks、skills 和 MCP 服务器——配有可视化教程、可直接复制的模板，以及有引导的学习路径。

**[15 分钟快速上手](#-15-分钟快速上手)** | **[找到你的级别](#-不知道从哪里开始)** | **[浏览功能目录](CATALOG.md)**

---

## 目录

- [问题所在](#问题所在)
- [Claude How To 如何解决这个问题](#claude-how-to-如何解决这个问题)
- [工作原理](#工作原理)
- [不知道从哪里开始？](#-不知道从哪里开始)
- [15 分钟快速上手](#-15-分钟快速上手)
- [你能用它构建什么？](#你能用它构建什么)
- [常见问题](#常见问题)
- [贡献](#贡献)
- [许可证](#许可证)

---

## 问题所在

你安装了 Claude Code，跑了几个提示词，然后呢？

- **官方文档描述了功能，但没有告诉你如何组合使用。** 你知道 slash commands 的存在，却不知道如何将它们与 hooks、memory 和 subagents 串联成一个真正节省数小时的工作流。
- **没有清晰的学习路径。** 应该先学 MCP 还是先学 hooks？先学 Skills 还是先学 subagents？结果是什么都浏览了一遍，却什么都没真正掌握。
- **示例太基础。** 一个"hello world"级别的 slash command 根本无法帮你搭建一条生产级的代码审查流水线——那种能使用 memory、委派给专项智能体并自动运行安全扫描的流水线。

你正在浪费 Claude Code 90% 的能力——而你甚至不知道自己错过了什么。

---

## Claude How To 如何解决这个问题

这不是另一份功能参考手册。这是一份**有结构、可视化、以示例驱动的指南**，通过你今天就能复制到项目中的真实模板，教你使用 Claude Code 的每一项功能。

| | 官方文档 | 本指南 |
|--|---------------|------------|
| **形式** | 参考文档 | 含 Mermaid 图表的可视化教程 |
| **深度** | 功能描述 | 底层工作原理 |
| **示例** | 基础代码片段 | 可立即使用的生产级模板 |
| **结构** | 按功能组织 | 渐进式学习路径（从入门到进阶） |
| **引导** | 自主探索 | 附时间估算的引导路线图 |
| **自我评估** | 无 | 交互式测验，找出你的知识盲区并制定个性化路径 |

### 你将获得：

- **10 个教程模块**，覆盖 Claude Code 的每项功能——从 slash commands 到自定义智能体团队
- **可直接复制的配置**——slash commands、CLAUDE.md 模板、hook 脚本、MCP 配置、subagent 定义和完整插件包
- **Mermaid 图表**，展示每个功能的内部工作原理，让你理解*为什么*，而不只是*如何做*
- **有引导的学习路径**，11-13 小时带你从入门到高级用户
- **内置自我评估**——在 Claude Code 中直接运行 `/self-assessment` 或 `/lesson-quiz hooks` 来发现知识盲区

**[开始学习路径 ->](LEARNING-ROADMAP.md)**

---

## 工作原理

### 1. 找到你的级别

完成[自我评估测验](LEARNING-ROADMAP.md#-find-your-level)，或在 Claude Code 中运行 `/self-assessment`。根据你已有的知识，获取个性化路线图。

### 2. 按引导路径学习

按顺序学习 10 个模块——每个模块都在上一个的基础上递进。学习过程中直接将模板复制到你的项目中。

### 3. 将功能组合成工作流

真正的威力在于功能的组合。学会将 slash commands + memory + subagents + hooks 串联成自动化流水线，处理代码审查、部署和文档生成。

### 4. 检验你的理解

每个模块结束后运行 `/lesson-quiz [topic]`。测验会精准定位你遗漏的内容，让你快速补齐知识盲区。

**[15 分钟快速上手](#-15-分钟快速上手)**

---

## 受到 5,900+ 开发者信赖

- **5,900+ GitHub stars**，来自每天使用 Claude Code 的开发者
- **690+ forks**——团队正在基于本指南定制自己的工作流
- **持续维护**——与每次 Claude Code 发布同步更新（最新版：v2.2.0，2026 年 3 月）
- **社区驱动**——由分享真实配置的开发者共同贡献

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不知道从哪里开始？

完成自我评估，或按级别选择：

| 级别 | 你能做到... | 从这里开始 | 时间 |
|-------|-----------|------------|------|
| **入门** | 启动 Claude Code 并对话 | [Slash Commands](01-slash-commands/) | 约 2.5 小时 |
| **中级** | 使用 CLAUDE.md 和自定义命令 | [Skills](03-skills/) | 约 3.5 小时 |
| **高级** | 配置 MCP 服务器和 hooks | [高级功能](09-advanced-features/) | 约 5 小时 |

**包含全部 10 个模块的完整学习路径：**

| 顺序 | 模块 | 级别 | 时间 |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/) | 入门 | 30 分钟 |
| 2 | [Memory](02-memory/) | 入门+ | 45 分钟 |
| 3 | [Checkpoints](08-checkpoints/) | 中级 | 45 分钟 |
| 4 | [CLI 基础](10-cli/) | 入门+ | 30 分钟 |
| 5 | [Skills](03-skills/) | 中级 | 1 小时 |
| 6 | [Hooks](06-hooks/) | 中级 | 1 小时 |
| 7 | [MCP](05-mcp/) | 中级+ | 1 小时 |
| 8 | [Subagents](04-subagents/) | 中级+ | 1.5 小时 |
| 9 | [高级功能](09-advanced-features/) | 高级 | 2-3 小时 |
| 10 | [Plugins](07-plugins/) | 高级 | 2 小时 |

**[完整学习路线图 ->](LEARNING-ROADMAP.md)**

---

## 15 分钟快速上手

```bash
# 1. 克隆本指南
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 复制你的第一个 slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 试用——在 Claude Code 中输入：
# /optimize

# 4. 想要更多？设置项目记忆：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安装一个 skill：
cp -r 03-skills/code-review ~/.claude/skills/
```

想要完整设置？以下是 **1 小时核心配置**：

```bash
# Slash commands（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 项目记忆（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安装 skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 周末目标：添加 hooks、subagents、MCP 和 plugins
# 按学习路径进行引导式配置
```

**[查看完整安装参考](#安装快速参考)**

---

## 你能用它构建什么？

| 使用场景 | 你将组合的功能 |
|----------|------------------------|
| **自动化代码审查** | Slash Commands + Subagents + Memory + MCP |
| **团队入职引导** | Memory + Slash Commands + Plugins |
| **CI/CD 自动化** | CLI Reference + Hooks + Background Tasks |
| **文档生成** | Skills + Subagents + Plugins |
| **安全审计** | Subagents + Skills + Hooks（只读模式） |
| **DevOps 流水线** | Plugins + MCP + Hooks + Background Tasks |
| **复杂重构** | Checkpoints + Planning Mode + Hooks |

---

## 常见问题

**这是免费的吗？**
是的。MIT 许可证，永久免费。可用于个人项目、工作或团队——唯一要求是保留许可证声明。

**是否持续维护？**
持续维护。本指南与每次 Claude Code 发布同步更新。当前版本：v2.2.0（2026 年 3 月），兼容 Claude Code 2.1+。

**这与官方文档有什么不同？**
官方文档是功能参考手册。本指南是带有图表、生产级模板和渐进式学习路径的教程。两者互为补充——先用本指南学习，需要具体细节时再查阅官方文档。

**全部学完需要多长时间？**
完整路径需要 11-13 小时。但 15 分钟内你就能获得实际价值——只需复制一个 slash command 模板并试用即可。

**可以搭配 Claude Sonnet / Haiku / Opus 使用吗？**
可以。所有模板均适用于 Claude Sonnet 4.6、Claude Opus 4.6 和 Claude Haiku 4.5。

**可以贡献内容吗？**
当然。请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南。我们欢迎新示例、bug 修复、文档改进和社区模板。

**可以离线阅读吗？**
可以。运行 `uv run scripts/build_epub.py` 可生成包含所有内容和渲染后图表的 EPUB 电子书。

---

## 今天就开始掌握 Claude Code

你已经安装了 Claude Code。横亘在你与 10 倍生产力之间的，只是如何使用它的知识。本指南为你提供了有结构的路径、可视化的讲解，以及可直接复制的模板。

MIT 许可证。永久免费。克隆它，fork 它，让它成为你自己的。

**[开始学习路径 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15 分钟快速上手](#-15-分钟快速上手)**

---

<details>
<summary>快速导航——所有功能</summary>

| 功能 | 说明 | 目录 |
|---------|-------------|--------|
| **功能目录** | 包含安装命令的完整参考 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 用户调用的快捷方式 | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 跨会话的持久上下文 | [02-memory/](02-memory/) |
| **Skills** | 可复用的能力 | [03-skills/](03-skills/) |
| **Subagents** | 专项 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP Protocol** | 外部工具访问 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驱动的自动化 | [06-hooks/](06-hooks/) |
| **Plugins** | 打包功能集合 | [07-plugins/](07-plugins/) |
| **Checkpoints** | 会话快照与回退 | [08-checkpoints/](08-checkpoints/) |
| **高级功能** | 规划、思考、后台任务 | [09-advanced-features/](09-advanced-features/) |
| **CLI 参考** | 命令、标志和选项 | [10-cli/](10-cli/) |
| **博客文章** | 真实使用案例 | [博客文章](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 调用方式 | 持久性 | 最适合 |
|---------|-----------|------------|----------|
| **Slash Commands** | 手动（`/cmd`） | 仅限当前会话 | 快捷操作 |
| **Memory** | 自动加载 | 跨会话 | 长期学习积累 |
| **Skills** | 自动调用 | 文件系统 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务分发 |
| **MCP Protocol** | 自动查询 | 实时 | 实时数据访问 |
| **Hooks** | 事件触发 | 已配置 | 自动化与验证 |
| **Plugins** | 一条命令 | 所有功能 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 基于会话 | 安全实验 |
| **Planning Mode** | 手动/自动 | 规划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务持续期间 | 长时间运行的操作 |
| **CLI Reference** | 终端命令 | 会话/脚本 | 自动化与脚本编写 |

</details>

<details>
<summary>安装快速参考</summary>

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

# Checkpoints（自动启用，在设置中配置）
# 参见 08-checkpoints/README.md

# 高级功能（在设置中配置）
# 参见 09-advanced-features/config-examples.json

# CLI 参考（无需安装）
# 参见 10-cli/README.md 中的使用示例
```

</details>

<details>
<summary>01. Slash Commands（斜杠命令）</summary>

**位置**：[01-slash-commands/](01-slash-commands/)

**说明**：以 Markdown 文件形式存储的用户调用快捷方式

**示例**：
- `optimize.md` - 代码优化分析
- `pr.md` - Pull request 准备
- `generate-api-docs.md` - API 文档生成器

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

**了解更多**：[Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory（记忆）</summary>

**位置**：[02-memory/](02-memory/)

**说明**：跨会话的持久上下文

**示例**：
- `project-CLAUDE.md` - 全团队项目规范
- `directory-api-CLAUDE.md` - 目录级规则
- `personal-CLAUDE.md` - 个人偏好设置

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
<summary>03. Skills（技能）</summary>

**位置**：[03-skills/](03-skills/)

**说明**：可复用、自动调用的能力，包含指令和脚本

**示例**：
- `code-review/` - 带脚本的全面代码审查
- `brand-voice/` - 品牌语调一致性检查器
- `doc-generator/` - API 文档生成器

**安装**：
```bash
# 个人技能
cp -r 03-skills/code-review ~/.claude/skills/

# 项目技能
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使用**：在相关场景下自动调用

</details>

<details>
<summary>04. Subagents（子智能体）</summary>

**位置**：[04-subagents/](04-subagents/)

**说明**：具有隔离上下文和自定义提示词的专项 AI 助手

**示例**：
- `code-reviewer.md` - 全面的代码质量分析
- `test-engineer.md` - 测试策略与覆盖率
- `documentation-writer.md` - 技术文档编写
- `secure-reviewer.md` - 以安全为重点的审查（只读）
- `implementation-agent.md` - 完整功能实现

**安装**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用**：由主智能体自动委派

</details>

<details>
<summary>05. MCP Protocol（MCP 协议）</summary>

**位置**：[05-mcp/](05-mcp/)

**说明**：用于访问外部工具和 API 的模型上下文协议

**示例**：
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件操作
- `multi-mcp.json` - 多 MCP 服务器

**安装**：
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP 服务器
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动添加到项目 .mcp.json（参见 05-mcp/ 中的示例）
```

**使用**：配置完成后，MCP 工具可自动供 Claude 使用

</details>

<details>
<summary>06. Hooks（钩子）</summary>

**位置**：[06-hooks/](06-hooks/)

**说明**：在响应 Claude Code 事件时自动执行的事件驱动 shell 命令

**示例**：
- `format-code.sh` - 写入前自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 扫描安全问题
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 验证用户提示词
- `notify-team.sh` - 在事件发生时发送通知

**安装**：
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

**使用**：Hooks 在事件发生时自动执行

**Hook 类型**（4 种类型，25 个事件）：
- **工具 Hooks**：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`PermissionRequest`
- **会话 Hooks**：`SessionStart`、`SessionEnd`、`Stop`、`StopFailure`、`SubagentStart`、`SubagentStop`
- **任务 Hooks**：`UserPromptSubmit`、`TaskCompleted`、`TaskCreated`、`TeammateIdle`
- **生命周期 Hooks**：`ConfigChange`、`CwdChanged`、`FileChanged`、`PreCompact`、`PostCompact`、`WorktreeCreate`、`WorktreeRemove`、`Notification`、`InstructionsLoaded`、`Elicitation`、`ElicitationResult`

</details>

<details>
<summary>07. Plugins（插件）</summary>

**位置**：[07-plugins/](07-plugins/)

**说明**：命令、智能体、MCP 和 hooks 的打包集合

**示例**：
- `pr-review/` - 完整的 PR 审查工作流
- `devops-automation/` - 部署与监控
- `documentation/` - 文档生成

**安装**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使用**：使用打包的 slash commands 和相关功能

</details>

<details>
<summary>08. Checkpoints and Rewind（检查点与回退）</summary>

**位置**：[08-checkpoints/](08-checkpoints/)

**说明**：保存对话状态并回退到之前的节点，以探索不同的实现思路

**核心概念**：
- **Checkpoint（检查点）**：对话状态的快照
- **Rewind（回退）**：返回到之前的检查点
- **Branch Point（分支点）**：从同一检查点探索多种方案

**使用**：
```
# 每次用户提示时会自动创建检查点
# 如需回退，按两次 Esc 或使用：
/rewind

# 然后从五个选项中选择：
# 1. 恢复代码和对话
# 2. 恢复对话
# 3. 恢复代码
# 4. 从此处摘要
# 5. 取消
```

**使用场景**：
- 尝试不同的实现方案
- 从错误中恢复
- 安全实验
- 对比备选方案
- 不同设计的 A/B 测试

</details>

<details>
<summary>09. Advanced Features（高级功能）</summary>

**位置**：[09-advanced-features/](09-advanced-features/)

**说明**：用于复杂工作流和自动化的高级能力

**包含**：
- **Planning Mode（规划模式）** — 编码前创建详细的实现计划
- **Extended Thinking（深度思考）** — 针对复杂问题的深度推理（通过 `Alt+T` / `Option+T` 切换）
- **Background Tasks（后台任务）** — 在不阻塞主线程的情况下运行长时间操作
- **Permission Modes（权限模式）** — `default`、`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions`
- **Headless Mode（无头模式）** — 在 CI/CD 中运行 Claude Code：`claude -p "Run tests and generate report"`
- **Session Management（会话管理）** — `/resume`、`/rename`、`/fork`、`claude -c`、`claude -r`
- **Configuration（配置）** — 在 `~/.claude/settings.json` 中自定义行为

完整配置示例请参见 [config-examples.json](09-advanced-features/config-examples.json)。

</details>

<details>
<summary>10. CLI Reference（CLI 参考）</summary>

**位置**：[10-cli/](10-cli/)

**说明**：Claude Code 的完整命令行界面参考

**快速示例**：
```bash
# 交互模式
claude "explain this project"

# 打印模式（非交互式）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# 为脚本输出 JSON
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**使用场景**：CI/CD 流水线集成、脚本自动化、批量处理、多会话工作流、自定义智能体配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码审查工作流

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

用户：/review-pr

Claude：
1. 加载项目记忆（编码规范）
2. 通过 GitHub MCP 获取 PR
3. 委派给 code-reviewer subagent
4. 委派给 test-engineer subagent
5. 综合分析结果
6. 提供全面的审查报告
```

### 自动化文档生成

```markdown
# 使用：Skills + Subagents + Memory

用户："Generate API documentation for the auth module"

Claude：
1. 加载项目记忆（文档规范）
2. 检测到文档生成请求
3. 自动调用 doc-generator skill
4. 委派给 api-documenter subagent
5. 创建带示例的完整文档
```

### DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

用户：/deploy production

Claude：
1. 运行部署前 hook（验证环境）
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
- 从 slash commands 开始，循序渐进
- 逐步添加功能
- 用 memory 管理团队规范
- 先在本地测试配置
- 记录自定义实现
- 对项目配置进行版本控制
- 与团队共享 plugins

### 不应该做的
- 不要创建冗余功能
- 不要硬编码凭据
- 不要跳过文档
- 不要将简单任务复杂化
- 不要忽视安全最佳实践
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
1. 验证环境变量
2. 检查 MCP 服务器安装
3. 测试凭据
4. 检查网络连通性

### Subagent 未委派
1. 检查工具权限
2. 验证智能体描述的清晰度
3. 检查任务复杂度
4. 独立测试智能体

</details>

<details>
<summary>测试</summary>

本项目包含完善的自动化测试：

- **单元测试**：使用 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**：使用 Ruff 进行代码检查和格式化
- **安全**：使用 Bandit 进行漏洞扫描
- **类型检查**：使用 mypy 进行静态类型分析
- **构建验证**：EPUB 生成测试
- **覆盖率追踪**：Codecov 集成

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行所有单元测试
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

每次向 `main`/`develop` 推送以及每个面向 `main` 的 PR 都会自动运行测试。详细信息请参见 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读本指南？生成一本 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

此命令会生成 `claude-howto-guide.epub`，包含所有内容以及渲染后的 Mermaid 图表。

更多选项请参见 [scripts/README.md](scripts/README.md)。

</details>

<details>
<summary>贡献</summary>

发现了问题，或想贡献示例？我们非常欢迎你的帮助！

**请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解以下详细指南：**
- 贡献类型（示例、文档、功能、bug、反馈）
- 如何搭建开发环境
- 目录结构以及如何添加内容
- 写作规范和最佳实践
- 提交（commit）和 PR 流程

**我们的社区准则：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我们如何相互对待
- [SECURITY.md](SECURITY.md) - 安全策略与漏洞报告

### 报告安全问题

如果你发现了安全漏洞，请负责任地报告：

1. **使用 GitHub 私有漏洞报告**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **请勿**针对安全漏洞开启公开 issue

快速开始：
1. Fork 并克隆仓库
2. 创建描述性分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按指南进行修改
4. 提交带有清晰描述的 pull request

**需要帮助？** 开一个 issue 或讨论，我们会引导你完成整个流程。

</details>

<details>
<summary>其他资源</summary>

- [Claude Code 官方文档](https://code.claude.com/docs/en/overview)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [Skills 仓库](https://github.com/luongnv89/skills) - 即用型 skills 合集
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny 的 Claude Code 工作流](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的创造者分享了他系统化的工作流：并行智能体、共享 CLAUDE.md、Plan 模式、slash commands、subagents 以及用于长时间自主会话的验证 hooks。

</details>

---

## 贡献

我们欢迎贡献！请参阅我们的[贡献指南](CONTRIBUTING.md)了解如何开始。

## 贡献者

感谢所有为本项目做出贡献的人！

| 贡献者 | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 许可证

MIT 许可证 - 参见 [LICENSE](LICENSE)。可自由使用、修改和分发。唯一的要求是保留许可证声明。

---

**最后更新**：2026 年 3 月
**Claude Code 版本**：2.1+
**兼容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
