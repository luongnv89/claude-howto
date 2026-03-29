# 課程測驗 — 題庫

每課 10 道題目。每道題包含：類別、題目文字、選項（3-4 個）、正確答案、解說與複習章節。

---

## 第 01 課：Slash Commands

### Q1
- **類別**：概念
- **題目**：Claude Code 中有哪四種 slash commands？
- **選項**：A) 內建、skills、plugin 指令、MCP prompts | B) 內建、自訂、hook 指令、API prompts | C) 系統、使用者、plugin、終端機指令 | D) 核心、擴充、巨集、腳本指令
- **正確答案**：A
- **解說**：Claude Code 有內建指令（如 /help、/compact）、skills（SKILL.md 檔案）、plugin 指令（命名空間的 plugin-name:command）及 MCP prompts（/mcp__server__prompt）。
- **複習**：Slash Commands 類型章節

### Q2
- **類別**：實作
- **題目**：如何將使用者提供的所有參數傳遞給 skill？
- **選項**：A) 使用 `${args}` | B) 使用 `$ARGUMENTS` | C) 使用 `$@` | D) 使用 `$INPUT`
- **正確答案**：B
- **解說**：`$ARGUMENTS` 擷取指令名稱後的所有文字。若要使用位置參數，則使用 `$0`、`$1` 等。
- **複習**：參數處理章節

### Q3
- **類別**：概念
- **題目**：當 skill（.claude/skills/name/SKILL.md）和舊式指令（.claude/commands/name.md）同名時，哪個優先？
- **選項**：A) 舊式指令 | B) Skill | C) 先建立的那個 | D) Claude 詢問使用者選擇
- **正確答案**：B
- **解說**：Skills 在同名情況下優先於舊式指令。Skill 系統取代了較舊的指令系統。
- **複習**：Skill 優先順序章節

### Q4
- **類別**：實作
- **題目**：如何將即時 shell 輸出注入 skill 的 prompt？
- **選項**：A) 使用 `$(command)` 語法 | B) 使用 `!`command`` （反引號加 !）語法 | C) 使用 `@shell:command` 語法 | D) 使用 `{command}` 語法
- **正確答案**：B
- **解說**：`!`command`` 語法會執行 shell 指令，並在 Claude 看到之前將輸出注入 skill prompt。
- **複習**：動態上下文注入章節

### Q5
- **類別**：概念
- **題目**：skill frontmatter 中的 `disable-model-invocation: true` 有什麼作用？
- **選項**：A) 完全阻止 skill 執行 | B) 僅允許使用者調用（Claude 無法自動調用） | C) 從 /help 選單中隱藏 | D) 停用 skill 的 AI 處理
- **正確答案**：B
- **解說**：`disable-model-invocation: true` 表示只有使用者能透過 `/command-name` 觸發指令。Claude 永遠不會自動調用它，適用於有副作用的 skills，如部署。
- **複習**：控制調用章節

### Q6
- **類別**：實作
- **題目**：您想建立一個只有 Claude 能自動調用的 skill（對使用者的 / 選單隱藏）。應設定哪個 frontmatter 欄位？
- **選項**：A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **正確答案**：B
- **解說**：`user-invocable: false` 從使用者的 slash 選單中隱藏 skill，但允許 Claude 根據上下文自動調用。
- **複習**：調用控制矩陣

### Q7
- **類別**：實作
- **題目**：名為「deploy」的新自訂 skill 的正確目錄結構是什麼？
- **選項**：A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **正確答案**：B
- **解說**：Skills 位於 `.claude/skills/` 下的目錄中，內含 `SKILL.md` 檔案。目錄名稱對應指令名稱。
- **複習**：Skill 類型與位置章節

### Q8
- **類別**：概念
- **題目**：Plugin 指令如何避免與使用者指令的名稱衝突？
- **選項**：A) 使用 `plugin-name:command-name` 命名空間 | B) 有特殊的 .plugin 副檔名 | C) 以 `p/` 為前綴 | D) 自動覆蓋使用者指令
- **正確答案**：A
- **解說**：Plugin 指令使用命名空間如 `pr-review:check-security` 來避免與獨立使用者指令的衝突。
- **複習**：Plugin 指令章節

### Q9
- **類別**：實作
- **題目**：您想限制 skill 可使用的工具。應新增哪個 frontmatter 欄位？
- **選項**：A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **正確答案**：B
- **解說**：SKILL.md frontmatter 中的 `allowed-tools` 欄位限定指令可調用的工具範圍。
- **複習**：Frontmatter 欄位參考

### Q10
- **類別**：概念
- **題目**：skill 中的 `@file` 語法用途是什麼？
- **選項**：A) 匯入另一個 skill | B) 參考檔案以將其內容包含在 prompt 中 | C) 建立符號連結 | D) 設定檔案權限
- **正確答案**：B
- **解說**：skill 中的 `@path/to/file` 語法會將被參考檔案的內容包含到 prompt 中，讓 skills 可以引入模板或上下文檔案。
- **複習**：檔案參考章節

---

## 第 02 課：Memory

### Q1
- **類別**：概念
- **題目**：Claude Code 的記憶層級有幾層？最高優先級是什麼？
- **選項**：A) 5 層，使用者記憶最高 | B) 7 層，託管政策最高 | C) 3 層，專案記憶最高 | D) 7 層，自動記憶最高
- **正確答案**：B
- **解說**：層級有 7 層：託管政策 > 專案記憶 > 專案規則 > 使用者記憶 > 使用者規則 > 本地專案記憶 > 自動記憶。託管政策（由管理員設定）具有最高優先級。
- **複習**：記憶層級章節

### Q2
- **類別**：實作
- **題目**：如何在對話中快速新增一條規則到記憶？
- **選項**：A) 輸入 `/memory add "rule text"` | B) 在訊息前加 `#` 前綴（例如 `# always use TypeScript`） | C) 輸入 `/rule "rule text"` | D) 使用 `@add-memory "rule text"`
- **正確答案**：B
- **解說**：`#` 前綴模式允許在對話中快速新增單條規則。Claude 會詢問要儲存到哪個記憶層級。
- **複習**：快速記憶更新章節

### Q3
- **類別**：概念
- **題目**：CLAUDE.md 中 `@path/to/file` 匯入的最大深度是多少？
- **選項**：A) 3 層 | B) 5 層 | C) 10 層 | D) 無限制
- **正確答案**：B
- **解說**：`@import` 語法支援最多 5 層的遞迴匯入，以防止無限迴圈。
- **複習**：匯入語法章節

