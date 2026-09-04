<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# PR 리뷰 플러그인

보안, 테스트, 문서 검증을 포함한 완전한 PR 리뷰 워크플로우를 제공합니다.

## 기능

✅ 보안 분석
✅ 테스트 커버리지 검사
✅ 문서 검증
✅ 코드 품질 평가
✅ 성능 영향 분석

## 설치

```bash
/plugin install pr-review
```

## 포함 항목

### 슬래시 명령어
- `/review-pr` - 종합 PR 리뷰
- `/check-security` - 보안 중심 리뷰
- `/check-tests` - 테스트 커버리지 분석

### 서브에이전트
- `security-reviewer` - 보안 취약점 탐지
- `test-checker` - 테스트 커버리지 분석
- `performance-analyzer` - 성능 영향 평가

### MCP 서버
- PR 데이터 연동을 위한 GitHub 통합

### 훅(Hooks)
- `pre-review.js` - 리뷰 전 검증

## 사용 방법

### 기본 PR 리뷰
```
/review-pr
```

### 보안 점검만 수행
```
/check-security
```

### 테스트 커버리지 점검
```
/check-tests
```

## 요구 사항

* Claude Code 1.0+
* GitHub 접근 권한
* Git 저장소

## 설정

GitHub 토큰을 설정합니다.
```bash
export GITHUB_TOKEN="your_github_token"
```

## 워크플로우 예시

```
User: /review-pr

Claude:
1. Runs pre-review hook (validates git repo)
2. Fetches PR data via GitHub MCP
3. Delegates security review to security-reviewer subagent
4. Delegates testing to test-checker subagent
5. Delegates performance to performance-analyzer subagent
6. Synthesizes all findings
7. Provides comprehensive review report

Result:
✅ Security: No critical issues found
⚠️  Testing: Coverage is 65%, recommend 80%+
✅ Performance: No significant impact
📝 Recommendations: Add tests for edge cases
```

---

**최종 업데이트**: 2026년 6월 2일
**Claude Code 버전**: 2.1.160
**출처**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
**호환 모델**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
