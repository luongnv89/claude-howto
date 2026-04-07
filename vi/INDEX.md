<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Các Ví Dụ Claude Code - Danh Mục Hoàn Chỉnh

Tài liệu này cung cấp danh mục hoàn chỉnh của tất cả các file ví dụ được tổ chức theo loại tính năng.

## Thống Kê Tóm Tắt

- **Tổng Số File**: 100+ files
- **Danh Mục**: 10 danh mục tính năng
- **Plugins**: 3 plugins hoàn chỉnh
- **Skills**: 6 skills hoàn chỉnh
- **Hooks**: 8 hooks ví dụ
- **Sẵn Sàng Sử Dụng**: Tất cả ví dụ

---

## 01. Lệnh Slash (10 files)

Các lệnh tắt do người dùng gọi cho các workflow phổ biến.

| File | Mô Tả | Use Case |
|------|-------------|----------|
| `optimize.md` | Trình phân tích tối ưu hóa code | Tìm vấn đề hiệu năng |
| `pr.md` | Chuẩn bị pull request | Tự động hóa workflow PR |
| `generate-api-docs.md` | Trình tạo tài liệu API | Tạo tài liệu API |
| `commit.md` | Trình hỗ trợ commit message | Commit chuẩn hóa |
| `setup-ci-cd.md` | Thiết lập pipeline CI/CD | Tự động hóa DevOps |
| `push-all.md` | Push tất cả thay đổi | Workflow push nhanh |
| `unit-test-expand.md` | Mở rộng độ phủ unit test | Tự động hóa test |
| `doc-refactor.md` | Tái cấu trúc tài liệu | Cải thiện tài liệu |
| `pr-slash-command.png` | Ví dụ screenshot | Tham khảo hình ảnh |
| `README.md` | Tài liệu | Hướng dẫn cài đặt và sử dụng |

**Đường Dẫn Cài Đặt**: `.claude/commands/`

**Cách Dùng**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Bộ Nhớ (6 files)

Ngữ cảnh lưu trữ và tiêu chuẩn dự án.

| File | Mô Tả | Phạm Vi | Vị Trí |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | Tiêu chuẩn dự án nhóm | Toàn dự án | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | Quy tắc cụ thể cho API | Thư mục | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Sở thích cá nhân | Người dùng | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Screenshot: bộ nhớ đã lưu | - | Tham khảo hình ảnh |
| `memory-ask-claude.png` | Screenshot: hỏi Claude | - | Tham khảo hình ảnh |
| `README.md` | Tài liệu | - | Tham khảo |

**Cài Đặt**: Sao chép đến vị trí phù hợp

**Cách Dùng**: Tự động tải bởi Claude

---

## 03. Skills (28 files)

Các khả năng tự động gọi với scripts và templates.

### Code Review Skill (5 files)
```
code-review/
├── SKILL.md                          # Định nghĩa skill
├── scripts/
│   ├── analyze-metrics.py            # Trình phân tích metrics code
│   └── compare-complexity.py         # So sánh độ phức tạp
└── templates/
    ├── review-checklist.md           # Checklist review
    └── finding-template.md           # Tài liệu phát hiện
```

**Mục Đích**: Review code toàn diện với phân tích bảo mật, hiệu năng, và chất lượng

**Tự Động Gọi**: Khi review code

---

### Brand Voice Skill (4 files)
```
brand-voice/
├── SKILL.md                          # Định nghĩa skill
├── templates/
│   ├── email-template.txt            # Định dạng email
│   └── social-post-template.txt      # Định dạng social media
└── tone-examples.md                  # Ví dụ tin nhắn
```

**Mục Đích**: Đảm bảo brand voice nhất quán trong communications

**Tự Động Gọi**: Khi tạo marketing copy

---

### Documentation Generator Skill (2 files)
```
doc-generator/
├── SKILL.md                          # Định nghĩa skill
└── generate-docs.py                  # Trình trích xuất doc Python
```

**Mục Đích**: Tạo tài liệu API toàn diện từ source code

**Tự Động Gọi**: Khi tạo/cập nhật tài liệu API

---

### Refactor Skill (5 files)
```
refactor/
├── SKILL.md                          # Định nghĩa skill
├── scripts/
│   ├── analyze-complexity.py         # Trình phân tích độ phức tạp
│   └── detect-smells.py              # Trình phát hiện code smells
├── references/
│   ├── code-smells.md                # Danh mục code smells
│   └── refactoring-catalog.md        # Patterns refactoring
└── templates/
    └── refactoring-plan.md           # Template kế hoạch refactoring
```

