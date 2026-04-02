<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review Plugin

完整的 PR 审查工作流插件，覆盖安全、测试与文档检查。

## Features

✅ 安全分析  
✅ 测试覆盖率检查  
✅ 文档完整性校验  
✅ 代码质量评估  
✅ 性能影响分析

## Installation

```bash
/plugin install pr-review
```

## What's Included

### Slash Commands
- `/review-pr` - 全面 PR 审查
- `/check-security` - 安全专项审查
- `/check-tests` - 测试覆盖率分析

### Subagents
- `security-reviewer` - 安全漏洞检测
- `test-checker` - 测试覆盖率分析
- `performance-analyzer` - 性能影响评估

### MCP Servers
- GitHub 集成（用于获取 PR 数据）

### Hooks
- `pre-review.js` - 审查前校验

## Usage

### Basic PR Review

```text
/review-pr
```

### Security Check Only

```text
/check-security
```

### Test Coverage Check

```text
/check-tests
```

## Requirements

- Claude Code 1.0+
- 可访问 GitHub
- Git 仓库

## Configuration

设置 GitHub token：

```bash
export GITHUB_TOKEN="your_github_token"
```

## Example Workflow

```text
User: /review-pr

Claude:
1. 运行 pre-review hook（校验 git 仓库）
2. 通过 GitHub MCP 获取 PR 数据
3. 委派 security-reviewer 做安全审查
4. 委派 test-checker 做测试检查
5. 委派 performance-analyzer 做性能分析
6. 汇总全部发现
7. 输出完整审查报告

Result:
✅ Security: No critical issues found
⚠️  Testing: Coverage is 65%, recommend 80%+
✅ Performance: No significant impact
📝 Recommendations: Add tests for edge cases
```
