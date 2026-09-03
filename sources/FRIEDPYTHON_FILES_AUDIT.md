# `friedpython` — audit file per PY2-09 / M26

Snapshot:

```text
TheBitPoets/friedpython@cb3f3dc97f9c226dc04e8592d0485fa5bc612d7f
```

Scopo: usare il materiale legacy come gap-check, non come sorgente da copiare.

## Spunti riutilizzabili concettualmente

- apertura/lettura/scrittura file;
- differenza tra contenuto testuale e percorso;
- necessità di chiudere correttamente una risorsa;
- context manager `with`;
- iterazione sulle righe;
- distinzione testo/binario come concetto futuro.

## Modernizzazioni obbligatorie

1. Baseline Python 3.12-compatible.
2. Percorsi gestiti con `pathlib.Path` nei nuovi esempi quando migliora chiarezza/portabilità.
3. Encoding testuale dichiarato esplicitamente come UTF-8.
4. Preferire `Path.read_text()` / `write_text()` per le operazioni intere più semplici, mostrando anche `with open(...)` perché il context manager resta un concetto fondamentale.
5. Niente assunzioni su current working directory esterna al Course Workspace.
6. Niente path assoluti specifici Windows/Linux negli esercizi canonici.
7. Niente gestione generica `except Exception` per nascondere bug.
8. Binario, CSV, JSON e serializzazione non sono core M26.

## Error boundary

Nel core di seconda distinguere:

```text
bug del programma
vs
problema esterno prevedibile
```

Errori candidati:

- `FileNotFoundError` — file richiesto assente;
- `PermissionError` — accesso negato quando plausibile nel profilo;
- eventuale errore di conversione del contenuto soltanto se la specifica lo richiede.

Non introdurre gerarchie complete di eccezioni, custom exceptions, `else/finally` o filosofia EAFP/LBYL come argomento autonomo.

## TheBitLab P4

Il grading filesystem è tracciato in `TheBitPoets/2cornot2c#757`.

Requisiti pedagogici attesi:

- fixture dichiarate e non modificabili quando sono input;
- workdir scrivibile isolato;
- verifica host-side degli artifact prodotti;
- nessuna dipendenza da filesystem host dello studente;
- path confinement;
- expected non esposto al worker untrusted.

Fino alla certificazione P4:

- attività formative nel Classroom Environment;
- assert/manual evidence;
- nessuna Activity che prometta grading filesystem autorevole.

## Decisione M26

Core di 3 ore:

```text
Path
→ file testo UTF-8
→ read/write
→ with/open
→ righe
→ FileNotFoundError / PermissionError mirati
→ separazione I/O da logica
```

Rinvio:

```text
CSV / JSON / binario / regex / serializzazione / eccezioni avanzate → Stage B o enrichment
```

La scelta protegge le 12 ore OOP congelate di PY2-10.
