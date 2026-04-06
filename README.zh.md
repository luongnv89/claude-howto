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

> 🌐 [English Version](README.md)

> 📚 **关于本指南**
> 
> 本指南是关于 **Claude Code** 的学习资源。
> 
> 由于 **Kimi Code** 与 Claude Code 具有相似的架构，我们附带了 **Kimi Code 适配说明**，方便使用 Kimi Code 的开发者参考。
> 
> - **核心内容**：学习 Claude Code 的功能和使用方法
> - **Kimi Code 适配**：在相关章节附带 Kimi Code 的对应命令和配置
> - **原始仓库**：[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)

---

## Claude Code ↔ Kimi Code 快速对照

| Claude Code | Kimi Code | 说明 |
|-------------|-----------|------|
| `claude` 命令 | `kimi` 命令 | CLI 命令 |
| `.claude/` 目录 | `.kimi/` 目录 | 配置目录 |
| `CLAUDE.md` | `KIMI.md` | 项目内存文件 |
| `~/.claude/` | `~/.kimi/` | 用户配置目录 |
| `@anthropic-ai/claude-code` | `@moonshot-ai/kimi-code` | npm 包名 |
| `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` | API 密钥环境变量 |

---

# 一个周末精通 Claude Code

从输入 `claude` 开始，到编排智能体、钩子、技能和 MCP 服务器——通过可视化教程、复制粘贴模板和引导式学习路径。

