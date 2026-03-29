---
name: blog-draft
description: 從構想和資源起草部落格文章。在使用者想要撰寫部落格文章、從研究建立內容或起草文章時使用。引導完成研究、腦力激盪、大綱和帶有版本控制的迭代起草過程。
---

## 使用者輸入

```text
$ARGUMENTS
```

你**必須**在繼續之前考慮使用者輸入。使用者應提供：
- **構想/主題**：部落格文章的主要概念或主題
- **資源**：URL、檔案或研究參考（選填但建議提供）
- **目標受眾**：部落格文章的對象（選填）
- **語氣/風格**：正式、隨意、技術性等（選填）

**重要**：如果使用者請求更新**現有部落格文章**，跳過步驟 0-8，直接從**步驟 9** 開始。先閱讀現有草稿檔案，然後進行迭代過程。

## 執行流程

按順序遵循這些步驟。**不要跳過步驟或在指定處未獲得使用者批准就繼續。**

### 步驟 0：建立專案資料夾

1. 使用格式產生資料夾名稱：`YYYY-MM-DD-short-topic-name`
   - 使用今天的日期
   - 從主題建立簡短的、URL 友善的 slug（小寫、連字號、最多 5 個單字）

2. 建立資料夾結構：
   ```
   blog-posts/
   └── YYYY-MM-DD-short-topic-name/
       └── resources/
   ```

3. 在繼續之前向使用者確認資料夾建立。

### 步驟 1：研究與資源收集

1. 在部落格文章目錄中建立 `resources/` 子資料夾

2. 對於每個提供的資源：
   - **URL**：擷取並將關鍵資訊儲存到 `resources/` 作為 markdown 檔案
   - **檔案**：閱讀並在 `resources/` 中摘要
   - **主題**：使用網路搜尋收集最新資訊

3. 為每個資源在 `resources/` 中建立摘要檔案：
   - `resources/source-1-[short-name].md`
   - `resources/source-2-[short-name].md`
   - 以此類推

4. 每份摘要應包含：
   ```markdown
   # Source: [Title/URL]

   ## Key Points
   - Point 1
   - Point 2

   ## Relevant Quotes/Data
   - Quote or statistic 1
   - Quote or statistic 2

   ## How This Relates to Topic
   Brief explanation of relevance
   ```

5. 向使用者呈現研究摘要。

### 步驟 2：腦力激盪與澄清

1. 根據構想和研究的資源，呈現：
   - 從研究中識別的**主要主題**
   - 部落格文章的**潛在切入角度**
   - 應涵蓋的**關鍵要點**
   - 需要澄清的資訊**缺口**

2. 提出澄清問題：
   - 你希望讀者獲得的主要收穫是什麼？
   - 研究中有特定的要點你想強調嗎？
   - 目標篇幅是多少？（短：500-800 字，中：1000-1500，長：2000+）
   - 有任何你想排除的要點嗎？

3. **在繼續之前等待使用者回覆。**

### 步驟 3：提出大綱

1. 建立結構化大綱，包含：

   ```markdown
   # Blog Post Outline: [Title]

   ## Meta Information
   - **Target Audience**: [who]
   - **Tone**: [style]
   - **Target Length**: [word count]
   - **Main Takeaway**: [key message]

   ## Proposed Structure

   ### Hook/Introduction
   - Opening hook idea
   - Context setting
   - Thesis statement

   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Supporting evidence from [source]

   ### Section 2: [Title]
   - Key point A
   - Key point B

   [Continue for all sections...]

   ### Conclusion
   - Summary of key points
   - Call to action or final thought

   ## Sources to Cite
   - Source 1
   - Source 2
   ```

2. 向使用者呈現大綱並**請求批准或修改**。

### 步驟 4：儲存已批准的大綱

1. 使用者批准大綱後，將其儲存為部落格文章資料夾中的 `OUTLINE.md`。

2. 確認大綱已儲存。

### 步驟 5：提交大綱（如果在 git 倉庫中）

1. 檢查目前目錄是否為 git 倉庫。

2. 如果是：
   - 暫存新檔案：部落格文章資料夾、資源和 OUTLINE.md
   - 以訊息建立提交：`docs: Add outline for blog post - [topic-name]`
   - 推送至遠端

