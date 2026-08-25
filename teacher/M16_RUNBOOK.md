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

Lo studente deve collegare sempre il test alla specifica.

## Ora teoria attiva 1 — assert e casi

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

## Ora teoria attiva 2 — regression e refactoring

1. Presentare una funzione quasi corretta.
2. Trovare un input che riproduce il bug.
3. Aggiungere un test che fallisce.
4. Correggere con una modifica minima.
5. Rieseguire tutti i test.
6. Refactorare nomi/struttura e rieseguire ancora.

## Laboratorio

- **A — Test reader:** prevedere quali assert passano o falliscono.
- **B — Add a test:** aggiungere un confine o un caso che espone un bug.
- **C — Implement from contract:** scrivere una funzione a partire da contratto + casi.
- **D — Regression:** bug → test rosso → fix → tutti verdi.
- **E — Refactor:** migliorare struttura mantenendo gli stessi test.

Se Git managed è disponibile, osservare il refactoring con `git diff`.

## Misconception watchlist

- test verdi non significano correttezza per ogni input;
- un test rosso non indica automaticamente la riga da cambiare;
- anche il test può essere incoerente con la specifica;
- un regression test va costruito per riprodurre il bug;
- refactoring non significa aggiungere funzionalità;
- `assert` non sostituisce la validazione degli input utente.

## Differenziazione

### Recupero

- una funzione con un solo `return`;
- tre assert semplici;
- un solo bug;
- refactoring limitato a naming/estrazione minima.

### Enrichment

- confrontare due implementazioni con gli stessi test;
- aggiungere più confini;
- spiegare quali casi non sono coperti;
- progettare una piccola suite di regression cases.

## Evidence docente

Raccogliere almeno:

- gruppo di assert;
- un caso di confine;
- un regression test aggiunto prima del fix;
- riesecuzione completa dopo il fix;
- refactoring con comportamento preservato.

## P2 TheBitLab

Il profilo `2cornot2c#756` è il target per test diretti delle funzioni. Il corso non deve simulare P2 trasformando artificialmente tutte le funzioni in programmi stdin/stdout.

Fino alla certificazione:

- `assert` nel workspace;
- evidence manuale/formativa;
- nessun parser fragile del codice.

## Git G1 / Checkpoint A

M16 prepara il primo checkpoint Git guidato:

```text
git status
→ git diff
→ test
→ git add
→ git commit
→ git log essenziale
```

Il materiale Git canonico resta separato dal corso Python.

## Cosa NON anticipare

- pytest come framework studente;
- fixtures, parametrizzazione e mocking;
- coverage numerica;
- property-based testing;
- CI obbligatoria.

## Exit checkpoint PY2-05

Prima del Checkpoint A lo studente dovrebbe saper:

1. definire e chiamare funzioni;
2. distinguere parametro/argomento;
3. usare `return` e distinguerlo da `print`;
4. capire lo scope locale beginner;
5. passare dati esplicitamente;
6. comporre funzioni;
7. progettare top-down;
8. scrivere contratti intuitivi;
9. trasformare casi in `assert`;
10. aggiungere un regression test;
11. refactorare con test verdi.

Dopo il Checkpoint A il corso passa a stringhe e sequenze testuali.
