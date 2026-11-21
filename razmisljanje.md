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
