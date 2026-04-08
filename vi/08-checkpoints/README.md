<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints và Rewind / Checkpoints and Rewind

Checkpoints cho phép bạn lưu trạng thái hội thoại và quay lại các điểm trước đó trong phiên Claude Code của bạn. Điều này vô giá khi khám phá các cách tiếp cận khác nhau, phục hồi từ sai lầm, hoặc so sánh các giải pháp thay thế.

## Tổng Quan / Overview

Checkpoints cho phép bạn lưu trạng thái hội thoại và quay lại các điểm trước đó, cho phép thử nghiệm an toàn và khám phá nhiều cách tiếp cận. Chúng là các snapshot của trạng thái hội thoại của bạn, bao gồm:
- Tất cả các trao đổi tin nhắn
- Các sửa đổi file được thực hiện
- Lịch sử sử dụng công cụ
- Ngữ cảnh phiên

Checkpoints vô giá khi khám phá các cách tiếp cận khác nhau, phục hồi từ sai lầm, hoặc so sánh các giải pháp thay thế.

## Các Khái Niệm Chính / Key Concepts

| Khái Niệm | Mô Tả |
|---------|-------------|
| **Checkpoint** | Snapshot của trạng thái hội thoại bao gồm tin nhắn, files, và ngữ cảnh |
| **Rewind** | Quay lại checkpoint trước đó, loại bỏ các thay đổi tiếp theo |
| **Điểm Nhánh** | Checkpoint từ đó nhiều cách tiếp cận được khám phá |

## Truy Cập Checkpoints / Accessing Checkpoints

Bạn có thể truy cập và quản lý checkpoints theo hai cách chính:

### Sử Dụng Phím Tắt / Using Keyboard Shortcut
Nhấn `Esc` hai lần (`Esc` + `Esc`) để mở giao diện checkpoint và duyệt các checkpoints đã lưu.

### Sử Dụng Lệnh Slash / Using Slash Command
Sử dụng lệnh `/rewind` (bí danh: `/checkpoint`) để truy cập nhanh:

```bash
# Mở giao diện rewind
/rewind

# Hoặc sử dụng bí danh
/checkpoint
```

## Các Tùy Chọn Rewind / Rewind Options

Khi bạn rewind, bạn được trình bày một menu năm tùy chọn:

1. **Khôi phục code và hội thoại** -- Hoàn nguyên cả files và tin nhắn đến checkpoint đó
2. **Khôi phục hội thoại** -- Chỉ rewind tin nhắn, giữ code hiện tại của bạn như-is
3. **Khôi phục code** -- Chỉ hoàn nguyên các thay đổi file, giữ toàn bộ lịch sử hội thoại
4. **Tóm tắt từ đây** -- Nén hội thoại từ điểm này thành tóm tắt được tạo bởi AI thay vì loại bỏ nó. Các tin nhắn gốc được bảo toàn trong transcript. Bạn có thể tùy chọn cung cấp hướng dẫn để tập trung tóm tắt vào các chủ đề cụ thể.
5. **Không sao cả** -- Hủy và quay lại trạng thái hiện tại

## Checkpoints Tự Động / Automatic Checkpoints

Claude Code tự động tạo checkpoints cho bạn:

- **Mọi prompt người dùng** - Một checkpoint mới được tạo với mỗi đầu vào người dùng
- **Liên tục** - Checkpoints tồn tại qua các phiên
- **Tự động dọn dẹp** - Checkpoints được tự động dọn dẹp sau 30 ngày

Điều này có nghĩa là bạn luôn có thể rewind đến bất kỳ điểm nào trước đó trong hội thoại của bạn, từ vài phút trước đến nhiều ngày trước.

## Các Trường Hợp Sử Dụng / Use Cases

| Kịch Bản | Workflow |
|----------|----------|
| **Khám Phá Cách Tiếp Cận** | Lưu → Thử A → Lưu → Rewind → Thử B → So Sánh |
| **Refactoring An Toàn** | Lưu → Refactor → Test → Nếu fail: Rewind |
| **A/B Testing** | Lưu → Thiết Kế A → Lưu → Rewind → Thiết Kế B → So Sánh |
| **Phục Hồi Sai Lầm** | Nhận thấy vấn đề → Rewind đến trạng thái tốt cuối |

## Sử Dụng Checkpoints / Using Checkpoints

### Xem và Rewind / Viewing and Rewinding

Nhấn `Esc` hai lần hoặc sử dụng `/rewind` để mở trình duyệt checkpoint. Bạn sẽ thấy danh sách tất cả các checkpoints có sẵn với timestamps. Chọn bất kỳ checkpoint nào để rewind đến trạng thái đó.

### Chi Tiết Checkpoint / Checkpoint Details

Mỗi checkpoint hiển thị:
- Timestamp khi nó được tạo
- Các file đã được sửa đổi
- Số lượng tin nhắn trong hội thoại
- Các công cụ đã được sử dụng

## Ví Dụ Thực Tiễn / Practical Examples

### Ví Dụ 1: Khám Phá Các Cách Tiếp Cận Khác Nhau / Example 1: Exploring Different Approaches

