# Course Structure — The Staggered Design/Implement Pipeline (INTERNAL — SUPERSEDED)

> ## ⚠ Superseded, 14 Aug 2026
>
> **This document describes an architecture the course no longer uses** — but see the partial
> reversal below. The staggered design/build pipeline — the strip, the seat names (Implementer /
> Verifier / Reverse engineer), the one-cycle lag, sealed materials, the divergence analysis, two
> problems in flight, and the separate check-in quizzes — was **replaced by weekly simulation-first
> problem sets**, because the accumulated machinery cost more student and instructor attention than
> it returned.
>
> ### The reversal reversed, 3 Sep 2026
>
> The seal and the divergence analysis are retired again, with the design section itself: sets
> are one list of questions on the previous unit's material, built on the instructor's stated
> design (`bf550-instructor` `decisions/simplify-the-course-shape.md`). What survives of this
> document's reasoning is the stagger — a set opens after its unit — and the boundary between
> chapter worlds and set problems. The rest below is history.
>
> ### Partial reversal, 16 Aug 2026
>
> **The seal and the divergence analysis are back**, reinstated inside the weekly format as
> sections 2 and 3 of every problem set. Removing them had left computational thinking with no home
> in the assignments — D1 (frame) and D4 (anticipate) survived in the simulation questions, but D2
> (decompose) and D3 (select) vanished entirely, and three of the five countermeasures against the
> widening-gap risk (§4.3 of [`computational-thinking-basis.md`](computational-thinking-basis.md))
> went with them.
>
> **Still retired, and staying retired:** the strip, the seat names, two problems in flight as a
> *cycle* structure, the separate check-in bank, and all cycle vocabulary. The reinstatement is
> narrow and deliberately cheap — a sealed design section and a divergence prompt, inside a
> conventional numbered problem set.
>
> §3's session budgets below assume the old Design/Build/Share naming and the pre-14-Aug calendar.
> **Both are stale** — re-derive against [`docs/schedule.md`](../docs/schedule.md) before using the
> arithmetic.
>
> **Canonical now:** the published [schedule](../docs/schedule.md) and
> [problem sets page](../docs/assignment-framework.md), plus
> `AUTHORING.md` in the private `bf550-instructor` repo.
>
> **What survives and is still worth reading here:** §6 on scaffolding the design task, §7's
> grading posture (credit for committing on time; being safe to be wrong), §8 on reading carrying
> first exposure at ~2 hr/week, and the session-budget arithmetic in §3.
>
> **Two numbers below are superseded — do not quote them.** §7's weights line
> (30 · 10 · 15 · 15 · 30) predates the published **40 · 10 · 10 · 35 · 5** in
> [`docs/assessment-and-ai-policy.md`](../docs/assessment-and-ai-policy.md). §4.1's
> "41 meetings, 13 cycles" predates the calendar's **39 meetings** (40 until class on Mon Sep 28
> was cancelled). The *posture* in §7 stands;
> the arithmetic does not. The
> [ML topic inventory](ml-topic-inventory.md) and
> [practice/assessment review](practice-assessment-alignment.md) record why the change was made.
>
> Retained unedited below for the reasoning, not as instructions.

> **Internal design document — not published** (`internal/` is excluded in `_config.yml`).
> Formerly the canonical description of how BF550 is structured week to week.
>
> | Companion | Covers |
> |---|---|
> | [`course-design-rationale.md`](course-design-rationale.md) | Why the course makes the code-literacy bet |
> | [`ml-pedagogy-design.md`](ml-pedagogy-design.md) | The probabilistic frame, notation literacy, week-by-week ML reframes |
> | [`future-depth-branches.md`](future-depth-branches.md) | Depth branches — designed, deferred to a future offering |
> | [`textbook-ai-design.md`](textbook-ai-design.md) | The AI-forward textbook and its tutor skill |
> | `assignment-framework-authoring.md` | Rules for writing exercises — **moved to the private `bf550-instructor` repo** |
> | [`computational-thinking-basis.md`](computational-thinking-basis.md) | What we mean by computational thinking; the literature grounding for the four design steps |
> | [`textbook-implementation.md`](textbook-implementation.md) | How the textbook gets built: toolchain, chapter anatomy, CI, co-design workflow |
> | `archive/` | Earlier drafts — **moved to the private `bf550-instructor` repo**, because their planted-defect inventories are answer keys |
>
> **Status:** agreed direction. The front page, schedule, and assessment pages are published;
> remaining student-facing propagation is tracked in §9.