**Mục Đích**: Refactor code có hệ thống với phân tích độ phức tạp

**Tự Động Gọi**: Khi refactor code

---

### Claude MD Skill (1 file)
```
claude-md/
└── SKILL.md                          # Định nghĩa skill
```

**Mục Đích**: Quản lý và tối ưu hóa files CLAUDE.md

---

### Blog Draft Skill (3 files)
```
blog-draft/
├── SKILL.md                          # Định nghĩa skill
└── templates/
    ├── draft-template.md             # Template blog draft
    └── outline-template.md           # Template blog outline
```

**Mục Đích**: Soạn blog posts với cấu trúc nhất quán

**Plus**: `README.md` - Tổng quan skills và hướng dẫn sử dụng

**Đường Dẫn Cài Đặt**: `~/.claude/skills/` hoặc `.claude/skills/`

---

## 04. Tác Nhân Con (9 files)

Các trợ lý AI chuyên biệt với khả năng tùy chỉnh.

| File | Mô Tả | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | Phân tích chất lượng code | read, grep, diff, lint_runner | Review toàn diện |
| `test-engineer.md` | Phân tích độ phủ test | read, write, bash, grep | Tự động hóa test |
| `documentation-writer.md` | Tạo tài liệu | read, write, grep | Tạo tài liệu |
| `secure-reviewer.md` | Review bảo mật (read-only) | read, grep | Kiểm tra bảo mật |
| `implementation-agent.md` | Triển khai hoàn chỉnh | read, write, bash, grep, edit, glob | Phát triển tính năng |
| `debugger.md` | Chuyên gia debug | read, bash, grep | Điều tra bug |
| `data-scientist.md` | Chuyên gia phân tích dữ liệu | read, write, bash | Workflow dữ liệu |
| `clean-code-reviewer.md` | Tiêu chuẩn clean code | read, grep | Chất lượng code |
| `README.md` | Tài liệu | - | Hướng dẫn cài đặt và sử dụng |

**Đường Dẫn Cài Đặt**: `.claude/agents/`

**Cách Dùng**: Tự động ủy quyền bởi tác nhân chính

---

## 05. Giao Thức MCP (5 files)

Các tích hợp công cụ và API bên ngoài.

| File | Mô Tả | Tích Hợp Với | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | Tích hợp GitHub | GitHub API | Quản lý PR/issue |
| `database-mcp.json` | Truy vấn database | PostgreSQL/MySQL | Truy vấn dữ liệu trực tiếp |
| `filesystem-mcp.json` | Thao tác file | Filesystem cục bộ | Quản lý file |
| `multi-mcp.json` | Nhiều servers | GitHub + DB + Slack | Tích hợp hoàn chỉnh |
| `README.md` | Tài liệu | - | Hướng dẫn cài đặt và sử dụng |

**Đường Dẫn Cài Đặt**: `.mcp.json` (phạm vi dự án) hoặc `~/.claude.json` (phạm vi người dùng)

**Cách Dùng**: `/mcp__github__list_prs`, v.v.

---

## 06. Hooks (9 files)

Các script tự động hóa dựa trên sự kiện thực thi tự động.

| File | Mô Tả | Sự Kiện | Use Case |
|------|-------------|-------|----------|
| `format-code.sh` | Tự động format code | PreToolUse:Write | Format code |
| `pre-commit.sh` | Chạy test trước commit | PreToolUse:Bash | Tự động hóa test |
| `security-scan.sh` | Quét bảo mật | PostToolUse:Write | Kiểm tra bảo mật |
| `log-bash.sh` | Ghi log bash commands | PostToolUse:Bash | Ghi log commands |
| `validate-prompt.sh` | Xác thực prompts | PreToolUse | Xác thực input |
| `notify-team.sh` | Gửi thông báo | Notification | Thông báo nhóm |
| `context-tracker.py` | Theo dõi usage context window | PostToolUse | Giám sát context |
| `context-tracker-tiktoken.py` | Theo dõi context dựa trên token | PostToolUse | Đếm token chính xác |
| `README.md` | Tài liệu | - | Hướng dẫn cài đặt và sử dụng |

**Đường Dẫn Cài Đặt**: Cấu hình trong `~/.claude/settings.json`

