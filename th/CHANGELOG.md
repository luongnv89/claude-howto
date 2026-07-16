<!-- i18n-source: CHANGELOG.md -->
<!-- i18n-date: 2026-07-15 -->

# บันทึกการเปลี่ยนแปลง (Changelog)

## [v2.1.131] — 2026-05-06

### ซิงค์กับ Claude Code v2.1.131

ปรับปรุงเนื้อหาบทเรียนจาก Claude Code v2.1.126 → v2.1.131 (release วันที่ 6 พฤษภาคม 2026)
Anthropic ออก v2.1.128, v2.1.129, และ v2.1.131 นับตั้งแต่การ sync ครั้งล่าสุด โดย
v2.1.127 และ v2.1.130 ถูกข้ามและไม่เคย release สู่สาธารณะ

### เพิ่มเติม (เอกสารภาษาอังกฤษ)

- flag `--plugin-url <url>` (v2.1.129) — ดึงไฟล์ archive `.zip` ของ plugin จาก
  URL สำหรับเซสชันปัจจุบัน ระบุซ้ำได้ บันทึกใน
  `07-plugins/README.md`
- ตัวแปรสภาพแวดล้อม `CLAUDE_CODE_FORCE_SYNC_OUTPUT` (v2.1.129) — บังคับให้ output
  เป็นแบบ synchronous สำหรับ terminals ที่การตรวจจับอัตโนมัติทำงานพลาด (เช่น Emacs `eat`)
  บันทึกใน `10-cli/README.md` และ `09-advanced-features/README.md`
- ตัวแปรสภาพแวดล้อม `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE` (v2.1.129) — เปิดใช้งาน
  การอัปเกรดในพื้นหลังสำหรับการติดตั้งผ่าน Homebrew/WinGet (ซึ่งปกติไม่
  อัปเดตอัตโนมัติ) บันทึกใน `10-cli/README.md` และ
  `09-advanced-features/README.md`
- ตัวแปรสภาพแวดล้อม `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` (v2.1.129) — จำเป็น
  ต้องตั้งค่าเพื่อ opt in เข้าใช้การค้นพบผ่าน gateway `/v1/models` (ดูหัวข้อเปลี่ยนแปลง) บันทึกใน
  `10-cli/README.md`
- การตั้งค่า `disableRemoteControl` (v2.1.128) — ผู้ดูแลระบบสามารถบล็อก
  `claude remote-control` และ `/remote-control` ผ่านขอบเขต managed/policy
  บันทึกใน `09-advanced-features/README.md`
- `--plugin-dir` รองรับไฟล์ archive `.zip` (v2.1.128) — นอกเหนือจาก
  directory inputs บันทึกใน `07-plugins/README.md`
- `skillOverrides` รองรับ `"name-only"` และ `"user-invocable-only"`
  (v2.1.129) — นอกเหนือจากค่า `"on"`/`"off"` เดิม บันทึกใน
  `03-skills/README.md`

### เปลี่ยนแปลง

- **การเปลี่ยนแปลงพฤติกรรม**: การค้นพบผ่าน gateway `/v1/models` เปลี่ยนเป็นแบบ **opt-in**
  (v2.1.129) ก่อนหน้านี้ (v2.1.126) การตั้งค่า `ANTHROPIC_BASE_URL` จะดึงข้อมูล
  `/model` จาก endpoint `/v1/models` ของ gateway โดยอัตโนมัติ ตั้งแต่ v2.1.129
  ผู้ใช้ต้องตั้งค่า `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` เพิ่มเติม
  หากไม่มีตัวแปรสภาพแวดล้อมนี้ `/model` จะย้อนกลับไปใช้รายการ static ที่ built-in ไว้
  บันทึกใน `10-cli/README.md`
- `/mcp` แสดงจำนวนเครื่องมือต่อ server และแสดงเครื่องหมายกำกับด้วยภาพสำหรับ server ที่รายงานว่ามี 0
  เครื่องมือ (v2.1.128) บันทึกใน `05-mcp/README.md`
