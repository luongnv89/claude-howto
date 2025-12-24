# Tasks: update-subagents-lesson

## Phase 1: Update README.md Structure

1. [x] **Update Overview section**
   - Add `/agents` command mention
   - Add built-in subagents overview
   - Update key benefits with official wording

2. [x] **Add File Locations section**
   - Document project subagents (`.claude/agents/`)
   - Document user subagents (`~/.claude/agents/`)
   - Document plugin agents
   - Document CLI-defined agents

3. [x] **Update Configuration section**
   - Update YAML frontmatter format with all fields
   - Add configuration fields table (name, description, tools, model, permissionMode, skills)
   - Add CLI-based configuration with `--agents` flag

## Phase 2: Add New Sections

4. [x] **Add Built-in Subagents section**
   - Document General-Purpose subagent (Sonnet, all tools)
   - Document Plan subagent (Sonnet, research tools)
   - Document Explore subagent (Haiku, read-only, thoroughness levels)

5. [x] **Add /agents Command section**
   - Document interactive menu options
   - Create, edit, delete operations
   - View available subagents

6. [x] **Add Resumable Agents section**
   - Document agentId concept
   - Show resume syntax
   - List use cases

7. [x] **Add Chaining Subagents section**
   - Multi-agent workflows
   - Sequential delegation

## Phase 3: Update Example Files

8. [x] **Update `code-reviewer.md`**
   - Add model field
   - Update to match official example format
   - Add proactive usage hints

9. [x] **Update `test-engineer.md`**
   - Add model field
   - Update system prompt format

10. [x] **Update `documentation-writer.md`**
    - Add model field
    - Update format

11. [x] **Update `secure-reviewer.md`**
    - Update to minimal permission pattern

12. [x] **Update `implementation-agent.md`**
    - Update tool list format

## Phase 4: Add New Example Files

13. [x] **Create `debugger.md`**
    - Copy from official docs example
    - Adapt to project style

14. [x] **Create `data-scientist.md`**
    - Copy from official docs example
    - Adapt to project style

## Phase 5: Finalize

15. [x] **Update Installation Instructions**
    - Add `/agents` method
    - Update verification steps

16. [x] **Update Related Concepts**
    - Link to new sections
    - Update comparison table

17. [x] **Update last modified date**

## Validation

- [x] All YAML frontmatter validates correctly
- [x] No broken internal links
- [x] Examples use consistent formatting
- [x] Built-in agents documented accurately
