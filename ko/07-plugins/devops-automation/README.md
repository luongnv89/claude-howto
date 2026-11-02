<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation Plugin

배포, 모니터링 및 인시던트 대응을 위한 완전한 DevOps 자동화 플러그인입니다.

## Features

✅ 자동 배포
✅ 롤백 절차
✅ 시스템 상태 모니터링
✅ 인시던트 대응 워크플로우
✅ Kubernetes 통합

## Installation

```bash
/plugin install devops-automation
```

## What's Included

### Slash Commands
- `/deploy` - 프로덕션 또는 스테이징 환경에 배포
- `/rollback` - 이전 버전으로 롤백
- `/status` - 시스템 상태 확인
- `/incident` - 프로덕션 인시던트 처리

### Subagents
- `deployment-specialist` - 배포 작업 담당
- `incident-commander` - 인시던트 조정 담당
- `alert-analyzer` - 시스템 상태 분석 담당

### MCP Servers
- Kubernetes 통합

### Scripts
- `deploy.sh` - 배포 자동화
- `rollback.sh` - 롤백 자동화
- `health-check.sh` - 상태 점검 유틸리티

### Hooks
- `pre-deploy.js` - 배포 전 검증
- `post-deploy.js` - 배포 후 작업

## Usage

### 스테이징 환경 배포
```
/deploy staging
```

### 프로덕션 환경 배포
```
/deploy production
```

### 롤백
```
/rollback production
```

### 상태 확인
```
/status
```

### 인시던트 처리
```
/incident
```

## Requirements

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- 구성된 클러스터 접근 권한

## Configuration

Kubernetes 설정을 구성합니다:
```bash
export KUBECONFIG=~/.kube/config
```

## Example Workflow

```
User: /deploy production

Claude:
1. Runs pre-deploy hook (validates kubectl, cluster connection)
2. Delegates to deployment-specialist subagent
3. Runs deploy.sh script
4. Monitors deployment progress via Kubernetes MCP
5. Runs post-deploy hook (waits for pods, smoke tests)
6. Provides deployment summary

Result:
✅ Deployment complete
📦 Version: v2.1.0
🚀 Pods: 3/3 ready
⏱️  Time: 2m 34s
```

---

**Last Updated**: June 2, 2026
**Claude Code Version**: 2.1.160
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
