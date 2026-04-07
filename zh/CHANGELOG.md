# 更新日志

## v2.2.0 — 2026-03-26

### 文档

- 与 Claude Code v2.1.84（f78c094）同步更新所有教程和参考文档 @luongnv89
  - 将 slash commands 更新为 55+ 个内置命令 + 5 个 bundled skills，并标记 3 个已弃用项
  - 将 hook 事件从 18 个扩展到 25 个，新增 `agent` hook 类型（现在共 4 类）
  - 在高级功能中加入自动模式（Auto Mode）、通道（Channels）、语音输入（Voice Dictation）
  - 为 skill frontmatter 增加 `effort`、`shell` 字段；为 agent 增加 `initialPrompt`、`disallowedTools` 字段
  - 增加 WebSocket MCP transport、elicitation、2KB 工具上限
  - 增加 plugin 的 LSP 支持、`userConfig`、`${CLAUDE_PLUGIN_DATA}`
  - 更新所有参考文档（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）
- 将 README 重写为落地页结构化指南（32a0776）@luongnv89

### Bug 修复

- 为通过 CI 词典检查，补充缺失的 cSpell 词条和 README 章节（93f9d51）@luongnv89
- 在 cSpell 词典中加入 `Sandboxing`（b80ce6f）@luongnv89

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug 修复

- 移除导致 CI 链接检查失败的失效 marketplace 链接（3fdf0d6）@luongnv89
- 将 `sandboxed` 和 `pycache` 加入 cSpell 词典（dc64618）@luongnv89

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 功能

- 新增自适应学习路径，包含自我评估和 lesson quiz skills（1ef46cd）@luongnv89
  - `/self-assessment` - 覆盖 10 个功能领域的交互式能力测验，并生成个性化学习路径
  - `/lesson-quiz [lesson]` - 每课知识检查，包含 8-10 道针对性问题

### Bug 修复

- 更新失效 URL、弃用项和过时引用（8fe4520）@luongnv89
- 修复 resources 和 self-assessment skill 中的损坏链接（7a05863）@luongnv89
- 在 concepts guide 中为嵌套代码块使用 tilde fences（5f82719）@VikalpP
- 为 cSpell 词典补充缺失词汇（8df7572）@luongnv89

### 文档

- Phase 5 QA - 修复各文档中的一致性、URL 和术语问题（00bbe4c）@luongnv89
- 完成 Phase 3-4 - 补充新功能覆盖和参考文档更新（132de29）@luongnv89
- 在 MCP 上下文膨胀章节加入 MCPorter runtime（ef52705）@luongnv89
- 为 6 份指南补充缺失命令、功能和设置（4bc8f15）@luongnv89
- 基于仓库现有规范补充 style guide（84141d0）@luongnv89
- 在指南对比表中加入自我评估行（8fe0c96）@luongnv89
- 将 VikalpP 加入贡献者名单，记录 PR #7（d5b4350）@luongnv89
- 在 README 和 roadmap 中加入 self-assessment 与 lesson-quiz skill 参考（d5a6106）@luongnv89

### 新贡献者

- @VikalpP 完成了他们的首次贡献，见 #7

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 功能

- 与 Claude Code 2026 年 2 月功能同步更新全部文档（487c96d）
  - 更新所有 10 个教程目录和 7 份参考文档中的 26 个文件
  - 补充 **Auto Memory** 文档 - 每个项目的持久学习能力
  - 补充 **Remote Control**、**Web Sessions** 和 **Desktop App** 文档
  - 补充 **Agent Teams** 文档（实验性多 agent 协作）
  - 补充 **MCP OAuth 2.0**、**Tool Search** 和 **Claude.ai Connectors** 文档
  - 补充 subagents 的 **Persistent Memory** 和 **Worktree Isolation** 文档
  - 补充 **Background Subagents**、**Task List**、**Prompt Suggestions** 文档
  - 补充 **Sandboxing** 和 **Managed Settings**（Enterprise）文档
  - 补充 **HTTP Hooks** 和 7 个新 hook 事件的文档
  - 补充 **Plugin Settings**、**LSP Servers** 和 marketplace 更新文档
  - 补充 Checkpoint 的 **Summarize from Checkpoint** 回退选项文档
  - 记录 17 个新的 slash commands（`/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` 等）
  - 记录新的 CLI flags（`--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` 等）
  - 记录 auto memory、effort 等级、agent teams 等新的环境变量

### 设计

- 将 logo 重设计为简洁调色的 compass-bracket 标志（20779db）

### Bug 修复 / 修正

- 更新模型名称：Sonnet 4.5 → **Sonnet 4.6**，Opus 4.5 → **Opus 4.6**
- 修正 permission mode 名称：用真实的 `default` / `acceptEdits` / `plan` / `dontAsk` / `bypassPermissions` 替代虚构的 “Unrestricted/Confirm/Read-only”
- 修正 hook 事件：移除虚构的 `PreCommit` / `PostCommit` / `PrePush`，加入真实事件（`SubagentStart`、`WorktreeCreate`、`ConfigChange` 等）
- 修正 CLI 语法：用 `claude -p`（print mode）替代虚构的 `claude-code --headless`
- 修正 checkpoint 命令：用真实的 `Esc+Esc` / `/rewind` 界面替代虚构的 `/checkpoint save/list/rewind/diff`
- 修正 session 管理：用真实的 `/resume` / `/rename` / `/fork` 替代虚构的 `/session list/new/switch/save`
- 修正 plugin manifest 格式：从 `plugin.yaml` 迁移到 `.claude-plugin/plugin.json`
- 修正 MCP 配置路径：`~/.claude/mcp.json` → `.mcp.json`（项目）/ `~/.claude.json`（用户）
- 修正文档 URL：`docs.claude.com` → `docs.anthropic.com`；移除虚构的 `plugins.claude.com`
- 移除多个文件中虚构的配置字段
- 将所有 “Last Updated” 日期更新到 2026 年 2 月

**完整更新日志**：https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
