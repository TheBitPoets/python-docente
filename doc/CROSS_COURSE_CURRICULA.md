# Curricula trasversali separati — Git e Container

## Principio

`python-docente` non deve assorbire corsi completi su Git o container.

Git e container sono competenze professionali trasversali che verranno sviluppate come **curricula autonomi**, riusabili da più anni e più materie. I corsi disciplinari (Python, TPSI, Romeo, ecc.) importano/richiamano soltanto il livello necessario nel punto in cui serve.

```text
Git curriculum ---------+
                        |
Container curriculum ---+--> Python / TPSI / Romeo / altri corsi
                        |
TheBitLab environment --+
```

## Corso Git — direzione approvata

Obiettivo futuro: un corso Git progressivo che accompagni gli studenti per più anni.

### Livello G1 — fondamenti / primo utilizzo

Adatto al primo biennio quando il workflow del corso lo richiede:

- perché esiste il versionamento;
- repository e working tree;
- stato delle modifiche;
- `git status`;
- `git diff`;
- `git add`;
- `git commit`;
- log/storia essenziale;
- messaggi di commit comprensibili;
- recupero da errori semplici senza comandi distruttivi improvvisati.

Nel track Python di seconda entra soltanto questo sottoinsieme minimo.

### Livello G2 — collaborazione di base

Per anni successivi:

- repository remoto;
- clone/fetch/pull/push;
- branch;
- merge;
- conflitti;
- `.gitignore`;
- tag;
- workflow individuale e di coppia.

### Livello G3 — collaborazione professionale

- pull request;
- code review;
- branch strategy;
- rebase con consapevolezza;
- cherry-pick quando appropriato;
- issue/commit/PR traceability;
- signed/verified provenance dove utile;
- CI associata al repository;
- release/tag workflow.

### Livello G4 — avanzato / internals e operations

- object model Git;
- refs/HEAD/index;
- reflog;
- reset/restore/revert con differenze e rischi;
- bisect;
- hooks;
- worktree;
- submodule/subtree come trade-off;
- repository grandi e binary assets;
- sicurezza delle credenziali;
- manutenzione/troubleshooting.

La distribuzione esatta per anno verrà definita nel futuro repository del corso Git.

## Materiale Git del docente

Le dispense esistenti del docente saranno richieste **quando inizieremo la progettazione del corso Git** oppure quando dovremo produrre il micro-modulo G1 integrato nel secondo anno Python.

Non servono ancora per chiudere l'architettura Python corrente.

Policy futura:

```text
dispense esistenti
→ audit
→ verifica con documentazione Git corrente
→ classificazione G1/G2/G3/G4
→ lesson/slide/Activity
→ corso Git canonico
```

## Corso Container — progetto separato

Il corso container/Docker resta un curriculum autonomo.

Repository sorgente esistente:

```text
kinderp/docker101
```

Backlog canonico già aperto nel repository:

```text
#1 — Future course rebuild: Italian Docker curriculum to TPSI5 standard
```

Direzione:

- audit e modernizzazione del corso inglese;
- adattamento/riscrittura in italiano;
- teoria + lab + troubleshooting;
- immagini/container/Dockerfile/layer/cache;
- storage/volumi;
- networking;
- Compose;
- registries;
- sicurezza/non-root;
- health/readiness;
- build/release/deploy;
- guide studente/docente;
- slide;
- Activity A–F;
- TheBitLab managed environment.

## Relazione con Python professionale

Il curriculum Python professionale deve insegnare **container literacy** sufficiente a impacchettare e distribuire un'applicazione Python, ma non duplicare il corso Container.

Esempio:

```text
Python professional
  -> perché containerizzare
  -> leggere/scrivere un Dockerfile Python essenziale
  -> build/run/config/health
  -> collegamento al corso Container per approfondimento
```

Analogamente il curriculum Python usa Git nel proprio workflow ma non diventa il corso Git.

## Regola di dipendenza

Un corso disciplinare può dichiarare una competenza Git/Container come:

- `introduced-here` — micro-concetto introdotto localmente perché necessario;
- `external-track` — rimando al curriculum trasversale;
- `prerequisite` — competenza richiesta da un livello precedente;
- `enrichment` — approfondimento facoltativo.

Non duplicare intere UDA Git/Container in più corsi.

## TheBitLab

Git e Container devono usare lo stesso Classroom Environment cross-course.

Il corso Git deve poter lavorare su repository didattici senza richiedere installazioni manuali esterne.

Il corso Container deve essere compatibile con i limiti/profili della piattaforma e distinguere chiaramente:

- container come oggetto di studio;
- container usato internamente da TheBitLab;
- grading sandbox;
- ambiente interattivo dello studente.

Questi boundary non vanno confusi nelle dispense.
