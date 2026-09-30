---
title: "How This Course Works"
permalink: /about/
toc: true
toc_sticky: true
---

BF550 is an applied statistics and machine-learning course for life scientists. The goal is
to build your **intuition for how machine-learning methods work and when to use them**, and
to apply that intuition to real molecular-biology and genomics problems. This page explains
how the course is structured and what to expect.

## What you'll learn

You'll come away able to:

- Recognize the major **classes of machine-learning algorithms** — supervised vs.
  unsupervised, classification, clustering, feature-importance and tree-based methods,
  dimensionality reduction — and understand how they differ.
- **Choose the right method** for a given biological question and dataset, and explain why.
- **Read and understand code**: say precisely what a piece of code does, recover the idea
  behind it, and judge whether it's well designed for the problem.
- **Work effectively with AI coding agents** — break a problem down, direct an agent to
  build a solution, and verify that the result actually does what you intended.

The emphasis throughout is on *judgment*: framing the problem, picking the method, and
checking the answer.

## Reading code is the focus

You come into this program from many different starting points — some of you have written a
lot of code, some very little. **This course focuses on reading and understanding code, not
on writing it from scratch**, so wherever you start, you'll be building the same core skill:
*code literacy*.

Code literacy is more than syntax. It means being able to:

- read a snippet and explain exactly what it does, including the tricky edge cases;
- look at code plus its tests and reconstruct the specification it was built to meet;
- see how a program is organized to solve a problem, and where its complexity and risk live;
- tell whether a piece of code — yours, a classmate's, a random snippet you
  found on the internet, or an AI's — actually works as intended.

These are the skills that make you effective with any codebase, and they're exactly the
skills you need to use AI coding tools well.

## Using AI coding agents

You'll be **provided with coding-agent tools, and you're encouraged to use them.** This
course is built around them rather than against them.

The work you turn in is structured so that the agent handles what it's good at (generating
code) while *you* do the thinking that matters: framing the problem, deciding what has to be
computed, choosing an approach, and anticipating how the answer could be wrong. In practice that
means **committing to an approach before you generate anything, then checking the result
against a case whose answer you already know for reasons that have nothing to do with the
code.**

