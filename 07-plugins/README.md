<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Plugins

This folder contains complete plugin examples that bundle multiple Claude Code features into cohesive, installable packages.

## Overview

Claude Code Plugins are bundled collections of customizations (slash commands, subagents, MCP servers, and hooks) that install with a single command. They represent the highest-level extension mechanism—combining multiple features into cohesive, shareable packages.

## Plugin Architecture

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|bundles| B
    A -->|bundles| C
    A -->|bundles| D
    A -->|bundles| E
    A -->|bundles| F
```

## Plugin Loading Process

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: Download plugin manifest
    Plugin-->>Claude: Return plugin definition
    Claude->>Install: Extract components
    Install->>SlashCmds: Configure
    Install->>Subagents: Configure
    Install->>MCPServers: Configure
    Install->>Hooks: Configure
    SlashCmds-->>Tools: Ready to use
    Subagents-->>Tools: Ready to use
    MCPServers-->>Tools: Ready to use
    Hooks-->>Tools: Ready to use
    Tools-->>Claude: Plugin installed ✅
```

> **No marketplace required (v2.1.157+)**: Plugins placed in `.claude/skills` directories now auto-load without a marketplace. Scaffold a new one with `claude plugin init <name>`, which creates it at `~/.claude/skills/<name>/` (user-global) and auto-loads it in the next session as `<name>@skills-dir`.

## Plugin Types & Distribution

| Type | Scope | Shared | Authority | Examples |
|------|-------|--------|-----------|----------|
| Official | Global | All users | Anthropic | PR Review, Security Guidance |
| Community | Public | All users | Community | DevOps, Data Science |
| Organization | Internal | Team members | Company | Internal standards, tools |
| Personal | Individual | Single user | Developer | Custom workflows |

## Plugin Definition Structure

Plugin manifest uses JSON format in `.claude-plugin/plugin.json`:

```json
{
  "name": "my-first-plugin",
  "description": "A greeting plugin",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "homepage": "https://example.com",
  "repository": "https://github.com/user/repo",
  "license": "MIT"
}
```

Beyond those identity fields, the manifest can point Claude Code at components that live somewhere other than the default folders, and carry discovery and dependency metadata:

| Field | Type | Description |
|-------|------|-------------|
| `workflows` | string \| array | Custom [workflow](https://code.claude.com/docs/en/workflows) script files or directories (replaces the default `workflows/`) |
| `outputStyles` | string \| array | Custom output style files or directories (replaces the default `output-styles/`) |
| `lspServers` | string \| array \| object | LSP servers for code intelligence — go to definition, find references, diagnostics. Commonly `"./.lsp.json"`. See [LSP server configuration](#lsp-server-configuration) |
| `channels` | array | Channel declarations for message injection (Telegram, Slack, Discord style) |
| `dependencies` | array | Other plugins this plugin requires, optionally with semver version constraints |
| `keywords` | array | Discovery tags used when browsing and searching marketplaces |
| `metadata` | object | Free-form object for your own data, such as entitlement or catalog fields |
| `experimental.themes` | string \| array | Color theme files or directories (replaces the default `themes/`) |
| `experimental.monitors` | string \| array | [Background Monitor](#background-monitors-v21105) configurations that start automatically when the plugin is active |

## Plugin Structure Example

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json       # Manifest (name, description, version, author)
├── commands/             # Skills as Markdown files
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/               # Custom agent definitions
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/               # Agent Skills with SKILL.md files
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/                # Event handlers in hooks.json
│   └── hooks.json
├── .mcp.json             # MCP server configurations
├── .lsp.json             # LSP server configurations for code intelligence
├── bin/                  # Executables added to Bash tool's PATH while plugin is enabled
├── settings.json         # Default settings applied when plugin is enabled (currently only `agent` key supported)
├── themes/               # Optional: ship custom Claude Code themes (v2.1.118+)
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

> **Note**: `commands/` is **legacy**. Official guidance is *"Use `skills/` for new plugins."* Existing `commands/` directories keep working — the three example plugins in this module ship one — but a new plugin should put its capabilities in `skills/` as `SKILL.md` directories instead of flat Markdown command files.

### LSP server configuration

Plugins can include Language Server Protocol (LSP) support for real-time code intelligence. LSP servers provide diagnostics, code navigation, and symbol information as you work.

**Configuration locations**:
- `.lsp.json` file in the plugin root directory
- The `lspServers` key in `plugin.json` — the official manifest field name. It accepts a string, an array, or an object: a string or array points at LSP config file(s) or directories (for example `"./.lsp.json"`), and an object declares the servers inline.

#### Field reference

| Field | Required | Description |
|-------|----------|-------------|
| `command` | Yes | LSP server binary (must be in PATH) |
| `extensionToLanguage` | Yes | Maps file extensions to language IDs |
| `args` | No | Command-line arguments for the server |
| `transport` | No | Communication method: `stdio` (default) or `socket` |
| `env` | No | Environment variables for the server process |
| `initializationOptions` | No | Options sent during LSP initialization |
| `settings` | No | Workspace configuration passed to the server |
| `workspaceFolder` | No | Override the workspace folder path |
| `startupTimeout` | No | Maximum time (ms) to wait for server startup |
| `shutdownTimeout` | No | Maximum time (ms) for graceful shutdown |
| `restartOnCrash` | No | Automatically restart if the server crashes |
| `maxRestarts` | No | Maximum restart attempts before giving up |

#### Example configurations

**Go (gopls)**:

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**Python (pyright)**:

```json
{
  "python": {
    "command": "pyright-langserver",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".py": "python",
      ".pyi": "python"
    }
  }
}
```

**TypeScript**:

```json
{
  "typescript": {
    "command": "typescript-language-server",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".ts": "typescript",
      ".tsx": "typescriptreact",
      ".js": "javascript",
      ".jsx": "javascriptreact"
    }
  }
}
```

#### Available LSP plugins

The official marketplace includes pre-configured LSP plugins:

| Plugin | Language | Server Binary | Install Command |
|--------|----------|---------------|----------------|
| `pyright-lsp` | Python | `pyright-langserver` | `pip install pyright` |
| `typescript-lsp` | TypeScript/JavaScript | `typescript-language-server` | `npm install -g typescript-language-server typescript` |
| `rust-lsp` | Rust | `rust-analyzer` | Install via `rustup component add rust-analyzer` |

#### LSP capabilities

Once configured, LSP servers provide:

- **Instant diagnostics** — errors and warnings appear immediately after edits
- **Code navigation** — go to definition, find references, implementations
- **Hover information** — type signatures and documentation on hover
- **Symbol listing** — browse symbols in the current file or workspace

### `bin/` directory on `PATH`

When a plugin is enabled, its `bin/` directory is prepended to the session's `PATH`. Any executable shipped there can be invoked directly from the Bash tool by name — no qualified path required.

```bash
# In a plugin layout:
my-plugin/
├── plugin.json
└── bin/
    └── my-tool          # executable file (chmod +x)

# Inside a Claude Code session with the plugin enabled:
$ my-tool --help
```

Use this for CLI helpers that hooks, skills, or commands inside the same plugin will shell out to. Mark the files executable in the plugin repo (`chmod +x`) — git preserves the bit.

## Plugin Options (v2.1.83+)

Plugins can declare user-configurable options in the manifest via `userConfig`. Values marked `sensitive: true` are stored in the system keychain rather than plain-text settings files:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "userConfig": {
    "apiKey": {
      "description": "API key for the service",
      "sensitive": true
    },
    "region": {
      "description": "Deployment region",
      "default": "us-east-1"
    }
  }
}
```

## Persistent Plugin Data (`${CLAUDE_PLUGIN_DATA}`) (v2.1.78+)

Plugins have access to a persistent state directory via the `${CLAUDE_PLUGIN_DATA}` environment variable. This directory is unique per plugin and survives across sessions, making it suitable for caches, databases, and other persistent state:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "command": "node ${CLAUDE_PLUGIN_DATA}/track-usage.js"
      }
    ]
  }
}
```

The directory is created automatically when the plugin is installed. Files stored here persist until the plugin is uninstalled.

### Background Monitors (v2.1.105)

Plugins can register background monitors that auto-arm when a session starts or when the plugin's skill is invoked. Add a top-level `monitors` key to your plugin manifest:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "monitors": [
    {
      "command": "tail -f /var/log/app.log",
      "trigger": "session_start"
    }
  ]
}
```

The `trigger` field accepts:
- `"session_start"` — arm the monitor automatically when a session begins
- `"skill_invoke"` — arm the monitor when the plugin's skill is invoked

Monitors use the same Monitor tool under the hood, streaming stdout lines as events Claude can react to.

## Inline Plugin via Settings (`source: 'settings'`) (v2.1.80+)

Plugins can be defined inline in settings files as marketplace entries using the `source: 'settings'` field. This allows embedding a plugin definition directly without requiring a separate repository or marketplace:

```json
{
  "pluginMarketplaces": [
    {
      "name": "inline-tools",
      "source": "settings",
      "plugins": [
        {
          "name": "quick-lint",
          "source": "./local-plugins/quick-lint"
        }
      ]
    }
  ]
}
```

## Plugin Settings

Plugins can ship a `settings.json` file to provide default configuration. This currently supports the `agent` key, which sets the main thread agent for the plugin:

```json
{
  "agent": "agents/specialist-1.md"
}
```

When a plugin includes `settings.json`, its defaults are applied on installation. Users can override these settings in their own project or user configuration.

## Standalone vs Plugin Approach

| Approach | Command Names | Configuration | Best For |
|----------|---------------|---|---|
| **Standalone** | `/hello` | Manual setup in CLAUDE.md | Personal, project-specific |
| **Plugins** | `/plugin-name:hello` | Automated via plugin.json | Sharing, distribution, team use |

Use **standalone slash commands** for quick personal workflows. Use **plugins** when you want to bundle multiple features, share with a team, or publish for distribution.

> **Spaced invocation (v2.1.136+)**: Plugin slash commands also work with a space — `/myplugin review` resolves to the canonical `/myplugin:review`. Either form is fine; the colon form is canonical and recommended in scripts.

> **`skills/` discovery (v2.1.136+)**: A `skills` entry in `plugin.json` no longer hides the plugin's default `skills/` directory. Skills declared in both places are merged, so you can list a few highlights in `plugin.json` without losing the rest.

> **Root-level `SKILL.md` plugins (v2.1.142+)**: A plugin with a top-level `SKILL.md` and **no `skills/` subdirectory** is itself surfaced as a single skill — the plugin *is* the skill. This is an additional pattern, not a replacement for the `skills/` directory or the `plugin.json` `skills` entry; use it for small single-skill plugins where the directory layout adds no value.

## Practical Examples

### Example 1: PR Review Plugin

**File:** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "repository": "https://github.com/your-org/pr-review",
  "license": "MIT"
}
```

