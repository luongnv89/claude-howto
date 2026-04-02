# Checkpoint Examples

Claude Code 中使用 checkpoints 的真实场景示例。

注意：每次用户输入都会自动创建 checkpoint，不需要手动保存。回退时按两次 `Esc`（`Esc+Esc`）或使用 `/rewind` 打开 checkpoint 浏览器。

## Example 1: Database Migration

### Scenario
你需要从 MySQL 迁移到 PostgreSQL，但希望比较“直接迁移”和“双写渐进迁移”两种方案。

### Workflow

```text
User: Let's implement a direct migration from MySQL to PostgreSQL
      [Checkpoint A created automatically]

Claude: I'll implement the direct migration...
[Changes database driver, updates queries, modifies schema]

User: Run the tests
      [Checkpoint B created automatically]

Claude: Running tests...
❌ 15 tests failing - connection pool issues

User: This approach has issues. Let's try the dual-write pattern instead.
[User presses Esc+Esc, selects Checkpoint A, chooses "Restore code and conversation"]

User: Now implement a dual-write pattern where we write to both databases

Claude: I'll implement dual-write migration...
[Implements dual-write layer, gradual migration strategy]

User: Run the tests

Claude: Running tests...
✅ All tests passing

User: The dual-write approach is clearly safer. Let's commit this.
```

## Example 2: Performance Optimization

### Scenario
需要尝试多种性能优化策略。

### Workflow

```text
User: Let's optimize the API response time. Current: 450ms
      [Checkpoint "Baseline" created automatically]

Claude: I'll add database query caching...
[Implements Redis caching]

User: Run performance tests

Claude: Results: 280ms average response time (38% improvement)

User: Let me try a different approach.
[User presses Esc+Esc, selects "Baseline" checkpoint, chooses "Restore code and conversation"]

User: Try database query optimization instead

Claude: I'll optimize database queries...
[Adds indexes, optimizes N+1 queries]

User: Run performance tests

Claude: Results: 180ms average response time (60% improvement)

User: Let me also try a third approach.
[User presses Esc+Esc, selects "Baseline" checkpoint, chooses "Restore code and conversation"]

User: Try response compression and CDN

Claude: I'll add compression and CDN...
[Implements gzip, sets up CDN]

User: Run performance tests

Claude: Results: 320ms average response time (29% improvement)

User: Query optimization was the best. Let me go back and combine it with caching.
[User presses Esc+Esc, selects the checkpoint after query optimization, chooses "Restore code and conversation"]

User: Now add Redis caching on top of these optimized queries

Claude: [Adds Redis caching on top of optimized queries]

User: Run performance tests

Claude: Results: 95ms average response time (79% improvement) 🎉

User: Perfect! This is the winner. Let's commit this.
```

## Example 3: UI/UX Iteration

### Scenario
为 dashboard 尝试不同布局方案。

### Workflow

```text
User: Let's redesign the dashboard with a sidebar layout
      [Checkpoint "Start" created automatically]

Claude: [Implements sidebar layout]

User: Show me a screenshot

Claude: [Shows screenshot]

User: The sidebar feels cramped. Let's try a top navigation instead.
[User presses Esc+Esc, selects "Start" checkpoint, chooses "Restore code and conversation"]

User: Try a top navigation layout

Claude: [Implements top navigation]

User: Show me a screenshot

Claude: [Shows screenshot]

User: Better, but let's try a card-based grid layout
[User presses Esc+Esc, selects "Start" checkpoint, chooses "Restore code and conversation"]

User: Try a card-based grid layout

Claude: [Implements card grid]

User: Show me a screenshot

Claude: [Shows screenshot]

User: This is great! But can we combine the top nav with the card grid?
[User presses Esc+Esc, selects the checkpoint after the card grid, chooses "Restore code and conversation"]

User: Add top navigation to the card grid layout

Claude: [Adds top navigation to card grid]

User: Perfect! This is the final design.
```

## Example 4: Debugging Session

### Scenario
排查一个复杂 bug，并验证多个假设。

### Workflow

