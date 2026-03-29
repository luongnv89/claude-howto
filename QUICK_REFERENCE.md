<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 範例 - 快速參考卡

## 安裝快速指令

### Slash Commands
```bash
# 安裝全部
cp 01-slash-commands/*.md .claude/commands/

# 安裝特定指令
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# 專案記憶體
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 個人記憶體
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# 個人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 專案 skills
cp -r 03-skills/code-review .claude/skills/
```

### Subagents
```bash
# 安裝全部
cp 04-subagents/*.md .claude/agents/

# 安裝特定代理
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 設定憑證
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安裝設定（專案範圍）
cp 05-mcp/github-mcp.json .mcp.json

# 或使用者範圍：加入 ~/.claude.json
```

### Hooks
```bash
# 安裝 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在設定中配置（~/.claude/settings.json）
```

### Plugins
```bash
# 從範例安裝（如已發布）
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints（檢查點）
```bash
# 檢查點會在每次使用者提示時自動建立
# 要回退，按兩次 Esc 或使用：
/rewind

# 然後選擇：還原程式碼和對話、還原對話、
# 還原程式碼、從此處摘要、或取消
```

### 進階功能
```bash
# 在設定中配置（.claude/settings.json）
# 參見 09-advanced-features/config-examples.json

# 規劃模式
/plan 任務描述

# 權限模式（使用 --permission-mode 旗標）
# default        - 對風險操作要求批准
# acceptEdits    - 自動接受檔案編輯，其他操作要求批准
# plan           - 唯讀分析，不修改
# dontAsk        - 接受所有操作（風險操作除外）
# auto           - 背景分類器自動決定權限
# bypassPermissions - 接受所有操作（需要 --dangerously-skip-permissions）

