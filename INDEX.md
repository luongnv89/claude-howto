<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - Complete Index

This document provides a complete index of all example files organized by feature type.

## Summary Statistics

- **Total Files**: 100+ files
- **Categories**: 10 feature categories
- **Plugins**: 3 complete plugins
- **Skills**: 6 complete skills
- **Hooks**: 8 example hooks
- **Ready to Use**: All examples

---

## 01. Slash Commands (10 files)

User-invoked shortcuts for common workflows.

| File | Description | Use Case |
|------|-------------|----------|
| `optimize.md` | Code optimization analyzer | Find performance issues |
| `pr.md` | Pull request preparation | PR workflow automation |
| `generate-api-docs.md` | API documentation generator | Generate API docs |
| `commit.md` | Commit message helper | Standardized commits |
| `setup-ci-cd.md` | CI/CD pipeline setup | DevOps automation |
| `push-all.md` | Push all changes | Quick push workflow |
| `unit-test-expand.md` | Expand unit test coverage | Test automation |
| `doc-refactor.md` | Documentation refactoring | Doc improvements |
| `pr-slash-command.png` | Screenshot example | Visual reference |
| `README.md` | Documentation | Setup and usage guide |

**Installation Path**: `.claude/commands/`

**Usage**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Memory (6 files)

Persistent context and project standards.

| File | Description | Scope | Location |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | Team project standards | Project-wide | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API-specific rules | Directory | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Personal preferences | User | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Screenshot: memory saved | - | Visual reference |
| `memory-ask-claude.png` | Screenshot: ask Claude | - | Visual reference |
| `README.md` | Documentation | - | Reference |

**Installation**: Copy to appropriate location

**Usage**: Automatically loaded by Claude

---

## 03. Skills (28 files)

Auto-invoked capabilities with scripts and templates.

### Code Review Skill (5 files)
```
code-review/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-metrics.py            # Code metrics analyzer
│   └── compare-complexity.py         # Complexity comparison
└── templates/
    ├── review-checklist.md           # Review checklist
    └── finding-template.md           # Finding documentation
```

**Purpose**: Comprehensive code review with security, performance, and quality analysis

**Auto-invoked**: When reviewing code

---

### Brand Voice Skill (4 files)
```
brand-voice/
├── SKILL.md                          # Skill definition
├── templates/
│   ├── email-template.txt            # Email format
│   └── social-post-template.txt      # Social media format
└── tone-examples.md                  # Example messages
```

**Purpose**: Ensure consistent brand voice in communications

**Auto-invoked**: When creating marketing copy

---

### Documentation Generator Skill (2 files)
```
doc-generator/
├── SKILL.md                          # Skill definition
└── generate-docs.py                  # Python doc extractor
```

**Purpose**: Generate comprehensive API documentation from source code

**Auto-invoked**: When creating/updating API documentation

---

### Refactor Skill (5 files)
```
refactor/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-complexity.py         # Complexity analyzer
│   └── detect-smells.py              # Code smell detector
├── references/
│   ├── code-smells.md                # Code smells catalog
│   └── refactoring-catalog.md        # Refactoring patterns
└── templates/
    └── refactoring-plan.md           # Refactoring plan template
```

**Purpose**: Systematic code refactoring with complexity analysis

**Auto-invoked**: When refactoring code

---

### Claude MD Skill (1 file)
```
claude-md/
└── SKILL.md                          # Skill definition
```

**Purpose**: Manage and optimize CLAUDE.md files

---

### Blog Draft Skill (3 files)
```
blog-draft/
├── SKILL.md                          # Skill definition
└── templates/
    ├── draft-template.md             # Blog draft template
    └── outline-template.md           # Blog outline template
```

**Purpose**: Draft blog posts with consistent structure

**Plus**: `README.md` - Skills overview and usage guide

**Installation Path**: `~/.claude/skills/` or `.claude/skills/`

---

## 04. Subagents (9 files)

Specialized AI assistants with custom capabilities.

| File | Description | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | Code quality analysis | read, grep, diff, lint_runner | Comprehensive reviews |
| `test-engineer.md` | Test coverage analysis | read, write, bash, grep | Test automation |
| `documentation-writer.md` | Documentation creation | read, write, grep | Doc generation |
| `secure-reviewer.md` | Security review (read-only) | read, grep | Security audits |
| `implementation-agent.md` | Full implementation | read, write, bash, grep, edit, glob | Feature development |
| `debugger.md` | Debugging specialist | read, bash, grep | Bug investigation |
| `data-scientist.md` | Data analysis specialist | read, write, bash | Data workflows |
| `clean-code-reviewer.md` | Clean code standards | read, grep | Code quality |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.claude/agents/`

**Usage**: Automatically delegated by main agent

---

## 05. MCP Protocol (5 files)

External tool and API integrations.

| File | Description | Integrates With | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub integration | GitHub API | PR/issue management |
| `database-mcp.json` | Database queries | PostgreSQL/MySQL | Live data queries |
| `filesystem-mcp.json` | File operations | Local filesystem | File management |
| `multi-mcp.json` | Multiple servers | GitHub + DB + Slack | Complete integration |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.mcp.json` (project scope) or `~/.claude.json` (user scope)