**Cách Dùng**: Cấu hình trong settings, thực thi tự động

**Hook Types** (4 types, 25 events):
- Tool Hooks: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Session Hooks: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Task Hooks: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Lifecycle Hooks: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Plugins (3 plugins hoàn chỉnh, 40 files)

Các bộ sưu tập tính năng được đóng gói.

### PR Review Plugin (10 files)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── review-pr.md                  # Review toàn diện
│   ├── check-security.md             # Kiểm tra bảo mật
│   └── check-tests.md                # Kiểm tra độ phủ test
├── agents/
│   ├── security-reviewer.md          # Chuyên gia bảo mật
│   ├── test-checker.md               # Chuyên gia test
│   └── performance-analyzer.md       # Chuyên gia hiệu năng
├── mcp/
│   └── github-config.json            # Tích hợp GitHub
├── hooks/
│   └── pre-review.js                 # Xác thực pre-review
└── README.md                         # Tài liệu plugin
```

**Tính Năng**: Phân tích bảo mật, độ phủ test, tác động hiệu năng

**Commands**: `/review-pr`, `/check-security`, `/check-tests`

**Cài Đặt**: `/plugin install pr-review`

---

### DevOps Automation Plugin (15 files)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── deploy.md                     # Triển khai
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # Trạng thái hệ thống
│   └── incident.md                   # Phản hồi sự cố
├── agents/
│   ├── deployment-specialist.md      # Chuyên gia triển khai
│   ├── incident-commander.md         # Điều phối viên sự cố
│   └── alert-analyzer.md             # Trình phân tích alert
├── mcp/
│   └── kubernetes-config.json        # Tích hợp Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # Kiểm tra pre-deployment
│   └── post-deploy.js                # Tasks post-deployment
├── scripts/
│   ├── deploy.sh                     # Tự động hóa triển khai
│   ├── rollback.sh                   # Tự động hóa rollback
│   └── health-check.sh               # Kiểm tra sức khỏe
└── README.md                         # Tài liệu plugin
```

**Tính Năng**: Triển khai Kubernetes, rollback, giám sát, phản hồi sự cố

**Commands**: `/deploy`, `/rollback`, `/status`, `/incident`

**Cài Đặt**: `/plugin install devops-automation`

---

