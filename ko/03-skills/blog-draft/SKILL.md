name: blog-draft
description: 아이디어와 자료를 바탕으로 블로그 게시물을 작성합니다. 사용자가 블로그 게시물을 작성하거나, 연구를 통해 콘텐츠를 만들거나, 기사를 초안할 때 사용합니다. 연구, 브레인스토밍, 개요 작성, 버전 관리를 통한 반복적인 초안 작성을 안내합니다.

## 사용자 입력

```text
$ARGUMENTS
```

계속 진행하기 전에 사용자 입력을 **반드시** 고려해야 합니다. 사용자는 다음을 제공해야 합니다:
- **아이디어/주제**: 블로그 게시물의 주요 개념 또는 테마
- **자료**: 연구를 위한 URL, 파일 또는 참고 자료 (선택 사항이지만 권장됨)
- **대상 독자**: 블로그 게시물이 누구를 위한 것인지 (선택 사항)
- **어조/스타일**: 공식적, 비공식적, 기술적 등 (선택 사항)

**중요**: 사용자가 **기존 블로그 게시물**에 대한 업데이트를 요청하는 경우, 0-8단계를 건너뛰고 **9단계**부터 바로 시작하세요. 먼저 기존 초안 파일을 읽은 다음, 반복 프로세스를 진행하세요.

## 실행 흐름

다음 단계를 순서대로 따르세요. **명시된 사용자 승인 없이는 단계를 건너뛰거나 다음으로 진행하지 마세요.**

### 0단계: 프로젝트 폴더 생성

1. 다음 형식으로 폴더 이름을 생성합니다: `YYYY-MM-DD-short-topic-name`
   - 오늘 날짜를 사용합니다.
   - 주제에서 짧고 URL 친화적인 슬러그를 생성합니다 (소문자, 하이픈, 최대 5단어).

2. 폴더 구조를 생성합니다:
   ```
   blog-posts/
   └── YYYY-MM-DD-short-topic-name/
       └── resources/
   ```

3. 계속 진행하기 전에 사용자에게 폴더 생성을 확인합니다.

### 1단계: 연구 및 자료 수집

1. 블로그 게시물 디렉터리에 `resources/` 하위 폴더를 생성합니다.

2. 제공된 각 자료에 대해:
   - **URL**: 주요 정보를 가져와 `resources/`에 마크다운 파일로 저장합니다.
   - **파일**: `resources/`에서 읽고 요약합니다.
   - **주제**: 웹 검색을 사용하여 최신 정보를 수집합니다.

3. 각 자료에 대해 `resources/`에 요약 파일을 생성합니다:
   - `resources/source-1-[short-name].md`
   - `resources/source-2-[short-name].md`
   - etc.

4. 각 요약에는 다음 내용이 포함되어야 합니다:
   ```markdown
   # Source: [Title/URL]

   ## Key Points
   - Point 1
   - Point 2

   ## Relevant Quotes/Data
   - Quote or statistic 1
   - Quote or statistic 2

   ## How This Relates to Topic
   Brief explanation of relevance
   ```

5. 사용자에게 연구 요약을 제시합니다.

### 2단계: 브레인스토밍 및 명확화

1. 아이디어와 연구된 자료를 바탕으로 다음을 제시합니다:
   - 연구에서 파악된 **주요 테마**
   - 블로그 게시물에 대한 **잠재적 관점**
   - 다루어야 할 **핵심 요점**
   - 명확화가 필요한 정보의 **공백**

2. 명확화 질문을 합니다:
   - 독자들이 얻어가길 바라는 주요 메시지는 무엇인가요?
   - 연구에서 강조하고 싶은 특정 요점이 있나요?
   - 목표 길이는 얼마인가요? (짧음: 500-800단어, 중간: 1000-1500단어, 김: 2000단어 이상)
   - 제외하고 싶은 요점이 있나요?

3. **진행하기 전에 사용자 응답을 기다립니다.**

### 3단계: 개요 제안

1. 다음을 포함하는 구조화된 개요를 생성합니다:

   ```markdown
   # Blog Post Outline: [Title]

   ## Meta Information
   - **Target Audience**: [who]
   - **Tone**: [style]
   - **Target Length**: [word count]
   - **Main Takeaway**: [key message]

   ## Proposed Structure

   ### Hook/Introduction
   - Opening hook idea
   - Context setting
   - Thesis statement

   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Supporting evidence from [source]

   ### Section 2: [Title]
   - Key point A
   - Key point B

   [Continue for all sections...]

   ### Conclusion
   - Summary of key points
   - Call to action or final thought

   ## Sources to Cite
   - Source 1
   - Source 2
   ```

2. 사용자에게 개요를 제시하고 **승인 또는 수정 요청 여부를 묻습니다.**

### 4단계: 승인된 개요 저장

1. 사용자가 개요를 승인하면, 블로그 게시물 폴더에 `OUTLINE.md`로 저장합니다.

2. 개요가 저장되었는지 확인합니다.

### 5단계: 개요 커밋 (git 저장소인 경우)

1. 현재 디렉터리가 git 저장소인지 확인합니다.

2. 그렇다면:
   - 새 파일들을 스테이징합니다: 블로그 게시물 폴더, resources, OUTLINE.md
   - Create commit with message: `docs: Add outline for blog post - [topic-name]`
   - 원격 저장소에 푸시합니다.

3. git 저장소가 아니라면, 이 단계를 건너뛰고 사용자에게 알립니다.

### 6단계: 초안 작성

