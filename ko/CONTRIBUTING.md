<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude How To 기여 가이드

이 프로젝트에 관심을 가져주셔서 감사합니다! 이 가이드는 효과적으로 기여하는 방법을 안내합니다.

## 이 프로젝트 소개

Claude How To는 Claude Code를 위한 시각적이고 예제 중심의 가이드입니다. 다음과 같은 콘텐츠를 제공합니다.

- **기능의 동작 방식을 설명하는 Mermaid 다이어그램**
- **즉시 사용할 수 있는 실전용 템플릿**
- **맥락과 모범 사례를 포함한 실제 예제**
- **초급부터 고급까지 이어지는 단계별 학습 경로**

## 기여 유형

### 1. 새로운 예제 또는 템플릿

기존 기능(Slash Commands, Skills, Hooks 등)에 대한 예제를 추가합니다.

- 바로 복사해서 사용할 수 있는 코드
- 동작 방식을 명확하게 설명
- 활용 사례 및 장점
- 문제 해결 팁

### 2. 문서 개선

- 이해하기 어려운 부분 명확하게 수정
- 오탈자 및 문법 수정
- 누락된 정보 추가
- 코드 예제 개선

### 3. 기능 가이드
새로운 Claude Code 기능에 대한 가이드를 작성합니다.
- 단계별 튜토리얼
- 아키텍처 다이어그램
- 일반적인 패턴과 안티패턴
- 실제 워크플로 예제

### 4. 버그 제보
발견한 문제를 제보합니다.
- 기대했던 동작 설명
- 실제 발생한 동작 설명
- 재현 절차 포함
- 사용한 Claude Code 버전 및 운영체제 정보 제공

### 5. 피드백 및 제안
가이드를 개선할 수 있도록 의견을 제공합니다.
- 더 나은 설명 제안
- 빠진 내용 지적
- 새로운 섹션 또는 문서 구조 개선 제안

## 시작하기

### 1. Fork 및 Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. 브랜치 생성
의미를 알 수 있는 브랜치 이름을 사용하세요.
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. 개발 환경 설정

Pre-commit Hook은 모든 커밋 전에 CI와 동일한 검사를 로컬에서 실행합니다. PR이 승인되려면 네 가지 검사를 모두 통과해야 합니다.

**필수 의존성:**

```bash
# Python 도구 (이 프로젝트에서는 uv를 패키지 관리자로 사용)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown 린터 (Node.js)
npm install -g markdownlint-cli

# Mermaid 다이어그램 검증 도구 (Node.js)
npm install -g @mermaid-js/mermaid-cli

# pre-commit 설치 및 Hook 활성화
uv pip install pre-commit
pre-commit install
```

**설정 확인:**

```bash
pre-commit run --all-files
```

모든 커밋에서 실행되는 Hook은 다음과 같습니다.