---

## 1. The core mechanism, in one paragraph

**Students design a solution to a biological problem one week, and meet our solution to it the
next.** Week *N* they receive a problem, work out how they would approach it, and commit that.
Week *N+1* our materials for that problem unseal, they analyze where their approach and ours
diverge, and they produce whichever piece of the solution we deliberately left out. Two problems
are in flight at any time, one week apart, and every week has the same shape.

That is the whole structure. Everything below is either a consequence of it or a way of presenting
it.

## 2. Why the stagger, rather than one problem per cycle

Compressing design and implementation into a single cycle forces three goals into conflict:

| Goal | Within one cycle | Staggered |
|---|---|---|
| **Design needs real time** | ~15–30 min at the end of a session | A full cycle, with a supervised clinic |
| **The seal needs to hold** | An intra-cycle commitment gate, unenforceable when a student simply opens the folder | A **cycle boundary** — coarse, natural, one materials release per cycle |
| **The schedule must survive disruption** | Hard cross-session dependency; a lost meeting breaks the cycle | The session stream absorbs a lost meeting — dates shift, sequence does not (§4.1) |

The stagger buys a fourth thing it is not aimed at. **A cycle of separation makes the divergence
analysis better**: students commit a design, then meet ours after a further cycle of instruction.
Same exercise, more honest.

### The one-cycle lag is a feature

Meeting Naive Bayes in a Design session and implementing it two days later is a great deal to ask,
and it crowds the studio. Under the stagger: **taught in cycle *N* → designed with it fresh that
cycle → implemented in cycle *N+1*, after it has settled.** Every studio session applies material that
has had a cycle to consolidate, and the Share session's critique clinic is stronger because students are
breaking a method whose code they wrote two days earlier.

**The schedule must state plainly that the build topic trails the teaching topic by one cycle**, or
it will confuse everyone including the instructor.

## 3. The cycle, in steady state

**Sessions are named by function, not by weekday.** The course meets three times per week, but the
term starts mid-week and holidays fall unevenly, so weekday labels would be wrong on the page and
wrong in students' heads. The three session types are:

| Session | What it is | Problem *N* (designing) | Problem *N−1* (building) |
|---|---|---|---|
| **① Design** | Teach the topic; open the new problem | Reading check-in (5) → teaching (75, interleaved) → **launch design *N*** (10) → wrap (5) | — |
| **② Build** | Studio | *incubating* | **Materials unseal** + read (15) → divergence analysis (30) → produce the missing piece (55) → wrap (5) |
| **③ Share** | Break the model; compare | *(block 2 is the design clinic)* | **Block 1** (~50): generalize + critique clinic · **Block 2** (~50): divergence share-out + design clinic |

A **cycle** is one pass through Design → Build → Share. **Normally a cycle is one calendar week**,
which keeps deadlines weekly and predictable; §4.1 covers short cycles.

**The design deadline is defined by the pipeline, not by a weekday:** design *N* is launched in the
Design session of cycle *N*, worked on across the cycle with a supervised clinic in the Share
session, and **due before the Build session of cycle *N+1***, which is where its materials unseal.
In practice this is a fixed weekly LMS deadline, but stating it against the *Build session* is what
makes the seal survive a shifted or canceled meeting.

### Session budgets

All three fit 105 minutes:

```
① Design   5 check-in + 75 teach/activity + 10 design launch +  5 wrap = 95  (10 slack)
② Build   15 unseal+read + 30 divergence + 55 produce        +  5 wrap = 105
③ Share   50 [generalize + critique clinic] + 50 [share-out + design clinic] + 5 wrap = 105
```

