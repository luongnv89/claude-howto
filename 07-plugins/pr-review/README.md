<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review Plugin

完整的 PR 審查工作流程，包含安全性、測試與文件檢查。

## 功能

✅ 安全分析
✅ 測試覆蓋率檢查
✅ 文件驗證
✅ 程式碼品質評估
✅ 效能影響分析

## 安裝

```bash
/plugin install pr-review
```

## 包含內容

### Slash Commands
- `/review-pr` - 全面的 PR 審查
- `/check-security` - 專注安全性的審查
- `/check-tests` - 測試覆蓋率分析

### Subagents
- `security-reviewer` - 安全漏洞偵測
- `test-checker` - 測試覆蓋率分析
- `performance-analyzer` - 效能影響評估

### MCP Servers
- GitHub 整合，用於取得 PR 資料

### Hooks
- `pre-review.js` - 預審查驗證

## 使用方式

### 基本 PR 審查
```
/review-pr
```

### 僅安全檢查
```
/check-security
```

### 測試覆蓋率檢查
```
/check-tests
```

## 需求

- Claude Code 1.0+
- GitHub 存取權限
- Git 儲存庫

## 組態設定

設定 GitHub token：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 範例工作流程

```
使用者：/review-pr

Claude：
1. 執行預審查 hook（驗證 git 儲存庫）
2. 透過 GitHub MCP 取得 PR 資料
3. 委派安全審查給 security-reviewer subagent
4. 委派測試給 test-checker subagent
5. 委派效能給 performance-analyzer subagent
6. 綜合所有發現
7. 提供全面的審查報告

結果：
✅ 安全性：未發現重大問題
⚠️  測試：覆蓋率 65%，建議 80%+
✅ 效能：無顯著影響
📝 建議：新增邊界情況測試
```

