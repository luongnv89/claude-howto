# Lesson Quiz — 题库

每课 10 道题。每道题包含：类别、题目、选项（3-4 个）、正确答案、解释以及复习章节。

---

## Lesson 01: 斜杠命令（Slash Commands）

### Q1
- **Category**: 概念型
- **Question**: Claude Code 中斜杠命令有哪四种类型？
- **Options**: A) 内置命令、技能、插件命令、MCP 提示 | B) 内置命令、自定义命令、钩子命令、API 提示 | C) 系统命令、用户命令、插件命令、终端命令 | D) 核心命令、扩展命令、宏命令、脚本命令
- **Correct**: A
- **Explanation**: Claude Code 拥有内置命令（如 /help、/compact）、技能（SKILL.md 文件）、插件命令（带命名空间的 plugin-name:command）以及 MCP 提示（/mcp__server__prompt）。
- **Review**: 斜杠命令类型章节

### Q2
- **Category**: 实践型
- **Question**: 如何将用户提供的所有参数传递给技能？
- **Options**: A) 使用 `${args}` | B) 使用 `$ARGUMENTS` | C) 使用 `$@` | D) 使用 `$INPUT`
- **Correct**: B
- **Explanation**: `$ARGUMENTS` 捕获命令名称后的所有文本。如需按位置访问参数，可使用 `$0`、`$1` 等。
- **Review**: 参数处理章节

### Q3
- **Category**: 概念型
- **Question**: 当同名的技能（.claude/skills/name/SKILL.md）和旧式命令（.claude/commands/name.md）同时存在时，哪个优先？
- **Options**: A) 旧式命令优先 | B) 技能优先 | C) 先创建的优先 | D) Claude 询问用户选择
- **Correct**: B
- **Explanation**: 技能比同名旧式命令拥有更高优先级。技能系统取代了旧版命令系统。
- **Review**: 技能优先级章节

### Q4
- **Category**: 实践型
- **Question**: 如何将实时 Shell 输出注入到技能的提示词中？
- **Options**: A) 使用 `$(command)` 语法 | B) 使用 `!`command`` （带 ! 的反引号）语法 | C) 使用 `@shell:command` 语法 | D) 使用 `{command}` 语法
- **Correct**: B
- **Explanation**: `!`command`` 语法会执行 Shell 命令，并在 Claude 处理前将其输出注入到技能提示词中。
- **Review**: 动态上下文注入章节

### Q5
- **Category**: 概念型
- **Question**: 技能 frontmatter 中的 `disable-model-invocation: true` 有什么作用？
- **Options**: A) 完全阻止技能运行 | B) 仅允许用户调用（Claude 不能自动调用） | C) 在 /help 菜单中隐藏该技能 | D) 禁用技能的 AI 处理
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` 表示只有用户可以通过 `/command-name` 触发该命令，Claude 永远不会自动调用它，适合有副作用的技能（如部署操作）。
- **Review**: 控制调用章节

### Q6
- **Category**: 实践型
- **Question**: 你想创建一个只能由 Claude 自动调用（对用户 / 菜单隐藏）的技能，应设置哪个 frontmatter 字段？
- **Options**: A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **Correct**: B
- **Explanation**: `user-invocable: false` 会将技能从用户的斜杠菜单中隐藏，但允许 Claude 根据上下文自动调用它。
- **Review**: 调用控制矩阵

### Q7
- **Category**: 实践型
- **Question**: 创建名为 "deploy" 的自定义技能，正确的目录结构是什么？
- **Options**: A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **Correct**: B
- **Explanation**: 技能存放在 `.claude/skills/` 下的子目录中，目录内包含一个 `SKILL.md` 文件。目录名即为命令名。
- **Review**: 技能类型与位置章节

### Q8
- **Category**: 概念型
- **Question**: 插件命令如何避免与用户命令产生名称冲突？
- **Options**: A) 使用 `plugin-name:command-name` 命名空间 | B) 使用特殊的 .plugin 扩展名 | C) 以 `p/` 前缀标识 | D) 自动覆盖用户命令
- **Correct**: A
- **Explanation**: 插件命令使用命名空间（如 `pr-review:check-security`），以避免与独立用户命令冲突。
- **Review**: 插件命令章节

### Q9
- **Category**: 实践型
- **Question**: 你想限制技能可以使用的工具，应添加哪个 frontmatter 字段？
- **Options**: A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **Correct**: B
- **Explanation**: SKILL.md frontmatter 中的 `allowed-tools` 字段用于限制命令可以调用的工具范围。
- **Review**: Frontmatter 字段参考

### Q10
- **Category**: 概念型
- **Question**: 技能中的 `@file` 语法有什么用途？
- **Options**: A) 导入另一个技能 | B) 引用文件并将其内容包含到提示词中 | C) 创建符号链接 | D) 设置文件权限
- **Correct**: B
- **Explanation**: 技能中的 `@path/to/file` 语法会将所引用文件的内容包含进提示词，允许技能引入模板或上下文文件。
- **Review**: 文件引用章节

---

## Lesson 02: 记忆（Memory）

### Q1
- **Category**: 概念型
- **Question**: Claude Code 记忆层级共有几层？哪层优先级最高？
- **Options**: A) 5 层，用户记忆（User Memory）优先级最高 | B) 7 层，托管策略（Managed Policy）优先级最高 | C) 3 层，项目记忆（Project Memory）优先级最高 | D) 7 层，自动记忆（Auto Memory）优先级最高
- **Correct**: B
- **Explanation**: 层级共 7 层：托管策略 > 项目记忆 > 项目规则 > 用户记忆 > 用户规则 > 本地项目记忆 > 自动记忆。由管理员设置的托管策略优先级最高。
- **Review**: 记忆层级章节

### Q2
- **Category**: 实践型
- **Question**: 如何在对话中快速添加新规则到记忆？
- **Options**: A) 输入 `/memory add "规则文本"` | B) 在消息前加 `#` 前缀（如 `# always use TypeScript`） | C) 输入 `/rule "规则文本"` | D) 使用 `@add-memory "规则文本"`
- **Correct**: B
- **Explanation**: `#` 前缀模式允许在对话中快速添加单条规则。Claude 会询问将其保存到哪个记忆层级。
- **Review**: 快速更新记忆章节

