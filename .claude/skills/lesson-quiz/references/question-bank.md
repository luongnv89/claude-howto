# Lesson Quiz — Question Bank

10 questions per lesson. Each question has: category, question text, options (3-4), correct answer, explanation, and review section.

---

## Lesson 01: Slash Commands

### Q1
- **Category**: conceptual
- **Question**: What are the four types of slash commands in Claude Code?
- **Options**: A) Built-in, skills, plugin commands, MCP prompts | B) Built-in, custom, hook commands, API prompts | C) System, user, plugin, terminal commands | D) Core, extension, macro, script commands
- **Correct**: A
- **Explanation**: Claude Code has built-in commands (like /help, /compact), skills (SKILL.md files), plugin commands (namespaced plugin-name:command), and MCP prompts (/mcp__server__prompt).
- **Review**: Types of Slash Commands section

### Q2
- **Category**: practical
- **Question**: How do you pass all user-provided arguments to a skill?
- **Options**: A) Use `${args}` | B) Use `$ARGUMENTS` | C) Use `$@` | D) Use `$INPUT`
- **Correct**: B
- **Explanation**: `$ARGUMENTS` captures all text after the command name. For positional args, use `$0`, `$1`, etc.
- **Review**: Argument handling section

### Q3
- **Category**: conceptual
- **Question**: When both a skill (.claude/skills/name/SKILL.md) and a legacy command (.claude/commands/name.md) exist with the same name, which takes priority?
- **Options**: A) The legacy command | B) The skill | C) Whichever was created first | D) Claude asks the user to choose
- **Correct**: B
- **Explanation**: Skills take precedence over legacy commands with the same name. The skill system supersedes the older command system.
- **Review**: Skill precedence section

### Q4
- **Category**: practical
- **Question**: How do you inject live shell output into a skill's prompt?
- **Options**: A) Use `$(command)` syntax | B) Use `!`command`` (backtick with !) syntax | C) Use `@shell:command` syntax | D) Use `{command}` syntax
- **Correct**: B
- **Explanation**: The `!`command`` syntax runs a shell command and injects its output into the skill prompt before Claude sees it.
- **Review**: Dynamic context injection section

### Q5
- **Category**: conceptual
- **Question**: What does `disable-model-invocation: true` do in a skill's frontmatter?
- **Options**: A) Prevents the skill from running entirely | B) Allows only the user to invoke it (Claude cannot auto-invoke) | C) Hides it from the /help menu | D) Disables the skill's AI processing
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` means only the user can trigger the command via `/command-name`. Claude will never auto-invoke it, useful for skills with side effects like deployments.
- **Review**: Controlling invocation section

### Q6
- **Category**: practical
- **Question**: You want to create a skill that only Claude can invoke automatically (hidden from the user's / menu). Which frontmatter field do you set?
- **Options**: A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **Correct**: B
- **Explanation**: `user-invocable: false` hides the skill from the user's slash menu but allows Claude to invoke it automatically based on context.
- **Review**: Invocation control matrix

### Q7
- **Category**: practical
- **Question**: What is the correct directory structure for a new custom skill called "deploy"?
- **Options**: A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **Correct**: B
- **Explanation**: Skills live in a directory under `.claude/skills/` with a `SKILL.md` file inside. The directory name matches the command name.
- **Review**: Skill types and locations section

### Q8
- **Category**: conceptual
- **Question**: How do plugin commands avoid name conflicts with user commands?
- **Options**: A) They use a `plugin-name:command-name` namespace | B) They have a special .plugin extension | C) They are prefixed with `p/` | D) They override user commands automatically
- **Correct**: A
- **Explanation**: Plugin commands use a namespace like `pr-review:check-security` to avoid conflicts with standalone user commands.
- **Review**: Plugin commands section

### Q9
- **Category**: practical
- **Question**: You want to restrict which tools a skill can use. Which frontmatter field do you add?
- **Options**: A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **Correct**: B
- **Explanation**: The `allowed-tools` field in SKILL.md frontmatter scopes which tools the command can invoke.
- **Review**: Frontmatter fields reference

### Q10
- **Category**: conceptual
- **Question**: What is the `@file` syntax used for in a skill?
- **Options**: A) Importing another skill | B) Referencing a file to include its content in the prompt | C) Creating a symlink | D) Setting file permissions
- **Correct**: B
- **Explanation**: The `@path/to/file` syntax in a skill includes the referenced file's content into the prompt, allowing skills to pull in templates or context files.
- **Review**: File references section

---

## Lesson 02: Memory

### Q1
- **Category**: conceptual
- **Question**: How many levels does the Claude Code memory hierarchy have, and what has the highest priority?
- **Options**: A) 5 levels, User Memory is highest | B) 7 levels, Managed Policy is highest | C) 3 levels, Project Memory is highest | D) 7 levels, Auto Memory is highest
- **Correct**: B
- **Explanation**: The hierarchy has 7 levels: Managed Policy > Project Memory > Project Rules > User Memory > User Rules > Local Project Memory > Auto Memory. Managed Policy (set by admins) has the highest priority.
- **Review**: Memory hierarchy section

### Q2
- **Category**: practical
- **Question**: How do you quickly add a new rule to memory during a conversation?
- **Options**: A) Type `/memory add "rule text"` | B) Prefix your message with `#` (e.g., `# always use TypeScript`) | C) Type `/rule "rule text"` | D) Use `@add-memory "rule text"`
- **Correct**: B
- **Explanation**: The `#` prefix pattern allows quick single-rule additions during conversation. Claude will ask which memory level to save it to.
- **Review**: Quick memory updates section