### Documentation Plugin (14 files)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin manifest
├── commands/
│   ├── generate-api-docs.md          # Tạo tài liệu API
│   ├── generate-readme.md            # Tạo README
│   ├── sync-docs.md                  # Đồng bộ tài liệu
│   └── validate-docs.md              # Xác thực tài liệu
├── agents/
│   ├── api-documenter.md             # Chuyên gia tài liệu API
│   ├── code-commentator.md           # Chuyên gia comment code
│   └── example-generator.md          # Trình tạo ví dụ
├── mcp/
│   └── github-docs-config.json       # Tích hợp GitHub
├── templates/
│   ├── api-endpoint.md               # Template API endpoint
│   ├── function-docs.md              # Template tài liệu function
│   └── adr-template.md               # Template ADR
└── README.md                         # Tài liệu plugin
```

**Tính Năng**: Tài liệu API, tạo README, đồng bộ docs, xác thực

**Commands**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Cài Đặt**: `/plugin install documentation`

**Plus**: `README.md` - Tổng quan plugins và hướng dẫn sử dụng

---

## 08. Checkpoints và Rewind (2 files)

Lưu trạng thái conversation và khám phá các cách tiếp cận thay thế.

| File | Mô Tả | Nội Dung |
|------|-------------|---------|
| `README.md` | Tài liệu | Hướng dẫn toàn diện về checkpoints |
| `checkpoint-examples.md` | Ví dụ thực tế | Database migration, tối ưu hóa hiệu năng, UI iteration, debug | | | |

**Khái Niệm Chính**:
- **Checkpoint**: Snapshot của trạng thái conversation
- **Rewind**: Trở về checkpoint trước đó
- **Branch Point**: Khám phá nhiều cách tiếp cận

**Cách Dùng**:
```
# Checkpoints được tạo tự động với mỗi user prompt
# Để rewind, nhấn Esc hai lần hoặc dùng:
/rewind
# Sau đó chọn: Khôi phục code và conversation, Khôi phục conversation,
# Khôi phục code, Tóm tắt từ đây, hoặc Bỏ qua
```

**Use Cases**:
- Thử các implementations khác nhau
- Phục hồi từ lỗi
- Thử nghiệm an toàn
- So sánh giải pháp
- A/B testing

---

## 09. Tính Nâng Cao (3 files)

Các khả năng nâng cao cho workflows phức tạp.

| File | Mô Tả | Tính Năng |
|------|-------------|----------|
| `README.md` | Hướng dẫn hoàn chỉnh | Tài liệu tất cả tính năng nâng cao |
| `config-examples.json` | Ví dụ cấu hình | 10+ cấu hình cụ thể theo use-case |
| `planning-mode-examples.md` | Ví dụ lập kế hoạch | REST API, database migration, refactoring |
| Scheduled Tasks | Tasks định kỳ với `/loop` và cron tools | Workflows định kỳ tự động |
| Chrome Integration | Tự động hóa trình duyệt qua headless Chromium | Testing và scraping web |
| Remote Control (expanded) | Phương thức kết nối, bảo mật, bảng so sánh | Quản lý session từ xa |
| Keyboard Customization | Phím tắt tùy chỉnh, hỗ trợ chord, contexts | Phím tắt cá nhân hóa |
| Desktop App (expanded) | Connectors, launch.json, tính năng enterprise | Tích hợp desktop | | | |

**Tính Năng Nâng Cao Được Bao Phủ**:

### Planning Mode
- Tạo kế hoạch triển khai chi tiết
- Ước tính thời gian và đánh giá rủi ro
- Phân tách task có hệ thống

### Extended Thinking
- Lý luận sâu cho vấn đề phức tạp
- Phân tích quyết định kiến trúc
- Đánh giá trade-off

### Background Tasks
- Operations dài hạn không chặn
- Workflows phát triển song song
- Quản lý và giám sát tasks

### Permission Modes
- **default**: Hỏi phê duyệt cho hành động rủi ro
- **acceptEdits**: Tự động chấp nhận edits file, hỏi cho các khác
- **plan**: Phân tích read-only, không sửa đổi
- **auto**: Tự động phê duyệt hành động an toàn, hỏi cho rủi ro
- **dontAsk**: Chấp nhận tất cả trừ rủi ro
- **bypassPermissions**: Chấp nhận tất cả (yêu cầu `--dangerously-skip-permissions`)

### Headless Mode (`claude -p`)
- Tích hợp CI/CD
- Thực thi task tự động
- Xử lý hàng loạt

### Session Management
- Nhiều work sessions
- Chuyển và lưu sessions
- Session persistence

### Interactive Features
- Phím tắt
- Lịch sử commands
- Tab completion
- Input đa dòng

### Configuration
- Quản lý settings toàn diện
- Cấu hình cụ thể theo môi trường
- Tùy chỉnh theo dự án

### Scheduled Tasks
- Tasks định kỳ với command `/loop`
- Cron tools: CronCreate, CronList, CronDelete
- Workflows định kỳ tự động

### Chrome Integration
- Tự động hóa trình duyệt qua headless Chromium
- Khả năng testing và scraping web
- Tương tác trang và trích xuất dữ liệu

### Remote Control (expanded)
- Phương thức và giao thức kết nối
- Cân nhắc bảo mật và best practices
- Bảng so sánh các tùy chọn truy cập từ xa

### Keyboard Customization
- Cấu hình keybinding tùy chỉnh
- Hỗ trợ chord cho phím tắt đa-phím
- Kích hoạt keybinding nhận biết ngữ cảnh

### Desktop App (expanded)
- Connectors cho tích hợp IDE
- Cấu hình launch.json
- Tính năng và triển khai enterprise

---

## 10. Sử Dụng CLI (1 file)

Các pattern và tham chiếu sử dụng giao diện dòng lệnh.

| File | Mô Tả | Nội Dung |
|------|-------------|---------|
| `README.md` | Tài liệu CLI | Flags, options, và patterns sử dụng |

**Tính Năng CLI Chính**:
- `claude` - Bắt đầu session tương tác
- `claude -p "prompt"` - Mode headless/không-tương-tác
- `claude web` - Khởi chạy web session
- `claude --model` - Chọn model (Sonnet 4.6, Opus 4.6)
- `claude --permission-mode` - Đặt permission mode
- `claude --remote` - Bật điều khiển từ xa qua WebSocket

---

## Files Tài Liệu (13 files)

| File | Vị Trí | Mô Tả |
|------|----------|-------------|
| `README.md` | `/` | Tổng quan ví dụ chính |
| `INDEX.md` | `/` | Danh mục hoàn chỉnh này |
| `QUICK_REFERENCE.md` | `/` | Tham khảo nhanh |
| `README.md` | `/01-slash-commands/` | Hướng dẫn lệnh slash |
| `README.md` | `/02-memory/` | Hướng dẫn bộ nhớ |
| `README.md` | `/03-skills/` | Hướng dẫn skills |
| `README.md` | `/04-subagents/` | Hướng dẫn tác nhân con |
| `README.md` | `/05-mcp/` | Hướng dẫn MCP |
| `README.md` | `/06-hooks/` | Hướng dẫn hooks |
| `README.md` | `/07-plugins/` | Hướng dẫn plugins |
| `README.md` | `/08-checkpoints/` | Hướng dẫn checkpoints |
| `README.md` | `/09-advanced-features/` | Hướng dẫn tính năng nâng cao |
| `README.md` | `/10-cli/` | Hướng dẫn CLI |

---

## Cây File Hoàn Chỉnh

```
claude-howto/
├── README.md                                    # Tổng quan chính
├── INDEX.md                                     # File này
├── QUICK_REFERENCE.md                           # Tham khảo nhanh
├── claude_concepts_guide.md                     # Hướng dẫn gốc
│
├── 01-slash-commands/                           # Lệnh Slash
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Bộ Nhớ
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Tác Nhân Con
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # Giao Thức MCP
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Tính Nâng Cao
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # Sử Dụng CLI
    └── README.md
