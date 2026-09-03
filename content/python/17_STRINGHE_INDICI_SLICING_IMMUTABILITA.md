# M17 — Stringhe: indici, slicing e immutabilità

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-06 — Stringhe come sequenze e testo  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- descrivere una `str` come sequenza ordinata immutabile di testo Unicode a livello beginner;
- usare `len()`;
- usare indici da `0` e indici negativi;
- leggere/scrivere slicing `start:stop` con stop escluso;
- usare uno step semplice quando serve;
- distinguere `IndexError` da slicing fuori range;
- spiegare perché `testo[0] = ...` non è ammesso;
- creare una nuova stringa invece di modificare quella esistente;
- scegliere iterazione diretta o per indice in base al problema.

---

# 1. Una stringa è una sequenza

```python
parola = "python"
```

Modello:

```text
indice       0  1  2  3  4  5
             p  y  t  h  o  n
indice neg. -6 -5 -4 -3 -2 -1
```

La posizione fa parte della struttura.

---

# 2. Lunghezza

```python
len("python")
```

restituisce:

```text
6
```

Gli indici validi positivi vanno da `0` a `len(testo) - 1`.

---

# 3. Accesso con indice

```python
parola[0]   # 'p'
parola[5]   # 'n'
parola[-1]  # 'n'
```

Prima di eseguire, prevedi sempre carattere e posizione.

---

# 4. `IndexError`

```python
parola[6]
```

con `parola = "python"` tenta di accedere a una posizione inesistente e genera `IndexError`.

Domanda di debug:

> qual è l'ultimo indice valido?

---

# 5. Slicing

```python
parola[1:4]
```

produce:

```text
'yth'
```

Regola:

```text
start incluso
stop escluso
```

È lo stesso modello già incontrato con `range`.

---

# 6. Slice fuori range

A differenza dell'accesso singolo, uno slice può oltrepassare il limite senza `IndexError`:

```python
parola[3:100]
```

produce la parte disponibile da indice 3 in poi.

Non confondere:

```text
indice singolo fuori range → errore
slice oltre il limite      → taglio della parte disponibile
```

---

# 7. Indici negativi

```python
parola[-1]
parola[-2]
```

sono utili quando il problema parla naturalmente di ultimo/penultimo carattere.

Non usarli per rendere il codice “più furbo” quando un indice positivo comunica meglio l'intenzione.

---

# 8. Step nello slicing

```python
parola[::2]
```

prende un carattere ogni due.

```python
parola[::-1]
```

produce una stringa in ordine inverso.

Queste forme devono essere spiegate tramite `start:stop:step`, non memorizzate come trucchi.

---

# 9. Immutabilità

Questo non è ammesso:

```python
parola[0] = "P"
```

Una stringa non viene modificata “in posto” carattere per carattere.

Per ottenere un nuovo valore:

```python
nuova = "P" + parola[1:]
```

Il valore originale resta invariato.

---

# 10. Iterazione diretta

Se serve soltanto il carattere:

```python
for carattere in parola:
    print(carattere)
```

È spesso più chiaro di:

```python
for i in range(len(parola)):
    print(parola[i])
```

---

# 11. Quando serve l'indice

L'indice è utile se la posizione è parte del problema:

- confrontare caratteri in posizioni diverse;
- estrarre campi fissi;
- costruire un trace posizione/carattere;
- verificare un pattern posizionale.

La scelta deve essere motivata.

---

# 12. Unicode: modello leggero ma corretto

Core:

> `str` rappresenta testo Unicode.

Per il secondo anno non serve approfondire encoding/code point/grapheme cluster.

Teacher note: evitare affermazioni assolute del tipo “ogni simbolo visibile è sempre un singolo indice”. I dettagli Unicode completi appartengono al percorso avanzato.

---

# 13. Letterali ed escape

Consolidare:

```python
"ciao"
'ciao'
"riga 1\nriga 2"
"tab\tvalore"
"C:\\cartella"
```

Triple quote e raw string possono comparire come preview mirata, non come prerequisito.

---

# 14. Worked example: prefisso e suffisso

Problema:

> Da un codice `ABC-123` estrai le tre lettere iniziali e le tre cifre finali.

```python
codice = "ABC-123"
prefisso = codice[:3]
suffisso = codice[-3:]
```

Casi di test devono chiarire la forma attesa del codice prima di affidarsi alle posizioni.

---

# 15. Error Clinic

- indice `len(testo)` usato come se fosse valido;
- stop incluso invece di escluso;
- tentativo di mutazione;
- indice usato quando bastava il carattere;
- variabile indice riutilizzata male;
- confusione tra slice fuori range e accesso singolo fuori range.

---

# 16. Activity candidate

- **A — Index/slice microscope:** prevedi valore o errore;
- **B — Controlled Change:** cambia uno slice e spiega inclusione/esclusione;
- **C — Implement:** estrai/ricomponi parti di un codice testuale;
- **D — Debug:** correggi indice, slice, mutazione o scelta di iterazione.

Nessuna nuova Activity P2/P1 viene materializzata in questa fase.

---

# 17. Checkpoint

Sai spiegare:

1. perché il primo indice è 0;
2. qual è l'ultimo indice positivo valido;
3. `start` incluso / `stop` escluso;
4. indice singolo fuori range vs slice fuori range;
5. che cosa significa immutabile;
6. iterazione diretta vs per indice;
7. perché uno slicing crea una nuova stringa.

---

# 18. Sintesi

```text
str = sequenza ordinata immutabile
```

```text
indice → una posizione
slice  → nuova sottostringa
```

```text
serve solo il carattere? → for diretto
serve la posizione?      → indice
```

Nel prossimo modulo useremo membership, ricerca e metodi per normalizzare e trasformare il testo in modo consapevole.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 `str`;
- *Think Python / Pensare in Python* — strings/traversal;
- *Learning Python / Imparare Python* — string object coverage;
- *Fluent Python* — controllo correttezza Unicode/sequence;
- `friedpython@cb3f3dc...` come source pack legacy, non copiato direttamente.
