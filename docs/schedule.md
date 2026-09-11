---
title: "Schedule"
permalink: /schedule/
toc: true
toc_sticky: true
---

## The arc: what is unknown?

Three acts, organized by one escalating question — *what is unknown, and how would you know your
answer is right?*

- **Act I — the unknown is a number** (units 1–3). Build a process, estimate what went into it, put
  an honest error bar on it, and find out why real data is messier than your first model.
  *Knowing you're right:* you set the truth yourself.
- **Act II — the unknown is an answer you have examples of** (units 4–9). Supervised learning:
  generative models, evaluation, then models that condition on what you measured.
  *Knowing you're right:* held-out data. Closes with the midterm.
- **Act III — nobody gives you the answer** (units 10–12). Prediction with no generative story, then
  structure with no labels at all. *Knowing you're right:* there is no ground truth — stability,
  internal validation, and skepticism are all you have. Closes with the Act III exam, after which
  the term belongs to your synthesis project.

## Fall 2026

The term is **40 class meetings**, and a **unit** is three of them — the sessions that carry one
problem set. A unit is not a calendar week. The term opens on a Wednesday and the holidays fall
unevenly, so after unit 1 a unit runs **Friday → Monday → Wednesday**: the topic and the new
problem open on Friday, you have the weekend with them, and Monday and Wednesday are working
sessions. No session is ever dropped — a holiday bends a unit rather than shortening it.

**A problem set covers one unit's material and is assigned at the next unit's first session** —
after the chapter, the lectures, and the labs — **and is due at the first session of the unit after
that**, the same session the following set is handed out. So the set open during a unit is on the
*previous* unit's ideas: you build things after they have had time to settle rather than on the day
you were introduced to them.

The **Problem set** column below reads *due / assigned* for that unit's first session. All three of
a unit's sessions carry working time on the set assigned in the first of them, so you have the
room, the instructors and the TAs for the whole of a set's life.

**Two units assign nothing — units 9 and 12.** That is deliberate: it means no problem set is ever
open while you are preparing for an exam. The midterm is Fri Nov 6, at the start of unit 10; the
Act III exam is Wed Dec 2, at the start of unit 13. It is also why there are **ten problem sets
across thirteen units** rather than one per unit.

Each unit number links to that unit's page, which carries the slides and the labs for its
meetings as they are posted — the material we work through in class, yours to finish at your own
pace afterwards.

