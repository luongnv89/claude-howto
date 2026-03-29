---
name: lesson-quiz
version: 1.0.0
description: Interactive lesson-level quiz for Claude Code tutorials. Tests understanding of a specific lesson (01-10) with 8-10 questions mixing conceptual and practical knowledge. Use before a lesson to pre-test, during to check progress, or after to verify mastery. Use when asked to "quiz me on hooks", "test my knowledge of lesson 3", "lesson quiz", "practice quiz for MCP", or "do I understand skills".
---

# 課程測驗

互動式測驗，透過 8-10 道題目測試對特定 Claude Code 課程的理解，提供逐題回饋，並找出需要複習的領域。

## 說明

### 步驟 1：確定課程

若使用者提供了課程作為參數（例如 `/lesson-quiz hooks` 或 `/lesson-quiz 03`），將其對應到課程目錄：

**課程對應表：**
- `01`, `slash-commands`, `commands` → 01-slash-commands
- `02`, `memory` → 02-memory
- `03`, `skills` → 03-skills
- `04`, `subagents`, `agents` → 04-subagents
- `05`, `mcp` → 05-mcp
- `06`, `hooks` → 06-hooks
- `07`, `plugins` → 07-plugins
- `08`, `checkpoints`, `checkpoint` → 08-checkpoints
- `09`, `advanced`, `advanced-features` → 09-advanced-features
- `10`, `cli` → 10-cli

若未提供參數，使用 AskUserQuestion 呈現選擇提示：

**問題 1**（標題：「課程」）：
「您想測驗哪堂課？」
選項：
1. "Slash Commands (01)" — 自訂指令、skills、frontmatter、參數
2. "Memory (02)" — CLAUDE.md、記憶層級、規則、自動記憶
3. "Skills (03)" — 漸進式揭露、自動觸發、SKILL.md
4. "Subagents (04)" — 任務委派、代理設定、隔離

**問題 2**（標題：「課程」）：
「您想測驗哪堂課？（續）」
選項：
1. "MCP (05)" — 外部整合、傳輸協定、伺服器、Tool Search
2. "Hooks (06)" — 事件自動化、PreToolUse、exit codes、JSON I/O
3. "Plugins (07)" — 整合方案、marketplace、plugin.json
4. "更多課程..." — Checkpoints、Advanced Features、CLI

若選擇「更多課程...」，呈現：

**問題 3**（標題：「課程」）：
「請選擇您的課程：」
選項：
1. "Checkpoints (08)" — 回溯、還原、安全實驗
2. "Advanced Features (09)" — 規劃模式、權限、print mode、思考模式
3. "CLI Reference (10)" — 旗標、輸出格式、腳本、管道

### 步驟 2：閱讀課程內容

閱讀課程 README.md 檔案以更新脈絡：
- 讀取檔案：`<lesson-directory>/README.md`

然後使用 `references/question-bank.md` 中該課程的題庫。題庫為每堂課提供 10 道預設題目，附正確答案與解說。

### 步驟 3：呈現測驗

詢問使用者測驗的時機背景：

使用 AskUserQuestion（標題：「時機」）：
「您是在課程的哪個階段進行這次測驗？」
選項：
1. "學前（預先測試）" — 我還沒讀過這堂課，測試我的先備知識
2. "學中（進度檢查）" — 我正在學習這堂課的途中
3. "學後（精熟檢查）" — 我已完成這堂課，想驗證理解程度

此脈絡會影響結果的呈現方式（見步驟 5）。

### 步驟 4：分回合呈現題目

從題庫中選取 10 道題目，分 5 回合呈現，每回合 2 題。每道題使用 AskUserQuestion 附上題目文字與 3-4 個選項。

**重要**：AskUserQuestion 每題最多 4 個選項，每回合 2 題。

每回合呈現 2 道題目。全部 5 回合完成後，進入計分。

**每回合題目格式：**

題庫中的每道題包含：
- `question`：題目文字
- `options`：3-4 個選項（其中一個正確，題庫中有標示）
- `correct`：正確答案標籤
- `explanation`：為何此答案正確
- `category`：「conceptual」或「practical」