### Q3
- **Category**: 概念型
- **Question**: CLAUDE.md 中 `@path/to/file` 导入的最大深度是多少？
- **Options**: A) 3 层 | B) 5 层 | C) 10 层 | D) 无限制
- **Correct**: B
- **Explanation**: `@import` 语法支持递归导入，最大深度为 5 层，以防止无限循环。
- **Review**: 导入语法章节

### Q4
- **Category**: 实践型
- **Question**: 如何将规则文件的作用域限定为仅适用于 `src/api/` 下的文件？
- **Options**: A) 将规则放在 `src/api/CLAUDE.md` 中 | B) 在 `.claude/rules/*.md` 文件的 YAML frontmatter 中添加 `paths: src/api/**` | C) 将文件命名为 `.claude/rules/api.md` | D) 在规则文件中使用 `@scope: src/api`
- **Correct**: B
- **Explanation**: `.claude/rules/` 中的文件支持带 glob 模式的 `paths:` frontmatter 字段，以将规则限定到特定目录。
- **Review**: 路径特定规则章节

### Q5
- **Category**: 概念型
- **Question**: 自动记忆的 MEMORY.md 在会话开始时会加载多少行？
- **Options**: A) 全部行 | B) 前 100 行 | C) 前 200 行 | D) 前 500 行
- **Correct**: C
- **Explanation**: MEMORY.md 的前 200 行会在会话开始时自动加载到上下文中。从 MEMORY.md 引用的主题文件按需加载。
- **Review**: 自动记忆章节

### Q6
- **Category**: 实践型
- **Question**: 你希望保存个人项目偏好且不提交到 git，应使用哪个文件？
- **Options**: A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **Correct**: B
- **Explanation**: 项目根目录下的 `CLAUDE.local.md` 用于个人项目特定偏好，应将其加入 git 忽略列表。
- **Review**: 记忆位置对比

### Q7
- **Category**: 概念型
- **Question**: `/init` 命令的作用是什么？
- **Options**: A) 从零初始化一个新的 Claude Code 项目 | B) 根据项目结构生成模板 CLAUDE.md | C) 将所有记忆重置为默认值 | D) 创建新会话
- **Correct**: B
- **Explanation**: `/init` 会分析你的项目并生成带有建议规则和标准的模板 CLAUDE.md，是一次性引导工具。
- **Review**: /init 命令章节

### Q8
- **Category**: 实践型
- **Question**: 如何完全禁用自动记忆？
- **Options**: A) 删除 ~/.claude/projects 目录 | B) 设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) 在 CLAUDE.md 中添加 `auto-memory: false` | D) 使用 `/memory disable auto`
- **Correct**: B
- **Explanation**: 设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 可禁用自动记忆；值为 `0` 则强制开启；未设置则默认开启。
- **Review**: 自动记忆配置章节

### Q9
- **Category**: 概念型
- **Question**: 低优先级记忆层级能否覆盖高优先级层级的规则？
- **Options**: A) 可以，最新规则始终优先 | B) 不能，高优先级层级始终优先 | C) 可以，如果低优先级层级使用 `!important` 标志 | D) 取决于规则类型
- **Correct**: B
- **Explanation**: 记忆优先级从托管策略向下流动，低优先级层级（如自动记忆）无法覆盖高优先级层级（如项目记忆）的规则。
- **Review**: 记忆层级章节

### Q10
- **Category**: 实践型
- **Question**: 你同时在两个代码库工作，希望 Claude 从两个目录加载 CLAUDE.md，应使用哪个标志？
- **Options**: A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **Correct**: B
- **Explanation**: `--add-dir` 标志可从其他目录加载 CLAUDE.md，从而实现多代码库上下文。
- **Review**: 附加目录章节

---

## Lesson 03: 技能（Skills）

### Q1
- **Category**: 概念型
- **Question**: 技能系统的渐进式披露有哪 3 个层级？
- **Options**: A) 元数据、指令、资源 | B) 名称、主体、附件 | C) 头部、内容、脚本 | D) 摘要、详情、数据
- **Correct**: A
- **Explanation**: 第 1 层：元数据（约 100 个 token，始终加载）；第 2 层：SKILL.md 主体（<5k token，触发时加载）；第 3 层：捆绑资源（脚本/参考资料/资产，按需加载）。
- **Review**: 渐进式披露架构章节

### Q2
- **Category**: 实践型
- **Question**: 技能被 Claude 自动调用的最重要因素是什么？
- **Options**: A) 技能的文件名 | B) frontmatter 中包含触发关键词的 `description` 字段 | C) 技能的目录位置 | D) frontmatter 中的 `auto-invoke: true` 字段
- **Correct**: B
- **Explanation**: Claude 完全根据技能的 `description` 字段来决定是否自动调用，该字段必须包含具体的触发短语和使用场景。
- **Review**: 自动调用章节

### Q3
- **Category**: 概念型
- **Question**: SKILL.md 文件推荐的最大行数是多少？
- **Options**: A) 100 行 | B) 250 行 | C) 500 行 | D) 1000 行
- **Correct**: C
- **Explanation**: SKILL.md 应保持在 500 行以内。较大的参考资料应放在 `references/` 子目录的文件中。
- **Review**: 内容指南章节

### Q4
- **Category**: 实践型
- **Question**: 如何让技能在拥有独立上下文的隔离子智能体中运行？
- **Options**: A) 在 frontmatter 中设置 `isolation: true` | B) 在 frontmatter 中设置 `context: fork` 并添加 `agent` 字段 | C) 在 frontmatter 中设置 `subagent: true` | D) 将技能放在 `.claude/agents/` 目录中
- **Correct**: B
- **Explanation**: `context: fork` 使技能在独立上下文中运行，`agent` 字段指定使用的智能体类型（如 `Explore`、`Plan` 或自定义智能体）。
- **Review**: 在子智能体中运行技能章节

### Q5
- **Category**: 概念型
- **Question**: 分配给技能元数据（第 1 层）的上下文预算大约是多少？
- **Options**: A) 上下文窗口的 0.5% | B) 上下文窗口的 2% | C) 上下文窗口的 5% | D) 上下文窗口的 10%
- **Correct**: B
- **Explanation**: 技能元数据占用约 2% 的上下文窗口（回退值：16,000 个字符）。可通过 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 进行配置。
- **Review**: 上下文预算章节

