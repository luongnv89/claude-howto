<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 为 Claude How To 贡献内容

感谢你愿意为这个项目做出贡献。这份指南会帮助你更高效地参与协作。

## 关于本项目

Claude How To 是一份面向 Claude Code 的可视化、以示例驱动的学习指南。我们提供：
- **Mermaid 图表**，解释各项功能的工作方式
- **可直接投入使用的模板**，你可以马上复制到项目中
- **带上下文和最佳实践的真实案例**
- **从入门到进阶的渐进式学习路径**

## 贡献类型

### 1. 新示例或新模板
为已有功能补充示例，例如 slash commands、skills、hooks 等：
- 可直接复制粘贴的代码
- 清楚说明工作原理
- 使用场景与收益
- 排障提示

### 2. 文档改进
- 澄清容易混淆的内容
- 修复拼写和语法问题
- 补充缺失信息
- 优化代码示例

### 3. 功能指南
为新的 Claude Code 功能编写指南：
- 分步骤教程
- 架构图
- 常见模式和反模式
- 真实工作流

### 4. Bug 报告
报告你遇到的问题：
- 你原本期望发生什么
- 实际发生了什么
- 复现步骤
- 相关的 Claude Code 版本和操作系统

### 5. 反馈与建议
帮助我们改进这份指南：
- 建议更好的解释方式
- 指出覆盖不足的地方
- 推荐新章节或重组结构

## 快速开始

### 1. Fork 并克隆
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. 创建分支
使用能说明用途的分支名：
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. 配置开发环境

pre-commit hooks 会在本地、每次提交前运行与 CI 相同的检查。PR 被接受前，下面四项检查都必须通过。

**必需依赖：**

```bash
# Python 工具链（uv 是本项目的包管理器）
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown lint 工具（Node.js）
npm install -g markdownlint-cli

# Mermaid 图表校验器（Node.js）
npm install -g @mermaid-js/mermaid-cli

# 安装 pre-commit 并启用 hooks
uv pip install pre-commit
pre-commit install
```

**验证配置：**

```bash
pre-commit run --all-files
```

每次提交都会运行这些 hooks：

| Hook | 检查内容 |
|------|----------|
| `markdown-lint` | Markdown 格式和结构 |
| `cross-references` | 相对链接、锚点、代码围栏 |
| `mermaid-syntax` | 所有 ` ```mermaid ` 代码块是否可正确解析 |
| `link-check` | 外部 URL 是否可访问 |
| `build-epub` | `.md` 变更时 EPUB 是否能无错误生成 |

## 目录结构

```
├── 01-slash-commands/      # 用户手动触发的快捷命令
├── 02-memory/              # 持久上下文示例
├── 03-skills/              # 可复用能力
├── 04-subagents/           # 专门化 AI 助手
├── 05-mcp/                 # Model Context Protocol 示例
├── 06-hooks/               # 事件驱动自动化
├── 07-plugins/             # 打包功能集合
├── 08-checkpoints/         # 会话快照
├── 09-advanced-features/   # 规划、思考、后台任务
├── 10-cli/                 # CLI 参考
├── scripts/                # 构建与工具脚本
└── README.md            # 主指南
```

## 如何贡献示例

### 添加 Slash Command
1. 在 `01-slash-commands/` 中创建一个 `.md` 文件
2. 包含：
   - 清晰说明用途
   - 使用场景
   - 安装说明
   - 使用示例
   - 自定义技巧
3. 更新 `01-slash-commands/README.md`

### 添加 Skill
1. 在 `03-skills/` 中创建一个目录
2. 包含：
   - `SKILL.md` - 主文档
   - `scripts/` - 如有需要可放辅助脚本
   - `templates/` - 提示词模板
   - README 中的示例用法
3. 更新 `03-skills/README.md`

### 添加 Subagent
1. 在 `04-subagents/` 中创建一个 `.md` 文件
2. 包含：
   - agent 的目标和能力
   - 系统提示词结构
   - 示例使用场景
   - 集成示例
3. 更新 `04-subagents/README.md`

### 添加 MCP 配置
1. 在 `05-mcp/` 中创建一个 `.json` 文件
2. 包含：
   - 配置说明
   - 所需环境变量
   - 配置步骤
   - 使用示例
3. 更新 `05-mcp/README.md`

### 添加 Hook
1. 在 `06-hooks/` 中创建一个 `.sh` 文件
2. 包含：
   - shebang 和说明
   - 逻辑清晰的注释
   - 错误处理
   - 安全考虑
3. 更新 `06-hooks/README.md`

## 编写规范

### Markdown 风格
- 使用清晰的标题层级（章节用 H2，小节用 H3）
- 段落保持简短且聚焦
- 列表用项目符号
- 代码块要标明语言
- 各章节之间保留空行

### 代码示例
- 示例要能直接复制粘贴
- 为不明显的逻辑添加注释
- 同时提供简单版和进阶版
- 展示真实使用场景
- 标出可能的坑

### 文档写作
- 解释“为什么”，而不只是“是什么”
- 包含前置条件
- 添加排障章节
- 链接相关主题
- 保持对初学者友好

### JSON/YAML
- 统一缩进风格（2 或 4 个空格）
- 为配置添加注释
- 包含验证示例

### 图表
- 尽量使用 Mermaid
- 保持图表简洁易读
- 在图表下方补充说明
- 链接到相关章节

## Commit 规范

使用 conventional commit 格式：
```
type(scope): description

