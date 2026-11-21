"""GUE poređenje za Dirihleovu beta funkciju sa 99% omotačem."""
import argparse
import numpy as np
import matplotlib.pyplot as plt

def generate_gue_spacings(target_count):
    N = 2000
    all_spacings = []
    current_count = 0
    # Ispravka: koristimo brojač umesto np.concatenate na praznoj listi
    while current_count < target_count:
        A = np.random.randn(N, N) + 1j * np.random.randn(N, N)
        H = (A + A.conj().T) / np.sqrt(2)
        evals = np.linalg.eigvalsh(H)
        mid_evals = evals[int(0.2*N):int(0.8*N)]
        spacings = np.diff(mid_evals)
        spacings = spacings / np.mean(spacings)
        all_spacings.append(spacings)
        current_count += len(spacings)
    return np.concatenate(all_spacings)[:target_count]

parser = argparse.ArgumentParser(description="GUE omotac za Dirihleove nule")
parser.add_argument("--input_file", default="dirichlet_scan.npz", help="Ulazni .npz")
parser.add_argument("--n_gue", type=int, default=400, help="Broj GUE realizacija za omotac")
parser.add_argument("--izlaz", default="dirichlet_gue_omotac.png", help="Izlazni grafik")
args = parser.parse_args()

np.random.seed(42)

data = np.load(args.input_file)
zeros = data['zeros']

# Razmaci nula (flatten pretvara listu torki u 1D niz)
riemann_spacings = np.diff(zeros.flatten())

# Normalizacija na srednju vrednost 1
riemann_s = riemann_spacings / np.mean(riemann_spacings)
print(f"Učitano {len(riemann_s)} Dirihleovih razmaka.")

# Generisanje GUE omotaca
print(f"Generisanje {args.n_gue} GUE nizova (ovo može potrajati ~10-20s)...")
gue_ks = []
for _ in range(args.n_gue):
    gue_s = generate_gue_spacings(len(riemann_s))
    all_s = np.sort(np.concatenate([riemann_s, gue_s]))
    cdf_riemann = np.searchsorted(np.sort(riemann_s), all_s, side='right') / len(riemann_s)
    cdf_gue = np.searchsorted(np.sort(gue_s), all_s, side='right') / len(gue_s)
    gue_ks.append(cdf_riemann - cdf_gue)

gue_ks = np.array(gue_ks)
percentile_99 = np.percentile(gue_ks, 99, axis=0)
percentile_1 = np.percentile(gue_ks, 1, axis=0)

# Razlika CDF za Dirihleove nule vs tačna GUE (prosečna referenca)
gue_s_ref = generate_gue_spacings(len(riemann_s))
all_s = np.sort(np.concatenate([riemann_s, gue_s_ref]))
cdf_riemann = np.searchsorted(np.sort(riemann_s), all_s, side='right') / len(riemann_s)
cdf_gue_ref = np.searchsorted(np.sort(gue_s_ref), all_s, side='right') / len(gue_s_ref)
diff = cdf_riemann - cdf_gue_ref

# Crtanje
fig, ax = plt.subplots(figsize=(12, 6))
ax.fill_between(all_s, percentile_1, percentile_99, color='gray', alpha=0.3, label='99% omotač (400 GUE)')
ax.plot(all_s, diff, 'b-', lw=1.5, label='Dirihleove nule - GUE')
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel("Normalizovani razmak s")
ax.set_ylabel("Razlika empirijske CDF")
ax.set_title(f"Da li je odstupanje Dirihleovih nula samo šum? (n = {len(riemann_s)})")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(args.izlaz, dpi=150)
print(f"Grafik sačuvan: {args.izlaz}")