1. 승인된 개요를 바탕으로 블로그 게시물 초안 전체를 작성합니다.

2. OUTLINE.md의 구조를 정확히 따릅니다.

3. 다음을 포함합니다:
   - 후크를 포함한 매력적인 서론
   - 명확한 섹션 헤더
   - 연구 자료로부터의 뒷받침하는 증거 및 예시
   - 섹션 간의 부드러운 전환
   - 주요 메시지가 담긴 강력한 결론
   - **인용**: 모든 비교, 통계, 데이터 포인트 및 사실적 주장은 원본 출처를 **반드시** 인용해야 합니다.

4. 초안을 블로그 게시물 폴더에 `draft-v0.1.md`로 저장합니다.

5. 형식:
   ```markdown
   # [Blog Post Title]

   *[Optional: subtitle or tagline]*

   [Full content with inline citations...]

   ---

   ## References
   - [1] Source 1 Title - URL or Citation
   - [2] Source 2 Title - URL or Citation
   - [3] Source 3 Title - URL or Citation
   ```

6. **인용 요구 사항**:
   - 모든 데이터 포인트, 통계 또는 비교는 인라인 인용을 **반드시** 포함해야 합니다.
   - 번호가 매겨진 참조 [1], [2] 등을 사용하거나 이름이 지정된 인용 [Source Name]을 사용합니다.
   - 인용을 마지막의 참조 섹션에 연결합니다.
   - Example: "Studies show that 65% of developers prefer TypeScript [1]"
   - Example: "React outperforms Vue in rendering speed by 20% [React Benchmarks 2024]"

### 7단계: 초안 커밋 (git 저장소인 경우)

1. git 저장소인지 확인합니다.

2. 그렇다면:
   - 초안 파일을 스테이징합니다.
   - Create commit with message: `docs: Add draft v0.1 for blog post - [topic-name]`
   - 원격 저장소에 푸시합니다.

3. git 저장소가 아니라면, 건너뛰고 사용자에게 알립니다.

### 8단계: 검토를 위한 초안 제시

1. 초안 내용을 사용자에게 제시합니다.

2. 피드백을 요청합니다:
   - 전반적인 인상은 어떤가요?
   - 확장 또는 축소가 필요한 섹션이 있나요?
   - 어조 조정이 필요한가요?
   - 누락된 정보가 있나요?
   - 특정 편집 또는 재작성이 필요한가요?

3. **사용자 응답을 기다립니다.**

### 9단계: 반복 또는 최종화

**사용자가 변경을 요청하는 경우:**
1. 요청된 모든 수정을 기록합니다.
2. 다음 조정 사항과 함께 6단계로 돌아갑니다:
   - 버전 번호를 증가시킵니다 (v0.2, v0.3 등).
   - 모든 피드백을 반영합니다.
   - `draft-v[X.Y].md`로 저장합니다.
   - 7-8단계를 반복합니다.

**사용자가 승인하는 경우:**
1. 최종 초안 버전을 확인합니다.
2. 사용자가 요청하는 경우 선택적으로 `final.md`로 이름을 변경합니다.
3. 블로그 게시물 생성 과정을 요약합니다:
   - 생성된 총 버전 수
   - 버전 간의 주요 변경 사항
   - 최종 단어 수
   - 생성된 파일

## 버전 추적

모든 초안은 점진적인 버전 관리를 통해 보존됩니다:
- `draft-v0.1.md` - 초기 초안
- `draft-v0.2.md` - 1차 피드백 후
- `draft-v0.3.md` - 2차 피드백 후
- 등

이는 블로그 게시물의 진화를 추적하고 필요한 경우 되돌릴 수 있게 합니다.

## 출력 파일 구조

```
blog-posts/
└── YYYY-MM-DD-topic-name/
    ├── resources/
    │   ├── source-1-name.md
    │   ├── source-2-name.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (if iterations)
    └── draft-v0.3.md (if more iterations)
```

## 품질 향상을 위한 팁

- **후크**: 질문, 놀라운 사실 또는 공감할 수 있는 시나리오로 시작합니다.
- **흐름**: 각 단락은 다음 단락과 연결되어야 합니다.
- **증거**: 연구 자료의 데이터로 주장을 뒷받침합니다.
- **인용**: 다음의 경우 출처를 **항상** 인용합니다:
  - 모든 통계 및 데이터 포인트 (예: "[출처]에 따르면, 75%의 ...")
  - 제품, 서비스 또는 접근 방식 간의 비교 (예: "X는 Y보다 2배 빠르게 작동합니다 [출처]")
  - 시장 동향, 연구 결과 또는 벤치마크에 대한 사실적 주장
  - [Source Name] 또는 [Author, Year] 형식으로 인라인 인용을 사용합니다.
- **어조**: 전체적으로 일관된 어조를 유지합니다.
- **길이**: 목표 단어 수를 준수합니다.
- **가독성**: 짧은 단락, 적절한 경우 글머리 기호를 사용합니다.
- **CTA**: 명확한 행동 유도 또는 생각할 거리를 제공하는 질문으로 끝냅니다.

## 참고 사항

- 명시된 체크포인트에서 항상 사용자 승인을 기다립니다.
- 기록을 위해 모든 초안 버전을 보존합니다.
- URL이 제공될 때 최신 정보를 위해 웹 검색을 사용합니다.
- 자료가 불충분한 경우, 사용자에게 더 많은 자료를 요청하거나 추가 연구를 제안합니다.
- 대상 독자 (기술적, 일반적, 비즈니스 등)에 따라 어조를 조정합니다.
