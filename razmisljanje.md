# Razmišljanje: koliko nula je potrebno za građenje broja?

*Zapis razmišljanja, a ne eksperiment. Pitanje je postavio Srećko Jovančević, a analizu je napisao Claude (Anthropic, Claude Opus 5.5). 21. novembar 2026.*

## Pitanje (Srećko)

Ako se broj 1 u stvari može pisati kao **01**, da li bi broj 2 trebalo da bude **002**? Drugim rečima: **koliko nula je potrebno za građenje broja?**

## Kratak odgovor

Zavisi od toga **kako** se broj gradi. Matematika ima više standardnih konstrukcija, i one daju različite odgovore:

| konstrukcija | kako izgleda broj n | koliko nula (∅) u zapisu |
|---|---|---|
| **pozicioni zapis** (407, 01, 002) | cifre na mestima | vodeće nule ne menjaju vrednost: 2 = 02 = 002; broj nula je proizvoljan |
| **Peano** (0 i „sledbenik“ S) | 2 = S(S(0)) | **uvek tačno jedna** nula, plus n koraka |
| **Zermelo** (n = {n−1}) | 2 = {{∅}} | **uvek tačno jedna** nula, umotana n puta |
| **fon Nojman** (n = {0, 1, …, n−1}) | 2 = {∅, {∅}} | **2ⁿ⁻¹** nula (za n ≥ 1) |

### Fon Nojman, ispisano do kraja

| n | zapis | broj ∅ |
|---|---|---|
| 0 | ∅ | 1 |
| 1 | {∅} | 1 |
| 2 | {∅, {∅}} | 2 |
| 3 | {∅, {∅}, {∅, {∅}}} | 4 |
| 4 | {∅, {∅}, {∅, {∅}}, {∅, {∅}, {∅, {∅}}}} | 8 |

Svaki broj sadrži *sve prethodne* brojeve, pa se nule udvostručuju: c(n) = c(0) + c(1) + … + c(n−1) = 2ⁿ⁻¹. Ovo je najbliže ideji „broj nosi celu istoriju od nule“: u broju 4 nula se pojavljuje osam puta, po jednom za svaki put kojim se od nule može stići do četiri.

## Šta je sa „01“ i „002“?

U pozicionom zapisu vodeće nule **ne nose vrednost**: 01 = 1, a 002 = 02 = 2. One čuvaju mesto (uloga *pozicija* iz odeljka 9 README-a), ali ne broje.

U predlogu „1 = 01, 2 = 002“ istu informaciju nose i nule i cifra:
- ako **nule broje** (jedna nula za 1, dve za 2), cifra na kraju je suvišna, i to je onda *unarni* zapis: samo ponavljanje znaka;
- ako **cifra broji**, nule su suvišne.

Čista verzija ideje da se broj gradi brojem koraka od nule već postoji: **Peano**, 2 = S(S(0)). Jedna nula je temelj, a broj je *koliko puta se od nje krenulo*. Ili **Zermelo**, 2 = {{∅}}, gde se ista jedna nula umotava dva puta.

## Veza sa idejom „svaki broj uz sebe ima nulu“

Sve tri konstrukcije (Peano, Zermelo, fon Nojman) imaju zajedničko to da **u svakom broju postoji nula**: kao temelj (Peano), kao jezgro u sredini (Zermelo) ili kao element koji se ponavlja (fon Nojman). U tom smislu ideja „svaki broj uz sebe ima nulu“ ima precizan oblik. Razlikuje se samo **koliko puta** se ta nula pojavljuje:

- **jednom** (Peano, Zermelo): nula je jedinstven izvor, a broj je dubina;
- **2ⁿ⁻¹ puta** (fon Nojman): nula je prisutna u svakom delu istorije broja.

## Otvorena misao

Ako se broj shvati kao „koliko puta je nula prisutna u njegovoj gradnji“, onda fon Nojmanova konstrukcija ne daje n, nego 2ⁿ⁻¹. Broj i broj nula u njemu se razilaze eksponencijalno. Da li je to samo osobina zapisa ili govori nešto o tome šta broj *jeste*, otvoreno je pitanje, i to filozofsko, a ne računsko.

## Provera (kod)