- `/color` เปล่า (ไม่มี args) เลือกสีเซสชันแบบสุ่ม (v2.1.128) ส่วน `/color <name|hex>`
  แบบระบุชัดเจนยังคงตั้งค่าสีที่เจาะจง บันทึกใน
  `01-slash-commands/README.md`
- flag `--channels` ใช้งานได้กับการยืนยันตัวตนแบบ API-key (console) แล้ว
  (v2.1.128) release ก่อนหน้ากำหนดให้ต้องใช้ Pro/Max OAuth บันทึกใน
  `09-advanced-features/README.md`
- Ctrl+R history picker ตั้งค่าเริ่มต้นเป็น **prompts ทั้งหมดในทุกโปรเจกต์**
  (v2.1.129) กด Ctrl+S ภายใน picker เพื่อจำกัดขอบเขตเป็นโปรเจกต์
  ปัจจุบัน บันทึกใน `09-advanced-features/README.md`
- `/context` ไม่ทิ้ง ASCII visualization ลงในการสนทนาอีกต่อไป
  (v2.1.129) visualization จะแสดงเฉพาะใน UI เท่านั้น ไม่มีต้นทุน ~1.6k token ต่อ
  การเรียกใช้อีกต่อไป บันทึกใน `09-advanced-features/README.md`
- ภาพที่มีขนาดเกินใน drag-and-drop จะถูกลดขนาดอัตโนมัติ (v2.1.128) — เวอร์ชัน
  ก่อนหน้าปฏิเสธภาพทันที

### แก้ไข

- การเปิดใช้งาน VS Code extension บน Windows (v2.1.131)
- การยืนยันตัวตนของ Mantle endpoint (v2.1.131)
- TTL 1 ชั่วโมงสำหรับ prompt-cache ไม่ถูกตัดเหลือ 5 นาทีอีกต่อไป (v2.1.129)
- Crash เมื่อ stdin payloads มีขนาดใหญ่กว่า 10 MB (v2.1.128)

### หมายเหตุสำหรับผู้ดูแลการแปล

โครงสร้างการแปล `vi/`, `zh/`, `uk/`, และ `ja/` ดูแลโดยชุมชนและ
อาจตามหลังแหล่งที่มาภาษาอังกฤษ ผู้ร่วมพัฒนาที่ sync การแปลควร diff
กับไฟล์ภาษาอังกฤษที่อัปเดตใน release นี้

## [v2.1.126] — 2026-05-02

### ซิงค์กับ Claude Code v2.1.126

ปรับปรุงเนื้อหาบทเรียนจาก Claude Code v2.1.119 → v2.1.126 (release วันที่ 1 พฤษภาคม 2026)
v2.1.120 ถูก rollback ในวันแรกที่ release (2026-04-24) แต่ re-release
สำเร็จในวันที่ 2026-04-28 พร้อมแก้ไข regression ที่รายงานไว้ตอนแรก
v2.1.124 และ v2.1.125 ถูก Anthropic ข้ามและไม่เคย release

### เพิ่มเติม (เอกสารภาษาอังกฤษ)

- subcommand `claude project purge [path]` (v2.1.126) — ลบ state ทั้งหมดของ Claude Code
  สำหรับโปรเจกต์ (transcripts, tasks, debug logs, ประวัติการแก้ไขไฟล์,
  ประวัติ prompt, รายการใน `~/.claude.json`) รองรับ `--dry-run`, `-y/--yes`,
  `-i/--interactive`, `--all` บันทึกใน `10-cli/README.md`
- subcommand `claude plugin prune` (v2.1.121) — ลบ plugin dependencies
  ที่ติดตั้งอัตโนมัติแล้วกลายเป็น orphaned; `plugin uninstall --prune` จะทำแบบ cascade บันทึกใน
  `07-plugins/README.md`
- subcommand `claude ultrareview [target]` (v2.1.120) — รัน `/ultrareview`
  แบบ non-interactive จาก CI/scripts พิมพ์ผลการตรวจสอบไปยัง stdout ออกด้วย exit code 0/1 เมื่อ
  สำเร็จ/ล้มเหลว; รองรับ `--json` และ `--timeout <minutes>` บันทึกใน
  `10-cli/README.md`
