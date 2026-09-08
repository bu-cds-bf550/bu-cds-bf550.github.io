---
title: "Lab 1 · Your working environment"
permalink: /labs/unit-01-1/
toc: true
toc_sticky: true
---

**Today:** when you walk out, the course toolchain is yours — VS Code running on the SCC, your
first assignment repository accepted and open, the `bf550` environment producing the same ten
coin flips twice, and Claude open in a window beside it to think out loud with.

Work top to bottom. Every step says what you should see; if you see something else, that is the
moment to wave someone over — not three steps later.

## Before you start

- You can log into [github.com](https://github.com) — create an account now if you never have.
- You have an SCC account through the course. If your login fails at step 1, tell us today.

## The steps

### 1 · VS Code on the SCC

Open BU's [VS Code on the SCC](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-editing/code-server/)
page and follow it to launch a session. You should end in a VS Code window running in your
browser.

Open a terminal in it (Terminal → New Terminal). Type `hostname` and press enter — you should
see a machine name starting with `scc`. You are now working on the cluster, not your laptop.

**NOTE:** On the screen where you submit your VS Code Server job, look for the field labeled
*Additional modules to load* and type in `miniconda`. This is mandatory for selecting the
right kernel later in step 8.

### 2 · Tell git who you are

```bash
git config --global user.name "Your Name"
git config --global user.email "you@bu.edu"
```

No output means it worked — check with `git config --global user.name`, which should echo your
name back.

### 3 · A starter environment, and the GitHub CLI

```bash
module load miniconda
conda create -y -n bf550 -c conda-forge python=3.13 gh
conda activate bf550
```

The create step takes a minute or two. When it finishes, your prompt gains a `(bf550)` prefix,
and `gh --version` prints a version line. This starter environment grows into the full course
environment in step 6.

### 4 · Connect to GitHub

```bash
gh auth login
gh extension install foundation50/gh-student
```

The first command walks you through logging in: choose **GitHub.com**, **HTTPS**, and **Login
with a web browser**, then enter the one-time code it shows you at the address it prints. When
it finishes, `gh auth status` says you are logged in. The second command installs the classroom
tool you will accept and submit every assignment with.

### 5 · Accept your first assignment

```bash
gh student accept bu-bioinfo-classrooms bf550-fall-2026 bf550-ps01
```

This creates your own private copy of Problem Set 1 on GitHub. When `gh student accept`
finishes, it prints the address of your new repository. Clone it and move inside:

```bash
gh repo clone bu-bioinfo-classrooms/bf550-fall-2026-bf550-ps01-YOURUSERNAME
cd bf550-fall-2026-bf550-ps01-YOURUSERNAME
```

`ls` shows `ps01.ipynb`, `ps01-design.md`, `environment.yml`, `pull_request_template.md`, and a
README.

### 6 · The full course environment

```bash
conda env update -n bf550 -f environment.yml
```

This adds everything the course uses — numpy, matplotlib, pytest, and the rest — to the
environment from step 3. Every assignment ships this same file; on the rare occasion it changes,
this same command brings you up to date.

### 7 · Clone the labs, once for the whole term

```bash
cd ~
git clone https://github.com/bu-cds-bf550/bf550-labs.git
```

Every lab after this one is a notebook in there. You clone it once — today — and keep working in
that same copy all term. When we tell you there is something new:

```bash
cd ~/bf550-labs && git pull
```

Your own edits stay where you left them, and a fix we push reaches you on your next pull. Nothing
in the labs is submitted or graded, so break them freely: `git checkout <notebook>` puts one back
the way it shipped.

### 8 · Open the notebook, pick the kernel

In VS Code: File → Open Folder → your `bf550-fall-2026-bf550-ps01-...` folder. Open
`ps01.ipynb`. In the top right of the notebook, choose the kernel: **Select Kernel → Python
Environments → bf550**.

**NOTE:** If you don't see the `bf550` conda environment available when you try to select a
kernel, make sure you added the `miniconda` module in the Additional modules field on the
screen where you launched your VS Code job. See step 1 for more instructions.

Run the first code cell — the setup check. It should print version numbers, ten coin flips, and
end without an error. Run it again: **the same ten flips**. That repeatability is the course's
foundation, and you just verified it.

### 9 · Claude, in a window of its own

Install [Claude Desktop](https://claude.com/download) on your own laptop and sign in with the
course-provided Claude Pro subscription. If you cannot install it — a managed machine, a
Chromebook — open [claude.ai](https://claude.ai) in a second browser tab instead. It is the same
chat, and everything below works the same way.

Now arrange your screen the way you will work all term: **VS Code on the SCC in one window,
Claude in the other** — side by side if your screen is big enough, one keystroke apart if it is
not. You will move between them constantly, and the moving is the point.

Try the round trip once, now. Copy the setup-check cell out of `ps01.ipynb`, paste it into
Claude, and ask it to explain what each line does. Then switch back to VS Code and read the cell
again with that explanation in hand. Code out, explanation back, **your own reading last** — that
is the loop this course is built on, and you will run it hundreds of times.

**Claude Desktop is your tool for AI levels 2 and 3**, which is everything this unit asks of you:
brainstorming and organizing your own thinking (level 2), and drafting that you then evaluate,
revise, and attribute (level 3). Level 4 is different — an agent that edits the files in your
repository directly, which is Claude Code, and we install it on the SCC in the next lab. Every
question states its level, and the level is part of the question.

### 10 · Start the real work

You are set up. For the rest of today, in order:

1. **Warm-ups** — Problem Set 1 (level 3). Ask Claude for anything, freely, in the window you
   just set up.
2. **Friday's reading** — [chapter 1](https://bu-cds-bf550.github.io/bf550-textbook/chapters/ch01-simulating-a-process.html),
   if the warm-ups are done.

## If you finish early

Keep going: the rest of the warm-ups, then Friday's reading. The chapter's practice problems
have worked solutions and are the cheapest way to find out whether the reading landed.

## If you are stuck

Raise a hand — this hour exists so that a stuck step costs you a minute, not an evening. Four
known snags:

- **`conda create` is slow or seems frozen** — the first create downloads packages; give it a
  few minutes. If it fails mentioning disk quota, call us over: home directories on the SCC have
  a size limit and we will move your environment.
- **The `bf550` kernel is not in the list** — the usual cause is a VS Code job launched without
  `miniconda` in *Additional modules to load*; relaunch the job with it (step 1). Otherwise make
  sure step 6 finished without errors, then reload the window (F1 → "Reload Window").
- **A clone asks for a password** — at step 7 it should not, since the labs repo is public: check
  the URL for a typo. At step 5 it means `gh` is not authenticated — run `gh auth status`, and
  `gh auth login` again if it says you are logged out.
- **Claude will not take the course subscription** — sign in with your BU address, and tell us
  today if it still will not; in the meantime [claude.ai](https://claude.ai) in a browser tab
  does everything this unit needs.
