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

## Những Gì Được Bao Gồm

### Lệnh Slash
- `/review-pr` - Review PR toàn diện
- `/check-security` - Review tập trung vào bảo mật
- `/check-tests` - Phân tích độ bao phủ test

### Tác Nhân Con
- `security-reviewer` - Phát hiện lỗ hổng bảo mật
- `test-checker` - Phân tích độ bao phủ test
- `performance-analyzer` - Đánh giá tác động đến hiệu năng

### MCP Server
- Tích hợp GitHub để lấy dữ liệu PR

### Hook
- `pre-review.js` - Xác thực trước khi review

## Cách Sử Dụng

### Review PR Cơ Bản
```
/review-pr
```

### Chỉ Kiểm Tra Bảo Mật
```
/check-security
```

### Kiểm Tra Độ Bao Phủ Test
```
/check-tests
```

## Yêu Cầu

- Claude Code 2.1+
- Quyền truy cập GitHub
- Kho chứa Git

## Cấu Hình

Thiết lập GitHub token của bạn:
```bash
export GITHUB_TOKEN="your_github_token"
```

## Ví Dụ Workflow

```
User: /review-pr

Claude:
1. Chạy hook pre-review (xác thực git repo)
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
