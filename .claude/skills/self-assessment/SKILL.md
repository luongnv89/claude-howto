---
name: self-assessment
version: 2.2.0
description: Comprehensive Claude Code self-assessment and learning path advisor. Runs a multi-category quiz covering 10 feature areas, produces a detailed skill profile with per-topic scores, identifies specific gaps, and generates a personalized learning path with prioritized next steps. Use when asked to "assess my level", "take the quiz", "find my level", "where should I start", "what should I learn next", "check my skills", "skill check", or "level up".
---

# 自我評估與學習路徑顧問

全面的互動式評估，評估 Claude Code 在 10 個功能領域的能力，找出具體技能缺口，並產生個人化的學習路徑來提升技能。

## 說明

### 步驟 1：歡迎 & 選擇評估模式

向使用者提供評估深度的選擇：

使用 AskUserQuestion 呈現以下選項：
- **快速評估** — 「8 題，約 2 分鐘。判斷您的總體程度（初學者/中級/進階）並提供學習路徑。」
- **深入評估** — 「5 個類別加上詳細問題，約 5 分鐘。提供各主題技能分數、找出具體缺口，並建立優先排序的學習路徑。」

若使用者選擇**快速評估**，前往步驟 2A。
若使用者選擇**深入評估**，前往步驟 2B。

---

### 步驟 2A：快速評估

呈現兩個多選題（AskUserQuestion 每題最多支援 4 個選項）：

**問題 1**（標題：「基礎」）：
「第 1/2 部分：您已經具備以下哪些 Claude Code 技能？」
選項：
1. "啟動 Claude Code 並對話" — 我能執行 `claude` 並與之互動
2. "建立/編輯過 CLAUDE.md" — 我已設定專案或使用者記憶
3. "使用過 3 個以上 slash commands" — 例如 /help、/compact、/model、/clear
4. "建立過自訂指令/skill" — 撰寫過 SKILL.md 或自訂指令檔案

**問題 2**（標題：「進階」）：
「第 2/2 部分：您已經具備以下哪些進階技能？」
選項：
1. "設定過 MCP 伺服器" — 例如 GitHub、資料庫或其他外部資料來源
2. "設定過 hooks" — 在 ~/.claude/settings.json 中設定過 hooks
3. "建立/使用過 subagents" — 使用 .claude/agents/ 進行任務委派
4. "使用過 print mode (claude -p)" — 使用 `claude -p` 進行非互動式或 CI/CD 使用

**計分方式：**
- 0-2 項 = 等級 1：初學者
- 3-5 項 = 等級 2：中級
- 6-8 項 = 等級 3：進階

前往步驟 3，帶入等級結果，列出未勾選的項目作為缺口。

---

### 步驟 2B：深入評估

呈現 5 回合問題，每回合一次 AskUserQuestion 呼叫。每回合涵蓋 2 個相關功能領域。所有回合使用多選。

**重要**：AskUserQuestion 每題最多支援 4 個選項。每回合恰好 1 題 4 個選項，涵蓋 2 個主題（每主題 2 個選項）。

---

**第 1 回合 — Slash Commands & Memory**（標題：「指令」）

「您做過以下哪些？請選擇所有適用的。」
選項：
1. "建立過自訂 slash command 或 skill" — 撰寫過含 frontmatter 的 SKILL.md 檔案，或建立過 .claude/commands/ 檔案
2. "在指令中使用過動態上下文" — 使用過 `$ARGUMENTS`、`$0`/`$1`、反引號 `!command` 語法，或 `@file` 參考
3. "設定過專案 + 個人記憶" — 建立過專案 CLAUDE.md 和個人 ~/.claude/CLAUDE.md（或 CLAUDE.local.md）
4. "使用過記憶層級功能" — 了解 7 層優先順序，使用過 .claude/rules/ 目錄、路徑特定規則，或 @import 語法

**第 1 回合計分：**
- 選項 1-2 對應 **Slash Commands**（0-2 分）
- 選項 3-4 對應 **Memory**（0-2 分）

---

**第 2 回合 — Skills & Hooks**（標題：「自動化」）

