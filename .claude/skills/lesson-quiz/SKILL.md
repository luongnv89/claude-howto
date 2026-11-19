---
name: lesson-quiz
description: "Test a learner on a single Claude Code tutorial lesson (01-10) with 10 questions, scoring answers and flagging weak spots. Runs in the learner's language when the tutorial has a translation. Use before, during, or after a lesson. Don't use for whole-tutorial assessment or explaining a topic instead of testing it."
effort: high
metadata:
  version: 1.7.0
  author: Luong NGUYEN
---

# Lesson Quiz

Interactive quiz that tests understanding of a specific Claude Code lesson with 10 questions, provides per-question feedback, and identifies areas to review.

## Prerequisites

This skill requires:

- The tutorial repo checked out, so the lesson directories `01-slash-commands/` … `10-cli/` and each `README.md` are readable.
- `references/question-bank.md` present in this skill (the source of all questions).

Before starting, confirm the target lesson's `README.md` exists. If it is missing, do not fabricate questions — warn the user and ask them to check the repository structure (see Error Handling).

**Guardrails:**

- **Never invent questions or answers.** Ask only questions drawn from `references/question-bank.md` for the selected lesson; if the bank lacks entries for a lesson, say so rather than making them up.
- **Score accurately.** Track which shuffled position holds the correct answer for every question and validate each response against it — never guess a score.
- **Confirm timing before scoring.** The pre/during/after choice changes how results are framed; do not skip it.

## Language

This skill and its question bank are written in English, but the quiz runs in the learner's language. Before Step 1, resolve the **quiz language**. Take the first of these that applies:

1. A language named in the request: an extra argument (`/lesson-quiz hooks ko`, `/lesson-quiz 06 korean`, `/lesson-quiz ko`) or a sentence ("한국어로 퀴즈 내줘", "quiz me in Japanese").
2. A standing instruction, already in the session's context, to respond in a particular language (for example from the learner's `CLAUDE.local.md`).
3. The language the learner has been writing in.
4. English.

Keep that language for the whole run. If the learner asks to switch partway through, switch and carry on from the same question.

The tutorial has a translated lesson tree for each of these languages:

| Language | Code | Lesson tree |
|----------|------|-------------|
| Vietnamese | `vi` | `vi/` |
| Chinese | `zh` | `zh/` |
| Ukrainian | `uk` | `uk/` |
| Japanese | `ja` | `ja/` |
| Korean | `ko` | `ko/` |
| Persian | `fa` | `fa/` |

When the quiz language is not English:

- **Read the translated lesson.** In Step 2, read `<tree>/<lesson-directory>/README.md` (Korean, Hooks: `ko/06-hooks/README.md`). If that file is missing, or the language has no tree, read the English README and tell the learner once that the lesson is not translated.
- **Translate the bank, don't rewrite it.** Present each question, its options, and its explanation in the quiz language. Keep the meaning, the number of options, and which option is correct. A translated question is still a bank question, so the guardrails above hold unchanged: score against the bank's `Correct` label.
- **Keep code and on-screen text verbatim.** Commands, flags, file names, paths, setting keys, event names, model names, menu items and other on-screen labels (including the ones offered as wrong answers), and anything in backticks stay exactly as the bank has them. A translation in parentheses after a menu item is fine. Two options must never end up reading the same.
- **Use the translation's terms.** If `<tree>/TRANSLATION_NOTES.md` exists, read its glossary and use those terms, so the quiz words things the way the lesson does.
- **Localize everything the learner sees.** AskUserQuestion questions, headers, option labels and descriptions, per-round feedback, the results report, and the follow-up prompt are all in the quiz language.
- **Point review at the translated lesson.** The bank's `Review` field names an English section. Cite the matching heading in the translated README you read, and link that file. A translation can lag the English lesson: if it does not cover what the explanation says, say so and point to the English section as well.

## Instructions

### Step 1: Determine the Lesson