**File:** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR Review

This command initiates a complete pull request review including:

1. Security analysis
2. Test coverage verification
3. Documentation updates
4. Code quality checks
5. Performance impact assessment
```

**File:** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: Read, Grep, Bash
---

# Security Reviewer

Specializes in finding security vulnerabilities:
- Authentication/authorization issues
- Data exposure
- Injection attacks
- Secure configuration
```

**Installation:**

```bash
/plugin install pr-review

# Result:
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

### Example 2: DevOps Plugin

**Components:**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

### Example 3: Documentation Plugin

**Bundled Components:**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

## Plugin Marketplace

The official Anthropic-managed plugin directory is `anthropics/claude-plugins-official`, auto-registered on first interactive launch. Enterprise admins can also create private plugin marketplaces for internal distribution.

There is also a **community marketplace**, `anthropics/claude-plugins-community`, hosting third-party plugins that have passed Anthropic's automated validation and safety screening — each pinned to a specific commit SHA in the catalog. Unlike the official marketplace you add it manually:

```bash
/plugin marketplace add anthropics/claude-plugins-community

# Then install from it using the claude-community marketplace name
/plugin install <plugin-name>@claude-community
```

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>anthropics/claude-plugins-official"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Private Registry"]

    A --> B
    A --> C
    A --> D

    B -->|Categories| B1["Development"]
    B -->|Categories| B2["DevOps"]
    B -->|Categories| B3["Documentation"]

    C -->|Search| C1["DevOps Automation"]
    C -->|Search| C2["Mobile Dev"]
    C -->|Search| C3["Data Science"]

    D -->|Internal| D1["Company Standards"]
    D -->|Internal| D2["Legacy Systems"]
    D -->|Internal| D3["Compliance"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#e8f5e9,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#fff3e0,stroke:#333,color:#333
```

### Marketplace Configuration

Enterprise and advanced users can control marketplace behavior through settings:

| Setting | Description |
|---------|-------------|
| `extraKnownMarketplaces` | Add additional marketplace sources beyond the defaults |
| `strictKnownMarketplaces` | Control which marketplaces users are allowed to add (managed-only) |
| `blockedMarketplaces` | Admin-managed blocklist of marketplaces (supports `hostPattern` / `pathPattern` regex fields since v2.1.119) |
| `deniedPlugins` | Admin-managed blocklist to prevent specific plugins from being installed |

> **Friendlier aliases (v2.1.232)**: `additionalMarketplaces` is accepted as an alias for
> `extraKnownMarketplaces`, and `allowedMarketplaces` for `strictKnownMarketplaces`.
> **Changelog-sourced** — the v2.1.232 changelog announces them, but the official settings
> reference does not yet list either name. The canonical keys are safe to keep using.

> **Owner wildcards (v2.1.223+)**: a `"owner/*"` entry allows or blocks every marketplace
> repo under one GitHub owner. **Accepted only in `strictKnownMarketplaces` and
> `blockedMarketplaces`.** Everywhere else a `github` source appears — including
> `extraKnownMarketplaces` and `/plugin marketplace add` — the `repo` value must name a
> single repository.

> **Enforcement** (v2.1.117+): `blockedMarketplaces` and `strictKnownMarketplaces` are enforced on every plugin lifecycle event — install, update, refresh, and autoupdate — not just at first add. `strictKnownMarketplaces` is managed-only.

Example `blockedMarketplaces` with host/path regex (v2.1.119):

```json
{
  "blockedMarketplaces": [
    {
      "hostPattern": "^evil\\.example\\.com$",
      "pathPattern": "^/marketplaces/.*"
    }
  ]
}
```

#### Marketplace `headersHelper` (v2.1.238)

A `url` marketplace — or an individual catalog entry — can name a `headersHelper` command that mints the HTTP headers used to fetch the catalog and any same-origin archives. This is how a private marketplace behind a token-issuing service authenticates without a static secret in the config.

A **catalog entry's** helper runs only on install or update, and only after its command has been shown to you: `claude plugin install` and `claude plugin update` prompt `[y/N]` before running it. Pass `-y` to accept without the prompt in automation.

### Additional Marketplace Features

- **Marketplace search bar (v2.1.172)**: When browsing a marketplace's plugins in `/plugin`, a search bar lets you filter the marketplace's plugins by name or keyword — handy for large marketplaces where scrolling the full list is slow.
- **Default git timeout**: Increased from 30s to 120s for large plugin repositories
- **Custom npm registries**: Plugins can specify custom npm registry URLs for dependency resolution
- **Version pinning**: Lock plugins to specific versions for reproducible environments
- **Projected context cost in the browse pane (v2.1.143)**: The `/plugin` marketplace browser shows each plugin's projected per-turn context-token cost — the sum of always-loaded skills, hooks, and MCP server descriptors. Use it to size plugin adoption before installing. The same projection is available post-install via [`claude plugin details <name>`](#claude-plugin-details-name-v21139).

Example browse row with the cost column:

