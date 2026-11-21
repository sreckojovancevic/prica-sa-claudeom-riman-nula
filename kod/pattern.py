"""Obrazac oko tesnih prolazaka: zamah i razmak suseda, sa nasumicnom kontrolom."""
import argparse
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Zamah i razmak oko tesnih prolazaka Z(t) kroz 0")
parser.add_argument("--ulaz", default="scan.npz", help="izlaz skripte scan.py (podrazumevano scan.npz)")
parser.add_argument("--prag", type=float, default=0.05, help="tesan prolazak: vrh/medijana ispod praga (podrazumevano 0.05)")
parser.add_argument("--seed", type=int, default=42, help="seed za nasumicnu kontrolu (podrazumevano 42)")
parser.add_argument("--izlaz", default="obrazac_oko_tesnih.png", help="ime grafika")
args = parser.parse_args()
if not (0 < args.prag < 1):
    parser.error("--prag mora biti izmedju 0 i 1")

d = np.load(args.ulaz); ts, Z, sc, peaks, rel = d["ts"], d["Z"], d["sc"], d["peaks"], d["rel"]
# tacnije pozicije nula: linearna interpolacija na mrezi
z = ts[sc] - Z[sc] * (ts[sc+1] - ts[sc]) / (Z[sc+1] - Z[sc])
gap = np.diff(z)                               # gap[i] = razmak nula i, i+1  (prolazak i)
avg = 2*np.pi/np.log(((z[:-1]+z[1:])/2)/(2*np.pi))
g = gap/avg                                    # normalizovan razmak (prosek ~1)

valid = np.arange(3, len(rel)-3)
tight = valid[rel[valid] < args.prag]
print(f"tesnih prolazaka (zamah < {100*args.prag:g}%): {len(tight)}\n")
print("pozicija u odnosu na tesni |  prosecan zamah (rel) | prosecan razmak (norm.)")
for k in (-3,-2,-1,0,1,2,3):
    print(f"   {k:+d}                     |   {rel[tight+k].mean():6.3f}             |   {g[tight+k].mean():5.3f}")
print(f"\n  svi prolasci (osnova)     |   {rel[valid].mean():6.3f}             |   {g[valid].mean():5.3f}")

# kontrola: da li je efekat slucajan? -- nasumicni skupovi iste velicine
rng = np.random.default_rng(args.seed)
sims = [rel[rng.choice(valid, len(tight), replace=False)+1].mean() for _ in range(2000)]
s = np.array(sims)
print(f"\nkontrola: zamah suseda +1 kod {len(tight)} nasumicnih prolazaka: prosek {s.mean():.3f}, 99.9 pct {np.percentile(s,99.9):.3f}")
for k in (-1, 1):
    sg = np.array([g[rng.choice(valid, len(tight), replace=False)+k].mean() for _ in range(5000)])
    print(f"kontrola razmak {k:+d}: tesni {g[tight+k].mean():.3f} | nasumicno {sg.mean():.3f}, 99.9 pct {np.percentile(sg,99.9):.3f}")

# raspodela po visini t: udeo tesnih po prozorima
bins = np.linspace(z[0], z[-1], 8)
idx = np.digitize(z[tight], bins); idx_all = np.digitize(z[valid], bins)
print("\nudeo tesnih po visini t:")
for b in range(1, len(bins)):
    n_t = (idx == b).sum(); n_a = (idx_all == b).sum()
    print(f"  t {bins[b-1]:6.0f}-{bins[b]:6.0f}: {n_t:3d} / {n_a:4d} = {100*n_t/n_a:.2f}%")

# grafik: prosecan profil oko tesnih
ks = np.arange(-6, 7)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].bar(ks, [rel[np.clip(tight+k,0,len(rel)-1)].mean() for k in ks], color="#3b6ea5")
ax[0].axhline(rel[valid].mean(), color="red", lw=1, label="prosek svih")
ax[0].set_xlabel("pozicija u odnosu na tesni prolazak"); ax[0].set_ylabel("prosecan zamah (rel.)")
ax[0].set_title("Zamah oscilatora oko tesnih prolazaka"); ax[0].legend()
ax[1].bar(ks, [g[np.clip(tight+k,0,len(g)-1)].mean() for k in ks], color="#5a9e6f")
ax[1].axhline(1, color="red", lw=1, label="prosecan razmak = 1")
ax[1].set_xlabel("pozicija u odnosu na tesni prolazak"); ax[1].set_ylabel("razmak nula (norm.)")
ax[1].set_title("Razmak izmedju nula oko tesnih prolazaka"); ax[1].legend()
plt.tight_layout(); plt.savefig(args.izlaz, dpi=130); print(f"grafik: {args.izlaz}")
