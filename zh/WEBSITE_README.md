# Claude How To 中文教程网站

这是 Claude How To 中文教程的 VitePress 静态网站版本，适用于内网部署。

## 快速开始

### 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run docs:dev

# 访问 http://localhost:5173
```

### 构建

```bash
# 构建静态文件
npm run docs:build

# 输出位于 .vitepress/dist/
```

### 预览构建结果

```bash
npm run docs:preview
```

## Docker 部署

### 构建镜像

```bash
docker build -t claude-howto:latest .
```

### 运行容器

```bash
docker run -d -p 3000:80 --name claude-howto-docs claude-howto:latest
```

### 使用 Docker Compose

```bash
docker-compose up -d
```

访问 `http://localhost:3000`

## 项目结构

```
.
├── .vitepress/
│   ├── config.ts          # VitePress 配置
│   ├── public/
│   │   └── logos/         # Logo 静态资源
│   └── theme/
│       ├── index.ts       # 自定义主题入口
│       ├── custom.css     # 品牌颜色和样式
│       └── components/
│           └── ProgressTracker.vue  # 学习进度跟踪组件
├── 01-slash-commands/     # 模块 1
├── 02-memory/             # 模块 2
├── ...                    # 其他模块
├── 10-cli/                # 模块 10
├── Dockerfile             # Docker 构建文件
├── docker-compose.yml     # Docker Compose 配置
├── nginx.conf             # Nginx 配置
└── package.json           # Node.js 依赖
```

## 功能特性

- **学习路径进度跟踪** - 使用 localStorage 记录学习进度
- **Mermaid 图表渲染** - 客户端渲染所有 Mermaid 图表
- **中文搜索** - 内置本地搜索支持中文
- **深色/浅色模式** - 支持主题切换
- **品牌配色** - 使用 Claude How To 设计系统颜色

## 技术栈

- [VitePress](https://vitepress.dev/) - Vue 驱动的静态站点生成器
- [Vue 3](https://vuejs.org/) - 渐进式 JavaScript 框架
- [Mermaid](https://mermaid.js.org/) - 基于 JavaScript 的图表工具
- [Nginx](https://nginx.org/) - 高性能 Web 服务器

## 自定义配置

### 修改端口

在 `docker-compose.yml` 中修改端口映射：

```yaml
ports:
  - "8080:80"  # 改为所需端口
```

### 修改品牌颜色

编辑 `.vitepress/theme/custom.css`：

```css
:root {
  --vp-c-brand-1: #22C55E;  /* 主色调 */
  --vp-c-brand-2: #16A34A;  /* 悬停色 */
}
```

## 许可证

MIT License