This course uses an adapted version of the [AI Assessment Scale
(AIAS)](https://aiassessmentscale.com/). This scale is a number from 1 to 5
with clearly defined criteria about how AI tools may be used, and how much AI
generated content may be included in your assignment responses. Each assignment
tells you exactly what level of AI use is expected (see [AI
levels](#two-things-youll-see-on-every-assignment) below), so there's never any
ambiguity about what's allowed.


| Level | Name | What it means |
|------:|------|---------------|
| 1 | No AI | Work on your own (e.g. the three reasoning questions in every problem set, and both exams). |
| 2 | AI Planning | AI for brainstorming/outlining; you develop the ideas yourself. |
| 3 | AI Collaboration | AI helps draft; you critically evaluate and revise its output. |
| 4 | Full AI | Use the agent throughout; you direct it, verify it, and own the result. |
| 5 | AI Exploration | Open-ended, creative use. |

Every level is a **maximum** — the most AI use we recommend, and where your attention belongs.
Code questions in the problem sets are **Level 3**: the agent may draft; you read, test, and say
what you kept. The project is **Level 4**. The three reasoning questions in every problem set, the
midterm, and the Act III exam are **Level 1**, so you and we can both see your unaided reading
skills grow over the term.

## Why this course is built the way it is

Two things are true at once. Machine learning has become the working language of modern
biology — and AI can now write competent code from a plain-English description. Some courses
respond to that second fact by banning AI. We do the opposite: **we assume it, provide it, and
build the course around the skills it cannot do for you.**

Here is what an AI cannot do for you. It cannot decide what question your data can actually
answer. It cannot decide what "correct" means for a problem you care about. It cannot tell you
whether the confident-looking answer it just produced is wrong. Those three skills — framing a
problem, defining correctness, and catching failure — are what this course teaches, using
machine learning on real biological data as the material.

You will read far more code than you write. That is deliberate. You come into this program with
wildly different programming backgrounds, and we are not going to pretend otherwise. Reading
code — saying precisely what it does, recovering what it was *meant* to do, judging whether it
should be trusted — is a skill almost none of you have practiced, regardless of background. It
levels the field, and in the age of AI-generated code, it is *the* skill.

The same goes for math. Some of you have a lot; some very little. Every idea in this course
arrives in the same order: first as a **story** about how data comes to exist, then as **code**
you can run and poke, and only then as **notation** — the formula, presented as a compressed
summary of something you have already played with. If you can read Python, you can learn to
read math. Formulas are never the entrance fee here; they are the souvenir.

## The rhythm

One topic per unit, ten problem sets across the term, three 105-minute meetings. The unit's topic opens in the
first meeting; the rest are working sessions with instructors and TAs in the room.

**You build the data before you analyze it.** Nearly every set starts by asking you to write a
*simulator*: code that produces a dataset from settings you choose. Then you analyze what came out
and see whether you can recover the settings you put in.

That one habit does a surprising amount of work. It is how scientists actually find out whether a
method can be trusted — you cannot validate anything against real data, because with real data
nobody knows the right answer. It is also why this course does not need an answer key: **you know
the truth, because you set it.**

And it means the mathematics arrives in a bearable order. You will meet sampling variability as
three histograms getting narrower, not as a formula. You will meet a p-value as *how often the
simulation is at least as extreme*, not as an integral. You will discover overdispersion because
your own data turns out messier than your own model predicted. The formulas show up later, as
compressed summaries of things you have already watched happen.

**Each unit composes.** Once you can build one process, you repeat it, mix two of them, nest one
inside another, or let its settings depend on something you measured. Those four operations —
repeat, nest, mix, condition — generate nearly every model in the first two acts. The third act
asks the harder question, *what if the thing you care about was never measured at all?*, and one
unit drops the probability story altogether to show you what that costs. Either way there is no
separate "how this course works" to learn on top of the statistics. The organizing principle *is*
the statistics.

Topics and the three-act arc are on the [schedule]({{ site.baseurl }}/schedule/), along with every
meeting date and deadline. The course has its own
free, open textbook — [*Biological Data Analysis, Simulation First*](https://bu-cds-bf550.github.io/bf550-textbook/) — written around this
approach; one chapter per unit is the reading, and you can start reading it right now.

## Using AI

You'll have a provided coding agent and a tutor for the [textbook](https://bu-cds-bf550.github.io/bf550-textbook/), and **every individual question** states
its [AI level](https://aiassessmentscale.com/) — not every assignment, every question:

- **Writing the code — level 3, the agent may draft.** Describe the piece in words, let the agent
  write it, then read what it wrote, run the checks, and say what you kept. Reading and testing are
  the thinking; typing is not.
- **Reading our design, reading code, and saying what the checks cannot see — no AI.** Three
  questions in every set. These are the skills that quietly disappear if you delegate them, and
  they are exactly what the exams assess.
- **The two exams — no AI.** A midterm (Mon Nov 9) and an Act III exam (Fri Dec 4), closed-book, both
  code-reading.

The no-AI questions exist for your benefit as much as ours. Research on novices using AI finds that
the students who struggle most are often the ones most convinced they're doing fine. Two unaided
questions in every set are how you and we both watch your own skill actually growing — so nobody
discovers a gap for the first time during an exam.

## What you hand in, and what it's worth

One notebook per set: your code, your figures, and your answers in complete sentences.

| | Weight | AI level |
|---|---:|---|
| Problem sets (10) | 40% | Stated per question — two are no-AI in every set |
| Written midterm (Mon Nov 9) | 10% | None |
| Act III exam (Fri Dec 4) | 10% | None |
| Synthesis project | 35% | Full |
| Participation | 5% | — |

The synthesis project is the course in miniature and the culminating assessment — **there is no
exam during finals period**. You design a generative process for a biological question you care
about, then show what a method can and cannot recover from it. By then you'll have done exactly
that ten times; the difference is that this time you choose the question.

**If you miss a unit** — it happens — the problem set stays open with no penalty until the
end of the next unit, and the questions that depend on earlier units always come with a reference
implementation so a bad unit never blocks a good one. Ask early.
