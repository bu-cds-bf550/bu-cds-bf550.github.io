---
title: "Assessment & AI Policy"
permalink: /assessment/
toc: true
toc_sticky: true
---

Your grade in BF550 reflects the two things the course is really about: **statistical and
machine-learning judgment**, and **code literacy**. It does not reward typing code from
memory. Because you're encouraged to use coding agents, every assessment is labeled with a
clear AI-use level so you always know what's expected.

## What you'll be graded on

The synthesis project is the course's culminating assessment, and **there is no exam during
finals period** — the term closes with the project.

| Component | What it measures | AI level | Weight |
|---|---|:--:|--:|
| Problem sets (10) | problem framing + applied ML + code literacy + agent use | per question | 40% |
| Written midterm — Mon Nov 9 (code reading) | Acts I–II, under exam conditions | 1 | 10% |
| Act III exam — Fri Dec 4 (code reading) | units 10–12, under exam conditions | 1 | 10% |
| Synthesis project | end-to-end judgment on a problem you chose | 4 | 35% |
| Participation | engagement in working sessions | — | 5% |

### Problem sets

Ten across the term. A set covers one unit's material and is assigned at the start of the *next*
unit — after the chapter, the lectures, and the labs — and due at the start of the unit after
that. Units 9 and 12 assign nothing, so no set is open while you prepare for an exam. A set opens
with the problem and our design of it; the questions build that design's pieces against data we
generated, so every question has an answer and every code question carries checks. The
[problem sets page]({{ site.baseurl }}/assignments/) explains the format; the
[schedule]({{ site.baseurl }}/schedule/) lists every deadline.

**Checking your own work is a graded skill here, not an afterthought.** In sets 2–4 the checks
are ours; from set 5 the question describes the cases in prose and you write the checks. Every
expected value carries the line that derives it, and a check whose value was read off a run is not
a check.

If you miss a unit, the set stays open with no penalty for a further unit.

### The no-AI questions

**Three questions in every problem set are AI level 1.** One asks you to read our design and say
which piece is the answer and what to expect before you run; one asks you to read code and say
precisely what it does and where it fails; one asks how every check could pass and the answer still
be wrong. They are not a hurdle bolted onto the course — both exams are code-reading exams, so
these questions are the rehearsal, happening in every set in the ordinary course of the work. By
the midterm you'll have done more than twenty of them.

Watch your own trajectory on them. It's the most honest signal you'll get about whether your unaided
skills are growing alongside your agent-assisted work.

### The two exams

Each act of the course closes with a **closed-book, no-AI code-reading exam (level 1)**: read
provided snippets, describe their behavior, recover their intent, spot edge cases and bugs —
the same skill every set's no-AI questions rehearse, assessed all at once.

- **Midterm — Mon Nov 9:** Acts I and II — simulating processes, estimation, Bayes, evaluation, and
  regression through generalized linear models.
- **Act III exam — Fri Dec 4:** units 10–12 — trees and forests, dimensionality reduction, and
  clustering.

### Synthesis project

The capstone and the course's **culminating assessment**: design a generative process for a
biological question you care about, then show what a method can and cannot recover from it — with
every decision justified mathematically or biologically. It is the same thing you will have done
ten times by then, on a question you chose. Unit 13 is project studio end to end. It's
**AI level 4** — use the agent freely; your design, your checks, and your critique are what's graded.

## AI use levels

This course uses the [AI Assessment Scale (AIAS)](https://aiassessmentscale.com/). Each
assignment names a level so the expectations are explicit:

| Level | Name | What it means for you |
|------:|------|---|
| 1 | No AI | Work on your own — the three reasoning questions in every problem set, and both exams. |
| 2 | AI Planning | Use AI to brainstorm or outline; develop the ideas yourself. |
| 3 | AI Collaboration | AI helps draft; you critically evaluate and revise its output. |
| 4 | Full AI | Use the agent throughout; you direct it, verify it, and own the result. |
| 5 | AI Exploration | Open-ended, creative use. |

**Levels are set per question, not per assignment, and every level is a maximum** — the most AI
use we recommend, and a pointer to where your attention belongs. Code questions are level 3: the
agent may draft; you read it, test it, and say what you kept. The project is level 4. What's graded
is your checks, your interpretation, and your critique — the parts an agent can't produce for you.

## Academic integrity in an AI-positive course

- Using a coding agent up to a question's stated level is **expected** — it's not a violation.
- What *is* a problem is presenting an agent's work as understanding you don't have: an
  annotation that doesn't match the code, "hand-calculated" test values you didn't actually
  work out, or a critique that misreads the implementation. These show up naturally, because
  the deliverables require you to demonstrate that you understand.
- The level-1 questions and the exams give an AI-free picture of your own code literacy alongside
  your agent-assisted work.
