# Changelog

## [v2.1.145] — 2026-05-20

### Synced to Claude Code v2.1.145

Bumps tutorial coverage from Claude Code v2.1.143 → v2.1.145 (May 19, 2026
release). Anthropic shipped two patches (v2.1.144 and v2.1.145) since the last
sync. Highlights: the `/extra-usage` rename to `/usage-credits`, `/model`
becoming session-only by default, three new bundled skills (`/run`, `/verify`,
`/run-skill-generator`), Stop/SubagentStop hook input fields
`background_tasks` and `session_crons`, `claude agents --json` for scripting,
and a security fix that closes the bare-env-var Bash auto-approve loophole.
This sync also catches up six root-level reference docs
(`LEARNING-ROADMAP.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `resources.md`,
`claude_concepts_guide.md`, `STYLE_GUIDE.md`) that were missed in the
v2.1.143 sync and were still pinned to v2.1.138.

### Added

- `/usage-credits` slash command (v2.1.144) — replaces `/extra-usage` as the
  primary name; `/extra-usage` still works as an alias. Documented in
  `01-slash-commands/README.md` and `CATALOG.md`.
- Three new bundled skills (v2.1.145) — `/run` (launches the project's app to
  see a change running), `/verify` (builds, runs, and observes the app to
  confirm a fix works), `/run-skill-generator` (teaches `/run`/`/verify` how
  to handle a specific project by generating a per-project skill). Documented
  in `03-skills/README.md`, `CATALOG.md`, and `QUICK_REFERENCE.md`. Brings
  the canonical bundled-skill count to **9**.
- Stop/SubagentStop hook input fields `background_tasks` and `session_crons`
  (v2.1.145) — hook authors can read these to decide whether to block stop
  while background work or scheduled tasks are still pending. Documented in
  `06-hooks/README.md`.
- `claude agents --json` (v2.1.145) — print the agent list as machine-readable
  JSON for scripting (status bars, session pickers, tmux-resurrect).
  Documented in `10-cli/README.md`.
- Five hook-event rows that were missing from summary tables — `Setup`,
  `UserPromptExpansion`, `PermissionDenied`, `PostToolBatch` (the narrative
  already claimed "29 events"; the summary tables in `CATALOG.md`,
  `claude_concepts_guide.md`, and `INDEX.md` only listed 25).

### Behavior changes

- **`/model` is session-only by default (v2.1.144)**: selecting a model now
  applies only to the current session; press `d` after selecting to set the
  choice as the new default for future sessions. Documented in
  `01-slash-commands/README.md`.
- **Bash bare env-var auto-approve closed (v2.1.145 security fix)**: a
  command of the form `FOO=bar somecommand` is no longer auto-approved when
  only `FOO=bar` was on the allowlist. Re-allow such commands explicitly via
  `Bash(...)` permission rules that cover the full command. Documented in
  `06-hooks/README.md`.
- **`context: fork` infinite-loop fix (v2.1.145)**: a skill using
  `context: fork` could previously trigger an infinite re-invocation loop in
  rare cases. Documented as a note in `03-skills/README.md`.

### Documentation

- Caught up six root-level reference docs from v2.1.138 to v2.1.145:
  `LEARNING-ROADMAP.md`, `QUICK_REFERENCE.md`, `INDEX.md`, `resources.md`,
  `claude_concepts_guide.md`, `STYLE_GUIDE.md`.
- Fixed the bundled-skills mismatch — `CATALOG.md`, `QUICK_REFERENCE.md`, and
  `03-skills/README.md` previously listed three different 5-item lists;
  reconciled to the canonical 9 (`/batch`, `/claude-api`, `/debug`,
  `/fewer-permission-prompts`, `/loop`, `/run`, `/run-skill-generator`,
  `/simplify`, `/verify`). The `QUICK_REFERENCE.md` cell had also incorrectly
  listed `/voice` and `/browse` as bundled skills — neither is bundled.
- Renamed "New Features (March 2026)" → "New Features (May 2026)" in
  `QUICK_REFERENCE.md` and `resources.md` to match the rest of the repo.
- Bumped the version badge in `README.md` from `2.1.138` to `2.1.145` and
  updated the two "latest: v2.1.138" claims in the body.
- Updated the STYLE_GUIDE sample metadata footer from `2.1.97` to `2.1.145`
  so contributors copy the current version.

## [v2.1.143] — 2026-05-19

### Synced to Claude Code v2.1.143

Bumps tutorial coverage from Claude Code v2.1.138 → v2.1.143 (May 15, 2026
release). Anthropic shipped five patches (v2.1.139–v2.1.143) since the last
sync. Highlights: `/goal` and `/scroll-speed` slash commands, the `claude
agents` Agent View (Research Preview) with a full dispatch flag set, a Stop
hook safety cap, hook exec form (`args`), `continueOnBlock` for PostToolUse,
hook `terminalSequence` output, Fast Mode defaulting to Opus 4.7,
PowerShell-by-default on Windows for Bedrock/Vertex/Foundry, and the
`worktree.bgIsolation` setting.

### Added

- `/goal <statement>` slash command (v2.1.139) — registers a session-level
  completion condition with a live overlay panel showing elapsed time, turn
  count, and token usage. Documented in `01-slash-commands/README.md` and
  cross-linked from `10-cli/README.md`.
- `/scroll-speed <±N>` slash command (v2.1.139) — tunes TUI live-preview
  scroll speed; persists per-machine. Documented in
  `01-slash-commands/README.md`.
- `claude agents` Agent View (Research Preview, v2.1.139) with dispatch flags
  `--cwd` (v2.1.141), `--add-dir`, `--settings`, `--mcp-config`,
  `--plugin-dir`, `--permission-mode`, `--model`, `--effort`,
  `--dangerously-skip-permissions` (v2.1.142). Documented in
  `10-cli/README.md`.
- `claude plugin details <name>` (v2.1.139) — full plugin inventory plus
  projected per-turn/per-invocation token-cost estimate. LSP servers added
  to the details pane in v2.1.142. Documented in `07-plugins/README.md`.
- Marketplace context-cost projection in the `/plugin` browse pane (v2.1.143).
  Documented in `07-plugins/README.md`.
- Hook **exec form** (`args: string[]`, v2.1.139) — direct `execve()` spawn
  with no shell parsing; mutually exclusive with the shell-form `command`
  field. Documented in `06-hooks/README.md`.
- Hook `continueOnBlock: true` field on PostToolUse (v2.1.139) — surfaces a
  blocked tool result back to Claude as a `tool_result` instead of aborting
  the turn. Documented in `06-hooks/README.md`.
- Hook `terminalSequence` JSON output field (v2.1.141) — emits raw OSC escape
  sequences for desktop notifications, window titles, and bells. Documented
  in `06-hooks/README.md`.
- `worktree.bgIsolation: "none"` setting (v2.1.143) — background sessions
  edit the current working copy directly instead of an isolated worktree.
  Documented in `09-advanced-features/README.md`.
- `CLAUDE_PROJECT_DIR` is now passed to every MCP stdio server's environment
  (v2.1.139), and `${CLAUDE_PROJECT_DIR}` substitution is supported in plugin
  and project `.mcp.json` `command`/`args`/`env` fields. Documented in
  `05-mcp/README.md`.
- Subagent OTEL headers `x-claude-code-agent-id` and
  `x-claude-code-parent-agent-id` (v2.1.139), exposed as
  `agent_id` / `parent_agent_id` attributes on `claude_code.llm_request`
  OTEL spans. Documented in `04-subagents/README.md`.
- `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` (v2.1.142) — pin Fast Mode back
  to Opus 4.6 after the v2.1.142 default flipped to Opus 4.7. Documented in
  `10-cli/README.md`.
- `CLAUDE_CODE_USE_POWERSHELL_TOOL=0` and
  `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` (v2.1.143) — opt out of
  the default-on PowerShell tool, or make it honor the system execution
  policy instead of `-ExecutionPolicy Bypass`. Documented in
  `09-advanced-features/README.md`.
- `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` (v2.1.143) — override the 8-consecutive-
  blocks safety cap for Stop hooks (set `0` to disable). Documented in
  `06-hooks/README.md` and `09-advanced-features/README.md`.
- `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` (v2.1.141) — force plugin installs to
  clone GitHub plugin sources over HTTPS for CI runners without SSH keys.
  Documented in `07-plugins/README.md`.
- `ANTHROPIC_WORKSPACE_ID` (v2.1.141) — scopes a federated workload-identity
  token to a specific workspace. Documented in `09-advanced-features/README.md`.
- Root-level `SKILL.md` plugin pattern (v2.1.142) — a plugin with only a
  top-level `SKILL.md` (no `skills/` subdirectory) is surfaced as a single
  skill. Documented in `07-plugins/README.md`.
- Plugins marketing name **Routines** for `/schedule` (Anthropic blog,
  2026-05-14) — surfaced as a one-line note in
  `09-advanced-features/README.md`; the CLI surface remains `/schedule`.

### Behavior changes

- **Fast Mode default flipped to Opus 4.7 (v2.1.142)**: `/fast` now runs Opus
  4.7 by default (was Opus 4.6). Set `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`
  to opt back in.
- **PowerShell tool enabled by default on Windows for Bedrock/Vertex/Foundry
  (v2.1.143)**: Claude Code invokes PowerShell with `-ExecutionPolicy Bypass`.
  Opt out with `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1` (honor
  system policy) or `CLAUDE_CODE_USE_POWERSHELL_TOOL=0` (disable the tool).
- **Remote Control, `/schedule`, claude.ai MCP connectors, and notification
  preferences auto-disabled when API-key auth is set (v2.1.139)**: setting
  `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper` disables all
  four claude.ai-bridged surfaces, even if a claude.ai login is also active.
- **Stop hook block loops capped at 8 consecutive blocks (v2.1.143)**: the
  session ends with a warning after 8 in a row, preventing buggy Stop hooks
  from looping the session forever. Override with
  `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
- **`subagent_type` matching is now case- and separator-insensitive (v2.1.140)**:
  `code-reviewer`, `Code Reviewer`, and `code_reviewer` all resolve to the
  same agent. Documented in `04-subagents/README.md`.

### Changed

- Root reference docs (`README.md`, `CATALOG.md`) updated from `28 hook
  events` to `29 hook events` — matches `06-hooks/README.md` and
  `LEARNING-ROADMAP.md` after the `Setup` hook landed in v2.1.138.

### Notes for translators

- Tutorial translations (`vi/`, `ja/`, `uk/`, `zh/`) follow English; sync
  this round's deltas in module READMEs and the CHANGELOG above. Footers
  must reflect `Last Updated: May 19, 2026` and `Claude Code Version: 2.1.143`.

## [v2.1.138] — 2026-05-09

### Synced to Claude Code v2.1.138

Bumps tutorial coverage from Claude Code v2.1.131 → v2.1.138 (May 9, 2026
release). Anthropic shipped seven patches between v2.1.132 and v2.1.138 since
the last sync.

### Added (English docs)

- `worktree.baseRef` setting (v2.1.133) — controls whether `claude --worktree`
  branches from `origin/<default>` (`"fresh"`, default) or local `HEAD`
  (`"head"`). **Behavior change**: the `"fresh"` default reverts the v2.1.128
  behavior, so users who relied on local-`HEAD` branching after v2.1.128 must
  opt back in. Documented in `09-advanced-features/README.md`.
- `autoMode.hard_deny` admin key (v2.1.136) — array of classifier rules that
  block a class of actions regardless of inferred user intent. Use for
  actions that must never run in auto mode (e.g., `rm -rf /`, force-push to
  protected branches). Unlike `soft_deny`, hard-deny rules are not negotiable
  by the classifier. Documented in `09-advanced-features/README.md`.
- `parentSettingsBehavior` admin key (v2.1.133+, admin-tier) — controls how
  the SDK's `managedSettings` merges with parent-process settings.
  `"first-wins"` keeps existing precedence; `"merge"` deep-merges values.
  Documented in `09-advanced-features/README.md`.
- `Setup` hook event — initial environment setup (one-time per session); use
  to provision tooling or install deps. Brings the documented hook-events
  total from 28 to 29. Documented in `06-hooks/README.md`.
- `effort.level` field in hook input JSON (v2.1.133) — exposes the active
  effort level (`low`/`medium`/`high`/`xhigh`/`max`) to hooks. Documented in
  `06-hooks/README.md`.
- `CLAUDE_CODE_SESSION_ID` environment variable in Bash subprocesses
  (v2.1.132) — session UUID matching the `session_id` field in hook input
  JSON, for correlating bash logs with hook telemetry. Documented in
  `06-hooks/README.md`.
- `CLAUDE_EFFORT` environment variable in Bash subprocesses (v2.1.133) —
  active effort level, matching `effort.level` in hook input JSON. Documented
  in `06-hooks/README.md`.
- `sandbox.bwrapPath` and `sandbox.socatPath` settings (v2.1.133+, Linux/WSL)
  — point Claude Code at non-standard install locations for `bubblewrap` and
  `socat`. Default to `$PATH` lookup. Documented in
  `09-advanced-features/README.md`.
- `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` environment variable (v2.1.132).
  Documented in `09-advanced-features/README.md`.
- `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` environment variable
  (v2.1.136) — re-enables the session-quality survey for organizations
  capturing OpenTelemetry data; off by default in OTEL deployments.
  Documented in `09-advanced-features/README.md`.

### Changed

- **Behavior change**: Plan mode now blocks all file writes unconditionally
  (v2.1.136), including when a matching `Edit(...)` rule exists in
  `permissions.allow`. Previously a permissive `Edit(...)` rule could let
  writes through in plan mode; that bypass is closed. Workflows that
  depended on the older behavior must exit plan mode (`Shift+Tab`) before
  editing. Documented in `09-advanced-features/README.md`.
- Plugin spaced slash commands (e.g., `/myplugin review`) now resolve to
  `/myplugin:review`. Plugin `skills` config entries no longer hide the
  default `skills/` directory — both are merged. Documented in
  `07-plugins/README.md`.
- MCP servers now persist across `/clear` (v2.1.132+). Documented in
  `05-mcp/README.md`.
- Subagents discover project, user, and plugin skills via the Skill tool
  (v2.1.133). Documented in `04-subagents/README.md`.
- `--permission-mode` is now honored when resuming plan-mode sessions
  (v2.1.132). Documented in `09-advanced-features/README.md`.
- `CronList` output now includes the qualifier(s) and the scheduled prompt
  body (v2.1.136), so you can audit what each cron will run without opening
  it. Documented in `09-advanced-features/README.md`.

### Fixed

- OAuth refresh-token concurrent-refresh race condition.
- INDEX.md count drift: Skills 28 → 16, Plugins 40 → 27, Hooks scripts
  8 → 9 (recounted from the markdown content tree). The new totals reflect a
  `.md`-only methodology that scopes counts to tutorial content rather than
  build artifacts and config.
- Stale source URLs in `CATALOG.md` (v2.1.118 → v2.1.138) and
  `claude_concepts_guide.md` (v2.1.117 → v2.1.138). Removed a duplicate
  legacy footer in the concepts guide.

### Notes for translation maintainers

The `vi/`, `zh/`, `uk/`, and `ja/` localized trees are community-maintained
and may lag the English source. Contributors syncing translations should diff
against the English files updated in this release.

## [v2.1.131] — 2026-05-06

### Synced to Claude Code v2.1.131

Bumps tutorial coverage from Claude Code v2.1.126 → v2.1.131 (May 6, 2026
release). Anthropic shipped v2.1.128, v2.1.129, and v2.1.131 since the last
sync; v2.1.127 and v2.1.130 were skipped and never released publicly.

### Added (English docs)

- `--plugin-url <url>` flag (v2.1.129) — fetches a plugin `.zip` archive from
  a URL for the current session. Repeatable. Documented in
  `07-plugins/README.md`.
- `CLAUDE_CODE_FORCE_SYNC_OUTPUT` env var (v2.1.129) — forces synchronous
  output for terminals where auto-detection misses (e.g., Emacs `eat`).
  Documented in `10-cli/README.md` and `09-advanced-features/README.md`.
- `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` env var (v2.1.129) — enables
  background upgrades for Homebrew/WinGet installs (which normally do not
  auto-update). Documented in `10-cli/README.md` and
  `09-advanced-features/README.md`.
- `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` env var (v2.1.129) — required
  to opt in to `/v1/models` gateway discovery (see Changed). Documented in
  `10-cli/README.md`.
- `disableRemoteControl` setting (v2.1.128) — admins can block
  `claude remote-control` and `/remote-control` via managed/policy scope.
  Documented in `09-advanced-features/README.md`.
- `--plugin-dir` accepts `.zip` archives (v2.1.128) — alongside directory
  inputs. Documented in `07-plugins/README.md`.
- `skillOverrides` accepts `"name-only"` and `"user-invocable-only"`
  (v2.1.129) — in addition to the previous `"on"`/`"off"`. Documented in
  `03-skills/README.md`.

### Changed

- **Behavior change**: Gateway `/v1/models` discovery is now **opt-in**
  (v2.1.129). Previously (v2.1.126), setting `ANTHROPIC_BASE_URL` automatically
  populated `/model` from the gateway's `/v1/models` endpoint. From v2.1.129,
  users must additionally set `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`;
  without the env var, `/model` falls back to the built-in static list.
  Documented in `10-cli/README.md`.
- `/mcp` shows tool count per server and visually flags servers reporting 0
  tools (v2.1.128). Documented in `05-mcp/README.md`.
- Bare `/color` (no args) picks a random session color (v2.1.128); explicit
  `/color <name|hex>` continues to set a specific color. Documented in
  `01-slash-commands/README.md`.
- `--channels` flag now works with API-key (console) authentication
  (v2.1.128). Earlier releases required Pro/Max OAuth. Documented in
  `09-advanced-features/README.md`.
- Ctrl+R history picker defaults to **all prompts across all projects**
  (v2.1.129). Press Ctrl+S inside the picker to narrow scope to the current
  project. Documented in `09-advanced-features/README.md`.
- `/context` no longer dumps its ASCII visualization into the conversation
  (v2.1.129). The viz is shown in-UI only; no more ~1.6k token cost per
  invocation. Documented in `09-advanced-features/README.md`.
- Oversized images in drag-and-drop are auto-downscaled (v2.1.128) — earlier
  versions rejected images outright.

### Fixed

- VS Code extension activation on Windows (v2.1.131).
- Mantle endpoint authentication (v2.1.131).
- 1-hour prompt-cache TTL no longer truncated to 5 minutes (v2.1.129).
- Crash on stdin payloads larger than 10 MB (v2.1.128).

### Notes for translation maintainers

The `vi/`, `zh/`, `uk/`, and `ja/` localized trees are community-maintained
and may lag the English source. Contributors syncing translations should diff
against the English files updated in this release.

## [v2.1.126] — 2026-05-02

### Synced to Claude Code v2.1.126

Bumps tutorial coverage from Claude Code v2.1.119 → v2.1.126 (May 1, 2026 release).
v2.1.120 was rolled back on its first release day (2026-04-24) but re-released
successfully on 2026-04-28 with the originally-reported regressions fixed.
v2.1.124 and v2.1.125 were skipped by Anthropic and never released.

### Added (English docs)

- `claude project purge [path]` subcommand (v2.1.126) — deletes all Claude Code
  state for a project (transcripts, tasks, debug logs, file-edit history,
  prompt history, `~/.claude.json` entry). Supports `--dry-run`, `-y/--yes`,
  `-i/--interactive`, `--all`. Documented in `10-cli/README.md`.
- `claude plugin prune` subcommand (v2.1.121) — removes orphaned auto-installed
  plugin dependencies; `plugin uninstall --prune` cascades. Documented in
  `07-plugins/README.md`.
- `claude ultrareview [target]` subcommand (v2.1.120) — runs `/ultrareview`
  non-interactively from CI/scripts, prints findings to stdout, exits 0/1 on
  success/failure; supports `--json` and `--timeout <minutes>`. Documented in
  `10-cli/README.md`.
- `${CLAUDE_EFFORT}` placeholder available inside skill content (v2.1.120) —
  resolves to the current effort level. Documented in `03-skills/README.md`.
- `alwaysLoad` MCP server config option (v2.1.121) — when `true`, all tools
  from that server skip tool-search deferral. Documented in `05-mcp/README.md`.
- `PostToolUse.hookSpecificOutput.updatedToolOutput` now works for all tools
  (v2.1.121), previously MCP-only. Documented in `06-hooks/README.md`.
- `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable (v2.1.122) — selects
  Bedrock service tier (`default`, `flex`, `priority`). Documented in
  `10-cli/README.md` env-var table.
- `--dangerously-skip-permissions` extended-path coverage (v2.1.121, v2.1.126)
  — now bypasses prompts for writes to `.claude/skills/`, `.claude/agents/`,
  `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, shell config files.
  Catastrophic removal commands (`rm -rf /` etc.) still prompt. Documented in
  `09-advanced-features/README.md` permission-modes section.
- OAuth code paste fallback (v2.1.126) — `claude auth login` accepts the OAuth
  code pasted into the terminal when the browser callback can't reach
  localhost (WSL2, SSH, containers). Documented in `10-cli/README.md`.
- Type-to-filter `/skills` menu (v2.1.121). Documented in `03-skills/README.md`.
- `AI_AGENT` environment variable (v2.1.120) — set on subprocesses so `gh` can
  attribute traffic to Claude Code. Documented in `10-cli/README.md` env-var
  table.

### Changed

- `--from-pr` (v2.1.119) and `/resume` PR-URL search (v2.1.122) now both
  support GitHub, GitHub Enterprise, GitLab, and Bitbucket URLs.
- Windows: Git for Windows / Git Bash no longer required (v2.1.120) — Claude
  Code uses PowerShell as the shell tool when Git Bash is absent. From v2.1.126,
  PowerShell is the primary shell when the PowerShell tool is enabled. Detection
  extended to PowerShell 7 installed via Microsoft Store, MSI without PATH, or
  `.NET global tool`. Documented in `09-advanced-features/README.md` platform
  notes.
- `/model` picker now lists models from your gateway's `/v1/models` endpoint
  when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway
  (v2.1.126). Documented in `10-cli/README.md`.
- `--dangerously-skip-permissions` no longer prompts for writes to a much
  broader allowlist (see Added). Catastrophic removals still prompt.
- Image paste auto-downscale (v2.1.126) — images larger than 2000px are
  downscaled on paste; oversized images in history are auto-removed and the
  request retried. (Tutorial-relevant only as a safety/UX note.)

### Security

- Fixed `allowManagedDomainsOnly` / `allowManagedReadPathsOnly` being ignored
  when a higher-priority managed-settings source lacked a `sandbox` block
  (v2.1.126).

### Notes for translation maintainers

The `vi/`, `zh/`, `uk/`, and `ja/` localized trees are community-maintained
and may lag the English source. Contributors syncing translations should diff
against the English files updated in this release.

## [v2.4.0] — 2026-04-27

### Synced to Claude Code v2.1.119

Bumps tutorial coverage from Claude Code v2.1.112 → v2.1.119 (April 23, 2026 release).
v2.1.120 was published April 24, briefly rolled back the same day due to regressions,
and re-released on April 28 with fixes — it is now part of the normal release line.
A subsequent v2.1.126 (May 1, 2026) is the next stable target and is covered in the
v2.1.126 entry above.

### Added (English docs)

- Native binary packaging note (v2.1.113) — CLI now ships per-platform native binaries
- `bfs`/`ugrep` Glob/Grep substitution footnote on native macOS/Linux builds (v2.1.117)
- `mcp_tool` hook type with example (v2.1.118)
- `duration_ms` field on PostToolUse / PostToolUseFailure inputs (v2.1.119)
- `prUrlTemplate` setting (v2.1.119) and expanded `--from-pr` provider list (GitLab, Bitbucket)
- `cleanupPeriodDays` extended scope (checkpoints + tasks + shell-snapshots + backups, v2.1.117)
- Plugin marketplace enforcement on every lifecycle event (v2.1.117) and `hostPattern`/`pathPattern` regex (v2.1.119)
- New env vars: `DISABLE_UPDATES`, `CLAUDE_CODE_HIDE_CWD`, `CLAUDE_CODE_FORK_SUBAGENT`, `OTEL_LOG_TOOL_DETAILS`, `ENABLE_TOOL_SEARCH` Vertex opt-in
- New slash commands: `/btw`, `/theme` with custom themes
- `/usage` canonical command (merges `/cost` + `/stats`, v2.1.118)
- Forked subagents (`CLAUDE_CODE_FORK_SUBAGENT=1`, v2.1.117)
- Auto mode `"$defaults"` token (v2.1.118)
- `wslInheritsWindowsSettings` managed policy (v2.1.118)
- Vim visual / visual-line modes (v2.1.118)
- `claude install [version]` and `claude plugin tag` subcommands

### Changed

- Documentation host migrated: `docs.anthropic.com/en/docs/claude-code/*` → `code.claude.com/docs/en/*`
- Opus 4.7 effort levels: `xhigh` is now the Claude Code default since the 2026-04-16 launch; Opus 4.7 native context window confirmed at 1M (v2.1.117 fixed `/context` miscounting it as 200K)
- Default effort raised from `medium` to `high` for Pro/Max subscribers on Opus 4.6 / Sonnet 4.6 (v2.1.117)
- `STYLE_GUIDE.md` Source URL updated from Claude Apps article to `code.claude.com/docs/en/changelog`

### Deprecated (tracked, not removed)

- `includeCoAuthoredBy` setting → use `attribution.commit` / `attribution.pr`
- `voiceEnabled` setting → use `voice.enabled`

### Notes for translation maintainers

The `vi/`, `zh/`, and `uk/` localized trees are community-maintained and may lag the English source. Contributors syncing translations should diff against the English files updated in this release.

## v2.1.112 — 2026-04-16

### Highlights

- Sync all English tutorials with Claude Code v2.1.112 and the new Opus 4.7 model (`claude-opus-4-7`), including the new `xhigh` effort level (default on Opus 4.7, between `high` and `max`), two new built-in slash commands (`/ultrareview`, `/less-permission-prompts`), auto-mode no longer requiring `--enable-auto-mode` for Max subscribers on Opus 4.7, the PowerShell tool on Windows, the "Auto (match terminal)" theme, and plan files named after prompts. All 18 EN doc footers bumped to Claude Code v2.1.112. @Luong NGUYEN

### Features

- Add complete Ukrainian (uk) localization across all modules, root docs, examples, and references (039dde2) @Evgenij I

### Bug Fixes

- Correct pre-tool-check.sh hook protocol bugs (bce7cf8) @yarlinghe
- Change bad mermaid example to text block to pass CI (b8a7b1f) @Evgenij I
- Fix CP1251 encoding in Ukrainian claude_concepts_guide.md ToC (d970cc6) @Evgenij I
- Replace stub Ukrainian README with full translation, fix broken anchors (f6d73e2) @Evgenij I
- Correct Claude Code version to 2.1.97 across all footers (63a1416) @Luong NGUYEN
- Apply 2026-04-09 documentation accuracy updates (e015f39) @Luong NGUYEN

### Documentation

- Sync to Claude Code v2.1.112 (Opus 4.7, `xhigh` effort, `/ultrareview`, `/less-permission-prompts`, PowerShell tool, Auto-match-terminal theme) @Luong NGUYEN
- Sync to Claude Code v2.1.110 (TUI, push notifications, session recap) (15f0085) @Luong NGUYEN
- Sync to Claude Code v2.1.101 with `/team-onboarding`, `/ultraplan`, Monitor tool (2deba3a) @Luong NGUYEN
- Sync Vietnamese documentation with English source (561c6cb) @Thiên Toán
- Update Last Updated date and Claude Code version across all files (7f2e773) @Luong NGUYEN
- Add Ukrainian language link to language switcher (9c224ff) @Luong NGUYEN
- Remove contributors section (f07313d) @Luong NGUYEN
- Update GitHub metrics to 21,800+ stars, 2,585+ forks (4f55374) @Luong NGUYEN

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.3.0...v2.1.112

---

## v2.3.0 — 2026-04-07

### Features

- build and publish EPUB artifacts per language (90e9c30) @Thiên Toán
- add missing pre-tool-check.sh hook to 06-hooks (b511ed1) @JiayuWang
- add Chinese translations in zh/ directory (89e89d4) @Luong NGUYEN
- Add performance-optimizer subagent and dependency-check hook (f53d080) @qk

### Bug Fixes

- Windows Git Bash compatibility + stdin JSON protocol (2cbb10c) @Luong NGUYEN
- correct autoCheckpoint config documentation in 08-checkpoints (749c79f) @JiayuWang
- embed SVG images instead of replacing with placeholders (1b16709) @Thiên Toán
- nested code fence rendering in memory README (ce24423) @Zhaoshan Duan
- apply review fixes dropped by squash merge (34259ca) @Luong NGUYEN
- make hook scripts compatible with Windows Git Bash and use stdin JSON protocol (107153d) @binyu li

### Documentation

- sync all tutorials with latest Claude Code docs (April 2026) (72d3b01) @Luong NGUYEN
- add Chinese language link to language switcher (6cbaa4d) @Luong NGUYEN
- add language switcher between English and Vietnamese (100c45e) @Luong NGUYEN
- add GitHub #1 Trending badge (0ca8c37) @Luong NGUYEN
- Introduce cc-context-stats for context zone monitoring (d41b335) @Luong NGUYEN
- Introduce luongnv89/skills collection and luongnv89/asm skill manager (7e3c0b6) @Luong NGUYEN
- Update README stats to reflect current GitHub metrics (5,900+ stars, 690+ forks) (5001525) @Luong NGUYEN
- Update README stats to reflect current GitHub metrics (3,900+ stars, 460+ forks) (9cb92d6) @Luong NGUYEN

### Refactoring

- replace Kroki HTTP dependency with local mmdc rendering (e76bbe4) @Luong NGUYEN
- shift quality checks to pre-commit, CI as 2nd pass (6d1e0ae) @Luong NGUYEN
- narrow auto-mode permissions baseline (2790fb2) @Luong NGUYEN
- Replace auto-adapt hook with one-time permissions setup script (995a5d6) @Luong NGUYEN

### Other

- shift-left quality gates — add mypy to pre-commit, fix CI failures (699fb39) @Luong NGUYEN
- Add Vietnamese (Tiếng Việt) Localization (a70777e) @Thiên Toán

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — 2026-03-26

### Documentation

- Sync all tutorials and references with Claude Code v2.1.84 (f78c094) @luongnv89
  - Update slash commands to 55+ built-in + 5 bundled skills, mark 3 deprecated
  - Expand hook events from 18 to 25, add `agent` hook type (now 4 types)
  - Add Auto Mode, Channels, Voice Dictation to advanced features
  - Add `effort`, `shell` skill frontmatter fields; `initialPrompt`, `disallowedTools` agent fields
  - Add WebSocket MCP transport, elicitation, 2KB tool cap
  - Add plugin LSP support, `userConfig`, `${CLAUDE_PLUGIN_DATA}`
  - Update all reference docs (CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX)
- Rewrite README as landing-page-structured guide (32a0776) @luongnv89

### Bug Fixes

- Add missing cSpell words and README sections for CI compliance (93f9d51) @luongnv89
- Add `Sandboxing` to cSpell dictionary (b80ce6f) @luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug Fixes

- Remove dead marketplace link failing CI link checks (3fdf0d6) @luongnv89
- Add `sandboxed` and `pycache` to cSpell dictionary (dc64618) @luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Features

- Add adaptive learning path with self-assessment and lesson quiz skills (1ef46cd) @luongnv89
  - `/self-assessment` — interactive proficiency quiz across 10 feature areas with personalized learning path
  - `/lesson-quiz [lesson]` — per-lesson knowledge check with 8-10 targeted questions

### Bug Fixes

- Update broken URLs, deprecations, and outdated references (8fe4520) @luongnv89
- Fix broken links in resources and self-assessment skill (7a05863) @luongnv89
- Use tilde fences for nested code blocks in concepts guide (5f82719) @VikalpP
- Add missing words to cSpell dictionary (8df7572) @luongnv89

### Documentation

- Phase 5 QA — fix consistency, URLs, and terminology across docs (00bbe4c) @luongnv89
- Complete Phases 3-4 — new feature coverage and reference doc updates (132de29) @luongnv89
- Add MCPorter runtime to MCP context bloat section (ef52705) @luongnv89
- Add missing commands, features, and settings across 6 guides (4bc8f15) @luongnv89
- Add style guide based on existing repo conventions (84141d0) @luongnv89
- Add self-assessment row to guide comparison table (8fe0c96) @luongnv89
- Add VikalpP to contributors list for PR #7 (d5b4350) @luongnv89
- Add self-assessment and lesson-quiz skill references to README and roadmap (d5a6106) @luongnv89

### New Contributors

- @VikalpP made their first contribution in #7

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Features

- Sync all documentation with Claude Code February 2026 features (487c96d)
  - Update 26 files across all 10 tutorial directories and 7 reference documents
  - Add documentation for **Auto Memory** — persistent learnings per project
  - Add documentation for **Remote Control**, **Web Sessions**, and **Desktop App**
  - Add documentation for **Agent Teams** (experimental multi-agent collaboration)
  - Add documentation for **MCP OAuth 2.0**, **Tool Search**, and **Claude.ai Connectors**
  - Add documentation for **Persistent Memory** and **Worktree Isolation** for subagents
  - Add documentation for **Background Subagents**, **Task List**, **Prompt Suggestions**
  - Add documentation for **Sandboxing** and **Managed Settings** (Enterprise)
  - Add documentation for **HTTP Hooks** and 7 new hook events
  - Add documentation for **Plugin Settings**, **LSP Servers**, and Marketplace updates
  - Add documentation for **Summarize from Checkpoint** rewind option
  - Document 17 new slash commands (`/fork`, `/desktop`, `/teleport`, `/tasks`, `/fast`, etc.)
  - Document new CLI flags (`--worktree`, `--from-pr`, `--remote`, `--teleport`, `--teammate-mode`, etc.)
  - Document new environment variables for auto memory, effort levels, agent teams, and more

### Design

- Redesign logo to compass-bracket mark with minimal palette (20779db)

### Bug Fixes / Corrections

- Update model names: Sonnet 4.5 → **Sonnet 4.6**, Opus 4.5 → **Opus 4.6**
- Fix permission mode names: replace fictional "Unrestricted/Confirm/Read-only" with actual `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`
- Fix hook events: remove fictional `PreCommit`/`PostCommit`/`PrePush`, add real events (`SubagentStart`, `WorktreeCreate`, `ConfigChange`, etc.)
- Fix CLI syntax: replace `claude-code --headless` with `claude -p` (print mode)
- Fix checkpoint commands: replace fictional `/checkpoint save/list/rewind/diff` with actual `Esc+Esc` / `/rewind` interface
- Fix session management: replace fictional `/session list/new/switch/save` with real `/resume`/`/rename`/`/fork`
- Fix plugin manifest format: migrate `plugin.yaml` → `.claude-plugin/plugin.json`
- Fix MCP config paths: `~/.claude/mcp.json` → `.mcp.json` (project) / `~/.claude.json` (user)
- Fix documentation URLs: `docs.claude.com` → `docs.anthropic.com`; remove fictional `plugins.claude.com`
- Remove fictional configuration fields across multiple files
- Update all "Last Updated" dates to February 2026

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