- placeholder `${CLAUDE_EFFORT}` ใช้ได้ภายใน skill content (v2.1.120) —
  แทนที่ด้วยระดับ effort ปัจจุบัน บันทึกใน `03-skills/README.md`
- ตัวเลือกการกำหนดค่า MCP server `alwaysLoad` (v2.1.121) — เมื่อเป็น `true` เครื่องมือ
  ทั้งหมดจาก server นั้นจะข้ามการเลื่อน tool-search บันทึกใน `05-mcp/README.md`
- `PostToolUse.hookSpecificOutput.updatedToolOutput` ใช้งานได้กับเครื่องมือทั้งหมดแล้ว
  (v2.1.121) ก่อนหน้านี้ใช้ได้เฉพาะ MCP บันทึกใน `06-hooks/README.md`
- ตัวแปรสภาพแวดล้อม `ANTHROPIC_BEDROCK_SERVICE_TIER` (v2.1.122) — เลือก
  Bedrock service tier (`default`, `flex`, `priority`) บันทึกใน
  ตาราง env-var ของ `10-cli/README.md`
- การครอบคลุม extended-path ของ `--dangerously-skip-permissions` (v2.1.121, v2.1.126)
  — ตอนนี้ข้าม prompt สำหรับการเขียนไปยัง `.claude/skills/`, `.claude/agents/`,
  `.claude/commands/`, `.claude/`, `.git/`, `.vscode/`, ไฟล์ config ของ shell
  คำสั่งลบที่ร้ายแรง (`rm -rf /` เป็นต้น) ยังคง prompt อยู่ บันทึกใน
  ส่วน permission-modes ของ `09-advanced-features/README.md`
- OAuth code paste fallback (v2.1.126) — `claude auth login` รับ OAuth
  code ที่วางลงใน terminal เมื่อ browser callback เข้าถึง
  localhost ไม่ได้ (WSL2, SSH, containers) บันทึกใน `10-cli/README.md`
- เมนู `/skills` แบบพิมพ์เพื่อกรอง (v2.1.121) บันทึกใน `03-skills/README.md`
- ตัวแปรสภาพแวดล้อม `AI_AGENT` (v2.1.120) — ตั้งค่าบน subprocesses เพื่อให้ `gh`
  สามารถระบุแหล่งที่มาของ traffic ว่ามาจาก Claude Code ได้ บันทึกใน ตาราง env-var
  ของ `10-cli/README.md`

### เปลี่ยนแปลง

- `--from-pr` (v2.1.119) และ `/resume` PR-URL search (v2.1.122) ตอนนี้ทั้งคู่
  รองรับ URLs ของ GitHub, GitHub Enterprise, GitLab, และ Bitbucket
- Windows: ไม่จำเป็นต้องใช้ Git for Windows / Git Bash อีกต่อไป (v2.1.120) — Claude
  Code ใช้ PowerShell เป็นเครื่องมือ shell เมื่อไม่มี Git Bash ตั้งแต่ v2.1.126
  PowerShell เป็น shell หลักเมื่อเปิดใช้งานเครื่องมือ PowerShell การตรวจจับ
  ขยายไปยัง PowerShell 7 ที่ติดตั้งผ่าน Microsoft Store, MSI ที่ไม่มี PATH, หรือ
  `.NET global tool` บันทึกใน platform notes ของ
  `09-advanced-features/README.md`
- `/model` picker แสดงรายการ models จาก endpoint `/v1/models` ของ gateway ของคุณ
  เมื่อ `ANTHROPIC_BASE_URL` ชี้ไปยัง gateway ที่เข้ากันได้กับ Anthropic
  (v2.1.126) บันทึกใน `10-cli/README.md`
- `--dangerously-skip-permissions` ไม่ prompt สำหรับการเขียนไปยัง allowlist ที่
  กว้างขึ้นมากอีกต่อไป (ดูหัวข้อเพิ่มเติม) การลบที่ร้ายแรงยังคง prompt อยู่
- Image paste auto-downscale (v2.1.126) — ภาพที่ใหญ่กว่า 2000px จะถูก
  ลดขนาดเมื่อวาง; ภาพที่มีขนาดเกินในประวัติจะถูกลบอัตโนมัติและ
  request จะถูกลองใหม่ (เกี่ยวข้องกับบทเรียนเฉพาะในฐานะหมายเหตุด้านความปลอดภัย/UX)

