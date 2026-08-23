# PY2-07 — Liste, tuple e dati tabellari

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra: settimane 21–23;
- monte ore nominale: 9 ore + checkpoint B nella settimana 24;
- prerequisiti: stringhe/sequenze, funzioni, cicli, selezione e test;
- baseline: Python 3.12;
- output: lo studente sa usare e scegliere liste/tuple, comprendere mutabilità e aliasing, applicare algoritmi sulle collezioni, evitare mutazioni pericolose durante l'iterazione e modellare dati tabellari/matrici semplici con liste annidate.

## Perché questa UDA esiste

Con le stringhe lo studente ha già imparato a elaborare una sequenza. Ora compare una struttura che può **cambiare nel tempo**.

La domanda guida diventa:

```text
ho una collezione ordinata?
→ deve cambiare?
→ aggiungo/rimuovo elementi?
→ mi serve un record fisso?
→ sto condividendo lo stesso oggetto o una copia?
→ devo iterare per valore o per indice?
→ una struttura annidata rappresenta davvero il dominio?
```

La mutabilità è un modello mentale, non soltanto un elenco di metodi.

---

# M20 — Liste: creare, accedere, modificare e iterare

## Obiettivi osservabili

Lo studente sa:

1. creare una `list`;
2. usare `len`, indici positivi/negativi e slicing;
3. leggere/modificare un elemento per indice;
4. aggiungere con `append`;
5. distinguere `append` ed `extend`;
6. usare `insert` quando la posizione è davvero parte del requisito;
7. rimuovere con `remove`/`pop` sapendo che hanno semantiche diverse;
8. iterare direttamente sugli elementi;
9. iterare con indice quando serve la posizione;
10. usare `enumerate` quando servono insieme indice e valore;
11. verificare membership con `in`;
12. spiegare che la lista è mutabile mentre `str` è immutabile.

## Modello mentale

```text
nome ─────> oggetto list mutabile
             [v0, v1, v2, ...]
```

Un'operazione mutante cambia **quell'oggetto**.

## Metodi mutanti e `None`

Errore obbligatorio da mostrare:

```python
numeri = [1, 2]
numeri = numeri.append(3)
```

Dopo `append`, `numeri` diventa `None` perché `append()` modifica la lista e non restituisce la lista.

Contrasto:

```python
numeri.append(3)
```

Il corso deve distinguere:

```text
operazione in-place
vs
funzione/metodo che produce un nuovo valore
```

Questa distinzione tornerà con `.sort()` vs `sorted()`.

## `append` vs `extend`

Esempio microscope:

```python
x = [1, 2]
x.append([3, 4])
# [1, 2, [3, 4]]
```

contro:

```python
x = [1, 2]
x.extend([3, 4])
# [1, 2, 3, 4]
```

Non memorizzare la differenza: far prevedere la struttura risultante.

## Iterazione per valore, indice, `enumerate`

### valore soltanto

```python
for valore in valori:
    ...
```

### posizione necessaria

```python
for i in range(len(valori)):
    ...
```

### indice + valore

```python
for i, valore in enumerate(valori):
    ...
```

`enumerate` entra qui perché ora la relazione indice/elemento è già compresa.

## Activity candidate

### A — Predict mutation

Prevedere la lista dopo una sequenza breve di operazioni.

### B — Controlled Change

Cambiare append/insert/remove per rispettare una nuova specifica.

### C — Implement

Costruire progressivamente una lista a partire da N input e calcolare semplici proprietà usando pattern già appresi.

### D — Debug

- `append` assegnato alla variabile;
- indice fuori range;
- `remove` confuso con `pop`;
- `append` vs `extend`;
- modifica della posizione sbagliata.

---

# M21 — Alias, copie, mutazione durante iterazione e algoritmi sulle liste

## Obiettivi osservabili

Lo studente sa:

- spiegare che due nomi possono riferirsi alla stessa lista;
- prevedere effetti di una mutazione attraverso un alias;
- creare una copia superficiale di primo livello con slicing o `.copy()`;
- distinguere alias e copia;
- capire che una copia superficiale non duplica ricorsivamente gli oggetti annidati;
- evitare di modificare strutturalmente una lista mentre la sta iterando senza una strategia esplicita;
- costruire una nuova lista filtrata/trasformata con un loop;
- cercare, contare e aggregare elementi;
- usare `sort()` vs `sorted()` con distinzione in-place/nuovo risultato;
- riconoscere quando l'ordine originale deve essere preservato;
- usare test per verificare sia risultato sia eventuale mutazione prevista.

## Alias

```python
a = [10, 20]
b = a
b.append(30)
```

Domanda prima dell'esecuzione:

> cosa contiene `a`?

Visualizzazione:

```text
a ─┐
   ├──> [10, 20, 30]
b ─┘
```

Questo modello prepara oggetti, parametri mutabili e OOP futuri.

