<!-- i18n-source: 05-mcp/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# MCP（Model Context Protocol）

このフォルダには、Claude Code における MCP サーバー設定と使用方法に関する包括的なドキュメントとサンプルが含まれている。

## 概要

MCP（Model Context Protocol）は、Claude が外部ツール、API、リアルタイムデータソースにアクセスするための標準化された方式である。メモリとは異なり、MCP は変化するデータへのライブアクセスを提供する。

主な特徴：
- 外部サービスへのリアルタイムアクセス
- ライブデータの同期
- 拡張可能なアーキテクチャ
- セキュアな認証
- ツールベースの対話

## MCP アーキテクチャ

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## MCP エコシステム

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## MCP のインストール方法

Claude Code は MCP サーバー接続のために複数のトランスポートプロトコルをサポートしている。

### HTTP トランスポート（推奨）

```bash
# 基本的な HTTP 接続
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 認証ヘッダー付き HTTP
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio トランスポート（ローカル）

ローカルで動作する MCP サーバー向け：

```bash
# ローカル Node.js サーバー
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# 環境変数付き
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE トランスポート（非推奨）

Server-Sent Events トランスポートは `http` の登場により非推奨となったが、引き続きサポートされている。

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Windows 固有の注意点

ネイティブ Windows（WSL ではない）では、npx コマンドに `cmd /c` を使う。

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 認証

Claude Code は OAuth 2.0 を必要とする MCP サーバーをサポートする。OAuth 対応サーバーに接続する際、Claude Code が認証フロー全体を処理する。

```bash
# OAuth 対応 MCP サーバーへ接続（対話フロー）
claude mcp add --transport http my-service https://my-service.example.com/mcp

# 非対話セットアップのために OAuth 認証情報を事前設定
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| 機能 | 説明 |
|------|------|
| **対話型 OAuth** | `/mcp` を使ってブラウザベースの OAuth フローをトリガー |
| **事前設定済み OAuth クライアント** | Notion、Stripe など一般的なサービス向けの組み込み OAuth クライアント（v2.1.30 以降） |
| **事前設定済み認証情報** | 自動セットアップ用の `--client-id`、`--client-secret`、`--callback-port` フラグ |
| **トークンの保存** | トークンはシステムキーチェーンに安全に保存される |
| **ステップアップ認証** | 特権操作に対するステップアップ認証をサポート |
| **ディスカバリのキャッシュ** | OAuth ディスカバリメタデータがキャッシュされ、再接続が高速化される |
| **メタデータのオーバーライド** | `.mcp.json` の `oauth.authServerMetadataUrl` でデフォルトの OAuth メタデータディスカバリを上書き |

#### OAuth メタデータディスカバリのオーバーライド

MCP サーバーが標準の OAuth メタデータエンドポイント（`/.well-known/oauth-authorization-server`）でエラーを返すが、動作する OIDC エンドポイントを公開している場合、Claude Code に特定の URL から OAuth メタデータを取得するよう指示できる。サーバー設定の `oauth` オブジェクト内で `authServerMetadataUrl` を設定する。

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

URL は `https://` を使用しなければならない。このオプションは Claude Code v2.1.64 以降が必要。

### Claude.ai MCP コネクタ

Claude.ai アカウントで設定された MCP サーバーは、Claude Code でも自動的に利用可能になる。つまり、Claude.ai の Web インターフェース経由でセットアップした MCP 接続は、追加設定なしでアクセスできる。

Claude.ai MCP コネクタは `--print` モード（v2.1.83 以降）でも利用可能で、非対話・スクリプト実行を可能にする。

> **起動時の注意（v2.1.117 以降）：** ローカルと claude.ai の MCP サーバーの両方が設定されている場合、並行接続がデフォルトとなる（以前は逐次接続）。複数サーバー使用時の起動レイテンシが削減される。

Claude Code 内で Claude.ai MCP サーバーを無効化するには、`ENABLE_CLAUDEAI_MCP_SERVERS` 環境変数を `false` に設定する。

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **注意：** この機能は Claude.ai アカウントでログインしているユーザーのみ利用できる。

## MCP セットアップの流れ

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

## MCP ツール検索

MCP ツールの説明文がコンテキストウィンドウの 10% を超える場合、Claude Code は自動的にツール検索を有効にし、モデルコンテキストを圧迫せずに適切なツールを効率的に選択する。

