"""Pretraga: visina vrha Z(t) izmedju uzastopnih prolazaka kroz 0.
Brzi Riemann-Siegel (glavna suma + C0 korekcija) za skeniranje,
pa precizna provera najtesnjih kandidata preko mpmath.siegelz."""
import numpy as np
import mpmath as mp
import sys

T_MIN, T_MAX, STEP = 14.0, float(sys.argv[1]) if len(sys.argv) > 1 else 7100.0, 0.005


def theta(t):
    return (t / 2) * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 \
        + 1 / (48 * t) + 7 / (5760 * t ** 3)


def Z_fast(t):
    a = np.sqrt(t / (2 * np.pi))
    N = np.floor(a).astype(int)
    p = a - N
    th = theta(t)
    out = np.zeros_like(t)
    for n in range(1, N.max() + 1):
        m = N >= n
        out[m] += np.cos(th[m] - t[m] * np.log(n)) / np.sqrt(n)
    out *= 2
    c = np.cos(2 * np.pi * p)
    c = np.where(np.abs(c) < 1e-9, 1e-9, c)
    C0 = np.cos(2 * np.pi * (p * p - p - 1 / 16)) / c
    out += (-1.0) ** (N - 1) * (t / (2 * np.pi)) ** -0.25 * C0
    return out


ts = np.arange(T_MIN, T_MAX, STEP)
Z = np.concatenate([Z_fast(ts[i:i + 200000]) for i in range(0, len(ts), 200000)])

sc = np.where(np.sign(Z[:-1]) != np.sign(Z[1:]))[0]
print(f"prolazaka kroz 0 nadjeno: {len(sc)}")
print(f"ocekivano (mpmath.nzeros({T_MAX:.0f})): {mp.nzeros(T_MAX)}")

# vrh izmedju uzastopnih prolazaka
peaks = np.array([np.abs(Z[sc[i] + 1:sc[i + 1] + 1]).max() for i in range(len(sc) - 1)])
# normalizacija: medijana vrhova u prozoru +-50
norm = np.array([np.median(peaks[max(0, i - 50):i + 51]) for i in range(len(peaks))])
rel = peaks / norm

# precizna provera 25 najtesnjih (po relativnoj visini)
mp.mp.dps = 20
order = np.argsort(rel)[:25]
print("\n rang |  nule (redni br.)  |   t_1       t_2     | vrh |Z| (tacno) | vrh / medijana okoline")
rows = []
for r, i in enumerate(order, 1):
    t1 = mp.findroot(mp.siegelz, (ts[sc[i]], ts[sc[i] + 1]), solver="anderson")
    t2 = mp.findroot(mp.siegelz, (ts[sc[i + 1]], ts[sc[i + 1] + 1]), solver="anderson")
    # tacan vrh: zlatni presek na |Z|
    f = lambda x: -abs(mp.siegelz(x))
    a, b = t1, t2
    g = (mp.sqrt(5) - 1) / 2
    for _ in range(40):
        c1, c2 = b - g * (b - a), a + g * (b - a)
        if f(c1) < f(c2):
            b = c2
        else:
            a = c1
    pk = abs(mp.siegelz((a + b) / 2))
    rows.append((i + 1, float(t1), float(t2), float(pk), float(pk / norm[i])))
    print(f" {r:3d}  | {i + 1:6d} i {i + 2:6d}  | {float(t1):9.4f} {float(t2):9.4f} | {float(pk):.6f} | {float(pk / norm[i]):.5f}")

np.savez("scan.npz", ts=ts, Z=Z, sc=sc, peaks=peaks, rel=rel)
