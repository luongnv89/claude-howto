---
name: Expand Unit Tests
description: 通过覆盖未测试分支与边界场景提升测试覆盖率
tags: testing, coverage, unit-tests
---

# Expand Unit Tests

按项目测试框架扩展现有单元测试：

1. **分析覆盖率**：运行覆盖率报告，定位未覆盖分支、边界场景与低覆盖区域
2. **识别缺口**：检查逻辑分支、错误路径、边界条件、空值/空输入
3. **按项目框架编写测试**：
   - Jest/Vitest/Mocha（JavaScript/TypeScript）
   - pytest/unittest（Python）
   - Go testing/testify（Go）
   - Rust test framework（Rust）
4. **聚焦关键场景**：
   - 错误处理与异常路径
   - 边界值（最小/最大、空、null）
   - 极端与角落场景
   - 状态迁移与副作用
5. **验证提升**：再次运行覆盖率，确认覆盖率有可量化增长

仅输出新增测试代码块。遵循现有测试模式与命名规范。
