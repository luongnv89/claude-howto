"""Regression tests for frontmatter in installable Japanese skill templates."""

from pathlib import Path

import pytest

SKILLS_DIR = Path(__file__).resolve().parents[2] / "ja" / "03-skills"


@pytest.mark.parametrize(
    "skill",
    [
        "blog-draft",
        "brand-voice",
        "claude-md",
        "code-review-specialist",
        "doc-generator",
        "refactor",
    ],
)
def test_japanese_skill_frontmatter_precedes_i18n_comments(skill: str) -> None:
    lines = (SKILLS_DIR / skill / "SKILL.md").read_text(encoding="utf-8").splitlines()

    # Claude Code recognizes frontmatter only when the opening --- is on line 1.
    assert lines[0] == "---"
    closing = lines.index("---", 1)
    frontmatter = lines[1:closing]
    assert f"name: {skill}" in frontmatter
    assert any(line.startswith("description: ") for line in frontmatter)
    if skill == "brand-voice":
        assert "user-invocable: false" in frontmatter

    body = "\n".join(lines[closing + 1 :])
    assert f"<!-- i18n-source: 03-skills/{skill}/SKILL.md -->" in body
    assert "<!-- i18n-source-sha: " in body
    assert "<!-- i18n-date: " in body
    assert not any(line.startswith("<!-- i18n-") for line in frontmatter)
