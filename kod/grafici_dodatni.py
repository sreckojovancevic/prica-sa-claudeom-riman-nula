"""Grafici: raspodela vrhova (iz scan.py) i sudar para nula (iz heatflow.py)."""
import argparse
import pickle
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Dodatni grafici iz scan.npz i heat.pkl")
parser.add_argument("--scan", default="scan.npz", help="izlaz skripte scan.py (podrazumevano scan.npz)")
parser.add_argument("--heat", default="heat.pkl", help="izlaz skripte heatflow.py (podrazumevano heat.pkl)")
parser.add_argument("--par", type=int, default=6709, help="koji par iz heat.pkl crtati (indeks prve nule; podrazumevano 6709)")
args = parser.parse_args()

d = np.load(args.scan); rel = d["rel"]
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(np.log10(rel), bins=80, color="#3b6ea5")
ax.set_xlabel("log10( vrh izmedju dva prolaska / medijana okoline )")
ax.set_ylabel("broj prolazaka")
ax.set_title(f"Zamah oscilatora Z(t) izmedju prolazaka kroz 0 (prvih {len(rel)+1} nula)")
for x, l in [(np.log10(0.00255), "6709/6710"), (np.log10(0.00298), "4765/4766")]:
    ax.axvline(x, color="red", lw=1)
    ax.text(x, ax.get_ylim()[1] * 0.8, " " + l, color="red", rotation=90, fontsize=8)
plt.tight_layout(); plt.savefig("raspodela_vrhova.png", dpi=130)
print("<1%:", (rel < 0.01).sum(), " <5%:", (rel < 0.05).sum(), " <10%:", (rel < 0.1).sum(), " ukupno:", len(rel))

res = pickle.load(open(args.heat, "rb"))
if args.par not in res:
    parser.error(f"par {args.par} nije u {args.heat}; dostupni: {sorted(res)}")
a, b, sc, traj = res[args.par]
fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
for s, rr in traj:
    for z in rr:
        col = "#3b6ea5" if abs(z.imag) < 1e-9 else "red"
        ax[0].plot(-4 * s * 1e4, z.real, "o", color=col, ms=4)
        ax[1].plot(-4 * s * 1e4, z.imag, "o", color=col, ms=4)
for A in ax:
    A.axvline(-4 * sc * 1e4, color="k", ls="--", lw=1); A.invert_xaxis()
    A.set_xlabel("dBN vreme t  (x 1e-4)   <-- glacanje")
ax[0].set_ylabel("polozaj nule (realni deo)"); ax[0].set_title(f"Nule {args.par} i {args.par+1}: priblizavanje i sudar")
ax[1].set_ylabel("imaginarni deo (odstupanje od linije)"); ax[1].set_title("Posle sudara: par napusta kriticnu liniju")
izlaz = "sudar_nula.png" if args.par == 6709 else f"sudar_nula_{args.par}_{args.par+1}.png"
plt.tight_layout(); plt.savefig(izlaz, dpi=130)
print(f"grafik: {izlaz}")
