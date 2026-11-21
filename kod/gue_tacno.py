"""Razmaci nula zete prema TACNOJ GUE raspodeli.

(a) Tacna GUE: E(s) = det(I - K_s), K = sine-jezgro na [0,s] (Bornemann 2010, Gauss-Legendre);
    CDF razmaka F(s) = 1 + E'(s). Nema suma uzorkovanja ni aproksimacije.
(b) Dvouzoracki KS (predlog): nule naspram uzorka GUE razmaka, ispravno odmotanih preko polukruga.
(c) Kalibracija: KS statistika za nizove od n PRAVIH GUE razmaka (koji su, kao i nule, medjusobno
    korelisani), da se dobije stvarna granica slucajnosti umesto klasicne (koja pretpostavlja nezavisnost).
GUE uzorci: tridijagonalni beta-Hermite model (Dumitriu-Edelman 2002), beta=2 -> isti spektar kao GUE."""
import argparse
import numpy as np
from scipy import stats
from scipy.linalg import eigvalsh_tridiagonal
from scipy.special import erf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="KS test razmaka nula zete prema tacnoj GUE raspodeli")
parser.add_argument("--ulaz", default="scan.npz", help="izlaz skripte scan.py (podrazumevano scan.npz)")
parser.add_argument("--t-min", type=float, default=1000.0, help="koristi nule iznad ove visine (podrazumevano 1000)")
parser.add_argument("--reps", type=int, default=400, help="broj GUE nizova za kalibraciju (podrazumevano 400)")
parser.add_argument("--seed", type=int, default=42, help="seed (podrazumevano 42)")
parser.add_argument("--delovi", type=int, default=4, help="na koliko delova po visini podeliti nule (podrazumevano 4)")
parser.add_argument("--izlaz", default=None, help="ime grafika (podrazumevano <ulaz>_gue_tacno.png)")
args = parser.parse_args()
rng = np.random.default_rng(args.seed)
izlaz = args.izlaz or args.ulaz.replace(".npz", "") + "_gue_tacno.png"

# ---------- (a) tacna GUE CDF
xg, wg = np.polynomial.legendre.leggauss(60)


def E(s):
    if s <= 0:
        return 1.0
    x = (xg + 1) * s / 2
    w = np.sqrt(wg * s / 2)
    K = np.sinc(x[:, None] - x[None, :])
    return np.linalg.det(np.eye(len(x)) - w[:, None] * K * w[None, :])


SG = np.linspace(0, 5, 2001)
h = 1e-4
F_EX = np.array([1 + (E(s + h) - E(s - h)) / (2 * h) if s > h else 0.0 for s in SG])
F_EX = np.clip(F_EX, 0, 1)
P_EX = np.gradient(F_EX, SG)


def F_gue(s):
    return np.interp(s, SG, F_EX, left=0.0, right=1.0)


def F_wig(s):
    return erf(2 * s / np.sqrt(np.pi)) - (4 * s / np.pi) * np.exp(-4 * s ** 2 / np.pi)


def ks1(sp, F):
    x = np.sort(sp)
    n = len(x)
    f = F(x)
    return max(np.max(np.arange(1, n + 1) / n - f), np.max(f - np.arange(n) / n))


# ---------- GUE generator (tridijagonalni model) sa ispravnim odmotavanjem
def gue_spacings(n_target, N=4000):
    out = []
    while sum(len(o) for o in out) < n_target:
        d = rng.normal(0, np.sqrt(2), N) / np.sqrt(2)
        e = np.sqrt(rng.chisquare(2 * np.arange(N - 1, 0, -1))) / np.sqrt(2)
        lam = eigvalsh_tridiagonal(d, e)                     # polukrug poluprecnika 2*sqrt(N) (izmereno)
        x = lam / (2 * np.sqrt(N))                           # -> [-1, 1]
        x = x[np.abs(x) < 0.5]                               # sredina spektra
        cum = N * (0.5 + (x * np.sqrt(1 - x ** 2) + np.arcsin(x)) / np.pi)  # odmotavanje
        out.append(np.diff(cum))
    return np.concatenate(out)[:n_target]


def gue_runs(n, reps):
    """reps nezavisnih nizova od po n uzastopnih GUE razmaka (korelisani unutar niza, kao nule)."""
    return [gue_spacings(n) for _ in range(reps)]


# ---------- nule zete
d = np.load(args.ulaz)
ts, Z, sc = d["ts"], d["Z"], d["sc"]
z = ts[sc] - Z[sc] * (ts[sc + 1] - ts[sc]) / (Z[sc + 1] - Z[sc])
Nf = lambda t: t / (2 * np.pi) * np.log(t / (2 * np.pi * np.e)) + 7 / 8
s_all = np.diff(Nf(z))
mid = (z[:-1] + z[1:]) / 2
keep = mid > args.t_min
s, mid = s_all[keep], mid[keep]
n = len(s)

