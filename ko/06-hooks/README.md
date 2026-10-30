<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 훅

훅은 Claude Code 세션 중 특정 이벤트에 반응하여 실행되는 자동화 스크립트입니다. 훅을 사용하면 자동화, 검증, 권한 관리, 사용자 정의 워크플로를 구현할 수 있습니다.

## 개요

훅은 Claude Code에서 특정 이벤트가 발생할 때 자동으로 실행되는 자동화 동작(셸 명령어, HTTP 웹훅, LLM 프롬프트, MCP 도구 호출, 서브에이전트 평가)입니다. 훅은 JSON 입력을 받고, 종료 코드와 JSON 출력으로 결과를 전달합니다.

**주요 기능:**
- 이벤트 기반 자동화
- JSON 기반 입력/출력
- `command`, `http`, `mcp_tool`, `prompt`, `agent` 훅 유형 지원
- 도구별 훅을 위한 패턴 매칭

## 구성

훅은 정해진 구조에 따라 설정 파일에서 구성합니다.

- `~/.claude/settings.json` - 사용자 설정(모든 프로젝트)
- `.claude/settings.json` - 프로젝트 설정(공유 가능, 커밋됨)
- `.claude/settings.local.json` - 로컬 프로젝트 설정(커밋되지 않음)
- 관리형 정책 - 조직 전체 설정
- 플러그인 `hooks/hooks.json` - 플러그인 범위 훅
- 스킬/에이전트 프런트매터 - 컴포넌트 수명 동안 유지되는 훅

### 기본 구성 구조

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

**주요 필드:**

| 필드 | 설명 | 예시 |
|-------|-------------|---------|
| `matcher` | 도구 이름과 매칭할 패턴(대소문자 구분) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | 훅 정의 배열 | `[{ "type": "command", ... }]` |
| `type` | 훅 유형: `"command"`(bash), `"prompt"`(LLM), `"http"`(웹훅), `"mcp_tool"`(MCP 도구 호출, v2.1.118+), `"agent"`(서브에이전트) | `"command"` |
| `command` | 실행할 셸 명령어 | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | 선택 사항인 타임아웃(초). 기본값: command/http/mcp_tool은 600, prompt는 30, agent는 60입니다. | `30` |
| `once` | `true`이면 첫 번째 실행이 성공한 뒤 훅이 제거됩니다(실패/차단/타임아웃된 실행에서는 유지). 스킬 프런트매터에서만 동작하며 설정과 에이전트 프런트매터에서는 무시됩니다 | `true` |
| `async` | `true`이면 차단하지 않고 백그라운드에서 실행합니다 | `true` |
| `asyncRewake` | `true`이면 백그라운드에서 실행하고 종료 코드 2일 때 Claude를 깨웁니다. `async`를 포함합니다. | `true` |
| `shell` | `"bash"` 또는 `"powershell"`을 받습니다. 기본값은 `"bash"`이며, Git Bash가 설치되지 않은 Windows에서는 `"powershell"`입니다. PowerShell 훅의 종료 코드 2는 v2.1.309부터만 차단하므로, PowerShell 가드 훅에 의존하기 전에 업그레이드하십시오. | `"bash"` |
| `statusMessage` | 훅이 실행되는 동안 표시할 사용자 정의 스피너 메시지 | `"Formatting…"` |
| `onFailure` | command 또는 HTTP 훅이 실패했을 때(시작 불가, 타임아웃, 예상하지 못한 종료 코드) 동작을 어떻게 처리할지 지정합니다: `"continue"`(기본값) 또는 `"block"`(v2.1.295+) | `"block"` |

> **참고**: 일부 이벤트는 기본 타임아웃을 낮춥니다. `UserPromptSubmit`은 `command`, `http`, `mcp_tool`의 기본값을 30초로, `MessageDisplay`는 10초로 낮춥니다. `SessionEnd` 훅은 1.5초 예산을 공유하며, 설정에서 훅별 `timeout`을 더 길게 지정하면 Claude Code가 그에 맞춰 예산을 최대 60초까지 늘립니다.

### 매처 패턴

| 패턴 | 설명 | 예시 |
|---------|-------------|---------|
| 정확한 문자열 | 특정 도구와 매칭 | `"Write"` |
| 정규식 패턴 | 여러 도구와 매칭 | `"Edit\|Write"` |
| 쉼표 구분 | 나열된 도구 중 하나와 매칭(v2.1.191+) | `"Write,Edit"` |
| 와일드카드 | 모든 도구와 매칭 | `"*"` 또는 `""` |
| MCP 도구 | 서버 및 도구 패턴 | `"mcp__memory__.*"` |

> **매처는 정확히 매칭됩니다(v2.1.195+).** 하이픈이 포함된 식별자(예: 하이픈이 들어간 MCP 도구 이름)가 더 이상 다른 도구와 실수로 부분 문자열 매칭되지 않습니다. `"Write,Edit"` 같은 쉼표 구분 매처는 목록의 어떤 도구에서든 실행됩니다. 이전 빌드에서는 이런 매처가 아무 알림 없이 전혀 실행되지 않았습니다.

**InstructionsLoaded 매처 값:**

| 매처 값 | 설명 |
|---------------|-------------|
| `session_start` | 세션 시작 시 로드된 지침 |
| `nested_traversal` | 중첩 디렉터리 탐색 중 로드된 지침 |
| `path_glob_match` | 경로 glob 패턴 매칭으로 로드된 지침 |

### `if` 조건으로 범위 좁히기(도구 인수 경로)

`matcher` 필드는 **도구 이름**(`"Write"`, `"Edit|Write"`, `"*"`)으로 훅을 선택합니다. 도구의 **인수**로 더 좁게 필터링하려면(예: 편집이 `src/`에 영향을 줄 때만 훅을 실행하거나, 비밀 파일 읽기를 막으려는 경우) 개별 훅 핸들러에 `if` 조건을 추가합니다. 이는 도구 이름 매처와 다릅니다. `matcher`는 *어떤 도구*인지를, `if`는 *어떤 호출*인지를 결정합니다.