「您做過以下哪些？請選擇所有適用的。」
選項：
1. "安裝並使用過自動觸發的 skill" — 根據描述自動觸發的 skill，無需手動 /command 調用
2. "控制過 skill 調用行為" — 在 SKILL.md frontmatter 中使用過 `disable-model-invocation`、`user-invocable` 或含 agent 欄位的 `context: fork`
3. "設定過 PreToolUse 或 PostToolUse hook" — 設定過在工具執行前/後運行的 hook（例如指令驗證器、自動格式化工具）
4. "使用過進階 hook 功能" — 設定過 prompt-type hooks、SKILL.md 中的元件範圍 hooks、HTTP hooks，或含自訂 JSON 輸出的 hooks（updatedInput、systemMessage）

**第 2 回合計分：**
- 選項 1-2 對應 **Skills**（0-2 分）
- 選項 3-4 對應 **Hooks**（0-2 分）

---

**第 3 回合 — MCP & Subagents**（標題：「整合」）

「您做過以下哪些？請選擇所有適用的。」
選項：
1. "連接過 MCP 伺服器並使用其工具" — 例如用於 PR/issue 的 GitHub MCP、用於查詢的資料庫 MCP，或任何外部資料來源
2. "使用過進階 MCP 功能" — 專案範圍 .mcp.json、OAuth 認證、含 @mention 的 MCP 資源、Tool Search，或 `claude mcp serve`
3. "建立或設定過自訂 subagents" — 在 .claude/agents/ 中定義含自訂工具、模型或權限的代理
4. "使用過進階 subagent 功能" — worktree 隔離、持久性代理記憶、Ctrl+B 背景任務、`Task(agent_name)` 代理白名單，或代理團隊

**第 3 回合計分：**
- 選項 1-2 對應 **MCP**（0-2 分）
- 選項 3-4 對應 **Subagents**（0-2 分）

---

**第 4 回合 — Checkpoints & Advanced Features**（標題：「進階使用者」）

「您做過以下哪些？請選擇所有適用的。」
選項：
1. "使用過 checkpoints 進行安全實驗" — 建立過 checkpoints，使用過 Esc+Esc 或 /rewind，還原過程式碼和/或對話，或使用過 Summarize 選項
2. "使用過規劃模式或延伸思考" — 透過 /plan、Shift+Tab 或 --permission-mode plan 啟動過規劃功能；透過 Alt+T/Option+T 切換過延伸思考
3. "設定過權限模式" — 透過 CLI 旗標、鍵盤快捷鍵或設定使用過 acceptEdits、plan、dontAsk 或 bypassPermissions 模式
4. "使用過遠端/桌面/網頁功能" — 使用過 `claude remote-control`、`claude --remote`、`/teleport`、`/desktop`，或含 `claude -w` 的 worktrees

**第 4 回合計分：**
- 選項 1 對應 **Checkpoints**（0-1 分）
- 選項 2-4 對應 **Advanced Features**（0-3 分，上限 2 分）

---

**第 5 回合 — Plugins & CLI**（標題：「精通」）

「您做過以下哪些？請選擇所有適用的。」
選項：
1. "安裝或建立過 plugin" — 使用過 marketplace 的預設 plugin，或建立過含 plugin.json manifest 的 .claude-plugin/ 目錄
2. "使用過 plugin 進階功能" — Plugin hooks、plugin MCP 伺服器、LSP 設定、plugin 命名空間指令，或用於測試的 --plugin-dir 旗標
3. "在腳本或 CI/CD 中使用過 print mode" — 使用過 `claude -p` 搭配 --output-format json、--max-turns、管道輸入，或整合至 GitHub Actions / CI 流程
4. "使用過進階 CLI 功能" — 工作階段恢復（-c/-r）、--agents 旗標、--json-schema 結構化輸出、--fallback-model、--from-pr，或批次處理迴圈

**第 5 回合計分：**
- 選項 1-2 對應 **Plugins**（0-2 分）
- 選項 3-4 對應 **CLI**（0-2 分）

---

### 步驟 3：計算並呈現結果

#### 3A：快速評估

計算總選擇數並判斷等級。然後呈現：

```markdown
## Claude Code 技能評估結果

### 您的等級：[等級 1：初學者 / 等級 2：中級 / 等級 3：進階]

您勾選了 **N/8** 項。

[根據等級的一句鼓勵語]

### 您的技能檔案

| 領域 | 狀態 |
|------|--------|
| 基本 CLI 與對話 | [已具備/缺口] |
| CLAUDE.md & Memory | [已具備/缺口] |
| Slash Commands（內建） | [已具備/缺口] |
| 自訂指令 & Skills | [已具備/缺口] |
| MCP 伺服器 | [已具備/缺口] |
| Hooks | [已具備/缺口] |
| Subagents | [已具備/缺口] |
| Print Mode & CI/CD | [已具備/缺口] |

### 已識別的缺口

[針對每個未勾選的項目，提供一行說明應學習的內容以及教學連結]

### 您的個人化學習路徑

[輸出等級專屬的學習路徑 — 見步驟 4]
```

