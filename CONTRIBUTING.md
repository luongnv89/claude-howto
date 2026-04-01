<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Contributing to Claude How To

Thank you for your interest in contributing to this project! This guide will help you understand how to contribute effectively.

## About This Project

Claude How To is a visual, example-driven guide to Claude Code. We provide:
- **Mermaid diagrams** explaining how features work
- **Production-ready templates** you can use immediately
- **Real-world examples** with context and best practices
- **Progressive learning paths** from beginner to advanced

## Types of Contributions

### 1. New Examples or Templates
Add examples for existing features (slash commands, skills, hooks, etc.):
- Copy-paste ready code
- Clear explanations of how it works
- Use cases and benefits
- Troubleshooting tips

### 2. Documentation Improvements
- Clarify confusing sections
- Fix typos and grammar
- Add missing information
- Improve code examples

### 3. Feature Guides
Create guides for new Claude Code features:
- Step-by-step tutorials
- Architecture diagrams
- Common patterns and anti-patterns
- Real-world workflows

### 4. Bug Reports
Report issues you encounter:
- Describe what you expected
- Describe what actually happened
- Include steps to reproduce
- Add relevant Claude Code version and OS

### 5. Feedback and Suggestions
Help improve the guide:
- Suggest better explanations
- Point out gaps in coverage
- Recommend new sections or reorganization

## Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. Create a Branch
Use a descriptive branch name:
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. Set Up Your Environment

Pre-commit hooks run the same checks as CI locally before every commit. All four checks must pass before a PR will be accepted.

**Required dependencies:**

```bash
# Python tooling (uv is the package manager for this project)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown linter (Node.js)
npm install -g markdownlint-cli

# Mermaid diagram validator (Node.js)
npm install -g @mermaid-js/mermaid-cli

# Install pre-commit and activate hooks
uv pip install pre-commit
pre-commit install
```

**Verify your setup:**

```bash
pre-commit run --all-files
```

The hooks that run on every commit are:

| Hook | What it checks |
|------|---------------|
| `markdown-lint` | Markdown formatting and structure |
| `cross-references` | Relative links, anchors, code fences |
| `mermaid-syntax` | All ` ```mermaid ` blocks parse correctly |
| `link-check` | External URLs are reachable |
| `build-epub` | EPUB generates without errors (on `.md` changes) |

## Directory Structure

```
├── 01-slash-commands/      # User-invoked shortcuts
├── 02-memory/              # Persistent context examples
├── 03-skills/              # Reusable capabilities
├── 04-subagents/           # Specialized AI assistants
├── 05-mcp/                 # Model Context Protocol examples
├── 06-hooks/               # Event-driven automation
├── 07-plugins/             # Bundled features
├── 08-checkpoints/         # Session snapshots
├── 09-advanced-features/   # Planning, thinking, backgrounds
├── 10-cli/                 # CLI reference
├── scripts/                # Build and utility scripts
└── README.md               # Main guide
```

## How to Contribute Examples

### Adding a Slash Command
1. Create a `.md` file in `01-slash-commands/`
2. Include:
   - Clear description of what it does
   - Use cases
   - Installation instructions
   - Usage examples
   - Customization tips
3. Update `01-slash-commands/README.md`

### Adding a Skill
1. Create a directory in `03-skills/`
2. Include:
   - `SKILL.md` - Main documentation
   - `scripts/` - Helper scripts if needed
   - `templates/` - Prompt templates
   - Example usage in README
3. Update `03-skills/README.md`

### Adding a Subagent
1. Create a `.md` file in `04-subagents/`
2. Include:
   - Agent purpose and capabilities
   - System prompt structure
   - Example use cases
   - Integration examples
3. Update `04-subagents/README.md`

### Adding MCP Configuration
1. Create a `.json` file in `05-mcp/`
2. Include:
   - Configuration explanation
   - Required environment variables
   - Setup instructions
   - Usage examples
3. Update `05-mcp/README.md`

### Adding a Hook
1. Create a `.sh` file in `06-hooks/`
2. Include:
   - Shebang and description
   - Clear comments explaining logic
   - Error handling
   - Security considerations
3. Update `06-hooks/README.md`

## Writing Guidelines

### Markdown Style
- Use clear headings (H2 for sections, H3 for subsections)
- Keep paragraphs short and focused
- Use bullet points for lists
- Include code blocks with language specification
- Add blank lines between sections

### Code Examples
- Make examples copy-paste ready
- Comment non-obvious logic
- Include both simple and advanced versions
- Show real-world use cases
- Highlight potential issues

### Documentation
- Explain the "why" not just the "what"
- Include prerequisites
- Add troubleshooting sections
- Link to related topics
- Keep it beginner-friendly

### JSON/YAML
- Use proper indentation (2 or 4 spaces consistently)
- Add comments explaining configuration
- Include validation examples

### Diagrams
- Use Mermaid when possible
- Keep diagrams simple and readable
- Include descriptions below diagrams
- Link to relevant sections

## Commit Guidelines

Follow conventional commit format:
```
type(scope): description

