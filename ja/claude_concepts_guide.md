<!-- i18n-source: claude_concepts_guide.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude コンセプト完全ガイド

スラッシュコマンド、サブエージェント、メモリ、MCP プロトコル、Agent Skills を、表・図・実例とともに包括的にまとめたリファレンスガイドである。

---

## 目次

1. [スラッシュコマンド](#スラッシュコマンド)
2. [サブエージェント](#サブエージェント)
3. [メモリ](#メモリ)
4. [MCP プロトコル](#mcp-プロトコル)
5. [Agent Skills](#agent-skills)
6. [プラグイン](#claude-code-プラグイン)
7. [フック](#フック)
8. [チェックポイントと巻き戻し](#チェックポイントと巻き戻し)
9. [高度な機能](#高度な機能)
10. [比較と統合](#比較と統合)

---

## スラッシュコマンド

### 概要

スラッシュコマンドは、ユーザーが呼び出すショートカットであり、Claude Code が実行できる Markdown ファイルとして保存される。チーム内で頻繁に使うプロンプトやワークフローを標準化するために用いる。

### アーキテクチャ

```mermaid
graph TD
    A["User Input: /command-name"] -->|Triggers| B["Search .claude/commands/"]
    B -->|Finds| C["command-name.md"]
    C -->|Loads| D["Markdown Content"]
    D -->|Executes| E["Claude Processes Prompt"]
    E -->|Returns| F["Result in Context"]
```

### ファイル構造

```mermaid
graph LR
    A["Project Root"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### コマンド配置の比較

| 配置場所 | スコープ | 利用可能範囲 | ユースケース | Git 管理 |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | プロジェクト固有 | チームメンバー | チームのワークフロー、共有標準 | ✅ あり |
| `~/.claude/commands/` | 個人 | ユーザー個人 | プロジェクト横断の個人ショートカット | ❌ なし |
| サブディレクトリ | 名前空間付き | 親ディレクトリに従う | カテゴリ別整理 | ✅ あり |

### 機能と利用シーン

| 機能 | 例 | 対応 |
|---------|---------|-----------|
| シェルスクリプト実行 | `bash scripts/deploy.sh` | ✅ あり |
| ファイル参照 | `@path/to/file.js` | ✅ あり |
| Bash 統合 | `$(git log --oneline)` | ✅ あり |
| 引数 | `/pr --verbose` | ✅ あり |
| MCP コマンド | `/mcp__github__list_prs` | ✅ あり |

### 実例

#### 例 1：コード最適化コマンド

**ファイル：** `.claude/commands/optimize.md`

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

**使い方：**
```bash
# Claude Code に入力
/optimize

# Claude がプロンプトを読み込み、コード入力を待つ
```

#### 例 2：プルリクエスト補助コマンド

**ファイル：** `.claude/commands/pr.md`

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

**使い方：**
```bash
/pr

# Claude がチェックリストを実行し PR を準備する
```

#### 例 3：階層型ドキュメント生成コマンド

**ファイル：** `.claude/commands/docs/generate-api-docs.md`

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

### コマンドのライフサイクル図

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

### ベストプラクティス

| ✅ 推奨 | ❌ 非推奨 |
|------|---------|
| 明確で動作指向の名前を付ける | 一度しか使わない作業をコマンド化する |
| description にトリガー語を記述する | コマンド内に複雑なロジックを組み込む |
| 1 タスクに焦点を絞る | 重複したコマンドを作る |
| プロジェクトコマンドはバージョン管理する | 機密情報をハードコードする |
| サブディレクトリで整理する | 長大なコマンド一覧を作る |
| シンプルで読みやすいプロンプトを書く | 略語や難解な表現を使う |

---

## サブエージェント

### 概要

サブエージェントは、独立したコンテキストウィンドウとカスタマイズされたシステムプロンプトを持つ専門 AI アシスタントである。関心の分離を保ったままタスクの委譲を可能にする。

### アーキテクチャ図

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

### サブエージェントのライフサイクル

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

### サブエージェント設定項目

| 設定項目 | 型 | 用途 | 例 |
|---------------|------|---------|---------|
| `name` | 文字列 | エージェントの識別子 | `code-reviewer` |
| `description` | 文字列 | 用途とトリガー語 | `Comprehensive code quality analysis` |
| `tools` | リスト / 文字列 | 利用可能なツール | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | 振る舞いの指示 | カスタムガイドライン |

### ツールアクセスの階層

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

### 実例

#### 例 1：完全なサブエージェント設定

**ファイル：** `.claude/agents/code-reviewer.md`

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

**ファイル：** `.claude/agents/test-engineer.md`

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

**ファイル：** `.claude/agents/documentation-writer.md`

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

#### 例 2：サブエージェント委譲の実例

```markdown
# シナリオ：決済機能の構築

## ユーザーリクエスト
「Stripe と統合した安全な決済処理機能を構築してほしい」

## メインエージェントのフロー

1. **計画フェーズ**
   - 要件を理解する
   - 必要なタスクを特定する
   - アーキテクチャを設計する

2. **コードレビュアー サブエージェントへ委譲**
   - タスク：「決済処理の実装をセキュリティ観点でレビューせよ」
   - コンテキスト：認証、API キー、トークン処理
   - レビュー対象：SQL インジェクション、キー漏洩、HTTPS 強制

3. **テストエンジニア サブエージェントへ委譲**
   - タスク：「決済フローの包括的なテストを作成せよ」
   - コンテキスト：成功・失敗・エッジケース
   - 作成するテスト：正常決済、カード拒否、ネットワーク障害、Webhook

4. **ドキュメントライター サブエージェントへ委譲**
   - タスク：「決済 API エンドポイントを文書化せよ」
   - コンテキスト：リクエスト・レスポンスのスキーマ
   - 成果物：curl 例とエラーコード付きの API ドキュメント

5. **統合**
   - メインエージェントが全ての出力を集約する
   - 結果を統合する
   - 完成したソリューションをユーザーに返す
```

#### 例 3：ツール権限のスコープ設定

**制限的な設定 — 特定コマンドのみ許可**

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

**拡張設定 — 実装用に全ツールを許可**

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

### サブエージェントのコンテキスト管理

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

### サブエージェントを使うべき場面

| シナリオ | サブエージェント利用 | 理由 |
|----------|--------------|-----|
| 多段階の複雑な機能 | ✅ あり | 関心を分離し、コンテキストの汚染を防ぐ |
| 簡単なコードレビュー | ❌ なし | オーバーヘッドに見合わない |
| 並列タスク実行 | ✅ あり | 各サブエージェントが独立したコンテキストを持つ |
| 専門知識が必要 | ✅ あり | カスタムシステムプロンプトを使える |
| 長時間の解析 | ✅ あり | メインコンテキストの枯渇を防ぐ |
| 単一タスク | ❌ なし | 不要なレイテンシを生む |

### Agent Teams

Agent Teams は、関連するタスクに取り組む複数のエージェントを協調動作させる。1 つずつサブエージェントへ委譲するのではなく、メインエージェントが複数のエージェント群をオーケストレーションし、中間結果を共有しつつ共通のゴールへ向かわせる。フロントエンドエージェント・バックエンドエージェント・テストエージェントが並行して動くフルスタック機能開発のような大規模タスクで有効である。

---

## メモリ

### 概要

メモリは、セッションや会話をまたいで Claude にコンテキストを保持させる仕組みである。形式は 2 種類あり、claude.ai での自動合成と、Claude Code でのファイルシステムベース CLAUDE.md である。

### メモリのアーキテクチャ

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

### Claude Code のメモリ階層（7 層）

Claude Code は 7 層からメモリを読み込む。優先度の高い順に：

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

### メモリ配置一覧

| 階層 | 配置場所 | スコープ | 優先度 | 共有 | 用途 |
|------|----------|-------|----------|--------|----------|
| 1. Managed Policy | エンタープライズ管理者 | 組織 | 最高 | 組織内全員 | コンプライアンス、セキュリティポリシー |
| 2. Project | `./CLAUDE.md` | プロジェクト | 高 | チーム（Git） | チーム標準、アーキテクチャ |
| 3. Project Rules | `.claude/rules/*.md` | プロジェクト | 高 | チーム（Git） | プロジェクト規約のモジュール化 |
| 4. User | `~/.claude/CLAUDE.md` | 個人 | 中 | 個人 | 個人の好み |
| 5. User Rules | `~/.claude/rules/*.md` | 個人 | 中 | 個人 | 個人ルールのモジュール化 |
| 6. Local | `.claude/local/CLAUDE.md` | ローカル | 低 | 共有しない | マシン固有設定 |
| 7. Auto Memory | 自動 | セッション | 最低 | 個人 | 学習された好み・パターン |

### Auto Memory

Auto Memory は、セッション中に観察されたユーザーの好みやパターンを自動的に取り込む。Claude はやり取りから学習し、次のような情報を覚える：

- コーディングスタイルの好み
- ユーザーがよく行う訂正
- フレームワーク・ツールの選択
- コミュニケーションスタイルの好み

Auto Memory はバックグラウンドで動き、手動の設定は不要である。

### メモリ更新のライフサイクル

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

### 実例

#### 例 1：プロジェクトメモリの構造

**ファイル：** `./CLAUDE.md`

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

#### 例 2：ディレクトリ別メモリ

**ファイル：** `./src/api/CLAUDE.md`

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

#### 例 3：個人メモリ

**ファイル：** `~/.claude/CLAUDE.md`

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

#### 例 4：セッション中のメモリ更新

**セッション中のやり取り：**

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

### Claude Web / Desktop でのメモリ

#### メモリ合成のタイムライン

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**メモリ要約の例：**

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

### メモリ機能の比較

| 機能 | Claude Web / Desktop | Claude Code（CLAUDE.md） |
|---------|-------------------|------------------------|
| 自動合成 | ✅ 24 時間ごと | ❌ 手動 |
| プロジェクト横断 | ✅ 共有 | ❌ プロジェクト固有 |
| チームアクセス | ✅ 共有プロジェクト | ✅ Git 管理 |
| 検索可能 | ✅ 標準機能 | ✅ `/memory` 経由 |
| 編集可能 | ✅ チャット内 | ✅ ファイル直接編集 |
| インポート / エクスポート | ✅ 可 | ✅ コピー & ペースト |
| 永続性 | ✅ 24 時間以上 | ✅ 無期限 |

---

## MCP プロトコル

### 概要

MCP（Model Context Protocol）は、Claude が外部ツール・API・リアルタイムデータソースへアクセスするための標準化された方式である。メモリと違い、MCP は変化するデータへのライブアクセスを提供する。

### MCP のアーキテクチャ

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

### MCP のエコシステム

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

### MCP のセットアップ手順

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

### 利用可能な MCP サーバー一覧

| MCP サーバー | 用途 | 主なツール | 認証 | リアルタイム |
|------------|---------|--------------|------|-----------|
| **Filesystem** | ファイル操作 | read, write, delete | OS 権限 | ✅ あり |
| **GitHub** | リポジトリ管理 | list_prs, create_issue, push | OAuth | ✅ あり |
| **Slack** | チームコミュニケーション | send_message, list_channels | トークン | ✅ あり |
| **Database** | SQL クエリ | query, insert, update | 認証情報 | ✅ あり |
| **Google Docs** | ドキュメントアクセス | read, write, share | OAuth | ✅ あり |
| **Asana** | プロジェクト管理 | create_task, update_status | API キー | ✅ あり |
| **Stripe** | 決済データ | list_charges, create_invoice | API キー | ✅ あり |
| **Memory** | 永続メモリ | store, retrieve, delete | ローカル | ❌ なし |

### 実例

#### 例 1：GitHub MCP の設定

**ファイル：** `.mcp.json`（プロジェクトスコープ）または `~/.claude.json`（ユーザースコープ）

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

**利用可能な GitHub MCP ツール：**

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

#### 例 2：Database MCP の設定

**設定：**

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

**利用例：**

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

#### 例 3：複数 MCP を組み合わせたワークフロー

**シナリオ：日次レポートの生成**

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

#### 例 4：Filesystem MCP の操作

**設定：**

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

**利用可能な操作：**

| 操作 | コマンド | 用途 |
|-----------|---------|---------|
| ファイル一覧 | `ls ~/projects` | ディレクトリ内容を表示 |
| ファイル読み込み | `cat src/main.ts` | 内容を読む |
| ファイル作成 | `create docs/api.md` | 新規ファイル作成 |
| ファイル編集 | `edit src/app.ts` | ファイルを変更 |
| 検索 | `grep "async function"` | ファイル内検索 |
| 削除 | `rm old-file.js` | ファイル削除 |

### MCP vs メモリ：判断マトリクス

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

### リクエスト・レスポンスのパターン

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

## Agent Skills

### 概要

Agent Skills は、命令・スクリプト・リソースをフォルダに同梱した、再利用可能でモデルが自律的に呼び出す能力である。Claude は関連するスキルを自動検出して利用する。

### スキルのアーキテクチャ

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

### スキルの読み込み手順

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

### スキルの種類と配置

| 種類 | 配置場所 | スコープ | 共有 | 同期 | 用途 |
|------|----------|-------|--------|------|----------|
| プリビルト | 組み込み | グローバル | 全ユーザー | 自動 | ドキュメント生成 |
| 個人 | `~/.claude/skills/` | 個人 | なし | 手動 | 個人の自動化 |
| プロジェクト | `.claude/skills/` | チーム | あり | Git | チーム標準 |
| プラグイン | プラグイン経由 | 状況による | 状況による | 自動 | 統合機能 |

### プリビルトスキル

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

### 同梱スキル

Claude Code には標準で 5 つの同梱スキルが含まれる：

| スキル | コマンド | 用途 |
|-------|---------|---------|
| **Simplify** | `/simplify` | 複雑なコードや説明を単純化 |
| **Batch** | `/batch` | 複数ファイル・項目に対する一括操作 |
| **Debug** | `/debug` | 根本原因分析を伴う体系的デバッグ |
| **Loop** | `/loop` | タイマーで定期実行 |
| **Claude API** | `/claude-api` | Anthropic API への直接アクセス |

これらの同梱スキルは常に利用可能であり、インストールや設定は不要である。

### 実例

#### 例 1：カスタムコードレビュースキル

**ディレクトリ構成：**

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

**ファイル：** `~/.claude/skills/code-review/SKILL.md`

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

## Python スクリプト：analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """コードの一般的なメトリクスを解析する。"""

    # 関数数をカウント
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # クラス数をカウント
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # 平均行長
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # 複雑度の概算
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

## Python スクリプト：compare-complexity.py

```python
#!/usr/bin/env python3
"""
変更前後でコードのサイクロマティック複雑度を比較する。
リファクタリングが実際に構造を単純化しているか確認するのに役立つ。
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """コードの複雑度メトリクスを解析する。"""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        McCabe の方式でサイクロマティック複雑度を計算する。
        判定点をカウント：if, elif, else, for, while, except, and, or
        """
        complexity = 1  # 基本複雑度

        # 判定点をカウント
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
        認知的複雑度を計算する — 理解の難しさ。
        ネストの深さと制御フローに基づく。
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # ネスト深度を追跡
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # インデント解除でネストを減らす
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        保守性指数（0〜100）。
        > 85: 優秀
        > 65: 良好
        > 50: 普通
        < 50: 不良
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # 簡略化した MI 計算
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """包括的な複雑度レポートを生成する。"""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """2 つのコードバージョンの複雑度メトリクスを比較する。"""

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

## テンプレート：review-checklist.md

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

## テンプレート：finding-template.md

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
// N+1 クエリ問題を示す
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // ユーザーごとにクエリ！
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// JOIN クエリで最適化
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

## 利用例

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

#### 例 2：ブランドボイス スキル

**ディレクトリ構成：**

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

**ファイル：** `.claude/skills/brand-voice/SKILL.md`

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
## 例

### ✅ 良い例
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

なぜ機能するか：明確な価値、具体的なベネフィット、行動指向

### ❌ 悪い例
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

なぜダメか：曖昧、企業的ジャーゴン、具体的な価値がない

## テンプレート：メール

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

## テンプレート：SNS

```
[Hook: Grab attention in first line]
[2-3 lines: Value or interesting fact]
[Call to action: Link, question, or engagement]
[Emoji: 1-2 max for visual interest]
```

## ファイル：tone-examples.md
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

#### 例 3：ドキュメント生成スキル

**ファイル：** `.claude/skills/doc-generator/SKILL.md`

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
### スキルの検出と起動

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

### スキルと他機能の比較

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

## Claude Code プラグイン

### 概要

Claude Code プラグインは、カスタマイズ（スラッシュコマンド、サブエージェント、MCP サーバー、フック）をひとつにまとめたパッケージで、コマンド 1 つでインストールできる。複数の機能を凝集した共有可能なパッケージにまとめる、最上位の拡張機構である。

### アーキテクチャ

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

### プラグインの読み込み手順

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

### プラグインの種類と配布

| 種類 | スコープ | 共有 | 提供元 | 例 |
|------|-------|--------|-----------|----------|
| Official | グローバル | 全ユーザー | Anthropic | PR Review、Security Guidance |
| Community | 公開 | 全ユーザー | コミュニティ | DevOps、Data Science |
| Organization | 社内 | チームメンバー | 企業 | 社内標準・ツール |
| Personal | 個人 | 個人のみ | 開発者 | カスタムワークフロー |

### プラグイン定義の構造

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT

# プラグインのメタデータ
tags:
  - category
  - use-case

# 要件
requires:
  - claude-code: ">=1.0.0"

# 同梱コンポーネント
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# 設定
config:
  auto_load: true
  enabled_by_default: true
---
```

### プラグインのディレクトリ構造

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

### 実例

#### 例 1：PR レビュープラグイン

**ファイル：** `.claude-plugin/plugin.json`

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

**ファイル：** `commands/review-pr.md`

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

**ファイル：** `agents/security-reviewer.md`

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

**インストール：**

```bash
/plugin install pr-review

# 結果：
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

#### 例 2：DevOps プラグイン

**コンポーネント：**

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

#### 例 3：ドキュメント プラグイン

**同梱コンポーネント：**

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

### プラグインマーケットプレイス

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

### プラグインのインストールとライフサイクル

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

### プラグインの機能比較

| 機能 | スラッシュコマンド | スキル | サブエージェント | プラグイン |
|---------|---------------|-------|----------|--------|
| **インストール** | 手動コピー | 手動コピー | 手動設定 | 1 コマンド |
| **セットアップ時間** | 5 分 | 10 分 | 15 分 | 2 分 |
| **バンドル** | 単一ファイル | 単一ファイル | 単一ファイル | 複数 |
| **バージョン管理** | 手動 | 手動 | 手動 | 自動 |
| **チーム共有** | ファイルコピー | ファイルコピー | ファイルコピー | インストール ID |
| **更新** | 手動 | 手動 | 手動 | 自動更新可 |
| **依存関係** | なし | なし | なし | 含む可能性 |
| **マーケットプレイス** | なし | なし | なし | あり |
| **配布** | リポジトリ | リポジトリ | リポジトリ | マーケットプレイス |

### プラグインのユースケース

| ユースケース | 推奨 | 理由 |
|----------|-----------------|-----|
| **チームのオンボーディング** | ✅ プラグイン推奨 | 即時セットアップ、設定一括 |
| **フレームワーク導入** | ✅ プラグイン推奨 | フレームワーク固有コマンドをまとめる |
| **エンタープライズ標準** | ✅ プラグイン推奨 | 中央配布、バージョン管理 |
| **簡単な作業の自動化** | ❌ コマンド推奨 | プラグインは過剰 |
| **単一ドメインの専門業務** | ❌ スキル推奨 | プラグインは重すぎる |
| **専門的な分析** | ❌ サブエージェント推奨 | 手動作成またはスキルで対応 |
| **ライブデータアクセス** | ❌ MCP 推奨 | 単独利用、バンドルしない |

### プラグイン作成の判断

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

### プラグインの公開

**公開手順：**

1. すべてのコンポーネントを含むプラグイン構造を作る
2. `.claude-plugin/plugin.json` マニフェストを記述する
3. ドキュメント付きの `README.md` を作る
4. `/plugin install ./my-plugin` でローカルテスト
5. プラグインマーケットプレイスへ提出する
6. レビューを受けて承認される
7. マーケットプレイスで公開される
8. ユーザーは 1 コマンドでインストールできる

**提出例：**

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

### プラグイン vs 手動設定

**手動セットアップ（2 時間以上）：**
- スラッシュコマンドを 1 つずつインストール
- サブエージェントを個別に作成
- MCP を個別に設定
- フックを手動で設定
- 全部を文書化
- チームに共有（正しく設定されることを祈る）

**プラグイン利用（2 分）：**
```bash
/plugin install pr-review
# ✅ すべてインストール・設定完了
# ✅ 即座に使える
# ✅ チームでも完全に同じ環境を再現可能
```

---

## 比較と統合

### 機能比較マトリクス

| 機能 | 起動方法 | 永続性 | スコープ | ユースケース |
|---------|-----------|------------|-------|----------|
| **スラッシュコマンド** | 手動（`/cmd`） | セッションのみ | 単一コマンド | クイックショートカット |
| **サブエージェント** | 自動委譲 | 独立コンテキスト | 専門タスク | タスク分担 |
| **メモリ** | 自動読み込み | セッション横断 | ユーザー / チーム文脈 | 長期学習 |
| **MCP プロトコル** | 自動クエリ | リアルタイム外部 | ライブデータアクセス | 動的情報 |
| **スキル** | 自動起動 | ファイルシステム | 再利用可能な専門性 | ワークフロー自動化 |

### 機能呼び出しのタイムライン

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

### 統合の実例：カスタマーサポート自動化

#### アーキテクチャ

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

#### リクエストの流れ

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

### 機能の総合オーケストレーション

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

### どの機能を使うか

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

### 選択フローチャート

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

## サマリー一覧

| 観点 | スラッシュコマンド | サブエージェント | メモリ | MCP | スキル | プラグイン |
|--------|---|---|---|---|---|---|
| **セットアップ難易度** | 易 | 中 | 易 | 中 | 中 | 易 |
| **学習曲線** | 低 | 中 | 低 | 中 | 中 | 低 |
| **チーム恩恵** | 高 | 高 | 中 | 高 | 高 | 非常に高 |
| **自動化レベル** | 低 | 高 | 中 | 高 | 高 | 非常に高 |
| **コンテキスト管理** | 単一セッション | 独立 | 永続 | リアルタイム | 永続 | 全機能 |
| **保守負担** | 低 | 中 | 低 | 中 | 中 | 低 |
| **スケーラビリティ** | 良 | 優 | 良 | 優 | 優 | 優 |
| **共有性** | 普 | 普 | 良 | 良 | 良 | 優 |
| **バージョン管理** | 手動 | 手動 | 手動 | 手動 | 手動 | 自動 |
| **インストール** | 手動コピー | 手動設定 | 不要 | 手動設定 | 手動コピー | 1 コマンド |

---

## クイックスタートガイド

### 第 1 週：シンプルに始める
- よく使う作業に対しスラッシュコマンドを 2〜3 個作成する
- 設定でメモリを有効化する
- チーム標準を CLAUDE.md に文書化する

### 第 2 週：リアルタイムアクセスを追加
- MCP を 1 つセットアップ（GitHub または Database）
- `/mcp` で設定する
- ワークフローでライブデータをクエリする

### 第 3 週：作業の分担
- 特定の役割を持つサブエージェントを最初に作る
- `/agents` コマンドを使う
- 簡単なタスクで委譲をテストする

### 第 4 週：すべてを自動化する
- 繰り返し作業に対しスキルを最初に作成する
- スキルマーケットプレイスを利用するか自作する
- 全機能を組み合わせて完全なワークフローを作る

### 継続的に
- 月次でメモリを見直し更新する
- 新しいパターンに気付いたらスキルを追加する
- MCP クエリを最適化する
- サブエージェントのプロンプトを精緻化する

---

## フック

### 概要

フックは、Claude Code のイベントに反応して自動実行されるシェルコマンドである。手動操作なしに自動化・検証・カスタムワークフローを実現する。

### フックイベント

Claude Code は 5 種類（command、http、mcp_tool、prompt、agent）にわたる **28 種類のフックイベント** をサポートする：

| フックイベント | トリガー | ユースケース |
|------------|---------|-----------|
| **SessionStart** | セッション開始 / 再開 / クリア / 圧縮時 | 環境構築、初期化 |
| **InstructionsLoaded** | CLAUDE.md やルールファイル読み込み時 | 検証、変換、補強 |
| **UserPromptSubmit** | ユーザーがプロンプト送信時 | 入力検証、プロンプトフィルタ |
| **PreToolUse** | 任意のツール実行前 | 検証、承認ゲート、ログ |
| **PermissionRequest** | 権限ダイアログ表示時 | 自動承認・拒否フロー |
| **PostToolUse** | ツール成功後 | 自動整形、通知、後処理 |
| **PostToolUseFailure** | ツール実行失敗時 | エラー処理、ログ |
| **Notification** | 通知送信時 | アラート、外部連携 |
| **SubagentStart** | サブエージェント生成時 | コンテキスト注入、初期化 |
| **SubagentStop** | サブエージェント終了時 | 結果検証、ログ |
| **Stop** | Claude の応答完了時 | サマリー生成、後処理 |
| **StopFailure** | API エラーでターン終了時 | エラー回復、ログ |
| **TeammateIdle** | エージェントチームのメンバーがアイドル時 | 作業分配、調整 |
| **TaskCompleted** | タスク完了時 | 後続処理 |
| **TaskCreated** | TaskCreate でタスク作成時 | タスク追跡、ログ |
| **ConfigChange** | 設定ファイル変更時 | 検証、伝播 |
| **CwdChanged** | 作業ディレクトリ変更時 | ディレクトリ別セットアップ |
| **FileChanged** | 監視対象ファイルの変更時 | ファイル監視、再ビルド |
| **PreCompact** | コンテキスト圧縮直前 | 状態の保存 |
| **PostCompact** | 圧縮完了後 | 圧縮後の処理 |
| **WorktreeCreate** | ワークツリー作成時 | 環境構築、依存関係インストール |
| **WorktreeRemove** | ワークツリー削除時 | クリーンアップ、リソース解放 |
| **Elicitation** | MCP サーバーがユーザー入力を要求時 | 入力検証 |
| **ElicitationResult** | ユーザーが入力要求に応答時 | 応答処理 |
| **SessionEnd** | セッション終了時 | クリーンアップ、最終ログ |

### よくあるフック

フックは `~/.claude/settings.json`（ユーザーレベル）または `.claude/settings.json`（プロジェクトレベル）に設定する：

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

### フック環境変数

- `$CLAUDE_FILE_PATH` — 編集・書き込み中のファイルパス
- `$CLAUDE_TOOL_NAME` — 使用中のツール名
- `$CLAUDE_SESSION_ID` — 現在のセッション ID
- `$CLAUDE_PROJECT_DIR` — プロジェクトディレクトリのパス

### ベストプラクティス

✅ **推奨：**
- フックは高速にする（1 秒以内）
- 検証や自動化に使う
- エラーを丁寧に処理する
- 絶対パスを使う

❌ **非推奨：**
- フックを対話的にする
- 長時間タスクをフックで実行する
- 認証情報をハードコードする

**詳細：** [06-hooks/](../06-hooks/)

---

## チェックポイントと巻き戻し

### 概要

チェックポイントは会話の状態を保存し、過去の地点へ巻き戻すことを可能にする。複数のアプローチを安全に試行・検討できる。

### 主要概念

| 概念 | 説明 |
|---------|-------------|
| **チェックポイント** | メッセージ、ファイル、コンテキストを含む会話状態のスナップショット |
| **巻き戻し** | 過去のチェックポイントへ戻り、それ以降の変更を破棄 |
| **分岐点** | 複数アプローチを試すための起点となるチェックポイント |

### チェックポイントへのアクセス

チェックポイントはユーザープロンプトのたびに自動作成される。巻き戻すには：

```bash
# Esc を 2 回押すとチェックポイントブラウザが開く
Esc + Esc

# または /rewind コマンド
/rewind
```

チェックポイントを選ぶと 5 つのオプションから選択できる：
1. **コードと会話を復元** — 両方をその時点へ戻す
2. **会話を復元** — メッセージを巻き戻し、現在のコードは保つ
3. **コードを復元** — ファイルを戻し、会話は保つ
4. **ここから要約** — 会話を要約に圧縮
5. **キャンセル** — 取り消す

### ユースケース

| シナリオ | ワークフロー |
|----------|----------|
| **アプローチ比較** | 保存 → A 試行 → 保存 → 巻き戻し → B 試行 → 比較 |
| **安全なリファクタリング** | 保存 → リファクタ → テスト → 失敗時に巻き戻し |
| **A/B テスト** | 保存 → 設計 A → 保存 → 巻き戻し → 設計 B → 比較 |
| **ミス回復** | 問題発見 → 直前の正常状態へ巻き戻し |

### 設定

```json
{
  "autoCheckpoint": true
}
```

**詳細：** [08-checkpoints/](../08-checkpoints/)

---

## 高度な機能

### プラニングモード

実装前に詳細な計画を作成する。

**起動：**
```bash
/plan Implement user authentication system
```

**メリット：**
- 工数見積もり付きの明確なロードマップ
- リスク評価
- 体系的なタスク分割
- レビューと修正の機会

### 拡張思考（Extended Thinking）

複雑な問題に対する深い推論。

**起動：**
- セッション中に `Alt+T`（macOS では `Option+T`）でトグル
- プログラム制御には環境変数 `MAX_THINKING_TOKENS` を設定

```bash
# 環境変数で拡張思考を有効化
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**メリット：**
- トレードオフを徹底分析
- より良いアーキテクチャ判断
- エッジケースの考慮
- 体系的な評価

### バックグラウンドタスク

会話をブロックせずに長時間処理を実行する。

**使い方：**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # 全タスク一覧
/task status bg-1234 # 進捗確認
/task show bg-1234   # 出力閲覧
/task cancel bg-1234 # タスクキャンセル
```

### 権限モード

Claude にできることを制御する。

| モード | 説明 | ユースケース |
|------|-------------|----------|
| **default** | 標準権限。機微な操作はプロンプト | 一般開発 |
| **acceptEdits** | ファイル編集を確認なく承認 | 信頼できる編集ワークフロー |
| **plan** | 解析・計画のみ、ファイル変更不可 | コードレビュー、アーキテクチャ計画 |
| **auto** | 安全な操作は自動承認、リスクのみ確認 | 安全性とのバランス自律性 |
| **dontAsk** | すべての操作を確認なく実行 | 経験者、自動化 |
| **bypassPermissions** | 制限なし、安全チェックなし | CI/CD、信頼できるスクリプト |

**使い方：**
```bash
claude --permission-mode plan          # 読み取り専用解析
claude --permission-mode acceptEdits   # 編集を自動承認
claude --permission-mode auto          # 安全な操作を自動承認
claude --permission-mode dontAsk       # 確認プロンプトなし
```

### ヘッドレスモード（Print Mode）

`-p`（print）フラグで、対話入力なしの自動化や CI/CD 向けに Claude Code を実行する。

**使い方：**
```bash
# 特定タスクを実行
claude -p "Run all tests"

# 入力をパイプして解析
cat error.log | claude -p "explain this error"

# CI/CD 連携（GitHub Actions）
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# スクリプト用 JSON 出力
claude -p --output-format json "list all functions in src/"
```

### 定期タスク

`/loop` コマンドで定期実行する。

**使い方：**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

定期タスクはバックグラウンドで実行され、完了時に結果を報告する。継続監視、定期チェック、自動メンテナンスのワークフローに有用である。

### Chrome 連携

Claude Code は Chrome ブラウザと連携できる。Web ページのナビゲーション、フォーム入力、スクリーンショット撮影、サイトからのデータ抽出など、開発ワークフロー内で Web 自動化が可能になる。

### セッション管理

複数の作業セッションを管理する。

**コマンド：**
```bash
/resume                # 過去の会話を再開
/rename "Feature"      # 現在のセッションに名前を付ける
/fork                  # 新セッションへフォーク
claude -c              # 直近の会話を継続
claude -r "Feature"    # 名前 / ID でセッションを再開
```

### インタラクティブ機能

**キーボードショートカット：**
- `Ctrl + R` — コマンド履歴検索
- `Tab` — 自動補完
- `↑ / ↓` — コマンド履歴
- `Ctrl + L` — 画面クリア

**複数行入力：**
```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

### 設定

完全な設定例：

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

**詳細ガイド：** [09-advanced-features/](../09-advanced-features/)

---

## モデルと推論努力（Reasoning Effort）

Claude Code は推論努力を調整可能な 3 モデルをサポートする：

| モデル | コンテキストウィンドウ | 努力レベル | デフォルト努力（Claude Code） |
|-------|----------------|---------------|------------------------------|
| Claude Opus 4.7 | 1M トークン（ネイティブ） | `low`、`medium`、`high`、`xhigh`、`max` | `xhigh`（Opus 4.7 リリース時、2026-04-16 以降） |
| Claude Sonnet 4.6 | 1M トークン | `low`、`medium`、`high`、`max` | Pro/Max 加入者では `high`（v2.1.117 で `medium` から引き上げ） |
| Claude Haiku 4.5 | 200K トークン | `low`、`medium`、`high` | `medium` |

> **注：** v2.1.117 では、Opus 4.7 セッションで `/context` がネイティブの 1M ではなく 200K に対して計算されていたバグが修正された。Opus 4.7 で本来の 1M コンテキストを使うには v2.1.117 以降にアップグレードすること。

> **注：** v2.1.118 で `/cost` と `/stats` は `/usage` に統合された。`/usage` がコスト・統計などのタブを持つ正規コマンドとなり、`/cost` と `/stats` は対応するタブを開くショートカット別名として残されている。

## 参考資料

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Claude Code Changelog](https://code.claude.com/docs/en/changelog)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*最終更新：2026 年 4 月 24 日*
*対応：Claude Haiku 4.5、Sonnet 4.6、Opus 4.7*
*収録機能：フック、チェックポイント、プラニングモード、拡張思考、バックグラウンドタスク、権限モード（6 種）、ヘッドレスモード、セッション管理、Auto Memory、Agent Teams、定期タスク、Chrome 連携、Channels、音声入力、同梱スキル*

---
**最終更新：** 2026 年 4 月 24 日
**Claude Code バージョン：** 2.1.119
**出典：**
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://www.anthropic.com/news/claude-opus-4-7
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117

**対応モデル：** Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
