---
description: Dọn dẹp code, stage changes, và chuẩn bị pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Danh Sách Kiểm Tra Chuẩn Bị Pull Request

Trước khi tạo PR, thực hiện các bước này:

1. Chạy linting: `prettier --write .`
2. Chạy tests: `npm test`
3. Review git diff: `git diff HEAD`
4. Stage changes: `git add .`
5. Tạo thông điệp commit theo conventional commits:
   - `fix:` cho sửa lỗi
   - `feat:` cho tính năng mới
   - `docs:` cho tài liệu
   - `refactor:` cho tái cấu trúc code
   - `test:` cho việc thêm tests
   - `chore:` cho bảo trì

6. Tạo tóm tắt PR bao gồm:
   - Những gì đã thay đổi
   - Tại sao nó thay đổi
   - Testing đã thực hiện
   - Tác động tiềm ẩn