3. 如果不是 git 倉庫，跳過此步驟並通知使用者。

### 步驟 6：撰寫草稿

1. 根據已批准的大綱，撰寫完整的部落格文章草稿。

2. 精確遵循 OUTLINE.md 中的結構。

3. 包含：
   - 帶有吸引眼球元素的引人入勝的引言
   - 清晰的章節標題
   - 來自研究的支持證據和範例
   - 章節之間的流暢過渡
   - 帶有收穫的有力結論
   - **引用**：所有比較、統計、數據和事實聲明必須引用原始來源

4. 將草稿儲存為部落格文章資料夾中的 `draft-v0.1.md`。

5. 格式：
   ```markdown
   # [Blog Post Title]

   *[Optional: subtitle or tagline]*

   [Full content with inline citations...]

   ---

   ## References
   - [1] Source 1 Title - URL or Citation
   - [2] Source 2 Title - URL or Citation
   - [3] Source 3 Title - URL or Citation
   ```

6. **引用要求**：
   - 每個數據點、統計或比較必須有行內引用
   - 使用編號引用 [1]、[2] 等，或具名引用 [Source Name]
   - 將引用連結到結尾的參考文獻章節
   - 範例："Studies show that 65% of developers prefer TypeScript [1]"
   - 範例："React outperforms Vue in rendering speed by 20% [React Benchmarks 2024]"

### 步驟 7：提交草稿（如果在 git 倉庫中）

1. 檢查是否在 git 倉庫中。

2. 如果是：
   - 暫存草稿檔案
   - 以訊息建立提交：`docs: Add draft v0.1 for blog post - [topic-name]`
   - 推送至遠端

3. 如果不是 git 倉庫，跳過並通知使用者。

### 步驟 8：呈現草稿供審查

1. 向使用者呈現草稿內容。

2. 請求回饋：
   - 整體印象？
   - 需要擴充或縮減的章節？
   - 需要調整的語氣？
   - 缺少的資訊？
   - 特定的編輯或重寫？

3. **等待使用者回覆。**

### 步驟 9：迭代或定稿

**如果使用者請求變更：**
1. 記錄所有請求的修改
2. 回到步驟 6 並進行以下調整：
   - 遞增版本號碼（v0.2、v0.3 等）
   - 納入所有回饋
   - 儲存為 `draft-v[X.Y].md`
   - 重複步驟 7-8

**如果使用者批准：**
1. 確認最終草稿版本
2. 如果使用者請求，可選擇性地重新命名為 `final.md`
3. 摘要部落格文章建立過程：
   - 建立的總版本數
   - 版本之間的主要變更
   - 最終字數
   - 建立的檔案

## 版本追蹤

所有草稿以遞增版本保存：
- `draft-v0.1.md` - 初始草稿
- `draft-v0.2.md` - 第一輪回饋後
- `draft-v0.3.md` - 第二輪回饋後
- 以此類推

這允許追蹤部落格文章的演變過程，並在需要時回退。

## 輸出檔案結構

```
blog-posts/
└── YYYY-MM-DD-topic-name/
    ├── resources/
    │   ├── source-1-name.md
    │   ├── source-2-name.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (if iterations)
    └── draft-v0.3.md (if more iterations)
```

## 品質提示

- **開場**：以問題、驚人事實或可共感的場景開始
- **流暢度**：每段應與下一段連接
- **證據**：以研究數據支持論點
- **引用**：務必引用來源：
  - 所有統計和數據點（例如 "According to [Source], 75% of..."）
  - 產品、服務或方法之間的比較（例如 "X performs 2x faster than Y [Source]"）
  - 關於市場趨勢、研究發現或基準的事實聲明
  - 使用行內引用格式：[Source Name] 或 [Author, Year]
- **語氣**：全文保持一致的語氣
- **篇幅**：遵守目標字數
- **可讀性**：使用簡短段落，適當時使用項目符號
- **行動呼籲**：以明確的行動呼籲或發人深省的問題結尾

## 備註

- 在標示的檢查點始終等待使用者批准
- 保留所有草稿版本以供歷史記錄
- 提供 URL 時使用網路搜尋獲取最新資訊
- 如果資源不足，請向使用者索取更多或建議額外研究
- 根據目標受眾調整語氣（技術性、一般性、商業性等）
