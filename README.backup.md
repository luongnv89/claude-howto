<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude How To

> 一份視覺化、範例驅動的 Claude Code 指南 — 從基礎概念到進階代理，提供可直接複製貼上的模板，帶來即時價值。

## 為什麼需要這份指南？

本專案以不同的方式補充 [Anthropic 官方文件](https://code.claude.com/docs/en/overview)：

| | 官方文件 | 本指南 |
|--|---------------|------------|
| **格式** | 參考文件 | 附圖表的視覺化教學 |
| **深度** | 功能描述 | 深入剖析運作原理 |
| **範例** | 基礎程式碼片段 | 可立即使用的生產環境模板 |
| **結構** | 依功能組織 | 漸進式學習路線（初學者 → 進階） |
| **入門引導** | 自學導向 | 附時間估算的導引路線圖 |
| **自我評估** | 無 | 互動式測驗，幫助識別技能差距並建立個人化學習路線 |

**本指南包含：**
- Mermaid 圖表解釋每個功能的運作方式
- 可直接複製到專案中的現成配置
- 附上下文和最佳實務的真實範例
- 從 `/help` 到建構自訂代理的清晰進程
- 基於常見問題的疑難排解指南

---

## 目錄

- [為什麼需要這份指南？](#為什麼需要這份指南)
- [功能目錄](#-功能目錄)
- [快速導覽](#快速導覽)
- [學習路線](#-學習路線)
- [快速參考](#-快速參考選擇您的功能)
- [快速入門](#-快速入門)
- **功能**
  - [01. 斜線指令](#01-斜線指令)
  - [02. 記憶體](#02-記憶體)
  - [03. 技能](#03-技能)
  - [04. 子代理](#04-子代理)
  - [05. MCP 協定](#05-mcp-協定)
  - [06. Hooks](#06-hooks)
  - [07. 外掛套件](#07-外掛套件)
  - [08. 檢查點](#08-檢查點與倒轉)
  - [09. 進階功能](#09-進階功能)
  - [10. CLI 參考](#10-cli-參考)
- [目錄結構](#目錄結構)
- [安裝快速參考](#安裝快速參考)
- [範例工作流程](#範例工作流程)
- [最佳實務](#最佳實務)
- [疑難排解](#疑難排解)
- [測試](#測試)
- [其他資源](#其他資源)
- [貢獻](#貢獻)
- [EPUB 產生](#epub-產生)
- [貢獻者](#貢獻者)
- [Star 歷史](#star-歷史)

---

## 功能目錄

**需要快速參考？** 請查看我們完整的 **[功能目錄](CATALOG.md)**，包含：

- 所有斜線指令（內建和自訂），附說明
- 子代理及其能力
- 技能及自動觸發條件
- 外掛套件的元件和安裝指令
- 用於外部整合的 MCP 伺服器
- 用於事件驅動自動化的 Hooks
- 每個功能的一鍵安裝指令

**[查看完整目錄](CATALOG.md)**

---

## 快速導覽

| 功能 | 說明 | 資料夾 |
|---------|-------------|--------|
| **功能目錄** | 附安裝指令的完整參考 | [CATALOG.md](CATALOG.md) |
| **斜線指令** | 使用者呼叫的快捷方式 | [01-slash-commands/](01-slash-commands/) |
| **記憶體** | 持久化上下文 | [02-memory/](02-memory/) |
| **技能** | 可重複使用的能力 | [03-skills/](03-skills/) |
| **子代理** | 專門化的 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP 協定** | 外部工具存取 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驅動自動化 | [06-hooks/](06-hooks/) |
| **外掛套件** | 整合功能套件 | [07-plugins/](07-plugins/) |
| **檢查點** | 工作階段快照與倒轉 | [08-checkpoints/](08-checkpoints/) |
| **進階功能** | 規劃、思考、背景任務 | [09-advanced-features/](09-advanced-features/) |
| **CLI 參考** | 命令、旗標和選項 | [10-cli/](10-cli/) |
| **部落格文章** | 真實使用範例 | [部落格文章](https://medium.com/@luongnv89) |

---

## 📚 學習路線

**不確定從哪裡開始？** 參加 [自我評估測驗](LEARNING-ROADMAP.md#-find-your-level) 找到推薦的路線，或在 Claude Code 中執行 `/self-assessment` 進行互動式版本。

> **內建技能**：此倉庫包含兩個可在 Claude Code 中直接使用的互動式技能：
> - `/self-assessment` — 評估您的整體 Claude Code 熟練度並獲得個人化學習路線
> - `/lesson-quiz [lesson]` — 測試您對任何特定課程的理解（例如 `/lesson-quiz hooks`）

| 順序 | 功能 | 等級 | 時間 | 推薦對象 |
|-------|---------|-------|------|-----------------|
| **1** | [斜線指令](01-slash-commands/) | ⭐ 初學者 | 30 分鐘 | 等級 1 起點 |
| **2** | [記憶體](02-memory/) | ⭐⭐ 初學者+ | 45 分鐘 | 等級 1 |
| **3** | [檢查點](08-checkpoints/) | ⭐⭐ 中級 | 45 分鐘 | 等級 1 |
| **4** | [CLI 基礎](10-cli/) | ⭐⭐ 初學者+ | 30 分鐘 | 等級 1 |
| **5** | [技能](03-skills/) | ⭐⭐ 中級 | 1 小時 | 等級 2 起點 |
| **6** | [Hooks](06-hooks/) | ⭐⭐ 中級 | 1 小時 | 等級 2 |
| **7** | [MCP](05-mcp/) | ⭐⭐⭐ 中級+ | 1 小時 | 等級 2 |
| **8** | [子代理](04-subagents/) | ⭐⭐⭐ 中級+ | 1.5 小時 | 等級 2 |
| **9** | [進階](09-advanced-features/) | ⭐⭐⭐⭐⭐ 高級 | 2-3 小時 | 等級 3 起點 |
| **10** | [外掛套件](07-plugins/) | ⭐⭐⭐⭐ 高級 | 2 小時 | 等級 3 |
| **11** | [CLI 精通](10-cli/) | ⭐⭐⭐ 高級 | 1 小時 | 等級 3 |

**總計**：約 11-13 小時 | 📖 **[完整學習路線圖 →](LEARNING-ROADMAP.md)**

---

## 🎯 快速參考：選擇您的功能

### 功能比較

| 功能 | 呼叫方式 | 持久性 | 最適合 |
|---------|-----------|------------|----------|
| **斜線指令** | 手動 (`/cmd`) | 僅限工作階段 | 快速捷徑 |
| **記憶體** | 自動載入 | 跨工作階段 | 長期學習 |
| **技能** | 自動觸發 | 檔案系統 | 自動化工作流程 |
| **子代理** | 自動委派 | 隔離上下文 | 任務分配 |
| **MCP 協定** | 自動查詢 | 即時 | 即時資料存取 |
| **Hooks** | 事件觸發 | 已配置 | 自動化與驗證 |
| **外掛套件** | 一個指令 | 所有功能 | 完整解決方案 |
| **檢查點** | 手動/自動 | 基於工作階段 | 安全實驗 |
| **規劃模式** | 手動/自動 | 規劃階段 | 複雜實作 |
| **背景任務** | 手動 | 任務期間 | 長時間運行操作 |
| **CLI 參考** | 終端指令 | 工作階段/腳本 | 自動化與腳本編寫 |

### 使用案例矩陣

| 使用案例 | 推薦功能 |
|----------|---------------------|
| **團隊入職** | 記憶體 + 斜線指令 + 外掛套件 |
| **程式碼品質** | 子代理 + 技能 + 記憶體 + Hooks |
| **文件** | 技能 + 子代理 + 外掛套件 |
| **DevOps** | 外掛套件 + MCP + Hooks + 背景任務 |
| **安全審查** | 子代理 + 技能 + Hooks（唯讀模式） |
| **API 整合** | MCP + 記憶體 |
| **快速任務** | 斜線指令 |
| **複雜專案** | 所有功能 + 規劃模式 |
| **重構** | 檢查點 + 規劃模式 + Hooks |
| **學習/實驗** | 檢查點 + 延伸思考 + 權限模式 |
| **CI/CD 自動化** | CLI 參考 + Hooks + 背景任務 |
| **效能最佳化** | 規劃模式 + 檢查點 + 背景任務 |
| **腳本自動化** | CLI 參考 + Hooks + MCP |
| **批次處理** | CLI 參考 + 背景任務 |

---

## ⚡ 快速入門

### 15 分鐘 - 第一步
```bash
# 複製您的第一個斜線指令
cp 01-slash-commands/optimize.md .claude/commands/

# 試試看！
# 在 Claude Code 中：/optimize
```

### 1 小時 - 基本設定
```bash
# 1. 斜線指令（15 分鐘）
cp 01-slash-commands/*.md .claude/commands/

# 2. 專案記憶體（15 分鐘）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 3. 安裝技能（15 分鐘）
cp -r 03-skills/code-review ~/.claude/skills/

# 4. 一起試試（15 分鐘）
# 看看它們如何協同運作！
```

### 週末 - 完整設定
- **第 1 天**：斜線指令、記憶體、技能、Hooks
- **第 2 天**：子代理、MCP 整合、外掛套件
- **成果**：完整的 Claude Code 進階使用者設定

📖 **[詳細的里程碑和練習 →](LEARNING-ROADMAP.md)**

---

## 01. 斜線指令

**位置**：[01-slash-commands/](01-slash-commands/)

**說明**：以 Markdown 檔案儲存的使用者呼叫快捷方式

**範例**：
- `optimize.md` - 程式碼最佳化分析
- `pr.md` - Pull Request 準備
- `generate-api-docs.md` - API 文件產生器

**安裝**：
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使用方式**：
```
/optimize
/pr
/generate-api-docs
```

**了解更多**：[探索 Claude Code 斜線指令](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

---

## 02. 記憶體

**位置**：[02-memory/](02-memory/)

**說明**：跨工作階段的持久化上下文

**範例**：
- `project-CLAUDE.md` - 團隊級專案標準
- `directory-api-CLAUDE.md` - 目錄專用規則
- `personal-CLAUDE.md` - 個人偏好

**安裝**：
```bash
# 專案記憶體
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目錄記憶體
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 個人記憶體
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用方式**：由 Claude 自動載入

---

## 03. 技能

**位置**：[03-skills/](03-skills/)

**說明**：可重複使用、自動觸發的能力，包含指令和腳本

**範例**：
- `code-review/` - 包含腳本的綜合程式碼審查
- `brand-voice/` - 品牌語調一致性檢查器
- `doc-generator/` - API 文件產生器

**安裝**：
```bash
# 個人技能
cp -r 03-skills/code-review ~/.claude/skills/

# 專案技能
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使用方式**：在相關時自動觸發

---

## 04. 子代理

**位置**：[04-subagents/](04-subagents/)

**說明**：具有隔離上下文和自訂提示的專門化 AI 助手

**範例**：
- `code-reviewer.md` - 綜合程式碼品質分析
- `test-engineer.md` - 測試策略與覆蓋率
- `documentation-writer.md` - 技術文件
- `secure-reviewer.md` - 安全導向審查（唯讀）
- `implementation-agent.md` - 完整功能實作

**安裝**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用方式**：由主代理自動委派

---

## 05. MCP 協定

**位置**：[05-mcp/](05-mcp/)

**說明**：用於存取外部工具和 API 的 Model Context Protocol

**範例**：
- `github-mcp.json` - GitHub 整合
- `database-mcp.json` - 資料庫查詢
- `filesystem-mcp.json` - 檔案操作
- `multi-mcp.json` - 多個 MCP 伺服器

**安裝**：
```bash
# 設定環境變數
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 透過 CLI 新增 MCP 伺服器
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手動新增至專案 .mcp.json（參見 05-mcp/ 的範例）
```

**使用方式**：配置後，MCP 工具會自動提供給 Claude 使用

---

## 06. Hooks

**位置**：[06-hooks/](06-hooks/)

**說明**：回應 Claude Code 事件時自動執行的事件驅動 shell 指令

**範例**：
- `format-code.sh` - 寫入前自動格式化程式碼
- `pre-commit.sh` - 提交前執行測試
- `security-scan.sh` - 掃描安全問題
- `log-bash.sh` - 記錄所有 bash 指令
- `validate-prompt.sh` - 驗證使用者提示
- `notify-team.sh` - 事件發生時傳送通知

**安裝**：
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 hooks：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**使用方式**：Hooks 在事件發生時自動執行

**Hook 類型**：
- **工具 Hooks**：`PreToolUse:*`、`PostToolUse:*`
- **工作階段 Hooks**：`Stop`、`SubagentStop`、`SubagentStart`
- **生命週期 Hooks**：`Notification`、`ConfigChange`、`WorktreeCreate`、`WorktreeRemove`

---

## 07. 外掛套件

**位置**：[07-plugins/](07-plugins/)

**說明**：包含指令、代理、MCP 和 hooks 的整合套件

**範例**：
- `pr-review/` - 完整的 PR 審查工作流程
- `devops-automation/` - 部署與監控
- `documentation/` - 文件產生

**安裝**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使用方式**：使用套裝的斜線指令和功能

---

## 08. 檢查點與倒轉

**位置**：[08-checkpoints/](08-checkpoints/)

**說明**：儲存對話狀態並倒轉到先前的時間點，探索不同的方法

**關鍵概念**：
- **檢查點**：對話狀態的快照
- **倒轉**：返回到先前的檢查點
- **分支點**：從同一檢查點探索多種方法

**使用方式**：
```
# 檢查點會在每次使用者提示時自動建立
# 要倒轉，按兩次 Esc 或使用：
/rewind

# 然後從五個選項中選擇：
# 1. 還原程式碼和對話
# 2. 還原對話
# 3. 還原程式碼
# 4. 從此處摘要
# 5. 取消
```

**使用案例**：
- 嘗試不同的實作方法
- 從錯誤中恢復
- 安全實驗
- 比較替代方案
- A/B 測試不同設計

**範例工作流程**：
```
1. 正常工作（檢查點會自動建立）
2. 嘗試實驗性方法
3. 如果成功：繼續
4. 如果失敗：按 Esc+Esc 或 /rewind 返回
```

---

## 09. 進階功能

**位置**：[09-advanced-features/](09-advanced-features/)

**說明**：用於複雜工作流程和自動化的進階能力

### 規劃模式

在編碼之前建立詳細的實作計畫：
```
User: /plan Implement user authentication system

Claude: [建立全面的逐步計畫]

User: Approve and proceed
```

**優點**：清晰的路線圖、時間估算、風險評估

### 延伸思考

針對複雜問題的深度推理。使用 `Alt+T` / `Option+T` 切換，或設定 `MAX_THINKING_TOKENS` 環境變數：
```bash
# 在工作階段中切換：按 Alt+T（macOS 上為 Option+T）

# 或透過環境變數設定
MAX_THINKING_TOKENS=10000 claude

# 然後提出複雜問題
User: Should we use microservices or monolith?
Claude: [透過延伸推理系統性分析權衡]
```

**優點**：更好的架構決策、全面的分析

### 背景任務

在不阻塞的情況下執行長時間操作：
```
User: Run tests in background

Claude: Started bg-1234, you can continue working

[稍後] Test results: 245 passed, 3 failed
```

**優點**：並行開發、無需等待

### 權限模式

控制 Claude 可以執行的操作：
- **`default`**：帶確認提示的標準權限
- **`acceptEdits`**：自動接受檔案編輯，確認其他操作
- **`plan`**：僅分析和規劃，不進行修改
- **`dontAsk`**：不需確認即接受所有操作
- **`bypassPermissions`**：跳過所有權限檢查（危險）

```bash
claude --permission-mode plan          # 程式碼審查模式
claude --permission-mode acceptEdits   # 學習模式
claude --permission-mode default       # 標準模式
```

### Headless 模式

在 CI/CD 和自動化中執行 Claude Code：
```bash
claude -p "Run tests and generate report"
```

**使用案例**：CI/CD、自動化審查、批次處理

### 工作階段管理

管理多個工作階段：
```bash
/resume                          # 互動式恢復先前的工作階段
/rename                          # 重新命名當前工作階段
/fork                            # 分叉當前工作階段
claude -c                        # 繼續最近的工作階段
claude -r "session"              # 恢復符合查詢的工作階段
```

### 互動功能

**鍵盤快捷鍵**：Ctrl+R（搜尋）、Tab（自動完成）、↑/↓（歷史紀錄）

**指令歷史**：存取先前的指令

**多行輸入**：跨多行的複雜提示

### 配置

在 `~/.claude/settings.json` 中自訂 Claude Code 行為：
```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Bash(git *)"],
    "deny": ["Bash(rm -rf *)"]
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }]
  },
  "env": {
    "MAX_THINKING_TOKENS": "10000"
  }
}
```

完整配置請參見 [config-examples.json](09-advanced-features/config-examples.json)。

---

## 10. CLI 參考

**位置**：[10-cli/](10-cli/)

**說明**：Claude Code 的完整命令列介面參考

**主要領域**：
- CLI 指令（`claude`、`claude -p`、`claude -c`、`claude -r`）
- 核心旗標（列印模式、繼續、恢復、版本）
- 模型與配置（`--model`、`--agents`）
- 系統提示自訂
- 工具與權限管理
- 輸出格式（text、JSON、stream-JSON）
- MCP 配置
- 工作階段管理

**快速範例**：
```bash
# 互動模式
claude "explain this project"

# 列印模式（非互動）
claude -p "review this code"

# 處理檔案內容
cat error.log | claude -p "explain this error"

# 用於腳本的 JSON 輸出
claude -p --output-format json "list functions"

# 恢復工作階段
claude -r "feature-auth" "continue implementation"
```

**使用案例**：
- CI/CD 管道整合
- 腳本自動化和管道
- 批次處理
- 多工作階段工作流程
- 自訂代理配置

---

## 目錄結構

```

├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md（本檔案）
```

---

## 安裝快速參考

```bash
# 斜線指令
cp 01-slash-commands/*.md .claude/commands/

# 記憶體
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 技能
cp -r 03-skills/code-review ~/.claude/skills/

# 子代理
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 外掛套件
/plugin install pr-review

# 檢查點（自動啟用，在設定中配置）
# 參見 08-checkpoints/README.md

# 進階功能（在設定中配置）
# 參見 09-advanced-features/config-examples.json

# CLI 參考（無需安裝）
# 參見 10-cli/README.md 的使用範例
```

---

## 範例工作流程

### 1. 完整程式碼審查工作流程

```markdown
# 使用：斜線指令 + 子代理 + 記憶體 + MCP

User: /review-pr

Claude:
1. 載入專案記憶體（編碼標準）
2. 透過 GitHub MCP 取得 PR
3. 委派給 code-reviewer 子代理
4. 委派給 test-engineer 子代理
5. 綜合結果
6. 提供全面的審查
```

### 2. 自動化文件

```markdown
# 使用：技能 + 子代理 + 記憶體

User: "Generate API documentation for the auth module"

Claude:
1. 載入專案記憶體（文件標準）
2. 偵測到文件產生請求
3. 自動觸發 doc-generator 技能
4. 委派給 api-documenter 子代理
5. 建立包含範例的全面文件
```

### 3. DevOps 部署

```markdown
# 使用：外掛套件 + MCP + Hooks

User: /deploy production

Claude:
1. 執行部署前 hook（驗證環境）
2. 委派給 deployment-specialist 子代理
3. 透過 Kubernetes MCP 執行部署
4. 監控進度
5. 執行部署後 hook（健康檢查）
6. 回報狀態
```

---

## 最佳實務

### 應做 ✅
- 從斜線指令開始，保持簡單
- 逐步新增功能
- 使用記憶體儲存團隊標準
- 先在本機測試配置
- 記錄自訂實作
- 版本控制專案配置
- 與團隊分享外掛套件

### 不應做 ❌
- 不要建立冗餘功能
- 不要硬編碼憑證
- 不要跳過文件撰寫
- 不要將簡單任務過度複雜化
- 不要忽視安全最佳實務
- 不要提交敏感資料

---

## 疑難排解

### 功能未載入
1. 檢查檔案位置和命名
2. 驗證 YAML frontmatter 語法
3. 檢查檔案權限
4. 檢查 Claude Code 版本相容性

### MCP 連線失敗
1. 驗證環境變數
2. 檢查 MCP 伺服器安裝
3. 測試憑證
4. 檢查網路連線

### 子代理未委派
1. 檢查工具權限
2. 驗證代理描述的清晰度
3. 檢查任務複雜度
6. 獨立測試代理

---

## 測試

本專案包含全面的自動化測試，以確保程式碼品質和可靠性。

### 測試概覽

- **單元測試**：使用 pytest 的 Python 測試（Python 3.10、3.11、3.12）
- **程式碼品質**：使用 Ruff 進行程式碼檢查和格式化
- **安全性**：使用 Bandit 進行弱點掃描
- **型別檢查**：使用 mypy 進行靜態型別分析
- **建構驗證**：EPUB 產生測試
- **覆蓋率追蹤**：Codecov 整合

### 在本機執行測試

```bash
# 安裝開發依賴項
uv pip install -r requirements-dev.txt

# 執行所有單元測試
pytest scripts/tests/ -v

# 執行附覆蓋率報告的測試
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 執行程式碼品質檢查
ruff check scripts/
ruff format --check scripts/

# 執行安全掃描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 執行型別檢查
mypy scripts/ --ignore-missing-imports
```

### GitHub 上的自動化測試

測試會在以下情況自動執行：
- 每次推送到 `main` 或 `develop` 分支
- 每個對 `main` 的 Pull Request

在 GitHub Actions 標籤中查看測試結果，或查看 [TESTING.md](.github/TESTING.md) 指南以獲取詳細資訊。

### 撰寫測試

貢獻時，請為新功能包含測試：

1. **撰寫測試**在 `scripts/tests/test_*.py`
2. **在本機執行測試**以驗證通過
3. **檢查覆蓋率**使用 `pytest --cov=scripts`
4. **與 PR 一起提交** — 所有貢獻都需要測試

詳細的測試指南，請參見 [TESTING.md](.github/TESTING.md)。

---

## 其他資源

- [Claude Code 文件](https://code.claude.com/docs/en/overview)
- [MCP 協定規格](https://modelcontextprotocol.io)
- [技能倉庫](https://github.com/luongnv89/skills) - 現成可用的技能集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny 的 Claude Code 工作流程](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的創造者分享他的系統化工作流程：並行代理、共享 CLAUDE.md、Plan 模式、斜線指令、子代理和驗證 hooks，用於自主的長時間運行工作階段。關鍵見解包括將重複工作流程轉換為可重複使用的指令，以及將 Claude 接入團隊工具（GitHub、Slack、BigQuery、Sentry）以實現端到端的工作和回饋循環。

---

## 貢獻

發現問題或想要貢獻範例？我們歡迎您的幫助！

**請閱讀 [CONTRIBUTING.md](CONTRIBUTING.md) 以獲取詳細指南：**
- 貢獻類型（範例、文件、功能、錯誤、回饋）
- 如何設定開發環境
- 目錄結構和如何新增內容
- 撰寫指南和最佳實務
- 提交和 PR 流程

**我們的社群標準：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我們如何互相對待
- [SECURITY.md](SECURITY.md) - 安全政策和弱點回報

### 回報安全問題

如果您發現安全弱點，請負責任地回報：

1. **使用 GitHub 私人弱點回報**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或閱讀** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 以獲取詳細說明
3. **不要**為安全弱點開啟公開 issue

安全問題會被嚴肅對待並迅速處理。請參見 [SECURITY.md](SECURITY.md) 以了解我們的完整安全政策。

快速入門：
1. Fork 並 clone 此倉庫
2. 建立描述性分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按照指南進行變更
4. 提交附有清楚描述的 Pull Request

**需要幫助？** 開啟 issue 或討論，我們會引導您完成流程。

---

## 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案。

您可以自由地：
- 在您的專案中使用本指南和範例
- 修改和調整內容
- 分享和散佈
- 用於商業用途

唯一的要求是包含授權條款和版權聲明的副本。

---

## EPUB 產生

想要離線閱讀本指南？產生 EPUB 電子書：

```bash
uv run scripts/build_epub.py
```

這會建立 `claude-howto-guide.epub`，包含所有內容及渲染的 Mermaid 圖表。

詳情請參見 [scripts/README.md](scripts/README.md)。

---

## 貢獻者

感謝所有對本專案做出貢獻的人！

| 貢獻者 | PR |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

## Star 歷史

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

**最後更新**：2026 年 3 月
**Claude Code 版本**：2.1+
**相容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5

