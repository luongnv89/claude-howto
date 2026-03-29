# 📚 目錄詳細說明

本倉庫的完整結構和每個章節的詳細內容說明。

---

## 🎯 核心章節 (10 個主要功能模組)

### 📍 [01-slash-commands/](01-slash-commands/) — 斜線命令
**用途**: 用戶觸發的快捷指令

- `optimize.md` — 程式碼最佳化分析
- `pr.md` — Pull Request 準備
- `commit.md` — Git 提交輔助
- `doc-refactor.md` — 文件重構
- `generate-api-docs.md` — API 文件生成
- `push-all.md` — 全部推送
- `setup-ci-cd.md` — CI/CD 設置
- `unit-test-expand.md` — 單元測試擴展
- README — 詳細使用指南

---

### 🧠 [02-memory/](02-memory/) — 記憶 (跨會話持久化上下文)

存儲跨會話的持久化資訊，讓 Claude 記住你的偏好、專案標準和個人規則。

- `project-CLAUDE.md` — 專案級記憶 (團隊共享標準)
- `directory-api-CLAUDE.md` — 目錄級記憶 (特定資料夾規則)
- `personal-CLAUDE.md` — 個人記憶 (個人偏好)
- README — 如何組織和使用記憶

---

### 🔧 [03-skills/](03-skills/) — 技能 (可復用的自動化工作流)

**子目錄:**

#### 📝 blog-draft/ — 部落格草稿技能
- `SKILL.md` — 技能定義
- `templates/draft-template.md` — 草稿範本
- `templates/outline-template.md` — 大綱範本

#### 🎨 brand-voice/ — 品牌聲調檢查
- `SKILL.md` — 品牌聲調一致性檢查程式
- `tone-examples.md` — 聲調範例參考

#### 📋 claude-md/ — Claude Markdown 文件
- `SKILL.md` — 處理特殊的 Claude Markdown 格式

#### 👀 code-review/ — 程式碼審查
- `SKILL.md` — 完整的程式碼審查工作流
- `templates/finding-template.md` — 發現記錄範本
- `templates/review-checklist.md` — 審查檢查清單

#### 📖 doc-generator/ — API 文件生成
- `SKILL.md` — 自動生成 API 文件

#### ♻️ refactor/ — 程式碼重構
- `SKILL.md` — 智慧重構指南
- `references/code-smells.md` — 程式碼壞味道參考
- `references/refactoring-catalog.md` — 重構目錄
- `templates/refactoring-plan.md` — 重構計畫範本

---

### 🤖 [04-subagents/](04-subagents/) — 子代理 (專門化的 AI 助手)

獨立的代理，各有專項任務和自定義提示詞：

- `code-reviewer.md` — 程式碼品質分析
- `test-engineer.md` — 測試策略和覆蓋率
- `documentation-writer.md` — 技術文件寫作
- `secure-reviewer.md` — 安全性審查 (唯讀模式)
- `implementation-agent.md` — 完整功能實現
- `clean-code-reviewer.md` — 乾淨程式碼檢查
- `data-scientist.md` — 數據科學任務
- `debugger.md` — 除錯助手
- README — 代理使用和自訂指南

---

### 🔌 [05-mcp/](05-mcp/) — MCP 協議 (外部工具整合)

Model Context Protocol 配置示例，連接外部 API 和工具

- README — MCP 設置和配置指南

---

### ⚡ [06-hooks/](06-hooks/) — 鉤子 (事件驅動自動化)

事件觸發的 Shell 指令，在特定時刻自動執行

- README — 鉤子類型、安裝和配置

---

### 📦 [07-plugins/](07-plugins/) — 外掛 (功能束)

功能集合，每個都包含 commands、agents、MCP 和 hooks

#### 🔍 pr-review/ — PR 審查外掛
- README — PR 審查工作流
- `agents/` — 性能分析、安全審查、測試檢查
- `commands/` — 審查、安全檢查、測試檢查命令

#### 🚀 devops-automation/ — DevOps 自動化外掛
- README — 部署和監控工作流
- `agents/` — 告警分析、部署專家、事件指揮官
- `commands/` — 部署、事件、回滾、狀態命令

