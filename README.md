# Priča sa Claude-om oko Rimana i nule

Zapis jednog razgovora (21. novembar 2026) između Srećka Jovančevića i Claude-a (Anthropic) o nuli, fazi i Rimanovoj hipotezi, sa eksperimentima koji su tokom razgovora pokrenuti i sa svim rezultatima. Tu su i oni koji nisu potvrdili polazne pretpostavke.

> **Ovo nije dokaz Rimanove hipoteze ni pokušaj dokaza.** Numerika ne može da dokaže tvrdnju o beskonačno mnogo nula. Ovde se testira **konzistentnost** jednog postulata o nuli na poznatom problemu, i ponavljaju se poznati rezultati sopstvenim računom.

---

## Autori

- **Srećko Jovančević**: ideje, postulat, vođenje razgovora i eksperimenta, kritička pitanja ([github.com/sreckojovancevic](https://github.com/sreckojovancevic))
- **Claude** (Anthropic, model Claude Opus 5.5): matematičke i fizičke formulacije, kod, proračuni, grafici, tekst ovog README-a

---

## 1. Kako je počelo

Na TikTok-u se pojavljuju tvrdnje da je AI „rešio Rimanovu hipotezu“. To nije tačno. U avgustu 2026. Anthropic je objavio rad u kome neobjavljena istraživačka verzija Claude-a **nije** dokazala hipotezu. Pri pokušaju je poboljšala donju granicu udela nula zeta funkcije na kritičnoj liniji (sa 41,6 % na 67,2 % prema izveštajima), uz Lean formalizaciju. Taj rad nije deo ovog repozitorijuma i ovde se ne proverava.

Odatle je razgovor prešao na Srećkovo dugogodišnje pitanje: **šta je nula?**

## 2. Postulat i šta je od njega ostalo

**Polazni postulat (Srećko):** *0 je faza: stanje prelaza između negativnog i pozitivnog, a ne samo broj.*

Tokom razgovora postulat je preformulisan više puta. Tabela pokazuje sve verzije, i odbačene i one koje su ostale.

| Formulacija | Status | Zašto |
|---|---|---|
| „0 nije broj“ (jer nije deljiva sama sobom) | **odbačeno** | Relacija deljivosti važi: 0 deli 0 (0 = k·0). Nedefinisano je samo *deljenje* 0/0. Nula je broj u svakoj standardnoj strukturi. |
| „Na liniji leže prosti brojevi“ | **ispravljeno** | Na kritičnoj liniji leže **nule zeta funkcije**, a prosti brojevi su njihova „interferencijska slika“ (eksplicitna formula). |
| „0 je motor / transformator“ | **odbačeno u doslovnom obliku** | Nula ništa ne pokreće. Prelaz pokreće proces. Nula je mesto prelaza. |
| „0 rotira oko sebe“ | **odbačeno** | arg(0) nije definisan: 0·e^(iθ) = 0 za svako θ, pa nula nema fazu i ne može se okretati. |
| „Svaka promena stanja je rad“ | **odbačeno** | ΔU = Q + W (toplota i rad su različiti kanali). Slobodno širenje gasa: W = 0, Q = 0, a entropija raste. |
| „Entropija je izmena stanja“ | **ispravljeno** | Entropija je *funkcija* stanja. Izmena je ΔS. |
| „Entropija teži 0“ | **ispravljeno** | Samo kad T → 0 (treći zakon). U izolovanom sistemu entropija raste (drugi zakon). |
| „Entropija ima i negativnu stranu“ | **klasično ne, kvantno delimično** | S = k·ln W ≥ 0 jer W ≥ 1. Ali uslovna kvantna entropija Bell stanja je S(A\|B) = −1 bit. |
| „Kroz 0 K se prolazi iz + u −“ | **odbačeno** | Prelaz na negativne temperature ide kroz ±∞, ne kroz 0 K. U β = 1/kT prolazi kroz β = 0. |
| „1 → −1 mora proći kroz 0“ | **uslovno tačno** | Tačno za neprekidan prelaz po realnoj osi (Bolcano). Netačno u kompleksnoj ravni (put po krugu ne dodiruje 0) i za diskretan skok. |
| „0 sudar uzme i vrati sebi“ | **odbačeno eksperimentom** | Posle sudara obe nule i dalje postoje, samo napuštaju liniju (eksperiment 5). Broj nula je očuvan. |
| „0 sama po sebi ima kretanje“ | **nije pokazano** | Kretale su se nule *funkcija* pri promeni funkcije, a vrednost 0 je stajala kao referenca. |
| **0 je prag** između + i − | **stoji** | Bolcano, Z(t) kod Rimana, AC napon, parametar uređenja kod faznih prelaza. |
| **0 je centar faze** | **stoji** | U nuli se sustiču sve faze. Fazni vrtlozi u fizici, princip argumenta u matematici. |
| **0 je osnovni mod oscilacije** | **stoji** | Broj n kao oscilacija e^(inθ). n = 0 je mod bez okretanja (DC komponenta). |
| **Nule su neuništive** | **stoji (teorema)** | Nula je fazni vrtlog sa celobrojnim namotajem +1, a ceo broj se ne menja neprekidno. Kod analitičkih funkcija ne postoje „anti-nule“ koje bi ih poništile. |
| **0 je referentna tačka i početak** | **stoji** | Završna formulacija razgovora: nula stoji dok se sadržaj kreće u odnosu na nju. |

**Završni oblik:** *nula je referentna tačka i početak; nepomičan okvir u odnosu na koji se definiše svaka promena; ono oko čega se faza okreće i kroz šta amplituda menja znak.*

Formalno jezgro: **0 je element koji ništa ne menja (a + 0 = a)**. Ostale osobine (0·a = 0 itd.) slede iz toga u kombinaciji sa ostatkom strukture.

## 3. Rimanova hipoteza tvojim jezikom

- Na kritičnoj liniji zeta se može napisati kao **realna** funkcija Z(t) = e^(iθ(t))·ζ(½+it). Z(t) je **linijski oscilator**: ide na + i −.
- Svaka nula na liniji je **prolazak Z(t) kroz 0**.
- U pomerenim koordinatama w = s − ½ ogledalo s ↔ 1−s postaje w ↔ −w, a hipoteza glasi: *sve netrivijalne nule imaju realni deo tačno 0, na pragu između + i − strane.*

Ovo je **preformulacija, ne dokaz**. Centriranje ogledala na nulu je izbor koordinata, odnosno konvencija.

### Model: lenjir kroz prsten (Srećko)

Prsten stoji, a kroz njegovu rupu se gura lenjir, odnosno brojevna prava. Ispred prstena su pozitivni podeoci, a sa druge strane izlaze negativni. Lenjir ne dodiruje prsten, nego prolazi kroz rupu. Prsten je nacrtan kao znak „0“.

Šta model tačno pokazuje:
- **Prsten je prag i referenca.** Deli prostor na „pre“ i „posle“ i u svakom trenutku pokazuje koji podeok je na pragu. Bez njega ne postoje ni + ni −, jer znak postoji samo u odnosu na nulu.
- **Neprekidan prelaz iz + u − mora kroz rupu** (Bolcano u fizičkom obliku).
- **Oba mehanizma promene znaka su prisutna istovremeno:** prsten je *krug oko nule* (faza, rotacija), a lenjir je *prava kroz nulu* (amplituda, promena znaka). To je kompleksna ravan: jedinični krug i realna osa kroz njegov centar.
- Lenjir kroz rupu prolazi trenutno, bez zadržavanja. Nula je stanje bez trajanja (skup trenutaka u kojima je sin t = 0 ima meru nula).

Ograde koje su ostale posle razgovora:
- **Prsten ne gura.** Gura ruka, odnosno proces. Prsten je fiksan, a lenjir se kreće.
- **Prsten „pokazuje transformaciju“, ali je ne vrši.** Podeoci su na lenjiru bili negativni i pre prolaska. Prsten obeležava granicu, a ne pretvara + u −.
- To što znak 0 liči na prsten je istorijska slučajnost: indijski znak za nulu je prvo bio **tačka** (bindu).

Kao nastavna analogija model je konkretan (može se napraviti od kartona) i pokazuje i prelaz kroz nulu i ulogu nule kao praga.

---

## 4. Eksperimenti

Svi brojevi su iz skripti u `kod/`. Grafici su u `grafici/`.

### Eksperiment 1: Lemerov par 6709/6710 (`lehmer.py`)

| | vrednost |
|---|---|
| nula 6709 | t = 7005,06287 |
| nula 6710 | t = 7005,10056 |
| razmak | 0,0377 (4,2 % prosečnog razmaka 0,8955) |
| najveći \|Z\| između njih | 0,00397 |
| tipičan vrh u okolini | oko 7,6 |

Oscilator jedva proviri preko nule, a zatim se vrati. Grafik: `grafici/lehmer_par.png`.

### Eksperiment 2: svi prolasci do t = 7100 (`scan.py`)

Brza Riman–Zigelova formula (glavna suma + C0 korekcija) na mreži koraka 0,005, a najtesniji kandidati su ponovo izračunati preciznim `mpmath.siegelz`.

- Pronađeno **6814 prolazaka kroz 0**. `mpmath.nzeros(7100)` = **6814**. Sve nule u ovom opsegu su na liniji (poznato je da hipoteza važi znatno dalje od ove visine), a poklapanje broja isključuje da je pretraga preskočila par.
- Najtesniji prolasci (vrh / medijana okoline): 6709/6710 **0,26 %**, 4765/4766 **0,30 %**, 3777/3778 0,57 %, 4510/4511 0,81 %, 4087/4088 0,83 %.
- Od 6813 prolazaka: 5 ispod 1 %, 45 ispod 5 %, 125 ispod 10 %.
- Klasični Lemerov par 6709/6710 algoritam je sam našao na prvom mestu.

Grafik: `grafici/raspodela_vrhova.png`.

### Eksperiment 3: obrazac oko tesnih prolazaka (`pattern.py`)

Predviđanje je zapisano **pre** merenja.

| Predviđanje | Rezultat |
|---|---|
| Susedi tesnog prolaska imaju **veći zamah** („nadoknada“) | **NIJE POTVRĐENO.** Susedi 1,51 i 1,64 naspram proseka 1,45, ali kontrola sa 2000 nasumičnih skupova daje isto toliko (granica 99,9 % je 2,10). |
| Susedni **razmaci** su veći | **POTVRĐENO.** Par je na 17,5 % prosečnog razmaka, a susedni razmaci su 1,30 i 1,30. Kontrola daje 1,00, granica 99,9 % je 1,18. |
| Tesni prolasci su raspoređeni bez trenda po visini | **Uglavnom potvrđeno.** Ispod t ≈ 1000 nema nijednog, iznad toga udeo je stabilan, 0,6–0,85 %. |

Zbir tri razmaka oko tesnog para je oko 2,78 (očekivano 3). Prostor se uglavnom čuva, samo se preraspodeli. To je **odbijanje nula** (level repulsion). Grafik: `grafici/obrazac_oko_tesnih.png`.

### Eksperiment 4: GUE ili Poason (`gue.py`)

6164 razmaka (nule iznad t = 1000), normalizovana preko Riman–fon Mangoltove gustine.

| | izmereno | GUE (Vignerova aproksimacija) | Poason |
|---|---|---|---|
| razmaci < 0,1 | 0,08 % | 0,11 % | 9,5 % |
| razmaci < 0,3 | 1,67 % | 2,73 % | 25,9 % |
| KS rastojanje | – | 0,0276 | 0,3073 |

- Nule su oko 11 puta bliže GUE nego nezavisnim tačkama. Montgomerijeva par-korelacija 1 − (sin πx/πx)² se vizuelno poklapa.
- **Formalni test savršenog slaganja PADA:** KS rastojanje 0,0276 je iznad kritične vrednosti 0,0208 (p = 0,01). Verovatni razlozi: (1) korišćena je Vignerova aproksimacija (2×2 matrice), a ne tačna GUE raspodela (razlika oko 1–2 %); (2) poznate korekcije konačne visine (Bogomolni–Kiting). **Ovo nije provereno** i ostaje kao otvoren korak.

Grafik: `grafici/gue_poredjenje.png`.

### Eksperiment 5: toplotni tok i sudar nula (`heatflow.py`)

Lokalni model de Brejn–Njumanovog toplotnog toka: Ξ se oko para aproksimira Čebiševljevim polinomom stepena 26, pa se exp(s·D²) primeni tačno. Smer t < 0 je glačanje (difuzija).

| par | razmak | sudar pri dBN vremenu t | gruba formula d²/8 |
|---|---|---|---|
| 6709/6710 (Lemer) | 0,0377 | −7,11·10⁻⁴ | slaže se |
| 4765/4766 (Lemer) | 0,0433 | −9,37·10⁻⁴ | slaže se |
| 6700/6701 (običan, kontrola) | 0,92 | oko −1,4 | **ne slaže se; prozor modela je premali, rezultat je samo gruba procena** |

Posle sudara par napušta liniju kao konjugovani par (jedna nula gore, druga dole). Nule ne nestaju. Grafik: `grafici/sudar_nula.png`.

**Ograde:** ovo je lokalni, nerigorozan model. Ne daje stvarnu granicu za Λ. Rigorozne donje granice dobijene ovom logikom su mnogo bolje (Čordaš, Odlizko, Smit, Varga 1993: −5,9·10⁻⁹; Sauter, Gurdon, Demišel 2011: −1,15·10⁻¹¹), a Rogers i Tao su 2018. dokazali Λ ≥ 0.

---

## 5. Greške i ispravke tokom razgovora

Zapisano radi proverljivosti, sa obe strane.

**Claude-ove greške:**
- Rečenicu „eto ti dokaza da je nula faza“, za koju je Srećko rekao da ju je Claude izgovorio u ranijem razgovoru, Claude nije našao pretragom prethodnih razgovora. U jedinom pronađenom razgovoru na tu temu (jun 2026) Claude je tvrdio suprotno. Nije isključeno da postoji razgovor koji pretraga nije našla.
- Claude je u jednom trenutku išao „prebrzo i preširoko“ (više opcija odjednom). Na Srećkov zahtev nastavljeno je korak po korak.
- Claude je broj kao oscilaciju prvo predstavio rotacijom e^(inθ). Na Srećkov zahtev prešlo se na linijsku oscilaciju. Pri tome je ispravljeno i to da se kod linijske oscilacije u 0 menja **strana**, a ne smer kretanja.
- Claude je svoj lokalni model nazvao „prenosni model“, što je bila nejasna reč. Ispravno je „lokalni model“.
- Prvo pokretanje `pattern.py` sadržalo je nečitku liniju koda. Ispravljena je pre objave, a rezultat se nije promenio.

**Srećkove pretpostavke koje nisu prošle** navedene su u tabeli u odeljku 2.

## 6. Otvoreno

- Ponoviti eksperiment 4 sa **tačnom** GUE raspodelom umesto Vignerove aproksimacije i proveriti da li odstupanje KS testa nestaje.
- Eksperiment 5 sa većim prozorom za obične parove.
- Proširiti eksperiment 2 na veće visine (zahteva bržu implementaciju).
- Postulat „0 je referentna tačka i početak“ formulisati tako da daje **proverljivo predviđanje** koje ne sledi iz postojeće teorije. Bez toga ostaje dobar jezik za opis, ali ne i nova teorija.

---

## 7. Pokretanje

```bash
pip install -r requirements.txt
cd kod
python3 lehmer.py            # eksperiment 1  -> lehmer_par.png        (~30 s)
python3 scan.py 7100         # eksperiment 2  -> scan.npz, tabela      (~45 s)
python3 pattern.py           # eksperiment 3  (treba scan.npz)
python3 gue.py               # eksperiment 4  (treba scan.npz)
python3 heatflow.py          # eksperiment 5  -> heat.pkl              (~30 s)
python3 grafici_dodatni.py   # raspodela_vrhova.png, sudar_nula.png
```

Kontrole koriste fiksni seed (42). Svi rezultati u ovom README-u su ponovljeni pokretanjem iz praznog foldera.

## 8. Literatura i izvori

- B. Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859)
- D. H. Lehmer, *On the roots of the Riemann zeta-function*, Acta Math. 95 (1956)
- H. L. Montgomery, *The pair correlation of zeros of the zeta function* (1973)
- A. M. Odlyzko, *On the distribution of spacings between zeros of the zeta function*, Math. Comp. 48 (1987)
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann Hypothesis*, Constr. Approx. 10 (1994)
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), [arXiv:1801.05914](https://arxiv.org/abs/1801.05914)
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, [arXiv:1904.12438](https://arxiv.org/abs/1904.12438)
- Nerecenzirane 2026. tvrdnje o gornjoj granici Λ (navedene radi konteksta, **nisu proverene**): J. Gomila, Λ ≤ 0,1787854 (avg. 2026); [arXiv:2611.06245](https://arxiv.org/abs/2611.06245), Λ < 0,156821
- Anthropic, *Riemann zeta* (avgust 2026), [anthropic.com/research/riemann-zeta](https://www.anthropic.com/research/riemann-zeta)
- G. Frege, *Die Grundlagen der Arithmetik* (1884): broj kao osobina pojma
- Brahmagupta, *Brāhmasphuṭasiddhānta* (628): pravila za nulu, imetak i dug

## Zahvalnice

Ovaj rad je nastao u zajedničkom razgovoru Srećka Jovančevića i **Claude-a** (Anthropic, Claude Opus 5.5). Claude je napisao kod, izvršio proračune, napravio grafike i sastavio ovaj tekst. Srećko je postavio postulat, vodio pravac eksperimenta i insistirao na tome da se prikaže sve, a ne samo ono što radi.