If the user provided a lesson as an argument (e.g., `/lesson-quiz hooks` or `/lesson-quiz 03`), map it to the lesson directory:

**Lesson mapping:**
- `01`, `slash-commands`, `commands` → 01-slash-commands
- `02`, `memory` → 02-memory
- `03`, `skills` → 03-skills
- `04`, `subagents`, `agents` → 04-subagents
- `05`, `mcp` → 05-mcp
- `06`, `hooks` → 06-hooks
- `07`, `plugins` → 07-plugins
- `08`, `checkpoints`, `checkpoint` → 08-checkpoints
- `09`, `advanced`, `advanced-features` → 09-advanced-features
- `10`, `cli` → 10-cli

A language code or name in the arguments (`ko`, `korean`, `한국어`) sets the quiz language (see Language); it is not part of the lesson name. A lesson named in another language maps by meaning (`훅` → 06-hooks).

If no lesson argument was provided, present a selection prompt using AskUserQuestion:

**Question 1** (header: "Lesson"):
"Which lesson do you want to quiz on?"
Options:
1. "Slash Commands (01)" — Custom commands, skills, frontmatter, arguments
2. "Memory (02)" — CLAUDE.md, memory hierarchy, rules, auto memory
3. "Skills (03)" — Progressive disclosure, auto-invocation, SKILL.md
4. "Subagents (04)" — Task delegation, agent config, isolation

**Question 2** (header: "Lesson"):
"Which lesson do you want to quiz on? (continued)"
Options:
1. "MCP (05)" — External integration, transport, servers, tool search
2. "Hooks (06)" — Event automation, PreToolUse, exit codes, JSON I/O
3. "Plugins (07)" — Bundled solutions, marketplace, plugin.json
4. "More lessons..." — Checkpoints, Advanced Features, CLI

If "More lessons..." is selected, present:

**Question 3** (header: "Lesson"):
"Select your lesson:"
Options:
1. "Checkpoints (08)" — Rewind, restore, safe experimentation
2. "Advanced Features (09)" — Planning, permissions, print mode, thinking
3. "CLI Reference (10)" — Flags, output formats, scripting, piping

### Step 2: Read the Lesson Content

Read the lesson README.md file to refresh context:
- Read file: `<lesson-directory>/README.md` (for a non-English quiz, the translated README — see Language)

Then use the question bank from `references/question-bank.md` for that lesson (10 pre-written questions with answers and explanations). To stay within the context budget, read only the one selected lesson's README — not all ten.

### Step 3: Present the Quiz

Ask the user about quiz timing context:

Use AskUserQuestion (header: "Timing"):
"When are you taking this quiz relative to the lesson?"
Options:
1. "Before (pre-test)" — I haven't read the lesson yet, testing my prior knowledge
2. "During (progress check)" — I'm partway through the lesson
3. "After (mastery check)" — I've completed the lesson and want to verify understanding

This context affects how the results are framed (see Step 5).

### Step 4: Present Questions in Rounds

Present 10 questions from the question bank in rounds of 2 questions each (5 rounds total). Each question uses AskUserQuestion with the question text and 3-4 answer options.

**IMPORTANT**: Use AskUserQuestion with max 4 options per question, 2 questions per round.

For each round, present 2 questions. After the user answers each round, immediately show per-question feedback: whether each answer was correct or incorrect, and if incorrect, show the correct answer and a brief explanation. Then proceed to the next round. After all 5 rounds, proceed to final scoring.

**Question format per round:**

Each question from the question bank has:
- `question`: The question text
- `options`: 3-4 answer choices (one correct, labeled in the bank)
- `correct`: The correct answer label
- `explanation`: Why the answer is correct
- `category`: "conceptual" or "practical"

**CRITICAL — Shuffle answer options**: For each question, you MUST randomize the order of the answer options before presenting them via AskUserQuestion. Do NOT present them in the order they appear in the question bank (A, B, C, D), and do NOT place the correct answer first. Use a different random permutation for each question. Track which shuffled position contains the correct answer so you can score accurately.

