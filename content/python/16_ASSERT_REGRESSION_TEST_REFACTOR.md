# M16 — `assert`, regression test, debug e refactoring

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-05 — Funzioni, decomposizione e testing  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- trasformare casi di test in semplici `assert`;
- distinguere caso normale, confine e caso non valido previsto dal contratto;
- leggere un `AssertionError` elementare;
- capire che un test fallito è informazione, non una soluzione automatica;
- aggiungere un test quando scopri un bug;
- verificare che la correzione non rompa casi già funzionanti;
- refactorare mantenendo invariato il comportamento richiesto;
- distinguere bug nel codice e test scritto male;
- confrontare due implementazioni con lo stesso contratto;
- spiegare il ciclo red → diagnose → fix → regression → refactor.

---

# 1. Dai casi su carta a test eseguibili

Finora abbiamo scritto tabelle come:

| input | atteso |
|---:|---:|
| 3 | 6 |
| 0 | 0 |
| -2 | -4 |

Per:

```python
def doppio(x):
    return x * 2
```

possiamo scrivere:

```python
assert doppio(3) == 6
assert doppio(0) == 0
assert doppio(-2) == -4
```

`assert` rende eseguibile una aspettativa.

---

# 2. Che cosa significa un `assert`

```python
assert espressione_booleana
```

Se l'espressione è `True`, l'esecuzione continua.

Se è `False`, Python segnala un `AssertionError`.

Non stiamo ancora studiando un framework di test.

Stiamo costruendo un ponte tra:

```text
caso di test pensato
→ aspettativa eseguibile
```

---

# 3. Un test verde non dimostra tutto

Tre assert che passano non dimostrano automaticamente che una funzione sia corretta per ogni possibile input.

I test danno **evidenza** e trovano bug.

La qualità dipende anche dai casi scelti.

Domande:

- ho provato un caso normale?;
- un confine?;
- un valore negativo se il dominio lo permette?;
- un caso che in passato falliva?.

---

# 4. Caso normale, confine, caso non valido

Per:

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

possiamo scegliere:

```python
assert eta_valida(30) is True
assert eta_valida(0) is True
assert eta_valida(120) is True
assert eta_valida(-1) is False
assert eta_valida(121) is False
```

I confini sono particolarmente importanti quando compaiono `<`, `<=`, `>` e `>=`.

---

# 5. Test fallito = domanda diagnostica

Supponiamo:

```python
def doppio(x):
    return x + 2

assert doppio(3) == 6
```

Il test fallisce.

Workflow:

```text
quale caso?
→ atteso?
→ ottenuto?
→ bug nel codice o nel test?
→ modifica minima
→ riesegui tutti i test
```

---

# 6. Il test può essere sbagliato

```python
assert doppio(3) == 7
```

Se la specifica dice “moltiplica per due”, il bug è nel test.

Non bisogna modificare il codice soltanto per far diventare verde un test errato.

Fonte autorevole:

```text
specifica / contratto
```

Il test deve rappresentarla correttamente.

---

# 7. Regression test

Scenario:

1. scopri un bug;
2. trovi un input che lo riproduce;
3. aggiungi un test per quell'input;
4. il test deve fallire prima della correzione;
5. correggi il codice;
6. riesegui il nuovo test e quelli precedenti.

Questo test protegge dal ritorno dello stesso bug in futuro.

---

# 8. Esempio di regression

Bug:

```python
def massimo(a, b):
    if a > b:
        return a
    return a
```

Caso che espone il problema:

```python
assert massimo(2, 5) == 5
```

Prima della correzione il test fallisce.

Poi correggiamo:

```python
def massimo(a, b):
    if a > b:
        return a
    return b
```

E rieseguiamo tutti i test.

---

# 9. Refactoring

Definizione operativa:

> migliorare la struttura del codice senza cambiare il comportamento richiesto.

Esempi:

- rinominare;
- estrarre una funzione;
- eliminare duplicazione;
- semplificare una condizione;
- separare I/O da logica;
- rimuovere una dipendenza globale.

I test aiutano a capire se il comportamento osservabile è rimasto lo stesso.

---

# 10. Test prima e dopo il refactoring

