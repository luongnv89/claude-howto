<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 插件

这个目录包含一组完整的插件示例，它们把多个 Claude Code 功能打包成可安装的一体化方案。

## 介绍

Claude Code 插件是把 slash commands、subagents、MCP servers 和 hooks 组合在一起的功能集合，可以通过一条命令安装。它们代表了 Claude Code 最高级别的扩展方式，把多个功能整合成可共享、可复用的完整方案。

## 概览

一个插件通常会把以下能力打包在一起：

- slash commands
- subagents
- MCP servers
- hooks

这样做的好处是：

- 一次安装即可使用完整工作流
- 团队共享更容易
- 配置更统一
- 便于版本控制和分发

## 插件架构

```mermaid
graph TB
    A["插件"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|打包| B
    A -->|打包| C
    A -->|打包| D
    A -->|打包| E
    A -->|打包| F
```

## 插件类型与分发

| 类型 | 范围 | 共享对象 | 维护者 | 示例 |
|------|------|----------|--------|------|
| 官方 | 全局 | 所有用户 | Anthropic | PR 审查、安全指导 |
| 社区 | 公开 | 所有用户 | 社区 | DevOps、数据科学 |
| 组织 | 内部 | 团队成员 | 公司 | 内部规范、工具 |
| 个人 | 个人 | 单个用户 | 开发者 | 自定义工作流 |

## 插件定义结构

插件清单使用 `.claude-plugin/plugin.json` 中的 JSON 格式：

```json
{
  "name": "my-first-plugin",
  "description": "一个问候插件",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  },
  "homepage": "https://example.com",
  "repository": "https://github.com/user/repo",
  "license": "MIT"
}
```

## 插件结构示例

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json       # 清单（名称、描述、版本、作者）
├── commands/             # 以 Markdown 文件形式存放的命令
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/               # 自定义 agent 定义
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/               # 带有 SKILL.md 文件的技能
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/                # hooks.json 中的事件处理器
│   └── hooks.json
├── .mcp.json             # MCP server 配置
├── .lsp.json             # LSP server 配置
├── settings.json         # 默认设置
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### LSP server 配置

插件可以包含 Language Server Protocol（LSP）支持，以获得实时代码智能。LSP server 会在你编写代码时提供诊断、代码导航和符号信息。

**配置位置**：
- 插件根目录中的 `.lsp.json` 文件
- `plugin.json` 中的内联 `lsp` 键

#### 字段参考

| 字段 | 必填 | 说明 |
|------|------|------|
| `command` | 是 | LSP server 可执行文件（必须在 PATH 中） |
| `extensionToLanguage` | 是 | 将文件扩展名映射到语言 ID |
| `args` | 否 | server 的命令行参数 |
| `transport` | 否 | 通信方式：`stdio`（默认）或 `socket` |
| `env` | 否 | server 进程的环境变量 |
| `initializationOptions` | 否 | LSP 初始化期间发送的选项 |
| `settings` | 否 | 传递给 server 的工作区配置 |
| `workspaceFolder` | 否 | 覆盖工作区文件夹路径 |
| `startupTimeout` | 否 | 等待 server 启动的最长时间（毫秒） |
| `shutdownTimeout` | 否 | 优雅关闭的最长时间（毫秒） |
| `restartOnCrash` | 否 | server 崩溃时自动重启 |
| `maxRestarts` | 否 | 放弃前的最大重启次数 |

#### 示例配置

**Go（gopls）**：

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**Python（pyright）**：

```json
{
  "python": {
    "command": "pyright-langserver",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".py": "python",
      ".pyi": "python"
    }
  }
}
```

**TypeScript**：

```json
{
  "typescript": {
    "command": "typescript-language-server",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".ts": "typescript",
      ".tsx": "typescriptreact",
      ".js": "javascript",
      ".jsx": "javascriptreact"
    }
  }
}
```

#### 可用的 LSP 插件

官方市场包含了预配置好的 LSP 插件：

