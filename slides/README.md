# Lecture decks

[Quarto revealjs](https://quarto.org/docs/presentations/revealjs/) decks, authored in markdown
with code that executes at render time. **One deck per meeting that has a lecture**, named
`unit-NN-M.qmd` for unit `NN`, session `M` — the shape the labs use. There is a lecture in every
session, so a three-session unit has three decks and three entries in `_data/slides.yml`, each
carrying its `session` and its `date`. Rendered decks are
published at `https://bu-cds-bf550.github.io/slides/<name>.html` with a PDF and a PowerPoint
file beside each one;
the unit pages and [`/slides/`](https://bu-cds-bf550.github.io/slides/) link to them from
[`_data/slides.yml`](../_data/slides.yml).

## Authoring

1. Copy [`_template.qmd`](_template.qmd) to `unit-NN-M.qmd`, or generate a skeleton with
   `tools/deck_skeleton.py --unit N --session M` in the instructor repo. The template
   demonstrates every construct the decks use: reveals (`. . .`), incremental lists, columns,
   executed Python
   with hidden or shown code, figures, output-on-the-next-slide, Graphviz/Mermaid diagrams,
   static images (`img/`), and speaker notes.
2. Add an entry to `_data/slides.yml` — `unit`, `session`, `date` (spelled as the schedule
   spells it), `title`, `file`. That entry makes the unit page show *view · PDF · PowerPoint*
   links against the right meeting and adds the row on `/slides/`.
3. Push. CI renders the deck, exports the PDF and the PowerPoint, gates the site, and deploys.

Conventions the decks inherit from the textbook (see its `CONVENTIONS.md`):

- **Activation, not delivery.** The reading carries first exposure; a deck puts the unit's
  ideas to work. A deck that re-teaches its chapter is too long.
- **Seed every random draw**, reusing the chapter's seeds where a chunk comes from the
  chapter, so what is projected in class is exactly what students find in the reading.
- **Slide headings are a public interface.** The instructor run-sheets cite slides by
  heading text, not by number, and name the deck the heading is in. Adding or reordering slides
  is free; renaming a heading, or moving one to another session's deck, means updating that
  unit's run-sheet.

### Speaker notes

Write them inline, under the slide they belong to:

```markdown
::: {.notes}
Ask for a show of hands before advancing.
:::
```

`strip-notes.lua` removes every `.notes` block from the public build, and
`tools/lint_no_instructor_content.py` fails the site build if a note ever reaches `_site/`.
The instructor build keeps them: `tools/build_slides.sh --instructor` renders into the
git-ignored `_instructor-slides/`; open a deck there and press `s`.

## Rendering locally

The easy way is the repository's Docker environment, a replica of the CI job (see the
`Makefile`): `make dev` serves each deck at `http://localhost:4200/unit-01.html` and re-renders
it whenever you save its source, reloading the browser tab; the whole site, decks included, is at
`http://localhost:4000` (the deck pages under `/slides/`). Open a deck on :4200 by name — that
server is rooted at `_site/slides/`, so the `/slides/` index Jekyll writes there loads unstyled,
its `/assets/...` links pointing above the root. `make pdf` renders decks and PDFs, `make instructor` the build with
speaker notes, `make site` the whole production build.

Without Docker you need [Quarto](https://quarto.org/docs/get-started/) 1.10+, Python with
[`requirements.txt`](requirements.txt), and for PDFs Node plus a Chrome/Chromium:

```bash
# from the repository root
export QUARTO_PYTHON=/path/to/python            # the interpreter with requirements.txt installed
quarto preview slides                          # a deck at :4200/unit-01.html, re-rendered on save
tools/build_slides.sh                          # all decks -> _site/slides/
tools/build_slides.sh --pdf                    # ...plus a PDF and a .pptx beside each deck
tools/build_slides.sh --instructor             # with speaker notes -> _instructor-slides/
```

The rendered decks live in `_site/slides/` next to Jekyll's output; `_config.yml` lists
`slides` under `keep_files` so `jekyll build` does not delete them, and excludes `slides/`
so Jekyll never touches the sources. Because that output directory sits outside the Quarto
project, rendering prints `WARN: Refusing to remove directory ... unit-01_files` and a warning
about the path configuration: harmless, but it does mean stale deck assets accumulate there
until `make clean`.

### PDF and PowerPoint export

The `.pptx` is **not** Quarto's `pptx` format. Pandoc's PowerPoint writer drops the `. . .`
pauses (they print as three dots), flattens incremental lists, and ignores the theme and the
slide attributes, so a deck exported that way is not the deck the room saw. Instead, on the same
decktape pass that prints the PDF, `--screenshots` saves every slide as a PNG, and
`tools/pptx_from_screenshots.py` puts them into a 16:9 `.pptx`, one picture per slide with an
empty notes pane. It is pixel-identical to the PDF and the web deck, and its text is not
editable or selectable — it exists so a student can take notes against the slides, not as an
editable copy. `python-pptx` (in `requirements.txt`) does the assembly.

PDF export uses [decktape](https://github.com/astefanutti/decktape) (installed, or via
`npx`); it finds Chrome via `CHROME_PATH`, then `google-chrome`/`chromium` on `PATH`, then a
Playwright-installed Chromium (`pip install playwright && playwright install chromium`).
