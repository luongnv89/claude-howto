# Jira Cloud Setup Guide

Step-by-step instructions for setting up Jira Cloud and the Atlassian MCP server for Claude Code integration. This guide covers account creation, API token generation, and MCP configuration.

## Step 1: Create a Jira Cloud Account

If you do not already have a Jira Cloud account:

1. Go to [https://www.atlassian.com/software/jira/free](https://www.atlassian.com/software/jira/free)
2. Click "Get it free" and sign up with your email
3. Choose a site name (e.g., `yourname-qa.atlassian.net`)
4. Select the **Free** plan (supports up to 10 users, which is sufficient for this bootcamp)
5. Complete the onboarding wizard -- you can skip the team invitation step

Your Jira Cloud instance will be available at `https://yourname-qa.atlassian.net`.

## Step 2: Generate an Atlassian API Token

The Atlassian MCP server authenticates using an API token (not your account password).

1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click "Create API token"
3. Give it a label (e.g., "Claude Code Bootcamp")
4. Click "Create"
5. **Copy the token immediately** -- you cannot view it again after closing the dialog

Store the token securely. You will need three pieces of information for the MCP configuration:

| Value | Example | Where to Find |
|-------|---------|---------------|
| Site URL | `https://yourname-qa.atlassian.net` | Your Jira Cloud URL |
| Email | `you@example.com` | The email you signed up with |
| API Token | `ATATT3x...` | Generated in step 2 above |

## Step 3: Configure the Atlassian MCP Server

Ask Claude Code to add the Atlassian MCP server to your project. You will need to provide:

- Your Jira site URL
- Your Atlassian email address
- Your API token

Claude will create or update the `.mcp.json` file in your project root. The configuration will look similar to this:

```json
{
  "mcpServers": {
    "atlassian": {
      "command": "npx",
      "args": ["-y", "@aashari/mcp-server-atlassian-jira"],
      "env": {
        "ATLASSIAN_SITE_URL": "https://yourname-qa.atlassian.net",
        "ATLASSIAN_USER_EMAIL": "you@example.com",
        "ATLASSIAN_API_TOKEN": "<your-api-token>"
      }
    }
  }
}
```

After configuring, **restart Claude Code** for the MCP server to be discovered.

## Step 4: Verify the Connection

Once Claude Code restarts with the Atlassian MCP configured:

- Ask Claude to list your Jira projects -- it should be able to query your Jira instance
- If you get authentication errors, verify your email and token are correct
- If the MCP server is not found, check that `npx` can install the package

## Step 5: Create Your QA Command Center Project in Jira

Use Claude Code to create your project management structure. Think about what a QA Command Center project needs:

- **Project**: The QA Command Center itself
- **Epics**: Major feature areas (test management, bug tracking, reporting, integrations)
- **Stories**: Specific work items under each epic with acceptance criteria

All project management should go through Claude Code conversations, not the Jira web UI. This is a core rule of the bootcamp: Claude does the work, you provide the direction.

## Security Notes

### Token Permissions

The API token inherits the permissions of your Atlassian account. For the free tier, this typically includes:

- Create and manage projects
- Create and manage issues (epics, stories, tasks, bugs)
- Read and update issue status
- Manage sprints and boards

### Token Storage

- **Do not commit your API token to version control.** If your repository is public, anyone can access your Jira instance.
- The `.mcp.json` file contains your token in the `env` field. Consider adding it to `.gitignore`.
- Alternatively, set environment variables in your shell profile and reference them in `.mcp.json`.

### Token Rotation

- API tokens do not expire automatically on the free tier
- Revoke and regenerate tokens if compromised
- You can manage tokens at [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

## Troubleshooting

| Issue | Solution |
|-------|---------|
| "Unauthorized" errors | Verify email and API token are correct |
| "Site not found" | Check the site URL format: `https://site.atlassian.net` (no trailing slash) |
| MCP server not loading | Restart Claude Code after editing `.mcp.json` |
| Cannot create project | Free tier may limit project types; use "Scrum" or "Kanban" software project |
| npx install fails | Run `npx -y @aashari/mcp-server-atlassian-jira --help` to test package availability |

## Quick Checklist

Before starting Session 5's Jira integration:

- [ ] Jira Cloud account created and accessible
- [ ] API token generated and saved securely
- [ ] Site URL, email, and token noted for configuration
- [ ] Atlassian MCP server entry added to `.mcp.json`
- [ ] Claude Code restarted after MCP configuration
- [ ] Claude can successfully query your Jira instance
