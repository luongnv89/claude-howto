---
description: 清理代码、暂存变更并准备 Pull Request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request Preparation Checklist

在创建 PR 前，执行以下步骤：

1. 运行格式化：`prettier --write .`
2. 运行测试：`npm test`
3. 检查 git diff：`git diff HEAD`
4. 暂存变更：`git add .`
5. 使用 conventional commits 规范编写提交信息：
   - `fix:` bug 修复
   - `feat:` 新功能
   - `docs:` 文档变更
   - `refactor:` 代码重构
   - `test:` 测试新增
   - `chore:` 维护任务

6. 生成 PR 摘要，至少包含：
   - 变更内容
   - 变更原因
   - 已执行测试
   - 可能影响