| 插件 | 语言 | Server Binary | 安装命令 |
|------|------|---------------|----------|
| `pyright-lsp` | Python | `pyright-langserver` | `pip install pyright` |
| `typescript-lsp` | TypeScript/JavaScript | `typescript-language-server` | `npm install -g typescript-language-server typescript` |
| `rust-lsp` | Rust | `rust-analyzer` | 使用 `rustup component add rust-analyzer` 安装 |

#### LSP 能力

配置完成后，LSP server 会提供：

- **即时诊断** - 编辑后立即显示错误和警告
- **代码导航** - 跳转到定义、查找引用和实现
- **悬浮信息** - 在悬停时查看类型签名和文档
- **符号列表** - 浏览当前文件或工作区中的符号

## 插件选项（v2.1.83+）

插件可以在清单中通过 `userConfig` 声明用户可配置选项。标记为 `sensitive: true` 的值会存储在系统钥匙串中，而不是明文设置文件里：

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "userConfig": {
    "apiKey": {
      "description": "服务的 API key",
      "sensitive": true
    },
    "region": {
      "description": "部署区域",
      "default": "us-east-1"
    }
  }
}
```

## 持久化插件数据（`${CLAUDE_PLUGIN_DATA}`）（v2.1.78+）

插件可以通过 `${CLAUDE_PLUGIN_DATA}` 环境变量访问一个持久化状态目录。这个目录对每个插件都是唯一的，并且会跨会话保留，适合缓存、数据库和其他持久化状态：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "command": "node ${CLAUDE_PLUGIN_DATA}/track-usage.js"
      }
    ]
  }
}
```

插件安装时会自动创建该目录。存放在这里的文件会一直保留，直到插件被卸载。

## 通过设置文件内联定义插件（`source: 'settings'`）（v2.1.80+）

插件可以在设置文件中以内联市场条目的方式定义，使用 `source: 'settings'` 字段即可。这允许你直接嵌入插件定义，而不必单独准备仓库或市场：

```json
{
  "pluginMarketplaces": [
    {
      "name": "inline-tools",
      "source": "settings",
      "plugins": [
        {
          "name": "quick-lint",
          "source": "./local-plugins/quick-lint"
        }
      ]
    }
  ]
}
```

## 插件设置

插件可以提供一个 `settings.json` 文件来定义默认配置。目前支持 `agent` 键，用来指定插件的主线程 agent：

```json
{
  "agent": "agents/specialist-1.md"
}
```

当插件包含 `settings.json` 时，这些默认值会在安装时自动应用。用户也可以在自己的项目或用户级配置中覆盖它们。

## 独立命令 vs 插件方式

| 方式 | 命令名称 | 配置方式 | 最适合 |
|------|----------|----------|--------|
| **独立命令** | `/hello` | 在 `CLAUDE.md` 中手动设置 | 个人、项目专用 |
| **插件** | `/plugin-name:hello` | 通过 `plugin.json` 自动配置 | 共享、分发、团队使用 |

对于快速的个人工作流，使用 **独立 slash commands**。当你想打包多个功能、与团队共享或者发布分发时，使用 **插件**。

## 实际示例

### 示例 1：PR 审查插件

**文件：** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "包含安全、测试和文档检查的完整 PR 审查工作流",
  "author": {
    "name": "Anthropic"
  },
  "repository": "https://github.com/your-org/pr-review",
  "license": "MIT"
}
```

**文件：** `commands/review-pr.md`

```markdown
---
name: Review PR
description: 启动包含安全和测试检查的完整 PR 审查
---

# PR Review

这个命令会启动一次完整的 Pull Request 审查，包括：

1. 安全分析
2. 测试覆盖率验证
3. 文档更新
4. 代码质量检查
5. 性能影响评估
```

**文件：** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: 面向安全的代码审查
tools: read, grep, diff
---

# Security Reviewer

专注于发现安全漏洞：
- 身份验证/授权问题
- 数据暴露
- 注入攻击
- 安全配置
```

**安装：**

```bash
/plugin install pr-review

# 结果：
# ✅ 已安装 3 个 slash commands
# ✅ 已配置 3 个 subagents
# ✅ 已连接 2 个 MCP servers
# ✅ 已注册 4 个 hooks
# ✅ 可以直接使用！
```

### 示例 2：DevOps 插件

**组件：**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

### 示例 3：文档插件

