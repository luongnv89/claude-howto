# Topic-Specific Recommendations

Use these specific recommendations when a topic is a gap. Paths are relative to this reference file (`.claude/skills/self-assessment/references/`).

**Slash Commands (score 0)**:
- Tutorial: [01-slash-commands/](../../../../01-slash-commands/)
- Focus on: Built-in commands reference, creating your first SKILL.md, `$ARGUMENTS` syntax
- Key exercise: Create a `/optimize` command and test it
- Done when: You can create a custom skill with arguments and dynamic context

**Slash Commands (score 1 — review)**:
- Focus on: Dynamic context with `!`backtick`` syntax, `@file` references, `disable-model-invocation` vs `user-invocable` control
- Done when: You can create a skill that injects live command output and controls its own invocation behavior

**Memory (score 0)**:
- Tutorial: [02-memory/](../../../../02-memory/)
- Focus on: CLAUDE.md creation, `/init` and `/memory` commands, `#` prefix for quick updates
- Key exercise: Create a project CLAUDE.md with your coding standards
- Done when: Claude remembers your preferences across sessions

**Memory (score 1 — review)**:
- Focus on: the 7 memory locations and how they are concatenated into context (loaded root-down, not overridden), .claude/rules/ directory with path-specific rules, `@import` syntax (max depth 4), Auto Memory MEMORY.md (Claude loads its first 200 lines or 25 KB, whichever comes first — a load cap, not a file-size limit)
- Done when: You have modular rules for different directories and understand how every memory file is concatenated into context

**Skills (score 0)**:
- Tutorial: [03-skills/](../../../../03-skills/)
- Focus on: SKILL.md format, auto-invocation via description field, progressive disclosure (3 loading levels)
- Key exercise: Install the code-review skill and verify it auto-triggers
- Done when: A skill automatically activates based on conversation context

**Skills (score 1 — review)**:
- Focus on: `context: fork` with `agent` field for subagent execution, `disable-model-invocation` vs `user-invocable`, the skill-listing budget (1% of the context window, fallback 8,000 characters, 250 characters per entry), bundled resources (scripts/, references/, assets/)
- Done when: You can create a skill that runs in a subagent with forked context

**Hooks (score 0)**:
- Tutorial: [06-hooks/](../../../../06-hooks/)
- Focus on: Configuration structure (matcher + hooks array), PreToolUse/PostToolUse events, exit codes (0=success, 2=block), JSON input/output format
- Key exercise: Create a PreToolUse hook that validates Bash commands
- Done when: A hook blocks dangerous commands before execution

**Hooks (score 1 — review)**:
- Focus on: All 33 hook events (including PostToolUseFailure, StopFailure, TaskCreated, CwdChanged, FileChanged, PostCompact, Elicitation, ElicitationResult, Setup, UserPromptExpansion, MessageDisplay, PreModelSwitch, PostModelSwitch — the last two added in v2.1.251), 5 hook types (command, http, mcp_tool, prompt, agent — agent hooks are experimental and may change), component-scoped hooks in SKILL.md frontmatter, HTTP hooks with allowedEnvVars, `CLAUDE_ENV_FILE` for SessionStart/CwdChanged/FileChanged
- Done when: You can create a prompt-based Stop hook and a component-scoped hook in a skill

**MCP (score 0)**:
- Tutorial: [05-mcp/](../../../../05-mcp/)
- Focus on: `claude mcp add` command, transport types (`http` recommended, `stdio`, `ws` for push-style servers, and the deprecated `sse` — note `--transport` does not accept `ws`, so add WebSocket servers with `claude mcp add-json`), GitHub MCP setup, environment variable expansion
- Key exercise: Add GitHub MCP server and query PRs
- Done when: You can query live data from an external service via MCP

**MCP (score 1 — review)**:
- Focus on: Project-scope .mcp.json (requires team approval), OAuth 2.0 auth, MCP resources with `@server:resource` mentions, Tool Search (ENABLE_TOOL_SEARCH), `claude mcp serve`, output limits (10,000 tokens warning; 25,000 tokens default max via `MAX_MCP_OUTPUT_TOKENS`; 50,000 characters disk-persistence threshold)
- Done when: You have a project .mcp.json and understand Tool Search auto mode