**Usage**: `/mcp__github__list_prs`, etc.

---

## 06. Hooks (9 files)

Event-driven automation scripts that execute automatically.

| File | Description | Event | Use Case |
|------|-------------|-------|----------|
| `format-code.sh` | Auto-format code | PreToolUse:Write | Code formatting |
| `pre-commit.sh` | Run tests before commit | PreToolUse:Bash | Test automation |
| `security-scan.sh` | Security scanning | PostToolUse:Write | Security checks |
| `log-bash.sh` | Log bash commands | PostToolUse:Bash | Command logging |
| `validate-prompt.sh` | Validate prompts | PreToolUse | Input validation |
| `notify-team.sh` | Send notifications | Notification | Team notifications |
| `context-tracker.py` | Track context window usage | PostToolUse | Context monitoring |
| `context-tracker-tiktoken.py` | Token-based context tracking | PostToolUse | Precise token counting |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: Configure in `~/.claude/settings.json`

**Usage**: Configured in settings, executed automatically

**Hook Types** (4 types, 25 events):
- Tool Hooks: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Session Hooks: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Task Hooks: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Lifecycle Hooks: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Plugins (3 complete plugins, 40 files)

Bundled collections of features.

### PR Review Plugin (10 files)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── review-pr.md                  # Comprehensive review
│   ├── check-security.md             # Security check
│   └── check-tests.md                # Test coverage check
├── agents/
│   ├── security-reviewer.md          # Security specialist
│   ├── test-checker.md               # Test specialist
│   └── performance-analyzer.md       # Performance specialist
├── mcp/
│   └── github-config.json            # GitHub integration
├── hooks/
│   └── pre-review.js                 # Pre-review validation
└── README.md                         # Plugin documentation
```

**Features**: Security analysis, test coverage, performance impact

**Commands**: `/review-pr`, `/check-security`, `/check-tests`

**Installation**: `/plugin install pr-review`

---

### DevOps Automation Plugin (15 files)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── deploy.md                     # Deployment
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # System status
│   └── incident.md                   # Incident response
├── agents/
│   ├── deployment-specialist.md      # Deployment expert
│   ├── incident-commander.md         # Incident coordinator
│   └── alert-analyzer.md             # Alert analyzer
├── mcp/
│   └── kubernetes-config.json        # Kubernetes integration
├── hooks/
│   ├── pre-deploy.js                 # Pre-deployment checks
│   └── post-deploy.js                # Post-deployment tasks
├── scripts/
│   ├── deploy.sh                     # Deployment automation
│   ├── rollback.sh                   # Rollback automation
│   └── health-check.sh               # Health checks
└── README.md                         # Plugin documentation
```

**Features**: Kubernetes deployment, rollback, monitoring, incident response

**Commands**: `/deploy`, `/rollback`, `/status`, `/incident`

**Installation**: `/plugin install devops-automation`

---

### Documentation Plugin (14 files)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── generate-api-docs.md          # API docs generation
│   ├── generate-readme.md            # README creation
│   ├── sync-docs.md                  # Doc synchronization
│   └── validate-docs.md              # Doc validation
├── agents/
│   ├── api-documenter.md             # API doc specialist
│   ├── code-commentator.md           # Code comment specialist
│   └── example-generator.md          # Example creator
├── mcp/
│   └── github-docs-config.json       # GitHub integration
├── templates/
│   ├── api-endpoint.md               # API endpoint template
│   ├── function-docs.md              # Function doc template
│   └── adr-template.md               # ADR template
└── README.md                         # Plugin documentation
```

**Features**: API docs, README generation, doc sync, validation

**Commands**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Installation**: `/plugin install documentation`

**Plus**: `README.md` - Plugins overview and usage guide

---

## 08. Checkpoints and Rewind (2 files)

Save conversation state and explore alternative approaches.

| File | Description | Content |
|------|-------------|---------|
| `README.md` | Documentation | Comprehensive checkpoint guide |
| `checkpoint-examples.md` | Real-world examples | Database migration, performance optimization, UI iteration, debugging |
| | | |

**Key Concepts**:
- **Checkpoint**: Snapshot of conversation state
- **Rewind**: Return to previous checkpoint
- **Branch Point**: Explore multiple approaches

**Usage**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind
# Then choose: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, or Never mind
```

