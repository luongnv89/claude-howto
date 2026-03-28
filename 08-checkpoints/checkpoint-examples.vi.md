# Ví dụ về Checkpoints

Các ví dụ thực tế về cách dùng checkpoints hiệu quả trong Claude Code.

Lưu ý: Checkpoints được tạo tự động với mỗi lần bạn gửi tin nhắn. Bạn không cần lưu thủ công. Để rewind, nhấn `Esc` hai lần (`Esc+Esc`) hoặc dùng `/rewind` để mở trình duyệt checkpoint.

## Ví dụ 1: Di chuyển cơ sở dữ liệu

### Tình huống
Bạn cần chuyển từ MySQL sang PostgreSQL và muốn thử cả hai hướng: migrate trực tiếp và migrate dần dần theo kiểu dual-write.

### Quy trình

```
User: Let's implement a direct migration from MySQL to PostgreSQL
      [Checkpoint A được tạo tự động]

Claude: I'll implement the direct migration...
[Thay đổi database driver, cập nhật queries, chỉnh schema]

User: Run the tests
      [Checkpoint B được tạo tự động]

Claude: Running tests...
❌ 15 tests failing - connection pool issues

User: This approach has issues. Let's try the dual-write pattern instead.
[Người dùng nhấn Esc+Esc, chọn Checkpoint A, chọn "Restore code and conversation"]

User: Now implement a dual-write pattern where we write to both databases

Claude: I'll implement dual-write migration...
[Triển khai dual-write layer, chiến lược migrate dần dần]

User: Run the tests

Claude: Running tests...
✅ All tests passing

User: The dual-write approach is clearly safer. Let's commit this.
```

## Ví dụ 2: Tối ưu hiệu năng

### Tình huống
Thử nhiều chiến lược tối ưu hiệu năng khác nhau.

### Quy trình

```
User: Let's optimize the API response time. Current: 450ms
      [Checkpoint "Baseline" được tạo tự động]

Claude: I'll add database query caching...
[Triển khai Redis caching]

User: Run performance tests

Claude: Results: 280ms average response time (38% improvement)

User: Let me try a different approach.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Baseline", chọn "Restore code and conversation"]

User: Try database query optimization instead

Claude: I'll optimize database queries...
[Thêm indexes, tối ưu N+1 queries]

User: Run performance tests

Claude: Results: 180ms average response time (60% improvement)

User: Let me also try a third approach.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Baseline", chọn "Restore code and conversation"]

User: Try response compression and CDN

Claude: I'll add compression and CDN...
[Triển khai gzip, thiết lập CDN]

User: Run performance tests

Claude: Results: 320ms average response time (29% improvement)

User: Query optimization was the best. Let me go back and combine it with caching.
[Người dùng nhấn Esc+Esc, chọn checkpoint sau khi tối ưu query, chọn "Restore code and conversation"]

User: Now add Redis caching on top of these optimized queries

Claude: [Thêm Redis caching lên trên các queries đã tối ưu]

User: Run performance tests

Claude: Results: 95ms average response time (79% improvement) 🎉

User: Perfect! This is the winner. Let's commit this.
```

## Ví dụ 3: Lặp lại thiết kế UI/UX

### Tình huống
Thử các layout khác nhau cho một dashboard.

### Quy trình

```
User: Let's redesign the dashboard with a sidebar layout
      [Checkpoint "Start" được tạo tự động]

Claude: [Triển khai sidebar layout]

User: Show me a screenshot

Claude: [Hiển thị screenshot]

User: The sidebar feels cramped. Let's try a top navigation instead.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Start", chọn "Restore code and conversation"]

User: Try a top navigation layout

Claude: [Triển khai top navigation]

User: Show me a screenshot

Claude: [Hiển thị screenshot]

User: Better, but let's try a card-based grid layout
[Người dùng nhấn Esc+Esc, chọn checkpoint "Start", chọn "Restore code and conversation"]

User: Try a card-based grid layout

Claude: [Triển khai card grid]

User: Show me a screenshot

Claude: [Hiển thị screenshot]

User: This is great! But can we combine the top nav with the card grid?
[Người dùng nhấn Esc+Esc, chọn checkpoint sau khi có card grid, chọn "Restore code and conversation"]

User: Add top navigation to the card grid layout

Claude: [Thêm top navigation vào card grid]

User: Perfect! This is the final design.
```

## Ví dụ 4: Phiên debug

### Tình huống
Truy tìm bug khó với nhiều giả thuyết khác nhau.

### Quy trình

