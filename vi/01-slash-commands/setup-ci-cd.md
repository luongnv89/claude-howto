---
name: Setup CI/CD Pipeline
description: Triển khai pre-commit hooks và GitHub Actions để đảm bảo chất lượng
tags: ci-cd, devops, automation
---

# Thiết Lập Pipeline CI/CD

Triển khai các cổng chất lượng DevOps toàn diện được điều chỉnh theo loại dự án:

1. **Phân tích dự án**: Phát hiện ngôn ngữ, framework, hệ thống build, và công cụ hiện có
2. **Cấu hình pre-commit hooks** với các công cụ cụ thể theo ngôn ngữ:
   - Định dạng: Prettier/Black/gofmt/rustfmt/v.v.
   - Linting: ESLint/Ruff/golangci-lint/Clippy/v.v.
   - Bảo mật: Bandit/gosec/cargo-audit/npm audit/v.v.
   - Kiểm tra kiểu: TypeScript/mypy/flow (nếu áp dụng)
   - Tests: Chạy các bộ test phù hợp
3. **Tạo các workflow GitHub Actions** (.github/workflows/):
   - Phản ánh các kiểm tra pre-commit trên push/PR
   - Ma trận đa phiên bản/nền tảng (nếu áp dụng)
   - Xác minh build và test
   - Các bước triển khai (nếu cần)
4. **Xác minh pipeline**: Test cục bộ, tạo PR kiểm tra, xác nhận tất cả các kiểm tra vượt qua

Sử dụng các công cụ miễn phí/mã nguồn mở. Tôn trọng các cấu hình hiện có. Giữ thực thi nhanh.
