# Priča sa Claude-om oko Rimana i nule

Zapis jednog razgovora (21. novembar 2026) između Srećka Jovančevića i Claude-a (Anthropic) o nuli, fazi i Rimanovoj hipotezi, sa eksperimentima koji su tokom razgovora pokrenuti i sa svim rezultatima. Tu su i oni koji nisu potvrdili polazne pretpostavke.

> **Ovo nije dokaz Rimanove hipoteze ni pokušaj dokaza.** Numerika ne može da dokaže tvrdnju o beskonačno mnogo nula. Ovde se testira **konzistentnost** jednog postulata o nuli na poznatom problemu, i ponavljaju se poznati rezultati sopstvenim računom.

---

## Autori

- **Srećko Jovančević**: ideje, postulat, vođenje razgovora i eksperimenta, kritička pitanja ([github.com/sreckojovancevic](https://github.com/sreckojovancevic))
- **Claude** (Anthropic, model Claude Opus 5.5): matematičke i fizičke formulacije, kod, proračuni, grafici, tekst ovog README-a, kritička provera spoljnih predloga
- **Qwen** (Alibaba): dinamičko čitanje Ojlerove formule i „nula kao seme razvoja“ (odeljak 8), predlog argumenata komandne linije (argparse) za sve skripte, predlog dvouzoračkog KS testa sa numeričkom GUE raspodelom, tumačenje grafika i razrada termina „oscilatorne kontrakcije nule“ (eksperiment 4b), doneto iz Srećkovih razgovora sa tim modelom

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

**Proširenje do t = 25000** (`python3 scan.py --t-max 25000 --izlaz scan25k.npz`):
- **29002 prolaska = 29002 nule** (`mpmath.nzeros(25000)`). I u ovom opsegu sve nule su na liniji i nijedan par nije preskočen.
- Novi najtesniji prolazak: **18859/18860, vrh 0,14 %** okoline (|Z| = 0,00215), oko dva puta tesnije od 6709/6710. Zatim 25095/25096 (0,25 %), 6709/6710 (0,26 %), 24199/24200 (0,27 %).

### Eksperiment 3: obrazac oko tesnih prolazaka (`pattern.py`)

Predviđanje je zapisano **pre** merenja.

| Predviđanje | Rezultat |
|---|---|
| Susedi tesnog prolaska imaju **veći zamah** („nadoknada“) | **NIJE POTVRĐENO.** Susedi 1,51 i 1,64 naspram proseka 1,45, ali kontrola sa 2000 nasumičnih skupova daje isto toliko (granica 99,9 % je 2,10). |
| Susedni **razmaci** su veći | **POTVRĐENO.** Par je na 17,5 % prosečnog razmaka, a susedni razmaci su 1,30 i 1,30. Kontrola daje 1,00, granica 99,9 % je 1,18. |
| Tesni prolasci su raspoređeni bez trenda po visini | ~~Uglavnom potvrđeno~~ **OBORENO na većem uzorku** (vidi ispod). Do t = 7100: ispod t ≈ 1000 nema nijednog, iznad toga 0,6–0,85 %. |

Zbir tri razmaka oko tesnog para je oko 2,78 (očekivano 3). Prostor se uglavnom čuva, samo se preraspodeli. To je **odbijanje nula** (level repulsion). Grafik: `grafici/obrazac_oko_tesnih.png`.

**Ponovljeno do t = 25000** (257 tesnih prolazaka, `--ulaz scan25k.npz`):

| | rezultat | kontrola (nasumično) |
|---|---|---|
| zamah suseda −1 / +1 | 1,47 / 1,39 (prosek svih 1,52) | +1: 1,52, gornja granica 99,9 % 1,82 → **opet bez efekta** (čak malo ispod proseka) |
| razmak suseda −1 / +1 | **1,30 / 1,26** | 1,00, granica 99,9 % 1,08 → **opet potvrđeno**, sada sa mnogo većom sigurnošću |
| udeo tesnih po visini | 0,46 % → 0,81 % → 0,83 % → 0,81 % → 1,01 % → 1,01 % → **1,12 %** (t od 14 do 25000) | — |

**Ispravka zaključka:** udeo tesnih prolazaka **raste sa visinom** (oko 2,4 puta od najnižeg do najvišeg dela). Na prvih 6814 nula trend se nije video. To se slaže sa eksperimentom 4b: na nižim visinama nule su pravilnije od GUE, pa su mali razmaci (i tesni prolasci) ređi. Grafik: `grafici/obrazac_oko_tesnih_25k.png`.

### Eksperiment 4: GUE ili Poason (`gue.py`)

6164 razmaka (nule iznad t = 1000), normalizovana preko Riman–fon Mangoltove gustine.

| | izmereno | GUE (Vignerova aproksimacija) | Poason |
|---|---|---|---|
| razmaci < 0,1 | 0,08 % | 0,11 % | 9,5 % |
| razmaci < 0,3 | 1,67 % | 2,73 % | 25,9 % |
| KS rastojanje | – | 0,0276 | 0,3073 |

- Nule su oko 11 puta bliže GUE nego nezavisnim tačkama. Montgomerijeva par-korelacija 1 − (sin πx/πx)² se vizuelno poklapa.
- **Formalni test savršenog slaganja PADA:** KS rastojanje 0,0276 je iznad kritične vrednosti 0,0208 (p = 0,01). Tada predloženi razlozi: (1) Vignerova aproksimacija umesto tačne GUE raspodele; (2) korekcije konačne visine. Razlog (1) je u 4b **oboren**, a (2) je u skladu sa podacima, ali nije direktno proveren.

Grafik: `grafici/gue_poredjenje.png`.

### Eksperiment 4b: tačna GUE raspodela (`gue_tacno.py`, `gue_omotac.py`)

**Šta je urađeno:**
- **Tačna GUE raspodela razmaka** preko Fredholmove determinante sine-jezgra, E(s) = det(I − K_s), F(s) = 1 + E′(s) (Bornemanov metod, 60 Gaus–Ležandrovih čvorova). Nema aproksimacije ni šuma uzorkovanja.
- **Nezavisna provera formule:** 200000 razmaka iz simuliranih GUE matrica (tridijagonalni model Dumitriu–Edelman, β = 2, N = 4000, sredina spektra odmotana preko polukruga) slaže se sa tačnom formulom: KS 0,0023 uz klasičnu granicu 0,0036. Od Vignerove aproksimacije se razlikuje (0,0038). Dve nezavisne metode potvrđuju jedna drugu.
- **Kalibrisana granica:** razmaci nula (i GUE nivoa) nisu nezavisni, pa klasična KS granica ne važi. Zato je KS izračunat i za 400 pravih GUE nizova iste dužine, a njihov 99. percentil je stvarna granica slučajnosti.

**Predviđanja zapisana pre merenja:**
- *predlog Qwen-a:* KS prema tačnoj GUE oko 0,015–0,018, ispod granice, pa bi „prethodni neuspeh bio isključivo zbog Vignerove aproksimacije“;
- *Claude:* KS će pasti, ali verovatno ostati iznad kalibrisane granice zbog korekcija konačne visine, uz manje odstupanje na većim visinama.

**Rezultati:**

| | t 1000–7100 (n = 6165) | t 1000–25000 (n = 28353) |
|---|---|---|
| KS prema Vignerovoj aproksimaciji | 0,0278 | 0,0233 |
| **KS prema tačnoj GUE** | **0,0293** | **0,0247** |
| klasična granica p = 0,01 (nezavisnost) | 0,0207 | 0,0097 |
| **kalibrisana granica** (99. percentil, 400 GUE nizova) | **0,0143** | **0,0064** |
| empirijski p | ≤ 0,0025 (nijedan od 400 nizova) | ≤ 0,0025 |

Po visini (t 1000–25000, četiri jednaka dela, kalibracija 200 nizova po delu):

| t | KS prema tačnoj GUE | GUE granica 99 % |
|---|---|---|
| 1001–7918 | 0,0290 | 0,0130 |
| 7918–13899 | 0,0244 | 0,0129 |
| 13899–19549 | 0,0245 | 0,0123 |
| 19549–24999 | 0,0241 | 0,0142 |

**Zaključci:**
1. **Predviđanje iz spoljnog predloga je oboreno.** KS prema tačnoj GUE je *veći* od KS prema Vigneru (0,0293 naspram 0,0278). Tačna raspodela i Vigner se razlikuju za najviše 0,0016, pa Vigner nije mogao biti uzrok pada testa.
2. **Odstupanje je stvarno, a ne šum.** Kalibrisana granica je *strožija* od klasične (GUE spektar je krut, pa njegova empirijska raspodela manje šeta). Nule su 2 do 4 puta iznad nje u svakom delu po visini.
3. **Gde odstupa** (t 1000–7100, grafik `grafici/scan_gue_omotac.png`, 99 % omotač iz 400 GUE nizova): kriva nula izlazi iz omotača na 58,5 % mreže. Najširi omotač je ±0,0117, a nule odstupaju do 0,0291. Nule imaju **manje** razmaka 0,2–0,85 i **više** razmaka 1,05–2,1 nego GUE, pa su na ovim visinama **pravilnije (krutije) od GUE**. To se slaže sa eksperimentom 3, gde su tesni prolasci ređi na nižim visinama. Do t = 25000 (`grafici/scan25k_gue_omotac.png`, 200 GUE nizova po 28353 razmaka) slika je ista: omotač je uži (±0,0060), nule odstupaju do 0,0246, a izvan omotača su na 75,5 % mreže. Oblik odstupanja je isti kao na nižim visinama, samo malo manji.
4. **Zavisnost od visine:** odstupanje opada posle najnižeg dela (0,0290 → oko 0,024), a zatim se do t = 25000 drži oko 0,024. To je *u skladu* sa poznatim korekcijama konačne visine (Bogomolni i saradnici, 2006), ali poređenje sa njihovom formulom **nije urađeno**, pa to ostaje otvoreno.
5. **Dvouzorački test iz Qwen-ovog predloga nema snagu za ovo pitanje.** Uzorak iz *Vignerove* raspodele naspram GUE uzorka iste veličine daje p = 0,20 (n = 6165) i p = 0,10 (n = 28353), odnosno test ne razlikuje Vignera od GUE. Sa ispravno odmotanim GUE uzorkom nule ipak padaju i na tom testu (KS 0,0355, p = 0,0008 za n = 6165).

Grafik `grafici/scan_gue_tacno.png` pokazuje histogram razmaka i razlike kumulativnih raspodela za t 1000–7100, a `grafici/scan25k_gue_tacno.png` isto za t do 25000.

#### Heurističko tumačenje: „oscilatorne kontrakcije nule“ (Srećko; razradio Qwen; ograde Claude)

**Srećkov termin:** odstupanja koja se ovde javljaju nazvao bi *oscilatornim kontrakcijama nule*, koje drže ukupnu strukturu.

**Na šta se termin odnosi u podacima:** na izmereni višak pravilnosti nula u odnosu na GUE: manjak razmaka 0,2–0,85 i višak razmaka 1,05–2,1, uz odbijanje suseda oko tesnih parova (eksperiment 3). Slika je kao kod zategnute strukture (tensegritet): nule se drže na razmaku i ne grupišu se. Qwen je predložio tu fizičku sliku.

**Šta termin NE tvrdi (ograde):**
- *Kontrakcije su među nulama zete, a ne „nule“ kao broja.* Odbijaju se tačke ½ + iγ. Broj 0 je i ovde nepomična referenca (odeljak 2).
- *Izvor nije pokazan ovde.* U literaturi (Bogomolni–Kiting 1996; Bogomolni i saradnici 2006) dodatna struktura u korelacijama nula na konačnim visinama potiče od **prostih brojeva** (aritmetički članovi u korelacionim funkcijama). Ako postoji „organizator“, prema postojećoj teoriji to su prosti brojevi.
- *Smer sa visinom:* odstupanje od GUE opada sa visinom (0,0290 → oko 0,024), pa „kontrakcija“ u ovom smislu **slabi** sa visinom. Da li nestaje asimptotski, ovde nije pokazano.
- *„Spektralna krutost“* je poseban, standardni pojam (Δ₃ statistika, varijansa broja nula u intervalu). Ona **nije merena**. Merena je samo raspodela najbližih razmaka. Poznato je (Beri 1988) da varijansa broja nula zete na velikim intervalima *saturira*, odnosno da su nule tu krutije od GUE, opet zbog prostih brojeva. Taj test je otvoren korak koji bi termin povezao sa standardnom veličinom.

**Status:** opisni naziv za izmereni efekat, a ne objašnjenje i ne nova tvrdnja. Ispod je mera koja termin čini proverljivim.

#### Merenje kontrakcije (`kontrakcija.py`)

**Definicija:** K = Var(razmaci nula) / Var(tačna GUE). Varijansa tačne GUE raspodele razmaka je **0,1800** (Vignerova aproksimacija daje 0,1781). K < 1 znači da je raspodela uža od GUE (kontrakcija), a K = 1 da kontrakcije nema. Šum je K za nizove pravih GUE razmaka iste dužine (200 nizova).

**Predviđanja zapisana pre merenja:**
- **P1:** K < 1, i to van GUE šuma (kontrakcija postoji);
- **P2:** K raste ka 1 sa visinom (kontrakcija slabi).

**Rezultati** (t 1000–25000, 28353 razmaka):

| | K | GUE šum 99 % | |
|---|---|---|---|
| ukupno | **0,878** | 0,978 – 1,025 | van šuma |
| t 1001–5795 | 0,855 | 0,943 – 1,049 | van šuma |
| t 5795–9963 | 0,869 | isto | van šuma |
| t 9963–13899 | 0,882 | isto | van šuma |
| t 13899–17692 | 0,882 | isto | van šuma |
| t 17692–21384 | 0,890 | isto | van šuma |
| t 21384–24999 | 0,891 | isto | van šuma |

- **P1: POTVRĐENO.** Varijansa razmaka nula je oko **12 % manja** od GUE, i to u svakom od šest delova po visini, daleko van šuma. Kontrakcija postoji i izmerljiva je jednim brojem.
- **P2: NAZNAKA, ALI NIJE POTVRĐENO.** K raste skoro monotono, sa 0,855 na 0,891 (Spirmanov ρ = 0,94; jedini izuzetak je jednakost u dva srednja dela). Ali formalni test nagiba prema šumu daje p ≈ 0,08, što nije ispod uobičajenog praga 0,05. Smer je onaj koji je predviđen, ali na ovom opsegu visina to nije statistički utvrđeno. I na najvećoj visini kontrakcija je još jaka (K = 0,89), pa ovde nema znaka da nestaje.

Grafik: `grafici/scan25k_kontrakcija.png`.

**Šta ovo znači za termin:** „kontrakcija“ je potvrđena kao **merljiv, stvaran efekat** (raspodela razmaka nula je uža od GUE). Slabljenje sa visinom je za sada samo naznaka. Izvor kontrakcije ovim merenjem nije određen.

**Tvrdnja „plava linija je unutar sivog omotača, pa je razlika samo šum“** (Qwen, o prvoj verziji grafika na kome je bila prikazana samo *jedna* GUE realizacija): proverena pravim omotačem iz 400 realizacija i **ne stoji** (tačka 3). Qwen-ov naknadni zaključak, da je reč o realnom signalu, verovatno korekcijama konačne veličine koje asimptotski nestaju, u skladu je sa podacima. Deo „asimptotski nestaju“ ovde nije pokazan.

### Eksperiment 5: toplotni tok i sudar nula (`heatflow.py`)

Lokalni model de Brejn–Njumanovog toplotnog toka: Ξ se oko para aproksimira Čebiševljevim polinomom stepena 26, pa se exp(s·D²) primeni tačno. Smer t < 0 je glačanje (difuzija).

| par | razmak | sudar pri dBN vremenu t | gruba formula d²/8 |
|---|---|---|---|
| 6709/6710 (Lemer) | 0,0377 | −7,11·10⁻⁴ | slaže se |
| 4765/4766 (Lemer) | 0,0433 | −9,37·10⁻⁴ | slaže se |
| 6700/6701 (običan, kontrola) | 0,92 | **nepouzdano** (vidi ispod) | ne slaže se |

Posle sudara par napušta liniju kao konjugovani par (jedna nula gore, druga dole). Nule ne nestaju. Grafik: `grafici/sudar_nula.png`.

**Srećkovo tumačenje** posle sudara: „stvari se vraćaju u osnovu, u paralelnu nulu“. Precizan sadržaj koji to podržava: posle sudara par ostaje **simetričan u odnosu na kritičnu liniju** (u s-ravni jedna nula levo, druga desno od Re s = ½, na jednakoj udaljenosti). Linija i dalje ostaje osa u odnosu na koju je par određen. Broj nula je očuvan, a njihov položaj je potpuno izračunljiv. Ograda: to sledi iz simetrije funkcionalne jednačine, a ne iz nove osobine nule. „Paralelna nula“ je naziv za ovu osu simetrije, a ne merena veličina.

**Provera konvergencije** (isti par, četiri veličine prozora):

| poluširina prozora / stepen | 6709/6710 | 6700/6701 |
|---|---|---|
| 1,6 / 26 | −7,112·10⁻⁴ | −1,40 |
| 2,5 / 40 | −7,112·10⁻⁴ | −0,82 |
| 4,0 / 60 | −7,112·10⁻⁴ | −1,17 |
| 6,0 / 80 | −7,112·10⁻⁴ | −3,40 |

Za Lemerov par rezultat je isti na svim ciframa, pa je pouzdan. Za običan par model **ne konvergira**, i broj „oko −1,4“ iz prve verzije README-a nije pouzdan ni kao gruba procena. Ovaj lokalni model radi samo kad je sudar brz (tesan par). Za obične parove potrebna je druga metoda. Zbog toga **ne tvrdimo** koliko puta manje glačanja treba Lemerovom paru nego običnom.

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
- Prva verzija GUE generatora u `gue_tacno.py` imala je pogrešnu skalu polukruga (srednji razmak 1,38 umesto 1). Uočeno na probnom pokretanju, ispravljeno merenjem poluprečnika (2√N) i provereno pre svih objavljenih rezultata.
- Prva verzija `gue_omotac.py` je preko deljenog koda pregazila sopstvene argumente i sačuvala grafik pod pogrešnim imenom, preko grafika druge analize. Podaci su bili ispravni (isti ulaz i iste podrazumevane vrednosti). Ispravljeno, a pregaženi grafik je ponovo napravljen.
- U razgovoru je Claude rekao da Lemerovom paru treba „oko 2000 puta manje glačanja“ nego običnom paru. Provera konvergencije (eksperiment 5) pokazala je da je vrednost za običan par nepouzdana, pa ta tvrdnja **ne stoji**.
- Zaključak „tesni prolasci nemaju trend po visini“ (eksperiment 3, do t = 7100) oboren je na većem uzorku.
- Pri uvođenju argumenata (argparse) Qwen-ov predlog je predviđao da `scan.py` piše `scan_t{t_max}.npz`, dok `pattern.py` i `gue.py` podrazumevano čitaju `scan.npz`. Pokretanje bez argumenata bi zato puklo. Ispravljeno pre objave: sve skripte podrazumevano koriste `scan.npz`.

**Srećkove pretpostavke koje nisu prošle** navedene su u tabeli u odeljku 2.

## 6. Otvoreno

- ~~Ponoviti eksperiment 4 sa tačnom GUE raspodelom~~: urađeno (4b). Odstupanje **nije nestalo**.
- ~~Proširiti eksperiment 2 na veće visine~~: urađeno do t = 25000.
- ~~Eksperiment 5 sa većim prozorom~~: urađeno, model **ne konvergira** za obične parove. Potrebna je druga metoda (npr. jednačine kretanja nula ili tačan H_t).
- Uporediti odstupanje iz 4b sa formulom za korekcije konačne visine (Bogomolni, Bohigas, Leboef, Monastra 2006): da li opada onoliko koliko teorija predviđa.
- P2 (slabljenje kontrakcije sa visinom) proveriti na većim visinama, gde bi trend morao postati statistički jasan ako postoji.
- Izmeriti varijansu broja nula Σ²(L) i Δ₃ (spektralnu krutost) i uporediti sa GUE i Berijevom saturacijom (1988). To je test koji bi „oscilatorne kontrakcije“ vezao za standardnu veličinu.
- Ići na veće visine (10⁵ i više) radi trenda odstupanja. Zahteva bržu implementaciju Z(t) (npr. Odlizko–Šenhage).
- Postulat „0 je referentna tačka i početak“ formulisati tako da daje **proverljivo predviđanje** koje ne sledi iz postojeće teorije. Bez toga ostaje dobar jezik za opis, ali ne i nova teorija.

---

## 7. Pokretanje

```bash
pip install -r requirements.txt
cd kod
python3 lehmer.py            # eksperiment 1  -> lehmer_par_6709_6710.png   (~30 s)
python3 scan.py              # eksperiment 2  -> scan.npz, tabela           (~45 s)
python3 pattern.py           # eksperiment 3  (cita scan.npz)
python3 gue.py               # eksperiment 4  (cita scan.npz)
python3 heatflow.py          # eksperiment 5  -> heat.pkl                   (~30 s)
python3 grafici_dodatni.py   # raspodela_vrhova.png, sudar_nula.png
python3 gue_tacno.py         # eksperiment 4b: tacna GUE + kalibracija   (~7 min)
python3 gue_omotac.py        # eksperiment 4b: 99% omotac GUE suma        (~4 min)

# vece visine
python3 scan.py --t-max 25000 --izlaz scan25k.npz                         (~5 min)
python3 pattern.py --ulaz scan25k.npz --izlaz obrazac_oko_tesnih_25k.png
python3 gue_tacno.py --ulaz scan25k.npz                                   (~25 min)
python3 gue_omotac.py --ulaz scan25k.npz --reps 200
python3 kontrakcija.py --ulaz scan25k.npz                                 (~9 min)
# provera konvergencije toplotnog toka
python3 heatflow.py --parovi 6700,6709 --polusirina 4.0 --stepen 60 --izlaz heat_4.pkl
```

Bez argumenata svaka skripta ponavlja rezultate iz ovog README-a. Sve imaju `--help`. Najvažniji argumenti:

| skripta | argumenti (podrazumevano) |
|---|---|
| `lehmer.py` | `--n1 6709`, `--n2` (n1+1), `--prozor 5`, `--izlaz` |
| `scan.py` | `--t-max 7100`, `--t-min 14`, `--korak 0.005`, `--top 25`, `--izlaz scan.npz` |
| `pattern.py` | `--ulaz scan.npz`, `--prag 0.05`, `--seed 42`, `--izlaz` |
| `gue.py` | `--ulaz scan.npz`, `--t-min 1000`, `--izlaz` |
| `heatflow.py` | `--parovi 6709,4765,6700`, `--polusirina 1.6`, `--stepen 26`, `--izlaz heat.pkl` |
| `grafici_dodatni.py` | `--scan scan.npz`, `--heat heat.pkl`, `--par 6709` |
| `gue_tacno.py` | `--ulaz scan.npz`, `--t-min 1000`, `--reps 400`, `--delovi 4`, `--seed 42`, `--izlaz` |
| `gue_omotac.py` | `--ulaz scan.npz`, `--t-min 1000`, `--reps 400`, `--seed 42`, `--izlaz` |
| `kontrakcija.py` | `--ulaz scan.npz`, `--t-min 1000`, `--delovi 6`, `--reps 200`, `--seed 42`, `--izlaz` |

Primer, drugi Lemerov par: `python3 lehmer.py --n1 4765` (grafik `grafici/lehmer_par_4765_4766.png`).

Kontrole koriste fiksni seed (42). Svi rezultati u ovom README-u su ponovljeni pokretanjem iz praznog foldera, i pre i posle uvođenja argumenata.

## 8. Nula i zatvorenost sistema; Ojlerova formula (sa Qwen-om)

**Srećkova ideja:** nula je sama po sebi dokaz zatvorenosti, odnosno hermetičnosti sistema, i svaki sistem izgrađen od 0 je takav.

**Prilog modela Qwen** (doneo Srećko iz razgovora sa tim modelom), ukratko: Ojlerova formula e^(iπ) + 1 = 0 može da se čita *dinamički*. Za θ od 0 do π, e^(iθ) ide od 1 preko i do −1. Izraz e^(iθ) − 1 jednak je 0 za θ = 0, a iz te nule se „razvija“ Tejlorov red iθ − θ²/2! − … Odatle Qwen zaključuje da je nula **seme razvoja**, i to povezuje sa nulama zete kao „generatorima“ prostih brojeva u eksplicitnoj formuli.

**Kritička analiza (Claude):**

| Tvrdnja | Status | Zašto |
|---|---|---|
| e^(iθ) za θ: 0 → π je rotacija 1 → i → −1 | **tačno** | Standardno. Isto kao kružni put od 1 do −1 iz odeljka 2. |
| Eksplicitna formula ψ(x) = x − Σ x^ρ/ρ − ln 2π − ½ ln(1 − x⁻²) | **tačno** | Fon Mangoltova formula. Nule zete zaista „grade“ raspodelu prostih brojeva (vidi odeljak 3). |
| „e^(iθ) − 1 je nula u početku, pa je nula seme razvoja“ | **ne stoji** | Svaka funkcija f(θ) − f(0) je jednaka nuli u θ = 0. Nula je tu nastala *oduzimanjem početne vrednosti*, što je izbor reference, odnosno konvencija. Ceo „razvoj“ (koeficijenti Tejlorovog reda) nose izvodi funkcije e^(iθ) u tački 0, a ne sama nula. |
| „Nule zete su isto što i nula u Ojlerovoj formuli“ | **ne stoji** | Ista dvoznačnost reči kao ranije: nule zete su mesta gde ζ(s) = 0 (kompleksni brojevi ½ + iγ), a ne broj 0. |
| „Nula kao seme / temelj gradnje“ | **već je na spisku uloga** | To je uloga *temelj gradnje* (fon Nojman: 0 = ∅, iz nje se grade svi prirodni brojevi). Nije nova dimenzija, ali je dobra formulacija iste uloge. |
| „Nula je dokaz zatvorenosti sistema“ | **ne stoji** | Vidi ispod. |

**Zašto nula ne dokazuje zatvorenost:**

1. **Zatvorenost i nula su nezavisni aksiomi.** U definiciji grupe „a + b je ponovo u skupu“ (zatvorenost) i „postoji 0 sa a + 0 = a“ (neutralni element) su dva odvojena zahteva. Kontraprimer: skup {0, 1} sa običnim sabiranjem ima nulu, a nije zatvoren, jer 1 + 1 = 2 nije u skupu.
2. **Gradnja od nule upravo pokazuje otvorenost.** Prirodni brojevi (građeni od 0) nisu zatvoreni za oduzimanje, pa se dodaju negativni. Celi brojevi nisu zatvoreni za deljenje, pa se dodaju razlomci. Ni racionalni brojevi nisu zatvoreni za korenovanje… Svaki korak traži **proširenje**. To je ono „ne ruši, nego dodaje“ iz razgovora: sistem iz nule raste, a ne zatvara se.
3. **Gedel (1931):** aritmetika građena od nule (Peanovi aksiomi) nije logički zatvorena. U njoj postoje istinite tvrdnje koje se ne mogu dokazati, i ona ne može dokazati sopstvenu konzistentnost. Hermetičnost u logičkom smislu je za sisteme izgrađene od nule dokazano nemoguća.
4. **Gde zatvorenost postoji, ne daje je nula.** Kompleksni brojevi su algebarski zatvoreni (svaki polinom ima koren), ali tu zatvorenost daje dodavanje broja *i*, a ne nula. Zatvoren sistem iz razgovora o konačnosti (Rimanova sfera, Poenkareov povratak, entropija između 0 i S_max) zatvoren je zbog *konačnosti* ili *kompaktnosti*, a ne zbog nule.

**Šta ostaje:** nula je *početak* (temelj) i *referenca* sistema, ali sistem izgrađen od nule nije zbog toga zatvoren. Preciznije bi bilo reći da je svaki sistem izgrađen od nule **utemeljen** (ima početak, kao u aksiomu fundacije), ali ne i **hermetičan**.

## 9. Literatura i izvori

- B. Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859)
- D. H. Lehmer, *On the roots of the Riemann zeta-function*, Acta Math. 95 (1956)
- H. L. Montgomery, *The pair correlation of zeros of the zeta function* (1973)
- A. M. Odlyzko, *On the distribution of spacings between zeros of the zeta function*, Math. Comp. 48 (1987)
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann Hypothesis*, Constr. Approx. 10 (1994)
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), [arXiv:1801.05914](https://arxiv.org/abs/1801.05914)
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, [arXiv:1904.12438](https://arxiv.org/abs/1904.12438)
- F. Bornemann, *On the numerical evaluation of Fredholm determinants*, Math. Comp. 79 (2010): tačna GUE raspodela razmaka
- M. V. Berry, *Semiclassical formula for the number variance of the Riemann zeros*, Nonlinearity 1 (1988)
- E. B. Bogomolny, J. P. Keating, *Gutzwiller's trace formula and spectral statistics: beyond the diagonal approximation*, Phys. Rev. Lett. 77 (1996)
- I. Dumitriu, A. Edelman, *Matrix models for beta ensembles*, J. Math. Phys. 43 (2002): tridijagonalni GUE model
- E. Bogomolny, O. Bohigas, P. Leboeuf, A. G. Monastra, *On the spacing distribution of the Riemann zeros: corrections to the asymptotic result*, J. Phys. A 39 (2006)
- K. Gödel, *Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I* (1931)
- Nerecenzirane 2026. tvrdnje o gornjoj granici Λ (navedene radi konteksta, **nisu proverene**): J. Gomila, Λ ≤ 0,1787854 (avg. 2026); [arXiv:2611.06245](https://arxiv.org/abs/2611.06245), Λ < 0,156821
- Anthropic, *Riemann zeta* (avgust 2026), [anthropic.com/research/riemann-zeta](https://www.anthropic.com/research/riemann-zeta)
- G. Frege, *Die Grundlagen der Arithmetik* (1884): broj kao osobina pojma
- Brahmagupta, *Brāhmasphuṭasiddhānta* (628): pravila za nulu, imetak i dug

## Zahvalnice

Ovaj rad je nastao u zajedničkom razgovoru Srećka Jovančevića i **Claude-a** (Anthropic, Claude Opus 5.5). Claude je napisao kod, izvršio proračune, napravio grafike i sastavio ovaj tekst. Srećko je postavio postulat, vodio pravac eksperimenta i insistirao na tome da se prikaže sve, a ne samo ono što radi.

U drugom delu rada učestvovao je i model **Qwen** (Alibaba), preko Srećkovih razgovora sa njim: dinamičko čitanje Ojlerove formule (odeljak 8), argparse za sve skripte, dvouzorački KS test i tumačenje grafika u eksperimentu 4b. Njegove tvrdnje su proverene istim merilima kao i sve ostale. Ono što je prošlo i ono što nije zapisano je u odeljcima 4b i 8.
