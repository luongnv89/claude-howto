<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints và Rewind

Checkpoints (điểm lưu trạng thái) cho phép bạn lưu lại trạng thái cuộc hội thoại và quay ngược về các thời điểm trước trong phiên Claude Code. Tính năng này cực kỳ hữu ích khi bạn muốn thử nhiều hướng tiếp cận khác nhau, phục hồi sau khi mắc lỗi, hoặc so sánh các giải pháp khác nhau.

## Tổng quan

Checkpoints cho phép lưu trạng thái cuộc hội thoại và quay lại các thời điểm trước, giúp bạn thử nghiệm an toàn và khám phá nhiều hướng tiếp cận. Mỗi checkpoint là một "ảnh chụp" trạng thái hội thoại, bao gồm:
- Toàn bộ tin nhắn đã trao đổi
- Các thay đổi file đã thực hiện
- Lịch sử sử dụng công cụ
- Ngữ cảnh phiên làm việc

Checkpoints đặc biệt hữu ích khi thử nhiều hướng tiếp cận, phục hồi sau lỗi, hoặc so sánh các giải pháp khác nhau.

## Các khái niệm chính

| Khái niệm | Mô tả |
|-----------|-------|
| **Checkpoint** | Ảnh chụp trạng thái hội thoại, bao gồm tin nhắn, file và ngữ cảnh |
| **Rewind** | Quay về checkpoint trước, bỏ đi các thay đổi sau đó |
| **Branch Point** | Checkpoint để từ đó phân nhánh và thử nhiều hướng tiếp cận |

## Cách truy cập Checkpoints

Có hai cách chính để truy cập và quản lý checkpoints:

### Dùng phím tắt
Nhấn `Esc` hai lần (`Esc` + `Esc`) để mở giao diện checkpoint và duyệt qua các checkpoint đã lưu.

### Dùng lệnh Slash
Dùng lệnh `/rewind` (hoặc bí danh `/checkpoint`) để truy cập nhanh:

```bash
# Mở giao diện rewind
/rewind

# Hoặc dùng bí danh
/checkpoint
```

## Các tùy chọn khi Rewind

Khi thực hiện rewind, bạn sẽ thấy menu với năm lựa chọn:

1. **Restore code and conversation** — Hoàn nguyên cả file lẫn tin nhắn về checkpoint đó
2. **Restore conversation** — Chỉ hoàn nguyên tin nhắn, giữ nguyên code hiện tại
3. **Restore code** — Chỉ hoàn nguyên các thay đổi file, giữ nguyên toàn bộ lịch sử hội thoại
4. **Summarize from here** — Nén hội thoại từ điểm này trở đi thành bản tóm tắt do AI tạo, thay vì xóa bỏ. Các tin nhắn gốc vẫn được lưu trong transcript. Bạn có thể cung cấp hướng dẫn để tóm tắt tập trung vào các chủ đề cụ thể.
5. **Never mind** — Hủy và quay về trạng thái hiện tại

## Checkpoint tự động

Claude Code tự động tạo checkpoint cho bạn:

- **Mỗi lần bạn gửi tin nhắn** — Checkpoint mới được tạo với mỗi lần nhập liệu
- **Bền vững** — Checkpoints tồn tại qua các phiên làm việc
- **Tự dọn dẹp** — Checkpoints được tự động xóa sau 30 ngày

Nghĩa là bạn luôn có thể quay về bất kỳ thời điểm nào trong cuộc hội thoại, từ vài phút trước đến vài ngày trước.

## Các trường hợp sử dụng

| Tình huống | Quy trình |
|-----------|-----------|
| **Thử nhiều hướng tiếp cận** | Lưu → Thử A → Lưu → Rewind → Thử B → So sánh |
| **Refactor an toàn** | Lưu → Refactor → Test → Nếu fail: Rewind |
| **A/B Testing** | Lưu → Thiết kế A → Lưu → Rewind → Thiết kế B → So sánh |
| **Phục hồi sau lỗi** | Phát hiện vấn đề → Rewind về trạng thái tốt gần nhất |

## Cách dùng Checkpoints

### Xem và Rewind