### Q3
- **Category**: conceptual
- **Question**: What is the maximum depth for `@path/to/file` imports in CLAUDE.md?
- **Options**: A) 3 levels deep | B) 5 levels deep | C) 10 levels deep | D) Unlimited
- **Correct**: B
- **Explanation**: The `@import` syntax supports recursive imports up to a maximum depth of 5 to prevent infinite loops.
- **Review**: Import syntax section

### Q4
- **Category**: practical
- **Question**: How do you scope a rule file to only apply to files in `src/api/`?
- **Options**: A) Put the rule in `src/api/CLAUDE.md` | B) Add `paths: src/api/**` YAML frontmatter to a `.claude/rules/*.md` file | C) Name the file `.claude/rules/api.md` | D) Use `@scope: src/api` in the rule file
- **Correct**: B
- **Explanation**: Files in `.claude/rules/` support a `paths:` frontmatter field with glob patterns to scope rules to specific directories.
- **Review**: Path-specific rules section

### Q5
- **Category**: conceptual
- **Question**: How many lines of Auto Memory's MEMORY.md are loaded at session start?
- **Options**: A) All lines | B) First 100 lines | C) First 200 lines | D) First 500 lines
- **Correct**: C
- **Explanation**: The first 200 lines of MEMORY.md are auto-loaded into context at session start. Topic files referenced from MEMORY.md are loaded on demand.
- **Review**: Auto Memory section

### Q6
- **Category**: practical
- **Question**: You want personal project preferences that are NOT committed to git. Which file should you use?
- **Options**: A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **Correct**: B
- **Explanation**: `CLAUDE.local.md` in the project root is for personal project-specific preferences. It should be git-ignored.
- **Review**: Memory locations comparison

### Q7
- **Category**: conceptual
- **Question**: What does the `/init` command do?
- **Options**: A) Initializes a new Claude Code project from scratch | B) Generates a template CLAUDE.md based on your project structure | C) Resets all memory to defaults | D) Creates a new session
- **Correct**: B
- **Explanation**: `/init` analyzes your project and generates a template CLAUDE.md with suggested rules and standards. It's a one-time bootstrapping tool.
- **Review**: /init command section

### Q8
- **Category**: practical
- **Question**: How do you disable Auto Memory completely?
- **Options**: A) Delete the ~/.claude/projects directory | B) Set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) Add `auto-memory: false` to CLAUDE.md | D) Use `/memory disable auto`
- **Correct**: B
- **Explanation**: Setting `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` disables auto memory. Value `0` forces it on. Unset = default on.
- **Review**: Auto Memory configuration section

### Q9
- **Category**: conceptual
- **Question**: Can a lower-priority memory tier override rules from a higher-priority tier?
- **Options**: A) Yes, the most recent rule always wins | B) No, higher tiers always take precedence | C) Yes, if the lower tier uses the `!important` flag | D) It depends on the rule type
- **Correct**: B
- **Explanation**: Memory precedence flows downward from Managed Policy. Lower tiers (like Auto Memory) cannot override higher tiers (like Project Memory).
- **Review**: Memory hierarchy section

### Q10
- **Category**: practical
- **Question**: You work across two repositories and want Claude to load CLAUDE.md from both. What flag do you use?
- **Options**: A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **Correct**: B
- **Explanation**: The `--add-dir` flag loads CLAUDE.md from additional directories, allowing multi-repo context.
- **Review**: Additional directories section

---

## Lesson 03: Skills

### Q1
- **Category**: conceptual
- **Question**: What are the 3 levels of progressive disclosure in the skill system?
- **Options**: A) Metadata, instructions, resources | B) Name, body, attachments | C) Header, content, scripts | D) Summary, details, data
- **Correct**: A
- **Explanation**: Level 1: Metadata (~100 tokens, always loaded), Level 2: SKILL.md body (<5k tokens, loaded on trigger), Level 3: Bundled resources (scripts/references/assets, loaded on demand).
- **Review**: Progressive disclosure architecture section

### Q2
- **Category**: practical
- **Question**: What is the most important factor for a skill to be auto-invoked by Claude?
- **Options**: A) The skill's file name | B) The `description` field in frontmatter with when-to-use keywords | C) The skill's directory location | D) The `auto-invoke: true` frontmatter field
- **Correct**: B
- **Explanation**: Claude decides whether to auto-invoke a skill based solely on its `description` field. It must include specific trigger phrases and scenarios.
- **Review**: Auto-invocation section

### Q3
- **Category**: conceptual
- **Question**: What is the maximum recommended length for a SKILL.md file?
- **Options**: A) 100 lines | B) 250 lines | C) 500 lines | D) 1000 lines
- **Correct**: C
- **Explanation**: SKILL.md should be kept under 500 lines. Larger reference material belongs in `references/` subdirectory files.
- **Review**: Content guidelines section

### Q4
- **Category**: practical
- **Question**: How do you make a skill run in an isolated subagent with its own context?
- **Options**: A) Set `isolation: true` in frontmatter | B) Set `context: fork` with an `agent` field in frontmatter | C) Set `subagent: true` in frontmatter | D) Put the skill in `.claude/agents/`
- **Correct**: B
- **Explanation**: `context: fork` runs the skill in a separate context, and the `agent` field specifies which agent type (e.g., `Explore`, `Plan`, custom agent) to use.
- **Review**: Running skills in subagents section

### Q5
- **Category**: conceptual
- **Question**: What is the approximate context budget allocated to skill metadata (Level 1)?
- **Options**: A) 0.5% of context window | B) 1% of context window | C) 5% of context window | D) 10% of context window
- **Correct**: B
- **Explanation**: Skill metadata occupies about 1% of the context window (fallback: 8,000 characters). This is configurable with `SLASH_COMMAND_TOOL_CHAR_BUDGET`.
- **Review**: Context budget section