```text
User: There's a memory leak in the application
      [Checkpoint "Before debugging" created automatically]

Claude: Let me investigate...
[Analyzes code]

User: I think it's in the event listeners. Let's fix those.

Claude: [Fixes event listener cleanup]

User: Run memory profiler

Claude: Still leaking memory - event listeners weren't the issue

User: Let me go back and try a different hypothesis.
[User presses Esc+Esc, selects "Before debugging" checkpoint, chooses "Restore code and conversation"]

User: Maybe it's the database connections?

Claude: [Implements connection pooling fixes]

User: Run memory profiler

Claude: Still leaking - not the connections either

User: Let me go back and try another angle.
[User presses Esc+Esc, selects "Before debugging" checkpoint, chooses "Restore code and conversation"]

User: Let's check for circular references

Claude: [Finds and fixes circular references in cache]

User: Run memory profiler

Claude: ✅ Memory leak fixed! The circular references in the caching layer were the culprit.

User: Excellent! Let's commit this fix.
```

## Example 5: API Design Evolution

### Scenario
多轮迭代 API 设计（REST 与 GraphQL 对比）。

### Workflow

```text
User: Create a REST API for our blog platform
      [Checkpoint "Before API design" created automatically]

Claude: [Creates basic CRUD API]

User: This is too simple. Let's add pagination and filtering

Claude: [Adds pagination and filtering]

User: We need better resource relationships

Claude: [Implements HATEOAS links]

User: Actually, let's try GraphQL instead of REST
[User presses Esc+Esc, selects "Before API design" checkpoint, chooses "Restore code and conversation"]

User: Implement a GraphQL API for our blog platform instead

Claude: [Implements GraphQL API]

User: I think REST is better for our use case.
[User presses Esc+Esc, selects the checkpoint after HATEOAS, chooses "Restore code and conversation"]

User: Let's finalize the REST approach.
```

## Example 6: Configuration Management

### Scenario
测试不同配置管理策略。

### Workflow

```text
User: Move configuration to environment variables
      [Checkpoint "Original config" created automatically]

Claude: [Implements env var configuration]

User: Test in development

Claude: Works locally but deployment issues in production

User: Let me try a different approach.
[User presses Esc+Esc, selects "Original config" checkpoint, chooses "Restore code and conversation"]

User: Try a config file approach with validation

Claude: [Implements YAML config with JSON schema validation]

User: Test in development

Claude: ✅ Works well, good validation errors

User: Can we also support env vars for sensitive values?

Claude: [Adds env var override for secrets]

User: Test deployment

Claude: ✅ All environments working correctly

User: Perfect! This is production-ready.
```

## Example 7: Test Strategy

### Scenario
搭建覆盖全面且执行效率合理的测试体系。

### Workflow

```text
User: Add unit tests for the auth module
      [Checkpoint created automatically]

Claude: [Adds Jest unit tests]

User: Run tests

Claude: 45 tests passing, 78% coverage

User: Add integration tests too

Claude: [Adds integration tests]

User: Run tests

Claude: 89 tests passing, 92% coverage, but tests are slow (3 minutes)

User: The tests are too slow. Let's optimize.

Claude: [Optimizes test setup, adds parallel execution]

User: Run tests

Claude: 89 tests passing, 92% coverage, 35 seconds ✅

User: Great! Now add E2E tests for critical paths

Claude: [Adds Playwright E2E tests]

User: Run all tests

Claude: 112 tests passing, 94% coverage, 2 minutes

User: Perfect balance of coverage and speed!
```

## Example 8: Using Summarize from Checkpoint

### Scenario
长时间 debug 后，希望压缩对话但保留关键上下文。

### Workflow

```text
User: [After 20+ messages of debugging and exploration]

[User presses Esc+Esc, selects an early checkpoint, chooses "Summarize from here"]
[Optionally provides instructions: "Focus on what we tried and what worked"]

Claude: [Generates a summary of the conversation from that point forward]
[Original messages are preserved in the transcript]
[The summary replaces the visible conversation, reducing context window usage]

User: Now let's continue with the approach that worked.
```

## Key Takeaways

1. **Checkpoints are automatic**：每次用户输入都会创建 checkpoint，无需手动保存
2. **Use Esc+Esc or /rewind**：这是打开 checkpoint 浏览器的两种方式
3. **Choose the right restore option**：根据需求选择恢复代码、对话、两者，或摘要
4. **Don't fear experimentation**：checkpoint 让激进试验也可控
5. **Combine with git**：checkpoint 用于探索，git 用于固化成果
6. **Summarize long sessions**：长会话可用 “Summarize from here” 降低上下文负担
