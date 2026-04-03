# Changelog

## v2.2.0 — 2026-03-26

### Tài Liệu / Documentation

- Đồng bộ tất cả các hướng dẫn và tham khảo với Claude Code v2.1.84 (f78c094) @luongnv89
  - Cập nhật slash commands thành 55+ built-in + 5 bundled skills, đánh dấu 3 deprecated
  - Mở rộng các sự kiện hook từ 18 lên 25, thêm loại hook `agent` (bây giờ 4 loại)
  - Thêm Auto Mode, Channels, Voice Dictation vào tính năng nâng cao
  - Thêm `effort`, `shell` skill frontmatter fields; `initialPrompt`, `disallowedTools` agent fields
  - Thêm WebSocket MCP transport, elicitation, giới hạn 2KB tool
  - Thêm hỗ trợ LSP plugin, `userConfig`, `${CLAUDE_PLUGIN_DATA}`
  - Cập nhật tất cả tài liệu tham khảo (CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX)
  - Viết lại README như hướng dẫn có cấu trúc landing-page (32a0776) @luongnv89

### Sửa Lỗi / Bug Fixes

- Thêm các từ cSpell bị thiếu và các phần README bị thiếu cho tuân thủ CI (93f9d51) @luongnv89
- Thêm `Sandboxing` vào từ điển cSpell (b80ce6f) @luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Sửa Lỗi / Bug Fixes

- Xóa link marketplace chết gây thất bại kiểm tra link CI (3fdf0d6) @luongnv89
- Thêm `sandboxed` và `pycache` vào từ điển cSpell (dc64618) @luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Tính Năng / Features

- Thêm đường dẫn học tập thích ứng với self-assessment và kỹ năng quiz bài học (1ef46cd) @luongnv89
  - `/self-assessment` — quiz trình độ tương tác trên 10 lĩnh vực tính năng với đường dẫn học tập được cá nhân hóa
  - `/lesson-quiz [lesson]` — kiểm tra kiến thức mỗi bài học với 8-10 câu hỏi được nhắm mục tiêu

### Sửa Lỗi / Bug Fixes

- Cập nhật các URL bị hỏ, các tính năng lỗi thời, và các tham khảo cũ (8fe4520) @luongnv89
- Sửa các liên kết bị hỏng trong resources và kỹ năng self-assessment (7a05863) @luongnv89
- Sử dụng hàng rào cho các khối code lồng nhau trong hướng dẫn khái niệm (5f82719) @VikalpP
- Thêm các từ còn thiếu vào từ điển cSpell (8df7572) @luongnv89

### Tài Liệu / Documentation

- Giai đoạn 5 QA — sửa nhất quán, URLs, và thuật ngữ trên các tài liệu (00bbe4c) @luongnv89
- Hoàn thành Giai đoạn 3-4 — phạm vi tính năng mới và cập nhật tài liệu tham khảo (132de29) @luongnv89
- Thêm runtime MCPorter vào phần context bloat MCP (ef52705) @luongnv89
- Thêm các lệnh, tính năng, và settings bị thiếu qua 6 hướng dẫn (4bc8f15) @luongnv89
- Thêm hướng dẫn style dựa trên các quy ước repo hiện có (84141d0) @luongnv89
- Thêm hàng self-assessment vào bảng so sánh hướng dẫn (8fe0c96) @luongnv89
- Thêm VikalpP vào danh sách người đóng góp cho PR #7 (d5b4350) @luongnv89
- Thêm các tham khảo self-assessment và lesson-quiz skill vào README và roadmap (d5a6106) @luongnv89

### Người Đóng Góp Mới / New Contributors

- @VikalpP đã thực hiện đóng góp đầu tiên của họ trong #7

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Tính Năng / Features

- Đồng bộ tất cả tài liệu với các tính năng Claude Code tháng 2 năm 2026 (487c96d)
  - Cập nhật 26 files trên tất cả 10 thư mục hướng dẫn và 7 tài liệu tham khảo
  - Thêm tài liệu cho **Auto Memory** — các bài học liên tục cho mỗi dự án
  - Thêm tài liệu cho **Remote Control**, **Web Sessions**, và **Desktop App**
  - Thêm tài liệu cho **Agent Teams** (hợp tác đa tác nhân thực nghiệm)
  - Thêm tài liệu cho **MCP OAuth 2.0**, **Tool Search**, và **Claude.ai Connectors**