### Q6
- **Category**: 实践型
- **Question**: 技能需要引用大型 API 规范，应将其放在哪里？
- **Options**: A) 直接内联在 SKILL.md 中 | B) 放在技能目录内的 `references/api-spec.md` 文件中 | C) 放在项目的 CLAUDE.md 中 | D) 放在单独的 `.claude/rules/` 文件中
- **Correct**: B
- **Explanation**: 大型参考资料应放在 `references/` 子目录中。Claude 按需加载第 3 层资源，保持 SKILL.md 精简。
- **Review**: 支撑文件结构章节

### Q7
- **Category**: 概念型
- **Question**: 技能中参考内容（Reference Content）和任务内容（Task Content）有什么区别？
- **Options**: A) 参考内容只读，任务内容可读写 | B) 参考内容向上下文添加知识，任务内容提供逐步操作指令 | C) 参考内容用于文档，任务内容用于代码 | D) 没有区别
- **Correct**: B
- **Explanation**: 参考内容向 Claude 的上下文添加领域知识（如品牌规范）；任务内容为工作流提供可执行的逐步指令。
- **Review**: 技能内容类型章节

### Q8
- **Category**: 实践型
- **Question**: 技能 frontmatter 的 `name` 字段允许使用哪些字符？
- **Options**: A) 任意字符 | B) 仅限小写字母、数字和连字符（最多 64 个字符） | C) 字母和下划线 | D) 仅限字母数字
- **Correct**: B
- **Explanation**: 名称必须为 kebab-case（小写字母加连字符），最多 64 个字符，且不能包含 "anthropic" 或 "claude"。
- **Review**: SKILL.md 格式章节

### Q9
- **Category**: 概念型
- **Question**: Claude 搜索技能的优先顺序是什么？
- **Options**: A) 用户 > 项目 > 企业 | B) 企业 > 个人 > 项目（插件使用命名空间） | C) 项目 > 用户 > 企业 | D) 按字母顺序
- **Correct**: B
- **Explanation**: 优先级顺序为：企业 > 个人 > 项目。插件技能使用命名空间（plugin-name:skill），因此不会产生冲突。
- **Review**: 技能类型与位置章节