| Hook | 검사 내용 |
|------|----------|
| `markdown-lint` | Markdown 형식 및 구조 검사 |
| `cross-references` | 상대 링크, 앵커, 코드 펜스 검사 |
| `mermaid-syntax` | 모든 ` ```mermaid ` 블록의 문법 검사 |
| `link-check` | 외부 URL 접근 가능 여부 확인 |
| `build-epub` | `.md` 변경 시 EPUB 생성 오류 확인 |

## 디렉터리 구조

```
├── 01-slash-commands/      # 사용자 실행 단축 명령
├── 02-memory/              # 영구 컨텍스트 예제
├── 03-skills/              # 재사용 가능한 기능
├── 04-subagents/           # 전문 AI 보조 에이전트
├── 05-mcp/                 # Model Context Protocol 예제
├── 06-hooks/               # 이벤트 기반 자동화
├── 07-plugins/             # 기능 번들
├── 08-checkpoints/         # 세션 스냅샷
├── 09-advanced-features/   # 계획, 사고 과정, 백그라운드 기능
├── 10-cli/                 # CLI 참조
├── scripts/                # 빌드 및 유틸리티 스크립트
└── README.md               # 메인 가이드
```

## 예제 기여 방법

### Slash Command 추가
1. `01-slash-commands/`에 `.md` 파일을 생성합니다.
2. 다음 내용을 포함합니다.
   - 기능 설명
   - 사용 사례
   - 설치 방법
   - 사용 예제
   - 사용자 지정 팁
3. `01-slash-commands/README.md`를 업데이트합니다.

### Skill 추가
1. `03-skills/`에 디렉터리를 생성합니다.
2. 다음 내용을 포함합니다.
   - `SKILL.md` - 메인 문서
   - `scripts/` - 필요한 경우 보조 스크립트
   - `templates/` - 프롬프트 템플릿
   - README의 사용 예제
3. `03-skills/README.md`를 업데이트합니다.

### Subagent 추가
1. `04-subagents/`에 `.md` 파일을 생성합니다.
2. 다음 내용을 포함합니다.
   - 에이전트의 목적과 기능
   - 시스템 프롬프트 구조
   - 사용 예제
   - 통합 예제
3. `04-subagents/README.md`를 업데이트합니다.

### MCP 설정 추가
1. `05-mcp/`에 `.json` 파일을 생성합니다.
2. 다음 내용을 포함합니다.
   - 설정 설명
   - 필요한 환경 변수
   - 설정 방법
   - 사용 예제
3. `05-mcp/README.md`를 업데이트합니다.

### Hook 추가
1. `06-hooks/`에 `.sh` 파일을 생성합니다.
2. 다음 내용을 포함합니다.
   - Shebang 및 설명
   - 동작을 설명하는 명확한 주석
   - 오류 처리
   - 보안 고려 사항
3. `06-hooks/README.md`를 업데이트합니다.

## 작성 가이드라인

### Markdown 스타일
- 명확한 제목 사용(H2는 섹션, H3는 하위 섹션)
- 문단은 짧고 핵심적으로 작성
- 목록은 글머리표 사용
- 언어를 지정한 코드 블록 포함
- 섹션 사이에 빈 줄 추가

### 코드 예제
- 바로 복사해서 사용할 수 있도록 작성
- 이해하기 어려운 로직에는 주석 추가
- 간단한 버전과 고급 버전 모두 제공
- 실제 활용 사례 제시
- 발생 가능한 문제점 강조

### 문서 작성
- "무엇"뿐 아니라 "왜"도 설명
- 사전 요구 사항 포함
- 문제 해결 섹션 추가
- 관련 주제 링크 제공
- 초보자도 이해하기 쉽게 작성

### JSON/YAML
- 올바른 들여쓰기 사용(2칸 또는 4칸을 일관되게 유지)
- 설정을 설명하는 주석 추가
- 검증 예제 포함

### 다이어그램
- 가능하면 Mermaid 사용
- 다이어그램은 단순하고 읽기 쉽게 유지
- 다이어그램 아래에 설명 추가
- 관련 섹션으로 연결되는 링크 제공

## 커밋 가이드라인

Conventional Commit 형식을 따르세요.
```
type(scope): description

[optional body]
```

Types:
- `feat`: 새로운 기능 또는 예제
- `fix`: 버그 수정 또는 오류 수정
- `docs`: 문서 변경
- `refactor`: 코드 구조 개선
- `style`: 서식 변경
- `test`: 테스트 추가 또는 변경
- `chore`: 빌드, 의존성 등

예시:
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 제출 전 확인

### 체크리스트
- [ ] 코드가 프로젝트 스타일과 규칙을 따르는가
- [ ] 새로운 예제에 명확한 문서가 포함되어 있는가
- [ ] README 파일(로컬 및 루트)이 모두 업데이트되었는가
- [ ] 민감한 정보(API 키, 자격 증명 등)가 포함되지 않았는가
- [ ] 예제가 테스트되었으며 정상 동작하는가
- [ ] 모든 링크가 올바르게 연결되어 있는가
- [ ] 파일 권한이 올바르게 설정되어 있는가(스크립트 실행 권한 포함)
- [ ] 커밋 메시지가 명확하고 이해하기 쉬운가

### 로컬 테스트
```bash
# 모든 pre-commit 검사 실행(CI와 동일한 검사)
pre-commit run --all-files

# 변경 사항 검토
git diff
```

## Pull Request 절차

1. **명확한 설명과 함께 PR 생성**
   - 무엇을 추가하거나 수정했는가?
   - 왜 필요한가?
   - 관련 이슈(있는 경우)

2. **관련 세부 정보 포함**
   - 새로운 기능인가? 사용 사례 포함
   - 문서 변경인가? 개선 사항 설명
   - 예제인가? 변경 전/후 비교 제공

3. **이슈 연결**
   - 관련 이슈를 자동으로 닫으려면 `Closes #123` 사용

