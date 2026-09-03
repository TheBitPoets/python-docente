# M16 — Runbook docente

## Modulo

**`assert`, regression test, debug e refactoring**  
UDA PY2-05 — Funzioni, decomposizione e testing

Stato: draft editoriale controllato.

## Obiettivo

Portare la classe dal semplice “provo qualche input” al ciclo:

```text
contratto → casi → assert → diagnosi → fix → regression → refactor
```

Lo studente deve collegare sempre il test alla specifica. `assert` è il ponte fra un caso pensato e un'aspettativa eseguibile, non l'inizio di un corso sui framework di testing.

---

# Priorità didattica

## MUST MASTER

Entro la fine del modulo lo studente deve saper:

1. trasformare casi semplici in `assert`;
2. scegliere almeno un caso normale e i confini rilevanti;
3. leggere un `AssertionError` elementare;
4. capire che un test verde non dimostra correttezza universale;
5. distinguere bug nel codice e test incoerente con la specifica;
6. costruire un regression test che riproduce un bug;
7. correggere con modifica minima e rieseguire tutti i test;
8. refactorare mantenendo gli stessi test verdi.

## GUIDED EXPOSURE

- confronto fra due implementazioni con lo stesso contratto;
- ragionare su casi non coperti;
- `git status`/`git diff` come evidence G1 guidata durante fix/refactor.

## TEACHER / DELIVERY ONLY

- profilo TheBitLab P2 `2cornot2c#756`;
- meccanica di import/sandbox/grading function-behavior;
- decisioni CI/runner.

P2 non è un concetto da studente e non deve occupare il deck di lezione ordinario.

---

# Ora teoria attiva 1 — assert e casi

1. Riprendere una funzione semplice e una tabella input/atteso.
2. Trasformare i casi in `assert`.
3. Aggiungere casi di confine.
4. Mostrare anche un test con expected sbagliato e chiedere se il problema è nel codice o nel test.

Esempio:

```python
def doppio(x):
    return x * 2

assert doppio(3) == 6
assert doppio(0) == 0
assert doppio(-2) == -4
```

Domanda costante:

> quale frase della specifica rappresenta questo test?

---

# Ora teoria attiva 2 — regression e refactoring

1. Presentare una funzione quasi corretta.
2. Trovare un input che riproduce il bug.
3. Aggiungere un test che fallisce.
4. Correggere con una modifica minima.
5. Rieseguire tutti i test.
6. Refactorare nomi/struttura e rieseguire ancora.

Il valore didattico sta nella sequenza causale, non nell'etichetta “regression”.

---

# Laboratorio

- **A — Test reader:** prevedere quali assert passano o falliscono.
- **B — Add a test:** aggiungere un confine o un caso che espone un bug.
- **C — Implement from contract:** scrivere una funzione a partire da contratto + casi.
- **D — Regression:** bug → test rosso → fix → tutti verdi.
- **E — Refactor:** migliorare struttura mantenendo gli stessi test.

Durante fix/refactor, se il profilo managed è disponibile, usare gli outcome G1:

```text
G1.OBSERVE.STATUS
G1.OBSERVE.DIFF
```

per osservare lo stato e il cambiamento. Non introdurre ancora staging/commit come nuovo blocco: arrivano al Checkpoint A.

---

# Minimum mastery gate — prima del Checkpoint A

Considerare M16 consolidato quando lo studente riesce a:

- convertire una tabella input/atteso in assert semplici;
- individuare almeno un confine rilevante;
- spiegare un assert fallito in termini di atteso/ottenuto;
- verificare se il bug è nel codice o nel test rispetto alla specifica;
- aggiungere un test che riproduce un bug;
- eseguire fix e tutti i test precedenti;
- refactorare senza cambiare il comportamento osservato.

Non richiedere pytest, coverage numerica, P2 o CI per superare il gate.

---

# Misconception watchlist

- test verdi non significano correttezza per ogni input;
- un test rosso non indica automaticamente la riga da cambiare;
- anche il test può essere incoerente con la specifica;
- un regression test va costruito per riprodurre il bug;
- refactoring non significa aggiungere funzionalità;
- `assert` non sostituisce la validazione degli input utente;
- “far diventare verde” non sostituisce la comprensione della causa.

---

# Differenziazione

## Recupero

- una funzione con un solo `return`;
- tre assert semplici;
- un solo bug;
- refactoring limitato a naming/estrazione minima.

## Enrichment

- due implementazioni con gli stessi test;
- più confini;
- spiegare quali casi non sono coperti;
- piccola suite di regression cases.

---

# Evidence docente

Raccogliere almeno:

- gruppo di assert;
- un caso di confine;
- un regression test aggiunto prima del fix;
- riesecuzione completa dopo il fix;
- refactoring con comportamento preservato;
- opzionalmente lettura di `git diff` del cambiamento.

---

# P2 TheBitLab — teacher/delivery boundary

Il profilo `2cornot2c#756` è il target per test diretti delle funzioni. Il corso non deve simulare P2 trasformando artificialmente tutte le funzioni in programmi stdin/stdout.

Fino alla certificazione:

- `assert` nel workspace;
- evidence manuale/formativa;
- nessun parser fragile del codice.

Questa sezione riguarda il delivery del corso, non ciò che lo studente deve studiare.

---

# Git G1 / handoff al Checkpoint A

M16 chiude la fase Observe e prepara il workflow G1 guidato del Checkpoint A.

La fonte canonica è `TheBitPoets/git`; Python non duplica le lesson. Il contratto locale è `config/git-g1-consumer.json` in modalità:

```text
embedded-outcome-subset
```

Al Checkpoint A il workflow sarà:

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

Gli outcome aggiunti al checkpoint sono staging intenzionale, commit intenzionale, lettura della storia e modello beginner `HEAD → branch corrente → commit corrente`.

---

# Cosa NON anticipare

- pytest come framework studente;
- fixtures, parametrizzazione e mocking;
- coverage numerica;
- property-based testing;
- CI obbligatoria;
- branch/merge/rebase/remotes come outcome Python.

---

# Exit checkpoint PY2-05

Prima del Checkpoint A lo studente dovrebbe saper:

1. definire e chiamare funzioni;
2. distinguere parametro/argomento;
3. usare `return` e distinguerlo da `print`;
4. capire lo scope locale beginner;
5. passare dati esplicitamente;
6. comporre funzioni;
7. progettare responsabilità in modo top-down senza burocrazia;
8. scrivere contratti intuitivi quando aiutano;
9. trasformare casi in `assert`;
10. aggiungere un regression test;
11. refactorare con test verdi;
12. osservare stato e diff del proprio cambiamento in modo guidato.

Dopo il Checkpoint A il corso passa a stringhe e sequenze testuali, mantenendo funzioni, test e Git come workflow trasversali.
