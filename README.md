# Python — curriculum docente

Repository canonico per il curriculum Python di TheBitPoets.

## Visione

Costruire un percorso di programmazione Python che parta da **zero assoluto** — problem solving, algoritmi, pseudocodice e diagrammi di flusso — e possa proseguire fino alle competenze richieste a un programmatore Python professionale.

Il repository contiene un curriculum generale riusabile su più anni. Il primo track operativo è:

- **Secondo anno**: 33 settimane × 3 ore = **99 ore**;
- ingresso: nessun prerequisito di programmazione;
- uscita target: programmazione strutturata solida, funzioni, stringhe, strutture dati fondamentali, file/eccezioni di base e introduzione completa a classi/oggetti;
- i moduli successivi restano disponibili come curriculum avanzato per anni successivi o approfondimenti.

## Principi di progettazione

1. **Prima il problema, poi il codice**: analisi, decomposizione, algoritmo, pseudocodice/flow chart, test mentale, implementazione.
2. **Scelta consapevole dei costrutti**: non basta far funzionare il programma; lo studente deve motivare `if/elif/else`, `for`, `while`, strutture dati e decomposizione scelti considerando leggibilità, correttezza e costo computazionale quando rilevante.
3. **Composizione reale**: condizioni e cicli annidati, cicli con selezioni, strutture dati annidate, funzioni che collaborano.
4. **Progressione per Activity**: osserva → modifica → implementa → debug → mini-progetto → prodotto integrato.
5. **Teoria + pratica + riflessione**: lesson, slide, esempi, esercizi graduati, debugging, test, rubriche e spiegazione del perché.
6. **Delivery riproducibile**: guide studente/docente, slide generate, CI, soluzioni/reference e integrazione TheBitLab dove supportata.
7. **Curriculum ≠ delivery**: contenuti e obiettivi vengono governati/versionati; errata, setup e chiarimenti possono evolvere senza cambiare il curriculum.

## Fonti e materiale esistente

- **Pensare da informatico / Think Python** come fonte didattica principale da mappare e modernizzare, senza copiarne passaggi non necessari.
- `TheBitPoets/friedpython` come **legacy/source pack**: esempi ed esercizi esistenti saranno auditati, classificati, revisionati e importati solo dove coerenti con il nuovo curriculum.
- documentazione Python e altre fonti autorevoli saranno catalogate in `sources/`.

## Stato

**Design phase**. Non iniziare ancora la produzione massiva delle lesson finché `doc/COURSE_ARCHITECTURE.md`, `doc/CURRICULUM_ROADMAP.md` e `tracks/secondo/COURSE_DESIGN.md` non sono approvati.

## Struttura prevista

```text
content/python/         lesson canoniche
activities/python/      Activity e relativi asset
slides/python/          deck sorgente
student/                guida e navigazione studente
teacher/                guida docente e delivery
tracks/secondo/         track 33 settimane / 99 ore
tracks/advanced/        prosecuzione professionale
sources/                catalogo fonti + mapping friedpython
projects/               progetti longitudinali/capstone
scripts/                automazione e validazione
tests/                  quality gates
doc/                    architettura, roadmap, decisioni e changelog
```

La struttura e il confine didattico del secondo anno vengono definiti prima di iniziare la produzione dei moduli.
