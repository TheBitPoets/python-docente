# M08 — Runbook docente

## Modulo

**Selezioni annidate, validazione e refactoring**  
UDA PY2-03 — Selezione e logica

Stato: controlled authoring continuation / draft.

## Obiettivo docente

Portare la classe da “so usare più `if`” a:

```text
capisco le dipendenze tra decisioni
→ seguo un path
→ valido prima di classificare
→ confronto strutture equivalenti
→ refactorizzo senza cambiare comportamento
```

Il criterio non è ridurre le righe, ma rappresentare correttamente la specifica e mantenerla verificabile.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. riconoscere quando una seconda decisione dipende davvero dalla prima;
2. seguire un path annidato con valori concreti;
3. validare il dominio prima di classificare;
4. distinguere valore fuori dominio da conversione impossibile;
5. confrontare annidamento e condizione composta;
6. preservare gli stessi casi durante un refactoring;
7. motivare la struttura scelta.

## GUIDED EXPOSURE

- booleano intermedio con un nome;
- idea di “coprire i path” senza metriche quantitative;
- mini-project integrato se il tempo lo consente.

## ENRICHMENT / BACKUP

- De Morgan;
- confronto fra più refactoring equivalenti;
- Romeo path trace.

De Morgan non fa parte dell'exit gate ordinario di M08.

---

# Preparazione

## Ambiente

- Classroom Environment TheBitLab;
- Python 3.12-compatible;
- REPL + script;
- Flowchart Lab se certificato, fallback carta/lavagna;
- Romeo soltanto come applicazione opzionale.

## Materiali

- lesson `content/python/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`;
- slide `slides/python/modules/08_ANNIDAMENTO_VALIDAZIONE_REFACTOR.md`;
- tabella dei path credenziali/account;
- problema voto `0..10`;
- un flow chart con decisione dipendente;
- mini-project di classificazione validata.

---

# Ora teoria attiva 1 — annidamento e path

## 0–10 min — retrieval M07

- primo ramo vero;
- `if` indipendenti vs `elif`;
- `and` / `or`;
- intervallo.

## 10–25 min — credenziali/account

Costruire il diagramma prima del codice.

Domanda:

> La seconda domanda ha senso se la prima è falsa?

Da qui emerge l'annidamento.

## 25–40 min — path trace

Tre percorsi distinti:

```text
credenziali false
credenziali true + account false
credenziali true + account true
```

Usare anche il caso `credenziali false + account true` per mostrare irrilevanza della seconda variabile in quel path.

## 40–55 min — annidato vs `and`

Confrontare due specifiche:

1. solo `accesso/non accesso`;
2. `credenziali errate/account disabilitato/accesso`.

Mostrare che una semplificazione può essere corretta nella prima e perdere informazioni nella seconda.

## 55–60 min — exit ticket

“Dipendenza reale o accidentale?” su una specifica nuova.

---

# Ora teoria attiva 2 — validazione e refactoring

## 0–20 min — voto valido

Separare:

```text
tipo corretto ma valore fuori dominio
```

da:

```text
conversione impossibile
```

Non introdurre `try/except`.

## 20–35 min — validazione prima della classificazione

Usare casi:

```text
-1, 0, 5, 6, 10, 11
```

Mostrare bug di validazione tardiva.

## 35–45 min — booleano nominato

```python
voto_valido = 0 <= voto <= 10
```

Domanda:

> il nome aggiunge un concetto del dominio?

## 45–60 min — refactoring protetto da test

Da annidato a condizione composta in un caso equivalente.

Workflow:

```text
congela casi
→ modifica struttura
→ riesegui stessi casi
→ confronta
```

Non aprire De Morgan in questo blocco se la classe non ha già consolidato path, validazione e refactoring.

---

# Ora laboratorio

## Fase 1 — path trace, 10 min

Due piccoli programmi annidati, tre input ciascuno.

## Fase 2 — validazione, 15 min

Implementare `voto 0..10` + classificazione.

## Fase 3 — debug clinic, 10 min

Bug:

