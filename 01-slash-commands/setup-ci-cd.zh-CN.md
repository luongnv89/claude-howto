---
name: Setup CI/CD Pipeline
description: 实现 pre-commit hooks 与 GitHub Actions 质量保障流程
tags: ci-cd, devops, automation
---

# Setup CI/CD Pipeline

按项目类型实现完整 DevOps 质量门禁：

1. **分析项目**：识别语言、框架、构建系统与现有工具链
2. **配置 pre-commit hooks**（按语言匹配工具）：
   - Formatting: Prettier/Black/gofmt/rustfmt 等
   - Linting: ESLint/Ruff/golangci-lint/Clippy 等
   - Security: Bandit/gosec/cargo-audit/npm audit 等
   - Type checking: TypeScript/mypy/flow（如适用）
   - Tests: 运行相关测试集
3. **创建 GitHub Actions workflows**（`.github/workflows/`）：
   - 在 push/PR 中镜像 pre-commit 检查
   - 多版本/多平台矩阵（如适用）
   - 构建与测试校验
   - 部署步骤（如需要）
4. **验证流水线**：本地测试、创建测试 PR、确认所有检查通过

优先使用免费/开源工具。尊重现有配置。保持执行速度。