## Copia superficiale

```python
b = a.copy()
```

oppure:

```python
b = a[:]
```

Per una lista piatta di valori immutabili il modello beginner è semplice: mutare la struttura di `b` non muta `a`.

### Strutture annidate

Mostrare con cautela:

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
```

La lista esterna è copiata, le liste interne sono ancora condivise.

`copy.deepcopy` non è core: basta capire che "copia" ha livelli.

## Mutare mentre si itera

Esempio problematico:

```python
for valore in numeri:
    if valore < 0:
        numeri.remove(valore)
```

Può saltare elementi perché la struttura cambia durante l'iterazione.

Strategie beginner:

1. costruire una nuova lista;
2. iterare su una copia quando la specifica richiede mutazione;
3. usare un indice/while solo se davvero necessario e progettato.

Preferire spesso una nuova lista perché rende l'intenzione chiara.

## Filtrare/trasformare con loop esplicito

```python
positivi = []
for valore in numeri:
    if valore > 0:
        positivi.append(valore)
```

Solo dopo padronanza, confronto opzionale:

```python
positivi = [valore for valore in numeri if valore > 0]
```

La comprehension semplice è **INTRO/EXT**, mai prerequisito per gli outcome core.

## Ordinamento

```python
ordinati = sorted(numeri)
```

preserva `numeri`.

```python
numeri.sort()
```

modifica `numeri` e restituisce `None`.

Questo riusa il modello mutazione vs nuovo valore.

## Performance intuitiva

Senza Big-O formale:

- cercare un valore in una lista richiede in generale una scansione finché viene trovato/finisce la lista;
- inserire/rimuovere in mezzo può richiedere lo spostamento di elementi;
- `append` è l'operazione naturale per crescita in fondo;
- non scegliere una lista per ogni problema per abitudine: set/dict arriveranno come alternative quando unicità/lookup sono dominanti.

## Activity candidate

### A — Alias microscope

Disegnare oggetti e riferimenti dopo assegnamenti/copie/mutazioni.

### B — Safe filtering

Riparare una funzione che rimuove elementi durante l'iterazione.

### C — Implement

Funzione che filtra/trasforma una lista senza mutare l'input, con test sull'input originale.

### D — Debug

- `.sort()` assegnato;
- alias involontario;
- shallow nested surprise;
- rimozione durante loop;
- copia creata nel punto sbagliato.

---

# M22 — Tuple, unpacking, strutture annidate e matrici

## Obiettivi osservabili

Lo studente sa:

1. creare una `tuple`;
2. spiegare l'immutabilità della tupla;
3. riconoscere che la virgola, non le sole parentesi, determina una tupla;
4. creare una tupla a un elemento (`(x,)`);
5. usare packing/unpacking semplice;
6. scegliere intuitivamente `list` vs `tuple`;
7. usare tuple come piccoli record/coordinate quando appropriato;
8. usare liste di tuple e altre composizioni semplici;
9. creare e attraversare una lista di liste;
10. accedere a matrice con `[riga][colonna]`;
11. usare cicli annidati sui dati tabellari;
12. evitare il classico aliasing di righe nella costruzione della matrice.

## Lista vs tupla

Domanda principale:

```text
questa sequenza rappresenta una collezione che deve cambiare
oppure un raggruppamento/fatto posizionale che voglio trattare come stabile?
```

Esempi:

- voti da aggiungere/rimuovere → `list`;
- coordinata `(x, y)` → `tuple` candidata;
- elenco modificabile di coordinate → `list[tuple]` concettualmente.

Non presentare "tuple sempre più veloci" come criterio beginner dominante.

## Unpacking

```python
punto = (3, 5)
x, y = punto
```

Rende espliciti i ruoli.

Anche:

```python
for indice, valore in enumerate(valori):
    ...
```

può essere riletto ora come unpacking della coppia prodotta dall'iterazione.

## Matrici come lista di liste

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
]
```

Accesso:

```python
matrice[1][2]
```

Iterazione:

```python
for riga in matrice:
    for valore in riga:
        ...
```

## Alias trap nella costruzione

Evitare come modello:

```python
matrice = [[0] * colonne] * righe
```

perché le righe interne possono essere lo stesso oggetto condiviso.

Costruzione beginner esplicita:

```python
matrice = []
for _ in range(righe):
    matrice.append([0] * colonne)
```

Una comprehension equivalente può essere enrichment dopo che il problema di aliasing è compreso.

## Dati tabellari

Problemi:

- somma righe/colonne;
- cerca valore e posizione;
- massimo per riga;
- griglia di posti/stati;
- tabella temperature/giorni;
- board semplice.

Non usare una matrice se una lista piatta descrive meglio il dominio.

## Activity candidate

### A — Tuple/list choice

Dato un modello di dati, scegliere struttura e motivare.

### B — Unpacking

