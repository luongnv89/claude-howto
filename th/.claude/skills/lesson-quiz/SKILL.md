<!-- i18n-source: .claude/skills/lesson-quiz/SKILL.md -->
<!-- i18n-date: 2026-07-16 -->
---
name: lesson-quiz
version: 1.0.0
description: Interactive lesson-level quiz for Claude Code tutorials. Tests understanding of a specific lesson (01-10) with 8-10 questions mixing conceptual and practical knowledge. Use before a lesson to pre-test, during to check progress, or after to verify mastery. Use when asked to "quiz me on hooks", "test my knowledge of lesson 3", "lesson quiz", "practice quiz for MCP", or "do I understand skills".
---

# Lesson Quiz

แบบทดสอบเชิงโต้ตอบที่ทดสอบความเข้าใจของบทเรียน Claude Code เฉพาะบท ด้วยคำถาม 8-10 ข้อ ให้ feedback รายข้อ และระบุจุดที่ควรทบทวน

## คำแนะนำ

### ขั้นตอน 1: กำหนดบทเรียน

หากผู้ใช้ระบุบทเรียนเป็นอาร์กิวเมนต์ (เช่น `/lesson-quiz hooks` หรือ `/lesson-quiz 03`) ให้จับคู่กับ directory ของบทเรียน:

**การจับคู่บทเรียน:**
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

หากไม่มีอาร์กิวเมนต์ ให้แสดง prompt การเลือกโดยใช้ AskUserQuestion:

**คำถามที่ 1** (header: "Lesson"):
"Which lesson do you want to quiz on?"
ตัวเลือก:
1. "Slash Commands (01)" — Custom commands, skills, frontmatter, arguments
2. "Memory (02)" — CLAUDE.md, memory hierarchy, rules, auto memory
3. "Skills (03)" — Progressive disclosure, auto-invocation, SKILL.md
4. "Subagents (04)" — Task delegation, agent config, isolation

**คำถามที่ 2** (header: "Lesson"):
"Which lesson do you want to quiz on? (continued)"
ตัวเลือก:
1. "MCP (05)" — External integration, transport, servers, tool search
2. "Hooks (06)" — Event automation, PreToolUse, exit codes, JSON I/O
3. "Plugins (07)" — Bundled solutions, marketplace, plugin.json
4. "More lessons..." — Checkpoints, Advanced Features, CLI

หากเลือก "More lessons..." ให้แสดง:

**คำถามที่ 3** (header: "Lesson"):
"Select your lesson:"
ตัวเลือก:
1. "Checkpoints (08)" — Rewind, restore, safe experimentation
2. "Advanced Features (09)" — Planning, permissions, print mode, thinking
3. "CLI Reference (10)" — Flags, output formats, scripting, piping

### ขั้นตอน 2: อ่านเนื้อหาบทเรียน

อ่านไฟล์ README.md ของบทเรียนเพื่อรีเฟรช context:
- อ่านไฟล์: `<lesson-directory>/README.md`

จากนั้นใช้คลังคำถามจาก `references/question-bank.md` สำหรับบทเรียนนั้น คลังคำถามมีคำถามที่เขียนไว้ล่วงหน้า 10 ข้อต่อบทเรียนพร้อมคำตอบที่ถูกต้องและคำอธิบาย

### ขั้นตอน 3: นำเสนอแบบทดสอบ

ถามผู้ใช้เกี่ยวกับบริบทช่วงเวลาของแบบทดสอบ:

ใช้ AskUserQuestion (header: "Timing"):
"When are you taking this quiz relative to the lesson?"
ตัวเลือก:
1. "Before (pre-test)" — I haven't read the lesson yet, testing my prior knowledge
2. "During (progress check)" — I'm partway through the lesson
3. "After (mastery check)" — I've completed the lesson and want to verify understanding

บริบทนี้มีผลต่อวิธีการนำเสนอผลลัพธ์ (ดูขั้นตอน 5)

### ขั้นตอน 4: นำเสนอคำถามเป็นรอบ

นำเสนอคำถาม 10 ข้อจากคลังคำถามเป็นรอบ รอบละ 2 ข้อ (รวม 5 รอบ) แต่ละคำถามใช้ AskUserQuestion พร้อมข้อความคำถามและตัวเลือกคำตอบ 3-4 ตัว

**สำคัญ**: ใช้ AskUserQuestion โดยมีตัวเลือกสูงสุด 4 ตัวต่อคำถาม และ 2 คำถามต่อรอบ

สำหรับแต่ละรอบ ให้นำเสนอ 2 คำถาม หลังจากผู้ใช้ตอบแต่ละรอบ ให้แสดง feedback รายข้อทันที: แต่ละคำตอบถูกหรือผิด และหากผิด ให้แสดงคำตอบที่ถูกต้องพร้อมคำอธิบายสั้นๆ จากนั้นดำเนินการต่อไปยังรอบถัดไป หลังจากครบทั้ง 5 รอบ ให้ดำเนินการคิดคะแนนสุดท้าย

**รูปแบบคำถามต่อรอบ:**

แต่ละคำถามจากคลังคำถามมี:
- `question`: ข้อความคำถาม
- `options`: ตัวเลือกคำตอบ 3-4 ตัว (ถูก 1 ตัว ระบุไว้ในคลัง)
- `correct`: ป้ายกำกับคำตอบที่ถูกต้อง
- `explanation`: เหตุผลว่าทำไมคำตอบจึงถูก
- `category`: "conceptual" หรือ "practical"

