<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation Plugin

為您的專案提供全面的文件產生與維護。

## 功能

✅ API 文件產生
✅ README 建立與更新
✅ 文件同步
✅ 程式碼註解改善
✅ 範例產生

## 安裝

```bash
/plugin install documentation
```

## 包含內容

### Slash Commands
- `/generate-api-docs` - 產生 API 文件
- `/generate-readme` - 建立或更新 README
- `/sync-docs` - 將文件與程式碼變更同步
- `/validate-docs` - 驗證文件

### Subagents
- `api-documenter` - API 文件專家
- `code-commentator` - 程式碼註解改善
- `example-generator` - 程式碼範例建立

### 範本
- `api-endpoint.md` - API 端點文件範本
- `function-docs.md` - 函式文件範本
- `adr-template.md` - 架構決策記錄範本

### MCP Servers
- GitHub 整合，用於文件同步

## 使用方式

### 產生 API 文件
```
/generate-api-docs
```

### 建立 README
```
/generate-readme
```

### 同步文件
```
/sync-docs
```

### 驗證文件
```
/validate-docs
```

## 需求

- Claude Code 1.0+
- GitHub 存取權限（選用）

## 範例工作流程

```
使用者：/generate-api-docs

Claude：
1. 掃描 /src/api/ 中的所有 API 端點
2. 委派給 api-documenter subagent
3. 擷取函式簽名與 JSDoc
4. 依模組/端點組織
5. 使用 api-endpoint.md 範本
6. 產生完整的 Markdown 文件
7. 包含 curl、JavaScript 及 Python 範例

結果：
✅ API 文件已產生
📄 建立的檔案：
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 覆蓋率：23/23 個端點已記錄
```

## 範本使用

### API 端點範本
用於記錄 REST API 端點，包含完整範例。

### 函式文件範本
用於記錄個別函式/方法。

### ADR 範本
用於記錄架構決策。

## 組態設定

設定 GitHub token 以進行文件同步：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 最佳實踐

- 讓文件保持在程式碼附近
- 隨著程式碼變更更新文件
- 包含實用的範例
- 定期驗證
- 使用範本以確保一致性