### Q10
- **Category**: 实践型
- **Question**: 如何阻止 Claude 自动调用技能，同时仍允许用户手动使用它？
- **Options**: A) 设置 `user-invocable: false` | B) 设置 `disable-model-invocation: true` | C) 删除 description 字段 | D) 设置 `auto-invoke: false`
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` 阻止 Claude 自动调用，但保留技能在用户 `/` 菜单中供手动使用。
- **Review**: 控制调用章节

---

## Lesson 04: 子智能体（Subagents）

### Q1
- **Category**: 概念型
- **Question**: 子智能体相比内联对话的主要优势是什么？
- **Options**: A) 速度更快 | B) 在独立的干净上下文窗口中运行，防止上下文污染 | C) 可使用更多工具 | D) 拥有更好的错误处理
- **Correct**: B
- **Explanation**: 子智能体获得全新的上下文窗口，只接收主智能体传递的内容，防止主对话被任务特定细节污染。
- **Review**: 概述章节

### Q2
- **Category**: 实践型
- **Question**: 智能体定义的优先级顺序是什么？
- **Options**: A) 项目 > 用户 > CLI | B) CLI > 用户 > 项目 | C) 用户 > 项目 > CLI | D) 优先级相同
- **Correct**: B
- **Explanation**: CLI 定义的智能体（`--agents` 标志）覆盖用户级别（`~/.claude/agents/`），后者覆盖项目级别（`.claude/agents/`）。
- **Review**: 文件位置章节

### Q3
- **Category**: 概念型
- **Question**: 哪个内置子智能体使用 Haiku 模型，并针对只读代码库探索进行了优化？
- **Options**: A) general-purpose | B) Plan | C) Explore | D) Bash
- **Correct**: C
- **Explanation**: Explore 子智能体使用 Haiku 进行快速只读代码库探索，支持三种深度级别：快速、中等、非常彻底。
- **Review**: 内置子智能体章节

### Q4
- **Category**: 实践型
- **Question**: 如何限制协调者智能体可以派生的子智能体？
- **Options**: A) 使用 `allowed-agents:` 字段 | B) 在 `tools` 字段中使用 `Task(agent_name)` 语法 | C) 设置 `spawn-limit: 2` | D) 使用 `restrict-agents: [name1, name2]`
- **Correct**: B
- **Explanation**: 在 tools 字段中添加 `Task(worker, researcher)` 会创建白名单——智能体只能派生名为 "worker" 或 "researcher" 的子智能体。
- **Review**: 限制可派生子智能体章节

### Q5
- **Category**: 概念型
- **Question**: 子智能体的 `isolation: worktree` 有什么作用？
- **Options**: A) 在 Docker 容器中运行智能体 | B) 给智能体独立的 git worktree，使其变更不影响主工作树 | C) 阻止智能体读取任何文件 | D) 在沙箱中运行智能体
- **Correct**: B
- **Explanation**: Worktree 隔离会创建独立的 git worktree。若智能体未做任何更改，会自动清理；若有更改，则返回 worktree 路径和分支名。
- **Review**: Worktree 隔离章节

### Q6
- **Category**: 实践型
- **Question**: 如何让子智能体在后台运行？
- **Options**: A) 在智能体配置中设置 `background: true` | B) 在智能体配置中使用 `async: true` | C) 启动后按 Ctrl+D | D) 使用 `--background` CLI 标志
- **Correct**: A
- **Explanation**: 智能体配置中的 `background: true` 使子智能体始终以后台任务方式运行。用户也可以使用 Ctrl+B 将前台任务转移到后台。
- **Review**: 后台子智能体章节

### Q7
- **Category**: 概念型
- **Question**: 子智能体的 `memory` 字段设置 `scope: project` 有什么作用？
- **Options**: A) 授予对项目 CLAUDE.md 的读取权限 | B) 创建一个与当前项目绑定的持久化记忆目录 | C) 共享主智能体的对话历史 | D) 加载项目的 git 历史
- **Correct**: B
- **Explanation**: `memory` 字段为子智能体创建持久化目录。`scope: project` 表示记忆与当前项目绑定。智能体 MEMORY.md 的前 200 行会自动加载。
- **Review**: 持久化记忆章节

### Q8
- **Category**: 实践型
- **Question**: 如何在子智能体的描述中加入短语，以鼓励 Claude 自动将任务委托给它？
- **Options**: A) 添加 "priority: high" | B) 在描述中包含 "use PROACTIVELY" 或 "MUST BE USED" | C) 设置 `auto-delegate: true` | D) 添加 "trigger: always"
- **Correct**: B
- **Explanation**: 在描述中包含 "use PROACTIVELY" 或 "MUST BE USED" 等短语，会强烈鼓励 Claude 自动委托匹配的任务。
- **Review**: 自动委托章节

### Q9
- **Category**: 概念型
- **Question**: 子智能体有效的 `permissionMode` 值有哪些？
- **Options**: A) read、write、admin | B) default、acceptEdits、bypassPermissions、plan、dontAsk、auto | C) safe、normal、dangerous | D) restricted、standard、elevated
- **Correct**: B
- **Explanation**: 子智能体支持六种权限模式：default（所有操作均提示）、acceptEdits（自动接受文件编辑）、bypassPermissions（跳过所有检查）、plan（只读）、dontAsk（自动拒绝未预批准的操作）、auto（后台分类器决定）。
- **Review**: 配置字段章节

### Q10
- **Category**: 实践型
- **Question**: 如何恢复之前运行中返回了 agentId 的子智能体？
- **Options**: A) 使用 `/resume agent-id` | B) 调用 Task 工具时传入带有 agentId 的 `resume` 参数 | C) 使用 `claude -r agent-id` | D) 子智能体无法恢复
- **Correct**: B
- **Explanation**: 可通过向 Task 工具传入带有之前返回的 agentId 的 `resume` 参数来恢复子智能体，完整保留上下文继续运行。
- **Review**: 可恢复智能体章节

---

## Lesson 05: MCP

### Q1
- **Category**: 概念型
- **Question**: MCP 有哪三种传输协议？哪种是推荐使用的？
- **Options**: A) HTTP（推荐）、Stdio、SSE（已弃用） | B) WebSocket（推荐）、REST、gRPC | C) TCP、UDP、HTTP | D) Stdio（推荐）、HTTP、SSE
- **Correct**: A
- **Explanation**: HTTP 推荐用于远程服务器；Stdio 用于本地进程（目前最常见）；SSE 已弃用但仍受支持。
- **Review**: 传输协议章节

### Q2
- **Category**: 实践型
- **Question**: 如何通过 CLI 添加 GitHub MCP 服务器？
- **Options**: A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **Correct**: B
- **Explanation**: 使用 `claude mcp add` 并加上 `--transport` 标志、名称和服务器 URL。对于 stdio 方式：`claude mcp add github -- npx -y @modelcontextprotocol/server-github`。
- **Review**: MCP 配置管理章节

### Q3
- **Category**: 概念型
- **Question**: 当 MCP 工具描述超过上下文窗口的 10% 时会发生什么？
- **Options**: A) 被截断 | B) MCP 工具搜索自动启用，以动态选择相关工具 | C) Claude 显示错误 | D) 多余的工具被禁用
- **Correct**: B
- **Explanation**: 当工具超过上下文 10% 时，MCP 工具搜索自动启用，最低需要 Sonnet 4 或 Opus 4（不支持 Haiku）。
- **Review**: MCP 工具搜索章节

### Q4
- **Category**: 实践型
- **Question**: 如何在 MCP 配置中使用环境变量回退值？
- **Options**: A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **Correct**: B
- **Explanation**: `${VAR:-default}` 在环境变量未设置时提供回退值。不带回退的 `${VAR}` 在变量未设置时会报错。
- **Review**: 环境变量展开章节

### Q5
- **Category**: 概念型
- **Question**: MCP 与记忆（Memory）在数据访问方面有什么区别？
- **Options**: A) MCP 更快，记忆更慢 | B) MCP 用于动态变化的外部数据，记忆用于持久静态偏好 | C) MCP 用于代码，记忆用于文本 | D) 两者可互换
- **Correct**: B
- **Explanation**: MCP 连接动态变化的外部数据源（API、数据库）；记忆存储持久的静态项目上下文和偏好。
- **Review**: MCP 与记忆对比章节

### Q6
- **Category**: 实践型
- **Question**: 团队成员首次遇到项目作用域的 `.mcp.json` 时会发生什么？
- **Options**: A) 自动加载 | B) 收到批准提示以信任项目的 MCP 服务器 | C) 除非主动选择，否则被忽略 | D) Claude 要求管理员批准
- **Correct**: B
- **Explanation**: 项目作用域的 `.mcp.json` 在每位团队成员首次使用时触发安全批准提示，此举是有意为之，用于防止信任未知的 MCP 服务器。
- **Review**: MCP 作用域章节

### Q7
- **Category**: 概念型
- **Question**: `claude mcp serve` 有什么作用？
- **Options**: A) 启动 MCP 服务器仪表盘 | B) 使 Claude Code 本身作为其他应用程序的 MCP 服务器 | C) 提供 MCP 文档服务 | D) 测试 MCP 服务器连接
- **Correct**: B
- **Explanation**: `claude mcp serve` 将 Claude Code 变为 MCP 服务器，从而实现多智能体编排，使一个 Claude 实例可以被另一个控制。
- **Review**: Claude 作为 MCP 服务器章节

### Q8
- **Category**: 实践型
- **Question**: MCP 工具的默认最大输出大小是多少？
- **Options**: A) 5,000 个 token | B) 10,000 个 token | C) 25,000 个 token | D) 50,000 个 token
- **Correct**: C
- **Explanation**: 默认最大值为 25,000 个 token（`MAX_MCP_OUTPUT_TOKENS`）。超过 10k token 时显示警告，磁盘持久化上限为 50k 个字符。
- **Review**: MCP 输出限制章节

### Q9
- **Category**: 概念型
- **Question**: 在托管配置中，`allowedMcpServers` 和 `deniedMcpServers` 同时匹配某个服务器时，哪个优先？
- **Options**: A) 允许规则优先 | B) 拒绝规则优先 | C) 后配置的优先 | D) 两者独立应用
- **Correct**: B
- **Explanation**: 在托管 MCP 配置中，拒绝规则始终优先于允许规则。
- **Review**: 托管 MCP 配置章节

### Q10
- **Category**: 实践型
- **Question**: 如何在对话中引用 MCP 资源？
- **Options**: A) 使用 `/mcp resource-name` | B) 使用 `@server-name:protocol://resource/path` 提及语法 | C) 使用 `mcp.get("resource")` | D) 资源自动加载
- **Correct**: B
- **Explanation**: MCP 资源通过对话中的 `@server-name:protocol://resource/path` 提及语法访问。
- **Review**: MCP 资源章节