#### 3B：深入評估

從 5 個回合計算各主題分數。每個主題獲得 0-2 分。然後呈現：

```markdown
## Claude Code 技能評估結果

### 總體等級：[等級 1 / 等級 2 / 等級 3]

**總分：N/20 分**

[一句鼓勵語]

### 您的技能檔案

| 功能領域 | 分數 | 精熟度 | 狀態 |
|-------------|-------|---------|--------|
| Slash Commands | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| Memory | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| Skills | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| Hooks | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| MCP | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| Subagents | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| Checkpoints | N/1 | [未學/熟練] | [學習/已精通] |
| Advanced Features | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| Plugins | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |
| CLI | N/2 | [未學/基礎/熟練] | [學習/複習/已精通] |

**精熟度說明：** 0 = 未學，1 = 基礎，2 = 熟練

### 優勢領域
[列出分數 2/2 的主題 — 這些已精通]

### 優先缺口（接下來學習）
[列出分數 0 的主題 — 需要優先關注，依依賴關係排序]

### 複習領域
[列出分數 1/2 的主題 — 已知基礎但進階功能尚未使用]

### 您的個人化學習路徑

[輸出缺口專屬的學習路徑 — 見步驟 4]
```

**深入評估的總體等級計算：**
- 0-6 總分 = 等級 1：初學者
- 7-13 總分 = 等級 2：中級
- 14-20 總分 = 等級 3：進階

---

### 步驟 4：產生個人化學習路徑

根據評估結果，產生針對使用者缺口的學習路徑。不要只是重複通用等級路徑 — 要加以調整。

#### 路徑產生規則

1. **跳過已精通的主題**：若某主題得分 2/2，不將其納入路徑。
2. **依依賴順序排列優先級**：Slash Commands 在 Skills 之前，Memory 在 Subagents 之前，等等。依賴順序為：
   - Slash Commands（無依賴）-> Skills（依賴 Slash Commands）
   - Memory（無依賴）-> Subagents（依賴 Memory）
   - CLI 基礎（無依賴）-> CLI 精通（依賴全部）
   - Checkpoints（無依賴）
   - Hooks（依賴 Slash Commands）
   - MCP（無依賴）-> Plugins（依賴 MCP、Skills、Hooks）
   - Advanced Features（依賴所有前述）
3. **分數 1/2 的主題**：建議「深入探討」— 連結到他們缺少的特定進階章節。
4. **估算時間**：僅加總他們需要學習/複習的主題。
5. **分組成階段**：將剩餘主題組織成每階段 2-3 個主題的邏輯階段。

#### 路徑輸出格式

```markdown
### 您的個人化學習路徑

**預估時間**：約 N 小時（已根據您目前的技能調整）

#### 階段 1：[階段名稱]（約 N 小時）
[僅在這些領域有缺口時]

**[主題名稱]** — [從頭學習 / 深入探討進階功能]
- 教學：[教學目錄連結]
- 重點：[他們需要的特定章節/概念]
- 關鍵練習：[一個具體的練習]
- 完成標準：[具體的成功標準]

**[主題名稱]** — ...

---

#### 階段 2：[階段名稱]（約 N 小時）
...

---

### 建議的實作專案

根據您的缺口，嘗試以下實際練習來鞏固學習：

1. **[專案名稱]**：[結合 2-3 個缺口主題的一行描述]
2. **[專案名稱]**：[一行描述]
3. **[專案名稱]**：[一行描述]
```

#### 各主題具體建議

當某主題為缺口時，使用以下具體建議：

**Slash Commands（分數 0）**：
- 教學：[01-slash-commands/](../../../01-slash-commands/)
- 重點：內建指令參考、建立您的第一個 SKILL.md、`$ARGUMENTS` 語法
- 關鍵練習：建立一個 `/optimize` 指令並測試
- 完成標準：您能建立含參數和動態上下文的自訂 skill

**Slash Commands（分數 1 — 複習）**：
- 重點：使用 `!`backtick`` 語法的動態上下文、`@file` 參考、`disable-model-invocation` vs `user-invocable` 控制
- 完成標準：您能建立注入即時指令輸出並控制自身調用行為的 skill

