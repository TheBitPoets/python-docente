# M18 — Ricerca, membership, metodi e normalizzazione delle stringhe

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-06 — Stringhe come sequenze e testo  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- usare `in` e `not in`;
- usare `find()` quando serve una posizione e interpretare correttamente `-1`;
- usare `count()` quando coincide con il requisito;
- usare `lower()`, `upper()`, `strip()`, `replace()`, `startswith()` e `endswith()`;
- capire che i metodi di `str` restituiscono nuove stringhe;
- scegliere tra metodo built-in e loop esplicito;
- normalizzare testo in modo consapevole;
- riconoscere alcuni errori tipici nell'uso di `find()` e `strip()`.

---

# 1. La domanda viene prima del metodo

Problema:

> La stringa contiene il carattere `@`?

Se serve soltanto una risposta sì/no:

```python
if "@" in email:
    ...
```

comunica direttamente l'intenzione.

---

# 2. `in` e `not in`

```python
"py" in "python"      # True
"java" in "python"   # False
"x" not in "python"  # True
```

Membership risponde:

```text
esiste questa sottostringa?
```

Non restituisce la posizione.

---

# 3. `find()`

```python
posizione = testo.find("@")
```

Se la sottostringa viene trovata, restituisce l'indice della prima occorrenza.

Se non viene trovata:

```text
-1
```

Quindi:

```python
if testo.find("@") != -1:
    ...
```

è possibile, ma se non serve la posizione `in` è spesso più leggibile.

---

# 4. Errore classico: `find()` usato come booleano

Questo è pericoloso:

```python
if testo.find("a"):
    ...
```

Perché:

- se `a` è in posizione `0`, il risultato è `0`, che è falsy;
- se non c'è, il risultato è `-1`, che è truthy.

Il codice comunica il contrario di ciò che molti beginner immaginano.

---

# 5. `count()`

```python
"banana".count("a")
```

restituisce `3`.

Usalo quando il requisito è davvero:

> quante occorrenze secondo la semantica standard del metodo?

Non riscrivere manualmente una scansione se l'obiettivo non è imparare quell'algoritmo.

---

# 6. Trasformazioni restituiscono nuove stringhe

```python
testo = " Python "
nuovo = testo.strip()
```

`testo` non viene modificato in posto.

La stringa è immutabile.

Errore tipico:

```python
testo.lower()
print(testo)
```

Se vuoi conservare il risultato:

```python
testo = testo.lower()
```

oppure usa una nuova variabile.

---

# 7. `lower()` e `upper()`

```python
nome.lower()
nome.upper()
```

Utili per confronti/normalizzazioni semplici.

Esempio:

```python
risposta = input().strip().lower()
if risposta == "si":
    ...
```

La normalizzazione deve essere una scelta del requisito, non un automatismo.

---

# 8. `strip()`

```python
"  ciao  ".strip()
```

rimuove caratteri di whitespace ai bordi secondo la semantica del metodo.

Attenzione:

```python
strip(chars)
```

non significa “rimuovi esattamente questa sottostringa dai bordi”. Il parametro indica un insieme di caratteri da rimuovere alle estremità.

---

# 9. Prefissi e suffissi

```python
testo.startswith("http")
testo.endswith(".py")
```

Quando il requisito parla di prefisso/suffisso, questi metodi esprimono bene l'intenzione.

---

# 10. `replace()`

```python
nuovo = testo.replace("-", " ")
```

restituisce una nuova stringa con le sostituzioni previste.

Domanda:

> voglio sostituire tutte le occorrenze secondo questa regola oppure sto cercando una trasformazione più specifica?

---

# 11. Metodo vs algoritmo manuale

Per imparare un pattern:

```python
def conta_vocali(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.lower() in "aeiou":
            conteggio += 1
    return conteggio
```

Qui il loop è parte dell'obiettivo didattico.

Se il problema reale coincide con un metodo standard, il metodo può essere più diretto.

---

# 12. Criterio di scelta

```text
capisco l'algoritmo
+
conosco gli strumenti standard
+
scelgo ciò che comunica meglio l'intenzione
```

Non vale:

```text
built-in sempre migliore
```

né:

```text
loop manuale sempre più didattico
```

Dipende dall'outcome.

---

# 13. Normalizzazione

Pattern comune:

```python
normalizzato = testo.strip().lower()
```

Prima chiediti:

- voglio ignorare spazi esterni?;
- voglio ignorare maiuscole/minuscole?;
- sto perdendo un'informazione che invece serviva?.

Normalizzare significa cambiare la rappresentazione per confrontarla/elaborarla in modo coerente.

---

# 14. Worked example: risposta sì/no

```python
def risposta_affermativa(testo):
    normalizzato = testo.strip().lower()
    return normalizzato == "si"
```

Casi:

```text
"si"       → True
" SI "     → True
"no"       → False
"sì"       → dipende dal contratto: è un caso diverso da definire
```

La specifica deve dire quali forme accetta.

---

# 15. Error Clinic

- `find()` usato come booleano;
- risultato di `lower()`/`strip()` ignorato;
- `strip(chars)` interpretato come rimozione di sottostringa;
- normalizzazione applicata al dato sbagliato;
- metodo standard riscritto manualmente senza obiettivo didattico;
- confronto case-sensitive quando il requisito richiede normalizzazione.

---

# 16. Activity candidate

- **A — Choose the operation:** membership, posizione, prefisso, normalizzazione, sostituzione;
- **B — Controlled Change:** da confronto case-sensitive a confronto normalizzato;
- **C — Implement:** semplice validator/normalizzatore;
- **D — Debug:** correggi `find`, metodo non assegnato, strip e normalizzazione.

Nessuna nuova Activity P2 viene materializzata finché il profilo function-behavior non è certificato.

---

# 17. Checkpoint

Sai spiegare:

1. `in` vs `find()`;
2. perché `find()` restituisce `-1`;
3. perché `if testo.find(...)` è fragile;
4. immutabilità e metodi che restituiscono nuove stringhe;
5. quando normalizzare;
6. metodo built-in vs loop manuale.

---

# 18. Sintesi

```text
serve solo sapere se esiste? → in
serve la posizione?          → find
serve contare?               → count se coincide col requisito
serve trasformare?           → metodo che restituisce nuova str
```

Nel prossimo modulo combineremo loop, funzioni e metodi in veri algoritmi su testo e parsing semplice.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 `str`;
- *Think Python / Pensare in Python* — strings/searching;
- *Learning Python / Imparare Python* — string methods;
- *Fluent Python* — Unicode correctness come controllo docente;
- `friedpython` pinned come fonte legacy da auditare prima di riuso.
