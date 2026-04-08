# Clean Code Rules for AI Code Generation
# Quy Tắc Viết Code Sạch cho AI Tạo Code

Các quy tắc này hướng dẫn việc tạo code để tạo ra code có thể bảo trì, chất lượng professional.

## Đặt Tên Có Ý Nghĩa / Meaningful Names
- Sử dụng tên tiết lộ ý định giải thích tại sao một thứ tồn tại
- Tránh disinformation và các phân biệt vô nghĩa (ví dụ: `data`, `info`, `manager`)
- Sử dụng tên có thể phát âm và tìm kiếm được
- Tên Class: danh từ (ví dụ: `UserAccount`, `PaymentProcessor`)
- Tên Method: động từ (ví dụ: `calculateTotal`, `sendEmail`)
- Tránh mental mapping và encodings (Hungarian notation, prefixes)

## Functions / Hàm
- Giữ functions nhỏ (< 20 dòng là lý tưởng)
- Làm một việc duy nhất - Nguyên tắc Đơn Trách Nhiệm
- Một level của abstraction per function
- Giới hạn arguments: 0-2 là lý tưởng, 3 tối đa, tránh flag arguments
- Không side effects - function nên làm điều tên nó nói
- Tách commands (thay đổi state) khỏi queries (trả về info)
- Ưu tiên exceptions hơn error codes

## Comments / Comments
- Code nên tự giải thích - tránh comments khi có thể
- Comments tốt: thông tin pháp lý, cảnh báo, TODOs, tài liệu public API
- Comments xấu: redundant, misleading, hoặc giải thích bad code
- Không comment out code - xóa nó (version control preserves history)
- Nếu bạn cần một comment, cân nhắc refactoring code thay thế

## Formatting
- Giữ files nhỏ và tập trung
- Vertical formatting: các concepts liên quan gần nhau, blank lines tách biệt concepts
- Horizontal formatting: giới hạn độ dài dòng (80-120 characters)
- Sử dụng indentation và team style nhất quán
- Nhóm các functions liên quan lại với nhau

## Objects and Data Structures
- Objects: ẩn data đằng sau abstractions, expose behavior qua methods
- Data structures: expose data, có minimal behavior
- Law of Demeter: chỉ nói chuyện với immediate friends, tránh `a.getB().getC().doSomething()`
- Không expose internal structure qua getters/setters một cách mù quáng

## Error Handling
- Sử dụng exceptions, không phải return codes hoặc error flags
- Viết `try-catch-finally` trước khi code có thể fail
- Cung cấp context trong exception messages
- Không return `null` - return empty collections hoặc sử dụng Optional/Maybe
- Không pass `null` như arguments

## Classes
- Classes nhỏ: measured by responsibilities, không phải lines
- Single Responsibility Principle: một lý do để thay đổi
- High cohesion: class variables được sử dụng bởi nhiều methods
- Low coupling: minimal dependencies giữa các classes
- Open/Closed Principle: open for extension, closed for modification

## Unit Tests
- Fast, Independent, Repeatable, Self-validating, Timely (F.I.R.S.T.)
- Một assert per test (hoặc một concept)
- Test code quality bằng với production code quality
- Test names có thể đọc được mô tả what đang being tested
- Arrange-Act-Assert pattern

## Code Quality Principles
- **DRY (Don't Repeat Yourself)**: Không duplication
- **YAGNI (You Aren't Gonna Need It)**: Không build cho hypothetical futures
- **KISS (Keep It Simple)**: Tránh unnecessary complexity
- **Boy Scout Rule**: Leave code cleaner than you found it

## Code Smells to Avoid / Mùi Code Cần Tránh
- Long functions hoặc classes
- Duplicate code
- Dead code (unused variables, functions, parameters)
- Feature envy (method more interested in other class)
- Inappropriate intimacy (classes knowing too much about each other)
- Long parameter lists
- Primitive obsession (overusing primitives thay vì small objects)
- Switch/case statements (cân nhắc polymorphism)
- Temporary fields (class variables only used sometimes)

## Concurrency
- Giữ concurrent code tách biệt khỏi other code
- Giới hạn scope của synchronized/locked data
- Sử dụng thread-safe collections
- Giữ synchronized sections nhỏ
- Biết your execution models và primitives

## System Design
- Tách construction khỏi use (dependency injection)
- Sử dụng factories, builders cho complex object creation
- Program to interfaces, not implementations
- Favor composition over inheritance
- Apply design patterns khi chúng simplify, không phải để khoe

## Refactoring
- Refactor liên tục, không phải trong big batches
- Luôn có passing tests trước và sau
- Small steps: một change tại một thời điểm
- Common refactorings: Extract Method, Rename, Move, Inline

## Documentation
- Self-documenting code > comments > external docs
- Public APIs cần clear documentation
- Include examples trong documentation
- Giữ docs close to code (lý tưởng là in code)

---

**Core Philosophy**: Code được đọc 10x nhiều hơn được viết. Tối ưu cho readability và maintainability, không phải cleverness.

---
**Cập Nhật Lần Cuối**: Tháng 4 năm 2026