**打包组件：**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

## 插件市场

Anthropic 官方维护的插件目录是 `anthropics/claude-plugins-official`。企业管理员也可以创建私有插件市场用于内部分发。

```mermaid
graph TB
    A["插件市场"]
    B["官方<br/>anthropics/claude-plugins-official"]
    C["社区<br/>市场"]
    D["企业<br/>私有仓库"]

    A --> B
    A --> C
    A --> D

    B -->|分类| B1["开发"]
    B -->|分类| B2["DevOps"]
    B -->|分类| B3["文档"]

    C -->|搜索| C1["DevOps 自动化"]
    C -->|搜索| C2["移动开发"]
    C -->|搜索| C3["数据科学"]

    D -->|内部| D1["公司规范"]
    D -->|内部| D2["遗留系统"]
    D -->|内部| D3["合规"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#e8f5e9,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#fff3e0,stroke:#333,color:#333
```

### 市场配置

企业和高级用户可以通过设置来控制市场行为：

| 设置 | 说明 |
|------|------|
| `extraKnownMarketplaces` | 在默认列表之外添加额外的市场源 |
| `strictKnownMarketplaces` | 控制允许用户添加哪些市场 |
| `deniedPlugins` | 管理员维护的黑名单，阻止特定插件被安装 |

### 额外的市场特性

- **默认 git 超时**：对大型插件仓库从 30 秒增加到 120 秒
- **自定义 npm registry**：插件可以指定自定义 npm registry URL 用于依赖解析
- **版本锁定**：将插件锁定到特定版本，以获得可复现的环境

### 市场定义 schema

插件市场定义在 `.claude-plugin/marketplace.json` 中：

```json
{
  "name": "my-team-plugins",
  "owner": "my-org",
  "plugins": [
    {
      "name": "code-standards",
      "source": "./plugins/code-standards",
      "description": "强制执行团队编码规范",
      "version": "1.2.0",
      "author": "platform-team"
    },
    {
      "name": "deploy-helper",
      "source": {
        "source": "github",
        "repo": "my-org/deploy-helper",
        "ref": "v2.0.0"
      },
      "description": "部署自动化工作流"
    }
  ]
}
```

| 字段 | 必填 | 说明 |
|------|------|------|
| `name` | 是 | 使用 kebab-case 的市场名称 |
| `owner` | 是 | 维护该市场的组织或用户 |
| `plugins` | 是 | 插件条目数组 |
| `plugins[].name` | 是 | 插件名称（kebab-case） |
| `plugins[].source` | 是 | 插件来源（路径字符串或来源对象） |
| `plugins[].description` | 否 | 插件的简要描述 |
| `plugins[].version` | 否 | 语义化版本字符串 |
| `plugins[].author` | 否 | 插件作者名称 |

### 插件来源类型

插件可以来自多个位置：

| 来源 | 语法 | 示例 |
|------|------|------|
| **相对路径** | 字符串路径 | `"./plugins/my-plugin"` |
| **GitHub** | `{ "source": "github", "repo": "owner/repo" }` | `{ "source": "github", "repo": "acme/lint-plugin", "ref": "v1.0" }` |
| **Git URL** | `{ "source": "url", "url": "..." }` | `{ "source": "url", "url": "https://git.internal/plugin.git" }` |
| **Git 子目录** | `{ "source": "git-subdir", "url": "...", "path": "..." }` | `{ "source": "git-subdir", "url": "https://github.com/org/monorepo.git", "path": "packages/plugin" }` |
| **npm** | `{ "source": "npm", "package": "..." }` | `{ "source": "npm", "package": "@acme/claude-plugin", "version": "^2.0" }` |
| **pip** | `{ "source": "pip", "package": "..." }` | `{ "source": "pip", "package": "claude-data-plugin", "version": ">=1.0" }` |

GitHub 和 git 来源支持可选的 `ref`（分支/标签）和 `sha`（提交哈希）字段用于版本锁定。

### 分发方式

**GitHub（推荐）**：
```bash
# 用户添加你的市场
/plugin marketplace add owner/repo-name
```

**其他 git 服务**（需要完整 URL）：
```bash
/plugin marketplace add https://gitlab.com/org/marketplace-repo.git
```

