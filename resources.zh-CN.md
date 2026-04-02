<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 优质资源列表

## 官方文档

| Resource | Description | Link |
|----------|-------------|------|
| Claude Code Docs | Claude Code 官方文档 | [code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview) |
| Anthropic Docs | Anthropic 全量文档 | [docs.anthropic.com](https://docs.anthropic.com) |
| MCP Protocol | Model Context Protocol 规范 | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| MCP Servers | 官方 MCP server 实现 | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| Anthropic Cookbook | 代码示例与教程 | [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) |
| Claude Code Skills | 社区 skills 仓库 | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| Agent Teams | 多 agent 协作 | [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) |
| Scheduled Tasks | `/loop` 与 cron 的周期任务 | [code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) |
| Chrome Integration | 浏览器自动化 | [code.claude.com/docs/en/chrome](https://code.claude.com/docs/en/chrome) |
| Keybindings | 键位定制 | [code.claude.com/docs/en/keybindings](https://code.claude.com/docs/en/keybindings) |
| Desktop App | 原生桌面应用 | [code.claude.com/docs/en/desktop](https://code.claude.com/docs/en/desktop) |
| Remote Control | 远程会话控制 | [code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control) |
| Auto Mode | 自动权限管理 | [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) |
| Channels | 多通道通信 | [code.claude.com/docs/en/channels](https://code.claude.com/docs/en/channels) |
| Voice Dictation | 语音输入 | [code.claude.com/docs/en/voice-dictation](https://code.claude.com/docs/en/voice-dictation) |

## Anthropic Engineering Blog

| Article | Description | Link |
|---------|-------------|------|
| Code Execution with MCP | 用代码执行解决 MCP 上下文膨胀（98.7% token 降低） | [anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp) |

---

## 30 分钟掌握 Claude Code

_视频_：https://www.youtube.com/watch?v=6eBSHbLKuN0

_**核心技巧**_
- **持续关注新功能与快捷键**
  - 定期看 release notes，跟进上下文与编辑能力更新。
  - 熟悉键盘快捷键，在 chat/file/editor 视图间快速切换。

- **高效初始化**
  - 为项目会话设置清晰名称与描述，便于检索。
  - 固定最常用文件/目录，确保 Claude 随时可访问。
  - 接入 GitHub 与常用 IDE 集成，减少上下文切换成本。

- **高质量代码库问答**
  - 针对架构、模式、模块提出具体问题。
  - 在问题中引用文件与行号（如 `src/auth/AuthService.ts:45-120`）。
  - 大仓库先给摘要或 manifest，帮助 Claude 聚焦。

- **编辑与重构**
  - 使用行内注释/代码块请求做定向改写。
  - 要求 before/after 对比。
  - 大改后让 Claude 同步生成测试或文档。

- **上下文管理**
  - 只提供当前任务所需上下文。
  - 使用结构化提示（文件 A、函数 B、问题 X）。
  - 移除过大无关文件，避免超出上下文窗口。

- **团队工具整合**
  - 连接团队仓库与文档。
  - 将高频工程任务沉淀为模板。
  - 共享 session 记录与 prompts。

- **提升产出质量**
  - 给出明确目标导向指令。
  - 精简无关注释与模板噪音。
  - 输出跑偏时重置上下文或重写提问。

- **常见实战场景**
  - Debug：贴错误堆栈，询问根因与修复。
  - Test 生成：要求 property-based / unit / integration tests。
  - Code Review：识别风险改动、边界条件和 code smells。

**提示**：组合使用这些方法效果最好——先固定关键文件与目标，再用聚焦 prompts 和迭代式重构逐步推进。

---

## Claude Code 推荐工作流

### 新仓库

1. **初始化仓库与 Claude 集成**
   - 建立 README、LICENSE、.gitignore 与根配置。
   - 创建 `CLAUDE.md`，记录架构、目标、编码规范。
   - 接入 Claude Code，启用代码建议、测试脚手架与自动化。

2. **先 Plan，再实现**
   - 使用 plan mode（`shift-tab` 或 `/plan`）先写规格。
   - 请求 Claude 给出架构建议与目录布局。
   - 通过目标导向 prompt 明确模块职责。

3. **小步迭代开发与评审**
   - 分块实现核心功能。
   - 每轮补单元测试、重构建议与文档。
   - 在 `CLAUDE.md` 持续维护任务清单。

4. **CI/CD 与发布自动化**
   - 让 Claude 生成 GitHub Actions、脚本与部署流程。
   - 更新 `CLAUDE.md` 后同步请求脚本调整。

### 旧仓库

1. **仓库上下文治理**
   - 更新 `CLAUDE.md` 记录结构、模式与关键文件。
   - 旧系统可补 `CLAUDE_LEGACY.md`（版本映射、已知问题、升级注意）。
   - 固定核心文件供 Claude 参考。

2. **上下文化问答与修改**
   - 按文件/函数定位做 code review、修复、重构或迁移。
   - 明确边界（只改哪些文件、是否允许新增依赖等）。

3. **分支与多会话并行**
   - 用 git worktree 隔离功能或 bug 修复。
   - 每个 worktree 启独立 Claude 会话。
   - 终端按分支/功能组织。

4. **团队自动化协同**
   - 通过 `.claude/commands/` 同步团队命令。
   - 用 slash commands / hooks 自动化重复任务与 PR 流程。
   - 共享会话上下文便于协作排障。

**Tips**：
- 新特性或修复先写 spec，再进 plan mode。
- 复杂旧仓库优先把规则沉淀到 CLAUDE 文档。
- 大任务拆阶段，使用清晰聚焦指令。
- 定期清理会话与 worktrees，降低上下文噪音。

---

## 新功能与能力（2026 年 3 月）

### 关键功能入口

| Feature | Description | Learn More |
|---------|-------------|------------|
| **Auto Memory** | Claude 自动学习并跨会话记住偏好 | [Memory Guide](02-memory/README.zh-CN.md) |
| **Remote Control** | 通过外部工具/脚本远程控制 Claude Code 会话 | [Advanced Features](09-advanced-features/README.zh-CN.md) |
| **Web Sessions** | 通过浏览器访问 Claude Code 进行远程开发 | [CLI Reference](10-cli/README.zh-CN.md) |
| **Desktop App** | 原生桌面应用，提供增强 UI | [Claude Code Docs](https://code.claude.com/docs/en/desktop) |
| **Extended Thinking** | 用 `Alt+T`/`Option+T` 或 `MAX_THINKING_TOKENS` 启用深度推理 | [Advanced Features](09-advanced-features/README.zh-CN.md) |
| **Permission Modes** | 细粒度权限模式：default、acceptEdits、plan、auto、dontAsk、bypassPermissions | [Advanced Features](09-advanced-features/README.zh-CN.md) |
| **7-Tier Memory** | Managed Policy、Project、Project Rules、User、User Rules、Local、Auto Memory | [Memory Guide](02-memory/README.zh-CN.md) |
| **Hook Events** | 25 类事件：PreToolUse、PostToolUse、PostToolUseFailure、Stop、StopFailure、SubagentStart、SubagentStop、Notification、Elicitation 等 | [Hooks Guide](06-hooks/README.zh-CN.md) |
| **Agent Teams** | 多 agents 协作处理复杂任务 | [Subagents Guide](04-subagents/README.zh-CN.md) |
| **Scheduled Tasks** | 基于 `/loop` 与 cron 的周期任务 | [Advanced Features](09-advanced-features/README.zh-CN.md) |
| **Chrome Integration** | 无头 Chromium 浏览器自动化 | [Advanced Features](09-advanced-features/README.zh-CN.md) |
| **Keyboard Customization** | 键位自定义（含组合键） | [Advanced Features](09-advanced-features/README.zh-CN.md) |
