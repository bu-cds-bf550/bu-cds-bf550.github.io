#!/usr/bin/env python3
"""Assemble a PowerPoint file from decktape's per-slide screenshots.

    tools/pptx_from_screenshots.py <screenshots-dir> <deck-basename> <output.pptx>

decktape exports the PDF by driving a browser through the deck one slide at a time, and with
`--screenshots` it also saves each slide as a PNG on the way. This script puts those images,
one per slide, into a 16:9 .pptx -- so the PowerPoint is the same rendering as the PDF and the
web deck, pixel for pixel, with none of Pandoc's pptx writer limitations (dropped fragment
pauses, flattened incremental lists, lost theme).

The slides are pictures: the text on them cannot be edited or selected. That is deliberate.
The .pptx exists for students who want to take notes against the slides -- in the notes pane
(every slide gets an empty one) or in text boxes beside the picture -- not as an editable copy
of the deck. The .qmd source is the thing to edit.

decktape names each screenshot <basename>_<index>_<WxH>.png with a 1-based index, and it
joins the screenshots directory with the *full* PDF path, so the files can land in a subtree
of the directory given; the search is recursive for that reason.

Needs python-pptx (slides/requirements.txt). Pillow, which it uses to read image sizes, comes
with matplotlib.
"""
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu

INDEX = re.compile(r"_(\d+)_\d+x\d+\.png$")


def screenshots(directory: Path, basename: str) -> list[Path]:
    files = [p for p in directory.rglob(f"{basename}_*_*x*.png") if INDEX.search(p.name)]
    files.sort(key=lambda p: int(INDEX.search(p.name).group(1)))
    return files


def build(images: list[Path], output: Path) -> None:
    prs = Presentation()
    prs.slide_width = Emu(12192000)   # 13.333 in: the 16:9 widescreen default
    prs.slide_height = Emu(6858000)   # 7.5 in
    blank = prs.slide_layouts[6]
    for image in images:
        slide = prs.slides.add_slide(blank)
        slide.shapes.add_picture(str(image), 0, 0, width=prs.slide_width, height=prs.slide_height)
        slide.notes_slide  # created on first access: an empty notes pane, ready for the student
    prs.save(str(output))


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    directory, basename, output = Path(argv[1]), argv[2], Path(argv[3])
    images = screenshots(directory, basename)
    if not images:
        print(f"pptx_from_screenshots: no {basename}_*.png under {directory}", file=sys.stderr)
        return 1
    build(images, output)
    print(f"{output}: {len(images)} slides")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