### ความปลอดภัย

- แก้ไข `allowManagedDomainsOnly` / `allowManagedReadPathsOnly` ที่ถูกละเว้น
  เมื่อแหล่ง managed-settings ที่มีลำดับความสำคัญสูงกว่าไม่มีบล็อก `sandbox`
  (v2.1.126)

### หมายเหตุสำหรับผู้ดูแลการแปล

โครงสร้างการแปล `vi/`, `zh/`, `uk/`, และ `ja/` ดูแลโดยชุมชนและ
อาจตามหลังแหล่งที่มาภาษาอังกฤษ ผู้ร่วมพัฒนาที่ sync การแปลควร diff
กับไฟล์ภาษาอังกฤษที่อัปเดตใน release นี้

## [v2.4.0] — 2026-04-27

### ซิงค์กับ Claude Code v2.1.119

ปรับปรุงเนื้อหาบทเรียนจาก Claude Code v2.1.112 → v2.1.119 (release วันที่ 23 เมษายน 2026)
v2.1.120 เผยแพร่วันที่ 24 เมษายน ถูก rollback ในวันเดียวกันช่วงสั้นๆ เนื่องจาก regression
และ re-release ในวันที่ 28 เมษายนพร้อมแก้ไข — ตอนนี้เป็นส่วนหนึ่งของสาย release ปกติแล้ว
v2.1.126 (1 พฤษภาคม 2026) ที่ตามมาเป็นเป้าหมาย stable ถัดไปและครอบคลุมในรายการ
v2.1.126 ด้านบน

### เพิ่มเติม (เอกสารภาษาอังกฤษ)

- หมายเหตุเกี่ยวกับการแพ็กเกจ native binary (v2.1.113) — ตอนนี้ CLI ส่งมอบ native binaries แยกตามแพลตฟอร์ม
- เชิงอรรถการแทนที่ Glob/Grep ด้วย `bfs`/`ugrep` บน native macOS/Linux builds (v2.1.117)
- ประเภท hook `mcp_tool` พร้อมตัวอย่าง (v2.1.118)
- ฟิลด์ `duration_ms` บน inputs ของ PostToolUse / PostToolUseFailure (v2.1.119)
- การตั้งค่า `prUrlTemplate` (v2.1.119) และรายการ provider ที่ขยายสำหรับ `--from-pr` (GitLab, Bitbucket)
- ขอบเขตที่ขยายของ `cleanupPeriodDays` (checkpoints + tasks + shell-snapshots + backups, v2.1.117)
- การบังคับใช้ plugin marketplace ในทุก lifecycle event (v2.1.117) และ regex `hostPattern`/`pathPattern` (v2.1.119)
- ตัวแปรสภาพแวดล้อมใหม่: `DISABLE_UPDATES`, `CLAUDE_CODE_HIDE_CWD`, `CLAUDE_CODE_FORK_SUBAGENT`, `OTEL_LOG_TOOL_DETAILS`, `ENABLE_TOOL_SEARCH` แบบ opt-in สำหรับ Vertex
- slash commands ใหม่: `/btw`, `/theme` พร้อม custom themes
- คำสั่งมาตรฐาน `/usage` (รวม `/cost` + `/stats`, v2.1.118)
- Forked subagents (`CLAUDE_CODE_FORK_SUBAGENT=1`, v2.1.117)
- token `"$defaults"` สำหรับ Auto mode (v2.1.118)
- managed policy `wslInheritsWindowsSettings` (v2.1.118)
- Vim visual / visual-line modes (v2.1.118)
- subcommand `claude install [version]` และ `claude plugin tag`

### เปลี่ยนแปลง

