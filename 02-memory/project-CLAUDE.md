# 專案配置

## 專案概覽
- **名稱**：電子商務平台
- **技術棧**：Node.js、PostgreSQL、React 18、Docker
- **團隊規模**：5 位開發人員
- **截止日期**：2025 年第四季

## 架構
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## 開發標準

### 程式碼風格
- 使用 Prettier 進行格式化
- 使用 ESLint 搭配 airbnb 設定
- 最大行寬：100 個字元
- 使用 2 個空格縮排

### 命名慣例
- **檔案**：kebab-case（user-controller.js）
- **類別**：PascalCase（UserService）
- **函式/變數**：camelCase（getUserById）
- **常數**：UPPER_SNAKE_CASE（API_BASE_URL）
- **資料庫表格**：snake_case（user_accounts）

### Git 工作流程
- 分支名稱：`feature/description` 或 `fix/description`
- 提交訊息：遵循 conventional commits
- 合併前需要 PR
- 所有 CI/CD 檢查必須通過
- 最少需要 1 個核准

### 測試要求
- 最低 80% 程式碼覆蓋率
- 所有關鍵路徑必須有測試
- 使用 Jest 進行單元測試
- 使用 Cypress 進行 E2E 測試
- 測試檔名：`*.test.ts` 或 `*.spec.ts`

### API 標準
- 僅使用 RESTful 端點
- JSON 請求/回應
- 正確使用 HTTP 狀態碼
- API 端點版本化：`/api/v1/`
- 所有端點附帶範例文件

### 資料庫
- 使用 migration 進行 schema 變更
- 絕不寫死憑證
- 使用連線池
- 開發環境啟用查詢記錄
- 需要定期備份

### 部署
- 基於 Docker 的部署
- Kubernetes 編排
- 藍綠部署策略
- 失敗時自動回滾
- 部署前執行資料庫 migration

## 常用指令

| 指令 | 用途 |
|---------|---------|
| `npm run dev` | 啟動開發伺服器 |
| `npm test` | 執行測試套件 |
| `npm run lint` | 檢查程式碼風格 |
| `npm run build` | 建置正式版本 |
| `npm run migrate` | 執行資料庫 migration |

## 團隊聯絡人
- 技術主管：Sarah Chen（@sarah.chen）
- 產品經理：Mike Johnson（@mike.j）
- DevOps：Alex Kim（@alex.k）

## 已知問題與解決方案
- PostgreSQL 連線池在尖峰時段限制為 20
- 解決方案：實作查詢佇列
- Safari 14 與 async generators 的相容性問題
- 解決方案：使用 Babel 轉譯器

## 相關專案
- 分析儀表板：`/projects/analytics`
- 行動應用程式：`/projects/mobile`
- 管理面板：`/projects/admin`