### Q6
- **Category**: practical
- **Question**: A skill needs to reference a large API specification. Where should you put it?
- **Options**: A) Inline in SKILL.md | B) In a `references/api-spec.md` file inside the skill directory | C) In the project's CLAUDE.md | D) In a separate `.claude/rules/` file
- **Correct**: B
- **Explanation**: Large reference material belongs in the `references/` subdirectory. Claude loads Level 3 resources on demand, keeping SKILL.md lean.
- **Review**: Supporting files structure section

### Q7
- **Category**: conceptual
- **Question**: What is the difference between Reference Content and Task Content in a skill?
- **Options**: A) Reference is read-only, Task is read-write | B) Reference adds knowledge to context, Task provides step-by-step instructions | C) Reference is for documentation, Task is for code | D) There is no difference
- **Correct**: B
- **Explanation**: Reference Content adds domain knowledge to Claude's context (e.g., brand guidelines). Task Content provides actionable step-by-step instructions for a workflow.
- **Review**: Skill content types section

### Q8
- **Category**: practical
- **Question**: What characters are allowed in the `name` field of a skill's frontmatter?
- **Options**: A) Any characters | B) Lowercase letters, numbers, and hyphens only (max 64 chars) | C) Letters and underscores | D) Alphanumeric only
- **Correct**: B
- **Explanation**: The name must be kebab-case (lowercase, hyphens), max 64 characters, and cannot contain "anthropic" or "claude".
- **Review**: SKILL.md format section

### Q9
- **Category**: conceptual
- **Question**: In what order does Claude search for skills?
- **Options**: A) User > Project > Enterprise | B) Enterprise > Personal > Project (plugin uses namespace) | C) Project > User > Enterprise | D) Alphabetical order
- **Correct**: B
- **Explanation**: Priority order is: Enterprise > Personal > Project. Plugin skills use a namespace (plugin-name:skill) so they don't conflict.
- **Review**: Skill types and locations section

