"""Z(t) oko para uzastopnih nula zeta funkcije: razmak, vrh izmedju nula, grafik."""
import argparse
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Z(t) oko para uzastopnih nula zeta funkcije")
parser.add_argument("--n1", type=int, default=6709, help="indeks prve nule (podrazumevano 6709)")
parser.add_argument("--n2", type=int, default=None, help="indeks druge nule (podrazumevano n1+1)")
parser.add_argument("--prozor", type=float, default=5.0, help="poluširina grafika oko sredine para (podrazumevano 5)")
parser.add_argument("--izlaz", default=None, help="ime PNG fajla (podrazumevano lehmer_par_N1_N2.png)")
args = parser.parse_args()

n1 = args.n1
n2 = args.n2 if args.n2 is not None else n1 + 1
if n1 < 1 or n2 <= n1:
    parser.error("mora vaziti 1 <= n1 < n2")
if args.prozor <= 0:
    parser.error("--prozor mora biti pozitivan")
izlaz = args.izlaz or f"lehmer_par_{n1}_{n2}.png"

mp.mp.dps = 25
z1 = mp.zetazero(n1).imag
z2 = mp.zetazero(n2).imag
print(f"nula {n1}: t = {mp.nstr(z1, 15)}")
print(f"nula {n2}: t = {mp.nstr(z2, 15)}")
print(f"razmak:     {mp.nstr(z2 - z1, 6)}")

avg = 2 * mp.pi / mp.log(z1 / (2 * mp.pi))
print(f"prosecan razmak na toj visini: {mp.nstr(avg, 6)}")
print(f"odnos razmak/prosek: {mp.nstr((z2 - z1) / avg, 4)}")

mid_ts = [z1 + (z2 - z1) * k / 200 for k in range(201)]
zs = [mp.siegelz(t) for t in mid_ts]
peak = max(zs, key=lambda v: abs(v))
print(f"najveci |Z(t)| izmedju njih: {mp.nstr(abs(peak), 6)}")

c = (z1 + z2) / 2
lo, hi = float(c) - args.prozor, float(c) + args.prozor
ts = [lo + (hi - lo) * k / 2000 for k in range(2001)]
Z = [float(mp.siegelz(t)) for t in ts]
print(f"najveci |Z| u prozoru [{lo:.2f}, {hi:.2f}]: {max(abs(v) for v in Z):.4f}")

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(ts, Z, lw=1)
ax[0].axhline(0, color="k", lw=0.6)
ax[0].axvspan(float(z1) - 0.1, float(z2) + 0.1, color="red", alpha=0.2)
ax[0].set_title(f"Z(t) za t u [{lo:.1f}, {hi:.1f}] — par {n1}/{n2} oznacen")
ax[0].set_xlabel("t")
ax[1].plot([float(t) for t in mid_ts], [float(v) for v in zs], lw=1.5, color="red")
ax[1].axhline(0, color="k", lw=0.6)
ax[1].set_title(f"Uvecano: izmedju nula {n1} i {n2}")
ax[1].set_xlabel("t")
plt.tight_layout()
plt.savefig(izlaz, dpi=130)
print(f"grafik: {izlaz}")
