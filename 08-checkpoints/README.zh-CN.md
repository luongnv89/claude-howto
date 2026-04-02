<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints and Rewind

Checkpoints 允许你保存对话状态，并在 Claude Code 会话中回退到历史节点。这对于探索不同实现路径、从错误中恢复、比较备选方案非常有价值。

## Overview

Checkpoints 通过保存对话状态并支持回退，让你可以安全试验与多路径探索。每个 checkpoint 都是一次会话快照，包含：
- 全部对话消息
- 已做文件修改
- 工具调用历史
- 当前会话上下文

在探索方案、纠错、对比替代实现时，checkpoints 非常实用。

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Checkpoint** | 会话状态快照，含消息、文件与上下文 |
| **Rewind** | 回到某个历史 checkpoint，并丢弃其后的变更 |
| **Branch Point** | 从某个 checkpoint 分叉探索多个方案 |

## Accessing Checkpoints

你可以通过两种方式访问和管理 checkpoints：

### 使用快捷键
按两次 `Esc`（`Esc` + `Esc`）打开 checkpoint 界面并浏览已保存节点。

### 使用 Slash Command
使用 `/rewind`（别名：`/checkpoint`）快速打开：

```bash
# Open rewind interface
/rewind

# Or use the alias
/checkpoint
```

## Rewind Options

回退时会看到 5 个选项：

1. **Restore code and conversation** -- 同时恢复代码与对话
2. **Restore conversation** -- 仅恢复对话，保留当前代码
3. **Restore code** -- 仅恢复代码，保留完整对话历史
4. **Summarize from here** -- 将该点之后对话压缩为 AI 摘要而非直接丢弃；原始消息仍保留在 transcript 中，可附加摘要聚焦指令
5. **Never mind** -- 取消回退，保持当前状态

## Automatic Checkpoints

Claude Code 会自动为你创建 checkpoints：

- **每次用户提问**：每条用户输入都会生成一个新 checkpoint
- **持久化保存**：checkpoint 可跨会话存在
- **自动清理**：30 天后自动清理

这意味着你可以回退到此前任意时间点（从几分钟前到几天前）。

## Use Cases

| Scenario | Workflow |
|----------|----------|
| **Exploring Approaches** | Save → Try A → Save → Rewind → Try B → Compare |
| **Safe Refactoring** | Save → Refactor → Test → If fail: Rewind |
| **A/B Testing** | Save → Design A → Save → Rewind → Design B → Compare |
| **Mistake Recovery** | Notice issue → Rewind to last good state |

## Using Checkpoints

### Viewing and Rewinding

按 `Esc` 两次或使用 `/rewind` 打开 checkpoint 浏览器。你会看到带时间戳的 checkpoint 列表。选择任意 checkpoint 即可回退。

### Checkpoint Details

每个 checkpoint 会显示：
- 创建时间
- 修改过的文件
- 对话消息数量
- 使用过的工具

## Practical Examples

### Example 1: Exploring Different Approaches

```text
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Makes changes at checkpoint A]

User: Actually, let's try in-memory caching instead

Claude: I'll rewind to explore a different approach...
[User presses Esc+Esc and rewinds to checkpoint A]
[Implements in-memory caching at checkpoint B]

User: Now I can compare both approaches
```

### Example 2: Recovering from Mistakes

```text
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Makes extensive changes]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll help you rewind to before the refactoring...
[User presses Esc+Esc and selects the checkpoint before the refactor]

User: Let's try a more conservative approach this time
```

### Example 3: Safe Experimentation

```text
User: Let's try rewriting this in a functional style
[Creates checkpoint before experiment]

Claude: [Makes experimental changes]

User: The tests are failing. Let's rewind.
[User presses Esc+Esc and rewinds to the checkpoint]

Claude: I've rewound the changes. Let's try a different approach.
```

### Example 4: Branching Approaches

```text
User: I want to compare two database designs
[Takes note of checkpoint - call it "Start"]

Claude: I'll create the first design...
[Implements Schema A]

User: Now let me go back and try the second approach
[User presses Esc+Esc and rewinds to "Start"]

Claude: Now I'll implement Schema B...
[Implements Schema B]

User: Great! Now I have both schemas to choose from
```

## Checkpoint Retention

Claude Code 会自动管理 checkpoints：

- 每次用户提问自动创建
- 历史 checkpoint 最多保留 30 天
- 自动清理以防存储无限增长

## Workflow Patterns

### Branching Strategy for Exploration

当你要探索多种方案：

```text
1. 初始实现 → Checkpoint A
2. 尝试方案 1 → Checkpoint B
3. 回退到 Checkpoint A
4. 尝试方案 2 → Checkpoint C
5. 对比 B 与 C
6. 选最佳方案继续
```

### Safe Refactoring Pattern

