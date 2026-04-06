# 内存

一个视觉指南，了解 Claude Code 如何记住跨会话的内容。

> 📚 **关于本指南**
> 
> 本模块介绍 **Claude Code** 的内存系统。
> 
> Kimi Code 用户可参考 **Kimi Code 适配**部分了解对应配置。

---

## 快速对照

| Claude Code | Kimi Code |
|-------------|-----------|
| `CLAUDE.md` | `KIMI.md` |
| `CLAUDE.local.md` | `KIMI.local.md` |
| `.claude/` 目录 | `.kimi/` 目录 |

---

## 概览

内存系统在每次对话开始时向 Claude 注入持久化上下文，随时间建立知识。

```
┌─────────────────────────────────────────────────────────────┐
│                     内存架构                                 │
├─────────────────────────────────────────────────────────────┤
│                                                            │
│                    会话启动                                  │
│                         │                                   │
│                         ▼                                   │
│              ┌─────────────────────┐                       │
│              │   上下文加载器      │                       │
│              └──────────┬──────────┘                       │
│                         │                                   │
│        ┌────────────────┼────────────────┐                 │
│        │                │                │                 │
│        ▼                ▼                ▼                 │
│   ┌─────────┐    ┌────────────┐    ┌───────────┐          │
│   │CLAUDE.md│    │CLAUDE.local│    │ 会话历史   │          │
│   │(项目)   │    │   .md      │    │  (短期)   │          │
│   └────┬────┘    │ (本地)     │    └─────┬─────┘          │
│        │         └─────┬──────┘          │                │
│        │               │                 │                │
│        │               ▼                 │                │
│        │      ┌─────────────────┐       │                │
│        │      │  开发者偏好      │       │                │
│        │      │  (敏感，不提交)  │       │                │
│        │      └─────────────────┘       │                │
│        │                                 │                │
│        └─────────────┬───────────────────┘                │
│                      │                                    │
│                      ▼                                    │
│           ┌───────────────────┐                          │
│           │  合并上下文        │                          │
│           │  注入提示词        │                          │
│           └───────────────────┘                          │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

### 记忆层级

```
┌─────────────────────────────────────────────────────────────┐
│                    记忆层级                                  │
├─────────────────────────────────────────────────────────────┤
│                                                            │
│   L3: 项目上下文                                           │
│   ─────────────────                                        │
│   CLAUDE.md ──▶ 架构、API、决策、模式                      │
│   持久化：是 | 范围：所有用户                                │
│   提交到仓库：是                                            │
│                                                            │
│   L2: 本地上下文                                           │
│   ─────────────────                                        │
│   CLAUDE.local.md ──▶ 偏好、环境、秘密                     │
│   持久化：是 | 范围：单个开发者                            │
│   提交到仓库：否 (.gitignored)                              │
│                                                            │
│   L1: 会话上下文                                           │
│   ─────────────────                                        │
│   对话历史 ──▶ 当前会话状态                                 │
│   持久化：否 | 范围：单个会话                              │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 安装

**Claude Code:**
```bash
# 在项目根目录创建 CLAUDE.md
cp project-CLAUDE.md CLAUDE.md

# 创建本地文件（敏感信息，不提交）
cp local-CLAUDE.md CLAUDE.local.md
echo "CLAUDE.local.md" >> .gitignore
```

**Kimi Code 适配:**
```bash
# 在项目根目录创建 KIMI.md
cp project-CLAUDE.md KIMI.md

# 创建本地文件（敏感信息，不提交）
cp local-CLAUDE.md KIMI.local.md
echo "KIMI.local.md" >> .gitignore
```

---

## CLAUDE.md 模板（项目级）

```markdown
# 项目记忆

## 架构概览
- **技术栈**: React + TypeScript + Node.js
- **数据库**: PostgreSQL with Prisma ORM
- **API**: REST with OpenAPI 规范
- **部署**: Docker + Kubernetes

## 关键模式

### 错误处理
- 始终使用 try/catch 包装 API 调用
- 使用自定义错误类：AppError、ValidationError
- 错误响应格式：`{ error: string, code: string, details?: any }`

### 类型定义
- 所有 API 响应使用共享的 DTO
- 验证模式使用 Zod
- 避免 `any`，使用 `unknown` + 类型守卫

## 常用命令
```bash
# 开发
npm run dev          # 启动开发服务器
npm run test:watch   # 运行测试监视模式

