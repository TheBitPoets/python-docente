# Python curriculum — matrice delle competenze (DRAFT)

Legenda:

- **CORE** — competenza obbligatoria nel track;
- **INTRO** — introdotta ma non portata a livello professionale;
- **EXT** — enrichment se tempo/gruppo lo permettono;
- **NEXT** — rinviata esplicitamente a un livello successivo.

| Area | Secondo anno | Core avanzato | Professional | Evidenza finale attesa |
|---|---|---|---|---|
| Problem solving / decomposizione | CORE | CORE | CORE | tradurre requisito in soluzione verificabile |
| Pseudocodice / flow chart | CORE | EXT | NEXT | rappresentare controllo del flusso prima del codice |
| Tipi fondamentali / espressioni | CORE | CORE | CORE | usare correttamente dati e operatori |
| `if/elif/else` e logica | CORE | CORE | CORE | scegliere e semplificare condizioni |
| `for` / `while` | CORE | CORE | CORE | scegliere il ciclo adeguato |
| Annidamento / pattern iterativi | CORE | CORE | CORE | risolvere problemi composti senza accidental complexity |
| Funzioni / decomposizione | CORE | CORE | CORE | separare responsabilità e logica I/O |
| Scope | INTRO | CORE | CORE | comprendere lifetime/namespace necessari al design |
| Stringhe | CORE | CORE | CORE | parsing e trasformazioni corrette |
| Liste / tuple | CORE | CORE | CORE | scegliere mutabilità/ordine consapevolmente |
| Set / dict | CORE | CORE | CORE | usare membership/lookup/modellazione adeguati |
| Strutture annidate | CORE | CORE | CORE | modellare dati composti |
| Comprehensions | INTRO/EXT | CORE | CORE | usarle quando migliorano leggibilità |
| Complessità | INTRO intuitiva | CORE | CORE | motivare trade-off tempo/memoria |
| File di testo | CORE | CORE | CORE | leggere/scrivere/elaborare in sicurezza |
| CSV/JSON | EXT | CORE | CORE | gestire formati strutturati |
| Eccezioni | INTRO | CORE | CORE | progettare error boundaries |
| Classi/oggetti | CORE | CORE | CORE | modellare stato + comportamento |
| Composizione OOP | CORE | CORE | CORE | collaborazioni tra oggetti semplici |
| Ereditarietà | EXT | CORE | CORE | usarla solo quando appropriata |
| Data model / special methods | NEXT | CORE | CORE | creare tipi pythonic |
| Iterators/generators | NEXT | CORE | CORE | elaborazione lazy e protocolli |
| First-class functions/decorators | NEXT | CORE | CORE | callback/estensione controllata |
| Moduli/package | INTRO | CORE | CORE | organizzare codice multi-file |
| Standard library | INTRO | CORE | CORE | conoscere e scoprire strumenti standard |
| Git | EXT/INTRO | CORE | CORE | workflow collaborativo riproducibile |
| Virtual environment | NEXT | INTRO/CORE | CORE | isolare interprete e dipendenze |
| `pip` / package indexes | NEXT | INTRO | CORE | installare e versionare dipendenze |
| `pyproject.toml` | NEXT | INTRO | CORE | configurare progetto moderno |
| Lock/reproducibility | NEXT | INTRO | CORE | ricreare ambiente in modo deterministico |
| uv/modern project manager | NEXT | EXT | CORE tool candidate | workflow pratico riproducibile |
| Formatter/linter | EXT/teacher-led | INTRO | CORE | quality gate automatizzato |
| Static typing | NEXT | INTRO | CORE | verificare contratti prima del runtime |
| Unit testing | INTRO | CORE | CORE | regression suite affidabile |
| pytest fixtures/parametrize | NEXT | INTRO | CORE | test mantenibili e data-driven |
| Integration/E2E testing | NEXT | INTRO | CORE | verificare boundary reali |
| Property-based testing | NEXT | EXT | CORE/EXT | verificare invarianti e edge cases |
| Configuration | NEXT | INTRO | CORE | separare codice e configurazione |
| Secrets | NEXT | INTRO | CORE | nessun segreto nel codice/repo/log |
| SQL | NEXT | INTRO/CORE | CORE | query, join, transazioni |
| DB-API / sqlite3 | NEXT | CORE | CORE | accesso DB senza ORM |
| SQLAlchemy Core | NEXT | EXT/CORE | CORE | data access strutturato |
| SQLAlchemy ORM | NEXT | EXT/CORE | CORE | mapping, session, relationships |
| Alembic migrations | NEXT | NEXT/INTRO | CORE | schema versionato e deployabile |
| HTTP client / JSON APIs | NEXT | INTRO | CORE | integrazione servizi robusta |
| API server | NEXT | EXT | CORE in backend track | progettare endpoint e validation |
| Async / concurrency | NEXT | INTRO | CORE concettuale + track | scegliere modello corretto |
| Logging | NEXT | INTRO | CORE | diagnostica utile e sicura |
| Metrics / tracing / health | NEXT | NEXT/INTRO | CORE operations | osservabilità operativa |
| Security fundamentals | INTRO | CORE | CORE | input/secrets/query/process safe boundaries |
| Profiling/performance | INTRO intuitiva | CORE | CORE | misurare prima di ottimizzare |
| CLI / OS integration | EXT | CORE | CORE | tool robusti con exit code/I/O |
| Packaging build wheel/sdist | NEXT | INTRO | CORE | artefatto installabile |
| CI/CD | NEXT | INTRO | CORE | quality/build/release automation |
| Docker | NEXT | EXT | CORE deployment literacy | immagine riproducibile e non-root |
| Documentation | CORE semplice | CORE | CORE | onboarding/API/runbook aggiornati |
| Code review | NEXT | INTRO | CORE | collaborare e migliorare qualità |
| Architecture/refactoring | INTRO | CORE | CORE | software mantenibile e boundaries chiari |

## Criterio per dichiarare “Python developer professionale”

Non basta completare tutti i moduli. Il capstone deve dimostrare almeno:

1. ambiente e dipendenze riproducibili;
2. struttura di progetto sensata;
3. API/CLI o altro boundary reale;
4. persistenza quando il dominio la richiede;
5. test unitari + integration;
6. typing e quality gates;
7. error handling/config/secrets corretti;
8. logging/health sufficienti a diagnosticare il programma;
9. CI verde da checkout pulito;
10. package/container/artifact eseguibile da un altro sviluppatore;
11. documentazione di installazione, uso, architettura e troubleshooting;
12. capacità di spiegare trade-off e limiti della soluzione.
