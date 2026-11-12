"""Tests for the Pele-based Mermaid validator (check_mermaid.py)."""

from __future__ import annotations

import logging
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import check_mermaid
from pele_renderer import (
    PeleDiagramError,
    PeleHelperError,
    PeleResult,
    PeleUnavailableError,
)

FLOW = "graph TD\n    A --> B\n"
SEQ = "sequenceDiagram\n    A->>B: hi\n"
BROKEN = "graph TD\n    A -->\n"


def _md(*blocks: str) -> str:
    body = ["# Title", ""]
    for block in blocks:
        body += ["Some prose.", "", f"```mermaid\n{block}```", ""]
    return "\n".join(body)


@pytest.fixture(autouse=True)
def _no_ambient_strictness(monkeypatch: pytest.MonkeyPatch) -> None:
    """CI=true on runners would make every 'non-strict' case strict."""
    monkeypatch.delenv("CI", raising=False)
    monkeypatch.delenv("PELE_REQUIRED", raising=False)


@pytest.fixture
def project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Run the validator from an empty tmp project (discovery is cwd-based)."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


class FakeRenderer:
    """Stands in for pele_renderer.render_diagrams and records its calls."""

    def __init__(self) -> None:
        self.calls: list[list[str]] = []

    def __call__(
        self, sources: Sequence[str], logger: logging.Logger, **_: Any
    ) -> list[PeleResult]:
        self.calls.append(list(sources))
        results = []
        for source in sources:
            if source == BROKEN:
                results.append(
                    PeleResult(
                        svg=None,
                        diagram_type=None,
                        error=PeleDiagramError("syntax", "Expecting node", 2, 9),
                    )
                )
            else:
                kind = "sequence" if source.startswith("sequence") else "flowchart"
                results.append(PeleResult(svg="<svg/>", diagram_type=kind))
        return results


@pytest.fixture
def fake_render(monkeypatch: pytest.MonkeyPatch) -> FakeRenderer:
    fake = FakeRenderer()
    monkeypatch.setattr(check_mermaid, "render_diagrams", fake)
    return fake


def _unavailable(*_a: Any, **_k: Any) -> list[PeleResult]:
    raise PeleUnavailableError("node not found on PATH")


class TestExtractBlocks:
    def test_extracts_fences_with_info_string_or_trailing_space(
        self, tmp_path: Path
    ) -> None:
        md = tmp_path / "diagram.md"
        md.write_text(
            "```mermaid \n"
            + FLOW
            + "```\n\n"
            + "```mermaid title=Overview\n"
            + SEQ
            + "```\n",
            encoding="utf-8",
        )
        blocks = check_mermaid.extract_blocks(md)
        assert [b.source for b in blocks] == [FLOW, SEQ]

    def test_ignores_inline_code_and_other_languages(self, tmp_path: Path) -> None:
        md = tmp_path / "table.md"
        md.write_text(
            "| Hook | Checks |\n"
            "|------|--------|\n"
            "| mermaid | Every ` ```mermaid ` block renders |\n\n"
            "```mermaidjs\n" + FLOW + "```\n\n"
            "```mermaid-foo\n" + FLOW + "```\n\n"
            "```mermaid\n" + SEQ + "```\n",
            encoding="utf-8",
        )
        blocks = check_mermaid.extract_blocks(md)
        assert [b.source for b in blocks] == [SEQ]


