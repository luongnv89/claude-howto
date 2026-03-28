<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Tính Năng Nâng Cao

Hướng dẫn toàn diện về các tính năng nâng cao của Claude Code bao gồm chế độ lập kế hoạch (planning mode), suy nghĩ mở rộng (extended thinking), chế độ tự động (auto mode), tác vụ nền (background tasks), chế độ phân quyền (permission modes), chế độ in (print mode - phi tương tác), quản lý phiên làm việc, tính năng tương tác, kênh truyền thông, nhập liệu bằng giọng nói, điều khiển từ xa (remote control), phiên web (web sessions), ứng dụng desktop (desktop app), danh sách tác vụ (task list), gợi ý lệnh (prompt suggestions), git worktrees, sandbox, cài đặt quản lý (managed settings) và cấu hình.

## Mục Lục

1. [Tổng Quan](#tổng-quan)
2. [Chế Độ Lập Kế Hoạch](#chế-độ-lập-kế-hoạch)
3. [Suy Nghĩ Mở Rộng](#suy-nghĩ-mở-rộng)
4. [Chế Độ Tự Động](#chế-độ-tự-động)
5. [Tác Vụ Nền](#tác-vụ-nền)
6. [Tác Vụ Theo Lịch](#tác-vụ-theo-lịch)
7. [Chế Độ Phân Quyền](#chế-độ-phân-quyền)
8. [Chế Độ Headless](#chế-độ-headless)
9. [Quản Lý Phiên Làm Việc](#quản-lý-phiên-làm-việc)
10. [Tính Năng Tương Tác](#tính-năng-tương-tác)
11. [Nhập Liệu Bằng Giọng Nói](#nhập-liệu-bằng-giọng-nói)
12. [Kênh Truyền Thông](#kênh-truyền-thông)
13. [Tích Hợp Chrome](#tích-hợp-chrome)
14. [Điều Khiển Từ Xa](#điều-khiển-từ-xa)
15. [Phiên Web](#phiên-web)
16. [Ứng Dụng Desktop](#ứng-dụng-desktop)
17. [Danh Sách Tác Vụ](#danh-sách-tác-vụ)
18. [Gợi Ý Lệnh](#gợi-ý-lệnh)
19. [Git Worktrees](#git-worktrees)
20. [Sandboxing](#sandboxing)
21. [Cài Đặt Quản Lý (Enterprise)](#cài-đặt-quản-lý-enterprise)
22. [Cấu Hình và Thiết Lập](#cấu-hình-và-thiết-lập)
23. [Thực Hành Tốt Nhất](#thực-hành-tốt-nhất)
24. [Tài Nguyên Liên Quan](#tài-nguyên-liên-quan)

---

## Tổng Quan

Các tính năng nâng cao trong Claude Code mở rộng khả năng cốt lõi với cơ chế lập kế hoạch, suy luận, tự động hóa và kiểm soát. Những tính năng này cho phép các quy trình làm việc phức tạp cho các tác vụ phát triển phức tạp, review code, tự động hóa và quản lý đa phiên.

**Các tính năng nâng cao chính bao gồm:**
- **Planning Mode**: Tạo kế hoạch triển khai chi tiết trước khi lập trình
- **Extended Thinking**: Suy luận sâu cho các vấn đề phức tạp
- **Auto Mode**: Bộ phân loại an toàn nền xem xét mỗi hành động trước khi thực thi (Research Preview)
- **Background Tasks**: Chạy các hoạt động dài mà không chặn cuộc hội thoại
- **Permission Modes**: Kiểm soát những gì Claude có thể làm (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Print Mode**: Chạy Claude Code phi tương tác cho tự động hóa và CI/CD (`claude -p`)
- **Session Management**: Quản lý nhiều phiên làm việc
- **Interactive Features**: Phím tắt, nhập đa dòng và lịch sử lệnh
- **Voice Dictation**: Nhập liệu bằng giọng nói push-to-talk hỗ trợ 20 ngôn ngữ STT
- **Channels**: Các MCP server đẩy tin nhắn vào phiên đang chạy (Research Preview)
- **Remote Control**: Điều khiển Claude Code từ Claude.ai hoặc ứng dụng Claude
- **Web Sessions**: Chạy Claude Code trên trình duyệt tại claude.ai/code
- **Desktop App**: Ứng dụng độc lập cho review diff trực quan và nhiều phiên song song
- **Task List**: Theo dõi tác vụ liên tục qua các lần nén context
- **Prompt Suggestions**: Gợi ý lệnh thông minh dựa trên ngữ cảnh
- **Git Worktrees**: Các nhánh worktree cách ly cho công việc song song
- **Sandboxing**: Cách ly filesystem và mạng ở cấp độ OS
- **Managed Settings**: Triển khai enterprise qua plist, Registry hoặc file quản lý
- **Configuration**: Tùy chỉnh hành vi với file cấu hình JSON

---

## Chế Độ Lập Kế Hoạch

Chế độ lập kế hoạch cho phép Claude suy nghĩ qua các tác vụ phức tạp trước khi triển khai, tạo ra một kế hoạch chi tiết để bạn có thể xem xét và phê duyệt.

### Planning Mode là gì?

Planning mode là phương pháp hai giai đoạn:
1. **Giai đoạn Lập Kế Hoạch**: Claude phân tích tác vụ và tạo kế hoạch triển khai chi tiết
2. **Giai đoạn Triển Khai**: Sau khi phê duyệt, Claude thực thi kế hoạch

### Khi Nào Dùng Planning Mode

✅ Dùng planning mode cho:
- Tái cấu trúc phức tạp nhiều file
- Triển khai tính năng mới
- Thay đổi kiến trúc
- Migration database
- Thiết kế lại API lớn

❌ Không dùng planning mode cho:
- Sửa lỗi đơn giản
- Thay đổi định dạng
- Chỉnh sửa một file
- Câu hỏi nhanh

### Kích Hoạt Planning Mode

**Slash command**:
```bash
/plan Implement user authentication system
```

**CLI flag**:
```bash
claude --permission-mode plan
```

**Đặt làm mặc định**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Phím tắt**:
- `Shift + Tab` - Chuyển đổi các chế độ phân quyền (bao gồm plan)
- `Alt + M` - Chuyển đổi chế độ phân quyền (Windows/Linux)

### Lợi Ích Của Planning Mode

- **Phương pháp triển khai có cấu trúc**: Phân tách chi tiết các bước triển khai
- **Xem xét và phê duyệt**: Phê duyệt hoặc điều chỉnh kế hoạch trước khi thực thi
- **Xác định rủi ro**: Nhận diện các vấn đề tiềm ẩn trước khi triển khai
- **Giai đoạn rõ ràng**: Các giai đoạn và mốc triển khai được tổ chức

### Ví Dụ: Triển Khai Tính Năng

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### Sửa Đổi Kế Hoạch

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Cấu Hình Planning Mode

Planning mode được kích hoạt qua CLI flag hoặc slash command:

```bash
# Kích hoạt plan mode qua CLI
claude --permission-mode plan

# Hoặc dùng slash command /plan trong REPL
/plan Implement user authentication system
```

**Model alias cho planning**: Dùng `opusplan` làm model alias để sử dụng Opus cho lập kế hoạch và Sonnet cho thực thi:

```bash
claude --model opusplan "design and implement the new API"
```

**Chỉnh sửa kế hoạch bên ngoài**: Nhấn `Ctrl+G` để mở kế hoạch hiện tại trong trình soạn thảo ngoài để sửa đổi chi tiết.

---

## Suy Nghĩ Mở Rộng

Extended thinking (suy nghĩ mở rộng) cho phép Claude dành nhiều thời gian hơn để suy luận về các vấn đề phức tạp trước khi đưa ra giải pháp.

### Extended Thinking là gì?

Extended thinking là quá trình suy luận từng bước có chủ ý, trong đó Claude:
- Phân tích các vấn đề phức tạp
- Xem xét nhiều cách tiếp cận
- Đánh giá sự đánh đổi
- Suy luận qua các trường hợp biên

### Kích Hoạt Extended Thinking

**Phím tắt**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - Bật/tắt extended thinking

**Kích hoạt tự động**:
- Bật theo mặc định cho tất cả model (Opus 4.6, Sonnet 4.6, Haiku 4.5)
- Opus 4.6: Suy luận thích ứng với mức độ effort: `low` (○), `medium` (◐), `high` (●), `max` (chỉ Opus 4.6)
- Các model khác: Ngân sách cố định tối đa 31.999 token

**Phương thức cấu hình**:
- Bật/tắt: `Alt+T` / `Option+T`, hoặc qua `/config`
- Xem suy luận: `Ctrl+O` (chế độ verbose)
- Đặt effort: lệnh `/effort` hoặc flag `--effort`

**Ngân sách tùy chỉnh**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Mức độ effort** (chỉ Opus 4.6):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), hoặc max (chỉ Opus 4.6)
```

**CLI flag**:
```bash
claude --effort high "complex architectural review"
```

**Slash command**:
```
/effort high
```

> **Lưu ý:** Từ khóa "ultrathink" trong prompt kích hoạt chế độ suy luận sâu. Mức độ effort `low`, `medium`, `high` và `max` (chỉ Opus 4.6) kiểm soát mức độ suy luận mà Claude thực hiện.

### Lợi Ích Của Extended Thinking

- **Suy luận sâu**: Dành nhiều thời gian hơn để suy nghĩ về các vấn đề phức tạp
- **Quyết định kiến trúc tốt hơn**: Đưa ra lựa chọn có thông tin với đánh giá toàn diện
- **Xem xét các trường hợp biên**: Suy nghĩ qua các vấn đề và kịch bản tiềm ẩn
- **Phân tích kỹ lưỡng**: Phương pháp có cấu trúc để giải quyết vấn đề phức tạp

### Ví Dụ: Quyết Định Kiến Trúc

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### Cấu Hình Extended Thinking

Extended thinking được kiểm soát qua biến môi trường, phím tắt và CLI flag:

```bash
# Đặt ngân sách token suy nghĩ
export MAX_THINKING_TOKENS=16000

# Đặt mức độ effort (chỉ Opus 4.6): low (○), medium (◐), high (●), hoặc max (chỉ Opus 4.6)
export CLAUDE_CODE_EFFORT_LEVEL=high
```

Bật/tắt trong phiên làm việc với `Alt+T` / `Option+T`, đặt effort với `/effort`, hoặc cấu hình qua `/config`.

---

## Chế Độ Tự Động

Auto Mode là chế độ phân quyền Research Preview (tháng 3 năm 2026) sử dụng bộ phân loại an toàn nền để xem xét mỗi hành động trước khi thực thi. Nó cho phép Claude làm việc tự chủ trong khi chặn các hoạt động nguy hiểm.

### Yêu Cầu

- **Plan**: Team plan (Enterprise và API đang được triển khai)
- **Model**: Claude Sonnet 4.6 hoặc Opus 4.6
- **Classifier**: Chạy trên Claude Sonnet 4.6 (thêm chi phí token)

### Bật Auto Mode

```bash
# Mở khóa auto mode bằng CLI flag
claude --enable-auto-mode

# Sau đó chuyển đến nó bằng Shift+Tab trong REPL
```

Hoặc đặt làm chế độ phân quyền mặc định:

```bash
claude --permission-mode auto
```

Cài đặt qua config:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Cách Bộ Phân Loại Hoạt Động

Bộ phân loại nền đánh giá mỗi hành động theo thứ tự quyết định sau:

1. **Quy tắc cho phép/từ chối** -- Các quy tắc phân quyền tường minh được kiểm tra trước
2. **Chỉ đọc/chỉnh sửa tự động phê duyệt** -- Đọc và chỉnh sửa file tự động được phép
3. **Classifier** -- Bộ phân loại nền xem xét hành động
4. **Dự phòng** -- Chuyển sang hỏi người dùng sau 3 lần chặn liên tiếp hoặc 20 lần chặn tổng cộng

### Các Hành Động Bị Chặn Mặc Định

Auto mode chặn các hành động sau theo mặc định:

| Hành Động Bị Chặn | Ví Dụ |
|-------------------|-------|
| Cài đặt pipe-to-shell | `curl \| bash` |
| Gửi dữ liệu nhạy cảm ra ngoài | API key, thông tin xác thực qua mạng |
| Triển khai production | Lệnh deploy nhắm vào production |
| Xóa hàng loạt | `rm -rf` trên thư mục lớn |
| Thay đổi IAM | Sửa đổi quyền và vai trò |
| Force push lên main | `git push --force origin main` |

### Các Hành Động Được Phép Mặc Định

| Hành Động Được Phép | Ví Dụ |
|--------------------|-------|
| Thao tác file cục bộ | Đọc, ghi, chỉnh sửa file dự án |
| Cài đặt dependency đã khai báo | `npm install`, `pip install` từ manifest |
| HTTP chỉ đọc | `curl` để lấy tài liệu |
| Push lên nhánh hiện tại | `git push origin feature-branch` |

### Cấu Hình Auto Mode

**In các quy tắc mặc định dạng JSON**:
```bash
claude auto-mode defaults
```

**Cấu hình cơ sở hạ tầng tin cậy** qua cài đặt quản lý `autoMode.environment` cho triển khai enterprise. Điều này cho phép quản trị viên định nghĩa các môi trường CI/CD tin cậy, mục tiêu triển khai và các mẫu cơ sở hạ tầng.

### Hành Vi Dự Phòng

Khi bộ phân loại không chắc chắn, auto mode chuyển sang hỏi người dùng:
- Sau **3 lần chặn liên tiếp** của bộ phân loại
- Sau **20 lần chặn tổng cộng** trong một phiên

Điều này đảm bảo người dùng luôn giữ quyền kiểm soát khi bộ phân loại không thể tự tin phê duyệt một hành động.

---

## Tác Vụ Nền

Tác vụ nền cho phép các hoạt động chạy dài thực thi mà không chặn cuộc hội thoại của bạn.

### Tác Vụ Nền là gì?

Tác vụ nền chạy không đồng bộ trong khi bạn tiếp tục làm việc:
- Bộ test lớn
- Quá trình build
- Migration database
- Script triển khai
- Công cụ phân tích

**Cách dùng cơ bản:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Hiển thị tất cả tác vụ
/task status bg-1234 # Kiểm tra tiến độ
/task show bg-1234   # Xem output
/task cancel bg-1234 # Hủy tác vụ
```

### Khởi Động Tác Vụ Nền

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### Quản Lý Tác Vụ Nền

**Liệt kê tác vụ đang hoạt động**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**Kiểm tra trạng thái tác vụ**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**Xem output tác vụ**:
```
User: /task show bg-1234

[Shows live output from the test run]
```

**Hủy tác vụ**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### Ví Dụ: Phát Triển Song Song

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### Cấu Hình

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Tác Vụ Theo Lịch

Scheduled Tasks (tác vụ theo lịch) cho phép bạn chạy các prompt tự động theo lịch lặp lại hoặc như lời nhắc một lần. Tác vụ có phạm vi phiên — chúng chạy trong khi Claude Code đang hoạt động và bị xóa khi phiên kết thúc. Có sẵn từ v2.1.72+.

### Lệnh `/loop`

```bash
# Khoảng thời gian tường minh
/loop 5m check if the deployment finished

# Ngôn ngữ tự nhiên
/loop check build status every 30 minutes
```

Các biểu thức cron 5 trường tiêu chuẩn cũng được hỗ trợ để lập lịch chính xác.

### Lời Nhắc Một Lần

Đặt lời nhắc chỉ bắt đầu một lần tại thời điểm cụ thể:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Quản Lý Tác Vụ Theo Lịch

| Tool | Mô Tả |
|------|--------|
| `CronCreate` | Tạo tác vụ theo lịch mới |
| `CronList` | Liệt kê tất cả tác vụ theo lịch đang hoạt động |
| `CronDelete` | Xóa tác vụ theo lịch |

**Giới hạn và hành vi**:
- Tối đa **50 tác vụ theo lịch** mỗi phiên
- Phạm vi phiên — bị xóa khi phiên kết thúc
- Tác vụ lặp lại tự động hết hạn sau **3 ngày**
- Tác vụ chỉ kích hoạt trong khi Claude Code đang chạy — không bắt kịp các lần bị bỏ lỡ

### Chi Tiết Hành Vi

| Khía Cạnh | Chi Tiết |
|-----------|---------|
| **Jitter lặp lại** | Tối đa 10% của khoảng thời gian (tối đa 15 phút) |
| **Jitter một lần** | Tối đa 90 giây trên ranh giới :00/:30 |
| **Lần bị bỏ lỡ** | Không bắt kịp — bị bỏ qua nếu Claude Code không chạy |
| **Persistence** | Không được lưu qua các lần khởi động lại |

### Tác Vụ Theo Lịch Trên Cloud

Dùng `/schedule` để tạo tác vụ theo lịch Cloud chạy trên cơ sở hạ tầng Anthropic:

```
/schedule daily at 9am run the test suite and report failures
```

Tác vụ theo lịch Cloud được lưu qua các lần khởi động lại và không yêu cầu Claude Code đang chạy cục bộ.

### Tắt Tác Vụ Theo Lịch

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### Ví Dụ: Theo Dõi Triển Khai

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Mẹo**: Tác vụ theo lịch có phạm vi phiên. Để tự động hóa liên tục tồn tại qua các lần khởi động lại, hãy dùng CI/CD pipelines, GitHub Actions hoặc tác vụ theo lịch của Desktop App.

---

## Chế Độ Phân Quyền

Chế độ phân quyền kiểm soát những hành động nào Claude có thể thực hiện mà không cần phê duyệt rõ ràng.

### Các Chế Độ Phân Quyền Có Sẵn

| Chế Độ | Hành Vi |
|--------|---------|
| `default` | Chỉ đọc file; nhắc cho tất cả các hành động khác |
| `acceptEdits` | Đọc và chỉnh sửa file; nhắc cho các lệnh |
| `plan` | Chỉ đọc file (chế độ nghiên cứu, không chỉnh sửa) |
| `auto` | Tất cả hành động với kiểm tra bộ phân loại an toàn nền (Research Preview) |
| `bypassPermissions` | Tất cả hành động, không kiểm tra quyền (nguy hiểm) |
| `dontAsk` | Chỉ các tool được phê duyệt trước thực thi; tất cả các tool khác bị từ chối |

Chuyển đổi giữa các chế độ bằng `Shift+Tab` trong CLI. Đặt mặc định bằng flag `--permission-mode` hoặc cài đặt `permissions.defaultMode`.

### Phương Thức Kích Hoạt

**Phím tắt**:
```bash
Shift + Tab  # Chuyển đổi qua cả 6 chế độ
```

**Slash command**:
```bash
/plan                  # Vào chế độ plan
```

**CLI flag**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Setting**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Ví Dụ Về Chế Độ Phân Quyền

#### Chế Độ Default
Claude yêu cầu xác nhận cho các hành động quan trọng:

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Chế Độ Plan
Xem xét kế hoạch triển khai trước khi thực thi:

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### Chế Độ Accept Edits
Tự động chấp nhận các sửa đổi file:

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### Các Trường Hợp Sử Dụng

**Review Code**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Lập Trình Cùng Nhau**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Tác Vụ Tự Động**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## Chế Độ Headless

Print mode (`claude -p`) cho phép Claude Code chạy mà không có đầu vào tương tác, hoàn hảo cho tự động hóa và CI/CD. Đây là chế độ phi tương tác, thay thế flag `--headless` cũ.

### Print Mode là gì?

Print mode cho phép:
- Thực thi script tự động
- Tích hợp CI/CD
- Xử lý hàng loạt
- Tác vụ theo lịch

### Chạy Trong Print Mode (Phi Tương Tác)

```bash
# Chạy tác vụ cụ thể
claude -p "Run all tests"

# Xử lý nội dung được pipe
cat error.log | claude -p "Analyze these errors"

# Tích hợp CI/CD (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Các Ví Dụ Dùng Print Mode Bổ Sung

```bash
# Chạy tác vụ cụ thể với lưu output
claude -p "Run all tests and generate coverage report"

# Với output có cấu trúc
claude -p --output-format json "Analyze code quality"

# Với đầu vào từ stdin
echo "Analyze code quality" | claude -p "explain this"
```

### Ví Dụ: Tích Hợp CI/CD

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Cấu Hình Print Mode

Print mode (`claude -p`) hỗ trợ nhiều flag cho tự động hóa:

```bash
# Giới hạn số lượt tự chủ
claude -p --max-turns 5 "refactor this module"

# Output JSON có cấu trúc
claude -p --output-format json "analyze this codebase"

# Với xác thực schema
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Tắt lưu phiên
claude -p --no-session-persistence "one-off analysis"
```

---

## Quản Lý Phiên Làm Việc

Quản lý nhiều phiên Claude Code hiệu quả.

### Lệnh Quản Lý Phiên

| Lệnh | Mô Tả |
|------|--------|
| `/resume` | Tiếp tục cuộc hội thoại theo ID hoặc tên |
| `/rename` | Đặt tên cho phiên hiện tại |
| `/fork` | Fork phiên hiện tại thành nhánh mới |
| `claude -c` | Tiếp tục cuộc hội thoại gần nhất |
| `claude -r "session"` | Tiếp tục phiên theo tên hoặc ID |

### Tiếp Tục Phiên

**Tiếp tục cuộc hội thoại cuối**:
```bash
claude -c
```

**Tiếp tục phiên có tên**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Đặt tên phiên hiện tại** (trong REPL):
```
/rename auth-refactor
```

### Fork Phiên

Fork một phiên để thử cách tiếp cận khác mà không mất phiên ban đầu:

```
/fork
```

Hoặc từ CLI:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Lưu Phiên

Các phiên được tự động lưu và có thể tiếp tục:

```bash
# Tiếp tục cuộc hội thoại cuối
claude -c

# Tiếp tục phiên cụ thể theo tên hoặc ID
claude -r "auth-refactor"

# Tiếp tục và fork để thử nghiệm
claude --resume auth-refactor --fork-session "alternative approach"
```

---

## Tính Năng Tương Tác

### Phím Tắt

Claude Code hỗ trợ phím tắt để tăng hiệu quả. Dưới đây là tài liệu tham khảo đầy đủ từ tài liệu chính thức:

| Phím Tắt | Mô Tả |
|----------|--------|
| `Ctrl+C` | Hủy đầu vào/quá trình tạo hiện tại |
| `Ctrl+D` | Thoát Claude Code |
| `Ctrl+G` | Chỉnh sửa kế hoạch trong trình soạn thảo ngoài |
| `Ctrl+L` | Xóa màn hình terminal |
| `Ctrl+O` | Bật/tắt output verbose (xem suy luận) |
| `Ctrl+R` | Tìm kiếm ngược lịch sử |
| `Ctrl+T` | Bật/tắt chế độ xem danh sách tác vụ |
| `Ctrl+B` | Các tác vụ đang chạy nền |
| `Esc+Esc` | Tua lại code/cuộc hội thoại |
| `Shift+Tab` / `Alt+M` | Chuyển đổi chế độ phân quyền |
| `Option+P` / `Alt+P` | Chuyển đổi model |
| `Option+T` / `Alt+T` | Bật/tắt extended thinking |

**Chỉnh Sửa Dòng (phím tắt readline tiêu chuẩn):**

| Phím Tắt | Hành Động |
|----------|-----------|
| `Ctrl + A` | Di chuyển đến đầu dòng |
| `Ctrl + E` | Di chuyển đến cuối dòng |
| `Ctrl + K` | Cắt đến cuối dòng |
| `Ctrl + U` | Cắt đến đầu dòng |
| `Ctrl + W` | Xóa từ về phía sau |
| `Ctrl + Y` | Dán (yank) |
| `Tab` | Tự động hoàn thành |
| `↑ / ↓` | Lịch sử lệnh |

### Tùy Chỉnh Phím Tắt

Tạo phím tắt bàn phím tùy chỉnh bằng cách chạy `/keybindings`, mở `~/.claude/keybindings.json` để chỉnh sửa (v2.1.18+).

**Định dạng cấu hình**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

Đặt binding thành `null` để hủy liên kết phím tắt mặc định.

### Các Context Có Sẵn

Các keybinding được giới hạn trong các context UI cụ thể:

| Context | Các Hành Động Phím |
|---------|-------------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | Điều hướng cài đặt theo context |
| **Tabs** | Chuyển đổi và quản lý tab |
| **Help** | Điều hướng panel trợ giúp |

Có tổng cộng 18 context bao gồm `Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker` và `Select`.

### Hỗ Trợ Chord

Keybindings hỗ trợ chuỗi chord (kết hợp nhiều phím):

```
"ctrl+k ctrl+s"   → Chuỗi hai phím: nhấn ctrl+k, rồi ctrl+s
"ctrl+shift+p"    → Phím modifier đồng thời
```

**Cú pháp phím**:
- **Modifiers**: `ctrl`, `alt` (hoặc `opt`), `shift`, `meta` (hoặc `cmd`)
- **Chữ hoa ngụ ý Shift**: `K` tương đương với `shift+k`
- **Phím đặc biệt**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, phím mũi tên

### Phím Dành Riêng và Xung Đột

| Phím | Trạng Thái | Ghi Chú |
|------|-----------|---------|
| `Ctrl+C` | Dành riêng | Không thể rebind (ngắt) |
| `Ctrl+D` | Dành riêng | Không thể rebind (thoát) |
| `Ctrl+B` | Xung đột terminal | Phím tiền tố tmux |
| `Ctrl+A` | Xung đột terminal | Phím tiền tố GNU Screen |
| `Ctrl+Z` | Xung đột terminal | Tạm dừng tiến trình |

> **Mẹo**: Nếu phím tắt không hoạt động, kiểm tra xung đột với terminal emulator hoặc multiplexer của bạn.

### Tab Completion

Claude Code cung cấp tab completion thông minh:

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### Lịch Sử Lệnh

Truy cập các lệnh trước đó:

```
User: <↑>  # Lệnh trước
User: <↓>  # Lệnh tiếp theo
User: Ctrl+R  # Tìm kiếm lịch sử

(reverse-i-search)`test': run all tests
```

### Nhập Đa Dòng

Cho các câu hỏi phức tạp, dùng chế độ đa dòng:

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Ví dụ:**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### Chỉnh Sửa Inline

Chỉnh sửa lệnh trước khi gửi:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Chế Độ Vim

Bật các keybinding Vi/Vim để chỉnh sửa văn bản:

**Kích hoạt**:
- Dùng lệnh `/vim` hoặc `/config` để bật
- Chuyển đổi chế độ bằng `Esc` cho NORMAL, `i/a/o` cho INSERT

**Phím điều hướng**:
- `h` / `l` - Di chuyển trái/phải
- `j` / `k` - Di chuyển xuống/lên
- `w` / `b` / `e` - Di chuyển theo từ
- `0` / `$` - Di chuyển đến đầu/cuối dòng
- `gg` / `G` - Nhảy đến đầu/cuối văn bản

**Text objects**:
- `iw` / `aw` - Bên trong/xung quanh từ
- `i"` / `a"` - Bên trong/xung quanh chuỗi có dấu nháy
- `i(` / `a(` - Bên trong/xung quanh dấu ngoặc đơn

### Chế Độ Bash

Thực thi lệnh shell trực tiếp với tiền tố `!`:

```bash
! npm test
! git status
! cat src/index.js
```

Dùng cái này để thực thi lệnh nhanh mà không cần chuyển ngữ cảnh.

---

## Nhập Liệu Bằng Giọng Nói

Voice Dictation (nhập liệu bằng giọng nói) cung cấp đầu vào giọng nói push-to-talk cho Claude Code, cho phép bạn nói prompt thay vì gõ.

### Kích Hoạt Voice Dictation

```
/voice
```

### Tính Năng

| Tính Năng | Mô Tả |
|----------|--------|
| **Push-to-talk** | Giữ phím để ghi âm, thả ra để gửi |
| **20 ngôn ngữ** | Speech-to-text hỗ trợ 20 ngôn ngữ |
| **Phím tắt tùy chỉnh** | Cấu hình phím push-to-talk qua `/keybindings` |
| **Yêu cầu tài khoản** | Yêu cầu tài khoản Claude.ai để xử lý STT |

### Cấu Hình

Tùy chỉnh keybinding push-to-talk trong file keybindings của bạn (`/keybindings`). Voice dictation dùng tài khoản Claude.ai của bạn để xử lý speech-to-text.

---

## Kênh Truyền Thông

Channels (Research Preview) cho phép các MCP server đẩy tin nhắn vào các phiên Claude Code đang chạy, cho phép tích hợp thời gian thực với các dịch vụ bên ngoài.

### Đăng Ký Kênh

```bash
# Đăng ký channel plugins khi khởi động
claude --channels discord,telegram
```

### Các Tích Hợp Được Hỗ Trợ

| Tích Hợp | Mô Tả |
|---------|--------|
| **Discord** | Nhận và phản hồi tin nhắn Discord trong phiên của bạn |
| **Telegram** | Nhận và phản hồi tin nhắn Telegram trong phiên của bạn |

### Cấu Hình

**Cài đặt quản lý** cho triển khai enterprise:

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

Cài đặt `allowedChannelPlugins` kiểm soát các channel plugin nào được phép trong toàn tổ chức.

### Cách Hoạt Động

1. Các MCP server hoạt động như channel plugin kết nối với các dịch vụ bên ngoài
2. Tin nhắn đến được đẩy vào phiên Claude Code đang hoạt động
3. Claude có thể đọc và phản hồi tin nhắn trong ngữ cảnh phiên
4. Channel plugin phải được phê duyệt qua cài đặt quản lý `allowedChannelPlugins`

---

## Tích Hợp Chrome

Chrome Integration (tích hợp Chrome) kết nối Claude Code với trình duyệt Chrome hoặc Microsoft Edge của bạn để tự động hóa và debug web trực tiếp. Đây là tính năng beta có sẵn từ v2.0.73+ (hỗ trợ Edge được thêm trong v1.0.36+).

### Bật Tích Hợp Chrome

**Khi khởi động**:

```bash
claude --chrome      # Bật kết nối Chrome
claude --no-chrome   # Tắt kết nối Chrome
```

**Trong phiên làm việc**:

```
/chrome
```

Chọn "Enabled by default" để kích hoạt Chrome Integration cho tất cả phiên trong tương lai. Claude Code chia sẻ trạng thái đăng nhập trình duyệt của bạn, vì vậy nó có thể tương tác với các ứng dụng web đã xác thực.

### Khả Năng

| Khả Năng | Mô Tả |
|---------|--------|
| **Debug trực tiếp** | Đọc console log, kiểm tra phần tử DOM, debug JavaScript theo thời gian thực |
| **Xác minh thiết kế** | So sánh các trang đã render với mockup thiết kế |
| **Xác thực form** | Test gửi form, xác thực đầu vào và xử lý lỗi |
| **Test ứng dụng web** | Tương tác với các ứng dụng đã xác thực (Gmail, Google Docs, Notion, v.v.) |
| **Trích xuất dữ liệu** | Scrape và xử lý nội dung từ trang web |
| **Ghi phiên** | Ghi lại các tương tác trình duyệt dưới dạng file GIF |

### Quyền Theo Trang

Chrome extension quản lý quyền truy cập theo từng trang. Cấp hoặc thu hồi quyền truy cập cho các trang cụ thể bất kỳ lúc nào qua popup của extension. Claude Code chỉ tương tác với các trang bạn đã cấp phép rõ ràng.

### Cách Hoạt Động

Claude Code điều khiển trình duyệt trong một cửa sổ hiển thị — bạn có thể xem các hành động xảy ra theo thời gian thực. Khi trình duyệt gặp trang đăng nhập hoặc CAPTCHA, Claude tạm dừng và chờ bạn xử lý thủ công trước khi tiếp tục.

### Giới Hạn Đã Biết

- **Hỗ trợ trình duyệt**: Chỉ Chrome và Edge — Brave, Arc và các trình duyệt Chromium khác không được hỗ trợ
- **WSL**: Không có sẵn trong Windows Subsystem for Linux
- **Nhà cung cấp bên thứ ba**: Không được hỗ trợ với Bedrock, Vertex hoặc Foundry API provider
- **Service worker idle**: Service worker của Chrome extension có thể đi vào trạng thái idle trong các phiên dài

> **Mẹo**: Chrome Integration là tính năng beta. Hỗ trợ trình duyệt có thể mở rộng trong các phiên bản tương lai.

---

## Điều Khiển Từ Xa

Remote Control (điều khiển từ xa) cho phép bạn tiếp tục phiên Claude Code đang chạy cục bộ từ điện thoại, máy tính bảng hoặc bất kỳ trình duyệt nào. Phiên cục bộ của bạn tiếp tục chạy trên máy của bạn — không có gì được chuyển lên cloud. Có sẵn trên các plan Pro, Max, Team và Enterprise (v2.1.51+).

### Bắt Đầu Remote Control

**Từ CLI**:

```bash
# Bắt đầu với tên phiên mặc định
claude remote-control

# Bắt đầu với tên tùy chỉnh
claude remote-control --name "Auth Refactor"
```

**Trong phiên làm việc**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Các flag có sẵn**:

| Flag | Mô Tả |
|------|--------|
| `--name "title"` | Tiêu đề phiên tùy chỉnh để dễ nhận dạng |
| `--verbose` | Hiển thị log kết nối chi tiết |
| `--sandbox` | Bật cách ly filesystem và mạng |
| `--no-sandbox` | Tắt sandboxing (mặc định) |

### Kết Nối Đến Phiên

Ba cách kết nối từ thiết bị khác:

1. **Session URL** — Được in ra terminal khi phiên bắt đầu; mở trong bất kỳ trình duyệt nào
2. **QR code** — Nhấn `spacebar` sau khi khởi động để hiển thị mã QR có thể quét
3. **Tìm theo tên** — Duyệt các phiên của bạn tại claude.ai/code hoặc trong ứng dụng Claude mobile (iOS/Android)

### Bảo Mật

- **Không mở cổng inbound** trên máy của bạn
- **Chỉ HTTPS outbound** qua TLS
- **Thông tin xác thực có phạm vi** — nhiều token tồn tại ngắn hạn, phạm vi hẹp
- **Cách ly phiên** — mỗi phiên từ xa là độc lập

### Remote Control vs Claude Code trên Web

| Khía Cạnh | Remote Control | Claude Code trên Web |
|-----------|---------------|---------------------|
| **Thực thi** | Chạy trên máy của bạn | Chạy trên cloud Anthropic |
| **Tool cục bộ** | Truy cập đầy đủ MCP server cục bộ, file và CLI | Không có dependency cục bộ |
| **Trường hợp dùng** | Tiếp tục công việc cục bộ từ thiết bị khác | Bắt đầu mới từ bất kỳ trình duyệt nào |

### Giới Hạn

- Một phiên từ xa cho mỗi instance Claude Code
- Terminal phải giữ mở trên máy host
- Phiên timeout sau khoảng 10 phút nếu mạng không thể truy cập

### Các Trường Hợp Sử Dụng

- Điều khiển Claude Code từ thiết bị di động hoặc máy tính bảng khi rời khỏi bàn làm việc
- Dùng UI claude.ai phong phú hơn trong khi duy trì thực thi tool cục bộ
- Review code nhanh khi di chuyển với toàn bộ môi trường phát triển cục bộ

---

## Phiên Web

Web Sessions cho phép bạn chạy Claude Code trực tiếp trên trình duyệt tại claude.ai/code, hoặc tạo phiên web từ CLI.

### Tạo Phiên Web

```bash
# Tạo phiên web mới từ CLI
claude --remote "implement the new API endpoints"
```

Lệnh này khởi động phiên Claude Code trên claude.ai mà bạn có thể truy cập từ bất kỳ trình duyệt nào.

### Tiếp Tục Phiên Web Cục Bộ

Nếu bạn đã bắt đầu phiên trên web và muốn tiếp tục cục bộ:

```bash
# Tiếp tục phiên web trong terminal cục bộ
claude --teleport
```

Hoặc trong một REPL tương tác:
```
/teleport
```

### Các Trường Hợp Sử Dụng

- Bắt đầu công việc trên một máy và tiếp tục trên máy khác
- Chia sẻ URL phiên với các thành viên nhóm
- Dùng UI web để review diff trực quan, rồi chuyển sang terminal để thực thi

---

## Ứng Dụng Desktop

Claude Code Desktop App cung cấp ứng dụng độc lập với review diff trực quan, phiên song song và connectors tích hợp. Có sẵn cho macOS và Windows (các plan Pro, Max, Team và Enterprise).

### Cài Đặt

Tải từ [claude.ai](https://claude.ai) cho nền tảng của bạn:
- **macOS**: Build universal (Apple Silicon và Intel)
- **Windows**: Bộ cài đặt x64 và ARM64 có sẵn

Xem [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) để biết hướng dẫn cài đặt.

### Bàn Giao Từ CLI

Chuyển phiên CLI hiện tại sang Desktop App:

```
/desktop
```

### Tính Năng Cốt Lõi

| Tính Năng | Mô Tả |
|----------|--------|
| **Diff view** | Review trực quan từng file với comment inline; Claude đọc comment và sửa đổi |
| **App preview** | Tự động khởi động dev server với trình duyệt nhúng để xác minh trực tiếp |
| **PR monitoring** | Tích hợp GitHub CLI với tự động sửa lỗi CI và tự động merge khi kiểm tra qua |
| **Phiên song song** | Nhiều phiên trong sidebar với cách ly Git worktree tự động |
| **Tác vụ theo lịch** | Tác vụ lặp lại (hàng giờ, hàng ngày, các ngày trong tuần, hàng tuần) chạy khi app mở |
| **Render phong phú** | Render code, markdown và diagram với syntax highlighting |

### Cấu Hình App Preview

Cấu hình hành vi dev server trong `.claude/launch.json`:

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### Connectors

Kết nối các dịch vụ bên ngoài để có ngữ cảnh phong phú hơn:

| Connector | Khả Năng |
|-----------|---------|
| **GitHub** | Theo dõi PR, issue tracking, review code |
| **Slack** | Thông báo, ngữ cảnh kênh |
| **Linear** | Issue tracking, quản lý sprint |
| **Notion** | Tài liệu, truy cập knowledge base |
| **Asana** | Quản lý tác vụ, theo dõi dự án |
| **Calendar** | Nhận thức lịch trình, ngữ cảnh cuộc họp |

> **Lưu ý**: Connectors không có sẵn cho các phiên từ xa (cloud).

### Phiên Từ Xa và SSH

- **Phiên từ xa**: Chạy trên cơ sở hạ tầng cloud Anthropic; tiếp tục ngay cả khi app đóng. Có thể truy cập từ claude.ai/code hoặc ứng dụng Claude mobile
- **Phiên SSH**: Kết nối với máy từ xa qua SSH với truy cập đầy đủ vào filesystem và tool từ xa. Claude Code phải được cài đặt trên máy từ xa

### Chế Độ Phân Quyền Trong Desktop

Desktop App hỗ trợ 4 chế độ phân quyền giống CLI:

| Chế Độ | Hành Vi |
|--------|---------|
| **Ask permissions** (mặc định) | Xem xét và phê duyệt mọi chỉnh sửa và lệnh |
| **Auto accept edits** | Chỉnh sửa file tự động phê duyệt; lệnh yêu cầu phê duyệt thủ công |
| **Plan mode** | Xem xét cách tiếp cận trước khi thực hiện bất kỳ thay đổi nào |
| **Bypass permissions** | Thực thi tự động (chỉ sandbox, do admin kiểm soát) |

### Tính Năng Enterprise

- **Admin console**: Kiểm soát quyền truy cập Code tab và cài đặt phân quyền cho tổ chức
- **MDM deployment**: Triển khai qua MDM trên macOS hoặc MSIX trên Windows
- **SSO integration**: Yêu cầu đăng nhập một lần cho các thành viên tổ chức
- **Managed settings**: Quản lý tập trung cấu hình nhóm và tính khả dụng model

---

## Danh Sách Tác Vụ

Tính năng Task List cung cấp theo dõi tác vụ liên tục tồn tại qua các lần nén context (khi lịch sử hội thoại được cắt để vừa với cửa sổ context).

### Bật/Tắt Danh Sách Tác Vụ

Nhấn `Ctrl+T` để bật/tắt chế độ xem danh sách tác vụ trong phiên.

### Tác Vụ Liên Tục

Tác vụ tồn tại qua các lần nén context, đảm bảo rằng các mục công việc chạy dài không bị mất khi context hội thoại bị cắt. Điều này đặc biệt hữu ích cho các triển khai phức tạp, nhiều bước.

### Thư Mục Tác Vụ Có Tên

Dùng biến môi trường `CLAUDE_CODE_TASK_LIST_ID` để tạo thư mục tác vụ có tên được chia sẻ qua các phiên:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

Điều này cho phép nhiều phiên chia sẻ cùng một danh sách tác vụ, hữu ích cho quy trình làm việc nhóm hoặc dự án nhiều phiên.

---

## Gợi Ý Lệnh

Prompt Suggestions (gợi ý lệnh) hiển thị các lệnh ví dụ mờ dựa trên lịch sử git và ngữ cảnh hội thoại hiện tại.

### Cách Hoạt Động

- Gợi ý xuất hiện dưới dạng văn bản mờ bên dưới prompt nhập của bạn
- Nhấn `Tab` để chấp nhận gợi ý
- Nhấn `Enter` để chấp nhận và gửi ngay lập tức
- Gợi ý nhận thức ngữ cảnh, lấy từ lịch sử git và trạng thái hội thoại

### Tắt Gợi Ý Lệnh

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktrees

Git Worktrees cho phép bạn khởi động Claude Code trong một worktree cách ly, cho phép làm việc song song trên các nhánh khác nhau mà không cần stash hoặc chuyển nhánh.

### Khởi Động Trong Worktree

```bash
# Khởi động Claude Code trong worktree cách ly
claude --worktree
# hoặc
claude -w
```

### Vị Trí Worktree

Worktrees được tạo tại:
```
<repo>/.claude/worktrees/<name>
```

### Sparse Checkout Cho Monorepo

Dùng cài đặt `worktree.sparsePaths` để thực hiện sparse-checkout trong các monorepo, giảm dung lượng đĩa và thời gian clone:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Tool và Hook Của Worktree

| Mục | Mô Tả |
|-----|--------|
| `ExitWorktree` | Tool để thoát và dọn sạch worktree hiện tại |
| `WorktreeCreate` | Sự kiện hook được kích hoạt khi worktree được tạo |
| `WorktreeRemove` | Sự kiện hook được kích hoạt khi worktree bị xóa |

### Tự Động Dọn Sạch

Nếu không có thay đổi nào được thực hiện trong worktree, nó sẽ tự động được dọn sạch khi phiên kết thúc.

### Các Trường Hợp Sử Dụng

- Làm việc trên nhánh tính năng trong khi giữ nhánh main không bị ảnh hưởng
- Chạy test trong môi trường cách ly mà không ảnh hưởng thư mục làm việc
- Thử các thay đổi thử nghiệm trong môi trường có thể bỏ đi
- Sparse-checkout các package cụ thể trong monorepo để khởi động nhanh hơn

---

## Sandboxing

Sandboxing cung cấp cách ly filesystem và mạng ở cấp độ OS cho các lệnh Bash được thực thi bởi Claude Code. Đây là phần bổ sung cho các quy tắc phân quyền và cung cấp một lớp bảo mật bổ sung.

### Bật Sandboxing

**Slash command**:
```
/sandbox
```

**CLI flags**:
```bash
claude --sandbox       # Bật sandboxing
claude --no-sandbox    # Tắt sandboxing
```

### Cài Đặt Cấu Hình

| Cài Đặt | Mô Tả |
|---------|--------|
| `sandbox.enabled` | Bật hoặc tắt sandboxing |
| `sandbox.failIfUnavailable` | Thất bại nếu sandboxing không thể kích hoạt |
| `sandbox.filesystem.allowWrite` | Các đường dẫn được phép ghi |
| `sandbox.filesystem.allowRead` | Các đường dẫn được phép đọc |
| `sandbox.filesystem.denyRead` | Các đường dẫn bị từ chối đọc |
| `sandbox.enableWeakerNetworkIsolation` | Bật cách ly mạng yếu hơn trên macOS |

### Cấu Hình Ví Dụ

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### Cách Hoạt Động

- Các lệnh Bash chạy trong môi trường sandbox với quyền truy cập filesystem bị hạn chế
- Quyền truy cập mạng có thể bị cách ly để ngăn các kết nối bên ngoài không mong muốn
- Hoạt động cùng với các quy tắc phân quyền để phòng thủ theo chiều sâu
- Trên macOS, dùng `sandbox.enableWeakerNetworkIsolation` để hạn chế mạng (cách ly mạng hoàn toàn không có sẵn trên macOS)

### Các Trường Hợp Sử Dụng

- Chạy code không tin cậy hoặc được tạo tự động một cách an toàn
- Ngăn các sửa đổi vô tình đối với file ngoài dự án
- Hạn chế quyền truy cập mạng trong các tác vụ tự động

---

## Cài Đặt Quản Lý (Enterprise)

Managed Settings (cài đặt quản lý) cho phép quản trị viên enterprise triển khai cấu hình Claude Code trên toàn tổ chức bằng các công cụ quản lý native của nền tảng.

### Phương Thức Triển Khai

| Nền Tảng | Phương Thức | Từ Phiên Bản |
|---------|------------|--------------|
| macOS | File plist được quản lý (MDM) | v2.1.51+ |
| Windows | Windows Registry | v2.1.51+ |
| Đa nền tảng | File cấu hình được quản lý | v2.1.51+ |
| Đa nền tảng | Drop-in được quản lý (thư mục `managed-settings.d/`) | v2.1.83+ |

### Drop-in Được Quản Lý

Từ v2.1.83, quản trị viên có thể triển khai nhiều file cài đặt được quản lý vào thư mục `managed-settings.d/`. Các file được merge theo thứ tự bảng chữ cái, cho phép cấu hình mô-đun trên các nhóm:

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Các Cài Đặt Quản Lý Có Sẵn

| Cài Đặt | Mô Tả |
|---------|--------|
| `disableBypassPermissionsMode` | Ngăn người dùng bật bypass permissions |
| `availableModels` | Hạn chế model người dùng có thể chọn |
| `allowedChannelPlugins` | Kiểm soát channel plugin nào được phép |
| `autoMode.environment` | Cấu hình cơ sở hạ tầng tin cậy cho auto mode |
| Chính sách tùy chỉnh | Chính sách phân quyền và tool đặc thù của tổ chức |

### Ví Dụ: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Cấu Hình và Thiết Lập

### Vị Trí File Cấu Hình

1. **Global config**: `~/.claude/config.json`
2. **Project config**: `./.claude/config.json`
3. **User config**: `~/.config/claude-code/settings.json`

### Ví Dụ Cấu Hình Đầy Đủ

**Cấu hình tính năng nâng cao cốt lõi:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**Ví dụ cấu hình mở rộng:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Biến Môi Trường

Ghi đè cấu hình bằng biến môi trường:

```bash
# Chọn model
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# Cấu hình API
export ANTHROPIC_API_KEY=sk-ant-...

# Cấu hình thinking
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# Bật/tắt tính năng
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Được đặt bởi flag --bare

# Cấu hình MCP
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Quản lý tác vụ
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (thử nghiệm)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true

# Cấu hình subagent và plugin
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=true

# Subprocess và streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### Lệnh Quản Lý Cấu Hình

```
User: /config
[Opens interactive configuration menu]
```

Lệnh `/config` cung cấp menu tương tác để bật/tắt các cài đặt như:
- Extended thinking bật/tắt
- Output verbose
- Chế độ phân quyền
- Chọn model

### Cấu Hình Theo Dự Án

Tạo `.claude/config.json` trong dự án của bạn:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Thực Hành Tốt Nhất

### Chế Độ Lập Kế Hoạch
- ✅ Dùng cho tác vụ phức tạp nhiều bước
- ✅ Xem xét kế hoạch trước khi phê duyệt
- ✅ Sửa đổi kế hoạch khi cần
- ❌ Không dùng cho tác vụ đơn giản

### Suy Nghĩ Mở Rộng
- ✅ Dùng cho quyết định kiến trúc
- ✅ Dùng cho giải quyết vấn đề phức tạp
- ✅ Xem xét quá trình suy nghĩ
- ❌ Không dùng cho câu hỏi đơn giản

### Tác Vụ Nền
- ✅ Dùng cho các hoạt động chạy dài
- ✅ Theo dõi tiến độ tác vụ
- ✅ Xử lý lỗi tác vụ một cách nhẹ nhàng
- ❌ Không khởi động quá nhiều tác vụ đồng thời

### Phân Quyền
- ✅ Dùng `plan` để review code (chỉ đọc)
- ✅ Dùng `default` để phát triển tương tác
- ✅ Dùng `acceptEdits` cho quy trình tự động hóa
- ✅ Dùng `auto` cho công việc tự chủ với các biện pháp bảo vệ an toàn
- ❌ Không dùng `bypassPermissions` trừ khi thực sự cần thiết

### Phiên Làm Việc
- ✅ Dùng các phiên riêng biệt cho các tác vụ khác nhau
- ✅ Lưu các trạng thái phiên quan trọng
- ✅ Dọn sạch các phiên cũ
- ❌ Không trộn lẫn công việc không liên quan trong một phiên

---

## Tài Nguyên Liên Quan

Để biết thêm thông tin về Claude Code và các tính năng liên quan:

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode)
- [Official Headless Mode Documentation](https://code.claude.com/docs/en/headless)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Checkpoints Guide](../08-checkpoints/) - Quản lý phiên và tua lại
- [Slash Commands](../01-slash-commands/) - Tài liệu tham khảo lệnh
- [Memory Guide](../02-memory/) - Ngữ cảnh liên tục
- [Skills Guide](../03-skills/) - Khả năng tự chủ
- [Subagents Guide](../04-subagents/) - Thực thi tác vụ được ủy thác
- [MCP Guide](../05-mcp/) - Truy cập dữ liệu bên ngoài
- [Hooks Guide](../06-hooks/) - Tự động hóa hướng sự kiện
- [Plugins Guide](../07-plugins/) - Extension đóng gói
- [Official Scheduled Tasks Documentation](https://code.claude.com/docs/en/scheduled-tasks)
- [Official Chrome Integration Documentation](https://code.claude.com/docs/en/chrome)
- [Official Remote Control Documentation](https://code.claude.com/docs/en/remote-control)
- [Official Keybindings Documentation](https://code.claude.com/docs/en/keybindings)
- [Official Desktop App Documentation](https://code.claude.com/docs/en/desktop)