Prima:

```python
assert calcola_sconto(100, 10) == 10
assert calcola_sconto(50, 0) == 0
```

Refactoring della funzione.

Dopo:

```text
riesegui gli stessi test
```

Se diventano rossi, il refactoring potrebbe aver cambiato il comportamento.

---

# 11. `assert` non sostituisce la gestione degli errori

Non usiamo `assert` per gestire input utente invalido o errori esterni prevedibili.

Qui `assert` serve a verificare aspettative durante sviluppo/esercitazione.

La gestione delle eccezioni e dei confini esterni verrà affrontata nel blocco file/errori.

---

# 12. Più test, responsabilità più piccole

Una funzione piccola e con contratto chiaro è più semplice da testare.

Questo collega M15 e M16:

```text
responsabilità chiara
→ input/output chiari
→ casi più chiari
→ test più semplici
```

---

# 13. Due implementazioni, stesso contratto

Supponiamo due funzioni che devono entrambe calcolare il valore assoluto di un intero.

Se rispettano lo stesso contratto, possiamo applicare gli stessi casi a entrambe.

Questo permette di confrontare:

- correttezza;
- leggibilità;
- struttura;
- lavoro svolto quando rilevante.

Non scegliamo soltanto la versione con meno righe.

---

# 14. Ciclo di debug protetto dai test

```text
test rosso
→ riproduci
→ localizza
→ modifica minima
→ test verde
→ tutti i test verdi
→ eventuale refactor
→ tutti i test ancora verdi
```

È un modello professionale ridotto a scala beginner.

---

# 15. Git G1: diff e primo checkpoint

Durante un fix/refactor:

```text
git diff
```

mostra ciò che è cambiato.

Al Checkpoint A arriveranno:

```text
git add
git commit
```

per salvare uno stato significativo del progetto.

Il corso Git rimane separato e più ampio.

---

# 16. TheBitLab P2

Questa UDA richiede idealmente test diretti delle funzioni:

```text
funzione + argomenti
→ sandbox
→ return/exception reale
→ confronto host-side con expected
```

Questo è il profilo `P2 / python-function-v1` tracciato in `2cornot2c#756`.

Fino alla certificazione:

- `assert` nel workspace come evidence;
- verifiche manuali/formative;
- niente parser fragile del codice;
- niente trasformazione forzata in stdin/stdout quando l'obiettivo è il comportamento della funzione.

---

# 17. Activity candidate

## A — Test reader

Prevedi quali assert passano/falliscono e perché.

## B — Add a test

Aggiungi un caso limite che espone un bug.

## C — Implement from contract

Implementa una funzione a partire da contratto + test.

## D — Debug regression

Riproduci bug → test rosso → fix → tutti verdi.

## E — Mini-project funzionale

Richiede:

- almeno 3 funzioni/responsabilità;
- I/O separato;
- selezione/cicli già appresi;
- almeno 5 casi complessivi;
- call graph breve;
- spiegazione di un refactoring.

---

# 18. Exit checkpoint PY2-05

Dovresti saper:

- definire/chiamare funzioni;
- distinguere parametro/argomento;
- usare `return`;
- distinguere `return`/`print`;
- capire scope locale beginner;
- comporre funzioni;
- progettare top-down;
- separare I/O/logica/output;
- scrivere casi e `assert`;
- aggiungere un regression test;
- refactorare con protezione dei test.

---

# 19. Sintesi

```text
contratto
→ casi
→ assert
→ implementazione
→ debug
→ regression
→ refactor
```

```text
test verde ≠ prova assoluta
```

```text
specifica autorevole
→ test coerente
→ codice coerente
```

Il Checkpoint A consoliderà il primo grande nucleo del corso e introdurrà il primo commit Git guidato.

---

# Fonti e riferimenti docente

Materiale originale del corso, progettato con riferimento a:

- documentazione Python 3.12 — `assert`, funzioni e `AssertionError`;
- *Think Python / Pensare in Python* — debugging e testing beginner;
- pratiche professionali di regression testing/refactoring adattate al secondo anno;
- TheBitLab `2cornot2c#756` — profilo P2 function-behavior.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.
