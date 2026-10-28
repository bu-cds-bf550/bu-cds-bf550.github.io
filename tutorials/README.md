# Tutorial decks

The decks for the standalone tutorials, one per tutorial, named `<slug>.qmd` for the tutorial
whose notebook repository is `bf550-<slug>-tutorial`. A tutorial covers a tool the problem sets
need that no unit introduces, in one lab block, outside the unit structure; its notebook ships
from the instructor repository to its own public template repository, and its deck lives here.
Rendered decks are published at `https://bu-cds-bf550.github.io/tutorials/<slug>.html` with a
PDF and a PowerPoint file beside each one; [`/tutorials/`](https://bu-cds-bf550.github.io/tutorials/)
and the unit pages link to them from [`_data/tutorials.yml`](../_data/tutorials.yml).

This directory is a second Quarto project beside [`slides/`](../slides/), with the same
configuration: [`_quarto.yml`](_quarto.yml) points at `slides/theme/bf550.scss` and
`slides/strip-notes.lua` by relative path, so a tutorial deck looks like a lecture deck and
follows every convention in [`slides/README.md`](../slides/README.md). A deck's file name must
not repeat one in `slides/`: the PDF export cache keys both sets by file name.

## Adding a tutorial deck

1. Write `tutorials/<slug>.qmd`, in the style of the lecture decks (start from
   [`slides/_template.qmd`](../slides/_template.qmd)).
2. Add an entry to `_data/tutorials.yml` — `id`, `notebook`, `unit`, `date`, `title`, `file`.
   That entry adds the row on `/tutorials/`; the unit named carries the tutorial under
   **In class** if its page has an `{% include tutorial-links.html unit="unit-NN" %}` line.
3. Push. CI renders the deck with the lecture decks, exports the PDF and the PowerPoint, gates
   the site, and deploys.

## Rendering locally

`make site` runs the whole production build, tutorials included. For a live preview of a deck
you are editing, from the repository root inside the container (`make shell`) or on a host with
Quarto installed:

```bash
quarto preview tutorials --no-browser --host 0.0.0.0 --port 4201
```

and open `http://localhost:4201/<slug>.html`. (`make dev` watches `slides/` only.)
