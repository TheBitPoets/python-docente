# Python secondo anno — mappa modulo → fonti → Activity → Romeo (DRAFT)

Questa matrice guida la produzione futura delle lesson. Non sostituisce `MODULE_MAP.md`: aggiunge provenienza, controllo di copertura e strategia pratica.

## Codici fonti

- **TP** — Pensare in Python / Think Python: fonte pedagogica primaria beginner.
- **LP** — Imparare Python / Learning Python: coverage sistematica del linguaggio.
- **FP** — Fluent Python: controllo dei modelli mentali/idiomi; raramente fonte diretta per studenti di seconda.
- **PN** — Python in a Nutshell: riferimento tecnico/coverage.
- **DOC** — documentazione ufficiale Python: autoritativa.
- **PS** — Pluralsight: gap-check, demo/lab, alternative explanations.
- **FR** — `friedpython`: source pack legacy da auditare.
- **RO** — Romeo: missioni simulate/runtime TheBitLab.

## Regola generale Activity

- **A** Observe/Trace — prevedi, esegui, spiega.
- **B** Controlled Change — modifica codice/diagramma esistente.
- **C** Implement — costruisci da specifica.
- **D** Debug/Diagnose — trova/correggi errore.
- **E** Mini-project — integra più competenze.
- **F** Capstone — prodotto integrato.

Non ogni modulo deve avere tutti i tipi. Nel primo nucleo prevalgono A/B/C/D; E/F crescono dopo le funzioni.

---

| Modulo | Focus | Fonti primarie | Controllo/gap-check | Activity dominante | Romeo | Evidence chiave |
|---|---|---|---|---|---|---|
| M00 | metodo di problem solving | TP | PS Algorithmics | A | opzionale demo | dati/input/output, spiegazione |
| M01 | problema → algoritmo/pseudocodice | TP | PS Algorithmics | A/B/C | no | algoritmo + casi limite |
| M02 | flow chart sequenza/selezione | TP | Flowchart Lab spec | A/B/C | no | diagramma + trace |
| M03 | flow chart cicli/annidamento | TP | PS Algorithmics | A/B/C/D | possibile missione astratta | diagramma annidato + trace |
| M04 | REPL, script, valori, I/O | TP | LP, DOC tutorial, PS Essentials | A/B/C/D | prima chiamata `romeo.easy` opzionale | REPL transcript/checkpoint + script |
| M05 | espressioni/operatori/prime funzioni | TP | LP, DOC | A/B/C | sì: chiamata funzione/parametro | risultato + spiegazione parametro/return |
| M06 | booleani e `if` | TP | LP, DOC | A/B/C/D | sì: comportamento condizionale | branch coverage manuale/test cases |
| M07 | `elif`, logica composta | TP | LP, DOC | B/C/D | sì selettivo | motivazione rami mutuamente esclusivi |
| M08 | annidamento/validazione/refactoring | TP | LP, PN | C/D | sì se naturale | confronto due soluzioni + casi limite |
| M09 | `while`, sentinelle | TP | LP, DOC | A/C/D | sì: loop fino a condizione simulata | terminazione + trace |
| M10 | `for`, `range`, scelta ciclo | TP | LP, DOC | A/B/C/D | sì: ripeti movimento N volte | motivazione `for` vs `while` |
| M11 | selezione + iterazione/pattern | TP | LP, PS Algorithmics | C/D | sì: missione con condizioni | conteggio/accumulatore/min-max/ricerca |
| M12 | cicli annidati/efficienza intuitiva | TP | PS Algorithmics, PN | C/D/E | opzionale | soluzione corretta + trade-off |
| M13 | funzioni produttive | TP | LP, DOC, PS Essentials | A/B/C | sì forte | funzione testabile + return |
| M14 | scope/composizione | TP | LP, PN | B/C/D | sì forte | assenza globali inutili + composizione |
| M15 | top-down/decomposizione | TP | LP, PS | C/E | sì forte: missione scomposta | design top-down + API funzioni |
| M16 | assert/test/debug/refactoring | TP | DOC, PS testing intro | D/E | sì: trajectory/event debug | test table + fix + refactor |
| Checkpoint A | consolidamento primo nucleo | tutte precedenti | — | E / verifica | sì candidato | prodotto/assessment |
| M17 | stringhe, indici, slicing | TP | LP, DOC, FR | A/B/C | no | trace indici/slicing |
| M18 | metodi stringa/ricerca/conteggio | TP | LP, DOC, FR | B/C/D | no | trasformazione/normalizzazione |
| M19 | algoritmi testo/parsing | TP | LP, FR, PN | C/D/E | no | parser semplice + test |
| M20 | liste base/mutabilità | TP | LP, DOC, FR, PS Data Structures | A/B/C | possibile dati missione, non necessario | mutazione controllata |
| M21 | alias/copie/algoritmi liste | TP | LP, FP, FR | A/C/D | opzionale | alias vs copia + bug diagnosis |
| M22 | tuple/unpacking/matrici | TP | LP, FP, FR, PS Data Structures | B/C/D/E | possibile coordinate | modello dati + doppi cicli |
| Checkpoint B | strutture sequenziali | FR + fonti core | — | E / verifica | opzionale | mini-progetto/assessment |
| M23 | set/unicità/membership | LP/TP | FP, DOC, PS Data Structures | A/B/C | no | scelta set vs list |
| M24 | dizionari/lookup/frequenze | TP | LP, FP, DOC, FR, PS Data Structures | A/B/C/D | possibile mapping comandi | dict corretto + lookup |
| M25 | strutture composte/modeling | TP | LP, FP, FR | C/D/E | sì se porta valore | motivazione modello dati |
| M26 | file + errori prevedibili | TP | LP, DOC, FR, PN | A/B/C/D | dati missione solo extension | file round-trip + boundary error |
| M27 | record → oggetto | TP | LP, PS OOP, FP come controllo | A/B/C | sì forte: `Robot` object API | classe/istanze indipendenti |
| M28 | `__init__`, metodi, stato | TP | LP, PS OOP, DOC | B/C/D | sì forte | stato + comportamento + test |
| M29 | composizione/responsabilità | TP | PS OOP, FP, PN | C/D/E | sì forte | collaborazione oggetti |
| M30 | capstone OOP | tutte | FP/PN solo teacher/reference | F | sì: capstone candidato principale | analisi + classi + collezioni + test + spiegazione |
| Checkpoint C | finalizzazione/recupero/enrichment | tutte | — | F / verifica | sì | capstone + reflection |

