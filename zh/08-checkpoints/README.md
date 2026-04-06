<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints 与 Rewind

Checkpoints 可以让你保存对话状态，并在 Claude Code 会话中回退到之前的时间点。无论你是在探索不同方案、修复错误，还是比较多个实现路径，这个能力都非常有用。

## 概览

Checkpoints 会保存会话状态，让你可以安全地试验和探索多种方案。它们本质上是当前对话状态的快照，包含：
- 所有已交换的消息
- 已做出的文件修改
- 工具使用历史
- 当前会话上下文

当你在尝试不同实现方式、从错误中恢复，或比较替代方案时，这个功能尤其好用。

## 核心概念

| 概念 | 说明 |
|---------|-------------|
| **Checkpoint** | 保存消息、文件和上下文的对话快照 |
| **Rewind** | 回到之前的 checkpoint，并丢弃之后的更改 |
| **Branch Point** | 从同一个 checkpoint 出发，探索多个方案 |

## 访问 Checkpoints

你可以通过两种主要方式访问和管理 checkpoints：

### 使用键盘快捷键

按两次 `Esc`（`Esc` + `Esc`）打开 checkpoint 界面并浏览已保存的 checkpoints。

### 使用 Slash Command

使用 `/rewind` 命令（别名：`/checkpoint`）快速进入：

```bash
# 打开 rewind 界面
/rewind

# 或者使用别名
/checkpoint
```

## Rewind 选项

回退时，你会看到一个包含五个选项的菜单：

1. **恢复代码和对话** - 把文件和消息都恢复到那个 checkpoint
2. **恢复对话** - 只回退消息，保留当前代码不变
3. **恢复代码** - 只回退文件修改，保留完整对话历史
4. **从这里开始总结** - 把从这里往后的对话压缩成 AI 生成的摘要，而不是直接丢弃。原始消息仍会保留在记录中。你也可以额外指定摘要应聚焦哪些主题。
5. **算了** - 取消并返回当前状态

## 自动 Checkpoints

Claude Code 会自动为你创建 checkpoints：

- **每次用户提示** - 每次用户输入都会创建一个新 checkpoint
- **持久保存** - checkpoints 会跨会话保留
- **自动清理** - 30 天后自动清理旧 checkpoints

这意味着你随时都可以回到之前的任意节点，从几分钟前到几天前都可以。

## 使用场景

| 场景 | 工作流 |
|----------|----------|
| **探索不同方案** | 保存 → 试方案 A → 保存 → Rewind → 试方案 B → 比较 |
| **安全重构** | 保存 → 重构 → 测试 → 如果失败：Rewind |
| **A/B 测试** | 保存 → 设计 A → 保存 → Rewind → 设计 B → 比较 |
| **错误恢复** | 发现问题 → Rewind 到最后一个正常状态 |

## 如何使用 Checkpoints

### 查看和回退

按两次 `Esc`，或者使用 `/rewind` 打开 checkpoint 浏览器。你会看到一个带时间戳的可用 checkpoint 列表。选择任意一个 checkpoint，即可回退到该状态。

### Checkpoint 详情

每个 checkpoint 会显示：
- 创建时间
- 被修改的文件
- 对话中的消息数量
- 使用过的工具

## 实战示例

更多可直接参考的中文示例见 [checkpoint-examples.md](checkpoint-examples.md)。

### 示例 1：探索不同方案

```text
User: 我们给 API 加一个缓存层吧

Claude: 我会为你的 API 端点添加 Redis 缓存……
[在 checkpoint A 处做出修改]

User: 其实我们先试试内存缓存

Claude: 我会 rewind 回去，探索另一种方案……
[用户按下 Esc+Esc 并回退到 checkpoint A]
[在 checkpoint B 处实现内存缓存]

User: 现在我可以比较两种方案了
```

### 示例 2：从错误中恢复

```text
User: 把认证模块重构成 JWT

Claude: 我会重构认证模块……
[做出大量修改]

User: 等等，这把 OAuth 集成弄坏了。我们回去。

Claude: 我来帮你回退到重构之前……
[用户按下 Esc+Esc，并选择重构前的 checkpoint]

User: 这次我们试一个更保守的方案
```

### 示例 3：安全试验

```text
User: 我们试着把它改写成函数式风格
[在实验前创建 checkpoint]

Claude: [执行实验性修改]

User: 测试失败了。我们回退吧。
[用户按下 Esc+Esc 并回退到 checkpoint]

Claude: 我已经回退这些更改了。我们试另一个方案。
```

### 示例 4：分支式探索

