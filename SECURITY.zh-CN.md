# 安全策略（Security Policy）

## 概览

`Claude How To` 项目的安全性对我们非常重要。本文档说明了我们的安全实践，以及如何以负责任的方式报告安全漏洞。

## 受支持版本

我们为以下版本提供安全更新：

| Version | Status | Support Until |
|---------|--------|---------------|
| Latest (main) | ✅ Active | Current + 6 months |
| 1.x releases | ✅ Active | Until next major version |

**说明**：作为以教学指南为主的项目，我们更关注“当前最佳实践”与“文档安全”的持续维护，而不是传统的软件版本支持模式。安全更新会直接应用到 `main` 分支。

## 安全实践

### 代码安全

1. **依赖管理**
   - 所有 Python 依赖固定在 `requirements.txt`
   - 通过 dependabot 与人工审查定期更新
   - 每次提交使用 Bandit 进行安全扫描
   - 使用 pre-commit hooks 进行安全检查

2. **代码质量**
   - 使用 Ruff Lint 发现常见问题
   - 使用 mypy 类型检查降低类型相关风险
   - pre-commit hooks 强制执行规范
   - 所有变更在合并前均需审查

3. **访问控制**
   - `main` 分支启用保护
   - 合并前必须经过 review
   - 合并前必须通过状态检查
   - 仓库写权限受限

### 文档安全

1. **示例中不包含密钥**
   - 示例中的 API Key 全部使用占位符
   - 不会硬编码凭据
   - `.env.example` 明确展示必需变量
   - 明确提示密钥管理注意事项

2. **安全最佳实践**
   - 示例默认展示更安全的实现模式
   - 在文档中高亮安全警示
   - 提供官方安全指南链接
   - 在相关章节解释凭据处理方式

3. **内容审查**
   - 所有文档都经过安全问题检查
   - 贡献指南包含安全注意事项
   - 验证外部链接与引用来源

### 依赖安全

1. **扫描**
   - 使用 Bandit 扫描全部 Python 代码漏洞
   - 通过 GitHub security alerts 检查依赖漏洞
   - 定期执行人工安全审计

2. **更新**
   - 及时应用安全补丁
   - 谨慎评估主版本升级
   - 在 changelog 中记录安全相关更新

3. **透明度**
   - 安全更新在提交记录中可追踪
   - 漏洞披露流程负责任执行
   - 适用时发布公开安全通告

## 漏洞报告

### 我们重视的安全问题

我们欢迎以下报告：
- 脚本或示例中的**代码漏洞**
- Python 包中的**依赖漏洞**
- 示例中的**密码学问题**
- 文档中的**认证/授权缺陷**
- 配置示例中的**数据暴露风险**
- 各类**注入漏洞**（SQL、命令等）
- **SSRF / XXE / 路径遍历**问题

### 不在范围内的问题

以下内容不属于本项目处理范围：
- Claude Code 本身的漏洞（请向 Anthropic 报告）
- 外部服务或第三方库自身问题（请向上游报告）
- 社工攻击或用户教育问题（不适用于本指南）
- 无 PoC 的纯理论漏洞
- 已通过官方通道披露的依赖漏洞

## 如何报告

### 私下报告（推荐）

**对于敏感安全问题，请使用 GitHub 私有漏洞报告：**

1. 访问：https://github.com/luongnv89/claude-howto/security/advisories
2. 点击 “Report a vulnerability”
3. 填写漏洞详情
4. 建议包含：
   - 漏洞清晰描述
   - 受影响组件（文件、章节、示例）
   - 潜在影响
   - 复现步骤（若适用）
   - 修复建议（若有）

**后续流程：**
- 我们会在 48 小时内确认收到
- 评估并判断严重级别
- 与你协作制定修复方案
- 协调披露时间线
- 在安全通告中致谢（如你希望匿名，也会尊重）

### 公开报告

对于非敏感或已公开问题：

1. 在 GitHub 创建带 `security` 标签的 Issue
2. 建议包含：
   - 标题：`[SECURITY]` + 简要描述
   - 详细问题说明
   - 受影响文件或章节
   - 潜在影响
   - 修复建议

## 漏洞响应流程

### 评估阶段（24 小时）

1. 确认收到报告
2. 使用 [CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document) 评估严重性
3. 判断是否在处理范围内
4. 给出初步评估反馈

### 修复阶段（1-7 天）

1. 开发修复方案
2. 审查并测试修复
3. 创建安全通告
4. 准备发布说明

