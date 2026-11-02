<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (모델 컨텍스트 프로토콜)

이 폴더에는 MCP 서버 구성 및 Claude Code와 함께 사용하는 방법에 대한 포괄적인 문서와 예시가 포함되어 있습니다.

## 개요

MCP (Model Context Protocol)는 Claude가 외부 도구, API 및 실시간 데이터 소스에 접근하는 표준화된 방법입니다. Memory와 달리 MCP는 변화하는 데이터에 대한 실시간 접근을 제공합니다.

주요 특징:
- 외부 서비스에 대한 실시간 접근
- 실시간 데이터 동기화
- 확장 가능한 아키텍처
- 안전한 인증
- 도구 기반 상호 작용

## MCP 아키텍처

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

## MCP 생태계

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

## MCP 설치 방법

Claude Code는 MCP 서버 연결을 위해 여러 전송 프로토콜을 지원합니다.

### HTTP 전송 (권장)

```bash
# Basic HTTP connection
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP with authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio 전송 (로컬)

로컬에서 실행되는 MCP 서버의 경우:

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# With environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

#### stdio 서버용 CLAUDE_PROJECT_DIR (v2.1.139 이상)

모든 MCP stdio 서버는 환경에 `CLAUDE_PROJECT_DIR=<repo root의 절대 경로>`가 이미 설정된 상태로 생성됩니다. 이는 후크(hook)에 사용되는 것과 동일한 규칙입니다. 플러그인 및 프로젝트의 `.mcp.json` 파일은 `command`, `args`, `env` 값에서 `${CLAUDE_PROJECT_DIR}`를 참조할 수 있으며, 이 대체는 `execve()` 전에 이루어집니다.

```json
{
  "mcpServers": {
    "repo-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["${CLAUDE_PROJECT_DIR}/.claude/mcp/repo-tools.js"],
      "env": {
        "REPO_ROOT": "${CLAUDE_PROJECT_DIR}"
      }
    }
  }
}
```

Claude Code가 어디에서 실행되었는지에 관계없이 stdio 서버가 프로젝트 루트에 상대적인 파일을 읽어야 할 때 이 기능을 사용하세요.

stdio MCP 서버는 또한 `CLAUDE_CODE_SESSION_ID`를 수신합니다 (후크 및 Bash에 전달된 값과 일치). 세션이 `--resume`으로 재개될 때도 마찬가지입니다 (v2.1.163 이상).

### SSE 전송 (사용 중단)

Server-Sent Events 전송은 `http` 방식에 비해 사용이 중단되었지만 여전히 지원됩니다.

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Windows 특정 참고 사항

네이티브 Windows (WSL 아님)에서는 npx 명령에 `cmd /c`를 사용하세요.

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 인증

Claude Code는 OAuth 2.0이 필요한 MCP 서버를 지원합니다. OAuth를 사용하는 서버에 연결할 때 Claude Code는 전체 인증 흐름을 처리합니다.

```bash
# Connect to an OAuth-enabled MCP server (interactive flow)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Pre-configure OAuth credentials for non-interactive setup
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Feature | Description |
|---------|-------------|
| **Interactive OAuth** | `/mcp`를 사용하여 브라우저 기반 OAuth 흐름을 트리거합니다. |
| **Pre-configured OAuth clients** | Notion, Stripe 등 일반 서비스용 내장 OAuth 클라이언트 (v2.1.30 이상) |
| **Pre-configured credentials** | 자동 설정을 위한 `--client-id`, `--client-secret`, `--callback-port` 플래그 |
| **Token storage** | 토큰은 시스템 키체인에 안전하게 저장됩니다. |
| **Step-up auth** | 권한이 필요한 작업에 대한 단계별 인증을 지원합니다. |
| **Discovery caching** | OAuth 검색 메타데이터는 더 빠른 재연결을 위해 캐시됩니다. |
| **Metadata override** | `.mcp.json`의 `oauth.authServerMetadataUrl`을 사용하여 기본 OAuth 메타데이터 검색을 재정의합니다. |

#### OAuth 메타데이터 검색 재정의

MCP 서버가 표준 OAuth 메타데이터 엔드포인트 (`/.well-known/oauth-authorization-server`)에서 오류를 반환하지만 작동하는 OIDC 엔드포인트를 노출하는 경우, Claude Code에 특정 URL에서 OAuth 메타데이터를 가져오도록 지시할 수 있습니다. 서버 구성의 `oauth` 객체에 `authServerMetadataUrl`을 설정하세요.

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

