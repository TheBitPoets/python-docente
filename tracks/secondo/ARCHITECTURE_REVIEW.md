# Python secondo — Architecture Review del track 33 settimane

> Stato: **review architetturale DRAFT**. Serve a verificare coerenza, carico e dipendenze prima del Course Design freeze.

## 1. Verdetto sintetico

Il track è **coerente e realizzabile come curriculum core**, a condizione di rispettare quattro regole:

1. le 99 ore nominali non vengono tutte consumate da nuovo contenuto;
2. i tre checkpoint restano realmente flessibili;
3. enrichment e tooling non diventano prerequisiti nascosti;
4. le Activity vengono prodotte solo sulle capability TheBitLab certificate oppure dichiarano evidence/fallback espliciti.

La struttura mantiene OOP nel core e non dipende dalla settimana 33 per essere completa.

---

# 2. Bilancio temporale

| Blocco | Settimane | Ore nominali |
|---|---:|---:|
| PY2-01 algoritmi/flow chart | 3 | 9 |
| PY2-02 primi programmi | 2 | 6 |
| PY2-03 selezione/logica | 3 | 9 |
| PY2-04 iterazione/pattern | 4 | 12 |
| PY2-05 funzioni/testing | 4 | 12 |
| Checkpoint A | 1 | 3 |
| PY2-06 stringhe | 3 | 9 |
| PY2-07 liste/tuple | 3 | 9 |
| Checkpoint B | 1 | 3 |
| PY2-08 set/dict | 3 | 9 |
| PY2-09 file/errori | 1 | 3 |
| PY2-10 OOP/capstone | 4 | 12 |
| Checkpoint C | 1 | 3 |
| **Totale** | **33** | **99** |

Core UDA:

```text
30 settimane = 90 ore nominali
```

Buffer/checkpoint:

```text
3 settimane = 9 ore esplicitamente flessibili
```

Questa separazione è obbligatoria: i checkpoint non possono essere riempiti anticipatamente di nuovi prerequisiti.

---

# 3. Realismo del calendario scolastico

Le 90 ore core restano comunque **nominali**. Festività, assemblee, verifiche, uscite e imprevisti possono ridurle.

Per questo ogni UDA deve distinguere:

- `CORE` — outcome senza cui il track non è completato;
- `ENRICHMENT` — tagliabile senza rompere prerequisiti;
- `FALLBACK` — percorso equivalente quando una capability non è disponibile.

Regola operativa:

> Se il calendario perde ore, si taglia prima enrichment e ampiezza degli esercizi, non i concetti strutturali già dichiarati core.

---

# 4. Dipendenze didattiche

La catena principale è aciclica e sensata:

```text
algoritmo/trace
→ programmi lineari
→ selezione
→ iterazione
→ funzioni/testing
→ stringhe
→ liste/tuple
→ set/dict + modellazione
→ file/error boundary essenziale
→ OOP/composizione/capstone
```

Competenze trasversali spirali:

```text
test case    dal primo algoritmo
trace        dal flow chart
error/debug  dal primo script
naming       dal primo programma
funzioni     preview precoce → formalizzazione PY2-05
efficienza   intuizione contestuale → mai capitolo isolato
spiegazione  in ogni Activity significativa
```

Non emerge una dipendenza circolare curricolare.

---

# 5. Prima metà dell'anno

## PY2-01 → PY2-05

È la parte più importante per costruire **programmazione** prima delle collezioni.

Soglia Checkpoint A:

- problema → algoritmo;
- flow chart/trace;
- I/O e tipi;
- `if/elif/else`;
- `for`/`while`;
- annidamento;
- contatore/accumulatore/min-max/search;
- funzioni;
- return;
- decomposizione top-down;
- semplici `assert` e regression thinking.

Verdetto: **carico alto ma coerente**, perché le funzioni vengono preannunciate presto e non compaiono improvvisamente alla settimana 13.

### Rischio principale

PY2-04 + PY2-05 occupano 8 settimane consecutive di concetti strutturali.

Mitigazione:

