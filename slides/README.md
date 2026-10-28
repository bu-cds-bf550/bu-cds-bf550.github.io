# Lecture decks

[Quarto revealjs](https://quarto.org/docs/presentations/revealjs/) decks, authored in markdown
with code that executes at render time. **One deck per meeting that has a lecture**, named
`unit-NN-M.qmd` for unit `NN`, session `M` — the shape the labs use. There is a lecture in every
session, so a three-session unit has three decks and three entries in `_data/slides.yml`, each
carrying its `session` and its `date`. Rendered decks are
published at `https://bu-cds-bf550.github.io/slides/<name>.html` with a PDF and a PowerPoint
file beside each one;
the unit pages and [`/slides/`](https://bu-cds-bf550.github.io/slides/) link to them from
[`_data/slides.yml`](../_data/slides.yml). The standalone tutorials' decks are a second Quarto
project of the same shape, [`tutorials/`](../tutorials/), published under `/tutorials/` and
listed in `_data/tutorials.yml`; everything below applies to them too.

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
   The PDF and PowerPoint of a deck whose source, images, theme, and tooling have not changed
   are reused from a cache (`.deck-export-cache/`, persisted between CI runs), so a push that
   touches one deck, or an image only that deck shows, re-exports one deck. A deck's images
   are the `img/` paths written in its source. `make clean` empties the cache locally.

Conventions the decks follow, the first three inherited from the textbook (see its `CONVENTIONS.md`):

- **The deck teaches the material a second way.** The deck and the chapter cover the same
  material by two different routes, and neither is a prerequisite for the other. A student who
  has not finished the chapter, or who reads English slowly, must still be able to follow the
  lecture, so a deck introduces every term it uses, in its own words, before the slide that uses
  it. What a deck does not do is walk the chapter section by section: it works the ideas through
  predicted-then-run code and questions asked in the room, and leaves the worked designs,
  derivations and practice problems to the reading. A lecture runs 45 to 60 minutes, which is
  about 20 to 26 content slides.
- **Seed every random draw**, reusing the chapter's seeds where a chunk comes from the
  chapter, so what is projected in class is exactly what students find in the reading.
- **Slide headings are a public interface.** The instructor run-sheets cite slides by
  heading text, not by number, and name the deck the heading is in. Adding or reordering slides
  is free; renaming a heading, or moving one to another session's deck, means updating that
  unit's run-sheet.

- **Slides follow the instructor's hand-written decks** (`unit-05-2`, `unit-05-3`, `unit-05-3b`
  and the unit 6 decks). Titles are short phrases or short claims that name the slide's subject,
  and never refer to the slide itself. A topic that needs more room continues on a slide with the
  same title plus *(cont.)*. The body is mostly bullets, about 40 visible words a slide; fragments
  are fine when the meaning is clear, an arrow (→) marks a consequence, and a key term is bolded
  where it is defined. Reveals pace the slide. A deck opens on a recap of last time, divides into
  `# Section` slides, introduces a symbol on a *New notation* slide after the room has computed what
  it stands for, and closes on *Next time*. Code is hidden unless the code is the point. Decks
  carry no speaker notes.

### Shadow decks

A deck that renders but is linked nowhere: `unit-NN-M-shadow.qmd`, the instructor's own version of
a session. Every `slides/*.qmd` not starting with `_` is rendered and exported, so a shadow deck
is published at `slides/unit-NN-M-shadow.html` (with its PDF and PowerPoint) and presented from
there, but it has **no entry in `_data/slides.yml`**, so no unit page, schedule row or
[`/slides/`](https://bu-cds-bf550.github.io/slides/) listing links to it. Its front matter adds a
`noindex, nofollow` robots tag. Unlinked is not private: anyone with the URL can open it, and the
content gate and `strip-notes.lua` apply to it as to any deck. The first,
[`unit-05-2-shadow.qmd`](unit-05-2-shadow.qmd), was swapped with the linked deck on 7 Oct 2026:
the instructor's deck is now `unit-05-2.qmd`, and the shadow holds the previous one.

A deck **hidden** until it is authored takes a leading underscore (`_unit-05-3.qmd`), so it is
not rendered at all, and leaves `_data/slides.yml`.

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
