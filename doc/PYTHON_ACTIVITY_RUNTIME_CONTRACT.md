# Python Activity / runtime contract — DRAFT

Questo documento definisce i profili didattici/grading Python di `python-docente` sopra i contratti TheBitLab. Non introduce runner paralleli: P1–P4 devono condividere il core Python grader e il medesimo sandbox autorevole; `romeo-sim` resta un runtime plugin di dominio separato.

## Principio

```text
Activity 1.0
→ scaffold studente
→ profilo di evidence/grading adeguato all'outcome
→ sandbox Docker autorevole quando esegue codice non fidato
→ confronto trusted host-side
→ report redatto allo studente
```

Non adattare artificialmente l'obiettivo didattico al solo grader disponibile. Se una capability non esiste ancora, usare evidence manuale/formativa esplicita oppure bloccare l'Activity che la richiede.

## Baseline

- linguaggio: `python`;
- baseline didattica: Python 3.12;
- grading autorevole di codice non fidato: sandbox TheBitLab;
- rete grading: disabilitata salvo futuro contratto specifico;
- teacher expected values/fixture segrete restano trusted host-side quando possibile;
- AI: disabilitata nelle Activity fondazionali salvo policy futura esplicita;
- pytest non è prerequisito del secondo anno: il framework entra più avanti nel curriculum professionale.

---

# P0 — trace / manual evidence

Per attività in cui il focus è previsione, spiegazione, progettazione o scelta:

- grading automatico facoltativo;
- rubric/manual evidence;
- tabelle di trace, diagrammi, spiegazioni e scelta dei costrutti;
- niente fake autograding semantico basato su regex/euristiche fragili.

Usi:

- algoritmi/flow chart;
- trace;
- motivazione `for` vs `while`;
- scelta struttura dati;
- qualità della decomposizione/refactoring.

---

# P1 — single-file stdin/stdout

**Stato piattaforma:** runner generico già esistente; vertical slice del corso ancora da certificare end-to-end in `python-docente#7`.

È il profilo iniziale per programmi completi a singolo file.

Concept Activity:

```json
{
  "language": "python",
  "source_name": "main.py",
  "grading_policy": {
    "compila": true,
    "test": true,
    "sandbox": true,
    "ai_feedback": false
  },
  "test_cases": [
    {
      "stdin": "...",
      "expected_stdout": "..."
    }
  ]
}
```

## Regole P1

1. Un solo file sorgente nel profilo iniziale.
2. I test confrontano output deterministico.
3. Evitare prompt/accessori quando non sono parte del requisito.
4. Usare più casi significativi; uno starter volutamente incompleto deve essere discriminato dai test.
5. Expected output/test completi restano teacher-side; scaffold e report studente devono essere redatti.
6. Nessuna dipendenza implicita da rete/filesystem esterno/package non dichiarati.
7. Timeout/CPU/memoria sono proprietà del runner/piattaforma.

## Primo vertical slice

Activity:

```text
py2-activity-b-input-somma-001
```

TheBitLab baseline separata per questo corso:

```text
cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0
```

Non modifica il pin congelato di TPSI5.

Gate: `python-docente#7`.

Nota CI corrente: i run Actions osservati hanno fallito **prima di eseguire qualunque step** su Ubuntu e Windows; quindi il vertical slice non è certificato e quel failure non è attribuito al corpo dello smoke. Non usare il vertical slice come autorizzazione alla produzione massiva finché #7 non è chiusa con evidenza reale.

---

# P2 — function behavior

**Issue piattaforma:** `TheBitPoets/2cornot2c#756`.

Necessario da PY2-05 quando l'outcome è una funzione/`return`, non un'interfaccia stdin/stdout.

Target:

```text
student module
→ sandbox
→ locate top-level callable
→ call(args, kwargs)
→ return actual value / bounded exception descriptor
→ trusted host compares with expected
```

## Vincoli

- mai importare/eseguire codice studente nel processo trusted;
- expected return/exception host-side;
- worker riceve solo gli input della chiamata;
- value codec deterministico e type-aware;
- stdout/stderr solo diagnostica;
- import-time side effects bounded da timeout;
- missing/non-callable target = failure esplicito;
- riuso identico del sandbox P1.

Uso didattico:

```text
casi su carta
→ assert
→ direct function behavior P2
→ pytest strutturato nei livelli professionali
```

---

# P3 — object behavior