- ย้าย host เอกสาร: `docs.anthropic.com/en/docs/claude-code/*` → `code.claude.com/docs/en/*`
- ระดับ effort ของ Opus 4.7: `xhigh` เป็นค่าเริ่มต้นของ Claude Code แล้วตั้งแต่การเปิดตัว 2026-04-16; ยืนยัน native context window ของ Opus 4.7 ที่ 1M แล้ว (v2.1.117 แก้ไข `/context` ที่นับผิดเป็น 200K)
- ค่าเริ่มต้นของ effort ยกระดับจาก `medium` เป็น `high` สำหรับผู้สมัครสมาชิก Pro/Max บน Opus 4.6 / Sonnet 4.6 (v2.1.117)
- อัปเดต Source URL ของ `STYLE_GUIDE.md` จากบทความ Claude Apps เป็น `code.claude.com/docs/en/changelog`

### เลิกใช้งาน (ติดตามไว้ ยังไม่ลบ)

- การตั้งค่า `includeCoAuthoredBy` → ใช้ `attribution.commit` / `attribution.pr`
- การตั้งค่า `voiceEnabled` → ใช้ `voice.enabled`

### หมายเหตุสำหรับผู้ดูแลการแปล

โครงสร้างการแปล `vi/`, `zh/`, และ `uk/` ดูแลโดยชุมชนและอาจตามหลังแหล่งที่มาภาษาอังกฤษ ผู้ร่วมพัฒนาที่ sync การแปลควร diff กับไฟล์ภาษาอังกฤษที่อัปเดตใน release นี้

## v2.1.112 — 2026-04-16

### ไฮไลต์

- ซิงค์บทเรียนภาษาอังกฤษทั้งหมดกับ Claude Code v2.1.112 และ model Opus 4.7 ใหม่ (`claude-opus-4-7`) รวมถึงระดับ effort `xhigh` ใหม่ (ค่าเริ่มต้นบน Opus 4.7 อยู่ระหว่าง `high` และ `max`) สอง slash commands built-in ใหม่ (`/ultrareview`, `/less-permission-prompts`) auto-mode ที่ไม่ต้องใช้ `--enable-auto-mode` อีกต่อไปสำหรับผู้สมัคร Max บน Opus 4.7 เครื่องมือ PowerShell บน Windows theme "Auto (match terminal)" และ plan files ที่ตั้งชื่อตาม prompts ปรับ footer ของเอกสาร EN ทั้ง 18 ไฟล์เป็น Claude Code v2.1.112 @Luong NGUYEN

### ฟีเจอร์

- เพิ่มการแปลภาษายูเครน (uk) ครบถ้วนในทุกโมดูล เอกสารหลัก ตัวอย่าง และเอกสารอ้างอิง (039dde2) @Evgenij I

### แก้ไขข้อบกพร่อง

- แก้ไขข้อบกพร่องของ protocol ใน hook pre-tool-check.sh (bce7cf8) @yarlinghe
- เปลี่ยนตัวอย่าง mermaid ที่ผิดพลาดเป็น text block เพื่อให้ผ่าน CI (b8a7b1f) @Evgenij I
- แก้ไขการเข้ารหัส CP1251 ใน ToC ของ claude_concepts_guide.md ภาษายูเครน (d970cc6) @Evgenij I
- แทนที่ README ภาษายูเครนแบบ stub ด้วยการแปลฉบับเต็ม แก้ไข anchors ที่เสีย (f6d73e2) @Evgenij I
- แก้ไขเวอร์ชัน Claude Code เป็น 2.1.97 ในทุก footer (63a1416) @Luong NGUYEN
- ใช้การอัปเดตความถูกต้องของเอกสารวันที่ 2026-04-09 (e015f39) @Luong NGUYEN

### เอกสาร

- ซิงค์กับ Claude Code v2.1.112 (Opus 4.7, effort `xhigh`, `/ultrareview`, `/less-permission-prompts`, เครื่องมือ PowerShell, theme Auto-match-terminal) @Luong NGUYEN
- ซิงค์กับ Claude Code v2.1.110 (TUI, push notifications, session recap) (15f0085) @Luong NGUYEN
- ซิงค์กับ Claude Code v2.1.101 พร้อม `/team-onboarding`, `/ultraplan`, เครื่องมือ Monitor (2deba3a) @Luong NGUYEN
- ซิงค์เอกสารภาษาเวียดนามกับแหล่งที่มาภาษาอังกฤษ (561c6cb) @Thiên Toán
- อัปเดตวันที่ Last Updated และเวอร์ชัน Claude Code ในทุกไฟล์ (7f2e773) @Luong NGUYEN
- เพิ่มลิงก์ภาษายูเครนใน language switcher (9c224ff) @Luong NGUYEN
- ลบส่วน contributors (f07313d) @Luong NGUYEN
- อัปเดตเมตริก GitHub เป็น 21,800+ stars, 2,585+ forks (4f55374) @Luong NGUYEN

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.3.0...v2.1.112

