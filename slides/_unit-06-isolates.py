# Unit 6's isolate setting, ready to paste into a deck's hidden setup chunk.
#
# A hospital lab's E. coli isolates, each screened for three resistance genes and grown on
# ceftriaxone. About 15% grow (resistant), in line with US surveillance: 15.3% third-generation
# cephalosporin resistance in E. coli across VA hospitals in 2019 (Lancet Infect Dis 2024,
# doi:10.1016/S1473-3099(24)00416-X) and 12.9% in febrile UTIs at Kaiser Northern California
# (Ann Emerg Med 2021, doi:10.1016/j.annemergmed.2021.01.003).
#
# The panel's rule: any panel gene present -> call resistant. It misses resistance from a
# mechanism the panel doesn't test, and it over-calls isolates that carry a gene without
# growing on the drug.
import numpy as np

genes = ["blaCTX-M", "blaCMY-2", "blaSHV"]
share_resistant = 0.15

# P(gene present | class). Resistant isolates mostly carry CTX-M; a few carry none of the
# three. Susceptible isolates occasionally carry one.
gene_prob = {"resistant":   np.array([0.75, 0.12, 0.08]),
             "susceptible": np.array([0.02, 0.02, 0.03])}

def draw_isolate(rng):
    if rng.random() < share_resistant:
        growth = "resistant"
    else:
        growth = "susceptible"
    present = rng.random(3) < gene_prob[growth]
    return growth, present

def panel_call(present):
    if present.any():
        return "resistant"
    return "susceptible"

def draw_isolates(n, rng):
    rows = []
    for i in range(n):
        growth, present = draw_isolate(rng)
        rows.append({"isolate": f"EC-{i + 1:03d}", "present": present,
                     "call": panel_call(present), "growth": growth})
    return rows

def confusion(rows):
    c = {"TP": 0, "FP": 0, "FN": 0, "TN": 0}
    for r in rows:
        if r["call"] == "resistant" and r["growth"] == "resistant":
            c["TP"] += 1
        elif r["call"] == "resistant":
            c["FP"] += 1
        elif r["growth"] == "resistant":
            c["FN"] += 1
        else:
            c["TN"] += 1
    return c

def markdown_table(rows):
    head = "| Isolate | " + " | ".join(f"*{g}*" for g in genes) + " | Panel call | Growth test |"
    rule = "|---|" + ":-:|" * len(genes) + "---|---|"
    lines = [head, rule]
    for r in rows:
        marks = " | ".join("+" if p else "–" for p in r["present"])
        lines.append(f"| {r['isolate']} | {marks} | {r['call']} | {r['growth']} |")
    return "\n".join(lines)

def rates(c):
    n = c["TP"] + c["FP"] + c["FN"] + c["TN"]
    return {"accuracy":    (c["TP"] + c["TN"]) / n,
            "sensitivity": c["TP"] / (c["TP"] + c["FN"]),
            "specificity": c["TN"] / (c["TN"] + c["FP"]),
            "PPV":         c["TP"] / (c["TP"] + c["FP"])}

# The full year: 500 isolates.
isolates = draw_isolates(500, np.random.default_rng(606))
full_counts = confusion(isolates)
full_rates = rates(full_counts)

# The hand-countable table: 12 isolates. The seed was chosen so that all four cells of the
# confusion table are filled: 2 caught, 1 missed, 1 over-called and 8 cleared.
small = draw_isolates(12, np.random.default_rng(45))
small_counts = confusion(small)
small_rates = rates(small_counts)
