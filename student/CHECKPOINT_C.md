# Checkpoint C — Finalizzazione, recupero ed evidence annuale

> Settimana 33 — nessun nuovo prerequisito.

## Scopo

Checkpoint C non introduce nuovi concetti obbligatori.

Serve a uno o più di questi obiettivi:

```text
finalizzare il capstone
recuperare un outcome core
correggere/documentare un bug
raccogliere evidence mancanti
spiegare le scelte progettuali
```

---

# 1. Se stai finalizzando il capstone completo

Il prodotto deve dimostrare in modo proporzionato:

- responsabilità OOP significative;
- stato e metodi;
- almeno un invariante;
- **composizione/collaborazione reale tra oggetti**;
- una struttura dati scelta e motivata;
- casi/test;
- almeno un edge case o transizione rifiutata;
- una evidence di bug-fix/regression/refactor;
- breve spiegazione del design.

La composizione non è opzionale nel capstone completo: è un outcome core del corso già insegnato in M29.

---

# 2. Se sei in percorso di recupero

Il docente può ridurre il dominio:

```text
meno funzionalità
meno dati
una sola relazione di collaborazione
niente file/Romeo/enrichment
```

ma non trasforma gli outcome core in facoltativi.

Se il prodotto ridotto non contiene una evidence sufficiente di composizione, puoi dimostrarla con un micro-task separato già basato su M29.

La settimana 33 non ti insegna una nozione nuova: ti permette di consolidare/dimostrare qualcosa già affrontato.

---

# 3. Checklist annuale essenziale

Devi poter spiegare, con esempi dal tuo lavoro:

## Problema e algoritmo

- input/output/vincoli;
- scelta dei costrutti;
- trace/casi limite quando pertinenti.

## Funzioni

- parametri/argomenti;
- `return`;
- scope locale;
- composizione di funzioni;
- decomposizione.

## Iterazione e stato

- `for` vs `while`;
- terminazione;
- contatore/accumulatore/min-max/ricerca;
- cicli annidati quando il dominio li richiede.

## Strutture dati

- `str/list/tuple/set/dict`;
- mutabilità/alias/copia;
- scelta della struttura dalle operazioni dominanti.

## OOP

- classe vs istanza;
- `self`/`__init__`;
- stato/metodi;
- invariante;
- istanze indipendenti;
- **composizione tra oggetti**;
- responsabilità.

## Testing/debug

- casi/assert;
- confini;
- regression test;
- refactoring con comportamento preservato.

---

# 4. Evidence di bug/regression

Documenta almeno un caso reale in forma breve:

```text
caso che falliva
→ atteso
→ ottenuto
→ causa
→ fix
→ test aggiunto/rieseguito
```

Non serve un report lungo. Serve una spiegazione verificabile.

---

# 5. Git G1 — riuso embedded

Checkpoint C non introduce G2.

Se stai versionando il capstone, riusa il workflow G1 già acquisito:

```text
git status
→ git diff
→ test
→ git add <path>
→ git diff --staged
→ git commit
→ git status
→ git log / git show
```

Il commit deve rappresentare un cambiamento coerente e verificato.

Non devi creare commit artificiali solo per raggiungere un numero.

---

# 6. Romeo / file / enrichment

Sono possibili soltanto quando aiutano il progetto e il relativo delivery è disponibile.

Non sono necessari per dimostrare il core annuale:

- hardware Romeo;
- rete;
- GUI/web;
- database;
- inheritance;
- property/dataclass;
- JSON/CSV;
- pytest professionale.

Un capstone più piccolo ma spiegabile e testato vale più di un progetto grande con parti non comprese.

---

# 7. Spiegazione finale

Devi poter rispondere in modo breve a domande come:

1. Qual è la responsabilità di ciascun oggetto?
2. Quale invariante proteggi?
3. Dove avviene la composizione e perché serve?
4. Perché hai scelto quella struttura dati?
5. Quale test di confine è importante?
6. Quale bug hai corretto e come hai impedito che tornasse?
7. Quale parte semplificheresti in una versione futura?

---

# Traguardo

Il secondo anno non termina con “conosco tante keyword”.

Il traguardo è saper collegare:

```text
problema
→ algoritmo
→ codice
→ strutture dati
→ oggetti
→ invarianti
→ composizione
→ test/debug/refactor
→ spiegazione
```
