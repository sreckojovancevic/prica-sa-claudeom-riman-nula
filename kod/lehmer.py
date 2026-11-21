import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

mp.mp.dps = 25

# Klasican Lehmerov par: nule br. 6709 i 6710
z1 = mp.zetazero(6709).imag
z2 = mp.zetazero(6710).imag
print(f"nula 6709: t = {mp.nstr(z1, 15)}")
print(f"nula 6710: t = {mp.nstr(z2, 15)}")
print(f"razmak:     {mp.nstr(z2 - z1, 6)}")

# prosecan razmak oko te visine: 2*pi / log(t/2pi)
avg = 2 * mp.pi / mp.log(z1 / (2 * mp.pi))
print(f"prosecan razmak na toj visini: {mp.nstr(avg, 6)}")
print(f"odnos razmak/prosek: {mp.nstr((z2 - z1) / avg, 4)}")

# maksimum |Z| izmedju dve nule
mid_ts = [z1 + (z2 - z1) * k / 200 for k in range(201)]
zs = [mp.siegelz(t) for t in mid_ts]
peak = max(zs, key=lambda v: abs(v))
print(f"najveci |Z(t)| izmedju njih: {mp.nstr(abs(peak), 6)}")

# tipican vrh oscilacije u okolini (uporedjenje)
ts = [7000 + 10 * k / 2000 for k in range(2001)]
Z = [float(mp.siegelz(t)) for t in ts]
print(f"tipican max |Z| u [7000,7010]: {max(abs(v) for v in Z):.4f}")

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(ts, Z, lw=1)
ax[0].axhline(0, color="k", lw=0.6)
ax[0].axvspan(float(z1) - 0.1, float(z2) + 0.1, color="red", alpha=0.2)
ax[0].set_title("Z(t) za t u [7000, 7010] — Lehmerov par oznacen")
ax[0].set_xlabel("t")

ax[1].plot([float(t) for t in mid_ts], [float(v) for v in zs], lw=1.5, color="red")
ax[1].axhline(0, color="k", lw=0.6)
ax[1].set_title("Uvecano: izmedju nula 6709 i 6710")
ax[1].set_xlabel("t")
plt.tight_layout()
plt.savefig("lehmer_par.png", dpi=130)
