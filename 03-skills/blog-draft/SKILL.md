---
name: blog-draft
description: Draft a blog post from ideas and resources. Use when users want to write a blog post, create content from research, or draft articles. Guides through research, brainstorming, outlining, and iterative drafting with version control.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding. User should provide:
- **Idea/Topic**: The main concept or theme for the blog post
- **Resources**: URLs, files, or references to research (optional but recommended)
- **Target audience**: Who the blog post is for (optional)
- **Tone/Style**: Formal, casual, technical, etc. (optional)

**IMPORTANT**: If the user is requesting updates to an **existing blog post**, skip steps 0-8 and start directly at **Step 9**. Read the existing draft file(s) first, then proceed with the iteration process.

## Execution Flow

Follow these steps sequentially. **Do not skip steps or proceed without user approval where indicated.**

### Step 0: Create Project Folder

1. Generate a folder name using format: `YYYY-MM-DD-short-topic-name`
   - Use today's date
   - Create a short, URL-friendly slug from the topic (lowercase, hyphens, max 5 words)

2. Create the folder structure:
   ```
   blog-posts/
   └── YYYY-MM-DD-short-topic-name/
       └── resources/
   ```

3. Confirm folder creation with user before proceeding.

### Step 1: Research & Resource Collection

1. Create `resources/` subfolder in the blog post directory

2. For each provided resource:
   - **URLs**: Fetch and save key information to `resources/` as markdown files
   - **Files**: Read and summarize in `resources/`
   - **Topics**: Use web search to gather up-to-date information

3. For each resource, create a summary file in `resources/`:
   - `resources/source-1-[short-name].md`
   - `resources/source-2-[short-name].md`
   - etc.

4. Each summary should include:
   ```markdown
   # Source: [Title/URL]

   ## Key Points
   - Point 1
   - Point 2

   ## Relevant Quotes/Data
   - Quote or statistic 1
   - Quote or statistic 2

   ## How This Relates to Topic
   Brief explanation of relevance
   ```

5. Present research summary to user.

### Step 2: Brainstorm & Clarify

1. Based on the idea and researched resources, present:
   - **Main themes** identified from research
   - **Potential angles** for the blog post
   - **Key points** that should be covered
   - **Gaps** in information that need clarification

2. Ask clarifying questions:
   - What is the main takeaway you want readers to have?
   - Are there specific points from the research you want to emphasize?
   - What's the target length? (short: 500-800 words, medium: 1000-1500, long: 2000+)
   - Any points you want to exclude?

3. **Wait for user responses before proceeding.**

### Step 3: Propose Outline

1. Create a structured outline including:

   ```markdown
   # Blog Post Outline: [Title]

   ## Meta Information
   - **Target Audience**: [who]
   - **Tone**: [style]
   - **Target Length**: [word count]
   - **Main Takeaway**: [key message]

   ## Proposed Structure

   ### Hook/Introduction
   - Opening hook idea
   - Context setting
   - Thesis statement

   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Supporting evidence from [source]

   ### Section 2: [Title]
   - Key point A
   - Key point B

   [Continue for all sections...]

   ### Conclusion
   - Summary of key points
   - Call to action or final thought

   ## Sources to Cite
   - Source 1
   - Source 2
   ```

2. Present outline to user and **ask for approval or modifications**.

### Step 4: Save Approved Outline

1. Once user approves the outline, save it to `OUTLINE.md` in the blog post folder.

2. Confirm the outline has been saved.

### Step 5: Commit Outline (if in git repo)

1. Check if current directory is a git repository.

2. If yes:
   - Stage the new files: blog post folder, resources, and OUTLINE.md
   - Create commit with message: `docs: Add outline for blog post - [topic-name]`
   - Push to remote

3. If not a git repo, skip this step and inform user.

### Step 6: Write Draft

1. Based on the approved outline, write the full blog post draft.

2. Follow the structure from OUTLINE.md exactly.

3. Include:
   - Engaging introduction with hook
   - Clear section headers
   - Supporting evidence and examples from research
   - Smooth transitions between sections
   - Strong conclusion with takeaway
   - **Citations**: All comparisons, statistics, data points, and factual claims MUST cite the original source

4. Save the draft as `draft-v0.1.md` in the blog post folder.

5. Format:
   ```markdown
   # [Blog Post Title]

   *[Optional: subtitle or tagline]*

   [Full content with inline citations...]

   ---

   ## References
   - [1] Source 1 Title - URL or Citation
   - [2] Source 2 Title - URL or Citation
   - [3] Source 3 Title - URL or Citation
   ```

6. **Citation Requirements**:
   - Every data point, statistic, or comparison MUST have an inline citation
   - Use numbered references [1], [2], etc., or named citations [Source Name]
   - Link citations to the References section at the end
   - Example: "Studies show that 65% of developers prefer TypeScript [1]"
   - Example: "React outperforms Vue in rendering speed by 20% [React Benchmarks 2024]"

### Step 7: Commit Draft (if in git repo)

1. Check if in git repository.

2. If yes:
   - Stage the draft file
   - Create commit with message: `docs: Add draft v0.1 for blog post - [topic-name]`
   - Push to remote

3. If not a git repo, skip and inform user.

### Step 8: Present Draft for Review

1. Present the draft content to user.

2. Ask for feedback:
   - Overall impression?
   - Sections that need expansion or reduction?
   - Tone adjustments needed?
   - Missing information?
   - Specific edits or rewrites?

3. **Wait for user response.**

### Step 9: Iterate or Finalize

**If user requests changes:**
1. Note all requested modifications
2. Return to Step 6 with the following adjustments:
   - Increment version number (v0.2, v0.3, etc.)
   - Incorporate all feedback
   - Save as `draft-v[X.Y].md`
   - Repeat Steps 7-8

**If user approves:**
1. Confirm the final draft version
2. Optionally rename to `final.md` if user requests
3. Summarize the blog post creation process:
   - Total versions created
   - Key changes between versions
   - Final word count
   - Files created

## Version Tracking

All drafts are preserved with incremental versioning:
- `draft-v0.1.md` - Initial draft
- `draft-v0.2.md` - After first round of feedback
- `draft-v0.3.md` - After second round of feedback
- etc.

This allows tracking the evolution of the blog post and reverting if needed.

## Output Files Structure

```
blog-posts/
└── YYYY-MM-DD-topic-name/
    ├── resources/
    │   ├── source-1-name.md
    │   ├── source-2-name.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (if iterations)
    └── draft-v0.3.md (if more iterations)
```

## Tips for Quality

- **Hook**: Start with a question, surprising fact, or relatable scenario
- **Flow**: Each paragraph should connect to the next
- **Evidence**: Support claims with data from research
- **Citations**: ALWAYS cite sources for:
  - All statistics and data points (e.g., "According to [Source], 75% of...")
  - Comparisons between products, services, or approaches (e.g., "X performs 2x faster than Y [Source]")
  - Factual claims about market trends, research findings, or benchmarks
  - Use inline citations with format: [Source Name] or [Author, Year]
- **Voice**: Maintain consistent tone throughout
- **Length**: Respect the target word count
- **Readability**: Use short paragraphs, bullet points where appropriate
- **CTA**: End with a clear call-to-action or thought-provoking question

## Notes

- Always wait for user approval at outlined checkpoints
- Preserve all draft versions for history
- Use web search for up-to-date information when URLs are provided
- If resources are insufficient, ask user for more or suggest additional research
- Adapt tone based on target audience (technical, general, business, etc.)

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
