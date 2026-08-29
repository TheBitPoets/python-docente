# M26 — File testo, `pathlib` ed errori esterni prevedibili

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-09 — Persistenza ed errori prevedibili  
> **Durata:** 3 ore core  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- spiegare perché un dato in memoria scompare quando il programma termina;
- rappresentare un percorso con `pathlib.Path`;
- leggere un intero file testo UTF-8;
- scrivere un intero file testo UTF-8;
- usare `with open(..., encoding="utf-8")` quando serve lavorare con una risorsa file;
- iterare sulle righe di un file;
- separare lettura/scrittura dalla logica di elaborazione;
- distinguere un bug da un errore esterno prevedibile;
- gestire in modo mirato almeno `FileNotFoundError`;
- riconoscere `PermissionError` come possibile errore esterno;
- mantenere tutti i file dentro il workspace gestito dal corso.

---

# 1. Memoria e persistenza

Durante l'esecuzione:

```python
voti = {"Anna": 8, "Luca": 7}
```

vive in memoria.

Quando il processo termina, quella struttura non diventa automaticamente persistente.

Un file permette di conservare dati tra esecuzioni.

---

# 2. Percorso e contenuto sono concetti diversi

```python
from pathlib import Path

percorso = Path("dati") / "messaggio.txt"
```

`percorso` rappresenta **dove** si trova il file.

Il contenuto è ciò che leggiamo o scriviamo in quel percorso.

Questa distinzione prepara anche software più grande e testabile.

---

# 3. Workspace del corso

Nel corso usiamo soltanto percorsi relativi al workspace gestito TheBitLab.

Esempio:

```text
dati/messaggio.txt
```

Non scrivere esercizi canonici che dipendono da:

```text
C:\Users\Mario\Desktop\...
/home/mario/...
```

Il corso deve funzionare allo stesso modo a scuola e a casa.

---

# 4. Leggere tutto il testo con `Path`

```python
from pathlib import Path

percorso = Path("dati") / "messaggio.txt"
testo = percorso.read_text(encoding="utf-8")
print(testo)
```

Per file piccoli e interamente testuali questa forma è molto leggibile.

---

# 5. Scrivere tutto il testo

```python
from pathlib import Path

percorso = Path("dati") / "risultato.txt"
percorso.write_text("ciao\n", encoding="utf-8")
```

La scrittura sostituisce il contenuto del file nella forma mostrata.

Il contratto deve chiarire se vogliamo sostituire o aggiungere dati.

---

# 6. Perché dichiariamo UTF-8

Un file testo è una sequenza di byte che deve essere interpretata secondo un encoding.

Nel corso scegliamo esplicitamente:

```text
UTF-8
```

Non approfondiamo ancora byte/code point/normalizzazione Unicode.

Il principio è:

> l'encoding è parte del contratto del file testuale.

---

# 7. `with open(...)`

Per capire il context manager:

```python
from pathlib import Path

percorso = Path("dati") / "messaggio.txt"

with percorso.open("r", encoding="utf-8") as file:
    contenuto = file.read()
```

All'uscita dal blocco `with`, la risorsa viene chiusa correttamente anche se durante il blocco si verifica un'eccezione.

---

# 8. Iterare sulle righe

```python
with percorso.open("r", encoding="utf-8") as file:
    for riga in file:
        print(riga.rstrip("\n"))
```

Attenzione: la riga letta può contenere il terminatore di riga.

Non usare `strip()` automaticamente se spazi iniziali/finali fanno parte del dato.

---

# 9. Separare I/O e logica

Preferiamo:

```python
def conta_righe_non_vuote(testo):
    conteggio = 0
    for riga in testo.splitlines():
        if riga.strip() != "":
            conteggio += 1
    return conteggio
```

poi:

```python
testo = percorso.read_text(encoding="utf-8")
risultato = conta_righe_non_vuote(testo)
```

La funzione di logica può essere testata senza dipendere dal filesystem.

---

# 10. `FileNotFoundError`

Se proviamo a leggere un file che non esiste:

```python
percorso.read_text(encoding="utf-8")
```

Python può generare:

```text
FileNotFoundError
```

Questo è un errore esterno prevedibile quando il file può legittimamente mancare.

---

# 11. Gestione mirata

```python
try:
    testo = percorso.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File non trovato")
```

Il blocco `try` deve essere **piccolo** e circondare l'operazione che può generare quell'errore.

Non usare:

```python
except Exception:
    pass
```

per nascondere qualunque problema.

---

# 12. `PermissionError`

Un altro possibile problema esterno è:

```text
PermissionError
```

quando il processo non può leggere/scrivere un percorso.

Nel Classroom Environment ben configurato questo dovrebbe essere raro, ma sapere distinguere “permesso negato” da “bug della funzione di calcolo” è utile.

