---
description: Tạo tài liệu API toàn diện từ mã nguồn
---

# Trình Tạo Tài Liệu API

Tạo tài liệu API bằng cách:

1. Quét tất cả các file trong `/src/api/`
2. Trích xuất chữ ký hàm và bình luận JSDoc
3. Tổ chức theo endpoint/module
4. Tạo markdown với các ví dụ
5. Bao gồm các schema request/response
6. Thêm tài liệu lỗi

Định dạng đầu ra:
- File markdown trong `/docs/api.md`
- Bao gồm các ví dụ curl cho tất cả endpoints
- Thêm các kiểu TypeScript
