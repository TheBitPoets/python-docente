---
marp: true
paginate: true
size: 16:9
title: M05 — Espressioni, operatori e prime funzioni
---

# M05 — Espressioni, operatori e prime funzioni
## Dal calcolo scritto bene a una prima trasformazione riusabile

PY2-02 — Primi programmi Python

---

# Oggi: che cosa deve restare davvero?

## MUST MASTER

```text
espressione → valore
/ vs // vs %
precedenza + parentesi
nomi per risultati intermedi
prima funzione
return vs print
casi di test
```

Le altre slide possono diventare approfondimento se la classe ha tempo.

---

# Problema iniziale

> 137 secondi: quanti minuti completi e quanti secondi restano?

```text
137 = 2 gruppi da 60 + 17
```

Ci servono due idee:

```text
quoziente intero
resto
```

---

# Un'espressione produce un valore

```python
2 + 3
```

produce `5`.

```python
prezzo * quantita
```

produce un valore se i nomi sono già definiti.

```text
valori → espressione → valore risultante
```

---

# Operatori principali

```text
+   somma
-   differenza
*   prodotto
/   divisione
//  divisione intera per difetto
%   resto
**  potenza
```

Domanda guida:

> quale trasformazione chiede il problema?

---

# `/` non è `//`

```python
17 / 3
```

→ `5.666...`

```python
17 // 3
```

→ `5`

Per problemi con interi non negativi:

> quanti gruppi completi da 3 stanno in 17?

---

# `%` = ciò che rimane

```python
17 % 3
```

→ `2`

Controllo:

```text
17 = (17 // 3) * 3 + (17 % 3)
17 = 5 * 3 + 2
```

---

# Worked example

```python
secondi_totali = int(input())
minuti = secondi_totali // 60
secondi = secondi_totali % 60
print(minuti, secondi)
```

Casi:

| input | output |
|---:|---|
| 137 | `2 17` |
| 60 | `1 0` |
| 59 | `0 59` |
| 0 | `0 0` |

---

# Dal resto alla prossima UDA

```python
8 % 2
```

→ `0`

```python
9 % 2
```

→ `1`

Nel prossimo blocco useremo:

```python
numero % 2 == 0
```

come condizione per prendere una decisione.

---

# Potenza: `**`

```python
2 ** 5
```

→ `32`

Errore comune:

```python
2 ^ 5
```

`^` non è la potenza in Python.

Basta riconoscere il contrasto: niente bitwise ora.

---

# Precedenza

Prevedi:

```python
2 + 3 * 4
```

→ `14`

Con parentesi:

```python
(2 + 3) * 4
```

→ `20`

---

# Regola pratica

```text
parentesi
→ potenze
→ *, /, //, %
→ +, -
```

Ma il vero obiettivo non è recitare la tabella.

> Usa parentesi quando chiariscono l'intenzione.

---

# Microscope: valore + tipo

Prevedi prima del REPL:

```python
7 + 3
7 / 2
7 // 2
7 % 2
4 * 3.5
```

Per ognuna scrivi:

```text
valore previsto
tipo previsto
```

---

# Nomi per spiegare il calcolo

Confronta:

```python
risultato = a + b * c - d / e
```

con risultati intermedi che hanno significato:

```python
costo_componenti = b * c
quota = d / e
risultato = a + costo_componenti - quota
```

Un nome utile comunica il significato del calcolo.

---

# f-string: presentazione

```python
nome = "Ada"
punti = 27
print(f"{nome} ha {punti} punti")
```

Ma in un test automatico:

```text
output richiesto = 54
```

non puoi stampare testo extra se il contratto non lo prevede.

---

# Calcolo vs presentazione

```python
base = 5
altezza = 3
area = base * altezza
print(area)
```

```text
calcolo       → base * altezza
risultato     → area
presentazione → print(area)
```

---

# Prima funzione

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Poi:

```python
area = area_rettangolo(5, 3)
print(area)
```

Una funzione può dare un nome a una trasformazione.

---

# `return` ≠ `print`

```python
def doppio(numero):
    return numero * 2
```

restituisce un valore.

```python
def mostra_doppio(numero):
    print(numero * 2)
```

produce output.

Approfondiremo la differenza in PY2-05.

---

# Testare una funzione piccola

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

Casi:

| base | altezza | atteso |
|---:|---:|---:|
| 5 | 3 | 15 |
| 1 | 7 | 7 |
| 0 | 4 | 0 |

Casi prima, codice poi.

---

# Error Clinic

### A
```python
quadrato = numero ^ 2
```

### B
```python
media = a + b + c / 3
```

### C
```python
minuti = secondi_totali / 60
```
se servono gruppi completi.

### D
```python
risultato = doppio
```
se volevi chiamare `doppio(5)`.

---

# Confrontare soluzioni

Per secondi → minuti/resto:

```python
minuti = secondi_totali // 60
resto = secondi_totali % 60
```

comunica direttamente:

```text
gruppi completi
resto
```

Criteri:

```text
correttezza
→ significato
→ leggibilità
→ lavoro non necessario
```

---

# ENRICHMENT / BACKUP — built-in

Python fornisce già molte funzioni:

```python
abs(-8)
round(3.14159, 2)
min(8, 3, 12)
max(8, 3, 12)
len("Python")
```

Questa slide è **facoltativa** in M05.

Non trasformarla in una lista da memorizzare e non usare `min/max` per evitare il successivo apprendimento del min/max progressivo.

---

# ENRICHMENT / BACKUP — `//` con negativi

`//` significa floor division, non semplicemente “taglia i decimali”.

Nel core usiamo soprattutto interi non negativi per il modello:

```text
gruppi completi + resto
```

I casi negativi possono essere esplorati solo se il core è già stabile.

---

# Activity planning

Per M05 candidiamo:

- A — trace di espressioni;
- B — formula da correggere;
- C — secondi → unità + resti;
- D — debug operatori/precedenza;
- E — mini-programma a trasformazione singola.

**Non materializziamo una nuova Activity P1 finché `python-docente#7` non è certificato.**

---

# Minimum mastery checkpoint

Prima di PY2-03 devi saper:

1. scegliere fra `/`, `//`, `%`;
2. correggere una precedenza con parentesi;
3. prevedere valore/tipo di una piccola espressione;
4. completare una funzione con `return`;
5. distinguere `return` da `print`;
6. proporre tre casi per il calcolo.

Built-in di enrichment non fanno parte del checkpoint.

---

# Recap

```text
espressione → valore
```

```text
// → gruppi completi
%  → resto
```

```text
parentesi → intenzione chiara
```

```text
funzione piccola → trasformazione con un nome
```

Prossimo blocco: **Booleani, confronti e `if`**.
