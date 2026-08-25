# M13 — Funzioni produttive: parametri, argomenti e `return`

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-05 — Funzioni, decomposizione e testing  
> **Baseline:** Python 3.12-compatible nel Classroom Environment TheBitLab

## Obiettivi

Alla fine del modulo dovresti saper:

- definire e chiamare una funzione;
- distinguere il nome di una funzione dalla sua chiamata;
- distinguere parametro e argomento;
- usare uno o più parametri semplici;
- restituire un valore con `return`;
- usare il valore restituito in un assegnamento o in un'altra espressione;
- distinguere una funzione che calcola da una funzione che stampa;
- sapere che una funzione senza `return` esplicito restituisce `None`;
- scrivere predicate semplici che restituiscono `bool`;
- verificare una funzione con più casi di test.

---

# 1. Dal blocco monolitico a una trasformazione nominata

Finora possiamo già scrivere programmi con input, selezioni e cicli.

Il rischio è produrre un unico blocco crescente di codice.

Una funzione ci permette di dare un nome a una responsabilità:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Il punto non è soltanto evitare righe duplicate.

Il punto è poter dire:

> questa parte del programma calcola l'area di un rettangolo.

---

# 2. Definizione e chiamata non sono la stessa cosa

Definizione:

```python
def doppio(numero):
    return numero * 2
```

Chiamata:

```python
doppio(5)
```

La definizione descrive il comportamento.
La chiamata lo usa con dati concreti.

Il nome `doppio` e l'espressione `doppio(5)` non sono la stessa cosa.

---

# 3. Parametro e argomento

```python
def doppio(numero):
    return numero * 2
```

`numero` è un **parametro**: il nome usato nella definizione.

Nella chiamata:

```python
doppio(7)
```

`7` è l'**argomento** fornito a quella chiamata.

Modello:

```text
argomento concreto
      ↓
parametro locale
      ↓
corpo funzione
```

---

# 4. Modello della chiamata

Per:

```python
def somma(a, b):
    return a + b

risultato = somma(2, 3)
```

possiamo pensare:

```text
2 → a
3 → b
corpo → a + b
return → 5
5 → punto della chiamata
risultato → 5
```

`return` restituisce un valore al chiamante.

---

# 5. `print` non è `return`

Confronta.

## Versione A

```python
def somma(a, b):
    print(a + b)
```

## Versione B

```python
def somma(a, b):
    return a + b
```

La versione A produce output.
La versione B produce un valore utilizzabile dal programma.

Con B possiamo fare:

```python
x = somma(2, 3)
print(x * 10)
```

La domanda non è “`print` è sbagliato?”.

La domanda è:

> qual è la responsabilità di questa funzione?

Se deve **calcolare**, `return` è il risultato naturale.

---

# 6. Separare calcolo e presentazione

Preferiamo spesso:

```python
def area_rettangolo(base, altezza):
    return base * altezza

area = area_rettangolo(3, 4)
print(area)
```

rispetto a:

```python
def area_rettangolo(base, altezza):
    print(base * altezza)
```

La prima forma:

- rende il calcolo riutilizzabile;
- rende il test più semplice;
- separa logica e interfaccia.

---

# 7. Più parametri

```python
def costo(prezzo_unitario, quantita):
    return prezzo_unitario * quantita
```

Chiamata:

```python
totale = costo(12, 3)
```

Trace:

```text
prezzo_unitario → 12
quantita        → 3
return          → 36
```

L'ordine degli argomenti posizionali deve rispettare il contratto della funzione.

---

# 8. Predicate: funzioni che rispondono sì/no

Dopo aver studiato le condizioni, possiamo dare un nome a una domanda booleana:

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

Poi:

```python
if eta_valida(eta):
    ...
```

Un buon nome rende leggibile la decisione.

---

# 9. Funzione senza `return` esplicito

```python
def saluta(nome):
    print("Ciao", nome)
```

La funzione produce output, ma non contiene un `return` esplicito.

Python restituisce comunque:

```python
None
```

A livello beginner basta ricordare:

> se una funzione deve produrre un valore utilizzabile, rendilo esplicito con `return`.

---

# 10. Codice dopo `return`

```python
def doppio(x):
    return x * 2
    print("fine")
```

Quando viene eseguito `return`, la chiamata della funzione termina.

Il `print` successivo non viene raggiunto.

Questo è un buon caso di Error Clinic.

---

# 11. Worked example: quoziente e resto

```python
def quoziente_resto(totale, gruppo):
    quoziente = totale // gruppo
    resto = totale % gruppo
    return quoziente, resto
```

Per ora il ritorno multiplo viene mostrato come tuple/unpacking **solo come preview controllata** se la classe è pronta.

Versione core più semplice:

```python
def resto_divisione(totale, gruppo):
    return totale % gruppo
```

Non anticipiamo tuple se distraggono dall'obiettivo `return`.

---

# 12. Testare una funzione

Prima del framework di testing possiamo già progettare casi:

```python
def doppio(x):
    return x * 2
```

Casi:

| input | atteso |
|---:|---:|
| 3 | 6 |
| 0 | 0 |
| -2 | -4 |

Poi verifichiamo:

```python
print(doppio(3))
print(doppio(0))
print(doppio(-2))
```

In M16 passeremo agli `assert`.

---

# 13. Call trace

```python
def differenza(a, b):
    return a - b

x = differenza(10, 4)
y = differenza(x, 3)
```

Completa:

| chiamata | `a` | `b` | return |
|---|---:|---:|---:|
| `differenza(10, 4)` | 10 | 4 | ? |
| `differenza(x, 3)` | ? | 3 | ? |

Il trace delle chiamate prepara il call graph di M14/M15.

---

# 14. Error Clinic

## A — chiamata dimenticata

```python
x = doppio
```

vs:

```python
x = doppio(5)
```

Non approfondiamo ancora le funzioni come oggetti; qui basta riconoscere che manca la chiamata richiesta.

## B — `return` mancante

```python
def doppio(x):
    risultato = x * 2
```

Il valore viene calcolato ma non restituito.

## C — stampa al posto di risultato

Una funzione che dovrebbe essere usata in un calcolo stampa invece di restituire.

## D — parametro errato

Il corpo usa un nome diverso dal parametro definito.

## E — codice dopo `return`

Codice non raggiungibile nella normale esecuzione di quel ramo.

---

# 15. Activity candidate

## A — Call trace

Completa parametro/argomento/return per più chiamate.

## B — Controlled Change

Trasforma una funzione che stampa in una funzione che restituisce e aggiorna il chiamante.

## C — Implement

Scrivi funzioni numeriche o predicate con almeno tre casi dichiarati prima del codice.

## D — Debug

Correggi `return` mancante, valore ignorato, parametro sbagliato e codice irraggiungibile.

Nessuna Activity P2 viene materializzata finché `2cornot2c#756` non è implementata e certificata con un consumer reale.

---

# 16. Checkpoint

Sai spiegare:

1. definizione vs chiamata;
2. parametro vs argomento;
3. `return` vs `print`;
4. dove finisce il valore restituito;
5. che cosa accade senza `return` esplicito;
6. perché un predicate che restituisce `bool` può migliorare la leggibilità;
7. come verificare una funzione su più input.

---

# 17. Sintesi

```text
argomenti
→ parametri locali
→ corpo
→ return
→ valore al chiamante
```

```text
funzione = responsabilità nominata + contratto
```

```text
calcolo → return
presentazione → print quando è davvero la responsabilità
```

Nel prossimo modulo studieremo dove vivono i nomi locali e come far collaborare funzioni passando i dati in modo esplicito.

---

# Fonti e riferimenti docente

Materiale originale del corso, progettato con riferimento a:

- documentazione Python 3.12 — definizione/chiamata di funzioni e `return`;
- *Think Python / Pensare in Python* — funzioni e modello beginner;
- *Learning Python / Imparare Python* — reference di funzioni e scope;
- TheBitLab `2cornot2c#756` — futuro profilo P2 function-behavior.

Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.
