---
marp: true
paginate: true
size: 16:9
title: M26 — File testo, pathlib ed errori
---

# M26 — File testo, `pathlib` ed errori prevedibili

PY2-09 — Persistenza ed errori prevedibili

---

# Memoria vs persistenza

```text
variabile/list/dict in memoria
→ termina il programma
→ dato non persistito automaticamente
```

Un file conserva dati tra esecuzioni.

---

# Percorso vs contenuto

```python
from pathlib import Path
percorso = Path("dati") / "messaggio.txt"
```

`Path` dice **dove**.  
Il file contiene **che cosa**.

---

# Workspace gestito

Usiamo percorsi relativi:

```text
dati/messaggio.txt
```

Non path assoluti specifici del PC dello studente.

---

# Leggere testo UTF-8

```python
testo = percorso.read_text(encoding="utf-8")
```

UTF-8 è parte del contratto del file.

---

# Scrivere testo UTF-8

```python
percorso.write_text("ciao\n", encoding="utf-8")
```

Chiarisci se il requisito vuole sostituire o aggiungere contenuto.

---

# `with open(...)`

```python
with percorso.open("r", encoding="utf-8") as file:
    contenuto = file.read()
```

Il context manager gestisce correttamente la risorsa.

---

# Iterare sulle righe

```python
with percorso.open("r", encoding="utf-8") as file:
    for riga in file:
        ...
```

Attenzione ai terminatori di riga.

---

# Separare I/O e logica

```text
file → testo
       ↓
funzione pura/testabile
       ↓
risultato
```

La logica non deve dipendere inutilmente dal filesystem.

---

# `FileNotFoundError`

File richiesto assente:

```python
try:
    testo = percorso.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File non trovato")
```

---

# Except mirato

Evita:

```python
except Exception:
    pass
```

Meglio intercettare il problema esterno previsto, vicino all'operazione che può generarlo.

---

# Bug vs errore esterno

```text
formula sbagliata → bug
file assente       → errore esterno prevedibile
permesso negato    → errore esterno prevedibile
```

---

# Testare senza filesystem

```python
assert somma_interi_testo("12\n15\n9\n") == 36
```

Più logica separiamo dall'I/O, più possiamo testarla facilmente.

---

# P4 TheBitLab

Target futuro:

```text
fixture input
+ workdir isolato
+ artifact output
+ verifica trusted host-side
```

`2cornot2c#757`.

---

# Non entra nel core

- CSV/JSON;
- binario;
- pickle;
- regex;
- eccezioni custom/avanzate.

Proteggiamo il tempo OOP.

---

# Checkpoint

Sai spiegare:

- memoria vs persistenza;
- Path vs contenuto;
- UTF-8;
- read/write;
- with;
- righe;
- FileNotFoundError;
- I/O vs logica.

---

# Recap

```text
Path → file UTF-8 → I/O isolato → logica testabile
```

Prossimo: classi e oggetti.
