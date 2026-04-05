[![GitHub Stars](https://img.shields.io/github/stars/TurokDSC/claude-mastery?style=flat&color=gold)](https://github.com/TurokDSC/claude-mastery/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/TurokDSC/claude-mastery?style=flat)](https://github.com/TurokDSC/claude-mastery/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.0.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# Claude Mastery

> From zero to orchestrating agents, hooks, skills, and MCP servers. Battle-tested configs from real production projects.

**By [TurokDSC](https://github.com/TurokDSC)** | Powering [HidenCloud](https://github.com/hidenenterprises) infrastructure

**[Quick Start](#-quick-start)** | **[Find Your Level](#-find-your-level)** | **[Feature Catalog](CATALOG.md)**

---

## Why This Exists

I built this while scaling HidenCloud's infrastructure across multiple projects — dashboards, game server panels, landing pages, and internal tools. Every config, hook, and agent in this repo has been tested in production.

This isn't theory. It's what actually works when you're managing:
- **Laravel dashboards** with automated code review pipelines
- **Pterodactyl panel** themes with security scanning
- **Nuxt/Next.js** frontends with CI/CD automation
- **Game server** infrastructure with DevOps automation

If you use Claude Code daily, this will save you hours.

---

## What's Inside

| Module | What You Get | Folder |
|--------|-------------|--------|
| **Slash Commands** | 8 production-ready commands (optimize, PR, docs, CI/CD) | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 3 CLAUDE.md templates (project, directory, personal) | [02-memory/](02-memory/) |
| **Skills** | 6 complete skills with scripts and templates | [03-skills/](03-skills/) |
| **Subagents** | 9 specialized agents (security, testing, docs, debugging) | [04-subagents/](04-subagents/) |
| **MCP** | 4 server configs (GitHub, database, filesystem, multi) | [05-mcp/](05-mcp/) |
| **Hooks** | 10 automation scripts (formatting, security, tracking) | [06-hooks/](06-hooks/) |
| **Plugins** | 3 complete plugins (PR review, DevOps, documentation) | [07-plugins/](07-plugins/) |
| **Checkpoints** | Guide + real examples for session management | [08-checkpoints/](08-checkpoints/) |
| **Advanced** | Planning mode, extended thinking, background tasks | [09-advanced-features/](09-advanced-features/) |
| **CLI** | Complete command-line reference | [10-cli/](10-cli/) |

**100+ files. Zero stubs. Everything production-ready.**

---

## Quick Start

```bash
# Clone
git clone https://github.com/TurokDSC/claude-mastery.git
cd claude-mastery

# Install slash commands
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/*.md /path/to/your-project/.claude/commands/

# Set up project memory
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# Install a skill
cp -r 03-skills/code-review ~/.claude/skills/

# Add subagents
cp 04-subagents/*.md /path/to/your-project/.claude/agents/

# Set up hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
cp 06-hooks/*.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/*
```

### Full Setup (1 hour)

```bash
# Everything at once
cp 01-slash-commands/*.md .claude/commands/
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp -r 03-skills/code-review ~/.claude/skills/
cp 04-subagents/*.md .claude/agents/
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh 06-hooks/*.py ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*
```

---

## Find Your Level

| Level | You Can... | Start Here | Time |
|-------|-----------|------------|------|
| **Beginner** | Start Claude Code and chat | [Slash Commands](01-slash-commands/) | ~2.5h |
| **Intermediate** | Use CLAUDE.md and custom commands | [Skills](03-skills/) | ~3.5h |
| **Advanced** | Configure MCP servers and hooks | [Advanced Features](09-advanced-features/) | ~5h |

### Full Learning Path

| # | Module | Level | Time |
|---|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/) | Beginner | 30 min |
| 2 | [Memory](02-memory/) | Beginner+ | 45 min |
| 3 | [Checkpoints](08-checkpoints/) | Intermediate | 45 min |
| 4 | [CLI Basics](10-cli/) | Beginner+ | 30 min |
| 5 | [Skills](03-skills/) | Intermediate | 1 hour |
| 6 | [Hooks](06-hooks/) | Intermediate | 1 hour |
| 7 | [MCP](05-mcp/) | Intermediate+ | 1 hour |
| 8 | [Subagents](04-subagents/) | Intermediate+ | 1.5 hours |
| 9 | [Advanced Features](09-advanced-features/) | Advanced | 2-3 hours |
| 10 | [Plugins](07-plugins/) | Advanced | 2 hours |

**[Complete Learning Roadmap ->](LEARNING-ROADMAP.md)**

---

## Real-World Workflows

These are actual workflows running in HidenCloud projects:

| Workflow | Features Combined |
|----------|------------------|
| **Automated Code Review** | Slash Commands + Subagents + Memory + MCP |
| **Team Onboarding** | Memory + Slash Commands + Plugins |
| **CI/CD Pipeline** | CLI + Hooks + Background Tasks |
| **API Documentation** | Skills + Subagents + Plugins |
| **Security Audits** | Subagents + Skills + Hooks (read-only) |
| **DevOps Deployment** | Plugins + MCP + Hooks + Background Tasks |
| **Safe Refactoring** | Checkpoints + Planning Mode + Hooks |

---

## My Stack

This guide is built from experience with:

- **Claude Opus 4.6 (1M context)** as primary model
- **22 custom skills** installed globally
- **8 specialized subagents** for different tasks
- **6 automation hooks** (security, formatting, logging, testing)
- **MCP servers**: memory, sequential-thinking, context7, playwright
- **Projects**: Laravel (HidenCloud Dash), Nuxt (HidenCloud Web), Pterodactyl (Panel), internal tools

---

## Feature Comparison

| Feature | Invocation | Persistence | Best For |
|---------|-----------|------------|----------|
| **Slash Commands** | Manual (`/cmd`) | Session only | Quick shortcuts |
| **Memory** | Auto-loaded | Cross-session | Long-term context |
| **Skills** | Auto-invoked | Filesystem | Automated workflows |
| **Subagents** | Auto-delegated | Isolated context | Task distribution |
| **MCP Protocol** | Auto-queried | Real-time | Live data access |
| **Hooks** | Event-triggered | Configured | Automation & validation |
| **Plugins** | One command | All features | Complete solutions |
| **Checkpoints** | Manual/Auto | Session-based | Safe experimentation |
| **Planning Mode** | Manual/Auto | Plan phase | Complex implementations |
| **Background Tasks** | Manual | Task duration | Long-running operations |

---

<details>
<summary>Installation Quick Reference</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
cp 06-hooks/*.py ~/.claude/hooks/
chmod +x ~/.claude/hooks/*

# Plugins
/plugin install pr-review

# Checkpoints (auto-enabled)
# See 08-checkpoints/README.md

# Advanced Features
# See 09-advanced-features/config-examples.json
```

</details>

<details>
<summary>Directory Structure</summary>

```
claude-mastery/
├── 01-slash-commands/     # 8 ready-to-use commands
├── 02-memory/             # 3 CLAUDE.md templates
├── 03-skills/             # 6 skills with scripts
│   ├── code-review/
│   ├── brand-voice/
│   ├── doc-generator/
│   ├── refactor/
│   ├── claude-md/
│   └── blog-draft/
├── 04-subagents/          # 9 specialized agents
├── 05-mcp/                # 4 server configurations
├── 06-hooks/              # 10 automation scripts
├── 07-plugins/            # 3 complete plugins
│   ├── pr-review/
│   ├── devops-automation/
│   └── documentation/
├── 08-checkpoints/        # Guide + examples
├── 09-advanced-features/  # Planning, thinking, config
├── 10-cli/                # CLI reference
├── scripts/               # EPUB builder + tests
├── prompts/               # Prompt templates
├── slides/                # Presentation materials
└── resources/             # Logos, icons, assets
```

</details>

<details>
<summary>Troubleshooting</summary>

### Feature Not Loading
1. Check file location and naming
2. Verify YAML frontmatter syntax
3. Check file permissions
4. Review Claude Code version compatibility

### MCP Connection Failed
1. Verify environment variables
2. Check MCP server installation
3. Test credentials
4. Review network connectivity

### Subagent Not Delegating
1. Check tool permissions
2. Verify agent description clarity
3. Review task complexity
4. Test agent independently

</details>

<details>
<summary>Offline Reading</summary>

Generate an EPUB ebook with all content:

```bash
uv run scripts/build_epub.py
```

</details>

<details>
<summary>Additional Resources</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

</details>

---

## FAQ

**Is this free?**
Yes. MIT licensed. Use it however you want.

**Does it work with Sonnet / Haiku / Opus?**
Yes. All templates work with Claude Sonnet 4.6, Opus 4.6, and Haiku 4.5.

**How long to go through everything?**
11-13 hours for the full path. But you get value in 15 minutes just by copying slash commands.

**Can I read it offline?**
Yes. Run `uv run scripts/build_epub.py` to generate an EPUB.

---

## License

MIT License - see [LICENSE](LICENSE).

---

**Maintained by [TurokDSC](https://github.com/TurokDSC)**
**Last Updated**: April 2026
**Claude Code Version**: 2.1+
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