```python
def fon_nojman(n):
    """n kao frozenset: 0 = prazan skup, n = {0, 1, ..., n-1}"""
    s = []
    for _ in range(n):
        s.append(frozenset(s))
    return frozenset(s)

def broj_nula(x):
    """koliko puta se prazan skup pojavljuje u ispisanom zapisu"""
    return 1 if len(x) == 0 else sum(broj_nula(e) for e in x)

for n in range(8):
    print(n, broj_nula(fon_nojman(n)))   # 1, 1, 2, 4, 8, 16, 32, 64
```

---

# Drugo pitanje: da li je Riman govorio o svim nulama?

## Pitanje i kapric (Srećko)

Ako se računa fon Nojman, da li je Riman govorio o *svim* nulama? I kapric, zapisan kao takav:

> **„Možda je (fon) Nojman ukazao na Rimana“**, u smislu: proverite gradivnu funkciju Rimana. Da li je govorio samo o *jednoj ekspresiji* nule, ili o *svim ekspresijama nule kroz građenje broja*?

## Šta je proverljivo (Claude)

**Istorijski: ne.** Riman (1859) je pisao o korenima jedne funkcije, ξ(t): *„es ist sehr wahrscheinlich, dass alle Wurzeln reell sind“* („veoma je verovatno da su svi koreni realni“). Fon Nojmanova konstrukcija brojeva nastala je 1923, 64 godine kasnije. Fon Nojman nije pisao o Rimanovoj hipotezi u vezi sa svojom konstrukcijom. „Ukazao je“ ovde može da znači samo *čitanje unazad*, a ne istorijsku vezu.

**Pojmovno: različite nule.** Kod Rimana „nula“ je koren funkcije (uloga **K**). Kod fon Nojmana to je prazan skup ∅ unutar zapisa broja (uloga **P**). Brojevi se ponašaju potpuno različito: nula zete do visine T ima oko (T/2π)·ln(T/2πe), a broj ∅ u fon Nojmanovom broju n je 2ⁿ⁻¹. Nijedna poznata formula ih ne povezuje.

**Ali kapric ima precizan matematički pandan, i to je zanimljiv deo.** Riman je zaista govorio o *jednoj* ekspresiji, o zeti celih brojeva. Kad se brojevi grade dalje, i svaki novi brojni sistem dobije **svoju** zeta funkciju:

| kako se grade brojevi | njihova zeta / L-funkcija | odgovarajuća hipoteza |
|---|---|---|
| celi brojevi (iz nule, Peano / fon Nojman) | Rimanova ζ(s) | **Rimanova hipoteza** |
| celi brojevi „po modulu“ (aritmetičke progresije) | Dirihleove L-funkcije L(s, χ) | **uopštena RH (GRH)** |
| prošireni brojni sistemi (npr. Gausovi celi brojevi a + bi, algebarski celi brojevi) | Dedekindova zeta ζ_K(s) | **proširena RH (ERH)** |
| najopštije (automorfne forme) | automorfne L-funkcije | **„velika“ RH (Grand RH)** |

Pitanje „da li je govorio samo o jednoj ekspresiji, ili o svim ekspresijama kroz građenje broja“ ima, dakle, stvaran odgovor: **Riman je formulisao hipotezu za jednu ekspresiju, a matematika ju je posle proširila na čitavu porodicu**, po jednu zeta funkciju za svaki način građenja brojeva. Sve one su otvorene (nijedna nije dokazana), i za sve se veruje da su nule na istoj kritičnoj liniji ½.

**Ograda:** to nije fon Nojmanova ideja, i ta porodica se ne gradi brojanjem ∅. Ali duh kaprica, da nula funkcije ne pripada jednoj ekspresiji nego celom građenju brojeva, poklapa se sa načinom na koji se Rimanova hipoteza danas razume.

## Moguća provera

Dirihleove L-funkcije se mogu izračunati numerički, kao i zeta (npr. `mpmath.dirichlet`). Isti eksperimenti iz README-a (prolasci kroz 0, Lemerovi parovi, kontrakcija K) mogli bi se ponoviti na drugoj „ekspresiji nule“. Pitanje bi bilo: **da li L-funkcije imaju istu kontrakciju K < 1 kao zeta**, ili je ona osobina samo Rimanove zete? To je otvoreno i proverljivo.

---

# Provera kaprica: Dirihleova L-funkcija χ₄ (folder `kapric/`)

Pitanje iz prethodnog odeljka, *da li druga „ekspresija nule“ ima istu kontrakciju kao Rimanova zeta*, provereno je na Dirihleovoj L-funkciji L(s, χ₄) (Dirihleova beta funkcija).

