#!/usr/bin/env bash
# Render the lecture decks (slides/*.qmd) into _site/slides/, and optionally export each one
# to PDF and PowerPoint. One script for both the laptop and CI, so what deploys is what was
# previewed.
#
#   tools/build_slides.sh                # HTML decks only
#   tools/build_slides.sh --pdf          # HTML + a PDF and a .pptx beside each deck
#   tools/build_slides.sh --instructor   # HTML with speaker notes kept, into _instructor-slides/
#
# The .pptx is not a Pandoc export: it is the PDF's slides as pictures, one per slide, made from
# the screenshots decktape takes on the same pass that prints the PDF and assembled by
# tools/pptx_from_screenshots.py. Same rendering as the web deck; the text is not editable.
# It exists for students who want to take notes against the slides.
#
# Needs: quarto, a Python with slides/requirements.txt installed (set QUARTO_PYTHON if it is
# not the one on PATH; python-pptx is in that file), and -- for --pdf -- node plus a
# Chrome/Chromium (CHROME_PATH, or google-chrome/chromium on PATH, or a Playwright-installed
# Chromium under ~/.cache).
set -euo pipefail
cd "$(dirname "$0")/.."

mode="${1:-html}"
case "$mode" in
  html|--html) quarto render slides ;;
  --instructor) quarto render slides --profile instructor
                echo "instructor decks (with notes) in _instructor-slides/ -- not for publication" ;;
  --pdf)
    quarto render slides
    chrome="${CHROME_PATH:-}"
    if [[ -z "$chrome" ]]; then
      for candidate in google-chrome google-chrome-stable chromium chromium-browser; do
        if command -v "$candidate" >/dev/null 2>&1; then chrome="$(command -v "$candidate")"; break; fi
      done
    fi
    if [[ -z "$chrome" ]]; then
      chrome="$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | sort -V | tail -1 || true)"
    fi
    if [[ -z "$chrome" ]]; then
      echo "build_slides: no Chrome/Chromium found; set CHROME_PATH" >&2; exit 1
    fi
    # decktape bundles Puppeteer, which would download its own Chromium; use the one we found.
    # An installed decktape (the Docker image has one) is used directly; otherwise npx fetches it.
    export PUPPETEER_SKIP_DOWNLOAD=true PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
    if command -v decktape >/dev/null 2>&1; then decktape=(decktape); else decktape=(npx -y decktape@3); fi
    shots="$(mktemp -d "${TMPDIR:-/tmp}/deck-shots.XXXXXX")"
    trap 'rm -rf "$shots"' EXIT
    for html in _site/slides/*.html; do
      [[ "$(basename "$html")" == "index.html" ]] && continue   # the Jekyll index page, not a deck
      # One pass through the deck prints the PDF and screenshots every slide; the screenshots
      # become the .pptx. decktape joins --screenshots-directory with the PDF's full path and
      # does not create that subtree, so make it -- the assembler searches $shots recursively.
      mkdir -p "$shots/$(dirname "$html")"
      "${decktape[@]}" reveal --chrome-path "$chrome" \
          --chrome-arg=--no-sandbox --chrome-arg=--disable-gpu \
          --screenshots --screenshots-directory "$shots" --screenshots-size 1920x1080 \
          "$html" "${html%.html}.pdf"
      python3 tools/pptx_from_screenshots.py "$shots" "$(basename "${html%.html}")" "${html%.html}.pptx"
    done ;;
  *) echo "usage: tools/build_slides.sh [--pdf|--instructor]" >&2; exit 2 ;;
esac