[optional body]
```

Types:
- `feat`: New feature or example
- `fix`: Bug fix or correction
- `docs`: Documentation changes
- `refactor`: Code restructuring
- `style`: Formatting changes
- `test`: Test additions or changes
- `chore`: Build, dependencies, etc.

Examples:
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## Before Submitting

### Checklist
- [ ] Code follows project style and conventions
- [ ] New examples include clear documentation
- [ ] README files are updated (both local and root)
- [ ] No sensitive information (API keys, credentials)
- [ ] Examples are tested and working
- [ ] Links are verified and correct
- [ ] Files have proper permissions (scripts are executable)
- [ ] Commit message is clear and descriptive

### Local Testing
```bash
# Run all pre-commit checks (same checks as CI)
pre-commit run --all-files

# Review your changes
git diff
```

## Pull Request Process

1. **Create PR with clear description**:
   - What does this add/fix?
   - Why is it needed?
   - Related issues (if any)

2. **Include relevant details**:
   - New feature? Include use cases
   - Documentation? Explain improvements
   - Examples? Show before/after

3. **Link to issues**:
   - Use `Closes #123` to auto-close related issues

4. **Be patient with reviews**:
   - Maintainers may suggest improvements
   - Iterate based on feedback
   - Final decision rests with maintainers

## Code Review Process

Reviewers will check:
- **Accuracy**: Does it work as described?
- **Quality**: Is it production-ready?
- **Consistency**: Does it follow project patterns?
- **Documentation**: Is it clear and complete?
- **Security**: Are there any vulnerabilities?

## Reporting Issues

### Bug Reports
Include:
- Claude Code version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots if applicable

### Feature Requests
Include:
- Use case or problem being solved
- Proposed solution
- Alternatives you've considered
- Additional context

### Documentation Issues
Include:
- What's confusing or missing
- Suggested improvements
- Examples or references

## Project Policies

### Sensitive Information
- Never commit API keys, tokens, or credentials
- Use placeholder values in examples
- Include `.env.example` for configuration files
- Document required environment variables

### Code Quality
- Keep examples focused and readable
- Avoid over-engineering solutions
- Include comments for non-obvious logic
- Test thoroughly before submitting

### Intellectual Property
- Original content owned by author
- Project uses educational license
- Respect existing copyrights
- Provide attribution where needed

## Getting Help

- **Questions**: Open a discussion in GitHub Issues
- **General Help**: Check existing documentation
- **Development Help**: Review similar examples
- **Code Review**: Tag maintainers in PRs

## Recognition

Contributors are recognized in:
- README.md Contributors section
- GitHub contributors page
- Commit history

## Security

When contributing examples and documentation, please follow secure coding practices:

- **Never hardcode secrets or API keys** - Use environment variables
- **Warn about security implications** - Highlight potential risks
- **Use secure defaults** - Enable security features by default
- **Validate inputs** - Show proper input validation and sanitization
- **Include security notes** - Document security considerations

For security issues, see [SECURITY.md](SECURITY.md) for our vulnerability reporting process.

## Code of Conduct

We are committed to providing a welcoming and inclusive community. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for our full community standards.

In brief:
- Be respectful and inclusive
- Welcome feedback gracefully
- Help others learn and grow
- Avoid harassment or discrimination
- Report issues to maintainers

All contributors are expected to uphold this code and treat each other with kindness and respect.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Questions?

- Check the [README](README.md)
- Review [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- Look at existing examples
- Open an issue for discussion

Thank you for contributing! 🙏
