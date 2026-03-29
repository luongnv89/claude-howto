<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

⚡ Hooks（鉤子）
用途: 事件驅動自動化
難度: ⭐⭐ 中級 | 時間: 1 小時

Hooks 是在 Claude Code 工作階段中特定事件發生時自動執行的腳本。它們實現自動化、驗證、權限管理和自訂工作流程。

## 概述

Hooks 是在 Claude Code 中特定事件發生時自動執行的動作（shell 命令、HTTP webhook、LLM 提示或 subagent 評估）。它們透過 JSON 輸入接收資料，並透過退出碼和 JSON 輸出傳達結果。

**主要功能：**
- 事件驅動的自動化
- 基於 JSON 的輸入/輸出
- 支援 command、prompt、HTTP 和 agent hook 類型
- 工具特定 hooks 的模式比對

## 組態設定

Hooks 在設定檔案中以特定結構設定：

- `~/.claude/settings.json` - 使用者設定（所有專案）
- `.claude/settings.json` - 專案設定（可共享、已提交）
- `.claude/settings.local.json` - 本地專案設定（未提交）
- 受管策略 - 全組織設定
- Plugin `hooks/hooks.json` - Plugin 範圍的 hooks
- Skill/Agent frontmatter - 元件生命週期 hooks

### 基本組態結構

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**主要欄位：**

| 欄位 | 說明 | 範例 |
|-------|-------------|---------|
| `matcher` | 比對工具名稱的模式（區分大小寫） | `"Write"`、`"Edit\|Write"`、`"*"` |
| `hooks` | Hook 定義的陣列 | `[{ "type": "command", ... }]` |
| `type` | Hook 類型：`"command"`（bash）、`"prompt"`（LLM）、`"http"`（webhook）或 `"agent"`（subagent） | `"command"` |
| `command` | 要執行的 shell 命令 | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | 可選的逾時秒數（預設 60） | `30` |
| `once` | 若為 `true`，每個工作階段只執行一次 hook | `true` |

### Matcher 模式

| 模式 | 說明 | 範例 |
|---------|-------------|---------|
| 精確字串 | 比對特定工具 | `"Write"` |
| 正規表達式模式 | 比對多個工具 | `"Edit\|Write"` |
| 萬用字元 | 比對所有工具 | `"*"` 或 `""` |
| MCP 工具 | 伺服器和工具模式 | `"mcp__memory__.*"` |

## Hook 類型

Claude Code 支援四種 hook 類型：

### Command Hooks

預設 hook 類型。執行 shell 命令，透過 JSON stdin/stdout 和退出碼進行通訊。

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP Hooks

> 在 v2.1.63 中新增。

接收與 command hooks 相同 JSON 輸入的遠端 webhook 端點。HTTP hooks 向 URL POST JSON 並接收 JSON 回應。啟用沙箱時，HTTP hooks 通過沙箱路由。URL 中的環境變數插值需要明確的 `allowedEnvVars` 清單以確保安全。

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://my-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**關鍵屬性：**
- `"type": "http"` -- 標識為 HTTP hook
- `"url"` -- webhook 端點 URL
- 啟用沙箱時通過沙箱路由
- URL 中的任何環境變數插值需要明確的 `allowedEnvVars` 清單

### Prompt Hooks