**Share is two blocks, not four activities.** Each block still functions at reduced attendance. The
share-out surfaces divergence findings — "three groups thought the objective was X, the materials
assumed Y; who is right?" — sampled across the room, not exhaustive. The **reading check-in opening
the Design session is telemetry, not assessment** — a short ungraded form whose job is telling the
instructor where to spend the session; the *graded* code-reading check-ins are biweekly and separate.

**The Build session needs no teaching block** — studio work is on the previous cycle's topic,
already taught, so the full session goes to the work. Content delivery lands at **~60 min/cycle
explicit plus ~35 min of content-by-demonstration** in the critique clinic, with the textbook (§8)
carrying first exposure.

## 4. The pipeline calendar

The topic order is organized by the course's own D2 question — **what is unknown?** — in three
acts, with the parallel D4 escalation (*how would you know you're right?*) getting harder each
act: a standard error → held-out data → no ground truth at all.

| Cycle | Act | Topic | Design (this cycle) | Build (previous cycle's) |
|---:|:--:|---|---|---|
| 1 | I | Course intro; reading code | P1 GC content | — (Build session = toolchain setup) |
| 2 | I | Estimation & uncertainty | P2 differential expression | P1 |
| 3 | I | Bayes; probabilities from counts | P3 species of origin | P2 |
| 4 | II | Naive Bayes (generative) | P4 rRNA classification | P3 |
| 5 | II | Evaluation, CV, leakage, calibration | P5 evaluate the classifier | P4 |
| 6 | II | Logistic regression (discriminative pivot) | P6 variant pathogenicity | P5 |
| 7 | II | Linear regression & regularization | P7 dose–response | P6 |
| 8 | II | Consolidation + **midterm** (Design session) | P8 method selection | P7 (**light build**) |
| 9 | III | Trees & forests (the honest outlier) | P9 biomarkers | P8 |
| 10 | III | PCA (t-SNE/UMAP as demo) | P10 matrix structure | P9 |
| 11 | III | Clustering: GMM → k-means, validating *k* | P11 cell types | P10 |
| 12 | III | **Act III exam** (Design session) · frontiers/NN (Share session) | **Synthesis project** | P11 |
| 13 | — | Project studio | — | project |

**Eleven problems, one per cycle; the synthesis project is the twelfth design.** The pipeline drains
*into* the project rather than alongside it — one less problem to author, and the project's
design uses the identical move students have made eleven times.

Sequencing choices that carry weight:

- **Regression sits at week 7, adjacent to logistic regression** — the linear/probabilistic
  family is contiguous, and regularization-as-a-prior closes the week-3 smoothing loop while it
  is fresh.
- **Trees sit at week 9, after the midterm.** The midterm then examines a coherent unit (the
  probabilistic supervised family, estimation → regression) from which trees — the method that
  drops the probability story — was always a category error; and the post-midterm week gets
  fresh, intuitive material exactly when a course otherwise sags. Trees also open Act III
  thematically: the first safety net removed.
- **Clustering is one week** (GMM → k-means as one idea), and **t-SNE/UMAP is a demo** inside
  the PCA week, not a treatment.

### The two exams

Each act closes with a secured, no-AI, code-reading exam. **Midterm, week 8**: Acts I–II.
**Act III exam, cycle 13's Design session**: cycles 9–11 only — frontiers material is exam-exempt.
**Nothing is examined in finals period**; after the Act III exam every remaining session is project
studio. See §4.1 for why the exam sits in cycle 13 rather than 12.

Cycle 12's shape: **Design session** = Act III exam (~75 min) + project design launch (~30) ·
**Build session** = studio, P11 build · **Share session** = frontiers demo + project design clinic.
Cycle 13: all sessions are project studio.

### 4.1 The session stream, holidays, and the Fall 2026 grid

**Cycles are always three sessions. The Design → Build → Share stream never breaks.** When a
holiday removes a meeting, the next meeting takes the next session type — so cycles drift relative
to calendar weeks, and **no session is ever dropped, compressed, or doubled up.** This is why
sessions are named by function: weekday labels would be wrong within two weeks of the term
starting.

Consequences to hold onto:

- **Deadlines are anchored to the stream, not the week.** Design *N* is due before cycle *N+1*'s
  Build session, because that is when its materials unseal. In a normal stretch this lands on a
  fixed weekday, but the *rule* is the session, not the day.
- **Reading is per cycle**, due before its Design session — not "weekly."
- **Nothing needs a contingency plan.** A lost meeting costs a shifted date, not lost content. The
  published calendar is the authoritative mapping and is reissued when it shifts.
- **Slack lives at the end.** Spare sessions beyond the last planned cycle absorb weather and
  closures; if nothing is lost they become extra project studio.

#### Fall 2026: 41 meetings, 13 cycles + 2

Derived from the published BU Fall 2026 calendar — classes begin **Tue Sep 1**, so an MWF section's
first meeting is **Wed Sep 2**; last day of classes **Thu Dec 10**. Holidays removing MWF meetings:
Labor Day (Mon Sep 7) and Indigenous Peoples' Day (Mon Oct 12), each with a **substitute Monday
schedule** on the following Tuesday (Sep 8, Oct 13) that an MWF section *does* meet; plus
Thanksgiving recess (Wed Nov 25, Fri Nov 27).

Net: **41 meetings = 13 full cycles (39) + 2 spare sessions.** Because the substitute Tuesdays
preserve the count exactly, **cycles 1–12 all run Wed → Fri → Mon**; Thanksgiving shifts the phase
once, and **cycles 13–14 run Mon → Wed → Fri**. That single phase shift is the only irregularity.

Student-facing grid: [`docs/schedule.md`](../docs/schedule.md) (`/schedule/`).

> **Unverified, flag before publishing:** `www.bu.edu` is unreachable from the authoring
> environment, so these dates come from secondary sources. Two specifics need checking against the
> registrar: whether classes meet on **Veterans Day (Wed Nov 11)**, and the **study period** dates.
> If Nov 11 turns out to be a holiday, the stream simply shifts by one session — which is the
> design working as intended, not a problem.

#### Exam placement in the Fall 2026 grid

- **Midterm: cycle 8's Design session, Wed Oct 21.** Closes Acts I–II as designed.
- **Act III exam: cycle 13's Design session, Mon Nov 30** — *not* cycle 12's, which the earlier
  plan implied. At cycle 12's Design session (Wed Nov 18) students have neither built nor
  critiqued clustering: P11's materials unseal Fri Nov 20 and its critique clinic is Mon Nov 23.
  Examining Act III's headline lesson before its deepest treatment would be a real flaw. Moving to
  Nov 30 puts the exam after all Act III material, gives Thanksgiving recess as study time, and
  still leaves **four sessions of pure project studio** (Dec 2, 4, 7, 9) — preserving the intent
  that the end of term belongs to the project.
- **Frontiers/neural nets moves to cycle 12's Design session** (Wed Nov 18), which is where it
  belongs anyway: light, exam-exempt, and it makes cycle 12 a normal teaching cycle.
- **The project design is due Wed Dec 2**, not before the exam, so students are not doing project
  design and exam study over the same recess.

## 5. What the student actually has to learn

One thing:

1. **Every problem gets designed one week and built the next.**

Everything else is a *view* of it. The strip, the seat names, the file bundle, and the
model card are four descriptions of a single fact — *which piece is yours this week* — and must be
taught as one thing. Presenting them as four systems is the main way this structure becomes hard to
follow.

**One canonical representation: the strip.** Everything else derives from it.

```
Week N        DESIGN      SPEC      TESTS      CODE
             ★ YOURS    ▨ sealed  ▨ sealed   ▨ sealed

Week N+1      DESIGN      SPEC      TESTS      CODE
            (committed)   given     given    ★ YOURS
```

- The **file bundle** mirrors the strip, one file per box.
- The **seat name** is a label for the starred box — *Implementer* (code), *Verifier* (tests),
  *Reverse engineer* (spec). Good names, memorable, but **not a rotation students must track.**
  Which piece is withheld varies for authoring reasons; the strip already says which.
- The **model card** is what goes in the DESIGN box. Strictly, the DESIGN box always holds the
  four-slot D1–D4 worksheet (§6); it earns the name *model card* from around week 3, once there is
  something to estimate. Weeks 1–2 are computations rather than models, so the "what's unknown" slot
  comes out near-empty — deliberately, since that emptiness is what sets up the count-versus-estimate
  distinction. See `ml-pedagogy-design.md` §5.

### The bundle

| File | Contents | When |
|---|---|---|
| `design.md` | The design | Cycle *N*, committed before cycle *N+1*'s Build session |
| `spec.md`, `test_*.py`, `impl.py` | The four artifacts — given or authored per the strip | Week *N+1* |
| `notes.md` | Divergence analysis, the reflective product for the starred box, and the process record (failures and what they taught) | Week *N+1* |

One design file, the starred artifact, one reflective file. There is no separate log.

**Depth branches are deferred to a future offering** — the full design is preserved in
[`future-depth-branches.md`](future-depth-branches.md). Year one's differentiation story: the
design stage and the divergence analysis have no ceiling, and the textbook's ungraded practice
problems provide unstructured depth.

**"Model card" is internal vocabulary only.** Students see `design.md` and the four questions;
the term never appears in student-facing material. The end-of-term "stack" survives as
*compile your designs* — the on-ramp to the synthesis project.

## 6. Scaffolding the design task

A week of time does not solve the blank page; it relocates it. Five scaffolds, cheapest first — the
textbook (§8) makes the best one nearly free.

1. **A fully worked design in the textbook every week, for an *analogous* problem** — not the one
   being designed. The highest-value scaffold available: students see what "done" looks like before
   attempting it, which is what most reliably prevents freezing.
2. **Progressive prompt removal.** Weeks 1–3: sub-prompts under every step. Weeks 4–8: step names
   only. Weeks 9+: the problem and the model card. **Publish the removal schedule up front**, so it
   reads as growth rather than as the handouts degrading.
3. **The Share session's design clinic with peer read-through.** Pairs swap drafts and ask questions — not
   critique, just *"what would your output actually look like?"* Catches the most common failure
   (answering a different question than the one asked) while the instructor is in the room.
4. **A pre-commit self-check.** Four or five questions: have I said what the output is? what would
   count as wrong? what did I have to decide that the problem did not decide for me?
5. **Anonymized prior-year designs, including weak ones, discussed openly.** Available from year
   two. Nothing normalizes "being wrong in week *N* is fine" faster.

### The design steps

Four steps, the same every week. They are also the four slots of the model card
(`ml-pedagogy-design.md` §4), so exposition and design share one template. Grounding in the
computational-thinking literature, and where we depart from it, is in
[`computational-thinking-basis.md`](computational-thinking-basis.md).

| Step | Prompt | Model-card slot |
|---|---|---|
| **D1 · Frame** | What process produced this data? | The story |
| **D2 · Decompose** | What has to be computed or estimated? | What's unknown |
| **D3 · Select** | *Early:* what would the right method need to do? *Later:* which method, and why that one? | How we pin them down |
| **D4 · Anticipate** | How could the answer be wrong — and how would you know? | How it fails |

The D3 two-stage framing exists because **method selection is degenerate when the toolbox holds one
item.** "What properties would it need?" is answerable with an empty toolbox and matures into real
selection as the menu fills.

## 7. Grading posture

**Weights (SUPERSEDED — see the banner; published weights are 40 · 10 · 10 · 35 · 5): weekly problems 30 · check-ins 10 · midterm 15 · Act III exam 15 · synthesis
project 30 · participation 5.** Two secured exams, one per act boundary; the project stays at
30% so the incentive structure and the course's stated philosophy agree. (Supersedes the
weights in issue #2, which predate the Act III exam.)

| | |
|---|---|
| **Design (week *N*)** | Credit for committing on time. **Not graded on quality** — stated on every assignment, because being safe to be wrong is what makes the task usable by students with the least background. |
| **Divergence analysis** | Graded in depth on the ~6 heavy problems (see authoring doc), rubric-checked otherwise. |
| **The starred artifact** | Per the seat: hand-calculated test values, or a reimplementable spec plus gap analysis, or annotated code plus the account of what the agent decided. |
| **Exams** | Midterm (wk 8, Acts I–II) and Act III exam (wk 12 Mon, wks 9–11), both no-AI code reading, 15% each. |
| **Re-entry rule** | A missed design converts to a *hindsight critique* — different prompt, same credit, no pretense the seal held. One missed week costs one week, never more. Published to students. |

Grading is TA-staffed (~20 hr/week per TA), with agentic grading assistance under
consideration — if adopted, it needs its own policy note before the term.

AI levels differ by stage — **design at AIAS 2, week *N+1* work at AIAS 4** (open: see §9). The
split is the cleanest statement of the course's ethos: *think first, unaided; then use the agent
freely.*

**The Share session's share-out supplies social stakes** so the ungraded designs do not decay into
box-ticking: three groups thought the objective was X, the materials assumed Y — who is right?

## 8. Reading carries first exposure

The format is flipped, deliberately. The Design session's 75 minutes are **activation and elaboration of
material already read**, not first delivery.

- **Budget ~2 hr/week**: one textbook chapter plus one short worked notebook.
- **Accountability is the reading check-in opening each Design session** — deliberately low-stakes; its real job is
  telling the instructor live which part of the reading did not land, so the 75 minutes can be spent
  there.
- **This is what makes the structure robust to disruption.** A student who misses a session recovers
  from the textbook rather than from a classmate's notes. That was the original brittleness concern
  and the textbook is the answer to it.

The textbook is therefore not a supplement — it is load-bearing infrastructure. Its design,
including the tutor-skill layer, is in [`textbook-ai-design.md`](textbook-ai-design.md).

> **The textbook contains no graded assignments, by design.** It holds explanation, worked examples,
> and ungraded **practice problems**; the weekly design problems and lab materials are released
> separately. This separation is what lets the textbook be fully open to a student's AI tutor
> without exposing any graded work — see `textbook-ai-design.md` §1. Keeping it clean is a standing
> authoring constraint, not an incidental fact: **a lab problem that migrates into the textbook
> breaks the tutor's safety property.**

## 9. Open and pending

**Deferred forks** (also in [`open-decisions.md`](open-decisions.md)):

1. **Decomposition stopping rule** — D2 needs a rule students can apply for how far down to go.
   Candidate: *down to the point where each component is a question you could look up a method for.*
   ([`computational-thinking-basis.md`](computational-thinking-basis.md) §8)
2. **How Bayesian?** Leaning: McElreath's pedagogy and generative framing, not his inference
   machinery. Grid approximation for genuine-posterior cases; full Bayes as optional enrichment.
3. **How much productive uncertainty per problem**, and per-problem disclosure (policy disclosure
   at term start is settled).
4. **Two problems in flight** is the stagger's real cost. Fallback if load proves too high: design
   every *other* week, at the price of the clean steady state.
5. **Synthesis project format at 50–60 students** — traditional presentations do not fit;
   candidate formats in `open-decisions.md`.

Settled since earlier drafts of this list: design stage is **AIAS 2**; simulation front-loads
cycles 2–4 + Share-session diagnostic; clustering is one cycle and t-SNE/UMAP a demo (both baked into the
§4 calendar).

**Pending propagation to student-facing pages** — none of this has been written up for students:

| What | Where |
|---|---|
| ~~Front page~~ · ~~schedule~~ · ~~assessment policy~~ | `index.md`, `docs/schedule.md`, `docs/assessment-and-ai-policy.md` | **Done** — rhythm, acts calendar, weights, exams, re-entry rule, per-stage AI levels all published |
| Contact format + rhythm on the remaining pages | `README.md`, `docs/course-design.md` | Still say 2 × 75 + lab and "weekly labs" |
| The **strip**; letters A–D retired; the bundle | `docs/assignment-framework.md`, `_labs/` | Full rewrite needed |
| `_lectures/week-*.md` topics | all 13 files | Still ordered by the old sequence |
| **Reading carries first exposure** at ~2 hr/week, stated to students | `docs/course-design.md` | |
| **v2 example problems** — port verified statements + planted-uncertainty inventories forward (sources now in the private `bf550-instructor` repo) | the private `bf550-instructor` repo | |
