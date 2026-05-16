<!-- 대상: nexus 레포의 .claude/commands/sync-check.md → /sync-check -->
---
description: scheduled_sync 사전 점검(validate_sync.sh)을 실행하고 결과를 요약한다
argument-hint: "[--config <path>]"
allowed-tools: Bash(bash scheduled_sync/validate_sync.sh*), Bash(crontab -l*), Read
---

nexus의 scheduled MLflow 동기화 설정을 점검한다.

## 절차

1. `scheduled_sync/validate_sync.sh`를 실행한다(인자 `$ARGUMENTS`가 있으면
   그대로 전달). 이 스크립트는 SSH 도달성, 원격 inbox 쓰기, 원격
   `import_delta.py` 존재, 중앙/로컬 MLflow `/health`, dry-run까지
   단계별로 검사한다.
2. 출력에서 **실패하거나 경고가 난 단계만** 골라 요약한다.
3. cron 충돌 경고가 있으면 현재 등록된 동기화 cron 항목을 함께 보여준다
   (`crontab -l` 중 sync 관련 라인).
4. 모든 단계 통과 시: "동기화 설정 정상" 한 줄과 확인된 원격/실험 수만 보고.
5. 실패 시: 가장 먼저 깨진 단계와, `docs/12_SCHEDULED_SYNC.md` 기준의
   해결 힌트를 1~2줄로 제시한다. 임의로 설정 파일을 수정하지 않는다.

## 주의

- 이 커맨드는 **읽기/검증 전용**이다. cron을 등록하거나 동기화를 실제
  실행하지 않는다.
- 로컬 MLflow가 떠 있어야 하는 단계가 있다. 미기동이면
  `bash scheduled_sync/start_local_mlflow.sh` 안내만 하고 자동 기동하지
  않는다.