### Q4
- **類別**：實作
- **題目**：如何將規則檔案的範圍限定為僅套用於 `src/api/` 中的檔案？
- **選項**：A) 將規則放在 `src/api/CLAUDE.md` | B) 在 `.claude/rules/*.md` 檔案中新增 `paths: src/api/**` YAML frontmatter | C) 將檔案命名為 `.claude/rules/api.md` | D) 在規則檔案中使用 `@scope: src/api`
- **正確答案**：B
- **解說**：`.claude/rules/` 中的檔案支援 `paths:` frontmatter 欄位，使用 glob 模式來限定規則的適用目錄。
- **複習**：路徑特定規則章節

### Q5
- **類別**：概念
- **題目**：Auto Memory 的 MEMORY.md 在工作階段開始時會載入多少行？
- **選項**：A) 全部行 | B) 前 100 行 | C) 前 200 行 | D) 前 500 行
- **正確答案**：C
- **解說**：MEMORY.md 的前 200 行會在工作階段開始時自動載入上下文。從 MEMORY.md 參考的主題檔案則按需載入。
- **複習**：Auto Memory 章節

### Q6
- **類別**：實作
- **題目**：您想要不提交到 git 的個人專案偏好設定。應使用哪個檔案？
- **選項**：A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **正確答案**：B
- **解說**：專案根目錄中的 `CLAUDE.local.md` 用於個人專案特定偏好。應將其加入 git ignore。
- **複習**：記憶位置比較

### Q7
- **類別**：概念
- **題目**：`/init` 指令做什麼？
- **選項**：A) 從頭初始化新的 Claude Code 專案 | B) 根據專案結構產生模板 CLAUDE.md | C) 將所有記憶重設為預設值 | D) 建立新的工作階段
- **正確答案**：B
- **解說**：`/init` 分析您的專案並產生包含建議規則和標準的模板 CLAUDE.md。這是一次性的啟動工具。
- **複習**：/init 指令章節

### Q8
- **類別**：實作
- **題目**：如何完全停用 Auto Memory？
- **選項**：A) 刪除 ~/.claude/projects 目錄 | B) 設定 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) 在 CLAUDE.md 中新增 `auto-memory: false` | D) 使用 `/memory disable auto`
- **正確答案**：B
- **解說**：設定 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 可停用自動記憶。值 `0` 強制開啟。未設定 = 預設開啟。
- **複習**：Auto Memory 設定章節

### Q9
- **類別**：概念
- **題目**：較低優先級的記憶層能否覆蓋較高優先級層的規則？
- **選項**：A) 可以，最新的規則總是勝出 | B) 不行，較高層級總是優先 | C) 可以，如果較低層使用 `!important` 旗標 | D) 視規則類型而定
- **正確答案**：B
- **解說**：記憶優先級從託管政策向下流動。較低層級（如自動記憶）無法覆蓋較高層級（如專案記憶）。
- **複習**：記憶層級章節

### Q10
- **類別**：實作
- **題目**：您跨兩個儲存庫工作，想讓 Claude 從兩者載入 CLAUDE.md。應使用什麼旗標？
- **選項**：A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **正確答案**：B
- **解說**：`--add-dir` 旗標從額外的目錄載入 CLAUDE.md，實現多儲存庫上下文。
- **複習**：額外目錄章節

---

## 第 03 課：Skills

### Q1
- **類別**：概念
- **題目**：skill 系統中的漸進式揭露有哪 3 個層級？
- **選項**：A) 中繼資料、說明、資源 | B) 名稱、主體、附件 | C) 標頭、內容、腳本 | D) 摘要、詳情、資料
- **正確答案**：A
- **解說**：層級 1：中繼資料（約 100 tokens，總是載入），層級 2：SKILL.md 主體（<5k tokens，觸發時載入），層級 3：打包資源（scripts/references/assets，按需載入）。
- **複習**：漸進式揭露架構章節

### Q2
- **類別**：實作
- **題目**：skill 被 Claude 自動調用最重要的因素是什麼？
- **選項**：A) skill 的檔案名稱 | B) frontmatter 中的 `description` 欄位含使用時機關鍵字 | C) skill 的目錄位置 | D) `auto-invoke: true` frontmatter 欄位
- **正確答案**：B
- **解說**：Claude 完全根據 `description` 欄位決定是否自動調用 skill。它必須包含具體的觸發短語和情境。
- **複習**：自動調用章節

### Q3
- **類別**：概念
- **題目**：SKILL.md 檔案的建議最大長度是多少？
- **選項**：A) 100 行 | B) 250 行 | C) 500 行 | D) 1000 行
- **正確答案**：C
- **解說**：SKILL.md 應控制在 500 行以內。較大的參考資料應放在 `references/` 子目錄的檔案中。
- **複習**：內容指引章節

### Q4
- **類別**：實作
- **題目**：如何讓 skill 在隔離的 subagent 中以獨立上下文運行？
- **選項**：A) 在 frontmatter 中設定 `isolation: true` | B) 在 frontmatter 中設定 `context: fork` 搭配 `agent` 欄位 | C) 在 frontmatter 中設定 `subagent: true` | D) 將 skill 放在 `.claude/agents/`
- **正確答案**：B
- **解說**：`context: fork` 在獨立上下文中運行 skill，`agent` 欄位指定使用哪種代理類型（例如 `Explore`、`Plan`、自訂代理）。
- **複習**：在 subagents 中運行 skills 章節

### Q5
- **類別**：概念
- **題目**：分配給 skill 中繼資料（層級 1）的大約上下文預算是多少？
- **選項**：A) 上下文視窗的 0.5% | B) 上下文視窗的 2% | C) 上下文視窗的 5% | D) 上下文視窗的 10%
- **正確答案**：B
- **解說**：Skill 中繼資料約佔上下文視窗的 2%（備用值：16,000 字元）。可透過 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 設定。
- **複習**：上下文預算章節

### Q6
- **類別**：實作
- **題目**：一個 skill 需要參考大型 API 規格。應放在哪裡？
- **選項**：A) 內嵌在 SKILL.md 中 | B) 放在 skill 目錄內的 `references/api-spec.md` 檔案 | C) 放在專案的 CLAUDE.md 中 | D) 放在獨立的 `.claude/rules/` 檔案中
- **正確答案**：B
- **解說**：大型參考資料應放在 `references/` 子目錄。Claude 按需載入層級 3 資源，保持 SKILL.md 精簡。
- **複習**：支援檔案結構章節