---

## Lesson 06: 钩子（Hooks）

### Q1
- **Category**: 概念型
- **Question**: Claude Code 中有哪四种类型的钩子？
- **Options**: A) 前置、后置、错误和过滤钩子 | B) 命令钩子、HTTP 钩子、提示词钩子和智能体钩子 | C) Before、After、Around 和 Through 钩子 | D) 输入、输出、过滤和转换钩子
- **Correct**: B
- **Explanation**: 命令钩子运行 Shell 脚本，HTTP 钩子调用 Webhook 端点，提示词钩子使用单轮 LLM 评估，智能体钩子使用基于子智能体的验证。
- **Review**: 钩子类型章节

### Q2
- **Category**: 实践型
- **Question**: 钩子脚本以退出码 2 退出，会发生什么？
- **Options**: A) 显示非阻塞警告 | B) 阻塞性错误——stderr 作为错误显示给 Claude，阻止工具调用 | C) 钩子被重试 | D) 会话结束
- **Correct**: B
- **Explanation**: 退出码 0 = 成功/继续；退出码 2 = 阻塞性错误（stderr 作为错误显示）；其他非零值 = 非阻塞（stderr 仅在详细模式显示）。
- **Review**: 退出码章节

### Q3
- **Category**: 概念型
- **Question**: PreToolUse 钩子从 stdin 接收哪些 JSON 字段？
- **Options**: A) `tool_name` 和 `tool_output` | B) `session_id`、`tool_name`、`tool_input`、`hook_event_name`、`cwd` 等 | C) 仅 `tool_name` | D) 完整的对话历史
- **Correct**: B
- **Explanation**: 钩子从 stdin 接收包含以下字段的 JSON 对象：session_id、transcript_path、hook_event_name、tool_name、tool_input、tool_use_id、cwd 以及 permission_mode。
- **Review**: JSON 输入结构章节

### Q4
- **Category**: 实践型
- **Question**: PreToolUse 钩子如何在执行前修改工具的输入参数？
- **Options**: A) 在 stderr 上返回修改后的 JSON | B) 在 stdout 上返回包含 `updatedInput` 字段的 JSON（退出码 0） | C) 写入临时文件 | D) 钩子无法修改输入
- **Correct**: B
- **Explanation**: PreToolUse 钩子可在 stdout 输出包含 `"updatedInput": {...}` 的 JSON（退出码 0），在 Claude 使用工具前修改其参数。
- **Review**: PreToolUse 输出章节

### Q5
- **Category**: 概念型
- **Question**: 哪种钩子事件支持 `CLAUDE_ENV_FILE`，用于将环境变量持久化到会话中？
- **Options**: A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) 所有事件
- **Correct**: C
- **Explanation**: 只有 SessionStart 钩子可以使用 `CLAUDE_ENV_FILE` 将环境变量持久化到会话中。
- **Review**: SessionStart 章节

### Q6
- **Category**: 实践型
- **Question**: 你想要一个钩子在技能首次加载时只运行一次，而不是在每次工具调用时运行，应添加哪个字段？
- **Options**: A) `run-once: true` | B) 在组件钩子定义中添加 `once: true` | C) `single: true` | D) `max-runs: 1`
- **Correct**: B
- **Explanation**: 组件作用域的钩子（在 SKILL.md 或智能体 frontmatter 中定义）支持 `once: true`，使其仅在首次激活时运行。
- **Review**: 组件作用域钩子章节

### Q7
- **Category**: 概念型
- **Question**: 在子智能体 frontmatter 中定义的 Stop 钩子会自动转换为什么？
- **Options**: A) PostToolUse 钩子 | B) SubagentStop 钩子 | C) SessionEnd 钩子 | D) 保持为 Stop 钩子
- **Correct**: B
- **Explanation**: 当 Stop 钩子放在子智能体的 frontmatter 中时，会自动转换为 SubagentStop，使其在该特定子智能体完成时触发。
- **Review**: 组件作用域钩子章节

### Q8
- **Category**: 实践型
- **Question**: 如何将钩子匹配到特定 MCP 服务器的所有工具？
- **Options**: A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"`（正则表达式模式） | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **Correct**: B
- **Explanation**: 对匹配器使用正则表达式模式。MCP 工具遵循 `mcp__server__tool` 命名规范，因此 `mcp__github__.*` 可匹配所有 GitHub MCP 工具。
- **Review**: 匹配器模式章节

### Q9
- **Category**: 概念型
- **Question**: Claude Code 总共支持多少种钩子事件？
- **Options**: A) 10 | B) 16 | C) 25 | D) 30
- **Correct**: C
- **Explanation**: Claude Code 支持 25 种钩子事件：PreToolUse、PostToolUse、PostToolUseFailure、UserPromptSubmit、Stop、StopFailure、SubagentStop、SubagentStart、PermissionRequest、Notification、PreCompact、PostCompact、SessionStart、SessionEnd、WorktreeCreate、WorktreeRemove、ConfigChange、CwdChanged、FileChanged、TeammateIdle、TaskCompleted、TaskCreated、Elicitation、ElicitationResult、InstructionsLoaded。
- **Review**: 钩子事件表

### Q10
- **Category**: 实践型
- **Question**: 你想调试钩子未触发的原因，最佳方法是什么？
- **Options**: A) 在钩子脚本中添加打印语句 | B) 使用 `--debug` 标志和 `Ctrl+O` 详细模式 | C) 查看系统日志 | D) 钩子没有调试工具
- **Correct**: B
- **Explanation**: `--debug` 标志和 `Ctrl+O` 详细模式会显示钩子执行详情，包括哪些钩子触发了、它们的输入和输出。
- **Review**: 调试章节

---

## Lesson 07: 插件（Plugins）

### Q1
- **Category**: 概念型
- **Question**: 插件的核心清单文件是什么？它位于哪里？
- **Options**: A) 根目录下的 `plugin.yaml` | B) `.claude-plugin/plugin.json` | C) 带有 "claude" 键的 `package.json` | D) `.claude/plugin.md`
- **Correct**: B
- **Explanation**: 插件清单位于 `.claude-plugin/plugin.json`，包含必填字段：name、description、version、author。
- **Review**: 插件定义结构章节