**私有仓库**：可以通过 git credential helper 或环境令牌支持。用户必须有该仓库的读取权限。

**官方市场提交**：可以将插件提交到 Anthropic 审核维护的市场，以便更广泛分发。

### 严格模式

控制市场定义与本地 `plugin.json` 文件的交互方式：

| 设置 | 行为 |
|------|------|
| `strict: true`（默认） | 本地 `plugin.json` 为权威来源；市场条目会对其进行补充 |
| `strict: false` | 市场条目就是完整的插件定义 |

**配合 `strictKnownMarketplaces` 的组织限制**：

| 值 | 效果 |
|----|------|
| 未设置 | 无限制，用户可以添加任意市场 |
| 空数组 `[]` | 锁定模式，不允许任何市场 |
| 模式数组 | 白名单模式，只允许匹配的市场被添加 |

```json
{
  "strictKnownMarketplaces": [
    "my-org/*",
    "github.com/trusted-vendor/*"
  ]
}
```

> **警告**：在带有 `strictKnownMarketplaces` 的严格模式下，用户只能从白名单市场安装插件。这适用于需要受控插件分发的企业环境。

## 插件安装与生命周期

```mermaid
graph LR
    A["发现"] -->|浏览| B["市场"]
    B -->|选择| C["插件页"]
    C -->|查看| D["组件"]
    D -->|安装| E["/plugin install"]
    E -->|解包| F["配置"]
    F -->|激活| G["使用"]
    G -->|检查| H["更新"]
    H -->|可用| G
    G -->|完成| I["禁用"]
    I -->|稍后| J["启用"]
    J -->|返回| G
```

## 插件能力对比

| 功能 | Slash Command | Skill | Subagent | Plugin |
|------|---------------|-------|----------|--------|
| **安装** | 手动复制 | 手动复制 | 手动配置 | 一条命令 |
| **设置时间** | 5 分钟 | 10 分钟 | 15 分钟 | 2 分钟 |
| **打包** | 单文件 | 单文件 | 单文件 | 多文件 |
| **版本管理** | 手动 | 手动 | 手动 | 自动 |
| **团队共享** | 复制文件 | 复制文件 | 复制文件 | 安装 ID |
| **更新** | 手动 | 手动 | 手动 | 自动可用 |
| **依赖** | 无 | 无 | 无 | 可能包含 |
| **市场** | 否 | 否 | 否 | 是 |
| **分发** | 仓库 | 仓库 | 仓库 | 市场 |

## 插件 CLI 命令

所有插件操作都可以通过 CLI 命令完成：

```bash
claude plugin install <name>@<marketplace>   # 从市场安装
claude plugin uninstall <name>               # 删除插件
claude plugin list                           # 列出已安装插件
claude plugin enable <name>                  # 启用已禁用的插件
claude plugin disable <name>                 # 禁用插件
claude plugin validate                       # 验证插件结构
```

## 安装方式

### 从市场安装
```bash
/plugin install plugin-name
# 或通过 CLI：
claude plugin install plugin-name@marketplace-name
```

### 启用 / 禁用（自动检测作用域）
```bash
/plugin enable plugin-name
/plugin disable plugin-name
```

### 本地插件（用于开发）
```bash
# 本地测试的 CLI 参数（可重复指定多个插件）
claude --plugin-dir ./path/to/plugin
claude --plugin-dir ./plugin-a --plugin-dir ./plugin-b
```

### 从 Git 仓库安装
```bash
/plugin install github:username/repo
```

## 何时创建插件

```mermaid
graph TD
    A["我该创建插件吗？"]
    A -->|需要多个组件| B{"多个命令<br/>或 subagents<br/>或 MCPs?"}
    B -->|是| C["✅ 创建插件"]
    B -->|否| D["使用单独功能"]
    A -->|团队工作流| E{"要和<br/>团队共享吗？"}
    E -->|是| C
    E -->|否| F["保持本地配置"]
    A -->|复杂设置| G{"需要自动<br/>配置吗？"}
    G -->|是| C
    G -->|否| D
```

### 插件适用场景

