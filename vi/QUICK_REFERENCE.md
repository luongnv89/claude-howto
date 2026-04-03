<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Ví Dụ Claude Code - Tham Khảo Nhanh

## 🚀 Lệnh Cài Đặt Nhanh

### Lệnh Slash
```bash
# Cài đặt tất cả
cp 01-slash-commands/*.md .claude/commands/

# Cài đặt cụ thể
cp 01-slash-commands/optimize.md .claude/commands/
```

### Bộ Nhớ
```bash
# Bộ nhớ dự án
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Bộ nhớ cá nhân
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# Skills cá nhân
cp -r 03-skills/code-review ~/.claude/skills/

# Skills dự án
cp -r 03-skills/code-review .claude/skills/
```

### Tác Nhân Con
```bash
# Cài đặt tất cả
cp 04-subagents/*.md .claude/agents/

# Cài đặt cụ thể
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# Thiết lập thông tin xác thực
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Cài đặt cấu hình (phạm vi dự án)
cp 05-mcp/github-mcp.json .mcp.json

# Hoặc phạm vi người dùng: thêm vào ~/.claude.json
```

### Hooks
```bash
# Cài đặt hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Cấu hình trong settings (~/.claude/settings.json)
```

### Plugins
```bash
# Cài đặt từ ví dụ (nếu đã xuất bản)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# Checkpoints được tạo tự động với mọi prompt của người dùng
# Để quay lại, nhấn Esc hai lần hoặc sử dụng:
/rewind

# Sau đó chọn: Khôi phục code và cuộc hội thoại, Khôi phục cuộc hội thoại,
# Khôi phục code, Tóm tắt từ đây, hoặc Thôi
```

### Tính Năng Nâng Cao
```bash
# Cấu hình trong settings (.claude/settings.json)
# Xem 09-advanced-features/config-examples.json

# Chế độ lập kế hoạch
/plan Mô tả tác vụ

# Chế độ quyền (sử dụng cờ --permission-mode)
# default        - Hỏi phê duyệt cho các hành động rủi ro
# acceptEdits    - Tự động chấp nhận chỉnh sửa file, hỏi cho các hành động khác
# plan           - Chỉ đọc phân tích, không sửa đổi
# dontAsk        - Chấp nhận tất cả hành động trừ các hành động rủi ro
# auto           - Bộ phân loại nền quyết định quyền tự động
# bypassPermissions - Chấp nhận tất cả hành động (yêu cầu --dangerously-skip-permissions)

# Quản lý phiên
/resume                # Tiếp tục cuộc hội thoại trước
/rename "name"         # Đặt tên cho phiên hiện tại
/fork                  # Fork phiên hiện tại
claude -c              # Tiếp tục cuộc hội thoại gần nhất
claude -r "session"    # Tiếp tục phiên theo tên/ID
```

---

## 📋 Bảng Cheat Sheet Tính Năng

| Tính Năng | Đường Dẫn Cài Đặt | Cách Sử Dụng |
|---------|-------------|-------|
| **Lệnh Slash (55+)** | `.claude/commands/*.md` | `/tên-lệnh` |
| **Bộ Nhớ** | `./CLAUDE.md` | Tự động tải |
| **Skills** | `.claude/skills/*/SKILL.md` | Tự động gọi |
| **Tác Nhân Con** | `.claude/agents/*.md` | Tự động ủy quyền |
| **MCP** | `.mcp.json` (dự án) hoặc `~/.claude.json` (người dùng) | `/mcp__server__action` |
| **Hooks (25 sự kiện)** | `~/.claude/hooks/*.sh` | Kích hoạt sự kiện (4 loại) |
| **Plugins** | Thông qua `/plugin install` | Gói tất cả |
| **Checkpoints** | Được tích hợp sẵn | `Esc+Esc` hoặc `/rewind` |
| **Chế Độ Lập Kế Hoạch** | Được tích hợp sẵn | `/plan <tác vụ>` |
| **Chế Độ Quyền (6)** | Được tích hợp sẵn | `--allowedTools`, `--permission-mode` |
| **Phiên Làm Việc** | Được tích hợp sẵn | `/session <lệnh>` |
| **Tác Vụ Nền** | Được tích hợp sẵn | Chạy trong nền |
| **Điều Khiển Từ Xa** | Được tích hợp sẵn | WebSocket API |
| **Phiên Web** | Được tích hợp sẵn | `claude web` |
| **Git Worktrees** | Được tích hợp sẵn | `/worktree` |
| **Tự Động Bộ Nhớ** | Được tích hợp sẵn | Tự động lưu vào CLAUDE.md |
| **Danh Sách Tác Vụ** | Được tích hợp sẵn | `/task list` |
| **Skills Được Gói (5)** | Được tích hợp sẵn | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 Trường Hợp Sử Dụng Phổ Biến

