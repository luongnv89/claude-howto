<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.160-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# 주말 동안 Claude Code 마스터하기

`claude` 명령어를 입력하는 것부터 에이전트, 훅, 스킬 및 MCP 서버를 구성하는 방법까지 시각적 튜토리얼, 직접 복사하여 붙여넣을 수 있는 템플릿 및 단계별 학습 경로를 통해 알아보세요.

**[15분 안에 시작하기](#15분-안에-시작하기)** | **[내 레벨 찾기](#어디서-시작해야-할지-모르겠나요)** | **[기능 카탈로그 보기](CATALOG.md)**

---

## 목차

- [문제점](#문제점)
- [Claude How To가 해결하는 방법](#claude-how-to가-해결하는-방법)
- [작동 방식](#작동-방식)
- [어디서 시작해야 할지 모르겠나요?](#어디서-시작해야-할지-모르겠나요)
- [15분 안에 시작하기](#15분-안에-시작하기)
- [무엇을 만들 수 있을까요?](#무엇을-만들-수-있을까요)
- [자주 묻는 질문](#faq)
- [기여하기](#기여하기)
- [라이선스](#라이선스)

---

## 문제점

Claude Code를 설치했습니다. 몇 개의 프롬프트도 실행해 보았습니다. 이제 무엇을 해야 할까요?

- **공식 문서는 기능을 설명하지만, 기능들을 어떻게 조합해야 하는지는 알려주지 않습니다.** 슬래시 명령어가 있다는 것은 알지만, 이를 훅, 메모리, 서브에이전트와 연결하여 실제로 시간을 절약해 주는 워크플로를 만드는 방법은 알기 어렵습니다.
- **명확한 학습 경로가 없습니다.** MCP를 먼저 배워야 할까요? 훅을 먼저 배워야 할까요? 스킬을 먼저 배워야 할까요, 서브에이전트를 먼저 배워야 할까요? 결국 모든 내용을 훑어보기만 하고 어느 것도 제대로 익히지 못하게 됩니다.
- **예제가 너무 기초적입니다.** "Hello World" 수준의 슬래시 명령어 예제는 메모리를 활용하고, 전문 에이전트에게 작업을 위임하며, 보안 스캔을 자동으로 실행하는 실전 코드 리뷰 파이프라인을 구축하는 데 도움이 되지 않습니다.

Claude Code의 강력한 기능 중 90%를 활용하지 못하고 있으며, 무엇을 모르는지조차 알지 못하는 상태입니다.

---

## Claude How To가 해결하는 방법

이것은 단순한 기능 레퍼런스가 아닙니다. 오늘 바로 프로젝트에 적용할 수 있는 실전 템플릿을 통해 Claude Code의 모든 기능을 배울 수 있도록 설계된 **구조화된 시각 중심의 실습 가이드**입니다.

| | Official Docs | This Guide |
|--|---------------|------------|
| **Format** | 기능 참조 문서 | Mermaid 다이어그램 기반 시각적 튜토리얼 |
| **Depth** | 기능 설명 | 내부 동작 원리까지 설명 |
| **Examples** | 기본 예제 | 즉시 활용 가능한 실전 템플릿 |
| **Structure** | 기능 중심 구성 | 초급 → 고급 단계별 학습 경로 |
| **Onboarding** | 자율 학습 | 예상 소요 시간이 포함된 가이드형 로드맵 |
| **Self-Assessment** | 없음 | 학습 공백을 찾고 맞춤형 경로를 제안하는 퀴즈 제공 |

### 제공되는 내용

- 슬래시 명령어부터 사용자 정의 에이전트 팀까지 Claude Code의 모든 기능을 다루는 **10개의 튜토리얼 모듈**
- 슬래시 명령어, CLAUDE.md 템플릿, 훅 스크립트, MCP 설정, 서브에이전트 정의, 플러그인 번들을 포함한 **즉시 사용 가능한 복사·붙여넣기 템플릿**
- 각 기능의 내부 동작 원리를 보여주는 **Mermaid 다이어그램**
- 초보자에서 고급 사용자까지 성장할 수 있는 **11~13시간 분량의 단계별 학습 경로**
- `/self-assessment` 또는 `/lesson-quiz hooks`를 통해 학습 공백을 파악할 수 있는 **내장 자기 평가 기능**

**[학습 로드맵 시작하기 ->](LEARNING-ROADMAP.md)**

---

## 작동 방식

### 1. 내 수준 찾기

[자기 평가 퀴즈](LEARNING-ROADMAP.md#-find-your-level)를 진행하거나 Claude Code에서 `/self-assessment`를 실행하세요. 현재 수준에 맞는 개인화된 학습 로드맵을 제공합니다.

### 2. 가이드 학습 경로 따라가기

10개의 모듈을 순서대로 학습하세요. 각 모듈은 이전 내용을 기반으로 구성되어 있으며, 학습하면서 템플릿을 프로젝트에 바로 적용할 수 있습니다.

### 3. 기능을 조합하여 워크플로 만들기

Claude Code의 진정한 강점은 기능 조합에 있습니다. 슬래시 명령어, 메모리, 서브에이전트, 훅을 연결하여 코드 리뷰, 배포, 문서 생성 등을 자동화하는 파이프라인을 구축하는 방법을 배웁니다.

### 4. 이해도 확인하기

각 모듈을 학습한 후 `/lesson-quiz [topic]`을 실행하세요. 놓친 내용을 정확히 찾아내어 빠르게 보완할 수 있습니다.

**[15분 안에 시작하기](#15분-안에-시작하기)**

---

## 개발자들이 신뢰하는 가이드

- Claude Code를 매일 사용하는 개발자들의 **GitHub Star**
- 팀 워크플로에 맞게 가이드를 확장하기 위한 **Fork**
- **지속적인 유지보수** — Claude Code의 모든 릴리스에 맞춰 업데이트 (최신 버전: v2.1.160, 2026년 6월)
- **커뮤니티 중심 운영** — 실전 설정을 공유하는 개발자들의 기여

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 어디서 시작해야 할지 모르겠나요?

자기 평가를 진행하거나 자신의 수준에 맞는 경로를 선택하세요.

| Level | You can... | Start here | Time |
|-------|-----------|------------|------|
| **Beginner** | Claude Code를 실행하고 대화할 수 있음 | [Slash Commands](01-slash-commands/) | 약 2.5시간 |
| **Intermediate** | CLAUDE.md 및 사용자 정의 명령어 사용 가능 | [Skills](03-skills/) | 약 3.5시간 |
| **Advanced** | MCP 서버 및 훅 구성 가능 | [Advanced Features](09-advanced-features/) | 약 5시간 |

**10개 모듈 전체 학습 경로**

| Order | Module | Level | Time |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/) | Beginner | 30분 |
| 2 | [Memory](02-memory/) | Beginner+ | 45분 |
| 3 | [Checkpoints](08-checkpoints/) | Intermediate | 45분 |
| 4 | [CLI Basics](10-cli/) | Beginner+ | 30분 |
| 5 | [Skills](03-skills/) | Intermediate | 1시간 |
| 6 | [Hooks](06-hooks/) | Intermediate | 1시간 |
| 7 | [MCP](05-mcp/) | Intermediate+ | 1시간 |
| 8 | [Subagents](04-subagents/) | Intermediate+ | 1.5시간 |
| 9 | [Advanced Features](09-advanced-features/) | Advanced | 2~3시간 |
| 10 | [Plugins](07-plugins/) | Advanced | 2시간 |

**[전체 학습 로드맵 ->](LEARNING-ROADMAP.md)**

---

## 15분 안에 시작하기

> **설치 참고 사항**: v2.1.113부터 Claude Code는 macOS, Linux, Windows용 네이티브 바이너리로 제공됩니다. `npm install -g @anthropic-ai/claude-code` 명령도 계속 사용할 수 있으며, 첫 실행 시 네이티브 바이너리가 선택적 의존성으로 다운로드됩니다. v2.1.116부터는 다운로드가 `https://downloads.claude.ai/claude-code-releases`에서 제공되므로, 기업 환경의 프록시에서는 해당 호스트를 허용 목록에 추가해야 합니다.

```bash
# 1. Clone the guide
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Try it — in Claude Code, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. Install a skill:
cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

전체 설정을 원하시나요? 다음은 **1시간 핵심 설정 가이드**입니다.

```bash
# Slash commands (15 min)
cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 min)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Install a skill (15 min)
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Weekend goal: add hooks, subagents, MCP, and plugins
# Follow the learning path for guided setup
```

**[전체 설치 가이드 보기](#15분-안에-시작하기)**

---

## 무엇을 만들 수 있을까요?

| Use Case | Features You'll Combine |
|----------|------------------------|
| **자동화된 코드 리뷰** | Slash Commands + Subagents + Memory + MCP |
| **팀 온보딩 시스템** | Memory + Slash Commands + Plugins |
| **CI/CD 자동화** | CLI Reference + Hooks + Background Tasks |
| **문서 자동 생성** | Skills + Subagents + Plugins |
| **보안 감사** | Subagents + Skills + Hooks (읽기 전용 모드) |
| **DevOps 파이프라인** | Plugins + MCP + Hooks + Background Tasks |
| **대규모 리팩터링** | Checkpoints + Planning Mode + Hooks |

---

## FAQ

**무료인가요?**
네. MIT 라이선스로 제공되며 영구적으로 무료입니다. 라이선스 고지만 유지하면 개인 프로젝트, 회사 업무, 팀 프로젝트 등 어디에서나 사용할 수 있습니다.

**계속 유지보수되나요?**
네. Claude Code의 모든 릴리스에 맞춰 지속적으로 업데이트됩니다. 현재 버전은 v2.1.160(2026년 6월)이며 Claude Code 2.1+와 호환됩니다.

**공식 문서와 어떤 차이가 있나요?**
공식 문서는 기능 참조용 문서입니다. 이 가이드는 다이어그램, 실전 템플릿, 단계별 학습 경로를 제공하는 튜토리얼입니다. 두 자료는 상호 보완적입니다. 학습은 이 가이드로 시작하고, 세부 사항이 필요할 때 공식 문서를 참고하세요.

**전체 학습에는 얼마나 걸리나요?**
전체 경로를 완료하는 데 약 11~13시간이 소요됩니다. 하지만 슬래시 명령어 템플릿 하나를 복사해 실행하는 것만으로도 15분 안에 즉각적인 효과를 얻을 수 있습니다.

**Claude Sonnet / Haiku / Opus에서도 사용할 수 있나요?**
네. 모든 템플릿은 Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5에서 사용할 수 있습니다.

**기여할 수 있나요?**
물론입니다. 자세한 내용은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 새로운 예제, 버그 수정, 문서 개선, 커뮤니티 템플릿 기여를 환영합니다.

**오프라인에서도 읽을 수 있나요?**
네. 모든 콘텐츠와 렌더링된 다이어그램이 포함된 EPUB 전자책을 생성하려면 다음 명령을 실행하세요.

---

## 지금 바로 Claude Code 마스터하기

이미 Claude Code는 설치되어 있습니다. 이제 생산성을 10배 향상시키는 데 필요한 것은 Claude Code를 제대로 활용하는 방법을 익히는 것뿐입니다. 이 가이드는 그 목표에 도달할 수 있도록 체계적인 학습 경로, 시각적 설명, 그리고 바로 사용할 수 있는 템플릿을 제공합니다.

MIT 라이선스로 제공됩니다. 영구적으로 무료입니다. 자유롭게 Clone하고, Fork하고, 원하는 방식으로 활용하세요.

**[학습 로드맵 시작하기 ->](LEARNING-ROADMAP.md)** | **[기능 카탈로그 보기](CATALOG.md)** | **[15분 안에 시작하기](#15분-안에-시작하기)**

---

<details>
<summary>빠른 탐색 — 전체 기능 목록</summary>

| 기능 | 설명 | 폴더 |
|---------|-------------|--------|
| **기능 카탈로그** | 설치 명령어를 포함한 전체 참조 문서 | [CATALOG.md](CATALOG.md) |
| **슬래시 명령어** | 사용자가 직접 실행하는 단축 명령어 | [01-slash-commands/](01-slash-commands/) |
| **메모리** | 지속적으로 유지되는 컨텍스트 | [02-memory/](02-memory/) |
| **스킬** | 재사용 가능한 기능 모음 | [03-skills/](03-skills/) |
| **서브에이전트** | 특정 역할에 특화된 AI 도우미 | [04-subagents/](04-subagents/) |
| **MCP 프로토콜** | 외부 도구 접근 기능 | [05-mcp/](05-mcp/) |
| **훅** | 이벤트 기반 자동화 | [06-hooks/](06-hooks/) |
| **플러그인** | 기능 패키지 번들 | [07-plugins/](07-plugins/) |
| **체크포인트** | 세션 스냅샷 및 되돌리기 | [08-checkpoints/](08-checkpoints/) |
| **고급 기능** | 계획 모드, 심층 사고, 백그라운드 작업 | [09-advanced-features/](09-advanced-features/) |
| **CLI 참조** | 명령어, 플래그 및 옵션 | [10-cli/](10-cli/) |
| **블로그 게시물** | 실전 활용 사례 | [Blog Posts](https://medium.com/@luongnv89) |


</details>

<details>
<summary>기능 비교</summary>

| 기능 | 실행 방식 | 지속성 | 적합한 용도 |
|---------|-----------|------------|----------|
| **슬래시 명령어** | 수동 실행 (`/cmd`) | 현재 세션만 | 빠른 단축 작업 |
| **메모리** | 자동 로드 | 세션 간 유지 | 장기 학습 및 컨텍스트 |
| **스킬** | 자동 호출 | 파일 시스템 기반 | 자동화된 워크플로 |
| **서브에이전트** | 자동 위임 | 격리된 컨텍스트 | 작업 분산 |
| **MCP 프로토콜** | 자동 조회 | 실시간 | 라이브 데이터 접근 |
| **훅** | 이벤트 발생 시 실행 | 설정 기반 | 자동화 및 검증 |
| **플러그인** | 단일 명령어 | 전체 기능 포함 | 완성형 솔루션 |
| **체크포인트** | 수동/자동 | 세션 기반 | 안전한 실험 |
| **계획 모드** | 수동/자동 | 계획 단계 유지 | 복잡한 구현 작업 |
| **백그라운드 작업** | 수동 실행 | 작업 수행 기간 | 장시간 실행 작업 |
| **CLI 참조** | 터미널 명령어 | 세션/스크립트 | 자동화 및 스크립팅 |

</details>

<details>
<summary>설치 빠른 참조</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (auto-enabled, configure in settings)
# See 08-checkpoints/README.md

# Advanced Features (configure in settings)
# See 09-advanced-features/config-examples.json

# CLI Reference (no installation needed)
# See 10-cli/README.md for usage examples
```

</details>

<details>
<summary>01. 슬래시 명령어</summary>

**위치**: [01-slash-commands/](01-slash-commands/)

**설명**: Markdown 파일로 저장되는 사용자 실행형 단축 명령어

**예시**:
- `optimize.md` - 코드 최적화 분석
- `pr.md` - Pull Request 준비
- `generate-api-docs.md` - API 문서 생성기

**설치**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**사용 방법**:
```
/optimize
/pr
/generate-api-docs
```

**자세히 보기**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. 메모리</summary>

**위치**: [02-memory/](02-memory/)

**설명**: 세션 간에도 유지되는 지속형 컨텍스트

**예시**:
- `project-CLAUDE.md` - 팀 공통 프로젝트 규칙
- `directory-api-CLAUDE.md` - 디렉터리별 규칙
- `personal-CLAUDE.md` - 개인 설정 및 선호도

**설치**:
```bash
# Project memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# Directory memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**사용 방법**: Claude가 자동으로 로드합니다.

</details>

<details>
<summary>03. 스킬</summary>

**위치**: [03-skills/](03-skills/)

**설명**: 지침과 스크립트를 포함하는 재사용 가능한 자동 실행 기능

**예시**:
- `code-review-specialist/` - 스크립트를 포함한 종합 코드 리뷰
- `brand-voice/` - 브랜드 톤앤매너 일관성 검사기
- `doc-generator/` - API 문서 생성기

**설치**:
```bash
# Personal skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review-specialist /path/to/project/.claude/skills/
```

**사용 방법**: 관련 작업 시 자동으로 호출됩니다.

</details>

<details>
<summary>04. 서브에이전트</summary>

**위치**: [04-subagents/](04-subagents/)

**설명**: 독립된 컨텍스트와 사용자 정의 프롬프트를 가진 전문화된 AI 도우미

**예시**:
- `code-reviewer.md` - 종합 코드 품질 분석
- `test-engineer.md` - 테스트 전략 및 커버리지 분석
- `documentation-writer.md` - 기술 문서 작성
- `secure-reviewer.md` - 보안 중심 리뷰 (읽기 전용)
- `implementation-agent.md` - 전체 기능 구현 담당

**설치**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**사용 방법**: 메인 에이전트가 필요에 따라 자동으로 작업을 위임합니다.

</details>

<details>
<summary>05. MCP 프로토콜</summary>

**위치**: [05-mcp/](05-mcp/)

**설명**: 외부 도구와 API에 접근하기 위한 Model Context Protocol

**예시**:
- `github-mcp.json` - GitHub 연동
- `database-mcp.json` - 데이터베이스 조회
- `filesystem-mcp.json` - 파일 작업
- `multi-mcp.json` - 다중 MCP 서버 구성

**설치**:

```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Add MCP server via CLI
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Or add to project .mcp.json manually (see 05-mcp/ for examples)
```

**사용 방법**: MCP 서버 설정이 완료되면 Claude가 해당 도구를 자동으로 사용할 수 있습니다.

</details>

<details>
<summary>06. 훅(Hooks)</summary>

**위치**: [06-hooks/](06-hooks/)

**설명**: Claude Code 이벤트에 반응하여 자동 실행되는 이벤트 기반 셸 명령어

**예시**:
- `format-code.sh` - 코드 작성 전 자동 포맷팅
- `pre-commit.sh` - 커밋 전 테스트 실행
- `security-scan.sh` - 보안 취약점 검사
- `log-bash.sh` - 모든 Bash 명령 기록
- `validate-prompt.sh` - 사용자 프롬프트 검증
- `notify-team.sh` - 이벤트 발생 시 알림 전송

**설치**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

`~/.claude/settings.json`에서 훅을 설정합니다.
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**사용 방법**: 이벤트가 발생하면 훅이 자동으로 실행됩니다.

**훅 종류** (5개 유형, 총 29개 이벤트)

- **도구 훅(Tool Hooks)**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **세션 훅(Session Hooks)**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **작업 훅(Task Hooks)**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **라이프사이클 훅(Lifecycle Hooks)**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. 플러그인</summary>

**위치**: [07-plugins/](07-plugins/)

**설명**: 명령어, 에이전트, MCP, 훅을 하나로 묶은 기능 패키지

**예시**:
- `pr-review/` - 완전한 PR 리뷰 워크플로
- `devops-automation/` - 배포 및 모니터링 자동화
- `documentation/` - 문서 생성 자동화

**설치**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**사용 방법**: 플러그인에 포함된 슬래시 명령어와 기능을 사용합니다.

</details>

<details>
<summary>08. 체크포인트와 되돌리기(Rewind)</summary>

**위치**: [08-checkpoints/](08-checkpoints/)

**설명**: 대화 상태를 저장하고 이전 시점으로 되돌아가 다른 접근 방식을 시도할 수 있는 기능

**핵심 개념**:

- **Checkpoint**: 대화 상태 스냅샷
- **Rewind**: 이전 체크포인트로 복원
- **Branch Point**: 동일한 체크포인트에서 여러 접근 방식 탐색

**사용 방법**:
```
# Checkpoints are created automatically with every user prompt
# To rewind, press Esc twice or use:
/rewind

# Then choose from five options:
# 1. Restore code and conversation
# 2. Restore conversation
# 3. Restore code
# 4. Summarize from here
# 5. Never mind
```

**활용 사례**:
- 여러 구현 방식을 시도할 때
- 실수를 복구할 때
- 안전하게 실험할 때
- 대안 솔루션을 비교할 때
- 다양한 설계를 A/B 테스트할 때

</details>

<details>
<summary>09. 고급 기능</summary>

**위치**: [09-advanced-features/](09-advanced-features/)

**설명**: 복잡한 워크플로와 자동화를 위한 고급 기능 모음

**포함 기능**:

- **Planning Mode** — 코딩 전에 상세한 구현 계획 수립
- **Extended Thinking** — 복잡한 문제 해결을 위한 심층 추론 (`Alt+T` / `Option+T`로 전환)
- **Background Tasks** — 작업을 차단하지 않고 장시간 작업 실행
- **Permission Modes** — `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** — CI/CD 환경에서 Claude Code 실행: `claude -p "Run tests and generate report"`
- **Session Management** — `/resume`, `/rename`, `/fork`, `claude -c`, `claude -r`
- **Configuration** — `~/.claude/settings.json`을 통한 동작 사용자 정의

전체 설정 예시는 [config-examples.json](09-advanced-features/config-examples.json)을 참고하세요.

</details>

<details>
<summary>10. CLI 참조</summary>

**위치**: [10-cli/](10-cli/)

**설명**: Claude Code 명령줄 인터페이스 전체 참조 문서

**빠른 예시**:

```bash
# Interactive mode
claude "explain this project"

# Print mode (non-interactive)
claude -p "review this code"

# Process file content
cat error.log | claude -p "explain this error"

# JSON output for scripts
claude -p --output-format json "list functions"

# Resume session
claude -r "feature-auth" "continue implementation"
```

**활용 사례**: CI/CD 파이프라인 연동, 스크립트 자동화, 배치 처리, 다중 세션 워크플로, 사용자 정의 에이전트 구성

</details>

<details>
<summary>예제 워크플로</summary>

### 전체 코드 리뷰 워크플로

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### 자동 문서 생성

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Claude:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### DevOps 배포

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Claude:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

</details>

<details>
<summary>디렉터리 구조</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>모범 사례</summary>

### 권장 사항
- 슬래시 명령어부터 간단하게 시작하세요.
- 기능은 점진적으로 추가하세요.
- 팀 표준은 메모리를 활용해 관리하세요.
- 설정은 먼저 로컬 환경에서 테스트하세요.
- 사용자 정의 구현은 문서화하세요.
- 프로젝트 설정 파일은 버전 관리에 포함하세요.
- 플러그인을 팀과 공유하세요.

### 피해야 할 사항
- 중복 기능을 만들지 마세요.
- 자격 증명을 코드에 하드코딩하지 마세요.
- 문서 작성을 생략하지 마세요.
- 단순한 작업을 지나치게 복잡하게 만들지 마세요.
- 보안 모범 사례를 무시하지 마세요.
- 민감한 데이터를 저장소에 커밋하지 마세요.

</details>

<details>
<summary>문제 해결</summary>

### 기능이 로드되지 않는 경우
1. 파일 위치와 이름을 확인합니다.
2. YAML Frontmatter 문법을 검증합니다.
3. 파일 권한을 확인합니다.
4. Claude Code 버전 호환성을 확인합니다.

### MCP 연결 실패
1. 환경 변수를 확인합니다.
2. MCP 서버 설치 상태를 점검합니다.
3. 인증 정보를 테스트합니다.
4. 네트워크 연결 상태를 확인합니다.

### 서브에이전트가 작업을 위임받지 못하는 경우
1. 도구 권한을 확인합니다.
2. 에이전트 설명이 명확한지 검토합니다.
3. 작업 복잡도를 검토합니다.
4. 에이전트를 독립적으로 테스트합니다.

</details>

<details>
<summary>테스트</summary>

이 프로젝트는 포괄적인 자동화 테스트를 제공합니다.

- **단위 테스트**: pytest 기반 Python 테스트 (Python 3.10, 3.11, 3.12)
- **코드 품질**: Ruff를 이용한 린트 및 포맷 검사
- **보안**: Bandit 기반 취약점 스캔
- **타입 검사**: mypy를 활용한 정적 타입 분석
- **빌드 검증**: EPUB 생성 테스트
- **커버리지 추적**: Codecov 연동

```bash
# Install development dependencies
uv pip install -r requirements-dev.txt

# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage report
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run code quality checks
ruff check scripts/
ruff format --check scripts/

# Run security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Run type checking
mypy scripts/ --ignore-missing-imports
```

모든 테스트는 `main` 또는 `develop` 브랜치로의 Push, 그리고 `main` 브랜치 대상 PR 생성 시 자동 실행됩니다. 자세한 내용은 [TESTING.md](.github/TESTING.md)를 참고하세요.

</details>

<details>
<summary>EPUB 생성</summary>

이 가이드를 오프라인으로 읽고 싶으신가요? EPUB 전자책을 생성할 수 있습니다.

```bash
uv run scripts/build_epub.py
```

이 명령은 렌더링된 Mermaid 다이어그램을 포함한 모든 콘텐츠가 담긴 `claude-howto-guide.epub` 파일을 생성합니다.

추가 옵션은 [scripts/README.md](scripts/README.md)를 참고하세요.

</details>

<details>
<summary>기여하기</summary>

문제를 발견했거나 예제를 추가하고 싶으신가요? 여러분의 기여를 환영합니다.

**다음 내용을 포함한 자세한 가이드는 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.**
- 기여 유형(예제, 문서, 기능, 버그 수정, 피드백)
- 개발 환경 설정 방법
- 디렉터리 구조 및 콘텐츠 추가 방법
- 작성 가이드라인 및 모범 사례
- 커밋 및 PR 절차

**커뮤니티 규칙**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 커뮤니티 구성원 간의 행동 기준
- [SECURITY.md](SECURITY.md) - 보안 정책 및 취약점 신고 절차


### 보안 이슈 신고

보안 취약점을 발견한 경우 책임감 있게 신고해 주세요.

1. **GitHub Private Vulnerability Reporting 사용**: https://github.com/luongnv89/claude-howto/security/advisories
2. 또는 [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md)를 참고하여 상세 절차를 확인하세요.
3. 보안 취약점에 대해서는 **공개 이슈를 생성하지 마세요.**

빠른 시작 절차:
1. 저장소를 Fork 및 Clone합니다.
2. 설명이 명확한 브랜치를 생성합니다 (`add/feature-name`, `fix/bug`, `docs/improvement`)
3. 가이드라인에 따라 변경 사항을 적용합니다.
4. 변경 내용을 설명하는 Pull Request를 제출합니다.

**도움이 필요하신가요?** 이슈 또는 Discussion을 생성해 주세요. 절차를 안내해 드리겠습니다.


</details>

<details>
<summary>추가 자료</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 바로 사용할 수 있는 스킬 모음
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 개발자가 직접 공유한 체계적인 워크플로: 병렬 에이전트, 공유 CLAUDE.md, Plan 모드, 슬래시 명령어, 서브에이전트, 검증 훅을 활용한 장시간 자율 세션 운영 방식

</details>

---

## 기여하기

기여를 환영합니다! 시작 방법은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

---

## 라이선스

MIT License - 자세한 내용은 [LICENSE](LICENSE)를 참고하세요. 자유롭게 사용, 수정, 배포할 수 있으며, 유일한 요구 사항은 라이선스 고지를 포함하는 것입니다.


---

**최종 업데이트**: 2026년 6월 2일
**Claude Code 버전**: 2.1.160
**출처**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://github.com/anthropics/claude-code/releases
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
**호환 모델**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
