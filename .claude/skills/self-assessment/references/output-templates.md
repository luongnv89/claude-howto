# Output Templates

Blank markdown templates for the assessment results and learning path. The Step 3A/3B result templates and the Step 4 path-format template are duplicated verbatim in SKILL.md so results can be produced without re-reading this file.

## Quick Assessment results (Step 3A)

```markdown
## Claude Code Skill Assessment Results

### Your Level: [Level 1: Beginner / Level 2: Intermediate / Level 3: Advanced]

You checked **N/8** items.

[One-line motivational summary based on level]

### Your Skill Profile

| Area | Status |
|------|--------|
| Basic CLI & Conversations | [Checked/Gap] |
| CLAUDE.md & Memory | [Checked/Gap] |
| Slash Commands (built-in) | [Checked/Gap] |
| Custom Commands & Skills | [Checked/Gap] |
| MCP Servers | [Checked/Gap] |
| Hooks | [Checked/Gap] |
| Subagents | [Checked/Gap] |
| Print Mode & CI/CD | [Checked/Gap] |

### Identified Gaps

[For each unchecked item, provide a 1-line description of what to learn and a link to the tutorial]

### Your Personalized Learning Path

[Output the level-specific learning path — see Step 4]
```

## Deep Assessment results (Step 3B)

```markdown
## Claude Code Skill Assessment Results

### Overall Level: [Level 1 / Level 2 / Level 3]

**Total Score: N/19 points**

[One-line motivational summary]

### Your Skill Profile

| Feature Area | Score | Mastery | Status |
|-------------|-------|---------|--------|
| Slash Commands | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Memory | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Skills | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Hooks | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| MCP | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Subagents | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Checkpoints | N/1 | [None/Proficient] | [Learn/Mastered] |
| Advanced Features | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| Plugins | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |
| CLI | N/2 | [None/Basic/Proficient] | [Learn/Review/Mastered] |

**Mastery key:** 0 = None, 1 = Basic, 2 = Proficient

### Strength Areas
[List topics with score 2/2 — these are mastered]

### Priority Gaps (Learn Next)
[List topics with score 0 — these need attention first, ordered by dependency]

### Review Areas
[List topics with score 1/2 — basics known but advanced features not yet used]

### Your Personalized Learning Path

[Output gap-specific learning path — see Step 4]
```

## Learning Path (Step 4)

```markdown
### Your Personalized Learning Path

**Estimated time**: ~N hours (adjusted for your current skills)

#### Phase 1: [Phase Name] (~N hours)
[Only if they have gaps in these areas]

**[Topic Name]** — [Learn from scratch / Deep dive into advanced features]
- Tutorial: [link to tutorial directory]
- Focus on: [specific sections/concepts they need]
- Key exercise: [one concrete exercise to do]
- You'll know it's done when: [specific success criterion]

**[Topic Name]** — ...

---

#### Phase 2: [Phase Name] (~N hours)
...

---

### Recommended Practice Projects

Based on your gaps, try these real-world exercises to solidify your learning:

1. **[Project name]**: [1-line description combining 2-3 gap topics]
2. **[Project name]**: [1-line description]
3. **[Project name]**: [1-line description]
```

---

**Last Updated**: August 25, 2026
**Claude Code Version**: 2.1.245
**Sources**:
- https://code.claude.com/docs/en/overview
