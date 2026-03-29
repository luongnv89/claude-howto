<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints 與回溯

📍 Checkpoints（檢查點）
用途: 會話快照和回放
難度: ⭐⭐ 中級 | 時間: 45 分鐘

Checkpoints 讓您可以儲存對話狀態並回溯到 Claude Code 工作階段中的先前時間點。這對於探索不同方法、從錯誤中恢復或比較替代方案來說非常有價值。

## 概述

Checkpoints 讓您可以儲存對話狀態並回溯到先前的時間點，實現安全的實驗和探索多種方法。它們是對話狀態的快照，包括：
- 所有交換的訊息
- 已進行的檔案修改
- 工具使用歷史
- 工作階段上下文

Checkpoints 在探索不同方法、從錯誤中恢復或比較替代方案時非常有價值。

## 核心概念

| 概念 | 說明 |
|---------|-------------|
| **Checkpoint** | 對話狀態的快照，包括訊息、檔案和上下文 |
| **回溯** | 返回到先前的 checkpoint，捨棄後續的變更 |
| **分支點** | 從此 checkpoint 探索多種方法 |

## 存取 Checkpoints

您可以透過兩種主要方式存取和管理 checkpoints：

### 使用鍵盤快捷鍵
按兩次 `Esc`（`Esc` + `Esc`）開啟 checkpoint 介面並瀏覽已儲存的 checkpoints。

### 使用 Slash Command
使用 `/rewind` 命令（別名：`/checkpoint`）快速存取：

```bash
# 開啟回溯介面
/rewind

# 或使用別名
/checkpoint
```

## 回溯選項

當您回溯時，會出現五個選項的選單：

1. **還原程式碼與對話** -- 將檔案和訊息都回復到該 checkpoint
2. **還原對話** -- 僅回溯訊息，保持目前的程式碼不變
3. **還原程式碼** -- 僅回復檔案變更，保留完整的對話歷史
4. **從此處摘要** -- 將從此點開始的對話壓縮為 AI 產生的摘要，而非捨棄它。原始訊息保留在紀錄中。您可以選擇性地提供指示，將摘要聚焦在特定主題上。
5. **取消** -- 取消並返回目前狀態

## 自動 Checkpoints

Claude Code 會自動為您建立 checkpoints：

- **每次使用者提示** - 每次使用者輸入時建立新的 checkpoint
- **持久化** - Checkpoints 在工作階段間持續存在
- **自動清理** - Checkpoints 在 30 天後自動清理

這表示您可以隨時回溯到對話中的任何先前時間點，從幾分鐘前到幾天前。

## 使用案例

| 情境 | 工作流程 |
|----------|----------|
| **探索方法** | 儲存 → 嘗試 A → 儲存 → 回溯 → 嘗試 B → 比較 |
| **安全重構** | 儲存 → 重構 → 測試 → 若失敗：回溯 |
| **A/B 測試** | 儲存 → 設計 A → 儲存 → 回溯 → 設計 B → 比較 |
| **錯誤恢復** | 發現問題 → 回溯至最後的正常狀態 |

## 使用 Checkpoints

### 檢視與回溯

按兩次 `Esc` 或使用 `/rewind` 開啟 checkpoint 瀏覽器。您會看到所有可用 checkpoints 的列表及其時間戳記。選擇任一 checkpoint 即可回溯到該狀態。

### Checkpoint 詳情

每個 checkpoint 顯示：
- 建立的時間戳記
- 已修改的檔案
- 對話中的訊息數量
- 使用的工具

## 實用範例

### 範例 1：探索不同方法

```
使用者：讓我們在 API 中新增快取層

Claude：我將在您的 API 端點新增 Redis 快取...
[在 checkpoint A 進行變更]

使用者：其實，讓我們改試記憶體內快取

Claude：我將回溯以探索不同的方法...
[使用者按 Esc+Esc 並回溯到 checkpoint A]
[在 checkpoint B 實作記憶體內快取]

使用者：現在我可以比較兩種方法了
```

### 範例 2：從錯誤中恢復

```
使用者：重構認證模組以使用 JWT

Claude：我將重構認證模組...
[進行大量變更]

使用者：等等，這破壞了 OAuth 整合。讓我們回去。

Claude：我將幫您回溯到重構之前...
[使用者按 Esc+Esc 並選擇重構前的 checkpoint]

使用者：這次讓我們嘗試更保守的方法
```

### 範例 3：安全實驗

```
使用者：讓我們試著用函數式風格重寫這個
[在實驗前建立 checkpoint]

Claude：[進行實驗性變更]

使用者：測試失敗了。讓我們回溯。
[使用者按 Esc+Esc 並回溯到 checkpoint]

Claude：我已回溯變更。讓我們嘗試不同的方法。
```

### 範例 4：分支方法

```
使用者：我想比較兩種資料庫設計
[記下 checkpoint - 稱為「起始」]

Claude：我將建立第一個設計...
[實作結構 A]

使用者：現在讓我回去試第二種方法
[使用者按 Esc+Esc 並回溯到「起始」]

Claude：現在我將實作結構 B...
[實作結構 B]

使用者：太好了！現在我有兩個結構可以選擇
```

