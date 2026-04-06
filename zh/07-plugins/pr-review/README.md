---
name: PR 审查插件
description: 为 Pull Request 提供完整的代码审查工作流
tags: plugins, code-review, pull-request
---

# PR 审查插件

完整的 PR 审查工作流，包含安全、测试和文档检查。

## 功能

✅ 安全分析
✅ 测试覆盖率检查
✅ 文档校验
✅ 代码质量评估
✅ 性能影响分析

## 安装

```bash
/plugin install pr-review
```

## 包含内容

### Slash 命令
- `/review-pr` - 全面 PR 审查
- `/check-security` - 面向安全的审查
- `/check-tests` - 测试覆盖率分析

### 子 agents
- `security-reviewer` - 安全漏洞检测
- `test-checker` - 测试覆盖率分析
- `performance-analyzer` - 性能影响评估

### MCP 服务器
- 用于 PR 数据的 GitHub 集成

### Hooks
- `pre-review.js` - 审查前验证

## 使用

### 基础 PR 审查

```
/review-pr
```

### 仅安全检查

```
/check-security
```

### 仅测试覆盖率检查

```
/check-tests
```

## 要求

- Claude Code 1.0+
- GitHub 访问权限
- Git 仓库

## 配置

设置 GitHub token：

```bash
export GITHUB_TOKEN="your_github_token"
```

## 示例工作流

```
用户：/review-pr

Claude:
1. 运行 pre-review hook（验证 git 仓库）
2. 通过 GitHub MCP 获取 PR 数据
3. 将安全审查委派给 security-reviewer subagent
4. 将测试分析委派给 test-checker subagent
5. 将性能分析委派给 performance-analyzer subagent
6. 汇总所有发现
7. 提供完整审查报告

结果：
✅ 安全：未发现关键问题
⚠️  测试：覆盖率为 65%，建议达到 80%+
✅ 性能：没有明显影响
📝 建议：为边界情况添加测试
```
