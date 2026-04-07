---
name: Documentation Refactor
description: Cấu trúc lại tài liệu dự án để rõ ràng và dễ truy cập
tags: documentation, refactoring, organization
---

# Documentation Refactor

Refactor cấu trúc tài liệu dự án được điều chỉnh theo loại dự án:

1. **Phân tích dự án**: Xác định loại (library/API/web app/CLI/microservices), kiến trúc, và personas người dùng
2. **Tập trung tài liệu**: Chuyển tài liệu kỹ thuật vào `docs/` với các tham chiếu chéo phù hợp
3. **README.md gốc**: Đơn giản hóa như điểm vào với tổng quan, bắt đầu nhanh, tóm tắt modules/components, giấy phép, liên hệ
4. **Tài liệu component**: Thêm các file README module/package/service-level với hướng dẫn thiết lập và testing
5. **Tổ chức `docs/`** theo các danh mục phù hợp:
   - Architecture, API Reference, Database, Design, Troubleshooting, Deployment, Contributing (điều chỉnh theo nhu cầu dự án)
6. **Tạo hướng dẫn** (chọn cái phù hợp):
   - User Guide: Tài liệu người dùng cuối cho các ứng dụng
   - API Documentation: Các endpoints, xác thực, ví dụ cho APIs
   - Development Guide: Thiết lập, testing, workflow đóng góp
   - Deployment Guide: Triển khai production cho các dịch vụ/ứng dụng
7. **Sử dụng Mermaid** cho tất cả các sơ đồ (architecture, flows, schemas)

Giữ tài liệu ngắn gọn, dễ quét, và phù hợp với loại dự án.
