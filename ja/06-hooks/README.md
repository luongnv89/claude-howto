<!-- i18n-source: 06-hooks/README.md -->
<!-- i18n-source-sha: 8e2b745 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# フック

フックは、Claude Code セッション中の特定イベントに応答して実行される自動化スクリプトである。自動化、検証、権限管理、カスタムワークフローを可能にする。

## 概要

フックは、Claude Code 内で特定イベントが発生したときに自動実行される自動化アクション（シェルコマンド、HTTP webhook、LLM プロンプト、MCP ツール呼び出し、サブエージェント評価）である。フックは JSON 入力を受け取り、終了コードと JSON 出力で結果を伝える。

**主な機能：**
- イベント駆動の自動化
- JSON ベースの入出力
- `command`、`http`、`mcp_tool`、`prompt`、`agent` の各フックタイプをサポート
- ツール固有のフック向けのパターンマッチング

## 設定

フックは設定ファイル内に決まった構造で記述する。

- `~/.claude/settings.json` - ユーザー設定（全プロジェクト）
- `.claude/settings.json` - プロジェクト設定（共有可、コミット対象）
- `.claude/settings.local.json` - ローカルプロジェクト設定（コミットしない）
- 管理ポリシー - 組織全体の設定
- プラグインの `hooks/hooks.json` - プラグインスコープのフック
- スキル/エージェントのフロントマター - コンポーネントライフタイムフック

### 基本的な設定構造

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

**主要フィールド：**

| フィールド | 説明 | 例 |
|-----------|------|-----|
| `matcher` | ツール名にマッチするパターン（大文字小文字を区別） | `"Write"`、`"Edit\|Write"`、`"*"` |
| `hooks` | フック定義の配列 | `[{ "type": "command", ... }]` |
| `type` | フックタイプ：`"command"`（bash）、`"prompt"`（LLM）、`"http"`（webhook）、`"mcp_tool"`（MCP ツール呼び出し、v2.1.118 以降）、`"agent"`（サブエージェント） | `"command"` |
| `command` | 実行するシェルコマンド | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | オプションのタイムアウト（秒、デフォルト 60） | `30` |
| `once` | `true` の場合、フックはセッションごとに 1 回のみ実行 | `true` |

### マッチャーパターン

| パターン | 説明 | 例 |
|---------|------|-----|
| 完全一致文字列 | 特定のツールにマッチ | `"Write"` |
| 正規表現 | 複数のツールにマッチ | `"Edit\|Write"` |
| ワイルドカード | すべてのツールにマッチ | `"*"` または `""` |
| MCP ツール | サーバーとツールのパターン | `"mcp__memory__.*"` |

**InstructionsLoaded のマッチャー値：**

| マッチャー値 | 説明 |
|-------------|------|
| `session_start` | セッション開始時に読み込まれる指示 |
| `nested_traversal` | ネストされたディレクトリ走査中に読み込まれる指示 |
| `path_glob_match` | パス glob パターンマッチで読み込まれる指示 |

## フックタイプ

Claude Code は 5 種類のフックタイプをサポートする。

### Command フック

デフォルトのフックタイプ。シェルコマンドを実行し、JSON の標準入出力と終了コードで通信する。

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP フック

> v2.1.63 で追加。

リモート webhook エンドポイントが、command フックと同じ JSON 入力を受け取る。HTTP フックは URL に JSON を POST し、JSON レスポンスを受け取る。サンドボックスが有効な場合、HTTP フックはサンドボックス経由でルーティングされる。URL 内の環境変数展開には、セキュリティのため明示的な `allowedEnvVars` リストが必要。

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

**主要プロパティ：**
- `"type": "http"` -- HTTP フックであることを示す
- `"url"` -- webhook エンドポイント URL
- サンドボックスが有効ならサンドボックス経由でルーティング
- URL 内の環境変数展開には明示的な `allowedEnvVars` リストが必要

### Prompt フック