| 設定 | 値 | 説明 |
|------|-----|------|
| `ENABLE_TOOL_SEARCH` | `auto`（デフォルト） | ツールの説明がコンテキストの 10% を超えた時点で自動的に有効化 |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | カスタムしきい値 `N` 個のツール数で自動的に有効化 |
| `ENABLE_TOOL_SEARCH` | `true` | ツール数に関係なく常に有効 |
| `ENABLE_TOOL_SEARCH` | `false` | 無効。すべてのツールの説明が完全な形で送信される |

> **注意：** ツール検索には Sonnet 4 以降、もしくは Opus 4 以降が必要。Haiku モデルはツール検索をサポートしない。

## 動的ツール更新

Claude Code は MCP の `list_changed` 通知をサポートする。MCP サーバーが利用可能なツールを動的に追加・削除・変更すると、Claude Code は更新を受け取り、ツール一覧を自動的に調整する。再接続や再起動は不要である。

## MCP Apps

MCP Apps は最初の公式 MCP 拡張で、MCP ツール呼び出しがチャットインターフェースに直接レンダリングされるインタラクティブな UI コンポーネントを返せるようにする。プレーンテキストのレスポンスではなく、MCP サーバーがリッチなダッシュボード、フォーム、データの可視化、マルチステップワークフローをチャット内に直接表示できる。会話を離れることなく、すべてがインラインで表示される。

## MCP Elicitation

MCP サーバーはインタラクティブダイアログを介してユーザーから構造化入力を要求できる（v2.1.49 以降）。これにより MCP サーバーはワークフローの途中で追加情報を要求できる。たとえば確認のプロンプト、選択肢のリストからの選択、必須フィールドの入力などが可能となり、MCP サーバーとの対話に対話性を加える。

## ツール説明と指示の上限

v2.1.84 以降、Claude Code は MCP サーバーごとのツール説明と指示に **2 KB の上限** を強制する。これは個々のサーバーが冗長すぎるツール定義でコンテキストを過剰に消費するのを防ぎ、コンテキストの肥大化を抑え、対話を効率的に保つ。

## MCP プロンプトをスラッシュコマンドとして利用

MCP サーバーはスラッシュコマンドとして表示されるプロンプトを公開できる。プロンプトは以下の命名規則でアクセスする。

```
/mcp__<server>__<prompt>
```

たとえば、`github` という名前のサーバーが `review` というプロンプトを公開している場合、`/mcp__github__review` として呼び出せる。

## サーバーの重複排除

同じ MCP サーバーが複数のスコープ（local、project、user）で定義されている場合、ローカル設定が優先される。これにより、競合なしにローカルカスタマイズで project レベルや user レベルの MCP 設定をオーバーライドできる。

## @ メンションによる MCP リソース

`@` メンション構文を使ってプロンプト内で MCP リソースを直接参照できる。

```
@server-name:protocol://resource/path
```

たとえば、特定のデータベースリソースを参照するには：

```
@database:postgres://mydb/users
```

これにより Claude が MCP リソースの内容を会話コンテキストの一部としてインラインで取得・包含できる。

## MCP のスコープ

MCP の設定は共有レベルの異なる複数のスコープに保存できる。

| スコープ | 場所 | 説明 | 共有相手 | 承認の要否 |
|----------|------|------|----------|-----------|
| **Local**（デフォルト） | `~/.claude.json`（プロジェクトパス配下） | 現在のユーザー、現在のプロジェクトに非公開（旧バージョンでは `project` と呼ばれていた） | 自分のみ | 不要 |
| **Project** | `.mcp.json` | git リポジトリにチェックインされる | チームメンバー | 必要（初回使用時） |
| **User** | `~/.claude.json` | 全プロジェクトで利用可能（旧バージョンでは `global` と呼ばれていた） | 自分のみ | 不要 |

### Project スコープの使用

プロジェクト固有の MCP 設定を `.mcp.json` に保存する。

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

チームメンバーはプロジェクト MCP の初回使用時に承認プロンプトが表示される。

## MCP 設定の管理

### MCP サーバーの追加

```bash
# HTTP ベースのサーバーを追加
claude mcp add --transport http github https://api.github.com/mcp

# ローカル stdio サーバーを追加
claude mcp add --transport stdio database -- npx @company/db-server

# すべての MCP サーバーを一覧表示
claude mcp list

# 特定サーバーの詳細を取得
claude mcp get github

# MCP サーバーを削除
claude mcp remove github

# プロジェクト固有の承認選択をリセット
claude mcp reset-project-choices

# Claude Desktop からインポート
claude mcp add-from-claude-desktop
```

## 利用可能な MCP サーバー一覧

