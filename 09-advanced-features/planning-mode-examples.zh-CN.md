# 规划模式示例（Planning Mode Examples）

本文件展示在 Claude Code 中高效使用规划模式的真实案例。

## 示例 1：构建 REST API

### 不使用规划模式

```text
User: Build a REST API for a blog

Claude: I'll create the API...
[Starts coding immediately, may miss requirements]
```

### 使用规划模式

```text
User: /plan Build a REST API for a blog

Claude: Let me create a comprehensive plan for the blog API.

[随后输出分阶段计划，再征求确认后执行]
```

核心价值：
- 先拆阶段再编码
- 明确时间预估与风险
- 让需求补充发生在动手前

## 示例 2：数据库迁移（MongoDB → PostgreSQL）

```text
User: /plan Migrate from MongoDB to PostgreSQL

Claude: This is a complex migration. Let me create a detailed plan.
```

典型阶段建议：
1. 现状分析与映射设计
2. PostgreSQL 环境搭建
3. 双写机制上线
4. 历史数据分批迁移
5. 渐进式切换读流量
6. 全量切主与回滚观察期

关键点：
- 每阶段都配回滚策略
- 全程做一致性校验
- 先灰度再全量

## 示例 3：前端类组件迁移到 Hooks

```text
User: /plan Refactor our React app from class components to hooks

Claude: I'll create a systematic refactoring plan.
```

建议分层推进：
- 先简单组件，再中等复杂组件，最后高复杂组件
- 抽取通用逻辑为 custom hooks
- 每小批次都验证测试与性能

## 规划模式实战建议

1. **先让计划可审阅**：先确认范围、依赖和验收标准
2. **分阶段执行**：每阶段可独立验收
3. **高风险任务必须有回滚方案**
4. **优先改动最小闭环**：减少一次性爆改
5. **配合 checkpoints 使用**：失败可快速回退

## 推荐提示词模板

```text
/plan [任务描述]

请输出：
1) 分阶段计划
2) 每阶段目标与产出
3) 风险与回滚策略
4) 预计改动文件与测试策略
5) 预计耗时
```