### Review Code
```bash
# Cách 1: Lệnh slash
cp 01-slash-commands/optimize.md .claude/commands/
# Sử dụng: /optimize

# Cách 2: Tác nhân con
cp 04-subagents/code-reviewer.md .claude/agents/
# Sử dụng: Tự động ủy quyền

# Cách 3: Skill
cp -r 03-skills/code-review ~/.claude/skills/
# Sử dụng: Tự động gọi

# Cách 4: Plugin (tốt nhất)
/plugin install pr-review
# Sử dụng: /review-pr
```

### Tài Liệu
```bash
# Lệnh slash
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Tác nhân con
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (giải pháp hoàn chỉnh)
/plugin install documentation
```

### DevOps
```bash
# Plugin hoàn chỉnh
/plugin install devops-automation

# Lệnh: /deploy, /rollback, /status, /incident
```

### Tiêu Chuẩn Đội
```bash
# Bộ nhớ dự án
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Chỉnh sửa cho đội của bạn
vim CLAUDE.md
```

### Tự Động Hóa & Hooks
```bash
# Cài đặt hooks (25 sự kiện, 4 loại: command, http, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Ví dụ:
# - Tests pre-commit: pre-commit.sh
# - Tự động định dạng code: format-code.sh
# - Quét bảo mật: security-scan.sh

# Chế độ Tự Động cho workflow hoàn toàn tự chủ
claude --enable-auto-mode -p "Refactor và test module auth"
# Hoặc chuyển đổi chế độ tương tác với Shift+Tab
```

### Refactor An Toàn
```bash
# Checkpoints được tạo tự động trước mỗi prompt
# Thử refactoring
# Nếu thành công: tiếp tục
# Nếu thất bại: nhấn Esc+Esc hoặc sử dụng /rewind để quay lại
```

### Triển Khai Phức Tạp
```bash
# Sử dụng chế độ lập kế hoạch
/plan Triển khai hệ thống xác thực người dùng

# Claude tạo kế hoạch chi tiết
# Xem xét và phê duyệt
# Claude triển khai có hệ thống
```

### Tích Hợp CI/CD
```bash
# Chạy ở chế độ headless (không tương tác)
claude -p "Chạy tất cả tests và tạo báo cáo"

# Với chế độ quyền cho CI
claude -p "Chạy tests" --permission-mode dontAsk

# Với Chế độ Tự Động cho tác vụ CI hoàn toàn tự chủ
claude --enable-auto-mode -p "Chạy tests và sửa lỗi thất bại"

# Với hooks để tự động hóa
# Xem 09-advanced-features/README.md
```

### Học & Thử Nghiệm
```bash
# Sử dụng chế độ kế hoạch để phân tích an toàn
claude --permission-mode plan

# Thử nghiệm an toàn - checkpoints được tạo tự động
# Nếu cần quay lại: nhấn Esc+Esc hoặc sử dụng /rewind
```

### Đội Tác Nhân
```bash
# Bật đội tác nhân
export CLAUDE_AGENT_TEAMS=1

# Hoặc trong settings.json
{ "agentTeams": { "enabled": true } }

# Bắt đầu với: "Triển khai tính năng X sử dụng cách tiếp cận đội"
```

### Tác Vụ Định Kỳ
```bash
# Chạy một lệnh mỗi 5 phút
/loop 5m /check-status

# Nhắc nhở một lần
/loop 30m "nhắc tôi kiểm tra deploy"
```

---

## 📁 Tham Khảo Vị Trí File

```
Dự Án Của Bạn/
├── .claude/
│   ├── commands/              # Lệnh slash đặt ở đây
│   ├── agents/                # Tác nhân con đặt ở đây
│   ├── skills/                # Skills dự án đặt ở đây
│   └── settings.json          # Cài đặt dự án (hooks, v.v.)
├── .mcp.json                  # Cấu hình MCP (phạm vi dự án)
├── CLAUDE.md                  # Bộ nhớ dự án
└── src/
    └── api/
        └── CLAUDE.md          # Bộ nhớ cụ thể thư mục

Home Người Dùng/
├── .claude/
│   ├── commands/              # Lệnh cá nhân
│   ├── agents/                # Tác nhân cá nhân
│   ├── skills/                # Skills cá nhân
│   ├── hooks/                 # Script hooks
│   ├── settings.json          # Cài đặt người dùng
│   ├── managed-settings.d/    # Cài đặt được quản lý (doanh nghiệp/tổ chức)
│   └── CLAUDE.md              # Bộ nhớ cá nhân
└── .claude.json               # Cấu hình MCP cá nhân (phạm vi người dùng)
```

