"""Lokalni toplotni tok de Bruijn-Newman tipa oko para nula.
H_t(gamma) = exp(-(t/4) d^2/dgamma^2) Xi(gamma)   (x = 2*gamma u dBN konvenciji)
t < 0  ->  obicna difuzija (izglacavanje): mali vrh izmedju nula nestaje, nule se sudaraju.
Lokalno: Xi se aproksimira Cebisevljevim polinomom, pa je exp(s D^2) p tacno (konacna suma)."""
import argparse
import pickle
import numpy as np
import mpmath as mp
from numpy.polynomial import Chebyshev as C

mp.mp.dps = 20


def Xi_local(gs, g0):
    # Xi(g) = -(1/2)(g^2+1/4) pi^(-1/4) |Gamma(1/4+ig/2)| Z(g); normalizacija na g0
    lg0 = mp.re(mp.loggamma(mp.mpf(1) / 4 + 0.5j * g0)) + mp.log(g0 ** 2 + 0.25)
    out = []
    for g in gs:
        lg = mp.re(mp.loggamma(mp.mpf(1) / 4 + 0.5j * g)) + mp.log(g ** 2 + 0.25)
        out.append(float(-mp.exp(lg - lg0) * mp.siegelz(g)))
    return np.array(out)


def collide(n1, label, half=1.6, deg=26):
    a = float(mp.zetazero(n1).imag); b = float(mp.zetazero(n1 + 1).imag)
    c = (a + b) / 2
    gs = np.linspace(c - half, c + half, 500)
    p = C.fit(gs, Xi_local(gs, c), deg)

    def p_s(s):  # exp(s D^2) p
        out, term, k = p, p, 0
        while True:
            k += 1
            term = term.deriv(2) * (s / k)
            if np.max(np.abs(term.coef)) < 1e-14 * np.max(np.abs(out.coef)) or k > deg:
                break
            out = out + term
        return out

    def pair_roots(s):
        r = p_s(s).roots()
        return sorted(r[np.abs(r - c) < 0.6 * (b - a) + 0.05], key=lambda z: z.real)

    # bisekcija: najmanje s pri kome par postaje kompleksan
    lo, hi = 0.0, (b - a) ** 2  # hi sigurno dovoljno
    for _ in range(60):
        mid = (lo + hi) / 2
        rr = pair_roots(mid)
        if any(abs(z.imag) > 1e-9 for z in rr):
            hi = mid
        else:
            lo = mid
    s_c = hi
    print(f"{label}: nule {n1}/{n1+1}, razmak {b-a:.4f}")
    print(f"   sudar pri s = {s_c:.3e}  ->  dBN vreme t = {-4*s_c:.3e}"
          f"   (gruba procena d^2/8 = {(b-a)**2/8:.3e})")
    traj = []
    for s in np.linspace(0, 1.6 * s_c, 33):
        traj.append((s, pair_roots(s)))
    return a, b, s_c, traj


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lokalni toplotni tok: kada se par uzastopnih nula sudari")
    parser.add_argument("--parovi", default="6709,4765,6700",
                        help="indeksi prve nule svakog para, odvojeni zarezom (par je n1, n1+1); podrazumevano 6709,4765,6700")
    parser.add_argument("--polusirina", type=float, default=1.6, help="poluširina prozora polinomne aproksimacije (podrazumevano 1.6)")
    parser.add_argument("--stepen", type=int, default=26, help="stepen Cebisevljevog polinoma (podrazumevano 26)")
    parser.add_argument("--izlaz", default="heat.pkl", help="izlazni .pkl (podrazumevano heat.pkl)")
    args = parser.parse_args()
    try:
        parovi = [int(x) for x in args.parovi.split(",") if x.strip()]
    except ValueError:
        parser.error("--parovi mora biti lista celih brojeva, npr. 6709,4765")
    if not parovi or min(parovi) < 1 or args.polusirina <= 0 or args.stepen < 4:
        parser.error("neispravni argumenti (n1 >= 1, polusirina > 0, stepen >= 4)")
    res = {}
    for n1 in parovi:
        res[n1] = collide(n1, f"par {n1}/{n1+1}", half=args.polusirina, deg=args.stepen)
    pickle.dump(res, open(args.izlaz, "wb"))
    print(f"\nsacuvano: {args.izlaz}")