进行较大改动时：

```text
1. 当前状态 → Checkpoint（自动）
2. 开始重构
3. 运行测试
4. 测试通过 → 继续
5. 测试失败 → 回退并尝试新方案
```

## Best Practices

由于 checkpoints 自动创建，你可以专注于开发，不必手动保存。但建议遵循以下实践：

### Using Checkpoints Effectively

✅ **Do:**
- 回退前先浏览可用 checkpoint
- 需要探索分支时主动使用 rewind
- 借助 checkpoint 对比不同方案
- 明确每个回退选项作用（恢复代码+对话、仅对话、仅代码、摘要）

❌ **Don't:**
- 只依赖 checkpoint 保存代码
- 期待 checkpoint 跟踪外部文件系统操作
- 用 checkpoint 替代 git commit

## Configuration

你可以在设置中开关自动 checkpoint：

```json
{
  "autoCheckpoint": true
}
```

- `autoCheckpoint`：是否在每次用户输入时自动创建 checkpoint（默认 `true`）

## Limitations

Checkpoint 的限制：

- **不跟踪 Bash 命令造成的更改**（如 `rm`/`mv`/`cp`）
- **不跟踪外部改动**（编辑器、终端中在 Claude Code 之外做的修改）
- **不能替代版本控制**（永久可审计改动请使用 git）

## Troubleshooting

### Missing Checkpoints

**Problem**：预期 checkpoint 未出现

**Solution**：
- 检查是否被清理
- 确认设置中 `autoCheckpoint` 已开启
- 检查磁盘空间

### Rewind Failed

**Problem**：无法回退到某 checkpoint

**Solution**：
- 确保无冲突的未提交改动
- 检查 checkpoint 是否损坏
- 尝试回退到其他 checkpoint

## Integration with Git

Checkpoints 与 git 是互补关系（而非替代）：

| Feature | Git | Checkpoints |
|---------|-----|-------------|
| Scope | 文件系统 | 对话 + 文件 |
| Persistence | 永久 | 会话级 |
| Granularity | Commit 粒度 | 任意时间点 |
| Speed | 相对慢 | 即时 |
| Sharing | 支持 | 有限 |

推荐组合方式：
1. 用 checkpoint 快速试验
2. 用 git commit 固化最终结果
3. 重大 git 操作前先确认 checkpoint
4. 将成功 checkpoint 对应状态提交到 git

## Quick Start Guide

### Basic Workflow

1. **正常工作** - Claude Code 自动创建 checkpoints
2. **想回退？** - 按两次 `Esc` 或执行 `/rewind`
3. **选 checkpoint** - 从列表中选择目标节点
4. **选恢复方式** - 恢复代码+对话 / 仅对话 / 仅代码 / 从此处摘要 / 取消
5. **继续工作** - 你已回到目标节点

### Keyboard Shortcuts

- **`Esc` + `Esc`** - 打开 checkpoint 浏览器
- **`/rewind`** - 另一种访问方式
- **`/checkpoint`** - `/rewind` 别名

## Knowing When to Rewind: Context Monitoring

Checkpoint 帮你“回去”，但你如何知道**什么时候该回退**？随着对话变长，Claude 的上下文窗口会逐步被占满，模型质量可能静默下降。你可能在不知情下用“半盲状态”继续产出。

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** 通过在 Claude Code 状态栏显示实时 **context zones** 来解决这个问题。它会标记当前窗口状态：**Plan**（绿，适合规划与编码）→ **Code**（黄，避免开启新规划）→ **Dump**（橙，应收尾并回退）。当分区变化时，你就知道该 checkpoint + 重开上下文，而不是硬推低质量输出。

## Related Concepts

- **[Advanced Features](../09-advanced-features/README.zh-CN.md)** - planning mode 与高级能力
- **[Memory Management](../02-memory/README.zh-CN.md)** - 对话历史与上下文管理
- **[Slash Commands](../01-slash-commands/README.zh-CN.md)** - 用户触发快捷命令
- **[Hooks](../06-hooks/README.zh-CN.md)** - 事件驱动自动化
- **[Plugins](../07-plugins/README.zh-CN.md)** - 打包扩展能力

## Additional Resources

- [Official Checkpointing Documentation](https://code.claude.com/docs/en/checkpointing)
- [Advanced Features Guide](../09-advanced-features/README.zh-CN.md) - extended thinking 等能力

## Summary

Checkpoints 是 Claude Code 的自动能力：你可以无压力探索不同方案，并随时回退到历史节点。每次用户输入都会自动创建新 checkpoint。

核心收益：
- 无惧试错，放心探索
- 快速从错误状态恢复
- 并行对比不同方案
- 与版本控制安全配合

请记住：checkpoint 不是 git 的替代品。checkpoint 用于快速实验，git 用于永久代码变更管理。