---

## 🔍 Tìm Ví Dụ

### Theo Danh Mục
- **Lệnh Slash**: `01-slash-commands/`
- **Bộ Nhớ**: `02-memory/`
- **Skills**: `03-skills/`
- **Tác Nhân Con**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Tính Năng Nâng Cao**: `09-advanced-features/`
- **CLI**: `10-cli/`

### Theo Trường Hợp Sử Dụng
- **Hiệu Suất**: `01-slash-commands/optimize.md`
- **Bảo Mật**: `04-subagents/secure-reviewer.md`
- **Testing**: `04-subagents/test-engineer.md`
- **Tài Liệu**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### Theo Độ Phức Tạp
- **Đơn Giản**: Lệnh slash
- **Trung Bình**: Tác nhân con, Bộ nhớ
- **Nâng Cao**: Skills, Hooks
- **Hoàn Chỉnh**: Plugins

---

## 🎓 Lộ Trình Học

### Ngày 1
```bash
# Đọc tổng quan
cat README.md

# Cài đặt một lệnh
cp 01-slash-commands/optimize.md .claude/commands/

# Thử dùng
/optimize
```

### Ngày 2-3
```bash
# Thiết lập bộ nhớ
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Cài đặt tác nhân con
cp 04-subagents/code-reviewer.md .claude/agents/
```

### Ngày 4-5
```bash
# Thiết lập MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# Thử lệnh MCP
/mcp__github__list_prs
```

### Tuần 2
```bash
# Cài đặt skill
cp -r 03-skills/code-review ~/.claude/skills/

# Để nó tự động gọi
# Chỉ cần nói: "Review đoạn code này tìm lỗi"
```

### Tuần 3+
```bash
# Cài đặt plugin hoàn chỉnh
/plugin install pr-review

# Sử dụng tính năng được gói
/review-pr
/check-security
/check-tests
```

---

## Tính Năng Mới (Tháng 3/2026)

| Tính Năng | Mô Tả | Cách Sử Dụng |
|---------|-------------|-------|
| **Chế Độ Tự Động** | Vận hành hoàn toàn tự chủ với bộ phân loại nền | Cờ `--enable-auto-mode`, `Shift+Tab` để chuyển đổi chế độ |
| **Kênh** | Tích hợp Discord và Telegram | Cờ `--channels`, bot Discord/Telegram |
| **Nhập Liệu Giọng Nói** | Nói lệnh và bối cảnh cho Claude | Lệnh `/voice` |
| **Hooks (25 sự kiện)** | Hệ thống hook mở rộng với 4 loại | Các loại hook command, http, prompt, agent |
| **MCP Elicitation** | MCP servers có thể yêu cầu input người dùng tại runtime | Tự động nhắc khi server cần làm rõ |
| **WebSocket MCP** | Vận chuyển WebSocket cho kết nối MCP | Cấu hình trong `.mcp.json` với URL `ws://` |
| **Plugin LSP** | Hỗ trợ Language Server Protocol cho plugins | `userConfig`, biến `${CLAUDE_PLUGIN_DATA}` |
| **Điều Khiển Từ Xa** | Điều khiển Claude Code qua WebSocket API | `claude --remote` cho tích hợp bên ngoài |
| **Phiên Web** | Giao diện Claude Code trên trình duyệt | `claude web` để khởi động |
| **Ứng Dụng Desktop** | Ứng dụng desktop native | Tải từ claude.ai/download |
| **Danh Sách Tác Vụ** | Quản lý tác vụ nền | `/task list`, `/task status <id>` |
| **Tự Động Bộ Nhớ** | Tự động lưu bộ nhớ từ cuộc hội thoại | Claude tự động lưu bối cảnh chính vào CLAUDE.md |
| **Git Worktrees** | Không gian làm việc cô lập cho phát triển song song | `/worktree` để tạo không gian làm việc cô lập |
| **Chọn Mô Hình** | Chuyển đổi giữa Sonnet 4.6 và Opus 4.6 | `/model` hoặc cờ `--model` |
| **Đội Tác Nhân** | Phối hợp nhiều tác nhân trên tác vụ | Bật với biến môi trường `CLAUDE_AGENT_TEAMS=1` |
| **Tác Vụ Định Kỳ** | Tác vụ định kỳ với `/loop` | `/loop 5m /command` hoặc công cụ CronCreate |
| **Tích Hợp Chrome** | Tự động hóa trình duyệt | Cờ `--chrome` hoặc lệnh `/chrome` |
| **Tùy Chỉnh Bàn Phím** | Phím tắt tùy chỉnh | Lệnh `/keybindings` |