---

# Politica delle fonti per gli studenti

Le lesson non devono diventare collage di libri.

Per ogni modulo:

1. `python-docente` produce una spiegazione canonica originale;
2. TP/Think Python guida la progressione beginner quando utile;
3. DOC verifica sintassi/semantica;
4. LP/PN controllano che non manchino concetti importanti;
5. FP impedisce di introdurre modelli mentali che dovranno essere disimparati più avanti;
6. PS offre alternative/lab e gap-check;
7. FR fornisce materiale grezzo da trasformare, non testo canonico;
8. RO fornisce contesto applicativo e runtime, non teoria generale.

## Regola `friedpython`

Ogni asset candidato viene classificato come:

```text
reuse-as-is
adapt
split
merge
rewrite
retire
```

Prima dell'import deve essere verificato per:

- compatibilità Python 3.12;
- correttezza;
- naming/stile;
- prerequisiti;
- difficoltà;
- eventuali solution leak;
- possibilità di trasformazione in Activity TheBitLab.

## Regola Romeo

Per ogni missione Romeo inserita nel corso deve esistere una riga di mapping che dichiari:

- concetto Python già introdotto;
- API Romeo usata;
- backend richiesto (`romeo-sim` per il core);
- Activity id/repository origin;
- evidence deterministica disponibile;
- fallback/general exercise equivalente.

Il corso beginner non dipende dal curriculum networking/web di Romeo.

## Regola testing

La progressione evidence è intenzionalmente anticipata:

```text
M00–M03: casi di test + trace
M04–M08: input/output attesi + esecuzione + debug
M09–M12: test di pattern/terminazione/casi limite
M13–M16: `assert` e test di funzioni
M17–M26: tabelle casi + test di trasformazioni/modelli dati
M27–M30: test del comportamento degli oggetti + capstone evidence
```

Pytest completo appartiene al percorso professionale successivo; TheBitLab può usare test nascosti anche se lo studente non ha ancora studiato pytest.
