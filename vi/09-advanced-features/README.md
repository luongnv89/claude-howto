<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Tính Năng Nâng Cao

Hướng dẫn toàn diện về các khả năng nâng cao của Claude Code, bao gồm chế độ lập kế hoạch, tư duy mở rộng, chế độ auto, tác vụ nền, chế độ quyền, chế độ print (không tương tác), quản lý phiên, tính năng tương tác, channels, nhập liệu bằng giọng nói, điều khiển từ xa, phiên web, ứng dụng desktop, danh sách tác vụ, gợi ý prompt, git worktree, sandboxing, cài đặt được quản lý và cấu hình.

## Mục Lục

1. [Tổng Quan](#tổng-quan)
2. [Chế Độ Lập Kế Hoạch](#chế-độ-lập-kế-hoạch)
3. [Tư Duy Mở Rộng](#tư-duy-mở-rộng)
4. [Chế Độ Auto](#chế-độ-auto)
5. [Tác Vụ Nền](#tác-vụ-nền)
6. [Công Cụ Monitor (Luồng Hướng Sự Kiện)](#công-cụ-monitor-luồng-hướng-sự-kiện)
7. [Workflow Động](#workflow-động)
8. [Tác Vụ Theo Lịch](#tác-vụ-theo-lịch)
9. [Chế Độ Quyền](#chế-độ-quyền)
10. [Chế Độ Headless](#chế-độ-headless)
11. [Quản Lý Phiên](#quản-lý-phiên)
12. [Nhắn Tin Giữa Các Phiên](#nhắn-tin-giữa-các-phiên)
13. [Tính Năng Tương Tác](#tính-năng-tương-tác)
14. [Kiểu Đầu Ra](#kiểu-đầu-ra)
15. [Dòng Trạng Thái](#dòng-trạng-thái)
16. [Chế Độ TUI (Toàn Màn Hình)](#chế-độ-tui-toàn-màn-hình)
17. [Nhập Liệu Bằng Giọng Nói](#nhập-liệu-bằng-giọng-nói)
18. [Channels](#channels)
19. [Tích Hợp Chrome](#tích-hợp-chrome)
20. [Điều Khiển Từ Xa](#điều-khiển-từ-xa)
21. [Phiên Web](#phiên-web)
22. [Ứng Dụng Desktop](#ứng-dụng-desktop)
23. [Danh Sách Tác Vụ](#danh-sách-tác-vụ)
24. [Gợi Ý Prompt](#gợi-ý-prompt)
25. [Git Worktree](#git-worktree)
26. [Sandboxing](#sandboxing)
27. [Cài Đặt Được Quản Lý (Enterprise)](#cài-đặt-được-quản-lý-enterprise)
28. [Cấu Hình và Cài Đặt](#cấu-hình-và-cài-đặt)
29. [Tin Cậy và Phạm Vi Quyền](#tin-cậy-và-phạm-vi-quyền)
30. [Nhóm Tác Nhân](#nhóm-tác-nhân)
31. [Thực Hành Tốt Nhất](#thực-hành-tốt-nhất)
32. [Tài Nguyên Bổ Sung](#tài-nguyên-bổ-sung)

---

## Tổng Quan

Các tính năng nâng cao trong Claude Code mở rộng khả năng cốt lõi với các cơ chế lập kế hoạch, suy luận, tự động hóa và kiểm soát. Những tính năng này cho phép xây dựng các workflow tinh vi cho tác vụ phát triển phức tạp, review code, tự động hóa và quản lý nhiều phiên.

**Các tính năng nâng cao chính bao gồm:**
- **Chế Độ Lập Kế Hoạch**: Tạo kế hoạch triển khai chi tiết trước khi viết code
- **Tư Duy Mở Rộng**: Suy luận sâu cho các vấn đề phức tạp
- **Chế Độ Auto**: Bộ phân loại an toàn chạy nền review từng hành động trước khi thực thi
- **Tác Vụ Nền**: Chạy các thao tác dài mà không chặn cuộc hội thoại
- **Chế Độ Quyền**: Kiểm soát những gì Claude được làm (`manual` — trước đây là `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Chế Độ Print**: Chạy Claude Code không tương tác cho tự động hóa và CI/CD (`claude -p`)
- **Quản Lý Phiên**: Quản lý nhiều phiên làm việc
- **Tính Năng Tương Tác**: Phím tắt, nhập nhiều dòng và lịch sử lệnh
- **Nhập Liệu Bằng Giọng Nói**: Nhập giọng nói kiểu push-to-talk với STT hỗ trợ 20 ngôn ngữ
- **Channels**: MCP server đẩy tin nhắn vào các phiên đang chạy (Research Preview)
- **Điều Khiển Từ Xa**: Điều khiển Claude Code từ Claude.ai hoặc ứng dụng Claude
- **Phiên Web**: Chạy Claude Code trên trình duyệt tại claude.ai/code
- **Ứng Dụng Desktop**: Ứng dụng độc lập để review diff trực quan và chạy nhiều phiên
- **Danh Sách Tác Vụ**: Theo dõi tác vụ bền vững qua các lần nén ngữ cảnh
- **Gợi Ý Prompt**: Gợi ý lệnh thông minh dựa trên ngữ cảnh
- **Git Worktree**: Các branch worktree cô lập để làm việc song song
- **Sandboxing**: Cô lập hệ thống file và mạng ở cấp hệ điều hành
- **Cài Đặt Được Quản Lý**: Triển khai cho doanh nghiệp qua plist, Registry hoặc file được quản lý
- **Cấu Hình**: Tùy chỉnh hành vi bằng các file cấu hình JSON

---

## Chế Độ Lập Kế Hoạch

Chế độ lập kế hoạch cho phép Claude suy nghĩ kỹ các tác vụ phức tạp trước khi triển khai, tạo ra một kế hoạch chi tiết để bạn review và phê duyệt.

### Chế Độ Lập Kế Hoạch Là Gì?

Chế độ lập kế hoạch là cách tiếp cận hai giai đoạn:
1. **Giai đoạn lập kế hoạch**: Claude phân tích tác vụ và tạo kế hoạch triển khai chi tiết
2. **Giai đoạn triển khai**: Sau khi được phê duyệt, Claude thực thi kế hoạch

### Khi Nào Dùng Chế Độ Lập Kế Hoạch

✅ Dùng chế độ lập kế hoạch cho:
- Refactor phức tạp trên nhiều file
- Triển khai tính năng mới
- Thay đổi kiến trúc
- Migration cơ sở dữ liệu
- Thiết kế lại API lớn

❌ Không dùng chế độ lập kế hoạch cho:
- Sửa lỗi đơn giản
- Thay đổi định dạng
- Chỉnh sửa một file
- Truy vấn nhanh

### Kích Hoạt Chế Độ Lập Kế Hoạch

**Lệnh slash**:
```bash
/plan Implement user authentication system
```

**Cờ CLI**:
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
- `Shift + Tab` - Chuyển đổi giữa các chế độ quyền (bao gồm plan)
- `Alt + M` - Chuyển đổi giữa các chế độ quyền (chỉ trên Windows, khi runtime không bật chế độ VT input)

### Lợi Ích Của Chế Độ Lập Kế Hoạch

- **Cách triển khai có cấu trúc**: Chia nhỏ chi tiết các bước triển khai
- **Review và phê duyệt**: Phê duyệt hoặc điều chỉnh kế hoạch trước khi thực thi
- **Nhận diện rủi ro**: Xác định các vấn đề tiềm ẩn trước khi triển khai
- **Các giai đoạn rõ ràng**: Các giai đoạn và cột mốc triển khai được tổ chức tốt

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

### Chỉnh Sửa Kế Hoạch

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Cấu Hình Chế Độ Lập Kế Hoạch

Chế độ lập kế hoạch được kích hoạt qua cờ CLI hoặc lệnh slash:

```bash
# Kích hoạt chế độ plan qua CLI
claude --permission-mode plan

# Hoặc dùng lệnh slash /plan bên trong REPL
/plan Implement user authentication system
```

**Model alias cho lập kế hoạch**: Dùng `opusplan` làm model alias để dùng Opus cho lập kế hoạch và Sonnet cho thực thi:

```bash
claude --model opusplan "design and implement the new API"
```

**Chỉnh sửa kế hoạch bên ngoài**: Nhấn `Ctrl+G` để mở kế hoạch hiện tại trong trình soạn thảo bên ngoài và chỉnh sửa chi tiết.

> **Cập nhật v2.1.112**: File kế hoạch giờ được đặt tên theo prompt đã tạo ra chúng (thay vì các từ ngẫu nhiên), giúp dễ duyệt và tái sử dụng hơn.

> **Cập nhật v2.1.136 — chế độ plan chặn ghi file vô điều kiện**: Chế độ plan giờ chặn mọi thao tác ghi file, kể cả khi có rule `Edit(...)` khớp trong `permissions.allow`. Trước đây một rule `Edit(...)` dễ dãi có thể cho phép ghi trong chế độ plan; lỗ hổng đó đã được đóng. Nếu workflow của bạn phụ thuộc vào hành vi cũ, hãy thoát chế độ plan (`Shift+Tab`) trước khi chỉnh sửa.

---

## Tư Duy Mở Rộng

Tư duy mở rộng cho phép Claude dành nhiều thời gian hơn để suy luận về các vấn đề phức tạp trước khi đưa ra giải pháp.

### Tư Duy Mở Rộng Là Gì?

Tư duy mở rộng là quá trình suy luận có chủ đích, từng bước, trong đó Claude:
- Chia nhỏ các vấn đề phức tạp
- Cân nhắc nhiều cách tiếp cận
- Đánh giá các đánh đổi
- Suy luận qua các trường hợp biên

### Kích Hoạt Tư Duy Mở Rộng

**Phím tắt**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - Bật/tắt tư duy mở rộng. Trên Opus 5.5 (model mặc định từ v2.1.280), Sonnet 5.5, Haiku 5.5 và các model Fable, không thể tắt tư duy — phím bật/tắt, `alwaysThinkingEnabled` và `MAX_THINKING_TOKENS=0` không có tác dụng ở đó.

**Kích hoạt tự động**:
- Bật mặc định cho mọi model (Opus 5.5, Sonnet 5.5, Haiku 5.5, các model Fable, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Sonnet 4.6, Haiku 4.5)
- Opus 5 / Opus 4.8: Suy luận thích ứng với các mức effort: `low` (○), `medium` (◐), `high` (●), `xhigh`, `max`. Mặc định là `medium` trên Opus 5.5 (model mặc định từ v2.1.280), Sonnet 5.5 và Haiku 5.5, `high` trên Opus 5 (v2.1.219), Sonnet 5, Opus 4.8 (v2.1.154), Opus 4.6 và Sonnet 4.6, và `xhigh` trên Opus 4.7. `xhigh` có trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8 và Opus 4.7 (lùi về `high` trên Opus 4.6 / Sonnet 4.6). `max` hoạt động trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7/4.6 và Sonnet 4.6 (chỉ trong phiên). Haiku 4.5 không có mức effort. Opus 5, Opus 4.8 và Opus 4.7 có cửa sổ ngữ cảnh gốc 1M token (bản sửa ngữ cảnh 1M có từ v2.1.117 — trước đó, `/context` đếm sai Opus 4.7 theo cửa sổ 200K và kích hoạt autocompact sớm). Từ v2.1.129, `/context` chỉ hiển thị phần trực quan trong UI; phần ASCII không còn lọt vào ngữ cảnh hội thoại (tiết kiệm ~1.6k token mỗi lần gọi), nên bạn có thể gọi `/context` thoải mái.
- Người dùng Pro/Max trên Opus 4.6 / Sonnet 4.6: effort mặc định được nâng từ `medium` lên `high` trong v2.1.117.
- Các model khác: Ngân sách cố định tới 31.999 token

**Các cách cấu hình**:
- Bật/tắt: `Alt+T` / `Option+T`, hoặc qua `/config`
- Xem quá trình suy luận: `Ctrl+O` (chế độ verbose)
- Đặt effort: lệnh `/effort` hoặc cờ `--effort`

**Ngân sách tùy chỉnh**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Mức effort** (hỗ trợ trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6 và Sonnet 4.6 — không có trên Haiku 4.5):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), hoặc max — mặc định là high trên Opus 5 và Opus 4.8
```

**Cờ CLI**:
```bash
claude --effort high "complex architectural review"
```

**Lệnh slash**:
```
/effort high
```

> **Lưu ý:** Từ khóa "ultrathink" trong prompt kích hoạt chế độ suy luận sâu. Từ v2.1.311, khi gõ trong terminal tương tác, nó còn chạy lượt đó ở effort `xhigh` trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.2 (v2.1.321+) và Fable 5.1 qua API của Anthropic (từ này chuyển sang màu cầu vồng khi có hiệu lực; nếu gõ trong lúc Claude đang làm việc, nó nâng mức cho phần còn lại của lượt đó; VS Code từ v2.1.316). Trên Bedrock hoặc các model khác, hãy đặt mức effort thay thế. `CLAUDE_CODE_DISABLE_ULTRATHINK=1` (v2.1.316) tắt từ khóa này. Các mức effort `low`, `medium`, `high` và `max` được hỗ trợ trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6 và Sonnet 4.6 (Haiku 4.5 không có). `xhigh` có trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8 và Opus 4.7. Effort mặc định là `medium` trên Opus 5.5, Sonnet 5.5 và Haiku 5.5, `high` trên Opus 5, Sonnet 5, Opus 4.8 (và Opus 4.6 / Sonnet 4.6) và `xhigh` trên Opus 4.7. Khác với Opus 4.8 và Opus 4.7 (vốn cố định effort mặc định ở lần chạy đầu), Opus 5 không giữ như vậy — mức bạn đã đặt trước đó được giữ lại. Thanh trượt `/effort` còn có nút bật/tắt **Ultracode** (Tab, hoặc `/effort ultracode [on|off]`), nhưng đây **không** phải mức effort của model — nó khiến Claude điều phối các workflow động ở bất kỳ mức effort nào phiên đang chạy. Từ v2.1.284, nó không còn ép `xhigh` và vẫn bật khi bạn đổi mức; `--effort ultracode` và `effortLevel: "ultracode"` của Agent SDK vẫn đặt `xhigh`.

### Cơ Chế Dự Phòng Của Bộ Phân Loại An Toàn Trên Opus 5

Tách biệt với [cài đặt `fallbackModel`](#model-dự-phòng-fallbackmodel) (xử lý tình trạng quá tải và không khả dụng), Claude Code áp dụng **cơ chế dự phòng theo danh mục** khi bộ phân loại an toàn gắn cờ một yêu cầu. Tính năng này cần Claude Code v2.1.219 trở lên.

- **Opus 5**: các yêu cầu bị gắn cờ an ninh mạng sẽ chạy lại trên Opus 4.8. Các yêu cầu bị gắn cờ sinh học thì kết thúc bằng một lời từ chối, vì Opus 5 chạy bộ phân loại sinh học riêng mà không có model dự phòng. Bạn sẽ nhận các lời từ chối đó ngay từ yêu cầu bị gắn cờ đầu tiên.
- Các khối lượng công việc về bảo mật tấn công hoặc sinh học — kiểm thử xâm nhập, bài tập Capture the Flag (CTF) và các codebase liên quan đến sinh học — thường xuyên kích hoạt cơ chế dự phòng, thường ngay từ yêu cầu đầu tiên.

Vì sao điều này quan trọng ở đây: nếu bạn chạy [tác nhân con security-review](../04-subagents/README.md) hoặc công việc CTF/pentest trên Opus 5, hãy chuẩn bị cho việc các prompt an ninh mạng âm thầm chạy lại trên Opus 4.8 (trần effort và cửa sổ ngữ cảnh khác), và các prompt liên quan đến sinh học bị từ chối thẳng. Hãy chỉ định rõ một model khác nếu hành vi đó gây cản trở.

**Kiểm soát việc chuyển đổi** — cài đặt `switchModelsOnFlag` (v2.1.170+, mặc định `true`) quyết định việc dự phòng có diễn ra âm thầm hay không. Đặt thành `false` thì Claude Code sẽ tạm dừng, cho bạn chọn giữa chuyển model và sửa prompt. Việc tạm dừng này chỉ áp dụng cho cuộc hội thoại chính: subagent không bao giờ tạm dừng, nên với **Ask each time** (`false`), một yêu cầu subagent bị gắn cờ sẽ thất bại thay vì chuyển model (v2.1.318; các phiên bản trước chạy lại nó trên model dự phòng). Cài đặt này xuất hiện trong `/config` với tên **Switch models when a message is flagged**.

```json
{
  "switchModelsOnFlag": false
}
```

### Lợi Ích Của Tư Duy Mở Rộng

- **Suy luận sâu**: Dành nhiều thời gian hơn để suy nghĩ về các vấn đề phức tạp
- **Quyết định kiến trúc tốt hơn**: Đưa ra lựa chọn sáng suốt với đánh giá toàn diện
- **Cân nhắc các trường hợp biên**: Suy nghĩ thấu đáo về các vấn đề và kịch bản tiềm ẩn
- **Phân tích kỹ lưỡng**: Cách tiếp cận có cấu trúc để giải quyết vấn đề phức tạp

### Ví Dụ: Quyết Định Kiến Trúc

```
User: ultrathink Should we use microservices or a monolith for our e-commerce platform?

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

### Cấu Hình Tư Duy Mở Rộng

Tư duy mở rộng được kiểm soát qua biến môi trường, phím tắt và cờ CLI:

```bash
# Đặt ngân sách token cho tư duy
export MAX_THINKING_TOKENS=16000

# Đặt mức effort (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6): low (○), medium (◐), high (●), xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), hoặc max — mặc định là high trên Opus 5 và Opus 4.8
export CLAUDE_CODE_EFFORT_LEVEL=high
```

Bật/tắt trong phiên bằng `Alt+T` / `Option+T`, đặt effort bằng `/effort`, hoặc cấu hình qua `/config`.

> **System prompt gọn (v2.1.154):** System prompt gọn giờ là **mặc định** cho mọi model ngoại trừ Haiku 4.5, Sonnet 5, Opus 4.7 và các model cũ hơn trong các dòng đó (Haiku 5.5 và Sonnet 5.5 cũng dùng nó), giúp giảm lượng token nền trên Opus 5 và Opus 4.8.

---

## Chế Độ Auto

Chế độ Auto là một chế độ quyền dùng bộ phân loại an toàn chạy nền để review từng hành động trước khi thực thi. Nó cho phép Claude làm việc tự chủ trong khi vẫn chặn các thao tác nguy hiểm. Chế độ này có trên mọi gói, nhưng cần model đủ điều kiện (Claude Opus 4.6 trở lên, Sonnet 4.6 trở lên, Haiku 5.5 hoặc một model Fable trên Anthropic API và Claude Platform on AWS; Sonnet 5 trở lên, Opus 4.7 trở lên, Haiku 5.5 hoặc một model Fable trên Bedrock, Vertex, Foundry và các phiên Claude apps gateway đã đăng nhập). Trên gói Team và Enterprise, chế độ này bật mặc định — quản trị viên có thể tắt nó cho tổ chức trong cài đặt được quản lý.

### Yêu Cầu

Chế độ auto chỉ khả dụng khi tài khoản của bạn đáp ứng tất cả các yêu cầu sau:

- **Gói**: mọi gói.
- **Tổ chức**: trên Team và Enterprise, chế độ auto khả dụng mặc định. Quản trị viên có thể tắt nó cho tổ chức bằng cách đặt `permissions.disableAutoMode` thành `"disable"` trong cài đặt được quản lý.
- **Model**: trên Anthropic API và Claude Platform on AWS — Claude Opus 4.6 trở lên, Sonnet 4.6 trở lên, Haiku 5.5 hoặc một model Fable. Trên Amazon Bedrock, Google Cloud's Agent Platform (Vertex AI), Microsoft Foundry và các phiên Claude apps gateway đã đăng nhập — chỉ Claude Sonnet 5 trở lên, Opus 4.7 trở lên, Haiku 5.5 (v2.1.293+) và các model Fable. Các model cũ hơn — Sonnet 4.5, Opus 4.5, Haiku 4.5 và các model claude-3 — không được hỗ trợ trên bất kỳ nhà cung cấp nào.
- **Nhà cung cấp**: khả dụng mặc định trên Anthropic API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform (Vertex AI), Microsoft Foundry và các phiên Claude apps gateway đã đăng nhập. Từ v2.1.158 đến v2.1.206, chế độ auto bị tắt trên tất cả các nhà cung cấp này trừ Anthropic API và Claude Platform on AWS cho đến khi bạn đặt `CLAUDE_CODE_ENABLE_AUTO_MODE=1`; v2.1.207 đã bỏ yêu cầu này. Biến này vẫn được chấp nhận để tương thích và không còn tác dụng từ v2.1.207 trở đi.
- **Bộ phân loại**: tốn thêm chi phí token, trừ trên gói Enterprise và tài khoản Claude API, nơi v2.1.278+ chạy việc kiểm tra phía server miễn phí

### Bật Chế Độ Auto

```bash
# Phiên tương tác khởi động ở chế độ auto khi chưa cấu hình chế độ quyền nào (v2.1.284+)
# Để chọn rõ ràng, ví dụ khi cài đặt của bạn mặc định một chế độ khác:
claude --permission-mode auto

# Hoặc chuyển vòng tới nó bằng Shift+Tab trong REPL
```

> **Cập nhật v2.1.112**: Chế độ auto không còn cần cờ `--enable-auto-mode`. Người dùng Max truy cập trực tiếp trên Opus 4.7.

> **Cập nhật v2.1.158**: Chế độ auto trở nên khả dụng trên Bedrock, Vertex và Foundry cho Opus 4.7/4.8, với điều kiện đặt `CLAUDE_CODE_ENABLE_AUTO_MODE=1`.
>
> **Cập nhật v2.1.207**: Yêu cầu opt-in đó đã bị bỏ. Chế độ auto giờ khả dụng mặc định trên Bedrock, Vertex AI, Microsoft Foundry và các phiên Claude apps gateway đã đăng nhập cho Claude Sonnet 5, Opus 4.7, Opus 4.8 và Fable 5 (và Opus 5 từ v2.1.219) — không cần cờ hay biến môi trường. Quản trị viên có thể tắt nó bằng `disableAutoMode` trong cài đặt được quản lý. `CLAUDE_CODE_ENABLE_AUTO_MODE` vẫn được chấp nhận để tương thích nhưng không còn tác dụng từ v2.1.207 trở đi.

Hoặc đặt nó làm chế độ quyền mặc định:

```bash
claude --permission-mode auto
```

Đặt qua cấu hình:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Cách Bộ Phân Loại Hoạt Động

Bộ phân loại chạy nền đánh giá từng hành động theo thứ tự quyết định sau:

1. **Rule allow/deny** -- Các rule quyền tường minh được kiểm tra trước
2. **Đọc/chỉnh sửa được tự động phê duyệt** -- Việc đọc và chỉnh sửa file được cho qua tự động
3. **Bộ phân loại** -- Bộ phân loại chạy nền review hành động
4. **Dự phòng** -- Quay về hỏi người dùng sau 3 lần chặn liên tiếp hoặc tổng cộng 20 lần chặn

### Các Hành Động Bị Chặn Mặc Định

Chế độ auto chặn các hành động sau theo mặc định:

| Hành động bị chặn | Ví dụ |
|----------------|---------|
| Cài đặt kiểu pipe-to-shell | `curl \| bash` |
| Gửi dữ liệu nhạy cảm ra ngoài | API key, thông tin xác thực qua mạng |
| Deploy lên production | Các lệnh deploy nhắm tới production |
| Xóa hàng loạt | `rm -rf` trên thư mục lớn |
| Thay đổi IAM | Sửa đổi quyền và vai trò |
| Force push lên main | `git push --force origin main` |

> **Nhiều quyết định hơn được chuyển cho bộ phân loại (v2.1.218)**: Bộ phân loại cũng quyết định các lệnh xóa nhắm vào thư mục gốc của hệ thống file hoặc thư mục home, như `rm -rf /` và `rm -rf ~`, kể cả khi lệnh xóa nằm trong command substitution hoặc process substitution. Trước v2.1.218, các dạng đơn giản sẽ hỏi phê duyệt thay vào đó, và các dạng substitution thì hỏi trong v2.1.208 đến v2.1.217. Các kiểm tra `&` chạy nền và đường dẫn Windows đáng ngờ cũng không còn mở hộp thoại quyền — bộ phân loại đánh giá chúng. Từ v2.1.281, các lệnh xóa đường dẫn quan trọng được nhận diện như trên lại hỏi trong chế độ auto, với đồng hồ đếm ngược 2 phút trong terminal và từ chối ngay lập tức ở nơi khác; bộ phân loại chỉ quyết định chúng khi đặt `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1`.

### Các Hành Động Được Cho Phép Mặc Định

| Hành động được cho phép | Ví dụ |
|----------------|---------|
| Thao tác file cục bộ | Đọc, ghi, chỉnh sửa file dự án |
| Cài đặt dependencies đã khai báo | `npm install`, `pip install` từ manifest |
| HTTP chỉ đọc | `curl` để lấy tài liệu |
| Push lên branch hiện tại | `git push origin feature-branch` |

### Cấu Hình Chế Độ Auto

**In các rule mặc định dưới dạng JSON**:
```bash
claude auto-mode defaults
```

**Khôi phục cấu hình chế độ auto mặc định** (v2.1.212), có prompt xác nhận (`--yes` để bỏ qua):
```bash
claude auto-mode reset
claude auto-mode reset --yes
```

**Cấu hình hạ tầng tin cậy** qua cài đặt được quản lý `autoMode.environment` cho các triển khai doanh nghiệp. Điều này cho phép quản trị viên định nghĩa các môi trường CI/CD, đích deploy và mẫu hạ tầng đáng tin cậy.

**Soạn các mục environment bằng `/auto-mode-setup`**: lệnh có hướng dẫn này đọc dự án và các phiên gần đây của bạn rồi đề xuất các mục `autoMode.environment` (và đôi khi cả rule), sau đó ghi chúng vào `~/.claude/settings.json` nếu bạn chấp nhận. Pro, Max, Ultra và Team cần v2.1.228+ (v2.1.233+ trên Windows gốc); Enterprise và API key Claude Console cần v2.1.283+. Từ v2.1.304, lệnh này cũng hoạt động trên Bedrock, Vertex, Foundry và khi tắt telemetry.

#### Mở rộng mặc định với `"$defaults"` (v2.1.118)

Từ v2.1.118, `autoMode.allow`, `autoMode.soft_deny` và `autoMode.environment` chấp nhận token `"$defaults"` để **nối thêm** các rule của bạn vào danh sách có sẵn thay vì thay thế nó. Trước v2.1.118, bất kỳ mảng do người dùng định nghĩa nào cũng âm thầm ghi đè các rule có sẵn. Một mảng không có `"$defaults"` vẫn thay thế các rule có sẵn của phần đó, ngoại trừ việc từ v2.1.316 một danh sách `allow` không có nó vẫn giữ rule có sẵn cho prompt của tác vụ theo lịch.

#### Chặn vô điều kiện với `autoMode.hard_deny` (v2.1.136)

`autoMode.hard_deny` (v2.1.136+) là một mảng các rule của bộ phân loại chặn một loại hành động **bất kể ý định suy ra của người dùng**. Dùng nó cho các hành động không bao giờ được chạy trong chế độ auto — ví dụ `rm -rf` trên đường dẫn gốc hoặc `git push --force` trên các branch được bảo vệ. Khác với `soft_deny`, các rule hard-deny không thể được bộ phân loại thương lượng.

```json
{
  "autoMode": {
    "hard_deny": ["Bash(rm -rf /:*)", "Bash(git push --force*)"]
  }
}
```

**Không có `"$defaults"` (thay thế các rule có sẵn của phần đó — hành vi duy nhất trước v2.1.118):**

```json
{
  "autoMode": {
    "allow": ["Bash(gh pr list:*)"]
  }
}
```

**Sau (mở rộng rule có sẵn — v2.1.118+):**

```json
{
  "autoMode": {
    "allow": ["$defaults", "Bash(gh pr list:*)"],
    "soft_deny": ["$defaults", "Bash(kubectl delete:*)"],
    "environment": ["$defaults", "trusted-ci.internal"]
  }
}
```

Dùng `"$defaults"` để giữ các rule nền có sẵn trong khi xếp thêm các bổ sung riêng của tổ chức hoặc dự án lên trên.

#### Phân loại mọi lệnh shell với `autoMode.classifyAllShell` (v2.1.193)

`autoMode.classifyAllShell` (boolean, v2.1.193+) định tuyến **mọi** lệnh Bash/PowerShell qua bộ phân loại của chế độ auto. Bật nó khi bạn muốn bộ phân loại kiểm tra mọi lệnh shell trong phiên.

```json
{
  "autoMode": {
    "classifyAllShell": true
  }
}
```

Cùng bản phát hành này hiển thị **lý do từ chối** khi chế độ auto chặn một hành động — thấy được trong transcript, toast từ chối và tab **Recently blocked** trong `/permissions` (trước v2.1.314 tên là Recently denied) (v2.1.193+).

#### Bảo vệ có sẵn dựa trên ý định (v2.1.183)

Tách biệt với `hard_deny` do người dùng cấu hình, chế độ auto chặn các lệnh phá hủy sau theo mặc định trừ khi bạn đã yêu cầu rõ ràng trong phiên này:

- `git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`
- `git commit --amend` (khi commit không phải do tác nhân tạo ra trong phiên này)
- `terraform destroy`, `pulumi destroy`, `cdk destroy` (trừ khi bạn yêu cầu với stack cụ thể)

Đây là bảo vệ mặc định có sẵn dựa trên ý định được suy ra — bạn không cần tự thêm chúng vào `hard_deny`.

### Hành Vi Dự Phòng

Khi bộ phân loại không chắc chắn, chế độ auto quay về hỏi người dùng:
- Sau **3 lần chặn liên tiếp** của bộ phân loại
- Sau **tổng cộng 20 lần chặn** của bộ phân loại trong một phiên

Điều này đảm bảo người dùng luôn giữ quyền kiểm soát khi bộ phân loại không thể tự tin phê duyệt một hành động.

### Khởi Tạo Quyền Tương Đương Chế Độ Auto

Nếu bạn muốn cách đơn giản hơn mà không cần bộ phân loại chạy nền, bạn có thể khởi tạo `~/.claude/settings.json` với một bộ rule quyền an toàn, thận trọng làm nền. Script bắt đầu với các rule chỉ đọc và kiểm tra cục bộ, sau đó cho phép bạn chọn bật chỉnh sửa, kiểm thử, ghi git cục bộ, cài đặt package và các hành động ghi trên GitHub chỉ khi bạn cần.

**File:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Xem trước những gì sẽ được thêm (không ghi thay đổi nào)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Áp dụng bộ nền thận trọng
python3 09-advanced-features/setup-auto-mode-permissions.py

# Chỉ thêm khả năng khi bạn cần
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

Script thêm các rule thuộc các nhóm sau:

| Nhóm | Ví dụ |
|----------|---------|
| Công cụ chỉ đọc cốt lõi | `Read(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| Kiểm tra cục bộ | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| Chỉnh sửa (tùy chọn) | `Edit(*)` |
| Test/build (tùy chọn) | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| Ghi git (tùy chọn) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)`, `Bash(git switch:*)`, `Bash(git stash:*)`, `Bash(git tag:*)` |
| Trình quản lý package | `Bash(npm ci:*)`, `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(pip3 install:*)` |
| Build & test | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell thông dụng | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

Các thao tác nguy hiểm (`rm -rf`, `sudo`, force push, `DROP TABLE`, `terraform destroy`, v.v.) được cố ý loại trừ. Script có tính idempotent — chạy hai lần sẽ không nhân đôi rule.

---

## Tác Vụ Nền

Tác vụ nền cho phép các thao tác chạy lâu được thực thi mà không chặn cuộc hội thoại của bạn.

### Tác Vụ Nền Là Gì?

Tác vụ nền chạy bất đồng bộ trong khi bạn tiếp tục làm việc:
- Bộ test dài
- Quá trình build
- Migration cơ sở dữ liệu
- Script deploy
- Công cụ phân tích

**Cách dùng cơ bản:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/tasks    # Xem và quản lý công việc nền (shell và tác nhân con); dừng tác vụ từ đây
Ctrl+B    # Chuyển một lệnh Bash hoặc tác nhân đang chạy xuống nền
```

### Khởi Chạy Tác Vụ Nền

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
View results: /tasks
```

### Quản Lý Tác Vụ Nền

Chạy `/tasks` (alias `/bashes`) để liệt kê các shell và tác nhân con đang chạy, mở một mục để xem đầu ra của nó, hoặc dừng nó. Không có lệnh con `/task` nào.

```text
User: /tasks

[Mở giao diện công việc nền: các shell và tác nhân con đang chạy,
 bao gồm cả các tác nhân con đã hoàn thành. Chọn một mục để xem
 đầu ra, hoặc dừng nó từ đây.]
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

Không có khối `settings.json` nào cho tác vụ nền. Tính năng này được kiểm soát bằng một biến môi trường:

```bash
# Tắt việc chạy Bash/tác nhân con ở nền và Ctrl+B (tác vụ MCP và công cụ Monitor vẫn chạy ở nền)
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
```

Mức độ đồng thời cũng không phải là cài đặt của tác vụ nền — số tác nhân chạy cùng lúc được quy định bởi `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (mặc định `20`).

Các lệnh Bash và PowerShell chạy nền chỉ có giới hạn thời gian trong các phiên không có người giám sát (v2.1.288): trong một lần chạy `-p`, một phiên Agent SDK, CI hoặc phiên cloud, lệnh được khởi chạy với `run_in_background` sẽ dừng sau `timeout` của nó — mặc định 30 phút (10 phút trong một lần chạy `-p` có prompt được truyền dưới dạng văn bản thay vì qua `--input-format stream-json`), tối đa 2 giờ — và Claude được thông báo khi lệnh bị dừng. Lệnh nền trong phiên terminal, ứng dụng desktop hoặc VS Code không có giới hạn thời gian (trong v2.1.285–v2.1.287, giới hạn áp dụng cho mọi phiên).

---

## Công Cụ Monitor (Luồng Hướng Sự Kiện)

> **Mới trong v2.1.98**: Công cụ Monitor cho phép Claude theo dõi stdout của một lệnh chạy nền và phản ứng ngay khi xuất hiện sự kiện khớp — thay thế cho các vòng lặp polling và `sleep` khi chờ các tiến trình chạy lâu.

Monitor gắn vào bất kỳ lệnh shell nào ghi ra stdout. Mỗi dòng stdout từ lệnh trở thành một thông báo đánh thức phiên. Claude chỉ định lệnh; harness stream đầu ra và chuyển giao sự kiện khi chúng xảy ra. Xem phần [Tác Vụ Nền](#tác-vụ-nền) liên quan để biết cách khởi chạy các tiến trình bên dưới.

> **Thời hạn (v2.1.271)**: mỗi lượt theo dõi của Monitor giờ đều có thời hạn — tối đa 30 phút, hoặc 10 phút trong các lần chạy `-p` một prompt. Khi hết hạn, Claude được thông báo để có thể đặt lại lượt theo dõi. Không còn cách nào để đặt một lượt theo dõi không bao giờ hết hạn.

> **Khả dụng (v2.1.310)**: trên Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform hoặc Microsoft Foundry, hoặc khi đặt `DISABLE_TELEMETRY` hay `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, Monitor cần Claude Code v2.1.310 trở lên. Trên Windows nó cần Git Bash.

> **Hook (v2.1.314)**: các hook khớp `Bash` giờ cũng chạy trên các lệnh shell mà công cụ Monitor khởi chạy — chúng có thể chặn hoặc hỏi, nhưng không thể phê duyệt hay viết lại các lệnh đó — và một điều kiện `if` của hook như `Monitor(tail *)` khớp các lệnh của Monitor giống cách `Bash(tail *)` khớp các lệnh của Bash.

### Vì Sao Nó Quan Trọng

Polling bằng `/loop` hoặc `sleep` tốn trọn một vòng gọi API mỗi chu kỳ, dù có gì thay đổi hay không. Monitor im lặng cho đến khi có sự kiện, tiêu tốn **không token nào** khi lệnh đang yên. Khi có sự kiện, Claude phản ứng ngay — không bị phát hiện trễ do phải chờ nhịp poll tiếp theo. Với bất cứ thứ gì chạy lâu hơn vài phút, cách này vừa rẻ hơn vừa nhanh hơn vòng lặp poll.

### Hai Mẫu Phổ Biến

**Bộ lọc luồng** theo dõi đầu ra liên tục từ một nguồn chạy lâu. Lệnh chạy mãi mãi; mỗi dòng khớp là một sự kiện.

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**Bộ lọc poll-và-phát** kiểm tra một nguồn theo chu kỳ và chỉ phát ra khi có thay đổi. Dùng cách này cho API, cơ sở dữ liệu hoặc bất cứ thứ gì không có luồng gốc.

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

### Ví Dụ Cụ Thể

"Khởi động dev server của tôi và theo dõi lỗi." Claude khởi chạy server dưới dạng tác vụ nền, gắn một bộ lọc Monitor (`tail -F server.log | grep --line-buffered -E "ERROR|FATAL"`), và phiên trở nên yên lặng. Ngay khi một dòng lỗi xuất hiện trong log, Claude thức dậy, đọc lỗi và có thể phản ứng — khởi động lại server, sửa lỗi hoặc báo cho bạn — mà bạn không cần phải kiểm tra.

> **Cảnh báo**: Khi pipe vào `grep`, **luôn** dùng `grep --line-buffered`. Nếu không, grep sẽ đệm stdout thành các khối 4KB, có thể làm trễ sự kiện tới vài phút trên các luồng ít lưu lượng. Đây là nguyên nhân số 1 khiến Monitor hỏng trong thực tế — nếu bộ lọc của bạn có vẻ im lặng khi lẽ ra không nên, hãy kiểm tra cờ `--line-buffered` trước tiên.

---

## Workflow Động

> **Mới trong v2.1.154**

Workflow động cho phép Claude điều phối hàng chục đến hàng trăm [tác nhân con](../04-subagents/README.md) chạy nền một cách **tất định** — fan-out, pipeline và các giai đoạn song song được mã hóa trong một script thay vì để model tùy ứng biến. Trong khi một tác nhân đơn lẻ giữ một cửa sổ ngữ cảnh, một workflow chia nhỏ tác vụ cho nhiều tác nhân và kết hợp lại kết quả của chúng.

Từ v2.1.219, workflow động mặc định theo **hướng dẫn kích thước trung bình (nhắm tới ít hơn 10 tác nhân)** — hoặc **nhỏ** khi bạn đăng nhập bằng gói Pro, từ v2.1.271. Chọn kích thước khác — hoặc không giới hạn — qua **Dynamic workflow size** trong `/config`, hoặc đặt khóa `workflowSizeGuideline` trong file cài đặt. Dòng trạng thái của workflow đang chạy hiển thị kích thước đang áp dụng và chỉ tới `/config` để thay đổi.

### Khi Nào Nên Dùng

- **Bao phủ toàn diện** — audit hoặc review song song trên nhiều file/khía cạnh.
- **Độ tin cậy** — tạo ra các góc nhìn độc lập, sau đó kiểm chứng đối kháng các phát hiện trước khi chốt.
- **Mở rộng vượt một ngữ cảnh** — các migration lớn, quét diện rộng hoặc nghiên cứu mà không ngữ cảnh đơn lẻ nào chứa nổi.

Với một tác vụ một lần mà bạn đã hiểu rõ, một tác nhân đơn lẻ (hoặc chỉnh sửa trực tiếp) vẫn là công cụ phù hợp — workflow phát huy hiệu quả khi công việc cần fan-out.

### Khởi Chạy và Theo Dõi

- **Khởi chạy**: yêu cầu Claude tạo workflow cho tác vụ (ví dụ "run a workflow to review every file in `src/`"). Claude viết script điều phối và chạy nó ở nền.
- **Theo dõi**: lệnh `/workflows` hiển thị các lượt chạy workflow đang chạy và đã hoàn thành với tiến độ trực tiếp.
- **`ultracode`**: bật nó bằng nút Ultracode trong thanh trượt `/effort` (Tab) hoặc `/effort ultracode [on|off]` — khi đó Claude điều phối workflow động theo mặc định, ở bất kỳ mức effort nào phiên đang chạy. Từ v2.1.284, nút bật/tắt giữ nguyên mức effort (trước đây nó ép `xhigh`); `--effort ultracode` và `effortLevel: "ultracode"` của Agent SDK vẫn đặt `xhigh`. `/effort ultracode` kéo dài trong phiên; đặt khóa `ultracode` trong cài đặt để mọi phiên khởi động với nó (`effortLevel` và `CLAUDE_CODE_EFFORT_LEVEL` không chấp nhận `ultracode`). (Từ v2.1.160, từ khóa kích hoạt là `ultracode`; từ "workflow" đơn thuần không còn kích hoạt một lượt chạy.)

Workflow xây dựng trên mô hình tác nhân con — xem [Tác Nhân Con](../04-subagents/README.md) để biết cách định nghĩa và giới hạn phạm vi từng tác nhân.

---

## Tác Vụ Theo Lịch

Tác vụ theo lịch cho phép bạn chạy prompt tự động theo lịch lặp lại hoặc dưới dạng nhắc nhở một lần. Các tác vụ gắn với phiên — chúng chỉ kích hoạt khi Claude Code đang chạy. Khi bạn tiếp tục phiên bằng `--resume` hoặc `--continue`, Claude Code khôi phục các tác vụ chưa hết hạn, trừ các tác vụ một lần đã quá giờ và `/loop` tự điều nhịp (chạy lại `/loop` để khởi động lại nó). Có từ v2.1.72+.

> **"Routines" giờ là "cloud scheduled tasks" (tháng 10/2026)**: Tài liệu của Anthropic đã đổi tên Routines — các tác vụ cloud bạn tạo bằng `/schedule` (alias `/routines`; xem bên dưới) — thành **cloud scheduled tasks (formerly routines)**, và gọi các tác vụ `/loop` và cron trên trang này là **session-scoped scheduled tasks**. Tên cũ vẫn còn trong URL `claude.ai/code/routines`, API `/fire` và nút bật/tắt quản trị **Scheduled tasks (Was Routines)**.

### Lệnh `/loop`

```bash
# Khoảng thời gian tường minh
/loop 5m check if the deployment finished

# Ngôn ngữ tự nhiên
/loop check build status every 30 minutes
```

Biểu thức cron 5 trường tiêu chuẩn cũng được hỗ trợ để lập lịch chính xác.

### Nhắc nhở một lần

Đặt nhắc nhở kích hoạt một lần vào một thời điểm cụ thể:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Quản lý tác vụ theo lịch

| Công cụ | Mô tả |
|------|-------------|
| `CronCreate` | Tạo một tác vụ theo lịch mới |
| `CronList` | Liệt kê mọi tác vụ theo lịch đang hoạt động. Từ v2.1.136, đầu ra còn bao gồm (các) qualifier và nội dung prompt được lên lịch, để bạn có thể kiểm tra mỗi cron sẽ chạy gì mà không cần mở nó. |
| `CronDelete` | Xóa một tác vụ theo lịch |

**Giới hạn và hành vi**:
- Tối đa **50 tác vụ theo lịch** mỗi phiên
- Gắn với phiên — được khôi phục khi `--resume`/`--continue` nếu chưa hết hạn
- Tác vụ lặp lại tự hết hạn **7 ngày** sau khi tạo (chúng kích hoạt một lần cuối rồi tự xóa)
- Tác vụ chỉ kích hoạt khi Claude Code đang chạy — không bù cho các lần bị lỡ

### Chi tiết hành vi

| Khía cạnh | Chi tiết |
|--------|--------|
| **Jitter cho tác vụ lặp lại** | Chạy trễ tối đa một nửa khoảng cách tới lần chạy kế tiếp, không quá 30 phút; tác vụ `*/5 * * * *` (do `/loop 5m` tạo) không bị trễ và bắt đầu sớm 15 giây |
| **Jitter cho tác vụ một lần** | Sớm tối đa 90 giây khi được lên lịch vào `:00` hoặc `:30` |
| **Lần kích hoạt bị lỡ** | Không bù — bị bỏ qua nếu Claude Code không chạy |
| **Tính bền vững** | Được khôi phục khi `--resume`/`--continue`, trừ tác vụ đã hết hạn, tác vụ một lần đã quá giờ và `/loop` tự điều nhịp; các lần chạy bị lỡ không được bù |

### Tác Vụ Theo Lịch Trên Cloud

Dùng `/schedule` để tạo tác vụ theo lịch trên cloud chạy trên hạ tầng của Anthropic:

```
/schedule daily at 9am run the test suite and report failures
```

Tác vụ theo lịch trên cloud được lưu qua các lần khởi động lại và không cần Claude Code chạy cục bộ. Mỗi lượt chạy bắt đầu ở chế độ auto trừ khi chế độ auto không khả dụng, nên một bộ phân loại sẽ phê duyệt hoặc chặn các hành động; một lượt chạy vẫn dừng lại và chờ câu trả lời trong phiên của nó khi một rule ask khớp hoặc số lần chặn chạm ngưỡng chặn lặp lại của chế độ auto. Trên gói Enterprise dùng vai trò tùy chỉnh, bạn còn cần một vai trò có quyền scheduled tasks.

### Tắt tác vụ theo lịch

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

> **`/schedule` bị tự động tắt ở các tier API key (v2.1.139)**: `/schedule` trên cloud âm thầm không khả dụng khi bất kỳ biến nào trong `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` hoặc `apiKeyHelper` được đặt — kể cả khi bạn cũng đã đăng nhập bằng claude.ai. Cùng điều kiện đó cũng tắt [Điều Khiển Từ Xa](#tắt-điều-khiển-từ-xa-disableremotecontrol-v21128), các connector MCP của claude.ai và tùy chọn thông báo. Bỏ đặt API key (hoặc chạy trên tier OAuth Pro/Max/Ultra) để dùng `/schedule`. `CronCreate` cục bộ không bị ảnh hưởng.

### Ví dụ: theo dõi một lần deploy

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Mẹo**: Tác vụ theo lịch gắn với phiên. Để có tự động hóa bền vững qua các lần khởi động lại, hãy dùng pipeline CI/CD, GitHub Actions hoặc tác vụ theo lịch của Ứng Dụng Desktop thay thế.

---

## Chế Độ Quyền

Chế độ quyền kiểm soát những hành động Claude có thể thực hiện mà không cần phê duyệt tường minh.

### Các Chế Độ Quyền Có Sẵn

| Chế độ | Hành vi |
|---|---|
| `manual` | Chỉ đọc file; hỏi cho mọi hành động khác. Đổi tên từ `default` trong v2.1.200 — `default` vẫn được chấp nhận như alias |
| `acceptEdits` | Đọc và chỉnh sửa file; hỏi khi chạy lệnh |
| `plan` | Chỉ đọc file (chế độ nghiên cứu, không chỉnh sửa) |
| `auto` | Mọi hành động, có kiểm tra của bộ phân loại an toàn chạy nền. Cần model đủ điều kiện (Sonnet 5 trở lên, Opus 4.7 trở lên, Haiku 5.5 hoặc một model Fable trên mọi nhà cung cấp; Opus 4.6 và Sonnet 4.6 cũng đủ điều kiện trên Anthropic API và Claude Platform on AWS) và nhà cung cấp phù hợp — có trên mọi gói, xem [Chế Độ Auto](#chế-độ-auto) |
| `bypassPermissions` | Mọi hành động mà không hỏi, trừ những hành động không chế độ nào tự động phê duyệt, như các lệnh xóa `rm` trên đường dẫn quan trọng (nguy hiểm) |
| `dontAsk` | Chỉ các công cụ đã được phê duyệt trước mới thực thi; mọi công cụ khác bị từ chối |

> **Lưu ý**: Chế độ quyền `default` được đổi tên thành **Manual** trong v2.1.200 (trên CLI, `--help`, VS Code và JetBrains), và một huy hiệu ⏸ màu xám xuất hiện ở chân trang khi chế độ này đang bật (v2.1.203). Cả `--permission-mode manual` và `--permission-mode default` đều hoạt động, cũng như `"defaultMode": "manual"` và `"defaultMode": "default"` trong cài đặt. Lưu ý khóa cài đặt là `permissions.defaultMode` — không có khóa `permissions.mode`, nên các ví dụ bên dưới dùng cách viết chuẩn.

Chuyển vòng qua các chế độ bằng `Shift+Tab` trong CLI. Đặt mặc định bằng cờ `--permission-mode` hoặc cài đặt `permissions.defaultMode`. Khi chưa cấu hình chế độ quyền nào, các phiên terminal tương tác và VS Code khởi động ở chế độ auto trên mọi gói và nhà cung cấp từ v2.1.284 (v2.1.283 chỉ làm vậy trên các nhà cung cấp bên thứ ba như Bedrock, Google Cloud's Agent Platform và Foundry, hoặc khi tắt telemetry); `permissions.defaultMode` vẫn ghi đè điều này, và một phiên không có chế độ auto sẽ khởi động ở Manual thay vào đó. Từ v2.1.302, một lượt chạy `claude -p` hoặc Agent SDK không đặt chế độ quyền sẽ khởi động ở chế độ Manual (giá trị cấu hình `default`) và từ chối các lời gọi công cụ cần phê duyệt; hãy truyền `--permission-mode` (ví dụ `auto` hoặc `acceptEdits`) hoặc `--allowedTools`.

> **Chế độ plan nhường lệnh shell cho bộ phân loại (v2.1.218)**: Khi [chế độ auto](#chế-độ-auto) khả dụng và cài đặt `useAutoModeDuringPlan` đang bật — mặc định là bật — bộ phân loại sẽ review các lệnh shell trong khi lập kế hoạch thay vì hỏi bạn. Lệnh được phê duyệt sẽ chạy, lệnh bị từ chối sẽ bị chặn. Chế độ plan vẫn chặn ghi file vô điều kiện.

Từ v2.1.160, ngay cả `acceptEdits` cũng hỏi trước khi ghi các file khởi động shell (`.zshenv`, `.zlogin`, `.bash_login`, `~/.config/git/`) và các cấu hình build có thể thực thi code (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, …), vốn có thể dẫn đến việc thực thi lệnh ngoài ý muốn.

> **`--dangerously-skip-permissions` mở rộng phạm vi đường dẫn (v2.1.121, v2.1.126)**: Cờ CLI `--dangerously-skip-permissions` (và chế độ `bypassPermissions` tương đương) giờ bỏ qua prompt cho việc ghi vào một danh sách cho phép rộng hơn nhiều — `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/`, `.git/`, `.vscode/` và các file cấu hình shell. Các lệnh xóa thảm họa (`rm -rf /`, v.v.) vẫn hỏi trong chế độ này — từ v2.1.281, prompt trong terminal chờ 2 phút rồi từ chối lệnh kèm gợi ý viết lại để các phiên không giám sát tiếp tục chạy, và từ v2.1.309 ứng dụng Desktop và VS Code từ chối ngay kèm gợi ý đó, trừ khi một hook `PermissionRequest` cho phép (`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` tắt thời gian chờ trong terminal và khiến panel VS Code hỏi thay vì từ chối). Chế độ auto xử lý các lệnh xóa đường dẫn quan trọng này theo cùng cách — prompt 2 phút trong terminal, từ chối ngay ở nơi khác — và chỉ gửi chúng cho bộ phân loại khi biến đó được đặt. Các lệnh bị gắn cờ `Dangerous rm operation not ruled out` (shell có thể đọc chúng khác với cách chúng được phân tích) cũng được xử lý như vậy, và không rule allow `Bash(*)`, cơ chế tự cho phép của sandbox hay `"allow"` của `PreToolUse` nào phê duyệt được chúng. Từ v2.1.311, khởi động Claude Code với `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS=1` trong môi trường khởi chạy (bị bỏ qua trong khối `env` của cài đặt) cho phép các lệnh xóa này chạy không cần hỏi ngay trong chế độ `bypassPermissions` — không áp dụng trong plan mode, panel VS Code hay Desktop, và không áp dụng khi có một hook `PermissionRequest`, một rule deny hoặc ask trên Bash, Edit hoặc Read, hay một `--permission-prompt-tool`. Từ v2.1.304, lệnh `rm` đệ quy trên đường dẫn ổ đĩa được mount như `/Volumes/USB` hoặc `/mnt/c/Users` của WSL cũng được xử lý tương tự kể cả khi có rule allow cho `rm`; khởi động Claude Code với `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1` để tắt prompt đó (khối `env` trong cài đặt bị bỏ qua). Hãy coi cờ này là công cụ sắc bén hơn trước; chỉ dùng nó trong các sandbox dùng một lần.

> **Phát hiện shell trên Windows (v2.1.120, v2.1.126)**: Git for Windows / Git Bash không còn bắt buộc. Khi không có Git Bash, Claude Code dùng PowerShell làm công cụ shell. Từ v2.1.126, PowerShell là shell *chính* khi công cụ PowerShell được bật, và việc phát hiện bao gồm PowerShell 7 cài qua Microsoft Store, MSI không có PATH, hoặc dưới dạng `.NET global tool`.

> **Công cụ PowerShell bật mặc định trên Windows cho Bedrock/Vertex/Foundry (v2.1.143)**: Từ v2.1.143, công cụ PowerShell được **bật mặc định trên Windows** cho người dùng Bedrock, Vertex và Foundry. Claude Code gọi PowerShell với `-ExecutionPolicy Bypass` để script chạy được kể cả khi chính sách hệ thống là `Restricted`. Để Claude Code tôn trọng execution policy của hệ thống, đặt `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`. Để tắt hoàn toàn công cụ PowerShell, đặt `CLAUDE_CODE_USE_POWERSHELL_TOOL=0`.

### Cách Kích Hoạt

**Phím tắt**:
```bash
Shift + Tab  # Chuyển vòng default → acceptEdits → plan, sau đó bypassPermissions/auto khi khả dụng (dontAsk không bao giờ xuất hiện trong vòng)
```

**Lệnh slash**:
```bash
/plan                  # Vào chế độ plan
```

**Cờ CLI**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Cài đặt**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Ví Dụ Về Chế Độ Quyền

#### Chế Độ Mặc Định
Claude hỏi xác nhận cho các hành động quan trọng:

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Chế Độ Plan
Review kế hoạch triển khai trước khi thực thi:

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

### Trường Hợp Sử Dụng

**Review code**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Lập trình cặp**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Tác vụ tự động**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## Chế Độ Headless

Chế độ print (`claude -p`) cho phép Claude Code chạy mà không cần đầu vào tương tác, hoàn hảo cho tự động hóa và CI/CD. Đây là chế độ không tương tác, thay thế cho cờ `--headless` cũ.

### Chế Độ Print Là Gì?

Chế độ print cho phép:
- Thực thi script tự động
- Tích hợp CI/CD
- Xử lý hàng loạt
- Tác vụ theo lịch

### Chạy Ở Chế Độ Print (Không Tương Tác)

```bash
# Chạy một tác vụ cụ thể
claude -p "Run all tests" --permission-mode auto

# Xử lý nội dung được pipe vào
cat error.log | claude -p "Analyze these errors"

# Tích hợp CI/CD (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Thêm Ví Dụ Dùng Chế Độ Print

```bash
# Chạy một tác vụ cụ thể và thu đầu ra
claude -p "Run all tests and generate coverage report" --permission-mode auto

# Với đầu ra có cấu trúc
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

### Cấu Hình Chế Độ Print

Chế độ print (`claude -p`) hỗ trợ nhiều cờ cho tự động hóa:

```bash
# Giới hạn số lượt tự chủ
claude -p --max-turns 5 "refactor this module"

# Đầu ra JSON có cấu trúc
claude -p --output-format json "analyze this codebase"

# Có xác thực schema
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Tắt lưu phiên
claude -p --no-session-persistence "one-off analysis"
```

### Chế Độ An Toàn (khắc phục sự cố)

`--safe-mode` (và biến môi trường `CLAUDE_CODE_SAFE_MODE`, ví dụ `CLAUDE_CODE_SAFE_MODE=1`) khởi động Claude Code với **mọi tùy chỉnh bị tắt** — CLAUDE.md, plugin, skill, hook và MCP server đều bị tắt.

```bash
# Khởi chạy với mọi tùy chỉnh bị tắt
claude --safe-mode

# Tương đương qua biến môi trường
CLAUDE_CODE_SAFE_MODE=1 claude
```

Đây là công cụ khắc phục sự cố: khi một cấu hình tùy chỉnh gây ra vấn đề, hãy khởi chạy ở chế độ an toàn để xác định vấn đề nằm ở thiết lập của bạn hay ở chính Claude Code.

---

## Quản Lý Phiên

Quản lý hiệu quả nhiều phiên Claude Code.

### Các Lệnh Quản Lý Phiên

| Lệnh | Mô tả |
|---------|-------------|
| `/resume` | Tiếp tục một cuộc hội thoại theo ID hoặc tên |
| `/rename` | Đặt tên cho phiên hiện tại |
| `/fork [prompt]` | Sao chép cuộc hội thoại sang một phiên nền độc lập mới và tiếp tục làm việc ở đây (v2.1.212+) |
| `/subtask <task>` | Tạo một tác nhân con được fork, kế thừa toàn bộ cuộc hội thoại và báo kết quả về đây (v2.1.212+) |
| `/branch [name]` | Chuyển vào một bản sao của cuộc hội thoại tại thời điểm này, giữ nguyên bản gốc |
| `claude -c` | Tiếp tục cuộc hội thoại gần nhất |
| `claude -r "session"` | Tiếp tục phiên theo tên hoặc ID |

### Tiếp Tục Phiên

**Tiếp tục cuộc hội thoại gần nhất**:
```bash
claude -c
```

**Tiếp tục một phiên có tên**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Đổi tên phiên hiện tại** (bên trong REPL):
```
/rename auth-refactor
```

> **Cập nhật v2.1.212**: Gõ `/resume` (không có đối số) trong agent view giờ mở bộ chọn các phiên trước đó — bao gồm cả các phiên đã bị xóa khỏi danh sách hiển thị — và tiếp tục phiên được chọn dưới dạng phiên nền.

> **Cập nhật v2.1.304**: Trên gói Pro, Max và Ultra, việc tiếp tục một cuộc hội thoại đã lâu không hoạt động mà sẽ dùng một phần đáng kể giới hạn sử dụng 5 giờ của bạn sẽ hiển thị hộp thoại **Resume this conversation?**: vẫn tiếp tục, hoặc bắt đầu cuộc hội thoại mới (Claude vẫn có thể tra cứu cuộc hội thoại trước nếu bạn nhắc tới).

### Fork và Phân Nhánh Phiên

Ba lệnh tạo bản sao của cuộc hội thoại, và chúng khác nhau ở *nơi bản sao chạy*:

`/subtask <task>` tạo một tác nhân con được fork, kế thừa toàn bộ cuộc hội thoại và làm tác vụ trong khi bạn tiếp tục làm việc — có dòng riêng trong `claude agents`, với kết quả được trả về cuộc hội thoại của bạn khi xong:

```
/subtask Investigate why the auth tests are flaky
```

`/fork [prompt]` thì sao chép cuộc hội thoại sang một **phiên nền** mới. Bản sao bắt đầu với mọi thứ cho tới hiện tại và chạy độc lập — không có gì quay về cuộc hội thoại này:

```
/fork Try the OAuth approach end to end
```

Để tự chuyển vào một bản sao thay vì ủy thác, hãy dùng `/branch [name]`, lệnh này giữ nguyên bản gốc và cho phép bạn quay lại bằng `/resume`:

```
/branch try-oauth-instead
```

> **Lưu ý**: `/fork` và `/subtask` đã hoán đổi vai trò trong **v2.1.212**. Trước v2.1.161, `/fork` là alias của `/branch`; từ v2.1.161 đến v2.1.211 nó khởi chạy một tác nhân con được fork — hành vi mà giờ `/subtask` đảm nhận. Khi agent view bị tắt, `/subtask` không khả dụng và `/fork` giữ hành vi tác nhân con được fork.

Hoặc fork từ CLI:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Lưu Trữ Phiên

Các phiên được tự động lưu và có thể tiếp tục:

```bash
# Tiếp tục cuộc hội thoại gần nhất
claude -c

# Tiếp tục phiên cụ thể theo tên hoặc ID
claude -r "auth-refactor"

# Tiếp tục và fork để thử nghiệm
claude --resume auth-refactor --fork-session "alternative approach"
```

### Tự Động Tiếp Tục Khi Chạm Giới Hạn Sử Dụng (v2.1.234)

Từ **v2.1.234**, một phiên bị chặn do giới hạn sử dụng claude.ai sẽ tự tiếp tục khi giới hạn đó được đặt lại — không cần prompt lại thủ công. Bật/tắt trong `/config` tại mục "Continue automatically at usage limit."

### Tóm Tắt Phiên (v2.1.108)

Khi bạn quay lại một phiên sau một thời gian vắng, Claude có thể hiển thị tóm tắt ngắn những gì đã hoàn thành. Tính năng này bật mặc định cho mọi gói và nhà cung cấp; tắt nó trong `/config` → **Session recap**.

> **OTEL telemetry — bật lại khảo sát phản hồi (v2.1.136+)**: Các tổ chức thu thập dữ liệu OpenTelemetry có thể bật lại khảo sát chất lượng phiên của Anthropic bằng cách đặt `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1`. Khảo sát bị tắt mặc định trong các triển khai OTEL vì trước đây nó được chuyển hướng khỏi pipeline telemetry.

> **OTEL telemetry — sự kiện log `assistant_response` (v2.1.193+)**: Claude Code phát ra sự kiện log OpenTelemetry `claude_code.assistant_response` chứa nội dung phản hồi của model, cho phép pipeline OTEL ghi lại những gì Claude nói bên cạnh telemetry công cụ/sự kiện hiện có.

> **OTEL telemetry — thuộc tính cache và GenAI (v2.1.300)**: Các sự kiện `api_request` thêm `cache_creation_5m_tokens`/`cache_creation_1h_tokens`, và các span mang thuộc tính theo quy ước ngữ nghĩa GenAI như `gen_ai.provider.name`.

> **OTEL telemetry — thuộc tính `tool_decision` (v2.1.301)**: Các sự kiện `tool_decision` thêm `classifier_verdict` và `permission_mode`.

> **OTEL telemetry — `safety_event` (v2.1.307; không còn được gửi từ v2.1.312)**: một sự kiện log `claude_code.safety_event` từng được phát cho mỗi lời gọi công cụ mà một rule quyền, chế độ auto, một kiểm tra an toàn, một hook hoặc sandbox đã từ chối, hỏi lại hoặc gửi trả, với các thuộc tính `category`, `decision` (`accept`/`reject`/`sent_back`) và `decision_source`. Nó không chứa nội dung lệnh, đường dẫn file hay tên host. Theo changelog v2.1.312, Claude Code không còn gửi sự kiện này nữa, dù tài liệu monitoring vẫn liệt kê nó.

> **OTEL telemetry — thuộc tính liên kết (v2.1.310)**: Các sự kiện `tool_decision` và `tool_result` thêm `request_id` để liên kết một lời gọi với phản hồi API của nó, và các sự kiện của tác nhân con mang `parent_agent_id`.

**Kiểm soát hành vi tóm tắt:**

```bash
/recap                                 # kích hoạt tóm tắt thủ công
/config                                # bật/tắt tự động tóm tắt
```

Hoặc qua biến môi trường:
```bash
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0 claude   # tắt tóm tắt
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=1 claude   # buộc bật tóm tắt
```

---

## Nhắn Tin Giữa Các Phiên

> **Được thêm trong v2.1.224**, mở rộng đến v2.1.239. Có trên **macOS, Linux và (từ v2.1.239) Windows**.

Trước đây các phiên giống như những hòn đảo riêng biệt. Nhắn tin giữa các phiên cho phép một phiên Claude Code
trò chuyện với phiên khác — bao gồm các phiên trên những máy khác của bạn và các phiên cloud — để bạn có thể
chuyển câu hỏi cho phiên đã nạp sẵn đúng ngữ cảnh thay vì phải
giải thích lại.

### Khám Phá Các Phiên

`ListAgents` liệt kê mọi thứ bạn có thể gửi tới: các tác nhân con bạn đã tạo, các phiên cục bộ khác
trên máy này, các phiên cloud của bạn và (khi Điều Khiển Từ Xa được kết nối) các phiên trên
những máy khác của bạn. Mỗi dòng được gắn nhãn theo loại, và từ v2.1.229 các dòng còn mang nhãn
`offline` và `cloud` để bạn phân biệt phiên có thể liên lạc được với phiên đang ngủ.

**Tên trong mỗi dòng chính là địa chỉ** — đó là thứ bạn gửi tới.

### Gửi Tin Nhắn

`SendMessage` nhận đích và tin nhắn:

```text
SendMessage({ to: "<session name>", message: "What did you conclude about the retry logic?" })
```

Từ v2.1.232, chỉ cần tên là đủ — bạn không cần thêm ref để phân biệt nữa
trừ khi hai dòng thực sự trùng tên.

### Chờ Một Phiên Rảnh (`notify_when_idle`, v2.1.236)

Khi phiên bạn nhắn tin đang giữa chừng một tác vụ, bạn thường muốn biết khi nào nó xong
thay vì poll nó. `SendMessage` nhận đầu vào `notify_when_idle` chính cho việc đó:

```text
SendMessage({
  to: "auth-refactor",
  message: "ping me when the migration finishes",
  notify_when_idle: true
})
```

Tính năng này là **opt-in và chỉ một lần** — phiên đích gửi một thông báo duy nhất vào lần tiếp theo
nó rảnh, và sau đó đăng ký kết thúc. Không có vòng lặp poll và không có thông báo
lặp lại nếu phiên bận rồi rảnh trở lại.

Hai thay đổi liên quan trong v2.1.239: `ListAgents` giờ còn báo cáo **tên của chính phiên đó** (để
một phiên có thể cho các phiên khác biết cách gửi tới nó) bên cạnh các đồng đội đang hoạt động, và nhắn tin giữa các phiên
trở nên khả dụng trên **Windows**.

### Cú Pháp Tắt `@`-Mention (v2.1.232)

Thay vì gọi công cụ một cách tường minh, bạn có thể `@`-mention một phiên trực tiếp trong
prompt để liên lạc với nó:

```text
@auth-refactor did the migration tests pass?
```

### Kiểm Soát Những Gì Được Nhận: `crossSessionInbound`

Tin nhắn đến được điều chỉnh bởi cài đặt `crossSessionInbound` (v2.1.224+):

| Giá trị | Hành vi |
|---|---|
| `"accept"` | Tin nhắn đến được chuyển tới Claude trong phiên này |
| `"hold"` | Bạn thấy thông báo có tin nhắn đến; tin nhắn không được chuyển tiếp |
| `"refuse"` | Tin nhắn đến bị bỏ |

Các giá trị tạo thành một thang bậc — `accept < hold < refuse` — và **cài đặt project và local
chỉ áp dụng khi chúng nghiêm ngặt hơn** giá trị ở phạm vi user. Một project có thể thắt chặt
việc nhận tin nhắn, không bao giờ nới lỏng. Từ v2.1.232, cài đặt này còn có một dòng trong `/config`,
"Messages from your other sessions."

### Phạm Vi và Giới Hạn

- Các phiên cục bộ trên cùng máy, cộng với các phiên cloud của bạn.
- Các phiên Điều Khiển Từ Xa trên những máy khác của bạn, có thể gửi tới theo tên (v2.1.225).
- Một phiên cloud **nhận** được tin nhắn của bạn nhưng chưa thể nhắn lại cho phiên cục bộ —
  hãy đọc câu trả lời trong transcript của chính nó.
- macOS và Linux từ v2.1.224; Windows từ v2.1.239.

---

## Tính Năng Tương Tác

### Phím Tắt

Claude Code hỗ trợ phím tắt để tăng hiệu quả. Đây là bảng tham chiếu đầy đủ từ tài liệu chính thức:

| Phím tắt | Mô tả |
|----------|-------------|
| `Ctrl+C` | Hủy đầu vào/quá trình sinh hiện tại |
| `Ctrl+D` | Thoát Claude Code |
| `Ctrl+G` | Chỉnh sửa kế hoạch trong trình soạn thảo bên ngoài |
| `Ctrl+L` | Vẽ lại màn hình (chỉ repaint — phím tắt nhấn hai lần để `/clear` đã bị bỏ trong v2.1.238) |
| `Ctrl+O` | Bật/tắt đầu ra chi tiết (xem quá trình suy luận) |
| `Ctrl+R` | Tìm ngược trong lịch sử. Mặc định là **mọi prompt trên mọi dự án** (v2.1.129+); nhấn `Ctrl+S` trong bộ chọn để thu hẹp về dự án hiện tại. Các phiên bản trước mặc định chỉ trong dự án. |
| `Ctrl+T` | Bật/tắt giao diện danh sách tác vụ |
| `Ctrl+B` | Đưa các tác vụ đang chạy xuống nền |
| `Esc+Esc` | Tua lại code/cuộc hội thoại |
| `Shift+Tab` / `Alt+M` | Chuyển đổi chế độ quyền |
| `Option+P` / `Alt+P` | Đổi model |
| `Option+T` / `Alt+T` | Bật/tắt tư duy mở rộng |
| `Option+O` / `Alt+O` | Bật/tắt chế độ nhanh (`/fast`) |
| `Ctrl+X` `Ctrl+K` | Dừng mọi tác nhân con chạy nền |
| `Ctrl+Enter` (hoặc `Ctrl+X` `Ctrl+S`) | Gửi ngay — gửi tất cả tin nhắn đang xếp hàng cùng lúc. Từ v2.1.281, các công cụ và tác nhân con đang chạy được chuyển xuống nền thay vì hủy lượt. Tin nhắn đã gửi và đang xếp hàng giữ màu xám cho đến khi model nhận được chúng (v2.1.275) |
| `Ctrl+S` | Cất tạm prompt hiện tại; nhấn lần nữa để khôi phục |
| `Ctrl+_` | Hoàn tác lần chỉnh sửa cuối trong ô nhập prompt |
| `:` | Gõ `:` ở đầu một từ để mở gợi ý emoji shortcode, ví dụ `:heart:` (v2.1.217+) |

**Chỉnh sửa dòng (phím tắt readline tiêu chuẩn):**

| Phím tắt | Hành động |
|----------|--------|
| `Ctrl + A` | Di chuyển về đầu dòng |
| `Ctrl + E` | Di chuyển về cuối dòng |
| `Ctrl + K` | Cắt tới cuối dòng |
| `Ctrl + U` | Cắt tới đầu dòng |
| `Ctrl + W` | Xóa từ phía trước |
| `Ctrl + Y` | Dán (yank) |
| `Tab` | Tự động hoàn thành |
| `↑ / ↓` | Lịch sử lệnh |

### Trợ Năng

Chế độ trình đọc màn hình (v2.1.208+) chuyển CLI sang chế độ hiển thị văn bản thuần được thiết kế cho trình đọc màn hình. Bật nó bằng cờ CLI, biến môi trường hoặc khóa `axScreenReader` trong cài đặt user (`~/.claude/settings.json`), cài đặt được quản lý hoặc một file được truyền qua `--settings` — từ v2.1.305, Claude Code bỏ qua khóa này, và các biến `CLAUDE_AX_*` trong khối `env`, trong cài đặt project và local:

```bash
claude --ax-screen-reader
```

```bash
export CLAUDE_AX_SCREEN_READER=1
```

```json
{
  "axScreenReader": true
}
```

### Tùy chỉnh phím tắt

Tạo phím tắt tùy chỉnh bằng cách chạy `/keybindings`, lệnh này mở `~/.claude/keybindings.json` để chỉnh sửa (v2.1.18+).

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

Đặt một binding thành `null` để gỡ phím tắt mặc định.

### Các context có sẵn

Phím tắt được giới hạn theo các context UI cụ thể:

| Context | Hành động chính |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | Điều hướng cài đặt theo context |
| **Tabs** | Chuyển và quản lý tab |
| **Help** | Điều hướng bảng trợ giúp |

Tổng cộng có 18 context, bao gồm `Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker` và `Select`.

### Hỗ trợ chord

Phím tắt hỗ trợ chuỗi chord (tổ hợp nhiều phím):

```
"ctrl+k ctrl+s"   → Two-key sequence: press ctrl+k, then ctrl+s
"ctrl+shift+p"    → Simultaneous modifier keys
```

**Cú pháp phím bấm**:
- **Phím bổ trợ**: `ctrl` (hoặc `control`), `alt` (hoặc `opt`, `option`, `meta`), `shift` và `cmd` (hoặc `command`, `super`, `win`) — `cmd` là phím bổ trợ riêng, không phải alias của `meta`, và chỉ được nhận diện trong các terminal có báo phím Super
- **Chữ hoa ngụ ý Shift**: `K` tương đương `shift+k`
- **Phím đặc biệt**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, các phím mũi tên

### Phím dành riêng và phím xung đột

| Phím | Trạng thái | Ghi chú |
|-----|--------|-------|
| `Ctrl+C` | Dành riêng | Không thể gán lại (ngắt) |
| `Ctrl+D` | Dành riêng | Không thể gán lại (thoát) |
| `Ctrl+B` | Xung đột terminal | Phím prefix của tmux |
| `Ctrl+A` | Xung đột terminal | Phím prefix của GNU Screen |
| `Ctrl+Z` | Xung đột terminal | Tạm dừng tiến trình |

> **Mẹo**: Nếu một phím tắt không hoạt động, hãy kiểm tra xung đột với trình giả lập terminal hoặc multiplexer của bạn.

### Tự Động Hoàn Thành Bằng Tab

Claude Code cung cấp tính năng tự động hoàn thành bằng tab thông minh:

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
User: <↑>  # Lệnh trước đó
User: <↓>  # Lệnh tiếp theo
User: Ctrl+R  # Tìm trong lịch sử

(reverse-i-search)`test': run all tests
```

### Nhập Nhiều Dòng

Với các truy vấn phức tạp, xuống dòng mới bằng `\` + Enter, Option+Enter (macOS), Shift+Enter hoặc Ctrl+J. Không có ký hiệu kết thúc `\end` — nhấn Enter để gửi:

```bash
User: Long complex prompt \
spanning multiple lines
```

**Ví dụ:**

```
User: Implement a user authentication system \
with the following requirements: \
- JWT tokens \
- Email verification \
- Password reset \
- 2FA support

Claude: [Processes the multi-line request]
```

### Chỉnh Sửa Tại Chỗ

Chỉnh sửa lệnh trước khi gửi:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Chế Độ Vim

Bật phím tắt Vi/Vim để chỉnh sửa văn bản:

**Kích hoạt**:
- Bật qua `/config` (bật/tắt "Editor / Vim mode") hoặc trong `~/.claude/settings.json` với `editorMode: "vim"`. Lệnh slash `/vim` độc lập đã bị bỏ (xem [issue #43370](https://github.com/anthropics/claude-code/issues/43370)); chế độ vim giờ được điều khiển bằng cấu hình.
- Chuyển chế độ bằng `Esc` cho NORMAL, `i/a/o` cho INSERT, `v` cho VISUAL, `V` cho VISUAL-LINE (v2.1.118+)

**Phím điều hướng**:
- `h` / `l` - Di chuyển trái/phải
- `j` / `k` - Di chuyển xuống/lên
- `w` / `b` / `e` - Di chuyển theo từ
- `0` / `$` - Di chuyển về đầu/cuối dòng
- `gg` / `G` - Nhảy tới đầu/cuối văn bản
- `%` - Nhảy tới dấu ngoặc tương ứng; kết hợp với `d`, `c`, `y` (v2.1.301)

**Đối tượng văn bản**:
- `iw` / `aw` - Bên trong/bao quanh từ
- `i"` / `a"` - Bên trong/bao quanh chuỗi trong dấu nháy
- `i(` / `a(` - Bên trong/bao quanh dấu ngoặc đơn

**Chế độ Visual (v2.1.118+)**:

| Phím | Chế độ | Hành vi |
|-----|------|----------|
| `v` | Visual | Chọn theo ký tự có phản hồi trực quan; mở rộng bằng các phím di chuyển |
| `V` | Visual-line | Chọn theo dòng; luôn chọn cả dòng |
| `y` | Yank | Sao chép vùng chọn visual hiện tại |
| `d` / `x` | Delete | Xóa vùng chọn visual hiện tại |
| `c` | Change | Xóa vùng chọn và vào chế độ INSERT |
| `Esc` | Exit | Quay về chế độ NORMAL |

Vùng chọn visual được tô sáng trong ô nhập để bạn thấy chính xác những gì sẽ được yank, xóa hoặc thay đổi trước khi thực hiện toán tử.

### Chế Độ Bash

Thực thi lệnh shell trực tiếp với tiền tố `!`:

```bash
! npm test
! git status
! cat src/index.js
```

Dùng cách này để thực thi lệnh nhanh mà không phải chuyển ngữ cảnh.

**Từ v2.1.193:** chế độ bash (`!`) có tự động hoàn thành đường dẫn file trực tiếp, nên đường dẫn được hoàn thành ngay khi bạn gõ lệnh shell mà không cần rời khỏi prompt.

**Từ v2.1.186:** đầu ra của lệnh `!` giờ được tự động gửi tới Claude, và Claude sẽ phản hồi. Để giữ hành vi cũ — đầu ra chỉ được thêm vào ngữ cảnh mà không có phản hồi — hãy đặt `"respondToBashCommands": false` trong `settings.json`.

---

## Kiểu Đầu Ra

Kiểu đầu ra (output style) thay đổi **cách** Claude phản hồi, không phải những gì nó biết. Chúng sửa đổi system prompt để đặt vai trò, giọng điệu và định dạng phản hồi mặc định. Hãy dùng khi bạn cứ phải prompt lại cùng một giọng văn mỗi lượt, hoặc khi bạn muốn Claude đóng một vai khác ngoài kỹ sư phần mềm.

Với các hướng dẫn về dự án hoặc codebase của bạn, hãy dùng [CLAUDE.md](../02-memory/) thay thế — đó là một cơ chế khác với những đánh đổi khác.

### Các kiểu có sẵn

| Kiểu | Hành vi |
|-------|----------|
| **Default** | System prompt tiêu chuẩn, được tinh chỉnh để hoàn thành các tác vụ kỹ thuật phần mềm hiệu quả |
| **Proactive** | Claude thực thi ngay và đưa ra giả định hợp lý thay vì dừng lại cho các quyết định thông thường. Hướng dẫn thực thi tự chủ mạnh hơn chế độ auto, nhưng **không** thay đổi chế độ quyền của bạn — bạn vẫn thấy các prompt xin quyền |
| **Explanatory** | Thêm các "Insights" mang tính giáo dục giữa các bước, giải thích lựa chọn triển khai và các mẫu trong codebase |
| **Learning** | Học qua thực hành theo kiểu cộng tác. Claude chia sẻ insight *và* để lại các đánh dấu `TODO(human)` để bạn tự triển khai những phần nhỏ, mang tính chiến lược |
| **Concise** (v2.1.237) | Claude đưa kết quả lên đầu và bỏ qua phần dẫn dắt và tường thuật. Mức độ kỹ lưỡng không đổi — chỉ phần khung bao quanh câu trả lời bị lược bỏ. Chọn nó trong `/config` → Output style, hoặc đặt `"outputStyle": "Concise"` |

### Chọn một kiểu

Chạy `/config` và chọn **Output style**, hoặc chạy `/output-style <style>` để chuyển trực tiếp — không có đối số thì nó liệt kê các kiểu có sẵn và đánh dấu kiểu hiện tại. Dù cách nào, lựa chọn đều được lưu vào `.claude/settings.local.json`. Để đặt mà không qua menu, hãy sửa trực tiếp cài đặt:

```json
{
  "outputStyle": "Explanatory"
}
```

> **Lưu ý**: Lệnh `/output-style` độc lập đã bị deprecate trong v2.1.73 và bị bỏ trong v2.1.91, nhưng nó đã **quay lại trong v2.1.269** và đang hoạt động trong v2.1.278. Nó hoạt động trong các phiên headless và Điều Khiển Từ Xa. `/config` và cài đặt `outputStyle` vẫn hoạt động.

Kiểu đầu ra là một phần của system prompt, vốn được Claude Code đọc một lần khi bắt đầu phiên — thay đổi có hiệu lực sau `/clear` hoặc trong phiên mới.

### Kiểu đầu ra tùy chỉnh

Một kiểu tùy chỉnh là một file Markdown có frontmatter, được lưu ở một trong ba cấp:

- User: `~/.claude/output-styles/`
- Project: `.claude/output-styles/`
- Chính sách được quản lý: `.claude/output-styles/` bên trong thư mục cài đặt được quản lý

Các kiểu cấp project được nạp từ mọi thư mục `.claude/output-styles/` nằm giữa thư mục làm việc và gốc repo. Từ v2.1.178, khi các thư mục lồng nhau định nghĩa cùng tên kiểu, kiểu gần thư mục làm việc nhất sẽ thắng.

```markdown
---
name: Diagrams first
description: Lead every explanation with a diagram
keep-coding-instructions: true
---

When explaining code, architecture, or data flow, start with a Mermaid diagram
showing the structure, then explain in prose.
```

| Frontmatter | Mục đích | Mặc định |
|-------------|---------|---------|
| `name` | Tên kiểu, nếu khác tên file | Kế thừa từ tên file |
| `description` | Hiển thị trong bộ chọn `/config` | Không có |
| `keep-coding-instructions` | Giữ các hướng dẫn kỹ thuật phần mềm có sẵn của Claude Code | `false` |
| `force-for-plugin` | Chỉ cho kiểu của plugin: tự động áp dụng mỗi khi plugin được bật, ghi đè `outputStyle` của người dùng | `false` |

**Đặt `keep-coding-instructions: true`** khi bạn thay đổi cách Claude giao tiếp nhưng vẫn muốn nó code theo cách cũ. Bỏ qua khi Claude hoàn toàn không làm kỹ thuật phần mềm — chẳng hạn một trợ lý viết lách hoặc nhà phân tích dữ liệu.

### Phạm vi và chi phí

Kiểu đầu ra chỉ áp dụng cho **cuộc hội thoại chính**. Một tác nhân con chạy system prompt riêng, nên kiểu đầu ra không thay đổi cách tác nhân con phản hồi; ngoại lệ là fork, vì nó kế thừa toàn bộ system prompt của tác nhân cha.

Thêm hướng dẫn làm tăng token đầu vào, dù prompt caching hấp thụ phần lớn sau yêu cầu đầu tiên. Explanatory và Learning theo thiết kế tạo ra phản hồi dài hơn, làm tăng token đầu ra.

### So sánh

| Tính năng | Cách hoạt động | Dùng khi |
|---------|--------------|-------------|
| Kiểu đầu ra | Sửa đổi system prompt | Bạn muốn vai trò, giọng điệu hoặc định dạng khác ở mọi lượt |
| [CLAUDE.md](../02-memory/) | Thêm một tin nhắn user sau system prompt | Claude cần luôn biết các quy ước dự án của bạn |
| `--append-system-prompt` | Nối thêm vào system prompt mà không bỏ gì | Bổ sung một lần cho một lần gọi |
| [Tác nhân con](../04-subagents/) | Chạy với system prompt, model và công cụ riêng | Bạn muốn một trợ thủ có phạm vi riêng biệt |
| [Skill](../03-skills/) | Nạp hướng dẫn riêng cho tác vụ khi được gọi | Bạn có một workflow tái sử dụng |

---

## Dòng Trạng Thái

Dòng trạng thái là một lệnh tùy chỉnh mà đầu ra của nó được hiển thị ở cuối phiên. Cấu hình nó bằng `/statusline`, hoặc đặt trực tiếp:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh",
    "padding": 0
  }
}
```

`padding` mặc định là `0`. Claude Code pipe một đối tượng JSON vào stdin của lệnh, nên script sẽ quyết định hiển thị gì.

### Các trường đầu vào có sẵn

| Nhóm | Trường |
|-------|--------|
| Phiên | `session_id`, `session_name`, `prompt_id`, `transcript_path`, `cwd`, `version` |
| Model | `model.id`, `output_style.name`, `effort.level`, `fast_mode`, `thinking.enabled` |
| Tác nhân | `agent.name`, `vim.mode` |
| Chi phí | `cost.total_cost_usd`, `cost.total_duration_ms`, `cost.total_api_duration_ms`, `cost.total_lines_added` |
| Ngữ cảnh | `context_window.context_window_size`, `.current_usage`, `.remaining_percentage`, `.total_input_tokens`, `.used_percentage` |
| Giới hạn | `rate_limits.five_hour.used_percentage`, `.resets_at` |
| Repo | `pr.number`, `pr.review_state`, `workspace.project_dir`, `workspace.added_dirs`, `workspace.git_worktree`, `workspace.repo.host` |
| Worktree | `worktree.name`, `.branch`, `.path`, `.original_branch`, `.original_cwd` |

### Ví dụ

```bash
#!/bin/bash
# ~/.claude/statusline.sh — model, mức dùng ngữ cảnh và chi phí
input=$(cat)
model=$(echo "$input" | jq -r '.model.id')
used=$(echo "$input" | jq -r '.context_window.used_percentage')
cost=$(echo "$input" | jq -r '.cost.total_cost_usd')
printf '%s | ctx %.0f%% | $%.2f' "$model" "$used" "$cost"
```

> **Lưu ý**: `statusLine` cần workspace được tin cậy. Script dòng trạng thái cũng nhận `COLUMNS` và `LINES` trong môi trường của chúng (v2.1.153+) để có thể điều chỉnh kích thước đầu ra theo terminal.

---

## Chế Độ TUI (Toàn Màn Hình)

> **Mới trong v2.1.110**

Chế độ TUI (Text User Interface) hiển thị Claude Code ở chế độ toàn màn hình với đầu ra không nhấp nháy — lý tưởng cho các terminal multiplexer như tmux hoặc các pane chia đôi của iTerm2.

### Bật Chế Độ TUI

Chuyển renderer bằng lệnh `/tui`, hoặc đặt `CLAUDE_CODE_NO_FLICKER=1` trước khi khởi chạy:

```bash
/tui fullscreen               # chuyển sang toàn màn hình từ bên trong phiên
/tui default                  # chuyển về renderer cổ điển
CLAUDE_CODE_NO_FLICKER=1 claude  # khởi động thẳng ở chế độ toàn màn hình
```

### Cấu Hình

| Cài đặt | Mô tả | Mặc định |
|---------|-------------|---------|
| `autoScrollEnabled` | Tự động cuộn tới tin nhắn mới nhất | `true` |

Tắt tự động cuộn qua `/config` hoặc `settings.json`:

```json
{
  "autoScrollEnabled": false
}
```

### Chế Độ Tập Trung

Lệnh `/focus` bật/tắt chế độ tập trung — một giao diện không xao nhãng chỉ hiển thị đầu ra liên quan nhất. `Ctrl+O` giờ chỉ chuyển đổi giữa transcript bình thường và chi tiết (chế độ tập trung là `/focus`).

---

## Nhập Liệu Bằng Giọng Nói

Nhập liệu bằng giọng nói cung cấp đầu vào giọng nói kiểu push-to-talk cho Claude Code, cho phép bạn nói prompt thay vì gõ.

### Kích Hoạt Nhập Liệu Bằng Giọng Nói

```
/voice
```

### Tính Năng

| Tính năng | Mô tả |
|---------|-------------|
| **Push-to-talk** | Giữ phím để ghi âm, thả ra để gửi |
| **20 ngôn ngữ** | Chuyển giọng nói thành văn bản hỗ trợ 20 ngôn ngữ |
| **Phím tắt tùy chỉnh** | Cấu hình phím push-to-talk qua `/keybindings` |
| **Yêu cầu tài khoản** | Cần tài khoản Claude.ai để xử lý STT |

### Cấu Hình

Tùy chỉnh phím push-to-talk trong file keybindings của bạn (`/keybindings`). Nhập liệu bằng giọng nói dùng tài khoản Claude.ai của bạn để xử lý chuyển giọng nói thành văn bản.

---

## Channels

Channels là một tính năng Research Preview, đẩy sự kiện từ các dịch vụ bên ngoài vào một phiên Claude Code đang chạy thông qua MCP server. Các nguồn bao gồm Telegram, Discord, iMessage và webhook bất kỳ, cho phép Claude phản ứng với thông báo theo thời gian thực mà không cần polling.

> **Xác thực (v2.1.128+)**: `--channels` giờ hoạt động với cả xác thực OAuth Pro/Max/Ultra **và** API key (console). Các bản phát hành trước yêu cầu OAuth.

### Đăng Ký Channels

```bash
# Đăng ký một channel plugin khi khởi động
claude --channels plugin:telegram@claude-plugins-official

# Đăng ký nhiều nguồn (phân tách bằng dấu cách)
claude --channels plugin:discord@claude-plugins-official plugin:telegram@claude-plugins-official
```

### Các Tích Hợp Được Hỗ Trợ

| Tích hợp | Mô tả |
|-------------|-------------|
| **Discord** | Nhận và trả lời tin nhắn Discord trong phiên của bạn |
| **Telegram** | Nhận và trả lời tin nhắn Telegram trong phiên của bạn |
| **iMessage** | Nhận thông báo iMessage trong phiên của bạn |
| **Webhooks** | Nhận sự kiện từ các nguồn webhook bất kỳ |

### Cấu Hình

Cấu hình channels bằng cờ `--channels` khi khởi động. Với các triển khai doanh nghiệp, dùng cài đặt được quản lý để kiểm soát những channel plugin nào được phép:

```json
{
  "channelsEnabled": true,
  "allowedChannelPlugins": [
    { "marketplace": "claude-plugins-official", "plugin": "discord" },
    { "marketplace": "claude-plugins-official", "plugin": "telegram" }
  ]
}
```

Cài đặt được quản lý `allowedChannelPlugins` kiểm soát những channel plugin nào được phép trong toàn tổ chức. Nó thay thế danh sách cho phép do Anthropic duy trì và cần `channelsEnabled: true`.

### Cách Hoạt Động

1. MCP server đóng vai trò channel plugin kết nối tới các dịch vụ bên ngoài
2. Tin nhắn và sự kiện đến được đẩy vào phiên Claude Code đang hoạt động
3. Claude có thể đọc và trả lời tin nhắn trong ngữ cảnh của phiên
4. Channel plugin phải nằm trong danh sách cho phép do Anthropic duy trì, hoặc trong danh sách `allowedChannelPlugins` của tổ chức bạn khi quản trị viên đặt nó
5. Không cần polling — sự kiện được đẩy theo thời gian thực

---

## Tích Hợp Chrome

Tích hợp Chrome kết nối Claude Code với trình duyệt Chrome hoặc Microsoft Edge của bạn để tự động hóa và gỡ lỗi web trực tiếp. Đây là tính năng beta có từ v2.0.73+ (cần extension Claude in Chrome v1.0.36+).

### Bật Tích Hợp Chrome

**Khi khởi động**:

```bash
claude --chrome      # Bật kết nối Chrome
claude --no-chrome   # Tắt kết nối Chrome
```

**Trong phiên**:

```
/chrome
```

Chọn "Enabled by default" để kích hoạt Tích hợp Chrome cho mọi phiên sau này. Claude Code dùng chung trạng thái đăng nhập của trình duyệt, nên có thể tương tác với các ứng dụng web đã xác thực.

> **Lưu ý**: Từ v2.1.290, file cài đặt của một project không thể bật tích hợp Chrome — hãy dùng `--chrome`, `/chrome` hoặc cài đặt user của bạn.

### Khả Năng

| Khả năng | Mô tả |
|------------|-------------|
| **Gỡ lỗi trực tiếp** | Đọc console log, kiểm tra phần tử DOM, gỡ lỗi JavaScript theo thời gian thực |
| **Kiểm chứng thiết kế** | So sánh trang được render với mockup thiết kế |
| **Kiểm tra form** | Kiểm thử việc gửi form, xác thực đầu vào và xử lý lỗi |
| **Kiểm thử ứng dụng web** | Tương tác với các ứng dụng đã xác thực (Gmail, Google Docs, Notion, v.v.) |
| **Trích xuất dữ liệu** | Thu thập và xử lý nội dung từ trang web |
| **Ghi lại phiên** | Ghi lại tương tác trình duyệt dưới dạng file GIF |

### Quyền theo từng site

Extension Chrome quản lý quyền truy cập theo từng site. Cấp hoặc thu hồi quyền truy cập cho các site cụ thể bất cứ lúc nào qua popup của extension. Claude Code chỉ tương tác với các site bạn đã cho phép rõ ràng.

### Cách hoạt động

Claude Code điều khiển trình duyệt trong một cửa sổ hiển thị — bạn có thể xem các hành động diễn ra theo thời gian thực. Khi trình duyệt gặp trang đăng nhập hoặc CAPTCHA, Claude tạm dừng và chờ bạn xử lý thủ công trước khi tiếp tục.

### Hạn chế đã biết

- **Hỗ trợ trình duyệt**: Chrome và Edge; Claude Code cũng kết nối được với các trình duyệt nhân Chromium khác như Brave, Arc, Vivaldi và Opera
- **WSL**: Không khả dụng trong Windows Subsystem for Linux
- **Nhà cung cấp bên thứ ba**: Không được hỗ trợ với các nhà cung cấp API Bedrock, Vertex hoặc Foundry
- **Service worker nhàn rỗi**: Service worker của extension Chrome có thể rơi vào trạng thái nhàn rỗi trong các phiên kéo dài

> **Mẹo**: Tích hợp Chrome là tính năng beta. Hỗ trợ trình duyệt có thể mở rộng trong các bản phát hành sau.

---

## Điều Khiển Từ Xa

Điều khiển từ xa cho phép bạn tiếp tục một phiên Claude Code đang chạy cục bộ từ điện thoại, máy tính bảng hoặc bất kỳ trình duyệt nào. Phiên cục bộ vẫn chạy trên máy của bạn — không có gì chuyển lên cloud. Có trên gói Pro, Max, Ultra, Team và Enterprise (v2.1.51+). Nếu vai trò tùy chỉnh Enterprise quản lý quyền truy cập của bạn, bạn cần một vai trò có cả quyền cloud sessions và quyền **Claude Code remote control**.

Điều khiển từ xa **không còn là research preview** — nhãn này đã bị bỏ vào tuần 34 năm 2026. Bất kỳ máy nào chạy `claude remote-control` giờ đều xuất hiện dưới dạng **thẻ thiết bị** trong tab Code của ứng dụng Claude, nên bạn có thể bắt đầu phiên trên máy đó trực tiếp từ điện thoại thay vì phải khởi động phiên trên máy trước rồi mới kết nối.

### Khởi Động Điều Khiển Từ Xa

**Từ CLI**:

```bash
# Khởi động với tên phiên mặc định
claude remote-control

# Khởi động với tên tùy chỉnh
claude remote-control --name "Auth Refactor"
```

**Từ bên trong phiên**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Các cờ có sẵn**:

| Cờ | Mô tả |
|------|-------------|
| `--name "title"` | Tiêu đề phiên tùy chỉnh để dễ nhận diện |
| `--verbose` | Hiển thị log kết nối chi tiết |

> **Lưu ý (v2.1.300)**: `claude remote-control` không còn chấp nhận `--sandbox` hay `--no-sandbox` (chúng chưa bao giờ có tác dụng; truyền một trong hai giờ sẽ thoát với lỗi). Để sandbox các phiên Điều khiển từ xa, hãy đặt `sandbox.enabled` trong file cài đặt.

### Kết nối tới một phiên

Ba cách kết nối từ thiết bị khác:

1. **URL phiên** — In ra terminal khi phiên bắt đầu; mở trong bất kỳ trình duyệt nào
2. **Mã QR** — Nhấn `spacebar` sau khi khởi động để hiển thị mã QR có thể quét
3. **Tìm theo tên** — Duyệt các phiên của bạn tại claude.ai/code hoặc trong ứng dụng di động Claude (iOS/Android)

### Bảo mật

- **Không mở cổng inbound** nào trên máy của bạn
- **Chỉ HTTPS outbound** qua TLS
- **Thông tin xác thực có phạm vi** — nhiều token ngắn hạn, phạm vi hẹp
- **Cô lập phiên** — mỗi phiên từ xa độc lập với nhau

### Điều khiển từ xa so với Claude Code trên web

| Khía cạnh | Điều khiển từ xa | Claude Code trên Web |
|--------|---------------|-------------------|
| **Thực thi** | Chạy trên máy của bạn | Chạy trên cloud của Anthropic |
| **Công cụ cục bộ** | Truy cập đầy đủ MCP server, file và CLI cục bộ | Không có dependencies cục bộ |
| **Trường hợp sử dụng** | Tiếp tục công việc cục bộ từ thiết bị khác | Bắt đầu mới từ bất kỳ trình duyệt nào |

### Hạn chế

- Một phiên từ xa cho mỗi tiến trình Claude Code tương tác — chế độ server (`claude remote-control`) phục vụ nhiều phiên cùng lúc (`--capacity`, mặc định 32)
- Terminal phải luôn mở trên máy host
- Nếu mạng không truy cập được, chế độ server thoát sau ~10 phút; phiên tương tác tiếp tục thử lại và kết nối lại khi mạng trở lại

### Trường hợp sử dụng

- Điều khiển Claude Code từ thiết bị di động hoặc máy tính bảng khi không ở bàn làm việc
- Dùng UI phong phú hơn của claude.ai trong khi vẫn thực thi công cụ cục bộ
- Review code nhanh khi đang di chuyển với toàn bộ môi trường phát triển cục bộ

### Thông Báo Đẩy (v2.1.110)

Khi Điều khiển từ xa đang hoạt động và "Push when Claude decides" được bật trong `/config`, Claude có thể gửi thông báo đẩy tới điện thoại của bạn — ví dụ khi một tác vụ dài hoàn thành hoặc cần đầu vào của bạn.

Để bật:
1. Kích hoạt Điều khiển từ xa: `/remote-control` hoặc `claude --rc`
2. Mở `/config` và bật **Push when Claude decides**

Thông báo đẩy cần gói đăng ký Claude và ứng dụng di động Claude.

### Tắt Điều Khiển Từ Xa (`disableRemoteControl`, v2.1.128+)

Quản trị viên trên gói Team hoặc Enterprise có thể chặn hoàn toàn Điều khiển từ xa bằng cài đặt `disableRemoteControl`. Khi là `true`, cả `claude remote-control` và `/remote-control` đều từ chối khởi động.

```json
{
  "disableRemoteControl": true
}
```

Cài đặt này được tôn trọng ở phạm vi **managed/policy** (ví dụ `/Library/Application Support/ClaudeCode/managed-settings.json` trên macOS) nên người dùng cá nhân không thể ghi đè. Hữu ích khi cần bắt buộc chỉ thực thi cục bộ trên toàn tổ chức.

> **Khi Điều khiển từ xa bị tự động tắt ở các tier API key (v2.1.139)**: Điều khiển từ xa bị **âm thầm tắt** bất cứ khi nào một trong các biến sau được đặt, kể cả khi bạn đồng thời đăng nhập bằng claude.ai:
>
> - `ANTHROPIC_API_KEY`
> - `ANTHROPIC_AUTH_TOKEN`
> - `apiKeyHelper` (settings.json)
>
> Cùng điều kiện đó cũng tắt [`/schedule`](#tác-vụ-theo-lịch), các connector MCP của claude.ai và tùy chọn thông báo — cả bốn bề mặt kết nối qua claude.ai đều yêu cầu đăng nhập OAuth là thông tin xác thực đang hoạt động. Bỏ đặt API key (hoặc chạy trên tier OAuth Pro/Max/Ultra) để dùng các tính năng này.

---

## Phiên Web

Phiên web cho phép bạn chạy Claude Code trực tiếp trên trình duyệt tại claude.ai/code, hoặc tạo phiên web từ CLI.

### Tạo Phiên Web

```bash
# Tạo phiên web mới từ CLI
claude --cloud "implement the new API endpoints"   # --remote là alias đã deprecate
```

Lệnh này khởi động một phiên Claude Code trên claude.ai mà bạn có thể truy cập từ bất kỳ trình duyệt nào.

### Tiếp Tục Phiên Web Ở Cục Bộ

Nếu bạn bắt đầu một phiên trên web và muốn tiếp tục nó ở cục bộ:

```bash
# Tiếp tục một phiên web trong terminal cục bộ — mở bộ chọn các phiên web của bạn
claude --teleport
```

Hoặc từ bên trong REPL tương tác:

```text
/teleport
```

`/tp` là alias của `/teleport`. Cả hai đều cần gói đăng ký claude.ai. Các phiên cloud
hiển thị gợi ý `/teleport` giải thích cách tiếp tục ở cục bộ (v2.1.223). Nếu phiên cloud đã được nén (compact), chỉ phần tóm tắt được chuyển sang — các tin nhắn trước đó mà nó tóm tắt không được sao chép vào terminal của bạn (Claude Code cảnh báo điều này từ v2.1.311).

> **Nguồn từ changelog**: changelog v2.1.223 cho thấy một dạng có đối số,
> `claude --teleport <session id>`, nhảy thẳng tới một phiên đã biết. Tài liệu tham chiếu
> CLI chỉ ghi dạng bộ chọn không đối số, nên hãy ưu tiên `claude --teleport` trừ khi
> bạn đã có sẵn ID phiên.

### Trường Hợp Sử Dụng

- Bắt đầu công việc trên một máy và tiếp tục trên máy khác
- Chia sẻ URL phiên với thành viên nhóm
- Dùng UI web để review diff trực quan, sau đó chuyển sang terminal để thực thi

---

## Ứng Dụng Desktop

Ứng dụng Claude Code Desktop cung cấp một ứng dụng độc lập với review diff trực quan, các phiên song song và connector tích hợp. Có trên macOS và Windows (gói Pro, Max, Ultra, Team và Enterprise).

### Cài Đặt

Tải về từ [claude.ai](https://claude.ai) cho nền tảng của bạn:
- **macOS**: Bản build Universal (Apple Silicon và Intel)
- **Windows**: Có trình cài đặt x64 và ARM64

Xem [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) để biết hướng dẫn thiết lập.

### Chuyển giao từ CLI

Chuyển phiên CLI hiện tại sang Ứng dụng Desktop:

```
/desktop
```

### Tính năng cốt lõi

| Tính năng | Mô tả |
|---------|-------------|
| **Giao diện diff** | Review trực quan từng file với bình luận inline; Claude đọc bình luận và chỉnh sửa |
| **Xem trước ứng dụng** | Tự khởi động dev server với trình duyệt nhúng để kiểm chứng trực tiếp |
| **Theo dõi PR** | **Auto-fix** để Claude sửa các CI check thất bại và bình luận review; **Merge when ready** bật auto-merge của GitHub (squash trong phiên cục bộ trừ khi branch gốc dùng merge queue). Cả hai nằm trong menu **⋮** của pull request trong thẻ **Changes** của phiên |
| **Phiên song song** | Nhiều phiên trong thanh bên; bật nút **Worktree** bên dưới ô prompt để cho một phiên Git worktree riêng (tắt theo mặc định) |
| **Tác vụ theo lịch** | Tác vụ lặp lại (hàng giờ, hàng ngày, ngày thường, hàng tuần) chạy khi ứng dụng đang mở |
| **Hiển thị phong phú** | Render code, markdown và sơ đồ với tô sáng cú pháp; checkbox danh sách tác vụ GitHub-Flavored-Markdown (`- [ ]` / `- [x]`) được render thành checkbox (v2.1.149+) |

### Cấu hình xem trước ứng dụng

Cấu hình hành vi dev server trong `.claude/launch.json`:

```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "my-app",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "port": 3000
    }
  ]
}
```

### Connector

Kết nối các dịch vụ bên ngoài để có ngữ cảnh phong phú hơn:

| Connector | Khả năng |
|-----------|------------|
| **GitHub** | Theo dõi PR, theo dõi issue, review code |
| **Slack** | Thông báo, ngữ cảnh channel |
| **Linear** | Theo dõi issue, quản lý sprint |
| **Notion** | Tài liệu, truy cập cơ sở tri thức |
| **Asana** | Quản lý tác vụ, theo dõi dự án |
| **Calendar** | Nắm lịch trình, ngữ cảnh cuộc họp |

> **Lưu ý**: Connector không khả dụng cho các phiên từ xa (cloud).

### Phiên từ xa và phiên SSH

- **Phiên từ xa**: Chạy trên hạ tầng cloud của Anthropic; tiếp tục chạy kể cả khi ứng dụng đã đóng. Truy cập được từ claude.ai/code hoặc ứng dụng di động Claude
- **Phiên SSH**: Kết nối tới máy từ xa qua SSH với toàn quyền truy cập hệ thống file và công cụ trên máy đó. Claude Code phải được cài trên máy từ xa

### Chế độ quyền trong Desktop

Ứng dụng Desktop hỗ trợ các chế độ quyền giống như CLI:

| Chế độ | Hành vi |
|------|----------|
| **Manual** (mặc định) | Review và phê duyệt mọi chỉnh sửa và lệnh |
| **Accept edits** | Chỉnh sửa file được tự động phê duyệt; lệnh cần phê duyệt thủ công |
| **Plan** | Review cách tiếp cận trước khi thực hiện bất kỳ thay đổi nào |
| **Auto** | Chạy mà không cần các prompt thông thường; bộ phân loại chạy nền kiểm tra hành động trước |
| **Bypass permissions** | Thực thi tự động (chỉ trong sandbox, do quản trị viên kiểm soát) |

### Tính năng doanh nghiệp

- **Admin console**: Kiểm soát quyền truy cập tab Code và cài đặt quyền cho tổ chức
- **Triển khai MDM**: Triển khai qua MDM trên macOS hoặc MSIX trên Windows
- **Tích hợp SSO**: Yêu cầu đăng nhập một lần (SSO) cho thành viên tổ chức
- **Cài đặt được quản lý**: Quản lý tập trung cấu hình nhóm và các model khả dụng

---

## Danh Sách Tác Vụ

Tính năng Danh sách tác vụ cung cấp khả năng theo dõi tác vụ bền vững, tồn tại qua các lần nén ngữ cảnh (khi lịch sử hội thoại bị cắt bớt để vừa cửa sổ ngữ cảnh).

### Bật/Tắt Danh Sách Tác Vụ

Nhấn `Ctrl+T` để bật hoặc tắt giao diện danh sách tác vụ trong phiên.

### Tác Vụ Bền Vững

Tác vụ được giữ lại qua các lần nén ngữ cảnh, đảm bảo các hạng mục công việc dài hạn không bị mất khi ngữ cảnh hội thoại bị cắt bớt. Điều này đặc biệt hữu ích cho các triển khai phức tạp, nhiều bước.

### Thư Mục Tác Vụ Có Tên

Dùng biến môi trường `CLAUDE_CODE_TASK_LIST_ID` để tạo các thư mục tác vụ có tên, dùng chung giữa các phiên:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

Điều này cho phép nhiều phiên dùng chung một danh sách tác vụ, hữu ích cho workflow nhóm hoặc các dự án nhiều phiên.

---

## Gợi Ý Prompt

Gợi ý prompt hiển thị các lệnh ví dụ màu xám dựa trên lịch sử git và ngữ cảnh hội thoại hiện tại của bạn.

### Cách Hoạt Động

- Gợi ý xuất hiện dưới dạng văn bản màu xám bên dưới ô nhập prompt
- Nhấn `Tab` để chấp nhận gợi ý
- Nhấn `Enter` để chấp nhận và gửi ngay
- Gợi ý nhận biết ngữ cảnh, dựa trên lịch sử git và trạng thái hội thoại

### Tắt Gợi Ý Prompt

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktree

Git worktree cho phép bạn khởi động Claude Code trong một worktree cô lập, giúp làm việc song song trên các branch khác nhau mà không cần stash hay chuyển branch.

### Khởi Động Trong Worktree

```bash
# Khởi động Claude Code trong một worktree cô lập
claude --worktree
# hoặc
claude -w
```

### Vị Trí Worktree

Worktree được tạo tại:
```
<repo>/.claude/worktrees/<name>
```

### Sparse Checkout Cho Monorepo

Dùng cài đặt `worktree.sparsePaths` để thực hiện sparse-checkout trong monorepo, giảm dung lượng đĩa và thời gian clone:

```json
{
  "worktree": {
    "sparsePaths": [".claude", "packages/my-package", "shared/"]
  }
}
```

Thêm `.claude` để mỗi worktree cũng nhận được `.claude/settings.json` và `.claude/rules/` của repository.

### Tham Chiếu Branch Gốc (`worktree.baseRef`)

**`worktree.baseRef`** (thêm trong v2.1.133) — kiểm soát việc `claude --worktree` tạo branch từ `origin/<default>` hay từ `HEAD` cục bộ.

- `"fresh"` (mặc định) — tạo branch từ `origin/<default-branch>`, bỏ qua các commit cục bộ chưa push. **Điều này đảo ngược hành vi được giới thiệu trong v2.1.128**, nên người dùng đã dựa vào việc tạo branch từ HEAD cục bộ sau v2.1.128 phải chọn bật lại.
- `"head"` — tạo branch từ `HEAD` cục bộ, giữ lại các commit chưa push.

Đặt trong `~/.claude/settings.json`:

```json
{ "worktree": { "baseRef": "head" } }
```

### Cô Lập Phiên Nền (`worktree.bgIsolation`)

**`worktree.bgIsolation`** (thêm trong v2.1.143) — kiểm soát việc các phiên nền (ví dụ từ `/bg`, `claude --bg` hoặc Agent View) có worktree riêng hay chỉnh sửa trực tiếp bản làm việc ở foreground.

- *(mặc định)* — phiên nền tạo một worktree cô lập trong `<repo>/.claude/worktrees/`, giống cách `--worktree` làm.
- `"none"` — phiên nền chỉnh sửa trực tiếp bản làm việc hiện tại. Dùng khi worktree không thực tế (ví dụ các artifact build native nặng) hoặc khi một tác nhân nền phải phối hợp chỉnh sửa với phiên foreground.

```json
{ "worktree": { "bgIsolation": "none" } }
```

Đánh đổi: `"none"` bỏ đi lớp bảo vệ của cô lập worktree — các chỉnh sửa đồng thời từ phiên nền và phiên foreground có thể gây merge conflict trong bản làm việc đang dùng.

### Công Cụ và Hook Của Worktree

| Mục | Mô tả |
|------|-------------|
| `EnterWorktree` | Công cụ để vào một worktree; từ v2.1.157 nó có thể chuyển giữa các worktree do Claude quản lý giữa chừng phiên |
| `ExitWorktree` | Công cụ để thoát và dọn dẹp worktree hiện tại |
| `WorktreeCreate` | Sự kiện hook được kích hoạt khi một worktree được tạo |
| `WorktreeRemove` | Sự kiện hook được kích hoạt khi một worktree bị xóa |

Từ v2.1.157, các worktree do Claude quản lý được để ở trạng thái không khóa khi tác nhân hoàn thành, nên `git worktree remove`/`prune` có thể dọn dẹp chúng.

### Tự Động Dọn Dẹp

Khi bạn thoát một phiên worktree tương tác và worktree không có thay đổi nào, Claude tự động xóa nó cùng branch của nó (phiên có tên sẽ hỏi trước). Nếu có thay đổi hoặc commit mới, hoặc một branch khác có commit mới đang được checkout trong đó (từ v2.1.304), Claude sẽ hỏi giữ hay xóa. Các lượt chạy `-p` không tương tác giữ nguyên worktree của chúng.

### Trường Hợp Sử Dụng

- Làm việc trên feature branch trong khi giữ nguyên branch main
- Chạy test cô lập mà không ảnh hưởng thư mục làm việc
- Thử các thay đổi thử nghiệm trong một môi trường dùng một lần
- Sparse-checkout các package cụ thể trong monorepo để khởi động nhanh hơn

---

## Sandboxing

Sandboxing cung cấp khả năng cô lập hệ thống file và mạng ở cấp hệ điều hành cho các lệnh Bash do Claude Code thực thi. Tính năng này bổ sung cho các rule quyền và cung cấp thêm một lớp bảo mật.

### Bật Sandboxing

**Lệnh slash** (lưu lựa chọn của bạn vào `.claude/settings.local.json` cho dự án này):
```text
/sandbox
```

**File cài đặt** (mọi dự án): đặt `"sandbox": { "enabled": true }` trong `~/.claude/settings.json`.

**Theo từng phiên**, không cần ghi file cài đặt:
```bash
claude --settings '{"sandbox": {"enabled": true}}'
```

> Không có cờ `claude --sandbox` / `--no-sandbox`. Từ v2.1.300, truyền chúng cho `claude remote-control` sẽ thoát với lỗi.

### Các Cài Đặt Cấu Hình

| Cài đặt | Mô tả |
|---------|-------------|
| `sandbox.enabled` | Bật hoặc tắt sandboxing |
| `sandbox.failIfUnavailable` | Báo lỗi nếu không thể kích hoạt sandboxing |
| `sandbox.filesystem.allowWrite` | Các đường dẫn được phép ghi |
| `sandbox.filesystem.allowRead` | Các đường dẫn được phép đọc |
| `sandbox.filesystem.denyRead` | Các đường dẫn bị từ chối đọc |
| `sandbox.network.allowedDomains` | Các domain mà tiến trình do Bash khởi chạy được phép truy cập (hỗ trợ wildcard `*.`) |
| `sandbox.network.deniedDomains` | Các domain bị chặn kể cả khi wildcard trong `allowedDomains` lẽ ra cho phép (v2.1.113+) |
| `sandbox.network.strictAllowlist` | (v2.1.219) Từ chối các host không nằm trong danh sách cho phép đối với lệnh trong sandbox mà không hỏi |
| `sandbox.enableWeakerNetworkIsolation` | Bật cô lập mạng yếu hơn trên macOS |
| `sandbox.bwrapPath` | (v2.1.133+, Linux/WSL) Đường dẫn tới binary `bubblewrap`. Mặc định: tìm trong `$PATH`. |
| `sandbox.socatPath` | (v2.1.133+, Linux/WSL) Đường dẫn tới binary `socat`. Mặc định: tìm trong `$PATH`. |
| `sandbox.credentials` | (v2.1.187+) Chặn các lệnh trong sandbox đọc file thông tin xác thực và biến môi trường bí mật. |
| `sandbox.allowAppleEvents` | (v2.1.181+, macOS) Chọn cho phép lệnh trong sandbox gửi Apple Events. |
| `sandbox.filesystem.disabled` | (v2.1.216+) Bỏ qua hoàn toàn cô lập hệ thống file trong khi vẫn thực thi cô lập mạng — hữu ích khi sandbox file làm hỏng công cụ nhưng kiểm soát lưu lượng mạng ra ngoài vẫn phải hoạt động. Chỉ được tôn trọng từ cài đặt user, cài đặt được quản lý hoặc `--settings`; cài đặt project không thể đặt nó. |
| `sandbox.excludedCommands` | Các mẫu lệnh theo cú pháp rule `Bash(...)`, như `"docker compose *"`, chạy bên ngoài sandbox và đi qua luồng quyền thông thường — nhưng chỉ khi các mục của bạn bao phủ mọi lệnh trong lời gọi Bash (chỉ một mục `docker compose *` vẫn để `npm ci && docker compose build` chạy trong sandbox), và một số dạng, như `sudo`, `cd`, chuyển hướng (redirection) hoặc heredoc, vẫn chạy trong sandbox ngay cả khi đó (v2.1.314 đã sửa mô tả của cài đặt này). Từ v2.1.309, khi sandbox được bật nhưng không thể chạy, chúng sẽ hỏi trước khi ghi vào các đường dẫn trong danh sách ghi của sandbox |
| `sandbox.allowNestedUserNamespaces` | (v2.1.305+, Linux/WSL2) Cho phép lệnh trong sandbox tạo user namespace (sandbox của Chromium/Electron, bubblewrap lồng nhau, `unshare`). Điều này tắt một ranh giới bảo mật; chỉ được tôn trọng từ cài đặt user hoặc cài đặt được quản lý hoặc `--settings`. Với Podman rootless, hãy dùng `excludedCommands` thay thế |

**Đường dẫn binary trên Linux/WSL** (v2.1.133+) — trỏ Claude Code tới các vị trí cài đặt không chuẩn:

```json
{
  "sandbox": {
    "bwrapPath": "/opt/bubblewrap/bin/bwrap",
    "socatPath": "/opt/socat/bin/socat"
  }
}
```

Ví dụ `deniedDomains` ghi đè một wildcard rộng (v2.1.113+):

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["*.example.com"],
      "deniedDomains": ["evil.example.com"]
    }
  }
}
```

Wildcard cho mọi thứ trên `example.com` đi qua, nhưng `deniedDomains` vẫn chặn host được chỉ định cụ thể.

> **Lưu ý** (v2.1.243): prompt xin quyền của công cụ Bash trong sandbox **không còn liệt kê các host mạng được phép**. Claude chỉ đơn giản thử gửi yêu cầu, và bạn phê duyệt từng host mới khi nó xuất hiện — nên đừng mong prompt hiển thị danh sách cho phép ngay từ đầu. Cùng bản phát hành này cũng không còn bỏ qua chi tiết vi phạm mạng khi lệnh bị chặn tình cờ thoát với mã `0`, nên một lần thành công trông có vẻ im lặng giờ vẫn báo cáo những gì đã bị chặn.

### Che Giấu Thông Tin Xác Thực (v2.1.221, v2.1.224)

> **Nguồn từ changelog**: các tùy chọn `sandbox.credentials` này lấy từ các mục changelog v2.1.221 và
> v2.1.224; tài liệu tham chiếu cài đặt chưa mô tả chi tiết chúng.

Trước v2.1.221, `sandbox.credentials` chỉ có thể `deny` một file thông tin xác thực — một lệnh
trong sandbox cần thông tin xác thực đó sẽ đơn giản là thất bại. `mode: "mask"` giữ cho lệnh hoạt động
mà không để lộ bí mật: tiến trình trong sandbox đọc một bản sao **sentinel** của file,
và proxy của sandbox thay thế giá trị thật trên đường đi ra mạng.

```json
{
  "sandbox": {
    "network": { "tlsTerminate": true },
    "credentials": {
      "files": [
        { "path": "~/.aws/credentials", "mode": "mask" }
      ]
    }
  }
}
```

| Khả năng | Từ phiên bản | Chức năng |
|---|---|---|
| `mode: "mask"` cho **file** thông tin xác thực | v2.1.221 | Lệnh trong sandbox đọc một sentinel; proxy thay giá trị thật vào khi đi ra ngoài. **Chỉ Linux và WSL** — trên macOS, việc che giấu file lùi về `deny`. |
| `extract` / `onExtractNoMatch` | v2.1.224 | Che giấu một trường bên trong giá trị biến môi trường có cấu trúc thay vì toàn bộ biến, và quyết định điều gì xảy ra khi mẫu không khớp. |
| `decode: "jwt"` với `maskClaims` | v2.1.224 | Giải mã một JWT và chỉ che giấu các claim được chỉ định, phần còn lại vẫn đọc được. |
| `awsPairs` / `sigv4` | v2.1.224 | Ký lại các yêu cầu AWS SigV4 tại proxy sau khi thay access key thật vào. |

**Hai ràng buộc dễ bị bỏ sót:**

- Mọi hình thức che giấu đều cần `network.tlsTerminate` — proxy phải nhìn được bên trong yêu cầu để
  thay giá trị.
- Các tùy chọn này **chỉ** được tôn trọng từ cài đặt user, cài đặt được quản lý hoặc `--settings`.
  Cài đặt project không thể bật che giấu hoặc thay đổi những gì được che giấu.

### Ví Dụ Cấu Hình

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    }
  }
}
```

### Cách Hoạt Động

- Lệnh Bash chạy trong môi trường sandbox với quyền truy cập hệ thống file bị hạn chế
- Truy cập mạng có thể được cô lập để ngăn các kết nối ra ngoài ngoài ý muốn
- Hoạt động cùng các rule quyền để phòng thủ nhiều lớp
- Trên macOS, Seatbelt chặn mọi kết nối mạng ngoại trừ kết nối tới proxy của sandbox; `sandbox.enableWeakerNetworkIsolation` **làm yếu** sự cô lập đó và chỉ dành cho các công cụ như Go CLI đứng sau proxy MITM `httpProxyPort`

### Trường Hợp Sử Dụng

- Chạy code không tin cậy hoặc code được sinh ra một cách an toàn
- Ngăn sửa đổi vô tình các file bên ngoài dự án
- Hạn chế truy cập mạng trong các tác vụ tự động

---

## Cài Đặt Được Quản Lý (Enterprise)

Cài đặt được quản lý cho phép quản trị viên doanh nghiệp triển khai cấu hình Claude Code trên toàn tổ chức bằng các công cụ quản lý gốc của nền tảng.

### Phương Thức Triển Khai

| Nền tảng | Phương thức | Từ phiên bản |
|----------|--------|-------|
| macOS | File plist được quản lý (MDM) | v2.1.51+ |
| Windows | Windows Registry | v2.1.51+ |
| Đa nền tảng | File cấu hình được quản lý | v2.1.51+ |
| Đa nền tảng | Drop-in được quản lý (thư mục `managed-settings.d/`) | v2.1.83+ |

### Drop-in Được Quản Lý

Từ v2.1.83, quản trị viên có thể triển khai nhiều file cài đặt được quản lý vào thư mục `managed-settings.d/`. Các file được gộp theo thứ tự bảng chữ cái, cho phép cấu hình theo module giữa các nhóm. Thư mục này nằm cạnh `managed-settings.json` trong thư mục hệ thống (`/Library/Application Support/ClaudeCode/` trên macOS, `/etc/claude-code/` trên Linux, `C:\Program Files\ClaudeCode\` trên Windows):

```
/etc/claude-code/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Các Cài Đặt Được Quản Lý Có Sẵn

| Cài đặt | Mô tả |
|---------|-------------|
| `permissions.disableBypassPermissionsMode` | Đặt thành `"disable"` để ngăn người dùng bật bypass permissions |
| `availableModels` | Giới hạn những model người dùng có thể chọn |
| `enforceAvailableModels` | (v2.1.175) Khi `true`, danh sách cho phép `availableModels` *cũng* ràng buộc model **Default** — nếu model mặc định được cấu hình không nằm trong danh sách, Claude Code lùi về model được phép đầu tiên. Cài đặt user và project không còn có thể mở rộng danh sách `availableModels` được quản lý. |
| `allowedChannelPlugins` | Kiểm soát những channel plugin nào được phép |
| `autoMode.environment` | Cấu hình hạ tầng tin cậy cho chế độ auto |
| `workflowSizeGuideline` | (v2.1.219) Đặt [hướng dẫn kích thước workflow động](#workflow-động) mang tính tư vấn. Đọc được từ mọi file cài đặt, không chỉ cài đặt được quản lý; khi một file đặt nó, dòng **Dynamic workflow size** bị ẩn khỏi `/config` |
| `wslInheritsWindowsSettings` | Chỉ Windows/WSL (v2.1.118+): khi `true`, Claude Code chạy trong WSL kế thừa cài đặt được quản lý từ host Windows, nên các chính sách doanh nghiệp triển khai qua Registry/MDM được áp dụng đồng nhất trên cả shell Windows và WSL |
| `parentSettingsBehavior` | (v2.1.133+, cấp quản trị) Kiểm soát cách `managedSettings` của SDK gộp với cài đặt của tiến trình cha. `"first-wins"` giữ thứ tự ưu tiên hiện có (cài đặt trước thắng khi xung đột); `"merge"` gộp sâu các giá trị. |
| Chính sách tùy chỉnh | Chính sách quyền và công cụ riêng của tổ chức |

### Ví Dụ: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>permissions</key>
  <dict>
    <key>disableBypassPermissionsMode</key>
    <string>disable</string>
  </dict>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Cấu Hình và Cài Đặt

### Vị Trí File Cấu Hình

1. **Cài đặt user**: `~/.claude/settings.json`
2. **Cài đặt project**: `.claude/settings.json` (được commit)
3. **Cài đặt project cục bộ**: `.claude/settings.local.json` (không commit)
4. **Cài đặt được quản lý**: `managed-settings.json` trong thư mục hệ thống (xem [Cài Đặt Được Quản Lý](#cài-đặt-được-quản-lý-enterprise))

### Ví Dụ Cấu Hình Đầy Đủ

**Cấu hình các tính năng nâng cao cốt lõi** (`.claude/settings.json`):

```json
{
  "permissions": {
    "defaultMode": "manual"
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "Edit", "hooks": [{ "type": "command", "command": "~/.claude/hooks/eslint-fix.sh" }] }
    ],
    "PostToolUse": [
      { "matcher": "Write", "hooks": [{ "type": "command", "command": "~/.claude/hooks/security-scan.sh" }] }
    ]
  }
}
```

Script hook nhận đầu vào của công cụ dưới dạng JSON qua stdin (ví dụ `tool_input.file_path`); không có phép thay thế `${file_path}`. MCP server không phải là một khóa cài đặt — hãy định nghĩa chúng trong `.mcp.json` ở gốc dự án:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}" }
    }
  }
}
```

**Ví dụ cấu hình mở rộng:**

```json
{
  "permissions": {
    "defaultMode": "manual",
    "allow": ["Bash(git log:*)", "Read"],
    "deny": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": [{ "type": "command", "command": "~/.claude/hooks/eslint-fix.sh" }] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": [{ "type": "command", "command": "~/.claude/hooks/security-scan.sh" }] }],
    "Stop": [{ "hooks": [{ "type": "command", "command": "~/.claude/hooks/notify.sh" }] }]
  }
}
```

MCP server GitHub cho thiết lập này được đặt trong `.mcp.json`, như ví dụ ở trên.

### Các Cài Đặt Bổ Sung Theo Người Dùng

Các khóa này đặt trong `~/.claude/settings.json` (hoặc `.claude/settings.json` của project) và kiểm soát hành vi tương tác cho từng người dùng:

| Cài đặt | Mô tả |
|---------|-------------|
| `askUserQuestionTimeout` | Tự động tiếp tục hộp thoại `AskUserQuestion` chưa được trả lời sau một khoảng thời gian nhàn rỗi. Từ **v2.1.200**, hộp thoại không còn tự động tiếp tục theo mặc định — đặt khóa này để chọn bật lại việc tự động tiếp tục theo thời gian. |
| `enableArtifact` | Bật/tắt công cụ Artifact theo từng người dùng (v2.1.196). |
| `crossSessionInbound` | (v2.1.224) Cách xử lý [tin nhắn giữa các phiên](#nhắn-tin-giữa-các-phiên) gửi đến — `"accept"`, `"hold"` hoặc `"refuse"`. Giá trị project và local chỉ áp dụng khi *nghiêm ngặt hơn* trên thang `accept < hold < refuse`. Hiển thị trong `/config` với tên "Messages from your other sessions" từ v2.1.232. |
| `dialogExpiry` | (v2.1.224) Thời gian một hộp thoại chưa được trả lời giữ mở. Mặc định `"5m"`; chấp nhận `"60s"`, `"5m"`, `"10m"` hoặc `"never"`. Bị ghi đè bởi `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS`. Hiển thị trong `/config` với tên "Dialog expiry" từ v2.1.232. |
| `modelPicker` | (v2.1.243) Chọn những model mà bộ chọn `/model` liệt kê, theo thứ tự và nhãn của riêng bạn. Một trong số ít cài đặt **thay thế thay vì gộp** giữa các lớp cài đặt — giá trị ở phạm vi gần nhất thắng hoàn toàn. |
| `promptCacheTtl` | (v2.1.243) Chọn thời gian sống của prompt cache cho cuộc hội thoại chính. |
| `subagentPromptCacheTtl` | (v2.1.243) Lựa chọn tương tự cho tác nhân con và các yêu cầu khác bên ngoài cuộc hội thoại chính. |
| `modelPricing` | (v2.1.243) **Cài đặt được quản lý.** Cung cấp mức giá theo hợp đồng của tổ chức bạn để `/cost`, dòng trạng thái và telemetry báo cáo theo đó thay vì giá niêm yết. |
| `keybindingFlavor` | **Deprecated từ v2.1.261 và không còn tác dụng.** Các phím chỉnh sửa từ trong prompt luôn theo quy ước readline, giống Bash: `Ctrl+W` xóa lùi tới khoảng trắng, `Alt+F` và `Alt+D` dừng ở cuối từ, và dấu câu phân tách các từ. Claude Code vẫn chấp nhận khóa này, nên file cài đặt có đặt nó vẫn hợp lệ. (Trong v2.1.238–v2.1.260, nó chọn giữa `"classic"` và `"readline"`.) |
| `spellcheck` | (v2.1.235) Gạch chân các từ sai chính tả trong ô nhập prompt bằng công cụ có trong `PATH` của bạn trong số `aspell`, `hunspell` hoặc `ispell`, thử theo thứ tự đó. Giá trị là object — `{"enabled": true, "language": "en_GB"}` — và tắt theo mặc định. **Chỉ đọc từ cài đặt user, cờ `--settings` và cài đặt được quản lý**: khối `spellcheck` trong `.claude/settings.json` hoặc `.claude/settings.local.json` của project bị bỏ qua. |
| `bashOutputMaxChars` | (v2.1.261) Số ký tự đầu ra của một lệnh Bash hoặc PowerShell **thành công** mà Claude nhận trực tiếp, tối đa 128K. Vượt quá giới hạn, Claude Code lưu đầu ra vào file và Claude nhận một bản xem trước ngắn kèm đường dẫn. Đặt khóa này khiến Claude Code bỏ qua `BASH_MAX_OUTPUT_LENGTH`. |
| `taskOutputMaxChars` | (v2.1.261) **Bị thay thế trong v2.1.278 và không còn tác dụng.** Trước đây nó giới hạn số ký tự đầu ra của **tác vụ nền** mà Claude nhận trực tiếp khi đọc bằng công cụ `TaskOutput`. v2.1.278 đã bỏ công cụ `TaskOutput` — giờ Claude đọc file đầu ra của tác vụ nền bằng `Read` — nên cả khóa này và `TASK_MAX_OUTPUT_LENGTH` đều không có tác dụng. Claude Code vẫn chấp nhận khóa này, nên file cài đặt có đặt nó vẫn hợp lệ. |
| `maxEffortLevel` | (v2.1.267) Giới hạn mức effort tối đa Claude Code được dùng, trên mọi nhà cung cấp kể cả Bedrock, Vertex và Foundry. Đặt ở cấp cao nhất hoặc theo từng model trong `modelSettings`. Người dùng vẫn có thể chọn mức thấp hơn. |
| `bashEditDiffEnabled` | (v2.1.269) Kết quả công cụ Bash bao gồm diff của các file mà lệnh đã thay đổi. |
| `syncClaudeAiSkills` / `syncClaudeAiPlugins` | (v2.1.275) Đặt một trong hai thành `false` để không đồng bộ các skill hoặc plugin bạn đã bật trên tài khoản claude.ai vào các phiên terminal. |

### Model Dự Phòng (`fallbackModel`)

Cài đặt `fallbackModel` cho phép bạn cấu hình **tối đa ba** model dự phòng, được thử lần lượt khi model chính bị quá tải hoặc không khả dụng.

```json
{
  "fallbackModel": ["claude-opus-4-8", "claude-sonnet-4-6", "claude-haiku-4-5"]
}
```

Từ **v2.1.166**, cờ `--fallback-model` cũng áp dụng cho các phiên tương tác (không chỉ headless). Khi dự phòng, Claude Code thử lại một lần với lỗi không mong đợi thuộc loại không thử lại được; các lỗi xác thực, giới hạn tốc độ, kích thước yêu cầu và lỗi truyền tải vẫn thất bại ngay.

### Biến Môi Trường

Ghi đè cấu hình bằng biến môi trường:

```bash
# Chọn model
export ANTHROPIC_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_MODEL=claude-opus-4-8   # (v2.1.236) Model mà phiên mới khởi động với. Khác với ANTHROPIC_MODEL, lựa chọn qua /model vẫn ghi đè nó — và lựa chọn đó được giữ qua các lần khởi động lại
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-8
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# Cấu hình API
export ANTHROPIC_API_KEY=sk-ant-...

# Cấu hình tư duy
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high   # low, medium, high, xhigh (Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8/4.7), hoặc max — mặc định là high trên Opus 5 và Opus 4.8 (hỗ trợ trên Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6)

# Bật/tắt tính năng
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1    # Tắt bộ nhớ tự động (không tạo hay nạp file bộ nhớ tự động nào)
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=0          # Công cụ Task là mặc định; 0 quay về công cụ TodoWrite cũ
export CLAUDE_CODE_SIMPLE=true              # Được đặt bởi cờ --bare

# Cấu hình MCP
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Prompt caching
export ENABLE_PROMPT_CACHING_1H=1      # Yêu cầu cache TTL 1 giờ cho mọi yêu cầu (mặc định: 1 giờ cho cuộc hội thoại chính khi dùng gói đăng ký, 5 phút với API key / nhà cung cấp cloud)

# Quản lý tác vụ
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Nhóm tác nhân (thử nghiệm)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Cấu hình tác nhân con và plugin
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Tiến trình con và streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000

# Đầu ra và trình quản lý package (v2.1.129+)
export CLAUDE_CODE_FORCE_SYNC_OUTPUT=1                      # Buộc đầu ra đồng bộ cho các terminal mà tự động phát hiện bỏ sót (Emacs eat, v.v.)
export CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1            # Bật nâng cấp nền cho bản cài qua Homebrew/WinGet
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1         # Chọn bật khám phá gateway /v1/models khi ANTHROPIC_BASE_URL được đặt

# Công cụ Windows PowerShell (v2.1.143+) — bật mặc định cho Bedrock/Vertex/Foundry trên Windows
export CLAUDE_CODE_USE_POWERSHELL_TOOL=0                    # Tắt hoàn toàn công cụ PowerShell
export CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1    # Tôn trọng ExecutionPolicy của hệ thống thay vì `-ExecutionPolicy Bypass`

# Workload identity federation (v2.1.141+)
export ANTHROPIC_WORKSPACE_ID=ws_abc123                     # Giới hạn token liên kết vào một workspace cụ thể khi rule bao phủ nhiều workspace

# Giới hạn an toàn cho Stop hook (v2.1.143+)
export CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=8                    # Số lần chặn liên tiếp tối đa của Stop hook trước khi phiên kết thúc kèm cảnh báo. Đặt 0 để tắt giới hạn.

# Giới hạn sinh lời gọi trên toàn phiên (v2.1.212)
export CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION=200         # Giới hạn số lời gọi công cụ WebSearch mỗi phiên, để chặn vòng lặp tìm kiếm mất kiểm soát. Mặc định 200.
export CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR=100       # (v2.1.290) Tốc độ nạp lại ngân sách đó, tính theo lời gọi/giờ. Mặc định 100 khi tương tác, 0 (không nạp lại) với -p.

# Trợ năng (v2.1.208)
export CLAUDE_AX_SCREEN_READER=1                            # Bật chế độ hiển thị văn bản thuần cho trình đọc màn hình. Tác dụng giống --ax-screen-reader hoặc "axScreenReader": true trong cài đặt user hoặc cài đặt được quản lý (bị bỏ qua trong cài đặt project/local từ v2.1.305).

# Các biến mới hơn (v2.1.221–v2.1.234) — lấy từ changelog; tài liệu tham chiếu CLI không có mục biến môi trường
export CLAUDE_CODE_ENABLE_TODO_TOOLS=1                      # (v2.1.233) Khôi phục các công cụ todo/theo dõi tác vụ (TaskCreate/Get/Update/List, TodoWrite), vốn chỉ có mặc định trên các model Claude 3.x, Opus 4 đến 4.7, Sonnet 4 đến 4.6 và Haiku 4.5 (v2.1.268)
export CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS=900000             # (v2.1.233) TTL của cache URL cho WebFetch. Mặc định 15 phút.
export CLAUDE_CODE_TOOL_MEMORY_LIMIT=2G                     # (v2.1.233, Linux) Chọn bật memory cgroup áp dụng cho các lệnh Bash
export ANTHROPIC_BEDROCK_REGION_PREFIX=us                   # (v2.1.224) Ưu tiên một inference profile liên vùng cụ thể của Bedrock
export CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1  # (v2.1.223) Khôi phục hành vi auto-compact trước v2.1.223 với các ID model không được nhận diện
export CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0             # (v2.1.229) Tắt việc giãn cách prefix khi fan-out workflow động
export CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS=300000            # (v2.1.224) Ghi đè cài đặt dialogExpiry
export CLAUDE_CODE_PROJECT_DIR_NAME=my-app                  # (v2.1.234) Tên ngắn cho thư mục transcript theo dự án, dành cho các host cấp cho mỗi phiên một thư mục cấu hình riêng
export CLAUDE_CODE_GOAL_CHECKIN_MINUTES=30                  # (v2.1.234) Số phút một tác vụ nền có thể đứng yên trước khi Claude kiểm tra lại khi /goal đang hoạt động. Đặt 0 để tắt việc kiểm tra.

# Các biến mới hơn (v2.1.268-v2.1.278) - lấy từ changelog
export CLAUDE_CODE_MCP_STARTUP_WAIT_MS=5000                 # (v2.1.274) Thời gian lượt không tương tác đầu tiên chờ các MCP server vẫn đang kết nối. 0 = không chờ, trừ các server được nêu tên bởi --allowedTools hoặc một hook mcp_tool (vẫn tối đa 2 giây, v2.1.284+).
export CLAUDE_CODE_WEBFETCH_DEADLINE_MS=300000              # (v2.1.268) Ghi đè thời hạn 300 giây mới của WebFetch. 0 tắt thời hạn.
export CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS=32        # (v2.1.269) Nâng giới hạn số tác nhân đồng thời mỗi lượt chạy của công cụ Workflow. Chấp nhận 1-256.
export CLAUDE_CODE_AUTO_MODE_SERVER=0                       # (v2.1.278; Anthropic API trực tiếp từ v2.1.281) Không dùng review của bộ phân loại chế độ auto phía server

# Các biến mới hơn (v2.1.299-v2.1.300)
export CLAUDE_CODE_DISABLE_FILE_MENTIONS=1                  # (v2.1.299) Không mở rộng các mention file/thư mục bằng @; Claude nhận đường dẫn và đọc chúng bằng công cụ file. Bị bỏ qua trong cài đặt project/local.
export CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS=200000           # (v2.1.299, cần v2.1.290+) Kích thước ngữ cảnh mà tại đó nén khi nhàn rỗi được áp dụng. Mặc định 200000, tối thiểu 100000. "idleCompaction": false để tắt.
export CLAUDE_CODE_GZIP_REQUEST_BODIES=0                    # (v2.1.300) Tắt nén gzip các body yêu cầu lớn gửi tới api.anthropic.com (dùng nếu proxy kiểm tra TLS xử lý sai chúng).
export CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS=0                 # (v2.1.300) Chỉnh sửa file artifact bằng công cụ file, rồi publish như một bước riêng, thay vì chỉnh sửa ngay trong lúc publish.

# Các biến mới hơn (v2.1.301-v2.1.302)
export CLAUDE_CODE_AUTO_MODE_MODEL=claude-sonnet-4-6  # model của bộ phân loại chế độ auto phía client (v2.1.302); bị bỏ qua với Opus 5, Sonnet 5.5, Opus 5.5 hoặc model bị chính sách của bạn loại trừ
export CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS=3600000  # ngừng chờ các lần đặt lại giới hạn sử dụng còn xa (v2.1.301)

# Các biến mới hơn (v2.1.304-v2.1.310) — đặt trong shell khởi chạy
export CLAUDE_CODE_AUTO_COMPACT_WINDOW=200k                 # (v2.1.304) Cửa sổ auto-compact, 100000-1000000 token; hậu tố k/M cần v2.1.304+, số thuần được hiểu là token
export CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1        # (v2.1.304) Tắt prompt rm đệ quy cho các ổ đĩa được mount như /Volumes/USB hoặc /mnt/c; bị bỏ qua trong khối env của cài đặt
export CLAUDE_CODE_WARN_DISK_FREE_GIB=10                    # (v2.1.304) Cảnh báo Claude khi dung lượng trống trên hệ thống file của thư mục làm việc giảm dưới N GiB
export CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1            # (v2.1.304) Bắt Claude chờ kết quả của tác vụ MCP trong phiên tương tác
export CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS=600000  # (v2.1.305) Khi có CLAUDE_CODE_RETRY_WATCHDOG, kiểm tra lại giới hạn sử dụng theo chu kỳ này (60000-10800000 ms) để tiếp tục sớm khi giới hạn được gỡ
export CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK=1        # (v2.1.309) Cho phép `claude ultrareview` chạy trong thư mục chưa tin cậy mà nó không thể hỏi (CI); chỉ dùng khi bạn tin tưởng bản checkout
```

> **v2.1.223 — `CLAUDE_CODE_DISABLE_1M_CONTEXT` được mở rộng**: biến này giờ giữ **mọi**
> model Claude có cửa sổ gốc 1M token ở mức 200K thông qua auto-compaction, thay vì
> chỉ một danh sách ID model cố định.

> **v2.1.108**: `ENABLE_PROMPT_CACHING_1H=1` — yêu cầu TTL prompt cache 1 giờ cho cuộc hội thoại chính và các yêu cầu khác. Nếu không có nó, cuộc hội thoại chính nhận 1 giờ khi dùng gói đăng ký Claude trong hạn mức gói và 5 phút khi dùng API key, usage credits hoặc nhà cung cấp cloud; `FORCE_PROMPT_CACHING_5M=1` buộc dùng 5 phút. (v2.1.129 sửa một lỗi hồi quy khiến TTL 1 giờ bị âm thầm hạ xuống 5 phút.)

> **v2.1.129**: `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` buộc đầu ra đồng bộ cho các terminal mà việc tự động phát hiện khả năng thất bại (ví dụ Emacs `eat`). `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE=1` bật nâng cấp nền cho bản cài qua Homebrew/WinGet, vốn nếu không sẽ không bao giờ tự cập nhật.

### Lệnh Quản Lý Cấu Hình

```
User: /config
[Opens interactive configuration menu]
```

Lệnh `/config` cung cấp menu tương tác để bật/tắt các cài đặt như:
- Bật/tắt tư duy mở rộng
- Đầu ra chi tiết
- Chế độ quyền
- Chọn model
- Kích thước workflow động (v2.1.219) — bị ẩn khi `workflowSizeGuideline` được đặt trong file cài đặt, xem [Workflow Động](#workflow-động)
- Nén khi nhàn rỗi (v2.1.302)

Trong menu tương tác, nhấn Enter hoặc Space để thay đổi cài đặt đang chọn, và Esc để lưu và đóng (v2.1.183+).

Bạn cũng có thể đặt một cài đặt trực tiếp từ prompt mà không cần mở menu:

```bash
/config thinking=false      # đặt một cài đặt ngay trên dòng (v2.1.181+)
/config --help              # liệt kê các khóa viết tắt có sẵn (v2.1.183+)
```

Cú pháp viết tắt `key=value` hoạt động trong phiên tương tác, với `-p` và trong Điều Khiển Từ Xa.

### Cấu Hình Theo Dự Án

Tạo `.claude/settings.json` trong dự án của bạn:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": [{ "type": "command", "command": "npm test && npm run lint" }] }]
  },
  "permissions": {
    "defaultMode": "manual"
  }
}
```

Đặt các MCP server của dự án trong `.mcp.json` ở gốc dự án:

```json
{
  "mcpServers": {
    "project-db": {
      "command": "mcp-postgres",
      "env": {
        "DATABASE_URL": "${PROJECT_DB_URL}"
      }
    }
  }
}
```

Dùng một user cơ sở dữ liệu chỉ đọc cho `PROJECT_DB_URL`; xem phần thiết lập chỉ đọc trong [MCP → Ví dụ cơ sở dữ liệu](../05-mcp/README.md).

---

## Tin Cậy và Phạm Vi Quyền

> **Nguồn từ changelog (v2.1.222, v2.1.232)**: những thắt chặt này lấy từ changelog;
> tài liệu tham chiếu cài đặt chưa mô tả rõ chúng.

Một chủ đề lặp lại trong các bản phát hành gần đây: các cài đặt liên quan đến bảo mật không còn có thể bị mở rộng
bởi một repository bạn đã clone. Có ba thay đổi cần biết.

**Repository lồng nhau cần xác nhận tin cậy riêng (v2.1.232).** Một git repository
bên trong thư mục cha đã được tin cậy không còn kế thừa sự tin cậy đó. Nếu bạn tin cậy
`~/work/monorepo` và nó chứa một submodule vendored, bạn sẽ được yêu cầu tin cậy
submodule đó riêng vào lần đầu Claude Code làm việc bên trong nó.

**`sandbox.ripgrep` chỉ ở phạm vi user (v2.1.232).** Cài đặt chỉ định binary ripgrep
mà sandbox dùng chỉ được tôn trọng từ cài đặt user, cài đặt được quản lý hoặc
`--settings`. Cài đặt project không còn có thể trỏ sandbox tới một binary khác.

**Tự khởi động Điều Khiển Từ Xa chỉ ở phạm vi user (v2.1.222).** Cài đặt cục bộ trong repo không thể
bật tự khởi động Điều Khiển Từ Xa; nó chỉ có thể được bật ở phạm vi user qua `/config`.

Quy luật cần ghi nhớ: nếu một cài đặt cho phép một file được commit mở rộng những gì Claude
Code được phép làm trên máy của bạn, hãy giả định rằng giờ nó chỉ ở phạm vi user.

---

## Nhóm Tác Nhân

Nhóm tác nhân (Agent Teams) là một tính năng thử nghiệm cho phép nhiều phiên bản Claude Code cộng tác trong một tác vụ. Tính năng này bị tắt theo mặc định.

### Bật Nhóm Tác Nhân

Bật qua biến môi trường hoặc cài đặt:

```bash
# Biến môi trường
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

Hoặc thêm vào JSON cài đặt của bạn:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Cách Nhóm Tác Nhân Hoạt Động

- Một **trưởng nhóm** điều phối toàn bộ tác vụ và giao các tác vụ con cho đồng đội
- Các **đồng đội** làm việc độc lập, mỗi người có cửa sổ ngữ cảnh riêng
- Một **danh sách tác vụ dùng chung** cho phép các thành viên tự phối hợp với nhau
- Dùng định nghĩa tác nhân con (`.claude/agents/` hoặc cờ `--agents`) để định nghĩa vai trò và chuyên môn của đồng đội

### Chế Độ Hiển Thị

Nhóm tác nhân hỗ trợ hai chế độ hiển thị, cấu hình bằng cờ `--teammate-mode`:

| Chế độ | Mô tả |
|------|-------------|
| `in-process` (mặc định) | Các đồng đội chạy trong cùng tiến trình terminal |
| `tmux` | Mỗi đồng đội có một pane chia riêng (cần tmux hoặc iTerm2) |
| `auto` | Tự động chọn chế độ hiển thị tốt nhất |

```bash
# Dùng pane chia của tmux để hiển thị đồng đội
claude --teammate-mode tmux

# Dùng tường minh chế độ in-process
claude --teammate-mode in-process
```

### Trường Hợp Sử Dụng

- Các tác vụ refactor lớn mà mỗi đồng đội xử lý một module khác nhau
- Review code và triển khai song song
- Các thay đổi nhiều file được phối hợp trên toàn codebase

> **Lưu ý**: Nhóm tác nhân là tính năng thử nghiệm và có thể thay đổi trong các bản phát hành sau. Xem [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) để có tài liệu tham chiếu đầy đủ.

---

## Thực Hành Tốt Nhất

### Chế Độ Lập Kế Hoạch
- ✅ Dùng cho các tác vụ phức tạp nhiều bước
- ✅ Review kế hoạch trước khi phê duyệt
- ✅ Chỉnh sửa kế hoạch khi cần
- ❌ Không dùng cho tác vụ đơn giản

### Tư Duy Mở Rộng
- ✅ Dùng cho các quyết định kiến trúc
- ✅ Dùng để giải quyết vấn đề phức tạp
- ✅ Review quá trình suy nghĩ
- ❌ Không dùng cho truy vấn đơn giản

### Tác Vụ Nền
- ✅ Dùng cho các thao tác chạy lâu
- ✅ Theo dõi tiến độ tác vụ
- ✅ Xử lý lỗi tác vụ một cách êm thấm
- ❌ Không khởi chạy quá nhiều tác vụ đồng thời

### Quyền
- ✅ Dùng `plan` để review code (chỉ đọc)
- ✅ Dùng `default` cho phát triển tương tác
- ✅ Dùng `acceptEdits` cho workflow tự động hóa
- ✅ Dùng `auto` cho công việc tự chủ có rào chắn an toàn
- ❌ Không dùng `bypassPermissions` trừ khi thực sự cần thiết

### Phiên
- ✅ Dùng các phiên riêng cho các tác vụ khác nhau
- ✅ Lưu các trạng thái phiên quan trọng
- ✅ Dọn dẹp các phiên cũ
- ❌ Không trộn công việc không liên quan trong một phiên

---

## Tài Nguyên Bổ Sung

Để biết thêm thông tin về Claude Code và các tính năng liên quan:

- [Tài liệu chính thức về Interactive Mode](https://code.claude.com/docs/en/interactive-mode)
- [Tài liệu chính thức về Headless Mode](https://code.claude.com/docs/en/headless)
- [Tham chiếu CLI](https://code.claude.com/docs/en/cli-reference)
- [Hướng dẫn Checkpoint](../08-checkpoints/) - Quản lý phiên và tua lại
- [Lệnh Slash](../01-slash-commands/) - Tham chiếu lệnh
- [Hướng dẫn Bộ nhớ](../02-memory/) - Ngữ cảnh bền vững
- [Hướng dẫn Skill](../03-skills/) - Khả năng tự chủ
- [Hướng dẫn Tác nhân con](../04-subagents/) - Thực thi tác vụ được ủy thác
- [Hướng dẫn MCP](../05-mcp/) - Truy cập dữ liệu bên ngoài
- [Hướng dẫn Hook](../06-hooks/) - Tự động hóa hướng sự kiện
- [Hướng dẫn Plugin](../07-plugins/) - Tiện ích mở rộng đóng gói
- [Tài liệu chính thức về Scheduled Tasks](https://code.claude.com/docs/en/scheduled-tasks)
- [Tài liệu chính thức về Chrome Integration](https://code.claude.com/docs/en/chrome)
- [Tài liệu chính thức về Remote Control](https://code.claude.com/docs/en/remote-control)
- [Tài liệu chính thức về Keybindings](https://code.claude.com/docs/en/keybindings)
- [Tài liệu chính thức về Desktop App](https://code.claude.com/docs/en/desktop)
- [Tài liệu chính thức về Agent Teams](https://code.claude.com/docs/en/agent-teams)

---

**Cập Nhật Lần Cuối**: Ngày 12 tháng 11 năm 2026
**Phiên Bản Claude Code**: 2.1.322
**Nguồn**:
- https://code.claude.com/docs/en/permission-modes#turn-off-the-critical-path-removal-prompt-in-bypasspermissions-mode
- https://github.com/anthropics/claude-code/releases/tag/v2.1.314
- https://code.claude.com/docs/en/desktop#run-a-session-in-its-own-worktree
- https://code.claude.com/docs/en/settings-reference#worktree-sparsepaths
- https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning
- https://code.claude.com/docs/en/feature-availability#ultra-plan
- https://code.claude.com/docs/en/changelog#2-1-312
- https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules
- https://code.claude.com/docs/en/changelog#2-1-314
- https://code.claude.com/docs/en/changelog#2-1-316
- https://code.claude.com/docs/en/claude-code-on-the-web#continue-a-cloud-session-in-your-terminal
- https://code.claude.com/docs/en/output-styles
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/auto-mode-classifier-billing
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/sandboxing
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/settings.md
- https://code.claude.com/docs/en/settings-reference
- https://code.claude.com/docs/en/whats-new/2026-w34
- https://code.claude.com/docs/en/model-config#adjust-effort-level
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/keybindings#modifiers
- https://code.claude.com/docs/en/model-config#extended-thinking
- https://github.com/anthropics/claude-code/releases/tag/v2.1.281
- https://github.com/anthropics/claude-code/releases/tag/v2.1.283
- https://code.claude.com/docs/en/permission-modes#critical-paths
- https://code.claude.com/docs/en/settings-reference#ultracode
- https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in
- https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode
- https://github.com/anthropics/claude-code/releases/tag/v2.1.284
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://code.claude.com/docs/en/tools-reference
- https://code.claude.com/docs/en/chrome
- https://github.com/anthropics/claude-code/releases/tag/v2.1.288
- https://github.com/anthropics/claude-code/releases/tag/v2.1.290
- https://github.com/anthropics/claude-code/releases/tag/v2.1.293
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/changelog#2-1-299
- https://code.claude.com/docs/en/changelog#2-1-300
- https://code.claude.com/docs/en/settings-reference#sandbox-enabled
- https://code.claude.com/docs/en/prompt-caching
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/monitoring-usage
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/channels
- https://code.claude.com/docs/en/desktop
- https://code.claude.com/docs/en/fullscreen
- https://code.claude.com/docs/en/changelog#2-1-301
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/permission-modes#which-mode-a-non-interactive-run-starts-in
- https://code.claude.com/docs/en/permission-modes#choose-the-classifier-model
- https://code.claude.com/docs/en/changelog#2-1-309
- https://code.claude.com/docs/en/permission-modes#critical-path-removals-in-each-permission-mode
- https://code.claude.com/docs/en/permission-modes#the-mounted-drive-prompt
- https://code.claude.com/docs/en/permission-modes#time-limits-and-denials-in-auto-and-bypasspermissions-modes
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/settings-reference#axscreenreader
- https://code.claude.com/docs/en/routines#where-the-name-routines-still-appears
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/desktop#monitor-pull-request-status
- https://code.claude.com/docs/en/changelog#2-1-281
- https://code.claude.com/docs/en/mcp#example-query-your-postgresql-database
- https://code.claude.com/docs/en/routines#permission-prompts-during-a-run
- https://code.claude.com/docs/en/changelog#2-1-310
- https://code.claude.com/docs/en/tools-reference#monitor-tool
- https://code.claude.com/docs/en/monitoring-usage#safety-event
- https://code.claude.com/docs/en/monitoring-usage#standard-attributes
- https://code.claude.com/docs/en/monitoring-usage#tool-decision-event
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/sessions#the-resume-this-conversation-dialog
- https://code.claude.com/docs/en/worktrees#clean-up-worktrees
- https://code.claude.com/docs/en/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands
- https://code.claude.com/docs/en/settings-reference#sandbox-allownestedusernamespaces
- https://code.claude.com/docs/en/env-vars#variables
- https://code.claude.com/docs/en/model-config#values-and-warnings-for-claude_code_auto_compact_window
- https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries-with-auto-mode-setup
- https://code.claude.com/docs/en/remote-control#requirements
- https://code.claude.com/docs/en/cli-reference#cli-flags
- https://code.claude.com/docs/en/scheduled-tasks#seven-day-expiry
- https://code.claude.com/docs/en/scheduled-tasks#jitter
- https://code.claude.com/docs/en/scheduled-tasks#limitations
- https://code.claude.com/docs/en/model-config#subagents-switch-or-fail-without-asking
- https://code.claude.com/docs/en/changelog#2-1-318
- https://code.claude.com/docs/en/tools-reference#time-limit-for-background-commands
- https://code.claude.com/docs/en/changelog#2-1-321
**Các Mô Hình Tương Thích**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