**Memory（分數 0）**：
- 教學：[02-memory/](../../../02-memory/)
- 重點：CLAUDE.md 建立、`/init` 和 `/memory` 指令、`#` 前綴快速更新
- 關鍵練習：建立含您程式碼規範的專案 CLAUDE.md
- 完成標準：Claude 能在不同工作階段記住您的偏好

**Memory（分數 1 — 複習）**：
- 重點：7 層層級和優先順序、含路徑特定規則的 .claude/rules/ 目錄、`@import` 語法（最大深度 5）、Auto Memory MEMORY.md（200 行限制）
- 完成標準：您有針對不同目錄的模組化規則，並了解完整層級

**Skills（分數 0）**：
- 教學：[03-skills/](../../../03-skills/)
- 重點：SKILL.md 格式、透過 description 欄位自動調用、漸進式揭露（3 個載入層級）
- 關鍵練習：安裝 code-review skill 並驗證自動觸發
- 完成標準：skill 能根據對話脈絡自動啟動

**Skills（分數 1 — 複習）**：
- 重點：含 `agent` 欄位的 `context: fork` 用於 subagent 執行、`disable-model-invocation` vs `user-invocable`、2% 上下文預算、打包資源（scripts/、references/、assets/）
- 完成標準：您能建立在 forked 上下文中以 subagent 運行的 skill

**Hooks（分數 0）**：
- 教學：[06-hooks/](../../../06-hooks/)
- 重點：設定結構（matcher + hooks 陣列）、PreToolUse/PostToolUse 事件、exit codes（0=成功，2=阻擋）、JSON 輸入/輸出格式
- 關鍵練習：建立驗證 Bash 指令的 PreToolUse hook
- 完成標準：hook 能在執行前阻擋危險指令

**Hooks（分數 1 — 複習）**：
- 重點：全部 25 個 hook 事件（包括 PostToolUseFailure、StopFailure、TaskCreated、CwdChanged、FileChanged、PostCompact、Elicitation、ElicitationResult）、4 種 hook 類型（command、http、prompt、agent）、SKILL.md frontmatter 中的元件範圍 hooks、含 allowedEnvVars 的 HTTP hooks、用於 SessionStart/CwdChanged/FileChanged 的 `CLAUDE_ENV_FILE`
- 完成標準：您能建立基於 prompt 的 Stop hook 和 skill 中的元件範圍 hook

**MCP（分數 0）**：
- 教學：[05-mcp/](../../../05-mcp/)
- 重點：`claude mcp add` 指令、傳輸類型（建議使用 HTTP）、GitHub MCP 設定、環境變數展開
- 關鍵練習：新增 GitHub MCP 伺服器並查詢 PR
- 完成標準：您能透過 MCP 從外部服務查詢即時資料

**MCP（分數 1 — 複習）**：
- 重點：專案範圍 .mcp.json（需團隊核准）、OAuth 2.0 認證、含 `@server:resource` mention 的 MCP 資源、Tool Search（ENABLE_TOOL_SEARCH）、`claude mcp serve`、輸出限制（10k/25k/50k）
- 完成標準：您有專案 .mcp.json 並了解 Tool Search auto 模式

