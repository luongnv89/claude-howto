# 更新日志

## v2.2.0 — 2026-03-26

### 文档

- 将所有教程和参考文档同步至 Claude Code v2.1.84（f78c094）@luongnv89
  - 将 slash commands 更新为 55+ 个内置命令 + 5 个内置技能，标记 3 个已废弃命令
  - 钩子事件从 18 个扩展至 25 个，新增 `agent` 钩子类型（现共 4 种类型）
  - 在进阶功能中新增 Auto Mode、Channels、Voice Dictation
  - 新增技能 frontmatter 字段 `effort`、`shell`；智能体字段 `initialPrompt`、`disallowedTools`
  - 新增 WebSocket MCP 传输、elicitation、2KB 工具上限说明
  - 新增插件 LSP 支持、`userConfig`、`${CLAUDE_PLUGIN_DATA}`
  - 更新所有参考文档（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）
- 将 README 重写为落地页结构化指南（32a0776）@luongnv89

### Bug 修复

- 补充 cSpell 词库并完善 README 章节以通过 CI 检查（93f9d51）@luongnv89
- 将 `Sandboxing` 加入 cSpell 词库（b80ce6f）@luongnv89

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug 修复

- 移除导致 CI 链接检查失败的无效 marketplace 链接（3fdf0d6）@luongnv89
- 将 `sandboxed` 和 `pycache` 加入 cSpell 词库（dc64618）@luongnv89

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 新功能

- 新增自适应学习路径，包含自我评估和课后测验技能（1ef46cd）@luongnv89
  - `/self-assessment` — 涵盖 10 个功能领域的交互式水平测验，并生成个性化学习路径
  - `/lesson-quiz [lesson]` — 针对单个课时的知识检验，包含 8-10 道定向问题

### Bug 修复

- 修复失效 URL、已废弃内容和过时引用（8fe4520）@luongnv89
- 修复资源目录和自我评估技能中的失效链接（7a05863）@luongnv89
- 在概念指南的嵌套代码块中使用波浪线围栏（5f82719）@VikalpP
- 补充 cSpell 词库中缺失的单词（8df7572）@luongnv89

### 文档

- 第五阶段 QA——修复文档中的一致性、URL 和术语问题（00bbe4c）@luongnv89
- 完成第三、四阶段——新功能覆盖与参考文档更新（132de29）@luongnv89
- 在 MCP 上下文膨胀章节中新增 MCPorter 运行时说明（ef52705）@luongnv89
- 在 6 份指南中补充缺失的命令、功能和设置项（4bc8f15）@luongnv89
- 基于现有仓库规范新增风格指南（84141d0）@luongnv89
- 在指南对比表中新增自我评估行（8fe0c96）@luongnv89
- 将 VikalpP 添加至贡献者列表（PR #7）（d5b4350）@luongnv89
- 在 README 和路线图中新增自我评估与课后测验技能的引用（d5a6106）@luongnv89

### 新贡献者

- @VikalpP 在 #7 中完成了他们的首次贡献

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 新功能

- 将所有文档同步至 Claude Code 2026 年 2 月版本功能（487c96d）
  - 更新了 10 个教程目录和 7 份参考文档中的共 26 个文件
  - 新增 **Auto Memory** 文档——每个项目的持久化学习记录
  - 新增 **Remote Control**、**Web Sessions** 和 **Desktop App** 文档
  - 新增 **Agent Teams** 文档（实验性多智能体协作功能）
  - 新增 **MCP OAuth 2.0**、**Tool Search** 和 **Claude.ai Connectors** 文档
  - 新增 **Persistent Memory** 和子智能体 **Worktree Isolation** 文档
  - 新增 **Background Subagents**、**Task List**、**Prompt Suggestions** 文档
  - 新增 **Sandboxing** 和 **Managed Settings**（企业版）文档
  - 新增 **HTTP Hooks** 和 7 个新钩子事件文档
  - 新增 **Plugin Settings**、**LSP Servers** 和 Marketplace 更新文档
  - 新增 **Summarize from Checkpoint** 回退选项文档
  - 记录 17 个新 slash commands（`/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` 等）
  - 记录新的 CLI 参数（`--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` 等）
  - 记录用于自动记忆、能力等级、智能体团队等功能的新环境变量

### 设计

- 将 Logo 重新设计为带有极简色彩的指南针括号标志（20779db）

### Bug 修复 / 内容纠正

- 更新模型名称：Sonnet 4.5 → **Sonnet 4.6**，Opus 4.5 → **Opus 4.6**
- 修正权限模式名称：将虚构的"Unrestricted/Confirm/Read-only"替换为实际的 `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`
- 修正钩子事件：移除虚构的 `PreCommit`/`PostCommit`/`PrePush`，补充真实事件（`SubagentStart`、`WorktreeCreate`、`ConfigChange` 等）
- 修正 CLI 语法：将 `claude-code --headless` 替换为 `claude -p`（打印模式）
- 修正检查点命令：将虚构的 `/checkpoint save/list/rewind/diff` 替换为实际的 `Esc+Esc` / `/rewind` 界面
- 修正会话管理：将虚构的 `/session list/new/switch/save` 替换为真实的 `/resume`/`/rename`/`/fork`
- 修正插件清单格式：迁移 `plugin.yaml` → `.claude-plugin/plugin.json`
- 修正 MCP 配置路径：`~/.claude/mcp.json` → `.mcp.json`（项目级）/ `~/.claude.json`（用户级）
- 修正文档 URL：`docs.claude.com` → `docs.anthropic.com`；移除虚构的 `plugins.claude.com`
- 移除多个文件中的虚构配置字段
- 将所有"最后更新"日期更新为 2026 年 2 月

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