**Issue piattaforma:** `TheBitPoets/2cornot2c#758`.

Necessario per autograding generico di classi/istanze senza ricorrere a parsing del sorgente.

Target:

```text
construct declared class
→ call declared methods
→ observe declared public state/property
→ actual observations
→ trusted host comparison
```

## Vincoli

- istanziazione sempre nel sandbox;
- expected values host-side;
- osservazioni solo su nomi dichiarati e portabili;
- private/dunder observation denied by default;
- niente `eval` di espressioni teacher/student;
- supporto a più istanze per verificarne indipendenza;
- shared value codec con P2;
- niente inspection della gerarchia come sostituto del comportamento.

Romeo non usa P3 per la simulazione di dominio: le Activity robotiche restano su `romeo-sim` quando servono traiettoria/event log/stato finale.

---

# P4 — filesystem behavior

**Issue piattaforma:** `TheBitPoets/2cornot2c#757`.

Necessario per Activity in cui l'outcome è vero file I/O.

Target:

```text
explicit read-only fixtures
+ student source
+ isolated bounded writable workdir
→ sandbox execution
→ bounded produced artifacts/manifest
→ trusted host compares expected artifacts
```

## Vincoli

- nessun mount del repository docente completo;
- fixture dichiarate soltanto;
- path relativi;
- no symlink/path traversal/special files;
- clean state per test;
- limiti numero/dimensione input/output;
- expected artifact contents host-side dove praticabile;
- report senza path host sensibili;
- distinguere normale `FileNotFoundError` dello studente da policy/infrastructure failure.

Fino a P4 certificato, PY2-09 resta completabile con lab nel Classroom Environment + evidence manuale/formativa; non simulare il filesystem con stdin se cambia l'outcome.

---

# Runtime di dominio — Romeo

Romeo resta fuori da P1–P4:

```text
Activity Romeo
→ runtime.romeo-sim.v1
→ TheBitLab runtime broker
→ external Romeo plugin
→ trajectory / event log / final state
```

Hardware fisico è una capability opzionale separata e non può essere requisito del core.

---

# Progressione didattica del testing

```text
problema + casi su carta
→ expected input/output
→ P1 stdin/stdout
→ assert
→ P2 function behavior
→ P3 object behavior / P4 filesystem behavior quando l'outcome lo richiede
→ pytest, fixtures, parametrize, integration/E2E nel percorso professionale
```

La piattaforma può usare infrastruttura interna più sofisticata senza obbligare lo studente a conoscerla prima del momento curricolare corretto.

---

# Output contract beginner P1

Quando il focus è il calcolo:

```python
numero = int(input())
print(numero * 2)
```

preferibile a:

```python
numero = int(input("Inserisci un numero: "))
print("Il doppio è", numero * 2)
```

se il testo accessorio non fa parte della specifica.

Quando l'interfaccia testuale è essa stessa requisito, il contratto può includere prompt/output completo.

---

# Error/reporting principles

Student-facing report deve distinguere, dove applicabile:

- output/return/state/artifact differente dall'atteso;
- runtime error;
- bounded traceback/exception;
- timeout;
- missing declared callable/class/artifact;
- sandbox/policy violation;
- runner/infrastructure unavailable.

Il report deve aiutare a diagnosticare senza trasformarsi in generatore automatico della soluzione.

---

# Activity taxonomy e profili

| Activity | Profilo tipico |
|---|---|
| A Observe/Trace | P0 |
| B Controlled Change | P1/P2/P3/P4 secondo outcome |
| C Implement | P1/P2/P3/P4 |
| D Debug/Diagnose | P0 + profilo eseguibile appropriato |
| E Mini-project | mix; evitare capability non certificate |
| F Integrated Product | mix + rubric/manual evidence; Romeo può usare runtime plugin |

Il livello A–F descrive la progressione didattica, non il tipo di runner.

---

# Gate prima di produzione massiva

Non produrre decine di Activity Python finché:

1. P1 vertical slice `python-docente#7` non ha evidence reale;
2. le Activity che richiedono P2/P3/P4 dichiarano la capability oppure restano manual/formative;
3. scaffold student/teacher separation è verificata;
4. Classroom Environment è certificato secondo `python-docente#2` / `2cornot2c#753`;
5. Course Workspace round-trip resta compatibile con `2cornot2c#755`;
6. Romeo viene usato solo attraverso il runtime plugin certificato.
