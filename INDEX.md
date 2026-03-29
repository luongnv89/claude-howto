<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 範例 - 完整索引

本文件提供按功能類型組織的所有範例檔案的完整索引。

## 統計摘要

- **總檔案數**: 100+ 個檔案
- **類別**: 10 個功能類別
- **Plugins**: 3 個完整 plugins
- **Skills**: 6 個完整 skills
- **Hooks**: 8 個範例 hooks
- **可直接使用**: 所有範例

---

## 01. Slash Commands（10 個檔案）

使用者呼叫的常見工作流程快捷方式。

| 檔案 | 描述 | 使用場景 |
|------|-------------|----------|
| `optimize.md` | 程式碼最佳化分析器 | 尋找效能問題 |
| `pr.md` | Pull request 準備 | PR 工作流程自動化 |
| `generate-api-docs.md` | API 文件生成器 | 生成 API 文件 |
| `commit.md` | Commit 訊息輔助工具 | 標準化 commits |
| `setup-ci-cd.md` | CI/CD 管道設定 | DevOps 自動化 |
| `push-all.md` | 推送所有變更 | 快速推送工作流程 |
| `unit-test-expand.md` | 擴展單元測試覆蓋率 | 測試自動化 |
| `doc-refactor.md` | 文件重構 | 文件改善 |
| `pr-slash-command.png` | 截圖範例 | 視覺參考 |
| `README.md` | 文件 | 設定和使用指南 |

**安裝路徑**: `.claude/commands/`

**使用方式**: `/optimize`、`/pr`、`/generate-api-docs`、`/commit`、`/setup-ci-cd`、`/push-all`、`/unit-test-expand`、`/doc-refactor`

---

## 02. Memory（6 個檔案）

持久性上下文和專案標準。

| 檔案 | 描述 | 範圍 | 位置 |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | 團隊專案標準 | 專案範圍 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 特定規則 | 目錄 | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 個人偏好 | 使用者 | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 截圖：記憶體已儲存 | - | 視覺參考 |
| `memory-ask-claude.png` | 截圖：詢問 Claude | - | 視覺參考 |
| `README.md` | 文件 | - | 參考 |

**安裝方式**: 複製到適當的位置

**使用方式**: Claude 自動載入

---

## 03. Skills（28 個檔案）

具有腳本和範本的自動呼叫能力。

### Code Review Skill（5 個檔案）
```
code-review/
├── SKILL.md                          # Skill 定義
├── scripts/
│   ├── analyze-metrics.py            # 程式碼度量分析器
│   └── compare-complexity.py         # 複雜度比較
└── templates/
    ├── review-checklist.md           # 審查檢查清單
    └── finding-template.md           # 發現文件範本
```

**用途**: 包含安全、效能和品質分析的全面程式碼審查

**自動呼叫**: 審查程式碼時

---

### Brand Voice Skill（4 個檔案）
```
brand-voice/
├── SKILL.md                          # Skill 定義
├── templates/
│   ├── email-template.txt            # 電子郵件格式
│   └── social-post-template.txt      # 社群媒體格式
└── tone-examples.md                  # 訊息範例
```

**用途**: 確保通訊中的品牌語調一致性

**自動呼叫**: 建立行銷文案時

---

### Documentation Generator Skill（2 個檔案）
```
doc-generator/
├── SKILL.md                          # Skill 定義
└── generate-docs.py                  # Python 文件提取器
```

**用途**: 從原始碼生成全面的 API 文件

**自動呼叫**: 建立/更新 API 文件時

---

### Refactor Skill（5 個檔案）
```
refactor/
├── SKILL.md                          # Skill 定義
├── scripts/
│   ├── analyze-complexity.py         # 複雜度分析器
│   └── detect-smells.py              # 程式碼異味偵測器
├── references/
│   ├── code-smells.md                # 程式碼異味目錄
│   └── refactoring-catalog.md        # 重構模式
└── templates/
    └── refactoring-plan.md           # 重構計畫範本
```

**用途**: 包含複雜度分析的系統化程式碼重構

**自動呼叫**: 重構程式碼時

---

### Claude MD Skill（1 個檔案）
```
claude-md/
└── SKILL.md                          # Skill 定義
```

**用途**: 管理和最佳化 CLAUDE.md 檔案

---

### Blog Draft Skill（3 個檔案）
```
blog-draft/
├── SKILL.md                          # Skill 定義
└── templates/
    ├── draft-template.md             # 部落格草稿範本
    └── outline-template.md           # 部落格大綱範本
```

