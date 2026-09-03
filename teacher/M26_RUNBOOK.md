# M26 — Runbook docente

## Modulo

**File testo, `pathlib` ed errori esterni prevedibili**  
UDA PY2-09 — Persistenza ed errori prevedibili

Stato: draft editoriale controllato.

## Obiettivo docente

In sole **3 ore core** introdurre il boundary di persistenza senza trasformare M26 in un corso di filesystem/eccezioni.

Modello target:

```text
Path relativo al workspace
→ file testo UTF-8
→ I/O piccolo
→ logica separata/testabile
→ errore esterno specifico
```

La priorità resta proteggere le 12 ore OOP congelate.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. distinguere dato in memoria e persistenza;
2. distinguere percorso e contenuto;
3. costruire un `Path` relativo al workspace;
4. leggere e scrivere un piccolo file testo dichiarando UTF-8;
5. usare un context manager `with` quando lavora esplicitamente con un file object;
6. iterare sulle righe in un esempio semplice;
7. separare I/O e logica di elaborazione;
8. gestire `FileNotFoundError` in modo mirato quando l'assenza è prevista;
9. distinguere bug del programma ed errore esterno prevedibile.

## GUIDED EXPOSURE

- `read_text/write_text` vs `Path.open` come due superfici per casi diversi;
- newline nelle righe;
- `PermissionError` come altro esempio di errore esterno;
- perché `except Exception: pass` è troppo ampio.

## ENRICHMENT / BACKUP

- append mode;
- confronto streaming vs lettura completa;
- trasformazioni riga-per-riga più ricche.

## TEACHER / DELIVERY ONLY

- P4 `2cornot2c#757`;
- fixture read-only/workdir isolato;
- artifact verification host-side;
- dettagli del grader filesystem.

P4 non è un concetto da studente.

---

# Ora teoria attiva 1 — persistenza, Path, UTF-8

## 0–10 min — memoria vs persistenza

Partire da un dict/list già noto e chiedere:

> che cosa rimane dopo che il processo termina?

## 10–25 min — percorso vs contenuto

```python
from pathlib import Path
percorso = Path("dati") / "misure.txt"
```

Il path dice **dove**, non contiene automaticamente il testo.

Usare solo percorsi relativi al workspace gestito.

## 25–40 min — lettura/scrittura semplice

```python
testo = percorso.read_text(encoding="utf-8")
percorso.write_text("ciao\n", encoding="utf-8")
```

Far emergere:

- encoding esplicito;
- lettura vs scrittura;
- scrittura che sostituisce il contenuto nella forma mostrata.

## 40–55 min — separare logica da I/O

Esempio:

```python
def somma_interi_testo(testo):
    ...
```

poi lettura del file e chiamata della funzione.

La funzione viene testata con stringhe normali, senza filesystem.

---

# Ora teoria attiva 2 — context manager, righe, error boundary

## 0–18 min — `with`

```python
with percorso.open("r", encoding="utf-8") as file:
    contenuto = file.read()
```

Modello beginner:

> il blocco delimita l'uso della risorsa e Python la chiude correttamente all'uscita.

Non aprire internals del context manager.

## 18–30 min — iterazione sulle righe

```python
with percorso.open("r", encoding="utf-8") as file:
    for riga in file:
        ...
```

Mostrare il newline e spiegare perché `strip()` non è automaticamente sicuro se gli spazi fanno parte del dato.

## 30–45 min — `FileNotFoundError`

```python
try:
    testo = percorso.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File non trovato")
```

Il `try` resta piccolo e circonda l'operazione che può fallire in quel modo.

## 45–55 min — bug vs errore esterno

Classificare casi:

```text
formula sbagliata → bug
file assente      → errore esterno previsto dal contratto
```

## Solo se resta tempo

Mostrare `PermissionError` o `except Exception: pass` come guided exposure. Non creare una nuova tassonomia da memorizzare.

---

# Laboratorio

## Fase A — fixture testo

Leggere un piccolo file del workspace.

## Fase B — logica separata

Passare il testo a una funzione già testabile con `assert`.

## Fase C — scrittura

Produrre un piccolo file risultato UTF-8.

## Fase D — righe

Usare `with` + iterazione su righe in un caso controllato.

## Fase E — Debug Clinic

- path host-specific;
- file mancante;
- newline inatteso;
- encoding omesso;
- logica mescolata all'I/O;
- `try` troppo ampio.

Il laboratorio deve restare piccolo. Se il core non è stabile, non aggiungere append mode o più eccezioni.

---

# Minimum mastery gate — prima di OOP

Considerare M26 consolidato quando lo studente riesce a:

- spiegare memoria vs persistenza;
- costruire un Path relativo al workspace;
- leggere/scrivere testo UTF-8;
- usare `with` su un file object;
- iterare su righe in un esempio semplice;
- tenere la logica di elaborazione in una funzione separata;
- gestire un `FileNotFoundError` specifico;
- spiegare la differenza fra bug ed errore esterno.

`PermissionError`, append mode e dettagli P4 non fanno parte del gate ordinario.

---

# Misconception watchlist

- path assoluto del proprio PC come requisito canonico;
- path confuso col contenuto;
- encoding considerato irrilevante;
- `strip()` usato automaticamente su ogni riga;
- `try/except` attorno a tutto il programma;
- qualsiasi eccezione interpretata come “problema esterno”;
- logica di dominio completamente mescolata all'I/O;
- P4/grader scambiato per parte della lezione studente.

---

# Differenziazione

## Recupero

- `Path` già fornito;
- file molto piccolo;
- `read_text` prima di `open`;
- una sola eccezione mirata;
- funzione di logica già separata da completare.

## Enrichment

- append mode se il requisito lo chiede;
- confronto lettura completa vs per-riga;
- `PermissionError` in scenario controllato;
- trasformazione per riga più ricca.

---

# Evidence docente

Raccogliere:

- path relativo corretto;
- lettura/scrittura UTF-8;
- esempio `with`;
- funzione di logica testata senza filesystem;
- gestione mirata di file mancante;
- spiegazione bug vs errore esterno.

---

# P4 TheBitLab — teacher/delivery boundary

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

Questa sezione riguarda il delivery, non il mastery studente.

---

# Friedpython

Audit: `sources/FRIEDPYTHON_FILES_AUDIT.md`.

Usare solo concetti validi dopo riscrittura moderna:

```text
pathlib
UTF-8
workspace-relative
context manager
I/O separato
```

CSV/JSON/binario restano fuori dal core.

---

# Cosa NON anticipare

- CSV/JSON;
- binario;
- pickle;
- regex;
- custom exceptions;
- gerarchie eccezioni;
- filesystem traversal.

---

# Handoff a PY2-10

M26 chiude il blocco strutture/persistenza.

Il corso entra ora nel traguardo finale:

```text
record/dict
→ classe/istanza
→ stato/metodi
→ invarianti
→ composizione
→ capstone OOP
```
