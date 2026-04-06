# 斜杠命令

一个视觉指南，帮助你创建自定义快捷方式，将重复任务转化为简单的 `/` 命令。

> 📚 **关于本指南**
> 
> 本模块介绍 **Claude Code** 的斜杠命令功能。
> 
> Kimi Code 用户可参考 **Kimi Code 适配**部分了解对应命令。

---

## 快速对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `claude` 启动 | `kimi` 启动 |
| `.claude/commands/` 目录 | `.kimi/commands/` 目录 |
| `/command` 调用 | `/command` 调用 |

---

## 概览

斜杠命令是用户定义的快捷方式，通过预定义的提示词加速重复性编码任务。

```
┌─────────────────────────────────────────────────────────────┐
│                     斜杠命令架构                               │
├─────────────────────────────────────────────────────────────┤
│                                                            │
│   用户输入                                                 │
│      │                                                     │
│      ▼                                                     │
│   ┌─────────────┐                                          │
│   │   /test     │ ◀── 用户调用                            │
│   └──────┬──────┘                                          │
│          │                                                  │
│          ▼                                                  │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│   │ 命令注册器   │───▶│  提示词解析  │───▶│ 参数处理    │    │
│   └─────────────┘    └──────┬──────┘    └─────────────┘    │
│                              │                             │
│                              ▼                             │
│                    ┌─────────────────────┐                 │
│                    │   上下文注入         │                 │
│                    │   (CLAUDE.md 等)    │                 │
│                    └──────────┬──────────┘                 │
│                               │                            │
│                               ▼                            │
│                    ┌─────────────────────┐                 │
│                    │    Claude 执行      │                 │
│                    └─────────────────────┘                 │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

### 工作流程

```
1. 创建 .md 文件 ───▶ 2. 放入 .claude/commands/ ───▶ 3. 使用 /command 调用
```

---

## 安装

**Claude Code:**
```bash
# 在项目根目录创建命令目录
mkdir -p .claude/commands

# 复制命令模板
cp /test.md .claude/commands/
cp /optimize.md .claude/commands/
cp /refactor.md .claude/commands/

# 在 Claude Code 中使用：输入 /test、/optimize 等
```

**Kimi Code 适配:**
```bash
# 在项目根目录创建命令目录
mkdir -p .kimi/commands

# 复制命令模板
cp /test.md .kimi/commands/
cp /optimize.md .kimi/commands/
cp /refactor.md .kimi/commands/