**用途**: 以一致的結構起草部落格文章

**另外**: `README.md` - Skills 概述和使用指南

**安裝路徑**: `~/.claude/skills/` 或 `.claude/skills/`

---

## 04. Subagents（9 個檔案）

具有自訂能力的專門化 AI 助手。

| 檔案 | 描述 | 工具 | 使用場景 |
|------|-------------|-------|----------|
| `code-reviewer.md` | 程式碼品質分析 | read、grep、diff、lint_runner | 全面審查 |
| `test-engineer.md` | 測試覆蓋率分析 | read、write、bash、grep | 測試自動化 |
| `documentation-writer.md` | 文件建立 | read、write、grep | 文件生成 |
| `secure-reviewer.md` | 安全審查（唯讀） | read、grep | 安全稽核 |
| `implementation-agent.md` | 完整實作 | read、write、bash、grep、edit、glob | 功能開發 |
| `debugger.md` | 除錯專家 | read、bash、grep | 錯誤調查 |
| `data-scientist.md` | 資料分析專家 | read、write、bash | 資料工作流程 |
| `clean-code-reviewer.md` | 整潔程式碼標準 | read、grep | 程式碼品質 |
| `README.md` | 文件 | - | 設定和使用指南 |

**安裝路徑**: `.claude/agents/`

**使用方式**: 由主代理自動委派

---

## 05. MCP Protocol（5 個檔案）

外部工具和 API 整合。

| 檔案 | 描述 | 整合對象 | 使用場景 |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub 整合 | GitHub API | PR/issue 管理 |
| `database-mcp.json` | 資料庫查詢 | PostgreSQL/MySQL | 即時資料查詢 |
| `filesystem-mcp.json` | 檔案操作 | 本機檔案系統 | 檔案管理 |
| `multi-mcp.json` | 多個伺服器 | GitHub + DB + Slack | 完整整合 |
| `README.md` | 文件 | - | 設定和使用指南 |

**安裝路徑**: `.mcp.json`（專案範圍）或 `~/.claude.json`（使用者範圍）

**使用方式**: `/mcp__github__list_prs` 等

---

## 06. Hooks（9 個檔案）

自動執行的事件驅動自動化腳本。

| 檔案 | 描述 | 事件 | 使用場景 |
|------|-------------|-------|----------|
| `format-code.sh` | 自動格式化程式碼 | PreToolUse:Write | 程式碼格式化 |
| `pre-commit.sh` | 提交前執行測試 | PreToolUse:Bash | 測試自動化 |
| `security-scan.sh` | 安全掃描 | PostToolUse:Write | 安全檢查 |
| `log-bash.sh` | 記錄 bash 指令 | PostToolUse:Bash | 指令記錄 |
| `validate-prompt.sh` | 驗證提示 | PreToolUse | 輸入驗證 |
| `notify-team.sh` | 發送通知 | Notification | 團隊通知 |
| `context-tracker.py` | 追蹤上下文視窗使用量 | PostToolUse | 上下文監控 |
| `context-tracker-tiktoken.py` | 基於 token 的上下文追蹤 | PostToolUse | 精確 token 計算 |
| `README.md` | 文件 | - | 設定和使用指南 |

**安裝路徑**: 在 `~/.claude/settings.json` 中配置

**使用方式**: 在設定中配置，自動執行

**Hook 類型**（4 種類型、25 個事件）：
- 工具 Hooks：PreToolUse、PostToolUse、PostToolUseFailure、PermissionRequest
- 工作階段 Hooks：SessionStart、SessionEnd、Stop、StopFailure、SubagentStart、SubagentStop
- 任務 Hooks：UserPromptSubmit、TaskCompleted、TaskCreated、TeammateIdle
- 生命週期 Hooks：ConfigChange、CwdChanged、FileChanged、PreCompact、PostCompact、WorktreeCreate、WorktreeRemove、Notification、InstructionsLoaded、Elicitation、ElicitationResult

---

## 07. Plugins（3 個完整 plugins、40 個檔案）

功能的整合套件。

