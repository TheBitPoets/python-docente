# M19 — Algoritmi su testo e parsing semplice

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-06 — Stringhe come sequenze e testo  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- combinare funzioni, cicli, selezione e metodi su stringhe;
- contare caratteri che soddisfano una proprietà;
- costruire progressivamente una nuova stringa quando serve;
- progettare e testare un palindromo semplice con normalizzazione dichiarata;
- validare pattern testuali elementari senza regex;
- estrarre parti con indici/slicing;
- progettare casi limite su stringa vuota, un carattere, spazi e maiuscole/minuscole;
- distinguere analisi del testo e formattazione dell'output;
- confrontare algoritmo manuale e soluzione basata su metodi;
- usare `split()` come ponte consapevole verso la prossima UDA sulle liste.

---

# 1. Le stringhe riusano tutto ciò che abbiamo imparato

Un algoritmo su testo combina:

```text
funzioni
+ loop
+ if
+ contatori/accumulatori
+ indici/slice
+ metodi str
+ test
```

La stringa cambia il dominio del problema, non le regole fondamentali del ragionamento.

---

# 2. Conteggio di caratteri

```python
def conta_cifre(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.isdigit():
            conteggio += 1
    return conteggio
```

Invariante:

> `conteggio` è il numero di caratteri cifra già elaborati.

---

# 3. Costruire una nuova stringa

Per piccoli esercizi beginner:

```python
def solo_lettere(testo):
    risultato = ""
    for carattere in testo:
        if carattere.isalpha():
            risultato += carattere
    return risultato
```

Qui `risultato` è un accumulatore testuale.

Teacher note: per grandi quantità di frammenti esistono strategie più efficienti; non serve complicare ora il modello.

---

# 4. Palindromo: prima l'algoritmo

Problema:

> Una parola è uguale letta da sinistra a destra e da destra a sinistra?

Prima del trucco compatto, ragioniamo sulle posizioni opposte.

Esempio:

```text
radar
0 ↔ -1
1 ↔ -2
centro
```

L'obiettivo è capire il confronto, non memorizzare una slice.

---

# 5. Versione con inversione

Dopo aver compreso l'algoritmo possiamo confrontare:

```python
def palindroma(testo):
    return testo == testo[::-1]
```

Domande:

- è corretta rispetto al contratto?;
- come gestiamo maiuscole?;
- spazi/punteggiatura vanno ignorati?;
- il requisito parla di parola o frase?.

La normalizzazione deve essere definita prima.

---

# 6. Normalizzazione del palindromo

Esempio di contratto semplice:

> Ignora spazi ai bordi e differenze maiuscole/minuscole; non rimuovere punteggiatura interna.

```python
def palindroma(testo):
    normalizzato = testo.strip().lower()
    return normalizzato == normalizzato[::-1]
```

Se il contratto cambia, cambiano anche i test.

---

# 7. Casi limite

Per una funzione testuale considera almeno:

```text
""        stringa vuota
"a"       un carattere
"Radar"   maiuscole
" radar " spazi ai bordi
```

Non esiste una risposta universale per ogni contratto: definisci prima il comportamento atteso.

---

# 8. Parsing semplice con posizioni note

Codice:

```text
ABC-123
```

Contratto:

```text
3 lettere
-
3 cifre
```

Possiamo controllare:

```python
def codice_valido(codice):
    if len(codice) != 7:
        return False
    return codice[:3].isalpha() and codice[3] == "-" and codice[4:].isdigit()
```

Questo è parsing posizionale semplice, senza regex.

---

# 9. Perché niente regex adesso?

Le espressioni regolari sono potenti, ma introdurle qui può nascondere:

- indici;
- slicing;
- composizione booleana;
- struttura del formato.

Regex appartiene al percorso avanzato/optional dopo che il modello base è stabile.

---

# 10. Analisi vs presentazione

Preferiamo:

```python
def conta_vocali(testo):
    ...
    return conteggio
```

poi:

```python
risultato = conta_vocali(testo)
print(risultato)
```

La funzione di analisi non deve stampare se il suo contratto è produrre un valore.

---

# 11. Metodo vs loop: confronto esplicito

Problema:

> Quante volte compare `a`?

Versione standard:

```python
testo.count("a")
```

Versione manuale:

```python
conteggio = 0
for carattere in testo:
    if carattere == "a":
        conteggio += 1
```

Entrambe possono essere corrette.

La scelta dipende dall'outcome:

- imparare scansione/contatore? → loop;
- esprimere una operazione standard? → metodo.

---

# 12. `split()` come ponte verso le liste

```python
parti = "rosso,verde,blu".split(",")
```

Il risultato non è una stringa.

È una:

```text
list
```

Per ora basta sapere che `split()` produce più pezzi raccolti in una struttura. Nella prossima UDA studieremo davvero liste, mutabilità, alias e metodi.

---

# 13. `join()` come preview controllata

Se abbiamo già una sequenza di frammenti, Python può unirli:

```python
",".join(parti)
```

Non serve ancora padroneggiare tutte le regole delle liste. È un ponte concettuale:

```text
stringa → split → più parti
più parti → join → stringa
```

---

# 14. Worked example: normalizzatore di username

Contratto semplice:

- rimuovi spazi ai bordi;
- converti in minuscolo;
- deve avere almeno 3 caratteri;
- deve contenere solo lettere/cifre/underscore.

```python
def username_valido(testo):
    nome = testo.strip().lower()
    if len(nome) < 3:
        return False

    for carattere in nome:
        if not (carattere.isalnum() or carattere == "_"):
            return False

    return True
```

Questo riusa funzioni, loop, `if`, metodi e `return`.

---

# 15. Error Clinic

- stringa vuota non considerata;
- off-by-one sugli indici;
- normalizzazione incompleta;
- tentativo di mutazione;
- risultato di un metodo ignorato;
- parsing che assume lunghezza senza verificarla;
- `split()` usato senza capire che restituisce una lista.

---

# 16. Activity candidate

- **A — Text trace:** indice/carattere/accumulatore;
- **B — Controlled Change:** cambia regola di normalizzazione e aggiorna i test;
- **C — Implement:** funzione testuale con contratto e casi limite;
- **D — Debug:** off-by-one, immutabilità, metodi, stringa vuota;
- **E — Mini-project:** analizzatore/normalizzatore con più funzioni e almeno 5 casi.

Nessuna nuova Activity P2 viene materializzata finché il profilo function-behavior non è certificato.

---

# 17. Exit checkpoint PY2-06

Dovresti saper:

- trattare `str` come sequenza immutabile;
- usare indici/slicing;
- scegliere iterazione diretta/per indice;
- usare membership e metodi appropriati;
- normalizzare consapevolmente;
- implementare un algoritmo testuale con loop;
- progettare casi limite;
- scrivere funzioni testabili su testo;
- motivare metodo vs loop;
- capire che `split()` produce una lista.

---

# 18. Sintesi

```text
str + loop + if + funzioni + test
→ algoritmi su testo
```

```text
split()
→ ponte verso list
```

La prossima UDA studierà proprio le liste: come si modificano, come si copiano e perché due nomi possono riferirsi alla stessa struttura.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 `str`;
- *Think Python / Pensare in Python* — string algorithms;
- *Learning Python / Imparare Python* — strings;
- *Fluent Python* — controllo teacher-side su Unicode/sequence;
- `friedpython` pinned come legacy source pack da auditare prima di riuso.