## Šta je urađeno

- **`kapric/dirichlet_scan.py`** (napisao Qwen, pokrenuo Srećko): skeniranje Hardijeve Z-funkcije za L(s, χ₄) na t od 10 do 1000. Našao je **867 nula**, što se tačno poklapa sa predviđanjem N(t) = (t/2π)·ln(4t/2πe) (866,9), i sa poznatim nulama (10,2437; 12,9880; 16,3426…). **Scan je ispravan.**
- **`kapric/dirichlet_gue.py`** (napisao Qwen, pokrenuo Srećko): poređenje sa GUE omotačem. **Ima grešku zbog koje je rezultat neupotrebljiv** (vidi ispod).
- **`kapric/dirichlet_kontrakcija.py`** (Claude): ispravljena analiza istih nula.

## Pronađene greške

1. **Udvostručene nule.** Scan čuva *parove* uzastopnih nula (z₁, z₂), (z₂, z₃)…, a `flatten()` je svaku nulu uzeo dvaput. Od „1731 razmaka“ **865 je bilo tačno 0**. Stvarnih razmaka ima 866.
2. **Globalna normalizacija.** Razmaci su deljeni jednim prosekom, iako se gustina nula od t = 10 do 1000 menja skoro trostruko. Ispravno je lokalno odmotavanje preko N(t).
3. **GUE generator** je imao istu grešku odmotavanja kao raniji predlog u eksperimentu 4b (srednjih 60 % spektra podeljeno jednim prosekom).
4. *(sitnica)* Fazni faktor u scanu koristi Γ(¼ + it/2). Za neparan karakter χ₄ treba Γ(¾ + it/2). Na položaj nula ovo ovde nije uticalo (broj se tačno slaže), ali formula nije tačna.
5. **Zaključak izveden pogrešnim putem.** Prvi komentar rezultata glasio je: najtešnji par (289/290, vrh 1,4 % okoline) „direktna je analogija Lemerovim parovima i sugeriše kontrakciju“. To ne sledi: kontrakcija znači *manje* malih razmaka, a tesni parovi se očekuju u svakom GUE skupu. Poređenja radi, kod zete je među prvih 870 nula najtešnji prolazak bio 3,2 %. Za kontrakciju je potrebna varijansa, a ne pojedinačan par.

## Rezultat (ispravna analiza)

| | K = Var / Var(GUE) | GUE šum 99 % (400 nizova po 866) |
|---|---|---|
| **L(s, χ₄)**, t 10–1000, 866 razmaka | **0,684** | 0,883 – 1,140 → **van šuma** (nijedan od 400 GUE nizova) |
| donja polovina (niže t) | 0,650 | |
| gornja polovina (više t) | 0,719 | |
| *zeta, t 10–1300, 896 razmaka (za poređenje)* | *0,793* | |

KS prema tačnoj GUE: 0,0633, uz GUE 99. percentil 0,0350, takođe van šuma. Grafik: `kapric/dirichlet_kontrakcija.png`.

## Zaključak

- **Kontrakcija postoji i kod Dirihleove L-funkcije χ₄.** K = 0,684 je daleko van GUE šuma. To odgovara na pitanje iz kaprica: kontrakcija *nije* osobina samo Rimanove zete. Javlja se i u drugoj „ekspresiji nule“.
- Zaključak je tačan, ali tek po merenju varijanse, a ne po tesnom paru.
- I ovde K raste sa visinom (0,650 → 0,719), u istom smeru kao kod zete.
- **Ograde:** uzorak je mali (866 razmaka). Visine su niske, a tamo su korekcije najveće. „Jača kontrakcija nego kod zete“ (0,684 naspram 0,793) može biti samo posledica visine i različite gustine (konduktor q = 4), pa ovo poređenje nije pošteno dok se ne uradi na istoj efektivnoj gustini. Izvor kontrakcije ni ovde nije određen. U literaturi su za L-funkcije te korekcije takođe aritmetičke (preko prostih brojeva i karaktera).

## Otvoreno

- Ići više (t do 10⁴ i dalje) i porediti zetu i L(s, χ₄) na **istoj efektivnoj gustini** nula.
- Probati još karaktera (npr. χ₃, χ₅) i videti da li K zavisi od karaktera ili samo od gustine.
