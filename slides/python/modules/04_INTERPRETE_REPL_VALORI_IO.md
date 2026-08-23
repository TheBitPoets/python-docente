---
marp: true
paginate: true
size: 16:9
title: M04 — Interprete, REPL, valori e input/output
---

# M04 — Interprete, REPL, valori e I/O
## Dal nostro algoritmo alle prime istruzioni Python

PY2-02 — Primi programmi Python

---

# Da dove partiamo?

Problema:

> Leggi due numeri interi e mostra la loro somma.

Prima di Python abbiamo già:

```text
INPUT → due interi
ELABORAZIONE → somma
OUTPUT → risultato
```

Python sarà il modo con cui descriviamo questi passi al computer.

---

# Oggi impariamo a...

- usare il REPL;
- riconoscere valori e tipi;
- dare nomi ai valori;
- usare `print()` e `input()`;
- convertire testo in numero;
- creare un primo file `.py`;
- leggere errori semplici;
- verificare più casi.

Regola della giornata:

> **prima prevedi, poi esegui.**

---

# Che cosa fa Python?

```text
programma .py
    ↓
interprete Python
    ↓
esecuzione
    ↓
output oppure errore
```

Python non esegue quello che volevamo dire.

Esegue quello che abbiamo scritto secondo le regole del linguaggio.

---

# REPL = laboratorio rapido

```text
Read → Eval → Print → Loop
```

Prima prevedi:

```python
2 + 3
```

Poi prova.

Ora fai lo stesso con:

```python
10 - 4
3 * 5
10 / 2
```

Non correre: confronta sempre previsione e risultato.

---

# Valori diversi

```python
42
-7
```

sono `int`.

```python
3.5
2.0
```

sono `float`.

```python
"42"
"Python"
```

sono `str`.

```python
True
False
```

sono `bool`.

---

# Microscope: 42 oppure "42"?

Confronta:

```python
42
```

con:

```python
"42"
```

Il primo è un numero.
Il secondo è testo.

Prevedi:

```python
2 + 3
"2" + "3"
```

Perché i risultati sono diversi?

---

# Un nome per un valore

```python
eta = 15
```

Modello iniziale:

```text
eta ──> 15
```

Poi:

```python
eta + 1
```

`=` qui è **assegnamento**.

Non significa che `eta` sarà uguale a 15 per sempre.

---

# Nomi che raccontano il dato

Confronta:

```python
x = 25
```

con:

```python
prezzo_totale = 25
```

Quale versione aiuta di più chi legge?

La leggibilità fa parte della correttezza professionale del codice.

---

# `print()` produce output

```python
nome = "Anna"
print(nome)
```

mostra:

```text
Anna
```

Nel REPL:

```python
2 + 3
```

può essere mostrato automaticamente.

In uno script, se vuoi output:

```python
print(2 + 3)
```

---

# `input()` riceve testo

```python
dato = input()
```

Anche se digiti:

```text
12
```

`dato` è una `str`.

Prova:

```python
print(type(dato))
```

Domanda:

> Se voglio fare `12 + 1`, che cosa devo cambiare?

---

# Convertire quando serve

```python
numero = int(input())
```

Succede:

```text
input()      → "12"
int("12")    → 12
numero       → 12
```

Poi:

```python
print(numero + 1)
```

produce `13`.

---

# Conversione impossibile

Che cosa succede?

```python
int("ciao")
```

La sintassi è valida.

Ma `"ciao"` non rappresenta un intero.

Quindi Python segnala un errore.

Errore ≠ fallimento personale.

Errore = informazione sul programma e sui dati.

---

# Dal REPL a `main.py`

Il REPL è ottimo per esperimenti.

Un programma che vuoi conservare va in un file:

```python
nome = input()
print(nome)
```

Salvalo come:

```text
main.py
```

Poi eseguilo nel Classroom Environment TheBitLab.

---

# Trace: non eseguire ancora

```python
primo = 4
secondo = 6
risultato = primo + secondo
print(risultato)
```

Completa mentalmente:

| passo | primo | secondo | risultato | output |
|---|---:|---:|---:|---|
| 1 | 4 | — | — | — |
| 2 | 4 | 6 | — | — |
| 3 | 4 | 6 | ? | — |
| 4 | 4 | 6 | ? | ? |

Poi prova davvero.

---

# Worked example: somma

```python
primo = int(input())
secondo = int(input())
risultato = primo + secondo
print(risultato)
```

Testiamo prima sulla carta:

| primo | secondo | atteso |
|---:|---:|---:|
| 2 | 3 | 5 |
| 0 | 0 | 0 |
| -4 | 10 | 6 |

Perché non basta provare soltanto `2 + 3`?

---

# Errore logico

Questo programma può terminare senza traceback:

```python
primo = int(input())
secondo = int(input())
risultato = primo - secondo
print(risultato)
```

Ma la specifica chiedeva una somma.

Quindi:

> **nessun errore Python ≠ programma corretto.**

Servono casi di test.

---

# Error Clinic

Che tipo di problema vedi?

### A

```python
print("ciao"
```

### B

```python
prezzo = 10
print(prezzo_totale)
```

### C

```python
numero = int("ciao")
```

### D

```python
risultato = primo - secondo
```

se dovevamo sommare.

---

# Leggere un traceback beginner

Per ora fai così:

1. guarda il **tipo di errore**;
2. leggi il messaggio;
3. individua la riga del tuo file;
4. chiediti cosa sta tentando di fare;
5. cambia una cosa alla volta;
6. riesegui il caso che falliva.

Non chiederti soltanto:

> “Come faccio a far sparire il messaggio?”

---

# Contratto di input/output

Nell'Activity la specifica dice:

> leggi due interi e stampa **soltanto** la somma.

Quindi:

```python
primo = int(input())
secondo = int(input())
print(primo + secondo)
```

è coerente.

Prompt e testo extra sono utili in altri programmi, ma qui cambierebbero l'output richiesto.

---

# Handoff al laboratorio

Activity B:

**Completa la somma**  
`py2-activity-b-input-somma-001`

Workflow:

```text
prevedi
→ apri starter
→ modifica solo il calcolo
→ salva
→ esegui/testa
→ leggi il report
→ spiega perché funziona
```

Tre casi: positivi, zeri, negativo+positivo.

---

# Checkpoint

Senza eseguire Python:

1. Che tipo restituisce `input()`?
2. Differenza tra `42` e `"42"`?
3. Perché usiamo `int(input())`?
4. Perché il REPL e uno script mostrano diversamente `2 + 3`?
5. Un programma senza traceback è sicuramente corretto?
6. Perché proviamo più di un input?

---

# Recap

```text
algoritmo → Python
```

```text
REPL = esperimenti
script = programma salvato
```

```text
input() → str
```

```text
tipo giusto → operazione giusta
```

```text
prevedi → esegui → confronta → correggi
```

Prossimo modulo: **espressioni, operatori e prime funzioni**.
