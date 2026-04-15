#!/usr/bin/env bash
# Demo: spin up a sample cohort with simulated students in various states
# so you can see the bootcamp platform in action.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$SCRIPT_DIR"

# Clean any previous demo data
rm -rf ~/.claude-bootcamp
rm -rf /tmp/qa-demo-alice /tmp/qa-demo-bob /tmp/qa-demo-carol

echo "============================================================"
echo "  AI Bootcamp Demo - Setting up sample cohort"
echo "============================================================"
echo ""

# 1. Open registration
./bootcamp open-registration --cohort "demo-2026-q2" --name "Demo Cohort Q2 2026" --deadline "2026-12-31"
echo ""

# 2. Register 3 demo students
./bootcamp register alice "Alice Anderson" alice@testdevlab.com --cohort demo-2026-q2
./bootcamp register bob "Bob Brown" bob@testdevlab.com --cohort demo-2026-q2
./bootcamp register carol "Carol Chen" carol@testdevlab.com --cohort demo-2026-q2
echo ""

# 3. Create sample project directories with varying completion levels

# --- Alice: completed S1-S3 (advanced student) ---
echo "Setting up Alice (completed S1-S3)..."
mkdir -p /tmp/qa-demo-alice/{server,client/src,.claude/{skills/test-gen,skills/qa-review,rules,agents}}
cat > /tmp/qa-demo-alice/package.json <<'EOF'
{"name":"qa-command-center","dependencies":{"express":"^4.18","react":"^18"},"devDependencies":{"vite":"^5"},"scripts":{"dev":"vite","start":"node server/index.js"}}
EOF
cat > /tmp/qa-demo-alice/server/index.js <<'EOF'
const express = require('express');
const app = express();
app.get('/api/v1/test-cases', (req, res) => res.json({ success: true, data: [] }));
EOF
for name in App TestCaseList TestCaseForm BugTracker TestSuiteList; do
  echo "export default function $name() { return <div>$name</div>; }" > /tmp/qa-demo-alice/client/src/$name.jsx
done
cat > /tmp/qa-demo-alice/CLAUDE.md <<'EOF'
# QA Command Center
## Standards
Follow ISTQB severity levels S1-S4. Use REST API conventions.
All responses: { success, data, error }.
## Naming
- kebab-case for files, PascalCase for React components
EOF
echo "Use REST conventions" > /tmp/qa-demo-alice/.claude/rules/api.md
cat > /tmp/qa-demo-alice/.claude/skills/test-gen/SKILL.md <<'EOF'
---
name: test-generator
description: Generate test suites using ISTQB boundary value and equivalence partitioning
---
# Test Generator
EOF
cat > /tmp/qa-demo-alice/.claude/skills/qa-review/SKILL.md <<'EOF'
---
name: qa-review
description: Review code from a QA perspective checking for missing validations
---
# QA Review
EOF

# --- Bob: struggling student (missing .claude/skills/ — fails S1 critical) ---
echo "Setting up Bob (struggling, will fail S1 until auto-unlock)..."
mkdir -p /tmp/qa-demo-bob/{server,client/src}
cat > /tmp/qa-demo-bob/package.json <<'EOF'
{"name":"qa-command-center","dependencies":{"express":"^4.18","react":"^18"}}
EOF
cat > /tmp/qa-demo-bob/server/index.js <<'EOF'
const express = require('express');
EOF
cat > /tmp/qa-demo-bob/client/src/App.jsx <<'EOF'
export default function App() { return <h1>Hello</h1>; }
EOF
# Deliberately no .claude/skills/ — Bob hasn't built any custom skills yet

# --- Carol: just setup, haven't started ---
echo "Setting up Carol (just registered)..."
mkdir -p /tmp/qa-demo-carol

echo ""
echo "============================================================"
echo "  Simulating student work..."
echo "============================================================"

# Alice: setup + complete S1-S3
./bootcamp setup --student-id alice --project-dir /tmp/qa-demo-alice
./bootcamp start-session 1 2>&1 | tail -5
# Simulate some prompts for alice
PYTHONPATH="$REPO_ROOT" python3 <<'PYEOF'
from workshop.platform import database as db
conn = db.get_connection()

# Alice prompts — high quality
alice_prompts = [
    "Create a full-stack project with Express backend and React frontend using Vite, named QA Command Center following the ISTQB naming conventions",
    "Generate a test case data model with ISTQB severity levels S1-S4 and priority P1-P4, with fields for title, preconditions, steps, and expected result",
    "Build a REST API for test cases with consistent {success, data, error} response format as specified in CLAUDE.md",
    "Create a React page for test case listing with severity filter badges and sortable columns",
    "Add a custom slash command for creating new test cases with a template including boundary value analysis",
]
for i, p in enumerate(alice_prompts):
    db.log_prompt(conn, "alice", 1, "prompt", p)

# Bob prompts — low quality (vague)
bob_prompts = [
    "make it work",
    "fix it",
    "help",
    "do the thing",
    "make a test",
    "idk what to do",
]
for p in bob_prompts:
    db.log_prompt(conn, "bob", 1, "prompt", p)

conn.close()
print("  Simulated prompts logged for Alice (high quality) and Bob (low quality)")
PYEOF

# Alice: pass S1, S2, S3
# Set current session for alice
echo "alice" > ~/.claude-bootcamp/student-id
for s in 1 2 3; do
  echo "$s" > ~/.claude-bootcamp/current-session
  ./bootcamp complete-session $s --project-dir /tmp/qa-demo-alice 2>&1 | tail -5
done

# Bob: setup + try S1 five times (auto-unlock)
echo "bob" > ~/.claude-bootcamp/student-id
./bootcamp setup --student-id bob --project-dir /tmp/qa-demo-bob
./bootcamp start-session 1 2>&1 | tail -3
echo ""
echo "--- Bob fails S1 five times to trigger auto-unlock ---"
# Note: complete-session exits 1 on failed gate; that's the expected behavior here,
# so we pipe through `|| true` to keep the loop going under `set -e`.
for i in 1 2 3 4 5; do
  echo ""
  echo "Bob attempt $i:"
  (./bootcamp complete-session 1 --project-dir /tmp/qa-demo-bob 2>&1 || true) | tail -15
done

# Carol: just setup
echo "carol" > ~/.claude-bootcamp/student-id
./bootcamp setup --student-id carol --project-dir /tmp/qa-demo-carol

echo ""
echo "============================================================"
echo "  Demo data ready! Try these commands:"
echo "============================================================"
echo ""
echo "  # View all students and their progress:"
echo "  ./bootcamp dashboard"
echo ""
echo "  # Alice's detailed status (advanced student):"
echo "  ./bootcamp status --student alice --detailed"
echo ""
echo "  # Bob's detailed status (shows auto-unlock):"
echo "  ./bootcamp status --student bob --detailed"
echo ""
echo "  # See Alice's prompts (high quality):"
echo "  ./bootcamp status --student alice --prompts"
echo ""
echo "  # Generate cohort score report as HTML:"
echo "  ./bootcamp scores --format html --output /tmp/demo-scores.html"
echo "  # Then open /tmp/demo-scores.html in browser"
echo ""
echo "  # Full AI scoring for Alice:"
echo "  ./bootcamp grade alice --no-ai"
echo ""
echo "  # To start over: rm -rf ~/.claude-bootcamp && ./workshop/demo.sh"
echo ""
