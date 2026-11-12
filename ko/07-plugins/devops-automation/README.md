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

### 스크립트
- `deploy.sh` - 배포 자동화
- `rollback.sh` - 롤백 자동화
- `health-check.sh` - 상태 점검 유틸리티

### 훅

`hooks/hooks.json`은 두 스크립트를 Bash 도구 호출에 등록합니다. 두 스크립트는 배포 명령어(`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`)에만 동작하고, 그 밖의 모든 명령어에는 0으로 종료합니다.

- `pre-deploy.js`(`PreToolUse`): `kubectl`이 없거나 클러스터에 연결할 수 없으면 명령어를 차단하며(종료 코드 2), Claude는 그 이유를 확인할 수 있습니다
- `post-deploy.js`(`PostToolUse`): 배포를 점검하고, 실패하면 Claude에게 알립니다. `DEPLOY_DEPLOYMENT`가 설정되어 있으면 `kubectl rollout status`를 실행하며(최대 120초), 이 명령은 새 파드를 기다립니다. 그렇지 않고 `DEPLOY_APP_LABEL`이 설정되어 있으면 대체 방법으로 해당 레이블이 붙은 파드가 Ready 상태가 될 때까지 `kubectl wait`로 기다립니다. 이때 아직 Ready 상태인 이전 파드도 이 점검을 통과합니다. 둘 다 설정되지 않으면 점검을 건너뜁니다. Claude에게 보내는 메모에는 어떤 점검을 실행했는지 표시됩니다

두 훅 모두 클러스터 상태를 읽기만 합니다(`kubectl version`, `cluster-info`, `rollout status`, `wait`).

명령어를 인식하는 방식: 스크립트는 heredoc 본문과 따옴표로 묶인 문자열을 제거하고, 명령어를 줄바꿈, `&&`, `||`, `;`, `|`, `&` 기준으로 나눈 뒤, 각 부분의 첫 단어를 확인합니다(`VAR=value`와 `sudo`, `env` 같은 래퍼는 건너뜀). 하위 명령어 앞에 전역 플래그가 있어도 인식되므로 `kubectl -n prod apply`와 `helm -n prod upgrade`는 배포로 간주되지만, `echo "kubectl apply"`, `cat scripts/deploy.sh`, `git commit -m "helm upgrade notes"`는 배포가 아닙니다. 이것은 셸 파서가 아니라 휴리스틱이므로, 따옴표 안에 숨은 배포(`bash -c "kubectl apply …"`), 다른 래퍼(`ssh`, `xargs`, `make deploy`) 뒤의 배포, 다른 스크립트 안의 배포는 놓칩니다. 이를 안전 경계로 삼지 마세요.

배포 명령어가 실행되는 동안 `Ctrl+Enter`를 눌러 턴이 끝나면, 명령어가 끝날 때 post-deploy 훅은 여전히 실행되지만 Claude Code가 `timeout` 값과 관계없이 10초 후에 훅을 종료하므로 점검이 끝나지 않을 수 있습니다.

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
- Node.js(훅 스크립트 실행)
- Kubernetes CLI (kubectl)
- 구성된 클러스터 접근 권한

## 설정

훅과 스크립트는 평소의 `kubectl` 설정(`~/.kube/config`, 또는 설정한 경우 `KUBECONFIG`)을 사용합니다.

배포 후 점검용(선택 사항, `DEPLOY_DEPLOYMENT`를 설정하거나, 파드 준비 상태 대체 점검을 위해 `DEPLOY_APP_LABEL`을 설정):
```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## 워크플로 예시

```text
User: /devops-automation:deploy production

Claude:
1. Delegates to deployment-specialist subagent
2. Runs deploy.sh script; the pre-deploy hook first checks kubectl and the cluster connection
3. post-deploy hook waits for pods to be ready
4. Provides deployment summary

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
**호환 모델**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
