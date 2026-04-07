import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Claude How To',
  description: '用一个周末掌握 Claude Code',
  lang: 'zh-CN',

  // Clean URLs without .html extension
  cleanUrls: true,

  // Last updated timestamp
  lastUpdated: true,

  // Exclude docs/plans from build
  srcExclude: ['docs/plans/**', 'resources/**'],

  // Ignore dead links for files in parent repo
  ignoreDeadLinks: true,

  // Head tags
  head: [
    ['meta', { name: 'theme-color', content: '#22C55E' }],
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:locale', content: 'zh-CN' }],
  ],

  // Markdown configuration
  markdown: {
    // Enable Mermaid diagrams
    mermaid: true,
  },

  // Theme configuration
  themeConfig: {
    // Logo
    logo: '/logos/claude-howto-logo.svg',
    siteTitle: 'Claude How To',

    // Navigation
    nav: [
      { text: '首页', link: '/' },
      { text: '学习路线', link: '/LEARNING-ROADMAP' },
      { text: '功能目录', link: '/CATALOG' },
      { text: '快速参考', link: '/QUICK_REFERENCE' },
    ],

    // Sidebar - preserving 01-10 module ordering
    sidebar: [
      {
        text: '开始',
        items: [
          { text: '简介', link: '/' },
          { text: '学习路线图', link: '/LEARNING-ROADMAP' },
          { text: '功能目录', link: '/CATALOG' },
          { text: '快速参考', link: '/QUICK_REFERENCE' },
        ]
      },
      {
        text: '01. Slash Commands',
        link: '/01-slash-commands/',
        collapsed: false,
        items: [
          { text: '概述', link: '/01-slash-commands/' },
          { text: 'optimize', link: '/01-slash-commands/optimize' },
          { text: 'pr', link: '/01-slash-commands/pr' },
          { text: 'commit', link: '/01-slash-commands/commit' },
          { text: 'generate-api-docs', link: '/01-slash-commands/generate-api-docs' },
          { text: 'setup-ci-cd', link: '/01-slash-commands/setup-ci-cd' },
          { text: 'push-all', link: '/01-slash-commands/push-all' },
          { text: 'unit-test-expand', link: '/01-slash-commands/unit-test-expand' },
          { text: 'doc-refactor', link: '/01-slash-commands/doc-refactor' },
        ]
      },
      {
        text: '02. Memory',
        link: '/02-memory/',
        collapsed: true,
        items: [
          { text: '概述', link: '/02-memory/' },
          { text: '项目 Memory', link: '/02-memory/project-CLAUDE' },
          { text: '目录 Memory', link: '/02-memory/directory-api-CLAUDE' },
          { text: '个人 Memory', link: '/02-memory/personal-CLAUDE' },
        ]
      },
      {
        text: '03. Skills',
        link: '/03-skills/',
        collapsed: true,
        items: [
          { text: '概述', link: '/03-skills/' },
          { text: '代码审查', link: '/03-skills/code-review/SKILL' },
          { text: '品牌语气', link: '/03-skills/brand-voice/SKILL' },
          { text: '文档生成', link: '/03-skills/doc-generator/SKILL' },
          { text: '重构', link: '/03-skills/refactor/SKILL' },
          { text: 'Claude MD', link: '/03-skills/claude-md/SKILL' },
          { text: '博客草稿', link: '/03-skills/blog-draft/SKILL' },
        ]
      },
      {
        text: '04. Subagents',
        link: '/04-subagents/',
        collapsed: true,
        items: [
          { text: '概述', link: '/04-subagents/' },
          { text: '代码审查员', link: '/04-subagents/code-reviewer' },
          { text: '测试工程师', link: '/04-subagents/test-engineer' },
          { text: '文档作者', link: '/04-subagents/documentation-writer' },
          { text: '安全审查员', link: '/04-subagents/secure-reviewer' },
          { text: '实现代理', link: '/04-subagents/implementation-agent' },
          { text: '调试专家', link: '/04-subagents/debugger' },
          { text: '数据科学家', link: '/04-subagents/data-scientist' },
          { text: '整洁代码审查员', link: '/04-subagents/clean-code-reviewer' },
        ]
      },
      {
        text: '05. MCP Protocol',
        link: '/05-mcp/',
        collapsed: true,
        items: [
          { text: '概述', link: '/05-mcp/' },
        ]
      },
      {
        text: '06. Hooks',
        link: '/06-hooks/',
        collapsed: true,
        items: [
          { text: '概述', link: '/06-hooks/' },
        ]
      },
      {
        text: '07. Plugins',
        link: '/07-plugins/',
        collapsed: true,
        items: [
          { text: '概述', link: '/07-plugins/' },
          { text: 'PR 审查', link: '/07-plugins/pr-review/' },
          { text: 'DevOps 自动化', link: '/07-plugins/devops-automation/' },
          { text: '文档生成', link: '/07-plugins/documentation/' },
        ]
      },
      {
        text: '08. Checkpoints',
        link: '/08-checkpoints/',
        collapsed: true,
        items: [
          { text: '概述', link: '/08-checkpoints/' },
          { text: '示例', link: '/08-checkpoints/checkpoint-examples' },
        ]
      },
      {
        text: '09. 高级功能',
        link: '/09-advanced-features/',
        collapsed: true,
        items: [
          { text: '概述', link: '/09-advanced-features/' },
          { text: '规划模式示例', link: '/09-advanced-features/planning-mode-examples' },
        ]
      },
      {
        text: '10. CLI 参考',
        link: '/10-cli/',
        collapsed: true,
        items: [
          { text: '概述', link: '/10-cli/' },
        ]
      },
    ],

    // Social links
    socialLinks: [
      { icon: 'github', link: 'https://github.com/luongnv89/claude-howto' }
    ],

    // Footer
    footer: {
      message: '基于 MIT 许可证发布',
      copyright: 'Copyright © 2026 Claude How To'
    },

    // Edit link
    editLink: {
      pattern: 'https://github.com/luongnv89/claude-howto/edit/main/zh/:path',
      text: '在 GitHub 上编辑此页'
    },

    // Local search with Chinese translations
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档'
          },
          modal: {
            noResultsText: '无法找到相关结果',
            resetButtonTitle: '清除查询条件',
            backButtonTitle: '关闭搜索',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭',
              navigateUpKeyAriaLabel: '上箭头',
              navigateDownKeyAriaLabel: '下箭头',
              closeKeyAriaLabel: 'ESC'
            }
          }
        }
      }
    },

    // Outline
    outline: {
      level: [2, 3],
      label: '目录'
    },

    // Doc footer
    docFooter: {
      prev: '上一页',
      next: '下一页'
    },

    // Last updated
    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'short'
      }
    },

    // Return to top
    returnToTopLabel: '返回顶部',

    // Sidebar menu label
    sidebarMenuLabel: '菜单',

    // Dark mode switch
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
  },

  // Vite config
  vite: {
    build: {
      minify: 'esbuild',
      chunkSizeWarningLimit: 1500
    }
  }
})