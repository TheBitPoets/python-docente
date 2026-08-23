# PY2-09 — Persistenza ed errori prevedibili

> Stato: **specifica didattica DRAFT**. Non è ancora la lesson finale né un curriculum freeze.

## Collocazione

- track: secondo anno;
- finestra core: settimana 28;
- monte ore: 3 ore core, estendibile usando buffer se il calendario lo permette;
- prerequisiti: stringhe, strutture dati, funzioni, errori/runtime e test di base;
- baseline: Python 3.12;
- output: lo studente legge/scrive semplici file di testo nel workspace, usa `pathlib` per i path, apre risorse con `with`, gestisce pochi errori esterni prevedibili con `try/except` specifici e distingue un errore del dato/risorsa da un bug del programma.

## Perché questa UDA è volutamente piccola

Il secondo anno deve arrivare all'OOP. File ed eccezioni sono importanti, ma non devono assorbire settimane di dettagli I/O avanzati prima delle classi.

Core:

```text
Path
→ file di testo UTF-8
→ with/open
→ lettura/scrittura
→ iterazione per riga
→ errore esterno prevedibile
→ try/except specifico
```

CSV, JSON, binario, custom exceptions e gestione avanzata restano enrichment/Stage B.

---

# M26 — File di testo, `pathlib`, `with` ed error boundaries

## Obiettivi osservabili

Lo studente sa:

1. distinguere dati in memoria e dati persistenti su file;
2. usare un path relativo al workspace;
3. creare un `Path` con `pathlib.Path`;
4. aprire un file di testo con encoding UTF-8 esplicito;
5. usare `with open(...)` e spiegare che la risorsa viene chiusa anche quando il blocco termina;
6. leggere tutto un piccolo file quando appropriato;
7. iterare riga per riga;
8. scrivere/sovrascrivere un piccolo file;
9. usare append soltanto quando la specifica lo richiede;
10. comprendere a livello beginner i modi `r`, `w`, `a`;
11. distinguere `FileNotFoundError`, errore di conversione del contenuto e bug del codice;
12. catturare un'eccezione **specifica** e gestire un caso previsto;
13. evitare `except:`/`except Exception` come modo per nascondere bug;
14. mantenere stretto il blocco `try` attorno all'operazione realmente fallibile;
15. progettare test/evidence con file esistente, mancante, vuoto e contenuto inatteso quando rilevante.

## Modello mentale: persistenza

```text
programma termina
ma
file resta nel filesystem
```

Il file introduce un boundary esterno:

- può non esistere;
- può avere contenuto inatteso;
- può non essere accessibile;
- può essere modificato da altro software/utente.

Il programma deve decidere quali casi sono parte del proprio contratto.

## Path: usare `pathlib`

Target:

```python
from pathlib import Path

percorso = Path("dati") / "voti.txt"
```

Non insegnare concatenazioni manuali tipo:

```python
"dati/" + nome
```

come modello generale dei path.

Evitiamo inoltre path assoluti specifici del PC docente/studente.

## Lettura con `with`

```python
from pathlib import Path

percorso = Path("dati.txt")

with percorso.open("r", encoding="utf-8") as file:
    testo = file.read()
```

Oppure, quando il focus è sulle righe:

```python
with percorso.open("r", encoding="utf-8") as file:
    for riga in file:
        ...
```

Il context manager è core perché elimina la gestione manuale fragile di `close()`.

## Newline e normalizzazione

Una riga letta può contenere `\n`.

Non insegnare automaticamente:

```python
riga.strip()
```

senza spiegare che `strip` rimuove whitespace anche ai bordi del contenuto.

Se il requisito è soltanto rimuovere newline finale, valutare:

```python
riga.rstrip("\n")
```

oppure normalizzazione esplicitamente richiesta.

## Scrittura

```python
with percorso.open("w", encoding="utf-8") as file:
    file.write("ciao\n")
```

Spiegare chiaramente:

- `w` sovrascrive/tronca;
- `a` aggiunge in fondo;
- scegliere il modo in base al requisito.

Il rischio di perdita dati è parte del modello mentale.

## `Path.read_text` / `write_text`

Possono essere mostrati come convenience per file piccoli:

```python
contenuto = percorso.read_text(encoding="utf-8")
```

ma `with/open` resta core per comprendere il modello di risorsa/stream e per l'iterazione riga per riga.

## Error boundary

### File mancante previsto

```python
try:
    contenuto = percorso.read_text(encoding="utf-8")
except FileNotFoundError:
    print("file non disponibile")
```

### Dato non convertibile

```python
try:
    valore = int(testo)
except ValueError:
    print("dato non valido")
```

Non mettere tutto il programma dentro un unico `try` enorme.

## Bug vs errore previsto

Esempi:

- utente indica un file opzionale che non esiste → caso esterno prevedibile;
- riga dovrebbe essere un intero ma contiene testo → dato non valido previsto dal dominio;
- programmatore usa nome variabile inesistente → bug, non da nascondere con `except` generico.

Questa distinzione è più importante di imparare molte classi di eccezione.

## `else`/`finally`/custom exceptions

Fuori dal core di questa settimana.

`with` copre già il principale bisogno di cleanup della risorsa file.

Stage B approfondirà:

