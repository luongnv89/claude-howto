# Instructor Guide

Complete guide for running the AI Bootcamp. Covers cohort management, session facilitation, troubleshooting, and grading.

## Before the Bootcamp

### Environment Checklist

Verify all workstations have:

- [ ] Claude Code CLI installed and authenticated
- [ ] Node.js 18+ and npm
- [ ] Python 3.10+
- [ ] Git configured with GitHub access
- [ ] Internet access (for MCP servers, Jira API, npm)
- [ ] VS Code or JetBrains IDE (recommended)

### Cohort Setup

```bash
cd workshop

# Create a new cohort
./bootcamp open-registration --cohort "TDL-2026-Q2" --deadline "2026-04-20"

# Register students (can also be done via CSV import)
./bootcamp register student001 "Alice Smith" alice@testdevlab.com
./bootcamp register student002 "Bob Johnson" bob@testdevlab.com

# Verify roster
./bootcamp dashboard
```

### Jira Cloud Setup (Sessions 5+)

Before Half-Day 3, ensure:

1. A Jira Cloud instance is available (free tier: `<org>.atlassian.net`)
2. Each student has an Atlassian API token
3. The Atlassian MCP server package is available: `@aashari/mcp-server-atlassian-jira`
   (community-maintained; verify currency at https://npm.im/@aashari/mcp-server-atlassian-jira before each cohort. Anthropic does not publish a first-party Atlassian MCP at the time of writing — use the Claude Code built-in plugin via `claude /plugin install atlassian` if available, otherwise the community package above.)

### Pre-Session Dry Run

Run through Session 1 yourself to verify:

- `./bootcamp setup` completes without errors
- Claude Code can scaffold a Vite + React + Express project
- Hooks are logging prompts to `~/.claude-bootcamp/logs/`
- `./bootcamp complete-session 1` gate checks work

## During the Bootcamp

### Half-Day Schedule Template

| Time | Activity | Duration | Notes |
|------|----------|----------|-------|
| 0:00 | Welcome and context | 5 min | Recap previous half-day (if applicable) |
| 0:05 | Session N overview | 10 min | Explain the feature, show deliverables list |
| 0:15 | Students work | 50 min | Walk around, answer questions, do NOT give prompts |
| 1:05 | Session N wrap-up | 10 min | Quick show-and-tell, common issues |
| 1:15 | Break | 15 min | |
| 1:30 | Session N+1 overview | 10 min | Explain the feature, show deliverables list |
| 1:40 | Students work | 50 min | Walk around, answer questions |
| 2:30 | Session N+1 wrap-up | 10 min | Show-and-tell, preview next half-day |
| 2:40 | Q&A and buffer | 20 min | Handle stragglers, celebrate wins |

### Facilitation Rules

1. **Never give prompts.** Students must craft their own. If stuck, ask guiding questions: "What does Claude need to know to build that?" or "What would you tell a junior developer to do?"

2. **Encourage pair work.** Manual QA drives (prompts Claude), automation QA navigates (reviews generated code). Mirrors real project teams.

3. **Let them fail.** Bad prompts are learning opportunities. If a student gets garbage output, ask: "What was missing from your prompt?" Don't intervene too quickly.

4. **Monitor the dashboard.** Run `./bootcamp dashboard` on a separate screen. Watch for:
   - Students stuck on one prompt for >10 minutes
   - Students who haven't started
   - Gate failures that indicate misunderstanding

5. **Progressive independence.** Sessions 1-3: more hand-holding, explain concepts. Sessions 4-7: answer questions only. Sessions 8-10: fully independent.

### Common Issues and Fixes

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| "Claude doesn't know about my project" | Missing CLAUDE.md or wrong directory | Check `pwd`, verify CLAUDE.md exists |
| Hooks not logging | Setup incomplete | Re-run `./bootcamp setup` |
| Gate check fails unexpectedly | Files in wrong location | Check deliverables.md for exact paths |
| MCP connection fails | Missing API token | Verify environment variables |
| Jira API returns 401 | Expired or wrong token | Regenerate Atlassian API token |
| Student falls behind | Overwhelmed or stuck | Offer checkpoint restore for previous session |

### Handling Different Skill Levels

**Manual QAs (no coding background):**

- Emphasize that Claude writes ALL the code
- Focus on describing features in plain English
- Pair with automation QAs for code review discussions
- Extra time on Sessions 1-2 (foundational concepts)

**Automation QAs (coding experience):**

- Challenge them with the "should-have" bonus items in deliverables
- Encourage them to inspect and understand generated code
- Have them write hook configs directly instead of describing them
- Extra focus on Sessions 5-6 and 9-10 (integration and CI/CD)

## After the Bootcamp

### Generating Final Scores

```bash
# Score all students
./bootcamp scores --format html --output cohort-report.html

# Score a specific student
./bootcamp grade student001

# Export to CSV for spreadsheets
./bootcamp scores --format csv --output scores.csv
```

### Score Review

Review scores before sharing. Look for:

- Students who scored high on deliverables but low on prompt quality (may have copy-pasted)
- Students who scored high on efficiency but low on deliverables (took shortcuts)
- Outlier scores that may indicate technical issues (hooks not logging, etc.)

### Feedback Collection

After the bootcamp:

1. Share individual scores with detailed breakdowns
2. Highlight top performers (90+ scores)
3. Provide improvement paths for students below 70
4. Collect instructor notes for next cohort improvements

### Closing Registration

```bash
./bootcamp close-registration
```

## Monitoring Commands Reference

```bash
# Real-time dashboard of all students
./bootcamp dashboard

# Check specific student progress
./bootcamp status --student student001

# View prompt logs for a student
./bootcamp status --student student001 --prompts

# Export all scores
./bootcamp scores --format json

# Grade a specific student (full analysis)
./bootcamp grade student001
```