---

## v2.3.0 — 2026-04-07

### ฟีเจอร์

- build และเผยแพร่ EPUB artifacts ต่อภาษา (90e9c30) @Thiên Toán
- เพิ่ม hook pre-tool-check.sh ที่ขาดหายไปใน 06-hooks (b511ed1) @JiayuWang
- เพิ่มการแปลภาษาจีนในไดเรกทอรี zh/ (89e89d4) @Luong NGUYEN
- เพิ่ม performance-optimizer subagent และ dependency-check hook (f53d080) @qk

### แก้ไขข้อบกพร่อง

- ความเข้ากันได้กับ Windows Git Bash + stdin JSON protocol (2cbb10c) @Luong NGUYEN
- แก้ไขเอกสารการกำหนดค่า autoCheckpoint ใน 08-checkpoints (749c79f) @JiayuWang
- ฝัง SVG images แทนการแทนที่ด้วย placeholders (1b16709) @Thiên Toán
- การ render nested code fence ใน README ของ memory (ce24423) @Zhaoshan Duan
- ใช้การแก้ไขจาก review ที่ตกหล่นจาก squash merge (34259ca) @Luong NGUYEN
- ทำให้ hook scripts เข้ากันได้กับ Windows Git Bash และใช้ stdin JSON protocol (107153d) @binyu li

### เอกสาร

- ซิงค์บทเรียนทั้งหมดกับเอกสาร Claude Code ล่าสุด (เมษายน 2026) (72d3b01) @Luong NGUYEN
- เพิ่มลิงก์ภาษาจีนใน language switcher (6cbaa4d) @Luong NGUYEN
- เพิ่ม language switcher ระหว่างภาษาอังกฤษและภาษาเวียดนาม (100c45e) @Luong NGUYEN
- เพิ่ม badge GitHub #1 Trending (0ca8c37) @Luong NGUYEN
- แนะนำ cc-context-stats สำหรับการตรวจสอบ context zone (d41b335) @Luong NGUYEN
- แนะนำ collection luongnv89/skills และ skill manager luongnv89/asm (7e3c0b6) @Luong NGUYEN
- อัปเดตสถิติ README ให้สอดคล้องกับเมตริก GitHub ปัจจุบัน (5,900+ stars, 690+ forks) (5001525) @Luong NGUYEN
- อัปเดตสถิติ README ให้สอดคล้องกับเมตริก GitHub ปัจจุบัน (3,900+ stars, 460+ forks) (9cb92d6) @Luong NGUYEN

### Refactoring

- แทนที่การพึ่งพา Kroki HTTP ด้วยการ render ผ่าน mmdc ในเครื่อง (e76bbe4) @Luong NGUYEN
- ย้ายการตรวจสอบคุณภาพไปยัง pre-commit ให้ CI เป็นการตรวจสอบรอบที่ 2 (6d1e0ae) @Luong NGUYEN
- จำกัด baseline ของ permissions สำหรับ auto-mode ให้แคบลง (2790fb2) @Luong NGUYEN
- แทนที่ hook auto-adapt ด้วย script ตั้งค่า permissions แบบครั้งเดียว (995a5d6) @Luong NGUYEN

### อื่นๆ

- shift-left quality gates — เพิ่ม mypy ใน pre-commit แก้ไข CI ที่ล้มเหลว (699fb39) @Luong NGUYEN
- เพิ่มการแปลภาษาเวียดนาม (Tiếng Việt) (a70777e) @Thiên Toán

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — 2026-03-26

### เอกสาร

