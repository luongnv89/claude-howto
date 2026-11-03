# Tiêu Chuẩn Cho Module API

File này bổ sung cho CLAUDE.md gốc đối với mọi thứ trong /src/api/. Các file bộ nhớ được
nối lại với nhau, không ghi đè lẫn nhau — CLAUDE.md gốc vẫn được áp dụng, và Claude Code
tải file này theo yêu cầu khi nó đọc, ghi hoặc chỉnh sửa file trong cây thư mục con này.

## Tiêu Chuẩn Riêng Cho API

### Xác Thực Request
- Dùng Zod để xác thực schema
- Luôn xác thực đầu vào
- Trả về 400 kèm các lỗi xác thực
- Bao gồm chi tiết lỗi theo từng trường

### Xác Thực Danh Tính
- Tất cả endpoint đều yêu cầu JWT token
- Token nằm trong header Authorization
- Token hết hạn sau 24 giờ
- Triển khai cơ chế refresh token

### Định Dạng Response

Tất cả response phải tuân theo cấu trúc này:

```json
{
  "success": true,
  "data": { /* dữ liệu thực tế */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

Response lỗi:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* lỗi theo từng trường */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Phân Trang
- Dùng phân trang dựa trên cursor (không dùng offset)
- Bao gồm boolean `hasMore`
- Giới hạn kích thước trang tối đa là 100
- Kích thước trang mặc định: 20

### Giới Hạn Tần Suất
- 1000 request mỗi giờ cho người dùng đã xác thực
- 100 request mỗi giờ cho endpoint công khai
- Trả về 429 khi vượt quá giới hạn
- Bao gồm header retry-after

### Caching
- Dùng Redis để cache session
- Thời gian cache: mặc định 5 phút
- Vô hiệu hóa cache khi có thao tác ghi
- Gắn tag loại tài nguyên cho cache key

---
**Cập Nhật Lần Cuối**: Ngày 10 tháng 10 năm 2026
**Phiên Bản Claude Code**: 2.1.296
**Nguồn**:
- https://code.claude.com/docs/en/memory
- https://github.com/anthropics/claude-code/releases/tag/v2.1.288
- https://github.com/anthropics/claude-code/releases/tag/v2.1.293
**Các Mô Hình Tương Thích**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