### 披露阶段（按严重性）

**Critical（CVSS 9.0-10.0）**
- 立即发布修复
- 发布公开安全通告
- 向报告者提前 24 小时通知

**High（CVSS 7.0-8.9）**
- 48-72 小时内发布修复
- 向报告者提前 5 天通知
- 发布时同步公开通告

**Medium（CVSS 4.0-6.9）**
- 在下一次常规更新中发布修复
- 发布时公开通告

**Low（CVSS 0.1-3.9）**
- 在下一次常规更新中包含修复
- 发布时给出通告

### 通告发布内容

我们发布的安全通告通常包括：
- 漏洞描述
- 受影响组件
- 严重性评估（CVSS 分数）
- 修复版本
- 临时缓解方案（若适用）
- 报告者致谢（经授权）

## 给报告者的最佳实践

### 报告前

- **先验证问题**：是否可稳定复现？
- **查重**：是否已有相同报告？
- **查文档**：是否已有安全使用说明？
- **验证修复**：你的建议修复是否有效？

### 报告时

- **具体明确**：提供精确文件路径与行号
- **给出上下文**：为何属于安全问题？
- **说明影响**：攻击者可能达成什么结果？
- **提供复现步骤**：我们如何复现？
- **建议修复**：你会如何修？

### 报告后

- **保持耐心**：项目资源有限
- **及时回应**：快速回复追问
- **先保密**：修复前不要公开披露
- **尊重协作**：遵循协调好的披露时间线

## 安全头与配置

### 仓库安全

- **Branch protection**：`main` 分支变更需 2 个审批
- **Status checks**：所有 CI/CD 检查必须通过
- **CODEOWNERS**：关键文件由指定 reviewer 负责
- **Signed commits**：建议贡献者使用签名提交

### 开发安全

```bash
# Install pre-commit hooks
pre-commit install

# Run security scans locally
bandit -c pyproject.toml -r scripts/
mypy scripts/ --ignore-missing-imports
ruff check scripts/
```

### 依赖安全

```bash
# Check for known vulnerabilities
pip install safety
safety check

# Or use pip-audit
pip install pip-audit
pip-audit
```

## 贡献者安全指南

### 编写示例时

1. **绝不硬编码密钥**

```python
# ❌ Bad
api_key = "sk-1234567890"

# ✅ Good
api_key = os.getenv("API_KEY")
```

2. **明确提示安全影响**

```markdown
⚠️ **Security Note**: Never commit `.env` files to git.
Add to `.gitignore` immediately.
```

3. **采用安全默认值**
- 默认启用认证
- 在适用场景下使用 HTTPS
- 验证并清洗输入
- 使用参数化查询

4. **记录安全考量**
- 解释“为什么安全重要”
- 对比安全/不安全写法
- 链接权威资料
- 将警告信息放在显著位置

### 审查贡献时

1. **检查是否暴露密钥**
- 扫描常见模式（`api_key=`、`password=`）
- 审查配置文件
- 检查环境变量使用

2. **验证安全编码实践**
- 不允许硬编码凭据
- 必须有正确输入校验
- 认证/授权实现需安全
- 文件处理需安全

3. **评估安全影响**
- 是否可能被滥用？
- 最坏情况是什么？
- 是否存在边界场景风险？

## 安全资源

### 官方标准
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)

### Python 安全
- [Python Security Advisories](https://www.python.org/dev/security/)
- [PyPI Security](https://pypi.org/help/#security)
- [Bandit Documentation](https://bandit.readthedocs.io/)

### 依赖管理
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [GitHub Security Alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

### 通用安全
- [Anthropic Security](https://www.anthropic.com/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## 安全通告归档

历史安全通告可在 [GitHub Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories) 查看。

## 联系方式

如有安全相关问题或希望讨论安全实践：

1. **私有安全报告**：使用 GitHub 私有漏洞报告
2. **一般安全问题**：创建带 `[SECURITY]` 标签的 Discussion
3. **安全策略反馈**：创建带 `security` 标签的 Issue

## 致谢

感谢安全研究者与社区成员帮助我们提升项目安全性。负责任报告漏洞的贡献者会在安全通告中致谢（如其希望匿名则不公开姓名）。

## 策略更新

本安全策略会在以下情况下评审更新：
- 发现新漏洞时
- 安全最佳实践演进时
- 项目范围发生变化时
- 至少每年一次

**Last Updated**: January 2026  
**Next Review**: January 2027

---

感谢你帮助保持 Claude How To 的安全！🔒