Nhấn `Esc` hai lần hoặc dùng `/rewind` để mở trình duyệt checkpoint. Bạn sẽ thấy danh sách các checkpoint có sẵn với nhãn thời gian. Chọn checkpoint bất kỳ để quay về trạng thái đó.

### Chi tiết Checkpoint

Mỗi checkpoint hiển thị:
- Thời điểm tạo
- Các file đã thay đổi
- Số lượng tin nhắn trong hội thoại
- Các công cụ đã dùng

## Ví dụ thực tế

### Ví dụ 1: Thử nhiều hướng tiếp cận

```
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Thực hiện thay đổi tại checkpoint A]

User: Actually, let's try in-memory caching instead

Claude: I'll rewind to explore a different approach...
[Người dùng nhấn Esc+Esc và rewind về checkpoint A]
[Triển khai in-memory caching tại checkpoint B]

User: Now I can compare both approaches
```

### Ví dụ 2: Phục hồi sau lỗi

```
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Thực hiện nhiều thay đổi]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll help you rewind to before the refactoring...
[Người dùng nhấn Esc+Esc và chọn checkpoint trước khi refactor]

User: Let's try a more conservative approach this time
```

### Ví dụ 3: Thử nghiệm an toàn

```
User: Let's try rewriting this in a functional style
[Tạo checkpoint trước khi thử nghiệm]

Claude: [Thực hiện các thay đổi thử nghiệm]

User: The tests are failing. Let's rewind.
[Người dùng nhấn Esc+Esc và rewind về checkpoint]

Claude: I've rewound the changes. Let's try a different approach.
```

### Ví dụ 4: Phân nhánh hướng tiếp cận

```
User: I want to compare two database designs
[Ghi nhớ checkpoint — đặt tên "Start"]

Claude: I'll create the first design...
[Triển khai Schema A]

User: Now let me go back and try the second approach
[Người dùng nhấn Esc+Esc và rewind về "Start"]

Claude: Now I'll implement Schema B...
[Triển khai Schema B]

User: Great! Now I have both schemas to choose from
```

## Thời hạn lưu Checkpoint

Claude Code tự động quản lý checkpoint của bạn:

- Checkpoint được tạo tự động với mỗi lần gửi tin nhắn
- Checkpoint cũ được lưu tối đa 30 ngày
- Checkpoint được tự động dọn dẹp để tránh tốn quá nhiều dung lượng

## Các mẫu quy trình làm việc

### Chiến lược phân nhánh khi khám phá

Khi thử nhiều hướng tiếp cận:

```
1. Bắt đầu với triển khai ban đầu → Checkpoint A
2. Thử Hướng 1 → Checkpoint B
3. Rewind về Checkpoint A
4. Thử Hướng 2 → Checkpoint C
5. So sánh kết quả từ B và C
6. Chọn hướng tốt nhất và tiếp tục
```

### Mẫu Refactor an toàn

Khi thực hiện thay đổi lớn:

```
1. Trạng thái hiện tại → Checkpoint (tự động)
2. Bắt đầu refactor
3. Chạy tests
4. Nếu tests pass → Tiếp tục làm việc
5. Nếu tests fail → Rewind và thử hướng khác
```

## Thực hành tốt

Vì checkpoint được tạo tự động, bạn có thể tập trung vào công việc mà không cần lo lưu trạng thái thủ công. Tuy nhiên, hãy ghi nhớ:

### Dùng Checkpoints hiệu quả

✅ **Nên làm:**
- Xem lại các checkpoint có sẵn trước khi rewind
- Dùng rewind khi muốn khám phá hướng khác
- Giữ checkpoint để so sánh các hướng tiếp cận khác nhau
- Hiểu rõ từng tùy chọn rewind (restore code and conversation, restore conversation, restore code, hoặc summarize)

❌ **Không nên:**
- Chỉ dựa vào checkpoint để bảo toàn code
- Kỳ vọng checkpoint theo dõi thay đổi file ngoài hệ thống
- Dùng checkpoint thay thế cho git commits

## Cấu hình

Bạn có thể bật/tắt checkpoint tự động trong cài đặt:

```json
{
  "autoCheckpoint": true
}
```

- `autoCheckpoint`: Bật/tắt tính năng tự động tạo checkpoint với mỗi lần gửi tin nhắn (mặc định: `true`)

