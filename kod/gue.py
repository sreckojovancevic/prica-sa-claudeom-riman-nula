"""Razmaci nula: poredjenje sa GUE (Vignerova aproksimacija) i Poasonom, par-korelacija."""
import argparse
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Raspodela razmaka nula: GUE ili Poason")
parser.add_argument("--ulaz", default="scan.npz", help="izlaz skripte scan.py (podrazumevano scan.npz)")
parser.add_argument("--t-min", type=float, default=1000.0, help="koristi samo nule iznad ove visine (podrazumevano 1000)")
parser.add_argument("--izlaz", default="gue_poredjenje.png", help="ime grafika")
args = parser.parse_args()

d = np.load(args.ulaz); ts, Z, sc = d["ts"], d["Z"], d["sc"]
z = ts[sc] - Z[sc]*(ts[sc+1]-ts[sc])/(Z[sc+1]-Z[sc])
# "unfolding": prosecna gustina nula N(t) ~ t/2pi log(t/2pi e) + 7/8
N = lambda t: t/(2*np.pi)*np.log(t/(2*np.pi*np.e)) + 7/8
u = N(z)
s = np.diff(u)
s = s[u[:-1] > N(args.t_min)]          # izbegni najnize nule (pravilnije)
print(f"razmaka u analizi: {len(s)}, prosek {s.mean():.4f}")

gue = lambda x: 32/np.pi**2 * x**2 * np.exp(-4*x**2/np.pi)
poi = lambda x: np.exp(-x)
# kumulativne raspodele za poredjenje (KS rastojanje)
xs = np.sort(s); emp = np.arange(1, len(xs)+1)/len(xs)
from math import erf
F_gue = np.array([erf(2*x/np.sqrt(np.pi)) - (4*x/np.pi)*np.exp(-4*x**2/np.pi) for x in xs])
F_poi = 1 - np.exp(-xs)
ks_g = np.abs(emp-F_gue).max(); ks_p = np.abs(emp-F_poi).max()
print(f"KS rastojanje od GUE:     {ks_g:.4f}")
print(f"KS rastojanje od Poasona: {ks_p:.4f}")
print(f"kriticna vrednost (p=0.01): {1.63/np.sqrt(len(s)):.4f}")
for a in (0.1, 0.2, 0.3):
    print(f"udeo razmaka < {a}: izmereno {np.mean(s<a)*100:.2f}% | GUE {np.interp(a, xs, F_gue)*100:.2f}% | Poason {(1-np.exp(-a))*100:.2f}%")

# par-korelacija (Montgomery): 1 - (sin pi x / pi x)^2
diffs = []
for k in range(1, 6):
    diffs.append(u[k:] - u[:-k])
dd = np.concatenate(diffs); dd = dd[dd < 3]
h, e = np.histogram(dd, bins=60, range=(0, 3))
c = (e[:-1]+e[1:])/2; R = h/(len(u)*(e[1]-e[0]))
x = np.linspace(0.001, 3, 400)

fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
ax[0].hist(s, bins=60, range=(0, 3.5), density=True, color="#c9d6e8", edgecolor="#3b6ea5", label="izmereno (nule zete)")
ax[0].plot(x, gue(x), "r", lw=2, label="GUE (kvantni haos)")
ax[0].plot(x, poi(x), "k--", lw=1.5, label="Poason (nezavisne tacke)")
ax[0].set_xlabel("razmak izmedju susednih nula (normalizovan)"); ax[0].set_title("Raspodela razmaka"); ax[0].legend()
ax[1].plot(c, R, "o", ms=3, color="#3b6ea5", label="izmereno")
ax[1].plot(x, 1-(np.sin(np.pi*x)/(np.pi*x))**2, "r", lw=2, label="Montgomeri: 1-(sin πx/πx)²")
ax[1].axhline(1, color="k", ls="--", lw=1, label="bez korelacije")
ax[1].set_xlabel("rastojanje"); ax[1].set_title("Par-korelacija nula"); ax[1].legend()
plt.tight_layout(); plt.savefig(args.izlaz, dpi=130); print(f"grafik: {args.izlaz}")
