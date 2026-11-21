"""Omotac GUE suma: da li razlika (nule - tacna GUE) izlazi iz opsega koji daju pravi GUE nizovi iste duzine.
Za svaki od --reps GUE nizova od n razmaka racuna se (empirijska CDF - tacna CDF) na mrezi;
crta se tackasti 99% (i 50%) opseg i kriva nula zete."""
import argparse
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# deljene funkcije iz gue_tacno.py (tacna CDF, GUE generator); izvrsavaju se PRE parsiranja ovih argumenata
_argv = sys.argv[:]
_seed = _argv[_argv.index("--seed") + 1] if "--seed" in _argv else "42"
sys.argv = ["gue_tacno.py", "--seed", _seed]
_src = open("gue_tacno.py").read()
exec(_src[:_src.index("# ---------- nule zete")])
sys.argv = _argv

parser = argparse.ArgumentParser(description="Omotac GUE suma oko razlike nule - tacna GUE")
parser.add_argument("--ulaz", default="scan.npz", help="izlaz skripte scan.py (podrazumevano scan.npz)")
parser.add_argument("--t-min", type=float, default=1000.0, help="koristi nule iznad ove visine (podrazumevano 1000)")
parser.add_argument("--reps", type=int, default=400, help="broj GUE nizova (podrazumevano 400)")
parser.add_argument("--seed", type=int, default=42, help="seed (podrazumevano 42)")
parser.add_argument("--izlaz", default=None, help="ime grafika (podrazumevano <ulaz>_gue_omotac.png)")
args = parser.parse_args()
izlaz = args.izlaz or args.ulaz.replace(".npz", "") + "_gue_omotac.png"

d = np.load(args.ulaz)
ts, Z, sc = d["ts"], d["Z"], d["sc"]
z = ts[sc] - Z[sc] * (ts[sc + 1] - ts[sc]) / (Z[sc + 1] - Z[sc])
Nf = lambda t: t / (2 * np.pi) * np.log(t / (2 * np.pi * np.e)) + 7 / 8
s = np.diff(Nf(z))
s = s[(z[:-1] + z[1:]) / 2 > args.t_min]
n = len(s)

grid = np.linspace(0, 3.5, 701)
Fg = F_gue(grid)
ecdf = lambda x: np.searchsorted(np.sort(x), grid, side="right") / len(x)
D_zeta = ecdf(s) - Fg
D = np.array([ecdf(gue_spacings(n)) - Fg for _ in range(args.reps)])
lo99, hi99 = np.percentile(D, [0.5, 99.5], axis=0)
lo50, hi50 = np.percentile(D, [25, 75], axis=0)
izvan = np.mean((D_zeta < lo99) | (D_zeta > hi99))
print(f"n = {n}, GUE nizova = {args.reps}")
print(f"najveci |nule - tacna GUE| = {np.max(np.abs(D_zeta)):.4f}")
print(f"najsiri 99% omotac GUE suma = +-{np.max(np.maximum(-lo99, hi99)):.4f}")
print(f"udeo tacaka mreze gde je kriva nula IZVAN 99% omotaca: {100*izvan:.1f}%")

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.fill_between(grid, lo99, hi99, color="gray", alpha=0.25, label=f"99% omotac ({args.reps} GUE nizova po {n})")
ax.fill_between(grid, lo50, hi50, color="gray", alpha=0.45, label="50% omotac")
ax.plot(grid, D_zeta, color="#1f5fa8", lw=1.6, label="nule zete - tacna GUE")
ax.axhline(0, color="k", lw=0.6)
ax.set_xlabel("normalizovan razmak"); ax.set_ylabel("empirijska CDF - tacna GUE CDF")
ax.set_title(f"Da li je odstupanje nula samo sum? (t od {args.t_min:.0f}, n = {n})")
ax.legend(fontsize=8, loc="lower right")
plt.tight_layout(); plt.savefig(izlaz, dpi=130)
print(f"grafik: {izlaz}")