| MCP サーバー | 用途 | 一般的なツール | 認証 | リアルタイム |
|--------------|------|----------------|------|--------------|
| **Filesystem** | ファイル操作 | read、write、delete | OS の権限 | ✅ Yes |
| **GitHub** | リポジトリ管理 | list_prs、create_issue、push | OAuth | ✅ Yes |
| **Slack** | チームコミュニケーション | send_message、list_channels | トークン | ✅ Yes |
| **Database** | SQL クエリ | query、insert、update | 認証情報 | ✅ Yes |
| **Google Docs** | ドキュメントアクセス | read、write、share | OAuth | ✅ Yes |
| **Asana** | プロジェクト管理 | create_task、update_status | API キー | ✅ Yes |
| **Stripe** | 決済データ | list_charges、create_invoice | API キー | ✅ Yes |
| **Memory** | 永続メモリ | store、retrieve、delete | ローカル | ❌ No |

## 実用例

### 例 1：GitHub MCP の設定

**ファイル：** `.mcp.json`（プロジェクトルート）

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**利用可能な GitHub MCP ツール：**

#### プルリクエスト管理
- `list_prs` - リポジトリ内の全 PR を一覧
- `get_pr` - diff を含む PR の詳細を取得
- `create_pr` - 新しい PR を作成
- `update_pr` - PR の説明・タイトルを更新
- `merge_pr` - PR を main ブランチにマージ
- `review_pr` - レビューコメントを追加

**リクエスト例：**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Issue 管理
- `list_issues` - 全 Issue を一覧
- `get_issue` - Issue の詳細を取得
- `create_issue` - 新しい Issue を作成
- `close_issue` - Issue をクローズ
- `add_comment` - Issue にコメントを追加

#### リポジトリ情報
- `get_repo_info` - リポジトリの詳細
- `list_files` - ファイルツリー構造
- `get_file_content` - ファイル内容を読み込み
- `search_code` - コードベースを横断検索

#### コミット操作
- `list_commits` - コミット履歴
- `get_commit` - 特定コミットの詳細
- `create_commit` - 新しいコミットを作成

**セットアップ：**
```bash
export GITHUB_TOKEN="your_github_token"
# または CLI で直接追加:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### 設定での環境変数展開

MCP 設定は環境変数の展開とフォールバックデフォルトをサポートする。`${VAR}` および `${VAR:-default}` 構文は次のフィールドで動作する：`command`、`args`、`env`、`url`、`headers`。

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

変数は実行時に展開される。
- `${VAR}` - 環境変数を使用、未設定ならエラー
- `${VAR:-default}` - 環境変数を使用、未設定なら default にフォールバック

### 例 2：Database MCP のセットアップ

**設定：**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**使用例：**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**セットアップ：**
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# または CLI で直接追加:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### 例 3：マルチ MCP ワークフロー

**シナリオ：日次レポート生成**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**セットアップ：**
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# 各 MCP サーバーを CLI で追加するか、.mcp.json で設定する
```

### 例 4：Filesystem MCP の操作

**設定：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**利用可能な操作：**

| 操作 | コマンド | 用途 |
|------|----------|------|
| ファイル一覧 | `ls ~/projects` | ディレクトリの内容を表示 |
| ファイル読み込み | `cat src/main.ts` | ファイル内容を読み込み |
| ファイル書き込み | `create docs/api.md` | 新規ファイルを作成 |
| ファイル編集 | `edit src/app.ts` | ファイルを変更 |
| 検索 | `grep "async function"` | ファイル内を検索 |
| 削除 | `rm old-file.js` | ファイルを削除 |

