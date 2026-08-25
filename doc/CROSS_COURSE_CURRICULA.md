# Curricula trasversali separati — Git e Container

> Stato: **Git curriculum materializzato in repository autonomo; Container curriculum separato**.

## Principio

`python-docente` non deve assorbire corsi completi su Git o container.

Git e container sono competenze professionali trasversali sviluppate come **curricula autonomi**, riusabili da più anni e più materie. I corsi disciplinari (Python, TPSI, Romeo, ecc.) consumano soltanto il livello necessario nel punto in cui serve.

```text
Git curriculum ---------+
                        |
Container curriculum ---+--> Python / TPSI / Romeo / altri corsi
                        |
TheBitLab environment --+
```

La dipendenza deve essere esplicita e verificabile, non una copia locale delle stesse dispense.

---

# Corso Git — stato corrente

Repository canonico:

```text
TheBitPoets/git
```

Architettura progressiva corrente:

```text
G1 — local fundamentals
G2 — branch / merge / remotes / collaboration
G3 — professional workflow / recovery / rebase / debug / release
G4 — internals / plumbing / refs / policy / automation
```

Mapping scolastico candidato:

```text
2° → G1
3° → G2
4° → G3
5° → G4 selettivo/professionale
```

G1 è materializzato editorialmente M01–M08 ma resta **freeze-candidate / draft** finché non viene chiuso il relativo gate decisionale/delivery.

Candidate ref consumato da Python seconda:

```text
65d8aff8c9a590560c500762d4dc7378a3239bf2
```

Contratto provider:

```text
doc/G1_CONSUMER_CONTRACT.md
```

nel repository `TheBitPoets/git`.

---

# G1 — contenuto canonico

```text
G1-M01  version control / Git vs GitHub / repository / snapshot
G1-M02  working tree / tracked-untracked / status
G1-M03  diff / patch / review
G1-M04  index / selective staging
G1-M05  commit / parent / HEAD
G1-M06  log / show / history
G1-M07  .gitignore / beginner recovery
G1-M08  integrated intentional-history checkpoint
```

Il modello centrale è:

```text
WORKING TREE → INDEX → HISTORY
```

con modello beginner di HEAD:

```text
HEAD → current branch → current commit
```

Recovery core G1 resta deliberatamente limitato e fail-safe; reset/reflog/rebase e recovery avanzato appartengono ai livelli successivi.

---

# Python seconda come consumer G1

Python non possiede il curriculum Git.

Dipendenza machine-readable locale:

```text
config/git-g1-consumer.json
```

Progressione congelata nel track Python:

```text
M14–M16
  G1.OBSERVE.STATUS
  G1.OBSERVE.DIFF
  evidence: guided

Checkpoint A
  status
  → diff
  → test
  → add <path>
  → diff --staged
  → commit
  → status
  → log/show

secondo semestre
  G1.WORKFLOW.CHECKPOINT
  G1.RECOVERY.BASIC
  evidence: independent-progressive
```

Per lesson, remediation, Activity e rubric specifiche Git, Python rimanda al corso Git canonico.

Git Lab canary canonico:

```text
g1-stage-selettivo-001
```

TheBitLab Git Lab platform candidate verde:

```text
TheBitPoets/2cornot2c#761/#762
24570f7a3af67634ec0cfbf54f486660359baaf2
```

La CI consumer di `python-docente` resta separatamente bloccata da `python-docente#8` prima dell'avvio del runner; quindi structural integration e delivery certification restano gate distinti.

---

# Materiale Git legacy

Il vecchio materiale/README docente nel repository Git è stato auditato come **legacy pedagogical source**, non come lesson canonica.

La policy corrente è:

```text
Git official docs / git help
→ autorità tecnica

Pro Git
→ coverage/concept map

materiale legacy docente/Manning
→ fonte pedagogica privata

lesson/slide/Activity TheBitPoets
→ materiale canonico originale
```

Non completare traduzioni legacy soltanto per ottenere copertura; le parti mancanti vengono coperte da materiale originale e fonti autorevoli.

---

# Corso Container — progetto separato

Il corso container/Docker resta un curriculum autonomo.

Repository sorgente esistente:

```text
kinderp/docker101
```

Backlog canonico:

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
  → perché containerizzare
  → leggere/scrivere un Dockerfile Python essenziale
  → build/run/config/health
  → collegamento al corso Container per approfondimento
```

Analogamente Python usa Git nel proprio workflow ma non diventa il corso Git.

---

# Regola di dipendenza cross-course

Un corso disciplinare può dichiarare una competenza trasversale come:

- `introduced-here` — micro-concetto contestuale necessario;
- `external-track` — outcome posseduto dal curriculum trasversale;
- `prerequisite` — competenza richiesta da un livello precedente;
- `enrichment` — approfondimento facoltativo.

Per dipendenze materializzate, preferire un contratto machine-readable con:

- repository/provider;
- track/livello;
- candidate/frozen ref;
- outcome consumati;
- evidence level;
- capability ambiente;
- boundary/non-goals.

Non duplicare intere UDA Git/Container in più corsi.

---

# TheBitLab

Git e Container devono usare lo stesso Classroom Environment cross-course.

Il corso Git deve poter lavorare su repository didattici senza richiedere installazioni manuali esterne, rete o account GitHub per G1 core.

Il corso Container deve distinguere chiaramente:

- container come oggetto di studio;
- container usato internamente da TheBitLab;
- grading sandbox;
- ambiente interattivo dello studente.

Questi boundary non vanno confusi nelle dispense.
