---
description: Phân tích code để tìm các vấn đề hiệu suất và đề xuất tối ưu hóa
---

# Tối Ưu Hóa Code

Review đoạn code được cung cấp để tìm các vấn đề sau theo thứ tự ưu tiên:

1. **Nút thắt hiệu suất** - xác định các thao tác O(n²), vòng lặp không hiệu quả
2. **Rò rỉ bộ nhớ** - tìm các tài nguyên chưa được giải phóng, tham chiếu vòng tròn
3. **Cải thiện thuật toán** - đề xuất các thuật toán hoặc cấu trúc dữ liệu tốt hơn
4. **Cơ hội caching** - xác định các tính toán lặp lại
5. **Vấn đề đồng thời** - tìm các điều kiện tranh đua hoặc vấn đề luồng

Định dạng phản hồi của bạn với:
- Mức độ nghiêm trọng của vấn đề (Critical/High/Medium/Low)
- Vị trí trong code
- Giải thích
- Khắc phục được khuyến nghị với ví dụ code