### Q10
- **Category**: practical
- **Question**: How do you prevent Claude from automatically invoking a skill while still allowing users to use it manually?
- **Options**: A) Set `user-invocable: false` | B) Set `disable-model-invocation: true` | C) Remove the description field | D) Set `auto-invoke: false`
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` prevents Claude from auto-invoking but keeps the skill available in the user's `/` menu for manual use.
- **Review**: Controlling invocation section

---

## Lesson 04: Subagents

### Q1
- **Category**: conceptual
- **Question**: What is the main advantage of subagents over inline conversation?
- **Options**: A) They are faster | B) They operate in a separate, clean context window preventing context pollution | C) They can use more tools | D) They have better error handling
- **Correct**: B
- **Explanation**: Subagents get a fresh context window, receiving only what the main agent passes. This prevents the main conversation from being polluted with task-specific details.
- **Review**: Overview section

### Q2
- **Category**: practical
- **Question**: What is the priority order for agent definitions?
- **Options**: A) Project > User > CLI | B) CLI > Project > User | C) User > Project > CLI | D) They all have equal priority
- **Correct**: B
- **Explanation**: CLI-defined agents (`--agents` flag) override Project-level (`.claude/agents/`), which override User-level (`~/.claude/agents/`).
- **Review**: File locations section

### Q3
- **Category**: conceptual
- **Question**: Which built-in subagent uses the Haiku model and is optimized for read-only codebase exploration?
- **Options**: A) general-purpose | B) Plan | C) Explore | D) Bash
- **Correct**: C
- **Explanation**: The Explore subagent uses Haiku for fast, read-only codebase exploration. It supports three thoroughness levels: quick, medium, very thorough.
- **Review**: Built-in subagents section

### Q4
- **Category**: practical
- **Question**: How do you restrict which subagents a coordinator agent can spawn?
- **Options**: A) Use `allowed-agents:` field | B) Use `Task(agent_name)` syntax in the `tools` field | C) Set `spawn-limit: 2` | D) Use `restrict-agents: [name1, name2]`
- **Correct**: B
- **Explanation**: Adding `Task(worker, researcher)` in the tools field creates an allowlist — the agent can only spawn subagents named "worker" or "researcher".
- **Review**: Restrict spawnable subagents section

### Q5
- **Category**: conceptual
- **Question**: What does `isolation: worktree` do for a subagent?
- **Options**: A) Runs the agent in a Docker container | B) Gives the agent its own git worktree so changes don't affect the main tree | C) Prevents the agent from reading any files | D) Runs the agent in a sandbox
- **Correct**: B
- **Explanation**: Worktree isolation creates a separate git worktree. If the agent makes no changes, it auto-cleans up. If changes are made, the worktree path and branch are returned.
- **Review**: Worktree isolation section

### Q6
- **Category**: practical
- **Question**: How do you make a subagent run in the background?
- **Options**: A) Set `background: true` in the agent config | B) Use `async: true` in the agent config | C) Press Ctrl+D after starting it | D) Use `--background` CLI flag
- **Correct**: A
- **Explanation**: `background: true` in the agent configuration makes the subagent always run as a background task. Users can also use Ctrl+B to send a foreground task to background.
- **Review**: Background subagents section

### Q7
- **Category**: conceptual
- **Question**: What does the `memory` field with scope `project` do for a subagent?
- **Options**: A) Gives read access to the project CLAUDE.md | B) Creates a persistent memory directory scoped to the current project | C) Shares the main agent's conversation history | D) Loads the project's git history
- **Correct**: B
- **Explanation**: The `memory` field creates a persistent directory for the subagent. Scope `project` means the memory is tied to the current project. The first 200 lines of the agent's MEMORY.md auto-load.
- **Review**: Persistent memory section

### Q8
- **Category**: practical
- **Question**: How do you include a phrase in a subagent's description to encourage Claude to automatically delegate tasks to it?
- **Options**: A) Add "priority: high" | B) Include "use PROACTIVELY" or "MUST BE USED" in the description | C) Set `auto-delegate: true` | D) Add "trigger: always"
- **Correct**: B
- **Explanation**: Including phrases like "use PROACTIVELY" or "MUST BE USED" in the description strongly encourages Claude to automatically delegate matching tasks.
- **Review**: Automatic delegation section

### Q9
- **Category**: conceptual
- **Question**: What are the valid `permissionMode` values for a subagent?
- **Options**: A) read, write, admin | B) default, acceptEdits, bypassPermissions, plan, dontAsk, auto | C) safe, normal, dangerous | D) restricted, standard, elevated
- **Correct**: B
- **Explanation**: Subagents support six permission modes: default (prompts for everything), acceptEdits (auto-accepts file edits), bypassPermissions (skips all), plan (read-only), dontAsk (auto-denies unless pre-approved), auto (background classifier decides).
- **Review**: Configuration fields section

### Q10
- **Category**: practical
- **Question**: How do you resume a subagent that returned an agentId from a previous run?
- **Options**: A) Use `/resume agent-id` | B) Pass the `resume` parameter with the agentId when calling Task tool | C) Use `claude -r agent-id` | D) Subagents cannot be resumed
- **Correct**: B
- **Explanation**: Subagents can be resumed by passing the `resume` parameter with the previously returned agentId, continuing with full context preserved.
- **Review**: Resumable agents section

---

## Lesson 05: MCP

### Q1
- **Category**: conceptual
- **Question**: What are the three MCP transport protocols, and which is recommended?
- **Options**: A) HTTP (recommended), Stdio, SSE (deprecated) | B) WebSocket (recommended), REST, gRPC | C) TCP, UDP, HTTP | D) Stdio (recommended), HTTP, SSE
- **Correct**: A
- **Explanation**: HTTP is recommended for remote servers. Stdio is for local processes (most common currently). SSE is deprecated but still supported.
- **Review**: Transport protocols section

### Q2
- **Category**: practical
- **Question**: How do you add a GitHub MCP server via CLI?
- **Options**: A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **Correct**: B
- **Explanation**: Use `claude mcp add` with `--transport` flag, a name, and the server URL. For stdio: `claude mcp add github -- npx -y @modelcontextprotocol/server-github`.
- **Review**: MCP configuration management section

### Q3
- **Category**: conceptual
- **Question**: What happens when MCP tool descriptions exceed 10% of the context window?
- **Options**: A) They are truncated | B) Tool Search auto-enables to dynamically select relevant tools | C) Claude shows an error | D) Extra tools are disabled
- **Correct**: B
- **Explanation**: MCP Tool Search auto-enables when tools exceed 10% of context. It requires Sonnet 4 or Opus 4 minimum (Haiku not supported).
- **Review**: MCP Tool Search section

### Q4
- **Category**: practical
- **Question**: How do you use environment variable fallbacks in MCP config?
- **Options**: A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **Correct**: B
- **Explanation**: `${VAR:-default}` provides a fallback value if the environment variable is not set. `${VAR}` without fallback will error if not set.
- **Review**: Environment variable expansion section

### Q5
- **Category**: conceptual
- **Question**: What is the difference between MCP and Memory for data access?
- **Options**: A) MCP is faster, Memory is slower | B) MCP is for live/changing external data, Memory is for persistent/static preferences | C) MCP is for code, Memory is for text | D) They are interchangeable
- **Correct**: B
- **Explanation**: MCP connects to live, changing external data sources (APIs, databases). Memory stores persistent, static project context and preferences.
- **Review**: MCP vs Memory section

### Q6
- **Category**: practical
- **Question**: What happens when a team member first encounters a project-scoped `.mcp.json`?
- **Options**: A) It loads automatically | B) They get an approval prompt to trust the project's MCP servers | C) It's ignored unless they opt in via settings | D) Claude asks the admin to approve
- **Correct**: B
- **Explanation**: Project-scoped `.mcp.json` triggers a security approval prompt on each team member's first use. This is intentional — it prevents untrusted MCP servers.
- **Review**: MCP Scopes section

### Q7
- **Category**: conceptual
- **Question**: What does `claude mcp serve` do?
- **Options**: A) Starts an MCP server dashboard | B) Makes Claude Code itself act as an MCP server for other applications | C) Serves MCP documentation | D) Tests MCP server connections
- **Correct**: B
- **Explanation**: `claude mcp serve` turns Claude Code into an MCP server, enabling multi-agent orchestration where one Claude instance can be controlled by another.
- **Review**: Claude as MCP Server section

### Q8
- **Category**: practical
- **Question**: What is the default maximum output size for MCP tools?
- **Options**: A) 5,000 tokens | B) 10,000 tokens | C) 25,000 tokens | D) 50,000 tokens
- **Correct**: C
- **Explanation**: Default max is 25,000 tokens (`MAX_MCP_OUTPUT_TOKENS`). A warning appears at 10k tokens. Disk persistence caps at 50k characters.
- **Review**: MCP Output Limits section

### Q9
- **Category**: conceptual
- **Question**: When both `allowedMcpServers` and `deniedMcpServers` match a server in managed config, which wins?
- **Options**: A) Allowed wins | B) Denied wins | C) The last one configured wins | D) Both are applied independently
- **Correct**: B
- **Explanation**: In managed MCP configuration, deny rules always take precedence over allow rules.
- **Review**: Managed MCP Configuration section

### Q10
- **Category**: practical
- **Question**: How do you reference an MCP resource in a conversation?
- **Options**: A) Use `/mcp resource-name` | B) Use `@server-name:protocol://resource/path` mention syntax | C) Use `mcp.get("resource")` | D) Resources are auto-loaded
- **Correct**: B
- **Explanation**: MCP resources are accessed via `@server-name:protocol://resource/path` mention syntax in conversation.
- **Review**: MCP Resources section