| 场景 | 建议 | 原因 |
|------|------|------|
| **团队入职** | ✅ 使用插件 | 即时安装，包含所有配置 |
| **框架初始化** | ✅ 使用插件 | 打包框架专属命令 |
| **企业规范** | ✅ 使用插件 | 集中分发，版本控制 |
| **快速任务自动化** | ❌ 使用命令 | 太重 |
| **单一领域能力** | ❌ 使用 Skill | 太重，直接用 skill 更合适 |
| **专门化分析** | ❌ 使用 Subagent | 可手动创建，或用 skill |
| **实时数据访问** | ❌ 使用 MCP | 独立使用，不要打包 |

## 测试插件

在发布前，使用 `--plugin-dir` CLI 参数在本地测试插件（可以重复指定多个插件）：

```bash
claude --plugin-dir ./my-plugin
claude --plugin-dir ./my-plugin --plugin-dir ./another-plugin
```

这会用已加载插件启动 Claude Code，让你可以：
- 验证所有 slash commands 是否可用
- 测试 subagents 和 agents 是否正常工作
- 确认 MCP servers 能正确连接
- 验证 hooks 的执行
- 检查 LSP server 配置
- 检查是否有配置错误

## 热重载

插件支持开发期间的热重载。当你修改插件文件时，Claude Code 可以自动检测变化。你也可以手动触发重载：

```bash
/reload-plugins
```

这会重新读取所有插件清单、commands、agents、skills、hooks 以及 MCP/LSP 配置，而无需重启会话。

## 插件托管设置

管理员可以使用托管设置在组织范围内控制插件行为：

| 设置 | 说明 |
|------|------|
| `enabledPlugins` | 默认启用的插件白名单 |
| `deniedPlugins` | 不允许安装的插件黑名单 |
| `extraKnownMarketplaces` | 在默认列表之外添加额外市场源 |
| `strictKnownMarketplaces` | 限制用户允许添加的市场 |
| `allowedChannelPlugins` | 控制每个发布渠道允许使用哪些插件 |

这些设置可以通过托管配置文件应用到组织级别，并且优先于用户级设置。

## 插件安全

插件 subagents 运行在受限沙箱中。以下 frontmatter 键在插件 subagent 定义中**不允许**使用：

- `hooks` - subagents 不能注册事件处理器
- `mcpServers` - subagents 不能配置 MCP servers
- `permissionMode` - subagents 不能覆盖权限模型

这可以确保插件不会越权，也不会修改主机环境的作用范围。

## 发布插件

**发布步骤：**

1. 使用所有组件创建插件结构
2. 编写 `.claude-plugin/plugin.json` 清单
3. 创建带文档的 `README.md`
4. 使用 `claude --plugin-dir ./my-plugin` 在本地测试
5. 提交到插件市场
6. 经过审查和批准
7. 发布到市场
8. 用户即可一条命令安装

**示例提交：**

```markdown
# PR 审查插件

## 描述
包含安全、测试和文档检查的完整 PR 审查工作流。

## 包含内容
- 3 个用于不同审查类型的 slash commands
- 3 个专门化 subagents
- GitHub 和 CodeQL MCP 集成
- 自动安全扫描 hooks

## 安装
```bash
/plugin install pr-review
```

## 功能
✅ 安全分析
✅ 测试覆盖率检查
✅ 文档校验
✅ 代码质量评估
✅ 性能影响分析

## 使用
```bash
/review-pr
/check-security
/check-tests
```

## 要求
- Claude Code 1.0+
- GitHub 访问权限
- CodeQL（可选）
```

## 插件 vs 手动配置

**手动设置（2+ 小时）：**
- 逐个安装 slash commands
- 单独创建 subagents
- 分别配置 MCP
- 手动设置 hooks
- 记录所有内容
- 和团队共享（希望他们能配对）

**使用插件（2 分钟）：**
```bash
/plugin install pr-review
# ✅ 一切都已安装并配置
# ✅ 可以立即使用
# ✅ 团队可以复现完全相同的设置
```

## 最佳实践

