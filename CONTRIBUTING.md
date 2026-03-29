<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 貢獻 Claude How To

感謝你有興趣為本專案做出貢獻！本指南將幫助你了解如何有效地進行貢獻。

## 關於本專案

Claude How To 是一套視覺化、範例驅動的 Claude Code 指南。我們提供：
- **Mermaid 圖表**解釋功能如何運作
- **正式可用的範本**讓你可以立即使用
- **實際範例**附帶上下文和最佳實踐
- **漸進式學習路徑**從入門到進階

## 貢獻類型

### 1. 新範例或範本
為現有功能新增範例（slash commands、skills、hooks 等）：
- 可直接複製貼上的程式碼
- 清晰解釋其運作方式
- 使用場景和優勢
- 疑難排解提示

### 2. 文件改善
- 澄清令人困惑的章節
- 修正錯字和語法
- 補充缺少的資訊
- 改善程式碼範例

### 3. 功能指南
為新的 Claude Code 功能建立指南：
- 逐步教學
- 架構圖表
- 常見模式和反模式
- 實際工作流程

### 4. 錯誤回報
回報你遇到的問題：
- 描述你預期的結果
- 描述實際發生的情況
- 包含重現步驟
- 附上相關的 Claude Code 版本和作業系統

### 5. 回饋和建議
幫助改善指南：
- 建議更好的解釋
- 指出覆蓋不足的地方
- 建議新的章節或重新組織

## 開始

### 1. Fork 並 Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. 建立分支
使用描述性的分支名稱：
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. 設定開發環境
```bash
# 建立虛擬環境
python3 -m venv .venv
source .venv/bin/activate

# 安裝 pre-commit hooks（可選但建議）
pip install pre-commit
pre-commit install

# 手動執行 pre-commit 檢查
pre-commit run --all-files
```

## 目錄結構

```
├── 01-slash-commands/      # 使用者呼叫的快捷指令
├── 02-memory/              # 持久化上下文範例
├── 03-skills/              # 可重複使用的能力
├── 04-subagents/           # 專門化的 AI 助手
├── 05-mcp/                 # Model Context Protocol 範例
├── 06-hooks/               # 事件驅動自動化
├── 07-plugins/             # 功能套件
├── 08-checkpoints/         # 工作階段快照
├── 09-advanced-features/   # 規劃模式、深度思考、背景任務
├── 10-cli/                 # CLI 參考
├── scripts/                # 建置和工具腳本
└── README.md               # 主指南
```

## 如何貢獻範例

### 新增 Slash Command
1. 在 `01-slash-commands/` 中建立 `.md` 檔案
2. 包含：
   - 清楚描述其功能
   - 使用場景
   - 安裝說明
   - 使用範例
   - 自訂提示
3. 更新 `01-slash-commands/README.md`

### 新增 Skill
1. 在 `03-skills/` 中建立目錄
2. 包含：
   - `SKILL.md` - 主要文件
   - `scripts/` - 輔助腳本（如需要）
   - `templates/` - 提示範本
   - README 中的使用範例
3. 更新 `03-skills/README.md`

### 新增 Subagent
1. 在 `04-subagents/` 中建立 `.md` 檔案
2. 包含：
   - Agent 目的和能力
   - 系統提示結構
   - 使用場景範例
   - 整合範例
3. 更新 `04-subagents/README.md`

### 新增 MCP 配置
1. 在 `05-mcp/` 中建立 `.json` 檔案
2. 包含：
   - 配置說明
   - 所需的環境變數
   - 設定說明
   - 使用範例
3. 更新 `05-mcp/README.md`

### 新增 Hook
1. 在 `06-hooks/` 中建立 `.sh` 檔案
2. 包含：
   - Shebang 和描述
   - 解釋邏輯的清楚註解
   - 錯誤處理
   - 安全注意事項
3. 更新 `06-hooks/README.md`

## 撰寫指引

### Markdown 風格
- 使用清楚的標題（H2 用於區段，H3 用於子區段）
- 保持段落簡短且聚焦
- 使用項目符號列表
- 在程式碼區塊中指定語言
- 區段之間加入空行

### 程式碼範例
- 讓範例可直接複製貼上
- 為非顯而易見的邏輯加入註解
- 包含簡單和進階版本
- 展示實際使用場景
- 標明潛在問題

### 文件
- 解釋「為什麼」而不僅是「是什麼」
- 包含前置條件
- 加入疑難排解章節
- 連結到相關主題
- 保持對入門者友善

### JSON/YAML
- 使用適當的縮排（一致使用 2 或 4 個空格）
- 加入解釋配置的註解
- 包含驗證範例

