---
name: Expand Unit Tests
description: 透過針對未測試的分支和邊界案例來增加測試覆蓋率
tags: testing, coverage, unit-tests
---

# 擴展單元測試

根據專案的測試框架擴展現有單元測試：

1. **分析覆蓋率**：執行覆蓋率報告以識別未測試的分支、邊界案例和低覆蓋率區域
2. **識別缺口**：審查程式碼的邏輯分支、錯誤路徑、邊界條件、null/空值輸入
3. **撰寫測試**，使用專案的框架：
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **針對特定場景**：
   - 錯誤處理與例外
   - 邊界值（最小值/最大值、空值、null）
   - 邊界案例與特殊案例
   - 狀態轉換與副作用
5. **驗證改善**：再次執行覆蓋率，確認有可衡量的提升

僅呈現新的測試程式碼區塊。遵循現有的測試模式與命名慣例。

