<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 📚 Claude Code 学习路线图

**初次接触 Claude Code？** 本指南帮助你按照自己的节奏掌握 Claude Code 的各项功能。无论你是完全的新手还是经验丰富的开发者，都可以先通过下方的自我评估测验找到适合自己的学习起点。

---

## 🧭 找到你的水平

每个人的起点不同。通过这个快速自我评估，找到合适的入门位置。

**请如实回答以下问题：**

- [ ] 我能启动 Claude Code 并进行对话（`claude`）
- [ ] 我已创建或编辑过 CLAUDE.md 文件
- [ ] 我已使用过至少 3 个内置 Slash Commands（如 /help、/compact、/model）
- [ ] 我已创建过自定义 Slash Command 或技能（SKILL.md）
- [ ] 我已配置过 MCP 服务器（如 GitHub、数据库）
- [ ] 我已在 ~/.claude/settings.json 中配置过 Hooks
- [ ] 我已创建或使用过自定义 Subagents（.claude/agents/）
- [ ] 我已使用过 print 模式（`claude -p`）进行脚本或 CI/CD

**你的水平：**

| 勾选数量 | 水平 | 从哪里开始 | 预计完成时间 |
|--------|-------|----------|------------------|
| 0-2 | **第 1 级：初级** — 入门起步 | [里程碑 1A](#里程碑-1a第一个命令与记忆) | 约 3 小时 |
| 3-5 | **第 2 级：中级** — 构建工作流 | [里程碑 2A](#里程碑-2a自动化技能--hooks) | 约 5 小时 |
| 6-8 | **第 3 级：高级** — 高级用户与团队负责人 | [里程碑 3A](#里程碑-3a高级功能) | 约 5 小时 |

> **提示**：如果不确定，可以从低一级开始。快速复习熟悉的内容，总好过漏掉基础概念。

> **交互式版本**：在 Claude Code 中运行 `/self-assessment`，可以进行引导式的交互测验，评估你在所有 10 个功能领域的熟练程度，并生成个性化的学习路径。

---

## 🎯 学习理念

本仓库中的文件夹按**推荐学习顺序**编号，基于三个核心原则：

1. **依赖关系** — 基础概念优先
2. **复杂程度** — 简单功能先于高级功能
3. **使用频率** — 最常用的功能最先学习

这一方式确保你在打好坚实基础的同时，能立即获得生产力提升。

---

## 🗺️ 你的学习路径

```mermaid
graph TD
    Q["🧭 自我评估测验<br/>找到你的水平"] --> L1
    Q --> L2
    Q --> L3

    subgraph L1["🟢 第1级：初级 — 入门起步"]
        direction LR
        A["1A: 第一个命令与记忆<br/>Slash Commands + Memory"] --> B["1B: 安全探索<br/>检查点 + CLI 基础"]
    end

    subgraph L2["🔵 第2级：中级 — 构建工作流"]
        direction LR
        C["2A: 自动化<br/>Skills + Hooks"] --> D["2B: 集成<br/>MCP + Subagents"]
    end

    subgraph L3["🔴 第3级：高级 — 高级用户"]
        direction LR
        E["3A: 高级功能<br/>规划 + 权限"] --> F["3B: 团队与分发<br/>Plugins + CLI 精通"]
    end

    L1 --> L2
    L2 --> L3

    style Q fill:#6A1B9A,color:#fff,stroke:#9C27B0,stroke-width:2px
    style A fill:#2E7D32,color:#fff
    style B fill:#2E7D32,color:#fff
    style C fill:#1565C0,color:#fff
    style D fill:#F57C00,color:#fff
    style E fill:#C62828,color:#fff
    style F fill:#B71C1C,color:#fff
```

**颜色说明：**
- 💜 紫色：自我评估测验
- 🟢 绿色：第 1 级 — 初级路径
- 🔵 蓝色 / 🟡 金色：第 2 级 — 中级路径
- 🔴 红色：第 3 级 — 高级路径

---

## 📊 完整路线图表格

| 步骤 | 功能 | 复杂度 | 时间 | 级别 | 依赖项 | 学习原因 | 核心收益 |
|------|---------|-----------|------|-------|--------------|----------------|--------------|
| **1** | [Slash Commands](01-slash-commands/) | ⭐ 初级 | 30 分钟 | 第 1 级 | 无 | 快速提升生产力（55+ 内置 + 5 个捆绑技能） | 即时自动化、团队规范 |
| **2** | [Memory](02-memory/) | ⭐⭐ 初级+ | 45 分钟 | 第 1 级 | 无 | 所有功能的基础 | 持久化上下文、个人偏好 |
| **3** | [检查点](08-checkpoints/) | ⭐⭐ 中级 | 45 分钟 | 第 1 级 | 会话管理 | 安全探索 | 实验、恢复 |
| **4** | [CLI 基础](10-cli/) | ⭐⭐ 初级+ | 30 分钟 | 第 1 级 | 无 | 核心 CLI 用法 | 交互模式与 print 模式 |
| **5** | [Skills](03-skills/) | ⭐⭐ 中级 | 1 小时 | 第 2 级 | Slash Commands | 自动专业能力 | 可复用能力、一致性 |
| **6** | [Hooks](06-hooks/) | ⭐⭐ 中级 | 1 小时 | 第 2 级 | 工具、命令 | 工作流自动化（25 个事件，4 种类型） | 验证、质量门控 |
| **7** | [MCP](05-mcp/) | ⭐⭐⭐ 中级+ | 1 小时 | 第 2 级 | 配置 | 实时数据访问 | 实时集成、API |
| **8** | [Subagents](04-subagents/) | ⭐⭐⭐ 中级+ | 1.5 小时 | 第 2 级 | Memory、命令 | 处理复杂任务（6 个内置包括 Bash） | 任务委派、专业化 |
| **9** | [高级功能](09-advanced-features/) | ⭐⭐⭐⭐⭐ 高级 | 2-3 小时 | 第 3 级 | 所有前置 | 高级用户工具 | 规划、自动模式、频道、语音输入、权限 |
| **10** | [Plugins](07-plugins/) | ⭐⭐⭐⭐ 高级 | 2 小时 | 第 3 级 | 所有前置 | 完整解决方案 | 团队快速上手、分发 |
| **11** | [CLI 精通](10-cli/) | ⭐⭐⭐ 高级 | 1 小时 | 第 3 级 | 建议：所有 | 掌握命令行用法 | 脚本、CI/CD、自动化 |

**总学习时间**：约 11-13 小时（或直接跳到你的水平节省时间）

---

## 🟢 第 1 级：初级 — 入门起步

**适合**：测验勾选 0-2 项的用户
**时间**：约 3 小时
**重点**：即时生产力提升，理解基础概念
**目标**：成为熟练的日常用户，准备好进入第 2 级

### 里程碑 1A：第一个命令与记忆

**主题**：Slash Commands + Memory
**时间**：1-2 小时
**复杂度**：⭐ 初级
**目标**：通过自定义命令和持久化上下文立即提升生产力

#### 你将实现的目标
✅ 为重复性任务创建自定义 Slash Commands
✅ 为团队规范配置项目记忆
✅ 配置个人偏好
✅ 了解 Claude 如何自动加载上下文

#### 动手练习

```bash
# 练习 1：安装你的第一个 Slash Command
mkdir -p .claude/commands
cp 01-slash-commands/optimize.md .claude/commands/

# 练习 2：创建项目记忆
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 练习 3：实际试用
# 在 Claude Code 中输入：/optimize
```

#### 成功标准
- [ ] 成功调用 `/optimize` 命令
- [ ] Claude 能从 CLAUDE.md 中记住你的项目规范
- [ ] 你了解何时使用 Slash Commands，何时使用 Memory

#### 下一步
完成后请阅读：
- [01-slash-commands/README.md](01-slash-commands/README.md)
- [02-memory/README.md](02-memory/README.md)

> **检验理解程度**：在 Claude Code 中运行 `/lesson-quiz slash-commands` 或 `/lesson-quiz memory` 测试你的学习成果。

---

### 里程碑 1B：安全探索

**主题**：检查点 + CLI 基础
**时间**：1 小时
**复杂度**：⭐⭐ 初级+
**目标**：学会安全地进行实验，并使用核心 CLI 命令

#### 你将实现的目标
✅ 创建并恢复检查点以进行安全实验
✅ 理解交互模式与 print 模式的区别
✅ 使用基本 CLI 标志和选项
✅ 通过管道处理文件

#### 动手练习

```bash
# 练习 1：尝试检查点工作流
# 在 Claude Code 中：
# 做一些实验性修改，然后按 Esc+Esc 或使用 /rewind
# 选择实验之前的检查点
# 选择"恢复代码和对话"以回退

# 练习 2：交互模式与 Print 模式
claude "explain this project"           # 交互模式
claude -p "explain this function"       # Print 模式（非交互）

# 练习 3：通过管道处理文件内容
cat error.log | claude -p "explain this error"
```

#### 成功标准
- [ ] 已创建并回退到检查点
- [ ] 使用了交互模式和 print 模式
- [ ] 向 Claude 管道传输文件进行分析
- [ ] 了解何时使用检查点进行安全实验

#### 下一步
- 阅读：[08-checkpoints/README.md](08-checkpoints/README.md)
- 阅读：[10-cli/README.md](10-cli/README.md)
- **准备好进入第 2 级了！** 前往 [里程碑 2A](#里程碑-2a自动化技能--hooks)

> **检验理解程度**：运行 `/lesson-quiz checkpoints` 或 `/lesson-quiz cli` 确认你已准备好进入第 2 级。

---

## 🔵 第 2 级：中级 — 构建工作流

**适合**：测验勾选 3-5 项的用户
**时间**：约 5 小时
**重点**：自动化、集成、任务委派
**目标**：建立自动化工作流、外部集成，准备好进入第 3 级

### 前置条件检查

开始第 2 级之前，请确保你已熟悉以下第 1 级概念：

- [ ] 能创建和使用 Slash Commands（[01-slash-commands/](01-slash-commands/)）
- [ ] 已通过 CLAUDE.md 配置项目记忆（[02-memory/](02-memory/)）
- [ ] 知道如何创建和恢复检查点（[08-checkpoints/](08-checkpoints/)）
- [ ] 能在命令行使用 `claude` 和 `claude -p`（[10-cli/](10-cli/)）

> **有遗漏？** 请先完成上方链接的教程再继续。

---

### 里程碑 2A：自动化（Skills + Hooks）

**主题**：Skills + Hooks
**时间**：2-3 小时
**复杂度**：⭐⭐ 中级
**目标**：自动化常见工作流和质量检查

#### 你将实现的目标
✅ 通过 YAML 前置元数据自动调用专业能力（包括 `effort` 和 `shell` 字段）
✅ 跨 25 个 Hook 事件配置事件驱动自动化
✅ 使用全部 4 种 Hook 类型（command、http、prompt、agent）
✅ 强制执行代码质量规范
✅ 为自己的工作流创建自定义 Hooks

#### 动手练习

```bash
# 练习 1：安装一个技能
cp -r 03-skills/code-review ~/.claude/skills/

# 练习 2：配置 Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/pre-tool-check.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/pre-tool-check.sh

# 练习 3：在设置中配置 Hooks
# 添加到 ~/.claude/settings.json：
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/pre-tool-check.sh"
          }
        ]
      }
    ]
  }
}
```

#### 成功标准
- [ ] 代码审查技能在相关场景自动触发
- [ ] PreToolUse Hook 在工具执行前运行
- [ ] 你理解技能自动调用与 Hook 事件触发的区别

#### 下一步
- 创建你自己的自定义技能
- 为你的工作流配置更多 Hooks
- 阅读：[03-skills/README.md](03-skills/README.md)
- 阅读：[06-hooks/README.md](06-hooks/README.md)

> **检验理解程度**：运行 `/lesson-quiz skills` 或 `/lesson-quiz hooks` 测试你的知识，然后再继续。

---

### 里程碑 2B：集成（MCP + Subagents）

**主题**：MCP + Subagents
**时间**：2-3 小时
**复杂度**：⭐⭐⭐ 中级+
**目标**：集成外部服务，委派复杂任务

#### 你将实现的目标
✅ 从 GitHub、数据库等访问实时数据
✅ 将工作委派给专业 AI 代理
✅ 了解何时使用 MCP 而非 Subagents
✅ 构建集成工作流

#### 动手练习

```bash
# 练习 1：配置 GitHub MCP
export GITHUB_TOKEN="your_github_token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 练习 2：测试 MCP 集成
# 在 Claude Code 中：/mcp__github__list_prs

# 练习 3：安装 Subagents
mkdir -p .claude/agents
cp 04-subagents/*.md .claude/agents/
```

#### 集成练习
尝试以下完整工作流：
1. 使用 MCP 获取一个 GitHub PR
2. 让 Claude 将审查委派给 code-reviewer subagent
3. 使用 Hooks 自动运行测试

#### 成功标准
- [ ] 成功通过 MCP 查询 GitHub 数据
- [ ] Claude 将复杂任务委派给 Subagents
- [ ] 你了解 MCP 与 Subagents 的区别
- [ ] 在工作流中结合使用 MCP + Subagents + Hooks

#### 下一步
- 配置更多 MCP 服务器（数据库、Slack 等）
- 为你的领域创建自定义 Subagents
- 阅读：[05-mcp/README.md](05-mcp/README.md)
- 阅读：[04-subagents/README.md](04-subagents/README.md)
- **准备好进入第 3 级了！** 前往 [里程碑 3A](#里程碑-3a高级功能)

> **检验理解程度**：运行 `/lesson-quiz mcp` 或 `/lesson-quiz subagents` 确认你已准备好进入第 3 级。

---

## 🔴 第 3 级：高级 — 高级用户与团队负责人

**适合**：测验勾选 6-8 项的用户
**时间**：约 5 小时
**重点**：团队工具、CI/CD、企业功能、插件开发
**目标**：成为高级用户，能够搭建团队工作流和 CI/CD

### 前置条件检查

开始第 3 级之前，请确保你已熟悉以下第 2 级概念：

- [ ] 能创建和使用带自动触发的技能（[03-skills/](03-skills/)）
- [ ] 已为事件驱动自动化配置 Hooks（[06-hooks/](06-hooks/)）
- [ ] 能为外部数据配置 MCP 服务器（[05-mcp/](05-mcp/)）
- [ ] 知道如何使用 Subagents 进行任务委派（[04-subagents/](04-subagents/)）

> **有遗漏？** 请先完成上方链接的教程再继续。

---

### 里程碑 3A：高级功能

**主题**：高级功能（规划、权限、扩展思考、自动模式、频道、语音输入、远程/桌面/Web）
**时间**：2-3 小时
**复杂度**：⭐⭐⭐⭐⭐ 高级
**目标**：掌握高级工作流和高级用户工具

#### 你将实现的目标
✅ 针对复杂功能使用规划模式
✅ 通过 6 种模式进行细粒度权限控制（default、acceptEdits、plan、auto、dontAsk、bypassPermissions）
✅ 通过 Alt+T / Option+T 切换扩展思考
✅ 后台任务管理
✅ 通过自动记忆学习个人偏好
✅ 带后台安全分类器的自动模式
✅ 结构化多会话工作流的频道功能
✅ 免手动操作的语音输入
✅ 远程控制、桌面应用和 Web 会话
✅ 多代理协作的代理团队

#### 动手练习

```bash
# 练习 1：使用规划模式
/plan Implement user authentication system

# 练习 2：尝试权限模式（6 种：default、acceptEdits、plan、auto、dontAsk、bypassPermissions）
claude --permission-mode plan "analyze this codebase"
claude --permission-mode acceptEdits "refactor the auth module"
claude --permission-mode auto "implement the feature"

# 练习 3：启用扩展思考
# 在会话中按 Alt+T（macOS 上按 Option+T）进行切换

# 练习 4：高级检查点工作流
# 1. 创建检查点"干净状态"
# 2. 使用规划模式设计功能
# 3. 通过 Subagent 委派实现
# 4. 在后台运行测试
# 5. 如果测试失败，回退到检查点
# 6. 尝试替代方案

# 练习 5：尝试自动模式（后台安全分类器）
claude --permission-mode auto "implement user settings page"

# 练习 6：启用代理团队
export CLAUDE_AGENT_TEAMS=1
# 向 Claude 说："Implement feature X using a team approach"

# 练习 7：定时任务
/loop 5m /check-status
# 或使用 CronCreate 创建持久化定时任务

# 练习 8：使用频道进行多会话工作流
# 使用频道跨会话组织工作

# 练习 9：语音输入
# 使用语音输入与 Claude Code 进行免手动操作的交互
```

#### 成功标准
- [ ] 为复杂功能使用了规划模式
- [ ] 配置了权限模式（plan、acceptEdits、auto、dontAsk）
- [ ] 通过 Alt+T / Option+T 切换了扩展思考
- [ ] 使用了带后台安全分类器的自动模式
- [ ] 为长时间操作使用了后台任务
- [ ] 探索了频道功能用于多会话工作流
- [ ] 尝试了语音输入进行免手动操作
- [ ] 了解远程控制、桌面应用和 Web 会话
- [ ] 启用并使用了代理团队进行协作任务
- [ ] 使用 `/loop` 进行周期性任务或定时监控

#### 下一步
- 阅读：[09-advanced-features/README.md](09-advanced-features/README.md)

> **检验理解程度**：运行 `/lesson-quiz advanced` 测试你对高级用户功能的掌握程度。

---

### 里程碑 3B：团队与分发（Plugins + CLI 精通）

**主题**：Plugins + CLI 精通 + CI/CD
**时间**：2-3 小时
**复杂度**：⭐⭐⭐⭐ 高级
**目标**：构建团队工具、创建插件、掌握 CI/CD 集成

#### 你将实现的目标
✅ 安装和创建完整的捆绑插件
✅ 掌握用于脚本和自动化的 CLI
✅ 使用 `claude -p` 配置 CI/CD 集成
✅ 为自动化流水线生成 JSON 输出
✅ 会话管理和批量处理

#### 动手练习

```bash
# 练习 1：安装完整插件
# 在 Claude Code 中：/plugin install pr-review

# 练习 2：CI/CD 的 print 模式
claude -p "Run all tests and generate report"

# 练习 3：为脚本生成 JSON 输出
claude -p --output-format json "list all functions"

# 练习 4：会话管理与恢复
claude -r "feature-auth" "continue implementation"

# 练习 5：带约束的 CI/CD 集成
claude -p --max-turns 3 --output-format json "review code"

# 练习 6：批量处理
for file in *.md; do
  claude -p --output-format json "summarize this: $(cat $file)" > ${file%.md}.summary.json
done
```

#### CI/CD 集成练习
创建一个简单的 CI/CD 脚本：
1. 使用 `claude -p` 审查变更文件
2. 将结果输出为 JSON
3. 使用 `jq` 处理特定问题
4. 集成到 GitHub Actions 工作流

#### 成功标准
- [ ] 安装并使用了插件
- [ ] 为团队构建或修改了插件
- [ ] 在 CI/CD 中使用了 print 模式（`claude -p`）
- [ ] 为脚本生成了 JSON 输出
- [ ] 成功恢复了之前的会话
- [ ] 创建了批量处理脚本
- [ ] 将 Claude 集成到 CI/CD 工作流

#### CLI 的真实使用场景
- **代码审查自动化**：在 CI/CD 流水线中运行代码审查
- **日志分析**：分析错误日志和系统输出
- **文档生成**：批量生成文档
- **测试洞察**：分析测试失败
- **性能分析**：审查性能指标
- **数据处理**：转换和分析数据文件

#### 下一步
- 阅读：[07-plugins/README.md](07-plugins/README.md)
- 阅读：[10-cli/README.md](10-cli/README.md)
- 创建团队级别的 CLI 快捷方式和插件
- 配置批量处理脚本

> **检验理解程度**：运行 `/lesson-quiz plugins` 或 `/lesson-quiz cli` 确认你的掌握程度。

---

## 🧪 测试你的知识

本仓库包含两个交互式技能，你可以在 Claude Code 中随时使用，以评估你的理解程度：

| 技能 | 命令 | 用途 |
|-------|---------|---------|
| **自我评估** | `/self-assessment` | 评估你在所有 10 个功能领域的整体熟练程度。选择快速模式（2 分钟）或深度模式（5 分钟），获取个性化技能档案和学习路径。 |
| **课程测验** | `/lesson-quiz [课程]` | 通过 10 道题测试你对特定课程的理解。可在课程前（预测）、期间（进度检查）或之后（掌握验证）使用。 |

**示例：**
```
/self-assessment                  # 找到你的整体水平
/lesson-quiz hooks                # 课程 06：Hooks 的测验
/lesson-quiz 03                   # 课程 03：Skills 的测验
/lesson-quiz advanced-features    # 课程 09 的测验
```

---

## ⚡ 快速开始路径

### 如果你只有 15 分钟
**目标**：获得第一个成果

1. 复制一个 Slash Command：`cp 01-slash-commands/optimize.md .claude/commands/`
2. 在 Claude Code 中试用：`/optimize`
3. 阅读：[01-slash-commands/README.md](01-slash-commands/README.md)

**成果**：你将拥有一个可用的 Slash Command，并了解基础知识

---

### 如果你有 1 小时
**目标**：配置核心生产力工具

1. **Slash Commands**（15 分钟）：复制并测试 `/optimize` 和 `/pr`
2. **项目记忆**（15 分钟）：按项目规范创建 CLAUDE.md
3. **安装技能**（15 分钟）：配置 code-review 技能
4. **综合试用**（15 分钟）：观察它们如何协同工作

**成果**：通过命令、记忆和自动技能获得基础生产力提升

---

### 如果你有一个周末
**目标**：熟练掌握大多数功能

**周六上午**（3 小时）：
- 完成里程碑 1A：Slash Commands + Memory
- 完成里程碑 1B：检查点 + CLI 基础

**周六下午**（3 小时）：
- 完成里程碑 2A：Skills + Hooks
- 完成里程碑 2B：MCP + Subagents

**周日**（4 小时）：
- 完成里程碑 3A：高级功能
- 完成里程碑 3B：Plugins + CLI 精通 + CI/CD
- 为团队构建自定义插件

**成果**：你将成为 Claude Code 高级用户，能够培训他人并自动化复杂工作流

---

## 💡 学习建议

### ✅ 应该做

- **先参加测验**，找到你的起点
- **完成每个里程碑的动手练习**
- **从简单开始**，逐步增加复杂度
- **测试每个功能**，再进入下一个
- **做笔记**，记录适合你工作流的内容
- **回顾**早期概念，学习高级主题时加深理解
- **使用检查点安全地进行实验**
- **与团队分享知识**

### ❌ 不应该做

- **跳过前置条件检查**，直接进入更高级别
- **试图一次学习所有内容** — 这会让人不知所措
- **不理解就复制配置** — 出问题时你不知道如何调试
- **忘记测试** — 始终验证功能是否正常运行
- **急于完成里程碑** — 花时间去理解
- **忽略文档** — 每个 README 都有有价值的细节
- **孤立学习** — 与队友讨论

---

## 🎓 学习风格

### 视觉型学习者
- 研究每个 README 中的 Mermaid 图表
- 观察命令执行流程
- 画出你自己的工作流图
- 使用上方的可视化学习路径

### 动手型学习者
- 完成每一个动手练习
- 尝试不同的变体
- 打破然后修复它们（使用检查点！）
- 创建你自己的示例

### 阅读型学习者
- 仔细阅读每个 README
- 研究代码示例
- 查看对比表格
- 阅读资源中链接的博客文章

### 社交型学习者
- 设立结对编程会话
- 向队友讲解概念
- 参与 Claude Code 社区讨论
- 分享你的自定义配置

---

## 📈 进度跟踪

使用以下清单按级别跟踪你的进度。随时运行 `/self-assessment` 获取最新技能档案，或在每个教程完成后运行 `/lesson-quiz [课程]` 验证你的理解。

### 🟢 第 1 级：初级
- [ ] 完成 [01-slash-commands](01-slash-commands/)
- [ ] 完成 [02-memory](02-memory/)
- [ ] 创建了第一个自定义 Slash Command
- [ ] 配置了项目记忆
- [ ] **里程碑 1A 达成**
- [ ] 完成 [08-checkpoints](08-checkpoints/)
- [ ] 完成 [10-cli](10-cli/) 基础
- [ ] 创建并回退到检查点
- [ ] 使用了交互模式和 print 模式
- [ ] **里程碑 1B 达成**

### 🔵 第 2 级：中级
- [ ] 完成 [03-skills](03-skills/)
- [ ] 完成 [06-hooks](06-hooks/)
- [ ] 安装了第一个技能
- [ ] 配置了 PreToolUse Hook
- [ ] **里程碑 2A 达成**
- [ ] 完成 [05-mcp](05-mcp/)
- [ ] 完成 [04-subagents](04-subagents/)
- [ ] 连接了 GitHub MCP
- [ ] 创建了自定义 Subagent
- [ ] 在工作流中结合了多种集成
- [ ] **里程碑 2B 达成**

### 🔴 第 3 级：高级
- [ ] 完成 [09-advanced-features](09-advanced-features/)
- [ ] 成功使用了规划模式
- [ ] 配置了权限模式（6 种，包括 auto）
- [ ] 使用了带安全分类器的自动模式
- [ ] 使用了扩展思考切换
- [ ] 探索了频道和语音输入
- [ ] **里程碑 3A 达成**
- [ ] 完成 [07-plugins](07-plugins/)
- [ ] 完成 [10-cli](10-cli/) 高级用法
- [ ] 配置了 print 模式（`claude -p`）CI/CD
- [ ] 为自动化创建了 JSON 输出
- [ ] 将 Claude 集成到 CI/CD 流水线
- [ ] 创建了团队插件
- [ ] **里程碑 3B 达成**

---

## 🆘 常见学习挑战

### 挑战 1："概念太多，一次接受不了"
**解决方案**：每次专注一个里程碑。完成所有练习后再继续。

### 挑战 2："不知道什么情况下该用哪个功能"
**解决方案**：参考主 README 中的[使用场景矩阵](README.md#use-case-matrix)。

### 挑战 3："配置不起作用"
**解决方案**：查看[故障排除](README.md#troubleshooting)部分，验证文件位置是否正确。

### 挑战 4："概念之间感觉有重叠"
**解决方案**：查看[功能对比](README.md#feature-comparison)表格，了解各功能的区别。

### 挑战 5："记不住所有内容"
**解决方案**：创建你自己的备忘单。使用检查点安全地进行实验。

### 挑战 6："我有经验，但不确定从哪里开始"
**解决方案**：参加上方的[自我评估测验](#-找到你的水平)。跳到你的级别，并使用前置条件检查找出任何遗漏。

---

## 🎯 完成后的下一步

完成所有里程碑后：

1. **创建团队文档** — 记录团队的 Claude Code 配置
2. **构建自定义插件** — 将团队工作流打包
3. **探索远程控制** — 从外部工具以编程方式控制 Claude Code 会话
4. **尝试 Web 会话** — 通过基于浏览器的界面使用 Claude Code 进行远程开发
5. **使用桌面应用** — 通过原生桌面应用访问 Claude Code 功能
6. **使用自动模式** — 让 Claude 在后台安全分类器的支持下自主工作
7. **利用自动记忆** — 让 Claude 随时间自动学习你的偏好
8. **配置代理团队** — 协调多个代理处理复杂的多方面任务
9. **使用频道** — 跨结构化多会话工作流组织工作
10. **尝试语音输入** — 使用免手动语音输入与 Claude Code 交互
11. **使用定时任务** — 通过 `/loop` 和 cron 工具自动化周期性检查
12. **贡献示例** — 与社区分享
13. **辅导他人** — 帮助队友学习
14. **优化工作流** — 基于实际使用持续改进
15. **保持更新** — 关注 Claude Code 发布和新功能

---

## 📚 附加资源

### 官方文档
- [Claude Code 文档](https://code.claude.com/docs/en/overview)
- [Anthropic 文档](https://docs.anthropic.com)
- [MCP 协议规范](https://modelcontextprotocol.io)

### 博客文章
- [发现 Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

### 社区
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [MCP Servers 仓库](https://github.com/modelcontextprotocol/servers)

---

## 💬 反馈与支持

- **发现问题？** 在仓库中创建 Issue
- **有建议？** 提交 Pull Request
- **需要帮助？** 查看文档或向社区提问

---

**最后更新**：2026 年 3 月
**维护者**：Claude How-To 贡献者
**许可证**：教育目的，可免费使用和改编

---

[← 返回主 README](README.md)
