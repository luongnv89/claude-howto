---
name: Expand Unit Tests
description: Tăng vùng phủ test bằng cách nhắm vào các nhánh chưa được test và các trường hợp ngoại lệ
tags: testing, coverage, unit-tests
---

# Mở Rộng Unit Tests

Mở rộng các unit tests hiện có được điều chỉnh theo framework testing của dự án:

1. **Phân tích vùng phủ**: Chạy báo cáo vùng phủ để xác định các nhánh chưa được test, các trường hợp ngoại lệ, và các khu vực có vùng phủ thấp
2. **Xác định các khoảng trống**: Review code để tìm các nhánh logic, các đường dẫn lỗi, các điều kiện biên, đầu vào null/rỗng
3. **Viết tests** sử dụng framework của dự án:
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **Nhắm vào các kịch bản cụ thể**:
   - Xử lý lỗi và ngoại lệ
   - Các giá trị biên (min/max, rỗng, null)
   - Các trường hợp ngoại lệ và trường hợp góc
   - Chuyển đổi trạng thái và tác dụng phụ
5. **Xác minh cải tiến**: Chạy vùng phủ một lần nữa, xác nhận gia tăng có thể đo lường được

Chỉ trình bày các khối code test mới. Theo dõi các mẫu test hiện có và quy ước đặt tên.