class TestValidBlocks:
    def test_valid_blocks_pass_with_count_line(
        self,
        project: Path,
        fake_render: FakeRenderer,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        (project / "a.md").write_text(_md(FLOW, SEQ), encoding="utf-8")
        (project / "b.md").write_text(_md(FLOW), encoding="utf-8")

        assert check_mermaid.main([]) == 0

        out = capsys.readouterr().out
        assert (
            "✅ Pele 1.6.0 rendered 3 Mermaid block(s) (2 unique) from 2 file(s): "
            "flowchart 1, sequence 1"
        ) in out

    def test_duplicates_rendered_once(
        self, project: Path, fake_render: FakeRenderer
    ) -> None:
        (project / "a.md").write_text(_md(FLOW, FLOW), encoding="utf-8")
        (project / "b.md").write_text(_md(FLOW, SEQ), encoding="utf-8")

        assert check_mermaid.main([]) == 0

        assert fake_render.calls == [[FLOW, SEQ]]

    def test_ignore_dirs_are_skipped(
        self, project: Path, fake_render: FakeRenderer
    ) -> None:
        (project / "a.md").write_text(_md(FLOW), encoding="utf-8")
        for ignored in ("node_modules", ".venv", "blog-posts"):
            (project / ignored).mkdir()
            (project / ignored / "x.md").write_text(_md(BROKEN), encoding="utf-8")

        assert check_mermaid.main([]) == 0
        assert fake_render.calls == [[FLOW]]


class TestBrokenBlocks:
    def test_failure_reports_path_and_line(
        self,
        project: Path,
        fake_render: FakeRenderer,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        (project / "doc.md").write_text(_md(FLOW, BROKEN), encoding="utf-8")
        # The second ```mermaid fence sits on line 12 of the generated file.
        lines = (project / "doc.md").read_text(encoding="utf-8").splitlines()
        assert lines[11] == "```mermaid"

        assert check_mermaid.main([]) == 1

        out = capsys.readouterr().out
        assert (
            "doc.md:12 (block 2): [syntax] Expecting node (diagram line 2, column 9)"
        ) in out

    def test_shared_broken_source_reported_for_every_block(
        self,
        project: Path,
        fake_render: FakeRenderer,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        (project / "a.md").write_text(_md(BROKEN), encoding="utf-8")
        (project / "b.md").write_text(_md(BROKEN), encoding="utf-8")

        assert check_mermaid.main([]) == 1

        out = capsys.readouterr().out
        assert "a.md:5 (block 1)" in out
        assert "b.md:5 (block 1)" in out
        assert fake_render.calls == [[BROKEN]]

    def test_helper_error_always_fails(
        self,
        project: Path,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        (project / "a.md").write_text(_md(FLOW), encoding="utf-8")

        def crash(*_a: Any, **_k: Any) -> list[PeleResult]:
            raise PeleHelperError("helper exited with status 1")

        monkeypatch.setattr(check_mermaid, "render_diagrams", crash)

        assert check_mermaid.main([]) == 1
        assert "❌ Pele helper failed" in capsys.readouterr().out


class TestStrictness:
    def test_unavailable_non_strict_warns_and_passes(
        self,
        project: Path,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        (project / "a.md").write_text(_md(FLOW), encoding="utf-8")
        monkeypatch.setattr(check_mermaid, "render_diagrams", _unavailable)

        assert check_mermaid.main([]) == 0

        out = capsys.readouterr().out
        assert "⚠" in out
        assert "skipping Mermaid validation" in out
        assert "Node.js >= 20" in out

    @pytest.mark.parametrize(
        ("argv", "env"),
        [
            (["--strict"], {}),
            ([], {"PELE_REQUIRED": "1"}),
            ([], {"CI": "true"}),
            ([], {"CI": "YES"}),
        ],
        ids=["flag", "PELE_REQUIRED", "CI", "CI-uppercase"],
    )
    def test_unavailable_strict_fails(
        self,
        project: Path,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        argv: list[str],
        env: dict[str, str],
    ) -> None:
        (project / "a.md").write_text(_md(FLOW), encoding="utf-8")
        monkeypatch.setattr(check_mermaid, "render_diagrams", _unavailable)
        for name, value in env.items():
            monkeypatch.setenv(name, value)

        assert check_mermaid.main(argv) == 1
        assert "❌ Pele is unavailable" in capsys.readouterr().out

    def test_falsy_env_is_not_strict(
        self, project: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        (project / "a.md").write_text(_md(FLOW), encoding="utf-8")
        monkeypatch.setattr(check_mermaid, "render_diagrams", _unavailable)
        monkeypatch.setenv("CI", "false")
        monkeypatch.setenv("PELE_REQUIRED", "0")

        assert check_mermaid.main([]) == 0

    @pytest.mark.parametrize(
        ("argv", "env"),
        [(["--strict"], {}), ([], {"PELE_REQUIRED": "1"}), ([], {"CI": "1"})],
        ids=["flag", "PELE_REQUIRED", "CI"],
    )
    def test_zero_blocks_strict_fails(
        self,
        project: Path,
        fake_render: FakeRenderer,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        argv: list[str],
        env: dict[str, str],
    ) -> None:
        (project / "a.md").write_text("# No diagrams here\n", encoding="utf-8")
        for name, value in env.items():
            monkeypatch.setenv(name, value)

        assert check_mermaid.main(argv) == 1
        assert "No Mermaid blocks found" in capsys.readouterr().out
        assert fake_render.calls == []

    def test_zero_blocks_non_strict_passes(
        self, project: Path, fake_render: FakeRenderer
    ) -> None:
        (project / "a.md").write_text("# No diagrams here\n", encoding="utf-8")

        assert check_mermaid.main([]) == 0
