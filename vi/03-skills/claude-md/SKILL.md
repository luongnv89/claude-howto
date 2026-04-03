---
name: claude-md
description: Tạo hoặc cập nhật các file CLAUDE.md theo các thực hành tốt nhất để onboarding tác nhân AI tối ưu
---

## Đầu Vào Người Dùng

```text
$ARGUMENTS
```

Bạn **BẮT BUỘC** phải xem xét đầu vào của người dùng trước khi tiếp tục (nếu không trống). Người dùng có thể chỉ định:
- `create` - Tạo CLAUDE.md mới từ đầu
- `update` - Cải thiện CLAUDE.md hiện có
- `audit` - Phân tích và báo cáo về chất lượng CLAUDE.md hiện tại
- Một đường dẫn cụ thể để tạo/cập nhật (ví dụ: `src/api/CLAUDE.md` cho hướng dẫn cụ thể thư mục)

## Nguyên Tắc Cốt Lõi

**LLMs là không trạng thái**: CLAUDE.md là file duy nhất được bao gồm tự động trong mọi cuộc hội thoại. Nó phục vụ như tài liệu onboarding chính cho các tác nhân AI vào codebase của bạn.

### Các Quy Tắc Vàng

1. **Less is More**: Các LLM biên giới có thể theo ~150-200 hướng dẫn. System prompt của Claude Code đã sử dụng ~50. Giữ CLAUDE.md của bạn tập trung và ngắn gọn.

2. **Ứng Dụng Phổ Biến**: Chỉ bao gồm thông tin liên quan đến MỌI phiên. Hướng dẫn cụ thể theo tác vụ thuộc về các file riêng.

3. **Đừng Sử Dụng Claude như Linter**: Hướng dẫn phong cách làm phình bối cảnh và làm giảm khả năng tuân theo hướng dẫn. Sử dụng các công cụ xác định (prettier, eslint, v.v.) thay thế.

4. **Không Bao Giờ Tự Động Tạo**: CLAUDE.md là điểm đòn bẩy cao nhất của hệ thống AI. Tạo nó thủ công với sự xem xét cẩn thận.

## Quy Trình Thực Thi

### 1. Phân Tích Dự Án

Đầu tiên, phân tích trạng thái dự án hiện tại:

1. Kiểm tra các file CLAUDE.md hiện có:
   - Cấp root: `./CLAUDE.md` hoặc `.claude/CLAUDE.md`
   - Cụ thể thư mục: `**/CLAUDE.md`
   - Cấu hình người dùng toàn cầu: `~/.claude/CLAUDE.md`

2. Xác định cấu trúc dự án:
   - Technology stack (ngôn ngữ, frameworks)
   - Loại dự án (monorepo, ứng dụng đơn, library)
   - Công cụ phát triển (quản lý package, hệ thống build, trình chạy test)

3. Xem lại tài liệu hiện có:
   - README.md
   - CONTRIBUTING.md
   - package.json, pyproject.toml, Cargo.toml, v.v.

### 2. Chiến Lược Nội Dung (WHAT, WHY, HOW)

Cấu trúc CLAUDE.md xung quanh ba chiều:

#### WHAT - Công Nghệ & Cấu Trúc
- Tổng quan technology stack
- Tổ chức dự án (đặc biệt quan trọng cho monorepos)
- Các thư mục chính và mục đích của chúng

#### WHY - Mục Đích & Bối Cảnh
- Dự án làm gì
- Tại sao các quyết định kiến trúc nhất định được đưa ra
- Mỗi thành phần chính chịu trách nhiệm cho gì

#### HOW - Workflow & Quy Ước
- Workflow phát triển (bun vs node, pip vs uv, v.v.)
- Thủ tục và lệnh testing
- Phương pháp xác minh và build
- Các "gotchas" quan trọng hoặc yêu cầu không rõ ràng

### 3. Chiến Lược Progressive Disclosure

Đối với các dự án lớn, khuyến nghị tạo thư mục `agent_docs/`:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

Trong CLAUDE.md, tham khảo các file này với các hướng dẫn như:
```markdown
Để có hướng dẫn build chi tiết, tham khảo `agent_docs/building_the_project.md`
```

**Quan Trọng**: Sử dụng các tham chiếu `file:line` thay vì các đoạn code để tránh bối cảnh lỗi thời.

### 4. Ràng Buộc Chất Lượng

Khi tạo hoặc cập nhật CLAUDE.md:

1. **Độ Dài Mục Tiêu**: Dưới 300 dòng (lý tưởng dưới 100)
2. **Không Quy Tắc Phong Cách**: Loại bỏ bất kỳ hướng dẫn linting/formatting nào
3. **Không Hướng Dẫn Cụ Theo Tác Vụ**: Di chuyển sang các file riêng
4. **Không Đoạn Code**: Sử dụng tham chiếu file thay thế
5. **Không Thông Tin Dư Thừa**: Đừng lặp lại những gì trong package.json hoặc README