**Subagents（分數 0）**：
- 教學：[04-subagents/](../../../04-subagents/)
- 重點：代理檔案格式（.claude/agents/*.md）、內建代理（general-purpose、Plan、Explore）、tools/model/permissionMode 設定
- 關鍵練習：建立 code-reviewer subagent 並測試委派
- 完成標準：Claude 將程式碼審查委派給您的自訂代理

**Subagents（分數 1 — 複習）**：
- 重點：worktree 隔離（`isolation: worktree`）、持久性代理記憶（含 scopes 的 `memory` 欄位）、背景代理（Ctrl+B/Ctrl+F）、`Task(agent_name)` 代理白名單、代理團隊（`--teammate-mode`）
- 完成標準：您有一個在 worktree 隔離中運行且含持久性記憶的 subagent

**Checkpoints（分數 0）**：
- 教學：[08-checkpoints/](../../../08-checkpoints/)
- 重點：Esc+Esc 和 /rewind 存取、5 個回溯選項（還原程式碼+對話、僅還原對話、僅還原程式碼、摘要、取消）、限制（bash 檔案系統操作不被追蹤）
- 關鍵練習：進行實驗性變更，然後回溯還原
- 完成標準：您能安心地進行實驗，知道可以回溯

**Advanced Features（分數 0）**：
- 教學：[09-advanced-features/](../../../09-advanced-features/)
- 重點：規劃模式（/plan 或 Shift+Tab）、權限模式（5 種類型）、延伸思考（Alt+T 切換）
- 關鍵練習：使用規劃模式設計一個功能，然後實作
- 完成標準：您能在規劃和實作模式間流暢切換

**Advanced Features（分數 1 — 複習）**：
- 重點：遠端控制（`claude remote-control`）、網頁工作階段（`claude --remote`）、桌面移交（`/desktop`）、worktrees（`claude -w`）、任務清單（Ctrl+T）、企業託管設定
- 完成標準：您能在 CLI、網頁和桌面間移交工作階段

**Plugins（分數 0）**：
- 教學：[07-plugins/](../../../07-plugins/)
- 重點：Plugin 結構（.claude-plugin/plugin.json）、plugin 打包內容（指令、代理、MCP、hooks、設定）、從 marketplace 安裝
- 關鍵練習：安裝一個 plugin 並探索其元件
- 完成標準：您了解何時使用 plugin vs 獨立元件

**Plugins（分數 1 — 複習）**：
- 重點：建立 plugin.json manifest、plugin hooks（hooks/hooks.json）、LSP 設定（.lsp.json）、`${CLAUDE_PLUGIN_ROOT}` 變數、用於測試的 --plugin-dir、marketplace 發布
- 完成標準：您能為團隊建立和測試 plugin

**CLI（分數 0）**：
- 教學：[10-cli/](../../../10-cli/)
- 重點：互動式 vs print mode、`claude -p` 搭配管道、`--output-format json`、工作階段管理（-c/-r）
- 關鍵練習：將檔案透過管道傳送至 `claude -p` 並取得 JSON 輸出
- 完成標準：您能在腳本中非互動式使用 Claude

**CLI（分數 1 — 複習）**：
- 重點：--agents 旗標搭配 JSON 設定、--json-schema 結構化輸出、--fallback-model、--from-pr、--strict-mcp-config、for 迴圈批次處理、`claude mcp serve`
- 完成標準：您有使用含結構化 JSON 輸出的 Claude 的 CI/CD 腳本

---

### 步驟 5：提供後續行動

呈現結果後，詢問使用者接下來想做什麼：

使用 AskUserQuestion 呈現以下選項：
- **開始學習** — 「協助我立即開始學習路徑中的第一個主題」
- **深入探討缺口** — 「詳細解說我的一個缺口領域，讓我在這裡學習」
- **實作專案** — 「設定一個涵蓋我缺口領域的實作專案」
- **重新評估** — 「我想重新測驗（可能用另一種模式）」

若選擇**開始學習**：閱讀第一個缺口教學的 README.md，引導使用者完成第一個練習。
若選擇**深入探討缺口**：詢問哪個缺口主題，然後閱讀相關教學 README.md，搭配範例解說關鍵概念。
若選擇**實作專案**：設計一個結合 2-3 個缺口主題的小型專案，附具體步驟。
若選擇**重新評估**：回到步驟 1。

## 錯誤處理

### 使用者在某回合未選擇任何項目
視為該回合主題 0 分。繼續下一回合。

### 使用者在所有回合都未選擇任何項目
指定等級 1：初學者。鼓勵從頭開始。輸出完整的等級 1 路徑。

### 使用者想重新測驗
從步驟 1 重新開始，進行全新評估。

### 使用者不同意自己的等級
承認他們的偏好。詢問他們認為自己屬於哪個等級。呈現其選擇等級的路徑，附上可能遺漏主題的先備條件檢查。

### 使用者詢問特定主題
若使用者在評估過程中說了類似「告訴我關於 hooks 的事」或「我想學 MCP」，記下來。呈現結果後，無論分數如何，在其學習路徑中突顯該主題。

## 驗證

### 觸發測試套件

**應觸發：**
- "assess my level"
- "take the quiz"
- "find my level"
- "where should I start"
- "what level am I"
- "learning path quiz"
- "self-assessment"
- "what should I learn next"
- "check my skills"
- "skill check"
- "level up"
- "how good am I at Claude Code"
- "evaluate my Claude Code knowledge"

**不應觸發：**
- "review my code"
- "create a skill"
- "help me with MCP"
- "explain slash commands"
- "what is a checkpoint"