# 数据库
npm run db:migrate   # 运行迁移
npm run db:seed      # 种子数据
```

## API 约定
- RESTful 端点: `/api/v1/resource`
- 认证: Bearer token in Authorization header
- 分页: `?page=1&limit=20`

## 文件组织
```
src/
  components/     # React 组件
  hooks/          # 自定义 hooks
  utils/          # 工具函数
  types/          # TypeScript 类型
  api/            # API 客户端
```

## 重要决策
- 使用 Zod 而非 Joi（更好的 TypeScript 集成）
- 使用 React Query 而非 Redux（服务端状态管理）
- 使用 pnpm 而非 npm（性能）
```

---

## CLAUDE.local.md 模板（本地级）

```markdown
# 本地开发者记忆

## 我的环境
- **Node 版本**: v18.17.0
- **包管理器**: pnpm
- **编辑器**: VS Code
- **操作系统**: macOS

## 个人偏好
- 使用单引号而非双引号
- 偏好箭头函数
- 异步函数使用 async/await
- 4 空格缩进

## 敏感配置
- **API 密钥位置**: ~/.config/myapp/api-keys
- **本地数据库**: postgres://localhost:5432/dev
- **测试环境**: http://localhost:3001

## 快捷命令
```bash
# 个人别名
alias cld='claude'                    # 快速启动
alias clt='claude -p "run tests"'     # 运行测试
```

## 工作流偏好
- 先写测试，后实现
- 小 PR，频繁提交
- 始终先创建功能分支
- 提交前运行 lint 和测试
```

---

## 工作原理（深度解析）

### 启动序列

```
┌─────────────────────────────────────────────────────────────────┐
│                    会话启动序列                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                │
│   1. 用户运行: claude (或 kimmi)                               │
│            │                                                   │
│            ▼                                                   │
│   2. 发现阶段                                                   │
│            │                                                   │
│            ├─▶ 扫描当前目录                                    │
│            │      ├─ CLAUDE.md / KIMI.md ──▶ 加载              │
│            │      └─ CLAUDE.local.md / KIMI.local.md ──▶ 加载  │
│            │                                                   │
│            ├─▶ 向上遍历父目录                                  │
│            │      ├─ 找到 CLAUDE.md / KIMI.md? ──▶ 加载        │
│            │      └─ 到达文件系统根或 git 根                    │
│            │                                                   │
│            ▼                                                   │
│   3. 上下文合并                                                 │
│            │                                                   │
│            ├─▶ 从根目录到当前目录按顺序合并                      │
│            │   (父目录上下文被子目录覆盖)                        │
│            │                                                   │
│            ├─▶ 添加 CLAUDE.local.md / KIMI.local.md             │
│            │   (最后，最高优先级)                               │
│            │                                                   │
│            ▼                                                   │
│   4. 提示词注入                                                 │
│            │                                                   │
│            ├─▶ 系统提示词 + 合并内存                            │
│            │                                                   │
│            ▼                                                   │
│   5. 会话开始                                                   │
│            │                                                   │
│            └─▶ 上下文立即可用                                   │
│                                                                │
└─────────────────────────────────────────────────────────────────┘
```

### 作用域层级

```
项目结构:
~
└── projects/
    └── my-app/
        ├── CLAUDE.md / KIMI.md          ◀── 根级内存
        ├── backend/
        │   ├── CLAUDE.md / KIMI.md      ◀── 后端特定
        │   └── src/
        └── frontend/
            └── CLAUDE.md / KIMI.md      ◀── 前端特定

当在 backend/src/ 中工作时，上下文 =
  根级 + 后端特定
  (后端特定覆盖根级冲突)
```

---

## Kimi Code 适配

### 配置路径