### 5. Các Phần Thiết Yếu

Một CLAUDE.md được cấu trúc tốt nên bao gồm:

```markdown
# Tên Dự Án

Mô tả ngắn một dòng.

## Tech Stack
- Ngôn ngữ chính và phiên bản
- Frameworks/thư viện chính
- Database/lưu trữ (nếu có)

## Cấu Trúc Dự Án
[Chỉ cho monorepos hoặc cấu trúc phức tạp]
- `apps/` - Điểm vào ứng dụng
- `packages/` - Thư viện được chia sẻ

## Lệnh Phát Triển
- Install: `command`
- Test: `command`
- Build: `command`

## Quy Ước Quan Trọng
[Chỉ các quy ước không rõ ràng, tác động cao]
- Quy ước 1 với giải thích ngắn
- Quy ước 2 với giải thích ngắn

## Vấn Đế Đã Biết / Gotchas
[Những gì luôn làm các nhà phát triển vấp phải]
- Vấn đề 1
- Vấn đề 2
```

### 6. Các Anti-Patterns Cần Tránh

**KHÔNG bao gồm:**
- Hướng dẫn phong cách code (sử dụng linters)
- Tài liệu về cách sử dụng Claude
- Giải thích dài về các mẫu rõ ràng
- Các ví dụ code copy-paste
- Thực hành tốt chung ("viết code sạch")
- Hướng dẫn cho các tác vụ cụ thể
- Nội dung được tạo tự động
- Danh sách TODO mở rộng

### 7. Checklist Xác Minh

Trước khi hoàn thành, xác minh:

- [ ] Dưới 300 dòng (lý tưởng dưới 100)
- [ ] Mọi dòng áp dụng cho TẤT CẢ các phiên
- [ ] Không quy tắc phong cách/formatting
- [ ] Không đoạn code (sử dụng tham chiếu file)
- [ ] Các lệnh được xác minh hoạt động
- [ ] Progressive disclosure được sử dụng cho các dự án phức tạp
- [ ] Các gotchas quan trọng được tài liệu hóa
- [ ] Không dư thừa với README.md

## Định Dạng Đầu Ra

### Cho `create` hoặc mặc định:

1. Phân tích dự án
2. Soạn thảo CLAUDE.md theo cấu trúc ở trên
3. Trình bày bản nháp để xem xét
4. Ghi vào vị trí phù hợp sau khi được chấp thuận

### Cho `update`:

1. Đọc CLAUDE.md hiện có
2. Kiểm tra theo các thực hành tốt nhất
3. Xác định:
   - Nội dung để loại bỏ (quy tắc phong cách, đoạn code, cụ thể tác vụ)
   - Nội dung để cô đọng
   - Thông tin thiết bị còn thiếu
4. Trình bày các thay đổi để xem xét
5. Áp dụng các thay đổi sau khi được chấp thuận

### Cho `audit`:

1. Đọc CLAUDE.md hiện có
2. Tạo một báo cáo với:
   - Số dòng hiện tại vs mục tiêu
   - Phần trăm nội dung áp dụng phổ biến
   - Danh sách các anti-patterns được tìm thấy
   - Khuyến nghị cải thiện
3. KHÔNG chỉnh sửa file, chỉ báo cáo

## Xử Lý AGENTS.md

Nếu người dùng yêu cầu tạo/cập nhật AGENTS.md:

AGENTS.md được sử dụng để định nghĩa các hành vi tác nhân chuyên biệt. Không giống CLAUDE.md (dành cho bối cảnh dự án), AGENTS.md định nghĩa:
- Các vai trò và khả năng tác nhân tùy chỉnh
- Hướng dẫn và ràng buộc cụ thể tác nhân
- Định nghĩa workflow cho các kịch bản đa tác nhân

Áp dụng các nguyên tắc tương tự:
- Giữ tập trung và ngắn gọn
- Sử dụng progressive disclosure
- Tham khảo tài liệu bên ngoài thay vì nhúng nội dung

## Ghi Chú

- Luôn xác minh các lệnh hoạt động trước khi bao gồm chúng
- Khi nghi ngờ, hãy loại bỏ - less is more
- Lời nhắc hệ thống cho Claude biết rằng CLAUDE.md "có thể hoặc có thể không liên quan" - càng nhiều tiếng ồn, càng bị bỏ qua
- Monorepos hưởng lợi nhất từ cấu trúc WHAT/WHY/HOW rõ ràng
- Các file CLAUDE.md cụ thể thư mục nên được tập trung hơn nữa