**Use Cases**:
- Try different implementations
- Recover from mistakes
- Safe experimentation
- Compare solutions
- A/B testing

---

## 09. Advanced Features (3 files)

Advanced capabilities for complex workflows.

| File | Description | Features |
|------|-------------|----------|
| `README.md` | Complete guide | All advanced features documentation |
| `config-examples.json` | Configuration examples | 10+ use-case-specific configurations |
| `planning-mode-examples.md` | Planning examples | REST API, database migration, refactoring |
| Scheduled Tasks | Recurring tasks with `/loop` and cron tools | Automated recurring workflows |
| Chrome Integration | Browser automation via headless Chromium | Web testing and scraping |
| Remote Control (expanded) | Connection methods, security, comparison table | Remote session management |
| Keyboard Customization | Custom keybindings, chord support, contexts | Personalized shortcuts |
| Desktop App (expanded) | Connectors, launch.json, enterprise features | Desktop integration |
| | | |

**Advanced Features Covered**:

### Planning Mode
- Create detailed implementation plans
- Time estimates and risk assessment
- Systematic task breakdown

### Extended Thinking
- Deep reasoning for complex problems
- Architectural decision analysis
- Trade-off evaluation

### Background Tasks
- Long-running operations without blocking
- Parallel development workflows
- Task management and monitoring

### Permission Modes
- **default**: Ask for approval on risky actions
- **acceptEdits**: Auto-accept file edits, ask for others
- **plan**: Read-only analysis, no modifications
- **auto**: Automatically approve safe actions, prompt for risky ones
- **dontAsk**: Accept all actions except risky ones
- **bypassPermissions**: Accept all (requires `--dangerously-skip-permissions`)

### Headless Mode (`claude -p`)
- CI/CD integration
- Automated task execution
- Batch processing

### Session Management
- Multiple work sessions
- Session switching and saving
- Session persistence

### Interactive Features
- Keyboard shortcuts
- Command history
- Tab completion
- Multi-line input

### Configuration
- Comprehensive settings management
- Environment-specific configs
- Per-project customization

### Scheduled Tasks
- Recurring tasks with `/loop` command
- Cron tools: CronCreate, CronList, CronDelete
- Automated recurring workflows

### Chrome Integration
- Browser automation via headless Chromium
- Web testing and scraping capabilities
- Page interaction and data extraction

### Remote Control (expanded)
- Connection methods and protocols
- Security considerations and best practices
- Comparison table of remote access options

### Keyboard Customization
- Custom keybindings configuration
- Chord support for multi-key shortcuts
- Context-aware keybinding activation

### Desktop App (expanded)
- Connectors for IDE integration
- launch.json configuration
- Enterprise features and deployment

---

## 10. CLI Usage (1 file)

Command-line interface usage patterns and reference.

| File | Description | Content |
|------|-------------|---------|
| `README.md` | CLI documentation | Flags, options, and usage patterns |

**Key CLI Features**:
- `claude` - Start interactive session
- `claude -p "prompt"` - Headless/non-interactive mode
- `claude web` - Launch web session
- `claude --model` - Select model (Sonnet 4.6, Opus 4.6)
- `claude --permission-mode` - Set permission mode
- `claude --remote` - Enable remote control via WebSocket

---

## Documentation Files (13 files)

| File | Location | Description |
|------|----------|-------------|
| `README.md` | `/` | Main examples overview |
| `INDEX.md` | `/` | This complete index |
| `QUICK_REFERENCE.md` | `/` | Quick reference card |
| `README.md` | `/01-slash-commands/` | Slash commands guide |
| `README.md` | `/02-memory/` | Memory guide |
| `README.md` | `/03-skills/` | Skills guide |
| `README.md` | `/04-subagents/` | Subagents guide |
| `README.md` | `/05-mcp/` | MCP guide |
| `README.md` | `/06-hooks/` | Hooks guide |
| `README.md` | `/07-plugins/` | Plugins guide |
| `README.md` | `/08-checkpoints/` | Checkpoints guide |
| `README.md` | `/09-advanced-features/` | Advanced features guide |
| `README.md` | `/10-cli/` | CLI guide |

---

## Complete File Tree

```
claude-howto/
├── README.md                                    # Main overview
├── INDEX.md                                     # This file
├── QUICK_REFERENCE.md                           # Quick reference card
├── claude_concepts_guide.md                     # Original guide
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI Usage
    └── README.md
```

---

## Quick Start by Use Case