- ซิงค์บทเรียนและเอกสารอ้างอิงทั้งหมดกับ Claude Code v2.1.84 (f78c094) @luongnv89
  - อัปเดต slash commands เป็น 55+ built-in + 5 bundled skills กำกับ 3 รายการว่าเลิกใช้งาน
  - ขยาย hook events จาก 18 เป็น 25 เพิ่มประเภท hook `agent` (ตอนนี้มี 4 ประเภท)
  - เพิ่ม Auto Mode, Channels, Voice Dictation ในฟีเจอร์ขั้นสูง
  - เพิ่มฟิลด์ frontmatter `effort`, `shell` สำหรับ skill; ฟิลด์ agent `initialPrompt`, `disallowedTools`
  - เพิ่ม WebSocket MCP transport, elicitation, ขีดจำกัดเครื่องมือ 2KB
  - เพิ่มการรองรับ LSP ของ plugin, `userConfig`, `${CLAUDE_PLUGIN_DATA}`
  - อัปเดตเอกสารอ้างอิงทั้งหมด (CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX)
- เขียน README ใหม่เป็นคู่มือที่มีโครงสร้างแบบ landing-page (32a0776) @luongnv89

### แก้ไขข้อบกพร่อง

- เพิ่มคำ cSpell และส่วน README ที่ขาดหายไปเพื่อให้เป็นไปตาม CI (93f9d51) @luongnv89
- เพิ่ม `Sandboxing` ลงใน cSpell dictionary (b80ce6f) @luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### แก้ไขข้อบกพร่อง

- ลบลิงก์ marketplace ที่ตายแล้วซึ่งทำให้การตรวจสอบลิงก์ของ CI ล้มเหลว (3fdf0d6) @luongnv89
- เพิ่ม `sandboxed` และ `pycache` ลงใน cSpell dictionary (dc64618) @luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### ฟีเจอร์

- เพิ่ม adaptive learning path พร้อม skills self-assessment และ lesson quiz (1ef46cd) @luongnv89
  - `/self-assessment` — แบบทดสอบความสามารถแบบ interactive ครอบคลุม 10 พื้นที่ฟีเจอร์ พร้อม learning path ที่ปรับแต่งเฉพาะบุคคล
  - `/lesson-quiz [lesson]` — การตรวจสอบความรู้รายบทเรียนพร้อมคำถามเจาะจง 8-10 ข้อ

### แก้ไขข้อบกพร่อง

- อัปเดต URLs ที่เสีย รายการที่เลิกใช้งาน และการอ้างอิงที่ล้าสมัย (8fe4520) @luongnv89
- แก้ไขลิงก์ที่เสียในส่วน resources และ skill self-assessment (7a05863) @luongnv89
- ใช้ tilde fences สำหรับ nested code blocks ในคู่มือ concepts (5f82719) @VikalpP
- เพิ่มคำที่ขาดหายไปลงใน cSpell dictionary (8df7572) @luongnv89

### เอกสาร

- Phase 5 QA — แก้ไขความสอดคล้อง URLs และคำศัพท์ในเอกสาร (00bbe4c) @luongnv89
- ทำ Phases 3-4 ให้สมบูรณ์ — การครอบคลุมฟีเจอร์ใหม่และการอัปเดตเอกสารอ้างอิง (132de29) @luongnv89
- เพิ่ม MCPorter runtime ในส่วน MCP context bloat (ef52705) @luongnv89
- เพิ่มคำสั่ง ฟีเจอร์ และการตั้งค่าที่ขาดหายไปใน 6 คู่มือ (4bc8f15) @luongnv89
- เพิ่ม style guide ตามแนวปฏิบัติที่มีอยู่ของ repo (84141d0) @luongnv89
- เพิ่มแถว self-assessment ในตารางเปรียบเทียบคู่มือ (8fe0c96) @luongnv89
- เพิ่ม VikalpP ในรายชื่อ contributors สำหรับ PR #7 (d5b4350) @luongnv89
- เพิ่มการอ้างอิง skill self-assessment และ lesson-quiz ใน README และ roadmap (d5a6106) @luongnv89

### ผู้ร่วมพัฒนาใหม่

- @VikalpP ร่วมพัฒนาครั้งแรกใน #7

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### ฟีเจอร์

