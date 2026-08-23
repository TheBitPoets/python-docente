# Python Activity / runtime contract — DRAFT

Questo documento definisce il profilo didattico iniziale delle Activity Python di `python-docente` sopra i contratti esistenti TheBitLab. Non introduce un nuovo runner.

## Principio

Per il core beginner usare il runner Python già presente in TheBitLab:

```text
Activity 1.0
→ scaffold student
→ main.py
→ Python runner core
→ sandbox Docker autorevole
→ test deterministici
→ report
```

`romeo-sim` e altri runtime plugin restano per domini speciali; non sono necessari per un normale esercizio Python.

## Baseline

- linguaggio: `python`;
- baseline didattica: Python 3.12;
- source iniziale: `main.py`;
- grading autorevole: Docker sandbox TheBitLab;
- grading locale: solo feedback formativo/test pubblico, non confine di sicurezza;
- rete grading: disabilitata;
- AI: disabilitata nelle Activity fondazionali salvo policy esplicita futura.

## Profilo P0 — trace/manual evidence

Per attività in cui il codice non deve essere eseguito o il focus è la previsione:

- grading automatico facoltativo;
- evidence manuale/rubric;
- possibile tabella di trace/output previsto;
- nessun tentativo di simulare una valutazione semantica con test fragili.

Usi: M04/M05 trace, spiegazione errori, scelta di una soluzione.

## Profilo P1 — single-file stdin/stdout

È il profilo core da PY2-02 fino a quando i problemi restano programmi lineari/strutturati a singolo file.

Activity:

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

### Regole P1

1. Un solo file sorgente.
2. I test confrontano output deterministico.
3. Evitare prompt interattivi non richiesti dal contratto.
4. Usare almeno un caso normale e, quando utile, edge/negative case.
5. Gli expected output/test case completi restano teacher-side; lo scaffold studente riceve metadata redatti.
6. Il codice studente non deve dipendere da rete, filesystem esterno o pacchetti non dichiarati.
7. Timeout e limiti sono proprietà del runner/piattaforma, non della lesson.

## Perché non usiamo subito pytest

Lo studente non deve imparare infrastruttura di test prima di aver capito input/output, funzioni e casi di test.

Progressione didattica:

```text
casi su carta
→ stdin/stdout
→ assert
→ test di funzioni
→ test di oggetti
→ pytest professionale
```

TheBitLab può usare infrastruttura nascosta internamente, ma la lesson non anticipa concetti non necessari.

## Profilo P2 — function behavior (da progettare)

Quando arriviamo a PY2-05/M13–M16 servirà poter verificare direttamente funzioni senza obbligare ogni soluzione a passare dall'I/O testuale.

Requisiti futuri:

- import sicuro del modulo studente;
- chiamate a funzioni dichiarate;
- expected return / expected exception;
- isolamento Docker identico;
- test pubblici/privati;
- niente import-time side effect richiesto;
- report comprensibile allo studente.

P2 **non è requisito di PY2-02** e non va implementato prematuramente.

## Profilo P3 — object behavior (futuro)

Per OOP:

- istanziazione classi;
- metodi/stato osservabile;
- invarianti comportamentali;
- test di più istanze;
- eventuale composizione.

Anche P3 resta futuro e deve riusare lo stesso sandbox boundary.

## Output contract beginner

Per grading deterministico preferire programmi che non stampano testo accessorio.

Esempio:

```python
numero = int(input())
print(numero * 2)
```

non:

```python
numero = int(input("Inserisci un numero: "))
print("Il doppio è", numero * 2)
```

quando il focus è il calcolo.

La seconda forma potrà essere usata in Activity dove l'interfaccia testuale è esplicitamente parte del requisito e l'expected output la include.

## Error handling

Nelle prime UDA il runner deve mostrare in modo utile:

- non-zero exit;
- stderr/traceback bounded;
- timeout;
- output differente dall'atteso.

La lesson insegna gradualmente a leggere gli errori; il runner non deve trasformare automaticamente il traceback in una soluzione.

## Activity taxonomy

- A: trace/observe — spesso manuale o semi-deterministico;
- B: modifica controllata — ottimo primo uso P1;
- C: implementazione — P1;
- D: debug — P1 o rubric + P1;
- E/F: possono richiedere più file/runtime e vanno introdotte solo con contratto piattaforma adeguato.

## Primo vertical slice

Activity:

```text
py2-activity-b-input-somma-001
```

Scopo tecnico:

- verificare Activity 1.0;
- scaffold `main.py`;
- separazione asset student/teacher;
- 3 test stdin/stdout;
- grading sandbox;
- report deterministico;
- nessun AI feedback;
- compatibilità Course Workspace.

Scopo didattico:

- `input()`;
- `int()`;
- variabili;
- operatore `+`;
- `print()`;
- modifica controllata.

## Gate prima di produzione massiva

Non produrre decine di Activity Python finché il vertical slice non ha dimostrato:

1. validazione Activity;
2. scaffold senza leakage;
3. esecuzione corretta su Python 3.12;
4. grading Docker;
5. report leggibile;
6. apertura/assegnazione dal Course Workspace TheBitLab;
7. workflow equivalente nel profilo classroom supportato.
