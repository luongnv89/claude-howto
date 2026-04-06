# 插件

一个视觉指南，了解如何捆绑功能为完整的、可安装的包。

> 📚 **关于本指南**
> 
> 本模块介绍 **Claude Code** 的插件系统。
> 
> Kimi Code 用户可参考 **Kimi Code 适配**部分了解对应配置。

---

## 快速对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `claude plugin` 命令 | `kimi plugin` 命令 |
| `.claude/` 安装目录 | `.kimi/` 安装目录 |
| `/plugin` 斜杠命令 | `/plugin` 斜杠命令 |

---

## 概览

插件是完整的功能包，捆绑了斜杠命令、内存、技能、钩子和子代理。

```
┌─────────────────────────────────────────────────────────────┐
│                     插件架构                                 │
├─────────────────────────────────────────────────────────────┤
│                                                            │
│   插件包                                                    │
│   ┌─────────────────────────────────────────────────────┐  │
│   │  plugin-name/                                       │  │
│   │  ├── commands/        # 斜杠命令                    │  │
│   │  ├── memory/          # CLAUDE.md / KIMI.md         │  │
│   │  ├── skills/          # 技能定义                    │  │
│   │  ├── hooks/           # 钩子脚本                    │  │
│   │  ├── agents/          # 子代理                      │  │
│   │  └── manifest.json    # 插件元数据                  │  │
│   └─────────────────────────────────────────────────────┘  │
│                            │                               │
│                            ▼                               │
│              ┌─────────────────────────┐                   │
│              │  claude plugin install  │                   │
│              │  或 kimi plugin install  │                   │
│              └─────────────────────────┘                   │
│                            │                               │
│                            ▼                               │
│   ┌─────────────────────────────────────────────────────┐  │
│   │  安装到 .claude/plugins/ 或 .kimi/plugins/          │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

### 工作流程

```
/plugin install name ──▶ 下载包 ──▶ 解压安装 ──▶ 激活所有功能
```

---

## 安装

**Claude Code:**
```bash
# 使用斜杠命令安装
/plugin install pr-review

# 或使用 CLI
claude plugin install pr-review

# 列出已安装插件
claude plugin list
```

**Kimi Code 适配:**
```bash
# 使用斜杠命令安装
/plugin install pr-review

# 或使用 CLI
kimi plugin install pr-review

# 列出已安装插件
kimi plugin list
```

---

## 插件结构

```
my-plugin/
├── manifest.json           # 插件元数据
├── commands/
│   ├── review.md
│   └── summarize.md
├── memory/
│   └── CLAUDE.md          # 或 KIMI.md
├── skills/
│   └── code-analysis/
│       └── CLAUDE.md      # 或 KIMI.md
├── hooks/
│   └── pre-commit.sh
└── agents/
    └── security-auditor.md
```

### manifest.json

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Automated PR review with security and style checks",
  "author": "Your Name",
  "commands": ["review", "summarize"],
  "skills": ["code-analysis"],
  "hooks": ["pre-commit"],
  "agents": ["security-auditor"]
}
```

---

## Kimi Code 适配

### 配置路径

| 配置项 | Claude Code | Kimi Code |
|--------|-------------|-----------|
| CLI 命令 | `claude plugin` | `kimi plugin` |
| 安装目录 | `.claude/plugins/` | `.kimi/plugins/` |
| 斜杠命令 | `/plugin` | `/plugin` |
| 清单格式 | `manifest.json` | `manifest.json` |

### 快速迁移

```bash
# 1. 在 Kimi Code 中安装相同插件
kimi plugin install pr-review

# 2. 或手动复制插件目录
cp -r .claude/plugins/* .kimi/plugins/
```

### 注意事项

- 插件格式和结构相同
- 大多数插件同时支持 Claude Code 和 Kimi Code
- 可以通过修改插件内的 `CLAUDE.md` 为 `KIMI.md` 来适配
- 社区插件可能优先支持其中一个工具

---

## 最佳实践

| 实践 | 原因 | 示例 |
|------|------|------|
| **单一职责** | 易于理解和使用 | "PR 审查" 而非 "开发工具箱" |
| **版本控制** | 跟踪变更 | 语义化版本 |
| **清晰文档** | 用户知道功能 | 详细的 README |
| **可配置** | 适应不同项目 | 配置选项 |
| **依赖声明** | 避免冲突 | 列出所需工具 |

---

## 故障排除

| 问题 | 检查 | 解决方案 |
|------|------|---------|
| 安装失败 | 网络 | 检查连接或手动安装 |
| 插件未激活 | 清单 | 验证 manifest.json 格式 |
| 命令不可用 | 目录 | 检查安装位置 |
| 与其他插件冲突 | 命名 | 使用唯一名称 |

---

## 下一步

- [学习检查点 →](../08-checkpoints/)
- [探索高级功能 →](../09-advanced-features/)
