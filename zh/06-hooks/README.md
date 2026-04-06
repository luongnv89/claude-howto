<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks 参考

Hooks 是在 Claude Code 事件发生时自动执行的 shell 命令，用来做格式化、校验、通知、审计等自动化工作。

## 概览

Hooks 是事件驱动的自动化机制。它们会在 Claude Code 发生某些动作时自动运行，不需要你手动触发。

常见用途：

- 写文件前自动格式化
- 提交前运行测试
- 扫描安全问题
- 记录 bash 命令
- 校验用户提示词
- 发送团队通知

## Hook 类型

Claude Code 提供 4 类、25 个事件：

- **Tool Hooks**：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`PermissionRequest`
- **Session Hooks**：`SessionStart`、`SessionEnd`、`Stop`、`StopFailure`、`SubagentStart`、`SubagentStop`
- **Task Hooks**：`UserPromptSubmit`、`TaskCompleted`、`TaskCreated`、`TeammateIdle`
- **Lifecycle Hooks**：`ConfigChange`、`CwdChanged`、`FileChanged`、`PreCompact`、`PostCompact`、`WorktreeCreate`、`WorktreeRemove`、`Notification`、`InstructionsLoaded`、`Elicitation`、`ElicitationResult`

## 安装

```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

然后在 `~/.claude/settings.json` 里配置：

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

## 使用方法

Hooks 会在匹配到事件时自动执行。你可以把它理解成 Claude Code 的事件回调。

## 常见示例

- `format-code.sh` - 写入前自动格式化
- `pre-commit.sh` - 提交前跑测试
- `security-scan.sh` - 做安全扫描
- `log-bash.sh` - 记录 bash 命令
- `validate-prompt.sh` - 校验输入
- `notify-team.sh` - 发通知

## 最佳实践

- 把 hooks 保持短小明确
- 只做单一职责
- 先在本地测试
- 不要在 hook 里放复杂业务逻辑
- 对副作用保持谨慎

## 故障排查

- 检查文件路径和权限
- 确认脚本可执行
- 检查 settings.json 语法
- 查看 Claude Code 版本兼容性

## 相关概念

- [Checkpoints and Rewind](../08-checkpoints/README.md)
- [Slash Commands](../01-slash-commands/README.md)
- [Skills](../03-skills/README.md)
- [Subagents](../04-subagents/README.md)
- [Plugins](../07-plugins/README.md)
- [Advanced Features](../09-advanced-features/README.md)

## 更多资源

- [Memory Guide](../02-memory/README.md)
- [Official Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
