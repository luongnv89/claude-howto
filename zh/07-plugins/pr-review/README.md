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
claude --plugin-dir ./07-plugins/pr-review
```

加载插件之前先检查它：

```bash
claude plugin validate ./07-plugins/pr-review
```

## 包含内容

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### Slash 命令

插件命令以 `plugin.json` 中的插件 `name` 作为命名空间：

- `/pr-review:review-pr` - 全面 PR 审查
- `/pr-review:check-security` - 面向安全的审查
- `/pr-review:check-tests` - 测试覆盖率分析

### 子 agents
- `security-reviewer` - 安全漏洞检测
- `test-checker` - 测试覆盖率分析
- `performance-analyzer` - 性能影响评估

### MCP 服务器

`.mcp.json` 声明了一个服务器 `github`：GitHub 官方 MCP 服务器（`ghcr.io/github/github-mcp-server`），通过 Docker 以只读模式运行。镜像固定在 [v2.1.0 版本](https://github.com/github/github-mcp-server/releases/tag/v2.1.0)；如需升级，请修改 `.mcp.json` 中的标签。它在 `/mcp` 中显示为 `plugin:pr-review:github`。

### Hooks

`hooks/hooks.json` 把 `pre-review.js` 注册到 `UserPromptExpansion` 事件上，matcher 匹配上面的三个命令。matcher 同时接受 `pr-review:review-pr`（Claude Code 2.1.322 为插件命令发送的 `command_name`）和不带前缀的 `review-pr`。当你输入其中一个命令时，该 hook 会：

- 如果当前目录不是 git 仓库，阻止该命令（退出码 2）
- 否则把当前分支（或说明 HEAD 处于 detached 状态、或仓库还没有任何提交的提示）以及未提交更改的提示添加到 Claude 的上下文中

## 使用

### 基础 PR 审查

```text
/pr-review:review-pr
```

### 仅安全检查

```text
/pr-review:check-security
```

### 仅测试覆盖率检查

```text
/pr-review:check-tests
```

## 要求

- Claude Code 2.1+
- Node.js（运行 hook 脚本）
- Docker（运行 GitHub MCP 服务器）
- GitHub personal access token
- Git 仓库

## 配置

在启动 Claude Code 之前设置 GitHub token：

```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` 会把它作为 `GITHUB_PERSONAL_ACCESS_TOKEN`（服务器读取的变量）传给服务器。运行 `/mcp` 检查 `plugin:pr-review:github` 是否已连接。

## 示例工作流

```text
用户：/pr-review:review-pr

Claude:
1. pre-review hook 检查 git 仓库，并把分支添加到上下文
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

---

**最后更新**: 2026 年 10 月 18 日
**Claude Code 版本**: 2.1.302
**来源**:
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