**[15分钟快速开始](#15分钟快速开始)** | **[不知道从哪里开始？](#不知道从哪里开始)** | **[浏览功能目录](CATALOG.md)**

---

## 目录

- [问题所在](#问题所在)
- [本指南如何解决](#本指南如何解决)
- [工作原理](#工作原理)
- [不知道从哪里开始？](#不知道从哪里开始)
- [15分钟快速开始](#15分钟快速开始)
- [你能用这些构建什么？](#你能用这些构建什么)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 问题所在

你安装了 Claude Code。运行了几个提示词。然后呢？

- **官方文档描述功能——但不展示如何组合使用。** 你知道斜杠命令存在，但不知道如何将它们与钩子、内存和子代理链接成一个能真正节省数小时的工作流程。
- **没有明确的学习路径。** 应该先学 MCP 还是钩子？技能还是子代理？你最终什么都浏览了一遍，什么都没掌握。
- **示例太基础。** 一个 "hello world" 斜杠命令无法帮助你构建一个使用内存、委派给专业代理并自动运行安全扫描的生产级代码审查管道。

你只使用了 Claude Code 10% 的功能——而且你不知道自己不知道什么。

---

## 本指南如何解决

这不是另一个功能参考。它是一个**结构化的、可视化的、案例驱动的指南**，教你使用每个 Claude Code 功能，并提供可以今天复制到项目中的真实模板。

| | 官方文档 | 本指南 |
|--|----------|--------|
| **格式** | 参考文档 | 带有 Mermaid 图表的可视化教程 |
| **深度** | 功能描述 | 底层工作原理 |
| **示例** | 基础代码片段 | 可立即使用的生产级模板 |
| **结构** | 按功能组织 | 渐进式学习路径（初级到高级） |
| **入门** | 自主学习 | 带时间估计的引导式路线图 |
| **自我评估** | 无 | 互动测验，找出差距并建立个性化路径 |

### 你将获得：

- **10个教程模块**，涵盖每个 Claude Code 功能——从斜杠命令到自定义代理团队
- **复制粘贴配置**——斜杠命令、CLAUDE.md 模板、钩子脚本、MCP 配置、子代理定义和完整插件包
- **Mermaid 图表**，展示每个功能的内部工作原理，让你理解*为什么*，而不只是*怎么做*
- **引导式学习路径**，带你从初学者到高级用户，耗时 11-13 小时
- **内置自我评估**——在 Claude Code 中直接运行 `/self-assessment` 或 `/lesson-quiz hooks` 来识别差距

**[开始学习路径 ->](LEARNING-ROADMAP.md)**

> 💡 **Kimi Code 用户注意**：以上功能在 Kimi Code 中有对应实现，具体命令和路径差异参见各模块的"Kimi Code 适配"部分。

---

## 工作原理

### 1. 找到你的水平

参加[自我评估测验](LEARNING-ROADMAP.md#-找到你的水平)或在 Claude Code 中运行 `/self-assessment`。根据你已知的知识获得个性化路线图。

### 2. 遵循引导路径

按顺序学习 10 个模块——每个都建立在上一个之上。学习时直接将模板复制到你的项目中。

### 3. 将功能组合成工作流

真正的力量在于组合功能。学习如何将斜杠命令 + 内存 + 子代理 + 钩子连接成自动化管道，处理代码审查、部署和文档生成。

### 4. 测试你的理解

每个模块后运行 `/lesson-quiz [主题]`。测验精确定位你遗漏的内容，让你快速填补空白。

**[15分钟快速开始](#15分钟快速开始)**

---

## 受 5,900+ 开发者信赖

- **5,900+ GitHub stars**，来自日常使用 Claude Code 的开发者
- **690+ forks**——团队将此指南调整用于自己的工作流程
- **积极维护**——与每次 Claude Code 发布同步（最新：v2.2.0，2026年3月）
- **社区驱动**——来自分享真实世界配置的开发者贡献

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不知道从哪里开始？

参加自我评估或选择你的水平：

| 水平 | 你会... | 从这里开始 | 时间 |
|------|---------|-----------|------|
| **初学者** | 启动 Claude Code 并聊天 | [斜杠命令](01-slash-commands/) | ~2.5 小时 |
| **中级** | 使用 CLAUDE.md 和自定义命令 | [技能](03-skills/) | ~3.5 小时 |
| **高级** | 配置 MCP 服务器和钩子 | [高级功能](09-advanced-features/) | ~5 小时 |

**包含全部 10 个模块的完整学习路径：**

| 顺序 | 模块 | 水平 | 时间 |
|------|------|------|------|
| 1 | [斜杠命令](01-slash-commands/) | 初级 | 30 分钟 |
| 2 | [内存](02-memory/) | 初级+ | 45 分钟 |
| 3 | [检查点](08-checkpoints/) | 中级 | 45 分钟 |
| 4 | [CLI 基础](10-cli/) | 初级+ | 30 分钟 |
| 5 | [技能](03-skills/) | 中级 | 1 小时 |
| 6 | [钩子](06-hooks/) | 中级 | 1 小时 |
| 7 | [MCP](05-mcp/) | 中级+ | 1 小时 |
| 8 | [子代理](04-subagents/) | 中级+ | 1.5 小时 |
| 9 | [高级功能](09-advanced-features/) | 高级 | 2-3 小时 |
| 10 | [插件](07-plugins/) | 高级 | 2 小时 |

**[完整学习路线图 ->](LEARNING-ROADMAP.md)**

---

## 15分钟快速开始

```bash
# 1. 克隆本指南
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 复制你的第一个斜杠命令
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 试试——在 Claude Code 中输入：
# /optimize

# 4. 想要更多？设置项目内存：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安装一个技能：
cp -r 03-skills/code-review ~/.claude/skills/
```

> 💡 **Kimi Code 适配**：
> ```bash
> # 对应的 Kimi Code 命令：
> mkdir -p /path/to/your-project/.kimi/commands
> cp 01-slash-commands/optimize.md /path/to/your-project/.kimi/commands/
> cp 02-memory/project-CLAUDE.md /path/to/your-project/KIMI.md
> cp -r 03-skills/code-review ~/.kimi/skills/
> ```

想要完整设置？这里是**1小时基础设置**：

```bash
# 斜杠命令 (15 分钟)
cp 01-slash-commands/*.md .claude/commands/

# 项目内存 (15 分钟)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安装一个技能 (15 分钟)
cp -r 03-skills/code-review ~/.claude/skills/

# 周末目标：添加钩子、子代理、MCP 和插件
# 跟随学习路径进行引导设置
```

> 💡 **Kimi Code 适配**：将 `.claude/` 替换为 `.kimi/`，`CLAUDE.md` 替换为 `KIMI.md`

**[查看完整安装参考](#15分钟快速开始)**

---

## 你能用这些构建什么？

| 用例 | 你将组合的功能 |
|------|--------------|
| **自动化代码审查** | 斜杠命令 + 子代理 + 内存 + MCP |
| **团队入职** | 内存 + 斜杠命令 + 插件 |
| **CI/CD 自动化** | CLI 参考 + 钩子 + 后台任务 |
| **文档生成** | 技能 + 子代理 + 插件 |
| **安全审计** | 子代理 + 技能 + 钩子（只读模式） |
| **DevOps 管道** | 插件 + MCP + 钩子 + 后台任务 |
| **复杂重构** | 检查点 + 规划模式 + 钩子 |

---

## 常见问题

**这是免费的吗？**
是的。MIT 许可证，永远免费。用于个人项目、工作、团队——唯一要求是包含许可证声明。

**这有维护吗？**
积极维护。指南与每次 Claude Code 发布同步。当前版本：v2.2.0（2026年3月），兼容 Claude Code 2.1+。

**这与官方文档有何不同？**
官方文档是功能参考。本指南是带有图表、生产级模板和渐进式学习路径的教程。它们互补——从这里开始学习，需要具体信息时参考官方文档。

**完成所有内容需要多长时间？**
完整路径 11-13 小时。但你将在 15 分钟内获得即时价值——只需复制一个斜杠命令模板并试用。

**我可以与 Claude Sonnet / Haiku / Opus 一起使用吗？**
是的。所有模板适用于 Claude Sonnet 4.6、Claude Opus 4.6 和 Claude Haiku 4.5。

**我可以贡献吗？**
绝对可以。查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。我们欢迎新示例、错误修复、文档改进和社区模板。

**我可以离线阅读吗？**
是的。运行 `uv run scripts/build_epub.py` 生成包含所有内容和渲染图表的 EPUB 电子书。

> 💡 **Kimi Code 用户常见问题**：
> - **Kimi Code 可以使用本指南吗？** 可以！大部分概念相同，命令和路径有对应关系
> - **Kimi Code 和 Claude Code 功能相同吗？** 架构相似，具体功能可能有所不同，请以实际产品为准

---

## 今天开始精通 Claude Code

你已经安装了 Claude Code。你和 10 倍生产力之间唯一的障碍是知道如何使用它。本指南为你提供结构化路径、可视化解释和复制粘贴模板。

MIT 许可证。永远免费。克隆它、fork 它、让它成为你的。

**[开始学习路径 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15分钟快速开始](#15分钟快速开始)**

---

<details>
<summary>快速导航——所有功能</summary>

| 功能 | 描述 | 文件夹 | Kimi Code 对应 |
|------|------|--------|----------------|
| **功能目录** | 带安装命令的完整参考 | [CATALOG.md](CATALOG.md) | - |
| **斜杠命令** | 用户调用的快捷方式 | [01-slash-commands/](01-slash-commands/) | `/` 命令 |
| **内存** | 持久化上下文 | [02-memory/](02-memory/) | `KIMI.md` |
| **技能** | 可复用能力 | [03-skills/](03-skills/) | 技能系统 |
| **子代理** | 专业 AI 助手 | [04-subagents/](04-subagents/) | 子代理 |
| **MCP 协议** | 外部工具访问 | [05-mcp/](05-mcp/) | MCP 服务器 |
| **钩子** | 事件驱动自动化 | [06-hooks/](06-hooks/) | 钩子 |
| **插件** | 捆绑功能 | [07-plugins/](07-plugins/) | 插件 |
| **检查点** | 会话快照与回退 | [08-checkpoints/](08-checkpoints/) | 检查点 |
| **高级功能** | 规划、思考、后台任务 | [09-advanced-features/](09-advanced-features/) | 高级功能 |
| **CLI 参考** | 命令、标志和选项 | [10-cli/](10-cli/) | CLI 参考 |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 调用方式 | 持久化 | 最适合 |
|------|---------|--------|--------|
| **斜杠命令** | 手动 (`/cmd`) | 仅会话 | 快速快捷方式 |
| **内存** | 自动加载 | 跨会话 | 长期学习 |
| **技能** | 自动调用 | 文件系统 | 自动化工作流 |
| **子代理** | 自动委派 | 隔离上下文 | 任务分发 |
| **MCP 协议** | 自动查询 | 实时 | 实时数据访问 |
| **钩子** | 事件触发 | 已配置 | 自动化与验证 |
| **插件** | 一个命令 | 所有功能 | 完整解决方案 |
| **检查点** | 手动/自动 | 基于会话 | 安全实验 |
| **规划模式** | 手动/自动 | 规划阶段 | 复杂实现 |
| **后台任务** | 手动 | 任务持续时间 | 长时间运行操作 |
| **CLI 参考** | 终端命令 | 会话/脚本 | 自动化与脚本 |

</details>

<details>
<summary>Claude Code ↔ Kimi Code 完整对照表</summary>

### 命令对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `claude` | `kimi` |
| `claude -p` | `kimi -p` |
| `claude -c` | `kimi -c` |
| `claude -r` | `kimi -r` |
| `claude mcp` | `kimi mcp` |
| `claude agents` | `kimi agents` |
| `claude plugin` | `kimi plugin` |

### 路径对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `.claude/` | `.kimi/` |
| `~/.claude/` | `~/.kimi/` |
| `.claude/commands/` | `.kimi/commands/` |
| `.claude/skills/` | `.kimi/skills/` |
| `.claude/agents/` | `.kimi/agents/` |
| `.claude/hooks/` | `.kimi/hooks/` |
| `CLAUDE.md` | `KIMI.md` |
| `CLAUDE.local.md` | `KIMI.local.md` |

### 包名对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `@anthropic-ai/claude-code` | `@moonshot-ai/kimi-code` |

### 环境变量对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `ANTHROPIC_API_KEY` | `MOONSHOT_API_KEY` |
| `CLAUDE_CODE_*` | `KIMI_CODE_*` |

</details>

<details>
<summary>安装快速参考（Claude Code）</summary>

```bash
# 斜杠命令
cp 01-slash-commands/*.md .claude/commands/

# 内存
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 技能
cp -r 03-skills/code-review ~/.claude/skills/

# 子代理
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 钩子
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 插件
/plugin install pr-review

# 检查点（自动启用，在设置中配置）
# 参见 08-checkpoints/README.md

# 高级功能（在设置中配置）
# 参见 09-advanced-features/config-examples.json

# CLI 参考（无需安装）
# 参见 10-cli/README.md 了解用法示例
```

</details>

<details>
<summary>安装快速参考（Kimi Code 适配）</summary>

```bash
# 斜杠命令
cp 01-slash-commands/*.md .kimi/commands/

# 内存
cp 02-memory/project-CLAUDE.md ./KIMI.md

# 技能
cp -r 03-skills/code-review ~/.kimi/skills/

# 子代理
cp 04-subagents/*.md .kimi/agents/

# MCP
export GITHUB_TOKEN="token"
kimi mcp add github -- npx -y @modelcontextprotocol/server-github

# 钩子
mkdir -p ~/.kimi/hooks
cp 06-hooks/*.sh ~/.kimi/hooks/
chmod +x ~/.kimi/hooks/*.sh

# 插件
/plugin install pr-review
```

</details>

---

## 贡献指南

我们欢迎贡献！请查看我们的 [贡献指南](CONTRIBUTING.md) 了解如何开始。

## 贡献者

感谢所有为本项目做出贡献的人！

| 贡献者 | PRs |
|--------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - 添加创建 epub 的工具](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - 修复(docs)：在概念指南中对嵌套代码块使用波浪号围栏](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 许可证

MIT 许可证 - 参见 [LICENSE](LICENSE)。可自由使用、修改和分发。唯一要求是包含许可证声明。

---

**最后更新**: 2026年3月
**Claude Code 版本**: 2.1+
**兼容模型**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
