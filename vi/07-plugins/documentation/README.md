<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin Documentation

Tạo và duy trì tài liệu toàn diện cho dự án của bạn.

## Tính Năng

✅ Tạo tài liệu API
✅ Tạo mới và cập nhật README
✅ Đồng bộ tài liệu
✅ Cải thiện comment trong code
✅ Tạo ví dụ

## Cài Đặt

```bash
claude --plugin-dir ./07-plugins/documentation
```

## Những Gì Được Bao Gồm

### Lệnh Slash
- `/generate-api-docs` - Tạo tài liệu API
- `/generate-readme` - Tạo mới hoặc cập nhật README
- `/sync-docs` - Đồng bộ tài liệu với các thay đổi code
- `/validate-docs` - Kiểm tra tài liệu

### Tác Nhân Con
- `api-documenter` - Chuyên gia tài liệu API
- `code-commentator` - Cải thiện comment trong code
- `example-generator` - Tạo ví dụ code

### Template
- `api-endpoint.md` - Template tài liệu cho API endpoint
- `function-docs.md` - Template tài liệu cho hàm
- `adr-template.md` - Template Architecture Decision Record (ADR)

### MCP Server
- Tích hợp GitHub để đồng bộ tài liệu

## Cách Sử Dụng

### Tạo Tài Liệu API
```
/generate-api-docs
```

### Tạo README
```
/generate-readme
```

### Đồng Bộ Tài Liệu
```
/sync-docs
```

### Kiểm Tra Tài Liệu
```
/validate-docs
```

## Yêu Cầu

- Claude Code 2.1+
- Quyền truy cập GitHub (tùy chọn)

## Ví Dụ Workflow

```
User: /generate-api-docs

Claude:
1. Quét tất cả API endpoint trong /src/api/
2. Giao việc cho tác nhân con api-documenter
3. Trích xuất chữ ký hàm và JSDoc
4. Sắp xếp theo module/endpoint
5. Dùng template api-endpoint.md
6. Tạo tài liệu markdown toàn diện
7. Bao gồm ví dụ curl, JavaScript và Python

Kết quả:
✅ Đã tạo tài liệu API
📄 Các file đã tạo:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Độ bao phủ: 23/23 endpoint đã có tài liệu
```

## Cách Dùng Template

### Template API Endpoint
Dùng để viết tài liệu cho REST API endpoint kèm ví dụ đầy đủ.

### Template Tài Liệu Hàm
Dùng để viết tài liệu cho từng hàm/phương thức.

### Template ADR
Dùng để ghi lại các quyết định kiến trúc.

## Cấu Hình

Thiết lập GitHub token để đồng bộ tài liệu:
```bash
export GITHUB_TOKEN="your_github_token"
```

## Best Practice

- Giữ tài liệu gần với code
- Cập nhật tài liệu cùng với các thay đổi code
- Bao gồm các ví dụ thực tế
- Kiểm tra định kỳ
- Dùng template để đảm bảo tính nhất quán

---

**Cập Nhật Lần Cuối**: Ngày 18 tháng 10 năm 2026
**Phiên Bản Claude Code**: 2.1.302
**Nguồn**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
