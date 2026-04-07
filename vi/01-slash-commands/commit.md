---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: Tạo git commit với bối cảnh
---

## Bối Cảnh

- Trạng thái git hiện tại: !`git status`
- Git diff hiện tại: !`git diff HEAD`
- Nhánh hiện tại: !`git branch --show-current`
- Các commit gần đây: !`git log --oneline -10`

## Nhiệm Vụ Của Bạn

Dựa trên các thay đổi ở trên, tạo một git commit đơn lẻ.

Nếu một thông điệp được cung cấp qua đối số, sử dụng nó: $ARGUMENTS

Nếu không, phân tích các thay đổi và tạo thông điệp commit phù hợp theo định dạng conventional commits:
- `feat:` cho các tính năng mới
- `fix:` cho các sửa lỗi
- `docs:` cho các thay đổi tài liệu
- `refactor:` cho việc refactor code
- `test:` cho việc thêm tests
- `chore:` cho các tác vụ bảo trì
