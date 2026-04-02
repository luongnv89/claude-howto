<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 参与贡献 Claude How To

感谢你愿意为这个项目贡献内容！本指南将帮助你高效、规范地参与协作。

## 关于本项目

`Claude How To` 是一份面向 Claude Code 的可视化、示例驱动指南。我们提供：
- **Mermaid 架构图**：解释功能如何运作
- **可直接落地的模板**：拿来即用
- **真实场景示例**：包含上下文与最佳实践
- **渐进式学习路径**：从入门到进阶

## 贡献类型

### 1）新增示例或模板
为现有能力补充示例（slash commands、skills、hooks 等）：
- 可复制即运行的代码
- 清晰的工作原理说明
- 使用场景与收益
- 故障排查提示

### 2）文档改进
- 澄清易混淆内容
- 修复错别字与语法问题
- 补充遗漏信息
- 改进代码示例

### 3）功能指南
为新的 Claude Code 功能撰写指南：
- 分步骤教程
- 架构图示
- 常见模式与反模式
- 真实工作流

### 4）Bug 报告
反馈你遇到的问题：
- 你的预期是什么
- 实际发生了什么
- 复现步骤
- Claude Code 版本与操作系统信息

### 5）反馈与建议
帮助指南持续优化：
- 建议更好的讲解方式
- 指出覆盖盲区
- 推荐新增章节或重构目录

## 快速开始

### 1）Fork 与 Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2）创建分支
请使用语义清晰的分支名：
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3）配置本地环境

pre-commit hooks 会在本地运行与 CI 相同的检查。PR 被接受前，这些检查都必须通过。

**必需依赖：**

```bash
# Python tooling (uv is the package manager for this project)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown linter (Node.js)
npm install -g markdownlint-cli

# Mermaid diagram validator (Node.js)
npm install -g @mermaid-js/mermaid-cli

# Install pre-commit and activate hooks
uv pip install pre-commit
pre-commit install
```

**验证环境：**

```bash
pre-commit run --all-files
```

每次提交会运行以下 hooks：

| Hook | What it checks |
|------|---------------|
| `markdown-lint` | Markdown 格式与结构 |
| `cross-references` | 相对链接、锚点、代码围栏 |
| `mermaid-syntax` | 所有 ` ```mermaid ` 代码块可正确解析 |
| `link-check` | 外部 URL 可访问 |
| `build-epub` | `.md` 变更时 EPUB 可无错误生成 |

## 目录结构

```
├── 01-slash-commands/      # 用户手动触发快捷命令
├── 02-memory/              # 持久上下文示例
├── 03-skills/              # 可复用能力模块
├── 04-subagents/           # 专用 AI 助手
├── 05-mcp/                 # MCP 示例
├── 06-hooks/               # 事件驱动自动化
├── 07-plugins/             # 打包功能集合
├── 08-checkpoints/         # 会话快照
├── 09-advanced-features/   # 规划、思考、后台任务
├── 10-cli/                 # CLI 参考
├── scripts/                # 构建与工具脚本
└── README.md               # 主指南
```

## 如何贡献示例

### 添加 Slash Command
1. 在 `01-slash-commands/` 新建 `.md` 文件
2. 包含以下内容：
   - 功能清晰描述
   - 使用场景
   - 安装说明
   - 使用示例
   - 自定义建议
3. 更新 `01-slash-commands/README.md`

### 添加 Skill
1. 在 `03-skills/` 新建目录
2. 包含以下内容：
   - `SKILL.md`：主文档
   - `scripts/`：必要时添加辅助脚本
   - `templates/`：提示词模板
   - README 中补充使用示例
3. 更新 `03-skills/README.md`

### 添加 Subagent
1. 在 `04-subagents/` 新建 `.md` 文件
2. 包含以下内容：
   - Agent 目标与能力
   - 系统提示词结构
   - 示例场景
   - 集成示例
3. 更新 `04-subagents/README.md`

### 添加 MCP 配置
1. 在 `05-mcp/` 新建 `.json` 文件
2. 包含以下内容：
   - 配置说明
   - 必需环境变量
   - 安装步骤
   - 使用示例
3. 更新 `05-mcp/README.md`

### 添加 Hook
1. 在 `06-hooks/` 新建 `.sh` 文件
2. 包含以下内容：
   - Shebang 与用途说明
   - 清晰注释解释逻辑
   - 错误处理
   - 安全注意事项
3. 更新 `06-hooks/README.md`

## 写作规范

### Markdown 风格
- 使用清晰标题层级（章节用 H2，子章节用 H3）
- 段落短而聚焦
- 列表项尽量精炼
- 代码块必须带语言标识
- 章节间留空行

### 代码示例
- 示例要可复制即运行
- 非显然逻辑加注释
- 尽量提供简版与进阶版
- 优先真实场景
- 提示潜在问题

### 文档内容
- 解释“为什么”，不止“做什么”
- 写明前置条件
- 增加故障排查章节
- 链接相关主题
- 对初学者友好

### JSON/YAML
- 缩进规范统一（2 或 4 空格，保持一致）
- 适当注释配置含义
- 可加入校验示例

### 图表
- 优先使用 Mermaid
- 图保持简洁可读
- 图下给出文字说明
- 关联到相关章节

## 提交规范

遵循 conventional commit：
```
type(scope): description

