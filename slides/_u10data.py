"""Data and helpers for BF550 unit 10 (generalized linear models).

Every dataset is simulated with a fixed seed, so the decks, the lab and the check-ins print the
same numbers. Import this file next to the decks:

    from _u10data import *

Sessions:
    1  logistic regression        alzheimers_cohort(), six_people(), likelihood()
                                  (gwas() and causal_snp_table() are the earlier s1 design)
    2  negative binomial          rnaseq_study(), shared_alpha(), nb_scan()
    3  cell-type proportions      single_cell(), cells_long()

gwas() and single_cell() are Josh Campbell's unit 9 hand-off simulations (unit 9 PLAN.md §6),
copied unchanged so that unit 10 does not depend on the unit 9 folder. Run this file to print
every number the unit 10 plan quotes.
"""
import numpy as np
import pandas as pd

# Josh's unit 9 palette, so the two units look alike.
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED = "#222222", "#6b6b6b"


# ---------------------------------------------------------------------------
# Session 1: case/control association study (logistic regression)
# ---------------------------------------------------------------------------

def gwas(seed=556, n_snps=1000, n=2000):
    """Case/control GWAS in two ancestry groups; SNP 500 is the only causal one.

    Ancestry B has a higher disease rate and different allele frequencies,
    so many SNPs look associated unless ancestry is in the model.
    Returns G (people x SNPs, 0/1/2 copies), anc (0 = A, 1 = B), case (0/1), causal.
    """
    rng = np.random.default_rng(seed)
    anc = (rng.random(n) < 0.5).astype(int)            # 0 = A, 1 = B
    fA = rng.uniform(0.1, 0.9, n_snps)
    fB = np.clip(fA + rng.normal(0, 0.15, n_snps), 0.05, 0.95)
    f = np.where(anc[:, None] == 1, fB[None, :], fA[None, :])
    G = rng.binomial(2, f)                              # people x SNPs, 0/1/2
    causal = 500
    eta = -1.5 + 1.0 * anc + 0.5 * G[:, causal]
    case = (rng.random(n) < 1 / (1 + np.exp(-eta))).astype(int)
    return G, anc, case, causal


def causal_snp_table(seed=556):
    """One row per person for the causal SNP: copies (0/1/2), ancestry (A/B), case (0/1)."""
    G, anc, case, causal = gwas(seed)
    return pd.DataFrame({"copies": G[:, causal],
                         "ancestry": np.where(anc == 1, "B", "A"),
                         "case": case})


def alzheimers_cohort(seed=2021, n=2000, q=0.15):
    """A community cohort of adults aged 60 to 94, each assessed for Alzheimer's disease.

    One row per person: age (whole years), e4 (copies of APOE e4: 0, 1 or 2), case (1 =
    Alzheimer's, 0 = healthy). Ages are weighted toward the younger bands (30% 60-69, 35%
    70-79, 23% 80-89, 12% 90-94). e4 copies follow Hardy-Weinberg with allele frequency q.
    Truth: logit p = -12 + 0.12 age + log(3) e4, i.e. the odds multiply by about 1.8 every 5
    years (incidence roughly doubles every 5 years past 65) and by 3 per e4 copy (Farrer et al.
    JAMA 1997: OR 3.2 for e3/e4). Seed 2021 gives 11.7% cases overall: 2.6%, 8.5%, 18.9% and
    29.9% by band, and a least-squares line on age that predicts below 0 for ages 60-63.
    """
    rng = np.random.default_rng(seed)
    band = rng.choice(4, n, p=[0.30, 0.35, 0.23, 0.12])
    age = np.array([60, 70, 80, 90])[band] + rng.integers(0, np.array([10, 10, 10, 5])[band])
    e4 = rng.binomial(2, q, n)
    eta = -12.0 + 0.12 * age + np.log(3.0) * e4
    case = (rng.random(n) < 1 / (1 + np.exp(-eta))).astype(int)
    return pd.DataFrame({"age": age, "e4": e4, "case": case})


