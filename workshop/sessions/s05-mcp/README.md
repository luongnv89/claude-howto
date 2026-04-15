# Session 5: Connecting to the QA Ecosystem -- MCP

Your QA Command Center has test cases, test suites, bugs, and specialized agents -- but it is an island. In this session, you connect it to the real QA ecosystem: GitHub for issue tracking and Jira Cloud for project management. All integrations go through MCP (Model Context Protocol), giving Claude direct access to external APIs.

## Learning Objectives

- Understand MCP architecture: transports, servers, tools, and resources
- Configure MCP servers in `.mcp.json` for project-scoped integrations
- Connect GitHub MCP for issue tracking and bug-to-issue synchronization
- Connect Atlassian MCP for Jira project management (epics, stories, sprints)
- Understand environment variable handling and security for API tokens
- Build UI features that bridge your local app with external services

## Prerequisites

- Session 4 gate passed (`./bootcamp complete-session 4`)
- Bug tracker module working with CRUD operations
- **GitHub personal access token** (Settings > Developer settings > Personal access tokens)
- **Jira Cloud account** with an Atlassian API token (see [jira-setup-guide.md](jira-setup-guide.md))

## Schedule

| Time | Activity | Duration |
|------|----------|----------|
| 0:00 | MCP concepts and configuration setup | 15 min |
| 0:15 | GitHub MCP integration | 20 min |
| 0:35 | Jira/Atlassian MCP integration | 25 min |
| 1:00 | Build test run executor page | 15 min |
| **Total** | | **75 min** |

## The Feature: MCP (Model Context Protocol)

> **Reference module**: [05-mcp/README.md](../../05-mcp/README.md)

MCP is a standardized protocol that gives Claude access to external tools, APIs, and data sources. Instead of you manually calling APIs and pasting results into Claude, MCP servers act as bridges that Claude calls directly.

### How MCP Works

```text
You <-> Claude Code <-> MCP Server <-> External Service
                          |
                     .mcp.json (configuration)
```

1. You configure an MCP server in `.mcp.json`
2. Claude discovers the server's available tools at startup
3. When you ask Claude to interact with the service, it calls the MCP tools directly
4. Results flow back through the MCP server to Claude

### MCP Configuration: .mcp.json