### PR Review Plugin（10 個檔案）
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Plugin 清單
├── commands/
│   ├── review-pr.md                  # 全面審查
│   ├── check-security.md             # 安全檢查
│   └── check-tests.md                # 測試覆蓋率檢查
├── agents/
│   ├── security-reviewer.md          # 安全專家
│   ├── test-checker.md               # 測試專家
│   └── performance-analyzer.md       # 效能專家
├── mcp/
│   └── github-config.json            # GitHub 整合
├── hooks/
│   └── pre-review.js                 # 預審查驗證
└── README.md                         # Plugin 文件
```

**功能**: 安全分析、測試覆蓋率、效能影響

**指令**: `/review-pr`、`/check-security`、`/check-tests`

**安裝方式**: `/plugin install pr-review`

---

### DevOps Automation Plugin（15 個檔案）
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin 清單
├── commands/
│   ├── deploy.md                     # 部署
│   ├── rollback.md                   # 回滾
│   ├── status.md                     # 系統狀態
│   └── incident.md                   # 事件回應
├── agents/
│   ├── deployment-specialist.md      # 部署專家
│   ├── incident-commander.md         # 事件協調員
│   └── alert-analyzer.md             # 警報分析器
├── mcp/
│   └── kubernetes-config.json        # Kubernetes 整合
├── hooks/
│   ├── pre-deploy.js                 # 部署前檢查
│   └── post-deploy.js                # 部署後任務
├── scripts/
│   ├── deploy.sh                     # 部署自動化
│   ├── rollback.sh                   # 回滾自動化
│   └── health-check.sh               # 健康檢查
└── README.md                         # Plugin 文件
```

**功能**: Kubernetes 部署、回滾、監控、事件回應

**指令**: `/deploy`、`/rollback`、`/status`、`/incident`

**安裝方式**: `/plugin install devops-automation`

---