### Q7
- **類別**：概念
- **題目**：skill 中的「參考內容」與「任務內容」有什麼區別？
- **選項**：A) 參考是唯讀的，任務是可讀寫的 | B) 參考為上下文增加知識，任務提供逐步指示 | C) 參考用於文件，任務用於程式碼 | D) 沒有區別
- **正確答案**：B
- **解說**：參考內容為 Claude 的上下文增加領域知識（例如品牌指南）。任務內容為工作流程提供可操作的逐步指示。
- **複習**：Skill 內容類型章節

### Q8
- **類別**：實作
- **題目**：skill frontmatter 的 `name` 欄位允許哪些字元？
- **選項**：A) 任何字元 | B) 僅小寫字母、數字和連字號（最多 64 個字元） | C) 字母和底線 | D) 僅英數字元
- **正確答案**：B
- **解說**：名稱必須是 kebab-case（小寫、連字號），最多 64 個字元，且不能包含「anthropic」或「claude」。
- **複習**：SKILL.md 格式章節

### Q9
- **類別**：概念
- **題目**：Claude 搜尋 skills 的順序是什麼？
- **選項**：A) 使用者 > 專案 > 企業 | B) 企業 > 個人 > 專案（plugin 使用命名空間） | C) 專案 > 使用者 > 企業 | D) 字母順序
- **正確答案**：B
- **解說**：優先順序為：企業 > 個人 > 專案。Plugin skills 使用命名空間（plugin-name:skill）因此不會衝突。
- **複習**：Skill 類型與位置章節

### Q10
- **類別**：實作
- **題目**：如何阻止 Claude 自動調用 skill，同時仍允許使用者手動使用？
- **選項**：A) 設定 `user-invocable: false` | B) 設定 `disable-model-invocation: true` | C) 移除 description 欄位 | D) 設定 `auto-invoke: false`
- **正確答案**：B
- **解說**：`disable-model-invocation: true` 阻止 Claude 自動調用，但保持 skill 在使用者的 `/` 選單中可手動使用。
- **複習**：控制調用章節

---

## 第 04 課：Subagents

### Q1
- **類別**：概念
- **題目**：Subagents 相較於內嵌對話的主要優勢是什麼？
- **選項**：A) 更快速 | B) 在獨立、乾淨的上下文視窗中運作，防止上下文汙染 | C) 能使用更多工具 | D) 更好的錯誤處理
- **正確答案**：B
- **解說**：Subagents 獲得全新的上下文視窗，只接收主代理傳遞的內容。這防止主對話被任務特定的細節汙染。
- **複習**：概覽章節

### Q2
- **類別**：實作
- **題目**：代理定義的優先順序是什麼？
- **選項**：A) 專案 > 使用者 > CLI | B) CLI > 使用者 > 專案 | C) 使用者 > 專案 > CLI | D) 全部相同優先級
- **正確答案**：B
- **解說**：CLI 定義的代理（`--agents` 旗標）覆蓋使用者層級（`~/.claude/agents/`），使用者層級覆蓋專案層級（`.claude/agents/`）。
- **複習**：檔案位置章節

### Q3
- **類別**：概念
- **題目**：哪個內建 subagent 使用 Haiku 模型並針對唯讀程式碼庫探索進行最佳化？
- **選項**：A) general-purpose | B) Plan | C) Explore | D) Bash
- **正確答案**：C
- **解說**：Explore subagent 使用 Haiku 進行快速、唯讀的程式碼庫探索。支援三種徹底程度：quick、medium、very thorough。
- **複習**：內建 subagents 章節

### Q4
- **類別**：實作
- **題目**：如何限制協調代理可以產生的 subagents？
- **選項**：A) 使用 `allowed-agents:` 欄位 | B) 在 `tools` 欄位中使用 `Task(agent_name)` 語法 | C) 設定 `spawn-limit: 2` | D) 使用 `restrict-agents: [name1, name2]`
- **正確答案**：B
- **解說**：在 tools 欄位中加入 `Task(worker, researcher)` 建立白名單 — 代理只能產生名為「worker」或「researcher」的 subagents。
- **複習**：限制可產生的 subagents 章節

### Q5
- **類別**：概念
- **題目**：subagent 的 `isolation: worktree` 做什麼？
- **選項**：A) 在 Docker 容器中運行代理 | B) 給代理獨立的 git worktree，使變更不影響主工作目錄 | C) 阻止代理讀取任何檔案 | D) 在沙箱中運行代理
- **正確答案**：B
- **解說**：Worktree 隔離建立獨立的 git worktree。若代理未做任何變更，會自動清除。若有變更，會回傳 worktree 路徑和分支。
- **複習**：Worktree 隔離章節

### Q6
- **類別**：實作
- **題目**：如何讓 subagent 在背景執行？
- **選項**：A) 在代理設定中設定 `background: true` | B) 在代理設定中使用 `async: true` | C) 啟動後按 Ctrl+D | D) 使用 `--background` CLI 旗標
- **正確答案**：A
- **解說**：代理設定中的 `background: true` 讓 subagent 總是以背景任務執行。使用者也可用 Ctrl+B 將前景任務送到背景。
- **複習**：背景 subagents 章節

### Q7
- **類別**：概念
- **題目**：subagent 中含 scope `project` 的 `memory` 欄位做什麼？
- **選項**：A) 提供專案 CLAUDE.md 的讀取權限 | B) 建立限定於當前專案的持久性記憶目錄 | C) 共享主代理的對話歷史 | D) 載入專案的 git 歷史
- **正確答案**：B
- **解說**：`memory` 欄位為 subagent 建立持久性目錄。scope `project` 表示記憶與當前專案綁定。代理的 MEMORY.md 前 200 行會自動載入。
- **複習**：持久性記憶章節

### Q8
- **類別**：實作
- **題目**：如何在 subagent 的描述中加入鼓勵 Claude 自動委派任務的短語？
- **選項**：A) 加入 "priority: high" | B) 在描述中加入 "use PROACTIVELY" 或 "MUST BE USED" | C) 設定 `auto-delegate: true` | D) 加入 "trigger: always"
- **正確答案**：B
- **解說**：在描述中加入如 "use PROACTIVELY" 或 "MUST BE USED" 的短語，可強烈鼓勵 Claude 自動委派匹配的任務。
- **複習**：自動委派章節

