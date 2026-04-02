# My Development Preferences

## About Me
- **Experience Level**: 8 年全栈开发经验
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: 直接、配示例
- **Learning Style**: 代码 + 可视化图示

## Code Preferences

### Error Handling
我偏好显式错误处理（try-catch）与有意义的错误信息。避免通用错误；调试时始终记录错误日志。

### Comments
注释应解释 WHY，而不是 WHAT。代码本身应尽量自解释。注释重点应放在业务逻辑或不直观的决策上。

### Testing
我偏好 TDD（测试驱动开发）。先写测试，再写实现。聚焦行为，不聚焦实现细节。

### Architecture
我偏好模块化、低耦合设计。使用依赖注入提升可测试性。明确关注点分离（Controllers、Services、Repositories）。

## Debugging Preferences
- `console.log` 前缀统一为：`[DEBUG]`
- 日志必须携带上下文：函数名、关键变量
- 可用时输出 stack trace
- 日志中始终包含时间戳

## Communication
- 复杂概念优先用图解释
- 先给具体示例，再讲原理
- 给出 before/after 代码片段
- 在结尾总结关键点

## Project Organization
我偏好的项目结构：
```text
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling
- **IDE**: VS Code（vim 键位）
- **Terminal**: Zsh + Oh-My-Zsh
- **Format**: Prettier（100 字符行宽）
- **Linter**: ESLint（airbnb 配置）
- **Test Framework**: Jest + React Testing Library
