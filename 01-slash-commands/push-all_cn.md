---
description: 暂存所有变更、创建提交并推送到远程（请谨慎使用）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# 提交并推送所有内容

⚠️ **注意**：暂存所有变更、提交并推送到远程。仅在确信所有变更属于同一批次时使用。

## 工作流

### 1. 分析变更
并行运行：
- `git status` - 显示修改/添加/删除/未跟踪的文件
- `git diff --stat` - 显示变更统计
- `git log -1 --oneline` - 显示最近提交以参考消息风格

### 2. 安全检查

**❌ 如果检测到以下内容，立即停止并警告：**
- 密钥：`.env*`、`*.key`、`*.pem`、`credentials.json`、`secrets.yaml`、`id_rsa`、`*.p12`、`*.pfx`、`*.cer`
- API 密钥：任何带有真实值的 `*_API_KEY`、`*_SECRET`、`*_TOKEN` 变量（非占位符，如 `your-api-key`、`xxx`、`placeholder`）
- 大文件：`>10MB` 且未使用 Git LFS
- 构建产物：`node_modules/`、`dist/`、`build/`、`__pycache__/`、`*.pyc`、`.venv/`
- 临时文件：`.DS_Store`、`thumbs.db`、`*.swp`、`*.tmp`

**API 密钥验证：**
检查修改文件中的以下模式：
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

**✅ 验证：**
- `.gitignore` 已正确配置
- 无合并冲突
- 正确的分支（如果是 main/master 则警告）
- API 密钥仅为占位符

### 3. 请求确认

呈现摘要：
```
📊 变更摘要：
- X 个文件已修改，Y 个已添加，Z 个已删除
- 总计：+AAA 行插入，-BBB 行删除

🔒 安全：✅ 无密钥 | ✅ 无大文件 | ⚠️ [警告]
🌿 分支：[名称] → origin/[名称]

我将执行：git add . → commit → push

输入 'yes' 继续或 'no' 取消。
```

**在明确输入 "yes" 之前等待。**

### 4. 执行（确认后）

按顺序运行：
```bash
git add .
git status  # 验证暂存
```

### 5. 生成提交消息

分析变更并创建约定式提交：

**格式：**
```
[类型]: 简短摘要（最多 72 个字符）

- 关键变更 1
- 关键变更 2
- 关键变更 3
```

**类型：** `feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore`、`perf`、`build`、`ci`

**示例：**
```
docs: 更新概念 README 文件，添加全面文档

- 添加架构图和表格
- 包含实践示例
- 扩展最佳实践章节
```

### 6. 提交并推送

```bash
git commit -m "$(cat <<'EOF'
[生成的提交消息]
EOF
)"
git push  # 如果失败：git pull --rebase && git push
git log -1 --oneline --decorate  # 验证
```

### 7. 确认成功

```
✅ 成功推送到远程！

提交：[哈希] [消息]
分支：[分支] → origin/[分支]
文件变更：X（+插入，-删除）
```

## 错误处理

- **git add 失败**：检查权限、锁定文件、验证仓库已初始化
- **git commit 失败**：修复 pre-commit hooks，检查 git 配置（user.name/email）
- **git push 失败**：
  - 非快进：`git pull --rebase && git push`
  - 无远程分支：`git push -u origin [分支]`
  - 受保护分支：改用 PR 工作流

## 适用场景

✅ **适合：**
- 多文件文档更新
- 带测试和文档的功能
- 跨文件的错误修复
- 项目范围的格式化/重构
- 配置变更

❌ **避免：**
- 不确定正在提交什么
- 包含密钥/敏感数据
- 无审查的受保护分支
- 存在合并冲突
- 希望精细提交历史
- Pre-commit hooks 正在失败

## 替代方案

如果用户想要更多控制，建议：
1. **选择性暂存**：审查/暂存特定文件
2. **交互式暂存**：使用 `git add -p` 进行补丁选择
3. **PR 工作流**：创建分支 → 推送 → PR（使用 `/pr` 命令）

**⚠️ 注意**：推送前始终审查变更。如有疑虑，使用单独的 git 命令以获得更多控制。
