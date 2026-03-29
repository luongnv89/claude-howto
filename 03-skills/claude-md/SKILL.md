---
name: claude-md
description: 遵循最佳實務建立或更新 CLAUDE.md 檔案，以實現最佳 AI agent 入職
---

## 使用者輸入

```text
$ARGUMENTS
```

你**必須**在繼續之前考慮使用者輸入（如果非空）。使用者可能指定：
- `create` - 從零開始建立新的 CLAUDE.md
- `update` - 改善現有的 CLAUDE.md
- `audit` - 分析並報告目前 CLAUDE.md 的品質
- 特定路徑以建立/更新（例如 `src/api/CLAUDE.md` 用於目錄特定指示）

## 核心原則

**LLM 是無狀態的**：CLAUDE.md 是唯一自動包含在每次對話中的檔案。它作為 AI agent 進入你的程式碼庫的主要入職文件。

### 黃金法則

1. **少即是多**：前沿 LLM 能遵循約 150-200 條指示。Claude Code 的系統提示已使用約 50 條。保持你的 CLAUDE.md 聚焦且簡潔。

2. **普遍適用性**：僅包含與每次工作階段相關的資訊。任務特定的指示應放在單獨的檔案中。

3. **不要將 Claude 當作 Linter 使用**：風格指南會膨脹上下文並降低指令遵循度。改用確定性工具（prettier、eslint 等）。

4. **絕不自動產生**：CLAUDE.md 是 AI 工具鏈中槓桿效果最高的點。用仔細考慮手工打造它。

## 執行流程

### 1. 專案分析

首先，分析目前的專案狀態：

1. 檢查現有的 CLAUDE.md 檔案：
   - 根目錄層級：`./CLAUDE.md` 或 `.claude/CLAUDE.md`
   - 目錄特定：`**/CLAUDE.md`
   - 全域使用者配置：`~/.claude/CLAUDE.md`

2. 識別專案結構：
   - 技術棧（語言、框架）
   - 專案類型（monorepo、單一應用、函式庫）
   - 開發工具（套件管理器、建置系統、測試執行器）

3. 審查現有文件：
   - README.md
   - CONTRIBUTING.md
   - package.json、pyproject.toml、Cargo.toml 等

### 2. 內容策略（什麼、為什麼、如何）

圍繞三個面向結構化 CLAUDE.md：

#### 什麼 - 技術與結構
- 技術棧概覽
- 專案組織（對 monorepo 特別重要）
- 關鍵目錄及其用途

#### 為什麼 - 目的與脈絡
- 專案的功能
- 為什麼做出某些架構決策
- 每個主要元件負責什麼

#### 如何 - 工作流程與慣例
- 開發工作流程（bun vs node、pip vs uv 等）
- 測試程序與指令
- 驗證與建置方法
- 關鍵的「陷阱」或非顯而易見的要求

### 3. 漸進式揭露策略

對於較大的專案，建議建立 `agent_docs/` 資料夾：

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

在 CLAUDE.md 中，使用如下指示引用這些檔案：
```markdown
For detailed build instructions, refer to `agent_docs/building_the_project.md`
```

**重要**：使用 `file:line` 引用而非程式碼片段，以避免過時的上下文。

### 4. 品質約束

建立或更新 CLAUDE.md 時：

1. **目標長度**：300 行以內（理想情況下 100 行以內）
2. **無風格規則**：移除任何格式化/靜態分析指示
3. **無任務特定指示**：移到單獨的檔案
4. **無程式碼片段**：改用檔案引用
5. **無冗餘資訊**：不要重複 package.json 或 README 中的內容

### 5. 必要章節

結構良好的 CLAUDE.md 應包含：

```markdown
# Project Name

Brief one-line description.

## Tech Stack
- Primary language and version
- Key frameworks/libraries
- Database/storage (if any)

## Project Structure
[Only for monorepos or complex structures]
- `apps/` - Application entry points
- `packages/` - Shared libraries

## Development Commands
- Install: `command`
- Test: `command`
- Build: `command`

## Critical Conventions
[Only non-obvious, high-impact conventions]
- Convention 1 with brief explanation
- Convention 2 with brief explanation

## Known Issues / Gotchas
[Things that consistently trip up developers]
- Issue 1
- Issue 2
```

### 6. 應避免的反模式

**不要包含：**
- 程式碼風格指南（使用 linter）
- 如何使用 Claude 的文件
- 顯而易見的模式的冗長解釋
- 複製貼上的程式碼範例
- 通用的最佳實務（「write clean code」）
- 特定任務的指示
- 自動產生的內容
- 大量的 TODO 清單

### 7. 驗證清單

定稿前驗證：

- [ ] 300 行以內（最好 100 行以內）
- [ ] 每一行都適用於所有工作階段
- [ ] 無風格/格式規則
- [ ] 無程式碼片段（使用檔案引用）
- [ ] 指令已驗證可執行
- [ ] 複雜專案使用漸進式揭露
- [ ] 關鍵陷阱已記錄
- [ ] 與 README.md 無冗餘

## 輸出格式

### 對於 `create` 或預設：

1. 分析專案
2. 按照上述結構起草 CLAUDE.md
3. 呈現草稿供審查
4. 批准後寫入適當位置

### 對於 `update`：

1. 閱讀現有 CLAUDE.md
2. 對照最佳實務審計
3. 識別：
   - 應移除的內容（風格規則、程式碼片段、任務特定內容）
   - 應濃縮的內容
   - 缺少的必要資訊
4. 呈現變更供審查
5. 批准後套用變更

### 對於 `audit`：

1. 閱讀現有 CLAUDE.md
2. 產生報告：
   - 目前行數 vs 目標
   - 普遍適用內容的百分比
   - 發現的反模式清單
   - 改善建議
3. 不要修改檔案，僅報告

## AGENTS.md 處理

如果使用者請求建立/更新 AGENTS.md：

AGENTS.md 用於定義專門的 agent 行為。與 CLAUDE.md（用於專案上下文）不同，AGENTS.md 定義：
- 自訂 agent 角色與能力
- Agent 特定的指示與限制
- 多 agent 場景的工作流程定義

套用類似原則：
- 保持聚焦且簡潔
- 使用漸進式揭露
- 引用外部文件而非嵌入內容

## 備註

- 在包含指令前始終驗證其可執行性
- 如有疑慮，就省略 - 少即是多
- 系統提示告訴 Claude，CLAUDE.md「可能與也可能與任務無關」- 雜訊越多，越容易被忽略
- Monorepo 從清晰的什麼/為什麼/如何結構中受益最多
- 目錄特定的 CLAUDE.md 檔案應更加聚焦
