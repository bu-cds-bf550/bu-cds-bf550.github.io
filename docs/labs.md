---
title: "Labs"
permalink: /labs/
toc: true
toc_sticky: true
---

Every class meeting has a lab: the material you work through during working time, with instructors
and TAs in the room. Work at your own pace, and finish one after class if you do not get all the
way through.

The first lab is a page on this site. It sets up your toolchain and walks you through your first
`gh student accept`. **Every lab after it is a Jupyter notebook in its unit's public lab
repository**, `bf550-unitNN-labs`, one repository per unit. At a unit's first meeting you accept
that unit's labs the same way you accept a problem set and clone your own copy:

```bash
gh student accept bu-bioinfo-classrooms bf550-fall-2026 bf550-unit03-labs
```

with the unit's number in place of `03`. Break these notebooks freely: changing a line to see what
happens is the point of them, and `git checkout <notebook>` puts one back the way it shipped.

*Until 14 Sep 2026 the labs were one repository, `bf550-labs`, cloned once. That clone still holds
units 1 and 2 and is no longer updated; the same notebooks are in `bf550-unit01-labs` and
`bf550-unit02-labs`.*

Nothing is submitted from a lab. A lab that produces something worth keeping feeds that unit's
problem set instead.

| Unit | Meeting | Lab |
|---:|---|---|
{% for lab in site.data.labs -%}
| {{ lab.unit | remove: "unit-" | plus: 0 }} | {{ lab.date }} | [{{ lab.title }}]({% if lab.path %}{{ site.labs_org }}/bf550-{{ lab.unit | remove: "-" }}-labs/blob/main/{{ lab.path }}{% else %}{{ site.baseurl }}/labs/{{ lab.id }}/{% endif %}) |
{% endfor %}

Each unit's labs are also listed on that unit's page, under **In class**. The [schedule]({{ site.baseurl }}/schedule/)
links every meeting date to its lab once that lab is posted.
