#!/usr/bin/env python3
"""Fail the build if instructor-facing material reaches the published site.

Scans the *built* site (default `_site`) rather than the sources, because that is what
actually ships: a file is published unless something excludes it, and the failure mode this
guards against is exactly a new file nobody remembered to exclude. Unit 1's instructor
run-sheet reached production this way -- `_config.yml` excluded `internal/` but not the
`lectures/` directory it landed in, and a markdown file with no frontmatter is copied
verbatim into the output.

The patterns are deliberately narrow. Case-insensitive "instructor" is useless here --
student-facing pages legitimately say "with instructors and TAs in the room" -- and so are
"unseal" and "answer key", both of which appear in the published assignment pages. Each
pattern below was checked to have zero matches across the published sources.

Counterpart to the textbook repo's `tools/lint_chapters.py` L4 boundary tripwire, which
guards the same border from the other side.
"""
import re
import sys
from pathlib import Path

TRIPWIRES = [
    (re.compile(r"\(INSTRUCTOR"), "instructor-only document marker"),
    (re.compile(r"\(INTERNAL"), "internal planning document marker"),
    (re.compile(r"\(PRIVATE"), "private document marker"),
    (re.compile(r"not released"), "explicitly unreleased material"),
    (re.compile(r"Do not give away"), "answer-withholding instruction to staff"),
    (re.compile(r"planted defect", re.I), "seeded-defect inventory"),
    (re.compile(r"run-sheet", re.I), "instructor run-sheet"),
    (re.compile(r'<aside class="notes"'), "speaker notes in a published slide deck"),
    (re.compile(r"window\._input_file"), "deck source embedded by the editable extension"),
]

SCAN_SUFFIXES = {".html", ".md", ".txt", ".json", ".xml"}


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    if not root.is_dir():
        print(f"lint: {root} is not a directory -- build the site first", file=sys.stderr)
        return 2

    hits = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for pattern, why in TRIPWIRES:
                if pattern.search(line):
                    rel = path.relative_to(root)
                    hits.append(f"{rel}:{lineno}: {why} -- matched {pattern.pattern!r}")

    if hits:
        print("Instructor-facing content found in the published site:\n", file=sys.stderr)
        for hit in hits:
            print(f"  {hit}", file=sys.stderr)
        print(
            "\nMove it to the bu-cds-bf550/bf550-instructor repository. If a match is a false\n"
            "positive, narrow the pattern in tools/lint_no_instructor_content.py -- do not\n"
            "widen an exclude to paper over it.",
            file=sys.stderr,
        )
        return 1

    print(f"lint: no instructor-facing content in {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
