<!-- i18n-source: 07-plugins/documentation/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# 문서화 플러그인

프로젝트 문서를 포괄적으로 생성하고 유지 관리합니다.

## 기능

✅ API 문서 생성
✅ README 작성 및 업데이트
✅ 문서 동기화
✅ 코드 주석 개선
✅ 예제 생성

## 설치

```bash
claude --plugin-dir ./07-plugins/documentation
```

## 포함 항목

### 슬래시 명령어
- `/generate-api-docs` - API 문서 생성
- `/generate-readme` - README 작성 또는 업데이트
- `/sync-docs` - 코드 변경 사항과 문서 동기화
- `/validate-docs` - 문서 검증

### 서브에이전트
- `api-documenter` - API 문서화 전문
- `code-commentator` - 코드 주석 개선
- `example-generator` - 코드 예제 작성

### 템플릿
- `api-endpoint.md` - API 엔드포인트 문서 템플릿
- `function-docs.md` - 함수 문서 템플릿
- `adr-template.md` - 아키텍처 결정 기록(ADR) 템플릿

### MCP 서버
- 문서 동기화를 위한 GitHub 통합

## 사용 방법

### API 문서 생성
```
/generate-api-docs
```

### README 작성
```
/generate-readme
```

### 문서 동기화
```
/sync-docs
```

### 문서 검증
```
/validate-docs
```

## 요구 사항

- Claude Code 2.1+
- GitHub 접근 권한(선택 사항)

## 워크플로 예시

```
User: /generate-api-docs

Claude:
1. Scans all API endpoints in /src/api/
2. Delegates to api-documenter subagent
3. Extracts function signatures and JSDoc
4. Organizes by module/endpoint
5. Uses api-endpoint.md template
6. Generates comprehensive markdown docs
7. Includes curl, JavaScript, and Python examples

Result:
✅ API documentation generated
📄 Files created:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Coverage: 23/23 endpoints documented
```

## 템플릿 사용법

### API 엔드포인트 템플릿
전체 예제를 포함해 REST API 엔드포인트를 문서화할 때 사용합니다.

### 함수 문서 템플릿
개별 함수·메서드를 문서화할 때 사용합니다.

### ADR 템플릿
아키텍처 결정을 문서화할 때 사용합니다.

## 설정

문서 동기화를 위해 GitHub 토큰을 설정합니다.
```bash
export GITHUB_TOKEN="your_github_token"
```

## 모범 사례

- 문서를 코드 가까이에 둡니다
- 코드를 변경할 때 문서도 함께 업데이트합니다
- 실용적인 예제를 포함합니다
- 정기적으로 검증합니다
- 일관성을 위해 템플릿을 사용합니다

---

**최종 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