# 工作階段管理
/resume                # 繼續先前的對話
/rename "name"         # 命名當前工作階段
/fork                  # 分支當前工作階段
claude -c              # 繼續最近的對話
claude -r "session"    # 按名稱/ID 繼續工作階段
```

---

## 功能速查表

| 功能 | 安裝路徑 | 使用方式 |
|---------|-------------|-------|
| **Slash Commands (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | 自動載入 |
| **Skills** | `.claude/skills/*/SKILL.md` | 自動呼叫 |
| **Subagents** | `.claude/agents/*.md` | 自動委派 |
| **MCP** | `.mcp.json`（專案）或 `~/.claude.json`（使用者） | `/mcp__server__action` |
| **Hooks（25 個事件）** | `~/.claude/hooks/*.sh` | 事件觸發（4 種類型） |
| **Plugins** | 透過 `/plugin install` | 整合所有功能 |
| **Checkpoints** | 內建 | `Esc+Esc` 或 `/rewind` |
| **Planning Mode** | 內建 | `/plan <task>` |
| **Permission Modes (6)** | 內建 | `--allowedTools`、`--permission-mode` |
| **Sessions** | 內建 | `/session <command>` |
| **Background Tasks** | 內建 | 在背景執行 |
| **Remote Control** | 內建 | WebSocket API |
| **Web Sessions** | 內建 | `claude web` |
| **Git Worktrees** | 內建 | `/worktree` |
| **Auto Memory** | 內建 | 自動儲存到 CLAUDE.md |
| **Task List** | 內建 | `/task list` |
| **Bundled Skills (5)** | 內建 | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |

---

## 常見使用場景

### 程式碼審查
```bash
# 方法 1：Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# 使用：/optimize

# 方法 2：Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# 使用：自動委派

# 方法 3：Skill
cp -r 03-skills/code-review ~/.claude/skills/
# 使用：自動呼叫

# 方法 4：Plugin（最佳）
/plugin install pr-review
# 使用：/review-pr
```

### 文件撰寫
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin（完整解決方案）
/plugin install documentation
```

### DevOps
```bash
# 完整 plugin
/plugin install devops-automation

# 指令：/deploy、/rollback、/status、/incident
```

### 團隊標準
```bash
# 專案記憶體
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 為你的團隊編輯
vim CLAUDE.md
```

### 自動化與 Hooks
```bash
# 安裝 hooks（25 個事件、4 種類型：command、http、prompt、agent）
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 範例：
# - 預提交測試：pre-commit.sh
# - 自動格式化程式碼：format-code.sh
# - 安全掃描：security-scan.sh

# Auto Mode 用於完全自主工作流程
claude --enable-auto-mode -p "Refactor and test the auth module"
# 或使用 Shift+Tab 在互動模式中切換模式
```

### 安全重構
```bash
# 檢查點在每次提示前自動建立
# 嘗試重構
# 如果成功：繼續
# 如果失敗：按 Esc+Esc 或使用 /rewind 回退
```

### 複雜實作
```bash
# 使用規劃模式
/plan Implement user authentication system

# Claude 建立詳細計畫
# 審查並批准
# Claude 系統化地實作
```

### CI/CD 整合
```bash
# 以無頭模式執行（非互動式）
claude -p "Run all tests and generate report"

# 使用 CI 的權限模式
claude -p "Run tests" --permission-mode dontAsk

# 使用 Auto Mode 進行完全自主的 CI 任務
claude --enable-auto-mode -p "Run tests and fix failures"

# 使用 hooks 進行自動化
# 參見 09-advanced-features/README.md
```

### 學習與實驗
```bash
# 使用 plan 模式進行安全分析
claude --permission-mode plan

# 安全實驗 - 檢查點自動建立
# 如果需要回退：按 Esc+Esc 或使用 /rewind
```

### Agent Teams
```bash
# 啟用 agent teams
export CLAUDE_AGENT_TEAMS=1

# 或在 settings.json 中
{ "agentTeams": { "enabled": true } }

# 開始使用：「使用團隊方式實作功能 X」
```

### 排程任務
```bash
# 每 5 分鐘執行一次指令
/loop 5m /check-status

# 一次性提醒
/loop 30m "remind me to check the deploy"
```

---

## 檔案位置參考

```
你的專案/
├── .claude/
│   ├── commands/              # Slash commands 放這裡
│   ├── agents/                # Subagents 放這裡
│   ├── skills/                # 專案 skills 放這裡
│   └── settings.json          # 專案設定（hooks 等）
├── .mcp.json                  # MCP 設定（專案範圍）
├── CLAUDE.md                  # 專案記憶體
└── src/
    └── api/
        └── CLAUDE.md          # 目錄特定記憶體

使用者主目錄/
├── .claude/
│   ├── commands/              # 個人指令
│   ├── agents/                # 個人代理
│   ├── skills/                # 個人 skills
│   ├── hooks/                 # Hook 腳本
│   ├── settings.json          # 使用者設定
│   ├── managed-settings.d/    # 受管理設定（企業/組織）
│   └── CLAUDE.md              # 個人記憶體
└── .claude.json               # 個人 MCP 設定（使用者範圍）
```

---

## 尋找範例

### 按類別
- **Slash Commands**: `01-slash-commands/`
- **Memory**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagents**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Advanced Features**: `09-advanced-features/`
- **CLI**: `10-cli/`

### 按使用場景
- **效能**: `01-slash-commands/optimize.md`
- **安全**: `04-subagents/secure-reviewer.md`
- **測試**: `04-subagents/test-engineer.md`
- **文件**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### 按複雜度
- **簡單**: Slash commands
- **中等**: Subagents、Memory
- **進階**: Skills、Hooks
- **完整**: Plugins

---

## 學習路徑

### 第 1 天
```bash
# 閱讀概述
cat README.md

# 安裝一個指令
cp 01-slash-commands/optimize.md .claude/commands/

# 試試看
/optimize
```

### 第 2-3 天
```bash
# 設定記憶體
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# 安裝 subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 第 4-5 天
```bash
# 設定 MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# 嘗試 MCP 指令
/mcp__github__list_prs
```

### 第 2 週
```bash
# 安裝 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 讓它自動呼叫
# 只需說：「審查這段程式碼是否有問題」
```

### 第 3 週以上
```bash
# 安裝完整 plugin
/plugin install pr-review

# 使用整合功能
/review-pr
/check-security
/check-tests
```

---

## 新功能（2026 年 3 月）

| 功能 | 描述 | 使用方式 |
|---------|-------------|-------|
| **Auto Mode** | 使用背景分類器的完全自主操作 | `--enable-auto-mode` 旗標，`Shift+Tab` 切換模式 |
| **Channels** | Discord 和 Telegram 整合 | `--channels` 旗標，Discord/Telegram 機器人 |
| **Voice Dictation** | 對 Claude 說話輸入指令和上下文 | `/voice` 指令 |
| **Hooks（25 個事件）** | 擴展的 hook 系統，包含 4 種類型 | command、http、prompt、agent hook 類型 |
| **MCP Elicitation** | MCP 伺服器可在執行期間請求使用者輸入 | 伺服器需要澄清時自動提示 |
| **WebSocket MCP** | MCP 連接的 WebSocket 傳輸 | 在 `.mcp.json` 中使用 `ws://` URL 設定 |
| **Plugin LSP** | Plugins 的 Language Server Protocol 支援 | `userConfig`、`${CLAUDE_PLUGIN_DATA}` 變數 |
| **Remote Control** | 透過 WebSocket API 控制 Claude Code | `claude --remote` 用於外部整合 |
| **Web Sessions** | 瀏覽器版 Claude Code 介面 | `claude web` 啟動 |
| **Desktop App** | 原生桌面應用程式 | 從 claude.ai/download 下載 |
| **Task List** | 管理背景任務 | `/task list`、`/task status <id>` |
| **Auto Memory** | 從對話中自動儲存記憶體 | Claude 自動將關鍵上下文儲存到 CLAUDE.md |
| **Git Worktrees** | 用於並行開發的隔離工作區 | `/worktree` 建立隔離工作區 |
| **Model Selection** | 在 Sonnet 4.6 和 Opus 4.6 之間切換 | `/model` 或 `--model` 旗標 |
| **Agent Teams** | 協調多個代理處理任務 | 使用 `CLAUDE_AGENT_TEAMS=1` 環境變數啟用 |
| **Scheduled Tasks** | 使用 `/loop` 的排程任務 | `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration** | 瀏覽器自動化 | `--chrome` 旗標或 `/chrome` 指令 |
| **Keyboard Customization** | 自訂鍵盤快捷鍵 | `/keybindings` 指令 |

---

## 技巧與訣竅

### 自訂
- 先按原樣使用範例
- 修改以符合你的需求
- 分享給團隊前先測試
- 將設定納入版本控制

### 最佳實踐
- 使用 memory 設定團隊標準
- 使用 plugins 建立完整工作流程
- 使用 subagents 處理複雜任務
- 使用 slash commands 處理快速任務

### 疑難排解
```bash
# 檢查檔案位置
ls -la .claude/commands/
ls -la .claude/agents/

# 驗證 YAML 語法
head -20 .claude/agents/code-reviewer.md

# 測試 MCP 連接
echo $GITHUB_TOKEN
```

---

## 功能矩陣

| 需求 | 使用功能 | 範例 |
|------|----------|---------|
| 快速捷徑 | Slash Command (55+) | `01-slash-commands/optimize.md` |
| 團隊標準 | Memory | `02-memory/project-CLAUDE.md` |
| 自動工作流程 | Skill | `03-skills/code-review/` |
| 專門化任務 | Subagent | `04-subagents/code-reviewer.md` |
| 外部資料 | MCP（+ Elicitation、WebSocket） | `05-mcp/github-mcp.json` |
| 事件自動化 | Hook（25 個事件、4 種類型） | `06-hooks/pre-commit.sh` |
| 完整解決方案 | Plugin（+ LSP 支援） | `07-plugins/pr-review/` |
| 安全實驗 | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| 完全自主 | Auto Mode | `--enable-auto-mode` 或 `Shift+Tab` |
| 聊天整合 | Channels | `--channels`（Discord、Telegram） |
| CI/CD 管道 | CLI | `10-cli/README.md` |

---

## 快速連結

- **主指南**: `README.md`
- **完整索引**: `INDEX.md`
- **摘要**: `EXAMPLES_SUMMARY.md`
- **原始指南**: `claude_concepts_guide.md`

---

## 常見問題

**問：我該使用哪個功能？**
答：從 slash commands 開始，根據需要新增功能。

**問：可以混合使用功能嗎？**
答：可以！它們可以一起運作。Memory + Commands + MCP = 強大。

**問：如何與團隊分享？**
答：將 `.claude/` 目錄提交到 git。

**問：機密資訊怎麼處理？**
答：使用環境變數，永遠不要寫死。

**問：可以修改範例嗎？**
答：當然可以！它們是可自訂的範本。

---

## 入門檢查清單

開始使用檢查清單：

- [ ] 閱讀 `README.md`
- [ ] 安裝 1 個 slash command
- [ ] 試用該指令
- [ ] 建立專案 `CLAUDE.md`
- [ ] 安裝 1 個 subagent
- [ ] 設定 1 個 MCP 整合
- [ ] 安裝 1 個 skill
- [ ] 試用完整的 plugin
- [ ] 根據需求自訂
- [ ] 與團隊分享

---

**快速開始**: `cat README.md`

**完整索引**: `cat INDEX.md`

**本參考卡**: 隨時查閱，方便快速參考！

