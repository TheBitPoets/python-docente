# M26 — Runbook docente

## Modulo

**File testo, `pathlib` ed errori esterni prevedibili**  
UDA PY2-09 — Persistenza ed errori prevedibili

Stato: draft editoriale controllato.

## Obiettivo docente

In sole 3 ore introdurre il boundary di persistenza senza trasformare M26 in un corso di filesystem/eccezioni.

Modello target:

```text
Path
→ file testo UTF-8
→ I/O piccolo
→ logica separata/testabile
→ errori esterni specifici
```

La priorità resta proteggere le 12 ore OOP congelate.

## Ora teoria attiva 1 — persistenza e Path

1. Memoria vs persistenza.
2. Percorso vs contenuto.
3. `Path("dati") / "file.txt"` dentro il workspace.
4. `read_text(..., encoding="utf-8")` e `write_text`.
5. Perché l'encoding è parte del contratto.

## Ora teoria attiva 2 — `with`, righe ed error boundary

1. `with percorso.open(...)` e context manager.
2. Iterazione sulle righe/newline.
3. Separazione I/O-logica.
4. `FileNotFoundError` mirato.
5. `PermissionError` come esempio di errore esterno.
6. Perché `except Exception: pass` è un anti-pattern beginner.

## Laboratorio

- lettura di fixture testo nel workspace;
- funzione pura che elabora il testo;
- assert sulla funzione senza filesystem;
- scrittura di un risultato;
- Debug Clinic su path, newline, encoding e except troppo ampio.

## Misconception watchlist

- path assoluto del proprio PC come requisito del programma;
- file = stringa del path;
- encoding irrilevante;
- `strip()` sempre sicuro sulle righe;
- `try/except` attorno a tutto il programma;
- qualsiasi eccezione = problema esterno;
- logica di dominio completamente mescolata con file I/O.

## Differenziazione

### Recupero

- `Path` già fornito;
- file piccolo;
- `read_text` prima di `open`;
- una sola eccezione mirata;
- logica già separata in funzione.

### Enrichment

- append mode soltanto se richiesto;
- conteggio/trasformazione per riga;
- `PermissionError` in scenario controllato;
- confronto `read_text` vs iterazione file.

## Evidence docente

Raccogliere:

- path relativo corretto;
- lettura/scrittura UTF-8;
- funzione di logica testata separatamente;
- gestione mirata di file mancante;
- spiegazione bug vs errore esterno.

## P4 TheBitLab

`2cornot2c#757` è il boundary futuro per grading filesystem:

```text
fixture read-only
+ workdir scrivibile isolato
+ artifact prodotti
+ verifica host-side
```

Fino alla certificazione:

- Classroom Environment;
- assert sulle funzioni pure;
- evidence/manual rubric sugli artifact;
- nessuna Activity P4 presentata come autogradata.

## Friedpython

Audit: `sources/FRIEDPYTHON_FILES_AUDIT.md`.

Usare solo concetti validi dopo riscrittura moderna: `pathlib`, UTF-8, workspace-relative, context manager. CSV/JSON/binario restano fuori dal core.

## Cosa NON anticipare

- CSV/JSON;
- binario;
- pickle;
- regex;
- custom exceptions;
- gerarchie eccezioni;
- filesystem traversal.

## Handoff a PY2-10

M26 chiude il blocco strutture/persistenza. Il corso entra ora nel traguardo finale:

```text
record/dict
→ classe/istanza
→ stato/metodi
→ invarianti
→ composizione
→ capstone OOP
```
