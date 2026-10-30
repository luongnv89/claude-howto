<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 서브에이전트 - 종합 참조 가이드

서브에이전트는 Claude Code가 작업을 위임할 수 있는 전문화된 AI 어시스턴트입니다. 각 서브에이전트는 특정 목적을 가지며, 주 대화와는 별개의 자체 컨텍스트 창을 사용하고, 특정 도구와 사용자 지정 시스템 프롬프트로 구성할 수 있습니다.

## 목차

1. [개요](#개요)
2. [주요 이점](#주요-이점)
3. [파일 위치](#파일-위치)
4. [구성](#구성)
5. [내장 서브에이전트](#내장-서브에이전트)
6. [서브에이전트 관리](#서브에이전트-관리)
7. [서브에이전트 사용](#서브에이전트-사용)
8. [재개 가능한 에이전트](#재개-가능한-에이전트)
9. [서브에이전트 체이닝](#서브에이전트-체이닝)
10. [서브에이전트용 영구 메모리](#서브에이전트용-영구-메모리)
11. [백그라운드 서브에이전트](#백그라운드-서브에이전트)
12. [워크트리 격리](#워크트리-격리)
13. [포크된 서브에이전트](#포크된-서브에이전트)
14. [생성 가능한 서브에이전트 제한](#생성-가능한-서브에이전트-제한)
15. [`claude agents` CLI 명령어](#claude-agents-cli-명령어)
16. [에이전트 팀 (실험적)](#에이전트-팀-실험적)
17. [플러그인 서브에이전트 보안](#플러그인-서브에이전트-보안)
18. [아키텍처](#아키텍처)
19. [컨텍스트 관리](#컨텍스트-관리)
20. [서브에이전트 사용 시기](#서브에이전트-사용-시기)
21. [모범 사례](#모범-사례)
22. [이 폴더의 서브에이전트 예시](#이-폴더의-서브에이전트-예시)
23. [설치 안내](#설치-안내)
24. [파일 구조](#파일-구조)
25. [관련 개념](#관련-개념)
26. [관측 가능성](#관측-가능성)
27. [추가 자료](#추가-자료)

---

## 개요

서브에이전트는 Claude Code에서 다음을 통해 위임된 작업을 실행할 수 있도록 합니다.

- 별도의 컨텍스트 창을 가진 **격리된 AI 어시스턴트** 생성
- 전문 지식을 위한 **맞춤형 시스템 프롬프트** 제공
- 기능 제한을 위한 **도구 접근 제어** 적용
- 복잡한 작업으로 인한 **컨텍스트 오염** 방지
- 여러 전문화된 작업의 **병렬 실행** 활성화

각 서브에이전트는 초기화된 상태에서 독립적으로 작동하며, 자신의 작업에 필요한 특정 컨텍스트만 받고, 그 결과를 주 에이전트에게 반환하여 종합합니다.

**빠른 시작**: Claude에게 서브에이전트를 만들어 달라고 요청하거나("보안을 리뷰하는 서브에이전트를 만들어 줘"), `.claude/agents/<name>.md` 파일을 직접 추가합니다. 아래 [서브에이전트 관리](#서브에이전트-관리)를 참고하십시오.

> **참고**: v2.1.198부터 `/agents` 명령어는 더 이상 대화형 생성 마법사를 열지 않습니다. 서브에이전트는 Claude에게 요청하거나 `.claude/agents/` 파일을 직접 편집하여 생성하고 관리합니다.

---

## 주요 이점

| Benefit | Description |
|---------|-------------|
| **컨텍스트 보존** | 별도의 컨텍스트에서 작동하여 주 대화의 오염을 방지 |
| **전문화된 전문성** | 특정 도메인에 맞게 미세 조정되어 성공률이 높음 |
| **재사용성** | 다양한 프로젝트에서 사용하고 팀과 공유 가능 |
| **유연한 권한** | 서브에이전트 유형에 따라 다른 도구 접근 수준 |
| **확장성** | 여러 에이전트가 여러 측면에서 동시에 작업 |

---

## 파일 위치

서브에이전트 파일은 다양한 범위로 여러 위치에 저장될 수 있습니다.

| Priority | Type | Location | Scope |
|----------|------|----------|-------|
| 1 (최고) | **관리형(Managed)** | 관리형 설정 | 조직 전체 |
| 2 | **CLI 정의** | `--agents` 플래그 (JSON)를 통해 | 세션 전용 |
| 3 | **프로젝트 서브에이전트** | `.claude/agents/` | 현재 프로젝트 |
| 4 | **사용자 서브에이전트** | `~/.claude/agents/` | 모든 프로젝트 |
| 5 (최저) | **플러그인 에이전트** | 플러그인 `agents/` 디렉터리 | 플러그인을 통해 |

중복된 이름이 존재하는 경우, 우선순위가 높은 소스가 우선합니다.

> **중첩된 `.claude/` 우선순위 (v2.1.178)**: 동일한 에이전트 이름이 여러 중첩된 `.claude/agents/` 디렉터리(예: 패키지 수준 `.claude/` 폴더를 가진 모노레포)에 정의되어 있을 때, **현재 작업 디렉터리에 가장 가까운** 정의가 우선합니다. 동일한 '가장 가까운 것이 우선' 규칙은 중첩된 워크플로 및 출력 스타일 정의에도 적용됩니다.

---

## 구성

### 파일 형식

서브에이전트는 YAML 프런트매터로 정의되며, 그 뒤에 마크다운 형식의 시스템 프롬프트가 옵니다.

```yaml
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # 선택 - 생략하면 모든 도구를 상속
disallowedTools: tool4  # 선택 - 명시적으로 금지할 도구
model: sonnet  # 선택 - sonnet, opus, haiku 또는 inherit
permissionMode: default  # 선택 - 권한 모드
maxTurns: 20  # 선택 - 에이전트 턴 수 제한
skills: skill1, skill2  # 선택 - 컨텍스트에 미리 로드할 스킬
mcpServers: server1  # 선택 - 사용할 수 있게 할 MCP 서버
memory: user  # 선택 - 영구 메모리 범위 (user, project, local)
background: false  # 선택 - 백그라운드 작업으로 실행
effort: high  # 선택 - 추론 노력 수준 (low, medium, high, xhigh, max)
isolation: worktree  # 선택 - git 워크트리 격리
initialPrompt: "Start by analyzing the codebase"  # 선택 - 자동 제출되는 첫 번째 턴
experimental:  # 선택 - 실험적 설정 블록
  cacheTtl: "1h"  # 이 서브에이전트의 캐시 TTL: "5m" 또는 "1h" (v2.1.248+)
hooks:  # 선택 - 구성 요소 범위 훅
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.
```

### 구성 필드

| Field | Required | Description |
|-------|----------|-------------|
| `name` | 예 | 고유 식별자(소문자와 하이픈). 조회 시 정규화됩니다(대소문자 및 구분자 무시, 아래 참고). 단, v2.1.218부터 `:`가 포함된 이름은 **거부**됩니다. `:`는 플러그인 네임스페이스용으로 예약되어 있습니다 |
| `description` | 예 | 목적에 대한 자연어 설명. 자동 호출을 장려하려면 "use PROACTIVELY"를 포함하십시오 |
| `tools` | 아니요 | 특정 도구의 쉼표로 구분된 목록. 생략하면 모든 도구를 상속합니다. 에이전트가 `claude --agent`로 주 스레드로 실행될 때 생성 가능한 서브에이전트를 제한하는 `Agent(agent_name)` 구문을 지원하며, 서브에이전트 안에서는 유형 목록이 무시됩니다. MCP: `mcp__<server>__*`는 서버 전체를 허용합니다(v2.1.299+: 정확히 그 서버 이름에만 일치). |
| `disallowedTools` | 아니요 | 서브에이전트가 사용해서는 안 되는 도구의 쉼표로 구분된 목록. 이름에 `__`가 포함된 MCP 서버의 경우: 여기에 `mcp__reports__*`를 쓰면 모든 `reports__v2` 도구도 함께 막히므로 `reports` 도구를 하나씩 나열하십시오. `tools`에서는 이런 서버를 `mcp__reports__v2__*`로 허용합니다 |
| `model` | 아니요 | 사용할 모델: `sonnet`, `opus`, `haiku`, 전체 모델 ID 또는 `inherit`. 기본값은 구성된 서브에이전트 모델입니다 |
| `permissionMode` | 아니요 | `default`(Manual 모드, v2.1.200부터 `manual`도 별칭으로 허용), `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan`, `auto`. v2.1.212부터 Task 도구의 `mode` 호출 매개변수는 지원 중단(deprecated)되어 무시되며, 여기서 재정의하지 않으면 서브에이전트는 기본적으로 부모 세션의 권한 모드를 상속합니다. 부모가 `bypassPermissions`, `acceptEdits` 또는 `auto`로 실행 중이면 서브에이전트의 `permissionMode`는 무시됩니다. 부모가 `plan` 모드이면 `permissionMode` 값과 관계없이 서브에이전트도 계획 모드에 머물며(에이전트 팀 팀원으로 실행되는 경우 제외), `dontAsk`를 설정했다면 계획 모드에서 확인을 요청했을 작업이 대신 거부됩니다 |
| `maxTurns` | 아니요 | 서브에이전트가 취할 수 있는 에이전트 턴의 최대 수 |
| `skills` | 아니요 | 미리 로드할 스킬의 쉼표로 구분된 목록. 시작 시 전체 스킬 콘텐츠를 서브에이전트의 컨텍스트에 주입합니다. **v2.1.133+:** 서브에이전트도 Skill 도구를 통해 프로젝트, 사용자 및 플러그인 스킬을 발견합니다. 이는 주 세션과 동일한 카탈로그이며, 더 이상 자체 내장된 세트에 국한되지 않습니다. 미리 로드되는 스킬은 최대 32개이며 각각 한 번만 로드되고, Skill 도구가 있는 서브에이전트는 나머지도 호출할 수 있습니다(v2.1.295). |
| `mcpServers` | 아니요 | 서브에이전트에서 사용할 수 있도록 할 MCP 서버 |
| `hooks` | 아니요 | 이 서브에이전트가 활성화된 동안에만 실행되는 훅. 모든 훅 이벤트를 지원하며, 가장 흔한 것은 `PreToolUse`, `PostToolUse`, `Stop`(`SubagentStop`으로 실행)입니다 |
| `memory` | 아니요 | 영구 메모리 디렉터리 범위: `user`, `project` 또는 `local` |
| `background` | 아니요 | 서브에이전트는 이미 기본적으로 백그라운드에서 실행됩니다(v2.1.198). v2.1.302부터는 데스크톱 앱과 VS Code에서 주 대화의 서브에이전트도 백그라운드에서 시작합니다. 포크 모드가 켜져 있는 동안(기본값) Claude는 이를 기다릴 수 없습니다. `claude -p`, Agent SDK, 데스크톱 앱, VS Code에서 서브에이전트 자신의 Agent 호출은 기본적으로 포그라운드에서 실행됩니다. 항상 백그라운드로 *강제*하고 인라인 실행을 막으려면 `true`로 설정합니다 |
| `effort` | 아니요 | 추론 노력 수준: `low`, `medium`, `high`, `xhigh` 또는 `max`. 세션의 노력 수준을 재정의하며, 사용 가능한 수준은 모델에 따라 다릅니다. Claude가 Agent 도구를 호출할 때 `effort` 값을 전달할 수도 있습니다(v2.1.292). |
| `isolation` | 아니요 | 서브에이전트에 자체 git 워크트리를 제공하려면 `worktree`로 설정 |
| `initialPrompt` | 아니요 | 서브에이전트가 주 에이전트로 실행될 때 자동으로 제출되는 첫 번째 턴 |
| `color` | 아니요 | 작업 목록과 트랜스크립트에서 서브에이전트의 표시 색상. `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` 중 하나 |
| `experimental` | 아니요 | 실험적 설정 블록(v2.1.248+). `experimental.cacheTtl`은 이 서브에이전트의 캐시 TTL을 `"5m"` 또는 `"1h"`로 설정합니다 |
| `omitClaudeMd` | 아니요 | `true`로 설정하면 사용자, 프로젝트, 로컬 CLAUDE.md 파일 없이 서브에이전트를 시작합니다(v2.1.271+). 관리형 정책 파일은 여전히 로드되며, 관리형 서브에이전트는 예외입니다. 에이전트가 `--agent` 또는 `agent` 설정으로 주 세션 에이전트로 실행될 때는 무시됩니다. `--agents` JSON에서도 사용할 수 있습니다 |
| `autoCompactWindow` | 아니요 | 이 서브에이전트의 컨텍스트를 주 대화 창보다 일찍 자동 압축합니다(v2.1.296+, `--agents` JSON에서도 사용 가능) |

#### 서브에이전트 모델 환경 변수

두 가지 환경 변수가 서브에이전트가 실행되는 모델에 영향을 줍니다.

| Variable | Version | Description |
|----------|---------|-------------|
| `CLAUDE_CODE_SUBAGENT_MODEL` | — | 서브에이전트에 사용할 모델을 설정합니다 |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` | v2.1.257+ | `1`로 설정하면 서브에이전트 프런트매터의 `model:`보다 서브에이전트 모델을 우선 적용합니다 |

> **v2.1.251에서 우선순위 변경**: 해당 릴리스 이전에는 `CLAUDE_CODE_SUBAGENT_MODEL`이 먼저 적용되어 `model: inherit`를 포함한 에이전트 프런트매터를 재정의했습니다. v2.1.251부터는 서브에이전트 자신의 `model:` 프런트매터가 우선합니다. 예를 들어 평가 실행 전체를 하나의 모델로 고정하려는 경우처럼 환경 변수가 다시 프런트매터를 재정의하게 하려면 `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`(v2.1.257+)을 설정하십시오.

### 주 스레드 에이전트 프런트매터 존중 (v2.1.117+/v2.1.119+)

에이전트가 주 스레드 에이전트로 호출될 때 (`claude --agent <name>` 또는 `--print` 모드를 통해), 다음 프런트매터 필드가 존중됩니다.

| Field | Version | Notes |
|-------|---------|-------|
| `mcpServers` | v2.1.117+ | 에이전트가 `claude --agent <name>`을 통해 주 스레드 에이전트로 호출될 때 로드됩니다 |
| `permissionMode` | v2.1.119+ | `--agent <name>`을 통해 내장 에이전트에 대해 존중됩니다 |
| `tools` / `disallowedTools` | v2.1.119+ | `--print` 모드(비대화형/스크립트 사용)에서 존중됩니다 |

**예시 — `mcpServers` 및 `permissionMode`를 사용하는 에이전트:**

```yaml
---
name: secure-researcher
description: Research agent with scoped MCP access and restricted permissions
permissionMode: acceptEdits
mcpServers:
  notion:
    type: http
    url: https://mcp.notion.com/mcp
  github:
    type: http
    url: https://api.githubcopilot.com/mcp/
    headers:
      Authorization: "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
tools: Read, Grep, Glob
---

You are a research agent. You may query Notion and GitHub through the
configured MCP servers, and read local files, but you cannot write or
execute commands outside of accepted edits.
```

실행 방법:

```bash
claude --agent secure-researcher
```

### 도구 구성 옵션

**옵션 1: 모든 도구 상속 (필드 생략)**
```yaml
---
name: full-access-agent
description: Agent with all available tools
---
```

**옵션 2: 개별 도구 지정**
```yaml
---
name: limited-agent
description: Agent with specific tools only
tools: Read, Grep, Glob, Bash
---
```

> **Glob/Grep에 대한 참고 (v2.1.113+):** 기본 macOS/Linux 빌드에서는 Glob과 Grep이 별도의 도구가 아닌 Bash 도구를 통해 `bfs`/`ugrep`으로 제공됩니다. Windows 및 npm-JS 빌드에서는 여전히 독립형 도구로 노출됩니다. 작성자는 `allowedTools`에서 Glob/Grep을 계속 참조할 수 있으며, 백엔드 대체는 투명하게 이루어집니다.

**옵션 3: 조건부 도구 접근**
```yaml
---
name: conditional-agent
description: Agent with filtered tool access
tools: Read, Bash(npm:*), Bash(test:*)
---
```

### CLI 기반 구성

단일 세션에 대한 서브에이전트를 JSON 형식의 `--agents` 플래그를 사용하여 정의합니다.

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

**`--agents` 플래그용 JSON 형식:**

```json
{
  "agent-name": {
    "description": "Required: when to invoke this agent",
    "prompt": "Required: system prompt for the agent",
    "tools": ["Optional", "array", "of", "tools"],
    "model": "optional: sonnet|opus|haiku"
  }
}
```

> **참고**: v2.1.243부터 `--agents`는 잘못된 JSON이나 잘못된 에이전트 정의를 더 이상 조용히 무시하지 않습니다. `--mcp-config`와 마찬가지로 Claude Code가 명확한 오류와 함께 종료됩니다.

**에이전트 정의의 우선순위:**

에이전트 정의는 다음 우선순위 순서로 로드됩니다(첫 번째 일치 항목이 우선합니다).
1. **관리형(Managed)** - 관리형 설정 (조직 전체)
2. **CLI 정의** - `--agents` 플래그 (세션 전용, JSON)
3. **프로젝트 수준** - `.claude/agents/` (현재 프로젝트)
4. **사용자 수준** - `~/.claude/agents/` (모든 프로젝트)
5. **플러그인 수준** - 플러그인 `agents/` 디렉터리

이를 통해 CLI 정의는 단일 세션에 대해 프로젝트, 사용자, 플러그인 정의를 재정의할 수 있으며, 관리형 정의는 여전히 우선합니다.

---

## 내장 서브에이전트

Claude Code에는 항상 사용할 수 있는 여러 내장 서브에이전트가 포함되어 있습니다.

| Agent | Model | Purpose |
|-------|-------|---------|
| **general-purpose** | 상속 | 복잡하고 다단계적인 작업 |
| **Plan** | 상속 | 계획 모드를 위한 조사 |
| **Explore** | 상속 (최대 Opus) | 읽기 전용 코드베이스 탐색 (quick/medium/very thorough) |
| **claude** | 상속 | 더 전문화된 에이전트에 맞지 않는 작업을 처리하는 범용 에이전트. 서브에이전트가 사용할 수 있는 모든 도구를 가집니다. 디스패치된 백그라운드 세션의 기본 에이전트이기도 합니다 |
| **statusline-setup** | Sonnet | `/statusline`으로 상태 표시줄을 구성할 때 실행 |
| **claude-code-guide** | Haiku | Claude Code 기능 질문에 답변 |

### 일반 목적 서브에이전트

| Property | Value |
|----------|-------|
| **모델** | 부모로부터 상속 |
| **도구** | 모든 도구 |
| **목적** | 복잡한 조사 작업, 다단계 작업, 코드 수정 |

**사용 시기**: 복잡한 추론을 통해 탐색과 수정이 모두 필요한 작업.

### 계획 서브에이전트

| Property | Value |
|----------|-------|
| **모델** | 부모로부터 상속 |
| **도구** | Read, Glob, Grep, Bash |
| **목적** | 계획 모드에서 코드베이스를 조사하기 위해 자동으로 사용됩니다 |

**사용 시기**: Claude가 계획을 제시하기 전에 코드베이스를 이해해야 할 때.

### 탐색 서브에이전트

| Property | Value |
|----------|-------|
| **모델** | 세션 모델을 상속하되 최대 Opus로 제한됩니다(v2.1.198). 빠르고 저렴하게 유지하려면 `model: haiku`로 설정하십시오 |
| **모드** | 엄격히 읽기 전용 |
| **도구** | Glob, Grep, Read, Bash (읽기 전용 명령만) |
| **목적** | 빠른 코드베이스 검색 및 분석 |

**사용 시기**: 코드를 변경하지 않고 검색/이해할 때.

**철저함 수준** - 탐색 깊이를 지정합니다.
- **"quick"** - 최소한의 탐색으로 빠른 검색, 특정 패턴을 찾는 데 유용
- **"medium"** - 적절한 탐색, 속도와 철저함의 균형, 기본 접근 방식
- **"very thorough"** - 여러 위치와 명명 규칙에 걸친 포괄적인 분석, 시간이 더 오래 걸릴 수 있음

### Claude 서브에이전트

| Property | Value |
|----------|-------|
| **모델** | 부모로부터 상속 |
| **도구** | 서브에이전트가 사용할 수 있는 모든 도구 |
| **목적** | 더 전문화된 에이전트에 맞지 않는 작업을 처리하는 범용 에이전트 |

**사용 시기**: 작업이 더 전문화된 내장 에이전트와 맞지 않을 때. 디스패치된 백그라운드 세션의 기본 에이전트이기도 하며, 어떤 권한 모드로 시작하는지는 해당 세션이 어떻게 시작되었는지에 따라 달라집니다.

### 상태 표시줄 설정 서브에이전트

| Property | Value |
|----------|-------|
| **모델** | Sonnet |
| **도구** | Read, Write, Bash |
| **목적** | Claude Code 상태 표시줄 디스플레이 구성 |

**사용 시기**: 상태 표시줄을 설정하거나 사용자 지정할 때.

### Claude Code 가이드 서브에이전트 (`claude-code-guide`)

| Property | Value |
|----------|-------|
| **모델** | Haiku (빠르고 낮은 지연 시간) |
| **도구** | 읽기 전용 |
| **목적** | Claude Code 기능 및 사용법에 대한 질문에 답변 |

**사용 시기**: 사용자가 Claude Code 작동 방식이나 특정 기능 사용법에 대해 질문할 때.

---

## 서브에이전트 관리

### Claude에게 요청 (권장)

서브에이전트를 만들거나 관리하는 가장 간단한 방법은 Claude에게 직접 요청하는 것입니다.

```text
Create a subagent that reviews code for security vulnerabilities.
```

Claude가 적절한 프런트매터(도구, 모델, 설명)를 골라 `.claude/agents/<name>.md` 파일을 작성해 줍니다. 이후 파일을 직접 다듬거나 Claude에게 수정을 요청할 수 있습니다.

> **참고**: `/agents` 명령어는 더 이상 대화형 생성 마법사를 열지 않습니다(v2.1.198에서 제거). 이제는 Claude에게 요청하거나 `.claude/agents/` 파일을 직접 편집하라고 안내합니다.

### 직접 파일 관리

```bash
# 프로젝트 서브에이전트 생성
mkdir -p .claude/agents
cat > .claude/agents/test-runner.md << 'EOF'
---
name: test-runner
description: Use proactively to run tests and fix failures
---

You are a test automation expert. When you see code changes, proactively
run the appropriate tests. If tests fail, analyze the failures and fix
them while preserving the original test intent.
EOF

# 사용자 서브에이전트 생성 (모든 프로젝트에서 사용 가능)
mkdir -p ~/.claude/agents
```

---

## 서브에이전트 사용

### 자동 위임

Claude는 다음을 기반으로 작업을 선제적으로 위임합니다.
- 요청에 있는 작업 설명
- 서브에이전트 구성의 `description` 필드
- 현재 컨텍스트 및 사용 가능한 도구

선제적인 사용을 장려하려면 `description` 필드에 "use PROACTIVELY" 또는 "MUST BE USED"를 포함하세요.

```yaml
---
name: code-reviewer
description: Expert code review specialist. Use PROACTIVELY after writing or modifying code.
---
```

### 명시적 호출

특정 서브에이전트를 명시적으로 요청할 수 있습니다.

```
> Use the test-runner subagent to fix failing tests
> Have the code-reviewer subagent look at my recent changes
> Ask the debugger subagent to investigate this error
```

> **대소문자 및 구분자 무시 `subagent_type` 일치 (v2.1.140)**: `Agent` 도구 호출 또는 `--agent` 플래그의 `subagent_type`은 대소문자를 무시하고 구분자 스타일을 무시하여 일치시킵니다. 즉, `code-reviewer`, `Code Reviewer`, `code_reviewer`는 모두 동일한 에이전트로 해결됩니다. 이는 사소한 대문자 사용 차이로 인해 기본 에이전트로 자동으로 대체되는 오랜 문제점을 해결합니다.

### @-멘션 호출

`@` 접두사를 사용하여 특정 서브에이전트가 호출되도록 보장합니다(자동 위임 휴리스틱을 우회합니다).

```
> @"code-reviewer (agent)" review the auth module
```

### 세션 전체 에이전트

특정 에이전트를 주 에이전트로 사용하여 전체 세션을 실행합니다.

```bash
# CLI 플래그 사용
claude --agent code-reviewer

# settings.json 사용
{
  "agent": "code-reviewer"
}
```

### 사용 가능한 에이전트 목록

어떤 서브에이전트가 구성되어 있는지 보려면 Claude에게 묻거나 `.claude/agents/`와 `~/.claude/agents/`를 살펴보십시오. (`claude agents`는 이와 무관합니다. 이 명령어는 백그라운드 세션용 에이전트 뷰를 엽니다. [CLI](../10-cli/README.md#에이전트-뷰-claude-agents-v21139) 참고.)

---

## 재개 가능한 에이전트

서브에이전트는 전체 컨텍스트를 보존한 채 이전 대화를 계속할 수 있습니다.

```bash
# 최초 호출
> Use the code-analyzer agent to start reviewing the authentication module
# agentId: "abc123" 반환

# 나중에 에이전트 재개
> Resume agent abc123 and now analyze the authorization logic as well
```

**사용 사례**:
- 여러 세션에 걸친 장기 실행 연구
- 컨텍스트 손실 없이 반복적인 개선
- 컨텍스트를 유지하는 다단계 워크플로

---

## 서브에이전트 체이닝

여러 서브에이전트를 순서대로 실행합니다.

```bash
> First use the code-analyzer subagent to find performance issues,
  then use the optimizer subagent to fix them
```

이를 통해 한 서브에이전트의 출력이 다른 서브에이전트의 입력으로 사용되는 복잡한 워크플로를 구현할 수 있습니다.

---

## 서브에이전트용 영구 메모리

`memory` 필드는 서브에이전트에게 대화를 넘어서도 유지되는 영구 디렉터리를 제공합니다. 이를 통해 서브에이전트는 시간이 지남에 따라 지식을 축적하고, 세션 간에 지속되는 메모, 발견 사항 및 컨텍스트를 저장할 수 있습니다.

### 메모리 범위

| Scope | Directory | Use Case |
|-------|-----------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | 모든 프로젝트에 걸쳐 개인 메모 및 환경 설정 |
| `project` | `.claude/agent-memory/<name>/` | 팀과 공유되는 프로젝트별 지식 |
| `local` | `.claude/agent-memory-local/<name>/` | 버전 제어에 커밋되지 않는 로컬 프로젝트 지식 |

### 작동 방식

- 메모리 디렉터리의 `MEMORY.md` 파일 첫 200줄이 서브에이전트의 시스템 프롬프트에 자동으로 로드됩니다
- 서브에이전트가 메모리 파일을 관리할 수 있도록 `Read`, `Write`, `Edit` 도구가 자동으로 활성화됩니다
- 서브에이전트는 필요에 따라 메모리 디렉터리에 추가 파일을 생성할 수 있습니다

### 구성 예시

```yaml
---
name: researcher
description: Research assistant that keeps findings in persistent memory across sessions
memory: user
---

You are a research assistant. Use your memory directory to store findings,
track progress across sessions, and build up knowledge over time.

Check your MEMORY.md file at the start of each session to recall previous context.
```

```mermaid
graph LR
    A["Subagent<br/>Session 1"] -->|writes| M["MEMORY.md<br/>(persistent)"]
    M -->|loads into| B["Subagent<br/>Session 2"]
    B -->|updates| M
    M -->|loads into| C["Subagent<br/>Session 3"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style M fill:#f3e5f5,stroke:#333,color:#333
```

---

## 백그라운드 서브에이전트

서브에이전트는 기본적으로 백그라운드에서 실행됩니다(v2.1.198). v2.1.302부터는 데스크톱 앱과 VS Code에서 주 대화의 서브에이전트도 백그라운드에서 시작합니다. 포크 모드가 켜져 있는 동안(기본값) Claude는 이를 기다릴 수 없습니다. `claude -p`, Agent SDK, 데스크톱 앱, VS Code에서 서브에이전트 자신의 Agent 호출은 기본적으로 포그라운드에서 실행됩니다. 서브에이전트가 실행되는 동안 Claude는 주 대화 작업을 계속하고 서브에이전트가 끝나면 알림을 받으므로, 더 이상 서브에이전트가 돌아올 때까지 기다렸다가 진행할 필요가 없습니다. VS Code(v2.1.304+)에서는 백그라운드 서브에이전트가 모든 단계를 채팅에 스트리밍하는 대신 Agent 카드 아래에 한 줄의 상태 표시로 나타납니다. `/tasks`를 열고 해당 항목을 클릭하면 도구 호출과 트랜스크립트를 볼 수 있습니다.

### 구성

백그라운드가 이미 기본값이므로, 프런트매터의 `background: true`는 서브에이전트를 항상 백그라운드에서 실행하도록 *강제*하고 인라인 실행을 막습니다.

```yaml
---
name: long-runner
background: true
description: Performs long-running analysis tasks in the background
---
```

### 키보드 단축키

| Shortcut | Action |
|----------|--------|
| `Ctrl+B` | 현재 실행 중인 서브에이전트 작업을 백그라운드로 전환 |
| `Ctrl+X` `Ctrl+K` | 실행 중인 모든 백그라운드 서브에이전트 중지 (확인하려면 3초 안에 두 번 누름. 기존 `Ctrl+F`를 대체) |

### 백그라운드 작업 비활성화

환경 변수를 설정하여 백그라운드 작업 지원을 완전히 비활성화합니다.

```bash
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
```

### Claude가 서브에이전트를 기다리게 하기

아무것도 구성하지 않으면 Claude가 주 대화에서 생성한 서브에이전트는 백그라운드에서 시작합니다. `claude -p`와 Agent SDK에서는 Claude가 스스로 판단하거나 사용자가 요청할 때 여전히 서브에이전트를 기다릴 수 있습니다. 대화형 터미널, VS Code, 데스크톱 세션에서는 포크 모드를 끈 뒤에만 Claude가 기다릴 수 있습니다(v2.1.302+).

```json
{
  "env": {
    "CLAUDE_CODE_FORK_SUBAGENT": "0"
  }
}
```

`claude`를 다시 시작한 뒤(또는 새 VS Code 대화를 연 뒤) 예를 들어 "reviewer 서브에이전트를 실행하고 보고서를 기다려 줘"라고 요청하십시오. `Ctrl+B`로 기다리는 작업을 여전히 백그라운드로 보낼 수 있습니다. 대신 `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`을 설정하면 Claude가 모든 서브에이전트를 기다리며, 백그라운드 명령어도 꺼집니다.

---

## 워크트리 격리

`isolation: worktree` 설정은 서브에이전트에게 자체 git 워크트리를 제공하여, 주 작업 트리에 영향을 주지 않고 독립적으로 변경할 수 있도록 합니다.

### 구성

```yaml
---
name: feature-builder
isolation: worktree
description: Implements features in an isolated git worktree
tools: Read, Write, Edit, Bash, Grep, Glob
---
```

### 작동 방식

```mermaid
graph TB
    Main["Main Working Tree"] -->|spawns| Sub["Subagent with<br/>Isolated Worktree"]
    Sub -->|makes changes in| WT["Separate Git<br/>Worktree + Branch"]
    WT -->|no changes| Clean["Auto-cleaned"]
    WT -->|has changes| Return["Returns worktree<br/>path and branch"]

    style Main fill:#e1f5fe,stroke:#333,color:#333
    style Sub fill:#f3e5f5,stroke:#333,color:#333
    style WT fill:#e8f5e9,stroke:#333,color:#333
    style Clean fill:#fff3e0,stroke:#333,color:#333
    style Return fill:#fff3e0,stroke:#333,color:#333
```

- 서브에이전트는 별도의 브랜치에서 자체 git 워크트리에서 작동합니다
- 서브에이전트가 변경 사항을 만들지 않으면 워크트리는 자동으로 정리됩니다
- 변경 사항이 있는 경우, 워크트리 경로와 브랜치 이름이 검토 또는 병합을 위해 주 에이전트로 반환됩니다

---

## 포크된 서브에이전트

포크된 서브에이전트는 새롭게 시작하는 대신, 포크 시점의 부모 대화 전체(시스템 프롬프트, 도구, 모델, 메시지 기록, 프롬프트 캐시)를 상속합니다. 이는 지금까지 수행한 작업을 잃지 않고 대체 경로를 탐색하는 데 유용합니다.

> **가용성**: v2.1.117에서 GA(General Availability)입니다. **v2.1.232부터 대화형 세션에서는 포크 모드가 기본으로 켜져 있습니다.** 퍼스트파티 빌드 여부와 관계없이 모든 빌드에 해당합니다. v2.1.302부터는 비대화형 모드(`claude -p`), Agent SDK, 데스크톱 앱, VS Code에서도 기본으로 켜져 있으며, `claude mcp serve`는 포크 서브에이전트를 제공하지 않습니다. v2.1.232보다 오래된 Claude Code에서는 `CLAUDE_CODE_FORK_SUBAGENT=1`을 설정하여 켜십시오.

> **포크 모드의 서브에이전트는 백그라운드에서 실행됩니다.** 포크 모드가 켜져 있는 곳(v2.1.302부터 기본적으로 모든 곳)에서는 Claude Code가 포크 여부와 관계없이 서브에이전트를 백그라운드에서 실행합니다. 그러면 대화형 터미널, VS Code, 데스크톱 세션에서 Claude는 서브에이전트를 기다릴 수 없습니다. 기다리게 하려면 포크 모드를 끄십시오([Claude가 서브에이전트를 기다리게 하기](#claude가-서브에이전트를-기다리게-하기) 참고).

### 구성

포크는 에이전트 파일에서 정의하지 않습니다. Claude가 Agent 도구에서 `subagent_type: "fork"`로 시작하거나, 사용자가 `/subtask <task>`로 직접 시작합니다(v2.1.212+).

```text
/subtask Explore an alternative implementation path and report the trade-offs
```

포크는 또 다른 포크를 생성할 수 없습니다. 포크를 막으려면 거부 규칙 `Agent(fork)`를 추가합니다.

```json
{
  "permissions": {
    "deny": ["Agent(fork)"]
  }
}
```

> **참고**: `context: fork`는 서브에이전트 필드가 아니라 **스킬** 프런트매터 필드입니다([스킬](../03-skills/README.md) 참고). Claude Code는 에이전트 정의에서 인식하지 못하는 필드를 조용히 무시합니다.

### 포크 모드 명시적으로 설정하기

모든 곳에서 포크 모드를 끄려면 `CLAUDE_CODE_FORK_SUBAGENT=0`을 설정합니다. v2.1.302 이전 버전에서는 `claude -p`와 Agent SDK에서 포크를 켜려면 `1`로 설정합니다.

```bash
export CLAUDE_CODE_FORK_SUBAGENT=0
claude
```

### 포크와 클린 컨텍스트 사용 시기

| Scenario | Fork (`subagent_type: "fork"`) | Clean context (default) |
|----------|-----------------|-------------------------|
| 대체 구현 탐색 | 예 | 아니요 (컨텍스트를 잃게 됨) |
| 기존 컨텍스트를 사용한 장기 조사 | 예 | 아니요 |
| 독립적인 전문화된 작업 | 아니요 | 예 |
| 컨텍스트 오염 방지 | 아니요 | 예 |

---

## 생성 가능한 서브에이전트 제한

`claude --agent`로 주 스레드에서 실행되는 에이전트가 어떤 서브에이전트를 생성할 수 있는지는 `tools` 필드의 `Agent(agent_type)` 구문으로 제어할 수 있습니다. 이는 위임을 위해 특정 서브에이전트를 허용 목록에 추가하는 방법을 제공합니다. 서브에이전트 정의에서는 괄호 안의 유형 목록이 무시됩니다.

> **참고**: v2.1.63에서 `Task` 도구는 `Agent`로 이름이 변경되었습니다. 기존 `Task(...)` 참조도 여전히 별칭으로 작동합니다.

### 예시

```yaml
---
name: coordinator
description: Coordinates work between specialized agents
tools: Agent(worker, researcher), Read, Bash
---

You are a coordinator agent. You can delegate work to the "worker" and
"researcher" subagents only. Use Read and Bash for your own exploration.
```

이 예시에서 `claude --agent coordinator`를 실행하면 주 스레드는 `worker`와 `researcher` 서브에이전트만 생성할 수 있습니다. 다른 곳에 정의되어 있더라도 다른 서브에이전트는 생성할 수 없습니다. `coordinator`가 대신 서브에이전트로 실행되면 유형 목록은 무시됩니다.

---

## `claude agents` CLI 명령어

`claude agents`는 **에이전트 뷰**(v2.1.139+)를 엽니다. 백그라운드 세션을 상태별로 그룹화하여 보여 주는 전체 화면 목록입니다. 구성된 서브에이전트 정의는 나열하지 않으며, 세션 상태를 스크립트로 다루려면 `claude agents --json`을 사용합니다.

```bash
claude agents
claude agents --json
```

구성된 서브에이전트는 `.claude/agents/`(프로젝트)와 `~/.claude/agents/`(사용자)에 있습니다.

---

## 에이전트 팀 (실험적)

에이전트 팀은 여러 Claude Code 인스턴스가 복잡한 작업을 함께 수행하도록 조정합니다. (결과를 반환하는 위임된 하위 작업인) 서브에이전트와 달리, 팀원은 자체 컨텍스트 창으로 독립적으로 작업하며 공유 사서함 시스템을 통해 서로 직접 메시지를 주고받을 수 있습니다.

> **공식 문서**: [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)

> **참고**: 에이전트 팀은 실험적 기능이며 기본적으로 비활성화되어 있습니다. Claude Code v2.1.32+가 필요합니다. 사용하기 전에 활성화해야 합니다.

### 서브에이전트 vs 에이전트 팀

| Aspect | Subagents | Agent Teams |
|--------|-----------|-------------|
| **위임 모델** | 부모가 하위 작업을 위임하고 결과를 기다립니다 | 팀 리더가 작업을 조정하고, 팀원은 독립적으로 실행합니다 |
| **컨텍스트** | 하위 작업당 새로운 컨텍스트, 결과는 다시 주입 | 각 팀원은 자체 영구 컨텍스트 창을 유지합니다 |
| **조정** | 부모가 관리하는 순차적 또는 병렬 | 자동 종속성 관리가 가능한 공유 작업 목록 |
| **통신** | 결과는 부모에게만 반환 (에이전트 간 메시징 없음) | 팀원은 사서함을 통해 서로 직접 메시지를 주고받을 수 있습니다 |
| **세션 재개** | 지원됨 | 인-프로세스 팀원에서는 지원되지 않음 |
| **최적 사용** | 집중적이고 잘 정의된 하위 작업 | 에이전트 간 통신 및 병렬 실행이 필요한 복잡한 작업 |

### 에이전트 팀 활성화

환경 변수를 설정하거나 `settings.json`에 추가합니다.

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

또는 `settings.json`에서 설정합니다.

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 팀 시작

활성화되면 프롬프트에서 Claude에게 팀원과 함께 작업하도록 요청하십시오.

```
User: Build the authentication module. Use a team — one teammate for the API endpoints,
      one for the database schema, and one for the test suite.
```

Claude는 팀을 생성하고 작업을 할당하며 작업을 자동으로 조정합니다.

### 디스플레이 모드

팀원 활동이 표시되는 방식을 제어합니다.

| Mode | Flag | Description |
|------|------|-------------|
| **Auto** | `--teammate-mode auto` | 터미널에 가장 적합한 디스플레이 모드를 자동으로 선택합니다 |
| **In-process** (default) | `--teammate-mode in-process` | 현재 터미널에 팀원 출력을 인라인으로 표시합니다 |
| **Split-panes** | `--teammate-mode tmux` | 각 팀원을 별도의 tmux 또는 iTerm2 창에 엽니다 |
| **iTerm2** | `--teammate-mode iterm2` | (v2.1.186+) 전용 iTerm2 창에 팀원을 생성합니다. `it2` CLI가 필요하며, 자동 모드에서는 찾을 수 없을 때 경고합니다 |

```bash
claude --teammate-mode tmux
```

`settings.json`에서 디스플레이 모드를 설정할 수도 있습니다.

```json
{
  "teammateMode": "tmux"
}
```

> **참고**: 분할 창 모드에는 tmux 또는 iTerm2가 필요합니다. VS Code 터미널, Windows 터미널 또는 Ghostty에서는 사용할 수 없습니다.

### 내비게이션

팀원 간에 이동하려면 에이전트 패널에서 위아래 화살표 키로 이동한 뒤 Enter를 누르거나(인-프로세스 모드), 팀원의 창을 클릭합니다(분할 창 모드).

### 팀 구성

팀 구성은 `~/.claude/teams/{team-name}/config.json`에 저장됩니다.

### 팀원 모델 선택

v2.1.234부터 `/config`의 "Default teammate model" 설정이 제거되었습니다. 이제 생성 호출에서 다른 모델을 명시적으로 지정하지 않는 한, 팀원은 기본적으로 팀 리더의 모델을 상속합니다.

### 아키텍처

```mermaid
graph TB
    Lead["Team Lead<br/>(Coordinator)"]
    TaskList["Shared Task List<br/>(Dependencies)"]
    Mailbox["Mailbox<br/>(Messages)"]
    T1["Teammate 1<br/>(Own Context)"]
    T2["Teammate 2<br/>(Own Context)"]
    T3["Teammate 3<br/>(Own Context)"]

    Lead -->|assigns tasks| TaskList
    Lead -->|sends messages| Mailbox
    TaskList -->|picks up work| T1
    TaskList -->|picks up work| T2
    TaskList -->|picks up work| T3
    T1 -->|reads/writes| Mailbox
    T2 -->|reads/writes| Mailbox
    T3 -->|reads/writes| Mailbox
    T1 -->|updates status| TaskList
    T2 -->|updates status| TaskList
    T3 -->|updates status| TaskList

    style Lead fill:#e1f5fe,stroke:#333,color:#333
    style TaskList fill:#fff9c4,stroke:#333,color:#333
    style Mailbox fill:#f3e5f5,stroke:#333,color:#333
    style T1 fill:#e8f5e9,stroke:#333,color:#333
    style T2 fill:#e8f5e9,stroke:#333,color:#333
    style T3 fill:#e8f5e9,stroke:#333,color:#333
```

**핵심 구성 요소**:

- **팀 리더**: 팀을 생성하고 작업을 할당하며 조정하는 주 Claude Code 세션
- **공유 작업 목록**: 자동 종속성 추적 기능이 있는 동기화된 작업 목록
- **사서함**: 팀원이 상태를 전달하고 조정할 수 있는 에이전트 간 메시징 시스템
- **팀원**: 자체 컨텍스트 창을 가진 독립적인 Claude Code 인스턴스

### 작업 할당 및 메시징

팀 리더는 작업을 태스크로 나누고 팀원에게 할당합니다. 공유 태스크 목록은 다음을 처리합니다.

- **자동 종속성 관리** — 태스크는 종속 태스크가 완료될 때까지 기다립니다
- **상태 추적** — 팀원은 작업하면서 태스크 상태를 업데이트합니다
- **에이전트 간 메시징** — 팀원은 조정을 위해 사서함을 통해 메시지를 보냅니다 (예: "데이터베이스 스키마가 준비되었으니 쿼리 작성을 시작할 수 있습니다")

### 계획 승인 워크플로

복잡하거나 위험한 작업이라면 팀원을 요청하기 전에 리더를 계획 모드로 전환하십시오. 리더가 계획 모드일 때 생성된 팀원은 계획이 준비될 때까지 읽기 전용으로 작업한 다음 리더에게 계획 승인 요청을 보냅니다. 생성 이후 해당 팀원의 권한 모드를 바꾸지 않았다면 Claude Code는 요청이 도착하는 즉시 계획을 승인하며(사용자에게 묻지 않음), 팀원의 편집과 명령어는 여전히 일반 권한 프롬프트를 거칩니다. 실행 중인 인-프로세스 팀원을 `Shift+Tab`으로 계획 모드로 전환하면, 그 계획은 리더가 대신 검토합니다.

### 팀을 위한 훅 이벤트

에이전트 팀은 두 가지 추가 [훅 이벤트](../06-hooks/)를 도입합니다.

| Event | Fires When | Use Case |
|-------|-----------|----------|
| `TeammateIdle` | 팀원이 현재 작업을 마치고 보류 중인 작업이 없을 때 | 알림 트리거, 후속 작업 할당 |
| `TaskCompleted` | 공유 작업 목록의 태스크가 완료로 표시될 때 | 유효성 검사 실행, 대시보드 업데이트, 종속 작업 체인 |

### 모범 사례

- **팀 규모**: 최적의 조정을 위해 팀을 3-5명의 팀원으로 유지
- **작업 규모**: 각 5-15분 소요되는 작업으로 분할 — 병렬화하기에 충분히 작고, 의미를 가지기에 충분히 큼
- **파일 충돌 방지**: 병합 충돌을 방지하기 위해 다른 파일 또는 디렉터리를 다른 팀원에게 할당
- **간단하게 시작**: 첫 팀에는 인-프로세스 모드를 사용하고, 익숙해지면 분할 창으로 전환
- **명확한 작업 설명**: 팀원이 독립적으로 작업할 수 있도록 구체적이고 실행 가능한 작업 설명을 제공

### 제한 사항

- **실험적**: 기능 동작이 향후 릴리스에서 변경될 수 있습니다
- **세션 재개 불가**: 인-프로세스 팀원은 세션 종료 후 재개할 수 없습니다
- **세션당 하나의 팀**: 단일 세션에서 중첩 팀 또는 여러 팀을 생성할 수 없습니다
- **고정된 리더십**: 팀 리더 역할은 팀원에게 이전될 수 없습니다
- **분할 창 제한**: tmux/iTerm2 필요; VS Code 터미널, Windows 터미널 또는 Ghostty에서는 사용할 수 없습니다
- **분할 창 권한**: 분할 창 팀원은 리더의 `--disallowedTools`와 `--tools`(v2.1.309+)를 이어받지만 `--allowedTools`는 이어받지 않습니다. 분할 창에서 작업을 미리 승인하려면 리더를 `claude --settings '{"permissions":{"allow":["Bash(npm *)"]}}'`로 시작하십시오. 인-프로세스 팀원은 리더의 실시간 규칙을 사용합니다
- **세션 간 팀 불가**: 팀원은 현재 세션 내에서만 존재합니다

> **경고**: 에이전트 팀은 실험적 기능입니다. 중요하지 않은 작업으로 먼저 테스트하고, 예기치 않은 동작이 있는지 팀원 조정을 모니터링하십시오.

---

## 플러그인 서브에이전트 보안

플러그인이 제공하는 서브에이전트는 보안을 위해 프런트매터 기능이 제한됩니다. 플러그인 서브에이전트 정의에서는 다음 필드가 **허용되지 않습니다**:

- `hooks` - 수명 주기 훅을 정의할 수 없습니다
- `mcpServers` - MCP 서버를 구성할 수 없습니다
- `permissionMode` - 권한 설정을 재정의할 수 없습니다

이는 플러그인이 서브에이전트 훅을 통해 권한을 에스컬레이션하거나 임의의 명령어를 실행하는 것을 방지합니다.

### 서브에이전트 출력 스캔 (v2.1.210+)

v2.1.210부터 Claude Code는 각 서브에이전트의 최종 보고서에서 하네스 자체의 출력 형식을 흉내 내는 텍스트를 스캔합니다. 가짜 `<system-reminder>` 스타일 태그, 조작된 `Human:`/`Assistant:` 턴, 권한 우회 플래그나 설정 파일 경로 언급 등이 대상입니다. 이는 서브에이전트 출력에 실려 오는 프롬프트 인젝션을 방어합니다. 예를 들어 부모 세션을 조작하도록 설계된 가짜 제어 토큰이 담긴 악성 웹 페이지를 서브에이전트가 가져온 경우입니다.

스캔에 무언가가 걸리면 Claude Code는 이를 무력화합니다. 백슬래시를 삽입하거나 스캔을 촉발한 항목을 명시하는 `[harness: subagent output matched instruction-shaped pattern(s): ...]` 같은 인라인 마커를 넣으며, 부모 세션은 표시된 텍스트를 따라야 할 지시가 아니라 전달할 발견 사항으로 취급해야 합니다. 스캔은 기본으로 켜져 있으며 문서화된 해제 방법은 없습니다. 스캔은 과하게 표시하는 쪽을 택합니다. 정상적인 서브에이전트 보고서라도 실제 플래그 이름(예: `--dangerously-skip-permissions`)을 그대로 인용하면 악의적인 일이 없었는데도 마커가 붙을 수 있습니다. 인젝션을 놓치는 것보다 오탐이 낫기 때문입니다.

### 서브에이전트 동시 실행 및 깊이 제한

> **세션당 생성 상한은 사라졌습니다.** Claude Code는 v2.1.212부터 세션당 서브에이전트 생성을 200개로 제한했지만, **v2.1.224에서 이 상한을 제거했습니다**. 오래 실행되는 세션도 더 이상 새 에이전트를 거부하지 않으며, 공식 서브에이전트 참조 문서도 Claude가 한 세션 동안 생성할 수 있는 서브에이전트 총수에는 제한이 없다고 분명히 밝힙니다. 이를 재정의하던 `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` 변수도 함께 사라졌습니다.

서브에이전트 확장(fan-out)에는 여전히 두 가지 제한이 적용되며, 둘 다 환경 변수로 설정합니다.

- `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (v2.1.217) - **동시에** 실행되는 서브에이전트의 최대 수. 기본값: 20.
- `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (v2.1.217) - 서브에이전트가 자체 서브에이전트를 생성할 때의 최대 **중첩 깊이**. **v2.1.219부터 기본값: 3**(v2.1.217–v2.1.218에서는 1). 중첩을 끄려면 `1`로 설정합니다([주요 동작](#주요-동작) 참고).

```bash
export CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=20
export CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=5
```

---

## 아키텍처

### 고수준 아키텍처

```mermaid
graph TB
    User["User"]
    Main["Main Agent<br/>(Coordinator)"]
    Reviewer["Code Reviewer<br/>Subagent"]
    Tester["Test Engineer<br/>Subagent"]
    Docs["Documentation<br/>Subagent"]

    User -->|asks| Main
    Main -->|delegates| Reviewer
    Main -->|delegates| Tester
    Main -->|delegates| Docs
    Reviewer -->|returns result| Main
    Tester -->|returns result| Main
    Docs -->|returns result| Main
    Main -->|synthesizes| User
```

### 서브에이전트 생명주기

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Separate<br/>Context Window

    User->>MainAgent: "Build new auth feature"
    MainAgent->>MainAgent: Analyze task
    MainAgent->>CodeReviewer: "Review this code"
    CodeReviewer->>Context: Initialize clean context
    Context->>CodeReviewer: Load reviewer instructions
    CodeReviewer->>CodeReviewer: Perform review
    CodeReviewer-->>MainAgent: Return findings
    MainAgent->>MainAgent: Incorporate results
    MainAgent-->>User: Provide synthesis
```

---

## 컨텍스트 관리

```mermaid
graph TB
    A["Main Agent Context<br/>50,000 tokens"]
    B["Subagent 1 Context<br/>20,000 tokens"]
    C["Subagent 2 Context<br/>20,000 tokens"]
    D["Subagent 3 Context<br/>20,000 tokens"]

    A -->|Clean slate| B
    A -->|Clean slate| C
    A -->|Clean slate| D

    B -->|Results only| A
    C -->|Results only| A
    D -->|Results only| A

    style A fill:#e1f5fe
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### 주요 사항

- 각 서브에이전트는 주 대화 기록 없이 **새로운 컨텍스트 창**을 얻습니다
- **관련 컨텍스트**만 특정 작업을 위해 서브에이전트에게 전달됩니다
- 결과는 주 에이전트로 **요약되어** 돌아옵니다
- 이는 긴 프로젝트에서 **컨텍스트 토큰 소진**을 방지합니다

### 성능 고려 사항

- **컨텍스트 효율성** - 에이전트가 주 컨텍스트를 보존하여 더 긴 세션을 가능하게 합니다
- **지연 시간** - 서브에이전트는 깨끗한 상태로 시작하며 초기 컨텍스트를 수집하는 데 지연 시간을 추가할 수 있습니다

### 주요 동작

- **중첩 생성 기본 활성화, 깊이 3 (v2.1.219)** - 서브에이전트는 주 대화 아래 세 단계까지 자체 서브에이전트를 생성할 수 있습니다. 제한을 바꾸려면 `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`를 설정하고, 중첩을 끄려면 `1`로 설정합니다. 깊이 제한에 도달하면 Claude Code는 포크를 제외한 모든 서브에이전트에서 `Agent` 도구를 숨깁니다. (이력: v2.1.172–v2.1.216은 변경할 방법 없이 기본적으로 최대 5단계까지 중첩, v2.1.217은 깊이 1의 옵트인 방식으로 변경, v2.1.219는 기본값을 3으로 설정.) 주 스레드 에이전트(`claude --agent`)가 생성할 수 있는 서브에이전트를 제어하려면 `Agent(agent_type)` 제한 구문([생성 가능한 서브에이전트 제한](#생성-가능한-서브에이전트-제한) 참고)을 사용하십시오. 서브에이전트 안에서는 유형 목록이 무시됩니다
- **백그라운드 권한** - 백그라운드 서브에이전트에 사전 승인되지 않은 권한이 필요하면, 요청하는 서브에이전트 이름과 함께 주 세션에 프롬프트가 나타납니다
- **백그라운드 전환** - `Ctrl+B`를 눌러 현재 실행 중인 작업을 백그라운드로 전환합니다
- **트랜스크립트** - 서브에이전트 트랜스크립트는 `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`에 저장됩니다
- **자동 압축** - 서브에이전트 컨텍스트는 용량의 ~95%에서 자동으로 압축됩니다(`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` 환경 변수로 재정의)
- **확장 사고 상속 (v2.1.198)** - 서브에이전트와 컨텍스트 압축이 이제 세션의 확장 사고 구성을 상속합니다(이전에는 항상 비활성화). 서브에이전트별 사고 필드는 없습니다

### 추가 제어

- **내장 Explore/Plan 에이전트 비활성화** - `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1`을 설정하면 내장 Explore 및 Plan 에이전트가 제거됩니다(v2.1.198)
- **모든 서브에이전트 프롬프트에 추가** - 비대화형 / `--print` 모드에서 `--append-subagent-system-prompt "<text>"`는 모든 서브에이전트의 시스템 프롬프트에 텍스트를 덧붙입니다(v2.1.205)
- **파일에서 추가** - `--append-subagent-system-prompt-file ./subagent-rules.txt`는 명령줄로 넘기기에 너무 긴 프롬프트를 위해 같은 추가 텍스트를 파일에서 읽습니다. 역시 `-p` 전용이며 `--append-subagent-system-prompt`와 함께 쓸 수 없습니다(v2.1.261)

---

## 서브에이전트 사용 시기

| Scenario | Use Subagent | Why |
|----------|--------------|-----|
| 여러 단계가 있는 복잡한 기능 | 예 | 관심사 분리, 컨텍스트 오염 방지 |
| 빠른 코드 검토 | 아니요 | 불필요한 오버헤드 |
| 병렬 작업 실행 | 예 | 각 서브에이전트는 자체 컨텍스트를 가집니다 |
| 전문화된 전문 지식 필요 | 예 | 맞춤형 시스템 프롬프트 |
| 장기 실행 분석 | 예 | 주 컨텍스트 소진 방지 |
| 단일 작업 | 아니요 | 불필요하게 지연 시간 추가 |

---

## 모범 사례

### 설계 원칙

**권장 사항:**
- Claude가 생성한 에이전트로 시작 - Claude로 초기 서브에이전트를 생성한 다음 반복하여 사용자 정의
- 집중된 서브에이전트 설계 - 모든 것을 하는 대신 단일하고 명확한 책임
- 자세한 프롬프트 작성 - 특정 지침, 예시 및 제약 조건 포함
- 도구 접근 제한 - 서브에이전트의 목적에 필요한 도구만 부여
- 버전 관리 - 팀 협업을 위해 프로젝트 서브에이전트를 버전 제어에 체크인

**피해야 할 사항:**
- 역할이 중복되는 서브에이전트 생성
- 서브에이전트에 불필요한 도구 접근 권한 부여
- 간단한 단일 단계 작업에 서브에이전트 사용
- 하나의 서브에이전트 프롬프트에 여러 관심사 혼합
- 필요한 컨텍스트 전달을 잊지 마세요

### 시스템 프롬프트 모범 사례

1. **역할에 대해 구체적으로 설명**
   ```
   You are an expert code reviewer specializing in [specific areas]
   ```

2. **우선순위를 명확하게 정의**
   ```
   Review priorities (in order):
   1. Security Issues
   2. Performance Problems
   3. Code Quality
   ```

3. **출력 형식 지정**
   ```
   For each issue provide: Severity, Category, Location, Description, Fix, Impact
   ```

4. **실행 단계 포함**
   ```
   When invoked:
   1. Run git diff to see recent changes
   2. Focus on modified files
   3. Begin review immediately
   ```

### 도구 접근 전략

1. **제한적으로 시작**: 필수 도구만으로 시작
2. **필요할 때만 확장**: 요구 사항에 따라 도구 추가
3. **가능할 때 읽기 전용**: 분석 에이전트에는 Read/Grep 사용
4. **샌드박스 실행**: Bash 명령을 특정 패턴으로 제한

---

## 이 폴더의 서브에이전트 예시

이 폴더에는 바로 사용할 수 있는 서브에이전트 예시가 포함되어 있습니다.

### 1. 코드 리뷰어 (`code-reviewer.md`)

**목적**: 포괄적인 코드 품질 및 유지 보수성 분석

**도구**: Read, Grep, Glob, Bash

**전문 분야**:
- 보안 취약점 감지
- 성능 최적화 식별
- 코드 유지 보수성 평가
- 테스트 커버리지 분석

**사용 시기**: 품질 및 보안에 중점을 둔 자동화된 코드 검토가 필요할 때

---

### 2. 테스트 엔지니어 (`test-engineer.md`)

**목적**: 테스트 전략, 커버리지 분석 및 자동화된 테스트

**도구**: Read, Write, Bash, Grep

**전문 분야**:
- 단위 테스트 생성
- 통합 테스트 설계
- 에지 케이스 식별
- 커버리지 분석 (80% 이상 목표)

**사용 시기**: 포괄적인 테스트 스위트 생성 또는 커버리지 분석이 필요할 때

---

### 3. 문서 작성기 (`documentation-writer.md`)

**목적**: 기술 문서, API 문서 및 사용자 가이드

**도구**: Read, Write, Grep

**전문 분야**:
- API 엔드포인트 문서화
- 사용자 가이드 생성
- 아키텍처 문서화
- 코드 주석 개선

**사용 시기**: 프로젝트 문서를 생성하거나 업데이트해야 할 때

---

### 4. 보안 리뷰어 (`secure-reviewer.md`)

**목적**: 최소한의 권한으로 보안에 중점을 둔 코드 검토

**도구**: Read, Grep

**전문 분야**:
- 보안 취약점 감지
- 인증/권한 부여 문제
- 데이터 노출 위험
- 인젝션 공격 식별

**사용 시기**: 수정 기능 없이 보안 감사만 필요한 경우

---

### 5. 구현 에이전트 (`implementation-agent.md`)

**목적**: 기능 개발을 위한 완전한 구현 기능

**도구**: Read, Write, Edit, Bash, Grep, Glob

**전문 분야**:
- 기능 구현
- 코드 생성
- 빌드 및 테스트 실행
- 코드베이스 수정

**사용 시기**: 기능 구현을 처음부터 끝까지 수행할 서브에이전트가 필요할 때

---

### 6. 디버거 (`debugger.md`)

**목적**: 오류, 테스트 실패 및 예기치 않은 동작을 위한 디버깅 전문가

**도구**: Read, Edit, Bash, Grep, Glob

**전문 분야**:
- 근본 원인 분석
- 오류 조사
- 테스트 실패 해결
- 최소한의 수정 구현

**사용 시기**: 버그, 오류 또는 예기치 않은 동작이 발생할 때

---

### 7. 데이터 과학자 (`data-scientist.md`)

**목적**: SQL 쿼리 및 데이터 통찰력을 위한 데이터 분석 전문가

**도구**: Bash, Read, Write

**전문 분야**:
- SQL 쿼리 최적화
- BigQuery 작업
- 데이터 분석 및 시각화
- 통계적 통찰력

**사용 시기**: 데이터 분석, SQL 쿼리 또는 BigQuery 작업이 필요할 때

---

### 8. 클린 코드 리뷰어 (`clean-code-reviewer.md`)

**목적**: 클린 코드 원칙에 따른 가독성 및 유지 보수성 리뷰

**도구**: Read, Grep, Glob, Bash

**전문 분야**:
- 명명, 함수 길이, 인자 개수
- 중복 및 죽은 코드
- 주석 품질과 의도
- 영리함보다 구조적 명확성

**사용 시기**: 정확성 리뷰와 구분되는 스타일 및 유지 보수성 점검이 필요할 때

---

### 9. 성능 최적화기 (`performance-optimizer.md`)

**목적**: 성능 병목 지점을 식별하고 해결

**도구**: Read, Edit, Bash, Grep, Glob

**전문 분야**:
- 알고리즘 복잡도와 핫 패스
- 메모리 할당과 누수
- 캐싱 및 쿼리 최적화
- 동시성 및 I/O 병목

**사용 시기**: 코드가 측정 가능할 만큼 느려서 표적 최적화가 필요할 때

---

## 설치 안내

### 방법 1: Claude에게 요청 (권장)

원하는 서브에이전트를 설명하고 Claude가 파일을 만들게 합니다.

```text
Create a project-level subagent that runs tests and fixes failures.
Give it access to Bash, Read, Edit, and Grep.
```

Claude가 적절한 프런트매터와 함께 `.claude/agents/<name>.md`를 작성합니다. 생성된 파일을 검토한 뒤 사용하십시오. (`/agents` 대화형 생성 마법사는 v2.1.198에서 제거되었으므로, 대신 Claude에게 요청하거나 파일을 직접 편집하십시오.)

### 방법 2: 프로젝트로 복사

에이전트 파일을 프로젝트의 `.claude/agents/` 디렉터리로 복사합니다.

```bash
# 프로젝트로 이동
cd /path/to/your/project

# agents 디렉터리가 없으면 생성
mkdir -p .claude/agents

# 이 폴더의 모든 에이전트 파일 복사
cp /path/to/04-subagents/*.md .claude/agents/

# README 제거 (.claude/agents에는 필요 없음)
rm .claude/agents/README.md
```

### 방법 3: 사용자 디렉터리로 복사

모든 프로젝트에서 사용할 수 있는 에이전트의 경우.

```bash
# 사용자 agents 디렉터리 생성
mkdir -p ~/.claude/agents

# 에이전트 복사
cp /path/to/04-subagents/code-reviewer.md ~/.claude/agents/
cp /path/to/04-subagents/debugger.md ~/.claude/agents/
# ... 필요에 따라 나머지 복사
```

### 확인

설치 후 디렉터리 목록을 확인하여 에이전트가 인식되는지 확인합니다.

```bash
ls .claude/agents/
```

현재 세션에서 어떤 서브에이전트를 사용할 수 있는지 Claude에게 물어볼 수도 있으며, Claude는 위임할 수 있는 내장 에이전트와 사용자 지정 에이전트를 알려 줍니다.

---

## 파일 구조

```
project/
├── .claude/
│   └── agents/
│       ├── code-reviewer.md
│       ├── test-engineer.md
│       ├── documentation-writer.md
│       ├── secure-reviewer.md
│       ├── implementation-agent.md
│       ├── debugger.md
│       ├── data-scientist.md
│       ├── clean-code-reviewer.md
│       └── performance-optimizer.md
└── ...
```

---

## 관련 개념

### 관련 기능

- **[슬래시 명령어](../01-slash-commands/)** - 사용자가 빠르게 호출하는 단축키
- **[메모리](../02-memory/)** - 영구적인 세션 간 컨텍스트
- **[스킬](../03-skills/)** - 재사용 가능한 자율 기능
- **[MCP 프로토콜](../05-mcp/)** - 실시간 외부 데이터 접근
- **[훅](../06-hooks/)** - 이벤트 기반 셸 명령 자동화
- **[플러그인](../07-plugins/)** - 번들 확장 패키지

### 다른 기능과의 비교

| Feature | User-Invoked | Auto-Invoked | Persistent | External Access | Isolated Context |
|---------|--------------|--------------|-----------|------------------|------------------|
| **슬래시 명령어** | 예 | 아니요 | 아니요 | 아니요 | 아니요 |
| **서브에이전트** | 예 | 예 | 아니요 | 아니요 | 예 |
| **메모리** | 자동 | 자동 | 예 | 아니요 | 아니요 |
| **MCP** | 자동 | 예 | 아니요 | 예 | 아니요 |
| **스킬** | 예 | 예 | 아니요 | 아니요 | 아니요 |

### 통합 패턴

```mermaid
graph TD
    User["User Request"] --> Main["Main Agent"]
    Main -->|Uses| Memory["Memory<br/>(Context)"]
    Main -->|Queries| MCP["MCP<br/>(Live Data)"]
    Main -->|Invokes| Skills["Skills<br/>(Auto Tools)"]
    Main -->|Delegates| Subagents["Subagents<br/>(Specialists)"]

    Subagents -->|Use| Memory
    Subagents -->|Query| MCP
    Subagents -->|Isolated| Context["Clean Context<br/>Window"]
```

---

## 관측 가능성

> **v2.1.139에 추가됨.**

서브에이전트에서 시작된 API 요청에는 추적 및 로그를 디스패치 세션과 상호 연관시킬 수 있도록 두 개의 추가 HTTP 헤더가 포함됩니다.

| Header | Description |
|--------|-------------|
| `x-claude-code-agent-id` | 요청을 하는 서브에이전트의 UUID입니다. |
| `x-claude-code-parent-agent-id` | 이 서브에이전트를 디스패치한 에이전트 (주 에이전트 또는 체인의 상위 서브에이전트)의 UUID입니다. |

동일한 식별자는 `claude_code.llm_request` OpenTelemetry 스팬에 `claude.code.agent.id` 및 `claude.code.agent.parent_id` 속성으로 노출됩니다. 이를 사용하여 다음을 수행할 수 있습니다.

- API 사용량을 부모 세션 대신 특정 서브에이전트 유형에 할당
- 사후 에이전트 호출 체인 재구성 (parent_id는 트리를 형성)
- 폭주하는 서브에이전트에 대한 경고 (예: 하나의 `agent.id`가 세션 사용량의 50% 이상을 차지)

종단 간 익스포터 설정에 대해서는 [고급 기능 → 텔레메트리](../09-advanced-features/README.md)의 OpenTelemetry 섹션을 참조하십시오.

## 추가 자료

- [공식 서브에이전트 문서](https://code.claude.com/docs/en/sub-agents)
- [CLI 참조](https://code.claude.com/docs/en/cli-reference) - `--agents` 플래그 및 기타 CLI 옵션
- [플러그인 가이드](../07-plugins/) - 다른 기능과 에이전트를 번들링하는 방법
- [스킬 가이드](../03-skills/) - 자동 호출 기능
- [메모리 가이드](../02-memory/) - 영구 컨텍스트
- [훅 가이드](../06-hooks/) - 이벤트 기반 자동화

---

**최종 업데이트**: 2026년 10월 26일
**Claude Code 버전**: 2.1.310
**출처**:
- https://code.claude.com/docs/en/sub-agents
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/changelog#2-1-172
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/releases/tag/v2.1.140
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/interactive-mode
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/agent-view
- https://code.claude.com/docs/en/sub-agents#permission-modes
- https://code.claude.com/docs/en/sub-agents#available-tools
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/sub-agents#turn-fork-mode-on-or-off
- https://code.claude.com/docs/en/sub-agents#which-subagents-run-in-the-background
- https://code.claude.com/docs/en/agent-teams#have-teammates-plan-before-implementing
- https://code.claude.com/docs/en/sub-agents#let-claude-wait-for-a-subagent
- https://code.claude.com/docs/en/sub-agents#mcp-server-names-that-contain-a-double-underscore
- https://code.claude.com/docs/en/agent-teams#permissions
- https://code.claude.com/docs/en/changelog#2-1-309
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/vs-code#see-a-background-subagents-tool-calls
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