| Unit | Sessions | Topic | Problem set Due/Assigned |
|---:|---|---|---|
| [**1**]({{ site.baseurl }}/units/unit-01/) | Wed **Sep 2** · Fri **Sep 4** · Wed **Sep 9** | Course intro and setup; simulating a process; binomial counts | NA / **PS1**  |
| [**2**]({{ site.baseurl }}/units/unit-02/) | Fri **Sep 11** · Mon **Sep 14** · Wed **Sep 16** | Null distributions; what a p-value is; multiple testing | NA / **PS2** |
| [**3**]({{ site.baseurl }}/units/unit-03/) | Fri **Sep 18** · Mon **Sep 21** · Wed **Sep 23** | Nesting; overdispersion; why counts vary more than they should | **PS2** / **PS3** |
| [**4**]({{ site.baseurl }}/units/unit-04/) | Fri **Sep 25** · Mon **Sep 28** · Wed **Sep 30** | Bayes' theorem; estimating probabilities from counts | **PS3** / **PS4** |
| [**5**]({{ site.baseurl }}/units/unit-05/) | Fri **Oct 2** · Mon **Oct 5** · Wed **Oct 7** | Naive Bayes: classification as a generative story | **PS4** / **PS5** |
| [**6**]({{ site.baseurl }}/units/unit-06/) | Fri **Oct 9** · Tue **Oct 13** · Wed **Oct 14** | Evaluation: overfitting, cross-validation, leakage, calibration | **PS5** / **PS6** |
| [**7**]({{ site.baseurl }}/units/unit-07/) | Fri **Oct 16** · Mon **Oct 19** · Wed **Oct 21** | Logistic regression: modeling the boundary directly | **PS6** / **PS7** |
| [**8**]({{ site.baseurl }}/units/unit-08/) | Fri **Oct 23** · Mon **Oct 26** · Wed **Oct 28** | Linear regression and regularization | **PS7** / **PS8** |
| [**9**]({{ site.baseurl }}/units/unit-09/) | Fri **Oct 30** · Mon **Nov 2** · Wed **Nov 4** | Generalized linear models: Poisson and negative binomial regression | **PS8** / NA |
| [**10**]({{ site.baseurl }}/units/unit-10/) | Fri **Nov 6** · Mon **Nov 9** · Wed **Nov 11** | **MIDTERM Fri Nov 6** (no AI, closed book — Acts I & II), then trees, forests, and boosting | NA / **PS9** |
| [**11**]({{ site.baseurl }}/units/unit-11/) | Fri **Nov 13** · Mon **Nov 16** · Wed **Nov 18** | Dimensionality reduction: PCA (t-SNE/UMAP demo) | **PS9** / **PS10** |
| [**12**]({{ site.baseurl }}/units/unit-12/) | Fri **Nov 20** · Mon **Nov 23** · Mon **Nov 30** | Clustering: mixture models → k-means; validating *k* | **PS10** / NA |
| [**13**]({{ site.baseurl }}/units/unit-13/) | Wed **Dec 2** · Fri **Dec 4** · Mon **Dec 7** · Wed **Dec 9** | **ACT III EXAM Wed Dec 2** (no AI, closed book — units 10–12), then the project launches and the rest is studio | — *the project* |

**Unit 13 is the project unit** and has four sessions rather than three — it carries the term's
last meeting, Wed Dec 9, and assigns no problem set. **PS10, due Fri Nov 20, is the last one.**

### Holidays, recesses, and the two odd days

| | |
|---|---|
| Mon **Sep 7** | Labor Day — no class. Falls inside unit 1, between Sep 4 and Sep 9 |
| Mon **Oct 12** | Indigenous Peoples' Day — no class. BU substitutes a Monday schedule on **Tue Oct 13**, which is unit 6's second session. It is the only substitute day of the term; Labor Day is not made up |
| Wed **Nov 25** – Sun **Nov 29** | Thanksgiving recess — no class. Falls inside unit 12, between Mon Nov 23 and Mon Nov 30. Unit 12 assigns no set, so the recess lands in a stretch with nothing due |
| Thu **Dec 10** | Last day of classes. We do not meet Thursdays, so **Wed Dec 9** is our last meeting |
| **Dec 11–13** · **Dec 14–18** | Study period · final exams period — **no exam for this course** |

**Wed Nov 11 is a class day.** Veterans Day is not a BU holiday in Fall 2026.

## Exams

| | When | Covers | Format |
|---|---|---|---|
| **Midterm** | Fri Nov 6 | Units 1–9 — simulating processes through generalized linear models | Closed book, no AI, code reading |
| **Act III exam** | Wed Dec 2 | Units 10–12 — trees, PCA, clustering | Closed book, no AI, code reading |

Each takes the first part of its session; the rest of that session belongs to what comes next —
trees after the midterm, the project launch after the Act III exam.

**There is no exam during finals period.** After Dec 2, every remaining session is project studio.

## The synthesis project

The course in miniature, and the culminating assessment: design a generative process for a
biological question you care about, then show what a method can and cannot recover from it. The same
thing you will have done ten times by then, on a problem you chose.

| | When |
|---|---|
| **Launch** | Wed Dec 2, after the Act III exam |
| **Studio** — instructors and TAs in the room | Fri Dec 4 · Mon Dec 7 · Wed Dec 9 |
| **Proposal** | Mon Dec 7 |
| **Project bundle** | during the finals period, Dec 14–18 |