### 圖表
- 盡量使用 Mermaid
- 保持圖表簡單且易讀
- 在圖表下方加入描述
- 連結到相關章節

## 提交指引

遵循慣例提交格式：
```
type(scope): description

[可選的正文]
```

類型：
- `feat`：新功能或範例
- `fix`：錯誤修正或更正
- `docs`：文件變更
- `refactor`：程式碼重構
- `style`：格式變更
- `test`：測試新增或變更
- `chore`：建置、依賴等

範例：
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 提交前

### 檢查清單
- [ ] 程式碼遵循專案風格和慣例
- [ ] 新範例包含清楚的文件
- [ ] README 檔案已更新（本地和根目錄）
- [ ] 沒有敏感資訊（API 金鑰、認證資訊）
- [ ] 範例已測試且可正常運作
- [ ] 連結已驗證且正確
- [ ] 檔案有適當的權限（腳本可執行）
- [ ] 提交訊息清楚且具描述性

### 本地測試
```bash
# 檢查檔案格式
pre-commit run --all-files

# 驗證連結是否有效（如適用）
# 手動使用 Claude Code 測試範例

# 審查你的變更
git diff

# 測試 EPUB 產生（如文件有變更）
uv run scripts/build_epub.py
```

## Pull Request 流程

1. **建立附帶清楚描述的 PR**：
   - 這新增/修正了什麼？
   - 為什麼需要？
   - 相關 issues（如果有）

2. **包含相關細節**：
   - 新功能？包含使用場景
   - 文件？解釋改善之處
   - 範例？展示前後對比

3. **連結到 issues**：
   - 使用 `Closes #123` 自動關閉相關 issues

4. **耐心等待審查**：
   - 維護者可能建議改善
   - 根據回饋進行迭代
   - 最終決定由維護者做出

## 程式碼審查流程

審查者會檢查：
- **正確性**：是否如描述般運作？
- **品質**：是否達到正式使用標準？
- **一致性**：是否遵循專案模式？
- **文件**：是否清楚且完整？
- **安全性**：是否有漏洞？

## 回報問題

### 錯誤回報
包含：
- Claude Code 版本
- 作業系統
- 重現步驟
- 預期行為
- 實際行為
- 截圖（如適用）

### 功能請求
包含：
- 使用場景或要解決的問題
- 建議的解決方案
- 你考慮過的替代方案
- 額外上下文

### 文件問題
包含：
- 什麼令人困惑或缺少
- 建議的改善
- 範例或參考

## 專案政策

### 敏感資訊
- 永不提交 API 金鑰、token 或認證資訊
- 在範例中使用佔位值
- 為配置檔案包含 `.env.example`
- 記錄所需的環境變數

### 程式碼品質
- 保持範例聚焦且可讀
- 避免過度工程化的解決方案
- 為非顯而易見的邏輯加入註解
- 提交前徹底測試

### 智慧財產權
- 原創內容由作者擁有
- 專案使用教育授權
- 尊重現有版權
- 在需要時提供歸屬

## 取得幫助

- **問題**：在 GitHub Issues 中開啟討論
- **一般幫助**：查閱現有文件
- **開發幫助**：參考類似範例
- **程式碼審查**：在 PR 中標記維護者

## 致謝

貢獻者會在以下地方得到認可：
- README.md 貢獻者區段
- GitHub 貢獻者頁面
- 提交歷史

## 安全

貢獻範例和文件時，請遵循安全程式碼實踐：

- **永不寫死機密或 API 金鑰** - 使用環境變數
- **警告安全影響** - 標明潛在風險
- **使用安全的預設值** - 預設啟用安全功能
- **驗證輸入** - 展示適當的輸入驗證和清理
- **包含安全注意事項** - 記錄安全注意事項

有關安全問題，請參閱 [SECURITY.md](SECURITY.md) 了解我們的漏洞回報流程。

## 行為準則

我們致力於提供一個友善且包容的社群。請閱讀 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 了解我們完整的社群標準。

簡而言之：
- 保持尊重和包容
- 優雅地接受回饋
- 幫助他人學習和成長
- 避免騷擾或歧視
- 向維護者回報問題

所有貢獻者都應遵守本準則，以善意和尊重對待彼此。

## 授權條款

透過為本專案做出貢獻，你同意你的貢獻將按 MIT 授權條款授權。詳見 [LICENSE](LICENSE) 檔案。

## 問題？

- 查閱 [README](README.md)
- 檢視 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- 參考現有範例
- 開啟 issue 進行討論

感謝你的貢獻！

