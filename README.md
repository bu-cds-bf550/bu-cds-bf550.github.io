# BF550 — Applied Statistics & Machine Learning for the Life Sciences

### 🌐 Course site → **<https://bu-cds-bf550.github.io/>**

An applied statistics, AI, and machine-learning course for the BU Bioinformatics MS,
anchored by molecular-biology and genomics projects and taught in the age of coding
agents. The course makes a deliberate bet: the primary coding learning objective is
**reading and understanding code (code literacy)**, not authoring it from scratch.

> **Layout.** This repo holds the course site (published via GitHub Pages) plus internal
> planning docs. Student-facing pages live in `docs/` and `_lectures/` and render on the site;
> lecture decks are Quarto sources in [`slides/`](slides/), rendered and PDF/PowerPoint-exported by CI into
> the same site (see [`slides/README.md`](slides/README.md));
> instructor-only rationale and open decisions live in [`internal/`](internal/), excluded from
> the site — see [`internal/open-decisions.md`](internal/open-decisions.md) and the
> [discussion issues](https://github.com/bu-cds-bf550/bu-cds-bf550.github.io/issues).
> `tools/lint_no_instructor_content.py` gates the built site against instructor material
> reaching production, and CI runs it on every push and pull request.
>
> **Working locally.** `make dev` runs the site (live reload, <http://localhost:4000>) and the
> slide decks (live reload, <http://localhost:4200/unit-01.html>) in a Docker replica of the CI
> job; `make site` runs the exact production build. Browse the site at :4000, which serves
> everything including the decks at `/slides/`; :4200 re-renders a deck as you edit it and is
> rooted at the deck directory, so open a deck there by name rather than its index. See the
> [`Makefile`](Makefile) and [`Dockerfile`](Dockerfile).
>
> **AI use:** how these materials were built is documented in
> [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

## At a glance

| | |
|---|---|
| **Credits** | 4 |
| **Contact** | Three 105-minute sessions per unit |
| **Length** | 15 weeks (see the calendar) |
| **Prereq** | Some programming experience (range expected: rudimentary → advanced) |
| **Coding agents** | Provided to students; assumed, allowed, and encouraged |
| **Pedagogical frameworks** | [TILT](https://www.tilthighered.com/resources) (transparent assignments) · [AIAS](https://aiassessmentscale.com/) (AI Assessment Scale) |

## Course documents

- **[How this course works](https://bu-cds-bf550.github.io/about/)** — student-facing
  overview: what you'll learn, the reading-over-authoring focus, and how the pieces fit.
  *(Instructor rationale lives in [`internal/course-design-rationale.md`](internal/course-design-rationale.md).)*
- **[Learning objectives](https://bu-cds-bf550.github.io/learning-objectives/)** — what students will be able to do.
- **[Course home](https://bu-cds-bf550.github.io/)** — the syllabus: course information,
  description, design, assessment weights, materials, and policies.
- **[Schedule](https://bu-cds-bf550.github.io/schedule/)** — the twelve-unit topic progression,
  organized by how each unit's generative process composes from the last, and the Fall 2026 grid:
  every meeting date, deadline, and both exam dates.
- **[Problem sets](https://bu-cds-bf550.github.io/assignments/)** — the unit format: our design of
  the unit's problem, the pieces you build and check, and the reasoning questions in your own
  words.
- **[Assessment & AI policy](https://bu-cds-bf550.github.io/assessment/)** — problem sets, the two
  written exams, grading, and the per-question AIAS mapping.
- **[Textbook](https://bu-cds-bf550.github.io/bf550-textbook/)** — the course's own free, open
  textbook, one chapter per unit, in the [`bf550-textbook`](https://github.com/bu-cds-bf550/bf550-textbook)
  repository.

Course design material is in [`internal/`](internal/): the
[design rationale](internal/course-design-rationale.md), the
[ML topic inventory](internal/ml-topic-inventory.md), the
[practice/assessment review](internal/practice-assessment-alignment.md), and
[open decisions](internal/open-decisions.md).

**Assignments, solutions, authoring guidelines, and anything that would spoil an exercise live in a
separate private repository**, `bu-cds-bf550/bf550-instructor`. Nothing that gives away an answer
belongs in this repo — it is public.

## Planning

Open design questions are tracked as [discussion issues](https://github.com/bu-cds-bf550/bu-cds-bf550.github.io/issues), one per decision. The
unit-by-unit structure itself is settled and lives in [`docs/schedule.md`](docs/schedule.md),
which is authoritative for both topics and dates.