LLM が評価するプロンプトで、フック内容は Claude が評価するプロンプトとなる。主に `Stop` および `SubagentStop` イベントで、知的なタスク完了チェックに使用される。

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM はプロンプトを評価し、構造化された判定を返す（詳細は [Prompt ベースのフック](#prompt-ベースのフック) を参照）。

### MCP Tool フック

> v2.1.118 で追加。

`mcp_tool` タイプは設定された MCP ツールを直接呼び出す。設定はシェルコマンドや URL ではなく、MCP サーバーとツール名を参照する。検証や反応ロジックがすでに設定済みの MCP サーバー側にある場合に有用である。

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "mcp_tool",
    "server": "my-mcp-server",
    "tool": "validate_edit"
  }]
}
```

**主要プロパティ：**
- `"type": "mcp_tool"` -- MCP ツールフックであることを示す
- `"server"` -- 設定済み MCP サーバーの名前
- `"tool"` -- そのサーバー上で呼び出すツール名

フック入力（ツール名、ツール入力、セッションコンテキスト）は MCP ツールの引数として渡される。MCP サーバーの設定方法は [MCP サーバーセットアップ](../05-mcp/README.md) を参照。

### Agent フック

サブエージェントベースの検証フックで、専用エージェントを生成して条件評価や複雑なチェックを実行する。prompt フック（単発の LLM 評価）と異なり、agent フックはツールを使用してマルチステップの推論を行える。

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**主要プロパティ：**
- `"type": "agent"` -- agent フックであることを示す
- `"prompt"` -- サブエージェントへのタスク説明
- エージェントはツール（Read、Grep、Bash など）を使用して評価を行える
- prompt フックと同様に構造化された判定を返す

## フックイベント

Claude Code は **28 種類のフックイベント** をサポートする。

| イベント | 発火タイミング | マッチャー入力 | ブロック可否 | 用途例 |
|----------|---------------|---------------|-------------|--------|
| **SessionStart** | セッション開始/再開/clear/compact | startup/resume/clear/compact | 不可 | 環境セットアップ |
| **InstructionsLoaded** | CLAUDE.md やルールファイルが読み込まれた後 | （なし） | 不可 | 指示の修正/フィルタ |
| **UserPromptSubmit** | ユーザーがプロンプトを送信 | （なし） | 可 | プロンプト検証 |
| **UserPromptExpansion** | ユーザープロンプトが展開（`@` メンション、スラッシュコマンド解決など） | （なし） | 可 | 展開後のプロンプトを変換/検査 |
| **PreToolUse** | ツール実行前 | ツール名 | 可（allow/deny/ask） | 入力の検証・修正 |
| **PermissionRequest** | 権限ダイアログ表示 | ツール名 | 可 | 自動承認/拒否 |
| **PermissionDenied** | ユーザーが権限プロンプトを拒否 | ツール名 | 不可 | ロギング、解析、ポリシー強制 |
| **PostToolUse** | ツール成功後 | ツール名 | 不可 | コンテキスト追加、フィードバック |
| **PostToolUseFailure** | ツール実行失敗時 | ツール名 | 不可 | エラー処理、ロギング |
| **PostToolBatch** | ツールバッチ完了後 | （なし） | 不可 | 集約レポート、バッチ検証 |
| **Notification** | 通知送信時 | 通知タイプ | 不可 | カスタム通知 |
| **SubagentStart** | サブエージェント生成 | エージェントタイプ名 | 不可 | サブエージェントセットアップ |
| **SubagentStop** | サブエージェント完了 | エージェントタイプ名 | 可 | サブエージェント検証 |
| **Stop** | Claude が応答を終えたとき | （なし） | 可 | タスク完了チェック |
| **StopFailure** | API エラーでターン終了 | （なし） | 不可 | エラー復旧、ロギング |
| **TeammateIdle** | エージェントチームのメイトがアイドル | （なし） | 可 | チームメイト連携 |
| **TaskCompleted** | タスク完了マーク | （なし） | 可 | タスク後の処理 |
| **TaskCreated** | TaskCreate でタスク作成 | （なし） | 不可 | タスク追跡、ロギング |
| **ConfigChange** | 設定ファイル変更 | （なし） | 可（ポリシーを除く） | 設定更新への反応 |
| **CwdChanged** | 作業ディレクトリ変更 | （なし） | 不可 | ディレクトリ固有のセットアップ |
| **FileChanged** | 監視ファイル変更 | （なし） | 不可 | ファイル監視、再ビルド |
| **PreCompact** | コンテキスト圧縮前 | manual/auto | 不可 | 圧縮前の処理 |
| **PostCompact** | 圧縮完了後 | （なし） | 不可 | 圧縮後の処理 |
| **WorktreeCreate** | ワークツリー作成中 | （なし） | 可（パス返却） | ワークツリー初期化 |
| **WorktreeRemove** | ワークツリー削除中 | （なし） | 不可 | ワークツリークリーンアップ |
| **Elicitation** | MCP サーバーがユーザー入力を要求 | （なし） | 可 | 入力検証 |
| **ElicitationResult** | ユーザーが elicitation に応答 | （なし） | 可 | 応答処理 |
| **SessionEnd** | セッション終了 | （なし） | 不可 | クリーンアップ、最終ロギング |

> **PostToolUse の duration（v2.1.119）：** `PostToolUse` と `PostToolUseFailure` のフック入力に `duration_ms` が含まれるようになった。詳細は [PostToolUse](#posttooluse) セクションを参照。

### PreToolUse

Claude がツールパラメータを生成した後、処理開始前に動作する。ツール入力の検証・修正に使う。

**設定：**
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

**一般的なマッチャー：** `Task`、`Bash`、`Glob`、`Grep`、`Read`、`Edit`、`Write`、`WebFetch`、`WebSearch`

**出力制御：**
- `permissionDecision`: `"allow"`、`"deny"`、`"ask"`
- `permissionDecisionReason`: 判定の理由
- `updatedInput`: 修正されたツール入力パラメータ

### PostToolUse

ツール完了直後に動作する。検証、ロギング、Claude へのコンテキスト返却に使う。

**設定：**
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

**出力制御：**
- `"block"` 判定で Claude にフィードバックを促す
- `additionalContext`: Claude へ追加されるコンテキスト

**追加入力フィールド（v2.1.119）：**

| フィールド | 型 | 説明 |
|-----------|----|------|
| `duration_ms` | number | ツール実行時間（ミリ秒）。権限プロンプトおよび PreToolUse フック実行時間は除外。`PostToolUse` と `PostToolUseFailure` の両フックで利用可能。 |

### UserPromptSubmit

ユーザーがプロンプトを送信し、Claude が処理を開始する前に動作する。

**設定：**
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

**出力制御：**
- `decision`: `"block"` で処理を阻止
- `reason`: ブロックされた理由
- `additionalContext`: プロンプトに追加されるコンテキスト

### Stop と SubagentStop

Claude が応答を終えたとき（Stop）、サブエージェントが完了したとき（SubagentStop）に動作する。知的なタスク完了チェックのために、prompt ベースの評価をサポートする。

**追加入力フィールド：** `Stop` と `SubagentStop` の両フックは、JSON 入力に `last_assistant_message` フィールドを受け取る。これは停止前の Claude もしくはサブエージェントからの最終メッセージを含み、タスク完了の評価に有用である。

**設定：**
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

サブエージェントが実行を開始したときに動作する。マッチャー入力はエージェントタイプ名であり、特定のサブエージェントタイプを対象にできる。

**設定：**
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

セッション開始または再開時に動作する。環境変数を永続化できる。

**マッチャー：** `startup`、`resume`、`clear`、`compact`

**特別な機能：** `CLAUDE_ENV_FILE` を使って環境変数を永続化できる（`CwdChanged` と `FileChanged` フックでも利用可能）。

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

セッション終了時に、クリーンアップや最終ロギングを実行する。終了をブロックすることはできない。

**Reason フィールドの値：**
- `clear` - ユーザーがセッションをクリア
- `logout` - ユーザーがログアウト
- `prompt_input_exit` - ユーザーがプロンプト入力で終了
- `other` - その他の理由

**設定：**
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

### Notification イベント

通知イベントの更新済みマッチャー：
- `permission_prompt` - 権限要求の通知
- `idle_prompt` - アイドル状態の通知
- `auth_success` - 認証成功
- `elicitation_dialog` - ユーザーへ表示されるダイアログ

## コンポーネントスコープのフック

フックは、特定のコンポーネント（スキル、エージェント、コマンド）のフロントマターにアタッチできる。

**SKILL.md、agent.md、command.md 内：**

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
          once: true  # セッションごとに 1 回のみ実行
---
```