### 应该做的 ✅
- 使用清晰、描述性的插件名
- 提供完整 README
- 正确使用语义化版本（semver）
- 一起测试所有组件
- 清楚记录依赖和要求
- 提供使用示例
- 包含错误处理
- 为发现性添加合适标签
- 保持向后兼容
- 保持插件聚焦且一致
- 包含完整测试
- 记录所有依赖

### 不要做的 ❌
- 不要打包无关功能
- 不要硬编码凭据
- 不要跳过测试
- 不要忘记文档
- 不要创建冗余插件
- 不要忽略版本管理
- 不要把组件依赖搞得过于复杂
- 不要忘记优雅处理错误

## 安装说明

### 从市场安装

1. **浏览可用插件：**
   ```bash
   /plugin list
   ```

2. **查看插件详情：**
   ```bash
   /plugin info plugin-name
   ```

3. **安装插件：**
   ```bash
   /plugin install plugin-name
   ```

### 从本地路径安装

```bash
/plugin install ./path/to/plugin-directory
```

### 从 GitHub 安装

```bash
/plugin install github:username/repo
```

### 列出已安装插件

```bash
/plugin list --installed
```

### 更新插件

```bash
/plugin update plugin-name
```

### 禁用 / 启用插件

```bash
# 临时禁用
/plugin disable plugin-name

# 重新启用
/plugin enable plugin-name
```

### 卸载插件

```bash
/plugin uninstall plugin-name
```

## 相关概念

以下 Claude Code 功能会和插件一起协作：

- **[Slash Commands](../01-slash-commands/README.md)** - 插件中打包的单独命令
- **[Memory](../02-memory/README.md)** - 插件的持久上下文
- **[Skills](../03-skills/README.md)** - 可以包装进插件的领域能力
- **[Subagents](../04-subagents/README.md)** - 作为插件组件包含的专门化 agent
- **[MCP Servers](../05-mcp/README.md)** - 打包在插件中的 Model Context Protocol 集成
- **[Hooks](../06-hooks/README.md)** - 触发插件工作流的事件处理器

## 完整示例工作流

### PR Review 插件完整工作流

```
1. 用户：/review-pr

2. 插件执行：
   ├── pre-review.js hook 验证 git repo
   ├── GitHub MCP 获取 PR 数据
   ├── security-reviewer subagent 分析安全
   ├── test-checker subagent 验证覆盖率
   └── performance-analyzer subagent 检查性能

3. 汇总并展示结果：
   ✅ 安全：没有发现关键问题
   ⚠️  测试：覆盖率 65%（建议 80%+）
   ✅ 性能：没有明显影响
   📝 提供了 12 条建议
```

## 故障排查

### 插件无法安装
- 检查 Claude Code 版本兼容性：`/version`
- 用 JSON 校验器验证 `plugin.json` 语法
- 检查网络连接（远程插件）
- 检查权限：`ls -la plugin/`

### 组件没有加载
- 验证 `plugin.json` 中的路径与实际目录结构一致
- 检查文件权限：`chmod +x scripts/`
- 检查组件文件语法
- 查看日志：`/plugin debug plugin-name`

### MCP 连接失败
- 确认环境变量已正确设置
- 检查 MCP server 的安装和健康状态
- 使用 `/mcp test` 独立测试 MCP 连接
- 查看 `mcp/` 目录中的 MCP 配置

### 安装后命令不可用
- 确认插件已成功安装：`/plugin list --installed`
- 检查插件是否已启用：`/plugin status plugin-name`
- 重启 Claude Code：`exit` 后重新打开
- 检查是否与现有命令冲突

### Hook 执行问题
- 确认 hook 文件权限正确
- 检查 hook 语法和事件名
- 查看 hook 日志中的错误细节
- 如有可能，手动测试 hooks

## 更多资源

- [官方插件文档](https://code.claude.com/docs/en/plugins)
- [发现插件](https://code.claude.com/docs/en/discover-plugins)
- [插件市场](https://code.claude.com/docs/en/plugin-marketplaces)
- [插件参考](https://code.claude.com/docs/en/plugins-reference)
- [MCP Server 参考](https://modelcontextprotocol.io/)
- [Subagent 配置指南](../04-subagents/README.md)
- [Hook 系统参考](../06-hooks/README.md)
