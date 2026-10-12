#!/usr/bin/env bash
# Export one deck to a PowerPoint file whose slides are pictures, with the deck's speaker
# notes in the notes pane. Nothing in the course uses this yet. The instructor repository's
# `tools/gdrive_slides.py` drives it inside the container to put a deck on Google Slides;
# see that repository's `gdrive-integration-spike.md` for what it was tried for and why it
# is parked.
#
#   tools/export_deck.sh slides/unit-03-1.qmd /tmp/unit-03-1.pptx
#
# Why pictures. Google Slides drops any paragraph carrying an equation when it imports a
# text .pptx -- the whole paragraph, not just the equation. A picture per slide is the same
# rendering as the web deck, so the algebra, the theme and the layout all survive; nothing on
# the slides can be edited afterwards, and the .qmd stays the thing to edit. This is
# `tools/build_slides.sh --pdf`'s export path, run for one deck and with the notes carried
# across.
#
# The deck is rendered under the **instructor profile**, which keeps the speaker notes and
# writes to `_instructor-slides/`, outside the published tree, so the notes never reach
# `_site/`.
#
# Needs: quarto, decktape, a Chrome/Chromium, and python-pptx -- all present in the course
# image, so run it there: `echo 'tools/export_deck.sh …' | make shell`.
set -euo pipefail
cd "$(dirname "$0")/.."

src="${1:-}"; out="${2:-}"
if [[ -z "$src" || -z "$out" ]]; then
  echo "usage: tools/export_deck.sh <slides/deck.qmd> <output.pptx>" >&2; exit 2
fi
[[ -f "$src" ]] || { echo "export_deck: no such deck: $src" >&2; exit 1; }
mkdir -p "$(dirname "$out")"
out="$(cd "$(dirname "$out")" && pwd)/$(basename "$out")"

# Quarto never renders a file whose name starts with `_`, and these decks are named that way
# on purpose (an unpublished deck is kept out of the project render). Render a copy under a
# plain name instead, and take it away again afterwards.
name="deck-export-$(basename "${src%.qmd}" | sed 's/^_*//')"
staged="slides/$name.qmd"
html="_instructor-slides/$name.html"
shots="$(mktemp -d "${TMPDIR:-/tmp}/deck-shots.XXXXXX")"
cleanup() { rm -rf "$shots" "$staged" "slides/${name}_files" "_instructor-slides/$name.html" "_instructor-slides/${name}_files"; }
trap cleanup EXIT
cp "$src" "$staged"

quarto render "$staged" --profile instructor >/dev/null
[[ -f "$html" ]] || { echo "export_deck: quarto wrote no $html" >&2; exit 1; }

chrome="${CHROME_PATH:-}"
if [[ -z "$chrome" ]]; then
  for candidate in google-chrome google-chrome-stable chromium chromium-browser; do
    if command -v "$candidate" >/dev/null 2>&1; then chrome="$(command -v "$candidate")"; break; fi
  done
fi
[[ -n "$chrome" ]] || { echo "export_deck: no Chrome/Chromium found; set CHROME_PATH" >&2; exit 1; }
if command -v decktape >/dev/null 2>&1; then decktape=(decktape); else decktape=(npx -y decktape@3); fi
export PUPPETEER_SKIP_DOWNLOAD=true PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

# decktape joins --screenshots-directory with the PDF's *full* path and does not create that
# subtree, so make it first. One pass prints the PDF and shoots every slide.
pdf="${out%.pptx}.pdf"
mkdir -p "$shots$(dirname "$pdf")"
"${decktape[@]}" reveal --chrome-path "$chrome" \
    --chrome-arg=--no-sandbox --chrome-arg=--disable-gpu \
    --screenshots --screenshots-directory "$shots" --screenshots-size 1920x1080 \
    "$html" "$pdf"

# decktape names each screenshot after the PDF it is printing, not after the deck.
python3 tools/pptx_from_screenshots.py "$shots" "$(basename "${pdf%.pdf}")" "$out" --notes "$html"
echo "export_deck: $out (and the PDF beside it)"
