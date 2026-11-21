"""Kontrakcija K za nule Dirihleove L-funkcije (ispravljena analiza izlaza dirichlet_scan.py).

Ispravke u odnosu na dirichlet_gue.py:
  1. dirichlet_scan.py cuva PAROVE uzastopnih nula (z1,z2),(z2,z3),...; flatten() je udvostrucavao
     svaku nulu, pa je polovina "razmaka" bila tacno 0. Ovde se uzimaju jedinstvene nule.
  2. Odmotavanje preko gustine nula N(t) = t/(2pi) ln(q t/(2 pi e)) umesto jednog globalnog proseka
     (gustina se od t=10 do 1000 menja skoro trostruko).
  3. Tacna GUE raspodela (Fredholmova determinanta) i GUE sum iz tridijagonalnog modela sa
     ispravnim odmotavanjem polukruga, umesto srednjih 60% gustog spektra podeljenih jednim prosekom.

K = Var(odmotani razmaci) / Var(tacna GUE).  K < 1 = kontrakcija (uza raspodela od GUE)."""
import argparse
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Kontrakcija K za nule Dirihleove L-funkcije")
parser.add_argument("--ulaz", default="dirichlet_scan.npz", help="izlaz dirichlet_scan.py (podrazumevano dirichlet_scan.npz)")
parser.add_argument("--q", type=int, default=4, help="modul (konduktor) karaktera (podrazumevano 4, chi_4)")
parser.add_argument("--reps", type=int, default=400, help="GUE nizova za sum (podrazumevano 400)")
parser.add_argument("--seed", type=int, default=42, help="seed (podrazumevano 42)")
parser.add_argument("--izlaz", default="dirichlet_kontrakcija.png", help="ime grafika")
args = parser.parse_args()
rng = np.random.default_rng(args.seed)

# ---- tacna GUE raspodela razmaka: E(s) = det(I - K_s), F(s) = 1 + E'(s)  (Bornemann 2010)
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
F_EX = np.clip(np.array([1 + (E(s + h) - E(s - h)) / (2 * h) if s > h else 0.0 for s in SG]), 0, 1)
P_EX = np.gradient(F_EX, SG)
VAR_GUE = np.trapezoid(SG ** 2 * P_EX, SG) - np.trapezoid(SG * P_EX, SG) ** 2


def F_gue(s):
    return np.interp(s, SG, F_EX, left=0.0, right=1.0)


def ks1(sp):
    x = np.sort(sp); n = len(x); f = F_gue(x)
    return max(np.max(np.arange(1, n + 1) / n - f), np.max(f - np.arange(n) / n))


def gue_spacings(n_target, N=4000):
    """GUE razmaci: tridijagonalni beta-Hermite model (Dumitriu-Edelman 2002, beta=2),
    sredina spektra (|x|<0.5), odmotano preko polukruga poluprecnika 2*sqrt(N)."""
    out, cnt = [], 0
    while cnt < n_target:
        d = rng.normal(0, 1, N)
        e = np.sqrt(rng.chisquare(2 * np.arange(N - 1, 0, -1))) / np.sqrt(2)
        x = eigvalsh_tridiagonal(d, e) / (2 * np.sqrt(N))
        x = x[np.abs(x) < 0.5]
        cum = N * (0.5 + (x * np.sqrt(1 - x ** 2) + np.arcsin(x)) / np.pi)
        sp = np.diff(cum)
        out.append(sp); cnt += len(sp)
    return np.concatenate(out)[:n_target]


# ---- nule iz dirichlet_scan.py: jedinstvene (ispravka 1)
d = np.load(args.ulaz)
z = np.unique(d["zeros"].ravel())
N = lambda t: t / (2 * np.pi) * np.log(args.q * t / (2 * np.pi * np.e))
s = np.diff(N(z))                      # ispravka 2: lokalno odmotavanje
n = len(s)
print(f"nule: {len(z)} (t {z.min():.3f} - {z.max():.3f}); ocekivano po N(t): {N(z.max()) - N(z.min()) + 1:.1f}")
print(f"razmaka: {n}, srednji odmotan razmak: {s.mean():.4f}")
print(f"varijansa tacne GUE: {VAR_GUE:.4f}")

K = np.var(s) / VAR_GUE
noise = np.array([np.var(gue_spacings(n)) / VAR_GUE for _ in range(args.reps)])
lo, hi = np.percentile(noise, [0.5, 99.5])
print(f"\nK = {K:.3f}   GUE sum 99%: {lo:.3f} - {hi:.3f}   -> {'VAN suma' if (K < lo or K > hi) else 'u sumu'}"
      f"   (udeo GUE nizova sa K <= izmerenog: {np.mean(noise <= K):.4f})")

ks = ks1(s)
null_ks = np.array([ks1(gue_spacings(n)) for _ in range(min(args.reps, 200))])
print(f"KS prema tacnoj GUE: {ks:.4f}   GUE 99. percentil: {np.percentile(null_ks, 99):.4f}")

# po visini: dve polovine
half = n // 2
for name, part in (("donja polovina", s[:half]), ("gornja polovina", s[half:])):
    print(f"   {name}: K = {np.var(part) / VAR_GUE:.3f}")

fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
ax[0].hist(s, bins=40, range=(0, 3.5), density=True, color="#c9d6e8", edgecolor="#3b6ea5", label=f"nule L(s, chi_{args.q}) (n={n})")
ax[0].plot(SG, P_EX, "r", lw=2, label="tacna GUE")
ax[0].set_xlim(0, 3.5); ax[0].set_xlabel("odmotan razmak"); ax[0].legend(); ax[0].set_title("Razmaci nula Dirihleove L-funkcije")
ax[1].hist(noise, bins=40, color="gray", alpha=0.6, label=f"K za {args.reps} GUE nizova po {n}")
ax[1].axvline(K, color="#1f5fa8", lw=2, label=f"K nula = {K:.3f}")
ax[1].axvline(1, color="k", lw=0.8)
ax[1].set_xlabel("K = Var / Var(GUE)"); ax[1].legend(fontsize=8); ax[1].set_title("Kontrakcija u odnosu na GUE sum")
plt.tight_layout(); plt.savefig(args.izlaz, dpi=130)
print(f"\ngrafik: {args.izlaz}")