**セットアップ：**
```bash
# CLI で直接追加:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP とメモリの比較：判断マトリクス

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## リクエスト/レスポンスパターン

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

## 環境変数

機密性の高い認証情報は環境変数に保存する。

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

そして MCP 設定で参照する。

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude を MCP サーバーにする（`claude mcp serve`）

Claude Code 自体が他のアプリケーション向けの MCP サーバーとして動作できる。これにより、外部ツール、エディタ、自動化システムが標準 MCP プロトコルを介して Claude の機能を活用できる。

```bash
# Claude Code を stdio 上の MCP サーバーとして起動
claude mcp serve
```

他のアプリケーションは、stdio ベースの MCP サーバーと同じようにこのサーバーに接続できる。たとえば、別の Claude Code インスタンスに Claude Code を MCP サーバーとして追加するには：

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

これは、ある Claude インスタンスが別のインスタンスをオーケストレーションするマルチエージェントワークフローの構築に有用である。

## 管理対象 MCP 設定（エンタープライズ）

エンタープライズ展開では、IT 管理者が `managed-mcp.json` 設定ファイルを通じて MCP サーバーポリシーを強制できる。このファイルは、組織全体で許可または禁止する MCP サーバーを排他的に制御する。

**配置場所：**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**機能：**
- `allowedMcpServers` -- 許可するサーバーのホワイトリスト
- `deniedMcpServers` -- 禁止するサーバーのブロックリスト
- サーバー名、コマンド、URL パターンによるマッチをサポート
- ユーザー設定より前に組織全体の MCP ポリシーを強制
- 認可されていないサーバー接続を防止

**設定例：**

```json
{
  "allowedMcpServers": [
    {
      "serverName": "github",
      "serverUrl": "https://api.github.com/mcp"
    },
    {
      "serverName": "company-internal",
      "serverCommand": "company-mcp-server"
    }
  ],
  "deniedMcpServers": [
    {
      "serverName": "untrusted-*"
    },
    {
      "serverUrl": "http://*"
    }
  ]
}
```

> **注意：** `allowedMcpServers` と `deniedMcpServers` の両方が同じサーバーにマッチする場合、deny ルールが優先される。

## プラグイン提供の MCP サーバー

プラグインは独自の MCP サーバーをバンドルでき、プラグインのインストール時に自動的に利用可能になる。プラグイン提供の MCP サーバーは 2 つの方法で定義できる。

1. **スタンドアロンの `.mcp.json`** -- プラグインのルートディレクトリに `.mcp.json` ファイルを配置
2. **`plugin.json` 内にインライン定義** -- プラグインマニフェスト内で MCP サーバーを直接定義

`${CLAUDE_PLUGIN_ROOT}` 変数を使ってプラグインのインストールディレクトリからの相対パスを参照する。

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## サブエージェントスコープの MCP

MCP サーバーはエージェントのフロントマター内で `mcpServers:` キーを使ってインライン定義でき、プロジェクト全体ではなく特定のサブエージェントにスコープできる。これは、ワークフロー内の他のエージェントには不要な特定の MCP サーバーへのアクセスを、あるエージェントが必要とする場合に有用である。

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

サブエージェントスコープの MCP サーバーは、そのエージェントの実行コンテキスト内でのみ利用でき、親エージェントや兄弟エージェントとは共有されない。

## MCP の出力上限

Claude Code はコンテキストオーバーフローを防ぐため、MCP ツールの出力に上限を強制する。

| 上限 | しきい値 | 動作 |
|------|----------|------|
| **警告** | 10,000 トークン | 出力が大きいことを示す警告を表示 |
| **デフォルト最大値** | 25,000 トークン | この上限を超えた出力は切り詰められる |
| **ディスク永続化** | 50,000 文字 | 50K 文字を超えるツール結果はディスクに永続化される |

最大出力上限は `MAX_MCP_OUTPUT_TOKENS` 環境変数で設定可能。

```bash
# 最大出力を 50,000 トークンに引き上げる
export MAX_MCP_OUTPUT_TOKENS=50000
```

## コード実行によるコンテキスト肥大化の解決

MCP の採用が拡大するにつれ、数十のサーバーと数百〜数千のツールに接続することは大きな課題を生む：**コンテキストの肥大化** である。これは MCP がスケールしたときの最大の問題と言ってよく、Anthropic のエンジニアリングチームが提案するエレガントな解決策が、ツールを直接呼び出す代わりにコード実行を使う方法である。

> **出典：** [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic Engineering Blog

### 問題：トークン浪費の 2 つの源

**1. ツール定義がコンテキストウィンドウを過負荷にする**

ほとんどの MCP クライアントは全ツール定義を事前に読み込む。数千のツールに接続している場合、モデルはユーザーのリクエストを読む前に数十万トークンを処理しなければならない。

**2. 中間結果がさらにトークンを消費する**

すべての中間ツール結果はモデルのコンテキストを通過する。Google Drive から Salesforce へ会議の文字起こしを転送する場合を考えると、文字起こし全体がコンテキストを **2 回** 流れる。読み込むときと、宛先に書き込むときである。2 時間の会議の文字起こしは 50,000 トークン以上の追加になり得る。

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### 解決策：コード API としての MCP ツール

ツール定義と結果をコンテキストウィンドウに通す代わりに、エージェントが MCP ツールを API として呼び出す **コードを書く**。コードはサンドボックス化された実行環境で動作し、最終結果のみがモデルに返される。

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### 仕組み

MCP ツールは型付き関数のファイルツリーとして提示される。

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

各ツールファイルには型付きラッパーが含まれる。

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

エージェントはツールをオーケストレーションするコードを書く。

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// データはツール間で直接流れる — モデルを経由しない
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**結果：トークン使用量は約 150,000 から約 2,000 に減少 — 98.7% の削減。**

### 主な利点

| 利点 | 説明 |
|------|------|
| **段階的開示** | エージェントはファイルシステムを参照して必要なツール定義のみを読み込み、全ツールを事前読込みしない |
| **コンテキスト効率の良い結果** | データは実行環境内でフィルタ/変換されてからモデルに返される |
| **強力な制御フロー** | ループ、条件分岐、エラー処理がモデルへのラウンドトリップなしにコード内で動作 |
| **プライバシー保護** | 中間データ（PII、機密レコード）は実行環境内に留まり、モデルコンテキストに入らない |
| **状態の永続化** | エージェントは中間結果をファイルに保存し、再利用可能なスキル関数を構築できる |

#### 例：大規模データセットのフィルタリング

```typescript
// コード実行なし — 10,000 行すべてがコンテキストを流れる
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// コード実行あり — 実行環境内でフィルタリング
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // 5 行のみがモデルに到達
```

#### 例：ラウンドトリップなしのループ

```typescript
// デプロイ通知をポーリング — すべてコード内で実行
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