使用 AskUserQuestion 呈現每道題目。記錄使用者的每題回答。

### 步驟 5：計分並呈現結果

所有回合結束後，計算分數並呈現結果。

**計分方式：**
- 每答對一題 = 1 分
- 滿分 = 10 分

**等級標準：**
- 9-10：精熟 — 理解優異
- 7-8：熟練 — 掌握良好，有少許缺口
- 5-6：發展中 — 已理解基礎，需要複習
- 3-4：起步 — 有明顯缺口，建議複習
- 0-2：尚未掌握 — 請從本課開頭開始學習

**輸出格式：**

```markdown
## 課程測驗結果：[課程名稱]

**成績：N/10** — [等級標籤]
**測驗時機**：課程[學前 / 學中 / 學後]
**題目分類統計**：N 題概念答對，N 題實作答對

### 逐題結果

| # | 類別 | 題目（簡述） | 您的回答 | 結果 |
|---|----------|-----------------|-------------|--------|
| 1 | 概念 | [題目簡述] | [回答] | [正確 / 錯誤] |
| 2 | 實作 | ... | ... | ... |
| ... | ... | ... | ... | ... |

### 答錯題目 — 請複習以下內容

[針對每道答錯的題目，顯示：]

**Q[N]：[完整題目文字]**
- 您的回答：[所選答案]
- 正確答案：[正確選項]
- 解說：[為何正確]
- 複習：[課程 README 中應重新閱讀的特定章節]

### [時機相關訊息]

[若為學前測試]：
**預先測試成績：N/10。** 這為您建立了基準！請在學習時重點關注您答錯的主題。完成課程後，重新測驗以衡量進步。

[若為學中測試]：
**進度檢查：N/10。** [若 7+：進展很好 — 繼續加油！若 4-6：請在繼續之前複習答錯的主題。若 <4：建議從頭重新閱讀。]

[若為學後測試]：
**精熟檢查：N/10。** [若 9-10：您已精通這堂課！可以進入下一課。若 7-8：即將達成 — 複習答錯的主題後重新測驗。若 <7：請花更多時間學習這堂課，特別是上面標記的章節。]

### 建議的後續步驟

[根據成績與時機：]
- [若精熟]：前往學習路線圖中的下一課：[下一課連結]
- [若熟練]：複習這些特定章節，然後重新測驗：[章節列表]
- [若發展中或以下]：重新閱讀完整課程：[課程連結]。重點關注：[弱項類別列表]
- [提議]：「您想要重新測驗、試試其他課程、還是針對特定主題獲取說明？」
```

### 步驟 6：提供後續選項

呈現結果後，使用 AskUserQuestion：

「您接下來想做什麼？」
選項：
1. "重新測驗" — 再試一次同一堂課的測驗
2. "測驗其他課程" — 切換到不同的課程
3. "解說答錯的主題" — 取得答錯題目的詳細解說
4. "結束" — 結束測驗

若選擇**重新測驗**：回到步驟 4（跳過時機問題，使用相同時機）。
若選擇**測驗其他課程**：回到步驟 1。
若選擇**解說主題**：詢問哪個題號，然後閱讀課程 README.md 的相關章節並搭配範例解說。

## 錯誤處理

### 無效的課程參數
若參數不符合任何課程，顯示有效的課程列表並要求使用者選擇。

### 使用者在測驗中途想退出
若使用者在任何回合中表示想停止，呈現已作答題目的部分結果。

### 找不到課程 README
若在預期路徑找不到 README.md 檔案，通知使用者並建議檢查儲存庫結構。

## 驗證

### 觸發測試套件

**應觸發：**
- "quiz me on hooks"
- "lesson quiz"
- "test my knowledge of lesson 3"
- "practice quiz for MCP"
- "do I understand skills"
- "quiz me on slash commands"
- "lesson-quiz 06"
- "test me on checkpoints"
- "how well do I know the CLI"
- "quiz me before I start the memory lesson"

**不應觸發：**
- "assess my overall level"（請使用 /self-assessment）
- "explain hooks to me"
- "create a hook"
- "what is MCP"
- "review my code"

