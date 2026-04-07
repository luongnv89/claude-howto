<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Danh Mục Tính Năng Claude Code

> Hướng dẫn tham khảo nhanh cho tất cả tính năng Claude Code: commands, agents, skills, plugins, và hooks.

**Điều Hướng**: [Commands](#lệnh-slash) | [Permission Modes](#permission-modes) | [Tác Nhân Con](#tác-nhân-con) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Bộ Nhớ](#files-bộ-nhớ) | [Tính Năng Mới](#tính-năng-mới-tháng-3-năm-2026)

---

## Tóm Tắt

| Tính Năng | Built-in | Ví Dụ | Tổng | Tham Chiếu |
|---------|----------|----------|-------|-----------|
| **Lệnh Slash** | 55+ | 8 | 63+ | [01-slash-commands/](../01-slash-commands/) |
| **Tác Nhân Con** | 6 | 10 | 16 | [04-subagents/](../04-subagents/) |
| **Skills** | 5 bundled | 4 | 9 | [03-skills/](../03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](../07-plugins/) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/](../05-mcp/) |
| **Hooks** | 25 sự kiện | 7 | 7 | [06-hooks/](../06-hooks/) |
| **Bộ Nhớ** | 7 loại | 3 | 3 | [02-memory/](../02-memory/) |
| **Tổng** | **99** | **43** | **117** | |

---

## Lệnh Slash

Commands là các lệnh tắt do người dùng gọi thực hiện các hành động cụ thể.

### Built-in Commands

| Command | Mô Tả | Khi Nào Dùng |
|---------|-------------|-------------|
| `/help` | Hiển thị thông tin help | Bắt đầu, học commands |
| `/btw` | Câu hỏi phụ không thêm vào context | Câu hỏi nhanh |
| `/chrome` | Cấu hình tích hợp Chrome | Tự động hóa trình duyệt |
| `/clear` | Xóa lịch sử conversation | Bắt đầu mới, giảm context |
| `/diff` | Trình xem diff tương tác | Review thay đổi |
| `/config` | Xem/chỉnh sửa cấu hình | Tùy chỉnh hành vi |
| `/status` | Hiển thị trạng thái session | Kiểm tra trạng thái hiện tại |
| `/agents` | Liệt kê các agents có sẵn | Xem tùy chọn ủy quyền |
| `/skills` | Liệt kê các skills có sẵn | Xem khả năng auto-invoke |
| `/hooks` | Liệt kê các hooks đã cấu hình | Debug tự động hóa |
| `/insights` | Phân tích patterns của session | Tối ưu hóa session |
| `/install-slack-app` | Cài đặt Claude Slack app | Tích hợp Slack |
| `/keybindings` | Tùy chỉnh phím tắt | Tùy chỉnh phím |
| `/mcp` | Liệt kê MCP servers | Kiểm tra tích hợp bên ngoài |
| `/memory` | Xem các file bộ nhớ đã tải | Debug tải context |
| `/mobile` | Tạo QR code mobile | Truy cập mobile |
| `/passes` | Xem usage passes | Thông tin subscription |
| `/plugin` | Quản lý plugins | Cài đặt/gỡ mở rộng |
| `/plan` | Vào planning mode | Triển khai phức tạp |
| `/rewind` | Rewind về checkpoint | Hoàn tác thay đổi, khám phá alternatives |
| `/checkpoint` | Quản lý checkpoints | Lưu/khôi phục trạng thái |
| `/cost` | Hiển thị chi phí usage token | Giám sát chi tiêu |
| `/context` | Hiển thị usage context window | Quản lý độ dài conversation |
| `/export` | Xuất conversation | Lưu để tham khảo |
| `/extra-usage` | Cấu hình giới hạn usage thêm | Quản lý rate limit |
| `/feedback` | Gửi feedback hoặc báo cáo bug | Báo cáo vấn đề |
| `/login` | Xác thực với Anthropic | Truy cập tính năng |
| `/logout` | Đăng xuất | Chuyển tài khoản |
| `/sandbox` | Bật/tắt sandbox mode | Thực thi command an toàn |
| `/vim` | Bật/tắt vim mode | Chỉnh sửa kiểu Vim |
| `/doctor` | Chạy chẩn đoán | Khắc phục sự cố |
| `/reload-plugins` | Tải lại plugins đã cài đặt | Quản lý plugin |
| `/release-notes` | Hiển thị release notes | Kiểm tra tính năng mới |
| `/remote-control` | Bật điều khiển từ xa | Truy cập từ xa |
| `/permissions` | Quản lý permissions | Kiểm soát truy cập |
| `/session` | Quản lý sessions | Workflows đa session |
| `/rename` | Đổi tên session hiện tại | Tổ chức sessions |
| `/resume` | Tiếp tục session trước | Tiếp tục làm việc |
| `/todo` | Xem/quản lý todo list | Theo dõi tasks |
| `/tasks` | Xem background tasks | Giám sát operations async |
| `/copy` | Sao chép response cuối vào clipboard | Chia sẻ output nhanh |
| `/teleport` | Chuyển session sang máy khác | Tiếp tục làm việc từ xa |
| `/desktop` | Mở Claude Desktop app | Chuyển sang interface desktop |
| `/theme` | Đổi màu theme | Tùy chỉnh giao diện |
| `/usage` | Hiển thị thống kê usage API | Giám sát quota và chi phí |
| `/fork` | Fork conversation hiện tại | Khám phá alternatives |
| `/stats` | Hiển thị thống kê session | Review metrics session |
| `/statusline` | Cấu hình status line | Tùy chỉnh hiển thị trạng thái |
| `/stickers` | Xem stickers của session | Phần thưởng vui |
| `/fast` | Bật/tắt mode output nhanh | Tăng tốc độ responses |
| `/terminal-setup` | Cấu hình tích hợp terminal | Thiết lập tính năng terminal |
| `/upgrade` | Kiểm tra cập nhật | Quản lý phiên bản |