---

## Lesson 06: Hooks

### Q1
- **Category**: conceptual
- **Question**: What are the four types of hooks in Claude Code?
- **Options**: A) Pre, Post, Error, and Filter hooks | B) Command, HTTP, Prompt, and Agent hooks | C) Before, After, Around, and Through hooks | D) Input, Output, Filter, and Transform hooks
- **Correct**: B
- **Explanation**: Command hooks run shell scripts, HTTP hooks call webhook endpoints, Prompt hooks use single-turn LLM evaluation, and Agent hooks use subagent-based verification.
- **Review**: Hook types section

### Q2
- **Category**: practical
- **Question**: A hook script exits with code 2. What happens?
- **Options**: A) Non-blocking warning shown | B) Blocking error — stderr is shown as an error to Claude, tool use is prevented | C) Hook is retried | D) Session ends
- **Correct**: B
- **Explanation**: Exit code 0 = success/continue, exit code 2 = blocking error (stderr shown as error), any other non-zero = non-blocking (stderr in verbose only).
- **Review**: Exit codes section

### Q3
- **Category**: conceptual
- **Question**: What JSON fields does a PreToolUse hook receive on stdin?
- **Options**: A) `tool_name` and `tool_output` | B) `session_id`, `tool_name`, `tool_input`, `hook_event_name`, `cwd`, and more | C) Only `tool_name` | D) The full conversation history
- **Correct**: B
- **Explanation**: Hooks receive a JSON object on stdin with: session_id, transcript_path, hook_event_name, tool_name, tool_input, tool_use_id, cwd, and permission_mode.
- **Review**: JSON input structure section

### Q4
- **Category**: practical
- **Question**: How can a PreToolUse hook modify the tool's input parameters before execution?
- **Options**: A) Return modified JSON on stderr | B) Return JSON with `updatedInput` field on stdout (exit code 0) | C) Write to a temp file | D) Hooks cannot modify inputs
- **Correct**: B
- **Explanation**: A PreToolUse hook can output JSON with `"updatedInput": {...}` on stdout (with exit 0) to modify the tool's parameters before Claude uses them.
- **Review**: PreToolUse output section

### Q5
- **Category**: conceptual
- **Question**: Which hook event supports `CLAUDE_ENV_FILE` for persisting environment variables into the session?
- **Options**: A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) All events
- **Correct**: C
- **Explanation**: Only SessionStart hooks can use `CLAUDE_ENV_FILE` to persist environment variables into the session.
- **Review**: SessionStart section

### Q6
- **Category**: practical
- **Question**: You want a hook that only runs once when a skill is first loaded, not on every tool call. What field do you add?
- **Options**: A) `run-once: true` | B) `once: true` in the component hook definition | C) `single: true` | D) `max-runs: 1`
- **Correct**: B
- **Explanation**: Component-scoped hooks (defined in SKILL.md or agent frontmatter) support `once: true` to run only on first activation.
- **Review**: Component-scoped hooks section

### Q7
- **Category**: conceptual
- **Question**: A Stop hook is defined in a subagent's frontmatter. What does it automatically convert to?
- **Options**: A) A PostToolUse hook | B) A SubagentStop hook | C) A SessionEnd hook | D) It stays as a Stop hook
- **Correct**: B
- **Explanation**: When a Stop hook is placed in a subagent's frontmatter, it auto-converts to SubagentStop so it runs when that specific subagent finishes.
- **Review**: Component-scoped hooks section

### Q8
- **Category**: practical
- **Question**: How do you match a hook to all MCP tools from a specific server?
- **Options**: A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"` (regex pattern) | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **Correct**: B
- **Explanation**: Use regex patterns for matchers. MCP tools follow the `mcp__server__tool` naming convention, so `mcp__github__.*` matches all GitHub MCP tools.
- **Review**: Matcher patterns section

### Q9
- **Category**: conceptual
- **Question**: How many hook events does Claude Code support in total?
- **Options**: A) 10 | B) 16 | C) 25 | D) 30
- **Correct**: C
- **Explanation**: Claude Code supports 25 hook events: PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, Stop, StopFailure, SubagentStop, SubagentStart, PermissionRequest, Notification, PreCompact, PostCompact, SessionStart, SessionEnd, WorktreeCreate, WorktreeRemove, ConfigChange, CwdChanged, FileChanged, TeammateIdle, TaskCompleted, TaskCreated, Elicitation, ElicitationResult, InstructionsLoaded.
- **Review**: Hook events table

### Q10
- **Category**: practical
- **Question**: You want to debug why a hook isn't firing. What's the best approach?
- **Options**: A) Add print statements to the hook script | B) Use `--debug` flag and `Ctrl+O` for verbose mode | C) Check the system log | D) Hooks don't have debugging tools
- **Correct**: B
- **Explanation**: The `--debug` flag and `Ctrl+O` verbose mode show hook execution details including which hooks fire, their inputs, and outputs.
- **Review**: Debugging section

---

## Lesson 07: Plugins

### Q1
- **Category**: conceptual
- **Question**: What is the core manifest file for a plugin and where does it live?
- **Options**: A) `plugin.yaml` in the root directory | B) `.claude-plugin/plugin.json` | C) `package.json` with a "claude" key | D) `.claude/plugin.md`
- **Correct**: B
- **Explanation**: The plugin manifest lives at `.claude-plugin/plugin.json` with required fields: name, description, version, author.
- **Review**: Plugin definition structure section

### Q2
- **Category**: practical
- **Question**: How do you test a plugin locally before publishing?
- **Options**: A) Use `/plugin test ./my-plugin` | B) Use `claude --plugin-dir ./my-plugin` | C) Use `claude plugin validate ./my-plugin` | D) Copy it to ~/.claude/plugins/
- **Correct**: B
- **Explanation**: The `--plugin-dir` flag loads a plugin from a local directory for testing. It's repeatable for loading multiple plugins.
- **Review**: Testing section

