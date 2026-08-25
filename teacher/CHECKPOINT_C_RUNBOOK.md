# Checkpoint C — Runbook docente

## Funzione

Settimana 33: finalizzazione, recupero ed evidence annuale.

**Nessun nuovo prerequisito.**

Il checkpoint serve a chiudere ciò che è già stato insegnato, non ad aggiungere nuovi concetti perché il calendario è quasi finito.

---

# Priorità

Ordine consigliato:

1. outcome core mancanti;
2. finalizzazione capstone;
3. bug/regression;
4. evidence annuale;
5. chiarezza di responsabilità/composizione;
6. enrichment soltanto dopo il core.

---

# Composizione — correzione importante

Il curriculum frozen richiede composizione fra gli outcome OOP obbligatori.

Quindi:

```text
capstone completo
→ composizione/collaborazione reale obbligatoria
```

Non accettare come equivalente:

> “non serve composizione”

se il capstone è usato come prodotto finale completo del track.

## Recovery

Se lo studente segue un percorso ridotto, ridurre il **dominio**, non cancellare l'outcome.

Esempio:

```text
classe A
+ semplice collaboratore B
+ una sola regola di collaborazione
```

Se il prodotto ridotto non può integrare composizione senza diventare artificiale, raccogliere una micro-evidence separata su M29. Questo non introduce un concetto nuovo: recupera un outcome già insegnato.

---

# Capstone completo — evidence minima

Verificare:

- responsabilità OOP significative;
- stato e metodi;
- invariante;
- composizione reale;
- struttura dati motivata;
- test normali/confini;
- transizione rifiutata o edge case;
- bug-fix/regression/refactor;
- spiegazione breve delle scelte.

Non valutare quantità di classi/righe come proxy della qualità.

---

# Recovery annuale

Usare micro-task mirati per outcome mancanti:

- trace ciclo / terminazione;
- stato progressivo/invariante di loop;
- `return`/scope;
- alias/copia;
- scelta struttura dati;
- transizione OOP;
- composizione;
- regression test.

Non chiedere uno stesso mega-progetto a chi deve recuperare un singolo deficit.

---

# Git G1 embedded

Nessun G2 nuovo.

Se il capstone viene versionato, riusare:

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

Git resta process evidence. Non imporre un numero di commit artificiale.

Se lo stato non è atteso, usare remediation G1 canonica e recovery beginner; niente comandi distruttivi improvvisati.

---

# Romeo / file / enrichment

Solo se utili e certificati/disponibili:

- `romeo-sim`;
- persistenza file;
- `__str__`/property/inheritance/dataclass come enrichment.

Non bloccare il core su capability esterne.

La variante generica del capstone deve restare sempre disponibile.

---

# Valutazione

La valutazione finale deve privilegiare:

```text
correttezza
→ comprensione
→ modello dati
→ responsabilità/invarianti
→ composizione
→ test/debug
→ spiegazione
```

Non:

```text
numero classi
numero file
numero feature
framework usati
```

---

# AI

Nelle evidence valutative core:

- nessuna AI generativa per produrre algoritmo/codice/soluzione;
- eventuale AI-assisted review/debug soltanto in attività esplicitamente autorizzate;
- lo studente deve sempre verificare, testare e spiegare.

---

# Gate di uscita

Checkpoint C è completo quando:

- non introduce nuovi prerequisiti;
- gli outcome core mancanti hanno evidence;
- la composizione OOP è dimostrata;
- il capstone è finalizzato o ridotto in modo controllato;
- eventuali enrichment non hanno sottratto tempo al core;
- il docente può distinguere chiaramente cosa è padroneggiato e cosa resta da recuperare.
