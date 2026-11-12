<!-- i18n-source: 07-plugins/devops-automation/README.md -->
<!-- i18n-source-sha: b968f42 -->
<!-- i18n-date: 2026-10-31 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps 자동화 플러그인

배포, 모니터링, 인시던트 대응을 위한 완전한 DevOps 자동화 플러그인입니다.

## 기능

✅ 자동 배포
✅ 롤백 절차
✅ 시스템 상태 모니터링
✅ 인시던트 대응 워크플로
✅ Kubernetes 통합

## 설치

```bash
claude --plugin-dir ./07-plugins/devops-automation
```

로드하기 전에 플러그인을 검사합니다.

```bash
claude plugin validate ./07-plugins/devops-automation
```

## 포함 항목

### 슬래시 명령어

플러그인 명령어에는 `plugin.json`의 플러그인 `name`이 네임스페이스로 붙습니다.

- `/devops-automation:deploy` - 프로덕션 또는 스테이징 환경에 배포
- `/devops-automation:rollback` - 이전 버전으로 롤백
- `/devops-automation:status` - 시스템 상태 확인
- `/devops-automation:incident` - 프로덕션 인시던트 처리

### 서브에이전트
- `deployment-specialist` - 배포 작업 담당
- `incident-commander` - 인시던트 조정 담당
- `alert-analyzer` - 시스템 상태 분석 담당

### MCP 서버

`.mcp.json`은 서버 하나, `kubernetes`를 선언합니다. `mcp-server-kubernetes` npm 패키지를 `npx`와 `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true`로 실행하므로 삭제 도구는 꺼져 있습니다. `/mcp`에서는 `plugin:devops-automation:kubernetes`로 표시됩니다.

### 스크립트
- `deploy.sh` - 배포 자동화
- `rollback.sh` - 롤백 자동화
- `health-check.sh` - 상태 점검 유틸리티

### 훅

`hooks/hooks.json`은 두 스크립트를 Bash 도구 호출에 등록합니다. 두 스크립트는 배포 명령어(`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`)에만 동작하고, 그 밖의 모든 명령어에는 0으로 종료합니다.

- `pre-deploy.js`(`PreToolUse`): `kubectl`이 없거나 클러스터에 연결할 수 없으면 명령어를 차단하며(종료 코드 2), Claude는 그 이유를 확인할 수 있습니다
- `post-deploy.js`(`PostToolUse`): `DEPLOY_APP_LABEL` 레이블이 붙은 파드가 준비될 때까지 최대 120초 기다리고, 준비되지 않으면 Claude에게 알립니다. `DEPLOY_APP_LABEL`이 설정되지 않으면 대기를 건너뜁니다

두 훅 모두 클러스터 상태를 읽기만 합니다(`kubectl version`, `cluster-info`, `wait`).

## 사용 방법

### 스테이징 환경 배포
```text
/devops-automation:deploy staging
```

### 프로덕션 환경 배포
```text
/devops-automation:deploy production
```

### 롤백
```text
/devops-automation:rollback production
```

### 상태 확인
```text
/devops-automation:status
```

### 인시던트 처리
```text
/devops-automation:incident
```

## 요구 사항

- Claude Code 2.1+
- Node.js(훅 스크립트와 MCP 서버 실행)
- Kubernetes CLI (kubectl)
- 구성된 클러스터 접근 권한

## 설정

Kubernetes 설정을 구성합니다(`.mcp.json`이 `KUBECONFIG`를 MCP 서버에 전달합니다).
```bash
export KUBECONFIG=~/.kube/config
```

배포 후 준비 상태 점검용(선택 사항):
```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## 워크플로 예시

```text
User: /devops-automation:deploy production

Claude:
1. Delegates to deployment-specialist subagent
2. Runs deploy.sh script; the pre-deploy hook first checks kubectl and the cluster connection
3. Monitors deployment progress via Kubernetes MCP
4. post-deploy hook waits for pods to be ready
5. Provides deployment summary

Result:
✅ Deployment complete
📦 Version: v2.1.0
🚀 Pods: 3/3 ready
⏱️  Time: 2m 34s
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
**호환 모델**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