**コンポーネントフックでサポートされるイベント：** `PreToolUse`、`PostToolUse`、`Stop`

これにより、フックを使用するコンポーネント内に直接定義でき、関連コードを近くにまとめられる。

### サブエージェントフロントマター内のフック

サブエージェントのフロントマターで `Stop` フックを定義すると、自動的にそのサブエージェントにスコープされた `SubagentStop` フックに変換される。これにより、メインセッション停止時ではなく、その特定サブエージェント完了時にのみフックが発火することが保証される。

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # 上記の Stop フックは、このサブエージェント用の SubagentStop に自動変換される
---
```

## PermissionRequest イベント

カスタム出力フォーマットで権限要求を処理する。

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

## フックの入出力

### JSON 入力（stdin 経由）

すべてのフックは stdin 経由で JSON 入力を受け取る。

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

**共通フィールド：**

| フィールド | 説明 |
|-----------|------|
| `session_id` | セッションの一意識別子 |
| `transcript_path` | 会話トランスクリプトファイルへのパス |
| `cwd` | カレント作業ディレクトリ |
| `hook_event_name` | フックを発火させたイベント名 |
| `agent_id` | このフックを実行しているエージェントの識別子 |
| `agent_type` | エージェントタイプ（`"main"`、サブエージェントタイプ名など） |
| `worktree` | エージェントが git ワークツリーで動作している場合のパス |

### 終了コード

| 終了コード | 意味 | 動作 |
|-----------|------|------|
| **0** | 成功 | 続行、JSON stdout を解析 |
| **2** | ブロッキングエラー | 操作をブロック、stderr をエラーとして表示 |
| **その他** | 非ブロッキングエラー | 続行、verbose モードで stderr を表示 |

### JSON 出力（stdout、終了コード 0）

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

## 環境変数

| 変数 | 利用可能なフック | 説明 |
|------|-----------------|------|
| `CLAUDE_PROJECT_DIR` | すべてのフック | プロジェクトルートへの絶対パス |
| `CLAUDE_ENV_FILE` | SessionStart、CwdChanged、FileChanged | 環境変数を永続化するファイルパス |
| `CLAUDE_CODE_REMOTE` | すべてのフック | リモート環境で動作中なら `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | プラグインフック | プラグインディレクトリへのパス |
| `${CLAUDE_PLUGIN_DATA}` | プラグインフック | プラグインデータディレクトリへのパス |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd フック | SessionEnd フック向けのミリ秒単位タイムアウト設定（デフォルトを上書き） |