### Documentation Plugin（14 個檔案）
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin 清單
├── commands/
│   ├── generate-api-docs.md          # API 文件生成
│   ├── generate-readme.md            # README 建立
│   ├── sync-docs.md                  # 文件同步
│   └── validate-docs.md              # 文件驗證
├── agents/
│   ├── api-documenter.md             # API 文件專家
│   ├── code-commentator.md           # 程式碼註解專家
│   └── example-generator.md          # 範例建立者
├── mcp/
│   └── github-docs-config.json       # GitHub 整合
├── templates/
│   ├── api-endpoint.md               # API 端點範本
│   ├── function-docs.md              # 函式文件範本
│   └── adr-template.md               # ADR 範本
└── README.md                         # Plugin 文件
```

**功能**: API 文件、README 生成、文件同步、驗證

**指令**: `/generate-api-docs`、`/generate-readme`、`/sync-docs`、`/validate-docs`

**安裝方式**: `/plugin install documentation`

**另外**: `README.md` - Plugins 概述和使用指南

---

## 08. Checkpoints and Rewind（2 個檔案）

儲存對話狀態並探索不同方法。

| 檔案 | 描述 | 內容 |
|------|-------------|---------|
| `README.md` | 文件 | 全面的檢查點指南 |
| `checkpoint-examples.md` | 實際範例 | 資料庫遷移、效能最佳化、UI 迭代、除錯 |
| | | |

**關鍵概念**：
- **Checkpoint（檢查點）**: 對話狀態的快照
- **Rewind（回退）**: 返回先前的檢查點
- **Branch Point（分支點）**: 探索多種方法

**使用方式**：
```
# 檢查點在每次使用者提示時自動建立
# 要回退，按兩次 Esc 或使用：
/rewind
# 然後選擇：還原程式碼和對話、還原對話、
# 還原程式碼、從此處摘要、或取消
```

**使用場景**：
- 嘗試不同的實作方式
- 從錯誤中復原
- 安全實驗
- 比較解決方案
- A/B 測試

---

## 09. Advanced Features（3 個檔案）

用於複雜工作流程的進階能力。

| 檔案 | 描述 | 功能 |
|------|-------------|----------|
| `README.md` | 完整指南 | 所有進階功能文件 |
| `config-examples.json` | 設定範例 | 10+ 個使用場景的特定設定 |
| `planning-mode-examples.md` | 規劃範例 | REST API、資料庫遷移、重構 |
| Scheduled Tasks | 使用 `/loop` 和 cron 工具的排程任務 | 自動化週期性工作流程 |
| Chrome Integration | 透過無頭 Chromium 進行瀏覽器自動化 | 網頁測試和擷取 |
| Remote Control（擴展） | 連接方式、安全、比較表 | 遠端工作階段管理 |
| Keyboard Customization | 自訂鍵盤快捷鍵、組合鍵支援、上下文 | 個人化快捷鍵 |
| Desktop App（擴展） | 連接器、launch.json、企業功能 | 桌面整合 |
| | | |

**涵蓋的進階功能**：

### Planning Mode（規劃模式）
- 建立詳細的實作計畫
- 時間估計和風險評估
- 系統化的任務分解

### Extended Thinking（延伸思考）
- 複雜問題的深度推理
- 架構決策分析
- 權衡評估

### Background Tasks（背景任務）
- 長時間操作不阻塞
- 並行開發工作流程
- 任務管理和監控

### Permission Modes（權限模式）
- **default**: 對風險操作要求批准
- **acceptEdits**: 自動接受檔案編輯，其他操作詢問
- **plan**: 唯讀分析，不修改
- **auto**: 自動批准安全操作，風險操作提示
- **dontAsk**: 接受所有操作（風險操作除外）
- **bypassPermissions**: 接受所有操作（需要 `--dangerously-skip-permissions`）

### Headless Mode（無頭模式，`claude -p`）
- CI/CD 整合
- 自動化任務執行
- 批次處理

### Session Management（工作階段管理）
- 多個工作階段
- 工作階段切換和儲存
- 工作階段持久化

### Interactive Features（互動功能）
- 鍵盤快捷鍵
- 指令歷史
- Tab 補全
- 多行輸入

### Configuration（設定）
- 全面的設定管理
- 環境特定設定
- 專案級自訂

### Scheduled Tasks（排程任務）
- 使用 `/loop` 指令的週期性任務
- Cron 工具：CronCreate、CronList、CronDelete
- 自動化週期性工作流程

### Chrome Integration
- 透過無頭 Chromium 進行瀏覽器自動化
- 網頁測試和擷取能力
- 頁面互動和資料提取

### Remote Control（擴展）
- 連接方式和協定
- 安全考量和最佳實踐
- 遠端存取選項比較表

### Keyboard Customization
- 自訂鍵盤快捷鍵設定
- 多鍵組合的組合鍵支援
- 上下文感知的鍵盤快捷鍵啟用

### Desktop App（擴展）
- IDE 整合的連接器
- launch.json 設定
- 企業功能和部署

---

## 10. CLI Usage（1 個檔案）

命令列介面使用模式和參考。

| 檔案 | 描述 | 內容 |
|------|-------------|---------|
| `README.md` | CLI 文件 | 旗標、選項和使用模式 |

**關鍵 CLI 功能**：
- `claude` - 啟動互動式工作階段
- `claude -p "prompt"` - 無頭/非互動模式
- `claude web` - 啟動網頁工作階段
- `claude --model` - 選擇模型（Sonnet 4.6、Opus 4.6）
- `claude --permission-mode` - 設定權限模式
- `claude --remote` - 透過 WebSocket 啟用遠端控制

---

## 文件檔案（13 個檔案）

| 檔案 | 位置 | 描述 |
|------|----------|-------------|
| `README.md` | `/` | 主要範例概述 |
| `INDEX.md` | `/` | 本完整索引 |
| `QUICK_REFERENCE.md` | `/` | 快速參考卡 |
| `README.md` | `/01-slash-commands/` | Slash commands 指南 |
| `README.md` | `/02-memory/` | Memory 指南 |
| `README.md` | `/03-skills/` | Skills 指南 |
| `README.md` | `/04-subagents/` | Subagents 指南 |
| `README.md` | `/05-mcp/` | MCP 指南 |
| `README.md` | `/06-hooks/` | Hooks 指南 |
| `README.md` | `/07-plugins/` | Plugins 指南 |
| `README.md` | `/08-checkpoints/` | Checkpoints 指南 |
| `README.md` | `/09-advanced-features/` | 進階功能指南 |
| `README.md` | `/10-cli/` | CLI 指南 |

---

## 完整檔案樹

```
claude-howto/
├── README.md                                    # 主要概述
├── INDEX.md                                     # 本檔案
├── QUICK_REFERENCE.md                           # 快速參考卡
├── claude_concepts_guide.md                     # 原始指南
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI Usage
    └── README.md
```

---

## 依使用場景快速開始

### 程式碼品質與審查
```bash
# 安裝 slash command
cp 01-slash-commands/optimize.md .claude/commands/

# 安裝 subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# 安裝 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 或安裝完整 plugin
/plugin install pr-review
```

### DevOps 與部署
```bash
# 安裝 plugin（包含所有功能）
/plugin install devops-automation
```

### 文件撰寫
```bash
# 安裝 slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 安裝 subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# 安裝 skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# 或安裝完整 plugin
/plugin install documentation
```

### 團隊標準
```bash
# 設定專案記憶體
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 編輯以符合你的團隊標準
```

### 外部整合
```bash
# 設定環境變數
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安裝 MCP 設定（專案範圍）
cp 05-mcp/multi-mcp.json .mcp.json
```

### 自動化與驗證
```bash
# 安裝 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在設定中配置 hooks（~/.claude/settings.json）
# 參見 06-hooks/README.md
```

### 安全實驗
```bash
# 檢查點在每次使用者提示時自動建立
# 要回退：按 Esc+Esc 或使用 /rewind
# 然後從回退選單中選擇要還原的內容