### Q2
- **Category**: 实践型
- **Question**: 如何在发布前本地测试插件？
- **Options**: A) 使用 `/plugin test ./my-plugin` | B) 使用 `claude --plugin-dir ./my-plugin` | C) 使用 `claude plugin validate ./my-plugin` | D) 将其复制到 ~/.claude/plugins/
- **Correct**: B
- **Explanation**: `--plugin-dir` 标志从本地目录加载插件进行测试，可重复使用以加载多个插件。
- **Review**: 测试章节

### Q3
- **Category**: 概念型
- **Question**: 插件钩子和 MCP 配置内部可用哪个环境变量来引用插件的安装目录？
- **Options**: A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **Correct**: B
- **Explanation**: `${CLAUDE_PLUGIN_ROOT}` 解析为插件的安装目录，使钩子和 MCP 配置中的路径引用具有可移植性。
- **Review**: 插件目录结构章节

### Q4
- **Category**: 实践型
- **Question**: "pr-review" 插件中有一个名为 "check-security" 的命令，用户如何调用它？
- **Options**: A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **Correct**: B
- **Explanation**: 插件命令使用 `plugin-name:command-name` 命名空间，以避免与用户命令和其他插件冲突。
- **Review**: 插件命令章节

### Q5
- **Category**: 概念型
- **Question**: 插件可以捆绑哪些组件？
- **Options**: A) 仅命令和设置 | B) 命令、智能体、技能、钩子、MCP 服务器、LSP 配置、设置、模板、脚本 | C) 仅命令、钩子和 MCP 服务器 | D) 仅技能和智能体
- **Correct**: B
- **Explanation**: 插件可捆绑：commands/、agents/、skills/、hooks/hooks.json、.mcp.json、.lsp.json、settings.json、templates/、scripts/、docs/、tests/。
- **Review**: 插件目录结构章节

### Q6
- **Category**: 实践型
- **Question**: 如何从 GitHub 安装插件？
- **Options**: A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) `git clone` 后再 `claude plugin register`
- **Correct**: B
- **Explanation**: 使用 `/plugin install github:username/repo` 直接从 GitHub 仓库安装。
- **Review**: 安装方法章节

### Q7
- **Category**: 概念型
- **Question**: 插件中 `settings.json` 的 `agent` 键有什么作用？
- **Options**: A) 指定身份验证凭据 | B) 设置插件激活时主线程使用的智能体 | C) 列出可用的子智能体 | D) 配置智能体权限
- **Correct**: B
- **Explanation**: 插件 settings.json 中的 `agent` 键指定插件激活时主线程使用的智能体定义。
- **Review**: 插件设置章节

### Q8
- **Category**: 实践型
- **Question**: 如何管理插件生命周期（启用/禁用/更新）？
- **Options**: A) 手动编辑配置文件 | B) 使用 `/plugin enable`、`/plugin disable`、`/plugin update plugin-name` | C) 使用 `claude plugin-manager` | D) 重新安装插件
- **Correct**: B
- **Explanation**: Claude Code 提供斜杠命令进行完整的生命周期管理：enable（启用）、disable（禁用）、update（更新）、uninstall（卸载）。
- **Review**: 安装方法章节

### Q9
- **Category**: 概念型
- **Question**: 插件相比独立技能/钩子/MCP 的主要优势是什么？
- **Options**: A) 插件速度更快 | B) 单命令安装、版本管理、市场分发，将所有内容打包在一起 | C) 插件拥有更多权限 | D) 插件可离线使用
- **Correct**: B
- **Explanation**: 插件将多个组件打包为一个可安装单元，具备版本管理、市场分发和自动更新功能——相比之下，独立组件需要手动安装配置。
- **Review**: 独立组件与插件对比章节

