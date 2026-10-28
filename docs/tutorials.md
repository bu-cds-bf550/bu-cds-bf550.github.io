---
title: "Tutorials"
permalink: /tutorials/
---

A tutorial covers a tool the problem sets need that no unit introduces, in one lab block, with
instructors and TAs in the room. Each tutorial is a notebook in its own public repository, with
self-checks that report and never grade, and a slide deck for the session it is taught in.
Nothing in a tutorial is submitted or graded; the problem sets and the units after it use what
it shows.

Accept a tutorial's notebook the way you accept a [lab]({{ site.baseurl }}/labs/), with the
tutorial's repository name in place of the unit's:

```bash
gh student accept bu-bioinfo-classrooms bf550-fall-2026 bf550-scikit-learn-tutorial
```

The repository's README says what to install before opening the notebook. Break the notebook
freely: `git checkout <notebook>` puts it back the way it shipped.

Each deck is a web page — arrow keys move between slides, `f` goes full screen, `m` opens a
slide menu — with a PDF beside it for offline reading and a PowerPoint file for taking notes
against the slides (each slide is a picture, with an empty notes pane; the text on it is not
editable).

| Meeting | Tutorial | Notebook | Slides |
|---|---|---|---|
{% for tutorial in site.data.tutorials -%}
| {{ tutorial.date }} | {{ tutorial.title }} | [{{ tutorial.notebook }}]({{ site.labs_org }}/bf550-{{ tutorial.id }}-tutorial/blob/main/{{ tutorial.notebook }}) | [view]({{ site.baseurl }}/tutorials/{{ tutorial.file }}.html) · [PDF]({{ site.baseurl }}/tutorials/{{ tutorial.file }}.pdf) · [PowerPoint]({{ site.baseurl }}/tutorials/{{ tutorial.file }}.pptx) |
{% endfor %}

A tutorial is also listed on the page of the unit whose session it takes, under **In class**.
Decks are authored in the site's [GitHub repository](https://github.com/bu-cds-bf550/bu-cds-bf550.github.io/tree/main/tutorials) and rebuilt on every change.
