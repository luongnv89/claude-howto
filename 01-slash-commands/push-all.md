---
description: 暫存所有變更、建立 commit 並推送至遠端（請謹慎使用）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# 提交並推送所有變更

⚠️ **注意**：暫存所有變更、建立 commit 並推送至遠端。僅在確定所有變更應一起提交時使用。

## 工作流程

### 1. 分析變更
同時執行：
- `git status` - 顯示已修改/新增/刪除/未追蹤的檔案
- `git diff --stat` - 顯示變更統計資料
- `git log -1 --oneline` - 顯示最近提交以參考訊息風格

### 2. 安全檢查

**❌ 偵測到以下情況時停止並警告：**
- 機密資料：`.env*`、`*.key`、`*.pem`、`credentials.json`、`secrets.yaml`、`id_rsa`、`*.p12`、`*.pfx`、`*.cer`
- API 金鑰：任何含有真實值的 `*_API_KEY`、`*_SECRET`、`*_TOKEN` 變數（非佔位符如 `your-api-key`、`xxx`、`placeholder`）
- 大型檔案：`>10MB` 且未使用 Git LFS
- 建置產物：`node_modules/`、`dist/`、`build/`、`__pycache__/`、`*.pyc`、`.venv/`
- 暫存檔案：`.DS_Store`、`thumbs.db`、`*.swp`、`*.tmp`

**API 金鑰驗證：**
檢查已修改檔案中的模式：
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ 偵測到真實金鑰！
AWS_SECRET_KEY=AKIA...         # ❌ 偵測到真實金鑰！
STRIPE_API_KEY=sk_live_...    # ❌ 偵測到真實金鑰！

# ✅ 可接受的佔位符：
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ 驗證：**
- `.gitignore` 已正確配置
- 無合併衝突
- 正確的分支（若為 main/master 則警告）
- API 金鑰僅為佔位符

### 3. 請求確認

呈現摘要：
```
📊 變更摘要：
- X 個檔案修改，Y 個新增，Z 個刪除
- 總計：+AAA 新增行，-BBB 刪除行

🔒 安全性：✅ 無機密資料 | ✅ 無大型檔案 | ⚠️ [警告]
🌿 分支：[名稱] → origin/[名稱]

將執行：git add . → commit → push

輸入 'yes' 繼續或 'no' 取消。
```

**等待明確的 "yes" 後再繼續。**

### 4. 執行（確認後）

依序執行：
```bash
git add .
git status  # 驗證暫存
```

### 5. 產生提交訊息

分析變更並建立 conventional commit：

**格式：**
```
[type]: 簡要摘要（最多 72 個字元）

- 主要變更 1
- 主要變更 2
- 主要變更 3
```

**類型：** `feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore`、`perf`、`build`、`ci`

**範例：**
```
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. 提交並推送

```bash
git commit -m "$(cat <<'EOF'
[產生的提交訊息]
EOF
)"
git push  # 若失敗：git pull --rebase && git push
git log -1 --oneline --decorate  # 驗證
```

### 7. 確認成功

```
✅ 已成功推送至遠端！

提交：[hash] [訊息]
分支：[分支] → origin/[分支]
變更檔案：X（+新增行，-刪除行）
```

## 錯誤處理

- **git add 失敗**：檢查權限、鎖定的檔案、驗證倉庫是否已初始化
- **git commit 失敗**：修復 pre-commit hooks、檢查 git config（user.name/email）
- **git push 失敗**：
  - Non-fast-forward：`git pull --rebase && git push`
  - 無遠端分支：`git push -u origin [branch]`
  - 受保護分支：改用 PR 工作流程

## 適用時機

✅ **適合：**
- 多檔案文件更新
- 包含測試與文件的功能
- 跨檔案的錯誤修復
- 全專案格式化/重構
- 配置變更

❌ **避免：**
- 不確定要提交什麼
- 包含機密/敏感資料
- 未經審查的受保護分支
- 存在合併衝突
- 需要精細的提交歷史
- pre-commit hooks 失敗

## 替代方案

如果使用者需要更多控制，建議：
1. **選擇性暫存**：審查/暫存特定檔案
2. **互動式暫存**：`git add -p` 進行局部選擇
3. **PR 工作流程**：建立分支 → 推送 → PR（使用 `/pr` 指令）

**⚠️ 請記住**：推送前務必審查變更。如有疑慮，使用個別 git 命令以獲得更多控制。