## Giới hạn

Checkpoints có các giới hạn sau:

- **Không theo dõi thay đổi từ lệnh Bash** — Các thao tác như `rm`, `mv`, `cp` trên hệ thống file không được ghi lại trong checkpoint
- **Không theo dõi thay đổi bên ngoài** — Thay đổi thực hiện ngoài Claude Code (trong editor, terminal...) không được ghi lại
- **Không thay thế version control** — Dùng git cho các thay đổi cần lưu vĩnh viễn và có thể kiểm tra lại

## Xử lý sự cố

### Checkpoint bị thiếu

**Vấn đề**: Không tìm thấy checkpoint mong đợi

**Giải pháp**:
- Kiểm tra xem checkpoints có bị xóa không
- Xác nhận `autoCheckpoint` đã được bật trong cài đặt
- Kiểm tra dung lượng ổ đĩa

### Rewind thất bại

**Vấn đề**: Không thể rewind về checkpoint

**Giải pháp**:
- Đảm bảo không có thay đổi chưa commit gây xung đột
- Kiểm tra xem checkpoint có bị hỏng không
- Thử rewind về checkpoint khác

## Tích hợp với Git

Checkpoints bổ trợ cho git (không thay thế):

| Tính năng | Git | Checkpoints |
|-----------|-----|-------------|
| Phạm vi | Hệ thống file | Hội thoại + file |
| Tính bền vững | Vĩnh viễn | Theo phiên |
| Độ chi tiết | Commits | Bất kỳ thời điểm nào |
| Tốc độ | Chậm hơn | Tức thì |
| Chia sẻ | Có | Hạn chế |

Dùng kết hợp cả hai:
1. Dùng checkpoint để thử nghiệm nhanh
2. Dùng git commit cho các thay đổi hoàn chỉnh
3. Tạo checkpoint trước khi thực hiện git operations
4. Commit các trạng thái checkpoint thành công vào git

## Hướng dẫn bắt đầu nhanh

### Quy trình cơ bản

1. **Làm việc bình thường** — Claude Code tự động tạo checkpoint
2. **Muốn quay lại?** — Nhấn `Esc` hai lần hoặc dùng `/rewind`
3. **Chọn checkpoint** — Chọn từ danh sách để rewind
4. **Chọn nội dung cần khôi phục** — Chọn restore code and conversation, restore conversation, restore code, summarize from here, hoặc hủy
5. **Tiếp tục làm việc** — Bạn đã quay về thời điểm đó

### Phím tắt

- **`Esc` + `Esc`** — Mở trình duyệt checkpoint
- **`/rewind`** — Cách khác để truy cập checkpoint
- **`/checkpoint`** — Bí danh của `/rewind`

## Các khái niệm liên quan

- **[Advanced Features](../09-advanced-features/)** — Chế độ lập kế hoạch và các tính năng nâng cao khác
- **[Memory Management](../02-memory/)** — Quản lý lịch sử hội thoại và ngữ cảnh
- **[Slash Commands](../01-slash-commands/)** — Các lệnh tắt do người dùng kích hoạt
- **[Hooks](../06-hooks/)** — Tự động hóa theo sự kiện
- **[Plugins](../07-plugins/)** — Gói mở rộng tích hợp sẵn

## Tài nguyên bổ sung

- [Tài liệu chính thức về Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [Hướng dẫn Advanced Features](../09-advanced-features/) — Extended thinking và các tính năng khác

## Tóm tắt

Checkpoints là tính năng tự động của Claude Code giúp bạn thử nghiệm thoải mái mà không sợ mất công. Mỗi lần bạn gửi tin nhắn, một checkpoint mới được tạo tự động — bạn có thể quay về bất kỳ thời điểm nào trong phiên làm việc.

Lợi ích chính:
- Thử nghiệm nhiều hướng tiếp cận mà không lo rủi ro
- Phục hồi nhanh sau khi mắc lỗi
- So sánh các giải pháp cạnh nhau
- Tích hợp an toàn với hệ thống version control

Nhớ rằng: checkpoint không thay thế git. Dùng checkpoint để thử nghiệm nhanh, dùng git cho các thay đổi code hoàn chỉnh.
