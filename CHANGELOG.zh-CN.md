# 更新日志（Changelog）

## v2.2.0 — 2026-03-26

### Documentation

- 将所有教程与参考文档同步到 Claude Code v2.1.84（f78c094）@luongnv89
  - 更新 slash commands：55+ 内置命令 + 5 个 bundled skills，并标注 3 个已弃用项
  - Hook 事件从 18 扩展到 25，新增 `agent` hook 类型（现共 4 种类型）
  - 在高级特性中新增 Auto Mode、Channels、Voice Dictation
  - 新增 skill frontmatter 字段：`effort`、`shell`；新增 agent 字段：`initialPrompt`、`disallowedTools`
  - 新增 WebSocket MCP transport、elicitation、2KB 工具上限说明
  - 新增 plugin LSP 支持、`userConfig`、`${CLAUDE_PLUGIN_DATA}`
  - 更新所有参考文档（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）
- 将 README 重写为落地页式结构指南（32a0776）@luongnv89

### Bug Fixes

- 新增缺失的 cSpell 词条并补充 README 章节以满足 CI 合规检查（93f9d51）@luongnv89
- 在 cSpell 字典中新增 `Sandboxing`（b80ce6f）@luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug Fixes

- 移除失效的 marketplace 链接，修复 CI 链接检查失败（3fdf0d6）@luongnv89
- 在 cSpell 字典中新增 `sandboxed` 和 `pycache`（dc64618）@luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Features

- 新增自适应学习路径，包含 self-assessment 与 lesson quiz skills（1ef46cd）@luongnv89
  - `/self-assessment`：覆盖 10 个能力维度的交互式熟练度测评，并生成个性化学习路径
  - `/lesson-quiz [lesson]`：按课程进行知识检查，包含 8-10 个针对性问题

### Bug Fixes

- 更新失效 URL、弃用项与过时引用（8fe4520）@luongnv89
- 修复 resources 与 self-assessment skill 中的坏链（7a05863）@luongnv89
- 在 concepts guide 中将嵌套代码块改用 tilde fence（5f82719）@VikalpP
- 在 cSpell 字典中补充缺失词条（8df7572）@luongnv89

### Documentation

- Phase 5 QA：修复文档中的一致性、URL 与术语问题（00bbe4c）@luongnv89
- 完成 Phases 3-4：补充新特性覆盖与参考文档更新（132de29）@luongnv89
- 在 MCP 上下文膨胀章节中新增 MCPorter runtime（ef52705）@luongnv89
- 在 6 份指南中补充缺失命令、特性与设置项（4bc8f15）@luongnv89
- 基于仓库既有约定新增 style guide（84141d0）@luongnv89
- 在指南对比表中新增 self-assessment 行（8fe0c96）@luongnv89
- 在贡献者列表中新增 VikalpP（PR #7）（d5b4350）@luongnv89
- 在 README 与 roadmap 中新增 self-assessment 和 lesson-quiz skill 引用（d5a6106）@luongnv89

### New Contributors

- @VikalpP 在 #7 中完成首次贡献

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Features

- 将全部文档同步到 Claude Code 2026 年 2 月特性（487c96d）
  - 更新 10 个教程目录与 7 份参考文档中的 26 个文件
  - 新增 **Auto Memory** 文档（按项目持久学习）
  - 新增 **Remote Control**、**Web Sessions**、**Desktop App** 文档
  - 新增 **Agent Teams** 文档（实验性多代理协作）
  - 新增 **MCP OAuth 2.0**、**Tool Search**、**Claude.ai Connectors** 文档
  - 新增 subagents 的 **Persistent Memory** 与 **Worktree Isolation** 文档
  - 新增 **Background Subagents**、**Task List**、**Prompt Suggestions** 文档
  - 新增 **Sandboxing** 与 **Managed Settings**（企业版）文档
  - 新增 **HTTP Hooks** 与 7 个新 hook 事件文档
  - 新增 **Plugin Settings**、**LSP Servers** 与 Marketplace 更新文档
  - 新增 **Summarize from Checkpoint** 回退选项文档
  - 文档化 17 个新 slash commands（如 `/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` 等）
  - 文档化新 CLI 参数（如 `--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` 等）
  - 文档化 auto memory、effort levels、agent teams 等相关新环境变量

### Design

- 将 logo 重设计为罗盘括号风格，采用极简配色（20779db）

### Bug Fixes / Corrections

- 更新模型名称：Sonnet 4.5 → **Sonnet 4.6**，Opus 4.5 → **Opus 4.6**
- 修正权限模式名：将虚构的 “Unrestricted/Confirm/Read-only” 替换为真实 `default` / `acceptEdits` / `plan` / `dontAsk` / `bypassPermissions`
- 修正 hook 事件：移除虚构的 `PreCommit` / `PostCommit` / `PrePush`，补充真实事件（`SubagentStart`、`WorktreeCreate`、`ConfigChange` 等）
- 修正 CLI 语法：将 `claude-code --headless` 替换为 `claude -p`（print mode）
- 修正 checkpoint 命令：将虚构的 `/checkpoint save/list/rewind/diff` 替换为真实 `Esc+Esc` / `/rewind` 界面
- 修正会话管理：将虚构的 `/session list/new/switch/save` 替换为真实 `/resume` / `/rename` / `/fork`
- 修正 plugin manifest 格式：迁移 `plugin.yaml` → `.claude-plugin/plugin.json`
- 修正 MCP 配置路径：`~/.claude/mcp.json` → `.mcp.json`（项目）/ `~/.claude.json`（用户）
- 修正文档 URL：`docs.claude.com` → `docs.anthropic.com`；移除虚构 `plugins.claude.com`
- 清理多个文件中的虚构配置字段
- 将所有 “Last Updated” 日期更新至 2026 年 2 月

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