### Q9
- **類別**：概念
- **題目**：subagent 的有效 `permissionMode` 值有哪些？
- **選項**：A) read、write、admin | B) default、acceptEdits、bypassPermissions、plan、dontAsk、auto | C) safe、normal、dangerous | D) restricted、standard、elevated
- **正確答案**：B
- **解說**：Subagents 支援六種權限模式：default（所有事都提示）、acceptEdits（自動接受檔案編輯）、bypassPermissions（跳過全部）、plan（唯讀）、dontAsk（除非預先核准否則自動拒絕）、auto（背景分類器決定）。
- **複習**：設定欄位章節

### Q10
- **類別**：實作
- **題目**：如何恢復一個從先前執行回傳 agentId 的 subagent？
- **選項**：A) 使用 `/resume agent-id` | B) 呼叫 Task 工具時傳入含 agentId 的 `resume` 參數 | C) 使用 `claude -r agent-id` | D) Subagents 無法恢復
- **正確答案**：B
- **解說**：Subagents 可透過傳入含先前回傳的 agentId 的 `resume` 參數來恢復，完整上下文會被保留。
- **複習**：可恢復的代理章節

---

## 第 05 課：MCP

### Q1
- **類別**：概念
- **題目**：MCP 有哪三種傳輸協定？建議使用哪個？
- **選項**：A) HTTP（建議）、Stdio、SSE（已棄用） | B) WebSocket（建議）、REST、gRPC | C) TCP、UDP、HTTP | D) Stdio（建議）、HTTP、SSE
- **正確答案**：A
- **解說**：HTTP 建議用於遠端伺服器。Stdio 用於本地程序（目前最常見）。SSE 已棄用但仍支援。
- **複習**：傳輸協定章節

### Q2
- **類別**：實作
- **題目**：如何透過 CLI 新增 GitHub MCP 伺服器？
- **選項**：A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **正確答案**：B
- **解說**：使用 `claude mcp add` 搭配 `--transport` 旗標、名稱和伺服器 URL。若為 stdio：`claude mcp add github -- npx -y @modelcontextprotocol/server-github`。
- **複習**：MCP 設定管理章節

### Q3
- **類別**：概念
- **題目**：當 MCP 工具描述超過上下文視窗的 10% 時會發生什麼？
- **選項**：A) 被截斷 | B) Tool Search 自動啟用以動態選擇相關工具 | C) Claude 顯示錯誤 | D) 額外工具被停用
- **正確答案**：B
- **解說**：當工具超過上下文的 10% 時，MCP Tool Search 會自動啟用。它需要 Sonnet 4 或 Opus 4 以上（不支援 Haiku）。
- **複習**：MCP Tool Search 章節

### Q4
- **類別**：實作
- **題目**：如何在 MCP 設定中使用環境變數備用值？
- **選項**：A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **正確答案**：B
- **解說**：`${VAR:-default}` 在環境變數未設定時提供備用值。不含備用值的 `${VAR}` 在未設定時會報錯。
- **複習**：環境變數展開章節

### Q5
- **類別**：概念
- **題目**：MCP 和 Memory 在資料存取方面有什麼區別？
- **選項**：A) MCP 更快，Memory 較慢 | B) MCP 用於即時/變動的外部資料，Memory 用於持久/靜態的偏好設定 | C) MCP 用於程式碼，Memory 用於文字 | D) 可互換使用
- **正確答案**：B
- **解說**：MCP 連接即時、變動的外部資料來源（API、資料庫）。Memory 儲存持久、靜態的專案上下文和偏好設定。
- **複習**：MCP vs Memory 章節

### Q6
- **類別**：實作
- **題目**：團隊成員首次遇到專案範圍的 `.mcp.json` 時會發生什麼？
- **選項**：A) 自動載入 | B) 他們會收到信任專案 MCP 伺服器的核准提示 | C) 除非透過設定選擇加入，否則被忽略 | D) Claude 請管理員核准
- **正確答案**：B
- **解說**：專案範圍的 `.mcp.json` 在每個團隊成員首次使用時觸發安全核准提示。這是刻意的設計 — 防止不受信任的 MCP 伺服器。
- **複習**：MCP 範圍章節

### Q7
- **類別**：概念
- **題目**：`claude mcp serve` 做什麼？
- **選項**：A) 啟動 MCP 伺服器儀表板 | B) 讓 Claude Code 本身作為 MCP 伺服器供其他應用程式使用 | C) 提供 MCP 文件 | D) 測試 MCP 伺服器連線
- **正確答案**：B
- **解說**：`claude mcp serve` 將 Claude Code 變成 MCP 伺服器，啟用多代理協調，讓一個 Claude 實例可被另一個控制。
- **複習**：Claude 作為 MCP 伺服器章節

### Q8
- **類別**：實作
- **題目**：MCP 工具的預設最大輸出大小是多少？
- **選項**：A) 5,000 tokens | B) 10,000 tokens | C) 25,000 tokens | D) 50,000 tokens
- **正確答案**：C
- **解說**：預設最大值為 25,000 tokens（`MAX_MCP_OUTPUT_TOKENS`）。10k tokens 時會顯示警告。磁碟持久化上限為 50k 字元。
- **複習**：MCP 輸出限制章節

### Q9
- **類別**：概念
- **題目**：在託管設定中，當 `allowedMcpServers` 和 `deniedMcpServers` 同時匹配一個伺服器時，哪個勝出？
- **選項**：A) 允許勝出 | B) 拒絕勝出 | C) 最後設定的勝出 | D) 兩者獨立套用
- **正確答案**：B
- **解說**：在託管 MCP 設定中，拒絕規則總是優先於允許規則。
- **複習**：託管 MCP 設定章節

### Q10
- **類別**：實作
- **題目**：如何在對話中參考 MCP 資源？
- **選項**：A) 使用 `/mcp resource-name` | B) 使用 `@server-name:protocol://resource/path` mention 語法 | C) 使用 `mcp.get("resource")` | D) 資源自動載入
- **正確答案**：B
- **解說**：MCP 資源透過對話中的 `@server-name:protocol://resource/path` mention 語法存取。
- **複習**：MCP 資源章節

---

## 第 06 課：Hooks