- ซิงค์เอกสารทั้งหมดกับฟีเจอร์ Claude Code เดือนกุมภาพันธ์ 2026 (487c96d)
  - อัปเดต 26 ไฟล์ในทุกไดเรกทอรีบทเรียนทั้ง 10 และเอกสารอ้างอิง 7 ฉบับ
  - เพิ่มเอกสารสำหรับ **Auto Memory** — การเรียนรู้ที่คงอยู่ต่อโปรเจกต์
  - เพิ่มเอกสารสำหรับ **Remote Control**, **Web Sessions**, และ **Desktop App**
  - เพิ่มเอกสารสำหรับ **Agent Teams** (การทำงานร่วมกันหลาย agents แบบทดลอง)
  - เพิ่มเอกสารสำหรับ **MCP OAuth 2.0**, **Tool Search**, และ **Claude.ai Connectors**
  - เพิ่มเอกสารสำหรับ **Persistent Memory** และ **Worktree Isolation** สำหรับ subagents
  - เพิ่มเอกสารสำหรับ **Background Subagents**, **Task List**, **Prompt Suggestions**
  - เพิ่มเอกสารสำหรับ **Sandboxing** และ **Managed Settings** (Enterprise)
  - เพิ่มเอกสารสำหรับ **HTTP Hooks** และ hook events ใหม่ 7 รายการ
  - เพิ่มเอกสารสำหรับ **Plugin Settings**, **LSP Servers**, และการอัปเดต Marketplace
  - เพิ่มเอกสารสำหรับตัวเลือก rewind แบบ **Summarize from Checkpoint**
  - บันทึก 17 slash commands ใหม่ (`/fork`, `/desktop`, `/teleport`, `/tasks`, `/fast` เป็นต้น)
  - บันทึก CLI flags ใหม่ (`--worktree`, `--from-pr`, `--remote`, `--teleport`, `--teammate-mode` เป็นต้น)
  - บันทึกตัวแปรสภาพแวดล้อมใหม่สำหรับ auto memory, ระดับ effort, agent teams, และอื่นๆ

### การออกแบบ

- ออกแบบโลโก้ใหม่เป็นเครื่องหมาย compass-bracket พร้อม palette แบบ minimal (20779db)

### แก้ไขข้อบกพร่อง / การแก้ไข

- อัปเดตชื่อ model: Sonnet 4.5 → **Sonnet 4.6**, Opus 4.5 → **Opus 4.6**
- แก้ไขชื่อ permission mode: แทนที่ "Unrestricted/Confirm/Read-only" ที่เป็นเรื่องสมมติด้วย `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions` ที่มีอยู่จริง
- แก้ไข hook events: ลบ `PreCommit`/`PostCommit`/`PrePush` ที่เป็นเรื่องสมมติ เพิ่ม events ที่มีอยู่จริง (`SubagentStart`, `WorktreeCreate`, `ConfigChange` เป็นต้น)
- แก้ไข syntax ของ CLI: แทนที่ `claude-code --headless` ด้วย `claude -p` (print mode)
- แก้ไขคำสั่ง checkpoint: แทนที่ `/checkpoint save/list/rewind/diff` ที่เป็นเรื่องสมมติด้วยอินเทอร์เฟซ `Esc+Esc` / `/rewind` ที่มีอยู่จริง
- แก้ไขการจัดการเซสชัน: แทนที่ `/session list/new/switch/save` ที่เป็นเรื่องสมมติด้วย `/resume`/`/rename`/`/fork` ที่มีอยู่จริง
- แก้ไขรูปแบบ plugin manifest: ย้าย `plugin.yaml` → `.claude-plugin/plugin.json`
- แก้ไข MCP config paths: `~/.claude/mcp.json` → `.mcp.json` (โปรเจกต์) / `~/.claude.json` (ผู้ใช้)
- แก้ไข URLs ของเอกสาร: `docs.claude.com` → `docs.anthropic.com`; ลบ `plugins.claude.com` ที่เป็นเรื่องสมมติ
- ลบฟิลด์การกำหนดค่าที่เป็นเรื่องสมมติในหลายไฟล์
- อัปเดตวันที่ "Last Updated" ทั้งหมดเป็นเดือนกุมภาพันธ์ 2026

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
