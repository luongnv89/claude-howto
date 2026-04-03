# Chính Sách Bảo Mật / Security Policy

## Tổng Quan / Overview

Bảo mật của dự án Claude How To là quan trọng đối với chúng tôi. Tài liệu này phác thảo các thực hành bảo mật của chúng và mô tả cách báo cáo các lỗ hổng bảo mật một cách có trách nhiệm.

## Các Phiên Bản Được Hỗ Trợ / Supported Versions

Chúng tôi cung cấp các bản cập nhật bảo mật cho các phiên bản sau:

| Phiên Bản | Trạng Thái | Hỗ Trợ Đến |
|---------|--------|---------------|
| Mới nhất (main) | ✅ Hoạt Động | Hiện tại + 6 tháng |
| Bản phát hành 1.x | ✅ Hoạt Động | Đến phiên bản lớn tiếp theo |

**Lưu ý**: Là một dự án hướng dẫn giáo dục, chúng tôi tập trung vào việc duy trì các thực hành tốt nhất hiện tại và bảo mật tài liệu hơn là hỗ trợ phiên bản truyền thống. Các bản cập nhật được áp dụng trực tiếp vào nhánh chính.

## Thực Hành Bảo Mật / Security Practices

### Bảo Mật Code

1. **Quản Lý Dependency**
   - Tất cả dependencies Python được pinned trong `requirements.txt`
   - Cập nhật thường xuyên qua dependabot và review thủ công
   - Quét bảo mật với Bandit trên mỗi commit
   - Pre-commit hooks cho các kiểm tra bảo mật

2. **Chất Lượng Code**
   - Linting với Ruff bắt các vấn đề phổ biến
   - Kiểm tra kiểu với mypy ngăn các lỗ hổng liên quan đến kiểu
   - Pre-commit hooks thực thi các tiêu chuẩn
   - Tất cả các thay đổi được review trước khi gộp

3. **Kiểm Soát Truy Cập**
   - Bảo vệ nhánh trên nhánh `main`
   - Yêu cầu review trước khi gộp
   - Các kiểm tra trạng thái phải pass trước khi gộp
   - Quyền ghi hạn chế đến repository

### Bảo Mật Tài Liệu

1. **Không Secrets trong Ví Dụ**
   - Tất cả API keys trong ví dụ là placeholders
   - Credentials không bao giờ được hardcode
   - Các file `.env.example` hiển thị các biến được yêu cầu
   - Cảnh báo rõ về quản lý secret

2. **Thực Hành Bảo Mật Tốt Nhất**
   - Các ví dụ minh họa các mẫu an toàn
   - Cảnh báo bảo mật được làm nổi bật trong tài liệu
   - Links đến các hướng dẫn bảo mật chính thức
   - Xử lý credential được thảo luận trong các phần liên quan

3. **Review Nội Dung**
   - Tất cả tài liệu được review cho các vấn đề bảo mật
   - Các cân nhắc bảo mật trong hướng dẫn đóng góp
   - Xác thực các liên kết và tham khảo bên ngoài

## Báo Cáo Một Lỗ Hổng Bảo Mật / Reporting a Vulnerability

### Vấn Đề Bảo Mật Chúng Tôi Quan Tâm

Chúng tôi đánh giá cao các báo cáo về:
- **Lỗ hổng code** trong scripts hoặc ví dụ
- **Lỗ hổng dependency** trong các gói Python
- **Vấn đề mật mã** trong bất kỳ ví dụ code nào
- **Lỗi Xác Thực/Ủy Quy** trong tài liệu
- **Rủi ro lộ dữ liệu** trong ví dụ cấu hình
- **Lỗ hổng tiêm nhiễm** (SQL, command, v.v.)

### Cách Báo Cáo / How to Report

Vui lòng báo cáo các lỗ hổng bảo mật một cách riêng tư:
- Gửi email đến: security@example.com
- Sử dụng tiêu đề email: [Security] Mô tả ngắn gọn
- Cung cấp đủ chi tiết để chúng tôi tái tạo và xác nhận vấn đề

Chúng tôi sẽ:
- Xác nhận nhận trong vòng 48 giờ
- Cung cấp timeline cho việc sửa
- Thông báo khi bản vá đã được phát hành
- Công khai thừa nhận báo cáo của bạn (nếu bạn muốn)