## Prompt ベースのフック

`Stop` および `SubagentStop` イベントには、LLM ベースの評価を使用できる。

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

**LLM レスポンススキーマ：**
```json
{
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

## 例

### 例 1：Bash コマンドバリデータ（PreToolUse）

**ファイル：** `.claude/hooks/validate-bash.py`

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
            sys.exit(2)  # 終了コード 2 = ブロッキングエラー

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**設定：**
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

### 例 2：セキュリティスキャナ（PostToolUse）

**ファイル：** `.claude/hooks/security-scan.py`

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

### 例 3：コード自動フォーマット（PostToolUse）

**ファイル：** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# stdin から JSON を読み取る
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# ファイル拡張子に基づいてフォーマット
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

### 例 4：プロンプトバリデータ（UserPromptSubmit）

**ファイル：** `.claude/hooks/validate-prompt.py`

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

### 例 5：知的な Stop フック（Prompt ベース）

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

### 例 6：コンテキスト使用量トラッカー（フックペア）

`UserPromptSubmit`（メッセージ前）と `Stop`（応答後）フックを組み合わせて、リクエストごとのトークン消費量を追跡する。

**ファイル：** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Tracks token consumption per request.

Uses UserPromptSubmit as "pre-message" hook and Stop as "post-response" hook
to calculate the delta in token usage for each request.

Token Counting Methods:
1. Character estimation (default): ~4 chars per token, no dependencies
2. tiktoken (optional): More accurate (~90-95%), requires: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# 設定
CONTEXT_LIMIT = 128000  # Claude のコンテキストウィンドウ（モデルに合わせて調整）
USE_TIKTOKEN = False    # tiktoken がインストール済みなら True にして精度向上


def get_state_file(session_id: str) -> str:
    """メッセージ前のトークン数を保存する一時ファイルパスを取得（セッションごとに分離）。"""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    テキスト内のトークン数をカウント。

    tiktoken が利用可能なら p50k_base エンコーディングを使用（約 90〜95% の精度）、
    それ以外は文字数による推定にフォールバック（約 80〜90% の精度）。
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # 推定にフォールバック

    # 文字ベースの推定：英語の場合、約 4 文字で 1 トークン
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """トランスクリプトファイルから全コンテンツを読み込み連結。"""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # 様々なメッセージ形式からテキストコンテンツを抽出
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
    """メッセージ前フック：リクエスト前の現在のトークン数を保存。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 後で比較するため一時ファイルに保存
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """応答後フック：トークンの差分を計算してレポート。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # メッセージ前のカウントを読み込む
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # 差分を計算
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # 使用量をレポート
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

**設定：**
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

**動作の仕組み：**
1. `UserPromptSubmit` がプロンプト処理前に発火し、現在のトークン数を保存
2. `Stop` が Claude の応答後に発火し、差分を計算して使用量をレポート
3. 各セッションは一時ファイル名内の `session_id` で分離

**トークンカウント方式：**

| 方式 | 精度 | 依存 | 速度 |
|------|------|------|------|
| 文字推定 | 約 80〜90% | なし | 1ms 未満 |
| tiktoken（p50k_base） | 約 90〜95% | `pip install tiktoken` | 10ms 未満 |

> **注意：** Anthropic は公式のオフライントークナイザをリリースしていない。両方式とも近似である。トランスクリプトはユーザープロンプト、Claude の応答、ツール出力を含むが、システムプロンプトや内部コンテキストは含まれない。

### 例 7：自動モード権限のシード（一度限りのセットアップスクリプト）

`~/.claude/settings.json` に Claude Code の自動モードベースラインに相当する約 67 個の安全な権限ルールをシードする一度限りのセットアップスクリプト。フックなし、将来の選択を覚えることもなし。1 回実行すれば良く、再実行しても安全（既存ルールはスキップ）。

**ファイル：** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 追加内容をプレビュー
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 適用
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**追加される項目：**

| カテゴリ | 例 |
|----------|-----|
| 組み込みツール | `Read(*)`、`Edit(*)`、`Write(*)`、`Glob(*)`、`Grep(*)`、`Agent(*)`、`WebSearch(*)` |
| Git 読み取り | `Bash(git status:*)`、`Bash(git log:*)`、`Bash(git diff:*)` |
| Git 書き込み（ローカル） | `Bash(git add:*)`、`Bash(git commit:*)`、`Bash(git checkout:*)` |
| パッケージマネージャ | `Bash(npm install:*)`、`Bash(pip install:*)`、`Bash(cargo build:*)` |
| ビルド・テスト | `Bash(make:*)`、`Bash(pytest:*)`、`Bash(go test:*)` |
| 一般的なシェル | `Bash(ls:*)`、`Bash(cat:*)`、`Bash(find:*)`、`Bash(cp:*)`、`Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`、`Bash(gh pr create:*)`、`Bash(gh issue list:*)` |

**意図的に除外される項目**（このスクリプトでは追加されない）：
- `rm -rf`、`sudo`、force push、`git reset --hard`
- `DROP TABLE`、`kubectl delete`、`terraform destroy`
- `npm publish`、`curl | bash`、本番デプロイ

### 例 8：学習進捗ロガー（SessionEnd）

各 Claude Code セッション終了時に、どのモジュールを学習したかをログに残す。進捗は
`~/.claude-howto-progress.json` に保存される。これはリポジトリ外のため、`git pull` 後も
上書きされず保持される。

**なぜ `Stop` ではなく `SessionEnd` を使うのか？**
`Stop` は Claude の *すべての* 応答後に発火する。`SessionEnd` はセッション終了時に
1 回だけ発火する。セッション終了時の日記エントリにはまさにこれが必要である。

**なぜ入力に `/dev/tty` を使うのか？**
フックスクリプトはフック JSON ペイロードを `stdin` 経由で受け取る。そのため対話的な
`read` はターミナルに到達するために `/dev/tty` を直接使う必要がある。

**ファイル：** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# SessionEnd hook: prompts for modules worked on, then appends a session record
# to ~/.claude-howto-progress.json for persistent learning progress tracking.

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# ガード：このリポジトリ内でのみ実行
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

echo ""
echo " Which modules did you work on? (e.g. 06,07 or press Enter to skip)"
echo " 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP"
echo " 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI"
printf " > "
read -r INPUT </dev/tty

if [ -z "$INPUT" ] || [ "$INPUT" = "skip" ]; then
  exit 0
fi

MODULES_JSON=$(echo "$INPUT" | tr ',' '\n' | tr -d ' ' | while read -r m; do
  case "$m" in
    01) echo '"01-slash-commands"' ;;
    02) echo '"02-memory"' ;;
    03) echo '"03-skills"' ;;
    04) echo '"04-subagents"' ;;
    05) echo '"05-mcp"' ;;
    06) echo '"06-hooks"' ;;
    07) echo '"07-plugins"' ;;
    08) echo '"08-checkpoints"' ;;
    09) echo '"09-advanced-features"' ;;
    10) echo '"10-cli"' ;;
    *)  echo "\"$m\"" ;;
  esac
done | paste -sd ',' -)

printf " Notes? (optional, press Enter to skip): "
read -r NOTES </dev/tty

# NOTES を別の引数として渡し、Python に JSON エスケープを処理させる。
# これにより、ノートに引用符やバックスラッシュを含む場合でも JSON が壊れない。
python3 - "$PROGRESS_FILE" "$DATE" "$TIME" "$MODULES_JSON" "$NOTES" <<'PYEOF'
import sys, json

path, date, time_str, modules_raw, notes = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

new_session = {
    "date": date,
    "time": time_str,
    "modules": json.loads(f"[{modules_raw}]") if modules_raw else [],
    "notes": notes,
}

with open(path, 'r') as f:
    data = json.load(f)

data.setdefault('sessions', []).append(new_session)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

echo " Saved to $PROGRESS_FILE"
```

