<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# 進階功能

🚀 Advanced Features（進階功能）
用途: Planning Mode、Extended Thinking、Background Tasks
難度: ⭐⭐⭐⭐ 進階 | 時間: 2-3 小時

Claude Code 進階能力的完整指南，包括規劃模式、延伸思考、自動模式、背景任務、權限模式、列印模式（非互動）、工作階段管理、互動功能、頻道、語音輸入、遠端控制、Web 工作階段、桌面應用程式、任務清單、提示建議、git worktree、沙盒、託管設定和配置。

## 目錄

1. [概覽](#概覽)
2. [規劃模式](#規劃模式)
3. [延伸思考](#延伸思考)
4. [自動模式](#自動模式)
5. [背景任務](#背景任務)
6. [排程任務](#排程任務)
7. [權限模式](#權限模式)
8. [Headless 模式](#headless-模式)
9. [工作階段管理](#工作階段管理)
10. [互動功能](#互動功能)
11. [語音輸入](#語音輸入)
12. [頻道](#頻道)
13. [Chrome 整合](#chrome-整合)
14. [遠端控制](#遠端控制)
15. [Web 工作階段](#web-工作階段)
16. [桌面應用程式](#桌面應用程式)
17. [任務清單](#任務清單)
18. [提示建議](#提示建議)
19. [Git Worktree](#git-worktree)
20. [沙盒](#沙盒)
21. [託管設定（企業版）](#託管設定企業版)
22. [配置與設定](#配置與設定)
23. [最佳實務](#最佳實務)
24. [相關概念](#相關概念)

---

## 概覽

Claude Code 的進階功能擴展了核心能力，提供規劃、推理、自動化和控制機制。這些功能支援複雜開發任務、程式碼審查、自動化和多工作階段管理的精密工作流程。

**主要進階功能包括：**
- **規劃模式**：在編碼之前建立詳細的實作計畫
- **延伸思考**：針對複雜問題的深度推理
- **自動模式**：背景安全分類器在執行前審查每個操作（研究預覽）
- **背景任務**：執行長時間操作而不阻塞對話
- **權限模式**：控制 Claude 可以做什麼（`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`）
- **列印模式**：以非互動方式執行 Claude Code，用於自動化和 CI/CD（`claude -p`）
- **工作階段管理**：管理多個工作階段
- **互動功能**：鍵盤快捷鍵、多行輸入和指令歷史
- **語音輸入**：按住說話的語音輸入，支援 20 種語言的語音轉文字
- **頻道**：MCP 伺服器將訊息推送到執行中的工作階段（研究預覽）
- **遠端控制**：從 Claude.ai 或 Claude 應用程式控制 Claude Code
- **Web 工作階段**：在瀏覽器中於 claude.ai/code 執行 Claude Code
- **桌面應用程式**：用於視覺化差異審查和多工作階段的獨立應用程式
- **任務清單**：跨上下文壓縮的持久任務追蹤
- **提示建議**：基於上下文的智慧指令建議
- **Git Worktree**：用於並行工作的隔離 worktree 分支
- **沙盒**：作業系統層級的檔案系統和網路隔離
- **託管設定**：透過 plist、Registry 或託管檔案進行企業部署
- **配置**：使用 JSON 配置檔案自訂行為

---

## 規劃模式

規劃模式允許 Claude 在實作之前仔細思考複雜任務，建立詳細的計畫供您審查和核准。

### 什麼是規劃模式？

規劃模式是一個兩階段方法：
1. **規劃階段**：Claude 分析任務並建立詳細的實作計畫
2. **實作階段**：核准後，Claude 執行計畫

### 何時使用規劃模式

✅ 適合使用規劃模式的情境：
- 複雜的多檔案重構
- 新功能實作
- 架構變更
- 資料庫遷移
- 大型 API 重新設計

❌ 不適合使用規劃模式的情境：
- 簡單的錯誤修復
- 格式化變更
- 單一檔案編輯
- 快速查詢

### 啟動規劃模式

**斜線指令**：
```bash
/plan Implement user authentication system
```

**CLI 旗標**：
```bash
claude --permission-mode plan
```

**設為預設**：
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**鍵盤快捷鍵**：
- `Shift + Tab` - 切換權限模式（包括 plan）
- `Alt + M` - 切換權限模式（Windows/Linux）

### 規劃模式的優點

- **結構化的實作方法**：詳細的實作步驟分解
- **審查與核准**：在執行前核准或調整計畫
- **風險識別**：在實作前識別潛在問題
- **清晰的階段**：有組織的實作階段和里程碑

### 範例：功能實作

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## 實作計畫

### 階段 1：基礎設施設定
1. 安裝 WebSocket 函式庫（socket.io）
2. 設定 WebSocket 伺服器
3. 配置連線管理

### 階段 2：後端實作
4. 建立通知服務
5. 實作通知佇列
6. 新增通知資料庫結構
7. 建立 API 端點

### 階段 3：前端整合
8. 設定 WebSocket 客戶端
9. 建立通知 UI 元件
10. 實作通知狀態管理
11. 新增通知權限

### 階段 4：測試與部署
12. 撰寫單元測試
13. 撰寫整合測試
14. 更新文件
15. 部署到 staging

預估時間：3-4 小時
要修改的檔案：12
要建立的新檔案：8

準備好繼續了嗎？（yes/no/modify plan）

User: yes

Claude: [開始按照計畫實作]
```

### 計畫修改

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[顯示移除佇列後的修改計畫]

User: Looks good, proceed

Claude: [實作修改後的計畫]
```

### 規劃模式配置

規劃模式透過 CLI 旗標或斜線指令啟動：

```bash
# 透過 CLI 啟動規劃模式
claude --permission-mode plan

# 或在 REPL 中使用 /plan 斜線指令
/plan Implement user authentication system
```

**規劃用的模型別名**：使用 `opusplan` 作為模型別名，以 Opus 進行規劃、Sonnet 進行執行：

```bash
claude --model opusplan "design and implement the new API"
```

**在外部編輯器中編輯計畫**：按 `Ctrl+G` 在外部編輯器中開啟當前計畫進行詳細修改。

---

## 延伸思考

延伸思考允許 Claude 在提供解決方案之前花更多時間推理複雜問題。

### 什麼是延伸思考？

延伸思考是一個深思熟慮的逐步推理過程，Claude 會：
- 分解複雜問題
- 考慮多種方法
- 評估取捨
- 推理邊界情況

### 啟動延伸思考

**鍵盤快捷鍵**：
- `Option + T`（macOS）/ `Alt + T`（Windows/Linux）- 切換延伸思考

**自動啟動**：
- 所有模型預設啟用（Opus 4.6、Sonnet 4.6、Haiku 4.5）
- Opus 4.6：自適應推理，努力等級：`low`（○）、`medium`（◐）、`high`（●）、`max`（僅限 Opus 4.6）
- 其他模型：最高 31,999 個 token 的固定預算

**配置方式**：
- 切換：`Alt+T` / `Option+T`，或透過 `/config`
- 查看推理：`Ctrl+O`（詳細模式）
- 設定努力等級：`/effort` 指令或 `--effort` 旗標

**自訂預算**：
```bash
export MAX_THINKING_TOKENS=1024
```

**努力等級**（僅限 Opus 4.6）：
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○)、medium (◐)、high (●) 或 max（僅限 Opus 4.6）
```

**CLI 旗標**：
```bash
claude --effort high "complex architectural review"
```

**斜線指令**：
```
/effort high
```

> **注意：**在提示中使用關鍵字「ultrathink」可啟動深度推理模式。努力等級 `low`、`medium`、`high` 和 `max`（僅限 Opus 4.6）控制 Claude 執行多少推理。

### 延伸思考的優點

- **深度推理**：花更多時間思考複雜問題
- **更好的架構決策**：透過全面評估做出明智的選擇
- **邊界情況的考慮**：思考潛在的問題和情境
- **全面的分析**：對複雜問題解決的結構化方法

### 範例：架構決策

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## 上下文分析
- 團隊規模：5 位開發者
- 預期流量：初始每日 10k 使用者
- 需要擴展到 100k+ 使用者
- 有限的 DevOps 資源
- 6 個月的 MVP 時程

## 方法 1：微服務
優點：
+ 獨立擴展
+ 技術靈活性
+ 團隊獨立性
+ 故障隔離

缺點：
- 運維複雜性
- 網路開銷
- 需要分散式追蹤
- 需要 DevOps 專業知識
- 初始開發較慢

## 方法 2：單體式
優點：
+ 更簡單的部署
+ 更快的初始開發
+ 更容易除錯
+ 更低的運維開銷
+ 單一程式碼庫

缺點：
- 後期擴展挑戰
- 全有或全無的部署
- 技術鎖定
- 可能緊密耦合

## 決策因素
1. 團隊規模（5 位開發者）→ 偏向單體式
2. DevOps 資源（有限）→ 偏向單體式
3. 時程（6 個月）→ 偏向單體式
4. 未來擴展（100k 使用者）→ 單體式 + 快取可達成
5. 複雜度預算 → 有限

## 建議
從**模組化單體式**開始：
- 單一部署單元
- 清晰的模組邊界
- 模組間的乾淨介面
- 為未來需要時提取為微服務做準備

這為您提供：
✓ 快速初始開發
✓ 低運維複雜性
✓ 後續提取服務的選項
✓ 清晰的架構

遷移路線：當您達到 50k+ 使用者或特定模組需要獨立擴展時，將這些模組提取為微服務。
</extended_thinking>

**建議**：實作具有清晰模組邊界的模組化單體式。

這種方法平衡了您當前的限制（團隊規模、時程、DevOps 資源）與未來的可擴展性需求。您可以在有明確的業務需求時，將特定模組遷移為微服務。
```

### 延伸思考配置

延伸思考透過環境變數、鍵盤快捷鍵和 CLI 旗標控制：

```bash
# 設定思考 token 預算
export MAX_THINKING_TOKENS=16000

# 設定努力等級（僅限 Opus 4.6）：low (○)、medium (◐)、high (●) 或 max（僅限 Opus 4.6）
export CLAUDE_CODE_EFFORT_LEVEL=high
```

在工作階段中使用 `Alt+T` / `Option+T` 切換，使用 `/effort` 設定努力等級，或透過 `/config` 配置。

---

## 自動模式

自動模式是一個研究預覽權限模式（2026 年 3 月），使用背景安全分類器在執行前審查每個操作。它允許 Claude 自主工作，同時阻擋危險操作。

### 需求

- **方案**：Team 方案（Enterprise 和 API 正在推出中）
- **模型**：Claude Sonnet 4.6 或 Opus 4.6
- **分類器**：在 Claude Sonnet 4.6 上執行（增加額外的 token 成本）

### 啟用自動模式

```bash
# 使用 CLI 旗標解鎖自動模式
claude --enable-auto-mode

# 然後在 REPL 中使用 Shift+Tab 切換到該模式
```

或將其設為預設權限模式：

```bash
claude --permission-mode auto
```

透過配置設定：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 分類器運作方式

背景分類器使用以下決策順序評估每個操作：

1. **允許/拒絕規則** -- 首先檢查明確的權限規則
2. **唯讀/編輯自動核准** -- 檔案讀取和編輯自動通過
3. **分類器** -- 背景分類器審查操作
4. **備用方案** -- 在連續 3 次或總共 20 次阻擋後回退到提示

### 預設阻擋的操作

自動模式預設阻擋以下操作：

| 阻擋的操作 | 範例 |
|----------------|---------|
| 管道到 shell 的安裝 | `curl \| bash` |
| 對外傳送敏感資料 | API 金鑰、透過網路傳送的憑證 |
| 生產環境部署 | 針對生產環境的部署指令 |
| 大量刪除 | 對大型目錄執行 `rm -rf` |
| IAM 變更 | 權限和角色修改 |
| 強制推送到 main | `git push --force origin main` |

### 預設允許的操作

| 允許的操作 | 範例 |
|----------------|---------|
| 本機檔案操作 | 讀取、寫入、編輯專案檔案 |
| 宣告的依賴安裝 | 從 manifest 執行 `npm install`、`pip install` |
| 唯讀 HTTP | `curl` 取得文件 |
| 推送到當前分支 | `git push origin feature-branch` |

### 配置自動模式

**以 JSON 列印預設規則**：
```bash
claude auto-mode defaults
```

**配置受信任的基礎設施**透過 `autoMode.environment` 託管設定進行企業部署。這允許管理員定義受信任的 CI/CD 環境、部署目標和基礎設施模式。

### 備用行為

當分類器不確定時，自動模式會回退到提示使用者：
- 在**連續 3 次**分類器阻擋後
- 在一個工作階段中**總共 20 次**分類器阻擋後

這確保當分類器無法自信地核准操作時，使用者始終保持控制權。

---

## 背景任務

背景任務允許長時間執行的操作在不阻塞您對話的情況下執行。

### 什麼是背景任務？

背景任務在您繼續工作時非同步執行：
- 長時間的測試套件
- 建構流程
- 資料庫遷移
- 部署腳本
- 分析工具

**基本用法：**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # 顯示所有任務
/task status bg-1234 # 檢查進度
/task show bg-1234   # 查看輸出
/task cancel bg-1234 # 取消任務
```

### 啟動背景任務

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[您可以繼續對話]

User: Meanwhile, let's refactor the auth module

Claude: [在測試於背景執行時處理 auth 模組]

[稍後，當測試完成時]

Claude: 📢 背景任務 bg-1234 完成：
✅ 245 個測試通過
❌ 3 個測試失敗
查看結果：/task show bg-1234
```

### 管理背景任務

**列出活動任務**：
```
User: /task list

活動中的背景任務：
1. [bg-1234] 執行測試（完成 50%，剩餘 2 分鐘）
2. [bg-1235] 建構 Docker 映像（完成 25%，剩餘 8 分鐘）
3. [bg-1236] 部署到 staging（完成 90%，剩餘 30 秒）
```

**檢查任務狀態**：
```
User: /task status bg-1234

任務 bg-1234：執行測試
狀態：進行中
進度：120/245 個測試（49%）
開始時間：2025-11-08 10:30:15
預計完成時間：2025-11-08 10:34:22
```

**查看任務輸出**：
```
User: /task show bg-1234

[顯示測試執行的即時輸出]
```

**取消任務**：
```
User: /task cancel bg-1234

已取消背景任務 bg-1234
```

### 範例：並行開發

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [在建構和程式碼檢查器執行的同時實作 API 端點]

[10 分鐘後]

Claude: 📢 建構成功完成（bg-5001）
📢 程式碼檢查器發現 12 個問題（bg-5002）

User: Show me the linter issues

Claude: [顯示 bg-5002 的程式碼檢查器輸出]
```

### 配置

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## 排程任務

排程任務讓您可以按照重複排程或作為一次性提醒自動執行提示。任務的範圍限於工作階段 — 在 Claude Code 活躍時執行，工作階段結束時清除。自 v2.1.72+ 起可用。

### `/loop` 指令

```bash
# 明確指定間隔
/loop 5m check if the deployment finished

# 自然語言
/loop check build status every 30 minutes
```

也支援標準的 5 欄位 cron 表達式，以進行精確排程。

### 一次性提醒

設定只觸發一次的特定時間提醒：

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### 管理排程任務

| 工具 | 說明 |
|------|-------------|
| `CronCreate` | 建立新的排程任務 |
| `CronList` | 列出所有活動的排程任務 |
| `CronDelete` | 移除排程任務 |

**限制和行為**：
- 每個工作階段最多 **50 個排程任務**
- 範圍限於工作階段 — 工作階段結束時清除
- 重複任務在 **3 天**後自動過期
- 任務僅在 Claude Code 執行時觸發 — 錯過的觸發不會補執行

### 行為細節

| 方面 | 細節 |
|--------|--------|
| **重複任務抖動** | 最多為間隔的 10%（最長 15 分鐘） |
| **一次性抖動** | 在 :00/:30 邊界最多 90 秒 |
| **錯過的觸發** | 不會補執行 — 如果 Claude Code 未在執行中則跳過 |
| **持久性** | 不會在重新啟動間保存 |

### 雲端排程任務

使用 `/schedule` 建立在 Anthropic 基礎設施上執行的雲端排程任務：

```
/schedule daily at 9am run the test suite and report failures
```

雲端排程任務在重新啟動間持久保存，不需要 Claude Code 在本機執行。

### 停用排程任務

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### 範例：監控部署

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **提示**：排程任務的範圍限於工作階段。如需在重新啟動後仍持續的自動化，請改用 CI/CD 管道、GitHub Actions 或桌面應用程式排程任務。

---

## 權限模式

權限模式控制 Claude 在沒有明確核准的情況下可以採取哪些操作。

### 可用的權限模式

| 模式 | 行為 |
|---|---|
| `default` | 僅讀取檔案；所有其他操作需要提示 |
| `acceptEdits` | 讀取和編輯檔案；指令需要提示 |
| `plan` | 僅讀取檔案（研究模式，不進行編輯） |
| `auto` | 所有操作都經過背景安全分類器檢查（研究預覽） |
| `bypassPermissions` | 所有操作，不進行權限檢查（危險） |
| `dontAsk` | 僅執行預先核准的工具；其他所有工具被拒絕 |

在 CLI 中使用 `Shift+Tab` 循環切換模式。使用 `--permission-mode` 旗標或 `permissions.defaultMode` 設定來設定預設值。

### 啟動方式

**鍵盤快捷鍵**：
```bash
Shift + Tab  # 在所有 6 種模式間循環
```

**斜線指令**：
```bash
/plan                  # 進入規劃模式
```

**CLI 旗標**：
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**設定**：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 權限模式範例

#### 預設模式
Claude 在重要操作前要求確認：

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### 規劃模式
在執行前審查實作計畫：

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## 實作計畫
[包含階段和步驟的詳細計畫]

Ready to proceed? (yes/no/modify)
```

#### 接受編輯模式
自動接受檔案修改：

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [不經詢問直接進行變更]
```

### 使用案例

**程式碼審查**：
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [讀取程式碼，提供回饋，但無法修改]
```

**配對程式設計**：
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [在每次變更前要求核准]
```

**自動化任務**：
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [不經詢問自動接受檔案編輯]
```

---

## Headless 模式

列印模式（`claude -p`）允許 Claude Code 在沒有互動輸入的情況下執行，非常適合自動化和 CI/CD。這是非互動模式，取代了舊的 `--headless` 旗標。

### 什麼是列印模式？

列印模式支援：
- 自動化腳本執行
- CI/CD 整合
- 批次處理
- 排程任務

### 以列印模式執行（非互動）

```bash
# 執行特定任務
claude -p "Run all tests"

# 處理管道內容
cat error.log | claude -p "Analyze these errors"

# CI/CD 整合（GitHub Actions）
- name: AI Code Review
  run: claude -p "Review PR"
```

### 更多列印模式使用範例

```bash
# 執行特定任務並擷取輸出
claude -p "Run all tests and generate coverage report"

# 結構化輸出
claude -p --output-format json "Analyze code quality"

# 從 stdin 輸入
echo "Analyze code quality" | claude -p "explain this"
```

### 範例：CI/CD 整合

**GitHub Actions**：
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### 列印模式配置

列印模式（`claude -p`）支援多個用於自動化的旗標：

```bash
# 限制自主回合數
claude -p --max-turns 5 "refactor this module"

# 結構化 JSON 輸出
claude -p --output-format json "analyze this codebase"

# 附 schema 驗證
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# 停用工作階段持久化
claude -p --no-session-persistence "one-off analysis"
```

---

## 工作階段管理

有效管理多個 Claude Code 工作階段。

### 工作階段管理指令

| 指令 | 說明 |
|---------|-------------|
| `/resume` | 按 ID 或名稱恢復對話 |
| `/rename` | 命名當前工作階段 |
| `/fork` | 將當前工作階段分叉為新分支 |
| `claude -c` | 繼續最近的對話 |
| `claude -r "session"` | 按名稱或 ID 恢復工作階段 |

### 恢復工作階段

**繼續上次對話**：
```bash
claude -c
```

**恢復已命名的工作階段**：
```bash
claude -r "auth-refactor" "finish this PR"
```

**重新命名當前工作階段**（在 REPL 中）：
```
/rename auth-refactor
```

### 分叉工作階段

分叉工作階段以嘗試替代方法而不失去原始工作：

```
/fork
```

或從 CLI：
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### 工作階段持久化

工作階段會自動儲存，可以恢復：

```bash
# 繼續上次對話
claude -c

# 按名稱或 ID 恢復特定工作階段
claude -r "auth-refactor"

# 恢復並分叉以進行實驗
claude --resume auth-refactor --fork-session "alternative approach"
```

---

## 互動功能

### 鍵盤快捷鍵

Claude Code 支援鍵盤快捷鍵以提高效率。以下是來自官方文件的完整參考：

| 快捷鍵 | 說明 |
|----------|-------------|
| `Ctrl+C` | 取消當前輸入/生成 |
| `Ctrl+D` | 退出 Claude Code |
| `Ctrl+G` | 在外部編輯器中編輯計畫 |
| `Ctrl+L` | 清除終端螢幕 |
| `Ctrl+O` | 切換詳細輸出（查看推理） |
| `Ctrl+R` | 反向搜尋歷史 |
| `Ctrl+T` | 切換任務清單視圖 |
| `Ctrl+B` | 背景執行任務 |
| `Esc+Esc` | 倒轉程式碼/對話 |
| `Shift+Tab` / `Alt+M` | 切換權限模式 |
| `Option+P` / `Alt+P` | 切換模型 |
| `Option+T` / `Alt+T` | 切換延伸思考 |

**行編輯（標準 readline 快捷鍵）：**

| 快捷鍵 | 動作 |
|----------|--------|
| `Ctrl + A` | 移至行首 |
| `Ctrl + E` | 移至行尾 |
| `Ctrl + K` | 剪下至行尾 |
| `Ctrl + U` | 剪下至行首 |
| `Ctrl + W` | 向後刪除字詞 |
| `Ctrl + Y` | 貼上（yank） |
| `Tab` | 自動完成 |
| `↑ / ↓` | 指令歷史 |

### 自訂按鍵繫結

執行 `/keybindings` 來建立自訂鍵盤快捷鍵，這會開啟 `~/.claude/keybindings.json` 進行編輯（v2.1.18+）。

**配置格式**：

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

將繫結設為 `null` 以取消預設快捷鍵的繫結。

### 可用的上下文

按鍵繫結的範圍限於特定的 UI 上下文：

| 上下文 | 關鍵動作 |
|---------|-------------|
| **Chat** | `submit`、`cancel`、`cycleMode`、`modelPicker`、`thinkingToggle`、`undo`、`externalEditor`、`stash`、`imagePaste` |
| **Confirmation** | `yes`、`no`、`previous`、`next`、`nextField`、`cycleMode`、`toggleExplanation` |
| **Global** | `interrupt`、`exit`、`toggleTodos`、`toggleTranscript` |
| **Autocomplete** | `accept`、`dismiss`、`next`、`previous` |
| **HistorySearch** | `search`、`previous`、`next` |
| **Settings** | 上下文專屬的設定導覽 |
| **Tabs** | 標籤切換和管理 |
| **Help** | 幫助面板導覽 |

總共有 18 個上下文，包括 `Transcript`、`Task`、`ThemePicker`、`Attachments`、`Footer`、`MessageSelector`、`DiffDialog`、`ModelPicker` 和 `Select`。

### 和弦支援

按鍵繫結支援和弦序列（多鍵組合）：

```
"ctrl+k ctrl+s"   → 兩鍵序列：按 ctrl+k，然後 ctrl+s
"ctrl+shift+p"    → 同時按修飾鍵
```

**按鍵語法**：
- **修飾鍵**：`ctrl`、`alt`（或 `opt`）、`shift`、`meta`（或 `cmd`）
- **大寫暗示 Shift**：`K` 等同於 `shift+k`
- **特殊鍵**：`escape`、`enter`、`return`、`tab`、`space`、`backspace`、`delete`、方向鍵

### 保留和衝突的按鍵

| 按鍵 | 狀態 | 備註 |
|-----|--------|-------|
| `Ctrl+C` | 保留 | 無法重新繫結（中斷） |
| `Ctrl+D` | 保留 | 無法重新繫結（退出） |
| `Ctrl+B` | 終端衝突 | tmux 前綴鍵 |
| `Ctrl+A` | 終端衝突 | GNU Screen 前綴鍵 |
| `Ctrl+Z` | 終端衝突 | 程序暫停 |

> **提示**：如果快捷鍵無法運作，請檢查是否與您的終端模擬器或多工器衝突。

### Tab 完成

Claude Code 提供智慧型 Tab 完成：

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### 指令歷史

存取先前的指令：

```
User: <↑>  # 上一個指令
User: <↓>  # 下一個指令
User: Ctrl+R  # 搜尋歷史

(reverse-i-search)`test': run all tests
```

### 多行輸入

對於複雜的查詢，使用多行模式：

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**範例：**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [處理多行請求]
```

### 行內編輯

在傳送前編輯指令：

```
User: Deploy to prodcution<Backspace><Backspace>uction

[在傳送前就地編輯]
```

### Vim 模式

啟用 Vi/Vim 按鍵繫結進行文字編輯：

**啟用方式**：
- 使用 `/vim` 指令或 `/config` 來啟用
- 使用 `Esc` 切換到 NORMAL 模式，`i/a/o` 切換到 INSERT 模式

**導覽鍵**：
- `h` / `l` - 左/右移動
- `j` / `k` - 下/上移動
- `w` / `b` / `e` - 按字詞移動
- `0` / `$` - 移至行首/行尾
- `gg` / `G` - 跳到文字開頭/結尾

**文字物件**：
- `iw` / `aw` - 字詞內部/周圍
- `i"` / `a"` - 引號字串內部/周圍
- `i(` / `a(` - 括號內部/周圍

### Bash 模式

使用 `!` 前綴直接執行 shell 指令：

```bash
! npm test
! git status
! cat src/index.js
```

使用此功能可以快速執行指令而不需切換上下文。

---

## 語音輸入

語音輸入為 Claude Code 提供按住說話的語音輸入功能，讓您可以用說的方式輸入提示而不是打字。

### 啟動語音輸入

```
/voice
```

### 功能

| 功能 | 說明 |
|---------|-------------|
| **按住說話** | 按住鍵錄音，放開後傳送 |
| **20 種語言** | 語音轉文字支援 20 種語言 |
| **自訂按鍵繫結** | 透過 `/keybindings` 配置按住說話鍵 |
| **帳號需求** | 需要 Claude.ai 帳號進行語音轉文字處理 |

### 配置

在按鍵繫結檔案（`/keybindings`）中自訂按住說話的按鍵繫結。語音輸入使用您的 Claude.ai 帳號進行語音轉文字處理。

---

## 頻道

頻道（研究預覽）允許 MCP 伺服器將訊息推送到執行中的 Claude Code 工作階段，實現與外部服務的即時整合。

### 訂閱頻道

```bash
# 在啟動時訂閱頻道外掛
claude --channels discord,telegram
```

### 支援的整合

| 整合 | 說明 |
|-------------|-------------|
| **Discord** | 在工作階段中接收和回應 Discord 訊息 |
| **Telegram** | 在工作階段中接收和回應 Telegram 訊息 |

### 配置

**企業部署的託管設定**：

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

`allowedChannelPlugins` 託管設定控制整個組織中允許使用的頻道外掛。

### 運作方式

1. MCP 伺服器作為頻道外掛連接到外部服務
2. 傳入的訊息被推送到活躍的 Claude Code 工作階段
3. Claude 可以在工作階段上下文中閱讀和回應訊息
4. 頻道外掛必須透過 `allowedChannelPlugins` 託管設定獲得核准

---

## Chrome 整合

Chrome 整合將 Claude Code 連接到您的 Chrome 或 Microsoft Edge 瀏覽器，用於即時的 Web 自動化和除錯。這是自 v2.0.73+ 起可用的 beta 功能（Edge 支援在 v1.0.36+ 中新增）。

### 啟用 Chrome 整合

**在啟動時**：

```bash
claude --chrome      # 啟用 Chrome 連線
claude --no-chrome   # 停用 Chrome 連線
```

**在工作階段中**：

```
/chrome
```

選擇「預設啟用」以在所有未來的工作階段中啟動 Chrome 整合。Claude Code 共享您瀏覽器的登入狀態，因此可以與已驗證的 Web 應用程式互動。

### 能力

| 能力 | 說明 |
|------------|-------------|
| **即時除錯** | 讀取主控台日誌、檢查 DOM 元素、即時除錯 JavaScript |
| **設計驗證** | 將渲染的頁面與設計稿進行比對 |
| **表單驗證** | 測試表單提交、輸入驗證和錯誤處理 |
| **Web 應用程式測試** | 與已驗證的應用程式互動（Gmail、Google Docs、Notion 等） |
| **資料擷取** | 從網頁抓取和處理內容 |
| **工作階段錄製** | 將瀏覽器互動錄製為 GIF 檔案 |

### 網站層級權限

Chrome 擴充功能管理每個網站的存取權限。隨時透過擴充功能彈出視窗授予或撤銷特定網站的存取權限。Claude Code 只與您明確允許的網站互動。

### 運作方式

Claude Code 在可見的視窗中控制瀏覽器 — 您可以即時觀看操作發生。當瀏覽器遇到登入頁面或 CAPTCHA 時，Claude 會暫停並等待您手動處理後再繼續。

### 已知限制

- **瀏覽器支援**：僅限 Chrome 和 Edge — 不支援 Brave、Arc 和其他 Chromium 瀏覽器
- **WSL**：不適用於 Windows Subsystem for Linux
- **第三方提供者**：不支援 Bedrock、Vertex 或 Foundry API 提供者
- **Service Worker 閒置**：Chrome 擴充功能的 service worker 可能在長時間工作階段中進入閒置狀態

> **提示**：Chrome 整合是 beta 功能。瀏覽器支援可能在未來版本中擴展。

---

## 遠端控制

遠端控制讓您可以從手機、平板或任何瀏覽器繼續在本機執行的 Claude Code 工作階段。您的本機工作階段持續在您的機器上執行 — 沒有任何內容移到雲端。適用於 Pro、Max、Team 和 Enterprise 方案（v2.1.51+）。

### 啟動遠端控制

**從 CLI**：

```bash
# 使用預設工作階段名稱啟動
claude remote-control

# 使用自訂名稱啟動
claude remote-control --name "Auth Refactor"
```

**從工作階段中**：

```
/remote-control
/remote-control "Auth Refactor"
```

**可用旗標**：

| 旗標 | 說明 |
|------|-------------|
| `--name "title"` | 自訂工作階段標題以便識別 |
| `--verbose` | 顯示詳細的連線日誌 |
| `--sandbox` | 啟用檔案系統和網路隔離 |
| `--no-sandbox` | 停用沙盒（預設） |

### 連接到工作階段

從另一個裝置連接的三種方式：

1. **工作階段 URL** — 工作階段啟動時印在終端中；在任何瀏覽器中開啟
2. **QR 碼** — 啟動後按 `空白鍵` 顯示可掃描的 QR 碼
3. **按名稱尋找** — 在 claude.ai/code 或 Claude 行動應用程式（iOS/Android）中瀏覽您的工作階段

### 安全性

- **不開啟入站埠** — 您的機器不會開啟任何入站埠
- **僅限出站 HTTPS** — 透過 TLS
- **範圍限定的憑證** — 多個短效、窄範圍的 token
- **工作階段隔離** — 每個遠端工作階段都是獨立的

### 遠端控制 vs Web 上的 Claude Code

| 方面 | 遠端控制 | Web 上的 Claude Code |
|--------|---------------|-------------------|
| **執行** | 在您的機器上執行 | 在 Anthropic 雲端執行 |
| **本機工具** | 完整存取本機 MCP 伺服器、檔案和 CLI | 無本機依賴 |
| **使用案例** | 從另一個裝置繼續本機工作 | 從任何瀏覽器重新開始 |

### 限制

- 每個 Claude Code 實例只能有一個遠端工作階段
- 主機上的終端必須保持開啟
- 如果網路無法連接，工作階段在約 10 分鐘後逾時

### 使用案例

- 在離開桌面時從行動裝置或平板控制 Claude Code
- 使用更豐富的 claude.ai UI 同時維持本機工具執行
- 在外出時使用完整的本機開發環境進行快速程式碼審查

---

## Web 工作階段

Web 工作階段允許您直接在瀏覽器中於 claude.ai/code 執行 Claude Code，或從 CLI 建立 Web 工作階段。

### 建立 Web 工作階段

```bash
# 從 CLI 建立新的 Web 工作階段
claude --remote "implement the new API endpoints"
```

這會在 claude.ai 上啟動一個 Claude Code 工作階段，您可以從任何瀏覽器存取。

### 在本機恢復 Web 工作階段

如果您在 Web 上啟動了工作階段並想在本機繼續：

```bash
# 在本機終端恢復 Web 工作階段
claude --teleport
```

或從互動式 REPL 中：
```
/teleport
```

### 使用案例

- 在一台機器上開始工作，在另一台上繼續
- 與團隊成員分享工作階段 URL
- 使用 Web UI 進行視覺化差異審查，然後切換到終端執行

---

## 桌面應用程式

Claude Code 桌面應用程式提供獨立的應用程式，具備視覺化差異審查、並行工作階段和整合的連接器。適用於 macOS 和 Windows（Pro、Max、Team 和 Enterprise 方案）。

### 安裝

從 [claude.ai](https://claude.ai) 下載您平台的版本：
- **macOS**：通用建構（Apple Silicon 和 Intel）
- **Windows**：提供 x64 和 ARM64 安裝程式

請參見 [桌面快速入門](https://code.claude.com/docs/en/desktop-quickstart) 以獲取設定說明。

### 從 CLI 移交

將您當前的 CLI 工作階段轉移到桌面應用程式：

```
/desktop
```

### 核心功能

| 功能 | 說明 |
|---------|-------------|
| **差異視圖** | 逐檔案的視覺化審查，附行內註解；Claude 讀取註解並修改 |
| **應用程式預覽** | 自動啟動開發伺服器，附嵌入式瀏覽器進行即時驗證 |
| **PR 監控** | GitHub CLI 整合，自動修復 CI 失敗並在檢查通過時自動合併 |
| **並行工作階段** | 側邊欄中的多個工作階段，附自動 Git worktree 隔離 |
| **排程任務** | 重複任務（每小時、每天、工作日、每週），在應用程式開啟時執行 |
| **豐富的渲染** | 程式碼、markdown 和圖表渲染，附語法高亮 |

### 應用程式預覽配置

在 `.claude/launch.json` 中配置開發伺服器行為：

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### 連接器

連接外部服務以獲取更豐富的上下文：

| 連接器 | 能力 |
|-----------|------------|
| **GitHub** | PR 監控、issue 追蹤、程式碼審查 |
| **Slack** | 通知、頻道上下文 |
| **Linear** | Issue 追蹤、sprint 管理 |
| **Notion** | 文件、知識庫存取 |
| **Asana** | 任務管理、專案追蹤 |
| **Calendar** | 排程感知、會議上下文 |

> **注意**：連接器不適用於遠端（雲端）工作階段。

### 遠端和 SSH 工作階段

- **遠端工作階段**：在 Anthropic 雲端基礎設施上執行；即使應用程式關閉也能繼續。可從 claude.ai/code 或 Claude 行動應用程式存取
- **SSH 工作階段**：透過 SSH 連接到遠端機器，完整存取遠端檔案系統和工具。必須在遠端機器上安裝 Claude Code

### 桌面版的權限模式

桌面應用程式支援與 CLI 相同的 4 種權限模式：

| 模式 | 行為 |
|------|----------|
| **請求權限**（預設） | 審查並核准每個編輯和指令 |
| **自動接受編輯** | 檔案編輯自動核准；指令需要手動核准 |
| **規劃模式** | 在進行任何變更前審查方法 |
| **繞過權限** | 自動執行（僅限沙盒，管理員控制） |

### 企業功能

- **管理主控台**：為組織控制 Code 標籤存取和權限設定
- **MDM 部署**：在 macOS 上透過 MDM 部署，在 Windows 上透過 MSIX 部署
- **SSO 整合**：要求組織成員使用單一登入
- **託管設定**：集中管理團隊配置和模型可用性

---

## 任務清單

任務清單功能提供持久的任務追蹤，在上下文壓縮（對話歷史被修剪以適應上下文視窗時）後仍然保存。

### 切換任務清單

在工作階段中按 `Ctrl+T` 來切換任務清單視圖的開關。

### 持久任務

任務在上下文壓縮後仍然保存，確保長時間運行的工作項目在對話上下文被修剪時不會遺失。這對於複雜的多步驟實作特別有用。

### 命名任務目錄

使用 `CLAUDE_CODE_TASK_LIST_ID` 環境變數建立跨工作階段共享的命名任務目錄：

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

這允許多個工作階段共享相同的任務清單，對於團隊工作流程或多工作階段專案非常有用。

---

## 提示建議

提示建議根據您的 git 歷史和當前對話上下文顯示灰色的範例指令。

### 運作方式

- 建議以灰色文字顯示在您的輸入提示下方
- 按 `Tab` 接受建議
- 按 `Enter` 接受並立即提交
- 建議具有上下文感知能力，從 git 歷史和對話狀態中提取

### 停用提示建議

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktree

Git Worktree 允許您在隔離的 worktree 中啟動 Claude Code，實現在不同分支上的並行工作，而不需要暫存或切換。

### 在 Worktree 中啟動

```bash
# 在隔離的 worktree 中啟動 Claude Code
claude --worktree
# 或
claude -w
```

### Worktree 位置

Worktree 建立在：
```
<repo>/.claude/worktrees/<name>
```

### Monorepo 的稀疏檢出

使用 `worktree.sparsePaths` 設定在 monorepo 中執行稀疏檢出，減少磁碟使用量和 clone 時間：

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Worktree 工具和 Hooks

| 項目 | 說明 |
|------|-------------|
| `ExitWorktree` | 退出並清理當前 worktree 的工具 |
| `WorktreeCreate` | 建立 worktree 時觸發的 Hook 事件 |
| `WorktreeRemove` | 移除 worktree 時觸發的 Hook 事件 |

### 自動清理

如果 worktree 中沒有進行任何變更，它會在工作階段結束時自動清理。

### 使用案例

- 在保持主分支不變的情況下處理功能分支
- 在隔離環境中執行測試，不影響工作目錄
- 在可丟棄的環境中嘗試實驗性變更
- 在 monorepo 中稀疏檢出特定套件以加快啟動速度

---

## 沙盒

沙盒為 Claude Code 執行的 Bash 指令提供作業系統層級的檔案系統和網路隔離。這是權限規則的補充，提供額外的安全層。

### 啟用沙盒

**斜線指令**：
```
/sandbox
```

**CLI 旗標**：
```bash
claude --sandbox       # 啟用沙盒
claude --no-sandbox    # 停用沙盒
```

### 配置設定

| 設定 | 說明 |
|---------|-------------|
| `sandbox.enabled` | 啟用或停用沙盒 |
| `sandbox.failIfUnavailable` | 如果無法啟動沙盒則失敗 |
| `sandbox.filesystem.allowWrite` | 允許寫入存取的路徑 |
| `sandbox.filesystem.allowRead` | 允許讀取存取的路徑 |
| `sandbox.filesystem.denyRead` | 拒絕讀取存取的路徑 |
| `sandbox.enableWeakerNetworkIsolation` | 在 macOS 上啟用較弱的網路隔離 |

### 範例配置

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### 運作方式

- Bash 指令在具有受限檔案系統存取的沙盒環境中執行
- 網路存取可以被隔離以防止意外的外部連線
- 與權限規則配合使用，實現縱深防禦
- 在 macOS 上，使用 `sandbox.enableWeakerNetworkIsolation` 進行網路限制（macOS 上不提供完整的網路隔離）

### 使用案例

- 安全地執行不受信任或生成的程式碼
- 防止意外修改專案外部的檔案
- 在自動化任務期間限制網路存取

---

## 託管設定（企業版）

託管設定讓企業管理員可以使用平台原生管理工具在整個組織中部署 Claude Code 配置。

### 部署方式

| 平台 | 方式 | 自 |
|----------|--------|-------|
| macOS | 託管 plist 檔案（MDM） | v2.1.51+ |
| Windows | Windows Registry | v2.1.51+ |
| 跨平台 | 託管配置檔案 | v2.1.51+ |
| 跨平台 | 託管 drop-in（`managed-settings.d/` 目錄） | v2.1.83+ |

### 託管 Drop-in

自 v2.1.83 起，管理員可以將多個託管設定檔案部署到 `managed-settings.d/` 目錄。檔案按字母順序合併，允許跨團隊的模組化配置：

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### 可用的託管設定

| 設定 | 說明 |
|---------|-------------|
| `disableBypassPermissionsMode` | 防止使用者啟用繞過權限 |
| `availableModels` | 限制使用者可以選擇的模型 |
| `allowedChannelPlugins` | 控制允許使用的頻道外掛 |
| `autoMode.environment` | 為自動模式配置受信任的基礎設施 |
| 自訂政策 | 組織專屬的權限和工具政策 |

### 範例：macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## 配置與設定

### 配置檔案位置

1. **全域配置**：`~/.claude/config.json`
2. **專案配置**：`./.claude/config.json`
3. **使用者配置**：`~/.config/claude-code/settings.json`

### 完整配置範例

**核心進階功能配置：**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**擴展配置範例：**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### 環境變數

使用環境變數覆蓋配置：

```bash
# 模型選擇
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API 配置
export ANTHROPIC_API_KEY=sk-ant-...

# 思考配置
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# 功能切換
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # 由 --bare 旗標設定

# MCP 配置
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# 任務管理
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent Teams（實驗性）
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true

# 子代理和外掛配置
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=true

# 子程序和串流
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### 配置管理指令

```
User: /config
[開啟互動式配置選單]
```

`/config` 指令提供互動式選單來切換設定，例如：
- 延伸思考開/關
- 詳細輸出
- 權限模式
- 模型選擇

### 專案級配置

在您的專案中建立 `.claude/config.json`：

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## 最佳實務

### 規劃模式
- ✅ 用於複雜的多步驟任務
- ✅ 在核准前審查計畫
- ✅ 需要時修改計畫
- ❌ 不要用於簡單任務

### 延伸思考
- ✅ 用於架構決策
- ✅ 用於複雜問題解決
- ✅ 審查思考過程
- ❌ 不要用於簡單查詢

### 背景任務
- ✅ 用於長時間運行的操作
- ✅ 監控任務進度
- ✅ 優雅地處理任務失敗
- ❌ 不要啟動太多並發任務

### 權限
- ✅ 用 `plan` 進行程式碼審查（唯讀）
- ✅ 用 `default` 進行互動式開發
- ✅ 用 `acceptEdits` 進行自動化工作流程
- ✅ 用 `auto` 進行具有安全防護的自主工作
- ❌ 除非絕對必要，不要使用 `bypassPermissions`

### 工作階段
- ✅ 為不同任務使用不同的工作階段
- ✅ 儲存重要的工作階段狀態
- ✅ 清理舊的工作階段
- ❌ 不要在一個工作階段中混合不相關的工作

---

## 其他資源

有關 Claude Code 和相關功能的更多資訊：

- [官方互動模式文件](https://code.claude.com/docs/en/interactive-mode)
- [官方 Headless 模式文件](https://code.claude.com/docs/en/headless)
- [CLI 參考](https://code.claude.com/docs/en/cli-reference)
- [檢查點指南](../08-checkpoints/) - 工作階段管理和倒轉
- [斜線指令](../01-slash-commands/) - 指令參考
- [記憶體指南](../02-memory/) - 持久化上下文
- [技能指南](../03-skills/) - 自主能力
- [子代理指南](../04-subagents/) - 委派任務執行
- [MCP 指南](../05-mcp/) - 外部資料存取
- [Hooks 指南](../06-hooks/) - 事件驅動自動化
- [外掛套件指南](../07-plugins/) - 整合擴充功能
- [官方排程任務文件](https://code.claude.com/docs/en/scheduled-tasks)
- [官方 Chrome 整合文件](https://code.claude.com/docs/en/chrome)
- [官方遠端控制文件](https://code.claude.com/docs/en/remote-control)
- [官方按鍵繫結文件](https://code.claude.com/docs/en/keybindings)
- [官方桌面應用程式文件](https://code.claude.com/docs/en/desktop)