## Checkpoint 保留

Claude Code 自動管理您的 checkpoints：

- Checkpoints 在每次使用者提示時自動建立
- 舊的 checkpoints 保留最多 30 天
- Checkpoints 會自動清理以防止無限的儲存成長

## 工作流程模式

### 探索的分支策略

當探索多種方法時：

```
1. 從初始實作開始 → Checkpoint A
2. 嘗試方法 1 → Checkpoint B
3. 回溯到 Checkpoint A
4. 嘗試方法 2 → Checkpoint C
5. 比較 B 和 C 的結果
6. 選擇最佳方法並繼續
```

### 安全重構模式

進行重大變更時：

```
1. 目前狀態 → Checkpoint（自動）
2. 開始重構
3. 執行測試
4. 若測試通過 → 繼續工作
5. 若測試失敗 → 回溯並嘗試不同方法
```

## 最佳實踐

由於 checkpoints 是自動建立的，您可以專注於工作而不必擔心手動儲存狀態。但請記住以下實踐：

### 有效使用 Checkpoints

✅ **請這樣做：**
- 回溯前檢視可用的 checkpoints
- 當您想探索不同方向時使用回溯
- 保留 checkpoints 以比較不同方法
- 了解每個回溯選項的功能（還原程式碼與對話、還原對話、還原程式碼、或摘要）

❌ **不要這樣做：**
- 僅依賴 checkpoints 來保存程式碼
- 期望 checkpoints 追蹤外部檔案系統變更
- 用 checkpoints 代替 git commits

## 組態設定

您可以在設定中切換自動 checkpoints：

```json
{
  "autoCheckpoint": true
}
```

- `autoCheckpoint`：啟用或停用每次使用者提示時的自動 checkpoint 建立（預設：`true`）

## 限制

Checkpoints 有以下限制：

- **Bash 命令變更未追蹤** - 像 `rm`、`mv`、`cp` 等檔案系統操作不會被 checkpoints 捕捉
- **外部變更未追蹤** - 在 Claude Code 外部進行的變更（在您的編輯器、終端機等）不會被捕捉
- **不能取代版本控制** - 使用 git 進行永久的、可審計的程式碼變更

## 疑難排解

### 找不到 Checkpoints

**問題**：預期的 checkpoint 未找到

**解決方案**：
- 檢查 checkpoints 是否被清除
- 驗證設定中 `autoCheckpoint` 已啟用
- 檢查磁碟空間

### 回溯失敗

**問題**：無法回溯到 checkpoint

**解決方案**：
- 確保沒有未提交的變更衝突
- 檢查 checkpoint 是否損壞
- 嘗試回溯到不同的 checkpoint

## 與 Git 的整合

Checkpoints 補充（但不取代）git：

| 功能 | Git | Checkpoints |
|---------|-----|-------------|
| 範圍 | 檔案系統 | 對話 + 檔案 |
| 持久性 | 永久 | 基於工作階段 |
| 精細度 | Commits | 任意時間點 |
| 速度 | 較慢 | 即時 |
| 分享 | 是 | 有限 |

搭配使用：
1. 使用 checkpoints 進行快速實驗
2. 使用 git commits 保存已定案的變更
3. 在 git 操作前建立 checkpoint
4. 將成功的 checkpoint 狀態提交至 git

## 快速入門指南

### 基本工作流程

1. **正常工作** - Claude Code 自動建立 checkpoints
2. **想回去？** - 按兩次 `Esc` 或使用 `/rewind`
3. **選擇 checkpoint** - 從列表中選擇以回溯
4. **選擇還原內容** - 從還原程式碼與對話、還原對話、還原程式碼、從此處摘要、或取消中選擇
5. **繼續工作** - 您已回到該時間點

### 鍵盤快捷鍵

- **`Esc` + `Esc`** - 開啟 checkpoint 瀏覽器
- **`/rewind`** - 存取 checkpoints 的替代方式
- **`/checkpoint`** - `/rewind` 的別名

## 相關概念

- **[進階功能](../09-advanced-features/)** - 規劃模式及其他進階能力
- **[記憶管理](../02-memory/)** - 管理對話歷史與上下文
- **[Slash Commands](../01-slash-commands/)** - 使用者觸發的快捷命令
- **[Hooks](../06-hooks/)** - 事件驅動的自動化
- **[Plugins](../07-plugins/)** - 打包的擴充套件

## 額外資源

- [官方 Checkpoints 文件](https://code.claude.com/docs/en/checkpointing)
- [進階功能指南](../09-advanced-features/) - 延伸思考及其他能力

## 總結

Checkpoints 是 Claude Code 的自動功能，讓您可以安全地探索不同方法而不怕丟失工作。每次使用者提示都會自動建立新的 checkpoint，因此您可以回溯到工作階段中的任何先前時間點。

主要優勢：
- 無畏地實驗多種方法
- 快速從錯誤中恢復
- 並排比較不同解決方案
- 安全地與版本控制系統整合

請記住：checkpoints 不能取代 git。使用 checkpoints 進行快速實驗，使用 git 進行永久的程式碼變更。

