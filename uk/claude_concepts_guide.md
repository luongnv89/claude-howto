<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Повний довідник концепцій Claude

Комплексний довідник, що охоплює слеш-команди, субагентів, пам'ять, протокол MCP та навички агентів з таблицями, діаграмами та практичними прикладами.

---

## Зміст

1. [Слеш-команди](#слеш-команди)
2. [Субагенти](#субагенти)
3. [Пам'ять](#память)
4. [Протокол MCP](#протокол-mcp)
5. [Навички агентів](#навички-агентів)
6. [Плагіни](#плагіни-claude-code)
7. [Хуки](#хуки)
8. [Контрольні точки та відкат](#контрольні-точки-та-відкат)
9. [Просунуті функції](#просунуті-функції)
10. [Порівняння та інтеграція](#порівняння-та-інтеграція)

---

## Слеш-команди

### Огляд

Слеш-команди — це ярлики, ініційовані користувачем, що зберігаються як Markdown-файли, які Claude Code може виконувати. Вони дозволяють командам стандартизувати часто використовувані промпти та робочі процеси.

### Архітектура

```mermaid
graph TD
    A["User Input: /command-name"] -->|Triggers| B["Search .claude/commands/"]
    B -->|Finds| C["command-name.md"]
    C -->|Loads| D["Markdown Content"]
    D -->|Executes| E["Claude Processes Prompt"]
    E -->|Returns| F["Result in Context"]
```

### Структура файлів

```mermaid
graph LR
    A["Project Root"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### Таблиця організації команд

| Location | Scope | Availability | Use Case | Git Tracked |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | Project-specific | Team members | Team workflows, shared standards | ✅ Yes |
| `~/.claude/commands/` | Personal | Individual user | Personal shortcuts across projects | ❌ No |
| Subdirectories | Namespaced | Based on parent | Organize by category | ✅ Yes |

### Функції та можливості

| Feature | Example | Supported |
|---------|---------|-----------|
| Shell script execution | `bash scripts/deploy.sh` | ✅ Yes |
| File references | `@path/to/file.js` | ✅ Yes |
| Bash integration | `$(git log --oneline)` | ✅ Yes |
| Arguments | `/pr --verbose` | ✅ Yes |
| MCP commands | `/mcp__github__list_prs` | ✅ Yes |

### Практичні приклади

#### Приклад 1: Команда оптимізації коду

**Файл:** `.claude/commands/optimize.md`

```markdown
---
name: Code Optimization
description: Analyze code for performance issues and suggest optimizations
tags: performance, analysis
---

# Code Optimization

Review the provided code for the following issues in order of priority:

1. **Performance bottlenecks** - identify O(n²) operations, inefficient loops
2. **Memory leaks** - find unreleased resources, circular references
3. **Algorithm improvements** - suggest better algorithms or data structures
4. **Caching opportunities** - identify repeated computations
5. **Concurrency issues** - find race conditions or threading problems

Format your response with:
- Issue severity (Critical/High/Medium/Low)
- Location in code
- Explanation
- Recommended fix with code example
```

**Використання:**
```bash
# User types in Claude Code
/optimize

# Claude loads the prompt and waits for code input
```

#### Приклад 2: Команда-помічник для Pull Request

**Файл:** `.claude/commands/pr.md`

```markdown
---
name: Prepare Pull Request
description: Clean up code, stage changes, and prepare a pull request
tags: git, workflow
---

# Pull Request Preparation Checklist

Before creating a PR, execute these steps:

1. Run linting: `prettier --write .`
2. Run tests: `npm test`
3. Review git diff: `git diff HEAD`
4. Stage changes: `git add .`
5. Create commit message following conventional commits:
   - `fix:` for bug fixes
   - `feat:` for new features
   - `docs:` for documentation
   - `refactor:` for code restructuring
   - `test:` for test additions
   - `chore:` for maintenance

6. Generate PR summary including:
   - What changed
   - Why it changed
   - Testing performed
   - Potential impacts
```

**Використання:**
```bash
/pr

# Claude runs through checklist and prepares the PR
```

#### Приклад 3: Ієрархічний генератор документації

**Файл:** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: Generate API Documentation
description: Create comprehensive API documentation from source code
tags: documentation, api
---

# API Documentation Generator

Generate API documentation by:

1. Scanning all files in `/src/api/`
2. Extracting function signatures and JSDoc comments
3. Organizing by endpoint/module
4. Creating markdown with examples
5. Including request/response schemas
6. Adding error documentation

Output format:
- Markdown file in `/docs/api.md`
- Include curl examples for all endpoints
- Add TypeScript types
```

### Діаграма життєвого циклу команди

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: Types /optimize
    Claude->>FS: Searches .claude/commands/
    FS-->>Claude: Returns optimize.md
    Claude->>Claude: Loads Markdown content
    Claude->>User: Displays prompt context
    User->>Claude: Provides code to analyze
    Claude->>CLI: (May execute scripts)
    CLI-->>Claude: Results
    Claude->>User: Returns analysis
```

### Найкращі практики

| ✅ Рекомендовано | ❌ Не рекомендовано |
|------|---------|
| Використовуйте зрозумілі, орієнтовані на дію назви | Створювати команди для одноразових завдань |
| Документуйте ключові слова в описі | Будувати складну логіку в командах |
| Зосередьте команду на одному завданні | Створювати дублюючі команди |
| Контролюйте версії проєктних команд | Жорстко прописувати конфіденційну інформацію |
| Організовуйте у підкаталогах | Створювати довгі списки команд |
| Використовуйте прості, зрозумілі промпти | Використовувати скорочені або незрозумілі формулювання |

---

## Субагенти

### Огляд

Субагенти — це спеціалізовані AI-асистенти з ізольованими контекстними вікнами та налаштованими системними промптами. Вони забезпечують делеговане виконання завдань, зберігаючи чітке розділення відповідальностей.

### Діаграма архітектури

```mermaid
graph TB
    User["👤 User"]
    Main["🎯 Main Agent<br/>(Coordinator)"]
    Reviewer["🔍 Code Reviewer<br/>Subagent"]
    Tester["✅ Test Engineer<br/>Subagent"]
    Docs["📝 Documentation<br/>Subagent"]

    User -->|asks| Main
    Main -->|delegates| Reviewer
    Main -->|delegates| Tester
    Main -->|delegates| Docs
    Reviewer -->|returns result| Main
    Tester -->|returns result| Main
    Docs -->|returns result| Main
    Main -->|synthesizes| User
```

### Життєвий цикл субагента

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Separate<br/>Context Window

    User->>MainAgent: "Build new auth feature"
    MainAgent->>MainAgent: Analyze task
    MainAgent->>CodeReviewer: "Review this code"
    CodeReviewer->>Context: Initialize clean context
    Context->>CodeReviewer: Load reviewer instructions
    CodeReviewer->>CodeReviewer: Perform review
    CodeReviewer-->>MainAgent: Return findings
    MainAgent->>MainAgent: Incorporate results
    MainAgent-->>User: Provide synthesis
```

### Таблиця конфігурації субагента

| Конфігурація | Тип | Призначення | Приклад |
|---------------|------|---------|---------|
| `name` | String | Ідентифікатор агента | `code-reviewer` |
| `description` | String | Призначення та ключові слова | `Comprehensive code quality analysis` |
| `tools` | List/String | Дозволені можливості | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | Поведінкові інструкції | Користувацькі настанови |

### Ієрархія доступу до інструментів

```mermaid
graph TD
    A["Subagent Configuration"] -->|Option 1| B["Inherit All Tools<br/>from Main Thread"]
    A -->|Option 2| C["Specify Individual Tools"]
    B -->|Includes| B1["File Operations"]
    B -->|Includes| B2["Shell Commands"]
    B -->|Includes| B3["MCP Tools"]
    C -->|Explicit List| C1["read, grep, diff"]
    C -->|Explicit List| C2["Bash(npm:*), Bash(test:*)"]
```

### Практичні приклади

#### Приклад 1: Повне налаштування субагента

**Файл:** `.claude/agents/code-reviewer.md`

```yaml
---
name: code-reviewer
description: Comprehensive code quality and maintainability analysis
tools: read, grep, diff, lint_runner
---

# Code Reviewer Agent

You are an expert code reviewer specializing in:
- Performance optimization
- Security vulnerabilities
- Code maintainability
- Testing coverage
- Design patterns

## Review Priorities (in order)

1. **Security Issues** - Authentication, authorization, data exposure
2. **Performance Problems** - O(n²) operations, memory leaks, inefficient queries
3. **Code Quality** - Readability, naming, documentation
4. **Test Coverage** - Missing tests, edge cases
5. **Design Patterns** - SOLID principles, architecture

## Review Output Format

For each issue:
- **Severity**: Critical / High / Medium / Low
- **Category**: Security / Performance / Quality / Testing / Design
- **Location**: File path and line number
- **Issue Description**: What's wrong and why
- **Suggested Fix**: Code example
- **Impact**: How this affects the system

## Example Review

### Issue: N+1 Query Problem
- **Severity**: High
- **Category**: Performance
- **Location**: src/user-service.ts:45
- **Issue**: Loop executes database query in each iteration
- **Fix**: Use JOIN or batch query
```

**Файл:** `.claude/agents/test-engineer.md`

```yaml
---
name: test-engineer
description: Test strategy, coverage analysis, and automated testing
tools: read, write, bash, grep
---

# Test Engineer Agent

You are expert at:
- Writing comprehensive test suites
- Ensuring high code coverage (>80%)
- Testing edge cases and error scenarios
- Performance benchmarking
- Integration testing

## Testing Strategy

1. **Unit Tests** - Individual functions/methods
2. **Integration Tests** - Component interactions
3. **End-to-End Tests** - Complete workflows
4. **Edge Cases** - Boundary conditions
5. **Error Scenarios** - Failure handling

## Test Output Requirements

- Use Jest for JavaScript/TypeScript
- Include setup/teardown for each test
- Mock external dependencies
- Document test purpose
- Include performance assertions when relevant

## Coverage Requirements

- Minimum 80% code coverage
- 100% for critical paths
- Report missing coverage areas
```

**Файл:** `.claude/agents/documentation-writer.md`

```yaml
---
name: documentation-writer
description: Technical documentation, API docs, and user guides
tools: read, write, grep
---

# Documentation Writer Agent

You create:
- API documentation with examples
- User guides and tutorials
- Architecture documentation
- Changelog entries
- Code comment improvements

## Documentation Standards

1. **Clarity** - Use simple, clear language
2. **Examples** - Include practical code examples
3. **Completeness** - Cover all parameters and returns
4. **Structure** - Use consistent formatting
5. **Accuracy** - Verify against actual code

## Documentation Sections

### For APIs
- Description
- Parameters (with types)
- Returns (with types)
- Throws (possible errors)
- Examples (curl, JavaScript, Python)
- Related endpoints

### For Features
- Overview
- Prerequisites
- Step-by-step instructions
- Expected outcomes
- Troubleshooting
- Related topics
```

#### Приклад 2: Делегування субагентам у дії

```markdown
# Scenario: Building a Payment Feature

## User Request
"Build a secure payment processing feature that integrates with Stripe"

## Main Agent Flow

1. **Planning Phase**
   - Understands requirements
   - Determines tasks needed
   - Plans architecture

2. **Delegates to Code Reviewer Subagent**
   - Task: "Review the payment processing implementation for security"
   - Context: Auth, API keys, token handling
   - Reviews for: SQL injection, key exposure, HTTPS enforcement

3. **Delegates to Test Engineer Subagent**
   - Task: "Create comprehensive tests for payment flows"
   - Context: Success scenarios, failures, edge cases
   - Creates tests for: Valid payments, declined cards, network failures, webhooks

4. **Delegates to Documentation Writer Subagent**
   - Task: "Document the payment API endpoints"
   - Context: Request/response schemas
   - Produces: API docs with curl examples, error codes

5. **Synthesis**
   - Main agent collects all outputs
   - Integrates findings
   - Returns complete solution to user
```

#### Приклад 3: Обмеження доступу до інструментів

**Обмежене налаштування — лише конкретні команди**

```yaml
---
name: secure-reviewer
description: Security-focused code review with minimal permissions
tools: read, grep
---

# Secure Code Reviewer

Reviews code for security vulnerabilities only.

This agent:
- ✅ Reads files to analyze
- ✅ Searches for patterns
- ❌ Cannot execute code
- ❌ Cannot modify files
- ❌ Cannot run tests

This ensures the reviewer doesn't accidentally break anything.
```

**Розширене налаштування — усі інструменти для реалізації**

```yaml
---
name: implementation-agent
description: Full implementation capabilities for feature development
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

Builds features from specifications.

This agent:
- ✅ Reads specifications
- ✅ Writes new code files
- ✅ Runs build commands
- ✅ Searches codebase
- ✅ Edits existing files
- ✅ Finds files matching patterns

Full capabilities for independent feature development.
```

### Управління контекстом субагента

```mermaid
graph TB
    A["Main Agent Context<br/>50,000 tokens"]
    B["Subagent 1 Context<br/>20,000 tokens"]
    C["Subagent 2 Context<br/>20,000 tokens"]
    D["Subagent 3 Context<br/>20,000 tokens"]

    A -->|Clean slate| B
    A -->|Clean slate| C
    A -->|Clean slate| D

    B -->|Results only| A
    C -->|Results only| A
    D -->|Results only| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### Коли використовувати субагентів

| Сценарій | Використовувати субагента | Чому |
|----------|--------------|-----|
| Складна функція з багатьма кроками | ✅ Так | Розділення відповідальностей, запобігання засміченню контексту |
| Швидкий код-рев'ю | ❌ Ні | Непотрібні накладні витрати |
| Паралельне виконання завдань | ✅ Так | Кожен субагент має власний контекст |
| Потрібна спеціалізована експертиза | ✅ Так | Налаштовані системні промпти |
| Тривалий аналіз | ✅ Так | Запобігає вичерпанню основного контексту |
| Одне завдання | ❌ Ні | Додає затримку без необхідності |

### Команди агентів

Команди агентів координують кількох агентів, що працюють над пов'язаними завданнями. Замість делегування одному субагенту за раз, команди агентів дозволяють основному агенту оркеструвати групу агентів, які співпрацюють, обмінюються проміжними результатами та працюють над спільною метою. Це корисно для масштабних завдань, таких як повноцінна розробка фічі, де фронтенд-агент, бекенд-агент та агент тестування працюють паралельно.

---

## Пам'ять

### Огляд

Пам'ять дозволяє Claude зберігати контекст між сесіями та розмовами. Вона існує у двох формах: автоматичний синтез у claude.ai та файлова система CLAUDE.md у Claude Code.

### Архітектура пам'яті

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|User provides info| C
    C -->|Synthesizes every 24h| D
    D -->|Loads automatically| A
    A -->|Uses context| C
```

### Ієрархія пам'яті в Claude Code (7 рівнів)

Claude Code завантажує пам'ять із 7 рівнів, від найвищого до найнижчого пріоритету:

```mermaid
graph TD
    A["1. Managed Policy<br/>Enterprise admin policies"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>Automatically captured preferences"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### Таблиця розташування пам'яті

| Рівень | Розташування | Область | Пріоритет | Спільний | Найкраще для |
|------|----------|-------|----------|--------|----------|
| 1. Керована політика | Адмін підприємства | Організація | Найвищий | Усі користувачі орг. | Відповідність, політики безпеки |
| 2. Проєкт | `./CLAUDE.md` | Проєкт | Високий | Команда (Git) | Стандарти команди, архітектура |
| 3. Правила проєкту | `.claude/rules/*.md` | Проєкт | Високий | Команда (Git) | Модульні конвенції проєкту |
| 4. Користувач | `~/.claude/CLAUDE.md` | Персональний | Середній | Індивідуальний | Особисті налаштування |
| 5. Правила користувача | `~/.claude/rules/*.md` | Персональний | Середній | Індивідуальний | Персональні модулі правил |
| 6. Локальний | `.claude/local/CLAUDE.md` | Локальний | Низький | Не спільний | Налаштування конкретної машини |
| 7. Авто-пам'ять | Автоматичний | Сесія | Найнижчий | Індивідуальний | Засвоєні вподобання, патерни |

### Авто-пам'ять

Авто-пам'ять автоматично фіксує вподобання користувача та патерни, виявлені під час сесій. Claude навчається з ваших взаємодій і запам'ятовує:

- Вподобання стилю кодування
- Типові виправлення, які ви робите
- Вибір фреймворків та інструментів
- Вподобання стилю комунікації

Авто-пам'ять працює у фоновому режимі і не потребує ручного налаштування.

### Життєвий цикл оновлення пам'яті

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: "Remember: use async/await"
    Claude->>User: "Which memory file?"
    User->>Claude: "Project memory"
    Claude->>Editor: Open ~/.claude/settings.json
    Claude->>Memory: Write to ./CLAUDE.md
    Memory-->>Claude: File saved
    Claude->>Claude: Load updated memory
    Claude-->>User: "Memory saved!"
```

### Практичні приклади

#### Приклад 1: Структура пам'яті проєкту

**Файл:** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

#### Приклад 2: Пам'ять для конкретного каталогу

**Файл:** `./src/api/CLAUDE.md`

~~~~markdown
# API Module Standards

This file overrides root CLAUDE.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

### Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
~~~~

#### Приклад 3: Персональна пам'ять

**Файл:** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
~~~~

#### Приклад 4: Оновлення пам'яті під час сесії

**Взаємодія в сесії:**

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

### Пам'ять у Claude Web/Desktop

#### Хронологія синтезу пам'яті

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**Приклад підсумку пам'яті:**

```markdown
## Claude's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

### Порівняння функцій пам'яті

| Функція | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| Авто-синтез | ✅ Кожні 24 год | ❌ Вручну |
| Між проєктами | ✅ Спільний | ❌ Специфічний для проєкту |
| Доступ команди | ✅ Спільні проєкти | ✅ Через Git |
| Пошук | ✅ Вбудований | ✅ Через `/memory` |
| Редагування | ✅ У чаті | ✅ Пряме редагування файлу |
| Імпорт/Експорт | ✅ Так | ✅ Копіювання/вставка |
| Постійність | ✅ 24 год+ | ✅ Необмежено |

---

## Протокол MCP

### Огляд

MCP (Model Context Protocol) — це стандартизований спосіб доступу Claude до зовнішніх інструментів, API та джерел даних у реальному часі. На відміну від пам'яті, MCP забезпечує живий доступ до змінюваних даних.

### Архітектура MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A
```

### Екосистема MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]
```

### Процес налаштування MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

### Таблиця доступних MCP-серверів

| MCP-сервер | Призначення | Основні інструменти | Авторизація | Реальний час |
|------------|---------|--------------|------|-----------|
| **Filesystem** | Файлові операції | read, write, delete | Права ОС | ✅ Так |
| **GitHub** | Управління репозиторіями | list_prs, create_issue, push | OAuth | ✅ Так |
| **Slack** | Командна комунікація | send_message, list_channels | Token | ✅ Так |
| **Database** | SQL-запити | query, insert, update | Облікові дані | ✅ Так |
| **Google Docs** | Доступ до документів | read, write, share | OAuth | ✅ Так |
| **Asana** | Управління проєктами | create_task, update_status | API Key | ✅ Так |
| **Stripe** | Платіжні дані | list_charges, create_invoice | API Key | ✅ Так |
| **Memory** | Постійна пам'ять | store, retrieve, delete | Локальний | ❌ Ні |

### Практичні приклади

#### Приклад 1: Конфігурація GitHub MCP

**Файл:** `.mcp.json` (область проєкту) або `~/.claude.json` (область користувача)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Доступні інструменти GitHub MCP:**

~~~~markdown
# GitHub MCP Tools

## Pull Request Management
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `update_pr` - Update PR description/title
- `merge_pr` - Merge PR to main branch
- `review_pr` - Add review comments

Example request:
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue Management
- `list_issues` - List all issues
- `get_issue` - Get issue details
- `create_issue` - Create new issue
- `close_issue` - Close issue
- `add_comment` - Add comment to issue

## Repository Information
- `get_repo_info` - Repository details
- `list_files` - File tree structure
- `get_file_content` - Read file contents
- `search_code` - Search across codebase

## Commit Operations
- `list_commits` - Commit history
- `get_commit` - Specific commit details
- `create_commit` - Create new commit
~~~~

#### Приклад 2: Налаштування Database MCP

**Конфігурація:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**Приклад використання:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

#### Приклад 3: Робочий процес з кількома MCP

**Сценарій: Генерація щоденного звіту**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

#### Приклад 4: Операції Filesystem MCP

**Конфігурація:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**Доступні операції:**

| Операція | Команда | Призначення |
|-----------|---------|---------|
| Список файлів | `ls ~/projects` | Показати вміст каталогу |
| Читання файлу | `cat src/main.ts` | Прочитати вміст файлу |
| Запис файлу | `create docs/api.md` | Створити новий файл |
| Редагування файлу | `edit src/app.ts` | Змінити файл |
| Пошук | `grep "async function"` | Пошук у файлах |
| Видалення | `rm old-file.js` | Видалити файл |

### MCP проти пам'яті: Матриця рішень

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### Патерн запит/відповідь

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

---

## Навички агентів

### Огляд

Навички агентів — це повторно використовувані можливості, що викликаються моделлю, упаковані як теки з інструкціями, скриптами та ресурсами. Claude автоматично виявляє та використовує відповідні навички.

### Архітектура навичок

```mermaid
graph TB
    A["Skill Directory"]
    B["SKILL.md"]
    C["YAML Metadata"]
    D["Instructions"]
    E["Scripts"]
    F["Templates"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### Процес завантаження навички

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude
    participant System as System
    participant Skill as Skill

    User->>Claude: "Create Excel report"
    Claude->>System: Scan available skills
    System->>System: Load skill metadata
    Claude->>Claude: Match user request to skills
    Claude->>Skill: Load xlsx skill SKILL.md
    Skill-->>Claude: Return instructions + tools
    Claude->>Claude: Execute skill
    Claude->>User: Generate Excel file
```

### Таблиця типів та розташування навичок

| Тип | Розташування | Область | Спільний | Синхронізація | Найкраще для |
|------|----------|-------|--------|------|----------|
| Вбудовані | Built-in | Глобальний | Усі користувачі | Авто | Створення документів |
| Персональні | `~/.claude/skills/` | Індивідуальний | Ні | Вручну | Персональна автоматизація |
| Проєктні | `.claude/skills/` | Команда | Так | Git | Стандарти команди |
| Плагінні | Через встановлення плагіна | Різний | Залежить | Авто | Інтегровані функції |

### Вбудовані навички

```mermaid
graph TB
    A["Pre-built Skills"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["Create presentations"]
    B --> B2["Edit slides"]
    C --> C1["Create spreadsheets"]
    C --> C2["Analyze data"]
    D --> D1["Create documents"]
    D --> D2["Format text"]
    E --> E1["Generate PDFs"]
    E --> E2["Fill forms"]
```

### Комплектні навички

Claude Code тепер включає 5 комплектних навичок, доступних одразу:

| Навичка | Команда | Призначення |
|-------|---------|---------|
| **Simplify** | `/simplify` | Спрощення складного коду або пояснень |
| **Batch** | `/batch` | Виконання операцій над кількома файлами або елементами |
| **Debug** | `/debug` | Систематичне налагодження з аналізом кореневої причини |
| **Loop** | `/loop` | Планування повторюваних завдань за таймером |
| **Claude API** | `/claude-api` | Пряма взаємодія з Anthropic API |

Ці комплектні навички завжди доступні і не потребують встановлення або конфігурації.

### Практичні приклади

#### Приклад 1: Навичка код-рев'ю

**Структура каталогу:**

```
~/.claude/skills/code-review/
├── SKILL.md
├── templates/
│   ├── review-checklist.md
│   └── finding-template.md
└── scripts/
    ├── analyze-metrics.py
    └── compare-complexity.py
```

**Файл:** `~/.claude/skills/code-review/SKILL.md`

```yaml
---
name: Code Review Specialist
description: Comprehensive code review with security, performance, and quality analysis
version: "1.0.0"
tags:
  - code-review
  - quality
  - security
when_to_use: When users ask to review code, analyze code quality, or evaluate pull requests
effort: high
shell: bash
---

# Code Review Skill

This skill provides comprehensive code review capabilities focusing on:

1. **Security Analysis**
   - Authentication/authorization issues
   - Data exposure risks
   - Injection vulnerabilities
   - Cryptographic weaknesses
   - Sensitive data logging

2. **Performance Review**
   - Algorithm efficiency (Big O analysis)
   - Memory optimization
   - Database query optimization
   - Caching opportunities
   - Concurrency issues

3. **Code Quality**
   - SOLID principles
   - Design patterns
   - Naming conventions
   - Documentation
   - Test coverage

4. **Maintainability**
   - Code readability
   - Function size (should be < 50 lines)
   - Cyclomatic complexity
   - Dependency management
   - Type safety

## Review Template

For each piece of code reviewed, provide:

### Summary
- Overall quality assessment (1-5)
- Key findings count
- Recommended priority areas

### Critical Issues (if any)
- **Issue**: Clear description
- **Location**: File and line number
- **Impact**: Why this matters
- **Severity**: Critical/High/Medium
- **Fix**: Code example

### Findings by Category

#### Security (if issues found)
List security vulnerabilities with examples

#### Performance (if issues found)
List performance problems with complexity analysis

#### Quality (if issues found)
List code quality issues with refactoring suggestions

#### Maintainability (if issues found)
List maintainability problems with improvements
```
## Python Script: analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """Analyze code for common metrics."""

    # Count functions
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # Count classes
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # Average line length
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # Estimate complexity
    complexity = len(re.findall(r'\b(if|elif|else|for|while|and|or)\b', code))

    return {
        'functions': functions,
        'classes': classes,
        'avg_line_length': avg_length,
        'complexity_score': complexity
    }

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
```

## Python Script: compare-complexity.py

```python
#!/usr/bin/env python3
"""
Compare cyclomatic complexity of code before and after changes.
Helps identify if refactoring actually simplifies code structure.
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """Analyze code complexity metrics."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calculate cyclomatic complexity using McCabe's method.
        Count decision points: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Base complexity

        # Count decision points
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b(?!$)',
            r'\bor\b(?!$)'
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        Calculate cognitive complexity - how hard is it to understand?
        Based on nesting depth and control flow.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Track nesting depth
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # Reduce nesting when unindenting
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Maintainability Index ranges from 0-100.
        > 85: Excellent
        > 65: Good
        > 50: Fair
        < 50: Poor
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Simplified MI calculation
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """Generate comprehensive complexity report."""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compare complexity metrics between two code versions."""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("CODE COMPLEXITY COMPARISON")
    print("=" * 60)

    print("\nBEFORE:")
    print(f"  Cyclomatic Complexity:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {before_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {before_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {before_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {before_metrics['avg_line_length']}")

    print("\nAFTER:")
    print(f"  Cyclomatic Complexity:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {after_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {after_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {after_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {after_metrics['avg_line_length']}")

    print("\nCHANGES:")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  Cyclomatic Complexity:    {cyclomatic_change:+d}")
    print(f"  Cognitive Complexity:     {cognitive_change:+d}")
    print(f"  Maintainability Index:    {mi_change:+.2f}")
    print(f"  Lines of Code:            {loc_change:+d}")

    print("\nASSESSMENT:")
    if mi_change > 0:
        print("  ✅ Code is MORE maintainable")
    elif mi_change < 0:
        print("  ⚠️  Code is LESS maintainable")
    else:
        print("  ➡️  Maintainability unchanged")

    if cyclomatic_change < 0:
        print("  ✅ Complexity DECREASED")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexity INCREASED")
    else:
        print("  ➡️  Complexity unchanged")

    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
```

## Template: review-checklist.md

```markdown
# Code Review Checklist

## Security Checklist
- [ ] No hardcoded credentials or secrets
- [ ] Input validation on all user inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection on state-changing operations
- [ ] XSS prevention with proper escaping
- [ ] Authentication checks on protected endpoints
- [ ] Authorization checks on resources
- [ ] Secure password hashing (bcrypt, argon2)
- [ ] No sensitive data in logs
- [ ] HTTPS enforced

## Performance Checklist
- [ ] No N+1 queries
- [ ] Appropriate use of indexes
- [ ] Caching implemented where beneficial
- [ ] No blocking operations on main thread
- [ ] Async/await used correctly
- [ ] Large datasets paginated
- [ ] Database connections pooled
- [ ] Regular expressions optimized
- [ ] No unnecessary object creation
- [ ] Memory leaks prevented

## Quality Checklist
- [ ] Functions < 50 lines
- [ ] Clear variable naming
- [ ] No duplicate code
- [ ] Proper error handling
- [ ] Comments explain WHY, not WHAT
- [ ] No console.logs in production
- [ ] Type checking (TypeScript/JSDoc)
- [ ] SOLID principles followed
- [ ] Design patterns applied correctly
- [ ] Self-documenting code

## Testing Checklist
- [ ] Unit tests written
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Integration tests present
- [ ] Coverage > 80%
- [ ] No flaky tests
- [ ] Mock external dependencies
- [ ] Clear test names
```

## Template: finding-template.md

~~~~markdown
# Code Review Finding Template

Use this template when documenting each issue found during code review.

---

## Issue: [TITLE]

### Severity
- [ ] Critical (blocks deployment)
- [ ] High (should fix before merge)
- [ ] Medium (should fix soon)
- [ ] Low (nice to have)

### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### Issue Description

**What:** Describe what the issue is.

**Why it matters:** Explain the impact and why this needs to be fixed.

**Current behavior:** Show the problematic code or behavior.

**Expected behavior:** Describe what should happen instead.

### Code Example

#### Current (Problematic)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 100+ queries for 20 users | High |
| User Experience | Slow page load | High |
| Scalability | Breaks at scale | Critical |
| Maintainability | Hard to debug | Medium |

### Related Issues

- Similar issue in `AdminUserList.tsx` line 120
- Related PR: #456
- Related issue: #789

### Additional Resources

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### Reviewer Notes

- This is a common pattern in this codebase
- Consider adding this to the code style guide
- Might be worth creating a helper function

### Author Response (for feedback)

*To be filled by the code author:*

- [ ] Fix implemented in commit: `abc123`
- [ ] Fix status: Complete / In Progress / Needs Discussion
- [ ] Questions or concerns: (describe)

---

## Finding Statistics (for Reviewer)

When reviewing multiple findings, track:

- **Total Issues Found:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**Recommendation:** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality:** 1-5 stars
~~~~

## Usage Example

~~~~markdown
User: Review this React component code

Claude: I'll conduct a comprehensive code review using my Code Review Skill.

[Loads SKILL.md]
[Analyzes code against checklist]
[Runs Python metrics script]
[Applies templates]

## Code Review Results

### Summary
Quality Score: 3.5/5
Key Findings: 7 items
Priority Areas: Performance optimization, error handling

### Critical Issues: 1

**Issue**: N+1 Query Problem
**Location**: UserComponent.tsx, lines 45-52
**Impact**: Renders 100+ database queries for list of 20 users
**Severity**: High
**Fix**:
```javascript
// Before: N+1 queries
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ queries

// After: Single query with JOIN
const users = fetchUsersWithPosts(); // 1 query
```

### Performance Findings
- Missing pagination on large lists
- Recommendation: Use React.memo() for items
- Database query: Could be optimized with index

### Quality Findings
- Function in line 20 is 127 lines (max: 50)
- Missing error boundary
- Props should have TypeScript types
~~~~

#### Приклад 2: Навичка голосу бренду

**Структура каталогу:**

```
.claude/skills/brand-voice/
├── SKILL.md
├── brand-guidelines.md
├── tone-examples.md
└── templates/
    ├── email-template.txt
    ├── social-post-template.txt
    └── blog-post-template.md
```

**Файл:** `.claude/skills/brand-voice/SKILL.md`

```yaml
---
name: Brand Voice Consistency
description: Ensure all communication matches brand voice and tone guidelines
tags:
  - brand
  - writing
  - consistency
when_to_use: When creating marketing copy, customer communications, or public-facing content
---

# Brand Voice Skill

## Overview
This skill ensures all communications maintain consistent brand voice, tone, and messaging.

## Brand Identity

### Mission
Help teams automate their development workflows with AI

### Values
- **Simplicity**: Make complex things simple
- **Reliability**: Rock-solid execution
- **Empowerment**: Enable human creativity

### Tone of Voice
- **Friendly but professional** - approachable without being casual
- **Clear and concise** - avoid jargon, explain technical concepts simply
- **Confident** - we know what we're doing
- **Empathetic** - understand user needs and pain points

## Writing Guidelines

### Do's ✅
- Use "you" when addressing readers
- Use active voice: "Claude generates reports" not "Reports are generated by Claude"
- Start with value proposition
- Use concrete examples
- Keep sentences under 20 words
- Use lists for clarity
- Include calls-to-action

### Don'ts ❌
- Don't use corporate jargon
- Don't patronize or oversimplify
- Don't use "we believe" or "we think"
- Don't use ALL CAPS except for emphasis
- Don't create walls of text
- Don't assume technical knowledge

## Vocabulary

### ✅ Preferred Terms
- Claude (not "the Claude AI")
- Code generation (not "auto-coding")
- Agent (not "bot")
- Streamline (not "revolutionize")
- Integrate (not "synergize")

### ❌ Avoid Terms
- "Cutting-edge" (overused)
- "Game-changer" (vague)
- "Leverage" (corporate-speak)
- "Utilize" (use "use")
- "Paradigm shift" (unclear)
```
## Examples

### ✅ Good Example
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

Why it works: Clear value, specific benefits, action-oriented

### ❌ Bad Example
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

Why it doesn't work: Vague, corporate jargon, no specific value

## Template: Email

```
Subject: [Clear, benefit-driven subject]

Hi [Name],

[Opening: What's the value for them]

[Body: How it works / What they'll get]

[Specific example or benefit]

[Call to action: Clear next step]

Best regards,
[Name]
```

## Template: Social Media

```
[Hook: Grab attention in first line]
[2-3 lines: Value or interesting fact]
[Call to action: Link, question, or engagement]
[Emoji: 1-2 max for visual interest]
```

## File: tone-examples.md
```
Exciting announcement:
"Save 8 hours per week on code reviews. Claude reviews your PRs automatically."

Empathetic support:
"We know deployments can be stressful. Claude handles testing so you don't have to worry."

Confident product feature:
"Claude doesn't just suggest code. It understands your architecture and maintains consistency."

Educational blog post:
"Let's explore how agents improve code review workflows. Here's what we learned..."
```

#### Приклад 3: Навичка генерації документації

**Файл:** `.claude/skills/doc-generator/SKILL.md`

~~~~yaml
---
name: API Documentation Generator
description: Generate comprehensive, accurate API documentation from source code
version: "1.0.0"
tags:
  - documentation
  - api
  - automation
when_to_use: When creating or updating API documentation
---

# API Documentation Generator Skill

## Generates

- OpenAPI/Swagger specifications
- API endpoint documentation
- SDK usage examples
- Integration guides
- Error code references
- Authentication guides

## Documentation Structure

### For Each Endpoint

```markdown
## GET /api/v1/users/:id

### Description
Brief explanation of what this endpoint does

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### Examples

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```

## Python Script: generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
        if node.name.startswith('get_') or node.name.startswith('post_'):
            doc = ast.get_docstring(node)
            endpoint = {
                'name': node.name,
                'docstring': doc,
                'params': [arg.arg for arg in node.args.args],
                'returns': self._extract_return_type(node)
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
~~~~
### Виявлення та виклик навичок

```mermaid
graph TD
    A["User Request"] --> B["Claude Analyzes"]
    B -->|Scans| C["Available Skills"]
    C -->|Metadata check| D["Skill Description Match?"]
    D -->|Yes| E["Load SKILL.md"]
    D -->|No| F["Try next skill"]
    F -->|More skills?| D
    F -->|No more| G["Use general knowledge"]
    E --> H["Extract Instructions"]
    H --> I["Execute Skill"]
    I --> J["Return Results"]
```

### Навички проти інших функцій

```mermaid
graph TB
    A["Extending Claude"]
    B["Slash Commands"]
    C["Subagents"]
    D["Memory"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B -->|User-invoked| G["Quick shortcuts"]
    C -->|Auto-delegated| H["Isolated contexts"]
    D -->|Persistent| I["Cross-session context"]
    E -->|Real-time| J["External data access"]
    F -->|Auto-invoked| K["Autonomous execution"]
```

---

## Плагіни Claude Code

### Огляд

Плагіни Claude Code — це комплектні збірки налаштувань (слеш-команди, субагенти, MCP-сервери та хуки), які встановлюються однією командою. Вони представляють найвищий рівень механізму розширення — об'єднують кілька функцій у цілісні пакети, якими можна ділитися.

### Архітектура

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|bundles| B
    A -->|bundles| C
    A -->|bundles| D
    A -->|bundles| E
    A -->|bundles| F
```

### Процес завантаження плагіна

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: Download plugin manifest
    Plugin-->>Claude: Return plugin definition
    Claude->>Install: Extract components
    Install->>SlashCmds: Configure
    Install->>Subagents: Configure
    Install->>MCPServers: Configure
    Install->>Hooks: Configure
    SlashCmds-->>Tools: Ready to use
    Subagents-->>Tools: Ready to use
    MCPServers-->>Tools: Ready to use
    Hooks-->>Tools: Ready to use
    Tools-->>Claude: Plugin installed ✅
```

### Типи та дистрибуція плагінів

| Тип | Область | Спільний | Авторитет | Приклади |
|------|-------|--------|-----------|----------|
| Офіційний | Глобальний | Усі користувачі | Anthropic | PR Review, Security Guidance |
| Спільноти | Публічний | Усі користувачі | Спільнота | DevOps, Data Science |
| Організаційний | Внутрішній | Члени команди | Компанія | Внутрішні стандарти, інструменти |
| Персональний | Індивідуальний | Один користувач | Розробник | Користувацькі робочі процеси |

### Структура визначення плагіна

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT

# Plugin metadata
tags:
  - category
  - use-case

# Requirements
requires:
  - claude-code: ">=1.0.0"

# Components bundled
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# Configuration
config:
  auto_load: true
  enabled_by_default: true
---
```

### Структура плагіна

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### Практичні приклади

#### Приклад 1: Плагін код-рев'ю PR

**Файл:** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "license": "MIT"
}
```

**Файл:** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR Review

This command initiates a complete pull request review including:

1. Security analysis
2. Test coverage verification
3. Documentation updates
4. Code quality checks
5. Performance impact assessment
```

**Файл:** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: read, grep, diff
---

# Security Reviewer

Specializes in finding security vulnerabilities:
- Authentication/authorization issues
- Data exposure
- Injection attacks
- Secure configuration
```

**Встановлення:**

```bash
/plugin install pr-review

# Result:
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

#### Приклад 2: Плагін DevOps

**Компоненти:**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

#### Приклад 3: Плагін документації

**Комплектні компоненти:**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

### Маркетплейс плагінів

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>Anthropic"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Registry"]

    A --> B
    A --> C
    A --> D

    B -->|Categories| B1["Development"]
    B -->|Categories| B2["DevOps"]
    B -->|Categories| B3["Documentation"]

    C -->|Search| C1["DevOps Automation"]
    C -->|Search| C2["Mobile Dev"]
    C -->|Search| C3["Data Science"]

    D -->|Internal| D1["Company Standards"]
    D -->|Internal| D2["Legacy Systems"]
    D -->|Internal| D3["Compliance"]
```

### Встановлення та життєвий цикл плагіна

```mermaid
graph LR
    A["Discover"] -->|Browse| B["Marketplace"]
    B -->|Select| C["Plugin Page"]
    C -->|View| D["Components"]
    D -->|Install| E["/plugin install"]
    E -->|Extract| F["Configure"]
    F -->|Activate| G["Use"]
    G -->|Check| H["Update"]
    H -->|Available| G
    G -->|Done| I["Disable"]
    I -->|Later| J["Enable"]
    J -->|Back| G
```

### Порівняння функцій плагінів

| Функція | Слеш-команда | Навичка | Субагент | Плагін |
|---------|---------------|-------|----------|--------|
| **Встановлення** | Ручне копіювання | Ручне копіювання | Ручна конфігурація | Одна команда |
| **Час налаштування** | 5 хвилин | 10 хвилин | 15 хвилин | 2 хвилини |
| **Комплектність** | Один файл | Один файл | Один файл | Кілька |
| **Версіонування** | Вручну | Вручну | Вручну | Автоматичне |
| **Поширення в команді** | Копіювати файл | Копіювати файл | Копіювати файл | ID встановлення |
| **Оновлення** | Вручну | Вручну | Вручну | Авто-доступне |
| **Залежності** | Немає | Немає | Немає | Можуть бути |
| **Маркетплейс** | Ні | Ні | Ні | Так |
| **Дистрибуція** | Репозиторій | Репозиторій | Репозиторій | Маркетплейс |

### Сценарії використання плагінів

| Сценарій використання | Рекомендація | Чому |
|----------|-----------------|-----|
| **Онбординг команди** | ✅ Використовуйте плагін | Миттєве налаштування, усі конфігурації |
| **Налаштування фреймворку** | ✅ Використовуйте плагін | Комплектує команди, специфічні для фреймворку |
| **Корпоративні стандарти** | ✅ Використовуйте плагін | Централізована дистрибуція, контроль версій |
| **Швидка автоматизація задач** | ❌ Використовуйте команду | Надмірна складність |
| **Одна предметна область** | ❌ Використовуйте навичку | Занадто важкий, краще навичка |
| **Спеціалізований аналіз** | ❌ Використовуйте субагента | Створіть вручну або використовуйте навичку |
| **Доступ до живих даних** | ❌ Використовуйте MCP | Автономний, не комплектуйте |

### Коли створювати плагін

```mermaid
graph TD
    A["Should I create a plugin?"]
    A -->|Need multiple components| B{"Multiple commands<br/>or subagents<br/>or MCPs?"}
    B -->|Yes| C["✅ Create Plugin"]
    B -->|No| D["Use Individual Feature"]
    A -->|Team workflow| E{"Share with<br/>team?"}
    E -->|Yes| C
    E -->|No| F["Keep as Local Setup"]
    A -->|Complex setup| G{"Needs auto<br/>configuration?"}
    G -->|Yes| C
    G -->|No| D
```

### Публікація плагіна

**Кроки для публікації:**

1. Створіть структуру плагіна з усіма компонентами
2. Напишіть маніфест `.claude-plugin/plugin.json`
3. Створіть `README.md` з документацією
4. Протестуйте локально за допомогою `/plugin install ./my-plugin`
5. Надішліть на маркетплейс плагінів
6. Пройдіть перевірку та затвердження
7. Опубліковано на маркетплейсі
8. Користувачі можуть встановити однією командою

**Приклад подачі:**

~~~~markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 slash commands for different review types
- 3 specialized subagents
- GitHub and CodeQL MCP integration
- Automated security scanning hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 1.0+
- GitHub access
- CodeQL (optional)
~~~~

### Плагін проти ручної конфігурації

**Ручне налаштування (2+ години):**
- Встановити слеш-команди одну за одною
- Створити субагентів окремо
- Налаштувати MCP окремо
- Налаштувати хуки вручну
- Задокументувати все
- Поширити в команді (сподіваючись на правильну конфігурацію)

**З плагіном (2 хвилини):**
```bash
/plugin install pr-review
# ✅ Everything installed and configured
# ✅ Ready to use immediately
# ✅ Team can reproduce exact setup
```

---

## Порівняння та інтеграція

### Матриця порівняння функцій

| Функція | Виклик | Постійність | Область | Сценарій використання |
|---------|-----------|------------|-------|----------|
| **Слеш-команди** | Ручний (`/cmd`) | Лише сесія | Одна команда | Швидкі ярлики |
| **Субагенти** | Авто-делеговані | Ізольований контекст | Спеціалізоване завдання | Розподіл завдань |
| **Пам'ять** | Авто-завантажена | Між сесіями | Контекст користувача/команди | Довгострокове навчання |
| **Протокол MCP** | Авто-запити | Реальний час, зовнішній | Доступ до живих даних | Динамічна інформація |
| **Навички** | Авто-викликані | На основі файлової системи | Повторно використовувана експертиза | Автоматизовані робочі процеси |

### Хронологія взаємодії

```mermaid
graph LR
    A["Session Start"] -->|Load| B["Memory (CLAUDE.md)"]
    B -->|Discover| C["Available Skills"]
    C -->|Register| D["Slash Commands"]
    D -->|Connect| E["MCP Servers"]
    E -->|Ready| F["User Interaction"]

    F -->|Type /cmd| G["Slash Command"]
    F -->|Request| H["Skill Auto-Invoke"]
    F -->|Query| I["MCP Data"]
    F -->|Complex task| J["Delegate to Subagent"]

    G -->|Uses| B
    H -->|Uses| B
    I -->|Uses| B
    J -->|Uses| B
```

### Практичний приклад інтеграції: Автоматизація підтримки клієнтів

#### Архітектура

```mermaid
graph TB
    User["Customer Email"] -->|Receives| Router["Support Router"]

    Router -->|Analyze| Memory["Memory<br/>Customer history"]
    Router -->|Lookup| MCP1["MCP: Customer DB<br/>Previous tickets"]
    Router -->|Check| MCP2["MCP: Slack<br/>Team status"]

    Router -->|Route Complex| Sub1["Subagent: Tech Support<br/>Context: Technical issues"]
    Router -->|Route Simple| Sub2["Subagent: Billing<br/>Context: Payment issues"]
    Router -->|Route Urgent| Sub3["Subagent: Escalation<br/>Context: Priority handling"]

    Sub1 -->|Format| Skill1["Skill: Response Generator<br/>Brand voice maintained"]
    Sub2 -->|Format| Skill2["Skill: Response Generator"]
    Sub3 -->|Format| Skill3["Skill: Response Generator"]

    Skill1 -->|Generate| Output["Formatted Response"]
    Skill2 -->|Generate| Output
    Skill3 -->|Generate| Output

    Output -->|Post| MCP3["MCP: Slack<br/>Notify team"]
    Output -->|Send| Reply["Customer Reply"]
```

#### Потік запитів

```markdown
## Customer Support Request Flow

### 1. Incoming Email
"I'm getting error 500 when trying to upload files. This is blocking my workflow!"

### 2. Memory Lookup
- Loads CLAUDE.md with support standards
- Checks customer history: VIP customer, 3rd incident this month

### 3. MCP Queries
- GitHub MCP: List open issues (finds related bug report)
- Database MCP: Check system status (no outages reported)
- Slack MCP: Check if engineering is aware

### 4. Skill Detection & Loading
- Request matches "Technical Support" skill
- Loads support response template from Skill

### 5. Subagent Delegation
- Routes to Tech Support Subagent
- Provides context: customer history, error details, known issues
- Subagent has full access to: read, bash, grep tools

### 6. Subagent Processing
Tech Support Subagent:
- Searches codebase for 500 error in file upload
- Finds recent change in commit 8f4a2c
- Creates workaround documentation

### 7. Skill Execution
Response Generator Skill:
- Uses Brand Voice guidelines
- Formats response with empathy
- Includes workaround steps
- Links to related documentation

### 8. MCP Output
- Posts update to #support Slack channel
- Tags engineering team
- Updates ticket in Jira MCP

### 9. Response
Customer receives:
- Empathetic acknowledgment
- Explanation of cause
- Immediate workaround
- Timeline for permanent fix
- Link to related issues
```

### Повна оркестрація функцій

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: Request: "Build auth system"
    Claude->>Memory: Load project standards
    Memory-->>Claude: Auth standards, team practices
    Claude->>MCP: Query GitHub for similar implementations
    MCP-->>Claude: Code examples, best practices
    Claude->>Skills: Detect matching Skills
    Skills-->>Claude: Security Review Skill + Testing Skill
    Claude->>SubAgent: Delegate implementation
    SubAgent->>SubAgent: Build feature
    Claude->>Skills: Apply Security Review Skill
    Skills-->>Claude: Security checklist results
    Claude->>SubAgent: Delegate testing
    SubAgent-->>Claude: Test results
    Claude->>User: Complete system delivered
```

### Коли використовувати кожну функцію

```mermaid
graph TD
    A["New Task"] --> B{Type of Task?}

    B -->|Repeated workflow| C["Slash Command"]
    B -->|Need real-time data| D["MCP Protocol"]
    B -->|Remember for next time| E["Memory"]
    B -->|Specialized subtask| F["Subagent"]
    B -->|Domain-specific work| G["Skill"]

    C --> C1["✅ Team shortcut"]
    D --> D1["✅ Live API access"]
    E --> E1["✅ Persistent context"]
    F --> F1["✅ Parallel execution"]
    G --> G1["✅ Auto-invoked expertise"]
```

### Дерево рішень для вибору

```mermaid
graph TD
    Start["Need to extend Claude?"]

    Start -->|Quick repeated task| A{"Manual or Auto?"}
    A -->|Manual| B["Slash Command"]
    A -->|Auto| C["Skill"]

    Start -->|Need external data| D{"Real-time?"}
    D -->|Yes| E["MCP Protocol"]
    D -->|No/Cross-session| F["Memory"]

    Start -->|Complex project| G{"Multiple roles?"}
    G -->|Yes| H["Subagents"]
    G -->|No| I["Skills + Memory"]

    Start -->|Long-term context| J["Memory"]
    Start -->|Team workflow| K["Slash Command +<br/>Memory"]
    Start -->|Full automation| L["Skills +<br/>Subagents +<br/>MCP"]
```

---

## Зведена таблиця

| Аспект | Слеш-команди | Субагенти | Пам'ять | MCP | Навички | Плагіни |
|--------|---|---|---|---|---|---|
| **Складність налаштування** | Легко | Середньо | Легко | Середньо | Середньо | Легко |
| **Крива навчання** | Низька | Середня | Низька | Середня | Середня | Низька |
| **Користь для команди** | Висока | Висока | Середня | Висока | Висока | Дуже висока |
| **Рівень автоматизації** | Низький | Високий | Середній | Високий | Високий | Дуже високий |
| **Управління контекстом** | Одна сесія | Ізольований | Постійний | Реальний час | Постійний | Усі функції |
| **Навантаження з обслуговування** | Низьке | Середнє | Низьке | Середнє | Середнє | Низьке |
| **Масштабованість** | Добра | Відмінна | Добра | Відмінна | Відмінна | Відмінна |
| **Можливість поширення** | Задовільна | Задовільна | Добра | Добра | Добра | Відмінна |
| **Версіонування** | Вручну | Вручну | Вручну | Вручну | Вручну | Автоматичне |
| **Встановлення** | Ручне копіювання | Ручна конфігурація | Н/Д | Ручна конфігурація | Ручне копіювання | Одна команда |

---

## Короткий посібник для початку

### Тиждень 1: Почніть просто
- Створіть 2-3 слеш-команди для типових завдань
- Увімкніть пам'ять у налаштуваннях
- Задокументуйте стандарти команди в CLAUDE.md

### Тиждень 2: Додайте доступ у реальному часі
- Налаштуйте 1 MCP (GitHub або Database)
- Використовуйте `/mcp` для конфігурації
- Запитуйте живі дані у ваших робочих процесах

### Тиждень 3: Розподіліть роботу
- Створіть першого субагента для конкретної ролі
- Використовуйте команду `/agents`
- Протестуйте делегування з простим завданням

### Тиждень 4: Автоматизуйте все
- Створіть першу навичку для повторюваної автоматизації
- Використовуйте маркетплейс навичок або створіть власну
- Об'єднайте усі функції для повного робочого процесу

### Постійно
- Переглядайте та оновлюйте пам'ять щомісяця
- Додавайте нові навички за потребою
- Оптимізуйте MCP-запити
- Вдосконалюйте промпти субагентів

---

## Хуки

### Огляд

Хуки — це shell-команди на основі подій, які виконуються автоматично у відповідь на події Claude Code. Вони забезпечують автоматизацію, валідацію та користувацькі робочі процеси без ручного втручання.

### Події хуків

Claude Code підтримує **25 подій хуків** у чотирьох типах хуків (command, http, prompt, agent):

| Подія хука | Тригер | Сценарії використання |
|------------|---------|-----------|
| **SessionStart** | Початок/відновлення/очищення/ущільнення сесії | Налаштування середовища, ініціалізація |
| **InstructionsLoaded** | Завантажено CLAUDE.md або файл правил | Валідація, трансформація, доповнення |
| **UserPromptSubmit** | Користувач надсилає промпт | Валідація вводу, фільтрація промптів |
| **PreToolUse** | Перед запуском будь-якого інструменту | Валідація, шлюзи затвердження, логування |
| **PermissionRequest** | Показано діалог дозволу | Авто-затвердження/відхилення |
| **PostToolUse** | Після успішного виконання інструменту | Авто-форматування, сповіщення, очищення |
| **PostToolUseFailure** | Помилка виконання інструменту | Обробка помилок, логування |
| **Notification** | Надіслано сповіщення | Алертинг, зовнішні інтеграції |
| **SubagentStart** | Створено субагента | Ін'єкція контексту, ініціалізація |
| **SubagentStop** | Субагент завершив роботу | Валідація результату, логування |
| **Stop** | Claude завершив відповідь | Генерація підсумку, завдання очищення |
| **StopFailure** | Помилка API завершує хід | Відновлення після помилки, логування |
| **TeammateIdle** | Тімейт у команді агентів без роботи | Розподіл роботи, координація |
| **TaskCompleted** | Завдання позначено як виконане | Пост-обробка завдання |
| **TaskCreated** | Завдання створено через TaskCreate | Відстеження завдань, логування |
| **ConfigChange** | Зміна конфігураційного файлу | Валідація, поширення |
| **CwdChanged** | Зміна робочого каталогу | Налаштування для конкретного каталогу |
| **FileChanged** | Зміна відстежуваного файлу | Моніторинг файлів, тригери перебудови |
| **PreCompact** | Перед ущільненням контексту | Збереження стану |
| **PostCompact** | Після завершення ущільнення | Дії після ущільнення |
| **WorktreeCreate** | Створення worktree | Налаштування середовища, встановлення залежностей |
| **WorktreeRemove** | Видалення worktree | Очищення, звільнення ресурсів |
| **Elicitation** | MCP-сервер запитує введення користувача | Валідація вводу |
| **ElicitationResult** | Користувач відповідає на запит | Обробка відповіді |
| **SessionEnd** | Завершення сесії | Очищення, фінальне логування |

### Типові хуки

Хуки налаштовуються у `~/.claude/settings.json` (рівень користувача) або `.claude/settings.json` (рівень проєкту):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "eslint $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### Змінні середовища хуків

- `$CLAUDE_FILE_PATH` — Шлях до файлу, що редагується/записується
- `$CLAUDE_TOOL_NAME` — Назва інструменту, що використовується
- `$CLAUDE_SESSION_ID` — Ідентифікатор поточної сесії
- `$CLAUDE_PROJECT_DIR` — Шлях до каталогу проєкту

### Найкращі практики

✅ **Рекомендовано:**
- Тримайте хуки швидкими (< 1 секунди)
- Використовуйте хуки для валідації та автоматизації
- Обробляйте помилки коректно
- Використовуйте абсолютні шляхи

❌ **Не рекомендовано:**
- Робити хуки інтерактивними
- Використовувати хуки для тривалих завдань
- Жорстко прописувати облікові дані

**Дивіться**: [06-hooks/](06-hooks/) для детальних прикладів

---

## Контрольні точки та відкат

### Огляд

Контрольні точки дозволяють зберігати стан розмови та повертатися до попередніх моментів, забезпечуючи безпечне експериментування та дослідження різних підходів.

### Ключові концепції

| Концепція | Опис |
|---------|-------------|
| **Контрольна точка** | Знімок стану розмови, включаючи повідомлення, файли та контекст |
| **Відкат** | Повернення до попередньої контрольної точки з відкиданням подальших змін |
| **Точка розгалуження** | Контрольна точка, від якої досліджуються кілька підходів |

### Доступ до контрольних точок

Контрольні точки створюються автоматично з кожним промптом користувача. Для відкату:

```bash
# Press Esc twice to open the checkpoint browser
Esc + Esc

# Or use the /rewind command
/rewind
```

При виборі контрольної точки доступні п'ять варіантів:
1. **Відновити код і розмову** — Повернути обидва до цього моменту
2. **Відновити розмову** — Повернути повідомлення, залишити поточний код
3. **Відновити код** — Повернути файли, залишити розмову
4. **Підсумувати звідси** — Стиснути розмову у підсумок
5. **Скасувати** — Відмінити

### Сценарії використання

| Сценарій | Робочий процес |
|----------|----------|
| **Дослідження підходів** | Зберегти → Спробувати A → Зберегти → Відкат → Спробувати B → Порівняти |
| **Безпечний рефакторинг** | Зберегти → Рефакторинг → Тест → Якщо невдача: Відкат |
| **A/B тестування** | Зберегти → Дизайн A → Зберегти → Відкат → Дизайн B → Порівняти |
| **Відновлення після помилки** | Помітити проблему → Відкат до останнього робочого стану |

### Конфігурація

```json
{
  "autoCheckpoint": true
}
```

**Дивіться**: [08-checkpoints/](08-checkpoints/) для детальних прикладів

---

## Просунуті функції

### Режим планування

Створюйте детальні плани реалізації перед кодуванням.

**Активація:**
```bash
/plan Implement user authentication system
```

**Переваги:**
- Чіткий план з оцінкою часу
- Оцінка ризиків
- Систематичне розбиття на завдання
- Можливість перегляду та модифікації

### Розширене мислення

Глибокий аналіз для складних проблем.

**Активація:**
- Перемикання `Alt+T` (або `Option+T` на macOS) під час сесії
- Встановіть змінну середовища `MAX_THINKING_TOKENS` для програмного контролю

```bash
# Enable extended thinking via environment variable
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**Переваги:**
- Ретельний аналіз компромісів
- Кращі архітектурні рішення
- Врахування крайніх випадків
- Систематична оцінка

### Фонові завдання

Запускайте тривалі операції без блокування розмови.

**Використання:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Режими дозволів

Контролюйте, що Claude може робити.

| Режим | Опис | Сценарій використання |
|------|-------------|----------|
| **default** | Стандартні дозволи з запитами для чутливих дій | Загальна розробка |
| **acceptEdits** | Автоматично приймати редагування файлів без підтвердження | Довірені робочі процеси редагування |
| **plan** | Лише аналіз і планування, без модифікації файлів | Код-рев'ю, планування архітектури |
| **auto** | Автоматично затверджувати безпечні дії, запитувати лише ризиковані | Збалансована автономія з безпекою |
| **dontAsk** | Виконувати всі дії без запитів підтвердження | Досвідчені користувачі, автоматизація |
| **bypassPermissions** | Повний необмежений доступ, без перевірок безпеки | CI/CD-конвеєри, довірені скрипти |

**Використання:**
```bash
claude --permission-mode plan          # Read-only analysis
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions
claude --permission-mode dontAsk       # No confirmation prompts
```

### Headless-режим (режим друку)

Запускайте Claude Code без інтерактивного введення для автоматизації та CI/CD за допомогою прапорця `-p` (print).

**Використання:**
```bash
# Run specific task
claude -p "Run all tests"

# Pipe input for analysis
cat error.log | claude -p "explain this error"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# JSON output for scripting
claude -p --output-format json "list all functions in src/"
```

### Заплановані завдання

Запускайте завдання за розкладом за допомогою команди `/loop`.

**Використання:**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

Заплановані завдання виконуються у фоновому режимі та повідомляють про результати після завершення. Вони корисні для безперервного моніторингу, періодичних перевірок та автоматизованих робочих процесів обслуговування.

### Інтеграція з Chrome

Claude Code може інтегруватися з браузером Chrome для завдань веб-автоматизації. Це забезпечує можливості навігації по веб-сторінках, заповнення форм, створення знімків екрану та витягування даних з вебсайтів безпосередньо у вашому робочому процесі розробки.

### Управління сесіями

Керуйте кількома робочими сесіями.

**Команди:**
```bash
/resume                # Resume a previous conversation
/rename "Feature"      # Name the current session
/fork                  # Fork into a new session
claude -c              # Continue most recent conversation
claude -r "Feature"    # Resume session by name/ID
```

### Інтерактивні функції

**Клавіатурні скорочення:**
- `Ctrl + R` — Пошук в історії команд
- `Tab` — Автодоповнення
- `↑ / ↓` — Історія команд
- `Ctrl + L` — Очистити екран

**Багаторядковий ввід:**
```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

### Конфігурація

Повний приклад конфігурації:

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "default"
  }
}
```

**Дивіться**: [09-advanced-features/](09-advanced-features/) для повного посібника

---

## Ресурси

- [Документація Claude Code](https://code.claude.com/docs/en/overview)
- [Документація Anthropic](https://docs.anthropic.com)
- [MCP-сервери на GitHub](https://github.com/modelcontextprotocol/servers)
- [Кулінарна книга Anthropic](https://github.com/anthropics/anthropic-cookbook)

---

*Останнє оновлення: квітень 2026*
*Для Claude Haiku 4.5, Sonnet 4.6 та Opus 4.6*
*Тепер включає: хуки, контрольні точки, режим планування, розширене мислення, фонові завдання, режими дозволів (6 режимів), headless-режим, управління сесіями, авто-пам'ять, команди агентів, заплановані завдання, інтеграцію з Chrome, канали, голосовий ввід та комплектні навички*

---
**Last Updated**: April 9, 2026
**Claude Code Version**: 2.1.97