- validazione dopo classificazione;
- dipendenza accidentale;
- condizione composta che perde un risultato distinto.

## Fase 4 — controlled refactor, 10 min

Ricevere una versione annidata e un set di test. Rifattorizzare soltanto se il comportamento richiesto resta identico.

## Fase 5 — mini-project, fino a 15 min o prosecuzione

Classificatore validato o configuratore semplice:

1. input/output/vincoli;
2. flow chart/pseudocodice;
3. tabella path;
4. codice;
5. test;
6. spiegazione.

Il progetto **può proseguire** come compito/recupero. Non deve comprimere l'handoff a `while` né diventare prerequisito extra.

---

# Minimum mastery gate — prima di PY2-04

Considerare M08/PY2-03 consolidato quando lo studente riesce a:

- spiegare perché una decisione è annidata o indipendente;
- seguire un path con due decisioni;
- validare un valore prima di classificarlo;
- proporre casi che coprono i risultati distinti;
- confrontare `if A: if B:` con `if A and B:` e dire quando perdono/non perdono informazione;
- rifattorizzare un caso semplice conservando gli stessi test;
- motivare la struttura scelta in una frase.

Non richiedere De Morgan o short-circuit per superare il gate di PY2-03.

---

# Misconception watchlist

## M1 — annidare rende il codice più “avanzato”

Correzione: annidamento solo quando rappresenta una dipendenza reale.

## M2 — meno livelli = sempre meglio

Correzione: verificare quali distinzioni la specifica richiede.

## M3 — validazione = `try/except`

Correzione: qui validiamo il **dominio del valore** già convertito.

## M4 — se il voto è -1 posso prima classificarlo come insufficiente

Correzione: la classificazione non ha senso fuori dal dominio valido.

## M5 — refactoring = riscrivere finché sembra più corto

Correzione: stessi test e stesso comportamento richiesto.

## M6 — una condizione composta è sempre equivalente a due livelli annidati

Correzione: dipende dagli output distinti e dai path richiesti.

## M7 — in M08 dobbiamo continuare a chiedere input finché è valido

Correzione: la ripetizione richiede `while`, non ancora introdotto.

---

# Differenziazione

## Recupero

- due decisioni massimo;
- evidenziare un path alla volta sul flow chart;
- tabella input → condizione 1 → condizione 2 → output;
- starter con struttura annidata già pronta;
- separare validità e classificazione su carta prima del codice.

## Enrichment

- confrontare due refactoring entrambi corretti;
- costruire il set minimo di casi che copre tutti i risultati distinti;
- semplice equivalenza di De Morgan guidata, senza formalismo;
- Romeo path trace su missione già nota.

---

# Evidence docente

Raccogliere:

- path trace annidato;
- tabella di validazione/confini;
- debug di validazione tardiva;
- refactoring con stessi test;
- mini-project o almeno design completo;
- motivazione “perché annidato / perché composto”.

M08 prepara la prima prova teorica/scritta e chiude il nucleo di selezione prima dei cicli.

---

# Cosa NON anticipare

- `while` per ripetere validazione;
- `try/except` come nuovo tema;
- early return/guard clause dentro funzioni come pattern sistematico;
- De Morgan formale;
- funzioni predicate avanzate;
- match/case;
- truthiness di collezioni.

---

# Handoff a PY2-04

Domanda finale:

> Se il dato non è valido, come facciamo a chiedere di nuovo finché la condizione cambia?

Questo apre naturalmente:

```text
while
→ stato che cambia
→ terminazione
→ sentinelle
→ validazione ripetuta
```

Poi confronteremo con `for` quando la ripetizione è guidata da un numero/insieme noto.

---

# Stato tecnico

- lesson M08: **draft presente**;
- slide M08: **draft presente**;
- nuova Activity P1: **non materializzata**;
- M04 canary: `python-docente#7`;
- private Actions blocker: `python-docente#8`;
- Flowchart Lab: `2cornot2c#753/#754`;
- Romeo runtime: applicazione opzionale finché non certificato;
- curriculum: **FROZEN**.