**インストール** — `settings.json` 内のパスが解決されるよう、スクリプトをプロジェクトのフックディレクトリにコピー：

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**設定**（`.claude/settings.json` 内）：

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-end.sh\""
          }
        ]
      }
    ]
  }
}
```

**出力 — `~/.claude-howto-progress.json`：**

```json
{
  "sessions": [
    {
      "date": "2026-04-18",
      "time": "14:32",
      "modules": ["06-hooks", "07-plugins"],
      "notes": "Installed first hook, tried pre-commit example"
    }
  ]
}
```

**示されている主要パターン：**

| パターン | なぜ重要か |
|---------|-----------|
| `SessionEnd` イベント | 終了時に 1 回だけ発火 — `Stop` のように毎応答後に発火しない |
| `read -r INPUT </dev/tty` | フックは `stdin` を占有（JSON ペイロード）するため、ユーザー入力には `/dev/tty` を使う |
| `$CLAUDE_PROJECT_DIR` | ポータブルなパス — `/Users/yourname/...` を絶対にハードコードしない |
| 先頭のガード句 | グローバル設定された場合に、無関係なプロジェクトでフックが動作するのを防ぐ |
| リポジトリ外に保存 | `~/` のパスは `git pull` でデータを上書きされず保持される |

**コンパニオン：ビジュアル進捗トラッカー**

10 モジュールすべてをカバーするチェックボックスベースの完全な UI を、ブラウザで開ける。

```bash
open local-progress/index.html
```

進捗はブラウザの `localStorage` に保存される（リポジトリ内のディスクには書き込まれない）。
**Export** ボタンでスナップショットを JSON として保存し、**Import** で復元できる。

## プラグインフック

プラグインは `hooks/hooks.json` ファイルにフックを含めることができる。

**ファイル：** `plugins/hooks/hooks.json`

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

**プラグインフック内の環境変数：**
- `${CLAUDE_PLUGIN_ROOT}` - プラグインディレクトリへのパス
- `${CLAUDE_PLUGIN_DATA}` - プラグインデータディレクトリへのパス

これにより、プラグインがカスタム検証や自動化フックを含められるようになる。

## MCP ツールフック

MCP ツールは `mcp__<server>__<tool>` パターンに従う。

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

## セキュリティに関する考慮事項

### 免責事項

**自己責任で使用すること：** フックは任意のシェルコマンドを実行する。以下については利用者が単独で責任を負う。
- 設定したコマンド
- ファイルアクセス/変更権限
- データ損失やシステム障害の可能性
- 本番運用前に安全な環境でフックをテストすること

### セキュリティ上の注意点

- **ワークスペースの信頼が必要：** `statusLine` および `fileSuggestion` のフック出力コマンドは、有効化前にワークスペースの信頼を受け入れる必要がある。
- **HTTP フックと環境変数：** HTTP フックは URL 内で環境変数の補間を使うために明示的な `allowedEnvVars` リストを必要とする。これにより、機密の環境変数がリモートエンドポイントへ意図せず漏洩することを防ぐ。
- **管理対象設定の階層：** `disableAllHooks` 設定は管理対象設定の階層を尊重するようになった。つまり、組織レベルの設定でフック無効化を強制でき、個別ユーザーが上書きできない。
- **PowerShell 自動承認（v2.1.119）：** PowerShell ツールコマンドは権限モードで Bash と同様に自動承認可能になった。Windows ユーザーが PowerShell バックエンドのシェルツールで Claude Code を実行する際の同等性が確保された。

### ベストプラクティス

| 推奨 | 非推奨 |
|------|-------|
| すべての入力を検証・サニタイズ | 入力データを盲目的に信用 |
| シェル変数を引用符で囲む：`"$VAR"` | 引用符なし：`$VAR` |
| パストラバーサル（`..`）をブロック | 任意のパスを許可 |
| `$CLAUDE_PROJECT_DIR` を使った絶対パス | パスのハードコード |
| 機密ファイル（`.env`、`.git/`、鍵）をスキップ | すべてのファイルを処理 |
| まずフックを単独でテスト | 未テストのフックをデプロイ |
| HTTP フックには明示的な `allowedEnvVars` を使う | webhook へすべての環境変数を露出 |

## デバッグ

### デバッグモードの有効化

詳細なフックログを得るため、Claude をデバッグフラグ付きで実行する。

```bash
claude --debug
```

### Verbose モード

Claude Code 内で `Ctrl+O` を押して verbose モードを有効化し、フック実行の進捗を確認する。

### フックを単独でテスト

```bash
# サンプル JSON 入力でテスト
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# 終了コードを確認
echo $?
```

## 完全な設定例

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

## フック実行の詳細

| 項目 | 動作 |
|------|------|
| **タイムアウト** | デフォルト 60 秒、コマンドごとに設定可能 |
| **並列化** | マッチしたフックはすべて並列実行 |
| **重複排除** | 同一のフックコマンドは重複排除される |
| **環境** | カレントディレクトリで Claude Code の環境のもと実行 |

## トラブルシューティング

### フックが実行されない
- JSON 設定の構文が正しいことを確認
- マッチャーパターンがツール名にマッチするか確認
- スクリプトが存在し実行可能であること：`chmod +x script.sh`
- `claude --debug` でフック実行ログを確認
- フックが（コマンド引数ではなく）stdin から JSON を読み込んでいるか確認

### フックが想定外にブロックする
- サンプル JSON でフックをテスト：`echo '{"tool_name": "Write", ...}' | ./hook.py`
- 終了コードを確認：許可は 0、ブロックは 2
- stderr 出力を確認（終了コード 2 のときに表示される）

### JSON パースエラー
- 必ず stdin から読み込み、コマンド引数を使わない
- 適切な JSON パースを使用（文字列操作ではなく）
- 欠落フィールドを安全に処理

## インストール

### Step 1：フックディレクトリの作成
```bash
mkdir -p ~/.claude/hooks
```

### Step 2：フックの例をコピー
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Step 3：設定ファイルでの設定
`~/.claude/settings.json` または `.claude/settings.json` を上記のフック設定で編集する。

## 関連概念

- **[チェックポイントと巻き戻し](../08-checkpoints/)** - 会話状態の保存と復元
- **[スラッシュコマンド](../01-slash-commands/)** - カスタムスラッシュコマンドの作成
- **[スキル](../03-skills/)** - 再利用可能な自律機能
- **[サブエージェント](../04-subagents/)** - 委譲タスクの実行
- **[プラグイン](../07-plugins/)** - 拡張機能のバンドルパッケージ
- **[高度な機能](../09-advanced-features/)** - 高度な Claude Code 機能の探索

## 追加リソース

- **[Official Hooks Documentation](https://code.claude.com/docs/en/hooks)** - 完全なフックリファレンス
- **[CLI Reference](https://code.claude.com/docs/en/cli-reference)** - コマンドラインインターフェースのドキュメント
- **[メモリガイド](../02-memory/)** - 永続的コンテキストの設定

---

**最終更新：** 2026 年 4 月 24 日
**Claude Code バージョン：** 2.1.119
**情報源：**
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**対応モデル：** Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
