![Claude How To](claude-howto-logo.svg)

# Claude Code Examples - Complete Index

This document provides a complete index of all example files organized by feature type.

## Summary Statistics

- **Total Files**: 90+ files
- **Categories**: 9 feature categories
- **Plugins**: 3 complete plugins
- **Skills**: 3 complete skills
- **Hooks**: 6 example hooks
- **Ready to Use**: All examples

---

## 📁 01. Slash Commands (4 files)

User-invoked shortcuts for common workflows.

| File | Description | Use Case |
|------|-------------|----------|
| `optimize.md` | Code optimization analyzer | Find performance issues |
| `pr.md` | Pull request preparation | PR workflow automation |
| `generate-api-docs.md` | API documentation generator | Generate API docs |
| `README.md` | Documentation | Setup and usage guide |

**Installation Path**: `.claude/commands/`

**Usage**: `/optimize`, `/pr`, `/generate-api-docs`

---

## 🤖 02. Subagents (6 files)

Specialized AI assistants with custom capabilities.

| File | Description | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | Code quality analysis | read, grep, diff, lint_runner | Comprehensive reviews |
| `test-engineer.md` | Test coverage analysis | read, write, bash, grep | Test automation |
| `documentation-writer.md` | Documentation creation | read, write, grep | Doc generation |
| `secure-reviewer.md` | Security review (read-only) | read, grep | Security audits |
| `implementation-agent.md` | Full implementation | read, write, bash, grep, edit, glob | Feature development |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.claude/agents/`

**Usage**: Automatically delegated by main agent

---

## 💾 03. Memory (4 files)

Persistent context and project standards.

| File | Description | Scope | Location |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | Team project standards | Project-wide | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API-specific rules | Directory | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Personal preferences | User | `~/.claude/CLAUDE.md` |
| `README.md` | Documentation | - | Reference |

**Installation**: Copy to appropriate location

**Usage**: Automatically loaded by Claude

---

## 🔌 04. MCP Protocol (5 files)

External tool and API integrations.

| File | Description | Integrates With | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub integration | GitHub API | PR/issue management |
| `database-mcp.json` | Database queries | PostgreSQL/MySQL | Live data queries |
| `filesystem-mcp.json` | File operations | Local filesystem | File management |
| `multi-mcp.json` | Multiple servers | GitHub + DB + Slack | Complete integration |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.claude/mcp.json`

**Usage**: `/mcp__github__list_prs`, etc.

---

## 🎯 05. Skills (11 files)

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

**Plus**: `README.md` - Skills overview and usage guide

**Installation Path**: `~/.claude/skills/` or `.claude/skills/`

---

## 📦 06. Plugins (3 complete plugins, 40 files)

Bundled collections of features.

### PR Review Plugin (10 files)
```
pr-review/
├── plugin.yaml                       # Plugin manifest
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
├── plugin.yaml                       # Plugin manifest
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
├── plugin.yaml                       # Plugin manifest
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

## ⚙️ 07. Hooks (7 files)

Event-driven automation scripts that execute automatically.

| File | Description | Event | Use Case |
|------|-------------|-------|----------|
| `format-code.sh` | Auto-format code | PreToolUse:Write | Code formatting |
| `pre-commit.sh` | Run tests before commit | PreCommit | Test automation |
| `security-scan.sh` | Security scanning | PostToolUse:Write | Security checks |
| `log-bash.sh` | Log bash commands | PostToolUse:Bash | Command logging |
| `validate-prompt.sh` | Validate prompts | UserPromptSubmit | Input validation |
| `notify-team.sh` | Send notifications | PostPush | Team notifications |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `~/.claude/hooks/`

**Usage**: Configured in settings, executed automatically

**Hook Types**:
- Tool Hooks: PreToolUse:*, PostToolUse:*
- Session Hooks: UserPromptSubmit, SessionStart, SessionEnd
- Git Hooks: PreCommit, PostCommit, PrePush

---

## 💾 08. Checkpoints and Rewind (3 files)

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
/checkpoint save "Before refactoring"
/checkpoint list
/checkpoint rewind "Before refactoring"
/checkpoint diff checkpoint-1 checkpoint-2
```

**Use Cases**:
- Try different implementations
- Recover from mistakes
- Safe experimentation
- Compare solutions
- A/B testing

---

## 🚀 09. Advanced Features (4 files)

Advanced capabilities for complex workflows.

| File | Description | Features |
|------|-------------|----------|
| `README.md` | Complete guide | All advanced features documentation |
| `config-examples.json` | Configuration examples | 10+ use-case-specific configurations |
| `planning-mode-examples.md` | Planning examples | REST API, database migration, refactoring |
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
- **Unrestricted**: Full access (default)
- **Confirm**: Ask before actions
- **Read-only**: Analysis only
- **Custom**: Granular control

### Headless Mode
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

---

## 📚 Documentation Files (11 files)

| File | Location | Description |
|------|----------|-------------|
| `README.md` | `/` | Main examples overview |
| `INDEX.md` | `/` | This complete index |
| `README.md` | `/01-slash-commands/` | Slash commands guide |
| `README.md` | `/02-subagents/` | Subagents guide |
| `README.md` | `/03-memory/` | Memory guide |
| `README.md` | `/04-mcp/` | MCP guide |
| `README.md` | `/05-skills/` | Skills guide |
| `README.md` | `/06-plugins/` | Plugins guide |
| `README.md` | `/07-hooks/` | Hooks guide |
| `README.md` | `/08-checkpoints/` | Checkpoints guide |
| `README.md` | `/09-advanced-features/` | Advanced features guide |
| `QUICK_REFERENCE.md` | `/` | Quick reference card |

