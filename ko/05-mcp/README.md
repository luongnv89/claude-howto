<!-- i18n-source: 05-mcp/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
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
# 기본 HTTP 연결
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 인증 헤더를 포함한 HTTP
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio 전송 (로컬)

로컬에서 실행되는 MCP 서버의 경우:

```bash
# 로컬 Node.js 서버
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# 환경 변수 사용
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

#### stdio 서버용 `CLAUDE_PROJECT_DIR` (v2.1.139 이상)

모든 MCP stdio 서버는 환경에 `CLAUDE_PROJECT_DIR=<저장소 루트의 절대 경로>`가 이미 설정된 상태로 생성됩니다. 이는 훅에 사용되는 것과 동일한 규칙입니다. 플러그인 및 프로젝트의 `.mcp.json` 파일은 `command`, `args`, `env` 값에서 `${CLAUDE_PROJECT_DIR}`를 참조할 수 있으며, 이 대체는 `execve()` 전에 이루어집니다.

```json
{
  "mcpServers": {
    "repo-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["${CLAUDE_PROJECT_DIR:-.}/.claude/mcp/repo-tools.js"],
      "env": {
        "REPO_ROOT": "${CLAUDE_PROJECT_DIR:-.}"
      }
    }
  }
}
```

> **참고**: 프로젝트, 로컬, 사용자 구성에서는 `${CLAUDE_PROJECT_DIR:-.}`처럼 기본값과 함께 작성하십시오. 이 변수는 Claude Code 자체의 환경이 아니라 서버의 환경에 설정되기 때문입니다. `${CLAUDE_PROJECT_DIR}`를 직접 치환하는 것은 플러그인 MCP 구성뿐입니다.

Claude Code가 어디에서 실행되었는지에 관계없이 stdio 서버가 프로젝트 루트에 상대적인 파일을 읽어야 할 때 이 기능을 사용하세요.

stdio MCP 서버는 또한 `CLAUDE_CODE_SESSION_ID`를 수신합니다(훅 및 Bash에 전달된 값과 일치). 세션이 `--resume`으로 재개될 때도 마찬가지입니다(v2.1.163 이상).

### SSE 전송 (지원 중단)

Server-Sent Events 전송은 `http` 방식에 비해 사용이 중단되었지만 여전히 지원됩니다.

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### WebSocket 전송 (`ws`)

WebSocket 서버는 지속적인 양방향 연결을 유지하므로, 요청 없이도 Claude에게 이벤트를 푸시하는 원격 MCP 서버에 적합합니다. 서버가 요청에 응답만 한다면 HTTP를 사용하십시오. HTTP는 OAuth와 `claude mcp add --transport` 플래그를 지원하지만 WebSocket은 둘 다 지원하지 않습니다.

`--transport`는 `ws`를 받지 않으므로 `.mcp.json`이나 `claude mcp add-json`으로 구성합니다.

```json
{
  "type": "ws",
  "url": "wss://mcp.example.com/socket",
  "headers": {
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
```

`type: "ws"` 항목은 `http`와 같은 `url`, `headers`, `headersHelper`, `timeout`, `alwaysLoad` 필드를 받습니다. 인증은 **헤더 방식만** 지원하며, WebSocket 서버에는 OAuth 흐름이 없습니다.

> **참고**: v2.1.285부터 `claude mcp list`는 WebSocket(`ws`) 서버를 URL 및 상태와 함께 표시합니다(이전 버전에서는 목록에서 빠졌습니다). `claude mcp get <name>`이나 `/mcp` 패널로도 확인할 수 있습니다.

HTTP 및 SSE와 마찬가지로 WebSocket 연결도 5분의 유휴 시간 창을 사용하며, stdio와 WebSocket에는 요청별 타이머가 없습니다. `type` 없이 `url`만 있는 항목은 오류가 되며, 오류 메시지는 `"http"`, `"sse"`, `"ws"`를 유효한 값으로 안내합니다.

### 세션 작업 디렉터리 (roots/list)

MCP 서버는 세션의 작업 디렉터리를 확인할 수 있습니다. 실행 디렉터리와 모든 `--add-dir`/`additionalDirectories` 항목이 MCP `roots/list` 요청으로 반환되며, 이 집합이 바뀔 때마다 `notifications/roots/list_changed` 알림이 전송됩니다(v2.1.203). 유휴 타임아웃은 이제 stdio 서버에도 적용되며(30분), 서버별 `timeout`이 유휴 하한으로 동작합니다(v2.1.203).

### Windows 관련 참고 사항

네이티브 Windows(WSL 아님)에서는 npx 명령어에 `cmd /c`를 사용하세요.

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### OAuth 2.0 인증

Claude Code는 OAuth 2.0이 필요한 MCP 서버를 지원합니다. OAuth를 사용하는 서버에 연결할 때 Claude Code는 전체 인증 흐름을 처리합니다.

```bash
# OAuth를 지원하는 MCP 서버에 연결(대화형 흐름)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# 비대화형 설정을 위해 OAuth 자격 증명을 미리 구성
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

> **경고** (v2.1.238): 프로젝트 `.mcp.json`의 `headersHelper`와, 프로젝트 또는 `--add-dir` 에이전트 파일의 인라인 MCP 서버는 이제 `claude -p`에서도 해당 폴더의 신뢰 대화상자가 수락되어 있어야 합니다. 이런 도우미는 또한 **상속된 자격 증명 환경 변수 없이** 실행되며, 사용자·관리형·claude.ai 범위의 도우미는 대신 Claude 구성 디렉터리에서 실행됩니다. 상속된 자격 증명이나 신뢰되지 않은 상태의 실행에 의존하던 프로젝트 구성은 신뢰 대화상자를 수락하고 다른 방식으로 자격 증명을 제공할 때까지 동작하지 않습니다.

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

### `/mcp` 명령어

세션 내에서 `/mcp`를 입력하여 연결된 서버를 나열하고, OAuth 흐름을 트리거하며, 연결 상태를 검사할 수 있습니다.

- **v2.1.121부터**, MCP는 일시적인 오류 발생 시 초기 연결을 최대 3번 재시도합니다.
- **v2.1.128부터**, `/mcp`는 연결된 각 서버의 **도구 개수**를 표시하고 **0개 도구**를 보고하는 서버를 시각적으로 표시하여 잘못 구성된 서버를 한눈에 알아볼 수 있도록 합니다.

## MCP 도구 검색

도구 검색은 기본적으로 켜져 있습니다. MCP 도구는 지연 로드되어 필요할 때 검색되므로, 도구 정의가 모델 컨텍스트를 채우지 않습니다. v2.1.304부터는 사용자 지정 `ANTHROPIC_BASE_URL` 게이트웨이 뒤에서도 켜진 상태로 유지되며, 게이트웨이는 `defer_loading` 도구 필드와 `tool_reference` 블록을 전달해야 합니다. v2.1.305부터 Claude Code는 게이트웨이가 400 또는 422로 거부한 요청을 도구 검색 없이 다시 시도합니다. 모든 도구를 미리 로드하고 이런 거부 요청을 건너뛰려면 `ENABLE_TOOL_SEARCH=false`를 설정하십시오. v2.1.304 이전에는 `ENABLE_TOOL_SEARCH`가 `true`, `auto`, `auto:N` 중 하나가 아니면 게이트웨이 뒤에서 도구 검색이 꺼져 있었습니다.

| 설정 | 값 | 설명 |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | (설정 안 함 — 기본값) | 모든 MCP 도구를 지연시키고 필요할 때 로드합니다 |
| `ENABLE_TOOL_SEARCH` | `auto` | 임계값 모드: 도구 정의가 컨텍스트 창의 10%에 도달할 때까지는 미리 로드하고, 그 이후에는 모두 지연시킵니다 |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | 사용자 지정 비율(0-100)을 쓰는 임계값 모드입니다. 예: 5%이면 `auto:5` |
| `ENABLE_TOOL_SEARCH` | `true` | 모든 MCP 도구를 지연시킵니다 |
| `ENABLE_TOOL_SEARCH` | `false` | 비활성화됩니다. 모든 도구 설명이 전체로 전송됩니다 |

> **참고:** 도구 검색에는 `tool_reference` 블록을 지원하는 모델이 필요합니다: Claude Opus 4, Claude Sonnet 4, Claude Haiku 4.5 및 이후 모델(Google Cloud의 Agent Platform에서는 Opus 4.5, Sonnet 4.5, Haiku 4.5 이후).

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

서버의 모든 도구를 도구 검색 뒤에 두려면 해당 서버 항목에 `"alwaysLoad": false`를 설정하십시오(v2.1.287 이상). 여기에는 서버 작성자가 미리 로드하도록 표시한 도구도 포함됩니다. `alwaysLoad`를 생략하면 그렇게 표시된 도구는 미리 로드됩니다. 서버 작성자는 개별 도구의 `_meta` 객체에 `"anthropic/alwaysLoad"`를 설정하여 도구를 표시하며, 구성의 서버 수준 `alwaysLoad` 설정으로 이를 재정의할 수 있습니다.

서버 작성자 참고: 두 번 호출해도 안전한 도구는 `tools/list` 항목에 `idempotentHint` 또는 `readOnlyHint` 어노테이션으로 표시하십시오. v2.1.307부터 Claude Code는 HTTP 또는 claude.ai 커넥터 연결이 닫혔을 때 대기 중이던 호출을 이런 도구에 대해서만 반복하며, 그 밖의 호출은 `connection closed before the tool call was answered`로 실패합니다.

## 동적 도구 업데이트

Claude Code는 MCP `list_changed` 알림을 지원합니다. MCP 서버가 사용 가능한 도구를 동적으로 추가, 제거 또는 수정하면 Claude Code는 업데이트를 수신하고 도구 목록을 자동으로 조정합니다. 재연결이나 다시 시작이 필요 없습니다.

## MCP 앱

MCP 앱은 최초의 공식 MCP 확장으로, MCP 도구 호출이 채팅 인터페이스에 직접 렌더링되는 대화형 UI 구성 요소를 반환할 수 있도록 합니다. 일반 텍스트 응답 대신 MCP 서버는 대화에서 벗어나지 않고도 풍부한 대시보드, 양식, 데이터 시각화 및 다단계 워크플로를 인라인으로 제공할 수 있습니다.

## MCP 정보 요청(Elicitation)

MCP 서버는 대화형 대화상자를 통해 사용자에게 구조화된 입력을 요청할 수 있습니다(v2.1.49 이상). 이를 통해 MCP 서버는 워크플로 중간에 추가 정보를 요청할 수 있습니다. 예를 들어, 확인을 요청하거나, 옵션 목록에서 선택하거나, 필수 필드를 채워 MCP 서버 상호 작용에 대화형 기능을 추가할 수 있습니다.

## 도구 설명 및 지침 상한

Claude Code는 장황한 서버가 컨텍스트를 비대하게 만들지 않도록 각 MCP 도구 설명과 각 서버의 지침을 잘라냅니다. 기본 한도는 서버 지침과 미리 로드되는 도구의 설명에 대해 **4,096자**(v2.1.296, 그 전에는 v2.1.84부터 2,048자), 도구 검색으로 Claude가 로드하는 설명에 대해 **16,384자**(v2.1.295)입니다. v2.1.280부터 `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`로 이 한도를 재정의할 수 있으며, 설정한 값이 **두** 한도를 모두 대체합니다(`8192`는 짧은 한도를 늘리고 긴 한도를 줄입니다). v2.1.299부터 `api.anthropic.com`에 있는 Anthropic 퍼스트 파티 MCP 서버의 설명과 지침은 Claude에게 전체가 전달됩니다. 중요한 내용은 설명의 앞부분에 두십시오.

## 슬래시 명령어로서의 MCP 프롬프트

MCP 서버는 Claude Code에서 슬래시 명령어로 나타나는 프롬프트를 노출할 수 있습니다. 프롬프트는 다음 명명 규칙을 사용하여 접근할 수 있습니다.

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

| 스코프 | 플래그 | 위치 | 설명 | 공유 대상 | 승인 필요 |
|-------|------|----------|-------------|-------------|------------------|
| **Local** (기본값) | `--scope local` | `~/.claude.json` (프로젝트 경로 아래) | 현재 사용자, 현재 프로젝트에만 비공개 (이전 버전에서는 `project`라고 불림) | 본인만 | 아니요 |
| **Project** | `--scope project` | `.mcp.json` | git 저장소에 체크인됨 | 팀원 | 예 (첫 사용 시) |
| **User** | `--scope user` | `~/.claude.json` | 모든 프로젝트에서 사용 가능 (이전 버전에서는 `global`이라고 불림) | 본인만 | 아니요 |

서버를 추가할 때 `--scope`(짧은 형식 `-s`)로 스코프를 선택합니다. 생략하면
Claude Code는 `local`을 사용합니다.

```bash
# 프로젝트 스코프 — .mcp.json에 기록되어 팀과 공유됨
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# 사용자 스코프 — 모든 프로젝트에서 사용 가능
claude mcp add --scope user --transport stdio memory -- npx @modelcontextprotocol/server-memory
```

### 프로젝트 스코프 사용

프로젝트별 MCP 구성을 `.mcp.json`에 저장하세요.

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

팀원들은 프로젝트 MCP를 처음 사용할 때 승인 프롬프트를 보게 됩니다. 신뢰되지 않은 워크스페이스에서는 저장소가 커밋된 `.claude/settings.json`으로 스스로 승인한 서버를 `claude mcp list`/`get`이 자동으로 실행하지 **않습니다**. 이런 서버는 신뢰 대화상자를 수락할 때까지 `⏸ Pending approval`로 표시되며, 신뢰되지 않은 폴더에서는 `enableAllProjectMcpServers`가 무시됩니다(v2.1.196).

## MCP 구성 관리

### MCP 서버 추가

```bash
# HTTP 기반 서버 추가
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# 로컬 stdio 서버 추가
claude mcp add --transport stdio database -- npx @company/db-server

# 모든 MCP 서버 나열
claude mcp list

# 특정 서버의 세부 정보 확인
claude mcp get github

# MCP 서버 제거
claude mcp remove github

# 프로젝트별 승인 선택 초기화
claude mcp reset-project-choices

# CLI에서 MCP 서버 인증(v2.1.186+)
claude mcp login github

# MCP 서버에서 로그아웃(v2.1.186+)
claude mcp logout github

# Claude Desktop에서 가져오기
claude mcp add-from-claude-desktop

# JSON 블롭으로 서버 추가(스크립트 설정에 유용)
claude mcp add-json events-server '{"type":"stdio","command":"npx","args":["@modelcontextprotocol/server-events"]}'
```

> **참고**: JSON 구성(`.mcp.json`, `~/.claude.json`, `claude mcp add-json`)에서 `type` 필드는 `http`의 별칭으로 `streamable-http`를 받습니다. MCP 사양은 이 전송을 `streamable-http`라고 부르므로, 서버 자체 문서에서 복사한 구성을 수정 없이 사용할 수 있습니다.

v2.1.238부터 `claude mcp list`와 `claude mcp get`은 비활성화된 서버를 상태 확인을 위해 연결하지 않고 `⊘ Disabled`로 표시합니다.

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
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
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
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
# 또는 CLI로 직접 추가:
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
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
- `${VAR}` - 환경 변수를 사용합니다. 설정되지 않았고 기본값도 없으면 서버는 문자 그대로의 `${VAR}`로 로드되며, `claude mcp list`와 `/mcp`가 누락된 변수에 대해 경고합니다
- `${VAR:-default}` - 환경 변수를 사용하며, 설정되지 않은 경우 기본값으로 대체

### 예시 2: 데이터베이스 MCP 설정

**구성:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DATABASE_URL}"]
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
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --dsn "$DATABASE_URL"
```

> **경고**: 이 설정은 Claude에게 쓰기 권한을 줍니다. 읽기 전용 모드를 켜지 않으면 DBHub의 `execute_sql` 도구는 `UPDATE`, `DELETE`, `DROP`을 포함해 받은 SQL을 모두 실행합니다. 로컬 또는 일회용 데이터베이스를 사용하고, 프로덕션 데이터베이스에는 절대 사용하지 마십시오.

**읽기 전용 설정(권장):**

`SELECT`만 실행할 수 있는 데이터베이스 사용자를 만듭니다(PostgreSQL 예시).

```sql
CREATE ROLE claude_readonly LOGIN PASSWORD 'change-me';
GRANT CONNECT ON DATABASE mydb TO claude_readonly;
GRANT USAGE ON SCHEMA public TO claude_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_readonly;
```

`dbhub.toml`에서 읽기 전용 모드를 켭니다. 예전의 `--readonly` 플래그는 더 이상 동작하지 않습니다. DBHub가 환경에서 `${DATABASE_URL}`을 채우므로 파일에 자격 증명을 넣지 않아도 됩니다.

```toml
[[sources]]
id = "default"
dsn = "${DATABASE_URL}"

[[tools]]
name = "execute_sql"
source = "default"
readonly = true
```

그런 다음 `--dsn`을 전달하는 대신 DBHub가 이 파일을 가리키도록 합니다. Claude Code는 같은 이름의 서버를 두 번 추가하지 않으므로, 먼저 위에서 추가한 쓰기 권한 `database` 서버를 제거하십시오.

```bash
# 위에서 추가한 쓰기 권한 서버를 교체
claude mcp remove database
export DATABASE_URL="postgresql://claude_readonly:change-me@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --config "$PWD/dbhub.toml"
```

읽기 전용 모드는 SQL 텍스트를 필터링하는 방식이며 과거에 우회 사례가 있었으므로(DBHub 0.22.6에서 수정), 실제로 데이터를 보호하는 것은 `SELECT` 전용 사용자입니다. [DBHub 읽기 전용 모드](https://dbhub.ai/tools/execute-sql#read-only-mode)를 참고하십시오.

### 예시 3: 다중 MCP 워크플로

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
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your_slack_bot_token"
export SLACK_TEAM_ID="your_slack_team_id"
# 각 MCP 서버를 CLI로 추가하거나 .mcp.json에 구성
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
# CLI로 직접 추가:
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
# ~/.bashrc 또는 ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"
```

그런 다음 MCP 구성에서 참조하세요.

```json
{
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
  }
}
```

## MCP 서버로서의 Claude (`claude mcp serve`)

Claude Code 자체는 다른 애플리케이션을 위한 MCP 서버 역할을 할 수 있습니다. 이를 통해 외부 도구, 편집기 및 자동화 시스템이 표준 MCP 프로토콜을 통해 Claude의 기능을 활용할 수 있습니다.

```bash
# Claude Code를 stdio 기반 MCP 서버로 시작
claude mcp serve
```

다른 애플리케이션은 다른 stdio 기반 MCP 서버와 마찬가지로 이 서버에 연결할 수 있습니다. 예를 들어, 다른 Claude Code 인스턴스에 Claude Code를 MCP 서버로 추가하려면 다음을 수행합니다.

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

이는 하나의 Claude 인스턴스가 다른 인스턴스를 조율하는 다중 에이전트 워크플로를 구축하는 데 유용합니다.

## 관리형 MCP 구성 (엔터프라이즈)

엔터프라이즈 배포의 경우, IT 관리자는 두 가지 별개의 메커니즘으로 MCP 서버 정책을 적용합니다. 하나는 고정된 서버 집합을 배포하고 독점적으로 제어하는 `managed-mcp.json` 파일이고, 다른 하나는 구성된 서버 중 어떤 서버를 로드할 수 있는지 필터링하는 `allowedMcpServers` / `deniedMcpServers` 설정 키입니다.

**위치:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux 및 WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

`managed-mcp.json`은 프로젝트 `.mcp.json`과 같은 형식(최상위 `mcpServers` 맵)을 사용합니다. 이 파일은 서버를 배포할 뿐, 필터링하지는 않습니다.

```json
{
  "mcpServers": {
    "example-remote": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"]
    }
  }
}
```

시스템의 모든 사용자가 이 파일을 읽을 수 있으므로 `env` 블록에 자격 증명을 절대 넣지 마십시오. 대신 `${VAR}` 확장, OAuth, `headersHelper`를 사용하십시오.

> **참고 (v2.1.305):** `managed-mcp.json`의 서버에는 `allowedMcpServers` 항목이 필요하지 않습니다. 허용 목록은 관리형 서버가 `env` 밖에서 `${VAR}` 확장을 사용할 때만 검사합니다. v2.1.305 이전에는 `env` 안에서만 `${VAR}`를 사용한 서버도 검사했습니다. 이런 서버를 막기 위해 `allowedMcpServers`에 의존했다면, 업그레이드 후 프롬프트 없이 로드되므로 대신 `deniedMcpServers` 항목을 추가하십시오.

**필터링: 허용 목록과 거부 목록**

`allowedMcpServers`, `deniedMcpServers`, `allowAllClaudeAiMcps`는 **`managed-mcp.json`의 필드가 아니라 설정 키**입니다. 강제 적용하려면 관리형 설정 소스(서버 관리형 설정, `managed-settings.json`, MDM 프로필, 레지스트리)에 넣으십시오.

- `allowedMcpServers` -- 허용된 서버의 허용 목록입니다. 같은 관리형 소스에 `allowManagedMcpServersOnly: true`를 함께 설정하십시오. 그렇지 않으면 허용 목록이 모든 스코프에서 병합되어 사용자가 목록을 넓힐 수 있습니다.
- `deniedMcpServers` -- 차단된 서버의 거부 목록입니다. 어떤 경우에도 모든 스코프에서 병합됩니다.
- `allowAllClaudeAiMcps` -- 배포된 `managed-mcp.json`과 함께 claude.ai 클라우드 커넥터를 로드합니다(v2.1.149 이상). 관리자가 제어하는 정책 계층에서만 읽습니다.

각 항목은 **하나의** 키만 가진 객체입니다.

| 키 | 매칭 대상 |
|-----|---------|
| `serverUrl` | 원격 서버 URL(정확히 일치하거나 `*` 와일드카드 사용) |
| `serverCommand` | stdio 서버를 시작하는 정확한 명령어와 인수를 배열로 지정합니다(모든 인수를 순서대로) |
| `serverName` | 사용자가 지정한 레이블입니다. **정확히 일치하는 경우만 매칭되며 와일드카드는 확장되지 않습니다** |

**예시 구성:**

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.example.com/*" },
    { "serverCommand": ["/usr/local/bin/company-mcp-server", "--config", "/etc/company/mcp-config.json"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" },
    { "serverUrl": "http://*" }
  ],
  "allowManagedMcpServersOnly": true
}
```

세 번째 관리형 설정인 `managedMcpServers`(v2.1.259 이상)를 사용하면 조직이 모든 사용자에게 HTTP/SSE MCP 서버를 제공할 수 있습니다. 항목은 `.mcp.json`과 같은 형태이며, 실행할 명령어를 지정한 항목은 건너뜁니다.

> **참고:** `allowedMcpServers`와 `deniedMcpServers`가 모두 서버와 일치할 경우, 거부 규칙이 우선권을 가집니다.

## 플러그인 제공 MCP 서버

플러그인은 자체 MCP 서버를 번들로 제공하여 플러그인 설치 시 자동으로 사용할 수 있도록 합니다. 플러그인 제공 MCP 서버는 두 가지 방식으로 정의할 수 있습니다.

1.  **독립형 `.mcp.json`** -- 플러그인 루트 디렉터리에 `.mcp.json` 파일을 배치
2.  **`plugin.json` 내 인라인** -- 플러그인 매니페스트 내에서 직접 MCP 서버 정의

플러그인 설치 디렉터리에 상대적인 경로를 참조하려면 `${CLAUDE_PLUGIN_ROOT}` 변수를 사용하세요.

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

MCP 서버는 에이전트 전면(frontmatter) 내 `mcpServers:` 키를 사용하여 인라인으로 정의할 수 있으며, 전체 프로젝트가 아닌 특정 서브에이전트로 범위가 지정됩니다. 이는 워크플로의 다른 에이전트가 필요로 하지 않는 특정 MCP 서버에 에이전트가 접근해야 할 때 유용합니다.

```yaml
---
name: my-tool-agent
description: Uses my-tool for specialized operations
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
| **기본 최대값** | 25,000 토큰 | 이보다 큰 출력은 파일로 저장되고, 대화에는 대신 파일 경로가 들어갑니다. |
| **디스크 영속성** | 50,000 문자 | 5만 문자를 초과하는 도구 결과는 디스크에 영구적으로 저장됩니다. |

최대 출력 제한은 `MAX_MCP_OUTPUT_TOKENS` 환경 변수를 통해 구성할 수 있습니다.

```bash
# 최대 출력을 50,000 토큰으로 늘리기
export MAX_MCP_OUTPUT_TOKENS=50000
```

## 오래 실행되는 도구 호출의 자동 백그라운드 전환 (v2.1.212)

2분보다 오래 실행되는 MCP 도구 호출은 이제 자동으로 백그라운드로 이동하므로, 느린 도구 때문에 세션이 막히지 않고 계속 사용할 수 있습니다. 임계값은 `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`로 구성할 수 있으며, 이를 통해 동작을 조정하거나 비활성화할 수 있습니다.

```bash
# 자동 백그라운드 전환 임계값을 5분(300,000ms)으로 변경
export CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=300000
```

`0`으로 설정하면 자동 백그라운드 전환이 꺼집니다. `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`은 백그라운드 명령어 및 백그라운드 서브에이전트와 함께 이 기능을 끕니다. 호출 실행 시간을 제한하려면 서버별 `timeout`(밀리초, 실제 경과 시간 기준의 엄격한 한도)을 추가하거나 모든 서버에 대해 `MCP_TOOL_TIMEOUT`(기본값 약 28시간)을 설정하십시오.

### MCP 작업 (공개 베타, v2.1.304 이상)

MCP tasks 확장을 지원하는 서버는 긴 작업을 직접 실행할 수 있습니다. 서버가 작업을 수락하는 즉시 Claude의 도구 호출이 반환되고, 하단에 `1 MCP task` 같은 개수가 표시되며, 작업이 끝나면 Claude가 결과를 받습니다. `/tasks`에서 `x`로 작업을 중지할 수 있습니다. 원격 서버의 작업은 종료한 뒤에도 계속 실행되며, 같은 세션을 재개하면 다시 추적할 수 있습니다. 작업을 사용하려면 프로토콜 리비전 2026-07-28, 기능 플래그 가져오기(따라서 Bedrock, Vertex, Foundry 또는 텔레메트리를 끈 환경은 불가), 그리고 터미널 CLI, Agent SDK 또는 GitHub Actions 세션이 필요합니다. 비대화형 실행에서는 Agent SDK 또는 `claude -p --input-format stream-json`에서만 사용할 수 있으며, 둘 다 `CLAUDE_AUTO_BACKGROUND_TASKS=1`이 필요합니다(일반 `claude -p "<prompt>"`에서는 사용할 수 없음). VS Code와 데스크톱 앱에서는 사용할 수 없으며, 서브에이전트의 호출은 작업이 되지 않습니다. Claude가 작업 결과를 기다리게 하려면 `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1`을 설정하십시오(모든 MCP 호출을 기다리게 하려면 `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=0`).

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

// 데이터는 도구 사이를 직접 흐르며 모델을 거치지 않음
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
// 코드 실행 없이 — 10,000개 행이 모두 컨텍스트를 통과
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> 컨텍스트에 10,000개 행을 반환

// 코드 실행 사용 — 실행 환경에서 필터링
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // 모델에는 5개 행만 전달됨
```

#### 예시: 왕복 없이 루프 실행

```typescript
// 배포 알림을 폴링 — 전부 코드 안에서 실행
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
npx mcporter list          # 설치 불필요 — 서버를 즉시 검색
pnpm add mcporter          # 프로젝트에 추가
brew install steipete/tap/mcporter  # Homebrew로 macOS에 설치
```

**예시 — TypeScript에서 도구 구성:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// 데이터가 모델 컨텍스트를 거치지 않고 도구 사이를 흐름
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**예시 — CLI 도구 호출:**

```bash
# 특정 도구를 직접 호출
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# 사용 가능한 서버와 도구 나열
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
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

   또는 프로젝트 루트에 `.mcp.json` 파일을 생성합니다:
```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

2.  **환경 변수를 설정합니다:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_personal_access_token"
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
npm install -g @bytebase/dbhub
```

**파일 시스템 MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP(지원 중단(deprecated)된 패키지):**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## 문제 해결

### 오류 출력부터 확인하기 (v2.1.219 이상)

서버가 연결되지 않으면 무엇이든 변경하기 전에 `claude mcp list`(또는 세션 안에서 `/mcp`)를 실행하십시오. 이제 Claude Code는 실패한 서버 옆에 **HTTP 상태 코드와 서버의 오류 텍스트**를 출력하므로, 일반적인 "failed to connect" 대신 `401 Unauthorized`나 `404 Not Found`를 확인할 수 있습니다.

```bash
# 연결 상태와 함께 실패 시 HTTP 상태 및 오류 텍스트 표시
claude mcp list
```

먼저 상태를 읽으십시오. 어떤 해결책을 적용할지 알려 줍니다.

- `401` / `403` → 잘못되었거나 만료된 자격 증명입니다. `claude mcp login <name>`으로 다시 인증하십시오
- `404` → 잘못된 URL입니다(`/mcp` 또는 `/sse` 경로 접미사 누락이 흔한 원인)
- `5xx` / 타임아웃 → 원격 서버가 다운된 상태입니다. [연결 시간 초과](#연결-시간-초과)를 참고하십시오

### 구성 값의 숨은 공백 (v2.1.219 이상)

Claude Code는 MCP 구성 값에 **앞뒤 공백**이 있으면 경고합니다. 이는 흔하면서도 찾기 어려운 인증 실패 원인입니다. 브라우저나 채팅 메시지에서 복사해 붙여 넣은 토큰에는 끝에 공백이나 줄바꿈이 붙어 있는 경우가 많으며, 이 값이 `Authorization` 헤더에 그대로 전송되어 잘못된 자격 증명으로 실패합니다.

이 경고가 표시되면 `.mcp.json`의 값(또는 확장 원본인 환경 변수)을 다시 확인하고 공백을 제거하십시오.

```bash
# 구분자 사이에 숨은 앞뒤 공백을 드러냄
printf '[%s]\n' "$GITHUB_PERSONAL_ACCESS_TOKEN"
```

### 헤드리스 실행에서 건너뛴 서버 (v2.1.219 이상)

`--mcp-config`로 전달한 서버 중 구성 검증에 실패한 서버는 실행을 중단시키는 대신 **건너뛰므로**, 헤드리스 스크립트가 도구의 절반이 빠진 채로 정상 동작하는 것처럼 보일 수 있습니다. 이제 Claude Code는 어떤 서버가 빠졌는지 보고합니다.

- **헤드리스 / `-p` 실행**: stream-json `init` 이벤트에 건너뛴 모든 항목을 나열하는 `mcp_server_errors` 필드가 포함됩니다. 실행 결과를 신뢰하기 전에 확인하십시오.
- **대화형 터미널 실행**: 같은 문제가 세션 시작 시 시작 경고로 출력됩니다.

```bash
# 헤드리스 실행에서 건너뛴 --mcp-config 항목 확인
claude -p "list my tools" --mcp-config ./servers.json \
  --output-format stream-json --verbose \
  | jq -r 'select(.type == "system" and .subtype == "init") | .mcp_server_errors'
```

### MCP 서버를 찾을 수 없음
```bash
# MCP 서버 설치 여부 확인
npm list -g @modelcontextprotocol/server-github

# 없으면 설치
npm install -g @modelcontextprotocol/server-github
```

### 인증 실패
```bash
# 환경 변수 설정 여부 확인
echo $GITHUB_PERSONAL_ACCESS_TOKEN

# 필요하면 다시 export
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"

# 토큰 권한이 올바른지 확인
# GitHub 토큰 스코프 확인: https://github.com/settings/tokens
```

### 연결 시간 초과
- 네트워크 연결 확인: `ping api.github.com`
- API 엔드포인트 접근 가능성 확인
- API의 속도 제한 확인
- 구성 항목에서 서버의 `timeout`(밀리초)을 늘리거나, 모든 서버에 대해 `MCP_TOOL_TIMEOUT`을 늘려 보기
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
- 복잡한 워크플로를 위해 여러 MCP 활용

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

**최종 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/managed-mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/mcp#configure-tool-search
- https://code.claude.com/docs/en/env-vars
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/mcp#tool-search-for-mcp-server-authors
- https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/changelog#2-1-305
- https://code.claude.com/docs/en/mcp#tool-search-through-an-llm-gateway
- https://code.claude.com/docs/en/managed-mcp#how-allowlists-and-denylists-apply-to-the-managed-set
- https://code.claude.com/docs/en/mcp#mcp-tasks-that-run-on-the-server
- https://code.claude.com/docs/en/mcp#what-a-call-needs-to-become-an-mcp-task
- https://code.claude.com/docs/en/mcp#make-claude-wait-for-the-result-of-an-mcp-task
- https://code.claude.com/docs/en/mcp#automatic-backgrounding-of-long-tool-calls
- https://code.claude.com/docs/en/mcp#time-limits-on-mcp-tool-calls
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/mcp#mark-tools-that-are-safe-to-call-twice
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
