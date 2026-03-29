---
name: Setup CI/CD Pipeline
description: 實作 pre-commit hooks 與 GitHub Actions 以進行品質保證
tags: ci-cd, devops, automation
---

# 設定 CI/CD 管線

根據專案類型實作完整的 DevOps 品質關卡：

1. **分析專案**：偵測語言、框架、建置系統及現有工具
2. **配置 pre-commit hooks**，使用語言特定工具：
   - 格式化：Prettier/Black/gofmt/rustfmt 等
   - 靜態分析：ESLint/Ruff/golangci-lint/Clippy 等
   - 安全性：Bandit/gosec/cargo-audit/npm audit 等
   - 型別檢查：TypeScript/mypy/flow（若適用）
   - 測試：執行相關測試套件
3. **建立 GitHub Actions 工作流程** (.github/workflows/)：
   - 在 push/PR 時執行與 pre-commit 相同的檢查
   - 多版本/平台矩陣（若適用）
   - 建置與測試驗證
   - 部署步驟（若需要）
4. **驗證管線**：在本地測試、建立測試 PR、確認所有檢查通過

使用免費/開源工具。尊重現有配置。保持執行速度。

