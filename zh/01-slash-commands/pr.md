---
description: 清理代码、暂存变更并准备 Pull Request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request 准备清单

在创建 PR 之前，请执行以下步骤：

1. 运行格式化：`prettier --write .`
2. 运行测试：`npm test`
3. 查看 git diff：`git diff HEAD`
4. 暂存变更：`git add .`
5. 按 conventional commits 创建提交信息：
   - `fix:` bug 修复
   - `feat:` 新功能
   - `docs:` 文档
   - `refactor:` 代码重构
   - `test:` 测试新增
   - `chore:` 维护

6. 生成 PR 摘要，包含：
   - 变更了什么
   - 为什么变更
   - 做了哪些测试
   - 可能的影响
