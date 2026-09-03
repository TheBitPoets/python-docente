---
marp: true
paginate: true
size: 16:9
title: M26 — File testo, pathlib ed errori
---

# M26 — File testo, `pathlib` ed errori prevedibili
## Un boundary minimo di persistenza in 3 ore

PY2-09 — Persistenza ed errori prevedibili

---

# Che cosa deve restare davvero?

```text
memoria vs persistenza
Path relativo al workspace
UTF-8
read / write
with
righe
I/O separato dalla logica
FileNotFoundError mirato
bug vs errore esterno
```

CSV/JSON/P4 e gerarchie di eccezioni non fanno parte del mastery.

---

# Memoria vs persistenza

```text
variabile/list/dict in memoria
→ termina il programma
→ il dato non viene conservato automaticamente
```

Un file permette di conservare dati tra esecuzioni.

---

# Percorso vs contenuto

```python
from pathlib import Path
percorso = Path("dati") / "messaggio.txt"
```

`Path` dice **dove**.  
Il file contiene **che cosa**.

Non confondere il percorso con il testo del file.

---

# Workspace gestito

Usiamo percorsi relativi:

```text
dati/messaggio.txt
```

Non path assoluti specifici del PC dello studente.

Il corso deve restare riproducibile a scuola e a casa.

---

# Leggere testo UTF-8

```python
testo = percorso.read_text(encoding="utf-8")
```

UTF-8 è parte del contratto del file testuale.

---

# Scrivere testo UTF-8

```python
percorso.write_text("ciao\n", encoding="utf-8")
```

Nella forma mostrata la scrittura sostituisce il contenuto.

Il requisito deve dire che cosa vogliamo ottenere.

---

# `with` e file object

```python
with percorso.open("r", encoding="utf-8") as file:
    contenuto = file.read()
```

Modello beginner:

> il blocco delimita l'uso della risorsa e Python la chiude correttamente all'uscita.

Niente internals del context manager ora.

---

# Iterare sulle righe

```python
with percorso.open("r", encoding="utf-8") as file:
    for riga in file:
        ...
```

Una riga letta può includere il terminatore di riga.

Non usare `strip()` automaticamente se gli spazi fanno parte del dato.

---

# Separare I/O e logica

```text
file → testo
       ↓
funzione di logica testabile
       ↓
risultato
```

Esempio:

```python
def somma_interi_testo(testo):
    ...
```

La funzione può essere testata senza un vero file.

---

# `FileNotFoundError`

Se l'assenza del file è prevista dal contratto:

```python
try:
    testo = percorso.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File non trovato")
```

Il `try` resta piccolo e vicino all'operazione che può fallire.

---

# Bug vs errore esterno

```text
formula sbagliata → bug del programma
file assente       → errore esterno prevedibile
```

Non trattarli allo stesso modo.

---

# GUIDED EXPOSURE — altri errori esterni

Un altro esempio può essere:

```text
PermissionError
```

Non serve memorizzare una gerarchia di eccezioni.

L'idea è soltanto:

> alcuni problemi provengono dall'ambiente esterno, non dalla formula/algoritmo.

---

# GUIDED EXPOSURE — except troppo ampio

Evita:

```python
except Exception:
    pass
```

per “far sparire” qualunque problema.

Intercetta solo l'errore esterno che il contratto prevede davvero.

---

# Testare senza filesystem

```python
assert somma_interi_testo("12\n15\n9\n") == 36
```

Più logica separiamo dall'I/O, più la parte centrale resta facile da testare.

---

# Non entra nel core

- CSV;
- JSON;
- binario;
- pickle;
- regex;
- eccezioni custom/avanzate;
- dettagli del grader filesystem.

Proteggiamo le 12 ore OOP.

---

# Minimum mastery checkpoint

Sai:

1. spiegare memoria vs persistenza?;
2. costruire un Path relativo?;
3. leggere/scrivere UTF-8?;
4. usare `with`?;
5. iterare sulle righe?;
6. separare I/O e logica?;
7. gestire `FileNotFoundError` in modo mirato?;
8. distinguere bug ed errore esterno?.

`PermissionError`, append mode e dettagli del grader non fanno parte del gate ordinario.

---

# Recap

```text
Path relativo
→ file UTF-8
→ I/O piccolo
→ logica separata/testabile
→ errore esterno mirato
```

Prossimo: classi e oggetti.