LLM 評估的提示，hook 內容是 Claude 評估的提示。主要用於 `Stop` 和 `SubagentStop` 事件，進行智慧任務完成檢查。

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM 評估提示並返回結構化決定（詳見[基於提示的 Hooks](#基於提示的-hooks)）。

### Agent Hooks

基於 subagent 的驗證 hooks，產生專門的 agent 來評估條件或執行複雜檢查。與 prompt hooks（單輪 LLM 評估）不同，agent hooks 可以使用工具並執行多步驟推理。

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**關鍵屬性：**
- `"type": "agent"` -- 標識為 agent hook
- `"prompt"` -- subagent 的任務描述
- Agent 可以使用工具（Read、Grep、Bash 等）執行評估
- 返回類似 prompt hooks 的結構化決定

## Hook 事件

Claude Code 支援 **25 個 hook 事件**：

| 事件 | 觸發時機 | Matcher 輸入 | 可阻擋 | 常見用途 |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | 工作階段開始/恢復/清除/壓縮 | startup/resume/clear/compact | 否 | 環境設定 |
| **InstructionsLoaded** | CLAUDE.md 或規則檔案載入後 | （無） | 否 | 修改/篩選指令 |
| **UserPromptSubmit** | 使用者提交提示 | （無） | 是 | 驗證提示 |
| **PreToolUse** | 工具執行前 | 工具名稱 | 是（允許/拒絕/詢問） | 驗證、修改輸入 |
| **PermissionRequest** | 顯示權限對話框 | 工具名稱 | 是 | 自動核准/拒絕 |
| **PostToolUse** | 工具成功執行後 | 工具名稱 | 否 | 新增上下文、回饋 |
| **PostToolUseFailure** | 工具執行失敗 | 工具名稱 | 否 | 錯誤處理、記錄 |
| **Notification** | 發送通知 | 通知類型 | 否 | 自訂通知 |
| **SubagentStart** | Subagent 產生 | Agent 類型名稱 | 否 | Subagent 設定 |
| **SubagentStop** | Subagent 完成 | Agent 類型名稱 | 是 | Subagent 驗證 |
| **Stop** | Claude 完成回應 | （無） | 是 | 任務完成檢查 |
| **StopFailure** | API 錯誤結束回合 | （無） | 否 | 錯誤恢復、記錄 |
| **TeammateIdle** | Agent 團隊的隊友閒置 | （無） | 是 | 隊友協調 |
| **TaskCompleted** | 任務標記為完成 | （無） | 是 | 任務後動作 |
| **TaskCreated** | 透過 TaskCreate 建立任務 | （無） | 否 | 任務追蹤、記錄 |
| **ConfigChange** | 組態檔案變更 | （無） | 是（策略除外） | 回應組態更新 |
| **CwdChanged** | 工作目錄變更 | （無） | 否 | 目錄特定設定 |
| **FileChanged** | 監控的檔案變更 | （無） | 否 | 檔案監控、重建 |
| **PreCompact** | 上下文壓縮前 | manual/auto | 否 | 壓縮前動作 |
| **PostCompact** | 壓縮完成後 | （無） | 否 | 壓縮後動作 |
| **WorktreeCreate** | 正在建立 Worktree | （無） | 是（路徑返回） | Worktree 初始化 |
| **WorktreeRemove** | 正在移除 Worktree | （無） | 否 | Worktree 清理 |
| **Elicitation** | MCP 伺服器請求使用者輸入 | （無） | 是 | 輸入驗證 |
| **ElicitationResult** | 使用者回應引出 | （無） | 是 | 回應處理 |
| **SessionEnd** | 工作階段終止 | （無） | 否 | 清理、最終記錄 |

### PreToolUse

在 Claude 建立工具參數之後、處理之前執行。用於驗證或修改工具輸入。

**組態：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**常見 matchers：** `Task`、`Bash`、`Glob`、`Grep`、`Read`、`Edit`、`Write`、`WebFetch`、`WebSearch`

**輸出控制：**
- `permissionDecision`：`"allow"`、`"deny"` 或 `"ask"`
- `permissionDecisionReason`：決定的說明
- `updatedInput`：修改後的工具輸入參數

### PostToolUse

在工具完成後立即執行。用於驗證、記錄或向 Claude 提供上下文回饋。

**組態：**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**輸出控制：**
- `"block"` 決定會提示 Claude 並附帶回饋
- `additionalContext`：為 Claude 新增的上下文

### UserPromptSubmit

在使用者提交提示時執行，在 Claude 處理之前。

**組態：**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**輸出控制：**
- `decision`：`"block"` 阻止處理
- `reason`：被阻擋時的說明
- `additionalContext`：新增至提示的上下文

### Stop 和 SubagentStop

在 Claude 完成回應（Stop）或 subagent 完成（SubagentStop）時執行。支援基於提示的評估以進行智慧任務完成檢查。

**額外輸入欄位：** `Stop` 和 `SubagentStop` hooks 在其 JSON 輸入中都會收到 `last_assistant_message` 欄位，包含 Claude 或 subagent 停止前的最後訊息。這對於評估任務完成很有用。

**組態：**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude completed all requested tasks.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SubagentStart

在 subagent 開始執行時執行。Matcher 輸入是 agent 類型名稱，允許 hooks 針對特定 subagent 類型。

**組態：**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

在工作階段開始或恢復時執行。可以持久化環境變數。

**Matchers：** `startup`、`resume`、`clear`、`compact`

**特殊功能：** 使用 `CLAUDE_ENV_FILE` 持久化環境變數（也可用於 `CwdChanged` 和 `FileChanged` hooks）：

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

在工作階段結束時執行以進行清理或最終記錄。無法阻擋終止。

**Reason 欄位值：**
- `clear` - 使用者清除了工作階段
- `logout` - 使用者登出
- `prompt_input_exit` - 使用者透過提示輸入退出
- `other` - 其他原因

**組態：**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### Notification 事件

通知事件的更新 matchers：
- `permission_prompt` - 權限請求通知
- `idle_prompt` - 閒置狀態通知
- `auth_success` - 認證成功
- `elicitation_dialog` - 向使用者顯示的對話框

## 元件範圍 Hooks

Hooks 可以在其 frontmatter 中附加到特定元件（skills、agents、commands）：

**在 SKILL.md、agent.md 或 command.md 中：**

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # 每個工作階段只執行一次
---
```

**元件 hooks 支援的事件：** `PreToolUse`、`PostToolUse`、`Stop`

這允許在使用 hooks 的元件中直接定義它們，將相關程式碼保持在一起。

### Subagent Frontmatter 中的 Hooks

當 `Stop` hook 在 subagent 的 frontmatter 中定義時，它會自動轉換為範圍限定在該 subagent 的 `SubagentStop` hook。這確保 stop hook 僅在該特定 subagent 完成時觸發，而不是在主工作階段停止時。

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # 上面的 Stop hook 會自動轉換為此 subagent 的 SubagentStop
---
```

## PermissionRequest 事件

以自訂輸出格式處理權限請求：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Custom message",
      "interrupt": false
    }
  }
}
```

## Hook 輸入與輸出

### JSON 輸入（透過 stdin）

所有 hooks 透過 stdin 接收 JSON 輸入：

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "main",
  "worktree": "/path/to/worktree"
}
```

