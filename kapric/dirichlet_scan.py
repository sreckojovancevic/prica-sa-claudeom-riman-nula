"""Skeniranje nula Dirihleove beta funkcije L(s, chi_4).
beta(s) = 4^-s * (zeta(s, 1/4) - zeta(s, 3/4))
Hardijeva Z-funkcija: Z_beta(t) = Re[ exp(i*theta(t)) * beta(1/2 + it) ]
gde je theta(t) = arg(Gamma(1/4 + it/2)) - (t/2)*ln(pi/4)."""

import argparse
import numpy as np
import mpmath as mp

parser = argparse.ArgumentParser(description="Skeniranje nula Dirihleove beta funkcije")
parser.add_argument("--t-max", type=float, default=1000.0, help="gornja granica za t (podrazumevano 1000)")
parser.add_argument("--t-min", type=float, default=10.0, help="donja granica za t (podrazumevano 10)")
parser.add_argument("--korak", type=float, default=0.02, help="korak mreze (podrazumevano 0.02)")
parser.add_argument("--top", type=int, default=25, help="koliko najtesnjih prolazaka precizno proveriti")
parser.add_argument("--izlaz", default="dirichlet_scan.npz", help="izlazni .npz fajl")
args = parser.parse_args()

if not (0 < args.t_min < args.t_max):
    parser.error("mora vaziti 0 < t-min < t-max")

mp.mp.dps = 20

def Z_beta(t):
    """Hardijeva Z-funkcija za Dirihleovu beta funkciju."""
    s = 0.5 + 1j * t
    # beta(s) preko Huroviceve zete
    beta_s = mp.power(4, -s) * (mp.zeta(s, 0.25) - mp.zeta(s, 0.75))
    # Fazni faktor
    theta = mp.arg(mp.gamma(0.25 + 0.5j * t)) - 0.5 * t * mp.log(mp.pi / 4)
    return mp.re(mp.exp(1j * theta) * beta_s)

# 1. Grubo skeniranje
print(f"Skeniranje Z_beta(t) od {args.t_min} do {args.t_max}...")
ts = np.arange(args.t_min, args.t_max, args.korak)
Z = np.array([float(Z_beta(t)) for t in ts])

sc = np.where(np.sign(Z[:-1]) != np.sign(Z[1:]))[0]
print(f"Pronadjeno {len(sc)} kandidata za prolazak kroz 0.")

# 2. Precizno nalaženje nula i vrhova
mp.mp.dps = 25
peaks = []
zeros = []

print("Precizna provera i racunanje vrhova...")
for i in range(len(sc) - 1):
    t1 = mp.findroot(Z_beta, (ts[sc[i]], ts[sc[i] + 1]), solver="anderson")
    t2 = mp.findroot(Z_beta, (ts[sc[i+1]], ts[sc[i+1] + 1]), solver="anderson")
    zeros.append((float(t1), float(t2)))
    
    # Zlatni presek za vrh
    f = lambda x: -abs(Z_beta(x))
    a, b = t1, t2
    g = (mp.sqrt(5) - 1) / 2
    for _ in range(40):
        c1, c2 = b - g * (b - a), a + g * (b - a)
        if f(c1) < f(c2): b = c2
        else: a = c1
    pk = abs(Z_beta((a + b) / 2))
    peaks.append(float(pk))

peaks = np.array(peaks)
# Normalizacija vrhova (medijana u prozoru +-50)
norm = np.array([np.median(peaks[max(0, i - 50):i + 51]) for i in range(len(peaks))])
rel = peaks / norm

# Ispis najtesnjih
order = np.argsort(rel)[:args.top]
print(f"\n{'rang':>4} | {'nule (redni br.)':>15} | {'vrh |Z|':>10} | {'vrh / medijana':>15}")
for r, i in enumerate(order, 1):
    t1, t2 = zeros[i]
    print(f" {r:3d}  | {i+1:6d} i {i+2:6d}  | {peaks[i]:10.6f} | {rel[i]:15.5f}")

# Cuvanje
zeros_arr = np.array(zeros)
np.savez(args.izlaz, ts=ts, Z=Z, sc=sc, zeros=zeros_arr, peaks=peaks, rel=rel)
print(f"\nSacuvano: {args.izlaz}")
