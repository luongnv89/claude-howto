<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Subagents 完整参考

## 概览

Subagents 是专门处理某类任务的独立 AI 助手。它们拥有隔离的上下文、自己的提示词和工具权限，适合把复杂工作拆分给不同角色。

## 主要好处

- 上下文隔离
- 角色分工清晰
- 适合并行和委派
- 便于把复杂任务拆开

## 文件位置

- 项目级：`.claude/agents/`
- 用户级：`~/.claude/agents/`

## 配置

### 文件格式

Subagent 通常是一个带 frontmatter 的 Markdown 文件。

```yaml
---
name: code-reviewer
description: 审查代码质量和安全问题
tools: Read, Grep, Bash
---

# Code Reviewer
```

### 配置字段

| 字段 | 说明 |
|------|------|
| `name` | subagent 名称 |
| `description` | 何时该调用它 |
| `tools` | 允许使用的工具 |
| `model` | 指定模型 |
| `prompt` | 任务提示词 |
| `context` | 上下文策略 |

### 工具配置选项

- 只读审查
- 限制 Bash
- 允许更强工具集

### 基于 CLI 的配置

你也可以通过命令行或设置文件定义 subagent。

## 内置 Subagents

Claude Code 自带一些常见角色，例如：

- 通用助手
- Planning agent
- Explore agent
- Bash agent
- Statusline 相关 agent
- Claude Code Guide agent

## 管理 Subagents

### 使用 `/agents` 命令（推荐）

```bash
/agents
```

### 直接管理文件

#### 创建项目 subagent

```bash
mkdir -p .claude/agents
```

#### 创建用户 subagent

```bash
mkdir -p ~/.claude/agents
```

## 使用 Subagents

### 自动委派

主 agent 可以根据任务描述自动把工作分配给合适的 subagent。

### 显式调用

你也可以明确让 Claude 使用某个 subagent。

### `@` 提及调用

在一些场景里，可以通过 `@agent-name` 方式引用。

### 会话级 agent

可以在整个会话中固定使用某个 agent。

### 列出可用 agents

```bash
claude agents
```

## 可恢复的 agents

某些 subagent 可以先启动，之后再恢复，便于长任务接力。

## 串联 Subagents

复杂任务里可以让多个 subagent 依次协作，例如：

1. 代码审查
2. 测试生成
3. 文档更新

## Subagents 的持久记忆

Subagents 可以拥有自己的 memory 范围，让它们在各自职责内保持一致。

### Memory 范围

- 项目级
- 用户级
- 子目录级

### 工作方式

Subagent 会在自己的上下文中读取对应记忆，不和主会话完全混在一起。

## 后台 Subagents

### 配置

有些 subagent 可以作为后台任务执行，不阻塞主会话。

### 快捷键

在支持的界面中，可用快捷键查看或切换后台 subagent。

### 关闭后台任务

如果你不想让任务后台运行，可以在设置中关闭。

## Worktree 隔离

### 配置

可以为 subagent 分配独立的 worktree。

### 工作方式

这样不同任务就不会互相污染文件状态。

## 限制可启动的 Subagents

你可以限制 Claude 只能 spawn 某些 subagent，以降低风险。

### 示例

- 只允许审查类 agent
- 禁止高风险自动化 agent

## `claude agents` CLI 命令

用于查看和管理当前可用的 agent。

## Agent Teams（实验性）

Agent teams 是更高级的协作模式，适合多个 subagent 并行处理复杂任务。

### Subagents vs Agent Teams

- Subagents 侧重委派单个任务
- Agent teams 侧重多角色协作

### 启用 Agent Teams

通过设置打开实验性功能。

### 启动团队

团队模式会把不同任务分配给不同角色。

### 显示模式

可以选择更适合终端或图形界面的显示方式。

### 导航

你可以在 team 中切换角色、查看状态和读取消息。

### 团队配置

适合为大型流程定义清晰角色。

### 架构

agent team 本质上是多个专门角色围绕同一任务协作。

### 任务分配与消息

主 agent 会负责把任务拆分并转发给对应 subagent。

### 计划审批流程

如果是 plan 驱动流程，团队会先审计划再执行。

### 团队相关 hook 事件

一些 hook 可以在 team 生命周期里触发。

### 最佳实践

- 角色定义要清楚
- 任务边界要明确
- 不要让多个 agent 做重复工作

### 局限

- 实验性功能可能会变化
- 复杂团队需要更多配置

## 插件中的 Subagent 安全

插件分发的 subagent 要特别注意权限、工具范围和边界条件。

## 架构

### 高层架构

主 agent、subagent、文件系统和工具权限共同构成执行链。

### 生命周期

1. 创建
2. 分配任务
3. 执行
4. 返回结果
5. 结束或恢复

## 上下文管理

### 关键点

- 子上下文尽量小
- 让每个 subagent 只负责自己的事
- 避免把所有信息都塞进去

### 性能考虑

过多的上下文会拖慢速度并降低准确性。

### 关键行为

subagent 在隔离上下文里工作，但仍能把结果汇总回主会话。

## 什么时候使用 Subagents

- 任务可拆分
- 需要隔离上下文
- 需要明确角色分工
- 需要并行协作

## 最佳实践

### 设计原则

- 单一职责
- 描述明确
- 工具权限最小化

### System Prompt 最佳实践

- 任务说明要具体
- 不要写太长
- 只保留执行任务所需的信息

### 工具访问策略

- 审查型 subagent 只读
- 实现型 subagent 适度开放写权限
- 高风险动作要保持审批

## 本目录中的示例 Subagents

### 1. [Code Reviewer](./code-reviewer.md)

用于全面代码质量审查。

### 2. [Test Engineer](./test-engineer.md)

用于测试策略、覆盖率和测试生成。

### 3. [Documentation Writer](./documentation-writer.md)

用于技术文档写作和更新。

### 4. [Secure Reviewer](./secure-reviewer.md)

用于安全检查，通常只读。

### 5. [Implementation Agent](./implementation-agent.md)

用于功能实现和代码修改。

### 6. [Debugger](./debugger.md)

用于定位 bug 和分析异常。

### 7. [Data Scientist](./data-scientist.md)

用于分析数据、解释结果和生成报告。

### 8. [Clean Code Reviewer](./clean-code-reviewer.md)

用于按 Clean Code 原则做专门审查。

## 安装说明

### 方法 1：使用 `/agents`

```bash
/agents
```

### 方法 2：复制到项目

```bash
mkdir -p .claude/agents
cp 04-subagents/*.md .claude/agents/
```

### 方法 3：复制到用户目录

```bash
mkdir -p ~/.claude/agents
cp 04-subagents/*.md ~/.claude/agents/
```

### 验证

- 运行 `/agents`
- 检查对应 agent 是否出现在列表中
- 试着让 Claude 委派一个简单任务

## 文件结构

```text
.claude/agents/
├── clean-code-reviewer.md
├── code-reviewer.md
├── data-scientist.md
├── debugger.md
├── documentation-writer.md
├── implementation-agent.md
├── secure-reviewer.md
├── test-engineer.md
└── README.md
```

## 相关概念

- [Skills 中文指南](../03-skills/README.md)
- [Memory 中文指南](../02-memory/README.md)
- [Hooks 中文指南](../06-hooks/README.md)
- [Plugins 中文指南](../07-plugins/README.md)