### 考慮すべきトレードオフ

コード実行は独自の複雑さを持ち込む。エージェント生成のコードを実行するには次が必要となる。

- 適切なリソース上限を持つ **セキュアなサンドボックス実行環境**
- 実行されたコードの **監視とログ記録**
- ツールの直接呼び出しと比較した追加の **インフラオーバーヘッド**

利点（トークンコスト削減、レイテンシ低下、ツール構成の改善）は、こうした実装コストと天秤にかける必要がある。MCP サーバーが少数だけのエージェントなら、ツールの直接呼び出しのほうがシンプルかもしれない。スケールするエージェント（数十のサーバー、数百のツール）にとって、コード実行は大きな改善である。

### MCPorter：MCP ツール構成のためのランタイム

[MCPorter](https://github.com/steipete/mcporter) は、MCP サーバーへの呼び出しをボイラープレートなしで実用的にする TypeScript ランタイム＆ CLI ツールキットである。選択的なツール公開と型付きラッパーを通じてコンテキストの肥大化を抑える助けにもなる。

**解決すること：** すべての MCP サーバーから全ツール定義を事前読み込みする代わりに、MCPorter は特定のツールを必要に応じて発見、検査、呼び出しできるようにする。これによりコンテキストを軽量に保てる。

**主な機能：**

| 機能 | 説明 |
|------|------|
| **ゼロ設定での発見** | Cursor、Claude、Codex、ローカル設定から MCP サーバーを自動発見 |
| **型付きツールクライアント** | `mcporter emit-ts` が `.d.ts` インターフェースとすぐ動作するラッパーを生成 |
| **構成可能な API** | `createServerProxy()` がツールを camelCase メソッドとして公開し、`.text()`、`.json()`、`.markdown()` ヘルパーを提供 |
| **CLI 生成** | `mcporter generate-cli` が任意の MCP サーバーをスタンドアロン CLI に変換し、`--include-tools` / `--exclude-tools` でフィルタリング |
| **パラメータの非表示** | オプションパラメータはデフォルトで非表示となり、スキーマの冗長性を低減 |

**インストール：**

```bash
npx mcporter list          # インストール不要 — サーバーをすぐに発見
pnpm add mcporter          # プロジェクトに追加
brew install steipete/tap/mcporter  # macOS の Homebrew 経由
```

**例 — TypeScript でツールを構成：**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// データはモデルコンテキストを通過せずにツール間を流れる
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**例 — CLI ツール呼び出し：**

```bash
# 特定のツールを直接呼び出し
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# 利用可能なサーバーとツールを一覧
npx mcporter list
```

MCPorter は上述のコード実行アプローチを補完するもので、MCP ツールを型付き API として呼び出すためのランタイム基盤を提供する。中間データをモデルコンテキストの外に保つことを容易にする。

## ベストプラクティス

### セキュリティに関する考慮事項

#### 推奨 ✅
- すべての認証情報に環境変数を使用する
- トークンと API キーを定期的にローテーションする（毎月推奨）
- 可能な限り読み取り専用トークンを使用する
- MCP サーバーのアクセス範囲を必要最小限に制限する
- MCP サーバーの使用状況とアクセスログを監視する
- 利用可能であれば外部サービスに OAuth を使用する
- MCP リクエストにレート制限を実装する
- 本番運用前に MCP 接続をテストする
- 稼働中の MCP 接続をすべてドキュメント化する
- MCP サーバーパッケージを最新に保つ

#### 非推奨 ❌
- 認証情報を設定ファイルにハードコードしない
- トークンや秘密情報を git にコミットしない
- チームのチャットやメールでトークンを共有しない
- 個人用トークンをチームプロジェクトに使用しない
- 不要な権限を付与しない
- 認証エラーを無視しない
- MCP エンドポイントを公開しない
- MCP サーバーを root/admin 権限で実行しない
- 機密データをログにキャッシュしない
- 認証メカニズムを無効化しない

### 設定のベストプラクティス

1. **バージョン管理：** `.mcp.json` を git に保存するが、シークレットには環境変数を使う
2. **最小権限：** 各 MCP サーバーに必要最小限の権限のみ付与する
3. **分離：** 可能なら異なる MCP サーバーを別プロセスで実行する
4. **監視：** 監査証跡のため、すべての MCP リクエストとエラーを記録する
5. **テスト：** 本番デプロイ前にすべての MCP 設定をテストする

### パフォーマンスのヒント

- 頻繁にアクセスするデータはアプリケーションレベルでキャッシュする
- データ転送量を減らすため、特定の MCP クエリを使う
- MCP 操作のレスポンスタイムを監視する
- 外部 API にはレート制限を検討する
- 複数操作を実行するときはバッチ処理を使う

## インストール手順

### 前提条件
- Node.js と npm がインストール済み
- Claude Code CLI がインストール済み
- 外部サービス用の API トークン/認証情報

### ステップバイステップのセットアップ

1. **最初の MCP サーバーを追加**（例：GitHub）：
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   または、プロジェクトルートに `.mcp.json` ファイルを作成：
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

2. **環境変数を設定：**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **接続をテスト：**
```bash
claude /mcp
```

4. **MCP ツールを使う：**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### 特定サービスのインストール

**GitHub MCP：**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP：**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP：**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP：**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## トラブルシューティング

### MCP サーバーが見つからない
```bash
# MCP サーバーがインストールされているか確認
npm list -g @modelcontextprotocol/server-github

# 未インストールならインストール
npm install -g @modelcontextprotocol/server-github
```

### 認証失敗
```bash
# 環境変数が設定されているか確認
echo $GITHUB_TOKEN

# 必要なら再設定
export GITHUB_TOKEN="your_token"

# トークンが正しい権限を持つか確認
# GitHub のトークンスコープは https://github.com/settings/tokens で確認
```

### 接続タイムアウト
- ネットワーク疎通を確認：`ping api.github.com`
- API エンドポイントが到達可能か確認
- API のレート制限を確認
- 設定でタイムアウトを延ばしてみる
- ファイアウォールやプロキシの問題を確認

### MCP サーバーがクラッシュする
- MCP サーバーのログを確認：`~/.claude/logs/`
- すべての環境変数が設定されているか確認
- 適切なファイル権限を確認
- MCP サーバーパッケージの再インストールを試す
- 同じポートで競合するプロセスがないか確認

## 関連概念

### メモリと MCP
- **メモリ：** 永続的で変化しないデータを保存（設定、コンテキスト、履歴）
- **MCP：** 変化するライブデータにアクセス（API、データベース、リアルタイムサービス）

### どちらを使うか
- **メモリを使う場合：** ユーザー設定、会話履歴、学習したコンテキスト
- **MCP を使う場合：** 現在の GitHub Issue、ライブデータベースクエリ、リアルタイムデータ

### 他の Claude 機能との統合
- メモリと MCP を組み合わせて豊かなコンテキストを構築
- プロンプト内で MCP ツールを使い、より良い推論を実現
- 複雑なワークフローには複数の MCP を活用

## 追加リソース

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/specification)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — ボイラープレートなしで MCP サーバーを呼び出すための TypeScript ランタイム＆ CLI
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — コンテキスト肥大化の解決に関する Anthropic のエンジニアリングブログ
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude API Documentation](https://docs.anthropic.com)

---

**最終更新：** 2026 年 4 月 24 日
**Claude Code バージョン：** 2.1.119
**情報源：**
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
**対応モデル：** Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