Example: If the question bank lists options A (correct), B, C, D — you might present them as: C, A, D, B. The correct answer is now in position 2.

Present each question using AskUserQuestion. Record the user's answer for each.

### Step 5: Score and Present Results

After all rounds, calculate the score and present results.

**Scoring:**
- Each correct answer = 1 point
- Total possible = 10 points

**Grade scale:**
- 9-10: Mastered — Excellent understanding
- 7-8: Proficient — Good grasp, minor gaps
- 5-6: Developing — Fundamentals understood, needs review
- 3-4: Beginning — Significant gaps, review recommended
- 0-2: Not yet — Start from the beginning of this lesson

**Output format:** Follow the report template in `references/results-template.md`. It defines the score line, the per-question results table, the "Incorrect Answers — Review These" block, the timing-specific message (pre-test / during / after), and the "Recommended Next Steps" section. Fill its bracketed placeholders with this run's data.

### Step 6: Offer Follow-up

After presenting results, use AskUserQuestion:

"What would you like to do next?"
Options:
1. "Retake this quiz" — Try the same lesson quiz again
2. "Quiz another lesson" — Switch to a different lesson
3. "Explain a topic I missed" — Get a detailed explanation of an incorrect answer
4. "Done" — End the quiz session

If **Retake**: Go back to Step 4 (skip timing question, use same timing).
If **Quiz another lesson**: Go back to Step 1.
If **Explain a topic**: Ask which question number, then read the relevant section from the lesson README.md and explain it with examples.

## Acceptance Criteria

A completed quiz run must satisfy all of these — verify each before presenting final results:

- Exactly one lesson (01-10) was resolved before any question was asked.
- The timing context (before / during / after) was captured via AskUserQuestion.
- 10 questions from `references/question-bank.md` for that lesson were presented, in 5 rounds of 2, with answer options shuffled per question.
- Every answer was scored against the tracked correct-position, producing an integer score in the range 0-10.
- For a non-English quiz: the translated lesson README was read (or the learner was told it is missing), every question and option shown was a translation of a bank entry, and everything the learner saw was in the quiz language.
- **Expected output**: a `## Lesson Quiz Results` report (headings translated for a non-English quiz) containing the score line (`Score: N/10` with a grade label), the per-question results table, an "Incorrect Answers — Review These" block for each miss, and a timing-specific message.
- The follow-up prompt (retake / another lesson / explain / done) was offered.

Example: for a 7/10 "after" run on Hooks, the report asserts `Score: 7/10 — Proficient`, lists all 10 rows in the results table, and expands the 3 incorrect questions with correct answer, explanation, and a review pointer.

## Edge Cases & Error Handling

### Invalid lesson argument
If the argument doesn't match any lesson, show the valid lesson list and ask the user to pick one.

### User wants to quit mid-quiz
If the user indicates they want to stop during any round, present partial results for the questions answered so far (score out of the number attempted, not out of 10).

### Lesson README not found
If the README.md file doesn't exist at the expected path, inform the user and suggest checking the repository structure. Do not proceed with fabricated content.

### Question bank missing entries for a lesson
If `references/question-bank.md` has no questions for the resolved lesson, tell the user and stop — never invent questions to fill the gap.

## Validation

### Triggering test suite

**Should trigger:**
- "quiz me on hooks"
- "lesson quiz"
- "test my knowledge of lesson 3"
- "practice quiz for MCP"
- "do I understand skills"
- "quiz me on slash commands"
- "lesson-quiz 06"
- "test me on checkpoints"
- "how well do I know the CLI"
- "quiz me before I start the memory lesson"
- "훅 퀴즈 내줘" (Korean: "quiz me on hooks")
- "/lesson-quiz hooks ko"

**Should NOT trigger:**
- "assess my overall level" (use /self-assessment)
- "explain hooks to me"
- "create a hook"
- "what is MCP"
- "review my code"