### Q1
- **類別**：概念
- **題目**：Claude Code 中有哪四種 hooks？
- **選項**：A) Pre、Post、Error 和 Filter hooks | B) Command、HTTP、Prompt 和 Agent hooks | C) Before、After、Around 和 Through hooks | D) Input、Output、Filter 和 Transform hooks
- **正確答案**：B
- **解說**：Command hooks 執行 shell 腳本，HTTP hooks 呼叫 webhook 端點，Prompt hooks 使用單輪 LLM 評估，Agent hooks 使用基於 subagent 的驗證。
- **複習**：Hook 類型章節

### Q2
- **類別**：實作
- **題目**：hook 腳本以 exit code 2 退出。會發生什麼？
- **選項**：A) 顯示非阻擋性警告 | B) 阻擋性錯誤 — stderr 作為錯誤顯示給 Claude，工具使用被阻止 | C) Hook 被重試 | D) 工作階段結束
- **正確答案**：B
- **解說**：Exit code 0 = 成功/繼續，exit code 2 = 阻擋性錯誤（stderr 作為錯誤顯示），其他非零值 = 非阻擋性（stderr 僅在 verbose 中顯示）。
- **複習**：Exit codes 章節

### Q3
- **類別**：概念
- **題目**：PreToolUse hook 在 stdin 上接收哪些 JSON 欄位？
- **選項**：A) `tool_name` 和 `tool_output` | B) `session_id`、`tool_name`、`tool_input`、`hook_event_name`、`cwd` 等 | C) 僅 `tool_name` | D) 完整的對話歷史
- **正確答案**：B
- **解說**：Hooks 在 stdin 上接收包含以下欄位的 JSON 物件：session_id、transcript_path、hook_event_name、tool_name、tool_input、tool_use_id、cwd 和 permission_mode。
- **複習**：JSON 輸入結構章節

### Q4
- **類別**：實作
- **題目**：PreToolUse hook 如何在執行前修改工具的輸入參數？
- **選項**：A) 在 stderr 上回傳修改後的 JSON | B) 在 stdout 上回傳含 `updatedInput` 欄位的 JSON（exit code 0） | C) 寫入暫存檔 | D) Hooks 無法修改輸入
- **正確答案**：B
- **解說**：PreToolUse hook 可在 stdout 上輸出含 `"updatedInput": {...}` 的 JSON（搭配 exit 0），在 Claude 使用前修改工具的參數。
- **複習**：PreToolUse 輸出章節

### Q5
- **類別**：概念
- **題目**：哪個 hook 事件支援 `CLAUDE_ENV_FILE` 將環境變數持久化到工作階段？
- **選項**：A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) 所有事件
- **正確答案**：C
- **解說**：只有 SessionStart hooks 能使用 `CLAUDE_ENV_FILE` 將環境變數持久化到工作階段。
- **複習**：SessionStart 章節

### Q6
- **類別**：實作
- **題目**：您想要一個僅在 skill 首次載入時運行一次的 hook，而非每次工具呼叫都運行。應新增什麼欄位？
- **選項**：A) `run-once: true` | B) 在元件 hook 定義中加入 `once: true` | C) `single: true` | D) `max-runs: 1`
- **正確答案**：B
- **解說**：元件範圍 hooks（定義在 SKILL.md 或 agent frontmatter 中）支援 `once: true`，僅在首次啟動時運行。
- **複習**：元件範圍 hooks 章節

### Q7
- **類別**：概念
- **題目**：在 subagent 的 frontmatter 中定義的 Stop hook 會自動轉換成什麼？
- **選項**：A) PostToolUse hook | B) SubagentStop hook | C) SessionEnd hook | D) 維持 Stop hook
- **正確答案**：B
- **解說**：當 Stop hook 放在 subagent 的 frontmatter 中時，會自動轉換為 SubagentStop，在該特定 subagent 完成時運行。
- **複習**：元件範圍 hooks 章節

### Q8
- **類別**：實作
- **題目**：如何將 hook 匹配到特定伺服器的所有 MCP 工具？
- **選項**：A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"`（regex 模式） | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **正確答案**：B
- **解說**：matchers 使用 regex 模式。MCP 工具遵循 `mcp__server__tool` 命名慣例，所以 `mcp__github__.*` 匹配所有 GitHub MCP 工具。
- **複習**：Matcher 模式章節

### Q9
- **類別**：概念
- **題目**：Claude Code 總共支援多少個 hook 事件？
- **選項**：A) 10 | B) 16 | C) 25 | D) 30
- **正確答案**：C
- **解說**：Claude Code 支援 25 個 hook 事件：PreToolUse、PostToolUse、PostToolUseFailure、UserPromptSubmit、Stop、StopFailure、SubagentStop、SubagentStart、PermissionRequest、Notification、PreCompact、PostCompact、SessionStart、SessionEnd、WorktreeCreate、WorktreeRemove、ConfigChange、CwdChanged、FileChanged、TeammateIdle、TaskCompleted、TaskCreated、Elicitation、ElicitationResult、InstructionsLoaded。
- **複習**：Hook 事件表

### Q10
- **類別**：實作
- **題目**：您想除錯為何 hook 沒有觸發。最佳方法是什麼？
- **選項**：A) 在 hook 腳本中加入 print 語句 | B) 使用 `--debug` 旗標和 `Ctrl+O` 開啟 verbose 模式 | C) 檢查系統日誌 | D) Hooks 沒有除錯工具
- **正確答案**：B
- **解說**：`--debug` 旗標和 `Ctrl+O` verbose 模式顯示 hook 執行細節，包括哪些 hooks 觸發、它們的輸入和輸出。
- **複習**：除錯章節

---

## 第 07 課：Plugins

### Q1
- **類別**：概念
- **題目**：plugin 的核心 manifest 檔案是什麼？位於何處？
- **選項**：A) 根目錄中的 `plugin.yaml` | B) `.claude-plugin/plugin.json` | C) 含 "claude" 鍵的 `package.json` | D) `.claude/plugin.md`
- **正確答案**：B
- **解說**：Plugin manifest 位於 `.claude-plugin/plugin.json`，包含必填欄位：name、description、version、author。
- **複習**：Plugin 定義結構章節

### Q2
- **類別**：實作
- **題目**：如何在發布前本地測試 plugin？
- **選項**：A) 使用 `/plugin test ./my-plugin` | B) 使用 `claude --plugin-dir ./my-plugin` | C) 使用 `claude plugin validate ./my-plugin` | D) 複製到 ~/.claude/plugins/
- **正確答案**：B
- **解說**：`--plugin-dir` 旗標從本地目錄載入 plugin 進行測試。可重複使用以載入多個 plugins。
- **複習**：測試章節

