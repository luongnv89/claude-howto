# 更新日誌

## v2.2.0 — 2026-03-26

### 文件

- 將所有教學和參考文件與 Claude Code v2.1.84 (f78c094) 同步 @luongnv89
  - 更新 slash commands 至 55+ 內建 + 5 個捆綁 skills，標記 3 個為已棄用
  - 將 hook 事件從 18 個擴展至 25 個，新增 `agent` hook 類型（現為 4 種類型）
  - 新增 Auto Mode、Channels、語音聽寫至進階功能
  - 新增 `effort`、`shell` skill frontmatter 欄位；`initialPrompt`、`disallowedTools` agent 欄位
  - 新增 WebSocket MCP 傳輸、elicitation、2KB 工具上限
  - 新增 plugin LSP 支援、`userConfig`、`${CLAUDE_PLUGIN_DATA}`
  - 更新所有參考文件（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）
- 將 README 改寫為登陸頁風格的結構化指南 (32a0776) @luongnv89

### 錯誤修正

- 新增缺少的 cSpell 單字和 README 區段以符合 CI 規範 (93f9d51) @luongnv89
- 新增 `Sandboxing` 至 cSpell 字典 (b80ce6f) @luongnv89

**完整更新日誌**：https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### 錯誤修正

- 移除導致 CI 連結檢查失敗的無效 marketplace 連結 (3fdf0d6) @luongnv89
- 新增 `sandboxed` 和 `pycache` 至 cSpell 字典 (dc64618) @luongnv89

**完整更新日誌**：https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 功能

- 新增自適應學習路徑，包含自我評估和課程測驗 skills (1ef46cd) @luongnv89
  - `/self-assessment` — 跨 10 個功能領域的互動式能力測驗，附個人化學習路徑
  - `/lesson-quiz [lesson]` — 每課知識測驗，包含 8-10 題目標問題

### 錯誤修正

- 更新失效的 URL、棄用項目和過時的參考 (8fe4520) @luongnv89
- 修正 resources 和 self-assessment skill 中的失效連結 (7a05863) @luongnv89
- 在概念指南中使用波浪號圍欄處理巢狀程式碼區塊 (5f82719) @VikalpP
- 新增缺少的單字至 cSpell 字典 (8df7572) @luongnv89

### 文件

- 第 5 階段品質保證——修正跨文件的一致性、URL 和術語 (00bbe4c) @luongnv89
- 完成第 3-4 階段——新功能覆蓋和參考文件更新 (132de29) @luongnv89
- 在 MCP 上下文膨脹區段新增 MCPorter 執行環境 (ef52705) @luongnv89
- 在 6 份指南中新增缺少的指令、功能和設定 (4bc8f15) @luongnv89
- 根據現有倉庫慣例新增風格指南 (84141d0) @luongnv89
- 在指南比較表中新增自我評估列 (8fe0c96) @luongnv89
- 將 VikalpP 新增至貢獻者列表（PR #7）(d5b4350) @luongnv89
- 在 README 和路線圖中新增 self-assessment 和 lesson-quiz skill 參考 (d5a6106) @luongnv89

### 新貢獻者

- @VikalpP 在 #7 中做出了首次貢獻

**完整更新日誌**：https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 功能

- 將所有文件與 Claude Code 2026 年 2 月功能同步 (487c96d)
  - 更新 10 個教學目錄和 7 份參考文件中的 26 個檔案
  - 新增 **Auto Memory（自動記憶）** 文件——每個專案的持久化學習
  - 新增 **Remote Control（遠端控制）**、**Web Sessions（網頁工作階段）** 和 **Desktop App（桌面應用程式）** 文件
  - 新增 **Agent Teams（代理團隊）** 文件（實驗性多代理協作）
  - 新增 **MCP OAuth 2.0**、**Tool Search** 和 **Claude.ai Connectors** 文件
  - 新增 subagents 的 **Persistent Memory（持久化記憶）** 和 **Worktree Isolation（工作樹隔離）** 文件
  - 新增 **Background Subagents（背景子代理）**、**Task List（任務清單）**、**Prompt Suggestions（提示建議）** 文件
  - 新增 **Sandboxing（沙箱）** 和 **Managed Settings（受管理設定）**（企業版）文件
  - 新增 **HTTP Hooks** 和 7 個新 hook 事件文件
  - 新增 **Plugin Settings**、**LSP Servers** 和 Marketplace 更新文件
  - 新增 **Summarize from Checkpoint（從檢查點摘要）** 回溯選項文件
  - 記錄 17 個新 slash commands（`/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` 等）
  - 記錄新 CLI 旗標（`--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` 等）
  - 記錄 auto memory、effort 層級、agent teams 等的新環境變數

### 設計

- 將 logo 重新設計為羅盤-括號標誌搭配簡約色調 (20779db)

### 錯誤修正 / 更正

- 更新模型名稱：Sonnet 4.5 → **Sonnet 4.6**，Opus 4.5 → **Opus 4.6**
- 修正權限模式名稱：將虛構的「Unrestricted/Confirm/Read-only」替換為實際的 `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`
- 修正 hook 事件：移除虛構的 `PreCommit`/`PostCommit`/`PrePush`，新增真實事件（`SubagentStart`、`WorktreeCreate`、`ConfigChange` 等）
- 修正 CLI 語法：將 `claude-code --headless` 替換為 `claude -p`（列印模式）
- 修正 checkpoint 指令：將虛構的 `/checkpoint save/list/rewind/diff` 替換為實際的 `Esc+Esc` / `/rewind` 介面
- 修正工作階段管理：將虛構的 `/session list/new/switch/save` 替換為真實的 `/resume`/`/rename`/`/fork`
- 修正 plugin manifest 格式：從 `plugin.yaml` 遷移至 `.claude-plugin/plugin.json`
- 修正 MCP 配置路徑：`~/.claude/mcp.json` → `.mcp.json`（專案）/ `~/.claude.json`（使用者）
- 修正文件 URL：`docs.claude.com` → `docs.anthropic.com`；移除虛構的 `plugins.claude.com`
- 移除多個檔案中的虛構配置欄位
- 將所有「最後更新」日期更新至 2026 年 2 月

**完整更新日誌**：https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0

