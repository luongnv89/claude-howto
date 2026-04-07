---
name: Setup CI/CD Pipeline
description: Implement pre-commit hooks and GitHub Actions for quality assurance
tags: ci-cd, devops, automation
---

# Setup CI/CD Pipeline

Implement comprehensive DevOps quality gates adapted to project type:

1. **Analyze project**: Detect language(s), framework, build system, and existing tooling
2. **Configure pre-commit hooks** with language-specific tools:
   - Formatting: Prettier/Black/gofmt/rustfmt/etc.
   - Linting: ESLint/Ruff/golangci-lint/Clippy/etc.
   - Security: Bandit/gosec/cargo-audit/npm audit/etc.
   - Type checking: TypeScript/mypy/flow (if applicable)
   - Tests: Run relevant test suites
3. **Create GitHub Actions workflows** (.github/workflows/):
   - Mirror pre-commit checks on push/PR
   - Multi-version/platform matrix (if applicable)
   - Build and test verification
   - Deployment steps (if needed)
4. **Verify pipeline**: Test locally, create test PR, confirm all checks pass

Use free/open-source tools. Respect existing configs. Keep execution fast.

---
**Last Updated**: April 2026