`if`는 [권한 규칙 구문](https://code.claude.com/docs/en/permissions)(`ToolName(pattern)`)을 사용하며, 도구 이름과 **그 인수를 함께** 평가합니다. `Read`/`Edit`/`Write`의 경로 패턴은 gitignore 의미 체계를 따르며 권한 규칙과 같은 기준점을 사용합니다. `.env` 같은 단순 이름은 모든 깊이에서 매칭되고, `src/**`는 현재 디렉터리 기준, `/src/**`는 프로젝트 루트 기준, `~/...`는 홈 디렉터리 기준이며, `//...`는 파일 시스템 절대 경로입니다.

`if` 필드는 `matcher`가 아니라 **훅 핸들러 수준**, 즉 `hooks` 배열 안에서 `type`, `command`와 같은 수준에 둡니다.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "if": "Edit(src/**)",
            "command": "./hooks/lint-src.sh"
          }
        ]
      },
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "if": "Read(.env)",
            "command": "./hooks/block-secret-read.sh"
          }
        ]
      }
    ]
  }
}
```

유효한 `if` 패턴 예시: `Edit(src/**)`(`src/` 아래 편집), `Read(~/.ssh/**)`(모든 SSH 키 읽기), `Read(.env)`(현재 디렉터리 또는 그 아래의 모든 `.env`), `Bash(git push *)`(`git push` 하위 명령어만).

> **v2.1.214 업데이트**: 훅 `if` 조건의 단일 세그먼트 `dir/**` 패턴(예: `Edit(src/**)`)은 이제 `<cwd>/dir`에만 매칭되며, 트리의 모든 깊이에 있는 해당 디렉터리에는 매칭되지 않습니다. 이전에는 `src/**`가 `foo/src/**`에도 매칭되었습니다. 모든 깊이에서 매칭하려면 `**/dir/**`를 사용하십시오. **중요**: 이 범위 축소는 훅 `if:` 조건과 allow 규칙 자동 승인에만 적용되며, deny/ask 권한 규칙은 여전히 모든 깊이의 `dir/**`와 매칭됩니다.

## 훅 유형

Claude Code는 다섯 가지 훅 유형을 지원합니다.

### 명령어 훅

기본 훅 유형입니다. 셸 명령어를 실행하고 JSON stdin/stdout과 종료 코드로 통신합니다.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

#### Exec 형식(`args`)

> v2.1.139에서 추가되었습니다.

셸 형식인 `"command": "..."` 대신, 명령어 훅은 `args` 배열을 사용해 `execve()`로 바이너리를 직접 실행할 수 있습니다. 셸 파싱이 없으므로 경로 플레이스홀더를 따옴표로 감쌀 필요가 없고, 구성이 셸 인젝션 버그에 영향을 받지 않습니다.

```json
{
  "type": "command",
  "command": "python3",
  "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/validate.py", "--strict"],
  "timeout": 60
}
```

`command`는 항상 필수입니다. `args`가 설정되면 `command`는 실행할 실행 파일(`PATH`에서 확인)이고 `args`는 그 인수 벡터입니다. 파이프, 리디렉션, `&&` 연결, 셸 확장이 필요하면 `args`를 생략(셸 형식)하고, 바이너리 하나를 인수와 함께 호출할 때는 `args`를 사용합니다.

### HTTP 훅

> v2.1.63에서 추가되었습니다.

명령어 훅과 같은 JSON 입력을 받는 원격 웹훅 엔드포인트입니다. HTTP 훅은 URL로 JSON을 POST하고 JSON 응답을 받습니다. 샌드박스가 활성화되어 있으면 HTTP 훅은 샌드박스를 거쳐 라우팅됩니다. 보안을 위해 헤더 값에 환경 변수를 보간하려면 명시적인 `allowedEnvVars` 목록이 필요합니다.

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "http",
        "url": "https://my-webhook.example.com/hook"
      }]
    }]
  }
}
```

**주요 속성:**
- `"type": "http"` -- HTTP 훅임을 나타냅니다
- `"url"` -- 웹훅 엔드포인트 URL
- 샌드박스가 활성화되어 있으면 샌드박스를 거쳐 라우팅됩니다
- `headers` 값에 환경 변수를 보간하려면 명시적인 `allowedEnvVars` 목록이 필요합니다

### 프롬프트 훅

훅 내용이 Claude가 평가하는 프롬프트인, LLM 평가 방식의 훅입니다. 주로 `Stop` 및 `SubagentStop` 이벤트에서 작업 완료 여부를 지능적으로 확인하는 데 사용합니다.

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM이 프롬프트를 평가하고 구조화된 결정을 반환합니다(자세한 내용은 [프롬프트 기반 훅](#프롬프트-기반-훅) 참고).

### MCP 도구 훅

> v2.1.118에서 추가되었습니다.

`mcp_tool` 유형은 구성된 MCP 도구를 직접 호출합니다. 구성에는 셸 명령어나 URL 대신 MCP 서버와 도구 이름을 지정합니다. 검증이나 대응 로직이 이미 구성해 둔 MCP 서버에 있을 때 유용합니다.

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "mcp_tool",
    "server": "my-mcp-server",
    "tool": "validate_edit",
    "input": { "file_path": "${tool_input.file_path}" }
  }]
}
```

**주요 속성:**
- `"type": "mcp_tool"` -- MCP 도구 훅임을 나타냅니다
- `"server"` -- 구성된 MCP 서버 이름
- `"tool"` -- 해당 서버에서 호출할 도구 이름
- `"input"` -- 도구에 전달할 선택적 인수입니다. 문자열 값은 `"${tool_input.file_path}"`처럼 훅의 JSON 입력에서 가져오는 `${path}` 치환을 지원합니다

도구의 인수는 훅 입력에서 직접 오는 것이 아니라 `input`(`${path}` 치환 포함)에서 옵니다. MCP 서버 구성 방법은 [MCP 서버 설정](../05-mcp/README.md)을 참고하십시오.

### 에이전트 훅

전용 에이전트를 생성하여 조건을 평가하거나 복잡한 검사를 수행하는 서브에이전트 기반 검증 훅입니다. 프롬프트 훅(단일 턴 LLM 평가)과 달리 에이전트 훅은 도구를 사용하고 여러 단계의 추론을 수행할 수 있습니다.

> **참고**: 에이전트 훅은 실험적 기능이며 변경될 수 있습니다.

> **참고**: v2.1.280부터 에이전트 훅은 `PermissionRequest`에서 실행되지 않습니다. 에이전트 훅의 응답으로는 요청을 허용하거나 거부할 수 없었기 때문입니다. 이 이벤트에서는 결정 객체를 반환하는 command 또는 HTTP 훅을 사용하십시오(프롬프트 훅의 `ok: false`는 `PermissionRequest`에 영향을 주지 않습니다).

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**주요 속성:**
- `"type": "agent"` -- 에이전트 훅임을 나타냅니다
- `"prompt"` -- 서브에이전트에게 맡길 작업 설명
- 에이전트는 평가를 위해 도구(Read, Grep, Bash 등)를 사용할 수 있습니다
- 프롬프트 훅과 비슷한 구조화된 결정을 반환합니다

## 훅 이벤트

Claude Code는 **33가지 훅 이벤트**를 지원합니다.

| 이벤트 | 실행 시점 | 매처 입력 | 차단 가능 | 일반적인 용도 |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | 세션 시작/재개/clear/compact | startup/resume/clear/compact/fork | 아니요 | 환경 설정 |
| **Setup** | `--init-only`, 또는 `-p`와 함께 쓴 `--init`/`--maintenance`(CI/스크립트 준비) | `init`/`maintenance` | 아니요 | 도구 프로비저닝, 의존성 설치 |
| **InstructionsLoaded** | CLAUDE.md 또는 규칙 파일이 로드된 후 | 로드 이유(`session_start`/`nested_traversal`/`path_glob_match`/`include`/`compact`) | 아니요 | 감사/관측성 로깅 |
| **UserPromptSubmit** | 사용자가 프롬프트를 제출할 때 | (없음) | 예 | 프롬프트 검증 |
| **UserPromptExpansion** | 사용자가 입력한 슬래시 명령어나 MCP 프롬프트가 프롬프트로 확장될 때 | 명령어 이름 | 예 | 확장된 프롬프트 변환 또는 검사 |
| **PreToolUse** | 도구 실행 전 | 도구 이름 | 예(allow/deny/ask/defer) | 입력 검증, 수정 |
| **PermissionRequest** | 권한 대화상자가 표시될 때 | 도구 이름 | 예 | 자동 승인/거부 |
| **PermissionDenied** | auto 모드가 도구 호출을 거부할 때 | 도구 이름 | 아니요 | 로깅, 분석, 정책 적용 |
| **PostToolUse** | 도구가 성공한 후 | 도구 이름 | 아니요 | 컨텍스트 추가, 피드백 |
| **PostToolUseFailure** | 도구 실행이 실패할 때 | 도구 이름 | 아니요 | 오류 처리, 로깅 |
| **PostToolBatch** | 도구 사용 묶음이 완료된 후 | (없음) | 예 | 집계 보고, 일괄 검증 |
| **Notification** | 알림이 전송될 때 | 알림 유형 | 아니요 | 사용자 정의 알림 |
| **MessageDisplay** | 어시스턴트 메시지 텍스트가 표시되는 동안 | (없음) | 아니요 | 표시되는 메시지 텍스트 변환 또는 숨기기(v2.1.152) |
| **SubagentStart** | 서브에이전트가 생성될 때 | 에이전트 유형 이름 | 아니요 | 서브에이전트 설정 |
| **SubagentStop** | 서브에이전트가 끝날 때 | 에이전트 유형 이름 | 예 | 서브에이전트 검증 |
| **Stop** | Claude가 응답을 마칠 때 | (없음) | 예 | 작업 완료 확인 |
| **StopFailure** | API 오류로 턴이 끝날 때 | 오류 유형(`rate_limit`, `overloaded`, `server_error`, …) | 아니요 | 오류 복구, 로깅 |
| **TeammateIdle** | 에이전트 팀의 팀원이 유휴 상태일 때 | (없음) | 예 | 팀원 조율 |
| **TaskCompleted** | 작업이 완료로 표시될 때 | (없음) | 예 | 작업 후 동작 |
| **TaskCreated** | TaskCreate로 작업이 생성될 때 | (없음) | 예 | 작업 추적, 로깅 |
| **ConfigChange** | 구성 파일이 변경될 때 | 구성 출처(`user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`) | 예(policy 제외) | 구성 업데이트에 대응 |
| **CwdChanged** | 작업 디렉터리가 변경될 때 | (없음) | 아니요 | 디렉터리별 설정 |
| **DirectoryAdded** | 세션 중 `/add-dir` 또는 SDK `register_repo_root` 제어 요청으로 새 작업 디렉터리가 등록될 때(v2.1.219) | `slash_command`/`register_repo_root` | 아니요 | 새로 추가된 디렉터리용 도구 설정 |
| **FileChanged** | 감시 중인 파일이 변경될 때 | 감시할 파일 이름(예: `.envrc\|.env`) | 아니요 | 파일 모니터링, 재빌드 |
| **PreCompact** | 컨텍스트 압축 전 | manual/auto | 예 | 압축 전 동작 |
| **PostCompact** | 압축이 완료된 후 | (없음) | 아니요 | 압축 후 동작 |
| **PreModelSwitch** | Claude Code가 요청된 모델 전환을 적용하기 전 | 전환 대상 모델의 정식 이름(`to_model`에서 도출) | 예 | 모델 변경 통제 또는 거부 |
| **PostModelSwitch** | Claude Code가 스스로 수행한 변경(예: 재개 시 모델 복원)을 포함해 세션 모델이 변경된 후 | 전환된 모델의 정식 이름(`to_model`에서 도출) | 아니요 | 모델 변경 기록 또는 대응 |
| **WorktreeCreate** | 워크트리가 생성될 때 | (없음) | 예(경로 반환) | 워크트리 초기화 |
| **WorktreeRemove** | 워크트리가 제거될 때 | (없음) | 예(0이 아닌 종료 코드 시 제거 실패) | 워크트리 정리 |
| **Elicitation** | MCP 서버가 사용자 입력을 요청할 때 | MCP 서버 이름 | 예 | 입력 검증 |
| **ElicitationResult** | 사용자가 elicitation에 응답할 때 | MCP 서버 이름 | 예 | 응답 처리 |
| **SessionEnd** | 세션이 종료될 때 | 종료 이유(`clear`/`resume`/`logout`/`prompt_input_exit`/`other`) | 아니요 | 정리, 최종 로깅 |

`PreModelSwitch`와 `PostModelSwitch`는 v2.1.251 이상이 필요합니다. 두 이벤트 모두 `from_model`과 `to_model`을 받으며, 매처는 `to_model`에서 도출한 정식 이름(예: `claude-opus-5`, `.*opus.*`)을 기준으로 평가됩니다. 이 이벤트들의 `command`, `http`, `mcp_tool` 기본 타임아웃은 30초로 낮아집니다.

> **`TaskCreated`와 `TaskCompleted`는 todo 도구가 활성화되어 있어야 합니다(v2.1.233).** 이 두
> 이벤트는 todo/작업 추적 도구(`TaskCreate`/`Get`/`Update`/`List`,
> `TodoWrite`)에서 실행되며, 이 도구들은 **Claude 3.x 모델, Opus 4~4.7, Sonnet 4~4.6,
> Haiku 4.5에서만 기본으로 제공됩니다**. 다른 모델에서는 이 훅이 유효한
> 구성이지만 전혀 실행되지 않으며, 출력도 오류도 없습니다.
> `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`을 설정하면 도구와 그에 따른 이벤트가 다시 활성화됩니다.

> **PostToolUse 소요 시간(v2.1.119):** 이제 `PostToolUse` 및 `PostToolUseFailure` 훅 입력에 `duration_ms`가 포함됩니다. 자세한 내용은 [PostToolUse](#posttooluse) 섹션을 참고하십시오.

### PreToolUse

Claude가 도구 매개변수를 만든 뒤, 처리하기 전에 실행됩니다. 도구 입력을 검증하거나 수정할 때 사용합니다.

**구성:**
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

**일반적인 매처:** `Agent`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**출력 제어:**
- `permissionDecision`: `"allow"`, `"deny"`, `"ask"`, `"defer"`
  - `"allow"`는 권한 프롬프트를 건너뜁니다(사용자 상호 작용이 필요한 도구와 조직에서 `ask`로 설정한 커넥터 도구는 제외)
  - `"deny"`는 도구 호출을 막습니다
  - `"ask"`는 사용자에게 확인을 요청하며, 프롬프트에 훅이 속한 플러그인이나 스킬의 이름이 표시됩니다(v2.1.301)
  - `"defer"`는 나중에 도구를 재개할 수 있도록 턴을 종료하며, `-p`를 사용한 비대화형 모드에서만 동작합니다(대화형 세션에서는 경고를 기록하고 무시합니다). 결과에는 `stop_reason: "tool_deferred"`가 포함됩니다. 이 값에서는 `permissionDecisionReason`, `updatedInput`, `additionalContext`가 모두 무시됩니다
  - 훅이 무엇을 반환하든 deny 및 ask 규칙은 여전히 평가됩니다. 여러 `PreToolUse` 훅의 결정이 다르면 우선순위는 `deny` > `defer` > `ask` > `allow`입니다
- `permissionDecisionReason`: 결정에 대한 설명입니다. `"ask"`에서는 (Claude가 아닌) 사용자에게, `"deny"`에서는 Claude에게 표시되며, `"allow"`와 `"defer"`에서는 디버그 로그에만 기록됩니다
- `updatedInput`: 대체할 도구 입력입니다(입력 객체 전체를 대체). v2.1.300부터 Claude 자신의 입력처럼 검증되어, 알 수 없는 키는 제거되고 도구가 거부하는 입력은 호출을 거부합니다. 같은 호출에 대해 여러 `PreToolUse` 훅이 `updatedInput`을 반환하면 Claude Code는 재작성 내용을 병합하지 않으며 어떤 입력으로 도구가 실행될지 보장하지 않으므로, 특정 도구의 입력은 하나의 훅만 재작성하도록 하십시오.

### PostToolUse

도구가 완료된 직후 실행됩니다. 검증, 로깅, Claude에게 컨텍스트를 다시 제공하는 용도로 사용합니다.

**구성:**
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

**출력 제어:**
- `"block"` 결정은 피드백과 함께 Claude에게 프롬프트를 보냅니다
- `additionalContext`: Claude에게 추가되는 컨텍스트

**추가 입력 필드(v2.1.119):**

| 필드 | 유형 | 설명 |
|-------|------|-------------|
| `duration_ms` | number | 도구 실행 시간(밀리초)입니다. 권한 프롬프트와 PreToolUse 훅 실행에 쓴 시간은 제외됩니다. `PostToolUse`와 `PostToolUseFailure` 훅 모두에서 사용할 수 있습니다. |

#### 복구 가능한 차단(`continueOnBlock`, v2.1.139)

`PostToolUse`에서 `"decision": "block"`을 반환하는 command 훅은 도구 결과 옆에 `reason`을 추가하며, Claude는 여전히 원래 출력을 봅니다. `continueOnBlock`은 **prompt** 훅 필드입니다(command 및 agent 훅에는 없음). 기본적으로 `PostToolUse`에서 `ok: false`를 반환하는 prompt 훅은 턴을 종료하고 이유를 경고 줄로 표시합니다. prompt 훅에 `"continueOnBlock": true`를 설정하면 대신 이유를 Claude에게 다시 전달하고 턴을 계속하므로, 모델이 피드백을 읽고 재시도하거나 조정할 수 있습니다.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Check this edit against our write policy (for example, read-only paths). Hook input: $ARGUMENTS",
            "continueOnBlock": true
          }
        ]
      }
    ]
  }
}
```

훅의 `reason`이 Claude가 조치할 수 있는 내용일 때(예: "이 파일은 읽기 전용이므로 다른 곳에 쓰십시오") 사용하고, 차단 시 턴 전체를 반드시 멈춰야 한다면 설정하지 마십시오.

### UserPromptSubmit

사용자가 프롬프트를 제출하면 Claude가 처리하기 전에 실행됩니다. v2.1.299부터는 스킬이나 사용자 정의 명령어가 확장되기 전에 실행되므로, 프롬프트를 차단하면 해당 명령어의 `!` 셸 줄도 실행되지 않습니다. `UserPromptExpansion`은 그 이후에 실행됩니다.

**구성:**
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

**출력 제어:**
- `decision`: 처리를 막으려면 `"block"`
- `reason`: 차단된 경우의 설명
- `additionalContext`: 프롬프트에 추가되는 컨텍스트

### Stop 및 SubagentStop

Claude가 응답을 마칠 때(Stop) 또는 서브에이전트가 완료될 때(SubagentStop) 실행됩니다. 작업 완료 여부를 지능적으로 확인하기 위한 프롬프트 기반 평가를 지원합니다.

**추가 입력 필드:** `Stop`과 `SubagentStop` 훅은 모두 JSON 입력에서 `last_assistant_message` 필드를 받으며, 여기에는 멈추기 전 Claude 또는 서브에이전트의 마지막 메시지가 들어 있습니다. 작업 완료를 평가할 때 유용합니다.

**구성:**
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

> **연속 차단 안전 상한(v2.1.143)**: 같은 턴에서 `Stop` 훅이 `"decision": "block"`을 반환(또는 `continue: false`를 설정)하는 일이 **8번 연속** 발생하면, Claude Code는 다음 차단을 무시하고 턴을 종료합니다. 임계값은 환경 변수 `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=<integer>`로 바꿀 수 있습니다(`0`으로 설정하면 상한이 완전히 비활성화됩니다). 이를 통해 버그가 있는 Stop 훅이 턴을 끝없이 반복하는 것을 방지합니다.

**반환 필드(v2.1.163):** `Stop` 또는 `SubagentStop` 훅은 `hookSpecificOutput.additionalContext`를 반환하여 Claude에게 피드백을 주고 **오류 라벨을 표시하지 않고 턴을 계속**할 수 있습니다. 이전에는 Stop 훅에서 모델에 영향을 주기가 번거로웠지만, 이제는 이전 피드백 방식(예: `"decision": "block"`)의 오류 라벨 동작 없이 깔끔하게 컨텍스트를 주입할 수 있습니다.

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Reminder: run the test suite before declaring done."
  }
}
```

### SubagentStart

서브에이전트가 실행을 시작할 때 실행됩니다. 매처 입력은 에이전트 유형 이름이므로 특정 서브에이전트 유형을 대상으로 훅을 지정할 수 있습니다.

**구성:**
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

세션이 시작되거나 재개될 때 실행됩니다. 환경 변수를 유지할 수 있습니다.

**매처:** `startup`, `resume`, `clear`, `compact`, `fork`

> **v2.1.214 업데이트**: 포크된 세션은 이제 출처를 `"fork"`로 보고합니다. 이전에는 `"resume"`으로 보고했습니다.

**특별 기능:** `CLAUDE_ENV_FILE`을 사용하여 환경 변수를 유지합니다(`CwdChanged` 및 `FileChanged` 훅에서도 사용 가능).

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

**세션 범위 출력(v2.1.152):** `SessionStart` 훅은 JSON을 반환하여 스킬을 다시 검색하고 세션 제목을 설정할 수 있습니다.

```json
{
  "reloadSkills": true,
  "hookSpecificOutput": {
    "sessionTitle": "Payments migration"
  }
}
```

최상위 `reloadSkills: true`는 같은 세션에서 스킬 재검색을 실행하여(`/reload-skills` 명령어와 같은 동작), 훅이 방금 설치한 스킬을 바로 사용할 수 있게 합니다. `hookSpecificOutput.sessionTitle`은 시작 및 재개 시 세션의 표시 제목을 설정합니다.

### SessionEnd

세션이 끝날 때 정리나 최종 로깅을 수행하기 위해 실행됩니다. 종료를 차단할 수는 없습니다.

**reason 필드 값:**
- `clear` - 사용자가 세션을 지움
- `resume` - 대화형 `/resume`으로 세션을 전환함
- `logout` - 사용자가 로그아웃함
- `prompt_input_exit` - 사용자가 프롬프트 입력으로 종료함
- `other` - 기타 이유

**구성:**
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

### Notification 이벤트

알림 이벤트용 매처가 업데이트되었습니다.
- `permission_prompt` - 권한 요청 알림
- `idle_prompt` - 유휴 상태 알림
- `auth_success` - 인증 성공
- `elicitation_dialog` - MCP 서버가 elicitation 양식을 열었음
- `elicitation_url_dialog` - MCP 서버가 브라우저 URL을 열도록 요청함
- `elicitation_complete` - URL 모드 elicitation이 완료를 보고함
- `elicitation_response` - elicitation 응답을 서버로 다시 보냄
- `agent_needs_input` - 백그라운드 에이전트가 입력을 필요로 함(v2.1.198)
- `agent_completed` - 백그라운드 에이전트가 완료됨(v2.1.198)
- `quota_auto_resume_fired` / `quota_auto_resume_stale` / `quota_auto_resume_disabled` - 사용량 한도 자동 재개 결과(v2.1.234)
- `plugin_notification` - 모드가 `$.ui.notify`로 알림을 발생시킴. 모드가 직접 설정하지 않으면 훅의 `title`은 모드 이름입니다

### PreModelSwitch

Claude Code가 요청된 모델 전환을 적용하기 **전에** 실행됩니다. 예를 들어 `/model`을 실행하거나 컴포넌트가 다른 모델을 요청할 때입니다. v2.1.251 이상이 필요합니다.

**매처:** `to_model`에서 도출한, 전환 대상 모델의 정식 이름입니다. 정확한 모델(`claude-opus-5`)이나 정규식으로 모델 계열(`.*opus.*`)을 매칭합니다.

**입력 필드:** 공통 필드에 더해 `from_model`(전환 전 사용 중인 모델)과 `to_model`(요청된 모델)을 받습니다.

**차단 가능:** 예. 종료 코드 `2`는 전환을 차단하고 stderr를 오류로 표시하므로 세션은 현재 모델을 유지합니다. 모델 변경을 통제하거나 거부할 때 사용합니다. 예를 들어 비용에 민감한 프로젝트가 가장 비싼 모델을 쓰지 않도록 할 수 있습니다.

**타임아웃:** 이 이벤트는 `command`, `http`, `mcp_tool`의 기본 타임아웃을 30초로 낮춥니다.

**구성:**
```json
{
  "hooks": {
    "PreModelSwitch": [
      {
        "matcher": ".*opus.*",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/gate-model-switch.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# gate-model-switch.sh - 이 프로젝트에서 Opus로의 전환을 거부
input=$(cat)
to_model=$(echo "$input" | jq -r '.to_model')

if [[ "$to_model" == *opus* ]]; then
  echo "This project is budgeted for Sonnet; staying on the current model." >&2
  exit 2
fi

exit 0
```

### PostModelSwitch

세션의 모델이 변경된 **후에** 실행됩니다. 사용자가 요청한 전환뿐 아니라 Claude Code가 스스로 수행하는 변경(예: 세션을 재개할 때 이전에 선택한 모델 복원)에서도 실행됩니다. v2.1.251 이상이 필요합니다.

**매처:** `PreModelSwitch`와 같습니다. `to_model`에서 도출한 정식 이름입니다.

**입력 필드:** 공통 필드와 함께 `from_model` 및 `to_model`을 받습니다.

**차단 가능:** 아니요. 전환이 이미 일어났으므로 훅은 관찰하고 대응만 할 수 있습니다.

**타임아웃:** 이 이벤트는 `command`, `http`, `mcp_tool`의 기본 타임아웃을 30초로 낮춥니다.

**구성:**
```json
{
  "hooks": {
    "PostModelSwitch": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/log-model-switch.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# log-model-switch.sh - 모든 모델 변경을 세션 로그에 추가
input=$(cat)
from=$(echo "$input" | jq -r '.from_model')
to=$(echo "$input" | jq -r '.to_model')

echo "$(date -Iseconds) $from -> $to" >> ~/.claude/model-switches.log
exit 0
```

## 컴포넌트 범위 훅

훅은 특정 컴포넌트(스킬, 에이전트, 명령어)의 프런트매터에 연결할 수 있습니다.

**SKILL.md, agent.md, command.md에서:**

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
          once: true  # 스킬 프런트매터 전용: 첫 번째 실행이 성공하면 제거됨
---
```

**지원 이벤트:** 모든 훅 이벤트입니다. 서브에이전트 훅은 서브에이전트가 활성 상태일 때만 실행되며(`Stop` → `SubagentStop`), 스킬 훅은 스킬이 호출될 때 등록되어 세션의 나머지 기간 동안 활성 상태로 유지됩니다. v2.1.304부터 한 출처(프로젝트, 개인 스킬 폴더, 또는 하나의 플러그인)의 스킬은 세션당 최대 1,024개의 훅과 16,384자의 매처 문자를 등록할 수 있으며, 한도를 넘은 스킬은 훅을 하나도 등록하지 않습니다(`claude --debug` 로그에서 `registers none of its hooks`를 검색하십시오).

이를 통해 훅을 사용하는 컴포넌트 안에 훅을 직접 정의하여 관련 코드를 한곳에 모아 둘 수 있습니다.

### 서브에이전트 프런트매터의 훅

서브에이전트의 프런트매터에 `Stop` 훅을 정의하면, 해당 서브에이전트로 범위가 지정된 `SubagentStop` 훅으로 자동 변환됩니다. 이렇게 하면 메인 세션이 멈출 때가 아니라 해당 서브에이전트가 완료될 때만 stop 훅이 실행됩니다.

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # 위 Stop 훅은 이 서브에이전트의 SubagentStop으로 자동 변환됨
---
```

**워크스페이스 신뢰 필요(v2.1.218):** **프로젝트** 서브에이전트의 프런트매터 훅은 이제 실행되기 전에, 에이전트 파일이 위치한 폴더에 대해 워크스페이스 신뢰를 수락해야 합니다. v2.1.218 이전에는 신뢰하지 않은 폴더에서도 이 훅이 실행될 수 있었습니다. 어떤 범위가 예외인지는 [서브에이전트 문서](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter)를 참고하십시오.

## PermissionRequest 이벤트

사용자 정의 출력 형식으로 권한 요청을 처리합니다.

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

## 훅 입력 및 출력

### JSON 입력(stdin)

모든 훅은 stdin으로 JSON 입력을 받습니다.

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
  "agent_type": "security-reviewer",
  "worktree": "/path/to/worktree",
  "effort": { "level": "medium" }
}
```

**공통 필드:**

| 필드 | 설명 |
|-------|-------------|
| `session_id` | 고유 세션 식별자 |
| `transcript_path` | 대화 트랜스크립트 파일 경로 |
| `cwd` | 현재 작업 디렉터리 |
| `prompt_id` | 처리 중인 프롬프트의 UUID로, OpenTelemetry `prompt.id` 속성과 연결됩니다(v2.1.196) |
| `hook_event_name` | 훅을 실행한 이벤트 이름 |
| `agent_id` | 이 훅을 실행하는 에이전트의 식별자 |
| `agent_type` | 에이전트 이름(예: `"Explore"` 또는 `"security-reviewer"`)입니다. 세션이 `--agent`를 사용하거나 훅이 서브에이전트 안에서 실행될 때만 존재합니다 |
| `worktree` | 에이전트가 git 워크트리에서 실행 중인 경우 해당 워크트리 경로 |
| `effort.level` | (v2.1.133+) 활성 effort 수준: `low`, `medium`, `high`, `xhigh`, `max` |

### 종료 코드

| 종료 코드 | 의미 | 동작 |
|-----------|---------|----------|
| **0** | 성공 | 계속 진행, JSON stdout 파싱 |
| **2** | 차단 오류 | 작업 차단, stderr를 오류로 표시 |
| **기타** | 비차단 오류 | 계속 진행. 트랜스크립트의 `<hook name> hook error` 알림에 stderr의 첫 줄이 표시됩니다 |

### JSON 출력(stdout, 종료 코드 0)

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

> **범위(v2.1.121+):** 이제 `hookSpecificOutput.updatedToolOutput`은 MCP 도구뿐 아니라 **모든** 도구에서 적용됩니다. `Bash`, `Edit`, `Read` 등에 대한 `PostToolUse` 훅은 Claude가 보기 전에 도구 출력을 재작성할 수 있으므로, 비밀 정보 마스킹, diff 정규화, 시끄러운 명령어 출력 필터링에 유용합니다. 값은 도구의 출력 형태와 일치해야 합니다. `Bash`는 `stdout`, `stderr`, `interrupted`, `isImage`를 가진 객체를 반환하며, 내장 도구에서 형태가 맞지 않는 값은 무시되고 원래 출력이 사용됩니다. 예시(`Bash` 출력에서 ANSI 색상 코드 제거):
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PostToolUse",
>     "updatedToolOutput": {
>       "stdout": "<output with ANSI escapes removed>",
>       "stderr": "",
>       "interrupted": false,
>       "isImage": false
>     }
>   }
> }
> ```

> **`retry`(PermissionDenied)**: JSON `hookSpecificOutput.retry: true`를 사용하면 거부된 도구 호출을 다시 시도해도 된다고 모델에게 알릴 수 있습니다.

> **지원 중단(deprecated)된 `PreToolUse` 결정 형식**: `PreToolUse`에서 최상위 `decision` 및 `reason` 필드는 **지원 중단**되었습니다. 대신 `hookSpecificOutput.permissionDecision`(`allow` / `deny` / `ask` / `defer`)과 `permissionDecisionReason`을 사용하십시오. 결정 간 우선순위는 `deny` > `defer` > `ask` > `allow`입니다. 또한 `suppressOutput`은 허용되지만 **아무 효과가 없습니다**.

#### `terminalSequence`(v2.1.141)

훅은 JSON 출력에 `terminalSequence`를 설정하여 원시 OSC(operating system command) 이스케이프 시퀀스를 내보낼 수 있습니다. 훅이 반환되면 호스트가 이 시퀀스를 제어 터미널에 씁니다. 별도의 TTY 없이도 데스크톱 알림, 창 제목 업데이트, 터미널 벨을 사용할 때 유용합니다.

| 필드 | 유형 | 설명 |
|-------|------|-------------|
| `terminalSequence` | string | 원시 이스케이프 시퀀스(일반적으로 OSC 9 / OSC 0 / OSC 777). 호스트 터미널에 그대로 기록됩니다. |

예시: 긴 작업이 완료되면 OSC 9 데스크톱 알림을 보냅니다. ESC와 BEL은 JSON 이스케이프(`\u001b`, `\u0007`)로 쓰거나 `printf`와 `jq`로 값을 만드십시오. JSON 문자열 안의 원시 제어 바이트는 파싱에 실패합니다.

```json
{
  "terminalSequence": "\u001b]9;Task complete\u0007"
}
```

Claude가 턴을 마칠 때 알림이 실행되도록 `Stop` 훅에 구성하십시오. 시퀀스 지원 여부는 터미널에 따라 다릅니다. iTerm2, Windows Terminal, WezTerm은 OSC 9를 지원하며 Kitty는 OSC 99를 사용합니다.

## 환경 변수

| 변수 | 사용 가능 범위 | 설명 |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | 모든 훅 | 프로젝트 루트의 절대 경로 |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | 환경 변수를 유지하기 위한 파일 경로 |
| `CLAUDE_CODE_REMOTE` | 모든 훅 | 원격 환경에서 실행 중이면 `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | 플러그인 훅 | 플러그인 디렉터리 경로 |
| `${CLAUDE_PLUGIN_DATA}` | 플러그인 훅 | 플러그인 데이터 디렉터리 경로 |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd 훅 | SessionEnd 훅의 타임아웃(밀리초)을 설정합니다(기본값 대체) |
| `CLAUDE_CODE_SESSION_ID` | Bash 도구 하위 프로세스(v2.1.132+) | 세션 UUID로, 훅 입력 JSON의 `session_id` 필드와 일치합니다. bash 로그와 훅 텔레메트리를 연결할 때 사용합니다. |
| `CLAUDE_EFFORT` | Bash 도구 하위 프로세스(v2.1.133+) | 활성 effort 수준(`low`/`medium`/`high`/`xhigh`/`max`)으로, 훅 입력 JSON의 `effort.level`과 일치합니다. |
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | 프로세스 전체(v2.1.143+) | Claude Code가 다음 차단을 무시하고 턴을 종료하기 전까지 허용되는 Stop 훅 연속 차단 최대 횟수(기본값 `8`). `0`으로 설정하면 상한이 비활성화됩니다. |

## 프롬프트 기반 훅

`Stop` 및 `SubagentStop` 이벤트에서는 LLM 기반 평가를 사용할 수 있습니다.

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

**LLM 응답 스키마:**
```json
{
  "ok": false,
  "reason": "Tests were not run after the last edit"
}
```

`ok: true`는 동작을 허용합니다. `ok`가 `false`이면 `reason`이 필요합니다.

## 예시

### 예시 1: Bash 명령어 검증기(PreToolUse)

**파일:** `.claude/hooks/validate-bash.py`

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
            sys.exit(2)  # 종료 코드 2 = 차단 오류

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**구성:**
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

### 예시 2: 보안 스캐너(PostToolUse)

**파일:** `.claude/hooks/security-scan.py`

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

### 예시 3: 코드 자동 포맷(PostToolUse)

**파일:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# stdin에서 JSON 읽기
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# 파일 확장자에 따라 포맷
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

### 예시 4: 프롬프트 검증기(UserPromptSubmit)

**파일:** `.claude/hooks/validate-prompt.py`

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
    prompt = input_data.get("prompt", "")

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

### 예시 5: 지능형 Stop 훅(프롬프트 기반)

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

### 예시 6: 컨텍스트 사용량 추적기(훅 쌍)

`UserPromptSubmit`(메시지 전)과 `Stop`(응답 후) 훅을 함께 사용하여 요청별 토큰 소비량을 추적합니다.

**파일:** `.claude/hooks/context-tracker.py`

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

# 구성
CONTEXT_LIMIT = 1000000  # Opus 5, Sonnet 5, Opus 4.8, Sonnet 4.6은 1M, Haiku 4.5는 200000 (사용 모델에 맞게 조정)
USE_TIKTOKEN = False    # 정확도를 높이려면 tiktoken 설치 후 True로 설정


def get_state_file(session_id: str) -> str:
    """Get temp file path for storing pre-message token count, isolated by session."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Count tokens in text.

    Uses tiktoken with p50k_base encoding if available (~90-95% accuracy),
    otherwise falls back to character estimation (~80-90% accuracy).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # 추정 방식으로 대체

    # 문자 기반 추정: 영어 기준 토큰당 약 4자
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Read and concatenate all content from transcript file."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # 다양한 메시지 형식에서 텍스트 내용 추출
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
    """Pre-message hook: Save current token count before request."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 나중에 비교할 수 있도록 임시 파일에 저장
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Post-response hook: Calculate and report token delta."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 메시지 전 토큰 수 불러오기
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # 차이 계산
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # 사용량 보고
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

**구성:**
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

**작동 방식:**
1. `UserPromptSubmit`은 프롬프트가 처리되기 전에 실행되어 현재 토큰 수를 저장합니다
2. `Stop`은 Claude가 응답한 후 실행되어 차이를 계산하고 사용량을 보고합니다
3. 각 세션은 임시 파일 이름의 `session_id`로 격리됩니다

**토큰 계산 방법:**

| 방법 | 정확도 | 의존성 | 속도 |
|--------|----------|--------------|-------|
| 문자 수 추정 | ~80-90% | 없음 | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

> **참고:** Anthropic은 공식 오프라인 토크나이저를 공개하지 않았습니다. 두 방법 모두 근사치입니다. 트랜스크립트에는 사용자 프롬프트, Claude의 응답, 도구 출력이 포함되며, v2.1.300부터는 각 API 요청의 시스템 프롬프트, 도구, 매개변수도 기록됩니다.

### 예시 7: auto 모드 권한 시드(일회성 설정 스크립트)

Claude Code의 auto 모드 기준선과 동등한 안전한 권한 규칙(기본 37개, 모든 카테고리 플래그를 켜면 최대 63개)을 `~/.claude/settings.json`에 시드하는 일회성 설정 스크립트입니다. 훅을 사용하지 않으며 이후 선택을 기억하지도 않습니다. 한 번만 실행하면 되며, 다시 실행해도 안전합니다(이미 있는 규칙은 건너뜀).

**파일:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 추가될 항목 미리 보기
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 적용
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**추가되는 항목:**

| 카테고리 | 예시 |
|----------|---------|
| 내장 도구 | `Read(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| 선택적 편집(--include-edits) | `Edit(*)` |
| Git 읽기 | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git 쓰기(로컬) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| 패키지 관리자 | `Bash(npm ci:*)`, `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(pip3 install:*)` |
| 빌드 및 테스트 | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| 일반 셸 | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**의도적으로 제외되는 항목**(이 스크립트는 절대 추가하지 않음):
- `rm -rf`, `sudo`, 강제 푸시, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, 프로덕션 배포

### 예시 8: 학습 진행 기록기(SessionEnd)

각 Claude Code 세션이 끝날 때 학습한 모듈을 기록합니다. 진행 상황은
`~/.claude-howto-progress.json`에 저장되며, 저장소 밖에 있으므로 `git pull`을 해도
덮어쓰이지 않습니다.

**왜 `Stop`이 아니라 `SessionEnd`인가요?**
`Stop`은 Claude의 *모든* 응답 후에 실행됩니다. `SessionEnd`는 세션이 종료될 때
한 번 실행되므로, 세션 종료 일지 항목에 딱 맞습니다.

**왜 대화형 프롬프트가 없나요?**
훅은 제어 터미널 없이 실행되므로 `/dev/tty`를 사용할 수 없고, 훅이 사용자에게
입력을 요청할 수 없습니다. Claude Code를 실행할 때 모듈(및 선택적 메모)을 환경 변수로
전달하십시오. 예: `CLAUDE_HOWTO_MODULES=06,07 claude`.

**파일:** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# SessionEnd 훅: 작업한 모듈을 기록한 뒤, 학습 진행 상황을 지속적으로 추적하기 위해
# ~/.claude-howto-progress.json에 세션 기록을 추가합니다.

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# 가드: 이 저장소 안에서만 실행
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

# 작업한 모듈. 예: CLAUDE_HOWTO_MODULES=06,07 claude 로 실행
# 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP
# 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI
INPUT="${CLAUDE_HOWTO_MODULES:-}"

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

# 선택적 메모. 예: CLAUDE_HOWTO_NOTES="tried the pre-commit example"
NOTES="${CLAUDE_HOWTO_NOTES:-}"

# NOTES를 별도 인수로 전달하여 Python이 JSON 이스케이프를 처리하도록 함 —
# 메모에 따옴표나 백슬래시가 있어도 JSON이 깨지지 않음.
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

**설치** — `settings.json`의 경로가 올바르게 확인되도록 스크립트를 프로젝트의 훅 디렉터리에 복사합니다.

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**구성**(`.claude/settings.json`):

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-end.sh\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

SessionEnd 훅의 기본 예산은 1.5초입니다. 훅별 `"timeout"`(초)을 설정하면 그에 맞춰 예산이 최대 60초까지 늘어나며, 자체 `timeout`이 없는 훅은 1.5초 후에 취소됩니다.

**출력 — `~/.claude-howto-progress.json`:**

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

**보여 주는 주요 패턴:**

| 패턴 | 중요한 이유 |
|---------|----------------|
| `SessionEnd` 이벤트 | `Stop`처럼 모든 응답 후가 아니라 종료 시 한 번만 실행됩니다 |
| `INPUT="${CLAUDE_HOWTO_MODULES:-}"` | 훅에는 터미널이 없으므로(`/dev/tty` 사용 불가) 입력은 환경 변수에서 받습니다 |
| `"timeout": 10` | SessionEnd 훅은 자체 `timeout`을 설정하지 않으면 1.5초 후에 취소됩니다 |
| `$CLAUDE_PROJECT_DIR` | 이식 가능한 경로입니다. `/Users/yourname/...`을 하드코딩하지 마십시오 |
| 상단의 가드 절 | 전역으로 설치한 경우 관련 없는 프로젝트에서 훅이 실행되지 않도록 합니다 |
| 저장소 밖에 저장 | `~/` 경로는 `git pull` 후에도 데이터가 덮어쓰이지 않습니다 |

**함께 쓰기: 시각적 진행 상황 추적기**

10개 모듈 전체를 체크박스 UI로 관리하려면 포함된 추적기를 브라우저에서 여십시오.

```bash
open local-progress/index.html
```

진행 상황은 브라우저 `localStorage`에 저장됩니다(저장소 안의 디스크에는 절대 기록되지 않음).
**Export** 버튼으로 스냅샷을 JSON으로 저장하고, **Import**로 복원할 수 있습니다.

## 플러그인 훅

플러그인은 `hooks/hooks.json` 파일에 훅을 포함할 수 있습니다.

**파일:** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**플러그인 훅의 환경 변수:**
- `${CLAUDE_PLUGIN_ROOT}` - 플러그인 디렉터리 경로
- `${CLAUDE_PLUGIN_DATA}` - 플러그인 데이터 디렉터리 경로

이를 통해 플러그인에 사용자 정의 검증 및 자동화 훅을 포함할 수 있습니다.

## MCP 도구용 훅

MCP 도구는 `mcp__<server>__<tool>` 패턴을 따릅니다.

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

## 보안 고려 사항

### 면책 조항

**사용에 따른 책임은 사용자에게 있습니다**: 훅은 임의의 셸 명령어를 실행합니다. 다음 사항에 대한 책임은 전적으로 사용자에게 있습니다.
- 구성한 명령어
- 파일 접근/수정 권한
- 데이터 손실 또는 시스템 손상 가능성
- 프로덕션 사용 전 안전한 환경에서의 훅 테스트

### 보안 참고 사항

- **워크스페이스 신뢰 필요:** `statusLine` 및 `fileSuggestion` 훅 출력 명령어는 이제 워크스페이스 신뢰를 수락해야 적용됩니다.
- **상태 줄 터미널 크기(v2.1.153):** 상태 줄 명령어 스크립트는 이제 `COLUMNS` 및 `LINES` 환경 변수를 받으므로, 터미널 너비/높이에 맞게 출력을 조정할 수 있습니다(예: `[ "$COLUMNS" -lt 80 ] && short_output`).
- **HTTP 훅과 환경 변수:** HTTP 훅에서 헤더 값에 환경 변수를 보간하려면 명시적인 `allowedEnvVars` 목록이 필요합니다. 이를 통해 민감한 환경 변수가 원격 엔드포인트로 실수로 유출되는 것을 방지합니다.
- **관리형 설정 계층 구조:** 이제 `disableAllHooks` 설정은 관리형 설정 계층 구조를 따르므로, 조직 수준 설정으로 개별 사용자가 재정의할 수 없는 훅 비활성화를 강제할 수 있습니다.
- **PowerShell 자동 승인(v2.1.119):** PowerShell 도구 명령어도 Bash와 마찬가지로 권한 모드에서 자동 승인될 수 있습니다. PowerShell 기반 셸 도구로 Claude Code를 실행하는 Windows 사용자도 동일한 동작을 얻습니다.
- **Bash 단순 환경 변수 자동 승인 차단(v2.1.145):** v2.1.145 이전에는 `FOO=bar somecommand` 형태의 Bash 명령어(허용 목록에 없는 명령어 앞에 단순 변수 할당을 붙인 형태)가, 허용 목록에 `FOO=bar`만 있어도 자동 승인될 수 있었습니다. v2.1.145에서 이 문제가 수정되어 이런 명령어는 이제 권한 프롬프트를 거칩니다. 암묵적 허용에 의존하던 스크립트는 프롬프트가 표시되기 시작하므로, 변수 할당만이 아니라 전체 명령어를 포함하는 `Bash(...)` 권한 규칙으로 명시적으로 다시 허용하십시오.

### 모범 사례

| 해야 할 일 | 하지 말아야 할 일 |
|-----|-------|
| 모든 입력을 검증하고 정제하기 | 입력 데이터를 무조건 신뢰하기 |
| 셸 변수를 따옴표로 감싸기: `"$VAR"` | 따옴표 없이 사용하기: `$VAR` |
| 경로 탐색(`..`) 차단하기 | 임의의 경로 허용하기 |
| `$CLAUDE_PROJECT_DIR`와 함께 절대 경로 사용하기 | 경로 하드코딩하기 |
| 민감한 파일(`.env`, `.git/`, 키) 건너뛰기 | 모든 파일 처리하기 |
| 먼저 훅을 단독으로 테스트하기 | 테스트하지 않은 훅 배포하기 |
| HTTP 훅에 명시적인 `allowedEnvVars` 사용하기 | 모든 환경 변수를 웹훅에 노출하기 |

## 디버깅

### 디버그 모드 활성화

훅 로그를 자세히 보려면 디버그 플래그와 함께 Claude를 실행합니다.

```bash
claude --debug
```

### 상세 모드

Claude Code에서 `Ctrl+O`를 사용하면 상세 모드가 활성화되어 훅 실행 진행 상황을 볼 수 있습니다.

### 훅을 독립적으로 테스트하기

```bash
# 샘플 JSON 입력으로 테스트
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# 종료 코드 확인
echo $?
```

## 전체 구성 예시

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

## 훅 실행 세부 정보

| 항목 | 동작 |
|--------|----------|
| **타임아웃** | command/http/mcp_tool은 기본 600초(prompt는 30초, agent는 60초)이며, 훅별로 구성할 수 있습니다 |
| **병렬 처리** | 매칭되는 모든 훅이 병렬로 실행됩니다. v2.1.302부터 한 이벤트에서 prompt 또는 agent 훅은 최대 12개까지만 동시에 실행되고 나머지는 차례를 기다립니다. |
| **중복 제거** | 동일한 훅 명령어는 중복 제거됩니다 |
| **환경** | Claude Code의 환경에서 현재 디렉터리를 기준으로 실행됩니다 |

## 문제 해결

### 훅이 실행되지 않음
- JSON 구성 구문이 올바른지 확인합니다
- 매처 패턴이 도구 이름과 일치하는지 확인합니다
- 스크립트가 존재하고 실행 가능한지 확인합니다: `chmod +x script.sh`
- `claude --debug`를 실행하여 훅 실행 로그를 확인합니다
- 훅이 (명령어 인수가 아니라) stdin에서 JSON을 읽는지 확인합니다

### 훅이 예기치 않게 차단함
- 샘플 JSON으로 훅을 테스트합니다: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- 종료 코드를 확인합니다: 허용은 0, 차단은 2여야 합니다
- stderr 출력을 확인합니다(종료 코드 2일 때 표시됨)

### JSON 파싱 오류
- 명령어 인수가 아니라 항상 stdin에서 읽습니다
- (문자열 조작이 아닌) 올바른 JSON 파싱을 사용합니다
- 누락된 필드를 적절히 처리합니다

## 설치

### 1단계: 훅 디렉터리 만들기
```bash
mkdir -p ~/.claude/hooks
```

### 2단계: 예시 훅 복사하기
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### 3단계: 설정에서 구성하기
`~/.claude/settings.json` 또는 `.claude/settings.json`을 위에 나온 훅 구성으로 편집합니다.

## 관련 개념

- **[체크포인트와 되감기](../08-checkpoints/)** - 대화 상태 저장 및 복원
- **[슬래시 명령어](../01-slash-commands/)** - 사용자 정의 슬래시 명령어 만들기
- **[스킬](../03-skills/)** - 재사용 가능한 자율 기능
- **[서브에이전트](../04-subagents/)** - 작업 위임 실행
- **[플러그인](../07-plugins/)** - 번들 확장 패키지
- **[고급 기능](../09-advanced-features/)** - Claude Code의 고급 기능 살펴보기

## 추가 자료

- **[공식 훅 문서](https://code.claude.com/docs/en/hooks)** - 전체 훅 레퍼런스
- **[CLI 레퍼런스](https://code.claude.com/docs/en/cli-reference)** - 명령줄 인터페이스 문서
- **[메모리 가이드](../02-memory/)** - 영구 컨텍스트 구성

---

**마지막 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/plugins/manifest-reference#quoting-and-path-separators
- https://github.com/anthropics/claude-code/releases/tag/v2.1.295
- https://code.claude.com/docs/en/hooks#pretooluse
- https://code.claude.com/docs/en/hooks#pretooluse-decision-control
- https://code.claude.com/docs/en/hooks#hook-lifecycle
- https://code.claude.com/docs/en/hooks#userpromptsubmit-input
- https://code.claude.com/docs/en/changelog#2-1-299
- https://code.claude.com/docs/en/changelog#2-1-300
- https://code.claude.com/docs/en/changelog#2-1-301
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later
- https://code.claude.com/docs/en/hooks-guide#limitations
- https://code.claude.com/docs/en/hooks#notification
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/hooks#limits-on-skill-hooks
- https://code.claude.com/docs/en/changelog#2-1-309
- https://code.claude.com/docs/en/hooks#failed-hooks-on-windows-without-git-bash
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
