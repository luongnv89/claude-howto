---
description: 暂存全部变更、创建 commit 并推送到远端（请谨慎使用）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# Commit and Push Everything

⚠️ **注意**：该命令会暂存**全部**变更、提交并推送到远端。仅在你确认所有变更应一并提交时使用。

## Workflow

### 1. 分析变更
并行运行：
- `git status` - 查看修改/新增/删除/未跟踪文件
- `git diff --stat` - 查看变更统计
- `git log -1 --oneline` - 查看最近提交风格

### 2. 安全检查

**❌ 若发现以下内容，必须停止并警告：**
- Secrets: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- API Keys: 任意 `*_API_KEY`, `*_SECRET`, `*_TOKEN` 且为真实值（非占位，如 `your-api-key`, `xxx`, `placeholder`）
- 大文件：未使用 Git LFS 且 `>10MB`
- 构建产物：`node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- 临时文件：`.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**API Key 校验示例：**
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ 检测到真实 key
AWS_SECRET_KEY=AKIA...         # ❌ 检测到真实 key
STRIPE_API_KEY=sk_live_...    # ❌ 检测到真实 key

# ✅ 可接受占位符：
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ 同时确认：**
- `.gitignore` 配置正确
- 无 merge conflict
- 分支正确（在 main/master 上要警告）
- API key 仅为占位符

### 3. 请求用户确认

展示摘要：
```text
📊 Changes Summary:
- X files modified, Y added, Z deleted
- Total: +AAA insertions, -BBB deletions

🔒 Safety: ✅ No secrets | ✅ No large files | ⚠️ [warnings]
🌿 Branch: [name] → origin/[name]

I will: git add . → commit → push

Type 'yes' to proceed or 'no' to cancel.
```

**必须等待用户明确输入 `yes` 才可继续。**

### 4. 执行（确认后）

按顺序执行：
```bash
git add .
git status  # 校验暂存结果
```

### 5. 生成提交信息

分析变更后，按 conventional commit 生成：

**格式：**
```text
[type]: Brief summary (max 72 characters)

- Key change 1
- Key change 2
- Key change 3
```

**类型：** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**示例：**
```text
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. 提交并推送

```bash
git commit -m "$(cat <<'EOF'
[Generated commit message]
EOF
)"
git push  # 若失败: git pull --rebase && git push
git log -1 --oneline --decorate  # 校验结果
```

### 7. 成功确认

```text
✅ Successfully pushed to remote!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X (+insertions, -deletions)
```

## Error Handling

- **git add 失败**：检查权限、锁定文件、仓库是否已初始化
- **git commit 失败**：修复 pre-commit hooks，检查 git 配置（user.name/email）
- **git push 失败**：
  - Non-fast-forward: `git pull --rebase && git push`
  - 无远端分支: `git push -u origin [branch]`
  - 受保护分支: 改为 PR 流程

## 何时使用

✅ **适合：**
- 多文件文档更新
- 功能 + 测试 + 文档一体提交
- 跨文件 bug 修复
- 项目级格式化/重构
- 配置类统一变更

❌ **不适合：**
- 不确定要提交哪些改动
- 包含敏感信息
- 受保护分支且未评审
- 有冲突未解决
- 想保留细粒度提交历史
- pre-commit hooks 仍失败

## 替代方案

如用户希望更可控，建议：
1. **选择性暂存**：仅暂存指定文件
2. **交互式暂存**：`git add -p` 按 patch 选择
3. **PR 流程**：建分支 → 推送 → 发 PR（可配合 `/pr`）

**⚠️ 牢记**：推送前务必审查变更。不确定时，请使用逐条 git 命令而非一次性全推送。