#### 📚 documentation/ — 文件生成外掛
- README — 文件生成工作流
- `agents/` — API 文件、程式碼註釋、範例生成
- `commands/` — API docs、README、同步、驗證
- `templates/` — ADR、API 端點、函數文件

---

### 📍 [08-checkpoints/](08-checkpoints/) — 檢查點 (會話快照和回放)

保存對話狀態並回到之前的檢查點

- README — 檢查點工作流
- `checkpoint-examples.md` — 實際使用範例

---

### 🚀 [09-advanced-features/](09-advanced-features/) — 進階功能

複雜工作流和自動化的高級功能

- README — 計畫模式、擴展思考、自動模式、背景任務、權限模式等
- `planning-mode-examples.md` — 計畫模式實例
- `config-examples.json` — 完整配置範例

---

### 💻 [10-cli/](10-cli/) — CLI 參考 (命令行介面)

Claude Code 命令行工具的完整參考

- README — 所有命令、標籤、選項和用例

---

## 📖 根目錄核心文檔

### 🎓 學習和指南
- **[README.md](README.md)** — 專案主入口，包含完整指南
- **[LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)** — 系統化學習路徑，按技能級別分類
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** — 快速參考卡
- **[CATALOG.md](CATALOG.md)** — 功能目錄和安裝命令
- **[claude_concepts_guide.md](claude_concepts_guide.md)** — Claude 概念完整指南

### 📋 文檔和規範
- **[INDEX.md](INDEX.md)** — 完整索引
- **[STYLE_GUIDE.md](STYLE_GUIDE.md)** — 寫作風格指南
- **[clean-code-rules.md](clean-code-rules.md)** — 乾淨程式碼規則

### 🔐 治理
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** — 社群行為準則
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — 貢獻指南
- **[SECURITY.md](SECURITY.md)** — 安全政策
- **[CHANGELOG.md](CHANGELOG.md)** — 變更日誌
- **[RELEASE_NOTES.md](RELEASE_NOTES.md)** — 發行說明

### 📁 .github/ — GitHub 配置
- `ISSUE_TEMPLATE/` — Issue 範本 (bug、文件、功能、問題)
- `SECURITY_REPORTING.md` — 安全漏洞報告指南
- `TESTING.md` — 測試指南
- `pull_request_template.md` — PR 範本

---

## 📦 .claude/ — Claude Code 特定文檔

### 🎓 skills/
- **lesson-quiz/** — 課程測驗技能
  - `SKILL.md` — 技能定義
  - `references/question-bank.md` — 題目庫

- **self-assessment/** — 自我評估技能
  - `SKILL.md` — 技能定義

---

## 📚 resources/ — 資源和參考

- **[DESIGN-SYSTEM.md](resources/DESIGN-SYSTEM.md)** — 設計系統
- **[QUICK-START.md](resources/QUICK-START.md)** — 快速開始指南
- **[README.md](resources/README.md)** — 資源說明

---

## 📊 scripts/ — 自動化指令碼

- **[README.md](scripts/README.md)** — 可用的指令碼和用法

---

## 💬 prompts/ — 提示詞範本

- **[remotion-video.md](prompts/remotion-video.md)** — 影片生成提示詞

---

## 📖 assets/logo — 標誌資源

- 專案標誌（深色和淺色模式）

---

## 🌍 翻譯和版本信息

- **原始專案**: [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)
- **翻譯版本**: 本倉庫 — 正體中文版本
- **版本**: 2.2.0
- **Claude Code**: 2.1+
- **相容模型**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5

---

## 🚀 快速導航

| 想要 | 前往 |
|------|------|
| 開始學習 | [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md) |
| 快速參考 | [QUICK_REFERENCE.md](QUICK_REFERENCE.md) |
| 所有功能清單 | [CATALOG.md](CATALOG.md) |
| 貢獻指南 | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 概念詳解 | [claude_concepts_guide.md](claude_concepts_guide.md) |
| 進階功能 | [09-advanced-features/README.md](09-advanced-features/README.md) |

---

**最後更新**: 2026 年 3 月
**翻譯者**: Claude Code (正體中文翻譯)