[optional body]
```

类型包括：
- `feat`：新功能或新示例
- `fix`：修复或更正
- `docs`：文档变更
- `refactor`：代码重构
- `style`：格式调整
- `test`：新增或修改测试
- `chore`：构建、依赖等

示例：
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 提交前检查

### 清单
- [ ] 代码符合项目风格与约定
- [ ] 新示例附带清晰文档
- [ ] README 已更新（本地和根目录）
- [ ] 不包含敏感信息（API key、凭据）
- [ ] 示例经过测试并可运行
- [ ] 链接已验证且正确
- [ ] 文件权限正确（脚本可执行）
- [ ] Commit 信息清晰且有描述性

### 本地测试
```bash
# 运行所有 pre-commit 检查（与 CI 相同）
pre-commit run --all-files

# 查看改动
git diff
```

## Pull Request 流程

1. **创建带有清晰说明的 PR**：
   - 这次提交做了什么？
   - 为什么需要它？
   - 是否有关联 issue？

2. **补充相关细节**：
   - 新功能？请说明使用场景
   - 文档？请说明改进点
   - 示例？展示前后对比

3. **关联 issue**：
   - 使用 `Closes #123` 自动关闭相关 issue

4. **耐心等待审查**：
   - 维护者可能会提出改进建议
   - 根据反馈迭代
   - 最终决定由维护者负责

## Code Review 流程

审查者会检查：
- **准确性**：描述是否与实际一致？
- **质量**：是否达到生产可用？
- **一致性**：是否符合项目模式？
- **文档**：是否清晰完整？
- **安全性**：是否存在漏洞？

## 报告问题

### Bug 报告
请包含：
- Claude Code 版本
- 操作系统
- 复现步骤
- 预期行为
- 实际行为
- 如有必要，附上截图

### 功能请求
请包含：
- 使用场景或要解决的问题
- 建议方案
- 你考虑过的替代方案
- 额外上下文

### 文档问题
请包含：
- 哪里令人困惑或缺失
- 建议如何改进
- 示例或参考资料

## 项目政策

### 敏感信息
- 永远不要提交 API key、token 或凭据
- 示例中使用占位符
- 为配置文件提供 `.env.example`
- 文档中说明所需环境变量

### 代码质量
- 示例要聚焦且易读
- 避免过度设计
- 对不明显的逻辑添加注释
- 提交前充分测试

### 知识产权
- 原创内容归作者所有
- 项目采用教育用途许可证
- 尊重已有版权
- 需要时注明来源

## 获取帮助

- **提问**：在 GitHub Issues 中发起 discussion
- **通用帮助**：先查看现有文档
- **开发帮助**：参考类似示例
- **Code Review**：在 PR 中 @ 维护者

## 认可

贡献者会被收录在：
- `README.md` 的 Contributors 部分
- GitHub contributors 页面
- Commit 历史

## 安全

在贡献示例和文档时，请遵守安全编码实践：

- **绝不要硬编码密钥或 API key** - 使用环境变量
- **提示安全影响** - 标出潜在风险
- **使用安全默认值** - 默认启用安全功能
- **验证输入** - 展示正确的输入校验和清理方式
- **加入安全提示** - 记录安全注意事项

如遇安全问题，请参见 [SECURITY.md](SECURITY.md) 获取漏洞报告流程。

## 行为准则

我们承诺打造一个热情且包容的社区。请阅读 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 查看完整社区标准。

简要来说：
- 保持尊重和包容
- 愉快地接受反馈
- 帮助他人成长和学习
- 避免骚扰或歧视
- 向维护者报告问题

所有贡献者都应遵守这份准则，并以善意和尊重对待彼此。

## 许可证

为本项目贡献内容，即表示你同意你的贡献将按 MIT License 许可。详情见 [LICENSE](LICENSE) 文件。

## 有问题？

- 查看 [README.md](README.md)
- 阅读 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- 查看已有示例
- 发起 issue 讨论

感谢你的贡献！