# 在 Kimi Code 中使用：输入 /test、/optimize 等
```

---

## 可用命令

| 命令 | 目的 | 用例 |
|------|------|------|
| `/optimize` | 识别代码中的性能瓶颈和优化机会 | 瓶颈分析、算法改进、内存优化 |
| `/test` | 生成/审查针对边缘情况的测试套件 | 单元测试、集成测试、TDD |
| `/refactor` | 改善代码结构而不改变功能 | 代码清理、模式提取、简化 |
| `/fix` | 诊断和修复代码中的 bug | 调试帮助、模式修复、问题解决 |
| `/explain` | 解释代码如何工作及其设计决策 | 入职、文档、学习 |

---

## 工作原理（深度解析）

### 内部处理流程

```
┌────────────────────────────────────────────────────────────────┐
│                    内部架构                                     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   1. 命令注册阶段                                               │
│   ─────────────────                                            │
│   .claude/commands/*.md                                        │
│          │                                                     │
│          ▼                                                     │
│   ┌─────────────────┐                                          │
│   │ 文件系统扫描器   │ 启动时扫描目录                            │
│   └────────┬────────┘                                          │
│            │                                                   │
│            ▼                                                   │
│   ┌─────────────────┐     ┌─────────────────┐                 │
│   │  YAML Frontmatter │───▶│   命令元数据    │                 │
│   │   解析器         │     │  (名称、描述)   │                 │
│   └─────────────────┘     └────────┬────────┘                 │
│                                    │                          │
│            ┌───────────────────────┼───────────────────────┐  │
│            │                       │                       │  │
│            ▼                       ▼                       ▼  │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐│
│   │   /optimize     │   │     /test       │   │    /refactor    ││
│   │   (已注册)       │   │   (已注册)       │   │   (已注册)       ││
│   └─────────────────┘   └─────────────────┘   └─────────────────┘│
│                                                                │
│   2. 命令执行阶段                                               │
│   ─────────────────                                            │
│                                                                │
│   用户输入: /test --target=auth.ts                             │
│          │                                                     │
│          ▼                                                     │
│   ┌─────────────────┐                                          │
│   │   命令解析器    │ 提取命令名和参数                          │
│   └────────┬────────┘                                          │
│            │                                                   │
│            ▼                                                   │
│   ┌─────────────────┐                                          │
│   │  上下文收集器   │ 加载 CLAUDE.md + 文件                     │
│   └────────┬────────┘                                          │
│            │                                                   │
│            ▼                                                   │
│   ┌─────────────────┐                                          │
│   │   提示词引擎    │ 将命令内容 + 参数 + 上下文合并            │
│   └────────┬────────┘                                          │
│            │                                                   │
│            ▼                                                   │
│   ┌─────────────────┐                                          │
│   │   Claude API    │ 执行提示词                                │
│   └─────────────────┘                                          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 上下文层

```
┌────────────────────────────────────────────────────────────┐
│                    上下文层                                │
├────────────────────────────────────────────────────────────┤
│                                                            │
│   第4层：命令内容 (用户定义的 .md 文件)                      │
│   ────────────────────────────────────────                 │
│   $ARGUMENTS 替换后的完整命令提示词                         │
│                                                            │
│   第3层：文件上下文 (自动)                                  │
│   ────────────────────────────────────────                 │
│   引用的文件、选中的代码、Git 上下文                         │
│                                                            │
│   第2层：项目内存 (CLAUDE.md)                               │
│   ────────────────────────────────────────                 │
│   项目指南、架构决策、模式                                   │
│                                                            │
│   第1层：系统提示词                                        │
│   ────────────────────────────────────────                 │
│   Claude 的基础行为和约束                                    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 模板

### /optimize - 性能优化

```yaml
---
name: optimize
description: Analyze code for performance bottlenecks and optimization opportunities
---

Analyze the provided code for performance issues:

1. **Identify bottlenecks** - Look for O(n²) algorithms, unnecessary loops, blocking operations
2. **Check resource usage** - Memory leaks, excessive allocations, unclosed resources
3. **Optimize hot paths** - Caching, memoization, early returns
4. **Measure impact** - Quantify potential speed/memory improvements

Output format:
- Severity: 🔴 Critical | 🟡 Warning | 🟢 Suggestion
- Current: Problem description
- Optimized: Fixed code with explanation
- Impact: Expected improvement

Here is the code to analyze:
$ARGUMENTS
```

### /test - 测试生成

```yaml
---
name: test
description: Generate comprehensive tests targeting edge cases
---

Generate comprehensive tests for the provided code:

1. **Unit tests** - Test individual functions with varied inputs
2. **Edge cases** - Null, empty, extreme values, boundary conditions
3. **Error cases** - Invalid inputs, exceptions, error handling
4. **Integration tests** - Test interactions between components

Testing principles:
- Use descriptive test names (should_xxx_when_yyy)
- Include happy path AND error path
- Mock external dependencies
- Assert on behavior, not implementation

Generate tests for:
$ARGUMENTS
```

### /refactor - 代码重构

```yaml
---
name: refactor
description: Improve code structure without changing functionality
---

Refactor the provided code for better maintainability:

1. **Extract functions** - Break down large functions (≤20 lines ideal)
2. **Naming** - Clear, intention-revealing names
3. **Remove duplication** - DRY principle, extract common patterns
4. **Simplify conditionals** - Early returns, guard clauses
5. **Type safety** - Better type annotations where applicable

Refactoring approach:
- Preserve behavior exactly (no functional changes)
- Keep changes small and reviewable
- Explain WHY each change improves the code

Refactor this code:
$ARGUMENTS
```

---

## Kimi Code 适配

### 配置路径

| 配置项 | Claude Code | Kimi Code |
|--------|-------------|-----------|
| 项目命令目录 | `.claude/commands/` | `.kimi/commands/` |
| 用户命令目录 | `~/.claude/commands/` | `~/.kimi/commands/` |
| 命令文件格式 | `.md` 文件 | `.md` 文件 |
| 调用方式 | `/command` | `/command` |

### 快速迁移

```bash
# 1. 创建 Kimi Code 命令目录
mkdir -p .kimi/commands

# 2. 复制 Claude Code 命令文件
cp .claude/commands/*.md .kimi/commands/

# 3. 在 Kimi Code 中使用相同的命令
# /optimize
# /test
# /refactor
```

### 注意事项

- 命令语法和格式完全相同
- 支持相同的 YAML Frontmatter 格式
- `$ARGUMENTS` 变量处理方式一致
- 文件命名规则相同（使用 kebab-case）

---

## 使用模式

### 模式 1：交互式分析

```
用户: /explain src/auth.ts
Claude: [详细解释代码工作原理]

用户: /optimize (继续对话，引用上述解释)
Claude: [基于上下文提供优化建议]
```

### 模式 2：连续改进

```
用户: /refactor src/utils.js
Claude: [重构建议]

用户: /test (引用重构后的代码)
Claude: [为新结构生成测试]
```

### 模式 3：错误修复

```
用户: /fix src/api.ts
Claude: [识别并解释 bug]

用户: /test src/api.ts
Claude: [为 bug 场景生成测试]
```

---

## 最佳实践

| 实践 | 为什么有效 | 示例 |
|------|-----------|------|
| **使用动词开头** | 清晰表达动作 | `/optimize` 而非 `/performance` |
| **具体描述** | Claude 知道要做什么 | "分析代码" vs "分析 O(n²) 算法" |
| **包含输出格式** | 一致的响应结构 | 使用 emoji 作为视觉层级 |
| **添加使用示例** | 帮助用户正确使用 | 在描述中包含 `$ARGUMENTS` |
| **渐进式详细** | 保持命令简洁，但允许深入 | 使用 "深入分析..." 模式 |

---

## 错误模式（避免这些）

| ❌ 反模式 | ✅ 更好的方式 | 原因 |
|----------|-------------|------|
| 模糊命令如 `/improve` | 具体命令如 `/optimize`, `/refactor` | 清晰表达意图 |
| 一次性提示词过长 | 分解为多个命令 | 提高可用性和清晰度 |
| 重复现有功能 | 使用内置命令 | 避免冗余 |
| 无参数验证 | 使用 `$ARGUMENTS` 描述 | 帮助用户正确使用 |
| 缺少示例 | 包含使用模式 | 更好的用户体验 |

---

## 故障排除

| 问题 | 可能原因 | 解决方案 |
|------|---------|---------|
| 命令未显示 | 目录结构错误 | 检查 `.claude/commands/` (Claude) 或 `.kimi/commands/` (Kimi) |
| 参数未传递 | 未使用 `$ARGUMENTS` | 在模板中包含 `$ARGUMENTS` |
| 响应过长 | 提示词无限制 | 添加 "保持简洁" 指令 |
| 命令无响应 | YAML 格式错误 | 验证 frontmatter 语法 |

---

## 下一步

- [学习内存系统 →](../02-memory/)
- [探索子代理 →](../04-subagents/)
