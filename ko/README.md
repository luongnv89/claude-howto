<!-- i18n-source: README.md -->
<!-- i18n-source-sha: 553a319 -->
<!-- i18n-date: 2026-05-16 -->

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
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.138-brightgreen)](../CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **Language / Ngôn ngữ / 语言 / Мова / 言語 / 언어:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](../zh/README.md) | [Українська](../uk/README.md) | [日本語](../ja/README.md) | [한국어](README.md)

> **한국어 안내:** 이 문서는 영문 `README.md`(소스 SHA `553a319`)의 한국어 번역본이다.
> 실무(예: nexus, openpi)에 바로 적용하는 흐름은 [실무 적용 가이드](PRACTICAL-GUIDE.md)를,
> 자주 쓰는 명령은 [퀵 레퍼런스](QUICK_REFERENCE.md)를 참고한다. 번역 용어 규칙은
> [TRANSLATION_NOTES.md](TRANSLATION_NOTES.md)에 정리되어 있다. 아직 번역되지 않은
> 모듈 본문(`01-`~`10-`), `CATALOG.md`, `LEARNING-ROADMAP.md` 등은 영문 원문으로 연결된다.

# 주말 동안 Claude Code 마스터하기

`claude`를 입력하는 수준에서 에이전트, 훅, 스킬, MCP 서버를 지휘하는 수준까지 — 시각적 튜토리얼, 복사해서 바로 쓰는 템플릿, 안내형 학습 경로와 함께.