```text
User: 我想比较两种数据库设计
[记下 checkpoint，命名为 "Start"]

Claude: 我先实现第一种设计……
[实现 Schema A]

User: 现在让我回去试第二种方案
[用户按下 Esc+Esc 并回退到 "Start"]

Claude: 现在我实现 Schema B……
[实现 Schema B]

User: 太好了，我现在有两个 schema 可以选择
```

## Checkpoint 保留策略

Claude Code 会自动管理你的 checkpoints：

- 每次用户输入都会自动创建 checkpoint
- 旧 checkpoint 最多保留 30 天
- 系统会自动清理，避免存储无限增长

## 工作流模式

### 探索时的分支策略

当你在探索多个方案时：

```text
1. 从初始实现开始 → Checkpoint A
2. 尝试方案 1 → Checkpoint B
3. 回退到 Checkpoint A
4. 尝试方案 2 → Checkpoint C
5. 比较 B 和 C 的结果
6. 选择最佳方案并继续
```

### 安全重构模式

当你在做大改动时：

```text
1. 当前状态 → Checkpoint（自动）
2. 开始重构
3. 运行测试
4. 如果测试通过 → 继续
5. 如果测试失败 → Rewind 并尝试别的方案
```

## 最佳实践

因为 checkpoints 是自动创建的，所以你可以专注于工作，而不用担心手动保存状态。不过，下面这些习惯仍然很重要：

### 如何高效使用 Checkpoints

✅ **应该做：**
- 回退前先看清楚可用的 checkpoints
- 当你想尝试不同方向时使用 rewind
- 保留 checkpoints 方便比较不同方案
- 理解每个 rewind 选项的作用（恢复代码和对话、恢复对话、恢复代码、或总结）

❌ **不要做：**
- 只依赖 checkpoints 来保存代码
- 指望 checkpoints 跟踪外部文件系统变化
- 把 checkpoints 当成 git commit 的替代品

## 配置

你可以在设置中开启或关闭自动 checkpoints：

```json
{
  "autoCheckpoint": true
}
```

- `autoCheckpoint`：是否在每次用户提示后自动创建 checkpoint（默认：`true`）

## 局限性

Checkpoints 很适合会话级回退，但它不是版本控制系统。对于需要长期保存、可审计、可共享的改动，仍然应该使用 git。

## 故障排查

### 找不到 Checkpoints

- 检查你是否在支持该功能的 Claude Code 版本中
- 确认自动 checkpoint 没有被关闭
- 重新打开会话再试一次

### Rewind 失败

- 确认你选择了一个有效的 checkpoint
- 查看是否存在与文件系统或权限相关的限制
- 尝试先分别恢复代码或对话，再决定是否同时恢复两者

## 与 Git 的集成

Checkpoints 和 git 是互补关系：

- Checkpoints 用于会话内探索和安全试验
- Git 用于永久保存代码历史
- 你可以先用 checkpoints 快速试错，再把最终方案提交到 git

## 快速开始

### 基本工作流

```text
1. 开始修改前自动创建 checkpoint
2. 尝试某个方案
3. 如果结果不理想，按 Esc 两次
4. 选择合适的 rewind 选项
5. 继续探索或提交最终方案
```

### 键盘快捷键

- `Esc` + `Esc`：打开 checkpoint 浏览器
- `/rewind`：通过命令进入回退界面
- `/checkpoint`：`/rewind` 的别名

## 什么时候该 rewind：上下文监控

如果你发现这些信号，通常就该回退了：

- 当前方案开始变复杂，而且你还没确定方向
- 测试刚失败，问题可能就是最近一两步引入的
- 你想比较两种实现方式
- 你想保留一个“干净起点”继续探索

## 相关概念

- **Memory**：跨会话的长期上下文，见 [02-memory/README.md](../02-memory/README.md)
- **Hooks**：事件驱动自动化，见 [06-hooks/README.md](../06-hooks/README.md)
- **Plugins**：打包功能集合，见 [07-plugins/README.md](../07-plugins/README.md)
- **Advanced Features**：包括 planning mode 和背景任务，见 [09-advanced-features/README.md](../09-advanced-features/README.md)

## 更多资源

- [根目录中文指南](../README.md)
- [Claude Code 官方检查点文档](https://code.claude.com/docs/en/checkpointing)
- [Claude Code 高级功能指南](../09-advanced-features/README.md)

## 总结

Checkpoints 的价值在于让你敢于试错。它让“先试再说”和“试错后立刻回退”变得安全，从而帮你更快找到正确方案。
