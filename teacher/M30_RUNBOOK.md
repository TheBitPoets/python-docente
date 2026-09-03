# M30 — Runbook docente

## Modulo

**Capstone OOP — prodotto finale del secondo anno**  
UDA PY2-10 — Classi, oggetti e capstone

Stato: draft editoriale controllato.

## Funzione del capstone

Il capstone deve dimostrare integrazione delle competenze core, non quantità di codice.

```text
analisi
→ modello dati
→ funzioni
→ oggetti
→ invarianti
→ composizione
→ test
→ debug/refactor
→ spiegazione
```

---

# Finestra reale

La mappa frozen assegna M27–M30 alle settimane 29–32.

Quindi:

```text
M29 / settimana 31
→ skeleton progettuale del capstone

M30 / settimana 32
→ implementazione + integration + review dedicata

Checkpoint C / settimana 33
→ eventuale finalizzazione / recupero / evidence
```

La vecchia formula “settimane 31–32” va letta come **handoff M29 + M30**, non come due settimane aggiuntive per M30.

---

# Contratto minimo del capstone completo

Richiedere in forma proporzionata:

- almeno **due responsabilità OOP significative**;
- **composizione/collaborazione reale** tra oggetti;
- almeno un invariante;
- almeno una scelta di struttura dati motivata;
- metodi con responsabilità riconoscibili;
- almeno 5 casi/test complessivi;
- almeno un edge case o transizione rifiutata;
- almeno una evidence di bug-fix/regression/refactor;
- breve spiegazione progettuale.

Non imporre un numero elevato di classi. La quantità non sostituisce il design.

---

# Variante generica

Dominio esempio:

```text
Veicolo
+ MissioneConsegna
```

Possibili responsabilità:

```text
Veicolo
  stato: posizione, carico, capacita
  metodi: carica, scarica, sposta

MissioneConsegna
  stato: veicolo, checkpoint, completati
  metodi: completa_checkpoint, conclusa
```

Vincoli:

- niente GUI;
- niente database;
- niente rete;
- persistenza file soltanto se realmente utile e M26 è consolidato.

---

# Variante Romeo

Solo se `romeo-sim` è certificato nel Classroom Environment.

Dominio:

```text
Missione
└─ usa Robot
```

Rubrica e outcome restano equivalenti alla variante generica.

Hardware fisico non è requisito del core.

---

# Skeleton prima del codice

Prima dell'implementazione raccogliere:

```text
responsabilità
classi candidate
stato
metodi
invarianti
relazioni di composizione
strutture dati
casi/test
```

Non chiedere documentazione lunga: basta ciò che guida decisioni reali.

---

# Sviluppo incrementale

Sequenza raccomandata:

```text
1. skeleton + casi
2. prima responsabilità
3. invariante + test
4. collaboratore
5. composizione
6. integrazione
7. edge case
8. bug/regression
9. refactor
10. spiegazione finale
```

Ogni fase deve lasciare qualcosa di eseguibile/verificabile quando possibile.

---

# Strutture dati

Il capstone deve riusare almeno una scelta di struttura dati significativa dal corso:

```text
list / tuple / set / dict
```

ma non deve usare più collezioni del necessario.

La rubrica valuta:

> perché questa struttura rappresenta bene le operazioni dominanti?

non:

> quante strutture diverse hai inserito?

---

# Test minimi

Chiedere casi su:

- costruzione;
- stato osservabile;
- transizione valida;
- transizione rifiutata/confine;
- collaborazione;
- indipendenza fra istanze quando pertinente.

La suite concreta dipende dal dominio.

---

# Regression + refactor

Richiedere almeno una evidence del ciclo:

```text
bug/caso mancante
→ test rosso
→ fix
→ tutti verdi
→ eventuale refactor
→ ancora verdi
```

Non serve un report lungo: bastano caso, causa, fix e verifica.

---

# Git G1 embedded

Git resta il workflow di processo già acquisito, non un nuovo corso nel capstone.

Checkpoint significativi possibili:

```text
skeleton coerente
core + test
fix/refactor finale
```

Non imporre un numero artificiale di commit.

Prima di ogni commit significativo:

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

Riusa `TheBitPoets/git` G1 canonico per remediation; nessun G2 nuovo.

---

# Spiegazione finale

Breve e concreta:

- problema;
- responsabilità/classi;
- composizione;
- invariante;
- struttura dati scelta;
- test/edge significativo;
- bug o refactor importante;
- limite attuale / miglioramento futuro.

La spiegazione deve essere coerente con il codice reale.

---

# Recovery

Se uno studente non riesce a completare il prodotto pieno:

```text
riduci dominio
→ mantieni outcome
```

Esempi:

- meno operazioni;
- una sola relazione di composizione;
- collezione più piccola;
- niente file/Romeo.

Se il prodotto ridotto non riesce a dimostrare un outcome frozen (per esempio composizione), raccogliere quell'evidence con un micro-task separato. Non trasformare l'outcome in opzionale.

---

# Enrichment soltanto dopo il core

Possibili:

- `__str__/__repr__`;
- property introduttiva;
- inheritance semplice;
- dataclass come confronto;
- persistenza file;
- scenario Romeo più ricco.

Nessuno di questi deve compromettere il capstone core.

---

# AI policy

Per capstone core/valutativo:

- nessuna generazione AI della soluzione;
- eventuale AI-assisted review/debug soltanto se l'attività lo dichiara esplicitamente e lo studente verifica/testa/spiega;
- il docente valuta la comprensione reale.

---

# P3 — teacher/delivery boundary

Il profilo `2cornot2c#758` riguarda eventuale object autograding. Non è prerequisito pedagogico per insegnare o valutare manualmente il capstone.

Fino alla certificazione:

- assert/manual evidence;
- rubriche;
- nessuna promessa di object autograding.

---

# Exit del secondo anno

Il prodotto finale deve permettere allo studente di spiegare questa catena:

```text
problema
→ algoritmo
→ dati
→ funzioni
→ strutture
→ oggetti
→ invarianti
→ composizione
→ test/debug/refactor
```

Questo è il traguardo. Non “più classi, più framework, più righe”.
