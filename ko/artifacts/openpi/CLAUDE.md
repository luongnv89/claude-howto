<!-- 대상: openpi 레포 루트에 `CLAUDE.md`로 복사 -->

# CLAUDE.md

openpi는 Physical Intelligence의 로봇 Vision-Language-Action(VLA) 모델
레포다(π₀, π₀-FAST, π₀.₅). JAX와 PyTorch 구현을 모두 포함한다. 라이브러리 +
학습/서빙 스크립트이며, 단일 앱이 아니다.

## 핵심 명령

```bash
# 테스트 (pyproject testpaths = src, scripts, packages)
pytest src scripts packages

# 수동 표시 테스트는 기본 제외됨; 필요 시
pytest -m manual src scripts packages

# 린트 / 포맷 (line-length 120, target py311, isort: force-single-line)
ruff check .
ruff format .

# 커밋 전 전체 게이트 (pre-commit: uv-lock, ruff, ruff-format)
pre-commit run --all-files

# 학습 / 서빙
python scripts/train.py <config_name>
python scripts/train_pytorch.py <config_name>
python scripts/serve_policy.py
python scripts/compute_norm_stats.py   # 새 데이터셋 추가 시 정규화 통계
```

Python 3.11+ 필요. 패키지 매니저는 `uv`.

## 아키텍처 지도

- `src/openpi/models/` — JAX 모델: `pi0.py`, `pi0_fast.py`, `gemma.py`,
  `siglip.py`, `lora.py`
- `src/openpi/models_pytorch/` — PyTorch 구현 및 transformers 패치
- `src/openpi/training/config.py` — **거대한 학습 설정 레지스트리**(pi0 /
  pi0_fast / pi05 변형 전부). 설정 조회·추가의 단일 진실원. 통째로 읽지 말고
  특정 설정명으로 좁혀 탐색한다(서브에이전트 `config-explorer` 권장).
- `src/openpi/training/data_loader.py`, `checkpoints.py` — 데이터 로딩,
  체크포인트 직렬화
- `src/openpi/policies/` — 추론용 정책 인터페이스
- `src/openpi/serving/` — 원격 추론 정책 서버
- `src/openpi/shared/` — 다운로드, 정규화, 이미지 유틸
- `scripts/` — `train.py`, `train_pytorch.py`, `serve_policy.py`,
  `compute_norm_stats.py`
- `examples/` — 로봇 플랫폼별(libero, droid, aloha_sim/real, ur5)
- `packages/openpi-client/` — 별도 배포되는 클라이언트 추론 패키지
- `third_party/` — ALOHA 서브모듈

## 하드 규칙

- **사용자가 명시 요청하기 전에는 커밋/푸시하지 않는다.**
- 새 로봇 플랫폼/데이터셋은 기존 설정을 복제·수정하는 방식으로
  `config.py`에 추가한다. 임의의 새 추상화를 만들지 않는다.
- `docker/`, `third_party/`, `src/openpi/models_pytorch/transformers_replace/*`
  는 ruff 제외 대상이다. 이 경로를 포맷하지 않는다.
- import 정렬은 isort `force-single-line` + `force-sort-within-sections`를
  따른다(ruff가 강제).
- 모델 수치 동작을 바꾸는 변경은 해당 `*_test.py`(예:
  `src/openpi/models/pi0_test.py`, `transforms_test.py`)로 검증한다.
- 큰 변경(예: PyTorch 포팅, 학습 루프 수정)은 먼저 플래닝 모드로 설계한다.

## 워크플로 선호

- 작은 수정 → 최소 diff. 타이포 고치려 섹션을 다시 쓰지 않는다.
- `config.py` 탐색은 `config-explorer` 서브에이전트에 위임해 메인
  컨텍스트 오염을 막는다.
- 품질 체크 실패 시 근본 원인을 고친다. `--no-verify`로 우회하지 않는다.

## 토큰 효율

- 방금 쓰거나 수정한 파일을 다시 읽지 않는다.
- 결과가 불확실하지 않으면 "검증" 목적의 명령 재실행을 하지 않는다.
- 요청받지 않았으면 큰 코드/파일 블록을 되풀이해 출력하지 않는다.
- 관련 편집은 한 번에 묶는다.
