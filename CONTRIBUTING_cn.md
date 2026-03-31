<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 为 Claude How To 做贡献

感谢您有兴趣为本项目做贡献！本指南将帮助您了解如何有效地参与贡献。

## 关于本项目

Claude How To 是一份以可视化、示例驱动方式介绍 Claude Code 的指南。我们提供：
- **Mermaid 图表**，直观解释各功能的工作原理
- **可直接使用的生产级模板**
- **带有背景说明和最佳实践的真实案例**
- **从入门到进阶的渐进式学习路径**

## 贡献类型

### 1. 新示例或模板
为现有功能（slash commands、skills、hooks 等）添加示例：
- 可直接复制粘贴的代码
- 清晰说明其工作原理
- 使用场景与优势
- 故障排查提示

### 2. 文档改进
- 澄清令人困惑的章节
- 修正错别字和语法错误
- 补充缺失信息
- 改进代码示例

### 3. 功能指南
为 Claude Code 新功能编写指南：
- 分步骤教程
- 架构图
- 常见模式与反模式
- 真实工作流程

### 4. Bug 报告
报告您遇到的问题：
- 描述您的预期行为
- 描述实际发生的情况
- 包含复现步骤
- 附上相关的 Claude Code 版本和操作系统信息

### 5. 反馈与建议
帮助改进本指南：
- 建议更清晰的表达方式
- 指出内容覆盖的空白
- 推荐新章节或调整目录结构

## 快速开始

### 1. Fork 并克隆
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. 创建分支
使用描述性的分支名称：
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. 配置开发环境
```bash
# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装 pre-commit hooks（可选，但推荐）
pip install pre-commit
pre-commit install

# 手动运行 pre-commit 检查
pre-commit run --all-files
```

## 目录结构

```
├── 01-slash-commands/      # 用户调用的快捷命令
├── 02-memory/              # 持久化上下文示例
├── 03-skills/              # 可复用能力
├── 04-subagents/           # 专用 AI 助手
├── 05-mcp/                 # Model Context Protocol 示例
├── 06-hooks/               # 事件驱动自动化
├── 07-plugins/             # 捆绑功能
├── 08-checkpoints/         # 会话快照
├── 09-advanced-features/   # 规划、思考、后台任务
├── 10-cli/                 # CLI 参考
├── scripts/                # 构建和实用脚本
└── README.md               # 主指南
```

## 如何贡献示例

### 添加 Slash Command
1. 在 `01-slash-commands/` 中创建一个 `.md` 文件
2. 包含以下内容：
   - 清晰描述其功能
   - 使用场景
   - 安装说明
   - 使用示例
   - 自定义提示
3. 更新 `01-slash-commands/README.md`

### 添加 Skill
1. 在 `03-skills/` 中创建一个目录
2. 包含以下内容：
   - `SKILL.md` - 主文档
   - `scripts/` - 如需要可放辅助脚本
   - `templates/` - 提示词模板
   - README 中的使用示例
3. 更新 `03-skills/README.md`

### 添加 Subagent
1. 在 `04-subagents/` 中创建一个 `.md` 文件
2. 包含以下内容：
   - Agent 的目的和能力
   - 系统提示结构
   - 使用案例示例
   - 集成示例
3. 更新 `04-subagents/README.md`

### 添加 MCP 配置
1. 在 `05-mcp/` 中创建一个 `.json` 文件
2. 包含以下内容：
   - 配置说明
   - 所需的环境变量
   - 配置步骤
   - 使用示例
3. 更新 `05-mcp/README.md`

### 添加 Hook
1. 在 `06-hooks/` 中创建一个 `.sh` 文件
2. 包含以下内容：
   - Shebang 行和描述
   - 清晰的注释说明逻辑
   - 错误处理
   - 安全注意事项
3. 更新 `06-hooks/README.md`

## 写作规范

### Markdown 风格
- 使用清晰的标题层级（H2 用于章节，H3 用于子章节）
- 段落简短、内容集中
- 使用项目符号列表
- 代码块需注明语言类型
- 章节之间添加空行

### 代码示例
- 确保示例可直接复制粘贴使用
- 为非显而易见的逻辑添加注释
- 同时提供简单版和进阶版
- 展示真实使用场景
- 标注潜在问题

### 文档
- 解释"为什么"，而不只是"是什么"
- 注明前提条件
- 添加故障排查章节
- 链接到相关主题
- 保持对初学者友好

### JSON/YAML
- 使用规范的缩进（统一使用 2 或 4 个空格）
- 添加注释解释配置项
- 包含验证示例