- `else`/`finally`;
- `raise`;
- eccezioni custom;
- exception chaining;
- EAFP/LBYL come trade-off Pythonico.

## Dati semplici da persistere

Core candidate:

- una riga per valore;
- elenco di nomi/voti;
- piccolo log testuale;
- configurazione elementare key/value solo se non richiede parsing artificioso.

Non inventare un formato complesso per evitare JSON: JSON verrà introdotto nel livello successivo quando serve davvero.

---

# Activity candidate

## A — Read/trace

Dato un file di 3–4 righe e un programma, prevedere valori letti/output.

## B — Controlled Change

Cambiare da lettura completa a elaborazione riga-per-riga o modificare il path relativo previsto.

## C — Implement

Funzione/programmino che legge numeri da file, ignora/gestisce secondo contratto un caso definito e produce un aggregato.

## D — Debug Clinic

- path assoluto del docente;
- file non chiuso manualmente;
- `w` usato quando serviva `a`;
- `strip` che elimina dati significativi;
- `except:` che nasconde un bug;
- `try` troppo ampio;
- `FileNotFoundError` non previsto.

## E — Enrichment

Persistenza di una struttura semplice via CSV/JSON, soltanto se il gruppo/calendario lo permette.

---

# `friedpython` — policy specifica PY2-09

Snapshot:

`TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f`

Materiale individuato:

- `apertura_di_un_file.py`;
- `esempi_uso.py`;
- `gestori_di_contesto.py`;
- `file_binari.py`;
- fixture storiche `myfile.txt` / `myfile.bin`.

## Core candidate

- apertura/lettura/scrittura testuale dopo audit;
- context manager `with`.

## Enrichment/Stage B

- binario;
- dettagli avanzati delle modalità;
- serializzazione più complessa.

Ogni esempio legacy deve essere trasformato per:

- `pathlib`;
- UTF-8 esplicito;
- workspace relativo;
- nessun path host-specific;
- separazione starter/fixture/solution;
- error handling moderno e specifico.

---

# Grading/TheBitLab: boundary da progettare

Il runner P1 attuale è single-source + stdin/stdout e non deve essere forzato a simulare file tramite input testuale quando l'outcome è filesystem I/O.

Serve un profilo futuro, qui chiamato provvisoriamente:

```text
P4 — filesystem behavior
```

Requisiti:

- fixture teacher dichiarate copiate **read-only** nel sandbox;
- directory di lavoro studente isolata e scrivibile quando il test richiede output file;
- path relativi stabili;
- nessun mount del repository docente completo;
- test host-side sugli artifact prodotti;
- limiti numero/dimensione file;
- niente symlink/path traversal;
- cleanup tra test;
- report di file mancanti/creati/modificati senza esporre contenuto teacher non autorizzato.

Finché P4 non è certificato:

- file lab nel Classroom Environment;
- evidence manuale/rubric;
- test locali controllati su fixture studente quando appropriato;
- nessun fake autograding che sostituisce il filesystem reale con stringhe se cambia l'obiettivo.

---

# Piano della settimana 28

## Ora teoria attiva 1

- memoria vs persistenza;
- Path relativi;
- `pathlib`;
- `with/open`;
- read vs iterazione righe.

## Ora teoria attiva 2

- write/append;
- UTF-8/newline;
- error boundary;
- FileNotFoundError/ValueError;
- Debug Clinic.

## Ora laboratorio

- lettura/elaborazione/scrittura piccolo file;
- esercizio con file mancante;
- evidence manuale/test locale;
- eventuale enrichment JSON solo se tempo.

---

# Exit checkpoint UDA

Lo studente dovrebbe saper:

- usare `Path` relativo;
- aprire file testo UTF-8 con `with`;
- leggere tutto o iterare righe secondo il problema;
- scrivere/sovrascrivere/appendere consapevolmente;
- distinguere file mancante e bug;
- catturare almeno `FileNotFoundError`/`ValueError` quando il contratto lo richiede;
- evitare `except` generico;
- spiegare perché il blocco `try` dovrebbe essere stretto;
- elaborare dati persistenti con funzioni/strutture già apprese.

---

# Remediation

- un file già fornito nel workspace;
- path fisso relativo;
- sola lettura prima della scrittura;
- una riga → una trasformazione;
- errore file mancante separato dall'errore contenuto;
- template `with` già fornito prima della scrittura autonoma.

# Enrichment

- `Path.read_text/write_text`;
- CSV standard library;
- JSON;
- modalità binaria/bytes;
- atomic write come concetto professionale, non implementazione core;
- encoding errors come preview.

---

# Fonti

- *Think Python / Pensare in Python*: files/exceptions;
- *Learning Python / Imparare Python*: file objects/exceptions coverage;
- *Python in a Nutshell*: file/path/exceptions reference;
- documentazione Python 3.12 `pathlib`, `open`, exceptions;
- Pluralsight Python Essentials/File Operations;
- `friedpython` pinned legacy pack.

---

# Criteri per produzione

- `pathlib` è il modello path core;
- UTF-8 esplicito;
- context manager core;
- binary/JSON/CSV non bloccano OOP;
- error handling specifico, niente catch-all beginner;
- P4 filesystem grader progettato oppure Activity filesystem marcate manual/formative;
- esempi legacy auditati e privi di path host-specific;
- l'intera UDA rimane completabile in una settimana core.
