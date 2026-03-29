<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 建置腳本

從 Claude How-To markdown 檔案建置 EPUB 電子書。

## 功能

- 依資料夾結構組織章節（01-slash-commands、02-memory 等）
- 透過 Kroki.io API 將 Mermaid 圖表算繪為 PNG 圖片
- 非同步並行擷取 — 平行算繪所有圖表
- 從專案 logo 產生封面圖片
- 將內部 markdown 連結轉換為 EPUB 章節參考
- 嚴格錯誤模式 — 若任何圖表無法算繪則失敗

## 需求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- 用於 Mermaid 圖表算繪的網路連線

## 快速入門

```bash
# 最簡單的方式 - uv 處理一切
uv run scripts/build_epub.py
```

## 開發設定

```bash
# 建立虛擬環境
uv venv

# 啟動並安裝依賴項
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# 執行測試
pytest scripts/tests/ -v

# 執行腳本
python scripts/build_epub.py
```

## 命令列選項

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

options:
  -h, --help            顯示此說明訊息並退出
  --root, -r ROOT       根目錄（預設：儲存庫根目錄）
  --output, -o OUTPUT   輸出路徑（預設：claude-howto-guide.epub）
  --verbose, -v         啟用詳細日誌
  --timeout TIMEOUT     API 逾時秒數（預設：30）
  --max-concurrent N    最大並行請求數（預設：10）
```

## 範例

```bash
# 以詳細輸出建置
uv run scripts/build_epub.py --verbose

# 自訂輸出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 限制並行請求（若被速率限制）
uv run scripts/build_epub.py --max-concurrent 5
```

## 輸出

在儲存庫根目錄建立 `claude-howto-guide.epub`。

EPUB 包含：
- 含專案 logo 的封面圖片
- 含巢狀章節的目錄
- 所有 markdown 內容轉換為 EPUB 相容的 HTML
- Mermaid 圖表算繪為 PNG 圖片

## 執行測試

```bash
# 使用虛擬環境
source .venv/bin/activate
pytest scripts/tests/ -v

# 或直接使用 uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## 依賴項

透過 PEP 723 內嵌腳本中繼資料管理：

| 套件 | 用途 |
|---------|---------|
| `ebooklib` | EPUB 產生 |
| `markdown` | Markdown 轉 HTML |
| `beautifulsoup4` | HTML 解析 |
| `httpx` | 非同步 HTTP 用戶端 |
| `pillow` | 封面圖片產生 |
| `tenacity` | 重試邏輯 |

## 疑難排解

**建置因網路錯誤而失敗**：檢查網路連線和 Kroki.io 狀態。嘗試 `--timeout 60`。

**速率限制**：使用 `--max-concurrent 3` 減少並行請求。

**缺少 logo**：若找不到 `claude-howto-logo.png`，腳本會產生純文字封面。