4. **리뷰를 기다려 주세요**
   - 유지 관리자가 개선 사항을 제안할 수 있습니다.
   - 피드백을 반영하여 수정해 주세요.
   - 최종 결정은 유지 관리자가 내립니다.

## 코드 리뷰 절차

리뷰어는 다음 사항을 확인합니다.
- **정확성**: 설명한 대로 동작하는가?
- **품질**: 실제 운영 환경에서도 사용할 수 있는 수준인가?
- **일관성**: 프로젝트의 기존 패턴을 따르는가?
- **문서화**: 명확하고 충분하게 작성되었는가?
- **보안**: 취약점은 없는가?

## 이슈 제보

### 버그 제보
다음 정보를 포함해 주세요.
- Claude Code 버전
- 운영체제
- 재현 방법
- 기대한 동작
- 실제 동작
- 필요한 경우 스크린샷


### 기능 요청
다음 정보를 포함해 주세요.
- 해결하려는 사용 사례 또는 문제
- 제안하는 해결 방법
- 고려했던 대안
- 추가 설명

### 문서 관련 문제
다음 정보를 포함해 주세요.
- 이해하기 어렵거나 누락된 부분
- 개선 제안
- 예제 또는 참고 자료

## 프로젝트 정책

### 민감한 정보
- API 키, 토큰 또는 자격 증명을 절대 커밋하지 마세요.
- 예제에서는 플레이스홀더 값을 사용하세요.
- 설정 파일에는 `.env.example`을 포함하세요.
- 필요한 환경 변수를 문서화하세요.

### 코드 품질
- 예제는 핵심에 집중하고 읽기 쉽게 작성하세요.
- 과도하게 복잡한 구현은 피하세요.
- 이해하기 어려운 로직에는 주석을 추가하세요.
- 제출 전에 충분히 테스트하세요.
-
### 지적 재산권
- 원본 콘텐츠의 저작권은 작성자에게 있습니다.
- 프로젝트는 교육 목적의 라이선스를 사용합니다.
- 기존 저작권을 존중하세요.
- 필요한 경우 출처를 명시하세요.

## 도움받기

- **질문**: GitHub Issues에서 Discussion을 생성하세요.
- **일반적인 도움**: 기존 문서를 먼저 확인하세요.
- **개발 관련 도움**: 비슷한 예제를 참고하세요.
- **코드 리뷰**: PR에서 유지 관리자를 멘션하세요.

## 기여자 인정

기여자는 다음 위치에서 인정받습니다.

- README.md의 Contributors 섹션
- GitHub Contributors 페이지
- 커밋 기록

## 보안

예제와 문서를 작성할 때는 안전한 코딩 원칙을 따라 주세요.

- **비밀 정보나 API 키를 하드코딩하지 마세요.** 환경 변수를 사용하세요.
- **보안상의 영향을 안내하세요.** 잠재적인 위험을 명확히 설명하세요.
- **안전한 기본값을 사용하세요.** 기본적으로 보안 기능을 활성화하세요.
- **입력을 검증하세요.** 적절한 입력 검증과 데이터 정제(Sanitization) 예제를 제공하세요.
- **보안 관련 참고 사항을 포함하세요.** 보안 고려 사항을 문서화하세요.

보안 문제는 취약점 제보 절차를 설명한 [SECURITY.md](SECURITY.md)를 참고하세요.

## 행동 강령

모든 사람이 환영받고 포용되는 커뮤니티를 만들기 위해 노력하고 있습니다. 자세한 커뮤니티 기준은 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)를 참고하세요.

요약하면 다음과 같습니다.
- 서로를 존중하고 포용하세요.
- 피드백을 열린 자세로 받아들이세요.
- 다른 사람의 학습과 성장을 도와주세요.
- 괴롭힘이나 차별을 하지 마세요.
- 문제가 발생하면 유지 관리자에게 알려 주세요.

모든 기여자는 이 행동 강령을 준수하며 서로를 친절하고 존중하는 태도로 대해야 합니다.

## 라이선스

이 프로젝트에 기여하면 기여한 내용이 MIT 라이선스로 배포되는 것에 동의하는 것으로 간주됩니다. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.

## 질문이 있으신가요?

- [README](README.md)를 확인하세요.
- [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)를 참고하세요.
- 기존 예제를 살펴보세요.
- 토론이 필요하면 이슈를 생성하세요.

기여해 주셔서 감사합니다! 🙏

---
**마지막 업데이트**: 2026년 4월 9일