```
User: Hãy thêm một lớp caching vào API

Claude: Tôi sẽ thêm Redis caching vào các API endpoints của bạn...
[Thực hiện thay đổi tại checkpoint A]

User: Thực ra, hãy thử in-memory caching thay thế

Claude: Tôi sẽ rewind để khám phá một cách tiếp cận khác...
[User nhấn Esc+Esc và rewinds đến checkpoint A]
[Triển khai in-memory caching tại checkpoint B]

User: Bây giờ tôi có thể so sánh cả hai cách tiếp cận
```

### Ví Dụ 2: Phục Hồi Từ Sai Lầm / Example 2: Recovering from Mistakes

```
User: Refactor module xác thực để sử dụng JWT

Claude: Tôi sẽ refactor module xác thực...
[Thực hiện các thay đổi rộng rãi]

User: Đợi, điều đó làm hỏng tích hợp OAuth. Hãy quay lại.

Claude: Tôi sẽ giúp bạn rewind đến trước khi refactor...
[User nhấn Esc+Esc và chọn checkpoint trước khi refactor]

User: Hãy thử một cách tiếp cận thận trọng hơn lần này
```

### Ví Dụ 3: Thử Nghiệm An Toàn / Example 3: Safe Experimentation

```
User: Hãy thử viết lại điều này theo phong cách functional
[Tạo checkpoint trước khi thử nghiệm]

Claude: [Thực hiện các thay đổi thử nghiệm]

User: Các tests đang fail. Hãy rewind.
[User nhấn Esc+Esc và rewinds đến checkpoint]

Claude: Tôi đã rewind các thay đổi. Hãy thử một cách tiếp cận khác.
```

### Ví Dụ 4: Các Cách Tiếp Cận Nhánh / Example 4: Branching Approaches

```
User: Tôi muốn so sánh hai thiết kế database
[Lưu ý checkpoint - gọi là "Bắt Đầu"]

Claude: Tôi sẽ tạo thiết kế đầu tiên...
[Triển khai Schema A]

User: Bây giờ để tôi quay lại và thử cách tiếp cận thứ hai
[User nhấn Esc+Esc và rewinds đến "Bắt Đầu"]

Claude: Bây giờ tôi sẽ triển khai Schema B...
[Triển khai Schema B]

User: Tuyệt! Bây giờ tôi có cả hai schemas để chọn
```

## Giữ Lại Checkpoint / Checkpoint Retention

Claude Code tự động quản lý checkpoints của bạn:

- Checkpoints được tạo tự động với mọi prompt người dùng
- Checkpoints cũ được giữ lên đến 30 ngày
- Checkpoints được tự động dọn dẹp để ngăn chặn tăng trưởng lưu trữ không giới hạn

## Các Mẫu Workflow / Workflow Patterns

### Chiến Lược Nhánh Để Khám Phá / Branching Strategy for Exploration

Khi khám phá nhiều cách tiếp cận:

```
1. Bắt đầu với triển khai ban đầu → Checkpoint A
2. Thử Cách Tiếp Cận 1 → Checkpoint B
3. Rewind đến Checkpoint A
4. Thử Cách Tiếp Cận 2 → Checkpoint C
5. So sánh kết quả từ B và C
6. Chọn cách tiếp cận tốt nhất và tiếp tục
```

### Mẫu Refactoring An Toàn / Safe Refactoring Pattern

Khi thực hiện các thay đổi đáng kể:

```
1. Trạng thái hiện tại → Checkpoint (tự động)
2. Bắt đầu refactoring
3. Chạy tests
4. Nếu tests pass → Tiếp tục làm việc
5. Nếu tests fail → Rewind và thử cách tiếp cận khác
```

## Thực Hành Tốt Nhất / Best Practices

Vì checkpoints được tạo tự động, bạn có thể tập trung vào công việc của mình mà không phải lo lắng về việc lưu trạng thái thủ công. Tuy nhiên, hãy ghi nhớ các thực hành sau:

### Sử Dụng Checkpoints Hiệu Quả / Using Checkpoints Effectively

✅ **Nên:**
- Review các checkpoints có sẵn trước khi rewind
- Sử dụng rewind khi bạn muốn khám phá các hướng khác nhau
- Giữ checkpoints để so sánh các cách tiếp cận khác nhau
- Hiểu những gì mỗi tùy chọn rewind làm (khôi phục code và hội thoại, khôi phục hội thoại, khôi phục code, hoặc tóm tắt)

❌ **Không Nên:**
- Dựa vào checkpoints một mình để bảo toàn code
- Mong đợi checkpoints theo dõi các thay đổi file hệ thống file bên ngoài
- Sử dụng checkpoints như một thay thế cho git commits

## Cấu Hình / Configuration

Bạn có thể bật/tắt checkpoints tự động trong settings của bạn:

```json
{
  "autoCheckpoint": true
}
```

- `autoCheckpoint`: Bật hoặc tắt tạo checkpoint tự động trên mọi prompt người dùng (mặc định: `true`)

## Hạn Chế / Limitations

Checkpoints có các hạn chế sau:

- **Các thay đổi lệnh Bash KHÔNG được theo dõi** - Các thao tác như `rm`, `mv`, `cp` trên hệ thống file không được ghi lại trong checkpoints
- **Các thay đổi bên ngoài KHÔNG được theo dõi** - Các thay đổi được thực hiện bên ngoài Claude Code (trong editor của bạn, terminal, v.v.) không được ghi lại
- **Không phải thay thế cho kiểm soát phiên bản** - Sử dụng git cho các thay đổi vĩnh viễn, có thể kiểm tra trong codebase của bạn

## Xử Lý Sự Cố / Troubleshooting

### Checkpoints Thiếu / Missing Checkpoints

**Vấn Đề**: Không tìm thấy checkpoint mong đợi

**Giải Pháp**:
- Kiểm tra nếu checkpoints đã bị xóa
- Xác minh rằng `autoCheckpoint` được bật trong settings của bạn
- Kiểm tra dung lượng đĩa

### Rewind Thất Bại / Rewind Failed

**Vấn Đề**: Không thể rewind đến checkpoint

**Giải Pháp**:
- Đảm bảo không có thay đổi chưa commit xung đột
- Kiểm tra nếu checkpoint bị hỏng
- Thử rewind đến một checkpoint khác

## Tích Hợp Với Git / Integration with Git

Checkpoints bổ sung (nhưng không thay thế) git:

| Tính Năng | Git | Checkpoints |
|---------|-----|-------------|
| Phạm Vi | Hệ thống file | Hội thoại + files |
| Liên Tục | Vĩnh viễn | Dựa trên phiên |
| Độ Chi Tiết | Commits | Bất kỳ điểm nào |
| Tốc Độ | Chậm hơn | Tức thì |
| Chia Sẻ | Có | Có hạn |

Sử dụng cả hai cùng nhau:
1. Sử dụng checkpoints để thử nghiệm nhanh
2. Sử dụng git commits cho các thay đổi đã hoàn thiện
3. Tạo checkpoint trước các thao tác git
4. Commit các trạng thái checkpoint thành công đến git

## Hướng Dẫn Bắt Đầu Nhanh / Quick Start Guide

### Workflow Cơ Bản / Basic Workflow

1. **Làm việc bình thường** - Claude Code tạo checkpoints tự động
2. **Muốn quay lại?** - Nhấn `Esc` hai lần hoặc sử dụng `/rewind`
3. **Chọn checkpoint** - Chọn từ danh sách để rewind
4. **Chọn những gì để khôi phục** - Chọn từ khôi phục code và hội thoại, khôi phục hội thoại, khôi phục code, tóm tắt từ đây, hoặc hủy
5. **Tiếp tục làm việc** - Bạn đã trở lại điểm đó

### Phím Tắt / Keyboard Shortcuts

- **`Esc` + `Esc`** - Mở trình duyệt checkpoint
- **`/rewind`** - Cách thay thế để truy cập checkpoints
- **`/checkpoint`** - Bí danh cho `/rewind`

## Biết Khi Nào Rewind: Giám Sát Ngữ Cảnh / Knowing When to Rewind: Context Monitoring

Checkpoints cho phép bạn quay lại — nhưng làm thế nào bạn biết *khi* bạn nên? Khi hội thoại của bạn tăng trưởng, cửa sổ ngữ cảnh của Claude được lấp đầy và chất lượng mô hình âm thầm giảm xuống. Bạn có thể đang shipping code từ một mô hình mù quáng một nửa mà không nhận ra.

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** giải quyết điều này bằng cách thêm **vùng ngữ cảnh** thời gian thực vào thanh trạng thái Claude Code của bạn. Nó theo dõi nơi bạn đang ở trong cửa sổ ngữ cảnh — từ **Plan** (xanh lá, an toàn để lập kế hoạch và code) qua **Code** (vàng, tránh bắt đầu các kế hoạch mới) đến **Dump** (cam, hoàn thành và rewind). Khi bạn thấy vùng thay đổi, bạn biết đó là thời gian để checkpoint và bắt đầu tươi mới thay vì đẩy tiếp với đầu ra bị giảm sút.

## Các Khái Niệm Liên Quan / Related Concepts

- **[Tính Năng Nâng Cao](../09-advanced-features/)** - Chế độ lập kế hoạch và các khả năng nâng cao khác
- **[Quản Lý Memory](../02-memory/)** - Quản lý lịch sử hội thoại và ngữ cảnh
- **[Slash Commands](../01-slash-commands/)** - Các phím tắt do người dùng gọi
- **[Hooks](../06-hooks/)** - Tự động hóa dựa trên sự kiện
- **[Plugins](../07-plugins/)** - Các gói mở rộng được đóng gói

## Tài Nguyên Thêm / Additional Resources

- [Tài Liệu Checkpointing Chính Thức](https://code.claude.com/docs/en/checkpointing)
- [Hướng Dẫn Tính Năng Nâng Cao](../09-advanced-features/) - Extended thinking và các khả năng khác

---

**Cập Nhật Lần Cuối**: Tháng 4 năm 2026
**Phiên Bản Claude Code**: 2.1+
**Các Mô Hình Tương Thích**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