**常見欄位：**

| 欄位 | 說明 |
|-------|-------------|
| `session_id` | 唯一的工作階段識別碼 |
| `transcript_path` | 對話紀錄檔案的路徑 |
| `cwd` | 目前工作目錄 |
| `hook_event_name` | 觸發 hook 的事件名稱 |
| `agent_id` | 執行此 hook 的 agent 識別碼 |
| `agent_type` | Agent 類型（`"main"`、subagent 類型名稱等） |
| `worktree` | git worktree 的路徑（若 agent 在其中執行） |

### 退出碼

| 退出碼 | 意義 | 行為 |
|-----------|---------|----------|
| **0** | 成功 | 繼續，解析 JSON stdout |
| **2** | 阻擋錯誤 | 阻擋操作，stderr 顯示為錯誤 |
| **其他** | 非阻擋錯誤 | 繼續，stderr 在詳細模式中顯示 |

### JSON 輸出（stdout，退出碼 0）

```json
{
  "continue": true,
  "stopReason": "Optional message if stopping",
  "suppressOutput": false,
  "systemMessage": "Optional warning message",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

## 環境變數

| 變數 | 可用性 | 說明 |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | 所有 hooks | 專案根目錄的絕對路徑 |
| `CLAUDE_ENV_FILE` | SessionStart、CwdChanged、FileChanged | 用於持久化環境變數的檔案路徑 |
| `CLAUDE_CODE_REMOTE` | 所有 hooks | 在遠端環境中執行時為 `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin hooks | Plugin 目錄的路徑 |
| `${CLAUDE_PLUGIN_DATA}` | Plugin hooks | Plugin 資料目錄的路徑 |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hooks | SessionEnd hooks 的可設定逾時毫秒數（覆寫預設值） |