```text
NAME              VERSION   AUTHOR     CTX/TURN   DESCRIPTION
code-reviewer     1.2.0     anthropic  +1,420     Multi-agent PR review
devops-toolkit    0.4.1     acme       +3,180     SRE playbooks, on-call helpers
docs-helper       0.9.0     community  +610       Doc-style guide enforcement
```

### Marketplace definition schema

Plugin marketplaces are defined in `.claude-plugin/marketplace.json`:

```json
{
  "name": "my-team-plugins",
  "owner": "my-org",
  "plugins": [
    {
      "name": "code-standards",
      "source": "./plugins/code-standards",
      "description": "Enforce team coding standards",
      "version": "1.2.0",
      "author": "platform-team"
    },
    {
      "name": "deploy-helper",
      "source": {
        "source": "github",
        "repo": "my-org/deploy-helper",
        "ref": "v2.0.0"
      },
      "description": "Deployment automation workflows"
    }
  ]
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Marketplace name in kebab-case |
| `owner` | Yes | Organization or user who maintains the marketplace |
| `plugins` | Yes | Array of plugin entries |
| `plugins[].name` | Yes | Plugin name (kebab-case) |
| `plugins[].source` | Yes | Plugin source (path string or source object) |
| `plugins[].description` | No | Brief plugin description |
| `plugins[].version` | No | Semantic version string |
| `plugins[].author` | No | Plugin author name |
| `plugins[].renames` | No | Maps a former plugin `name` to its current name (or `null` if removed) so users migrate automatically (v2.1.193) |
| `plugins[].displayName` | No | Human-readable name shown in the UI; not used for lookup (v2.1.143) |
| `plugins[].defaultEnabled` | No | If `false`, the plugin installs disabled until the user opts in (v2.1.154) |

### Plugin source types

Plugins can be sourced from multiple locations:

| Source | Syntax | Example |
|--------|--------|---------|
| **Relative path** | String path | `"./plugins/my-plugin"` |
| **GitHub** | `{ "source": "github", "repo": "owner/repo" }` | `{ "source": "github", "repo": "acme/lint-plugin", "ref": "v1.0" }` |
| **Git URL** | `{ "source": "url", "url": "..." }` | `{ "source": "url", "url": "https://git.internal/plugin.git" }` |
| **Git subdirectory** | `{ "source": "git-subdir", "url": "...", "path": "..." }` | `{ "source": "git-subdir", "url": "https://github.com/org/monorepo.git", "path": "packages/plugin" }` |
| **npm** | `{ "source": "npm", "package": "..." }` | `{ "source": "npm", "package": "@acme/claude-plugin", "version": "^2.0" }` |
| **pip** | `{ "source": "pip", "package": "..." }` | `{ "source": "pip", "package": "claude-data-plugin", "version": ">=1.0" }` |
| **Archive** (v2.1.224+) | `{ "source": "archive", "url": "..." }` | `{ "source": "archive", "url": "https://cdn.example.com/lint-plugin-1.2.0.zip", "sha256": "…" }` |
| **Command** (v2.1.229+) | `{ "source": "command", "command": "..." }` | `{ "source": "command", "command": "acme-plugin-resolver --print-dir" }` |

GitHub and git sources support optional `ref` (branch/tag) and `sha` (commit hash) fields for version pinning.

**Bare source names and `metadata.pluginRoot` (v2.1.239)**: a marketplace's `metadata.pluginRoot` now takes effect — a bare plugin source name in the catalog resolves to a directory under that root, instead of having to be spelled as a full relative path on every entry.

**Skills synced from claude.ai (v2.1.239)**: plugins synced down from claude.ai appear as `name@synced`. Address them that way in `claude plugin enable <name>@synced` and `claude plugin disable <name>@synced`. A synced plugin never overrides an installed plugin of the same name — the two coexist, distinguished by the `@synced` suffix.

#### `archive` source (v2.1.224+)

Install a plugin from a zip over HTTPS — no git clone, no npm install.

```json
{
  "source": "archive",
  "url": "https://cdn.example.com/lint-plugin-1.2.0.zip",
  "sha256": "3b1f0c2e9a7d4f5b8c6e1a2d3f4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b"
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `url` | Yes | **HTTPS only.** `http://`, loopback, link-local, and cloud-metadata hosts are rejected — and re-checked on **every redirect hop**, so a redirect cannot smuggle you onto a blocked host |
| `sha256` | No | 64 hex characters. On mismatch the install fails with `Plugin archive integrity check failed` |

Archives are capped at **256 MiB**. Pin `sha256` for anything you did not build yourself — without it, whoever controls the URL controls the code that runs in your session.

#### `command` source (v2.1.229+)

Let a locally installed tool decide where the plugin lives. Useful when an internal
package manager already knows how to fetch and lay out your plugins.

```json
{
  "source": "command",
  "command": "acme-plugin-resolver --print-dir",
  "timeout": 60,
  "mode": "copy"
}
```

The contract is strict: **the command must print exactly one line on stdout and exit with
code 0.** That line is the absolute path of a directory containing the complete plugin.

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| `command` | Yes | — | The command to run |
| `timeout` | No | `60` (seconds) | Maximum 600 |
| `mode` | No | `"copy"` | `"copy"` snapshots the directory; `"link"` symlinks it, so edits are live |

The command is re-resolved each session and the result is applied without a restart.
Organizations can block this source type entirely with `disableCommandPluginSources`.

Reserved marketplace names now include `first-party-plugins` and `healthcare` (v2.1.205) — these are held for official use and cannot be claimed by a custom marketplace.

### Distribution methods

**GitHub (recommended)**:
```bash
# Users add your marketplace
/plugin marketplace add owner/repo-name
```

**Other git services** (full URL required):
```bash
/plugin marketplace add https://gitlab.com/org/marketplace-repo.git
```

Bare `gitlab.com` repo URLs — including nested subgroups — clone the same way `github.com`
URLs do (v2.1.232). **The scheme is mandatory**: since v2.1.196 a bare
`gitlab.example.com/team/plugins` is rejected as an invalid `owner/repo` shorthand, so use
the full `https://gitlab.com/company/plugins.git` form. v2.1.232 also added GitLab
token-family secret redaction and gave the `glab` CLI the same sandbox and credential-path
protection `gh` already had.

**Private repositories**: Supported via git credential helpers or environment tokens. Users must have read access to the repository.

**Official marketplace submission**: Submit plugins to the Anthropic-curated marketplace for broader distribution via [claude.ai/settings/plugins/submit](https://claude.ai/settings/plugins/submit) or [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit).

### Managing Marketplaces

```bash
# Marketplace CLI commands
claude plugin marketplace add <source>       # Add marketplace (GitHub, URL, local)
claude plugin marketplace update [name]      # Refresh catalog index
claude plugin marketplace remove <name>      # Remove marketplace
claude plugin marketplace list               # List configured marketplaces
```

> **Important**: `marketplace update` only refreshes the plugin catalog (what's available to install). It does NOT update installed plugins. Use `plugin update <name>` to update specific installed plugins.

### Strict mode

Control how marketplace definitions interact with local `plugin.json` files:

| Setting | Behavior |
|---------|----------|
| `strict: true` (default) | Local `plugin.json` is authoritative; marketplace entry supplements it |
| `strict: false` | Marketplace entry is the entire plugin definition |

**Organization restrictions** with `strictKnownMarketplaces`:

| Value | Effect |
|-------|--------|
| Not set | No restrictions — users can add any marketplace |
| Empty array `[]` | Lockdown — no marketplaces allowed |
| Array of patterns | Allowlist — only matching marketplaces can be added |

```json
{
  "strictKnownMarketplaces": [
    "my-org/*",
    "github.com/trusted-vendor/*"
  ]
}
```

> **Warning**: In strict mode with `strictKnownMarketplaces`, users can only install plugins from allowlisted marketplaces. This is useful for enterprise environments requiring controlled plugin distribution.

## Plugin Installation & Lifecycle

```mermaid
graph LR
    A["Discover"] -->|Browse| B["Marketplace"]
    B -->|Select| C["Plugin Page"]
    C -->|View| D["Components"]
    D -->|Install| E["/plugin install"]
    E -->|Extract| F["Configure"]
    F -->|Activate| G["Use"]
    G -->|Check| H["Update"]
    H -->|Available| G
    G -->|Done| I["Disable"]
    I -->|Later| J["Enable"]
    J -->|Back| G
```

## Plugin Features Comparison

| Feature | Slash Command | Skill | Subagent | Plugin |
|---------|---------------|-------|----------|--------|
| **Installation** | Manual copy | Manual copy | Manual config | One command |
| **Setup Time** | 5 minutes | 10 minutes | 15 minutes | 2 minutes |
| **Bundling** | Single file | Single file | Single file | Multiple |
| **Versioning** | Manual | Manual | Manual | Automatic |
| **Team Sharing** | Copy file | Copy file | Copy file | Install ID |
| **Updates** | Manual | Manual | Manual | Auto-available |
| **Dependencies** | None | None | None | May include |
| **Marketplace** | No | No | No | Yes |
| **Distribution** | Repository | Repository | Repository | Marketplace |

## Plugin CLI Commands

All plugin operations are available as CLI commands:

```bash
claude plugin install <name>@<marketplace>   # Install from a marketplace
claude plugin uninstall <name>               # Remove a plugin
claude plugin update <name>                  # Update installed plugin to latest version
claude plugin list                           # List installed plugins
claude plugin enable <name>                  # Enable a disabled plugin
claude plugin disable <name>                 # Disable a plugin
claude plugin validate <path>                # Validate the plugin structure at <path>
claude plugin tag [path]                     # Create a {name}--v{version} release git tag (v2.1.118+)
claude plugin prune                          # Remove orphaned auto-installed plugin dependencies (v2.1.121+)
claude plugin uninstall <name> --prune       # Uninstall and cascade-clean orphaned dependencies (v2.1.121+)
claude plugin details <name>                 # Show inventory + projected per-turn token cost (v2.1.139+)
claude plugin init <name>                    # Scaffold a new plugin (alias: claude plugin new)
```

**Aliases**: `claude plugin new` for `init`, `remove` / `rm` for `uninstall`, `ls` for `list`, and `autoremove` for `prune`.

**Flags worth knowing:**

| Command | Flag | Purpose |
|---------|------|---------|
| `plugin init` | `--with <components...>` | Scaffold specific component folders: `skills`, `agents`, `hooks`, `mcp`, `lsp`, `output-style`, `channel` |
| `plugin init` | `-f`, `--force` | Overwrite an existing `.claude-plugin/` directory |
| `plugin install` | `--config <key=value>` | Set a `userConfig` option at install time |
| `plugin install` | `-y`, `--yes` | Accept commands without a confirmation prompt |
| `plugin list` | `--available` | Also list plugins available from marketplaces (requires `--json`) |
| `plugin tag` | `--push` | Push the tag to the remote after creating it |
| `plugin tag` | `--dry-run` | Print what would be tagged without creating the tag |
| `plugin validate` | `--strict` | Treat warnings as errors |
| `plugin validate` | `--json` | Emit a machine-readable validation report (v2.1.259+) |

Example: `claude plugin tag ./my-plugin` takes a **path** to the plugin (not a version string). It creates a `{name}--v{version}` git tag derived from `plugin.json`, validating that `plugin.json` and any enclosing marketplace entry agree, and is the recommended way to cut plugin releases for distribution.

`claude plugin prune` is useful after installing or uninstalling marketplace plugins that pulled in their own dependencies — it removes any auto-installed plugins whose parent plugin has since been removed. `plugin uninstall --prune` does the same cascade in a single step.

> **Dependency enforcement (v2.1.143)**: `claude plugin disable <name>` **refuses** if another enabled plugin still depends on the target (the dependency graph would break). `claude plugin enable <name>` **force-enables transitive dependencies** after a single confirmation prompt rather than requiring a separate enable for each. Use `claude plugin prune` to clean up dependencies whose dependents were later removed.

### `claude plugin details <name>` (v2.1.139+)

`claude plugin details <name>` prints the plugin's full component inventory — skills, hooks, MCP servers, LSP servers, background monitors, slash commands — plus a **projected per-turn (and per-invocation) token cost**. Use it to size a plugin before adopting it, especially on context-constrained models.

Example output (abbreviated):

```text
plugin: code-reviewer (1.2.0)
skills:        3      hooks: 2      mcp: 1      lsp: 0      monitors: 0
commands:      /review, /security-review
projected ctx: +1,420 tokens per turn  ·  +9,800 tokens per /review invocation
```

LSP servers were added to the details pane in v2.1.142. See also the marketplace browse pane's projected context cost (v2.1.143) covered in [Plugin Marketplace](#plugin-marketplace).

## Installation Methods

### From Marketplace
```bash
/plugin install plugin-name
# or from CLI:
claude plugin install plugin-name@marketplace-name
```

**Does it take effect right away?** Since **v2.1.221**, usually yes — read the last line of
the install summary:

| Install summary says | What it means |
|---|---|
| `Plugin is now active.` | Claude Code activated the plugin as part of the install. Nothing more to do. |
| `Run /reload-plugins to activate.` | The plugin is installed but not live yet — either activating it would have invalidated the prompt cache, or the activation attempt failed. |

Before v2.1.221, no install took effect in the current session until you ran
`/reload-plugins` or restarted, so older guides describe that step as unconditional.

### Enable / Disable (with auto-detected scope)
```bash
/plugin enable plugin-name
/plugin disable plugin-name
```

The `/plugin` interface surfaces unused plugins so you can clean them up (v2.1.187+). Enable/disable also works when a plugin's `plugin.json` `name` differs from its marketplace entry name (v2.1.195+).

### Listing installed plugins (v2.1.163)
Confirm which plugins are active in the current session:
```bash
/plugin list             # all installed plugins
/plugin list --enabled   # only enabled plugins
/plugin list --disabled  # only disabled plugins
```

### Local Plugin (for development)
```bash
# CLI flag for local testing (repeatable for multiple plugins)
claude --plugin-dir ./path/to/plugin
claude --plugin-dir ./plugin-a --plugin-dir ./plugin-b

# --plugin-dir also accepts a .zip archive path (v2.1.128+)
claude --plugin-dir ./my-plugin.zip

# Fetch a plugin .zip archive from a URL for the current session (v2.1.129+, repeatable)
claude --plugin-url https://example.com/releases/my-plugin-0.3.0.zip
```

### From Git Repository
```bash
/plugin install github:username/repo
```

## Auto-Update

Claude Code can automatically update marketplaces and their installed plugins at startup.

| Marketplace Type | Auto-Update Default | How to Toggle |
|------------------|---------------------|---------------|
| Official (`claude-plugins-official`) | ✅ Enabled | `/plugin` → Marketplaces → Select |
| Third-party / Local | ❌ Disabled | Same UI path |

When auto-update runs, Claude Code:
1. Refreshes marketplace catalog
2. Updates installed plugins to latest versions
3. Reports the outcome per plugin: `Plugin is now active.` when Claude Code activated it as part of the update, or `Run /reload-plugins to activate.` when it did not

### Environment Variables

| Variable | Effect |
|----------|--------|
| `DISABLE_AUTOUPDATER=1` | Disable all auto-updates (Claude Code + plugins) |
| `DISABLE_AUTOUPDATER=1` + `FORCE_AUTOUPDATE_PLUGINS=1` | Keep plugin updates, disable Claude Code updates |
| `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` | (v2.1.141+) Force `claude plugin install` to clone GitHub plugin sources over HTTPS instead of SSH, even when an SSH remote is available. Use in CI runners or containers without SSH keys. |

```bash
# Disable all auto-updates
export DISABLE_AUTOUPDATER=1

# Keep plugin auto-updates only
export DISABLE_AUTOUPDATER=1
export FORCE_AUTOUPDATE_PLUGINS=1

# CI runner without SSH keys — force HTTPS for plugin installs
export CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1
claude plugin install code-reviewer@anthropic
```

> **Remote session plugin loading (v2.1.179)**: Plugin loading performance in remote sessions was improved in v2.1.179, so plugins become available faster when you connect to a remote session.

## When to Create a Plugin

```mermaid
graph TD
    A["Should I create a plugin?"]
    A -->|Need multiple components| B{"Multiple commands<br/>or subagents<br/>or MCPs?"}
    B -->|Yes| C["✅ Create Plugin"]
    B -->|No| D["Use Individual Feature"]
    A -->|Team workflow| E{"Share with<br/>team?"}
    E -->|Yes| C
    E -->|No| F["Keep as Local Setup"]
    A -->|Complex setup| G{"Needs auto<br/>configuration?"}
    G -->|Yes| C
    G -->|No| D
```

### Plugin Use Cases

| Use Case | Recommendation | Why |
|----------|-----------------|-----|
| **Team Onboarding** | ✅ Use Plugin | Instant setup, all configurations |
| **Framework Setup** | ✅ Use Plugin | Bundles framework-specific commands |
| **Enterprise Standards** | ✅ Use Plugin | Central distribution, version control |
| **Quick Task Automation** | ❌ Use Command | Overkill complexity |
| **Single Domain Expertise** | ❌ Use Skill | Too heavy, use skill instead |
| **Specialized Analysis** | ❌ Use Subagent | Create manually or use skill |
| **Live Data Access** | ❌ Use MCP | Standalone, don't bundle |

## Testing a Plugin

Before publishing, test your plugin locally using the `--plugin-dir` CLI flag (repeatable for multiple plugins):

```bash
claude --plugin-dir ./my-plugin
claude --plugin-dir ./my-plugin --plugin-dir ./another-plugin

# --plugin-dir accepts .zip archives in addition to directories (v2.1.128+)
claude --plugin-dir ./my-plugin.zip

# --plugin-url fetches a plugin .zip from a URL for this session (v2.1.129+, repeatable)
claude --plugin-url https://example.com/releases/my-plugin-0.3.0.zip
```

This launches Claude Code with your plugin loaded, allowing you to:
- Verify all slash commands are available
- Test subagents and agents function correctly
- Confirm MCP servers connect properly
- Validate hook execution
- Check LSP server configurations
- Check for any configuration errors

## Hot-Reload

Plugins support hot-reload during development. When you modify plugin files, Claude Code can detect changes automatically. You can also force a reload with:

```bash
/reload-plugins
```

This re-reads all plugin manifests, commands, agents, skills, hooks, and MCP/LSP configurations without restarting the session.

## Managed Settings for Plugins

Administrators can control plugin behavior across an organization using managed settings:

| Setting | Description |
|---------|-------------|
| `enabledPlugins` | Allowlist of plugins that are enabled by default |
| `deniedPlugins` | Blocklist of plugins that cannot be installed |
| `extraKnownMarketplaces` | Add additional marketplace sources beyond the defaults |
| `strictKnownMarketplaces` | Restrict which marketplaces users are allowed to add (managed-only; enforced on every plugin lifecycle event since v2.1.117) |
| `blockedMarketplaces` | Blocklist of marketplaces; enforced on every plugin lifecycle event since v2.1.117; supports `hostPattern` / `pathPattern` regex fields since v2.1.119 |
| `allowedChannelPlugins` | Control which plugins are permitted per release channel |
| `disableCommandPluginSources` | Block the `command` plugin source type org-wide (v2.1.229+) |

> **Friendlier aliases (v2.1.232)**: `additionalMarketplaces` is accepted as an alias for
> `extraKnownMarketplaces`, and `allowedMarketplaces` for `strictKnownMarketplaces`.
> **Changelog-sourced** — the v2.1.232 changelog announces them, but the official settings
> reference does not yet list either name. The canonical keys are safe to keep using.

> **Owner wildcards (v2.1.223+)**: a `"owner/*"` entry allows or blocks every marketplace
> repo under one GitHub owner. **Accepted only in `strictKnownMarketplaces` and
> `blockedMarketplaces`.** Everywhere else a `github` source appears — including
> `extraKnownMarketplaces` and `/plugin marketplace add` — the `repo` value must name a
> single repository.

These settings can be applied at the organization level via managed configuration files and take precedence over user-level settings.

## Plugin Security

Plugin subagents run in a restricted sandbox. The following frontmatter keys are **not allowed** in plugin subagent definitions:

- `hooks` -- Subagents cannot register event handlers
- `mcpServers` -- Subagents cannot configure MCP servers
- `permissionMode` -- Subagents cannot override the permission model

This ensures that plugins cannot escalate privileges or modify the host environment beyond their declared scope.

## Publishing a Plugin

**Steps to publish:**

1. Create plugin structure with all components
2. Write `.claude-plugin/plugin.json` manifest
3. Create `README.md` with documentation
4. Test locally with `claude --plugin-dir ./my-plugin`
5. Tag the release with `claude plugin tag ./my-plugin` (v2.1.118+) — takes the plugin **path** and creates a `{name}--v{version}` git tag derived from `plugin.json`
6. Submit to plugin marketplace
7. Get reviewed and approved
8. Published on marketplace
9. Users can install with one command

**Example submission:**

```markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 slash commands for different review types
- 3 specialized subagents
- GitHub and CodeQL MCP integration
- Automated security scanning hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 2.1+
- GitHub access
- CodeQL (optional)
```

## Plugin vs Manual Configuration

**Manual Setup (2+ hours):**
- Install slash commands one by one
- Create subagents individually
- Configure MCPs separately
- Set up hooks manually
- Document everything
- Share with team (hope they configure correctly)

**With Plugin (2 minutes):**
```bash
/plugin install pr-review
# ✅ Everything installed and configured
# ✅ Ready to use immediately
# ✅ Team can reproduce exact setup
```

## Best Practices

### Do's ✅
- Use clear, descriptive plugin names
- Include comprehensive README
- Version your plugin properly (semver)
- Test all components together
- Document requirements clearly
- Provide usage examples
- Include error handling
- Tag appropriately for discovery
- Maintain backward compatibility
- Keep plugins focused and cohesive
- Include comprehensive tests
- Document all dependencies

### Don'ts ❌
- Don't bundle unrelated features
- Don't hardcode credentials
- Don't skip testing
- Don't forget documentation
- Don't create redundant plugins
- Don't ignore versioning
- Don't overcomplicate component dependencies
- Don't forget to handle errors gracefully

## Installation Instructions

### Installing from Marketplace

1. **Browse available plugins:**
   ```bash
   /plugin list
   ```

2. **View plugin details:**
   ```bash
   claude plugin details plugin-name
   ```

3. **Install a plugin:**
   ```bash
   /plugin install plugin-name
   ```

### Installing from Local Path

```bash
/plugin install ./path/to/plugin-directory
```

### Installing from GitHub

```bash
/plugin install github:username/repo
```

### Listing Installed Plugins

```bash
/plugin list             # all installed plugins
/plugin list --enabled   # only enabled plugins
/plugin list --disabled  # only disabled plugins
```

### Updating a Plugin

Use the CLI form — it is the one documented under [`plugin update`](https://code.claude.com/docs/en/plugins-reference) and the one Claude Code itself points you to when an update is available:

```bash
claude plugin update plugin-name
```

### Disabling/Enabling a Plugin

```bash
# Temporarily disable
/plugin disable plugin-name

# Re-enable
/plugin enable plugin-name
```

### Uninstalling a Plugin

```bash
/plugin uninstall plugin-name
```

## Related Concepts

The following Claude Code features work together with plugins:

- **[Slash Commands](../01-slash-commands/)** - Individual commands bundled in plugins
- **[Memory](../02-memory/)** - Persistent context for plugins
- **[Skills](../03-skills/)** - Domain expertise that can be wrapped into plugins
- **[Subagents](../04-subagents/)** - Specialized agents included as plugin components
- **[MCP Servers](../05-mcp/)** - Model Context Protocol integrations bundled in plugins
- **[Hooks](../06-hooks/)** - Event handlers that trigger plugin workflows

## Complete Example Workflow

### PR Review Plugin Full Workflow

```
1. User: /review-pr

2. Plugin executes:
   ├── pre-review.js hook validates git repo
   ├── GitHub MCP fetches PR data
   ├── security-reviewer subagent analyzes security
   ├── test-checker subagent verifies coverage
   └── performance-analyzer subagent checks performance

3. Results synthesized and presented:
   ✅ Security: No critical issues
   ⚠️  Testing: Coverage 65% (recommend 80%+)
   ✅ Performance: No significant impact
   📝 12 recommendations provided
```

## Troubleshooting

### Plugin Won't Install
- Check Claude Code version compatibility: `/version`
- Verify `plugin.json` syntax with a JSON validator
- Check internet connection (for remote plugins)
- Review permissions: `ls -la plugin/`

### Components Not Loading
- Verify paths in `plugin.json` match actual directory structure
- Check file permissions: `chmod +x scripts/`
- Review component file syntax
- Check the component inventory: `claude plugin details plugin-name`

### MCP Connection Failed
- Verify environment variables are set correctly
- Check MCP server installation and health
- Test MCP connection independently with `/mcp test`
- Review MCP configuration in `mcp/` directory

### Commands Not Available After Install
- Ensure plugin was installed successfully: `/plugin list`
- Check if plugin is enabled: `/plugin list --enabled`
- Check whether it's active yet — see the install summary guidance in [Installation Methods](#installation-methods): `Plugin is now active.` needs no action, `Run /reload-plugins to activate.` means run that command (a restart is not required)
- Check for naming conflicts with existing commands

### Hook Execution Issues
- Verify hook files have correct permissions
- Check hook syntax and event names
- Review hook logs for error details
- Test hooks manually if possible

## Additional Resources

- [Official Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Discover Plugins](https://code.claude.com/docs/en/discover-plugins)
- [Plugin Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference)
- [MCP Server Reference](https://modelcontextprotocol.io/)
- [Subagent Configuration Guide](../04-subagents/README.md)
- [Hook System Reference](../06-hooks/README.md)

---

**Last Updated**: September 6, 2026
**Claude Code Version**: 2.1.263
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/changelog#2-1-172
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/discover-plugins.md
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/releases/tag/v2.1.141
- https://github.com/anthropics/claude-code/releases/tag/v2.1.142
- https://github.com/anthropics/claude-code/releases/tag/v2.1.143
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/model-config
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
