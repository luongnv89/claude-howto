---
name: Documentation Refactor
description: 为提升清晰度与可访问性而重构项目文档结构
tags: documentation, refactoring, organization
---

# Documentation Refactor

按项目类型调整并重构文档结构：

1. **分析项目**：识别类型（库/API/Web 应用/CLI/微服务）、架构与用户画像
2. **集中管理文档**：将技术文档归集到 `docs/`，并建立正确的交叉引用
3. **根 README.md**：精简为入口页，包含概览、快速开始、模块/组件摘要、许可证、联系方式
4. **组件文档**：为模块/包/服务补充 README，包含安装与测试说明
5. **按相关类别组织 `docs/`**：
   - Architecture、API Reference、Database、Design、Troubleshooting、Deployment、Contributing（按项目需求调整）
6. **创建指南（按需选择）**：
   - User Guide：面向应用终端用户
   - API Documentation：面向 API，含端点、认证、示例
   - Development Guide：开发环境、测试、贡献流程
   - Deployment Guide：服务/应用的生产部署
7. **所有图表统一使用 Mermaid**（架构图、流程图、模式图）

保持文档简洁、可快速扫描，并与项目类型保持上下文一致。