---

## 🗂️ Complete File Tree

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
│   └── README.md
│
├── 02-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
│
├── 03-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
│
├── 04-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 05-skills/                                   # Skills
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
│   └── README.md
│
├── 06-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── plugin.yaml
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
│   │   ├── plugin.yaml
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
│   │   ├── plugin.yaml
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
├── 07-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
└── 09-advanced-features/                        # Advanced Features
    ├── config-examples.json
    ├── planning-mode-examples.md
    └── README.md
```

---

## 🚀 Quick Start by Use Case

### Code Quality & Reviews
```bash
# Install slash command
cp 01-slash-commands/optimize.md .claude/commands/

# Install subagent
cp 02-subagents/code-reviewer.md .claude/agents/

# Install skill
cp -r 05-skills/code-review ~/.claude/skills/

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
cp 02-subagents/documentation-writer.md .claude/agents/

# Install skill
cp -r 05-skills/doc-generator ~/.claude/skills/

# Or install complete plugin
/plugin install documentation
```

### Team Standards
```bash
# Set up project memory
cp 03-memory/project-CLAUDE.md ./CLAUDE.md

# Edit to match your team's standards
```

### External Integrations
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Install MCP config
cp 04-mcp/multi-mcp.json .claude/mcp.json
```

### Automation & Validation
```bash
# Install hooks
mkdir -p ~/.claude/hooks
cp 07-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configure hooks in settings
# See 07-hooks/README.md
```

### Safe Experimentation
```bash
# Checkpoints are auto-enabled
# Use in your workflow:
/checkpoint save "Before refactoring"
/checkpoint list
/checkpoint rewind "Before refactoring"

# See 08-checkpoints/README.md for examples
```

### Advanced Workflows
```bash
# Configure advanced features
# See 09-advanced-features/config-examples.json

# Use planning mode
/plan Implement feature X

# Use permission modes
/permission readonly    # For code review
/permission confirm     # For learning

# Run background tasks
Run tests in background

# See 09-advanced-features/README.md for complete guide
```

---

## 📊 Feature Coverage Matrix

| Category | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Examples | Total |
|----------|----------|--------|-----|-------|---------|-----------|------|----------|-------|
| **Slash Commands** | 3 | - | - | - | - | - | 1 | - | **4** |
| **Subagents** | - | 5 | - | - | - | - | 1 | - | **6** |
| **Memory** | - | - | - | - | - | 3 | 1 | - | **4** |
| **MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **Skills** | - | - | - | - | 3 | 7 | 1 | - | **11** |
| **Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **36** |
| **Hooks** | - | - | - | 6 | - | - | 1 | - | **7** |
| **Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **TOTAL** | **14** | **14** | **7** | **9** | **6** | **13** | **12** | **3** | **78** |

---

## 🎯 Learning Path

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

## 🔍 Search by Keyword

### Performance
- `01-slash-commands/optimize.md` - Performance analysis
- `02-subagents/code-reviewer.md` - Performance review
- `05-skills/code-review/` - Performance metrics
- `06-plugins/pr-review/agents/performance-analyzer.md` - Performance specialist

### Security
- `02-subagents/secure-reviewer.md` - Security review
- `05-skills/code-review/` - Security analysis
- `06-plugins/pr-review/` - Security checks

### Testing
- `02-subagents/test-engineer.md` - Test engineer
- `06-plugins/pr-review/commands/check-tests.md` - Test coverage

### Documentation
- `01-slash-commands/generate-api-docs.md` - API docs command
- `02-subagents/documentation-writer.md` - Doc writer agent
- `05-skills/doc-generator/` - Doc generator skill
- `06-plugins/documentation/` - Complete doc plugin

### Deployment
- `06-plugins/devops-automation/` - Complete DevOps solution

### Automation
- `07-hooks/` - Event-driven automation
- `07-hooks/pre-commit.sh` - Pre-commit automation
- `07-hooks/format-code.sh` - Auto-formatting
- `09-advanced-features/` - Headless mode for CI/CD

### Validation
- `07-hooks/security-scan.sh` - Security validation
- `07-hooks/validate-prompt.sh` - Prompt validation

### Experimentation
- `08-checkpoints/` - Safe experimentation with rewind
- `08-checkpoints/checkpoint-examples.md` - Real-world examples

### Planning
- `09-advanced-features/planning-mode-examples.md` - Planning mode examples
- `09-advanced-features/README.md` - Extended thinking

### Configuration
- `09-advanced-features/config-examples.json` - Configuration examples

---

## 📝 Notes

- All examples are ready to use
- Modify to fit your specific needs
- Examples follow Claude Code best practices
- Each category has its own README with detailed instructions
- Scripts include proper error handling
- Templates are customizable

---

## 🤝 Contributing

Want to add more examples? Follow the structure:
1. Create appropriate subdirectory
2. Include README.md with usage
3. Follow naming conventions
4. Test thoroughly
5. Update this index

---

**Last Updated**: November 2025
**Total Examples**: 90+ files
**Categories**: 9 features
**Hooks**: 6 automation scripts
**Configuration Examples**: 10+ scenarios
**Ready to Use**: ✅ All examples
