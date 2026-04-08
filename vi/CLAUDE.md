# CLAUDE.md

File này cung cấp hướng dẫn cho Claude Code (claude.ai/code) khi làm việc với code trong repository này.

## Tổng Quan Dự Án

Claude How To là một repository tutorial về các tính năng của Claude Code. Đây là **documentation-as-code** — sản phẩm chính là các file markdown được tổ chức thành các module học tập đánh số (01-10), không phải một ứng dụng thực thi.

**Kiến trúc**: Mỗi module (01-10) bao phủ một tính năng cụ thể của Claude Code với các template copy-paste, sơ đồ Mermaid, và ví dụ. Hệ thống build xác thực chất lượng documentation và tạo ebook EPUB.

## Các Lệnh Thường Dùng

### Kiểm Tra Chất Lượng Pre-commit

Tất cả documentation phải vượt qua bốn kiểm tra chất lượng trước khi commit (các kiểm tra này chạy tự động qua pre-commit hooks):

```bash
# Cài đặt pre-commit hooks (chạy trên mỗi commit)
pre-commit install

# Chạy tất cả các kiểm tra thủ công
pre-commit run --all-files
```

Bốn kiểm tra là:
1. **markdown-lint** — Cấu trúc và định dạng Markdown qua `markdownlint`
2. **cross-references** — Liên kết nội bộ, anchors, cú pháp code fence (Python script)
3. **mermaid-syntax** — Xác thực tất cả sơ đồ Mermaid parse đúng (Python script)
4. **link-check** — Các URL bên ngoài có thể truy cập được (Python script)
5. **build-epub** — EPUB tạo ra không có lỗi (khi có thay đổi `.md`)

### Thiết Lập Môi Trường Phát Triển

```bash
# Cài đặt uv (Python package manager)
pip install uv

# Tạo virtual environment và cài đặt Python dependencies
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Cài đặt Node.js tools (markdown linter và Mermaid validator)
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli

# Cài đặt pre-commit hooks
uv pip install pre-commit
pre-commit install
```

### Testing

Các script Python trong `scripts/` có unit tests:

```bash
# Chạy tất cả tests
pytest scripts/tests/ -v

# Chạy với coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Chạy test cụ thể
pytest scripts/tests/test_build_epub.py -v
```

### Chất Lượng Code

```bash
# Lint và format Python code
ruff check scripts/
ruff format scripts/

# Security scan
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# Type checking
mypy scripts/ --ignore-missing-imports
```

### Build EPUB

```bash
# Tạo ebook (render Mermaid diagrams qua Kroki.io API)
uv run scripts/build_epub.py

# Với các tùy chọn
uv run scripts/build_epub.py --verbose --output custom-name.epub --max-concurrent 5
```

## Cấu Trúc Thư Mục

```
├── 01-slash-commands/      # Các lối tắt do người dùng gọi
├── 02-memory/              # Ví dụ về bối cảnh liên tục
├── 03-skills/              # Các khả năng có thể tái sử dụng
├── 04-subagents/           # Các tác nhân AI chuyên dụng
├── 05-mcp/                 # Ví dụ Model Context Protocol
├── 06-hooks/              # Tự động hóa dựa trên sự kiện
├── 07-plugins/             # Các tính năng được đóng gói
├── 08-checkpoints/         # Các snapshot của phiên
├── 09-advanced-features/   # Lập kế hoạch, suy nghĩ, background tasks
├── 10-cli/                 # Tham chiếu CLI
├── scripts/
│   ├── build_epub.py           # EPUB generator (render Mermaid qua Kroki API)
│   ├── check_cross_references.py   # Xác thực liên kết nội bộ
│   ├── check_links.py          # Kiểm tra các URL bên ngoài
│   ├── check_mermaid.py        # Xác thực cú pháp Mermaid
│   └── tests/                  # Unit tests cho scripts
├── .pre-commit-config.yaml    # Định nghĩa các kiểm tra chất lượng
└── README.md               # Hướng dẫn chính (cũng là index của module)
```

## Hướng Dẫn Nội Dung

### Cấu Trúc Module

Mỗi thư mục đánh số tuân theo pattern:
- **README.md** — Tổng quan về tính năng với các ví dụ
- **Các file ví dụ** — Template copy-paste (`.md` cho commands, `.json` cho configs, `.sh` cho hooks)
- Các file được tổ chức theo độ phức tạp của tính năng và dependencies

### Sơ Đồ Mermaid
- Tất cả sơ đồ phải parse thành công (được kiểm tra bởi pre-commit hook)
- EPUB build render sơ đồ qua Kroki.io API (cần internet)
- Sử dụng Mermaid cho flowcharts, sequence diagrams, và architecture visuals

### Cross-References
- Sử dụng relative paths cho internal links (ví dụ: `(01-slash-commands/README.md)`)
- Code fences phải chỉ định ngôn ngữ (ví dụ: ` ```bash `, ` ```python `)
- Anchor links sử dụng format `#heading-name`

### Link Validation
- Các URL bên ngoài phải có thể truy cập được (được kiểm tra bởi pre-commit hook)
- Tránh link đến nội dung tạm thời
- Sử dụng permalinks nếu có thể

## Các Điểm Kiến Trúc Quan Trọng

1. **Các thư mục đánh số thể hiện thứ tự học tập** — Prefix 01-10 thể hiện thứ tự được khuyến nghị để học các tính năng của Claude Code. Đánh số này có chủ đích; không tổ chức lại theo bảng chữ cái.

2. **Scripts là các tiện ích, không phải sản phẩm** — Các script Python trong `scripts/` hỗ trợ chất lượng documentation và tạo EPUB. Nội dung thực tế nằm trong các thư mục module đánh số.

3. **Pre-commit là người gác cổng** — Tất cả bốn kiểm tra chất lượng phải pass trước khi PR được chấp nhận. CI pipeline chạy các kiểm tra tương tự như lần thứ hai.

4. **Mermaid rendering cần network** — EPUB build gọi Kroki.io API để render diagrams. Các lỗi build ở đây thường là vấn đề network hoặc cú pháp Mermaid không hợp lệ.

5. **Đây là tutorial, không phải thư viện** — Khi thêm nội dung, tập trung vào giải thích rõ ràng, ví dụ copy-paste, và sơ đồ trực quan. Giá trị nằm ở việc dạy các khái niệm, không cung cấp code có thể tái sử dụng.

## Commit Conventions

Tuân theo format conventional commit:
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`
- `refactor(hooks): Simplify hook configuration examples`

Scope nên khớp với tên thư mục khi áp dụng.
