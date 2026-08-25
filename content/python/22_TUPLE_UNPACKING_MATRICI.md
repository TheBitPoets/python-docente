# M22 — Tuple, unpacking, liste annidate e matrici

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-07 — Liste, tuple e dati tabellari  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- creare e leggere una `tuple`;
- spiegare che una tupla è una sequenza immutabile;
- creare correttamente una tupla a un elemento `(x,)`;
- usare packing e unpacking semplici;
- scegliere intuitivamente `list` vs `tuple`;
- usare tuple come piccoli record posizionali/coordinate quando appropriato;
- usare liste di tuple e strutture combinate semplici;
- creare e attraversare una lista di liste;
- usare accesso `[riga][colonna]`;
- riusare cicli annidati sui dati tabellari;
- diagnosticare la trappola delle righe condivise nella costruzione di matrici.

---

# 1. Una tupla è una sequenza immutabile

```python
punto = (3, 5)
```

Come una lista, ha ordine e indici.

```python
punto[0]
punto[1]
```

Ma non puoi fare:

```python
punto[0] = 10
```

Il contenitore tupla è immutabile.

---

# 2. Perché scegliere una tupla?

Domanda beginner:

```text
questa sequenza deve crescere/cambiare
oppure rappresenta un raggruppamento stabile di valori posizionali?
```

Esempi candidati:

- voti da aggiungere/rimuovere → `list`;
- coordinata `(x, y)` → `tuple`;
- colore RGB `(r, g, b)` → `tuple` candidata;
- lista modificabile di coordinate → lista di tuple.

Non scegliamo tuple perché “sono sempre più veloci”. Il criterio principale è il modello dei dati.

---

# 3. La virgola conta

```python
x = (40)
```

`x` è un intero.

```python
y = (40,)
```

`y` è una tupla a un elemento.

È la virgola che costruisce il raggruppamento tuple in questo caso.

---

# 4. Packing

Python può creare una tupla anche tramite comma expression:

```python
punto = 3, 5
```

Per il corso beginner preferiamo spesso le parentesi quando migliorano la leggibilità:

```python
punto = (3, 5)
```

---

# 5. Unpacking

```python
punto = (3, 5)
x, y = punto
```

Ora:

```text
x → 3
y → 5
```

L'unpacking dà nomi significativi ai ruoli dei valori.

---

# 6. `enumerate()` riletto con unpacking

Abbiamo già scritto:

```python
for indice, valore in enumerate(valori):
    ...
```

Ora possiamo capire meglio il modello:

```text
enumerate produce coppie
→ la coppia viene unpacked in indice, valore
```

Non serve approfondire il tipo interno dell'iteratore.

---

# 7. Tuple contenenti oggetti mutabili

Enrichment controllato:

```python
t = (1, [2, 3], 4)
```

Non puoi sostituire:

```python
t[1] = []
```

ma la lista che si trova dentro è ancora un oggetto mutabile:

```python
t[1].append(9)
```

Quindi:

> immutabilità della tupla significa che i riferimenti dei suoi elementi non possono essere riassegnati tramite la tupla; non significa che ogni oggetto contenuto diventi magicamente immutabile.

Questo è enrichment, non prerequisito della scelta list/tuple.

---

# 8. Liste annidate

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
]
```

Una lista può contenere altre liste.

Accesso:

```python
matrice[0]       # prima riga
matrice[1][2]    # 6
```

---

# 9. Dati tabellari

Modello:

```text
riga 0 → [1, 2, 3]
riga 1 → [4, 5, 6]
```

Questo rappresenta naturalmente problemi come:

- griglie;
- posti occupati/liberi;
- tabelle di misure;
- board semplici;
- matrici numeriche elementari.

Non usare una matrice se una lista piatta comunica meglio il dominio.

---

# 10. Attraversare una matrice

Per valore:

```python
for riga in matrice:
    for valore in riga:
        print(valore)
```

Se servono coordinate:

```python
for r in range(len(matrice)):
    for c in range(len(matrice[r])):
        print(r, c, matrice[r][c])
```

La scelta riusa M12: valore soltanto vs posizione necessaria.

---

# 11. Worked example: somma per riga

```python
def somme_righe(matrice):
    risultati = []

    for riga in matrice:
        totale = 0
        for valore in riga:
            totale += valore
        risultati.append(totale)

    return risultati
```

Invariante interno:

> `totale` è la somma dei valori già visti nella riga corrente.

Invariante esterno:

> `risultati` contiene le somme delle righe già elaborate.

---

# 12. Alias trap nella costruzione

Questo sembra creare righe indipendenti:

```python
matrice = [[0] * colonne] * righe
```

ma le righe possono riferirsi **alla stessa lista interna**.

Poi:

```python
matrice[0][0] = 1
```

può modificare la prima posizione di tutte le righe.

È M21 che ritorna dentro le matrici.

---

# 13. Costruzione sicura beginner

Forma esplicita:

```python
matrice = []

for _ in range(righe):
    matrice.append([0] * colonne)
```

Ogni iterazione crea una nuova lista riga.

Una comprehension equivalente può essere mostrata solo dopo:

```python
matrice = [[0] * colonne for _ in range(righe)]
```

come enrichment, non come prerequisito.

---

# 14. Ragged rows

Non tutte le liste di liste sono matrici rettangolari:

```python
dati = [
    [1, 2],
    [3, 4, 5],
]
```

Per questo, quando usiamo indici, spesso il limite corretto della colonna è:

```python
len(matrice[r])
```

non una costante assunta senza contratto.

---

# 15. List vs tuple: confronto

| Domanda | `list` | `tuple` |
|---|---|---|
| sequenza ordinata | sì | sì |
| mutabile | sì | no, al primo livello del contenitore |
| append/remove | sì | no |
| record posizionale stabile | possibile | spesso naturale |
| collezione che cresce | naturale | di solito no |

La scelta dipende dal significato dei dati.

---

# 16. Error Clinic

- `(5)` pensato come tupla a un elemento;
- tentativo di assegnamento a elemento tuple;
- unpacking con numero di valori incompatibile;
- `[riga][colonna]` invertiti;
- range colonne fisso su righe di lunghezza diversa;
- `[[0] * C] * R` con righe alias;
- lista annidata scelta senza motivo quando bastava una lista piatta.

---

# 17. Activity candidate

- **A — List or tuple?** struttura + motivazione;
- **B — Unpacking trace:** coppie/coordinate;
- **C — Matrix traversal:** somma/ricerca per righe e colonne;
- **D — Alias matrix debug:** diagnosticare righe condivise;
- **E — Mini-project tabellare:** più funzioni, matrice piccola, test, spiegazione del modello dati.

Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.

---

# 18. Friedpython tuple: cosa riusiamo e cosa no

Spunti validi:

- immutabilità;
- conversione list/tuple;
- `index`/`count`;
- tupla a un elemento;
- oggetto mutabile annidato come enrichment.

Da non copiare:

- sintassi `print T` Python 2;
- note storiche non necessarie;
- comprehension prima del nostro ordine didattico.

---

# 19. Exit checkpoint PY2-07

Dovresti saper:

- usare liste e metodi essenziali;
- prevedere mutazioni;
- spiegare alias vs copia;
- filtrare/trasformare senza mutazione accidentale;
- usare `sort`/`sorted` correttamente;
- usare tuple/unpacking;
- scegliere list vs tuple;
- costruire e attraversare una lista di liste;
- evitare righe condivise involontarie;
- motivare la struttura usata.

---

# 20. Sintesi

```text
list  → sequenza mutabile
 tuple → sequenza stabile/immutabile come contenitore
```

```text
matrice = lista di righe
```

```text
aliasing non sparisce nelle strutture annidate
```

Checkpoint B consoliderà stringhe, liste e tuple prima di set e dizionari.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 tuple/liste/sequenze;
- *Think Python / Pensare in Python* — tuples/lists;
- *Learning Python / Imparare Python* — sequence types;
- audit `sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`.