---

## Mẹo & Thủ Thuật

### Tùy Chỉnh
- Bắt đầu với ví dụ nguyên trạng
- Chỉnh sửa phù hợp nhu cầu của bạn
- Thử nghiệm trước khi chia sẻ với đội
- Sử dụng version control cho cấu hình của bạn

### Thực Hành Tốt Nhất
- Sử dụng bộ nhớ cho tiêu chuẩn đội
- Sử dụng plugins cho workflow hoàn chỉnh
- Sử dụng tác nhân con cho tác vụ phức tạp
- Sử dụng lệnh slash cho tác vụ nhanh

### Xử Lý Sự Cố
```bash
# Kiểm tra vị trí file
ls -la .claude/commands/
ls -la .claude/agents/

# Xác minh cú pháp YAML
head -20 .claude/agents/code-reviewer.md

# Kiểm tra kết nối MCP
echo $GITHUB_TOKEN
```

---

## 📊 Ma Trận Tính Năng

| Nhu Cầu | Sử Dụng Cái Này | Ví Dụ |
|------|----------|---------|
| Lối tắt nhanh | Lệnh Slash (55+) | `01-slash-commands/optimize.md` |
| Tiêu chuẩn đội | Bộ Nhớ | `02-memory/project-CLAUDE.md` |
| Workflow tự động | Skill | `03-skills/code-review/` |
| Tác vụ chuyên biệt | Tác Nhân Con | `04-subagents/code-reviewer.md` |
| Dữ liệu bên ngoài | MCP (+ Elicitation, WebSocket) | `05-mcp/github-mcp.json` |
| Tự động hóa sự kiện | Hook (25 sự kiện, 4 loại) | `06-hooks/pre-commit.sh` |
| Giải pháp hoàn chỉnh | Plugin (+ hỗ trợ LSP) | `07-plugins/pr-review/` |
| Thử nghiệm an toàn | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| Hoàn toàn tự chủ | Chế Độ Tự Động | `--enable-auto-mode` hoặc `Shift+Tab` |
| Tích hợp chat | Kênh | `--channels` (Discord, Telegram) |
| Pipeline CI/CD | CLI | `10-cli/README.md` |

---

## 🔗 Liên Kết Nhanh

- **Hướng Dẫn Chính**: `README.md`
- **Index Hoàn Chỉnh**: `INDEX.md`
- **Tóm Tắt**: `EXAMPLES_SUMMARY.md`
- **Hướng Dẫn Gốc**: `claude_concepts_guide.md`

---

## 📞 Câu Hỏi Phổ Biến

**Câu: Tôi nên dùng cái nào?**
Đáp: Bắt đầu với lệnh slash, thêm tính năng khi cần.

**Câu: Tôi có thể kết hợp tính năng không?**
Đáp: Có! Chúng hoạt động cùng nhau. Bộ Nhớ + Lệnh + MCP = mạnh mẽ.

**Câu: Làm sao chia sẻ với đội?**
Đáp: Commit thư mục `.claude/` vào git.

**Câu: Còn bí mật thì sao?**
Đáp: Sử dụng biến môi trường, không bao giờ hardcode.

**Câu: Tôi có thể sửa ví dụ không?**
Đáp: Chắc chắn rồi! Chúng là mẫu để tùy chỉnh.

---

## ✅ Checklist

Checklist bắt đầu:

- [ ] Đọc `README.md`
- [ ] Cài đặt 1 lệnh slash
- [ ] Thử lệnh đó
- [ ] Tạo `CLAUDE.md` dự án
- [ ] Cài đặt 1 tác nhân con
- [ ] Thiết lập 1 tích hợp MCP
- [ ] Cài đặt 1 skill
- [ ] Thử một plugin hoàn chỉnh
- [ ] Tùy chỉnh cho nhu cầu của bạn
- [ ] Chia sẻ với đội

---

**Bắt Đầu Nhanh**: `cat README.md`

**Index Hoàn Chỉnh**: `cat INDEX.md`

**Tham Khảo Này**: Giữ sẵn để tham khảo nhanh!