[optional body]
```

类型说明：
- `feat`：新增功能或示例
- `fix`：修复问题
- `docs`：文档改动
- `refactor`：结构重构
- `style`：纯格式调整
- `test`：测试相关改动
- `chore`：构建/依赖/CI 等

示例：
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 提交前检查

### Checklist
- [ ] 代码与文档符合项目风格
- [ ] 新示例有完整说明
- [ ] README（本目录和根目录）已同步更新
- [ ] 不包含敏感信息（API key、凭据）
- [ ] 示例经过测试且可运行
- [ ] 链接已验证
- [ ] 文件权限正确（脚本可执行）
- [ ] commit message 清晰准确

### 本地测试
```bash
# Run all pre-commit checks (same checks as CI)
pre-commit run --all-files

# Review your changes
git diff
```

## Pull Request 流程

1. **创建描述清晰的 PR**：
   - 改了什么？
   - 为什么需要改？
   - 关联 issue（若有）

2. **补充必要细节**：
   - 新功能：请给使用场景
   - 文档改进：说明改进点
   - 示例更新：给出前后对比

3. **关联 Issue**：
   - 使用 `Closes #123` 自动关闭相关 issue

4. **耐心等待 review**：
   - 维护者可能提出改进建议
   - 请根据反馈迭代
   - 最终合并决策由维护者负责

## Code Review 关注点

审查通常关注：
- **准确性**：是否与描述一致
- **质量**：是否可用于生产场景
- **一致性**：是否符合项目既有模式
- **文档完整性**：是否清晰、完整
- **安全性**：是否引入漏洞风险

## 问题反馈

### Bug 报告建议包含
- Claude Code 版本
- 操作系统
- 复现步骤
- 预期行为
- 实际行为
- 必要截图

### Feature Request 建议包含
- 要解决的场景或问题
- 建议方案
- 你考虑过的替代方案
- 其他上下文信息

### 文档问题建议包含
- 哪部分不清楚或缺失
- 你的改进建议
- 可参考的示例或资料

## 项目策略

### 敏感信息
- 不要提交 API key、token、凭据
- 示例中使用占位值
- 配置文件建议提供 `.env.example`
- 写清必需环境变量

### 代码质量
- 示例聚焦、可读
- 避免过度设计
- 非显然逻辑请注释
- 提交前充分测试

### 知识产权
- 原创内容版权归作者
- 项目采用教育友好许可
- 尊重既有版权
- 必要时提供来源标注

## 获取帮助

- **问题咨询**：在 GitHub Issues / Discussions 发起讨论
- **通用帮助**：先查现有文档
- **开发参考**：查看相似示例
- **代码审查**：在 PR 中 @ 维护者

## 贡献者认可

贡献会在以下位置被记录：
- `README.md` Contributors 区域
- GitHub contributors 页面
- 提交历史

## 安全

贡献示例与文档时，请遵循安全编码实践：

- **不要硬编码密钥或凭据** —— 使用环境变量
- **提示安全影响** —— 标注潜在风险
- **使用安全默认值** —— 默认开启安全配置
- **校验输入** —— 展示输入校验与清洗
- **加入安全说明** —— 写明安全考量

若涉及安全漏洞，请查看 [SECURITY.md](SECURITY.zh-CN.md) 中的漏洞报告流程。

## 行为准则

我们致力于建设友好、包容的社区。请阅读 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.zh-CN.md)。

简要原则：
- 保持尊重与包容
- 以建设性方式接受反馈
- 帮助他人学习成长
- 不进行骚扰或歧视行为
- 发现问题及时向维护者反馈

所有贡献者都应遵守该准则，并以善意与尊重相待。

## 许可证

向本项目贡献即表示你同意：你的贡献内容将基于 MIT License 授权。详情见 [LICENSE](LICENSE)。

## Questions?

- 查看 [README](README.zh-CN.md)
- 查看 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.zh-CN.md)
- 参考已有示例
- 开 issue 进行讨论

感谢你的贡献！🙏
