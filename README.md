> **本倉庫為 [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) 的正體中文翻譯版本。**
> 翻譯倉庫：[huckly/claude-howto-zh-tw](https://github.com/huckly/claude-howto-zh-tw)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

[![GitHub Stars](https://img.shields.io/github/stars/huckly/claude-howto-zh-tw?style=flat&color=gold)](https://github.com/huckly/claude-howto-zh-tw/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/huckly/claude-howto-zh-tw?style=flat)](https://github.com/huckly/claude-howto-zh-tw/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# 一個週末精通 Claude Code

從輸入 `claude` 開始，到能夠靈活運用 agents（代理）、hooks（鉤子）、skills（技能）和 MCP 伺服器——透過圖文教學、即用範本和系統化學習路徑。

**[📚 詳細目錄](TABLE_OF_CONTENTS.md)** | **[15 分鐘快速上手](#-15-分鐘快速上手)** | **[找到你的程度](#-不確定從哪裡開始)** | **[瀏覽功能目錄](CATALOG.md)**

---

## 目錄

- [問題所在](#問題所在)
- [Claude How To 如何解決這些問題](#claude-how-to-如何解決這些問題)
- [使用方式](#使用方式)
- [不確定從哪裡開始？](#-不確定從哪裡開始)
- [15 分鐘快速上手](#-15-分鐘快速上手)
- [你可以用這些做什麼？](#你可以用這些做什麼)
- [常見問題](#常見問題)
- [參與貢獻](#參與貢獻)
- [授權條款](#授權條款)

---

## 問題所在

你安裝了 Claude Code，也試了幾個提示語。然後呢？

- **官方文件描述了功能——但沒有告訴你如何組合使用。** 你知道 slash commands（斜線指令）的存在，但不知道如何將它們與 hooks、memory（記憶）和 subagents（子代理）串連成一套真正能節省大量時間的工作流程。
- **沒有清晰的學習路徑。** 應該先學 MCP 還是 hooks？先學 skills 還是 subagents？你最終可能每樣都瀏覽了一遍，卻什麼都沒真正掌握。
- **範例太基礎。** 一個「hello world」斜線指令無法幫你建構一套運用 memory、委派專門 agents 並自動執行安全掃描的正式程式碼審查流程。

你正浪費了 Claude Code 90% 的能力——而且你不知道自己不知道什麼。

---

## Claude How To 如何解決這些問題

這不是另一份功能參考文件。這是一套**結構化、視覺化、範例驅動的指南**，教你如何使用 Claude Code 的每個功能，並提供可以直接複製到專案中的實戰範本。

| | 官方文件 | 本指南 |
|--|---------|--------|
| **格式** | 參考文件 | 搭配 Mermaid 圖表的視覺化教學 |
| **深度** | 功能描述 | 深入理解底層運作原理 |
| **範例** | 基本片段 | 可立即使用的正式範本 |
| **結構** | 依功能組織 | 漸進式學習路徑（入門到進階） |
| **引導** | 自行探索 | 附時間預估的引導路線圖 |
| **自我評估** | 無 | 互動式測驗，幫你找出不足之處並建立個人化學習路徑 |

### 你將獲得：

- **10 個教學模組**，涵蓋 Claude Code 的每個功能——從 slash commands 到自訂 agent 團隊
- **即複即用的配置**——slash commands、CLAUDE.md 範本、hook 腳本、MCP 配置、subagent 定義及完整 plugin 套件
- **Mermaid 圖表**展示每個功能的內部運作方式，讓你理解*為什麼*，而不只是*怎麼做*
- **引導式學習路徑**，帶你從入門到進階使用者，預計 11-13 小時完成
- **內建自我評估**——在 Claude Code 中直接執行 `/self-assessment` 或 `/lesson-quiz hooks` 來找出學習盲點

**[開始學習路徑 ->](LEARNING-ROADMAP.md)**

---

## 使用方式

### 1. 找到你的程度

參加[自我評估測驗](LEARNING-ROADMAP.md#-find-your-level)或在 Claude Code 中執行 `/self-assessment`。根據你已掌握的知識獲得個人化路線圖。

### 2. 跟隨引導路徑

按順序完成 10 個模組——每個都建立在前一個基礎上。學習過程中可直接將範本複製到你的專案中。

### 3. 將功能組合成工作流程

真正的威力在於功能的組合。學會將 slash commands + memory + subagents + hooks 串連成自動化流程，處理程式碼審查、部署和文件產生。

### 4. 驗證你的理解

每個模組結束後執行 `/lesson-quiz [主題]`。測驗會精確指出你遺漏的部分，讓你快速填補知識空缺。

**[15 分鐘快速上手](#-15-分鐘快速上手)**

---

## 📚 10 個核心章節一覽

| # | 章節 | 說明 | 級別 | 時間 |
|---|------|------|------|------|
| 📍 | **[01-slash-commands/](01-slash-commands/)** | 用戶觸發的快捷指令<br>`optimize` `pr` `commit` `doc-refactor` `generate-api-docs` | ⭐ 初級 | 30 分 |
| 🧠 | **[02-memory/](02-memory/)** | 跨會話持久化上下文<br>`project-CLAUDE.md` `directory-api-CLAUDE.md` `personal-CLAUDE.md` | ⭐ 初級 | 45 分 |
| 🔧 | **[03-skills/](03-skills/)** | 可復用的自動化工作流<br>`code-review` `brand-voice` `doc-generator` `refactor` | ⭐⭐ 中級 | 1 小時 |
| 🤖 | **[04-subagents/](04-subagents/)** | 專門化的 AI 助手<br>`code-reviewer` `test-engineer` `secure-reviewer` `implementation-agent` | ⭐⭐ 中級 | 1.5 小時 |
| 🔌 | **[05-mcp/](05-mcp/)** | 外部工具和 API 整合<br>Model Context Protocol 配置 | ⭐⭐ 中級 | 1 小時 |
| ⚡ | **[06-hooks/](06-hooks/)** | 事件驅動自動化<br>Pre/Post Tool Use、Pre/Post Bash、Notification | ⭐⭐ 中級 | 1 小時 |
| 📦 | **[07-plugins/](07-plugins/)** | 功能集合套件<br>`pr-review` `devops-automation` `documentation` | ⭐⭐⭐ 進階 | 2 小時 |
| 📍 | **[08-checkpoints/](08-checkpoints/)** | 會話快照和回放<br>探索多個實現方式、A/B 測試 | ⭐⭐ 中級 | 45 分 |
| 🚀 | **[09-advanced-features/](09-advanced-features/)** | 進階功能<br>Planning Mode、Extended Thinking、Background Tasks、Permission Modes | ⭐⭐⭐⭐ 進階 | 2-3 小時 |
| 💻 | **[10-cli/](10-cli/)** | 命令行介面完全參考<br>所有命令、標籤、選項和 CI/CD 用法 | ⭐⭐⭐ 進階 | 1 小時 |

**[📚 檢視詳細目錄 →](TABLE_OF_CONTENTS.md)**

---

## 受到 3,900+ 開發者信賴

- **3,900+ GitHub 星標**，來自日常使用 Claude Code 的開發者
- **460+ 分叉**——團隊依自身工作流程調整本指南
- **積極維護**——與每次 Claude Code 發布同步更新（最新版本：v2.2.0，2026 年 3 月）
- **社群驅動**——來自開發者分享的實際配置

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不確定從哪裡開始？

進行自我評估或選擇你的程度：

| 程度 | 你可以... | 從這裡開始 | 時間 |
|------|----------|-----------|------|
| **入門** | 啟動 Claude Code 並對話 | [Slash Commands](01-slash-commands/) | 約 2.5 小時 |
| **中級** | 使用 CLAUDE.md 和自訂指令 | [Skills](03-skills/) | 約 3.5 小時 |
| **進階** | 配置 MCP 伺服器和 hooks | [進階功能](09-advanced-features/) | 約 5 小時 |

**完整學習路徑，包含全部 10 個模組：**

| 順序 | 模組 | 程度 | 時間 |
|------|------|------|------|
| 1 | [Slash Commands](01-slash-commands/) | 入門 | 30 分鐘 |
| 2 | [Memory](02-memory/) | 入門+ | 45 分鐘 |
| 3 | [Checkpoints](08-checkpoints/) | 中級 | 45 分鐘 |
| 4 | [CLI 基礎](10-cli/) | 入門+ | 30 分鐘 |
| 5 | [Skills](03-skills/) | 中級 | 1 小時 |
| 6 | [Hooks](06-hooks/) | 中級 | 1 小時 |
| 7 | [MCP](05-mcp/) | 中級+ | 1 小時 |
| 8 | [Subagents](04-subagents/) | 中級+ | 1.5 小時 |
| 9 | [進階功能](09-advanced-features/) | 進階 | 2-3 小時 |
| 10 | [Plugins](07-plugins/) | 進階 | 2 小時 |

**[完整學習路線圖 ->](LEARNING-ROADMAP.md)**

---

## 15 分鐘快速上手

```bash
# 1. 複製指南
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 複製你的第一個 slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 試試看——在 Claude Code 中輸入：
# /optimize

# 4. 想要更多？設定專案記憶：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安裝一個 skill：
cp -r 03-skills/code-review ~/.claude/skills/
```

想要完整設定？以下是 **1 小時基本設定**：

```bash
# Slash commands（15 分鐘）
cp 01-slash-commands/*.md .claude/commands/

# 專案記憶（15 分鐘）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安裝一個 skill（15 分鐘）
cp -r 03-skills/code-review ~/.claude/skills/

# 週末目標：加入 hooks、subagents、MCP 和 plugins
# 跟隨學習路徑進行引導式設定
```

**[查看完整安裝參考](#安裝快速參考)**

---

## 你可以用這些做什麼？

| 使用場景 | 你將組合的功能 |
|---------|--------------|
| **自動化程式碼審查** | Slash Commands + Subagents + Memory + MCP |
| **團隊入職訓練** | Memory + Slash Commands + Plugins |
| **CI/CD 自動化** | CLI 參考 + Hooks + 背景任務 |
| **文件產生** | Skills + Subagents + Plugins |
| **安全稽核** | Subagents + Skills + Hooks（唯讀模式） |
| **DevOps 流程** | Plugins + MCP + Hooks + 背景任務 |
| **複雜重構** | Checkpoints + 規劃模式 + Hooks |

---

## 常見問題

**這是免費的嗎？**
是的。MIT 授權，永遠免費。可用於個人專案、工作、團隊中——唯一要求是保留授權聲明。

**有在維護嗎？**
積極維護中。本指南與每次 Claude Code 發布同步更新。當前版本：v2.2.0（2026 年 3 月），相容 Claude Code 2.1+。

**這和官方文件有什麼不同？**
官方文件是功能參考。本指南是包含圖表、正式範本和漸進式學習路徑的教學。兩者互補——從這裡開始學習，需要具體細節時參考官方文件。

**完成全部內容需要多長時間？**
完整路徑需要 11-13 小時。但你可以在 15 分鐘內獲得立即價值——只需複製一個 slash command 範本並試用即可。

**我可以搭配 Claude Sonnet / Haiku / Opus 使用嗎？**
可以。所有範本均適用於 Claude Sonnet 4.6、Claude Opus 4.6 和 Claude Haiku 4.5。

**我可以參與貢獻嗎？**
當然可以。請參閱 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指引。我們歡迎新範例、錯誤修正、文件改善和社群範本。

**我可以離線閱讀嗎？**
可以。執行 `uv run scripts/build_epub.py` 即可產生包含所有內容和渲染圖表的 EPUB 電子書。

---

## 立即開始精通 Claude Code

你已經安裝了 Claude Code。你和 10 倍生產力之間唯一的差距就是知道如何使用它。本指南為你提供結構化路徑、視覺化說明和即複即用的範本。

MIT 授權。永遠免費。複製它、分叉它、讓它成為你的。

**[開始學習路徑 ->](LEARNING-ROADMAP.md)** | **[瀏覽功能目錄](CATALOG.md)** | **[15 分鐘快速上手](#-15-分鐘快速上手)**

---

<details>
<summary>快速導覽——所有功能</summary>

| 功能 | 說明 | 資料夾 |
|------|------|--------|
| **功能目錄** | 含安裝指令的完整參考 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 使用者手動呼叫的快捷指令 | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 持久化上下文 | [02-memory/](02-memory/) |
| **Skills** | 可重複使用的能力 | [03-skills/](03-skills/) |
| **Subagents** | 專門化的 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP Protocol** | 外部工具存取 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驅動自動化 | [06-hooks/](06-hooks/) |
| **Plugins** | 功能套件 | [07-plugins/](07-plugins/) |
| **Checkpoints** | 工作階段快照與回溯 | [08-checkpoints/](08-checkpoints/) |
| **進階功能** | 規劃模式、深度思考、背景任務 | [09-advanced-features/](09-advanced-features/) |
| **CLI 參考** | 指令、旗標和選項 | [10-cli/](10-cli/) |
| **部落格文章** | 實際使用範例 | [部落格文章](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能比較</summary>

| 功能 | 呼叫方式 | 持久性 | 最適合 |
|------|---------|--------|--------|
| **Slash Commands** | 手動（`/cmd`） | 僅限工作階段 | 快捷操作 |
| **Memory** | 自動載入 | 跨工作階段 | 長期記憶 |
| **Skills** | 自動觸發 | 檔案系統 | 自動化工作流程 |
| **Subagents** | 自動委派 | 隔離上下文 | 任務分配 |
| **MCP Protocol** | 自動查詢 | 即時 | 即時資料存取 |
| **Hooks** | 事件觸發 | 已配置 | 自動化與驗證 |
| **Plugins** | 一鍵安裝 | 所有功能 | 完整解決方案 |
| **Checkpoints** | 手動/自動 | 工作階段 | 安全實驗 |
| **規劃模式** | 手動/自動 | 規劃階段 | 複雜實作 |
| **背景任務** | 手動 | 任務期間 | 長時間執行作業 |
| **CLI 參考** | 終端指令 | 工作階段/腳本 | 自動化與腳本 |

</details>

<details>
<summary>安裝快速參考</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints（自動啟用，在設定中配置）
# 參見 08-checkpoints/README.md

# 進階功能（在設定中配置）
# 參見 09-advanced-features/config-examples.json

# CLI 參考（無需安裝）
# 參見 10-cli/README.md 的使用範例
```

</details>

<details>
<summary>01. Slash Commands</summary>

**位置**：[01-slash-commands/](01-slash-commands/)

**功能**：以 Markdown 檔案儲存的使用者呼叫快捷指令

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

**進一步了解**：[探索 Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**位置**：[02-memory/](02-memory/)

**功能**：跨工作階段的持久化上下文

**範例**：
- `project-CLAUDE.md` - 全團隊專案標準
- `directory-api-CLAUDE.md` - 目錄專屬規則
- `personal-CLAUDE.md` - 個人偏好

**安裝**：
```bash
# 專案記憶
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目錄記憶
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 個人記憶
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用方式**：Claude 自動載入

</details>

<details>
<summary>03. Skills</summary>

**位置**：[03-skills/](03-skills/)

**功能**：含指示與腳本的可重複使用、自動觸發能力

**範例**：
- `code-review/` - 含腳本的完整程式碼審查
- `brand-voice/` - 品牌語氣一致性檢查器
- `doc-generator/` - API 文件產生器

**安裝**：
```bash
# 個人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 專案 skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使用方式**：相關時自動觸發

</details>

<details>
<summary>04. Subagents</summary>

**位置**：[04-subagents/](04-subagents/)

**功能**：具有隔離上下文和自訂提示的專門化 AI 助手

**範例**：
- `code-reviewer.md` - 全面的程式碼品質分析
- `test-engineer.md` - 測試策略與覆蓋率
- `documentation-writer.md` - 技術文件撰寫
- `secure-reviewer.md` - 安全導向審查（唯讀）
- `implementation-agent.md` - 完整功能實作

**安裝**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用方式**：由主代理自動委派

</details>

<details>
<summary>05. MCP Protocol</summary>

**位置**：[05-mcp/](05-mcp/)

**功能**：Model Context Protocol（模型上下文協定），用於存取外部工具和 API

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

# 或手動加入專案 .mcp.json（參見 05-mcp/ 的範例）
```

**使用方式**：配置完成後，MCP 工具自動可供 Claude 使用

</details>

<details>
<summary>06. Hooks</summary>

**位置**：[06-hooks/](06-hooks/)

**功能**：回應 Claude Code 事件時自動執行的事件驅動 shell 指令

**範例**：
- `format-code.sh` - 寫入前自動格式化程式碼
- `pre-commit.sh` - 提交前執行測試
- `security-scan.sh` - 掃描安全問題
- `log-bash.sh` - 記錄所有 bash 指令
- `validate-prompt.sh` - 驗證使用者提示
- `notify-team.sh` - 在事件發生時發送通知

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

**Hook 類型**（4 種類型，25 個事件）：
- **工具 Hooks**：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`PermissionRequest`
- **工作階段 Hooks**：`SessionStart`、`SessionEnd`、`Stop`、`StopFailure`、`SubagentStart`、`SubagentStop`
- **任務 Hooks**：`UserPromptSubmit`、`TaskCompleted`、`TaskCreated`、`TeammateIdle`
- **生命週期 Hooks**：`ConfigChange`、`CwdChanged`、`FileChanged`、`PreCompact`、`PostCompact`、`WorktreeCreate`、`WorktreeRemove`、`Notification`、`InstructionsLoaded`、`Elicitation`、`ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**位置**：[07-plugins/](07-plugins/)

**功能**：捆綁指令、agents、MCP 和 hooks 的功能套件

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

**使用方式**：使用捆綁的 slash commands 和功能

</details>

<details>
<summary>08. Checkpoints（檢查點）與回溯</summary>

**位置**：[08-checkpoints/](08-checkpoints/)

**功能**：儲存對話狀態並回溯到先前的時間點，以探索不同方案

**核心概念**：
- **Checkpoint（檢查點）**：對話狀態的快照
- **Rewind（回溯）**：返回到先前的檢查點
- **Branch Point（分支點）**：從同一個檢查點探索多種方案

**使用方式**：
```
# 每次使用者提示時自動建立檢查點
# 要回溯，按 Esc 兩次或使用：
/rewind

# 然後從五個選項中選擇：
# 1. 還原程式碼和對話
# 2. 還原對話
# 3. 還原程式碼
# 4. 從此處摘要
# 5. 算了
```

**使用場景**：
- 嘗試不同的實作方案
- 從錯誤中恢復
- 安全實驗
- 比較替代方案
- A/B 測試不同設計

</details>

<details>
<summary>09. 進階功能</summary>

**位置**：[09-advanced-features/](09-advanced-features/)

**功能**：用於複雜工作流程和自動化的進階能力

**包含**：
- **規劃模式** — 編碼前建立詳細的實作計劃
- **深度思考** — 針對複雜問題的深度推理（使用 `Alt+T` / `Option+T` 切換）
- **背景任務** — 執行長時間作業而不阻塞
- **權限模式** — `default`、`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions`
- **無頭模式** — 在 CI/CD 中執行 Claude Code：`claude -p "Run tests and generate report"`
- **工作階段管理** — `/resume`、`/rename`、`/fork`、`claude -c`、`claude -r`
- **配置** — 在 `~/.claude/settings.json` 中自訂行為

參見 [config-examples.json](09-advanced-features/config-examples.json) 了解完整配置。

</details>

<details>
<summary>10. CLI 參考</summary>

**位置**：[10-cli/](10-cli/)

**功能**：Claude Code 的完整命令列介面參考

**快速範例**：
```bash
# 互動模式
claude "explain this project"

# 列印模式（非互動）
claude -p "review this code"

# 處理檔案內容
cat error.log | claude -p "explain this error"

# 腳本用 JSON 輸出
claude -p --output-format json "list functions"

# 恢復工作階段
claude -r "feature-auth" "continue implementation"
```

**使用場景**：CI/CD 流程整合、腳本自動化、批次處理、多工作階段工作流程、自訂 agent 配置

</details>

<details>
<summary>範例工作流程</summary>

### 完整的程式碼審查工作流程

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

使用者：/review-pr

Claude：
1. 載入專案記憶（編碼標準）
2. 透過 GitHub MCP 取得 PR
3. 委派給 code-reviewer subagent
4. 委派給 test-engineer subagent
5. 綜合各項發現
6. 提供全面審查結果
```

### 自動化文件產生

```markdown
# 使用：Skills + Subagents + Memory

使用者："Generate API documentation for the auth module"

Claude：
1. 載入專案記憶（文件標準）
2. 偵測到文件產生請求
3. 自動觸發 doc-generator skill
4. 委派給 api-documenter subagent
5. 建立包含範例的完整文件
```

### DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

使用者：/deploy production

Claude：
1. 執行部署前 hook（驗證環境）
2. 委派給 deployment-specialist subagent
3. 透過 Kubernetes MCP 執行部署
4. 監控進度
5. 執行部署後 hook（健康檢查）
6. 報告狀態
```

</details>

<details>
<summary>目錄結構</summary>

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

</details>

<details>
<summary>最佳實踐</summary>

### 建議做法
- 從簡單的 slash commands 開始
- 逐步增加功能
- 使用 memory 記錄團隊標準
- 先在本地測試配置
- 為自訂實作撰寫文件
- 將專案配置加入版本控制
- 與團隊分享 plugins

### 避免事項
- 不要建立重複的功能
- 不要在程式碼中寫死認證資訊
- 不要跳過文件撰寫
- 不要過度複雜化簡單任務
- 不要忽視安全最佳實踐
- 不要提交敏感資料

</details>

<details>
<summary>疑難排解</summary>

### 功能未載入
1. 檢查檔案位置和命名
2. 確認 YAML frontmatter 語法
3. 檢查檔案權限
4. 確認 Claude Code 版本相容性

### MCP 連線失敗
1. 確認環境變數
2. 檢查 MCP 伺服器安裝
3. 測試認證資訊
4. 確認網路連線

### Subagent 未委派
1. 檢查工具權限
2. 確認 agent 描述清晰
3. 檢視任務複雜度
4. 獨立測試 agent

</details>

<details>
<summary>測試</summary>

本專案包含完整的自動化測試：

- **單元測試**：使用 pytest 的 Python 測試（Python 3.10、3.11、3.12）
- **程式碼品質**：使用 Ruff 進行 Lint 和格式化
- **安全性**：使用 Bandit 進行漏洞掃描
- **型別檢查**：使用 mypy 進行靜態型別分析
- **建置驗證**：EPUB 產生測試
- **覆蓋率追蹤**：Codecov 整合

```bash
# 安裝開發依賴
uv pip install -r requirements-dev.txt

# 執行所有單元測試
pytest scripts/tests/ -v

# 執行測試並產生覆蓋率報告
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 執行程式碼品質檢查
ruff check scripts/
ruff format --check scripts/

# 執行安全掃描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 執行型別檢查
mypy scripts/ --ignore-missing-imports
```

測試會在每次推送到 `main`/`develop` 和每個 PR 到 `main` 時自動執行。詳見 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 產生</summary>

想要離線閱讀本指南？產生 EPUB 電子書：

```bash
uv run scripts/build_epub.py
```

這會建立包含所有內容（含渲染後 Mermaid 圖表）的 `claude-howto-guide.epub`。

詳見 [scripts/README.md](scripts/README.md) 了解更多選項。

</details>

<details>
<summary>參與貢獻</summary>

發現問題或想貢獻範例？我們非常歡迎你的幫助！

**請閱讀 [CONTRIBUTING.md](CONTRIBUTING.md) 了解詳細指引：**
- 貢獻類型（範例、文件、功能、錯誤、回饋）
- 如何設定開發環境
- 目錄結構及如何新增內容
- 撰寫指引和最佳實踐
- 提交和 PR 流程

**我們的社群準則：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我們如何相互對待
- [SECURITY.md](SECURITY.md) - 安全政策和漏洞回報

### 回報安全問題

如果你發現安全漏洞，請負責任地回報：

1. **使用 GitHub 私有漏洞回報**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或閱讀** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 了解詳細說明
3. **不要**為安全漏洞開啟公開 issue

快速開始：
1. Fork 並 clone 倉庫
2. 建立描述性分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按照指引進行修改
4. 提交清楚描述的 Pull Request

**需要幫助？** 開啟 issue 或討論，我們會引導你完成流程。

</details>

<details>
<summary>其他資源</summary>

- [Claude Code 文件](https://code.claude.com/docs/en/overview)
- [MCP 協定規格](https://modelcontextprotocol.io)
- [Skills 倉庫](https://github.com/luongnv89/skills) - 即用 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny 的 Claude Code 工作流程](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的作者分享他的系統化工作流程：平行 agents、共享 CLAUDE.md、規劃模式、slash commands、subagents 和用於長時間自主工作階段的驗證 hooks。

</details>

---

## 參與貢獻

我們歡迎貢獻！請參閱 [貢獻指南](CONTRIBUTING.md) 了解如何開始。

## 貢獻者

感謝所有為本專案做出貢獻的人！

| 貢獻者 | PRs |
|--------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - 新增 epub 建立工具](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): 在概念指南中使用波浪號圍欄處理巢狀程式碼區塊](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 授權條款

MIT 授權 - 詳見 [LICENSE](LICENSE)。可自由使用、修改和散布。唯一要求是保留授權聲明。

---

**最後更新**：2026 年 3 月
**Claude Code 版本**：2.1+
**相容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