### Q3
- **類別**：概念
- **題目**：在 plugin hooks 和 MCP 設定中，可使用什麼環境變數來參考 plugin 的安裝目錄？
- **選項**：A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **正確答案**：B
- **解說**：`${CLAUDE_PLUGIN_ROOT}` 解析為 plugin 的安裝目錄，使 hooks 和 MCP 設定中的路徑參考具有可攜性。
- **複習**：Plugin 目錄結構章節

### Q4
- **類別**：實作
- **題目**：「pr-review」plugin 中有一個名為「check-security」的指令。使用者如何調用？
- **選項**：A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **正確答案**：B
- **解說**：Plugin 指令使用 `plugin-name:command-name` 命名空間來避免與使用者指令和其他 plugins 的衝突。
- **複習**：Plugin 指令章節

### Q5
- **類別**：概念
- **題目**：Plugin 可以打包哪些元件？
- **選項**：A) 僅指令和設定 | B) 指令、代理、skills、hooks、MCP 伺服器、LSP 設定、設定、模板、腳本 | C) 僅指令、hooks 和 MCP 伺服器 | D) 僅 skills 和代理
- **正確答案**：B
- **解說**：Plugins 可打包：commands/、agents/、skills/、hooks/hooks.json、.mcp.json、.lsp.json、settings.json、templates/、scripts/、docs/、tests/。
- **複習**：Plugin 目錄結構章節

### Q6
- **類別**：實作
- **題目**：如何從 GitHub 安裝 plugin？
- **選項**：A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) `git clone` 然後 `claude plugin register`
- **正確答案**：B
- **解說**：使用 `/plugin install github:username/repo` 直接從 GitHub 儲存庫安裝。
- **複習**：安裝方法章節

### Q7
- **類別**：概念
- **題目**：plugin 的 `settings.json` 中 `agent` 鍵做什麼？
- **選項**：A) 指定認證憑證 | B) 設定 plugin 的主執行緒代理 | C) 列出可用的 subagents | D) 設定代理權限
- **正確答案**：B
- **解說**：plugin 的 settings.json 中 `agent` 鍵指定 plugin 啟用時作為主執行緒代理的代理定義。
- **複習**：Plugin 設定章節

### Q8
- **類別**：實作
- **題目**：如何管理 plugin 生命週期（啟用/停用/更新）？
- **選項**：A) 手動編輯設定檔 | B) 使用 `/plugin enable`、`/plugin disable`、`/plugin update plugin-name` | C) 使用 `claude plugin-manager` | D) 重新安裝 plugin
- **正確答案**：B
- **解說**：Claude Code 提供完整生命週期管理的 slash commands：enable、disable、update、uninstall。
- **複習**：安裝方法章節

### Q9
- **類別**：概念
- **題目**：Plugin 相較於獨立 skills/hooks/MCP 的主要優勢是什麼？
- **選項**：A) Plugins 更快 | B) 單一指令安裝、版本控制、marketplace 分發、將所有元件打包在一起 | C) Plugins 有更多權限 | D) Plugins 可離線使用
- **正確答案**：B
- **解說**：Plugins 將多個元件打包成一個可安裝的單元，具有版本控制、marketplace 分發和自動更新功能 — 相對於獨立元件的手動設定。
- **複習**：獨立 vs Plugin 比較章節