### Custom Commands (Ví Dụ)

| Command | Mô Tả | Khi Nào Dùng | Phạm Vi | Cài Đặt |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | Phân tích code để tối ưu hóa | Cải thiện hiệu năng | Project | `cp ../01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Chuẩn bị pull request | Trước khi gửi PRs | Project | `cp ../01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | Tạo tài liệu API | Tài liệu hóa APIs | Project | `cp ../01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | Tạo git commit với context | Commit thay đổi | User | `cp ../01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | Stage, commit, và push | Triển khai nhanh | User | `cp ../01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | Tái cấu trúc tài liệu | Cải thiện docs | Project | `cp ../01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | Thiết lập pipeline CI/CD | Dự án mới | Project | `cp ../01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | Mở rộng độ phủ test | Cải thiện testing | Project | `cp ../01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Phạm Vi**: `User` = workflows cá nhân (`~/.claude/commands/`), `Project` = chia sẻ team (`.claude/commands/`)

**Tham Chiếu**: [01-slash-commands/](../01-slash-commands/) | [Tài Liệu Chính Thức](https://code.claude.com/docs/en/interactive-mode)

**Cài Đặt Nhanh (Tất Cả Custom Commands)**:
```bash
cp ../01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

Claude Code hỗ trợ 6 permission modes điều khiển cách tool use được ủy quyền.

| Mode | Mô Tả | Khi Nào Dùng |
|------|-------------|-------------|
| `default` | Hỏi cho mỗi tool call | Sử dụng tương tác tiêu chuẩn |
| `acceptEdits` | Tự động chấp nhận edits file, hỏi cho các khác | Workflows chỉnh sửa tin cậy |
| `plan` | Chỉ tools read-only, không ghi | Lập kế hoạch và khám phá |
| `auto` | Chấp nhận tất cả tools mà không hỏi | Vận hành hoàn toàn tự động (Research Preview) |
| `bypassPermissions` | Bỏ qua tất cả kiểm tra permissions | CI/CD, môi trường headless |
| `dontAsk` | Bỏ qua tools cần yêu cầu permission | Scripting không tương tác |

> **Lưu Ý**: `auto` mode là tính năng Research Preview (Tháng 3 năm 2026). Chỉ dùng `bypassPermissions` trong môi trường tin cậy, được sandbox.

**Tham Chiếu**: [Tài Liệu Chính Thức](https://code.claude.com/docs/en/permissions)

---

## Tác Nhân Con

Các trợ lý AI chuyên biệt với context bị cô lập cho các tasks cụ thể.

### Built-in Subagents

| Agent | Mô Tả | Tools | Model | Khi Nào Dùng |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | Tasks đa bước, nghiên cứu | All tools | Kế thừa model | Nghiên cứu phức tạp, tasks đa file |
| **Plan** | Lập kế hoạch triển khai | Read, Glob, Grep, Bash | Kế thừa model | Thiết kế kiến trúc, lập kế hoạch |
| **Explore** | Khám phá codebase | Read, Glob, Grep | Haiku 4.5 | Tìm kiếm nhanh, hiểu code |
| **Bash** | Thực thi command | Bash | Kế thừa model | Operations Git, tasks terminal |
| **statusline-setup** | Cấu hình status line | Bash, Read, Write | Sonnet 4.6 | Cấu hình hiển thị status line |
| **Claude Code Guide** | Trợ giúp và tài liệu | Read, Glob, Grep | Haiku 4.5 | Nhận trợ giúp, học tính năng |

### Subagent Configuration Fields

| Field | Type | Mô Tả |
|-------|------|-------------|
| `name` | string | Định danh agent |
| `description` | string | Agent làm gì |
| `model` | string | Ghi đè model (ví dụ: `haiku-4.5`) |
| `tools` | array | Danh sách tools được phép |
| `effort` | string | Mức độ effort lý luận (`low`, `medium`, `high`) |
| `initialPrompt` | string | System prompt được chèn khi agent bắt đầu |
| `disallowedTools` | array | Tools bị từ chối rõ ràng cho agent này |

### Custom Subagents (Ví Dụ)

| Agent | Mô Tả | Khi Nào Dùng | Phạm Vi | Cài Đặt |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | Chất lượng code toàn diện | Sessions review code | Project | `cp ../04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | Thiết kế kiến trúc tính năng | Lập kế hoạch tính năng mới | Project | `cp ../04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | Phân tích codebase sâu | Hiểu tính năng hiện có | Project | `cp ../04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Review nguyên tắc Clean Code | Review khả năng bảo trì | Project | `cp ../04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | Chiến lược & độ phủ test | Lập kế hoạch test | Project | `cp ../04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | Tài liệu kỹ thuật | Tài liệu API, hướng dẫn | Project | `cp ../04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | Review tập trung bảo mật | Kiểm tra bảo mật | Project | `cp ../04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | Triển khai tính năng hoàn chỉnh | Phát triển tính năng | Project | `cp ../04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | Phân tích nguyên nhân gốc | Điều tra bug | User | `cp ../04-subagents/debugger.md ~/.claude/agents/` |
| `data-scientist` | Truy vấn SQL, phân tích dữ liệu | Tasks dữ liệu | User | `cp ../04-subagents/data-scientist.md ~/.claude/agents/` |

> **Phạm Vi**: `User` = cá nhân (`~/.claude/agents/`), `Project` = chia sẻ team (`.claude/agents/`)

**Tham Chiếu**: [04-subagents/](../04-subagents/) | [Tài Liệu Chính Thức](https://code.claude.com/docs/en/sub-agents)

**Cài Đặt Nhanh (Tất Cả Custom Agents)**:
```bash
cp ../04-subagents/*.md .claude/agents/
```

---

## Skills

Các khả năng tự động gọi với hướng dẫn, scripts, và templates.

### Ví Dụ Skills

| Skill | Mô Tả | Khi Tự Động Gọi | Phạm Vi | Cài Đặt |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | Review code toàn diện | "Review this code", "Check quality" | Project | `cp -r ../03-skills/code-review .claude/skills/` |
| `brand-voice` | Kiểm tra nhất quán brand | Viết marketing copy | Project | `cp -r ../03-skills/brand-voice .claude/skills/` |
| `doc-generator` | Trình tạo tài liệu API | "Generate docs", "Document API" | Project | `cp -r ../03-skills/doc-generator .claude/skills/` |
| `refactor` | Refactor code có hệ thống (Martin Fowler) | "Refactor this", "Clean up code" | User | `cp -r ../03-skills/refactor ~/.claude/skills/` |

> **Phạm Vi**: `User` = cá nhân (`~/.claude/skills/`), `Project` = chia sẻ team (`.claude/skills/`)

### Skill Structure

```
~/.claude/skills/skill-name/
├── SKILL.md          # Định nghĩa & hướng dẫn skill
├── scripts/          # Scripts hỗ trợ
└── templates/        # Templates output
```

### Skill Frontmatter Fields

Skills hỗ trợ YAML frontmatter trong `SKILL.md` để cấu hình:

| Field | Type | Mô Tả |
|-------|------|-------------|
| `name` | string | Tên hiển thị skill |
| `description` | string | Skill làm gì |
| `autoInvoke` | array | Cụm từ kích hoạt cho auto-invocation |
| `effort` | string | Mức độ effort lý luận (`low`, `medium`, `high`) |
| `shell` | string | Shell để dùng cho scripts (`bash`, `zsh`, `sh`) |

**Tham Chiếu**: [03-skills/](../03-skills/) | [Tài Liệu Chính Thức](https://code.claude.com/docs/en/skills)

**Cài Đặt Nhanh (Tất Cả Skills)**:
```bash
cp -r ../03-skills/* ~/.claude/skills/
```

### Bundled Skills

| Skill | Mô Tả | Khi Tự Động Gọi |
|-------|-------------|-------------------|
| `/simplify` | Review code về chất lượng | Sau khi viết code |
| `/batch` | Chạy prompts trên nhiều files | Operations hàng loạt |
| `/debug` | Debug tests/errors thất bại | Sessions debugging |
| `/loop` | Chạy prompts theo interval | Tasks định kỳ |
| `/claude-api` | Xây dựng apps với Claude API | Phát triển API |

---

## Plugins

Bộ sưu tập được đóng gói của commands, agents, MCP servers, và hooks.

### Ví Dụ Plugins

| Plugin | Mô Tả | Components | Khi Nào Dùng | Phạm Vi | Cài Đặt |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | Workflow review PR | 3 commands, 3 agents, GitHub MCP | Review code | Project | `/plugin install pr-review` |
| `devops-automation` | Triển khai & giám sát | 4 commands, 3 agents, K8s MCP | Tasks DevOps | Project | `/plugin install devops-automation` |
| `documentation` | Bộ tạo tài liệu | 4 commands, 3 agents, templates | Tài liệu | Project | `/plugin install documentation` |

> **Phạm Vi**: `Project` = chia sẻ team, `User` = workflows cá nhân

### Plugin Structure

```
.claude-plugin/
├── plugin.json       # File manifest
├── commands/         # Lệnh slash
├── agents/           # Tác nhân con
├── skills/           # Skills
├── mcp/              # Cấu hình MCP
├── hooks/            # Script hooks
└── scripts/          # Scripts tiện ích
```

**Tham Chiếu**: [07-plugins/](../07-plugins/) | [Tài Liệu Chính Thức](https://code.claude.com/docs/en/plugins)

**Plugin Management Commands**:
```bash
/plugin list              # Liệt kê plugins đã cài
/plugin install <name>    # Cài plugin
/plugin remove <name>     # Gỡ plugin
/plugin update <name>     # Cập nhật plugin
```

---

## MCP Servers

Máy chủ Model Context Protocol cho truy cập công cụ và API bên ngoài.

### MCP Servers Phổ Biến

| Server | Mô Tả | Khi Nào Dùng | Phạm Vi | Cài Đặt |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | Quản lý PR, issues, code | Workflows GitHub | Project | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | Truy vấn SQL, truy cập dữ liệu | Operations database | Project | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | Operations file nâng cao | Tasks file phức tạp | User | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | Communication team | Thông báo, cập nhật | Project | Cấu hình trong settings |
| **Google Docs** | Truy cập tài liệu | Chỉnh sửa, review docs | Project | Cấu hình trong settings |
| **Asana** | Quản lý dự án | Theo dõi tasks | Project | Cấu hình trong settings |
| **Stripe** | Dữ liệu thanh toán | Phân tích tài chính | Project | Cấu hình trong settings |
| **Memory** | Bộ nhớ lưu trữ | Nhớ lại qua sessions | User | Cấu hình trong settings |
| **Context7** | Tài liệu thư viện | Tra cứu docs cập nhật | Built-in | Built-in |

> **Phạm Vi**: `Project` = team (`.mcp.json`), `User` = cá nhân (`~/.claude.json`), `Built-in` = được cài trước

### MCP Configuration Example

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Tham Chiếu**: [05-mcp/](../05-mcp/) | [Tài Liệu Giao Thức MCP](https://modelcontextprotocol.io)

**Cài Đặt Nhanh (GitHub MCP)**:
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

Tự động hóa dựa trên sự kiện thực thi shell commands trên các sự kiện Claude Code.

### Hook Events

| Event | Mô Tả | Khi Được Kích Hoạt | Use Cases |
|-------|-------------|----------------|-----------|
| `SessionStart` | Session bắt đầu/tiếp tục | Khởi tạo session | Tasks thiết lập |
| `InstructionsLoaded` | Hướng dẫn được tải | CLAUDE.md hoặc file rules được tải | Xử lý hướng dẫn tùy chỉnh |
| `UserPromptSubmit` | Trước khi xử lý prompt | User gửi tin nhắn | Xác thực input |
| `PreToolUse` | Trước khi thực thi tool | Trước khi bất kỳ tool chạy | Xác thực, logging |
| `PermissionRequest` | Dialog permission được hiển thị | Trước hành động nhạy cảm | Flows phê duyệt tùy chỉnh |
| `PostToolUse` | Sau khi tool thành công | Sau khi bất kỳ tool hoàn thành | Formatting, thông báo |
| `PostToolUseFailure` | Thực thi tool thất bại | Sau khi tool lỗi | Xử lý lỗi, logging |
| `Notification` | Thông báo được gửi | Claude gửi thông báo | Cảnh báo bên ngoài |
| `SubagentStart` | Subagent được tạo | Task subagent bắt đầu | Khởi tạo context subagent |
| `SubagentStop` | Subagent hoàn thành | Task subagent hoàn tất | Chuỗi hành động |
| `Stop` | Claude hoàn thành phản hồi | Phản hồi hoàn tất | Dọn dẹp, báo cáo |
| `StopFailure` | Lỗi API kết thúc turn | Lỗi API xảy ra | Phục hồi lỗi, logging |
| `TeammateIdle` | Agent teammate rảnh | Phối hợp agent team | Phân phối work |
| `TaskCompleted` | Task được đánh dấu hoàn tất | Task xong | Xử lý post-task |
| `TaskCreated` | Task được tạo qua TaskCreate | Task mới được tạo | Theo dõi task, logging |
| `ConfigChange` | Cấu hình được cập nhật | Settings được sửa đổi | Phản ứng thay đổi config |
| `CwdChanged` | Thư mục làm việc thay đổi | Thư mục thay đổi | Thiết lập cụ thể theo thư mục |
| `FileChanged` | File được theo dõi thay đổi | File được sửa | Giám sát file, rebuild |
| `PreCompact` | Trước operation compact | Nén context | Bảo toàn trạng thái |
| `PostCompact` | Sau khi compact hoàn tất | Compact xong | Hành động post-compact |
| `WorktreeCreate` | Worktree đang được tạo | Git worktree được tạo | Thiết lập môi trường worktree |
| `WorktreeRemove` | Worktree đang bị gỡ | Git worktree bị gỡ | Dọn dẹp tài nguyên worktree |
| `Elicitation` | MCP server yêu cầu input | MCP elicitation | Xác thực input |
| `ElicitationResult` | User phản hồi elicitation | User phản hồi | Xử lý phản hồi |
| `SessionEnd` | Session chấm dứt | Chấm dứt session | Dọn dẹp, lưu trạng thái |

### Ví Dụ Hooks

| Hook | Mô Tả | Event | Phạm Vi | Cài Đặt |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | Xác thực command | PreToolUse:Bash | Project | `cp ../06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | Quét bảo mật | PostToolUse:Write | Project | `cp ../06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | Tự động format | PostToolUse:Write | User | `cp ../06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | Xác thực prompt | UserPromptSubmit | Project | `cp ../06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Theo dõi usage token | Stop | User | `cp ../06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | Xác thực pre-commit | PreToolUse:Bash | Project | `cp ../06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | Ghi log commands | PostToolUse:Bash | User | `cp ../06-hooks/log-bash.sh ~/.claude/hooks/` |

> **Phạm Vi**: `Project` = team (`.claude/settings.json`), `User` = cá nhân (`~/.claude/settings.json`)

### Hook Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**Tham Chiếu**: [06-hooks/](../06-hooks/) | [Tài Liệu Chính Thức](https://code.claude.com/docs/en/hooks)

**Cài Đặt Nhanh (Tất Cả Hooks)**:
```bash
mkdir -p ~/.claude/hooks && cp ../06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Files Bộ Nhớ

Ngữ cảnh lưu trữ được tải tự động qua sessions.

### Loại Bộ Nhớ

| Loại | Vị Trí | Phạm Vi | Khi Nào Dùng |
|------|----------|-------|-------------|
| **Managed Policy** | Policies được quản lý bởi tổ chức | Tổ chức | Thực thi tiêu chuẩn toàn tổ chức |
| **Project** | `./CLAUDE.md` | Project (team) | Tiêu chuẩn team, context dự án |
| **Project Rules** | `.claude/rules/` | Project (team) | Rules dự án modular |
| **User** | `~/.claude/CLAUDE.md` | User (cá nhân) | Sở thích cá nhân |
| **User Rules** | `~/.claude/rules/` | User (cá nhân) | Rules cá nhân modular |
| **Local** | `./CLAUDE.local.md` | Local (git-ignored) | Ghi đè cụ thể theo máy (không trong tài liệu chính thức tính đến tháng 3/2026; có thể là legacy) |
| **Auto Memory** | Tự động | Session | Insights và chỉnh sửa được tự động nắm bắt |

> **Phạm Vi**: `Organization` = được quản lý bởi admins, `Project` = chia sẻ với team qua git, `User` = sở thích cá nhân, `Local` = không được commit, `Session` = được tự động quản lý

**Tham Chiếu**: [02-memory/](../02-memory/) | [Tài Liệu Chính Thức](https://code.claude.com/docs/en/memory)

**Cài Đặt Nhanh**:
```bash
cp ../02-memory/project-CLAUDE.md ./CLAUDE.md
cp ../02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## Tính Năng Mới (Tháng 3 Năm 2026)

| Tính Năng | Mô Tả | Cách Dùng |
|---------|-------------|------------|
| **Remote Control** | Điều khiển sessions Claude Code từ xa qua API | Sử dụng API điều khiển từ xa để gửi prompts và nhận responses theo chương trình |
| **Web Sessions** | Chạy Claude Code trong môi trường dựa trên trình duyệt | Truy cập qua `claude web` hoặc qua Anthropic Console |
| **Desktop App** | Ứng dụng desktop native cho Claude Code | Sử dụng `/desktop` hoặc tải từ website Anthropic |
| **Agent Teams** | Phối hợp nhiều agents làm việc trên các tasks liên quan | Cấu hình teammate agents cộng tác và chia sẻ context |
| **Task List** | Quản lý và giám sát background tasks | Sử dụng `/tasks` để xem và quản lý operations nền |
| **Prompt Suggestions** | Gợi ý command nhận biết ngữ cảnh | Gợi ý xuất hiện tự động dựa trên ngữ cảnh hiện tại |
| **Git Worktrees** | Git worktrees bị cô lập để phát triển song song | Sử dụng commands worktree để làm việc branch song song an toàn |
| **Sandboxing** | Môi trường thực thi bị cô lập để an toàn | Sử dụng `/sandbox` để bật/tắt; chạy commands trong môi trường bị hạn chế |
| **MCP OAuth** | Xác thực OAuth cho MCP servers | Cấu hình credentials OAuth trong settings MCP server để truy cập an toàn |
| **MCP Tool Search** | Tìm kiếm và khám phá MCP tools động | Sử dụng tìm kiếm tool để tìm MCP tools có sẵn qua các servers được kết nối |
| **Scheduled Tasks** | Thiết lập tasks định kỳ với `/loop` và cron tools | Sử dụng `/loop 5m /command` hoặc công cụ CronCreate |
| **Chrome Integration** | Tự động hóa trình duyệt với headless Chromium | Sử dụng flag `--chrome` hoặc command `/chrome` |
| **Keyboard Customization** | Tùy chỉnh keybindings bao gồm hỗ trợ chord | Sử dụng `/keybindings` hoặc chỉnh sửa `~/.claude/keybindings.json` |
| **Auto Mode** | Vận hành hoàn toàn tự động mà không cần prompts permission (Research Preview) | Sử dụng `--mode auto` hoặc `/permissions auto`; Tháng 3 năm 2026 |
| **Channels** | Communication đa kênh (Telegram, Slack, v.v.) (Research Preview) | Cấu hình plugins channels; Tháng 3 năm 2026 |
| **Voice Dictation** | Input giọng nói cho prompts | Sử dụng icon microphone hoặc keybinding giọng nói |
| **Agent Hook Type** | Hooks tạo subagent thay vì chạy shell command | Đặt `"type": "agent"` trong cấu hình hook |
| **Prompt Hook Type** | Hooks chèn văn bản prompt vào conversation | Đặt `"type": "prompt"` trong cấu hình hook |
| **MCP Elicitation** | MCP servers có thể yêu cầu input người dùng trong khi thực thi tool | Xử lý qua các sự kiện hook `Elicitation` và `ElicitationResult` |
| **WebSocket MCP Transport** | Transport dựa trên WebSocket cho kết nối MCP server | Sử dụng `"transport": "websocket"` trong cấu hình MCP server |
| **Plugin LSP Support** | Tích hợp Language Server Protocol qua plugins | Cấu hình servers LSP trong `plugin.json` cho tính năng editor |
| **Managed Drop-ins** | Cấu hình drop-ins được quản lý bởi tổ chức (v2.1.83) | Được cấu hình bởi admin qua policies được quản lý; tự động áp dụng cho tất cả users |

---

## Ma Trận Tham Khảo Nhanh

### Hướng Dẫn Chọn Tính Năng

| Nhu Cầu | Tính Năng Khuyến Nghị | Tại Sao |
|------|---------------------|-----|
| Phím tắt nhanh | Lệnh Slash | Thủ công, ngay lập tức |
| Ngữ cảnh lưu trữ | Bộ Nhớ | Tự động tải |
| Tự động hóa phức tạp | Skill | Tự động gọi |
| Task chuyên biệt | Tác Nhân Con | Context bị cô lập |
| Dữ liệu bên ngoài | MCP Server | Truy cập thời gian thực |
| Tự động hóa sự kiện | Hook | Được kích hoạt bởi sự kiện |
| Giải pháp hoàn chỉnh | Plugin | Gói tất cả trong một |

### Ưu Tiên Cài Đặt

| Ưu Tiên | Tính Năng | Command |
|----------|---------|---------|
| 1. Thiết Yếu | Bộ Nhớ | `cp ../02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Dùng Hàng Ngày | Lệnh Slash | `cp ../01-slash-commands/*.md .claude/commands/` |
| 3. Chất Lượng | Tác Nhân Con | `cp ../04-subagents/*.md .claude/agents/` |
| 4. Tự Động Hóa | Hooks | `cp ../06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. Bên Ngoài | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. Nâng Cao | Skills | `cp -r ../03-skills/* ~/.claude/skills/` |
| 7. Hoàn Chỉnh | Plugins | `/plugin install pr-review` |

---

## Cài Đặt Một Lệnh Hoàn Chỉnh

Cài đặt tất cả ví dụ từ repository này:

```bash
# Tạo thư mục
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Cài đặt tất cả tính năng
cp ../01-slash-commands/*.md .claude/commands/ && \
cp ../02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r ../03-skills/* ~/.claude/skills/ && \
cp ../04-subagents/*.md .claude/agents/ && \
cp ../06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Tài Nguyên Thêm

- [Tài Liệu Chính Thức Claude Code](https://code.claude.com/docs/en/overview)
- [Đặc Tả Giao Thức MCP](https://modelcontextprotocol.io)
- [Lộ Trình Học Tập](../LEARNING-ROADMAP.md)
- [README Chính](../README.md)

---

**Cập Nhật Lần**: Tháng 3 năm 2026
