<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# Nắm vững Claude Code trong vòng một cuối tuần

Từ việc chỉ biết gõ lệnh `claude`, bạn sẽ tiến đến việc điều phối các agent, hooks, skills và MCP server — thông qua các hướng dẫn trực quan, template copy-paste sẵn và lộ trình học có hệ thống.

**[Bắt đầu trong 15 phút](#-bắt-đầu-trong-15-phút)** | **[Xác định trình độ của bạn](#-chưa-biết-bắt-đầu-từ-đâu)** | **[Xem danh mục tính năng](CATALOG.md)**

---

## Mục lục

- [Vấn đề](#vấn-đề)
- [Claude How To giải quyết điều đó như thế nào](#claude-how-to-giải-quyết-điều-đó-như-thế-nào)
- [Cách hoạt động](#cách-hoạt-động)
- [Chưa biết bắt đầu từ đâu?](#-chưa-biết-bắt-đầu-từ-đâu)
- [Bắt đầu trong 15 phút](#-bắt-đầu-trong-15-phút)
- [Bạn có thể xây dựng gì với hướng dẫn này?](#bạn-có-thể-xây-dựng-gì-với-hướng-dẫn-này)
- [Câu hỏi thường gặp](#câu-hỏi-thường-gặp)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)

---

## Vấn đề

Bạn đã cài Claude Code. Bạn đã chạy thử vài lệnh. Và rồi thì sao?

- **Tài liệu chính thức mô tả tính năng — nhưng không chỉ bạn cách kết hợp chúng.** Bạn biết slash commands tồn tại, nhưng không biết cách kết hợp chúng với hooks, memory và subagents thành một workflow thực sự tiết kiệm hàng giờ làm việc.
- **Không có lộ trình học rõ ràng.** Nên học MCP trước hooks không? Skills trước subagents không? Bạn cứ lướt qua mọi thứ mà không thực sự nắm vững điều gì.
- **Ví dụ quá đơn giản.** Một slash command "hello world" không giúp bạn xây dựng được một pipeline code review thực tế — thứ sử dụng memory, giao việc cho các agent chuyên biệt, và tự động chạy quét bảo mật.

Bạn đang bỏ lãng 90% sức mạnh của Claude Code — và bạn không biết mình đang bỏ lỡ gì.

---

## Claude How To giải quyết điều đó như thế nào

Đây không phải một tài liệu tham khảo tính năng thông thường. Đây là **hướng dẫn có cấu trúc, trực quan, học qua ví dụ thực tế** — dạy bạn sử dụng mọi tính năng của Claude Code với các template thực chiến có thể copy vào dự án của bạn ngay hôm nay.

| | Tài liệu chính thức | Hướng dẫn này |
|--|---------------------|---------------|
| **Hình thức** | Tài liệu tham khảo | Hướng dẫn trực quan với sơ đồ Mermaid |
| **Chiều sâu** | Mô tả tính năng | Giải thích cơ chế hoạt động bên trong |
| **Ví dụ** | Đoạn code cơ bản | Template thực chiến dùng được ngay |
| **Cấu trúc** | Phân loại theo tính năng | Lộ trình học tiến dần (từ cơ bản đến nâng cao) |
| **Bắt đầu** | Tự định hướng | Có roadmap hướng dẫn kèm ước tính thời gian |
| **Tự đánh giá** | Không có | Quiz tương tác để xác định điểm yếu và tạo lộ trình cá nhân hóa |

### Bạn nhận được gì:

- **10 module hướng dẫn** bao phủ mọi tính năng của Claude Code — từ slash commands đến đội agent tùy chỉnh
- **Config copy-paste sẵn** — slash commands, CLAUDE.md template, hook scripts, MCP configs, subagent definitions và plugin bundle đầy đủ
- **Sơ đồ Mermaid** minh họa cơ chế hoạt động bên trong từng tính năng, để bạn hiểu *tại sao*, không chỉ *như thế nào*
- **Lộ trình học có hướng dẫn** đưa bạn từ người mới đến power user trong 11–13 giờ
- **Tự đánh giá tích hợp** — chạy `/self-assessment` hoặc `/lesson-quiz hooks` ngay trong Claude Code để xác định điểm còn thiếu

**[Bắt đầu lộ trình học ->](LEARNING-ROADMAP.vi.md)**

---

## Cách hoạt động

### 1. Xác định trình độ của bạn

Làm [bài kiểm tra tự đánh giá](LEARNING-ROADMAP.md#-find-your-level) hoặc chạy `/self-assessment` trong Claude Code. Nhận roadmap cá nhân hóa dựa trên những gì bạn đã biết.

### 2. Theo lộ trình có hướng dẫn

Học lần lượt 10 module theo thứ tự — mỗi module xây dựng trên nền module trước. Copy template trực tiếp vào dự án của bạn trong khi học.

### 3. Kết hợp các tính năng thành workflow

Sức mạnh thực sự nằm ở việc kết hợp các tính năng lại với nhau. Học cách ghép slash commands + memory + subagents + hooks thành những pipeline tự động xử lý code review, triển khai, và tạo tài liệu.

### 4. Kiểm tra mức độ hiểu biết

Chạy `/lesson-quiz [chủ đề]` sau mỗi module. Quiz sẽ chỉ ra chính xác điều bạn còn thiếu để bạn bổ sung nhanh chóng.

**[Bắt đầu trong 15 phút](#-bắt-đầu-trong-15-phút)**

---

## Được tin dùng bởi hơn 3.900 lập trình viên

- **Hơn 3.900 GitHub stars** từ các lập trình viên sử dụng Claude Code hàng ngày
- **Hơn 460 forks** — các team đang tùy chỉnh hướng dẫn này cho workflow riêng của họ
- **Được duy trì tích cực** — đồng bộ với mỗi bản phát hành Claude Code (phiên bản mới nhất: v2.2.0, tháng 3/2026)
- **Được cộng đồng đóng góp** — đến từ các lập trình viên chia sẻ cấu hình thực tế của họ

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## Chưa biết bắt đầu từ đâu?

Làm bài tự đánh giá hoặc chọn theo trình độ:

| Trình độ | Bạn có thể... | Bắt đầu tại | Thời gian |
|----------|--------------|-------------|-----------|
| **Người mới** | Khởi động Claude Code và chat | [Slash Commands](01-slash-commands/README.vi.md) | ~2.5 giờ |
| **Trung cấp** | Dùng CLAUDE.md và custom commands | [Skills](03-skills/README.vi.md) | ~3.5 giờ |
| **Nâng cao** | Cấu hình MCP server và hooks | [Advanced Features](09-advanced-features/README.vi.md) | ~5 giờ |

**Lộ trình đầy đủ với cả 10 module:**

| Thứ tự | Module | Trình độ | Thời gian |
|--------|--------|----------|-----------|
| 1 | [Slash Commands](01-slash-commands/README.vi.md) | Người mới | 30 phút |
| 2 | [Memory](02-memory/README.vi.md) | Người mới+ | 45 phút |
| 3 | [Checkpoints](08-checkpoints/README.vi.md) | Trung cấp | 45 phút |
| 4 | [CLI Basics](10-cli/README.vi.md) | Người mới+ | 30 phút |
| 5 | [Skills](03-skills/README.vi.md) | Trung cấp | 1 giờ |
| 6 | [Hooks](06-hooks/README.vi.md) | Trung cấp | 1 giờ |
| 7 | [MCP](05-mcp/README.vi.md) | Trung cấp+ | 1 giờ |
| 8 | [Subagents](04-subagents/README.vi.md) | Trung cấp+ | 1.5 giờ |
| 9 | [Advanced Features](09-advanced-features/README.vi.md) | Nâng cao | 2–3 giờ |
| 10 | [Plugins](07-plugins/README.vi.md) | Nâng cao | 2 giờ |

**[Lộ trình học đầy đủ ->](LEARNING-ROADMAP.vi.md)**

---

## Bắt đầu trong 15 phút

```bash
# 1. Clone hướng dẫn về máy
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy slash command đầu tiên của bạn
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Thử ngay — trong Claude Code, gõ:
# /optimize

# 4. Muốn thêm? Thiết lập project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. Cài đặt một skill:
cp -r 03-skills/code-review ~/.claude/skills/
```

Muốn thiết lập đầy đủ hơn? Đây là **setup thiết yếu trong 1 giờ**:

```bash
# Slash commands (15 phút)
cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 phút)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Cài một skill (15 phút)
cp -r 03-skills/code-review ~/.claude/skills/

# Mục tiêu cuối tuần: thêm hooks, subagents, MCP và plugins
# Theo lộ trình học để được hướng dẫn từng bước
```

**[Xem hướng dẫn cài đặt đầy đủ](#tham-khảo-nhanh-cài-đặt)**

---

## Bạn có thể xây dựng gì với hướng dẫn này?

| Trường hợp sử dụng | Tính năng bạn sẽ kết hợp |
|--------------------|--------------------------|
| **Code Review tự động** | Slash Commands + Subagents + Memory + MCP |
| **Onboarding nhân viên mới** | Memory + Slash Commands + Plugins |
| **Tự động hóa CI/CD** | CLI Reference + Hooks + Background Tasks |
| **Tạo tài liệu tự động** | Skills + Subagents + Plugins |
| **Kiểm tra bảo mật** | Subagents + Skills + Hooks (chế độ read-only) |
| **Pipeline DevOps** | Plugins + MCP + Hooks + Background Tasks |
| **Tái cấu trúc code phức tạp** | Checkpoints + Planning Mode + Hooks |

---

## Câu hỏi thường gặp

**Có miễn phí không?**
Có. Giấy phép MIT, miễn phí mãi mãi. Dùng cho dự án cá nhân, tại nơi làm việc, trong team — không có hạn chế nào ngoài việc đính kèm thông báo giấy phép.

**Có được duy trì không?**
Có và rất tích cực. Hướng dẫn được đồng bộ với mỗi bản phát hành Claude Code. Phiên bản hiện tại: v2.2.0 (tháng 3/2026), tương thích với Claude Code 2.1+.

**Khác gì so với tài liệu chính thức?**
Tài liệu chính thức là tài liệu tham khảo tính năng. Hướng dẫn này là tutorial kèm sơ đồ, template thực chiến và lộ trình học tiến dần. Hai thứ bổ trợ nhau — học tại đây trước, tra tài liệu chính thức khi cần chi tiết cụ thể.

**Học hết mất bao lâu?**
11–13 giờ cho toàn bộ lộ trình. Nhưng bạn sẽ thấy hiệu quả ngay trong 15 phút — chỉ cần copy một slash command template và thử dùng.

**Có dùng được với Claude Sonnet / Haiku / Opus không?**
Có. Tất cả template đều hoạt động với Claude Sonnet 4.6, Claude Opus 4.6 và Claude Haiku 4.5.

**Có thể đóng góp không?**
Hoàn toàn được. Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết hướng dẫn. Chúng tôi chào đón các ví dụ mới, sửa lỗi, cải thiện tài liệu và template từ cộng đồng.

**Có đọc offline được không?**
Có. Chạy `uv run scripts/build_epub.py` để tạo file EPUB với toàn bộ nội dung và sơ đồ đã được render.

---

## Bắt đầu làm chủ Claude Code ngay hôm nay

Bạn đã cài Claude Code rồi. Điều duy nhất ngăn bạn tăng năng suất gấp 10 lần là biết cách dùng nó đúng cách. Hướng dẫn này cung cấp cho bạn lộ trình có cấu trúc, giải thích trực quan và template copy-paste để đạt được điều đó.

Giấy phép MIT. Miễn phí mãi mãi. Clone về, fork ra, biến nó thành của bạn.

**[Bắt đầu lộ trình học ->](LEARNING-ROADMAP.vi.md)** | **[Xem danh mục tính năng](CATALOG.md)** | **[Bắt đầu trong 15 phút](#-bắt-đầu-trong-15-phút)**

---

<details>
<summary>Điều hướng nhanh — Tất cả tính năng</summary>

| Tính năng | Mô tả | Thư mục |
|-----------|-------|---------|
| **Feature Catalog** | Tham khảo đầy đủ kèm lệnh cài đặt | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | Phím tắt do người dùng gọi | [01-slash-commands/](01-slash-commands/README.vi.md) |
| **Memory** | Bộ nhớ ngữ cảnh lâu dài | [02-memory/](02-memory/README.vi.md) |
| **Skills** | Khả năng tái sử dụng | [03-skills/](03-skills/README.vi.md) |
| **Subagents** | AI assistant chuyên biệt | [04-subagents/](04-subagents/README.vi.md) |
| **MCP Protocol** | Truy cập công cụ bên ngoài | [05-mcp/](05-mcp/README.vi.md) |
| **Hooks** | Tự động hóa theo sự kiện | [06-hooks/](06-hooks/README.vi.md) |
| **Plugins** | Gói tính năng đóng gói sẵn | [07-plugins/](07-plugins/README.vi.md) |
| **Checkpoints** | Snapshot phiên làm việc & tua lại | [08-checkpoints/](08-checkpoints/README.vi.md) |
| **Advanced Features** | Planning, thinking, background tasks | [09-advanced-features/](09-advanced-features/README.vi.md) |
| **CLI Reference** | Lệnh, flags và tùy chọn | [10-cli/](10-cli/README.vi.md) |
| **Blog Posts** | Ví dụ sử dụng thực tế | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>So sánh tính năng</summary>

| Tính năng | Cách gọi | Lưu trữ | Phù hợp nhất cho |
|-----------|----------|---------|-----------------|
| **Slash Commands** | Thủ công (`/cmd`) | Chỉ trong phiên | Phím tắt nhanh |
| **Memory** | Tự động tải | Xuyên phiên | Học dài hạn |
| **Skills** | Tự động kích hoạt | Filesystem | Workflow tự động |
| **Subagents** | Tự động ủy quyền | Context riêng biệt | Phân công nhiệm vụ |
| **MCP Protocol** | Tự động truy vấn | Thời gian thực | Truy cập dữ liệu live |
| **Hooks** | Kích hoạt theo sự kiện | Đã cấu hình | Tự động hóa & kiểm tra |
| **Plugins** | Một lệnh | Tất cả tính năng | Giải pháp hoàn chỉnh |
| **Checkpoints** | Thủ công/Tự động | Theo phiên | Thử nghiệm an toàn |
| **Planning Mode** | Thủ công/Tự động | Giai đoạn lập kế hoạch | Triển khai phức tạp |
| **Background Tasks** | Thủ công | Thời gian task | Tác vụ chạy dài |
| **CLI Reference** | Lệnh terminal | Phiên/Script | Tự động hóa & scripting |

</details>

<details>
<summary>Tham khảo nhanh cài đặt</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (tự động bật, cấu hình trong settings)
# Xem 08-checkpoints/README.md

# Advanced Features (cấu hình trong settings)
# Xem 09-advanced-features/config-examples.json

# CLI Reference (không cần cài đặt)
# Xem 10-cli/README.md để biết ví dụ sử dụng
```

</details>

---

> **Ghi chú cho bản dịch tiếng Việt:** File này được dịch bởi cộng đồng. Nếu bạn thấy điểm nào chưa chính xác hoặc muốn cải thiện, vui lòng mở Pull Request. Bản gốc tiếng Anh luôn là nguồn chính xác nhất: [README.md](README.md).