---

# 13. Bug vs errore esterno

## Bug

```python
risultato = prezzo + quantita
```

quando serviva una moltiplicazione.

## Errore esterno

```text
file richiesto assente
permesso negato
```

Non trattarli allo stesso modo.

---

# 14. Worked example: diario di misure

File:

```text
12
15
9
```

Funzione di parsing/logica:

```python
def somma_interi_testo(testo):
    totale = 0

    for riga in testo.splitlines():
        if riga.strip() != "":
            totale += int(riga)

    return totale
```

I/O:

```python
percorso = Path("dati") / "misure.txt"
testo = percorso.read_text(encoding="utf-8")
print(somma_interi_testo(testo))
```

---

# 15. Testare la logica senza file

```python
assert somma_interi_testo("12\n15\n9\n") == 36
assert somma_interi_testo("") == 0
assert somma_interi_testo("5\n\n7\n") == 12
```

Questa separazione riduce la parte che richiede un vero filesystem.

---

# 16. TheBitLab P4

Un grading file corretto deve poter fornire:

```text
fixture input controllata
+ workdir scrivibile isolato
+ verifica host-side degli artifact
```

È il profilo `python-filesystem-v1` tracciato in `2cornot2c#757`.

Il **candidato software P4 è ora provato end-to-end** anche attraverso il normale Student Lab Docker:

- fixture di grading teacher-side montata read-only;
- workdir isolato e bounded;
- expected artifact confrontato sul trusted host;
- traversal/path esterni/symlink/subdirectory bloccati nel profilo v1;
- `FileNotFoundError` mantenuto come errore del programma studente;
- output limit e timeout fail-closed;
- report teacher-only redatto prima della vista studente;
- primo consumer reale M26 verde in CI.

Questa evidenza **non equivale ancora a release P4 stabile**. Il candidato deve essere unificato con la toolchain P2 e ricevere una nuova identità/digest immutabile prima della materializzazione P4 più ampia.

---

# 17. Error Clinic

- path assoluto specifico del proprio PC;
- encoding omesso;
- `strip()` usato distruggendo spazi significativi;
- file aperto senza context manager quando serve una gestione esplicita;
- `except Exception` troppo ampio;
- `try` enorme che nasconde dove nasce il problema;
- logica mescolata completamente con I/O;
- scrittura che sovrascrive quando il requisito voleva conservare dati precedenti.

---

# 18. Activity candidate

Resta autorizzato **un solo canarino P4**:

```text
py2-activity-b-file-risultato-001
Controlled Change: print(totale) → risultato.txt
```

Il canarino usa una fixture pubblica piccola per le prove studente e una fixture teacher-side distinta per il grading autorevole. La soluzione deve creare l'artifact richiesto; lo starter calcola e stampa correttamente il totale ma fallisce perché non persiste `risultato.txt`.

Le altre forme restano candidate editoriali, non ancora materializzate in massa:

- **A — Path/contract trace:** percorso, input file, output atteso;
- **B — Controlled Change:** il canarino attuale;
- **C — Implement:** leggi file testo e applica una funzione già testabile;
- **D — Debug:** path, FileNotFoundError, newline, exception troppo ampia;
- **E — Mini-persistence:** produce un file risultato con evidence P4/manuale.

Finché P4 non riceve la release/toolchain immutabile unificata con P2, **non creare altre Activity P4 soltanto per aumentare la copertura automatica**.

---

# 19. Cosa NON entra nel core

- CSV;
- JSON;
- file binari;
- pickle/serializzazione;
- regex;
- custom exceptions;
- `else/finally` come capitolo;
- filesystem traversal;
- path assoluti host-specific.

Questi restano Stage B/enrichment.

---

# 20. Exit checkpoint M26

Sai:

1. memoria vs persistenza;
2. percorso vs contenuto;
3. `Path` relativo al workspace;
4. UTF-8 esplicito;
5. `read_text`/`write_text`;
6. `with open` e chiusura della risorsa;
7. iterazione righe;
8. separazione I/O-logica;
9. `FileNotFoundError` mirato;
10. bug vs errore esterno.

---

# 21. Sintesi

```text
Path
→ file testo UTF-8
→ I/O piccolo e isolato
→ logica testabile separatamente
```

```text
errore esterno prevedibile
→ except specifico e piccolo
```

Il prossimo blocco è il traguardo finale del secondo anno: **classi, oggetti, stato, invarianti, composizione e capstone OOP**.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 `pathlib`, `open`, text I/O ed eccezioni built-in;
- *Think Python / Pensare in Python* — files/debugging;
- *Learning Python / Imparare Python* — file objects/exceptions;
- audit `sources/FRIEDPYTHON_FILES_AUDIT.md`;
- TheBitLab `2cornot2c#757` — P4 filesystem behavior.