### Q3
- **Category**: conceptual
- **Question**: What environment variable is available inside plugin hooks and MCP configs to reference the plugin's installation directory?
- **Options**: A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **Correct**: B
- **Explanation**: `${CLAUDE_PLUGIN_ROOT}` resolves to the plugin's installed directory, enabling portable path references in hooks and MCP configs.
- **Review**: Plugin directory structure section

### Q4
- **Category**: practical
- **Question**: A plugin has a command called "check-security" in the "pr-review" plugin. How does a user invoke it?
- **Options**: A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **Correct**: B
- **Explanation**: Plugin commands use a `plugin-name:command-name` namespace to avoid conflicts with user commands and other plugins.
- **Review**: Plugin commands section

### Q5
- **Category**: conceptual
- **Question**: Which components can a plugin bundle?
- **Options**: A) Only commands and settings | B) Commands, agents, skills, hooks, MCP servers, LSP config, settings, templates, scripts | C) Only commands, hooks, and MCP servers | D) Only skills and agents
- **Correct**: B
- **Explanation**: Plugins can bundle: commands/, agents/, skills/, hooks/hooks.json, .mcp.json, .lsp.json, settings.json, templates/, scripts/, docs/, tests/.
- **Review**: Plugin directory structure section

### Q6
- **Category**: practical
- **Question**: How do you install a plugin from GitHub?
- **Options**: A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) `git clone` then `claude plugin register`
- **Correct**: B
- **Explanation**: Use `/plugin install github:username/repo` to install directly from a GitHub repository.
- **Review**: Installation methods section

### Q7
- **Category**: conceptual
- **Question**: What does the `settings.json` `agent` key do in a plugin?
- **Options**: A) Specifies authentication credentials | B) Sets the main thread agent for the plugin | C) Lists available subagents | D) Configures agent permissions
- **Correct**: B
- **Explanation**: The `agent` key in a plugin's settings.json specifies which agent definition to use as the main thread agent when the plugin is active.
- **Review**: Plugin Settings section

### Q8
- **Category**: practical
- **Question**: How do you manage plugin lifecycle (enable/disable/update)?
- **Options**: A) Edit a config file manually | B) Use `/plugin enable`, `/plugin disable`, `/plugin update plugin-name` | C) Use `claude plugin-manager` | D) Reinstall the plugin
- **Correct**: B
- **Explanation**: Claude Code provides slash commands for full lifecycle management: enable, disable, update, uninstall.
- **Review**: Installation methods section

### Q9
- **Category**: conceptual
- **Question**: What is the main advantage of a plugin over standalone skills/hooks/MCP?
- **Options**: A) Plugins are faster | B) Single-command install, versioned, marketplace distribution, bundles everything together | C) Plugins have more permissions | D) Plugins work offline
- **Correct**: B
- **Explanation**: Plugins package multiple components into one installable unit with versioning, marketplace distribution, and automatic updates — vs. manual setup of standalone components.
- **Review**: Standalone vs Plugin comparison section