**[15분 만에 시작하기](#15분-만에-시작하기)** | **[내 레벨 찾기](#어디서-시작할지-모르겠다면)** | **[기능 카탈로그 보기](../CATALOG.md)**

---

## 목차

- [문제점](#문제점)
- [Claude How To가 이것을 해결하는 방법](#claude-how-to가-이것을-해결하는-방법)
- [작동 방식](#작동-방식)
- [어디서 시작할지 모르겠다면](#어디서-시작할지-모르겠다면)
- [15분 만에 시작하기](#15분-만에-시작하기)
- [이걸로 무엇을 만들 수 있나](#이걸로-무엇을-만들-수-있나)
- [FAQ](#faq)
- [기여하기](#기여하기)
- [라이선스](#라이선스)

---

## 문제점

Claude Code를 설치했다. 프롬프트도 몇 개 실행해 봤다. 그다음은?

- **공식 문서는 기능을 설명하지만, 그것들을 어떻게 조합하는지는 보여주지 않는다.** 슬래시 커맨드가 존재한다는 건 알지만, 그것을 훅·메모리·서브에이전트와 엮어서 실제로 몇 시간을 절약하는 워크플로로 만드는 법은 모른다.
- **명확한 학습 경로가 없다.** MCP를 훅보다 먼저 배워야 하나? 스킬을 서브에이전트보다 먼저? 결국 모든 걸 훑기만 하고 어느 것도 제대로 익히지 못한다.
- **예제가 너무 기초적이다.** "hello world" 슬래시 커맨드는 메모리를 사용하고, 전문 에이전트에 위임하며, 보안 스캔을 자동 실행하는 운영 수준의 코드 리뷰 파이프라인을 만드는 데 도움이 되지 않는다.

당신은 Claude Code 성능의 90%를 놓치고 있다 — 그리고 무엇을 모르는지조차 모른다.

---

## Claude How To가 이것을 해결하는 방법

이것은 또 하나의 기능 레퍼런스가 아니다. **구조화되고, 시각적이며, 예제 중심인 가이드**로, 모든 Claude Code 기능을 오늘 당장 프로젝트에 복사해 넣을 수 있는 실전 템플릿과 함께 가르친다.

| | 공식 문서 | 이 가이드 |
|--|---------------|------------|
| **형식** | 레퍼런스 문서 | Mermaid 다이어그램이 있는 시각적 튜토리얼 |
| **깊이** | 기능 설명 | 내부에서 어떻게 동작하는지 |
| **예제** | 기초 스니펫 | 즉시 사용하는 운영 수준 템플릿 |
| **구조** | 기능별 정리 | 점진적 학습 경로(초급→고급) |
| **온보딩** | 자율 진행 | 소요 시간이 표시된 안내형 로드맵 |
| **자가 진단** | 없음 | 약점을 찾아 맞춤 경로를 만드는 대화형 퀴즈 |

### 무엇을 얻는가:

- **10개 튜토리얼 모듈** — 슬래시 커맨드부터 커스텀 에이전트 팀까지 모든 Claude Code 기능을 다룬다
- **복사해서 쓰는 설정** — 슬래시 커맨드, CLAUDE.md 템플릿, 훅 스크립트, MCP 설정, 서브에이전트 정의, 전체 플러그인 번들
- **Mermaid 다이어그램** — 각 기능이 내부에서 어떻게 동작하는지 보여주어, *어떻게*뿐 아니라 *왜*까지 이해하게 한다
- **안내형 학습 경로** — 11~13시간 만에 초급에서 파워 유저로
- **내장 자가 진단** — Claude Code에서 `/self-assessment` 또는 `/lesson-quiz hooks`를 실행해 약점을 찾는다

**[학습 경로 시작하기  ->](../LEARNING-ROADMAP.md)**

---

## 작동 방식

### 1. 내 레벨 찾기

[자가 진단 퀴즈](../LEARNING-ROADMAP.md)를 보거나 Claude Code에서 `/self-assessment`를 실행한다. 이미 아는 것을 바탕으로 맞춤 로드맵을 받는다.

### 2. 안내형 경로 따라가기

10개 모듈을 순서대로 진행한다 — 각 모듈은 이전 모듈 위에 쌓인다. 배우면서 템플릿을 프로젝트에 바로 복사한다.

### 3. 기능을 워크플로로 조합하기

진짜 힘은 기능 조합에 있다. 슬래시 커맨드 + 메모리 + 서브에이전트 + 훅을 엮어, 코드 리뷰·배포·문서 생성을 처리하는 자동 파이프라인을 만드는 법을 배운다.

### 4. 이해도 점검하기

각 모듈 후 `/lesson-quiz [주제]`를 실행한다. 퀴즈가 놓친 부분을 짚어주어 빠르게 빈틈을 메운다.

**[15분 만에 시작하기](#15분-만에-시작하기)**

---

## 개발자들이 신뢰하는 가이드

- Claude Code를 매일 쓰는 개발자들이 준 **GitHub 스타**
- 이 가이드를 자기 워크플로에 맞춰 쓰는 팀들의 **포크**
- **활발히 유지보수** — 모든 Claude Code 릴리스에 맞춰 동기화(최신: v2.1.138, 2026년 5월)
- **커뮤니티 주도** — 실무 설정을 공유하는 개발자들의 기여

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 어디서 시작할지 모르겠다면

자가 진단을 보거나 레벨을 고른다:

| 레벨 | 할 수 있는 것 | 시작 지점 | 시간 |
|-------|-----------|------------|------|
| **초급** | Claude Code 실행 및 대화 | [슬래시 커맨드](../01-slash-commands/) | 약 2.5시간 |
| **중급** | CLAUDE.md와 커스텀 커맨드 사용 | [스킬](../03-skills/) | 약 3.5시간 |
| **고급** | MCP 서버와 훅 설정 | [고급 기능](../09-advanced-features/) | 약 5시간 |

**10개 모듈 전체 학습 경로:**

| 순서 | 모듈 | 레벨 | 시간 |
|-------|--------|-------|------|
| 1 | [슬래시 커맨드](../01-slash-commands/) | 초급 | 30분 |
| 2 | [메모리](../02-memory/) | 초급+ | 45분 |
| 3 | [체크포인트](../08-checkpoints/) | 중급 | 45분 |
| 4 | [CLI 기초](../10-cli/) | 초급+ | 30분 |
| 5 | [스킬](../03-skills/) | 중급 | 1시간 |
| 6 | [훅](../06-hooks/) | 중급 | 1시간 |
| 7 | [MCP](../05-mcp/) | 중급+ | 1시간 |
| 8 | [서브에이전트](../04-subagents/) | 중급+ | 1.5시간 |
| 9 | [고급 기능](../09-advanced-features/) | 고급 | 2~3시간 |
| 10 | [플러그인](../07-plugins/) | 고급 | 2시간 |

**[전체 학습 로드맵 ->](../LEARNING-ROADMAP.md)**

---

## 15분 만에 시작하기

> **설치 참고**: v2.1.113부터 Claude Code는 플랫폼별 네이티브 바이너리(macOS/Linux/Windows)로 배포된다. `npm install -g @anthropic-ai/claude-code`도 여전히 동작한다 — 네이티브 바이너리는 첫 사용 시 옵션 의존성으로 다운로드된다. v2.1.116 기준 다운로드는 `https://downloads.claude.ai/claude-code-releases`에서 받는다 — 사내 프록시는 이 호스트를 허용 목록에 추가해야 한다.

```bash
# 1. 가이드 클론
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 첫 슬래시 커맨드 복사
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 실행해 보기 — Claude Code에서 입력:
# /optimize

# 4. 더 해볼 준비가 됐다면? 프로젝트 메모리 설정:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 스킬 설치:
cp -r 03-skills/code-review ~/.claude/skills/
```

전체 설정을 원하는가? **1시간 핵심 설정**은 다음과 같다:

```bash
# 슬래시 커맨드 (15분)
cp 01-slash-commands/*.md .claude/commands/

# 프로젝트 메모리 (15분)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 스킬 설치 (15분)
cp -r 03-skills/code-review ~/.claude/skills/

# 주말 목표: 훅, 서브에이전트, MCP, 플러그인 추가
# 안내형 설정은 학습 경로를 따른다
```

**[전체 설치 레퍼런스 보기](#15분-만에-시작하기)**

---

## 이걸로 무엇을 만들 수 있나

| 사용 사례 | 조합할 기능 |
|----------|------------------------|
| **자동 코드 리뷰** | 슬래시 커맨드 + 서브에이전트 + 메모리 + MCP |
| **팀 온보딩** | 메모리 + 슬래시 커맨드 + 플러그인 |
| **CI/CD 자동화** | CLI 레퍼런스 + 훅 + 백그라운드 태스크 |
| **문서 생성** | 스킬 + 서브에이전트 + 플러그인 |
| **보안 감사** | 서브에이전트 + 스킬 + 훅(읽기 전용 모드) |
| **DevOps 파이프라인** | 플러그인 + MCP + 훅 + 백그라운드 태스크 |
| **복잡한 리팩터링** | 체크포인트 + 플래닝 모드 + 훅 |

---

## FAQ

**무료인가?**
그렇다. MIT 라이선스, 영구 무료. 개인 프로젝트, 회사, 팀에서 자유롭게 사용한다 — 라이선스 표기 포함 외에 제약 없음.

**유지보수되는가?**
활발히. 가이드는 모든 Claude Code 릴리스에 맞춰 동기화된다. 현재 버전: v2.1.138(2026년 5월), Claude Code 2.1+ 호환.

**공식 문서와 무엇이 다른가?**
공식 문서는 기능 레퍼런스다. 이 가이드는 다이어그램, 운영 수준 템플릿, 점진적 학습 경로가 있는 튜토리얼이다. 둘은 상호 보완적이다 — 여기서 배우고, 구체적인 내용이 필요할 때 문서를 참조한다.

**전체를 보는 데 얼마나 걸리나?**
전체 경로는 11~13시간. 하지만 15분 만에 즉시 가치를 얻는다 — 슬래시 커맨드 템플릿을 복사해 실행해 보기만 하면 된다.

**Claude Sonnet / Haiku / Opus와 함께 쓸 수 있나?**
그렇다. 모든 템플릿은 Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5에서 동작한다.

**기여할 수 있나?**
물론이다. 가이드라인은 [CONTRIBUTING.md](../CONTRIBUTING.md)를 참조한다. 새 예제, 버그 수정, 문서 개선, 커뮤니티 템플릿을 환영한다.

**오프라인으로 읽을 수 있나?**
그렇다. `uv run scripts/build_epub.py`를 실행하면 모든 내용과 렌더링된 다이어그램이 담긴 EPUB 전자책이 생성된다.

---

## 오늘부터 Claude Code 마스터하기

Claude Code는 이미 설치돼 있다. 당신과 10배 생산성 사이에 남은 유일한 것은 사용법을 아는 것이다. 이 가이드는 구조화된 경로, 시각적 설명, 복사해 쓰는 템플릿으로 거기까지 데려간다.

MIT 라이선스. 영구 무료. 클론하고, 포크하고, 당신 것으로 만들어라.

**[학습 경로 시작하기 ->](../LEARNING-ROADMAP.md)** | **[기능 카탈로그 보기](../CATALOG.md)** | **[15분 만에 시작하기](#15분-만에-시작하기)**

---

<details>
<summary>빠른 탐색 — 전체 기능</summary>

| 기능 | 설명 | 폴더 |
|---------|-------------|--------|
| **기능 카탈로그** | 설치 명령 포함 완전 레퍼런스 | [CATALOG.md](../CATALOG.md) |
| **슬래시 커맨드** | 사용자가 실행하는 단축 명령 | [01-slash-commands/](../01-slash-commands/) |
| **메모리** | 영속 컨텍스트 | [02-memory/](../02-memory/) |
| **스킬** | 재사용 가능한 기능 | [03-skills/](../03-skills/) |
| **서브에이전트** | 전문화된 AI 어시스턴트 | [04-subagents/](../04-subagents/) |
| **MCP 프로토콜** | 외부 도구 접근 | [05-mcp/](../05-mcp/) |
| **훅** | 이벤트 기반 자동화 | [06-hooks/](../06-hooks/) |
| **플러그인** | 번들된 기능 | [07-plugins/](../07-plugins/) |
| **체크포인트** | 세션 스냅샷 및 되감기 | [08-checkpoints/](../08-checkpoints/) |
| **고급 기능** | 플래닝, 사고, 백그라운드 태스크 | [09-advanced-features/](../09-advanced-features/) |
| **CLI 레퍼런스** | 명령, 플래그, 옵션 | [10-cli/](../10-cli/) |
| **블로그 글** | 실무 사용 예제 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>기능 비교</summary>

| 기능 | 호출 방식 | 영속성 | 적합한 용도 |
|---------|-----------|------------|----------|
| **슬래시 커맨드** | 수동(`/cmd`) | 세션 한정 | 빠른 단축 |
| **메모리** | 자동 로드 | 세션 간 유지 | 장기 학습 |
| **스킬** | 자동 호출 | 파일시스템 | 자동 워크플로 |
| **서브에이전트** | 자동 위임 | 격리된 컨텍스트 | 작업 분산 |
| **MCP 프로토콜** | 자동 질의 | 실시간 | 라이브 데이터 접근 |
| **훅** | 이벤트 트리거 | 설정 기반 | 자동화 및 검증 |
| **플러그인** | 명령 하나 | 모든 기능 | 완성형 솔루션 |
| **체크포인트** | 수동/자동 | 세션 기반 | 안전한 실험 |
| **플래닝 모드** | 수동/자동 | 플랜 단계 | 복잡한 구현 |
| **백그라운드 태스크** | 수동 | 작업 지속 시간 | 장시간 작업 |
| **CLI 레퍼런스** | 터미널 명령 | 세션/스크립트 | 자동화 및 스크립팅 |

</details>

<details>
<summary>설치 퀵 레퍼런스</summary>

```bash
# 슬래시 커맨드
cp 01-slash-commands/*.md .claude/commands/

# 메모리
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 스킬
cp -r 03-skills/code-review ~/.claude/skills/

# 서브에이전트
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 훅
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 플러그인
/plugin install pr-review

# 체크포인트 (자동 활성화, 설정에서 구성)
# 08-checkpoints/README.md 참조

# 고급 기능 (설정에서 구성)
# 09-advanced-features/config-examples.json 참조

# CLI 레퍼런스 (설치 불필요)
# 사용 예제는 10-cli/README.md 참조
```

</details>

<details>
<summary>01. 슬래시 커맨드</summary>

**위치**: [01-slash-commands/](../01-slash-commands/)

**무엇**: Markdown 파일로 저장되는 사용자 호출 단축 명령

**예제**:
- `optimize.md` - 코드 최적화 분석
- `pr.md` - 풀 리퀘스트 준비
- `generate-api-docs.md` - API 문서 생성기

**설치**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**사용법**:
```text
/optimize
/pr
/generate-api-docs
```

**더 알아보기**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. 메모리</summary>

**위치**: [02-memory/](../02-memory/)

**무엇**: 세션 간 영속 컨텍스트

**예제**:
- `project-CLAUDE.md` - 팀 전체 프로젝트 표준
- `directory-api-CLAUDE.md` - 디렉터리별 규칙
- `personal-CLAUDE.md` - 개인 선호 설정

**설치**:
```bash
# 프로젝트 메모리
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 디렉터리 메모리
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 개인 메모리
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**사용법**: Claude가 자동으로 로드

</details>

<details>
<summary>03. 스킬</summary>

**위치**: [03-skills/](../03-skills/)

**무엇**: 지시문과 스크립트를 갖춘, 재사용 가능하고 자동 호출되는 기능

**예제**:
- `code-review/` - 스크립트가 포함된 종합 코드 리뷰
- `brand-voice/` - 브랜드 보이스 일관성 검사기
- `doc-generator/` - API 문서 생성기

**설치**:
```bash
# 개인 스킬
cp -r 03-skills/code-review ~/.claude/skills/

# 프로젝트 스킬
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**사용법**: 관련 상황에서 자동 호출

</details>

<details>
<summary>04. 서브에이전트</summary>

**위치**: [04-subagents/](../04-subagents/)

**무엇**: 격리된 컨텍스트와 커스텀 프롬프트를 갖춘 전문 AI 어시스턴트

**예제**:
- `code-reviewer.md` - 종합 코드 품질 분석
- `test-engineer.md` - 테스트 전략 및 커버리지
- `documentation-writer.md` - 기술 문서
- `secure-reviewer.md` - 보안 중심 리뷰(읽기 전용)
- `implementation-agent.md` - 전체 기능 구현

**설치**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**사용법**: 메인 에이전트가 자동으로 위임

</details>

<details>
<summary>05. MCP 프로토콜</summary>

**위치**: [05-mcp/](../05-mcp/)

**무엇**: 외부 도구와 API에 접근하기 위한 Model Context Protocol

**예제**:
- `github-mcp.json` - GitHub 연동
- `database-mcp.json` - 데이터베이스 질의
- `filesystem-mcp.json` - 파일 작업
- `multi-mcp.json` - 다중 MCP 서버

**설치**:
```bash
# 환경 변수 설정
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# CLI로 MCP 서버 추가
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 또는 프로젝트 .mcp.json에 수동 추가 (예제는 05-mcp/ 참조)
```

**사용법**: 설정되면 MCP 도구가 Claude에 자동으로 제공됨

</details>

<details>
<summary>06. 훅</summary>

**위치**: [06-hooks/](../06-hooks/)

**무엇**: Claude Code 이벤트에 반응해 자동 실행되는 이벤트 기반 셸 명령

**예제**:
- `format-code.sh` - 쓰기 전 코드 자동 포맷
- `pre-commit.sh` - 커밋 전 테스트 실행
- `security-scan.sh` - 보안 문제 스캔
- `log-bash.sh` - 모든 bash 명령 로깅
- `validate-prompt.sh` - 사용자 프롬프트 검증
- `notify-team.sh` - 이벤트 발생 시 알림 전송

**설치**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

`~/.claude/settings.json`에서 훅 설정:
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

**사용법**: 이벤트 발생 시 훅이 자동 실행

**훅 종류** (5종, 28개 이벤트):
- **도구 훅**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **세션 훅**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **태스크 훅**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **라이프사이클 훅**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. 플러그인</summary>

**위치**: [07-plugins/](../07-plugins/)

**무엇**: 커맨드, 에이전트, MCP, 훅을 묶은 번들

**예제**:
- `pr-review/` - 완성형 PR 리뷰 워크플로
- `devops-automation/` - 배포 및 모니터링
- `documentation/` - 문서 생성

**설치**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**사용법**: 번들된 슬래시 커맨드와 기능 사용

</details>

<details>
<summary>08. 체크포인트와 되감기</summary>

**위치**: [08-checkpoints/](../08-checkpoints/)

**무엇**: 대화 상태를 저장하고 이전 지점으로 되감아 다른 접근을 탐색

**핵심 개념**:
- **체크포인트**: 대화 상태의 스냅샷
- **되감기**: 이전 체크포인트로 복귀
- **분기점**: 같은 체크포인트에서 여러 접근 탐색

**사용법**:
```text
# 체크포인트는 모든 사용자 프롬프트마다 자동 생성됨
# 되감으려면 Esc를 두 번 누르거나 다음을 사용:
/rewind

# 그다음 다섯 가지 옵션 중 선택:
# 1. 코드와 대화 복원
# 2. 대화 복원
# 3. 코드 복원
# 4. 여기서부터 요약
# 5. 취소
```

**사용 사례**:
- 다른 구현 접근 시도
- 실수 복구
- 안전한 실험
- 대안 비교
- 다른 설계 A/B 테스트

</details>

<details>
<summary>09. 고급 기능</summary>

**위치**: [09-advanced-features/](../09-advanced-features/)

**무엇**: 복잡한 워크플로와 자동화를 위한 고급 기능

**포함**:
- **플래닝 모드** — 코딩 전 상세 구현 계획 작성
- **확장 사고(Extended Thinking)** — 복잡한 문제를 위한 깊은 추론(`Alt+T` / `Option+T`로 토글)
- **백그라운드 태스크** — 차단 없이 장시간 작업 실행
- **권한 모드** — `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **헤드리스 모드** — CI/CD에서 Claude Code 실행: `claude -p "Run tests and generate report"`
- **세션 관리** — `/resume`, `/rename`, `/fork`, `claude -c`, `claude -r`
- **설정** — `~/.claude/settings.json`에서 동작 커스터마이즈

전체 설정은 [config-examples.json](../09-advanced-features/config-examples.json)을 참조한다.

</details>

<details>
<summary>10. CLI 레퍼런스</summary>

**위치**: [10-cli/](../10-cli/)

**무엇**: Claude Code의 완전한 명령행 인터페이스 레퍼런스

**빠른 예제**:
```bash
# 대화형 모드
claude "explain this project"

# 프린트 모드(비대화형)
claude -p "review this code"

# 파일 내용 처리
cat error.log | claude -p "explain this error"

# 스크립트용 JSON 출력
claude -p --output-format json "list functions"

# 세션 재개
claude -r "feature-auth" "continue implementation"
```

**사용 사례**: CI/CD 파이프라인 통합, 스크립트 자동화, 배치 처리, 다중 세션 워크플로, 커스텀 에이전트 설정

</details>

<details>
<summary>예제 워크플로</summary>

### 완전한 코드 리뷰 워크플로

```markdown
# 사용: 슬래시 커맨드 + 서브에이전트 + 메모리 + MCP

User: /review-pr

Claude:
1. 프로젝트 메모리 로드(코딩 표준)
2. GitHub MCP로 PR 가져오기
3. code-reviewer 서브에이전트에 위임
4. test-engineer 서브에이전트에 위임
5. 결과 종합
6. 종합 리뷰 제공
```

### 자동 문서화

```markdown
# 사용: 스킬 + 서브에이전트 + 메모리

User: "auth 모듈의 API 문서를 생성해줘"

Claude:
1. 프로젝트 메모리 로드(문서 표준)
2. 문서 생성 요청 감지
3. doc-generator 스킬 자동 호출
4. api-documenter 서브에이전트에 위임
5. 예제가 포함된 종합 문서 생성
```

### DevOps 배포

```markdown
# 사용: 플러그인 + MCP + 훅

User: /deploy production

Claude:
1. 배포 전 훅 실행(환경 검증)
2. deployment-specialist 서브에이전트에 위임
3. Kubernetes MCP로 배포 실행
4. 진행 상황 모니터링
5. 배포 후 훅 실행(헬스 체크)
6. 상태 보고
```

</details>

<details>
<summary>디렉터리 구조</summary>

```text
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
│   ├── code-review/
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

### 권장

- 슬래시 커맨드로 간단하게 시작
- 기능을 점진적으로 추가
- 팀 표준에는 메모리 사용
- 설정은 먼저 로컬에서 테스트
- 커스텀 구현은 문서화
- 프로젝트 설정은 버전 관리
- 플러그인은 팀과 공유

### 비권장

- 중복 기능을 만들지 말 것
- 자격 증명을 하드코딩하지 말 것
- 문서화를 건너뛰지 말 것
- 간단한 작업을 과하게 복잡화하지 말 것
- 보안 모범 사례를 무시하지 말 것
- 민감 데이터를 커밋하지 말 것

</details>

<details>
<summary>문제 해결</summary>

### 기능이 로드되지 않음
1. 파일 위치와 이름 확인
2. YAML 프론트매터 문법 확인
3. 파일 권한 확인
4. Claude Code 버전 호환성 검토

### MCP 연결 실패
1. 환경 변수 확인
2. MCP 서버 설치 확인
3. 자격 증명 테스트
4. 네트워크 연결 검토

### 서브에이전트가 위임되지 않음
1. 도구 권한 확인
2. 에이전트 설명의 명확성 확인
3. 작업 복잡도 검토
4. 에이전트를 독립적으로 테스트

</details>

<details>
<summary>테스트</summary>

이 프로젝트는 종합적인 자동 테스트를 포함한다:

- **단위 테스트**: pytest 기반 Python 테스트(Python 3.10, 3.11, 3.12)
- **코드 품질**: Ruff로 린팅 및 포맷팅
- **보안**: Bandit로 취약점 스캔
- **타입 검사**: mypy로 정적 타입 분석
- **빌드 검증**: EPUB 생성 테스트
- **커버리지 추적**: Codecov 연동

```bash
# 개발 의존성 설치
uv pip install -r requirements-dev.txt

# 모든 단위 테스트 실행
pytest scripts/tests/ -v

# 커버리지 리포트와 함께 테스트 실행
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 코드 품질 검사 실행
ruff check scripts/
ruff format --check scripts/

# 보안 스캔 실행
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 타입 검사 실행
mypy scripts/ --ignore-missing-imports
```

테스트는 `main`/`develop` 푸시마다, 그리고 `main`에 대한 모든 PR마다 자동 실행된다. 자세한 내용은 [TESTING.md](../.github/TESTING.md)를 참조한다.

</details>

<details>
<summary>EPUB 생성</summary>

이 가이드를 오프라인으로 읽고 싶은가? EPUB 전자책을 생성한다:

```bash
uv run scripts/build_epub.py
```

모든 내용과 렌더링된 Mermaid 다이어그램이 포함된 `claude-howto-guide.epub`이 생성된다.

더 많은 옵션은 [scripts/README.md](../scripts/README.md)를 참조한다.

</details>

<details>
<summary>기여하기</summary>

문제를 발견했거나 예제를 기여하고 싶은가? 도움을 환영한다!

**자세한 가이드라인은 [CONTRIBUTING.md](../CONTRIBUTING.md)를 참조:**
- 기여 종류(예제, 문서, 기능, 버그, 피드백)
- 개발 환경 설정 방법
- 디렉터리 구조와 콘텐츠 추가 방법
- 작성 가이드라인과 모범 사례
- 커밋 및 PR 절차

**커뮤니티 표준:**
- [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) - 서로를 대하는 방식
- [SECURITY.md](../SECURITY.md) - 보안 정책 및 취약점 보고

### 보안 이슈 보고

보안 취약점을 발견하면 책임 있게 보고한다:

1. **GitHub Private Vulnerability Reporting 사용**: https://github.com/luongnv89/claude-howto/security/advisories
2. **또는** 자세한 절차는 [.github/SECURITY_REPORTING.md](../.github/SECURITY_REPORTING.md) 참조
3. 보안 취약점에 대해 공개 이슈를 **열지 말 것**

빠른 시작:
1. 레포 포크 및 클론
2. 설명적인 브랜치 생성(`add/feature-name`, `fix/bug`, `docs/improvement`)
3. 가이드라인에 따라 변경
4. 명확한 설명과 함께 풀 리퀘스트 제출

**도움이 필요한가?** 이슈나 디스커션을 열면 절차를 안내한다.

</details>

<details>
<summary>추가 자료</summary>

- [Claude Code 문서](https://code.claude.com/docs/en/overview)
- [MCP 프로토콜 명세](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 바로 쓰는 스킬 모음
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny의 Claude Code 워크플로](https://x.com/bcherny/status/2007179832300581177) - Claude Code 제작자가 체계화한 워크플로를 공유한다: 병렬 에이전트, 공유 CLAUDE.md, 플래닝 모드, 슬래시 커맨드, 서브에이전트, 자율 장시간 세션을 위한 검증 훅.

</details>

---

## 기여하기

기여를 환영한다! 시작 방법에 대한 자세한 내용은 [기여 가이드](../CONTRIBUTING.md)를 참조한다.

---

## 라이선스

MIT 라이선스 - [LICENSE](../LICENSE) 참조. 사용, 수정, 배포 자유. 유일한 요구사항은 라이선스 표기 포함이다.

---

**최종 수정**: 2026년 5월 9일
**Claude Code 버전**: 2.1.138
**출처**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://github.com/anthropics/claude-code/releases/tag/v2.1.113
**호환 모델**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
