"""Mera "oscilatorne kontrakcije": odnos varijanse razmaka nula zete prema varijansi tacne GUE raspodele.
K = Var(razmaci nula) / Var_GUE.   K < 1 -> raspodela uza od GUE (kontrakcija);  K = 1 -> nema kontrakcije.
Sum: K za nizove PRAVIH GUE razmaka iste duzine (tridijagonalni model), da bi se videlo da li je odstupanje van suma.
P1: K < 1 van suma.  P2: K raste ka 1 sa visinom."""
import sys

# deljene funkcije iz gue_tacno.py (tacna GUE raspodela, GUE generator); PRE parsiranja ovih argumenata
_argv = sys.argv[:]
_seed = _argv[_argv.index("--seed") + 1] if "--seed" in _argv else "42"
sys.argv = ["gue_tacno.py", "--seed", _seed]
_src = open("gue_tacno.py").read()
exec(_src[:_src.index("# ---------- nule zete")])
sys.argv = _argv

import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Kontrakcija: Var(razmaci nula) / Var(GUE), ukupno i po visini")
parser.add_argument("--ulaz", default="scan.npz", help="izlaz skripte scan.py (podrazumevano scan.npz)")
parser.add_argument("--t-min", type=float, default=1000.0, help="koristi nule iznad ove visine (podrazumevano 1000)")
parser.add_argument("--delovi", type=int, default=6, help="broj jednakih delova po visini (podrazumevano 6)")
parser.add_argument("--reps", type=int, default=200, help="GUE nizova za sum (podrazumevano 200)")
parser.add_argument("--seed", type=int, default=42, help="seed (podrazumevano 42)")
parser.add_argument("--izlaz", default=None, help="ime grafika (podrazumevano <ulaz>_kontrakcija.png)")
args = parser.parse_args()
izlaz = args.izlaz or args.ulaz.replace(".npz", "") + "_kontrakcija.png"

var_gue = np.trapezoid(SG ** 2 * P_EX, SG) - np.trapezoid(SG * P_EX, SG) ** 2
print(f"varijansa tacne GUE raspodele razmaka: {var_gue:.4f}   (Vignerova aproks.: {3*np.pi/8-1:.4f})")

d = np.load(args.ulaz)
ts, Z, sc = d["ts"], d["Z"], d["sc"]
z = ts[sc] - Z[sc] * (ts[sc + 1] - ts[sc]) / (Z[sc + 1] - Z[sc])
Nf = lambda t: t / (2 * np.pi) * np.log(t / (2 * np.pi * np.e)) + 7 / 8
s = np.diff(Nf(z))
mid = (z[:-1] + z[1:]) / 2
keep = mid > args.t_min
s, mid = s[keep], mid[keep]
n = len(s)


def noise(m, reps):
    return np.array([np.var(gue_spacings(m)) / var_gue for _ in range(reps)])


K_all = np.var(s) / var_gue
nz = noise(n, args.reps)
print(f"\nukupno: n = {n}, t {args.t_min:.0f}-{mid.max():.0f}, srednji razmak {s.mean():.4f}")
print(f"   K = {K_all:.4f}   GUE sum: {np.percentile(nz,0.5):.4f} - {np.percentile(nz,99.5):.4f} (99%)"
      f"   -> {'VAN suma' if (K_all < np.percentile(nz,0.5) or K_all > np.percentile(nz,99.5)) else 'u sumu'}")

edges = np.quantile(mid, np.linspace(0, 1, args.delovi + 1))
m_bin = int(np.floor(n / args.delovi))
nb = noise(m_bin, args.reps)
lo, hi = np.percentile(nb, [0.5, 99.5])
print(f"\npo visini ({args.delovi} delova po ~{m_bin}; GUE sum 99%: {lo:.4f} - {hi:.4f}):")
rows = []
for a, b in zip(edges[:-1], edges[1:]):
    msk = (mid >= a) & (mid <= b)
    K = np.var(s[msk]) / var_gue
    tc = np.median(mid[msk])
    rows.append((a, b, tc, K))
    print(f"   t {a:7.0f}-{b:7.0f} (sredina {tc:7.0f}): K = {K:.4f}  {'VAN suma' if (K < lo or K > hi) else 'u sumu'}")

tcs = np.array([r[2] for r in rows]); Ks = np.array([r[3] for r in rows])
x = np.log(np.log(tcs / (2 * np.pi)))
slope, icpt = np.polyfit(x, Ks, 1)
# sum nagiba: isti fit na nizovima GUE vrednosti (bez trenda) -> raspodela nagiba pod "nema trenda"
null_slopes = [np.polyfit(x, rng.choice(nb, len(x)), 1)[0] for _ in range(4000)]
p_slope = (np.sum(np.array(null_slopes) >= slope) + 1) / (len(null_slopes) + 1)
print(f"\ntrend: K ~ {icpt:.3f} + {slope:.3f} * log(log(t/2pi));  jednostrani p (nagib > 0 slucajno) = {p_slope:.4f}")
print(f"spearman (K raste sa t?): rho = {np.corrcoef(np.argsort(np.argsort(tcs)), np.argsort(np.argsort(Ks)))[0,1]:.3f}")

fig, ax = plt.subplots(figsize=(8, 4.3))
ax.axhspan(lo, hi, color="gray", alpha=0.3, label=f"GUE sum 99% (nizovi po {m_bin})")
ax.axhline(1, color="k", lw=0.8, label="K = 1 (GUE, bez kontrakcije)")
ax.plot(tcs, Ks, "o-", color="#1f5fa8", label="nule zete")
ax.set_xlabel("visina t (sredina dela)"); ax.set_ylabel("K = Var(razmaci) / Var(GUE)")
ax.set_title("Kontrakcija raspodele razmaka nula u odnosu na GUE")
ax.legend(fontsize=8); plt.tight_layout(); plt.savefig(izlaz, dpi=130)
print(f"\ngrafik: {izlaz}")