### Q10
- **Category**: 实践型
- **Question**: 插件的钩子配置文件位于插件目录的什么位置？
- **Options**: A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` 钩子部分 | D) `.claude/settings.json`
- **Correct**: B
- **Explanation**: 插件钩子配置在插件目录结构中的 `hooks/hooks.json` 文件中。
- **Review**: 插件钩子章节

---

## Lesson 08: 检查点（Checkpoints）

### Q1
- **Category**: 概念型
- **Question**: 检查点会捕获哪四类内容？
- **Options**: A) Git 提交、分支、标签、暂存 | B) 消息、文件修改、工具使用历史、会话上下文 | C) 代码、测试、日志、配置 | D) 输入、输出、错误、时间
- **Correct**: B
- **Explanation**: 检查点捕获：对话消息、Claude 工具造成的文件修改、工具使用历史以及会话上下文。
- **Review**: 概述章节

### Q2
- **Category**: 实践型
- **Question**: 如何访问检查点浏览器？
- **Options**: A) 使用 `/checkpoints` 命令 | B) 按 `Esc + Esc`（双击 Esc）或使用 `/rewind` | C) 使用 `/history` 命令 | D) 按 `Ctrl+Z`
- **Correct**: B
- **Explanation**: 双击 Esc（Esc+Esc）或 `/rewind` 命令可打开检查点浏览器，选择恢复点。
- **Review**: 访问检查点章节

### Q3
- **Category**: 概念型
- **Question**: 回溯（rewind）有多少个选项？分别是什么？
- **Options**: A) 3 个：撤销、重做、重置 | B) 5 个：恢复代码+对话、仅恢复对话、仅恢复代码、从此处摘要、取消 | C) 2 个：完全恢复、部分恢复 | D) 4 个：代码、消息、两者、取消
- **Correct**: B
- **Explanation**: 5 个选项分别为：恢复代码和对话（完全回滚）、仅恢复对话、仅恢复代码、从此处摘要（压缩）、取消。
- **Review**: 回溯选项章节

### Q4
- **Category**: 实践型
- **Question**: 你通过 Claude Code 中的 Bash 执行了 `rm -rf temp/`，然后想要回溯。检查点能恢复这些文件吗？
- **Options**: A) 能，检查点捕获一切 | B) 不能，Bash 文件系统操作（rm、mv、cp）不被检查点追踪 | C) 只有在使用 Edit 工具时才能恢复 | D) 只有在启用了 autoCheckpoint 时才能恢复
- **Correct**: B
- **Explanation**: 检查点只追踪 Claude 工具（Write、Edit）造成的文件更改，Bash 命令（如 rm、mv、cp）在检查点追踪范围之外。
- **Review**: 限制章节

### Q5
- **Category**: 概念型
- **Question**: 检查点保留多长时间？
- **Options**: A) 直到会话结束 | B) 7 天 | C) 30 天 | D) 永久
- **Correct**: C
- **Explanation**: 检查点跨会话持久保留，最长 30 天，之后自动清理。
- **Review**: 检查点持久化章节

### Q6
- **Category**: 实践型
- **Question**: 回溯时"从此处摘要"有什么作用？
- **Options**: A) 删除该点之后的对话 | B) 将对话压缩为 AI 生成的摘要，同时在转录文件中保留原文 | C) 创建更改的要点列表 | D) 将对话导出到文件
- **Correct**: B
- **Explanation**: "摘要"会将对话压缩为简短的 AI 生成摘要，原始完整文本保留在转录文件中。
- **Review**: 摘要选项章节

### Q7
- **Category**: 概念型
- **Question**: 检查点何时会自动创建？
- **Options**: A) 每 5 分钟 | B) 在每次用户提示时 | C) 只有手动保存时 | D) 在每次工具使用后
- **Correct**: B
- **Explanation**: 自动检查点在每次用户提示时创建，捕获 Claude 处理请求前的状态。
- **Review**: 自动检查点章节

### Q8
- **Category**: 实践型
- **Question**: 如何禁用自动检查点创建？
- **Options**: A) 使用 `--no-checkpoints` 标志 | B) 在设置中设置 `autoCheckpoint: false` | C) 删除 checkpoints 目录 | D) 检查点无法禁用
- **Correct**: B
- **Explanation**: 在配置中设置 `autoCheckpoint: false` 可禁用自动检查点创建（默认为 true）。
- **Review**: 配置章节

### Q9
- **Category**: 概念型
- **Question**: 检查点能否替代 git 提交？
- **Options**: A) 可以，它们更强大 | B) 不能，两者互补——检查点有会话范围限制且会过期，git 是永久且可共享的 | C) 可以，对于小项目 | D) 仅在个人开发中适用
- **Correct**: B
- **Explanation**: 检查点是临时的（30 天保留）、会话范围的，且无法共享；git 提交是永久的、可审计的、可共享的。应两者结合使用。
- **Review**: 与 git 集成章节

### Q10
- **Category**: 实践型
- **Question**: 你想比较两种不同的实现方案，推荐的检查点工作流程是什么？
- **Options**: A) 创建两个独立会话 | B) 在方案 A 前创建检查点，尝试方案 A，回滚到检查点，再尝试方案 B，对比结果 | C) 改用 git 分支 | D) 没有好的比较方法
- **Correct**: B
- **Explanation**: 分支策略：在干净状态创建检查点，尝试方案 A 并记录结果，回滚到同一检查点，再尝试方案 B，对比两种结果。
- **Review**: 工作流程模式章节

---

## Lesson 09: 高级功能（Advanced Features）

### Q1
- **Category**: 概念型
- **Question**: Claude Code 中有哪六种权限模式？
- **Options**: A) read、write、execute、admin、root、sudo | B) default、acceptEdits、plan、auto、dontAsk、bypassPermissions | C) safe、normal、elevated、admin、unrestricted、god | D) view、edit、run、deploy、full、bypass
- **Correct**: B
- **Explanation**: 六种模式分别为：default（所有操作均提示）、acceptEdits（自动接受文件编辑）、plan（只读分析）、auto（后台分类器决定）、dontAsk（自动拒绝未预批准的操作）、bypassPermissions（跳过所有检查）。
- **Review**: 权限模式章节

### Q2
- **Category**: 实践型
- **Question**: 如何激活规划模式？
- **Options**: A) 仅通过 `/plan` 命令 | B) 通过 `/plan`、`Shift+Tab`/`Alt+M`、`--permission-mode plan` 标志或默认配置 | C) 仅通过 `--planning` 标志 | D) 规划模式始终开启
- **Correct**: B
- **Explanation**: 规划模式可通过多种方式激活：/plan 命令、Shift+Tab/Alt+M 快捷键、--permission-mode plan CLI 标志，或作为配置中的默认值。
- **Review**: 规划模式章节

### Q3
- **Category**: 概念型
- **Question**: `opusplan` 模型别名有什么作用？
- **Options**: A) 所有操作都使用 Opus | B) 规划阶段使用 Opus，实现阶段使用 Sonnet | C) 使用专门针对规划优化的模型 | D) 自动启用规划模式
- **Correct**: B
- **Explanation**: `opusplan` 是一个模型别名，在规划阶段使用 Opus（更高质量的分析），在执行阶段使用 Sonnet（更快的实现）。
- **Review**: 规划模式章节

### Q4
- **Category**: 实践型
- **Question**: 如何在会话中切换扩展思考（extended thinking）？
- **Options**: A) 输入 `/think` | B) 按 `Option+T`（macOS）或 `Alt+T` | C) 使用 `--thinking` 标志 | D) 始终启用，无法切换
- **Correct**: B
- **Explanation**: Option+T（macOS）或 Alt+T 可切换扩展思考，所有模型默认启用。Opus 4.6 支持自适应努力级别。
- **Review**: 扩展思考章节

### Q5
- **Category**: 概念型
- **Question**: "think" 或 "ultrathink" 是激活增强思考的特殊关键词吗？
- **Options**: A) 是，它们会激活更深层的推理 | B) 否，它们被视为普通提示词文本，没有特殊行为 | C) 只有 "ultrathink" 是特殊的 | D) 仅在使用 Opus 时有效
- **Correct**: B
- **Explanation**: 文档明确指出这些是普通提示词指令，不是特殊激活关键词。扩展思考通过 Alt+T 切换和环境变量来控制。
- **Review**: 扩展思考章节

### Q6
- **Category**: 实践型
- **Question**: 如何在 CI/CD 流水线中以带轮次限制的结构化 JSON 输出运行 Claude？
- **Options**: A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **Correct**: B
- **Explanation**: 带 `--output-format json` 和 `--max-turns` 的打印模式（`-p`）是标准的 CI/CD 集成模式。
- **Review**: 无头/打印模式章节

### Q7
- **Category**: 概念型
- **Question**: 任务列表功能（Ctrl+T）提供什么？
- **Options**: A) 运行中后台进程的列表 | B) 在上下文压缩后仍持久保存、可通过 `CLAUDE_CODE_TASK_LIST_ID` 共享的待办事项列表 | C) 过去会话的历史记录 | D) 待处理工具调用的队列
- **Correct**: B
- **Explanation**: 任务列表（Ctrl+T）在上下文压缩后仍然持久，可通过使用 `CLAUDE_CODE_TASK_LIST_ID` 命名任务目录，在不同会话间共享。
- **Review**: 任务列表章节

### Q8
- **Category**: 实践型
- **Question**: 在规划模式下如何在外部编辑器中编辑计划？
- **Options**: A) 从终端复制粘贴 | B) 按 `Ctrl+G` 在外部编辑器中打开计划 | C) 使用 `/export-plan` 命令 | D) 计划无法在外部编辑
- **Correct**: B
- **Explanation**: Ctrl+G 在配置的外部编辑器中打开当前计划进行修改。
- **Review**: 规划模式章节

### Q9
- **Category**: 概念型
- **Question**: `dontAsk` 和 `bypassPermissions` 模式有什么区别？
- **Options**: A) 两者相同 | B) `dontAsk` 自动拒绝未预批准的操作；`bypassPermissions` 完全跳过所有检查 | C) `dontAsk` 用于文件；`bypassPermissions` 用于命令 | D) `bypassPermissions` 更安全
- **Correct**: B
- **Explanation**: dontAsk 自动拒绝权限请求，除非匹配预批准模式；bypassPermissions 完全跳过所有安全检查，常规使用非常危险。
- **Review**: 权限模式章节

### Q10
- **Category**: 实践型
- **Question**: 如何将 CLI 会话移交给桌面应用？
- **Options**: A) 使用 `/export` 命令 | B) 使用 `/desktop` 命令 | C) 复制会话 ID 并粘贴到应用中 | D) CLI 和桌面之间无法转移会话
- **Correct**: B
- **Explanation**: `/desktop` 命令将当前 CLI 会话移交给原生桌面应用，用于可视化差异审查和多会话管理。
- **Review**: 桌面应用章节

---

## Lesson 10: CLI 参考（CLI Reference）

### Q1
- **Category**: 概念型
- **Question**: Claude CLI 的两种主要模式是什么？
- **Options**: A) 在线模式和离线模式 | B) 交互式 REPL（`claude`）和打印模式（`claude -p`） | C) GUI 模式和终端模式 | D) 单次模式和批量模式
- **Correct**: B
- **Explanation**: 交互式 REPL 是默认的对话模式；打印模式（-p）是非交互式的，可脚本化、可管道传输，执行一次响应后退出。
- **Review**: CLI 架构章节

### Q2
- **Category**: 实践型
- **Question**: 如何将文件通过管道传给 Claude 并获取 JSON 输出？
- **Options**: A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **Correct**: B
- **Explanation**: 通过 stdin 将内容管道传输到打印模式（-p），并使用 --output-format json 获取结构化输出。
- **Review**: 交互式与打印模式章节

### Q3
- **Category**: 概念型
- **Question**: `-c` 和 `-r` 标志有什么区别？
- **Options**: A) 两者作用相同 | B) `-c` 继续最近的会话；`-r` 按名称或 ID 恢复指定会话 | C) `-c` 创建新会话；`-r` 恢复会话 | D) `-c` 用于代码；`-r` 用于审查
- **Correct**: B
- **Explanation**: `-c/--continue` 恢复最近的对话；`-r/--resume "name"` 按名称或会话 ID 恢复指定会话。
- **Review**: 会话管理章节

### Q4
- **Category**: 实践型
- **Question**: 如何保证 Claude 输出符合模式的有效 JSON？
- **Options**: A) 仅使用 `--output-format json` | B) 使用 `--output-format json --json-schema '{"type":"object",...}'` | C) 使用 `--strict-json` 标志 | D) JSON 输出始终符合模式
- **Correct**: B
- **Explanation**: 单独使用 `--output-format json` 只能产生尽力而为的 JSON；配合 `--json-schema` 提供 JSON Schema 定义，才能保证输出符合该模式。
- **Review**: 输出与格式章节

### Q5
- **Category**: 概念型
- **Question**: 哪个标志仅在打印模式（-p）下有效，在交互模式下无效？
- **Options**: A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **Correct**: B
- **Explanation**: `--system-prompt-file` 从文件加载系统提示词，但仅在打印模式下有效。交互式会话请使用 `--system-prompt`（内联字符串）。
- **Review**: 系统提示词标志对比表

### Q6
- **Category**: 实践型
- **Question**: 如何限制 Claude 在安全审计中仅使用只读工具？
- **Options**: A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **Correct**: B
- **Explanation**: 结合 `--permission-mode plan`（只读分析）和 `--tools`（特定工具白名单），将 Claude 限制为只执行读取操作。
- **Review**: 工具与权限管理章节

### Q7
- **Category**: 概念型
- **Question**: 智能体定义的优先级顺序是什么？
- **Options**: A) 项目 > 用户 > CLI | B) CLI > 用户 > 项目 | C) 用户 > CLI > 项目 | D) 优先级相同
- **Correct**: B
- **Explanation**: CLI 定义的智能体（--agents 标志）优先级最高，其次是用户级别（~/.claude/agents/），最后是项目级别（.claude/agents/）。
- **Review**: 智能体配置章节

### Q8
- **Category**: 实践型
- **Question**: 如何从现有会话创建分支，尝试不同方案而不丢失原始内容？
- **Options**: A) 使用 `/fork` 命令 | B) 使用 `--resume session-name --fork-session "branch name"` | C) 使用 `--clone session-name` | D) 使用 `/branch session-name`
- **Correct**: B
- **Explanation**: `--resume` 配合 `--fork-session` 从恢复的会话创建新的独立分支，同时保留原始对话。
- **Review**: 会话管理章节

### Q9
- **Category**: 概念型
- **Question**: 用户已登录时，`claude auth status` 返回什么退出码？
- **Options**: A) 1 | B) 0 | C) 200 | D) 不返回退出码
- **Correct**: B
- **Explanation**: 已登录时 `claude auth status` 退出码为 0，未登录时为 1，便于在 CI/CD 认证检查脚本中使用。
- **Review**: CLI 命令表

### Q10
- **Category**: 实践型
- **Question**: 如何批量处理多个文件？
- **Options**: A) `claude --batch *.md` | B) 使用 for 循环：`for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) 不支持批量处理
- **Correct**: B
- **Explanation**: 配合打印模式使用 Shell for 循环，每次处理一个文件。每次调用相互独立，可产生结构化输出。
- **Review**: 批量处理章节
