<!-- i18n-source: 07-plugins/pr-review/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# PR 리뷰 플러그인

보안, 테스트, 문서 검증을 포함한 완전한 PR 리뷰 워크플로를 제공합니다.

## 기능

✅ 보안 분석
✅ 테스트 커버리지 검사
✅ 문서 검증
✅ 코드 품질 평가
✅ 성능 영향 분석

## 설치

```bash
claude --plugin-dir ./07-plugins/pr-review
```

로드하기 전에 플러그인을 검사합니다.

```bash
claude plugin validate ./07-plugins/pr-review
```

## 포함 항목

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### 슬래시 명령어

플러그인 명령어에는 `plugin.json`의 플러그인 `name`이 네임스페이스로 붙습니다.

- `/pr-review:review-pr` - 종합 PR 리뷰
- `/pr-review:check-security` - 보안 중심 리뷰
- `/pr-review:check-tests` - 테스트 커버리지 분석

### 서브에이전트
- `security-reviewer` - 보안 취약점 탐지
- `test-checker` - 테스트 커버리지 분석
- `performance-analyzer` - 성능 영향 평가

### MCP 서버

`.mcp.json`은 서버 하나, `github`를 선언합니다. GitHub의 공식 MCP 서버(`ghcr.io/github/github-mcp-server`)이며 Docker로 읽기 전용 모드로 실행됩니다. 이미지는 [v2.1.0 릴리스](https://github.com/github/github-mcp-server/releases/tag/v2.1.0)로 고정되어 있으며, 업그레이드하려면 `.mcp.json`의 태그를 변경하세요. `/mcp`에서는 `plugin:pr-review:github`로 표시됩니다.

### 훅(Hooks)

`hooks/hooks.json`은 `pre-review.js`를 `UserPromptExpansion` 이벤트에 등록하며, 위의 세 명령어에 대한 matcher를 사용합니다. matcher는 `pr-review:review-pr`(Claude Code 2.1.322가 플러그인 명령어에 대해 보내는 `command_name`)와 접두사 없는 `review-pr`를 모두 허용합니다. 이 중 하나를 입력하면 훅은 다음을 수행합니다.

- 현재 디렉터리가 git 저장소가 아니면 명령어를 차단합니다(종료 코드 2)
- 그렇지 않으면 현재 브랜치(또는 HEAD가 분리된 상태이거나 저장소에 아직 커밋이 없다는 안내)와, 커밋되지 않은 변경 사항에 대한 안내를 Claude의 컨텍스트에 추가합니다
- bare 저장소(또는 `.git` 내부)에서는 검토할 작업 트리가 없다는 안내만 추가합니다

## 사용 방법

### 기본 PR 리뷰
```text
/pr-review:review-pr
```

### 보안 점검만 수행
```text
/pr-review:check-security
```

### 테스트 커버리지 점검
```text
/pr-review:check-tests
```

## 요구 사항

- Claude Code 2.1+
- Node.js(훅 스크립트 실행)
- Docker(GitHub MCP 서버 실행)
- GitHub 개인 액세스 토큰
- Git 저장소

## 설정

Claude Code를 시작하기 전에 GitHub 토큰을 설정합니다.
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json`은 이 토큰을 서버가 읽는 변수인 `GITHUB_PERSONAL_ACCESS_TOKEN`으로 서버에 전달합니다. `/mcp`를 실행해 `plugin:pr-review:github`가 연결되었는지 확인하세요.

## 워크플로 예시

```text
User: /pr-review:review-pr

Claude:
1. pre-review hook checks the git repository and adds the branch to context
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

**최종 업데이트**: 2026년 10월 18일
**Claude Code 버전**: 2.1.302
**출처**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**호환 모델**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
