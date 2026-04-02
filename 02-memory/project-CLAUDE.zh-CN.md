# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- 使用 Prettier 进行格式化
- 使用 ESLint（airbnb 配置）
- 每行最大 100 字符
- 使用 2 空格缩进

### Naming Conventions
- **Files**: kebab-case (`user-controller.js`)
- **Classes**: PascalCase (`UserService`)
- **Functions/Variables**: camelCase (`getUserById`)
- **Constants**: UPPER_SNAKE_CASE (`API_BASE_URL`)
- **Database Tables**: snake_case (`user_accounts`)

### Git Workflow
- 分支命名：`feature/description` 或 `fix/description`
- 提交信息：遵循 conventional commits
- 合并前必须发起 PR
- 所有 CI/CD 检查必须通过
- 至少需要 1 个审批

### Testing Requirements
- 最低 80% 代码覆盖率
- 所有关键路径必须有测试
- 单元测试使用 Jest
- E2E 使用 Cypress
- 测试文件命名：`*.test.ts` 或 `*.spec.ts`

### API Standards
- 仅使用 RESTful endpoints
- 请求/响应统一 JSON
- 正确使用 HTTP 状态码
- API 版本化：`/api/v1/`
- 为所有 endpoint 提供示例文档

### Database
- Schema 变更必须通过 migration
- 严禁硬编码凭据
- 使用连接池
- 开发环境启用查询日志
- 定期备份

### Deployment
- 基于 Docker 部署
- Kubernetes 编排
- 蓝绿部署策略
- 失败自动回滚
- 部署前执行数据库迁移

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | 启动开发服务器 |
| `npm test` | 运行测试套件 |
| `npm run lint` | 代码风格检查 |
| `npm run build` | 生产构建 |
| `npm run migrate` | 执行数据库迁移 |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL 连接池在高峰时段限制为 20
- Workaround: 实现查询队列
- Safari 14 与 async generators 存在兼容性问题
- Workaround: 使用 Babel 转译

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