### Code Quality & Reviews
```bash
# Install slash command
cp 01-slash-commands/optimize.md .claude/commands/

# Install subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# Install skill
cp -r 03-skills/code-review ~/.claude/skills/

# Or install complete plugin
/plugin install pr-review
```

### DevOps & Deployment
```bash
# Install plugin (includes everything)
/plugin install devops-automation
```

### Documentation
```bash
# Install slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Install subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Install skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Or install complete plugin
/plugin install documentation
```

### Team Standards
```bash
# Set up project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Edit to match your team's standards
```

### External Integrations
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Install MCP config (project scope)
cp 05-mcp/multi-mcp.json .mcp.json
```

### Automation & Validation
```bash
# Install hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configure hooks in settings (~/.claude/settings.json)
# See 06-hooks/README.md
```

### Safe Experimentation
```bash
# Checkpoints are created automatically with every user prompt
# To rewind: press Esc+Esc or use /rewind
# Then choose what to restore from the rewind menu

# See 08-checkpoints/README.md for examples
```

### Advanced Workflows
```bash
# Configure advanced features
# See 09-advanced-features/config-examples.json

# Use planning mode
/plan Implement feature X

# Use permission modes
claude --permission-mode plan          # For code review (read-only)
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions

# Run in headless mode for CI/CD
claude -p "Run tests and report results"

# Run background tasks
Run tests in background

# See 09-advanced-features/README.md for complete guide
```

---

## Feature Coverage Matrix

| Category | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Images | Total |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagents** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## Learning Path

### Beginner (Week 1)
1. ✅ Read `README.md`
2. ✅ Install 1-2 slash commands
3. ✅ Create project memory file
4. ✅ Try basic commands

### Intermediate (Week 2-3)
1. ✅ Set up GitHub MCP
2. ✅ Install a subagent
3. ✅ Try delegating tasks
4. ✅ Install a skill

### Advanced (Week 4+)
1. ✅ Install complete plugin
2. ✅ Create custom slash commands
3. ✅ Create custom subagent
4. ✅ Create custom skill
5. ✅ Build your own plugin

### Expert (Week 5+)
1. ✅ Set up hooks for automation
2. ✅ Use checkpoints for experimentation
3. ✅ Configure planning mode
4. ✅ Use permission modes effectively
5. ✅ Set up headless mode for CI/CD
6. ✅ Master session management

---

## Search by Keyword

### Performance
- `01-slash-commands/optimize.md` - Performance analysis
- `04-subagents/code-reviewer.md` - Performance review
- `03-skills/code-review/` - Performance metrics
- `07-plugins/pr-review/agents/performance-analyzer.md` - Performance specialist

### Security
- `04-subagents/secure-reviewer.md` - Security review
- `03-skills/code-review/` - Security analysis
- `07-plugins/pr-review/` - Security checks

### Testing
- `04-subagents/test-engineer.md` - Test engineer
- `07-plugins/pr-review/commands/check-tests.md` - Test coverage

### Documentation
- `01-slash-commands/generate-api-docs.md` - API docs command
- `04-subagents/documentation-writer.md` - Doc writer agent
- `03-skills/doc-generator/` - Doc generator skill
- `07-plugins/documentation/` - Complete doc plugin

### Deployment
- `07-plugins/devops-automation/` - Complete DevOps solution

### Automation
- `06-hooks/` - Event-driven automation
- `06-hooks/pre-commit.sh` - Pre-commit automation
- `06-hooks/format-code.sh` - Auto-formatting
- `09-advanced-features/` - Headless mode for CI/CD

### Validation
- `06-hooks/security-scan.sh` - Security validation
- `06-hooks/validate-prompt.sh` - Prompt validation

### Experimentation
- `08-checkpoints/` - Safe experimentation with rewind
- `08-checkpoints/checkpoint-examples.md` - Real-world examples

### Planning
- `09-advanced-features/planning-mode-examples.md` - Planning mode examples
- `09-advanced-features/README.md` - Extended thinking

### Configuration
- `09-advanced-features/config-examples.json` - Configuration examples

---

## Notes

- All examples are ready to use
- Modify to fit your specific needs
- Examples follow Claude Code best practices
- Each category has its own README with detailed instructions
- Scripts include proper error handling
- Templates are customizable

---

## Contributing

Want to add more examples? Follow the structure:
1. Create appropriate subdirectory
2. Include README.md with usage
3. Follow naming conventions
4. Test thoroughly
5. Update this index

---

**Last Updated**: April 11, 2026
**Claude Code Version**: 2.1.101
**Sources**:
- https://code.claude.com/docs/en/overview
**Total Examples**: 100+ files
**Categories**: 10 features
**Hooks**: 8 automation scripts
**Configuration Examples**: 10+ scenarios
**Ready to Use**: All examples