Completare codice che trasforma tuple in nomi significativi.

### C — Matrix traversal

Implementare elaborazione riga/colonna con cicli annidati.

### D — Alias matrix debug

Diagnosticare e correggere righe condivise.

### E — Mini-project dati tabellari

Piccola griglia/matrice con:

- costruzione;
- elaborazione;
- ricerca/aggregazione;
- più funzioni;
- casi limite;
- spiegazione della struttura scelta.

---

# Checkpoint B — settimana 24

Usi prioritari:

- consolidamento stringhe/liste/tuple;
- recupero alias/copia/slicing;
- mini-project;
- seconda prova teorica/strumento di evidence secondo calendario;
- import selettivo di Activity `friedpython` solo dopo audit.

Non introduce nuovi prerequisiti.

---

# `friedpython` — policy specifica PY2-07

Snapshot:

`TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f`

Materiale individuato:

### `liste/`

- operazioni base;
- metodi lista;
- assegnamento tramite indirizzamento/slicing;
- indirizzamento/slicing/matrici;
- iterazioni/espressioni di mapping.

### `tuple/`

- conversioni/metodi/immutabilità;
- esempi d'uso.

### `esercizi_liste/`

- 6 script esercizio;
- verifica PDF storica.

## Regole di riuso

- la parte comprehension/mapping non determina l'ordine: loop espliciti prima;
- controllare ogni esempio per Python 3.12 e semantica moderna;
- separare spiegazione, starter e solution;
- aggiungere test su aliasing/mutazione/casi limite;
- non importare commenti storici come lesson;
- matrici sì, ma dopo alias/copia e cicli annidati;
- classificare ogni esercizio A–F prima dell'import.

---

# Piano delle tre settimane

## Settimana 21 — M20

- lista come sequenza mutabile;
- metodi essenziali;
- iterazione/enumerate;
- lab predizione/mutazione.

## Settimana 22 — M21

- alias/copia;
- shallow nested;
- mutazione durante loop;
- filtro/trasformazione;
- sort vs sorted;
- lab Debug Clinic.

## Settimana 23 — M22

- tuple/unpacking;
- scelta list/tuple;
- strutture annidate;
- matrici;
- alias trap;
- lab mini-project.

Settimana 24: checkpoint B.

---

# Exit checkpoint UDA

Lo studente dovrebbe saper:

- creare/modificare/iterare liste;
- scegliere metodo appropriato;
- spiegare mutazione vs nuovo valore;
- riconoscere alias e creare una copia superficiale;
- prevedere effetti su strutture annidate semplici;
- evitare mutazione strutturale ingenua durante iterazione;
- filtrare/trasformare con loop;
- usare sort/sorted correttamente;
- creare/usare tuple e unpacking;
- scegliere list vs tuple con motivazione;
- modellare una matrice semplice come lista di liste;
- attraversare matrici con loop annidati;
- evitare righe aliasate;
- progettare test che controllano anche eventuale mutazione/non-mutazione dell'input.

---

# Remediation

- oggetti fisici/cartoncini per alias vs copia;
- liste da 3 elementi;
- un metodo per volta con stato prima/dopo;
- disegnare frecce nome → oggetto;
- matrici 2×3 prima di dimensioni generiche;
- niente comprehension finché filtro con loop non è stabile.

# Enrichment

- simple comprehension come riscrittura di loop noto;
- `zip` su due sequenze corte;
- tuple multiple return dopo comprensione del packing;
- key function di `sorted` con esempio molto semplice;
- confronto costo intuitivo append vs inserimento front/middle;
- shallow vs deep copy con esempio, senza rendere `deepcopy` core.

---

# Fonti

- *Think Python / Pensare in Python*: lists, tuples, aliasing, traversal;
- *Learning Python / Imparare Python*: built-in sequence coverage;
- *Fluent Python*: sequence/mutability/unpacking correctness;
- *Python in a Nutshell*: reference;
- documentazione Python 3.12 list/tuple/sorted/enumerate;
- Pluralsight Python Data Structures;
- `friedpython` pinned come legacy source pack.

---

# Dipendenze piattaforma

- Python 3.12;
- P1 per programmi completi;
- P2 `TheBitPoets/2cornot2c#756` utile per funzioni che restituiscono liste/tuple; il value codec deve preservare il tipo quando necessario;
- nessun runtime speciale.

---

# Criteri per produzione

- audit dei 6 esercizi liste + materiali tuple completato;
- alias/copia presente come concetto core, non nota marginale;
- `.append()`/`.sort()` returning `None` presente nei Debug Clinic;
- mutation-during-iteration affrontata;
- simple comprehension solo dopo loop;
- matrice costruita senza alias trap;
- almeno una Activity di scelta struttura, non solo manipolazione sintattica;
- P2 usato solo dopo capacità piattaforma certificata o fallback esplicito.