```

---

## Bắt Đầu Nhanh Theo Use Case

### Chất Lượng & Reviews Code
```bash
# Cài đặt lệnh slash
cp 01-slash-commands/optimize.md .claude/commands/

# Cài đặt tác nhân con
cp 04-subagents/code-reviewer.md .claude/agents/

# Cài đặt skill
cp -r 03-skills/code-review ~/.claude/skills/

# Hoặc cài đặt plugin hoàn chỉnh
/plugin install pr-review
```

### DevOps & Triển Khai
```bash
# Cài đặt plugin (bao gồm tất cả)
/plugin install devops-automation
```

### Tài Liệu
```bash
# Cài đặt lệnh slash
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Cài đặt tác nhân con
cp 04-subagents/documentation-writer.md .claude/agents/

# Cài đặt skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Hoặc cài đặt plugin hoàn chỉnh
/plugin install documentation
```

### Tiêu Chuẩn Nhóm
```bash
# Thiết lập bộ nhớ dự án
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Chỉnh sửa để khớp với tiêu chuẩn nhóm của bạn
```

### Tích Hợp Bên Ngoài
```bash
# Đặt biến môi trường
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Cài đặt config MCP (phạm vi dự án)
cp 05-mcp/multi-mcp.json .mcp.json
```

### Tự Động Hóa & Xác Thực
```bash
# Cài đặt hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Cấu hình hooks trong settings (~/.claude/settings.json)
# Xem 06-hooks/README.md
```

### Thử Nghiệm An Toàn
```bash
# Checkpoints được tạo tự động với mỗi user prompt
# Để rewind: nhấn Esc+Esc hoặc dùng:
/rewind
# Sau đó chọn: Khôi phục code và conversation, Khôi phục conversation,
# Khôi phục code, Tóm tắt từ đây, hoặc Bỏ qua

# Xem 08-checkpoints/README.md cho ví dụ
```

### Workflows Nâng Cao
```bash
# Cấu hình tính năng nâng cao
# Xem 09-advanced-features/config-examples.json

# Sử dụng planning mode
/plan Triển khai tính năng X

# Sử dụng permission modes
claude --permission-mode plan          # Cho review code (read-only)
claude --permission-mode acceptEdits   # Tự động chấp nhận edits
claude --permission-mode auto          # Tự động phê duyệt hành động an toàn

# Chạy trong mode headless cho CI/CD
claude -p "Chạy test và báo cáo kết quả"

# Chạy background tasks
Chạy test trong background