- molte Activity brevi e progressive;
- Romeo/general micro-problems per varietà;
- niente feature extra (`match`, comprehension, recursion, pytest);
- checkpoint A realmente usato per recupero/verifica/progetto, non nuova sintassi.

---

# 6. Seconda metà dell'anno

## PY2-06 → PY2-08

La progressione delle strutture dati è corretta:

```text
str = sequenza immutabile già nota come testo
→ list = sequenza mutabile
→ tuple = raggruppamento/sequenza stabile
→ set = unicità/membership
→ dict = key → value / lookup
→ strutture composte
→ scelta della struttura
```

Verdetto: **coerente e centrato sull'uso**, non sull'inventario dei metodi.

### Rischio principale: PY2-07 densità

In 9 ore contiene:

- metodi lista;
- mutabilità;
- alias/copia;
- filtro/trasformazione;
- sort/sorted;
- tuple/unpacking;
- matrici.

Mitigazione obbligatoria:

1. metodi lista limitati al set realmente usato nei problemi;
2. alias/copia = core, non sacrificabile;
3. comprehension = enrichment;
4. deep copy = solo concetto/enrichment;
5. matrici limitate a 2D semplici;
6. checkpoint B assorbe consolidamento e prove, non nuovo data model.

Se serve tagliare, si tagliano prima comprehension/zip/key functions/deep-copy detail, **non aliasing**.

---

# 7. File/errori: scelta deliberatamente minima

PY2-09 ha 3 ore.

Core:

```text
Path relativo
with/open
UTF-8
read/write/righe
r/w/a essenziale
FileNotFoundError/ValueError
errore previsto vs bug
```

Non core:

- CSV/JSON;
- binario;
- custom exceptions;
- finally/else avanzati;
- serialization design.

Verdetto: **scelta corretta**. Persistenza viene introdotta senza sottrarre OOP dal finale.

---

# 8. OOP: 12 ore core + checkpoint C

PY2-10 riceve 4 settimane = 12 ore, con la settimana 33 disponibile per finalizzazione ma non necessaria a introdurre concetti obbligatori.

Core:

- class/instance;
- attributes;
- `self`;
- `__init__`;
- methods;
- state/behavior;
- invariants;
- multiple independent instances;
- composition;
- responsibilities;
- capstone.

Enrichment:

- `__str__`/`__repr__`;
- property;
- inheritance semplice;
- dataclass dopo classe esplicita.

Verdetto: **realistico**, se inheritance/dataclass non diventano una checklist obbligatoria.

Il capstone deve essere piccolo e totalmente spiegabile, non un progetto enorme che assorbe settimane mancanti.

---

# 9. Valutazioni

Vincolo approvato:

- almeno una prova teoria/scritta;
- almeno una prova pratica/pratico-scritta;
- per quadrimestre.

La struttura proposta sfrutta UDA/checkpoint invece di aggiungere settimane artificiali.

## Primo quadrimestre

- V1: algoritmi/flow chart/semantica/selezione;
- V2: pratica integrata selezione + cicli + funzioni/debug, vicino a Checkpoint A.

## Secondo quadrimestre

- V3: stringhe/liste/tuple/strutture e modellazione;
- V4: pratica integrata/OOP-capstone slice.

Verdetto: **compatibile col calendario**, purché le prove vengano progettate come evidence del curriculum e non aggiungano nuovi argomenti.

---

# 10. Git G1: non deve dipendere dalla settimana 33

Decisione architetturale della review:

> Git G1 è una competenza trasversale introdotta progressivamente nel workflow, non una UDA Python e non un enrichment affidato soltanto alla settimana 33.

Progressione raccomandata:

```text
settimane 13–16  repo/status/diff
Checkpoint A     primo commit guidato
secondo semestre add/commit/log come routine crescente
Checkpoint C     eventuale consolidamento, non prima esposizione
```

Dettaglio in `tracks/secondo/GIT_G1_INTEGRATION.md`.

Il corso Git autonomo resta la fonte canonica futura; Python introduce soltanto ciò che serve al workflow.

---

# 11. Romeo: ruolo corretto

Romeo è una **spine applicativa opzionale/ricorrente**, non una dipendenza curricolare universale.

Uso naturale:

