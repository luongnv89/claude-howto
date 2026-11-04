# Changelog

## v2.3.0 — 2026-04-07

### Tính Năng / Features

- Xây dựng và xuất bản các tạo tác EPUB cho mỗi ngôn ngữ (90e9c30) @Thiên Toán
- Thêm hook pre-tool-check.sh bị thiếu vào 06-hooks (b511ed1) @JiayuWang
- Thêm bản dịch tiếng Trung vào thư mục zh/ (89e89d4) @Luong NGUYEN
- Thêm subagent tối ưu hóa hiệu suất và hook kiểm tra phụ thuộc (f53d080) @qk

### Sửa Lỗi / Bug Fixes

- Khả năng tương thích Windows Git Bash + giao thức stdin JSON (2cbb10c) @Luong NGUYEN
- Sửa tài liệu cấu hình autoCheckpoint trong 08-checkpoints (749c79f) @JiayuWang
- Nhúng hình ảnh SVG thay vì thay thế bằng placeholder (1b16709) @Thiên Toán
- Sửa hiển thị hàng rào code lồng nhau trong README bộ nhớ (ce24423) @Zhaoshan Duan
- Áp dụng các sửa chữa từ đánh giá bị loại bỏ bởi squash merge (34259ca) @Luong NGUYEN
- Làm cho các tập lệnh hook tương thích với Windows Git Bash và sử dụng giao thức stdin JSON (107153d) @binyu li

### Tài Liệu / Documentation

- Đồng bộ tất cả các hướng dẫn với các tài liệu Claude Code mới nhất (Tháng 4 2026) (72d3b01) @Luong NGUYEN
- Thêm liên kết ngôn ngữ tiếng Trung vào bộ chuyển đổi ngôn ngữ (6cbaa4d) @Luong NGUYEN
- Thêm bộ chuyển đổi ngôn ngữ giữa tiếng Anh và tiếng Việt (100c45e) @Luong NGUYEN
- Thêm huy hiệu GitHub #1 Trending (0ca8c37) @Luong NGUYEN
- Giới thiệu cc-context-stats để giám sát vùng ngữ cảnh (d41b335) @Luong NGUYEN
- Giới thiệu bộ sưu tập luongnv89/skills và trình quản lý kỹ năng luongnv89/asm (7e3c0b6) @Luong NGUYEN
- Cập nhật thống kê README để phản ánh các số liệu GitHub hiện tại (5,900+ stars, 690+ forks) (5001525) @Luong NGUYEN
- Cập nhật thống kê README để phản ánh các số liệu GitHub hiện tại (3,900+ stars, 460+ forks) (9cb92d6) @Luong NGUYEN

### Tái cấu trúc / Refactoring

- Thay thế phụ thuộc Kroki HTTP bằng hiển thị mmdc cục bộ (e76bbe4) @Luong NGUYEN
- Chuyển các kiểm tra chất lượng sang pre-commit, CI làm đường chuyền thứ hai (6d1e0ae) @Luong NGUYEN
- Thu hẹp đường cơ sở quyền tự động (2790fb2) @Luong NGUYEN
- Thay thế hook tự động thích ứng bằng tập lệnh thiết lập quyền một lần (995a5d6) @Luong NGUYEN

### Khác / Other

- Chuyển các cổng chất lượng sang trái — thêm mypy vào pre-commit, sửa các lỗi CI (699fb39) @Luong NGUYEN
- Thêm bản địa hóa tiếng Việt (Tiếng Việt) (a70777e) @Thiên Toán

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

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

- Cập nhật các URL bị hỏng, các tính năng lỗi thời, và các tham khảo cũ (8fe4520) @luongnv89
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