**สำคัญมาก — สลับลำดับตัวเลือกคำตอบ**: สำหรับแต่ละคำถาม คุณ**ต้อง**สุ่มลำดับของตัวเลือกคำตอบก่อนนำเสนอผ่าน AskUserQuestion อย่านำเสนอตามลำดับที่ปรากฏในคลังคำถาม (A, B, C, D) และอย่าวางคำตอบที่ถูกต้องไว้เป็นตัวแรก ใช้การเรียงสับเปลี่ยนแบบสุ่มที่ต่างกันสำหรับแต่ละคำถาม ติดตามว่าตำแหน่งที่สลับแล้วตำแหน่งใดมีคำตอบที่ถูกต้องเพื่อให้คิดคะแนนได้อย่างแม่นยำ

ตัวอย่าง: หากคลังคำถามระบุตัวเลือก A (ถูก), B, C, D — คุณอาจนำเสนอเป็น: C, A, D, B คำตอบที่ถูกต้องจะอยู่ที่ตำแหน่ง 2

นำเสนอแต่ละคำถามโดยใช้ AskUserQuestion บันทึกคำตอบของผู้ใช้ในแต่ละข้อ

### ขั้นตอน 5: คิดคะแนนและนำเสนอผลลัพธ์

หลังจากครบทุกรอบ ให้คำนวณคะแนนและนำเสนอผลลัพธ์

**การคิดคะแนน:**
- คำตอบที่ถูกแต่ละข้อ = 1 คะแนน
- คะแนนเต็มที่เป็นไปได้ = 10 คะแนน

**เกณฑ์เกรด:**
- 9-10: Mastered — ความเข้าใจยอดเยี่ยม
- 7-8: Proficient — เข้าใจดี มีช่องว่างเล็กน้อย
- 5-6: Developing — เข้าใจพื้นฐาน ต้องทบทวน
- 3-4: Beginning — มีช่องว่างมาก แนะนำให้ทบทวน
- 0-2: Not yet — เริ่มต้นใหม่จากต้นบทเรียนนี้

**รูปแบบผลลัพธ์:**

```markdown
## Lesson Quiz Results: [Lesson Name]

**Score: N/10** — [Grade label]
**Quiz timing**: [Before / During / After] the lesson
**Question breakdown**: N conceptual correct, N practical correct

### Per-Question Results

| # | Category | Question (short) | Your Answer | Result |
|---|----------|-----------------|-------------|--------|
| 1 | Conceptual | [abbreviated question] | [their answer] | [Correct / Incorrect] |
| 2 | Practical | ... | ... | ... |
| ... | ... | ... | ... | ... |

### Incorrect Answers — Review These

[For each incorrect answer, show:]

**Q[N]: [Full question text]**
- Your answer: [what they chose]
- Correct answer: [correct option]
- Explanation: [why it's correct]
- Review: [specific section of the lesson README to re-read]

### [Timing-specific message]

[If pre-test]:
**Pre-test score: N/10.** This gives you a baseline! Focus your study on the topics you missed. After completing the lesson, retake the quiz to measure your improvement.

[If during]:
**Progress check: N/10.** [If 7+: Great progress — keep going! If 4-6: Review the incorrect topics before continuing. If <4: Consider re-reading from the beginning.]

[If after]:
**Mastery check: N/10.** [If 9-10: You've mastered this lesson! Move on to the next. If 7-8: Almost there — review the missed topics and retake. If <7: Spend more time with the lesson, especially the sections marked above.]

### Recommended Next Steps

[Based on score and timing:]
- [If mastered]: Proceed to the next lesson in the roadmap: [next lesson link]
- [If proficient]: Review these specific sections, then retake: [list sections]
- [If developing or below]: Re-read the full lesson: [lesson link]. Focus on: [list weak categories]
- [Offer]: "Would you like to retake this quiz, try a different lesson, or get help with a specific topic?"
```

### ขั้นตอน 6: เสนอการดำเนินการต่อ

หลังจากนำเสนอผลลัพธ์ ให้ใช้ AskUserQuestion:

"What would you like to do next?"
ตัวเลือก:
1. "Retake this quiz" — Try the same lesson quiz again
2. "Quiz another lesson" — Switch to a different lesson
3. "Explain a topic I missed" — Get a detailed explanation of an incorrect answer
4. "Done" — End the quiz session

หากเลือก **Retake**: กลับไปที่ขั้นตอน 4 (ข้ามคำถามเรื่องช่วงเวลา ใช้ช่วงเวลาเดิม)
หากเลือก **Quiz another lesson**: กลับไปที่ขั้นตอน 1
หากเลือก **Explain a topic**: ถามว่าคำถามข้อใด จากนั้นอ่านหัวข้อที่เกี่ยวข้องจาก README.md ของบทเรียนและอธิบายพร้อมตัวอย่าง

## การจัดการข้อผิดพลาด

### อาร์กิวเมนต์บทเรียนไม่ถูกต้อง
หากอาร์กิวเมนต์ไม่ตรงกับบทเรียนใด ให้แสดงรายการบทเรียนที่ถูกต้องและขอให้ผู้ใช้เลือกหนึ่งบท

### ผู้ใช้ต้องการออกกลางแบบทดสอบ
หากผู้ใช้แสดงเจตนาว่าต้องการหยุดระหว่างรอบใดๆ ให้นำเสนอผลลัพธ์บางส่วนสำหรับคำถามที่ตอบไปแล้ว

### ไม่พบ README ของบทเรียน
หากไฟล์ README.md ไม่มีอยู่ใน path ที่คาดหวัง ให้แจ้งผู้ใช้และแนะนำให้ตรวจสอบโครงสร้างของ repository

## การตรวจสอบความถูกต้อง

### ชุดทดสอบการ trigger

**ควร trigger:**
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

**ไม่ควร trigger:**
- "assess my overall level" (use /self-assessment)
- "explain hooks to me"
- "create a hook"
- "what is MCP"
- "review my code"
