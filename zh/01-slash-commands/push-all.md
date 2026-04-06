---
description: 暂存所有变更，创建提交并推送到远程（请谨慎使用）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# 提交并推送全部内容

⚠️ **注意**：将所有变更都暂存、提交并推送到远程。只有在你确认所有改动都应该放在一起时才使用。

## 工作流

### 1. 分析变更
并行运行：
- `git status` - 显示已修改/已添加/已删除/未跟踪文件
- `git diff --stat` - 显示变更统计
- `git log -1 --oneline` - 查看最近一次提交，便于统一提交信息风格

### 2. 安全检查

**❌ 如果发现以下内容，立即停止并警告：**
- Secrets：`.env*`、`*.key`、`*.pem`、`credentials.json`、`secrets.yaml`、`id_rsa`、`*.p12`、`*.pfx`、`*.cer`
- API Keys：任何 `*_API_KEY`、`*_SECRET`、`*_TOKEN` 变量包含真实值，而不是占位符，如 `your-api-key`、`xxx`、`placeholder`
- 大文件：`>10MB` 且未使用 Git LFS
- 构建产物：`node_modules/`、`dist/`、`build/`、`__pycache__/`、`*.pyc`、`.venv/`
- 临时文件：`.DS_Store`、`thumbs.db`、`*.swp`、`*.tmp`

**API Key 校验：**
检查修改文件中是否存在以下模式：
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ 检测到真实密钥！
AWS_SECRET_KEY=AKIA...         # ❌ 检测到真实密钥！
STRIPE_API_KEY=sk_live_...    # ❌ 检测到真实密钥！

# ✅ 可接受的占位符：
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ 确认：**
- `.gitignore` 配置正确
- 没有合并冲突
- 分支正确（如果是 `main`/`master` 要提醒）
- API key 只是占位符

### 3. 请求确认

展示摘要：
```
📊 变更摘要：
- X 个文件已修改，Y 个文件已新增，Z 个文件已删除
- 总计：+AAA 行新增，-BBB 行删除

🔒 安全性：✅ 无 secrets | ✅ 无大文件 | ⚠️ [警告]
🌿 分支： [name] → origin/[name]

我将执行：git add . → commit → push

请输入 'yes' 继续，或输入 'no' 取消。
```

**在收到明确的 "yes" 之前不要继续。**

### 4. 执行（确认后）

按顺序运行：
```bash
git add .
git status  # 验证暂存状态
```

### 5. 生成提交信息

分析变更并创建 conventional commit：

**格式：**
```
[type]: 简要摘要（最多 72 个字符）

- 关键改动 1
- 关键改动 2
- 关键改动 3
```

**类型：** `feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore`、`perf`、`build`、`ci`

**示例：**
```
docs: 更新概念文档，补充完整说明

- 添加架构图和表格
- 补充实用示例
- 扩展最佳实践部分
```

### 6. 提交并推送

```bash
git commit -m "$(cat <<'EOF'
[生成的提交信息]
EOF
)"
git push  # 如果失败：git pull --rebase && git push
git log -1 --oneline --decorate  # 验证
```

### 7. 确认成功

```
✅ 已成功推送到远程！

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X (+insertions, -deletions)
```

## 错误处理

- `git add` 失败：检查权限、锁定文件，确认仓库已初始化
- `git commit` 失败：修复 pre-commit hooks，检查 git 配置（user.name/email）
- `git push` 失败：
  - 非快进：`git pull --rebase && git push`
  - 没有远程分支：`git push -u origin [branch]`
  - 受保护分支：改用 PR 工作流

## 适用场景

✅ **适合：**
- 多文件文档更新
- 同时包含测试和文档的功能
- 跨多个文件的 bug 修复
- 项目级格式化/重构
- 配置变更

❌ **避免：**
- 不确定要提交哪些内容
- 包含 secrets/敏感数据
- 受保护分支且未经过审核
- 存在合并冲突
- 想保留更细粒度的提交历史
- pre-commit hooks 失败

## 替代方案

如果用户想保留控制权，可以建议：
1. **选择性暂存**：查看并暂存特定文件
2. **交互式暂存**：使用 `git add -p` 逐块选择
3. **PR 工作流**：创建分支 → 推送 → 发起 PR（使用 `/pr` 命令）

**⚠️ 记住**：在推送前始终先检查变更。拿不准时，使用单独的 git 命令会更可控。