- sequenze/prime funzioni;
- `if`;
- `for`/`while`;
- decomposizione;
- simulator debugging;
- OOP/capstone.

Uso non forzato:

- stringhe;
- set/dict;
- file;

se non emerge una missione realmente utile.

Hardware fisico mai requisito core.

Mapping dettagliato deve essere versionato separatamente.

---

# 12. TheBitLab capability matrix del track

| Area | Profilo/capability | Stato |
|---|---|---|
| flow chart | `flowchart.lab.v1` | design blocker `2cornot2c#753/#754`; fallback manuale |
| programmi Python | P1 stdin/stdout | runner esiste; vertical slice course non certificato `python-docente#7` |
| funzioni | P2 | open `2cornot2c#756` |
| oggetti | P3 | open `2cornot2c#758` |
| filesystem | P4 | open `2cornot2c#757` |
| Romeo | `runtime.romeo-sim.v1` | runtime esistente; cross-profile certification ancora da chiudere |
| VS Code | `editor.vscode.v1` candidate | managed integration da certificare |
| workspace/dashboard | Course Workspace | architecture definita; product flow `2cornot2c#755` |

Regola:

> Un blocker di autograding non blocca la **spiegazione** del concetto; blocca soltanto la promessa che quella evidence venga valutata automaticamente attraverso quel profilo.

---

# 13. Rischi ordinati

## R1 — Classroom Environment non certificato

Impatto: alto.

Mitigazione: `python-docente#2` + `2cornot2c#753/#754`.

## R2 — P1 vertical slice non verde

Impatto: alto sulla produzione Activity.

Stato: `python-docente#7`; Actions osservate falliscono pre-execution, non è ancora evidence del grader.

Mitigazione: non mass-produrre Activity fino alla certificazione.

## R3 — Flowchart Lab non implementato

Impatto: medio sul delivery, basso sul curriculum.

Fallback: carta/template/manual evidence con stesso outcome.

## R4 — P2/P3/P4 non implementati

Impatto: medio sul grading automatico, basso sull'insegnabilità.

Fallback: assert/lab/manual rubric; non distorcere l'Activity in P1 se cambia l'outcome.

## R5 — PY2-07 troppo denso

Impatto: medio.

Mitigazione: tagliare enrichment prima del core alias/copy/data modelling.

## R6 — Romeo non certificato cross-profile

Impatto: basso sul core grazie al capstone generico equivalente.

## R7 — Troppe fonti/tool

Impatto: medio sulla produzione.

Mitigazione: una lesson è originale; fonti sono coverage/reference, non syllabus concorrenti.

---

# 14. Gap curricolari cercati e risultato

Non risultano buchi core sui requisiti dichiarati dall'utente:

- problem solving/algoritmi: coperto;
- flow chart: coperto;
- input/output/tipi: coperto;
- controllo del flusso e annidamento: coperto;
- scelta `for`/`while`: coperto;
- funzioni/decomposizione: coperto;
- test/debug: coperti in spirale;
- stringhe: coperte;
- liste/tuple/set/dict: coperte;
- strutture annidate/matrici: coperte;
- scelta struttura dati: core esplicito;
- efficienza intuitiva: integrata;
- file/errori: core minimo;
- OOP: core obbligatorio;
- composizione: core;
- progetto pratico: capstone + Romeo/general;
- Git minimo: integrazione trasversale progettata.

Il profilo professionale completo resta nella roadmap multi-year e non va compresso nel secondo anno.

---

# 15. Raccomandazione di freeze

La **struttura curricolare del secondo anno può essere considerata candidata al freeze** dopo:

1. review finale delle 10 SPEC;
2. mapping Romeo selettivo completato;
3. Git G1 integration fissata;
4. verifica che Course Design/Content Pack indichino tutte le SPEC;
5. nessuna nuova UDA necessaria emersa dalla gap review.

Il **Content Pack 1.0 non può invece essere dichiarato pronto/pubblicabile** finché i blocker ambiente/delivery necessari non hanno i gate previsti.

Questa distinzione permette di congelare *cosa insegniamo* senza fingere che *come lo consegniamo/autogradiamo* sia già tutto certificato.