def six_people():
    """The hand-sized example for the likelihood steps: six people, their ages, case 0/1.

    Chosen so that the maximum-likelihood b1 is interior (no separation): smf.logit gives
    b0 = -10.34, b1 = 0.134. Holding b0 at -10, the likelihood is 0.0018 at b1 = 0.10, 0.025
    at b1 = 0.12, and peaks at b1 = 0.129.
    """
    return pd.DataFrame({"person": list("ABCDEF"),
                         "age": [64, 70, 75, 80, 85, 90],
                         "case": [0, 1, 0, 0, 1, 1]})


def likelihood(b0, b1, x, y):
    """Each person's probability of what happened under the curve (b0, b1), and their product."""
    p = 1 / (1 + np.exp(-(b0 + b1 * np.asarray(x, float))))
    each = np.where(np.asarray(y) == 1, p, 1 - p)
    return p, each, float(np.prod(each))


def gwas_scan(G, case, covariate=None):
    """One logistic regression per SNP; returns each SNP's p-value for its copies term."""
    import statsmodels.api as sm
    p = np.empty(G.shape[1])
    for j in range(G.shape[1]):
        cols = [G[:, j]] if covariate is None else [G[:, j], covariate]
        X = sm.add_constant(np.column_stack(cols).astype(float))
        p[j] = sm.Logit(case, X).fit(disp=0).pvalues[1]
    return p


# ---------------------------------------------------------------------------
# Session 2: RNA-seq counts (negative binomial regression)
# ---------------------------------------------------------------------------

def rnaseq_study(seed=419, n_genes=2000, n_per=3, n_changed=200, alpha=0.1, fold=2.5,
                 equal_depth=True, n_reads=300_000):
    """3 control and 3 treated samples.

    equal_depth=True (the deck's setting): every sample is sequenced to exactly `n_reads` reads.
    Each sample draws its own true expression level for every gene from a gamma distribution
    (unit 3's first level), the levels become each gene's share of the reads, and the sample's
    n_reads reads are dealt out among the genes in those shares (a multinomial draw, so each gene's
    count is Binomial(n_reads, its share): the second level). Each gene's counts are then close to
    negative binomial with Var = mu + alpha * mu^2. No offset is needed.

    equal_depth=False: samples get different relative depths and counts are gamma-Poisson; the
    fitting helpers then use log(lib_size) as an offset.

    Genes 0 .. n_changed-1 change by `fold` (half up, half down); the rest are unchanged.
    Returns counts (genes x samples), samples (DataFrame: sample, treatment, lib_size = 1 at equal
    depth, else total reads in millions), changed (bool per gene).
    """
    rng = np.random.default_rng(seed)
    base = np.exp(rng.normal(4, 1.5, n_genes))           # relative expression of each gene
    fc = np.ones(n_genes)
    fc[:n_changed] = np.where(np.arange(n_changed) < n_changed // 2, fold, 1 / fold)
    trt = np.repeat([0, 1], n_per)
    r = 1 / alpha
    if equal_depth:
        mu = base[:, None] * np.where(trt == 1, fc[:, None], 1.0)
        level = rng.gamma(r, mu / r)                      # level 1: each sample's true levels
        share = level / level.sum(axis=0, keepdims=True)
        counts = np.column_stack([rng.multinomial(n_reads, share[:, j]) for j in range(2 * n_per)])
        lib_size = np.ones(2 * n_per)
    else:
        lib = np.round(rng.uniform(0.6, 1.6, 2 * n_per), 2)
        mu = base[:, None] * lib[None, :] * np.where(trt == 1, fc[:, None], 1.0)
        counts = rng.poisson(rng.gamma(r, mu / r))
        lib_size = counts.sum(axis=0) / 1e6
    samples = pd.DataFrame({"sample": [f"ctl{i + 1}" for i in range(n_per)]
                            + [f"trt{i + 1}" for i in range(n_per)],
                            "treatment": np.where(trt == 1, "treated", "control"),
                            "lib_size": lib_size})
    return counts, samples, fc != 1


def gene_table(counts, samples, g):
    """One gene's counts as a tidy table with the sample columns, ready for smf.glm."""
    d = samples.copy()
    d["count"] = counts[g]
    return d


def shared_alpha(counts, samples):
    """One dispersion for every gene, by the method of moments.

    Per gene and group, the excess of the variance over the Poisson part (the mean) estimates
    alpha * mu^2; summing excess and mu^2 over all genes and both groups gives one pooled alpha.
    Counts are divided by lib_size first, which is 1 for every sample at equal depth (the deck's
    setting); with equal_depth=False, count / s has variance mu/s + alpha * mu^2 and the formula
    accounts for that.
    """
    s = samples["lib_size"].to_numpy()
    scaled = counts / s[None, :]
    num = den = 0.0
    for grp in samples["treatment"].unique():
        k = (samples["treatment"] == grp).to_numpy()
        m = scaled[:, k].mean(axis=1)
        v = scaled[:, k].var(axis=1, ddof=1)
        num += (v - m * np.mean(1 / s[k])).sum()
        den += (m ** 2).sum()
    return max(num / den, 1e-6)


def nb_scan(counts, samples, alpha=None, family="nb"):
    """One count GLM per gene, treatment as the predictor.

    The fit carries log(lib_size) as an offset, which is log 1 = 0 at equal depth (the deck's
    setting, so the model has no offset in effect) and matters only with equal_depth=False.

    family="nb" with a fixed alpha (sm.GLM), "nb_own" for each gene's own alpha
    (sm.NegativeBinomial), or "poisson". Returns log fold changes and p-values (NaN where a fit
    fails or a gene has fewer than 10 reads).
    """
    import warnings
    import statsmodels.api as sm
    X = sm.add_constant((samples["treatment"] == "treated").to_numpy().astype(float))
    off = np.log(samples["lib_size"].to_numpy())
    b = np.full(len(counts), np.nan)
    p = np.full(len(counts), np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for g, y in enumerate(counts):
            if y.sum() < 10:
                continue
            try:
                if family == "poisson":
                    m = sm.GLM(y, X, family=sm.families.Poisson(), offset=off).fit()
                elif family == "nb":
                    m = sm.GLM(y, X, family=sm.families.NegativeBinomial(alpha=alpha),
                               offset=off).fit()
                else:
                    m = sm.NegativeBinomial(y, X, offset=off).fit(disp=0)
                b[g], p[g] = m.params[1], m.pvalues[1]
            except Exception:
                pass
    return b, p


# ---------------------------------------------------------------------------
# Session 3: single-cell composition (multinomial logit, log-ratios)
# ---------------------------------------------------------------------------

CELL_TYPES = ["T cell", "B cell", "Monocyte", "NK cell", "Epithelial"]


def single_cell(seed=557, n_per=6, cells_per_sample=3000):
    """Cell-type counts per sample. Only T cells truly expand in disease (x2 in abundance)."""
    rng = np.random.default_rng(seed)
    types = list(CELL_TYPES)
    base = np.array([0.20, 0.15, 0.25, 0.10, 0.30])
    rows = []
    for status in ["control", "disease"]:
        for i in range(n_per):
            w = base * np.exp(rng.normal(0, 0.12, 5))
            if status == "disease":
                w[0] *= 2.0                               # only T cells change
            prop = w / w.sum()
            counts = rng.multinomial(cells_per_sample, prop)
            rows.append({"sample": f"{status[:3]}{i + 1}", "status": status,
                         **dict(zip(types, counts))})
    return pd.DataFrame(rows), types


def cells_long(df, types=CELL_TYPES, reference="B cell"):
    """One row per cell (sample, status, cell_type, y), y coded 0 = reference, 1.. = the others.

    smf.mnlogit fits log(p_type / p_reference) for every non-reference type.
    """
    order = [reference] + [t for t in types if t != reference]
    parts = [pd.DataFrame({"sample": r["sample"], "status": r["status"], "cell_type": t},
                          index=range(int(r[t])))
             for _, r in df.iterrows() for t in order]
    cells = pd.concat(parts, ignore_index=True)
    cells["y"] = cells["cell_type"].map({t: i for i, t in enumerate(order)})
    return cells, order


# ---------------------------------------------------------------------------
# Plot style (Josh's unit 9 setup_plots and box_strip)
# ---------------------------------------------------------------------------

def setup_plots():
    import matplotlib as mpl
    mpl.rcParams.update({
        "figure.figsize": (9, 4.5), "figure.dpi": 110, "savefig.dpi": 150,
        "font.size": 15, "axes.titlesize": 16, "axes.labelsize": 15,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": MUTED, "axes.labelcolor": INK,
        "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.grid": True, "grid.color": "#e6e5e1", "grid.linewidth": 0.8,
        "lines.linewidth": 2, "lines.markersize": 8, "legend.frameon": False,
        "figure.facecolor": "#fcfcfa", "axes.facecolor": "#fcfcfa",
        "savefig.facecolor": "#fcfcfa",
    })


def box_strip(ax, y, x=0.0, color=INK, width=0.5, seed=0, box=True):
    """A gray box (no median line) with seeded, sideways-jittered points on top."""
    y = np.asarray(y, dtype=float)
    if box:
        ax.boxplot([y], positions=[x], widths=width, showfliers=False, patch_artist=True,
                   medianprops={"visible": False},
                   boxprops={"facecolor": "#e9e8e4", "edgecolor": MUTED},
                   whiskerprops={"color": MUTED}, capprops={"color": MUTED})
    jit = np.random.default_rng(seed).uniform(-width * 0.35, width * 0.35, len(y))
    ax.scatter(x + jit, y, s=40, color=color, zorder=3, edgecolor="white", linewidth=0.6)


# ---------------------------------------------------------------------------
# Self-check: prints every number the plan quotes
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    import statsmodels.formula.api as smf
    from scipy import stats

    print("== Session 1: GWAS (seed 556) ==")
    d = causal_snp_table()
    print("case rate by ancestry:", d.groupby("ancestry")["case"].mean().round(3).to_dict())
    m1 = smf.logit("case ~ copies", d).fit(disp=0)
    m2 = smf.logit("case ~ copies + ancestry", d).fit(disp=0)
    print(f"copies alone: b1 {m1.params['copies']:.3f}, OR {np.exp(m1.params['copies']):.2f}")
    print(f"with ancestry: b1 {m2.params['copies']:.3f}, OR {np.exp(m2.params['copies']):.2f},"
          f" ancestry b {m2.params['ancestry[T.B]']:.2f}")
    G, anc, case, causal = gwas()
    p0, p1 = gwas_scan(G, case), gwas_scan(G, case, anc)
    bonf = 0.05 / G.shape[1]
    print(f"Bonferroni hits: {(p0 < bonf).sum()} without ancestry, {(p1 < bonf).sum()} with"
          f" (SNPs {np.where(p1 < bonf)[0].tolist()})")

    print("\n== Session 2: RNA-seq, 3 vs 3 (seed 419) ==")
    counts, samples, changed = rnaseq_study()
    print(samples.to_string(index=False))
    a = shared_alpha(counts, samples)
    print(f"shared alpha {a:.3f} (truth 0.1)")
    for fam in ("poisson", "nb_own", "nb"):
        b, p = nb_scan(counts, samples, alpha=a, family=fam)
        print(f"  {fam:8s} unchanged genes at p<0.05: {np.nanmean(p[~changed] < 0.05):.3f};"
              f" changed found: {np.nanmean(p[changed] < 0.05):.2f};"
              f" failed fits: {int(np.isnan(p).sum())}")

    print("\n== Session 3: composition (seed 557) ==")
    df, types = single_cell()
    prop = df[types].div(df[types].sum(axis=1), axis=0)
    print(prop.groupby(df["status"]).mean().round(3).to_string())
    print("naive t-tests on proportions:",
          {t: round(stats.ttest_ind(prop[t][df.status == "disease"],
                                    prop[t][df.status == "control"]).pvalue, 4) for t in types})
    cells, order = cells_long(df)
    mm = smf.mnlogit("y ~ status", cells).fit(disp=0)
    print("per-cell mnlogit (reference B cell), n =", len(cells))
    for i, t in enumerate(order[1:]):
        print(f"  {t:11s} b1 {mm.params.iloc[1, i]:+.3f}  p {mm.pvalues.iloc[1, i]:.3g}")
    print("per-sample log-ratio linear model:")
    for t in order[1:]:
        df["lr"] = np.log(df[t] / df["B cell"])
        mo = smf.ols("lr ~ status", df).fit()
        print(f"  {t:11s} b1 {mo.params.iloc[1]:+.3f}  p {mo.pvalues.iloc[1]:.3g}")
