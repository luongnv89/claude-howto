# Cấu Hình Dự Án

## Tổng Quan Dự Án
- **Tên**: Nền Tảng Thương Mại Điện Tử
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Quy Mô Nhóm**: 5 lập trình viên
- **Hạn Chót**: Q4 2025

## Kiến Trúc
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Tiêu Chuẩn Phát Triển

### Phong Cách Code
- Dùng Prettier để định dạng
- Dùng ESLint với cấu hình airbnb
- Độ dài dòng tối đa: 100 ký tự
- Thụt lề 2 dấu cách

### Quy Ước Đặt Tên
- **File**: kebab-case (user-controller.js)
- **Class**: PascalCase (UserService)
- **Hàm/Biến**: camelCase (getUserById)
- **Hằng số**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Bảng Database**: snake_case (user_accounts)

### Git Workflow
- Tên branch: `feature/description` hoặc `fix/description`
- Commit message: Tuân theo conventional commits
- Bắt buộc có PR trước khi merge
- Tất cả các kiểm tra CI/CD phải pass
- Cần tối thiểu 1 approval

### Yêu Cầu Testing
- Code coverage tối thiểu 80%
- Tất cả các luồng quan trọng phải có test
- Dùng Jest cho unit test
- Dùng Cypress cho E2E test
- Tên file test: `*.test.ts` hoặc `*.spec.ts`

### Tiêu Chuẩn API
- Chỉ dùng endpoint RESTful
- Request/response dạng JSON
- Dùng HTTP status code đúng cách
- Đánh phiên bản cho API endpoint: `/api/v1/`
- Tài liệu hóa tất cả endpoint kèm ví dụ

### Database
- Dùng migration cho các thay đổi schema
- Không bao giờ hardcode thông tin xác thực
- Dùng connection pooling
- Bật query logging trong môi trường development
- Bắt buộc backup định kỳ

### Triển Khai
- Triển khai dựa trên Docker
- Điều phối bằng Kubernetes
- Chiến lược triển khai blue-green
- Tự động rollback khi thất bại
- Database migration chạy trước khi deploy

## Các Lệnh Thường Dùng

| Lệnh | Mục Đích |
|---------|---------|
| `npm run dev` | Khởi động development server |
| `npm test` | Chạy bộ test |
| `npm run lint` | Kiểm tra phong cách code |
| `npm run build` | Build cho production |
| `npm run migrate` | Chạy database migration |

## Liên Hệ Trong Nhóm
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Vấn Đề Đã Biết & Cách Khắc Phục
- Connection pooling của PostgreSQL bị giới hạn ở 20 trong giờ cao điểm
- Cách khắc phục: Triển khai hàng đợi query
- Safari 14 gặp vấn đề tương thích với async generator
- Cách khắc phục: Dùng Babel transpiler

## Dự Án Liên Quan
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`

---
**Cập Nhật Lần Cuối**: Ngày 4 tháng 8 năm 2026
**Phiên Bản Claude Code**: 2.1.220
**Nguồn**:
- https://code.claude.com/docs/en/memory
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