# 參見 08-checkpoints/README.md 了解範例
```

### 進階工作流程
```bash
# 設定進階功能
# 參見 09-advanced-features/config-examples.json

# 使用規劃模式
/plan Implement feature X

# 使用權限模式
claude --permission-mode plan          # 程式碼審查（唯讀）
claude --permission-mode acceptEdits   # 自動接受編輯
claude --permission-mode auto          # 自動批准安全操作

# 以無頭模式執行 CI/CD
claude -p "Run tests and report results"

# 執行背景任務
Run tests in background

# 參見 09-advanced-features/README.md 了解完整指南
```

---

## 功能覆蓋矩陣

| 類別 | 指令 | 代理 | MCP | Hooks | 腳本 | 範本 | 文件 | 圖片 | 總計 |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagents** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## 學習路徑

### 初級（第 1 週）
1. 閱讀 `README.md`
2. 安裝 1-2 個 slash commands
3. 建立專案記憶體檔案
4. 嘗試基本指令

### 中級（第 2-3 週）
1. 設定 GitHub MCP
2. 安裝一個 subagent
3. 嘗試委派任務
4. 安裝一個 skill

### 進階（第 4 週以上）
1. 安裝完整 plugin
2. 建立自訂 slash commands
3. 建立自訂 subagent
4. 建立自訂 skill
5. 建構你自己的 plugin

### 專家（第 5 週以上）
1. 設定自動化 hooks
2. 使用檢查點進行實驗
3. 設定規劃模式
4. 有效使用權限模式
5. 為 CI/CD 設定無頭模式
6. 精通工作階段管理

---

## 依關鍵字搜尋

### 效能
- `01-slash-commands/optimize.md` - 效能分析
- `04-subagents/code-reviewer.md` - 效能審查
- `03-skills/code-review/` - 效能度量
- `07-plugins/pr-review/agents/performance-analyzer.md` - 效能專家

### 安全
- `04-subagents/secure-reviewer.md` - 安全審查
- `03-skills/code-review/` - 安全分析
- `07-plugins/pr-review/` - 安全檢查

### 測試
- `04-subagents/test-engineer.md` - 測試工程師
- `07-plugins/pr-review/commands/check-tests.md` - 測試覆蓋率

### 文件
- `01-slash-commands/generate-api-docs.md` - API 文件指令
- `04-subagents/documentation-writer.md` - 文件撰寫代理
- `03-skills/doc-generator/` - 文件生成 skill
- `07-plugins/documentation/` - 完整文件 plugin

### 部署
- `07-plugins/devops-automation/` - 完整 DevOps 解決方案

### 自動化
- `06-hooks/` - 事件驅動自動化
- `06-hooks/pre-commit.sh` - 預提交自動化
- `06-hooks/format-code.sh` - 自動格式化
- `09-advanced-features/` - CI/CD 的無頭模式

### 驗證
- `06-hooks/security-scan.sh` - 安全驗證
- `06-hooks/validate-prompt.sh` - 提示驗證

### 實驗
- `08-checkpoints/` - 使用回退的安全實驗
- `08-checkpoints/checkpoint-examples.md` - 實際範例

### 規劃
- `09-advanced-features/planning-mode-examples.md` - 規劃模式範例
- `09-advanced-features/README.md` - 延伸思考

### 設定
- `09-advanced-features/config-examples.json` - 設定範例

---

## 備註

- 所有範例都可直接使用
- 根據你的具體需求進行修改
- 範例遵循 Claude Code 最佳實踐
- 每個類別都有自己的 README，包含詳細說明
- 腳本包含適當的錯誤處理
- 範本可自訂

---

## 貢獻

想新增更多範例？請遵循以下結構：
1. 建立適當的子目錄
2. 包含使用說明的 README.md
3. 遵循命名慣例
4. 徹底測試
5. 更新本索引

---

**最後更新**: 2026 年 3 月
**範例總數**: 100+ 個檔案
**類別**: 10 個功能
**Hooks**: 8 個自動化腳本
**設定範例**: 10+ 個場景
**可直接使用**: 所有範例