### Q10
- **類別**：實作
- **題目**：Plugin hooks 設定在 plugin 目錄結構中的位置？
- **選項**：A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` hooks 區段 | D) `.claude/settings.json`
- **正確答案**：B
- **解說**：Plugin hooks 在 plugin 目錄結構中的 `hooks/hooks.json` 設定。
- **複習**：Plugin hooks 章節

---

## 第 08 課：Checkpoints

### Q1
- **類別**：概念
- **題目**：Checkpoints 擷取哪四種內容？
- **選項**：A) Git commits、branches、tags、stashes | B) 訊息、檔案修改、工具使用歷史、工作階段上下文 | C) 程式碼、測試、日誌、設定 | D) 輸入、輸出、錯誤、時間
- **正確答案**：B
- **解說**：Checkpoints 擷取對話訊息、Claude 工具所做的檔案修改、工具使用歷史和工作階段上下文。
- **複習**：概覽章節

### Q2
- **類別**：實作
- **題目**：如何存取 checkpoint 瀏覽器？
- **選項**：A) 使用 `/checkpoints` 指令 | B) 按 `Esc + Esc`（連按兩次 Escape）或使用 `/rewind` | C) 使用 `/history` 指令 | D) 按 `Ctrl+Z`
- **正確答案**：B
- **解說**：連按兩次 Escape（Esc+Esc）或 `/rewind` 指令可開啟 checkpoint 瀏覽器來選擇還原點。
- **複習**：存取 checkpoints 章節

### Q3
- **類別**：概念
- **題目**：有多少個回溯選項？分別是什麼？
- **選項**：A) 3 個：復原、重做、重設 | B) 5 個：還原程式碼+對話、僅還原對話、僅還原程式碼、從此處摘要、取消 | C) 2 個：完整還原、部分還原 | D) 4 個：程式碼、訊息、兩者、取消
- **正確答案**：B
- **解說**：5 個選項為：還原程式碼和對話（完整回溯）、僅還原對話、僅還原程式碼、從此處摘要（壓縮）、取消。
- **複習**：回溯選項章節

### Q4
- **類別**：實作
- **題目**：您在 Claude Code 中透過 Bash 使用了 `rm -rf temp/`，然後想回溯。Checkpoint 會還原那些檔案嗎？
- **選項**：A) 會，checkpoints 擷取所有內容 | B) 不會，Bash 檔案系統操作（rm、mv、cp）不被 checkpoints 追蹤 | C) 只有在使用 Edit 工具時才會 | D) 只有在 autoCheckpoint 啟用時才會
- **正確答案**：B
- **解說**：Checkpoints 只追蹤由 Claude 工具（Write、Edit）所做的檔案變更。rm、mv、cp 等 Bash 指令在 checkpoint 追蹤之外運作。
- **複習**：限制章節

### Q5
- **類別**：概念
- **題目**：Checkpoints 保留多久？
- **選項**：A) 直到工作階段結束 | B) 7 天 | C) 30 天 | D) 永久
- **正確答案**：C
- **解說**：Checkpoints 跨工作階段保留最多 30 天，之後自動清除。
- **複習**：Checkpoint 持久性章節

### Q6
- **類別**：實作
- **題目**：回溯時「從此處摘要」做什麼？
- **選項**：A) 從該點刪除對話 | B) 將對話壓縮為 AI 產生的摘要，同時在逐字稿中保留原始內容 | C) 建立變更的項目符號清單 | D) 將對話匯出為檔案
- **正確答案**：B
- **解說**：摘要將對話壓縮為較短的 AI 產生摘要。原始完整文字保留在逐字稿檔案中。
- **複習**：摘要選項章節

### Q7
- **類別**：概念
- **題目**：Checkpoints 何時自動建立？
- **選項**：A) 每 5 分鐘 | B) 每次使用者提示時 | C) 僅在手動儲存時 | D) 每次工具使用後
- **正確答案**：B
- **解說**：自動 checkpoints 在每次使用者提示時建立，在 Claude 處理請求之前擷取狀態。
- **複習**：自動 checkpoints 章節

### Q8
- **類別**：實作
- **題目**：如何停用自動 checkpoint 建立？
- **選項**：A) 使用 `--no-checkpoints` 旗標 | B) 在設定中設定 `autoCheckpoint: false` | C) 刪除 checkpoints 目錄 | D) Checkpoints 無法停用
- **正確答案**：B
- **解說**：在設定中設定 `autoCheckpoint: false` 可停用自動 checkpoint 建立（預設為 true）。
- **複習**：設定章節

### Q9
- **類別**：概念
- **題目**：Checkpoints 能取代 git commits 嗎？
- **選項**：A) 能，它們更強大 | B) 不能，它們是互補的 — checkpoints 限定於工作階段且會過期，git 是永久且可共享的 | C) 能，適用於小型專案 | D) 僅適用於單人開發
- **正確答案**：B
- **解說**：Checkpoints 是暫時的（30 天保留期）、限定於工作階段且無法共享。Git commits 是永久的、可稽核且可共享的。兩者搭配使用。
- **複習**：與 git 整合章節

### Q10
- **類別**：實作
- **題目**：您想比較兩種不同的方法。建議的 checkpoint 工作流程是什麼？
- **選項**：A) 建立兩個獨立的工作階段 | B) 在方法 A 前建立 checkpoint，嘗試後回溯到 checkpoint，嘗試方法 B，比較結果 | C) 改用 git branches | D) 沒有好的方法來比較
- **正確答案**：B
- **解說**：分支策略：在乾淨狀態建立 checkpoint，嘗試方法 A，記錄結果，回溯到同一 checkpoint，嘗試方法 B。比較兩個結果。
- **複習**：工作流程模式章節

---

## 第 09 課：Advanced Features

### Q1
- **類別**：概念
- **題目**：Claude Code 中有哪六種權限模式？
- **選項**：A) read、write、execute、admin、root、sudo | B) default、acceptEdits、plan、auto、dontAsk、bypassPermissions | C) safe、normal、elevated、admin、unrestricted、god | D) view、edit、run、deploy、full、bypass
- **正確答案**：B
- **解說**：六種模式為：default（所有事都提示）、acceptEdits（自動接受檔案編輯）、plan（唯讀分析）、auto（背景分類器決定）、dontAsk（除非預先核准否則自動拒絕）、bypassPermissions（跳過所有檢查）。
- **複習**：權限模式章節

### Q2
- **類別**：實作
- **題目**：如何啟動規劃模式？
- **選項**：A) 僅透過 `/plan` 指令 | B) 透過 `/plan`、`Shift+Tab`/`Alt+M`、`--permission-mode plan` 旗標，或預設設定 | C) 僅透過 `--planning` 旗標 | D) 規劃模式總是開啟
- **正確答案**：B
- **解說**：規劃模式可透過多種方式啟動：/plan 指令、Shift+Tab/Alt+M 鍵盤快捷鍵、--permission-mode plan CLI 旗標，或在設定中設為預設。
- **複習**：規劃模式章節

### Q3
- **類別**：概念
- **題目**：`opusplan` 模型別名做什麼？
- **選項**：A) 所有事都使用 Opus | B) 規劃階段使用 Opus，實作階段使用 Sonnet | C) 使用特別最佳化的規劃模型 | D) 自動啟用規劃模式
- **正確答案**：B
- **解說**：`opusplan` 是一個模型別名，規劃階段使用 Opus（更高品質的分析），執行階段使用 Sonnet（更快的實作）。
- **複習**：規劃模式章節

### Q4
- **類別**：實作
- **題目**：如何在工作階段中切換延伸思考？
- **選項**：A) 輸入 `/think` | B) 按 `Option+T`（macOS）或 `Alt+T` | C) 使用 `--thinking` 旗標 | D) 總是啟用且無法切換
- **正確答案**：B
- **解說**：Option+T（macOS）或 Alt+T 可切換延伸思考。所有模型預設啟用。Opus 4.6 支援自適應努力等級。
- **複習**：延伸思考章節

### Q5
- **類別**：概念
- **題目**：「think」或「ultrathink」是否為啟動增強思考的特殊關鍵字？
- **選項**：A) 是，它們啟動更深層的推理 | B) 否，它們被視為普通的提示文字，沒有特殊行為 | C) 只有「ultrathink」是特殊的 | D) 僅適用於 Opus
- **正確答案**：B
- **解說**：文件明確指出這些是普通的提示指令，不是特殊的啟動關鍵字。延伸思考透過 Alt+T 切換和環境變數控制。
- **複習**：延伸思考章節

### Q6
- **類別**：實作
- **題目**：如何在 CI/CD 流程中以結構化 JSON 輸出和回合限制運行 Claude？
- **選項**：A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **正確答案**：B
- **解說**：Print mode（`-p`）搭配 `--output-format json` 和 `--max-turns` 是標準的 CI/CD 整合模式。
- **複習**：Headless/Print Mode 章節

### Q7
- **類別**：概念
- **題目**：任務清單功能（Ctrl+T）提供什麼？
- **選項**：A) 執行中背景程序的清單 | B) 在上下文壓縮後仍保留的持久性待辦清單，可透過 `CLAUDE_CODE_TASK_LIST_ID` 共享 | C) 過去工作階段的歷史 | D) 待處理工具呼叫的佇列
- **正確答案**：B
- **解說**：任務清單（Ctrl+T）在上下文壓縮時持續存在，可透過使用 `CLAUDE_CODE_TASK_LIST_ID` 的命名任務目錄跨工作階段共享。
- **複習**：任務清單章節

### Q8
- **類別**：實作
- **題目**：如何在規劃模式中從外部編輯器編輯計畫？
- **選項**：A) 從終端機複製貼上 | B) 按 `Ctrl+G` 在外部編輯器中開啟計畫 | C) 使用 `/export-plan` 指令 | D) 計畫無法從外部編輯
- **正確答案**：B
- **解說**：Ctrl+G 在您設定的外部編輯器中開啟目前的計畫以進行修改。
- **複習**：規劃模式章節

### Q9
- **類別**：概念
- **題目**：`dontAsk` 和 `bypassPermissions` 模式有什麼區別？
- **選項**：A) 相同 | B) `dontAsk` 除非預先核准否則自動拒絕；`bypassPermissions` 完全跳過所有檢查 | C) `dontAsk` 用於檔案；`bypassPermissions` 用於指令 | D) `bypassPermissions` 更安全
- **正確答案**：B
- **解說**：dontAsk 除非匹配預先核准的模式否則自動拒絕權限請求。bypassPermissions 完全跳過所有安全檢查 — 不適合常規使用。
- **複習**：權限模式章節

### Q10
- **類別**：實作
- **題目**：如何將 CLI 工作階段移交給桌面應用程式？
- **選項**：A) 使用 `/export` 指令 | B) 使用 `/desktop` 指令 | C) 複製工作階段 ID 並貼到應用程式中 | D) 工作階段無法在 CLI 和桌面間轉移
- **正確答案**：B
- **解說**：`/desktop` 指令將目前的 CLI 工作階段移交給原生桌面應用程式，進行視覺化差異審查和多工作階段管理。
- **複習**：桌面應用程式章節

---

## 第 10 課：CLI Reference

### Q1
- **類別**：概念
- **題目**：Claude CLI 的兩種主要模式是什麼？
- **選項**：A) 線上和離線模式 | B) 互動式 REPL（`claude`）和 Print mode（`claude -p`） | C) GUI 和終端機模式 | D) 單一和批次模式
- **正確答案**：B
- **解說**：互動式 REPL 是預設的對話模式。Print mode（-p）是非互動式、可腳本化、可管道的 — 回應後即退出。
- **複習**：CLI 架構章節

### Q2
- **類別**：實作
- **題目**：如何將檔案透過管道傳入 Claude 並取得 JSON 輸出？
- **選項**：A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **正確答案**：B
- **解說**：透過 stdin 將內容管道傳入 print mode（-p），並使用 --output-format json 取得結構化輸出。
- **複習**：互動式 vs Print Mode 章節

### Q3
- **類別**：概念
- **題目**：`-c` 和 `-r` 旗標有什麼區別？
- **選項**：A) 兩者相同 | B) `-c` 繼續最近的工作階段；`-r` 按名稱或 ID 恢復 | C) `-c` 建立新工作階段；`-r` 恢復 | D) `-c` 用於程式碼；`-r` 用於審查
- **正確答案**：B
- **解說**：`-c/--continue` 恢復最近的對話。`-r/--resume "name"` 按名稱或工作階段 ID 恢復特定工作階段。
- **複習**：工作階段管理章節

### Q4
- **類別**：實作
- **題目**：如何保證 Claude 輸出符合 schema 的 JSON？
- **選項**：A) 只用 `--output-format json` | B) 使用 `--output-format json --json-schema '{"type":"object",...}'` | C) 使用 `--strict-json` 旗標 | D) JSON 輸出總是符合 schema
- **正確答案**：B
- **解說**：單獨使用 `--output-format json` 產生盡力而為的 JSON。加上 `--json-schema` 搭配 JSON Schema 定義可保證輸出匹配 schema。
- **複習**：輸出與格式章節

### Q5
- **類別**：概念
- **題目**：哪個旗標僅在 print mode（-p）中有效，在互動模式中無效？
- **選項**：A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **正確答案**：B
- **解說**：`--system-prompt-file` 從檔案載入系統提示，但僅在 print mode 中有效。互動式工作階段使用 `--system-prompt`（內嵌字串）。
- **複習**：系統提示旗標比較表

### Q6
- **類別**：實作
- **題目**：如何限制 Claude 僅使用唯讀工具進行安全稽核？
- **選項**：A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **正確答案**：B
- **解說**：結合 `--permission-mode plan`（唯讀分析）與 `--tools`（特定工具白名單）來限制 Claude 僅執行讀取操作。
- **複習**：工具與權限管理章節

### Q7
- **類別**：概念
- **題目**：代理定義的優先順序是什麼？
- **選項**：A) 專案 > 使用者 > CLI | B) CLI > 使用者 > 專案 | C) 使用者 > CLI > 專案 | D) 全部相同優先級
- **正確答案**：B
- **解說**：CLI 定義的代理（--agents 旗標）具有最高優先級，其次是使用者層級（~/.claude/agents/），然後是專案層級（.claude/agents/）。
- **複習**：代理設定章節

### Q8
- **類別**：實作
- **題目**：如何分叉現有工作階段以嘗試不同方法而不遺失原始內容？
- **選項**：A) 使用 `/fork` 指令 | B) 使用 `--resume session-name --fork-session "branch name"` | C) 使用 `--clone session-name` | D) 使用 `/branch session-name`
- **正確答案**：B
- **解說**：`--resume` 搭配 `--fork-session` 從恢復的工作階段建立新的獨立分支，保留原始對話。
- **複習**：工作階段管理章節

### Q9
- **類別**：概念
- **題目**：使用者已登入時，`claude auth status` 回傳什麼 exit code？
- **選項**：A) 1 | B) 0 | C) 200 | D) 不回傳 exit code
- **正確答案**：B
- **解說**：`claude auth status` 已登入時回傳 exit code 0，未登入時回傳 1。這使其可用於 CI/CD 認證檢查的腳本。
- **複習**：CLI 指令表

### Q10
- **類別**：實作
- **題目**：如何使用 Claude 批次處理多個檔案？
- **選項**：A) `claude --batch *.md` | B) 使用 for 迴圈：`for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) 不支援批次處理
- **正確答案**：B
- **解說**：使用 shell for 迴圈搭配 print mode 逐一處理檔案。每次調用獨立且可產生結構化輸出。
- **複習**：批次處理章節
