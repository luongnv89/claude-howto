<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Agent Skills 指南

## 概览

Skills 是可以复用、可自动触发的能力包。一个 skill 通常包含 `SKILL.md`、参考文件、脚本和模板。Claude 在合适的场景下会自动加载它。

### 主要好处

- 可复用
- 可渐进加载
- 可以把脚本、模板、说明放在一起
- 适合标准化流程

## Skills 的工作方式：渐进式披露

Skills 不会一次性把所有内容都塞进上下文，而是按需加载。

### 三层加载

1. **只看描述**：先判断这个 skill 是否相关
2. **加载 `SKILL.md`**：读取核心说明
3. **按需加载支持文件**：脚本、模板、参考资料

## Skill 加载流程

1. Claude 扫描技能目录
2. 根据描述判断是否匹配当前任务
3. 读取 `SKILL.md`
4. 如有需要，再加载脚本和辅助文件

## Skill 类型与位置

Skills 可以放在：

- 项目目录下的 `.claude/skills/`
- 用户目录下的 `~/.claude/skills/`

### 自动发现

只要目录结构正确，Claude 就会自动发现这些 Skills。

## 创建自定义 Skills

### 基本目录结构

```text
my-skill/
└── SKILL.md
```

### `SKILL.md` 格式

```yaml
---
name: my-skill
description: 这个 skill 的用途，以及什么时候触发
---

# Your Skill Name

## Instructions

## Examples
```

### 必填字段

- `name`
- `description`

### 可选 frontmatter 字段

- `argument-hint`
- `allowed-tools`
- `model`
- `disable-model-invocation`
- `user-invocable`
- `context`
- `agent`
- `hooks`

## Skill 内容类型

### 参考内容

适合放规则、标准、文档片段和示例。

### 任务内容

适合放具体步骤、执行流程和结果格式要求。

## 控制 Skill 的调用

你可以通过 `disable-model-invocation`、`user-invocable` 和工具白名单来控制 Claude 是否能自动调用这个 skill。

## 字符串替换

Skills 支持 `$ARGUMENTS`、`$0`、`$1` 等参数替换。

### 动态上下文注入

你可以在 prompt 里插入 shell 命令结果：

```md
- 当前 git 状态：!`git status`
- 当前 diff：!`git diff HEAD`
- 当前分支：!`git branch --show-current`
```

## 在 subagent 中运行 Skills

某些 skill 适合在隔离上下文中运行，这样可以降低对主会话的影响。

## 实战示例

### 示例 1：代码审查 Skill

一个典型的审查 skill 会包含：

- 审查模板
- 风险等级
- 输出格式
- 需要关注的维度

### 示例 2：代码库可视化 Skill

可以把代码库结构、依赖关系和模块边界总结给 Claude，便于快速理解。

### 示例 3：部署 Skill（只允许用户触发）

适合带副作用的操作，比如生产环境部署。通常会配合 `disable-model-invocation: true`。

### 示例 4：品牌语气 Skill

用于检查输出是否符合品牌语气、语调和表达风格。

### 示例 5：`CLAUDE.md` 生成 Skill

可以从项目文档中生成或补充 `CLAUDE.md`。

### 示例 6：带脚本的重构 Skill

常见组合是：

- `SKILL.md`
- `scripts/`
- `templates/`
- `references/`

## 管理 Skills

### 查看可用 Skills

```bash
/skills
```

### 测试一个 Skill

把它放到测试目录或者临时项目里，然后通过相应命令触发。

### 更新 Skill

修改 `SKILL.md` 或支持文件后，重新打开会话或重新加载即可。

### 限制 Claude 对 Skill 的访问

你可以通过权限配置，只允许 Claude 访问某些 skill。

## 最佳实践

### 1. 描述要具体

让 `description` 明确说明这个 skill 在什么时候触发。

### 2. 保持聚焦

一个 skill 解决一个问题，不要什么都塞进去。

### 3. 包含触发词

在描述里加入相关关键词，帮助 Claude 更准确地选择它。

### 4. `SKILL.md` 不要太长

尽量控制在 500 行以内，超过就拆分支持文件。

### 5. 引用支持文件

把重复内容移到脚本或参考文件中，主文件只保留核心说明。

## 故障排查

### 快速参考

- 检查目录结构是否正确
- 检查 `SKILL.md` frontmatter 是否有效
- 检查 skill 名称是否和调用名一致

### Skill 没有触发

- 检查描述是否足够具体
- 检查目录是否在 Claude 可见范围内
- 检查是否被更高优先级的 skill 覆盖

### Skill 触发太频繁

- 收紧描述
- 增加约束条件
- 用更具体的触发词

### Claude 看不到全部 Skills

- 检查路径
- 检查权限
- 重新加载会话

## 安全注意事项

- 不要在 skill 中硬编码密钥
- 对副作用操作保持用户触发
- 给自动触发的 skill 设置清晰边界

## Skills vs 其他功能

| 功能 | 触发方式 | 适合场景 |
|------|----------|----------|
| Skills | 自动/半自动 | 复用能力、流程标准化 |
| Slash Commands | 手动 | 快捷命令 |
| Subagents | 自动委派 | 隔离任务 |
| Hooks | 事件触发 | 自动化和验证 |

## 内置 Skills

Claude Code 自带一些 Skills，例如批处理、调试、简化和 Claude API 相关内容。

## 共享 Skills

### 项目 Skills（团队共享）

把 skill 放在项目目录里，团队成员都能用。

### 个人 Skills

```bash
# 复制到个人目录
mkdir -p ~/.claude/skills

# 让脚本可执行
chmod +x ~/.claude/skills/*/scripts/*
```

### Plugin 分发

你也可以把 Skills 作为插件的一部分发布出去。

## 继续深入

如果你要管理一整套 Skills，可以再做一个 skill collection 或 skill manager，用来统一发现、更新和分发。

## 更多资源

- [根目录中文指南](../README.md)
- [Slash Commands 中文参考](../01-slash-commands/README.md)
- [Memory 中文指南](../02-memory/README.md)
- [Subagents 中文参考](../04-subagents/README.md)