Project-scoped MCP configuration lives in `.mcp.json` at your project root:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-token>"
      }
    }
  }
}
```

Key points about `.mcp.json`:

- **Project scope**: Settings apply only to this project (vs `~/.claude.json` for global)
- **Environment variables**: Sensitive tokens go in the `env` field
- **Transport**: Most servers use `stdio` transport (command + args)
- **Multiple servers**: You can configure as many MCP servers as you need

### Adding MCP Servers via CLI

You can also add servers using the `claude mcp add` command:

```bash
claude mcp add github --command "npx" --args "-y" "@modelcontextprotocol/server-github" --env "GITHUB_PERSONAL_ACCESS_TOKEN=<token>"
```

### Available MCP Servers

For this session, you will use two servers:

| Server | Package | Purpose |
|--------|---------|---------|
| GitHub | `@modelcontextprotocol/server-github` | Issues, PRs, repos, code search |
| Atlassian | `@aashari/mcp-server-atlassian-jira` | Jira projects, epics, stories, sprints |

## What You Will Build

### 1. GitHub MCP Integration

Configure the GitHub MCP server and use it to:

- List your GitHub repositories and issues
- Create GitHub Issues from bugs in your bug tracker
- Add a "Create GitHub Issue" button to the bug tracker UI that syncs a local bug to a GitHub issue

The goal is bidirectional awareness: bugs created in your QA Command Center can be pushed to GitHub for developer visibility.

### 2. Jira MCP Integration

Configure the Atlassian MCP server and use Claude to:

- Create a Jira project for your QA Command Center
- Create at least one epic (e.g., "Test Management" or "Bug Tracking")
- Create stories under the epic with acceptance criteria
- All done via Claude Code conversations, not the Jira UI

This is where project management begins. From this session onward, you will manage your QA Command Center backlog in Jira.

> **Setup guide**: See [jira-setup-guide.md](jira-setup-guide.md) for step-by-step instructions on creating your Jira Cloud account and generating an Atlassian API token.

### 3. Test Run Executor Page

A new React page that represents the concept of executing test runs:

- Display a list of test suites available for execution
- A "Run" action that marks a suite as in-progress
- Status tracking: pending, running, passed, failed
- Results summary showing pass/fail counts
- Timestamp for when the run was executed

This page ties together test suites (Session 3) with an execution workflow, preparing for CI integration in Session 10.

## Requirements

### Must-Have (Gate Checks)

- [ ] `.mcp.json` exists in the project root
- [ ] GitHub MCP server is configured in `.mcp.json`
- [ ] Atlassian/Jira MCP server is configured in `.mcp.json`
- [ ] Test run executor React page exists and renders
- [ ] At least one successful MCP interaction has occurred (e.g., GitHub issues listed)

### Should-Have (Bonus Points)

- [ ] "Create GitHub Issue" button exists in the bug tracker UI
- [ ] Bug-to-issue sync works (creates a real GitHub issue from a local bug)
- [ ] Jira project exists with at least 1 epic
- [ ] Jira stories exist under the epic with acceptance criteria
- [ ] Test run executor shows status badges (pending/running/passed/failed)
- [ ] MCP environment variables are properly configured (not hardcoded in committed files)

## Rules

1. **All external interactions through Claude Code.** Do not manually create Jira projects, epics, or stories through the Jira web UI. Do not use `curl` or Postman to call GitHub's API. Every interaction with external services must go through Claude Code using MCP tools.

2. **Secure your tokens.** Never commit API tokens to version control. Use environment variables in `.mcp.json` and consider adding `.mcp.json` to `.gitignore` if it contains sensitive values. Alternatively, use environment variable references that resolve at runtime.

3. **Create at least one Jira epic.** This is the beginning of your project management workflow. Think about what epics your QA Command Center needs. Each major feature area (test management, bug tracking, reporting) could be an epic.

4. **MCP is a tool, not a toy.** Use MCP for real QA workflows, not just to prove it works. Creating a GitHub issue from a bug report is a real workflow. Listing random repositories is a demo.

## Hints (Not Solutions)

### Setting Up GitHub MCP

- You need a GitHub personal access token. Generate one at GitHub Settings > Developer settings > Personal access tokens > Tokens (classic). Give it `repo` and `issues` scopes.
- Ask Claude to help you configure the GitHub MCP server. Describe what you want to connect to and let Claude set up the `.mcp.json` configuration.
- Once configured, try asking Claude to list your GitHub issues or repositories. This verifies the connection works.

### Setting Up Jira MCP

- Follow [jira-setup-guide.md](jira-setup-guide.md) first to create your Jira Cloud account and API token.
- The Atlassian MCP server needs your Atlassian email and API token. Ask Claude to configure it.
- Start by asking Claude to create a Jira project. Then describe the epics and stories you want. Think in terms of QA Command Center features: what work items would a QA team track?

### Bug-to-Issue Sync

- The "Create GitHub Issue" button is a UI element in your bug tracker that triggers MCP through Claude. Think about how to bridge the gap: the button itself is a React component, but the actual GitHub issue creation happens when you describe the bug to Claude and ask it to create a GitHub issue.
- Consider what information from a bug report maps to a GitHub issue: title, description, labels (severity), assignees.

### Building the Test Run Executor

- A test run executor is a page that lets you "execute" test suites. In this context, execution means changing the status from pending to running to passed/failed.
- Think about the data model: a test run references a test suite, has a status, a start time, an end time, and results (how many test cases passed/failed).
- This page prepares for Session 10 where test runs will be triggered from CI pipelines.

### Common Pitfalls

- MCP servers need to be installed (typically via npx). If Claude cannot find the server, ensure Node.js and npm are working.
- Token permissions matter. A GitHub token without `repo` scope cannot access private repositories. A Jira token without project admin permissions cannot create projects.
- `.mcp.json` must be valid JSON. A missing comma or bracket will prevent all MCP servers from loading.
- If MCP tools are not appearing, restart Claude Code after modifying `.mcp.json`.

## Jira Integration

This session introduces Jira integration, which continues through the remaining sessions. See [jira-setup-guide.md](jira-setup-guide.md) for detailed setup instructions.

From this point forward:

- Each new feature should have a corresponding Jira epic or story
- Use Claude Code to create and update Jira tickets
- Link dependent tickets together
- Track your progress in Jira, not just in the gate checks

## Verification

Before running `./bootcamp complete-session 5`, verify:

1. **MCP configured**: `.mcp.json` exists with GitHub and Atlassian servers
2. **GitHub works**: Ask Claude to list your GitHub issues -- it should return results
3. **Jira works**: Ask Claude about your Jira project -- it should find the project and epics you created
4. **Test run page renders**: Navigate to the test run executor page in your browser
5. **Bug-to-issue sync** (bonus): If implemented, create a bug and push it to GitHub

```bash
./bootcamp complete-session 5
```

## What Comes Next

In Session 6, you will add automation through hooks -- event-driven scripts that run before and after Claude Code actions. You will create hooks that enforce your CLAUDE.md standards automatically, validate code before commits, and trigger notifications. The MCP connections from this session remain active and are used in later sessions for CI integration (Session 10).
