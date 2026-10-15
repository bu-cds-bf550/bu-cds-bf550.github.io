---
title: "Problem Sets"
permalink: /assignments/
toc: true
toc_sticky: true
---

A problem set is **one list of questions on one unit's material.** It opens when the next unit
starts — after you have read the chapter, heard the lectures, and done the labs — and it is due
when the unit after that starts. Ten sets across the term; the
[schedule]({{ site.baseurl }}/schedule/) has every date.

Everything about how a set works — what each question asks, where your code and your answers go,
how the checks report, and what to do before you submit — is in the notebook itself. It is written
to be opened and worked top to bottom without reading anything first. This page is about what a
set is for.

## We do the design; you build and verify

Every set opens with a biological question and **our design of it**: what process produced the
data, what has to be computed, which method and why, and what we will check. Then the questions
build the pieces of that design, one at a time. The data beside the notebook is ours — generated
from the process the design describes, so we know exactly what went into it. That is what lets
every check mean something and every question have an answer.

The productive work is yours: building each piece, reading what your agent produced, running the
checks, saying what the result means, and saying what the checks cannot see.

## Checking your own work

Every code question carries checks. In the early sets we write them; later, the question describes
the cases and you write them. The skill is the same either way, and it is the one students most
underestimate: the code you are handed may be wrong, the code your agent writes may be wrong, and
there is no one to ask — so how do you know?

You check against cases where the answer follows from the *structure* of the situation rather than
from any computation. If the allele frequency is zero, nobody can be a carrier. If a tolerance is
as wide as the whole class, every simulated class counts. And then you check a relationship that
has to hold in between — because two boundaries are not coverage. A simulator with the inheritance
backwards passes both p = 0 and p = 1 and fails only at p = 0.4. Constructing cases like that is
one of the most transferable things in this course, and it is how you will be expected to check
anything, ever, once nobody is grading you.

## AI use

Every question states its [AI level](https://aiassessmentscale.com/), and **the level is a
maximum** — the most AI use we recommend, and a pointer to where your attention belongs. You may
always use less. Code questions are level 3: have the agent draft if you like, then read what it
wrote, run the checks, and say what you kept. The reasoning questions — read our design, read a
piece of code, say what the checks cannot see — are level 1, no AI. The final exam is a code-reading
exam, so those questions are the rehearsal, happening in every set in the ordinary course of the
work. Using AI on them costs you the practice, not the points. The
[assessment page]({{ site.baseurl }}/assessment/) has the levels in full.

Answers in complete sentences. A number with no sentence around it earns no credit — the number is
almost never the point, and in a course where an agent can produce any number you ask for, the
sentence is the only part that shows you understood it.

## Working sessions

**Every class meeting includes working time** — roughly 45 minutes to an hour with instructors and
TAs in the room. The set open during a unit is the one on the *previous* unit's material, so the
questions in front of you are about ideas you have already met, and the room can be used for
getting unstuck rather than for first exposure.

You are not expected to finish a set in class. You are expected to get far enough in, with help
available, that the rest is tractable alone.

## Practicing without spending your grade

Every textbook chapter carries practice problems built the same way, on different content, **with
worked solutions.** Ungraded and optional. If you want more repetitions before the graded set — or
want to check whether the reading landed — that is what they are for.

## If you miss a set

The set stays open with no penalty for a further unit. One missed set costs one set, never more.
