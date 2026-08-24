# Python curriculum — decision register

> Second-year curriculum architecture **FROZEN 2026-08-24**.  
> Canonical freeze: `doc/CURRICULUM_FREEZE_2026_2027.md`.

Questo file non deve riaprire decisioni congelate. Mantiene invece la distinzione fra decisioni **CLOSED/FROZEN**, scelte di **delivery ancora aperte** e decisioni dei track professionali/futuri.

## D1 — Versione Python del track secondo — CLOSED

- baseline didattica certificabile iniziale: **Python 3.12**;
- core scritto in modo conservativo/forward-compatible quando ragionevole;
- nessun outcome dipende da feature 3.13/3.14 non necessarie;
- patch/minor future del Classroom Environment sono delivery/tooling se non cambiano gli outcome.

## D2 — Confine OOP del secondo anno — FROZEN

Core obbligatorio:

- classi, istanze, attributi;
- `self`, `__init__`, metodi;
- stato/comportamento;
- invarianti semplici;
- più istanze indipendenti;
- composizione/responsabilità;
- capstone OOP.

Enrichment: `__str__/__repr__`, properties, inheritance semplice, dataclass dopo classe esplicita.

## D3 — Progetto applicativo — FROZEN

Modello ibrido:

```text
problemi e micro-progetti generali
+ Romeo simulato come spine selettiva
+ capstone OOP Romeo o fallback generico equivalente
```

Romeo non è il syllabus e hardware fisico non è requisito core.

## D4 — Flow chart — PEDAGOGY CLOSED / DELIVERY OPEN

Pedagogia congelata:

- carta/lavagna e simboli standard sempre validi;
- target digitale: **TheBitLab Flowchart Lab cross-platform**;
- Flowgorithm può essere companion Windows opzionale, mai requisito canonico.

Implementazione/certificazione: `2cornot2c#753/#754`.

## D5 — Git nel secondo anno — FROZEN

Git è curriculum separato; Python seconda consuma G1 progressivamente:

- `status`, `diff` da PY2-05;
- `add`, `commit` al Checkpoint A;
- history/log essenziale e checkpoint nel secondo semestre.

Le dispense Git esistenti verranno auditate quando produrremo G1 definitivo o il corso Git autonomo.

## D6 — Toolchain professionale — OPEN PER STAGE C, NON BLOCCA SECONDA

Concetti obbligatori nella roadmap professionale:

- venv/isolamento;
- dependency/project management;
- `pyproject.toml`;
- formatter/linter;
- static typing;
- pytest;
- build/package.

Candidati pratici attuali: uv, Ruff, Pyright/mypy, pytest, Hypothesis, SQLAlchemy 2.x, Alembic.

Regola già fissata: **concept/standard first, tool second**. La selezione/versione concreta dei tool resta versionabile e non modifica il freeze di seconda.

## D7 — Database pluriennale — ROADMAP CLOSED / DELIVERY FUTURA

Progressione approvata:

```text
SQL fundamentals
→ sqlite3 / DB-API
→ repository/data access
→ SQLAlchemy Core
→ SQLAlchemy ORM
→ Alembic
→ async DB nel track avanzato
```

Resta da distribuire tra anni/corsi e coordinare con SQL/TPSI.

## D8 — Testing precoce — FROZEN

```text
paper cases dal problem solving
→ stdin/stdout
→ assert + regression thinking
→ function/object/filesystem behavior quando supportato
→ pytest nel livello professionale
```

## D9 — `match/case` — FROZEN

Non sostituisce `if/elif/else`; solo enrichment successivo quando porta valore reale.

## D10 — Comprehensions — FROZEN

Loop espliciti prima; comprehension semplice solo dopo padronanza del loop equivalente. Nested/advanced in Stage B.

## D11 — Set nel secondo anno — FROZEN

Sì, come parte della competenza di scelta della struttura dati; meno peso di list/dict.

## D12 — Eccezioni nel secondo anno — FROZEN

Solo boundary essenziale per errori prevedibili, soprattutto input/file, senza trasformare la seconda in un corso sulle gerarchie di eccezioni. Advanced exception model in Stage B.

## D13 — TheBitLab — ARCHITECTURE CLOSED / CERTIFICATION OPEN

Già fissato:

- Activity 1.0 + Content Pack v1 + Course Design v1;
- Classroom Environment unico ambiente supportato;
- Course Workspace mutabile / Course Bundle immutabile;
- P0 manuale/trace;
- P1 stdin/stdout;
- P2 function behavior;
- P3 object behavior;
- P4 filesystem behavior;
- `romeo-sim` come runtime plugin esterno.

Aperti:

- `python-docente#2`, `#6`, `#7`, `#8`;
- `2cornot2c#753/#754/#755/#756/#757/#758`;
- certificazioni reali dei profili.

## D14 — Tassonomia — FROZEN

Gerarchia:

```text
Stage → UDA → moduli/lesson → Activity
```

Track seconda: **PY2-01…PY2-10 + tre checkpoint**, con M00–M30 come mappa modulare.

## D15 — Slide/guide standard — CLOSED A LIVELLO AUTHORING

Standard TPSI5 adattato a seconda:

- lesson canonica per modulo;
- deck per modulo, densità ridotta e più trace;
- `student/README.md` e `teacher/README.md`;
- runbook docente;
- Activity A–F;
- solution/reference e rubric/manual evidence;
- QA/CI;
- curriculum freeze vs delivery changes.

La build finale HTML/PDF/PPTX e i quality gate restano delivery work.

## D16 — Distribuzione Stage B/C negli anni successivi — OPEN

Da decidere in seguito come distribuire il curriculum completo fra:

- terzo;
- quarto;
- quinto;
- corsi opzionali;
- percorsi avanzati.

Non riapre il freeze del secondo anno.

---

# Decisioni aperte che possono davvero richiedere scelta futura

1. toolchain professionale concreta/versioni per Stage C;
2. distribuzione Stage B/C tra terzo/quarto/quinto;
3. forma finale del corso Git autonomo e progressione per anno;
4. forma finale del corso Container/Docker;
5. variante concreta del capstone OOP entro gli outcome congelati;
6. selezione individuale degli esercizi `friedpython` dopo audit;
7. pesi rubric finali entro il modello di valutazione già approvato.

Nessuno di questi punti autorizza a modificare implicitamente il curriculum frozen di seconda.
