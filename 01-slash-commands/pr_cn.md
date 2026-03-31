---
description: 清理代码、暂存变更，并准备 pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request 准备清单

在创建 PR 之前，执行以下步骤：

1. 运行 lint：`prettier --write .`
2. 运行测试：`npm test`
3. 审查 git diff：`git diff HEAD`
4. 暂存变更：`git add .`
5. 按约定式提交格式创建提交消息：
   - `fix:` 用于错误修复
   - `feat:` 用于新功能
   - `docs:` 用于文档
   - `refactor:` 用于代码重构
   - `test:` 用于添加测试
   - `chore:` 用于维护

6. 生成包含以下内容的 PR 摘要：
   - 变更内容
   - 变更原因
   - 执行的测试
   - 潜在影响