### 图表
- 尽可能使用 Mermaid
- 保持图表简洁易读
- 在图表下方添加描述
- 链接到相关章节

## 提交规范

遵循约定式提交格式：
```
type(scope): description

[可选正文]
```

类型说明：
- `feat`：新功能或新示例
- `fix`：Bug 修复或错误更正
- `docs`：文档变更
- `refactor`：代码重构
- `style`：格式调整
- `test`：添加或修改测试
- `chore`：构建、依赖等

示例：
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 提交前检查

### 核对清单
- [ ] 代码符合项目风格和规范
- [ ] 新示例包含清晰的文档说明
- [ ] README 文件已更新（本地和根目录均需更新）
- [ ] 不含敏感信息（API 密钥、凭证等）
- [ ] 示例已经过测试且正常运行
- [ ] 链接已验证且正确
- [ ] 文件权限正确（脚本文件具有可执行权限）
- [ ] 提交信息清晰且具有描述性

### 本地测试
```bash
# 检查文件格式
pre-commit run --all-files

# 验证链接是否有效（如适用）
# 使用 Claude Code 手动测试示例

# 查看您的变更
git diff

# 测试 EPUB 生成（如果文档有变更）
uv run scripts/build_epub.py
```

## Pull Request 流程

1. **创建带有清晰描述的 PR**：
   - 这个 PR 添加或修复了什么？
   - 为什么需要这个更改？
   - 关联的 issue（如有）

2. **包含相关细节**：
   - 新功能？请附上使用场景
   - 文档更新？请说明改进之处
   - 示例？请展示修改前后的对比

3. **关联 issue**：
   - 使用 `Closes #123` 自动关闭相关 issue

4. **耐心等待审查**：
   - 维护者可能会提出改进建议
   - 根据反馈进行迭代
   - 最终决定权归维护者所有

## 代码审查流程

审查者将检查以下内容：
- **准确性**：是否按描述正常工作？
- **质量**：是否达到生产就绪标准？
- **一致性**：是否遵循项目规范？
- **文档**：是否清晰完整？
- **安全性**：是否存在安全漏洞？

## 报告问题

### Bug 报告
请包含：
- Claude Code 版本
- 操作系统
- 复现步骤
- 预期行为
- 实际行为
- 相关截图（如适用）

### 功能请求
请包含：
- 使用场景或待解决的问题
- 建议的解决方案
- 您已考虑过的替代方案
- 其他补充背景

### 文档问题
请包含：
- 令人困惑或缺失的内容
- 改进建议
- 参考示例或引用来源

## 项目政策

### 敏感信息
- 切勿提交 API 密钥、token 或凭证
- 在示例中使用占位符值
- 为配置文件提供 `.env.example`
- 说明所需的环境变量

### 代码质量
- 保持示例简洁易读
- 避免过度设计
- 为非显而易见的逻辑添加注释
- 提交前进行充分测试

### 知识产权
- 原创内容归作者所有
- 项目采用教育许可证
- 尊重现有版权
- 在需要时注明来源

## 获取帮助

- **提问**：在 GitHub Issues 中发起讨论
- **通用帮助**：查阅现有文档
- **开发帮助**：参考类似示例
- **代码审查**：在 PR 中 @ 维护者

## 致谢

贡献者将在以下位置获得致谢：
- README.md 贡献者章节
- GitHub 贡献者页面
- 提交历史

## 安全

在贡献示例和文档时，请遵循安全编码实践：

- **切勿硬编码密钥或 API 密钥** - 使用环境变量
- **警示安全隐患** - 突出标注潜在风险
- **使用安全的默认配置** - 默认启用安全功能
- **验证输入** - 展示正确的输入验证和数据清洗方式
- **包含安全说明** - 记录安全注意事项

如发现安全问题，请参阅 [SECURITY.md](SECURITY.md) 了解我们的漏洞报告流程。

## 行为准则

我们致力于提供一个热情、包容的社区。请阅读 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 了解我们完整的社区规范。

简而言之：
- 保持尊重与包容
- 优雅地接受反馈
- 帮助他人学习和成长
- 避免骚扰或歧视
- 向维护者报告问题

所有贡献者都应遵守本准则，以善意和尊重对待彼此。

## 许可证

向本项目提交贡献，即表示您同意您的贡献将以 MIT 许可证授权。详情请参阅 [LICENSE](LICENSE) 文件。

## 有疑问？

- 查阅 [README](README.md)
- 阅读 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- 参考现有示例
- 提交 issue 发起讨论

感谢您的贡献！🙏
