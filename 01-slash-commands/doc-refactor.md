---
name: doc-refactor
description: Restructure project documentation for clarity and accessibility
---

# Documentation Refactor

Refactor project documentation structure adapted to project type:

1. **Analyze project**: Identify type (library/API/web app/CLI/microservices), architecture, and user personas
2. **Centralize docs**: Move technical documentation to `docs/` with proper cross-references
3. **Root README.md**: Streamline as entry point with overview, quickstart, modules/components summary, license, contacts
4. **Component docs**: Add module/package/service-level README files with setup and testing instructions
5. **Organize `docs/`** by relevant categories:
   - Architecture, API Reference, Database, Design, Troubleshooting, Deployment, Contributing (adapt to project needs)
6. **Create guides** (select applicable):
   - User Guide: End-user documentation for applications
   - API Documentation: Endpoints, authentication, examples for APIs
   - Development Guide: Setup, testing, contribution workflow
   - Deployment Guide: Production deployment for services/apps
7. **Use Mermaid** for all diagrams (architecture, flows, schemas)

Keep docs concise, scannable, and contextual to project type.

---
**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/commands
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
