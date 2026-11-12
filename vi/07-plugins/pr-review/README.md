<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin PR Review

Workflow review PR hoàn chỉnh với các kiểm tra bảo mật, testing và tài liệu.

## Tính Năng

✅ Phân tích bảo mật
✅ Kiểm tra độ bao phủ test
✅ Xác minh tài liệu
✅ Đánh giá chất lượng code
✅ Phân tích tác động đến hiệu năng

## Cài Đặt

```bash
claude --plugin-dir ./07-plugins/pr-review
```

Kiểm tra plugin trước khi tải:

```bash
claude plugin validate ./07-plugins/pr-review
```

## Những Gì Được Bao Gồm

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### Lệnh Slash

Lệnh của plugin được đặt namespace theo `name` của plugin trong `plugin.json`:

- `/pr-review:review-pr` - Review PR toàn diện
- `/pr-review:check-security` - Review tập trung vào bảo mật
- `/pr-review:check-tests` - Phân tích độ bao phủ test

### Tác Nhân Con
- `security-reviewer` - Phát hiện lỗ hổng bảo mật
- `test-checker` - Phân tích độ bao phủ test
- `performance-analyzer` - Đánh giá tác động đến hiệu năng

### MCP Server

`.mcp.json` khai báo một server, `github`: MCP server chính thức của GitHub (`ghcr.io/github/github-mcp-server`), chạy bằng Docker ở chế độ chỉ đọc. Server này hiển thị là `plugin:pr-review:github` trong `/mcp`.

### Hook

`hooks/hooks.json` đăng ký `pre-review.js` cho sự kiện `UserPromptExpansion`, với matcher khớp ba lệnh ở trên. Khi bạn gõ một trong các lệnh đó, hook sẽ:

- chặn lệnh (exit code 2) khi thư mục hiện tại không phải là git repository
- nếu không, thêm nhánh hiện tại, kèm ghi chú về các thay đổi chưa commit, vào ngữ cảnh của Claude

## Cách Sử Dụng

### Review PR Cơ Bản
```text
/pr-review:review-pr
```

### Chỉ Kiểm Tra Bảo Mật
```text
/pr-review:check-security
```

### Kiểm Tra Độ Bao Phủ Test
```text
/pr-review:check-tests
```

## Yêu Cầu

- Claude Code 2.1+
- Node.js (chạy script hook)
- Docker (chạy GitHub MCP server)
- Một GitHub personal access token
- Kho chứa Git

## Cấu Hình

Thiết lập GitHub token của bạn trước khi khởi động Claude Code:
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` truyền token này cho server dưới tên `GITHUB_PERSONAL_ACCESS_TOKEN`, biến mà server đọc. Chạy `/mcp` để kiểm tra `plugin:pr-review:github` đã kết nối.

## Ví Dụ Workflow

```text
User: /pr-review:review-pr

Claude:
1. Hook pre-review kiểm tra git repository và thêm nhánh vào ngữ cảnh
2. Lấy dữ liệu PR qua GitHub MCP
3. Giao việc review bảo mật cho tác nhân con security-reviewer
4. Giao việc testing cho tác nhân con test-checker
5. Giao việc hiệu năng cho tác nhân con performance-analyzer
6. Tổng hợp tất cả các phát hiện
7. Cung cấp báo cáo review toàn diện

Kết quả:
✅ Bảo mật: Không phát hiện vấn đề nghiêm trọng
⚠️  Testing: Coverage là 65%, khuyến nghị 80%+
✅ Hiệu năng: Không có tác động đáng kể
📝 Đề xuất: Bổ sung test cho các edge case
```

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
**Các Mô Hình Tương Thích**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
