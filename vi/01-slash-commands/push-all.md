---
description: Stage tất cả thay đổi, tạo commit, và push đến remote (sử dụng thận trọng)
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# Commit và Push Tất Cả

⚠️ **CẢNH BÁO**: Stage TẤT CẢ thay đổi, commit, và push đến remote. Chỉ sử dụng khi tin rằng tất cả thay đổi thuộc về nhau.

## Quy Trình

### 1. Phân Tích Thay Đổi
Chạy song song:
- `git status` - Hiển thị các file đã được sửa/thêm/xóa/chưa được theo dõi
- `git diff --stat` - Hiển thị thống kê thay đổi
- `git log -1 --oneline` - Hiển thị commit gần đây cho kiểu thông điệp

### 2. Kiểm Tra An Toàn

**❌ DỪNG LẠI và CẢNH BÁO nếu phát hiện:**
- Bí mật: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- API Keys: Bất kỳ biến `*_API_KEY`, `*_SECRET`, `*_TOKEN` nào có giá trị thực (không phải placeholder như `your-api-key`, `xxx`, `placeholder`)
- Files lớn: `>10MB` mà không có Git LFS
- Build artifacts: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- Files tạm: `.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**Xác Thực API Key:**
Kiểm tra các file đã sửa đổi cho các mẫu như:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ Phát hiện khóa thật!
AWS_SECRET_KEY=AKIA...         # ❌ Phát hiện khóa thật!
STRIPE_API_KEY=sk_live_...    # ❌ Phát hiện khóa thật!

# ✅ Placeholder chấp nhận được:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ Xác minh:**
- `.gitignore` được cấu hình đúng
- Không có xung đột merge
- Nhánh đúng (cảnh báo nếu main/master)
- API keys chỉ là placeholder

### 3. Yêu Cầu Xác Nhận

Trình bày tóm tắt:
```
📊 Tóm Tắt Thay Đổi:
- X file đã sửa, Y thêm, Z xóa
- Tổng: +AAA chèn, -BBB xóa

🔒 An toàn: ✅ Không có bí mật | ✅ Không có file lớn | ⚠️ [cảnh báo]
🌿 Nhánh: [name] → origin/[name]

Tôi sẽ: git add . → commit → push

Gõ 'yes' để tiếp tục hoặc 'no' để hủy.
```

**CHỜ "yes" rõ ràng trước khi tiếp tục.**

### 4. Thực Thi (Sau Khi Xác Nhận)

Chạy tuần tự:
```bash
git add .
git status  # Xác minh staging
```

### 5. Tạo Thông Điệp Commit

Phân tích các thay đổi và tạo commit theo quy ước:

**Định dạng:**
```
[type]: Tóm tắt ngắn (tối đa 72 ký tự)

- Thay đổi chính 1
- Thay đổi chính 2
- Thay đổi chính 3
```

**Các loại:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**Ví dụ:**
```
docs: Cập nhật các file README concept với tài liệu toàn diện

- Thêm sơ đồ kiến trúc và bảng
- Bao gồm các ví dụ thực tế
- Mở rộng các phần thực hành tốt nhất
```

### 6. Commit và Push

```bash
git commit -m "$(cat <<'EOF'
[Thông điệp commit được tạo]
EOF
)"
git push  # Nếu thất bại: git pull --rebase && git push
git log -1 --oneline --decorate  # Xác minh
```

### 7. Xác Nhận Thành Công

```
✅ Đã push thành công đến remote!

Commit: [hash] [message]
Nhánh: [branch] → origin/[branch]
Files đã thay đổi: X (+chèn, -xóa)
```

## Xử Lý Lỗi

- **git add thất bại**: Kiểm tra quyền, files bị khóa, xác minh repo được khởi tạo
- **git commit thất bại**: Sửa các pre-commit hooks, kiểm tra cấu hình git (user.name/email)
- **git push thất bại**:
  - Non-fast-forward: `git pull --rebase && git push`
  - Không có nhánh remote: `git push -u origin [branch]`
  - Nhánh được bảo vệ: Sử dụng workflow PR thay thế

## Khi Nào Sử Dụng

✅ **Tốt:**
- Các cập nhật tài liệu đa file
- Tính năng với tests và docs
- Sửa lỗi trên nhiều file
- Định dạng/refactoring toàn dự án
- Thay đổi cấu hình

❌ **Tránh:**
- Không chắc những gì đang được commit
- Chứa bí mật/dữ liệu nhạy cảm
- Các nhánh được bảo vệ mà không có review
- Có xung đột merge
- Muốn lịch sử commit chi tiết
- Pre-commit hooks đang thất bại

## Các Giải Pháp Thay Thế

Nếu người dùng muốn kiểm soát, đề xuất:
1. **Staging có chọn lọc**: Review/stage các file cụ thể
2. **Staging tương tác**: `git add -p` để chọn patch
3. **Workflow PR**: Tạo nhánh → push → PR (sử dụng lệnh `/pr`)

**⚠️ Nhớ**: Luôn review các thay đổi trước khi push. Khi nghi ngờ, sử dụng các lệnh git riêng lẻ để kiểm soát nhiều hơn.