| 配置项 | Claude Code | Kimi Code |
|--------|-------------|-----------|
| 项目内存文件 | `CLAUDE.md` | `KIMI.md` |
| 本地内存文件 | `CLAUDE.local.md` | `KIMI.local.md` |
| 搜索顺序 | 从根到当前目录 | 从根到当前目录 |
| 合并策略 | 子目录覆盖父目录 | 子目录覆盖父目录 |
| 本地文件忽略 | 添加到 `.gitignore` | 添加到 `.gitignore` |

### 快速迁移

```bash
# 1. 重命名或复制现有配置文件
mv CLAUDE.md KIMI.md 2>/dev/null || cp CLAUDE.md KIMI.md
mv CLAUDE.local.md KIMI.local.md 2>/dev/null || cp CLAUDE.local.md KIMI.local.md

# 2. 更新 .gitignore
grep -q "KIMI.local.md" .gitignore || echo "KIMI.local.md" >> .gitignore

# 3. 更新文件内容中的路径引用
# 将 .claude/ 替换为 .kimi/
sed -i 's/\.claude\//.kimi\//g' KIMI.md KIMI.local.md 2>/dev/null || true
```

### 注意事项

- Kimi Code 使用相同的内存机制和搜索策略
- 文件格式和结构完全相同
- 本地敏感信息应始终添加到 `.gitignore`
- 可以同时在项目中保留 CLAUDE.md 和 KIMI.md

---

## 最佳实践

| 实践 | 原因 | 示例 |
|------|------|------|
| **按技术栈分组** | 便于查找 | 架构、API、常用命令 |
| **使用示例** | 澄清抽象规则 | "使用 try/catch" + 代码示例 |
| **定期更新** | 保持准确 | 架构变更后更新 |
| **保持简洁** | 避免上下文膨胀 | 关注模式和约定 |
| **使用相对路径** | 跨环境工作 | `./src/` 而非 `/home/user/...` |

---

## 常见用例

### 用例 1：大型代码库入职

**CLAUDE.md / KIMI.md:**
```markdown
## 新开发者入职

### 关键目录
- `src/core/` - 业务逻辑，只读
- `src/features/` - 功能实现，活跃开发
- `tests/integration/` - 集成测试

### 首次设置
1. cp .env.example .env
2. docker-compose up -d db
3. npm run migrate
4. npm run seed

### 代码审查清单
- 单元测试覆盖率 > 80%
- 集成测试覆盖 API 端点
- 错误处理遵循 src/core/errors.ts 模式
```

### 用例 2：API 项目

**CLAUDE.md / KIMI.md:**
```markdown
## API 约定

### 端点结构
```
GET    /api/v1/resource      # 列表
GET    /api/v1/resource/:id  # 详情
POST   /api/v1/resource      # 创建
PUT    /api/v1/resource/:id  # 完整更新
PATCH  /api/v1/resource/:id  # 部分更新
DELETE /api/v1/resource/:id  # 删除
```

### 响应格式
```typescript
// 成功
{ data: T, meta?: PaginationMeta }

// 错误
{ error: string, code: string, details?: any }
```

### 认证
所有端点需要 Bearer token:
`Authorization: Bearer <token>`

### 速率限制
- 100 请求/分钟（认证）
- 20 请求/分钟（未认证）
```

### 用例 3：前端项目

**CLAUDE.md / KIMI.md:**
```markdown
## React 模式

### 组件结构
```typescript
// 导入
// 类型
// 组件
// 导出
```

### 状态管理
- 本地状态: useState
- 服务端状态: React Query
- 全局状态: Zustand（最小化使用）

### 样式
- 使用 Tailwind CSS
- 变体使用 class-variance-authority
- 深色模式: `dark:` 前缀

### 测试
- 组件: React Testing Library
- 逻辑: Vitest
- E2E: Playwright
```

---

## 故障排除

| 问题 | 检查 | 解决方案 |
|------|------|---------|
| 未加载内存 | 文件位置 | 确保在项目根目录 |
| 上下文错误 | 文件格式 | 使用有效的 Markdown |
| 本地配置被提交 | .gitignore | 添加 CLAUDE.local.md / KIMI.local.md |
| 上下文太旧 | 文件内容 | 更新架构变更 |
| 内存未更新 | 作用域 | 检查子目录是否有覆盖 |

---

## 下一步

- [学习技能 →](../03-skills/)
- [探索子代理 →](../04-subagents/)