URL은 `https://`를 사용해야 합니다. 이 옵션은 Claude Code v2.1.64 이상에서 필요합니다.

#### 인증 시작 알림 및 동적 헤더 새로 고침 (v2.1.193)

- **시작 인증 알림 (v2.1.193 이상)**: 시작 시 Claude Code는 아직 인증이 필요한 MCP 서버 목록을 알림으로 표시하여, 로그인이 필요한 서버가 조용히 작동하지 않는 상태로 방치되지 않도록 합니다.
- **`headersHelper` 자동 새로 고침 (v2.1.193 이상)**: `headersHelper`를 통해 사용자 지정 인증을 제공하는 경우, 서버가 HTTP 401 또는 403을 반환하면 도우미가 자동으로 다시 호출됩니다. 수동 재연결 없이 자격 증명이 즉시 새로 고쳐집니다. [사용자 지정 인증을 위해 동적 헤더 사용](https://code.claude.com/docs/en/mcp)을 참조하세요.

### Claude.ai MCP 커넥터

Claude.ai 계정에서 구성된 MCP 서버는 Claude Code에서 자동으로 사용할 수 있습니다. 이는 Claude.ai 웹 인터페이스를 통해 설정한 모든 MCP 연결이 추가 구성 없이 접근 가능하다는 것을 의미합니다.

Claude.ai MCP 커넥터는 `--print` 모드에서도 사용할 수 있습니다 (v2.1.83 이상). 이를 통해 비대화형 및 스크립트 기반 사용이 가능합니다.

> **시작 참고 사항 (v2.1.117 이상):** 로컬 및 claude.ai MCP 서버가 모두 구성된 경우 동시 연결이 기본값입니다 (이전에는 순차적). 이는 여러 서버를 사용할 때 시작 대기 시간을 줄여줍니다.

Claude Code에서 Claude.ai MCP 서버를 비활성화하려면 `ENABLE_CLAUDEAI_MCP_SERVERS` 환경 변수를 `false`로 설정하세요.

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **참고:** 이 기능은 Claude.ai 계정으로 로그인한 사용자에게만 제공됩니다.

## MCP 설정 프로세스

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

### /mcp 명령

세션 내에서 `/mcp`를 입력하여 연결된 서버를 나열하고, OAuth 흐름을 트리거하며, 연결 상태를 검사할 수 있습니다.

- **v2.1.121부터**, MCP는 일시적인 오류 발생 시 초기 연결을 최대 3번 재시도합니다.
- **v2.1.128부터**, `/mcp`는 연결된 각 서버의 **도구 개수**를 표시하고 **0개 도구**를 보고하는 서버를 시각적으로 표시하여 잘못 구성된 서버를 한눈에 알아볼 수 있도록 합니다.

## MCP 도구 검색

MCP 도구 설명이 컨텍스트 창의 10%를 초과할 때, Claude Code는 모델 컨텍스트를 압도하지 않고 올바른 도구를 효율적으로 선택하기 위해 자동으로 도구 검색을 활성화합니다.

| Setting | Value | Description |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto` (기본값) | 도구 설명이 컨텍스트의 10%를 초과할 때 자동으로 활성화됩니다. |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | `N`개 도구의 사용자 지정 임계값에서 자동으로 활성화됩니다. |
| `ENABLE_TOOL_SEARCH` | `true` | 도구 개수와 관계없이 항상 활성화됩니다. |
| `ENABLE_TOOL_SEARCH` | `false` | 비활성화됩니다; 모든 도구 설명이 전체로 전송됩니다. |

> **참고:** 도구 검색은 Sonnet 4 이상 또는 Opus 4 이상이 필요합니다. Haiku 모델은 도구 검색에 지원되지 않습니다.

### 서버별 도구 검색 우회 (v2.1.121 이상)

특정 MCP 서버의 도구가 모든 단계에서 필요한 경우, 해당 구성에 `"alwaysLoad": true`를 표시하여 도구 검색 연기를 건너뛰고 도구를 항상 사용 가능하게 유지하세요.

```json
{
  "mcpServers": {
    "always-on-tool": {
      "command": "node",
      "args": ["./tools/always.js"],
      "alwaysLoad": true
    }
  }
}
```

항상 로드되는 각 도구는 더 관련성 높은 도구를 표시하는 데 사용될 수 있는 컨텍스트를 소비하므로 아껴서 사용하세요.

## 동적 도구 업데이트

Claude Code는 MCP `list_changed` 알림을 지원합니다. MCP 서버가 사용 가능한 도구를 동적으로 추가, 제거 또는 수정하면 Claude Code는 업데이트를 수신하고 도구 목록을 자동으로 조정합니다. 재연결이나 다시 시작이 필요 없습니다.

## MCP 앱

MCP 앱은 최초의 공식 MCP 확장으로, MCP 도구 호출이 채팅 인터페이스에 직접 렌더링되는 대화형 UI 구성 요소를 반환할 수 있도록 합니다. 일반 텍스트 응답 대신 MCP 서버는 대화에서 벗어나지 않고도 풍부한 대시보드, 양식, 데이터 시각화 및 다단계 워크플로우를 인라인으로 제공할 수 있습니다.

<h2>MCP 정보 요청</h2>

MCP 서버는 대화형 대화 상자를 통해 사용자에게 구조화된 입력을 요청할 수 있습니다 (v2.1.49 이상). 이를 통해 MCP 서버는 워크플로우 중간에 추가 정보를 요청할 수 있습니다. 예를 들어, 확인을 요청하거나, 옵션 목록에서 선택하거나, 필수 필드를 채워 MCP 서버 상호 작용에 대화형 기능을 추가할 수 있습니다.

## 도구 설명 및 지시 상한

v2.1.84부터 Claude Code는 MCP 서버당 도구 설명 및 지시에 대해 **2KB 상한선**을 적용합니다. 이는 개별 서버가 지나치게 장황한 도구 정의로 과도한 컨텍스트를 소비하는 것을 방지하여 컨텍스트 비대화를 줄이고 상호 작용을 효율적으로 유지합니다.

## 슬래시 명령으로서의 MCP 프롬프트

MCP 서버는 Claude Code에서 슬래시 명령으로 나타나는 프롬프트를 노출할 수 있습니다. 프롬프트는 다음 명명 규칙을 사용하여 접근할 수 있습니다.

```
/mcp__<server>__<prompt>
```

예를 들어, `github`라는 서버가 `review`라는 프롬프트를 노출하는 경우 `/mcp__github__review`로 호출할 수 있습니다.

## 서버 중복 제거

동일한 MCP 서버가 여러 스코프(로컬, 프로젝트, 사용자)에 정의된 경우, 로컬 구성이 우선권을 가집니다. 이를 통해 충돌 없이 프로젝트 수준 또는 사용자 수준 MCP 설정을 로컬 사용자 지정으로 재정의할 수 있습니다.

## 최근 수명 주기 수정 사항 (v2.1.136)

v2.1.136에서 오랫동안 지속된 MCP 수명 주기 버그 두 가지가 수정되었습니다. 다중 서버 설정을 실행하는 경우 업그레이드할 가치가 있습니다.

-   **MCP 서버가 `/clear` 후에도 유지됩니다**: `.mcp.json`, 플러그인 또는 claude.ai 커넥터를 통해 구성된 서버는 VS Code, JetBrains 또는 Agent SDK에서 `/clear` 후 더 이상 사라지지 않습니다. 이전 버전은 자동으로 서버를 삭제하고 다시 시작해야 했습니다.
-   **OAuth 새로 고침 토큰 동시 새로 고침 수정**: 여러 서버가 동시에 새로 고침을 경쟁할 때 다중 서버 OAuth 설정에서 더 이상 새로 고침 토큰이 손실되지 않습니다. 이로써 여러 OAuth 보호 MCP 서버 설정에 영향을 미치던 "매일 아침 다시 인증해야 하는" 패턴이 사라집니다.

## @ 멘션을 통한 MCP 리소스

`@` 멘션 구문을 사용하여 프롬프트에서 MCP 리소스를 직접 참조할 수 있습니다.

```
@server-name:protocol://resource/path
```

예를 들어, 특정 데이터베이스 리소스를 참조하려면 다음과 같이 할 수 있습니다.

```
@database:postgres://mydb/users
```

이를 통해 Claude는 대화 컨텍스트의 일부로 MCP 리소스 콘텐츠를 인라인으로 가져와 포함할 수 있습니다.

## MCP 스코프

MCP 구성은 다양한 수준의 공유를 통해 여러 스코프에 저장될 수 있습니다.

| Scope | Location | Description | Shared With | Requires Approval |
|-------|----------|-------------|-------------|------------------|
| **Local** (기본값) | `~/.claude.json` (프로젝트 경로 아래) | 현재 사용자, 현재 프로젝트에만 비공개 (이전 버전에서는 `project`라고 불림) | 본인만 | 아니요 |
| **Project** | `.mcp.json` | git 저장소에 체크인됨 | 팀원 | 예 (첫 사용 시) |
| **User** | `~/.claude.json` | 모든 프로젝트에서 사용 가능 (이전 버전에서는 `global`이라고 불림) | 본인만 | 아니요 |

### 프로젝트 스코프 사용

프로젝트별 MCP 구성을 `.mcp.json`에 저장하세요.

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

팀원들은 프로젝트 MCP를 처음 사용할 때 승인 프롬프트를 보게 될 것입니다.

## MCP 구성 관리

### MCP 서버 추가

```bash
# Add HTTP-based server
claude mcp add --transport http github https://api.github.com/mcp

# Add local stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# List all MCP servers
claude mcp list

# Get details on specific server
claude mcp get github

# Remove an MCP server
claude mcp remove github

# Reset project-specific approval choices
claude mcp reset-project-choices

# Authenticate an MCP server from the CLI (v2.1.186+)
claude mcp login github

# Sign out of an MCP server (v2.1.186+)
claude mcp logout github

# Import from Claude Desktop
claude mcp add-from-claude-desktop
```

`claude mcp login <name>` / `claude mcp logout <name>`은 `/mcp` 메뉴의 OAuth 흐름과 상호 작용 없이 인증하거나 로그아웃하는 비대화형 방식입니다. `login`에 `--no-browser`를 추가하면 SSH 또는 헤드리스 세션에서 OAuth를 stdin을 통해 완료할 수 있습니다.

## 사용 가능한 MCP 서버 표

| MCP Server | Purpose | Common Tools | Auth | Real-time |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 파일 작업 | read, write, delete | OS 권한 | ✅ 예 |
| **GitHub** | 저장소 관리 | list_prs, create_issue, push | OAuth | ✅ 예 |
| **Slack** | 팀 커뮤니케이션 | send_message, list_channels | Token | ✅ 예 |
| **Database** | SQL 쿼리 | query, insert, update | 자격 증명 | ✅ 예 |
| **Google Docs** | 문서 접근 | read, write, share | OAuth | ✅ 예 |
| **Asana** | 프로젝트 관리 | create_task, update_status | API Key | ✅ 예 |
| **Stripe** | 결제 데이터 | list_charges, create_invoice | API Key | ✅ 예 |
| **Memory** | 영구 메모리 | store, retrieve, delete | 로컬 | ❌ 아니요 |

## 실제 예시

### 예시 1: GitHub MCP 구성

**파일:** `.mcp.json` (프로젝트 루트)

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

**사용 가능한 GitHub MCP 도구:**

#### Pull Request 관리
- `list_prs` - 저장소의 모든 PR 나열
- `get_pr` - diff를 포함한 PR 세부 정보 가져오기
- `create_pr` - 새 PR 생성
- `update_pr` - PR 설명/제목 업데이트
- `merge_pr` - PR을 메인 브랜치로 병합
- `review_pr` - 검토 의견 추가

**예시 요청:**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### 이슈 관리
- `list_issues` - 모든 이슈 나열
- `get_issue` - 이슈 세부 정보 가져오기
- `create_issue` - 새 이슈 생성
- `close_issue` - 이슈 닫기
- `add_comment` - 이슈에 댓글 추가

#### 저장소 정보
- `get_repo_info` - 저장소 세부 정보
- `list_files` - 파일 트리 구조
- `get_file_content` - 파일 내용 읽기
- `search_code` - 코드베이스 전체 검색

#### 커밋 작업
- `list_commits` - 커밋 기록
- `get_commit` - 특정 커밋 세부 정보
- `create_commit` - 새 커밋 생성

**설정**:
```bash
export GITHUB_TOKEN="your_github_token"
# Or use the CLI to add directly:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### 구성의 환경 변수 확장

MCP 구성은 대체 기본값과 함께 환경 변수 확장을 지원합니다. `${VAR}` 및 `${VAR:-default}` 구문은 `command`, `args`, `env`, `url`, `headers` 필드에서 작동합니다.

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

변수는 런타임에 확장됩니다.
- `${VAR}` - 환경 변수를 사용하며, 설정되지 않은 경우 오류 발생
- `${VAR:-default}` - 환경 변수를 사용하며, 설정되지 않은 경우 기본값으로 대체

### 예시 2: 데이터베이스 MCP 설정

**구성:**

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

**예시 사용법:**

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

**설정**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Or use the CLI to add directly:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### 예시 3: 다중 MCP 워크플로우

**시나리오: 일일 보고서 생성**

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

**설정**:
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# Add each MCP server via the CLI or configure them in .mcp.json
```

### 예시 4: 파일 시스템 MCP 작업

**구성:**

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

**사용 가능한 작업:**

| Operation | Command | Purpose |
|-----------|---------|---------|
| 파일 나열 | `ls ~/projects` | 디렉터리 내용 표시 |
| 파일 읽기 | `cat src/main.ts` | 파일 내용 읽기 |
| 파일 쓰기 | `create docs/api.md` | 새 파일 생성 |
| 파일 편집 | `edit src/app.ts` | 파일 수정 |
| 검색 | `grep "async function"` | 파일 내 검색 |
| 삭제 | `rm old-file.js` | 파일 삭제 |

**설정**:
```bash
# Use the CLI to add directly:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP vs Memory: 의사 결정 매트릭스

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

## 요청/응답 패턴

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

## 환경 변수

민감한 자격 증명은 환경 변수에 저장하세요.

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

그런 다음 MCP 구성에서 참조하세요.

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## MCP 서버로서의 Claude (claude mcp serve)

Claude Code 자체는 다른 애플리케이션을 위한 MCP 서버 역할을 할 수 있습니다. 이를 통해 외부 도구, 편집기 및 자동화 시스템이 표준 MCP 프로토콜을 통해 Claude의 기능을 활용할 수 있습니다.

```bash
# Start Claude Code as an MCP server on stdio
claude mcp serve
```

다른 애플리케이션은 다른 stdio 기반 MCP 서버와 마찬가지로 이 서버에 연결할 수 있습니다. 예를 들어, 다른 Claude Code 인스턴스에 Claude Code를 MCP 서버로 추가하려면 다음을 수행합니다.

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

이는 하나의 Claude 인스턴스가 다른 인스턴스를 조율하는 다중 에이전트 워크플로우를 구축하는 데 유용합니다.

## 관리형 MCP 구성 (엔터프라이즈)

엔터프라이즈 배포의 경우, IT 관리자는 `managed-mcp.json` 구성 파일을 통해 MCP 서버 정책을 적용할 수 있습니다. 이 파일은 조직 전체에서 어떤 MCP 서버가 허용되거나 차단되는지에 대한 독점적인 제어를 제공합니다.

**위치:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**특징:**
- `allowedMcpServers` -- 허용된 서버의 화이트리스트
- `deniedMcpServers` -- 금지된 서버의 블랙리스트
- `allowAllClaudeAiMcps` -- claude.ai 클라우드 MCP 커넥터의 조직 전체 로드를 허용하는 관리 설정 (v2.1.149 이상)
- 서버 이름, 명령 및 URL 패턴별 일치 지원
- 사용자 구성보다 우선적으로 적용되는 조직 전체 MCP 정책
- 승인되지 않은 서버 연결 방지

**예시 구성:**

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

> **참고:** `allowedMcpServers`와 `deniedMcpServers`가 모두 서버와 일치할 경우, 거부 규칙이 우선권을 가집니다.

## 플러그인 제공 MCP 서버

플러그인은 자체 MCP 서버를 번들로 제공하여 플러그인 설치 시 자동으로 사용할 수 있도록 합니다. 플러그인 제공 MCP 서버는 두 가지 방식으로 정의할 수 있습니다.

1.  **독립형 `.mcp.json`** -- 플러그인 루트 디렉토리에 `.mcp.json` 파일을 배치
2.  **`plugin.json` 내 인라인** -- 플러그인 매니페스트 내에서 직접 MCP 서버 정의

플러그인 설치 디렉토리에 상대적인 경로를 참조하려면 `${CLAUDE_PLUGIN_ROOT}` 변수를 사용하세요.

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

## 서브에이전트 스코프 MCP

MCP 서버는 에이전트 전면(frontmatter) 내 `mcpServers:` 키를 사용하여 인라인으로 정의할 수 있으며, 전체 프로젝트가 아닌 특정 서브에이전트로 범위가 지정됩니다. 이는 워크플로우의 다른 에이전트가 필요로 하지 않는 특정 MCP 서버에 에이전트가 접근해야 할 때 유용합니다.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

서브에이전트 스코프 MCP 서버는 해당 에이전트의 실행 컨텍스트 내에서만 사용할 수 있으며, 부모 또는 형제 에이전트와 공유되지 않습니다.

## MCP 출력 제한

Claude Code는 컨텍스트 오버플로우를 방지하기 위해 MCP 도구 출력에 제한을 적용합니다.

| Limit | Threshold | Behavior |
|-------|-----------|----------|
| **경고** | 10,000 토큰 | 출력이 크다는 경고가 표시됩니다. |
| **기본 최대값** | 25,000 토큰 | 이 제한을 초과하는 출력은 잘립니다. |
| **디스크 영속성** | 50,000 문자 | 5만 문자를 초과하는 도구 결과는 디스크에 영구적으로 저장됩니다. |

최대 출력 제한은 `MAX_MCP_OUTPUT_TOKENS` 환경 변수를 통해 구성할 수 있습니다.

```bash
# Increase the max output to 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## 코드 실행으로 컨텍스트 비대화 해결

MCP 채택이 확대됨에 따라 수십 개의 서버에 수백 또는 수천 개의 도구를 연결하는 것은 **컨텍스트 비대화**라는 심각한 문제를 야기합니다. 이것은 MCP가 대규모로 직면하는 가장 큰 문제이며, Anthropic의 엔지니어링 팀은 직접 도구 호출 대신 코드 실행을 사용하는 우아한 해결책을 제시했습니다.

> **출처**: [MCP를 사용한 코드 실행: 더 효율적인 에이전트 구축](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic 엔지니어링 블로그

### 문제: 토큰 낭비의 두 가지 원인

**1. 도구 정의가 컨텍스트 창을 과부하시킵니다.**

대부분의 MCP 클라이언트는 모든 도구 정의를 미리 로드합니다. 수천 개의 도구에 연결되면 모델은 사용자 요청을 읽기도 전에 수십만 개의 토큰을 처리해야 합니다.

**2. 중간 결과가 추가 토큰을 소비합니다.**

모든 중간 도구 결과는 모델의 컨텍스트를 통과합니다. Google Drive에서 Salesforce로 회의록을 전송하는 것을 생각해 보세요. 전체 회의록은 컨텍스트를 **두 번** 통과합니다. 한 번은 읽을 때, 또 한 번은 대상에 쓸 때입니다. 2시간짜리 회의록은 50,000개 이상의 추가 토큰을 의미할 수 있습니다.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### 해결책: 코드 API로서의 MCP 도구

도구 정의와 결과를 컨텍스트 창을 통해 전달하는 대신, 에이전트는 MCP 도구를 API로 호출하는 **코드를 작성**합니다. 코드는 샌드박스 실행 환경에서 실행되며, 최종 결과만 모델로 반환됩니다.

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

#### 작동 방식

MCP 도구는 타입이 지정된 함수들의 파일 트리로 제공됩니다.

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

각 도구 파일은 타입이 지정된 래퍼를 포함합니다.

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

에이전트는 도구를 조율하는 코드를 작성합니다.

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Data flows directly between tools — never through the model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**결과: 토큰 사용량이 약 150,000개에서 약 2,000개로 감소합니다. 이는 98.7% 감소한 수치입니다.**

### 주요 이점

| Benefit | Description |
|---------|-------------|
| **점진적 노출** | 에이전트는 모든 도구를 한 번에 로드하는 대신 파일 시스템을 탐색하여 필요한 도구 정의만 로드합니다. |
| **컨텍스트 효율적인 결과** | 데이터는 모델로 반환되기 전에 실행 환경에서 필터링/변환됩니다. |
| **강력한 제어 흐름** | 루프, 조건문 및 오류 처리가 모델을 왕복하지 않고 코드에서 실행됩니다. |
| **개인 정보 보호** | 중간 데이터 (PII, 민감한 기록)는 실행 환경에 남아 있으며 모델 컨텍스트에 절대 들어가지 않습니다. |
| **상태 영속성** | 에이전트는 중간 결과를 파일에 저장하고 재사용 가능한 스킬 함수를 구축할 수 있습니다. |

#### 예시: 대규모 데이터 세트 필터링

```typescript
// Without code execution — all 10,000 rows flow through context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// With code execution — filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only 5 rows reach the model
```

#### 예시: 왕복 없이 루프 실행

```typescript
// Poll for a deployment notification — runs entirely in code
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

### 고려할 절충안

코드 실행은 그 자체로 복잡성을 야기합니다. 에이전트 생성 코드를 실행하려면 다음이 필요합니다.

-   적절한 리소스 제한이 있는 **안전한 샌드박스 실행 환경**
-   실행된 코드에 대한 **모니터링 및 로깅**
-   직접 도구 호출에 비해 추가적인 **인프라 오버헤드**

토큰 비용 절감, 지연 시간 감소, 도구 구성 개선이라는 이점은 이러한 구현 비용과 비교하여 고려해야 합니다. MCP 서버가 몇 개만 있는 에이전트의 경우 직접 도구 호출이 더 간단할 수 있습니다. 대규모 에이전트(수십 개의 서버, 수백 개의 도구)의 경우 코드 실행은 상당한 개선입니다.

### MCPorter: MCP 도구 구성을 위한 런타임

[MCPorter](https://github.com/steipete/mcporter)는 상용구 없이 MCP 서버 호출을 실용적으로 만들고 선택적 도구 노출 및 유형화된 래퍼를 통해 컨텍스트 비대화를 줄이는 데 도움이 되는 TypeScript 런타임 및 CLI 툴킷입니다.

**해결하는 문제:** 모든 MCP 서버에서 모든 도구 정의를 미리 로드하는 대신, MCPorter는 필요에 따라 특정 도구를 검색, 검사 및 호출하여 컨텍스트를 간결하게 유지합니다.

**주요 기능:**

| Feature | Description |
|---------|-------------|
| **제로 구성 검색** | Cursor, Claude, Codex 또는 로컬 구성에서 MCP 서버를 자동으로 검색합니다. |
| **유형화된 도구 클라이언트** | `mcporter emit-ts`는 `.d.ts` 인터페이스와 즉시 실행 가능한 래퍼를 생성합니다. |
| **구성 가능한 API** | `createServerProxy()`는 `.text()`, `.json()`, `.markdown()` 도우미가 있는 camelCase 메서드로 도구를 노출합니다. |
| **CLI 생성** | `mcporter generate-cli`는 `--include-tools` / `--exclude-tools` 필터링을 통해 모든 MCP 서버를 독립형 CLI로 변환합니다. |
| **매개변수 숨기기** | 선택적 매개변수는 기본적으로 숨겨져 스키마의 장황함을 줄입니다. |

**설치:**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**예시 — TypeScript에서 도구 구성:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Data flows between tools without passing through the model context
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**예시 — CLI 도구 호출:**

```bash
# Call a specific tool directly
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# List available servers and tools
npx mcporter list
```

MCPorter는 위에서 설명한 코드 실행 접근 방식을 보완하여 MCP 도구를 유형화된 API로 호출하기 위한 런타임 인프라를 제공합니다. 이를 통해 중간 데이터를 모델 컨텍스트 외부에 유지하는 것을 간소화합니다.

## 모범 사례

### 보안 고려 사항

#### 해야 할 일 ✅
- 모든 자격 증명에 환경 변수를 사용하세요.
- 토큰 및 API 키를 정기적으로 (매월 권장) 교체하세요.
- 가능한 경우 읽기 전용 토큰을 사용하세요.
- MCP 서버 접근 범위를 필요한 최소한으로 제한하세요.
- MCP 서버 사용량 및 접근 로그를 모니터링하세요.
- 사용 가능한 경우 외부 서비스에 OAuth를 사용하세요.
- MCP 요청에 속도 제한을 구현하세요.
- 운영 환경에 배포하기 전에 MCP 연결을 테스트하세요.
- 모든 활성 MCP 연결을 문서화하세요.
- MCP 서버 패키지를 최신 상태로 유지하세요.

#### 하지 말아야 할 일 ❌
- 구성 파일에 자격 증명을 하드코딩하지 마세요.
- 토큰이나 비밀 정보를 Git에 커밋하지 마세요.
- 팀 채팅이나 이메일로 토큰을 공유하지 마세요.
- 팀 프로젝트에 개인 토큰을 사용하지 마세요.
- 불필요한 권한을 부여하지 마세요.
- 인증 오류를 무시하지 마세요.
- MCP 엔드포인트를 공개적으로 노출하지 마세요.
- root/관리자 권한으로 MCP 서버를 실행하지 마세요.
- 민감한 데이터를 로그에 캐시하지 마세요.
- 인증 메커니즘을 비활성화하지 마세요.

### 구성 모범 사례

1.  **버전 관리**: `.mcp.json`은 Git에 보관하되, 비밀 정보에는 환경 변수를 사용하세요.
2.  **최소 권한**: 각 MCP 서버에 필요한 최소한의 권한을 부여하세요.
3.  **격리**: 가능한 경우 다른 MCP 서버를 별도의 프로세스에서 실행하세요.
4.  **모니터링**: 감사 추적을 위해 모든 MCP 요청 및 오류를 기록하세요.
5.  **테스트**: 프로덕션 환경에 배포하기 전에 모든 MCP 구성을 테스트하세요.

### 성능 팁

- 자주 접근하는 데이터는 애플리케이션 수준에서 캐시하세요.
- 데이터 전송을 줄이기 위해 특정 MCP 쿼리를 사용하세요.
- MCP 작업의 응답 시간을 모니터링하세요.
- 외부 API에 대한 속도 제한을 고려하세요.
- 여러 작업을 수행할 때 배치 처리를 사용하세요.

## 설치 지침

### 전제 조건
- Node.js 및 npm 설치됨
- Claude Code CLI 설치됨
- 외부 서비스를 위한 API 토큰/자격 증명

### 단계별 설정

1.  CLI를 사용하여 **첫 번째 MCP 서버를 추가합니다** (예: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

    또는 프로젝트 루트에 `.mcp.json` 파일을 생성합니다:
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

2.  **환경 변수를 설정합니다:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3.  **연결을 테스트합니다:**
```bash
claude /mcp
```

4.  **MCP 도구를 사용합니다:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### 특정 서비스 설치

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**데이터베이스 MCP:**
```bash
npm install -g @modelcontextprotocol/server-database
```

**파일 시스템 MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP:**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## 문제 해결

### MCP 서버를 찾을 수 없음
```bash
# Verify MCP server is installed
npm list -g @modelcontextprotocol/server-github

# Install if missing
npm install -g @modelcontextprotocol/server-github
```

### 인증 실패
```bash
# Verify environment variable is set
echo $GITHUB_TOKEN

# Re-export if needed
export GITHUB_TOKEN="your_token"

# Verify token has correct permissions
# Check GitHub token scopes at: https://github.com/settings/tokens
```

### 연결 시간 초과
- 네트워크 연결 확인: `ping api.github.com`
- API 엔드포인트 접근 가능성 확인
- API의 속도 제한 확인
- 구성에서 시간 초과 값 늘려보기
- 방화벽 또는 프록시 문제 확인

### MCP 서버 충돌
- MCP 서버 로그 확인: `~/.claude/logs/`
- 모든 환경 변수가 설정되어 있는지 확인
- 적절한 파일 권한 확인
- MCP 서버 패키지 재설치 시도
- 동일한 포트에서 충돌하는 프로세스 확인

## 관련 개념

### Memory vs MCP
- **Memory**: 영구적이고 변하지 않는 데이터(기본 설정, 컨텍스트, 기록)를 저장합니다.
- **MCP**: 실시간으로 변하는 데이터(API, 데이터베이스, 실시간 서비스)에 접근합니다.

### 각각을 사용하는 시기
- **Memory 사용 시기**: 사용자 기본 설정, 대화 기록, 학습된 컨텍스트
- **MCP 사용 시기**: 현재 GitHub 이슈, 실시간 데이터베이스 쿼리, 실시간 데이터

### 다른 Claude 기능과의 통합
- 풍부한 컨텍스트를 위해 MCP를 Memory와 결합
- 더 나은 추론을 위해 프롬프트에서 MCP 도구 사용
- 복잡한 워크플로우를 위해 여러 MCP 활용

## 추가 자료

- [공식 MCP 문서](https://code.claude.com/docs/en/mcp)
- [MCP 프로토콜 사양](https://modelcontextprotocol.io/specification)
- [MCP GitHub 저장소](https://github.com/modelcontextprotocol/servers)
- [사용 가능한 MCP 서버](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — 상용구 없이 MCP 서버를 호출하기 위한 TypeScript 런타임 및 CLI
- [MCP를 사용한 코드 실행](https://www.anthropic.com/engineering/code-execution-with-mcp) — 컨텍스트 비대화 해결에 대한 Anthropic의 엔지니어링 블로그
- [Claude Code CLI 참조](https://code.claude.com/docs/en/cli-reference)
- [Claude API 문서](https://docs.anthropic.com)

---

**최종 업데이트**: 2026년 6월 28일
**Claude Code 버전**: 2.1.195
**출처**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://docs.anthropic.com/en/docs/claude-code/mcp
**호환 모델**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
