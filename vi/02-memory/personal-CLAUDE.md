# Tùy Chọn Phát Triển Của Tôi

## Về Tôi
- **Mức Độ Kinh Nghiệm**: 8 năm phát triển full-stack
- **Ngôn Ngữ Ưa Thích**: TypeScript, Python
- **Phong Cách Giao Tiếp**: Trực tiếp, kèm ví dụ
- **Phong Cách Học**: Sơ đồ trực quan kèm code

## Tùy Chọn Về Code

### Xử Lý Lỗi
Tôi ưu tiên xử lý lỗi tường minh với khối try-catch và thông báo lỗi có ý nghĩa.
Tránh các lỗi chung chung. Luôn log lỗi để debug.

### Comment
Dùng comment để giải thích TẠI SAO, không phải CÁI GÌ. Code nên tự giải thích chính nó.
Comment nên giải thích logic nghiệp vụ hoặc các quyết định không hiển nhiên.

### Testing
Tôi ưu tiên TDD (phát triển hướng kiểm thử).
Viết test trước, sau đó mới implement.
Tập trung vào hành vi, không phải chi tiết implementation.

### Kiến Trúc
Tôi ưu tiên thiết kế module hóa, liên kết lỏng.
Dùng dependency injection để dễ kiểm thử.
Tách biệt các mối quan tâm (Controllers, Services, Repositories).

## Tùy Chọn Khi Debug
- Dùng console.log với tiền tố: `[DEBUG]`
- Bao gồm ngữ cảnh: tên hàm, các biến liên quan
- Dùng stack trace khi có
- Luôn bao gồm timestamp trong log

## Giao Tiếp
- Giải thích các khái niệm phức tạp bằng sơ đồ
- Đưa ví dụ cụ thể trước khi giải thích lý thuyết
- Bao gồm các đoạn code trước/sau
- Tóm tắt các điểm chính ở cuối

## Tổ Chức Dự Án
Tôi tổ chức các dự án của mình như sau:
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

## Công Cụ
- **IDE**: VS Code với phím tắt vim
- **Terminal**: Zsh với Oh-My-Zsh
- **Định Dạng**: Prettier (độ dài dòng 100 ký tự)
- **Linter**: ESLint với cấu hình airbnb
- **Framework Test**: Jest với React Testing Library

---
**Cập Nhật Lần Cuối**: Ngày 4 tháng 8 năm 2026
**Phiên Bản Claude Code**: 2.1.220
**Nguồn**:
- https://code.claude.com/docs/en/memory
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