**Subagents (score 0)**:
- Tutorial: [04-subagents/](../../../../04-subagents/)
- Focus on: Agent file format (.claude/agents/*.md), built-in agents (Explore, Plan, general-purpose, claude, statusline-setup, claude-code-guide), tools/model/permissionMode config, spawn limits (depth default 3 since v2.1.219, concurrency default 20, and the 200-per-session spawn cap removed in v2.1.224)
- Key exercise: Create a code-reviewer subagent and test delegation
- Done when: Claude delegates code review to your custom agent

**Subagents (score 1 — review)**:
- Focus on: Worktree isolation (`isolation: worktree`), persistent agent memory (`memory` field with scopes), background agents (Ctrl+B/Ctrl+F), agent allowlists with `Agent(agent_type)` (`Task(...)` remains a back-compat alias), agent teams (`--teammate-mode`)
- Done when: You have a subagent with persistent memory running in worktree isolation

**Checkpoints (score 0)**:
- Tutorial: [08-checkpoints/](../../../../08-checkpoints/)
- Focus on: Esc+Esc and /rewind access, 6 rewind options (restore code and conversation, restore conversation, restore code, summarize from here, summarize up to here, never mind), limitations — bash filesystem ops, subagent edits (except a foreground `context: fork` skill), edits made outside Claude Code, and symlinked/hardlinked paths are all untracked
- Key exercise: Make experimental changes, then rewind to restore
- Done when: You can confidently experiment knowing you can rewind

**Advanced Features (score 0)**:
- Tutorial: [09-advanced-features/](../../../../09-advanced-features/)
- Focus on: Planning mode (/plan or Shift+Tab), permission modes (6 types: manual — renamed from default in v2.1.200 — acceptEdits, plan, auto, dontAsk, bypassPermissions), extended thinking (Alt+T toggle)
- Key exercise: Use planning mode to design a feature, then implement it
- Done when: You can switch between planning and implementation modes fluently

**Advanced Features (score 1 — review)**:
- Focus on: Remote control (`claude --remote-control`, alias `--rc`), web sessions (`claude --cloud`; `--remote` is a deprecated alias), desktop handoff (`/desktop`), worktrees (`claude -w`), task lists (Ctrl+T), managed settings for enterprise
- Done when: You can hand off sessions between CLI, web, and desktop

**Plugins (score 0)**:
- Tutorial: [07-plugins/](../../../../07-plugins/)
- Focus on: Plugin structure (.claude-plugin/plugin.json), what plugins bundle (skills, agents, MCP, hooks, settings — plus the legacy `commands/` directory, which still works but `skills/` is preferred for new plugins), installation from marketplace
- Key exercise: Install a plugin and explore its components
- Done when: You understand when to use a plugin vs standalone components

**Plugins (score 1 — review)**:
- Focus on: Creating plugin.json manifest, plugin hooks (hooks/hooks.json), LSP configuration (.lsp.json), `${CLAUDE_PLUGIN_ROOT}` variable, --plugin-dir for testing, marketplace publishing
- Done when: You can create and test a plugin for your team

**CLI (score 0)**:
- Tutorial: [10-cli/](../../../../10-cli/)
- Focus on: Interactive vs print mode, `claude -p` with piping, `--output-format json`, session management (-c/-r)
- Key exercise: Pipe a file to `claude -p` and get JSON output
- Done when: You can use Claude non-interactively in a script

**CLI (score 1 — review)**:
- Focus on: --agents flag with JSON config, --json-schema for structured output, --fallback-model, --from-pr, --strict-mcp-config, batch processing with for loops, `claude mcp serve`
- Done when: You have a CI/CD script that uses Claude with structured JSON output

---

**Last Updated**: September 2, 2026
**Claude Code Version**: 2.1.257
**Sources**:
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/plugins-reference