# Xem 09-advanced-features/README.md cho hướng dẫn hoàn chỉnh
```

---

## Ma Trận Phủ Sở Tính Năng

| Danh Mục | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Images | Tổng |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Lệnh Slash** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Bộ Nhớ** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Tác Nhân Con** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Nâng Cao** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## Lộ Trình Học Tập

### Người Mới Bắt Đầu (Tuần 1)
1. ✅ Đọc `README.md`
2. ✅ Cài đặt 1-2 lệnh slash
3. ✅ Tạo file bộ nhớ dự án
4. ✅ Thử các commands cơ bản

### Trung Cấp (Tuần 2-3)
1. ✅ Thiết lập GitHub MCP
2. ✅ Cài đặt một tác nhân con
3. ✅ Thử ủy quyền tasks
4. ✅ Cài đặt một skill

### Nâng Cao (Tuần 4+)
1. ✅ Cài đặt plugin hoàn chỉnh
2. ✅ Tạo lệnh slash tùy chỉnh
3. ✅ Tạo tác nhân con tùy chỉnh
4. ✅ Tạo skill tùy chỉnh
5. ✅ Xây dựng plugin của riêng bạn

### Chuyên Gia (Tuần 5+)
1. ✅ Thiết lập hooks cho tự động hóa
2. ✅ Sử dụng checkpoints để thử nghiệm
3. ✅ Cấu hình planning mode
4. ✅ Sử dụng permission modes hiệu quả
5. ✅ Thiết lập headless mode cho CI/CD
6. ✅ Làm chủ session management

---

## Tìm Kiếm Theo Từ Khóa

### Hiệu Năng
- `01-slash-commands/optimize.md` - Phân tích hiệu năng
- `04-subagents/code-reviewer.md` - Review hiệu năng
- `03-skills/code-review/` - Metrics hiệu năng
- `07-plugins/pr-review/agents/performance-analyzer.md` - Chuyên gia hiệu năng

### Bảo Mật
- `04-subagents/secure-reviewer.md` - Review bảo mật
- `03-skills/code-review/` - Phân tích bảo mật
- `07-plugins/pr-review/` - Kiểm tra bảo mật

### Testing
- `04-subagents/test-engineer.md` - Kỹ sư test
- `07-plugins/pr-review/commands/check-tests.md` - Độ phủ test

### Tài Liệu
- `01-slash-commands/generate-api-docs.md` - Command tài liệu API
- `04-subagents/documentation-writer.md` - Tác nhân viết tài liệu
- `03-skills/doc-generator/` - Skill tạo tài liệu
- `07-plugins/documentation/` - Plugin tài liệu hoàn chỉnh

### Triển Khai
- `07-plugins/devops-automation/` - Giải pháp DevOps hoàn chỉnh

### Tự Động Hóa
- `06-hooks/` - Tự động hóa dựa trên sự kiện
- `06-hooks/pre-commit.sh` - Tự động hóa pre-commit
- `06-hooks/format-code.sh` - Tự động format
- `09-advanced-features/` - Headless mode cho CI/CD

### Xác Thực
- `06-hooks/security-scan.sh` - Xác thực bảo mật
- `06-hooks/validate-prompt.sh` - Xác thực prompt

### Thử Nghiệm
- `08-checkpoints/` - Thử nghiệm an toàn với rewind
- `08-checkpoints/checkpoint-examples.md` - Ví dụ thực tế

### Lập Kế Hoạch
- `09-advanced-features/planning-mode-examples.md` - Ví dụ planning mode
- `09-advanced-features/README.md` - Extended thinking

### Cấu Hình
- `09-advanced-features/config-examples.json` - Ví dụ cấu hình

---

## Ghi Chú

- Tất cả ví dụ đều sẵn sàng sử dụng
- Chỉnh sửa để phù hợp với nhu cầu cụ thể của bạn
- Ví dụ tuân theo best practices của Claude Code
- Mỗi danh mục có README riêng với hướng dẫn chi tiết
- Scripts bao gồm xử lý lỗi thích hợp
- Templates có thể tùy chỉnh

---

## Đóng Góp

Muốn thêm ví dụ nữa? Theo cấu trúc:
1. Tạo thư mục con phù hợp
2. Bao gồm README.md với hướng dẫn sử dụng
3. Theo quy ước đặt tên
4. Test kỹ lưỡng
5. Cập nhật danh mục này

---

**Cập Nhật Lần**: Tháng 3 năm 2026
**Tổng Số Ví Dụ**: 100+ files
**Danh Mục**: 10 tính năng
**Hooks**: 8 scripts tự động hóa
**Ví Dụ Cấu Hình**: 10+ scenarios
**Sẵn Sàng Sử Dụng**: Tất cả ví dụ