## 基於提示的 Hooks

對於 `Stop` 和 `SubagentStop` 事件，您可以使用基於 LLM 的評估：

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all tasks are complete. Return your decision.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**LLM 回應結構：**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## 範例

### 範例 1：Bash 命令驗證器（PreToolUse）

**檔案：** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Blocking dangerous rm -rf / command"),
    (r"\bsudo\s+rm", "Blocking sudo rm command"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Exit 2 = blocking error

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**組態：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### 範例 2：安全掃描器（PostToolUse）

**檔案：** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Security warnings for {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 範例 3：自動格式化程式碼（PostToolUse）

**檔案：** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# 從 stdin 讀取 JSON
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# 根據副檔名格式化
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### 範例 4：提示驗證器（UserPromptSubmit）

**檔案：** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Dangerous: database deletion"),
    (r"rm\s+-rf\s+/", "Dangerous: root deletion"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Blocked: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 範例 5：智慧 Stop Hook（基於提示）

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if Claude completed all requested tasks. Check: 1) Were all files created/modified? 2) Were there unresolved errors? If incomplete, explain what's missing.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 範例 6：上下文使用追蹤器（Hook 配對）

使用 `UserPromptSubmit`（訊息前）和 `Stop`（回應後）hooks 配對追蹤每個請求的 token 消耗。

**檔案：** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - 追蹤每個請求的 token 消耗。

使用 UserPromptSubmit 作為「訊息前」hook，Stop 作為「回應後」hook，
計算每個請求的 token 使用差異。

Token 計算方法：
1. 字元估算（預設）：約 4 個字元/token，無依賴項
2. tiktoken（可選）：更精確（約 90-95%），需要：pip install tiktoken
"""
import json
import os
import sys
import tempfile

# 組態
CONTEXT_LIMIT = 128000  # Claude 的上下文視窗（根據您的模型調整）
USE_TIKTOKEN = False    # 若已安裝 tiktoken 則設為 True 以獲得更好的準確度


def get_state_file(session_id: str) -> str:
    """取得用於儲存訊息前 token 計數的暫存檔案路徑，按工作階段隔離。"""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    計算文字中的 tokens。

    若可用則使用 tiktoken 的 p50k_base 編碼（約 90-95% 準確度），
    否則退回字元估算（約 80-90% 準確度）。
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # 退回估算

    # 基於字元的估算：英文約 4 個字元/token
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """讀取並串接紀錄檔案中的所有內容。"""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # 從各種訊息格式中擷取文字內容
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """訊息前 hook：在請求前儲存目前的 token 計數。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 儲存至暫存檔案以供後續比較
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """回應後 hook：計算差異並回報使用量。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 載入訊息前計數
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # 計算差異
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # 回報使用量
    method = "tiktoken" if USE_TIKTOKEN else "estimated"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% used, ~{remaining:,} remaining)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"This request: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**組態：**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**運作方式：**
1. `UserPromptSubmit` 在您的提示處理前觸發 - 儲存目前的 token 計數
2. `Stop` 在 Claude 回應後觸發 - 計算差異並回報使用量
3. 每個工作階段透過暫存檔案名稱中的 `session_id` 隔離

**Token 計算方法：**

| 方法 | 準確度 | 依賴項 | 速度 |
|--------|----------|--------------|-------|
| 字元估算 | 約 80-90% | 無 | <1ms |
| tiktoken (p50k_base) | 約 90-95% | `pip install tiktoken` | <10ms |

> **注意：** Anthropic 尚未發布官方的離線分詞器。兩種方法都是近似值。紀錄包括使用者提示、Claude 的回應和工具輸出，但不包括系統提示或內部上下文。

### 範例 7：Auto-Adapt 模式（PostToolUse）

自動從您的工具核准中學習並更新 `~/.claude/settings.json` 權限。每次您接受工具執行時，hook 會將命令概括為可重用的權限規則 — 這樣您就不必再次核准同類型的命令。危險/破壞性命令**永遠不會**被記住。

首次執行時，它會在您的組態中植入與 auto-mode 等效的基準權限（讀取/寫入檔案、git 操作、套件管理器、常用 CLI 工具）。

**檔案：** `.claude/hooks/auto-adapt-mode.py`

```python
#!/usr/bin/env python3
"""
auto-adapt-mode：從使用者的工具核准中學習並更新 Claude 組態。

Hook 類型：PostToolUse
事件：在工具成功執行後觸發（表示使用者已核准）
"""

import json
import os
import sys
import re
from pathlib import Path

SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
LOG_PATH = Path.home() / ".claude" / "auto-adapt-mode.log"

# Auto-mode 基準：安全的、本地的、可逆的操作
AUTO_MODE_BASELINE = [
    "Read(*)", "Edit(*)", "Write(*)", "Glob(*)", "Grep(*)",
    "Bash(git status:*)", "Bash(git log:*)", "Bash(git diff:*)",
    "Bash(git add:*)", "Bash(git commit:*)", "Bash(git checkout:*)",
    "Bash(npm install:*)", "Bash(npm test:*)", "Bash(npm run:*)",
    "Bash(pip install:*)", "Bash(pytest:*)",
    "Bash(ls:*)", "Bash(cat:*)", "Bash(find:*)", "Bash(mkdir:*)",
    "Bash(cp:*)", "Bash(mv:*)", "Bash(chmod:*)",
    "Bash(gh pr view:*)", "Bash(gh issue list:*)",
    "Agent(*)", "Skill(*)", "WebSearch(*)", "WebFetch(*)",
    # ...（完整清單包含 70+ 個安全模式）
]

# 永遠不會被自動記住的命令
DANGEROUS_PATTERNS = [
    r"rm\s+(-[a-zA-Z]*r[a-zA-Z]*|--recursive)",   # rm -rf
    r"git\s+push\s+(-[a-zA-Z]*f|--force)",          # force push
    r"git\s+reset\s+--hard",                         # hard reset
    r"DROP\s+(TABLE|DATABASE)",                       # SQL 破壞性
    r"curl\s+.*\|\s*(bash|sh)",                       # 管道至 shell
    r"sudo\b",                                        # 權限提升
    r"docker\s+(rm|rmi|system\s+prune)",              # 容器破壞性
    r"kubectl\s+delete",                              # k8s 破壞性
    r"terraform\s+destroy",                           # 基礎設施破壞性
    r"npm\s+publish",                                 # 不可逆的發布
    r"deploy\s+.*prod",                               # 正式環境部署
    # ...（完整清單包含 25+ 個模式）
]


def is_dangerous_command(command: str) -> bool:
    """檢查 bash 命令是否匹配任何危險模式。"""
    return any(re.search(p, command, re.IGNORECASE) for p in DANGEROUS_PATTERNS)


def generalize_tool_permission(tool_name: str, tool_input: dict) -> str | None:
    """將特定工具呼叫轉換為概括的權限規則。"""
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if not command or is_dangerous_command(command):
            return None
        parts = command.strip().split()
        base = parts[0]
        # 複合命令："git push" -> "Bash(git push:*)"
        compound = ["git", "npm", "npx", "pip", "cargo", "go", "gh", "python3"]
        if base in compound and len(parts) > 1:
            sub = parts[1]
            if sub.lower() in {"rm", "delete", "destroy", "publish"}:
                return None
            return f"Bash({base} {sub}:*)"
        return f"Bash({base}:*)"
    elif tool_name == "Bash":  # 永遠不允許通用 Bash(*)
        return None
    else:
        return f"{tool_name}(*)"


def main():
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})
    if not tool_name:
        sys.exit(0)

    # 載入設定、確保基準、若安全則新增規則
    settings = json.load(open(SETTINGS_PATH)) if SETTINGS_PATH.exists() else {}
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])

    # 首次執行時植入基準
    marker = Path.home() / ".claude" / ".auto-adapt-mode-initialized"
    if not marker.exists():
        existing = set(allow)
        for rule in AUTO_MODE_BASELINE:
            if rule not in existing:
                allow.append(rule)
        marker.touch()

    # 概括並新增新規則
    rule = generalize_tool_permission(tool_name, tool_input)
    if rule and rule not in allow:
        allow.append(rule)
        with open(SETTINGS_PATH, "w") as f:
            json.dump(settings, f, indent=2)
            f.write("\n")

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**組態：**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/auto-adapt-mode.py\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

**運作方式：**
1. `PostToolUse` 在**每次**成功工具執行後觸發（表示您已核准）
2. Hook 擷取工具名稱和輸入，然後概括為權限規則
3. 複合命令如 `git push origin main` 變成 `Bash(git push:*)` — 匹配任何 `git push` 變體
4. 規則被新增至 `~/.claude/settings.json` → `permissions.allow`（若尚未存在）
5. 首次執行時植入約 70 個 auto-mode 等效基準權限

**安全保證：**
- 危險命令（force push、rm -rf、sudo、DROP TABLE 等）**永遠不會**被記住
- 不可逆操作（npm publish、terraform destroy、正式環境部署）**總是**被阻擋
- `deny` 清單中的命令永遠不會被覆寫
- Hook 永遠不會阻擋工具執行（總是以 0 退出）
- `~/.claude/auto-adapt-mode.log` 的日誌檔案追蹤所有決定以供稽核

**概括範例：**

| 您核准的 | 新增的規則 | 涵蓋 |
|-------------|-----------|--------|
| `git push origin main` | `Bash(git push:*)` | 所有 git push 變體 |
| `npm run build` | `Bash(npm run:*)` | 所有 npm 腳本 |
| `ls -la src/` | `Bash(ls:*)` | 所有 ls 呼叫 |
| `rm -rf /tmp/test` | *（被阻擋）* | 永遠不會被記住 |
| `git push --force` | *（被阻擋）* | 永遠不會被記住 |
| `Write` 工具 | `Write(*)` | 所有檔案寫入 |

> **提示：** 刪除 `~/.claude/.auto-adapt-mode-initialized` 以重新植入基準權限。檢查 `~/.claude/auto-adapt-mode.log` 以稽核新增了哪些規則以及哪些被阻擋。

## Plugin Hooks

Plugins 可以在其 `hooks/hooks.json` 檔案中包含 hooks：

**檔案：** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**Plugin Hooks 中的環境變數：**
- `${CLAUDE_PLUGIN_ROOT}` - Plugin 目錄的路徑
- `${CLAUDE_PLUGIN_DATA}` - Plugin 資料目錄的路徑

這允許 plugins 包含自訂的驗證和自動化 hooks。

## MCP 工具 Hooks

MCP 工具遵循 `mcp__<server>__<tool>` 的模式：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Memory operation logged\"}'"
          }
        ]
      }
    ]
  }
}
```

## 安全考量

### 免責聲明

**使用風險自負**：Hooks 執行任意 shell 命令。您需自行負責：
- 您設定的命令
- 檔案存取/修改權限
- 潛在的資料遺失或系統損壞
- 在安全環境中測試 hooks 後再用於生產環境

### 安全注意事項

- **需要工作區信任：** `statusLine` 和 `fileSuggestion` hook 輸出命令現在需要工作區信任接受後才會生效。
- **HTTP hooks 和環境變數：** HTTP hooks 需要明確的 `allowedEnvVars` 清單才能在 URL 中使用環境變數插值。這防止敏感環境變數意外洩漏至遠端端點。
- **受管設定層級：** `disableAllHooks` 設定現在遵循受管設定層級，表示組織級設定可以強制執行個別使用者無法覆寫的 hook 停用。

### 最佳實踐

| 建議做法 | 不建議做法 |
|-----|-------|
| 驗證並清理所有輸入 | 盲目信任輸入資料 |
| 引用 shell 變數：`"$VAR"` | 使用未引用的：`$VAR` |
| 阻擋路徑遍歷（`..`） | 允許任意路徑 |
| 使用 `$CLAUDE_PROJECT_DIR` 的絕對路徑 | 硬編碼路徑 |
| 跳過敏感檔案（`.env`、`.git/`、金鑰） | 處理所有檔案 |
| 先獨立測試 hooks | 部署未測試的 hooks |
| 對 HTTP hooks 使用明確的 `allowedEnvVars` | 將所有環境變數暴露給 webhooks |

## 除錯

### 啟用除錯模式

使用 debug 旗標執行 Claude 以獲得詳細的 hook 日誌：

```bash
claude --debug
```

### 詳細模式

在 Claude Code 中使用 `Ctrl+O` 啟用詳細模式並查看 hook 執行進度。

### 獨立測試 Hooks

```bash
# 使用範例 JSON 輸入測試
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# 檢查退出碼
echo $?
```

## 完整組態範例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify all tasks are complete before stopping.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Hook 執行細節

| 方面 | 行為 |
|--------|----------|
| **逾時** | 預設 60 秒，每個命令可設定 |
| **並行化** | 所有匹配的 hooks 並行執行 |
| **去重** | 相同的 hook 命令會去重 |
| **環境** | 在目前目錄中使用 Claude Code 的環境執行 |

## 疑難排解

### Hook 未執行
- 驗證 JSON 組態語法是否正確
- 檢查 matcher 模式是否匹配工具名稱
- 確保腳本存在且可執行：`chmod +x script.sh`
- 執行 `claude --debug` 查看 hook 執行日誌
- 驗證 hook 從 stdin 讀取 JSON（而非命令參數）

### Hook 意外阻擋
- 使用範例 JSON 測試 hook：`echo '{"tool_name": "Write", ...}' | ./hook.py`
- 檢查退出碼：0 表示允許，2 表示阻擋
- 檢查 stderr 輸出（退出碼 2 時顯示）

### JSON 解析錯誤
- 始終從 stdin 讀取，而非命令參數
- 使用適當的 JSON 解析（而非字串操作）
- 優雅地處理缺失欄位

## 安裝

### 步驟 1：建立 Hooks 目錄
```bash
mkdir -p ~/.claude/hooks
```

### 步驟 2：複製範例 Hooks
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### 步驟 3：在設定中組態
編輯 `~/.claude/settings.json` 或 `.claude/settings.json`，加入上方所示的 hook 組態。

## 相關概念

- **[Checkpoints 與回溯](../08-checkpoints/)** - 儲存與還原對話狀態
- **[Slash Commands](../01-slash-commands/)** - 建立自訂 slash commands
- **[Skills](../03-skills/)** - 可重用的自主能力
- **[Subagents](../04-subagents/)** - 委派的任務執行
- **[Plugins](../07-plugins/)** - 打包的擴充套件
- **[進階功能](../09-advanced-features/)** - 探索進階 Claude Code 能力

## 額外資源

- **[官方 Hooks 文件](https://code.claude.com/docs/en/hooks)** - 完整的 hooks 參考
- **[CLI 參考](https://code.claude.com/docs/en/cli-reference)** - 命令列介面文件
- **[Memory 指南](../02-memory/)** - 持久上下文組態