### Q10
- **Category**: practical
- **Question**: Where do plugin hooks configuration live within the plugin directory?
- **Options**: A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` hooks section | D) `.claude/settings.json`
- **Correct**: B
- **Explanation**: Plugin hooks are configured in `hooks/hooks.json` within the plugin directory structure.
- **Review**: Plugin hooks section

---

## Lesson 08: Checkpoints

### Q1
- **Category**: conceptual
- **Question**: What four things do checkpoints capture?
- **Options**: A) Git commits, branches, tags, stashes | B) Messages, file modifications, tool usage history, session context | C) Code, tests, logs, configs | D) Inputs, outputs, errors, timing
- **Correct**: B
- **Explanation**: Checkpoints capture conversation messages, file modifications made by Claude's tools, tool usage history, and session context.
- **Review**: Overview section

### Q2
- **Category**: practical
- **Question**: How do you access the checkpoint browser?
- **Options**: A) Use `/checkpoints` command | B) Press `Esc + Esc` (double-escape) or use `/rewind` | C) Use `/history` command | D) Press `Ctrl+Z`
- **Correct**: B
- **Explanation**: Double-escape (Esc+Esc) or the `/rewind` command opens the checkpoint browser to select a restore point.
- **Review**: Accessing checkpoints section

### Q3
- **Category**: conceptual
- **Question**: How many rewind options are available, and what are they?
- **Options**: A) 3: Undo, Redo, Reset | B) 5: Restore code+conversation, Restore conversation, Restore code, Summarize from here, Never mind | C) 2: Full restore, Partial restore | D) 4: Code, Messages, Both, Cancel
- **Correct**: B
- **Explanation**: The 5 options are: Restore code and conversation (full rollback), Restore conversation only, Restore code only, Summarize from here (compress), Never mind (cancel).
- **Review**: Rewind options section

### Q4
- **Category**: practical
- **Question**: You used `rm -rf temp/` via Bash in Claude Code, then want to rewind. Will the checkpoint restore those files?
- **Options**: A) Yes, checkpoints capture everything | B) No, Bash filesystem operations (rm, mv, cp) are not tracked by checkpoints | C) Only if you used the Edit tool instead | D) Only if autoCheckpoint was enabled
- **Correct**: B
- **Explanation**: Checkpoints only track file changes made by Claude's tools (Write, Edit). Bash commands like rm, mv, cp operate outside checkpoint tracking.
- **Review**: Limitations section

### Q5
- **Category**: conceptual
- **Question**: How long are checkpoints retained?
- **Options**: A) Until session ends | B) 7 days | C) 30 days | D) Indefinitely
- **Correct**: C
- **Explanation**: Checkpoints persist across sessions for up to 30 days, after which they are automatically cleaned up.
- **Review**: Checkpoint persistence section

### Q6
- **Category**: practical
- **Question**: What does "Summarize from here" do when rewinding?
- **Options**: A) Deletes the conversation from that point | B) Compresses the conversation into an AI-generated summary while preserving the original in the transcript | C) Creates a bullet-point list of changes | D) Exports the conversation to a file
- **Correct**: B
- **Explanation**: Summarize compresses the conversation into a shorter AI-generated summary. The original full text is preserved in the transcript file.
- **Review**: Summarize option section

### Q7
- **Category**: conceptual
- **Question**: When are checkpoints created automatically?
- **Options**: A) Every 5 minutes | B) On every user prompt | C) Only when you manually save | D) After every tool use
- **Correct**: B
- **Explanation**: Automatic checkpoints are created with every user prompt, capturing the state before Claude processes the request.
- **Review**: Automatic checkpoints section

### Q8
- **Category**: practical
- **Question**: How do you disable automatic checkpoint creation?
- **Options**: A) Use `--no-checkpoints` flag | B) Set `autoCheckpoint: false` in settings | C) Delete the checkpoints directory | D) Checkpoints cannot be disabled
- **Correct**: B
- **Explanation**: Set `autoCheckpoint: false` in your configuration to disable automatic checkpoint creation (default is true).
- **Review**: Configuration section

### Q9
- **Category**: conceptual
- **Question**: Are checkpoints a replacement for git commits?
- **Options**: A) Yes, they're more powerful | B) No, they are complementary — checkpoints are session-scoped and expire, git is permanent and shareable | C) Yes, for small projects | D) Only in solo development
- **Correct**: B
- **Explanation**: Checkpoints are temporary (30-day retention), session-scoped, and cannot be shared. Git commits are permanent, auditable, and shareable. Use both together.
- **Review**: Integration with git section

### Q10
- **Category**: practical
- **Question**: You want to compare two different approaches. What's the recommended checkpoint workflow?
- **Options**: A) Create two separate sessions | B) Checkpoint before approach A, try it, rewind to checkpoint, try approach B, compare results | C) Use git branches instead | D) There's no good way to compare approaches
- **Correct**: B
- **Explanation**: The branching strategy: checkpoint at clean state, try approach A, note results, rewind to the same checkpoint, try approach B. Compare both outcomes.
- **Review**: Workflow patterns section

---

## Lesson 09: Advanced Features

### Q1
- **Category**: conceptual
- **Question**: What are the six permission modes in Claude Code?
- **Options**: A) read, write, execute, admin, root, sudo | B) default, acceptEdits, plan, auto, dontAsk, bypassPermissions | C) safe, normal, elevated, admin, unrestricted, god | D) view, edit, run, deploy, full, bypass
- **Correct**: B
- **Explanation**: The six modes are: default (prompts for everything), acceptEdits (auto-accepts file edits), plan (read-only analysis), auto (background classifier decides), dontAsk (auto-denies unless pre-approved), bypassPermissions (skips all checks).
- **Review**: Permission Modes section

### Q2
- **Category**: practical
- **Question**: How do you activate planning mode?
- **Options**: A) Only via `/plan` command | B) Via `/plan`, `Shift+Tab`/`Alt+M`, `--permission-mode plan` flag, or default config | C) Via `--planning` flag only | D) Planning is always on
- **Correct**: B
- **Explanation**: Planning mode can be activated multiple ways: /plan command, Shift+Tab/Alt+M keyboard shortcut, --permission-mode plan CLI flag, or as a default in config.
- **Review**: Planning Mode section

### Q3
- **Category**: conceptual
- **Question**: What does the `opusplan` model alias do?
- **Options**: A) Uses only Opus for everything | B) Uses Opus for planning phase and Sonnet for implementation | C) Uses a special planning-optimized model | D) Enables plan mode automatically
- **Correct**: B
- **Explanation**: `opusplan` is a model alias that uses Opus for the planning phase (higher quality analysis) and Sonnet for the execution phase (faster implementation).
- **Review**: Planning Mode section

### Q4
- **Category**: practical
- **Question**: How do you toggle extended thinking during a session?
- **Options**: A) Type `/think` | B) Press `Option+T` (macOS) or `Alt+T` | C) Use `--thinking` flag | D) It's always enabled and cannot be toggled
- **Correct**: B
- **Explanation**: Option+T (macOS) or Alt+T toggles extended thinking. It's enabled by default for all models. Opus 4.6 supports adaptive effort levels.
- **Review**: Extended Thinking section

### Q5
- **Category**: conceptual
- **Question**: Are "think" or "ultrathink" special keywords that activate enhanced thinking?
- **Options**: A) Yes, they activate deeper reasoning | B) No, they are treated as regular prompt text with no special behavior | C) Only "ultrathink" is special | D) They work only with Opus
- **Correct**: B
- **Explanation**: The documentation explicitly states these are regular prompt instructions, not special activation keywords. Extended thinking is controlled via Alt+T toggle and environment variables.
- **Review**: Extended Thinking section

### Q6
- **Category**: practical
- **Question**: How do you run Claude in a CI/CD pipeline with structured JSON output and a turn limit?
- **Options**: A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **Correct**: B
- **Explanation**: Print mode (`-p`) with `--output-format json` and `--max-turns` is the standard CI/CD integration pattern.
- **Review**: Headless/Print Mode section

### Q7
- **Category**: conceptual
- **Question**: What does the Task List feature (Ctrl+T) provide?
- **Options**: A) A list of running background processes | B) A persistent to-do list that survives context compaction, shareable via `CLAUDE_CODE_TASK_LIST_ID` | C) A history of past sessions | D) A queue of pending tool calls
- **Correct**: B
- **Explanation**: The Task List (Ctrl+T) is persistent across context compactions and can be shared across sessions via named task directories using `CLAUDE_CODE_TASK_LIST_ID`.
- **Review**: Task List section

### Q8
- **Category**: practical
- **Question**: How do you edit a plan externally (in your preferred editor) during planning mode?
- **Options**: A) Copy-paste from the terminal | B) Press `Ctrl+G` to open the plan in an external editor | C) Use `/export-plan` command | D) Plans can't be edited externally
- **Correct**: B
- **Explanation**: Ctrl+G opens the current plan in your configured external editor for modification.
- **Review**: Planning Mode section

### Q9
- **Category**: conceptual
- **Question**: What is the difference between `dontAsk` and `bypassPermissions` modes?
- **Options**: A) They are the same | B) `dontAsk` auto-denies unless pre-approved; `bypassPermissions` skips all checks entirely | C) `dontAsk` is for files; `bypassPermissions` is for commands | D) `bypassPermissions` is safer
- **Correct**: B
- **Explanation**: dontAsk auto-denies permission requests unless they match pre-approved patterns. bypassPermissions skips all safety checks entirely — it's dangerous for routine use.
- **Review**: Permission Modes section

### Q10
- **Category**: practical
- **Question**: How do you hand off a CLI session to the desktop app?
- **Options**: A) Use `/export` command | B) Use `/desktop` command | C) Copy the session ID and paste in the app | D) Sessions can't transfer between CLI and desktop
- **Correct**: B
- **Explanation**: The `/desktop` command hands off the current CLI session to the native desktop application for visual diff review and multi-session management.
- **Review**: Desktop App section

---

## Lesson 10: CLI Reference

### Q1
- **Category**: conceptual
- **Question**: What are the two primary modes of the Claude CLI?
- **Options**: A) Online and offline mode | B) Interactive REPL (`claude`) and Print mode (`claude -p`) | C) GUI and terminal mode | D) Single and batch mode
- **Correct**: B
- **Explanation**: Interactive REPL is the default conversational mode. Print mode (-p) is non-interactive, scriptable, pipeable — it exits after one response.
- **Review**: CLI architecture section

### Q2
- **Category**: practical
- **Question**: How do you pipe a file into Claude and get JSON output?
- **Options**: A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **Correct**: B
- **Explanation**: Pipe content via stdin to print mode (-p) and use --output-format json for structured output.
- **Review**: Interactive vs Print Mode section

### Q3
- **Category**: conceptual
- **Question**: What is the difference between `-c` and `-r` flags?
- **Options**: A) Both do the same thing | B) `-c` continues the most recent session; `-r` resumes by name or ID | C) `-c` creates a new session; `-r` resumes | D) `-c` is for code; `-r` is for review
- **Correct**: B
- **Explanation**: `-c/--continue` resumes the most recent conversation. `-r/--resume "name"` resumes a specific session by name or session ID.
- **Review**: Session management section

### Q4
- **Category**: practical
- **Question**: How do you guarantee schema-valid JSON output from Claude?
- **Options**: A) Just use `--output-format json` | B) Use `--output-format json --json-schema '{"type":"object",...}'` | C) Use `--strict-json` flag | D) JSON output is always schema-valid
- **Correct**: B
- **Explanation**: `--output-format json` alone produces best-effort JSON. Adding `--json-schema` with a JSON Schema definition guarantees the output matches the schema.
- **Review**: Output and format section

### Q5
- **Category**: conceptual
- **Question**: Which flag only works in print mode (-p) and has no effect in interactive mode?
- **Options**: A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **Correct**: B
- **Explanation**: `--system-prompt-file` loads a system prompt from a file but only works in print mode. Use `--system-prompt` (inline string) for interactive sessions.
- **Review**: System prompt flags comparison table

### Q6
- **Category**: practical
- **Question**: How do you restrict Claude to only use read-only tools for a security audit?
- **Options**: A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **Correct**: B
- **Explanation**: Combine `--permission-mode plan` (read-only analysis) with `--tools` (allowlist of specific tools) to restrict Claude to only read operations.
- **Review**: Tool and permission management section

### Q7
- **Category**: conceptual
- **Question**: What is the agent definition priority order?
- **Options**: A) Project > User > CLI | B) CLI > Project > User | C) User > CLI > Project | D) All are equal priority
- **Correct**: B
- **Explanation**: CLI-defined agents (--agents flag) have highest priority, then Project-level (.claude/agents/), then User-level (~/.claude/agents/).
- **Review**: Agents configuration section

### Q8
- **Category**: practical
- **Question**: How do you fork an existing session to try a different approach without losing the original?
- **Options**: A) Use `/fork` command | B) Use `--resume session-name --fork-session "branch name"` | C) Use `--clone session-name` | D) Use `/branch session-name`
- **Correct**: B
- **Explanation**: `--resume` with `--fork-session` creates a new independent branch from the resumed session, preserving the original conversation.
- **Review**: Session management section

### Q9
- **Category**: conceptual
- **Question**: What exit code does `claude auth status` return when the user is logged in?
- **Options**: A) 1 | B) 0 | C) 200 | D) It doesn't return an exit code
- **Correct**: B
- **Explanation**: `claude auth status` exits with code 0 when logged in, 1 when not. This makes it scriptable for CI/CD authentication checks.
- **Review**: CLI commands table

### Q10
- **Category**: practical
- **Question**: How do you process multiple files in a batch with Claude?
- **Options**: A) `claude --batch *.md` | B) Use a for loop: `for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) Batch processing is not supported
- **Correct**: B
- **Explanation**: Use shell for-loops with print mode to process files one at a time. Each invocation is independent and can produce structured output.
- **Review**: Batch processing section