```
User: There's a memory leak in the application
      [Checkpoint "Before debugging" được tạo tự động]

Claude: Let me investigate...
[Phân tích code]

User: I think it's in the event listeners. Let's fix those.

Claude: [Sửa việc dọn dẹp event listener]

User: Run memory profiler

Claude: Still leaking memory - event listeners weren't the issue

User: Let me go back and try a different hypothesis.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Before debugging", chọn "Restore code and conversation"]

User: Maybe it's the database connections?

Claude: [Sửa connection pooling]

User: Run memory profiler

Claude: Still leaking - not the connections either

User: Let me go back and try another angle.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Before debugging", chọn "Restore code and conversation"]

User: Let's check for circular references

Claude: [Tìm và sửa circular references trong cache]

User: Run memory profiler

Claude: ✅ Memory leak fixed! The circular references in the caching layer were the culprit.

User: Excellent! Let's commit this fix.
```

## Ví dụ 5: Phát triển thiết kế API

### Tình huống
Thiết kế REST API qua nhiều vòng lặp.

### Quy trình

```
User: Create a REST API for our blog platform
      [Checkpoint "Before API design" được tạo tự động]

Claude: [Tạo CRUD API cơ bản]

User: This is too simple. Let's add pagination and filtering

Claude: [Thêm pagination và filtering]

User: We need better resource relationships

Claude: [Triển khai HATEOAS links]

User: Actually, let's try GraphQL instead of REST
[Người dùng nhấn Esc+Esc, chọn checkpoint "Before API design", chọn "Restore code and conversation"]

User: Implement a GraphQL API for our blog platform instead

Claude: [Triển khai GraphQL API]

User: I think REST is better for our use case.
[Người dùng nhấn Esc+Esc, chọn checkpoint sau khi có HATEOAS, chọn "Restore code and conversation"]

User: Let's finalize the REST approach.
```

## Ví dụ 6: Quản lý cấu hình

### Tình huống
Thử các cách tiếp cận cấu hình khác nhau.

### Quy trình

```
User: Move configuration to environment variables
      [Checkpoint "Original config" được tạo tự động]

Claude: [Triển khai cấu hình bằng env var]

User: Test in development

Claude: Works locally but deployment issues in production

User: Let me try a different approach.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Original config", chọn "Restore code and conversation"]

User: Try a config file approach with validation

Claude: [Triển khai YAML config với JSON schema validation]

User: Test in development

Claude: ✅ Works well, good validation errors

User: Can we also support env vars for sensitive values?

Claude: [Thêm env var override cho secrets]

User: Test deployment

Claude: ✅ All environments working correctly

User: Perfect! This is production-ready.
```

## Ví dụ 7: Chiến lược kiểm thử

### Tình huống
Triển khai bộ kiểm thử toàn diện.

### Quy trình

```
User: Add unit tests for the auth module
      [Checkpoint được tạo tự động]

Claude: [Thêm Jest unit tests]

User: Run tests

Claude: 45 tests passing, 78% coverage

User: Add integration tests too

Claude: [Thêm integration tests]

User: Run tests

Claude: 89 tests passing, 92% coverage, but tests are slow (3 minutes)

User: The tests are too slow. Let's optimize.

Claude: [Tối ưu test setup, thêm parallel execution]

User: Run tests

Claude: 89 tests passing, 92% coverage, 35 seconds ✅

User: Great! Now add E2E tests for critical paths

Claude: [Thêm Playwright E2E tests]

User: Run all tests

Claude: 112 tests passing, 94% coverage, 2 minutes

User: Perfect balance of coverage and speed!
```

## Ví dụ 8: Dùng tính năng Summarize from Checkpoint

### Tình huống
Sau một phiên debug dài, bạn muốn rút gọn hội thoại nhưng vẫn giữ lại ngữ cảnh.

### Quy trình

```
User: [Sau 20+ tin nhắn debug và khám phá]

[Người dùng nhấn Esc+Esc, chọn checkpoint đầu, chọn "Summarize from here"]
[Tùy chọn cung cấp hướng dẫn: "Focus on what we tried and what worked"]

Claude: [Tạo bản tóm tắt hội thoại từ điểm đó trở đi]
[Tin nhắn gốc vẫn được lưu trong transcript]
[Bản tóm tắt thay thế hội thoại hiển thị, giảm lượng context window sử dụng]

User: Now let's continue with the approach that worked.
```

## Bài học rút ra

1. **Checkpoints là tự động**: Mỗi lần gửi tin nhắn tạo một checkpoint — không cần lưu thủ công
2. **Dùng Esc+Esc hoặc /rewind**: Đây là hai cách truy cập trình duyệt checkpoint
3. **Chọn đúng tùy chọn khôi phục**: Restore code, conversation, cả hai, hoặc summarize tùy nhu cầu
4. **Đừng sợ thử nghiệm**: Checkpoints giúp bạn thử thay đổi táo bạo mà không lo rủi ro
5. **Kết hợp với git**: Dùng checkpoint để khám phá, dùng git cho công việc hoàn chỉnh
6. **Tóm tắt phiên dài**: Dùng "Summarize from here" để giữ hội thoại gọn gàng
