<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Đóng Góp Cho Claude How To / Contributing to Claude How To

Cảm ơn bạn quan tâm đến việc đóng góp cho dự án này! Hướng dẫn này sẽ giúp bạn hiểu cách đóng góp hiệu quả.

## Về Dự Án Này / About This Project

Claude How To là một hướng dẫn trực quan, dựa trên ví dụ cho Claude Code. Chúng tôi cung cấp:
- **Sơ đồ Mermaid** giải thích cách các tính năng hoạt động
- **Mẫu sản xuất sẵn** bạn có thể sử dụng ngay lập tức
- **Ví dụ thực tế** với ngữ cảnh và thực hành tốt nhất
- **Đường dẫn học tập tiến bộ** từ người mới bắt đầu đến nâng cao

## Các Loại Đóng Góp / Types of Contributions

### 1. Ví Dụ hoặc Mẫu Mới
Thêm ví dụ cho các tính năng hiện có (slash commands, skills, hooks, v.v.):
- Code sẵn sàng để copy-paste
- Giải thích rõ ràng cách nó hoạt động
- Các trường hợp sử dụng và lợi ích
- Mẹo xử lý sự cố

### 2. Cải Tiện Tài Liệu
- Làm rõ các phần nhầm hiểu
- Sửa lỗi chính tả và ngữ pháp
- Thêm thông tin còn thiếu
- Cải thiện các ví dụ code

### 3. Hướng Dẫn Tính Năng
Tạo hướng dẫn cho các tính năng Claude Code mới:
- Hướng dẫn từng bước
- Sơ đồ kiến trúc
- Các mẫu và anti-patterns phổ biến
- Workflows thực tế

### 4. Báo Cáo Lỗi
Báo cáo các vấn đề bạn gặp phải:
- Mô tả những gì bạn mong đợi
- Mô tả những gì thực sự xảy ra
- Bao gồm các bước để tái tạo
- Thêm phiên bản Claude Code và OS có liên quan

### 5. Feedback và Đề Xuất
Giúp cải thiện hướng dẫn:
- Đề xuất giải thích tốt hơn
- Chỉ ra các khoảng trống trong phạm vi
- Khuyến nghị các phần mới hoặc tái tổ chức

## Bắt Đầu / Getting Started

### 1. Fork và Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. Tạo một Nhánh
Sử dụng tên nhánh mô tả:
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. Thiết Lập Môi Trường Của Bạn

Pre-commit hooks chạy cùng các kiểm tra như CI cục bộ trước mỗi commit. Tất cả bốn kiểm tra phải pass trước khi PR được chấp nhận.

**Dependencies được yêu cầu:**

```bash
# Python tooling (uv là trình quản lý package cho dự án này)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown linter (Node.js)
npm install -g markdownlint-cli

# Mermaid diagram validator (Node.js)
npm install -g @mermaid-js/mermaid-cli

# Install pre-commit và activate hooks
uv pip install pre-commit
pre-commit install
```

**Xác minh thiết lập của bạn:**

```bash
pre-commit run --all-files
```

Các hooks chạy trên mỗi commit là:
