# M21 — Alias, copie, filtri e ordinamento delle liste

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-07 — Liste, tuple e dati tabellari  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- spiegare che due nomi possono riferirsi alla stessa lista;
- prevedere gli effetti di una mutazione attraverso un alias;
- creare una copia superficiale con `.copy()` o slicing;
- distinguere alias e copia;
- capire che una copia superficiale non duplica ricorsivamente gli oggetti annidati;
- evitare mutazioni strutturali ingenue durante l'iterazione;
- filtrare/trasformare una lista costruendone una nuova con loop esplicito;
- cercare, contare e aggregare elementi riusando i pattern già noti;
- distinguere `sort()` e `sorted()`;
- verificare sia il risultato sia l'eventuale mutazione dell'input.

---

# 1. Due nomi, un solo oggetto

```python
a = [10, 20]
b = a
b.append(30)
```

Che cosa contiene `a`?

```text
[10, 20, 30]
```

Modello:

```text
a ─┐
   ├──> [10, 20, 30]
b ─┘
```

`b = a` non crea una nuova lista.

---

# 2. Alias

Un alias è un altro nome per lo stesso oggetto.

Se l'oggetto è mutabile, una mutazione osservata tramite un nome è visibile anche tramite gli altri alias.

Questo modello sarà importante anche per parametri mutabili e OOP.

---

# 3. Copia superficiale

```python
a = [10, 20]
b = a.copy()
```

oppure:

```python
b = a[:]
```

Ora `a` e `b` sono liste esterne diverse.

Per liste piatte di valori immutabili:

```python
b.append(30)
```

non modifica `a`.

---

# 4. Copia non significa clonazione infinita

```python
a = [[1], [2]]
b = a.copy()
b[0].append(9)
```

Le liste esterne sono diverse, ma gli oggetti interni sono ancora condivisi.

Modello:

```text
a ─> [ ─────> [1, 9], ─────> [2] ]
b ─> [ ─────> [1, 9], ─────> [2] ]
```

Per il core basta capire:

> una copia superficiale copia il contenitore esterno, non ricrea ricorsivamente tutto ciò che contiene.

`deepcopy` non è prerequisito.

---

# 5. Testare alias e copia

Non testare soltanto il risultato finale.

Se una funzione promette di non mutare l'input:

```python
originale = [3, -1, 5]
risultato = solo_positivi(originale)

assert risultato == [3, 5]
assert originale == [3, -1, 5]
```

Il secondo assert verifica il contratto di non-mutazione.

---

# 6. Mutare la lista mentre la percorri

Questo pattern è rischioso:

```python
for valore in numeri:
    if valore < 0:
        numeri.remove(valore)
```

Mentre il `for` avanza, la struttura cambia e alcuni elementi possono essere saltati.

---

# 7. Strategia sicura: nuova lista

```python
positivi = []

for valore in numeri:
    if valore >= 0:
        positivi.append(valore)
```

Vantaggi beginner:

- input resta leggibile;
- output è separato;
- il contratto è chiaro;
- il test può verificare che l'input non cambi.

---

# 8. Iterare su una copia

Quando la specifica richiede davvero di modificare la lista originale:

```python
for valore in numeri.copy():
    if valore < 0:
        numeri.remove(valore)
```

È una strategia possibile, ma va usata consapevolmente.

Spesso costruire una nuova lista resta più chiaro.

---

# 9. Filtrare

```python
def solo_positivi(numeri):
    risultato = []
    for numero in numeri:
        if numero > 0:
            risultato.append(numero)
    return risultato
```

Questo riusa:

```text
loop + if + append + return + test
```

---

# 10. Trasformare

```python
def doppi(numeri):
    risultato = []
    for numero in numeri:
        risultato.append(numero * 2)
    return risultato
```

La lista originale non viene modificata se il contratto non lo richiede.

---

# 11. Comprehension: solo confronto opzionale

Dopo aver compreso il loop:

```python
positivi = [x for x in numeri if x > 0]
```

può essere mostrata come forma equivalente e concisa.

Non è prerequisito del core di seconda.

---

# 12. `sort()` vs `sorted()`

```python
numeri.sort()
```

- modifica `numeri`;
- restituisce `None`.

```python
ordinati = sorted(numeri)
```

- produce una nuova lista ordinata;
- lascia `numeri` invariata.

Domanda:

> devo preservare l'ordine originale?

---

# 13. Bug `sort()` assegnato

```python
numeri = numeri.sort()
```

Dopo:

```text
numeri → None
```

È lo stesso modello già visto con `append()`.

---

# 14. Ricerca e aggregazione sulle liste

I pattern M11 ora lavorano su dati conservati:

```python
def massimo_lista(numeri):
    massimo = numeri[0]
    for numero in numeri[1:]:
        if numero > massimo:
            massimo = numero
    return massimo
```

Nota: non usare `max` come nome variabile perché oscura la built-in `max()`.

---

# 15. Friedpython: massimo da modernizzare

L'esercizio legacy sul massimo è concettualmente buono, ma usa:

```python
max = numeri[0]
```

Nel corso lo riscriviamo con:

```python
massimo = numeri[0]
```

per non oscurare il nome built-in.

---

# 16. Friedpython: lista inversa come confronto

Lo spunto legacy usa `reversed()` + `append`.

Possiamo confrontare:

```text
nuova lista costruita manualmente
list(reversed(numeri))
numeri[::-1]
numeri.reverse()
```

La domanda centrale è:

> creo un nuovo oggetto o modifico l'originale?

---

# 17. Performance intuitiva

Senza Big-O formale:

- ricerca in lista → in generale scansione finché trovi/fine;
- inserimento/rimozione in mezzo → può spostare elementi;
- `append` → crescita naturale in coda;
- se domina unicità o lookup per chiave, una lista potrebbe non essere la struttura migliore.

Set/dict arriveranno presto proprio per questo.

---

# 18. Error Clinic

- alias involontario;
- `.copy()` interpretato come copia ricorsiva;
- rimozione durante `for` sulla stessa lista;
- `sort()` assegnato;
- funzione che muta input quando prometteva nuova lista;
- nome `max`/`list`/`str` usato come variabile oscurando built-in importanti.

---

# 19. Activity candidate

- **A — Alias microscope:** disegna nomi e oggetti;
- **B — Safe filtering:** ripara mutazione durante iterazione;
- **C — Implement:** funzione che filtra/trasforma senza mutare input;
- **D — Debug:** alias, shallow copy, sort/None, mutation contract.

---

# 20. Checkpoint

Sai spiegare:

1. `b = a` vs `b = a.copy()`;
2. shallow copy;
3. perché rimuovere durante iterazione può saltare elementi;
4. `sort` vs `sorted`;
5. come testare che l'input non venga mutato;
6. perché evitare di oscurare built-in con nomi variabile.

---

# 21. Sintesi

```text
alias → stesso oggetto
copy  → nuovo contenitore esterno
```

```text
mutazione prevista? → testala
non-mutazione promessa? → testala
```

```text
sort()   → in-place / None
sorted() → nuova lista
```

Nel prossimo modulo confronteremo liste e tuple e useremo liste annidate per dati tabellari e matrici.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 su liste/copie/ordinamento;
- *Think Python / Pensare in Python* — aliasing/mutability;
- *Learning Python / Imparare Python* — list operations;
- audit `sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`.
