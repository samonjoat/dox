import importlib.util
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("dox_lint", ROOT / "scripts" / "dox_lint.py")
assert SPEC is not None
assert SPEC.loader is not None
dox_lint = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dox_lint)


ROOT_AGENTS = """
<!-- DOX-CORE-START: protected -->
# DOX framework

## Child DOX Index

- `docs/AGENTS.md` — docs scope.
<!-- DOX-CORE-END: protected -->
"""

CHILD_AGENTS = """
# Docs DOX

## Purpose

Docs.

## Ownership

Docs.

## Local Contracts

Docs.

## Work Guidance

Docs.

## Verification

Docs.

## Child DOX Index

No child DOX files yet.
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


class DoxLintTests(unittest.TestCase):
    def test_valid_tree_passes(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root / "AGENTS.md", ROOT_AGENTS)
            write(root / "docs" / "AGENTS.md", CHILD_AGENTS)

            self.assertEqual(dox_lint.validate(root), [])

    def test_core_marker_mentions_without_html_comments_fail(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root / "AGENTS.md",
                """
                # DOX framework

                This text mentions `DOX-CORE-START` and `DOX-CORE-END`, but has no comments.

                ## Child DOX Index

                No child DOX files yet.
                """,
            )

            errors = dox_lint.validate(root)

            self.assertIn("root AGENTS.md missing DOX-CORE-START HTML comment marker", errors)
            self.assertIn("root AGENTS.md missing DOX-CORE-END HTML comment marker", errors)

    def test_child_index_entry_missing_description_fails_but_path_is_checked(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(
                root / "AGENTS.md",
                """
                <!-- DOX-CORE-START: protected -->
                # DOX framework

                ## Child DOX Index

                - `docs/AGENTS.md`
                - `missing/AGENTS.md`
                <!-- DOX-CORE-END: protected -->
                """,
            )
            write(root / "docs" / "AGENTS.md", CHILD_AGENTS)

            errors = dox_lint.validate(root)

            self.assertIn("AGENTS.md: child index entry for docs/AGENTS.md missing description", errors)
            self.assertIn("AGENTS.md: child index entry for missing/AGENTS.md missing description", errors)
            self.assertIn("AGENTS.md: child index points to missing missing/AGENTS.md", errors)


if __name__ == "__main__":
    unittest.main()
