---
name: code-review-specialist
description: Review code toàn diện với phân tích bảo mật, hiệu suất, và chất lượng. Sử dụng khi người dùng yêu cầu review code, phân tích chất lượng code, đánh giá pull requests, hoặc đề cập đến review code, phân tích bảo mật, hoặc tối ưu hóa hiệu suất.
---

# Code Review Skill

Skill này cung cấp các khả năng review code toàn diện tập trung vào:

1. **Phân Tích Bảo Mật**
   - Các vấn đề xác thực/uỷ quyền
   - Rủi ro lộ dữ liệu
   - Lỗ hổng tiêm nhiễm
   - Điểm yếu mật mã
   - Ghi log dữ liệu nhạy cảm

2. **Review Hiệu Suất**
   - Hiệu quả thuật toán (phân tích Big O)
   - Tối ưu hóa bộ nhớ
   - Tối ưu hóa truy vấn cơ sở dữ liệu
   - Cơ hội caching
   - Các vấn đề đồng thời

3. **Chất Lượng Code**
   - Nguyên tắc SOLID
   - Mẫu thiết kế
   - Quy ước đặt tên
   - Tài liệu hóa
   - Phủ vùng test

4. **Khả Năng Duy Trì**
   - Khả năng đọc code
   - Kích thước hàm (nên < 50 dòng)
   - Độ phức tạp vòng lục
   - Quản lý dependency
   - An toàn kiểu

## Mẫu Review

Đối với mỗi đoạn code được review, cung cấp:

### Tóm Tắt
- Đánh giá chất lượng tổng thể (1-5)
- Số lượng phát hiện chính
- Các khu vực ưu tiên được khuyến nghị

### Vấn Đề Nguy Kịch (nếu có)
- **Vấn đề**: Mô tả rõ ràng
- **Vị Trí**: File và số dòng
- **Tác Động**: Tại sao điều này quan trọng
- **Mức Độ**: Nguy Kịch/Cao/Trung Bình
- **Khắc Phục**: Ví dụ code

### Các Phát Hiện Theo Danh Mục

#### Bảo Mật (nếu tìm thấy vấn đề)
Liệt kê các lỗ hổng bảo mật với ví dụ

#### Hiệu Suất (nếu tìm thấy vấn đề)
Liệt kê các vấn đề hiệu suất với phân tích độ phức tạp

#### Chất Lượng (nếu tìm thấy vấn đề)
Liệt kê các vấn đề chất lượng code với các đề xuất refactor

#### Khả Năng Duy Trì (nếu tìm thấy vấn đề)
Liệt kê các vấn đề duy trì với các cải tiến

## Lịch Sử Phiên Bản

- v1.0.0 (2024-12-10): Phiên bản phát hành ban đầu với phân tích bảo mật, hiệu suất, chất lượng, và khả năng duy trì