print("== provera tacne GUE raspodele")
mean = np.trapezoid(SG * P_EX, SG)
g_check = gue_spacings(200000)
print(f"   F(5) = {F_EX[-1]:.6f}, srednji razmak = {mean:.4f}")
print(f"   max |tacna - Vigner| = {np.max(np.abs(F_EX - F_wig(SG))):.4f}")
print(f"   KS(200000 simuliranih GUE razmaka, tacna CDF) = {ks1(g_check, F_gue):.4f}"
      f"   (srednji razmak simulacije {g_check.mean():.4f})")

print(f"\n== nule zete: {n} razmaka, t od {args.t_min:.0f} do {mid.max():.0f}")
k_wig, k_ex = ks1(s, F_wig), ks1(s, F_gue)
print(f"   KS prema Vignerovoj aproksimaciji: {k_wig:.4f}")
print(f"   KS prema TACNOJ GUE:               {k_ex:.4f}")
print(f"   klasicna granica p=0.01 (pretpostavlja nezavisnost): {1.628/np.sqrt(n):.4f}")

null = np.array([ks1(r, F_gue) for r in gue_runs(n, args.reps)])
p_emp = (np.sum(null >= k_ex) + 1) / (len(null) + 1)
print(f"   kalibracija ({args.reps} GUE nizova po {n}): medijana {np.median(null):.4f}, "
      f"99. percentil {np.percentile(null, 99):.4f}  ->  empirijski p = {p_emp:.4f}")

print("\n== dvouzoracki KS (predlog), GUE uzorak ispravno odmotan")
for mult in (1, 10):
    g = gue_spacings(mult * n)
    st, p = stats.ks_2samp(s, g)
    crit = np.sqrt(-0.5 * np.log(0.01 / 2) * (n + len(g)) / (n * len(g)))
    print(f"   GUE uzorak {mult:2d}x ({len(g)}): KS = {st:.4f}, p = {p:.4f}, klasicna granica = {crit:.4f}")
# koliko bi Vignerova raspodela "prosla" isti dvouzoracki test (snaga testa)
xs = np.linspace(0, 5, 200001)
cw = F_wig(xs)
wig_sample = np.interp(rng.random(n), cw, xs)
g = gue_spacings(n)
st, p = stats.ks_2samp(wig_sample, g)
print(f"   kontrola snage: {n} razmaka iz VIGNEROVE raspodele naspram GUE uzorka: KS = {st:.4f}, p = {p:.4f}")

print(f"\n== po visini ({args.delovi} dela, kalibracija 200 nizova po delu)")
edges = np.quantile(mid, np.linspace(0, 1, args.delovi + 1))
rows = []
for a, b in zip(edges[:-1], edges[1:]):
    m = (mid >= a) & (mid <= b)
    k = ks1(s[m], F_gue)
    nl = np.array([ks1(r, F_gue) for r in gue_runs(m.sum(), 200)])
    pe = (np.sum(nl >= k) + 1) / (len(nl) + 1)
    rows.append((a, b, m.sum(), k, np.percentile(nl, 99), pe))
    print(f"   t {a:7.0f}-{b:7.0f}: n={m.sum():6d}  KS={k:.4f}  GUE 99%: {np.percentile(nl,99):.4f}  p={pe:.4f}")

# ---------- grafik
fig, ax = plt.subplots(1, 2, figsize=(12, 4.3))
ax[0].hist(s, bins=70, range=(0, 3.5), density=True, color="#c9d6e8", edgecolor="#3b6ea5", label=f"nule zete (n={n})")
ax[0].plot(SG, P_EX, "r", lw=2, label="tacna GUE")
ax[0].plot(SG, 32 / np.pi ** 2 * SG ** 2 * np.exp(-4 * SG ** 2 / np.pi), "k:", lw=1.5, label="Vignerova aproks.")
ax[0].set_xlim(0, 3.5); ax[0].set_xlabel("normalizovan razmak"); ax[0].set_title("Razmaci nula i tacna GUE"); ax[0].legend()
xsrt = np.sort(s)
emp = np.arange(1, n + 1) / n
ax[1].plot(xsrt, emp - F_gue(xsrt), lw=1.2, label="nule - tacna GUE")
ax[1].plot(xsrt, emp - F_wig(xsrt), lw=1, alpha=0.7, label="nule - Vigner")
gs = np.sort(gue_spacings(n))
ax[1].plot(gs, emp - F_gue(gs), lw=0.8, color="gray", alpha=0.8, label="jedan GUE niz - tacna GUE (sum)")
ax[1].axhline(0, color="k", lw=0.6)
ax[1].set_xlim(0, 3.5); ax[1].set_xlabel("razmak"); ax[1].set_ylabel("razlika kumulativnih raspodela")
ax[1].set_title("Gde se razlikuju"); ax[1].legend(fontsize=8)
plt.tight_layout(); plt.savefig(izlaz, dpi=130)
print(f"\ngrafik: {izlaz}")
