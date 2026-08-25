---
marp: true
paginate: true
size: 16:9
title: M13 — Funzioni, parametri e return
---

# M13 — Funzioni produttive
## Parametri, argomenti e `return`

PY2-05 — Funzioni, decomposizione e testing

---

# Perché una funzione?

Non solo per evitare righe duplicate.

Una funzione dà un nome a una responsabilità:

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

---

# Definizione vs chiamata

Definizione:

```python
def doppio(numero):
    return numero * 2
```

Chiamata:

```python
doppio(5)
```

---

# Parametro vs argomento

```python
def doppio(numero):
```

`numero` = parametro.

```python
doppio(7)
```

`7` = argomento.

---

# Modello della chiamata

```text
argomenti
→ parametri locali
→ corpo
→ return
→ valore al chiamante
```

---

# `return` non è `print`

```python
def somma(a, b):
    print(a + b)
```

vs

```python
def somma(a, b):
    return a + b
```

Quale posso usare dentro un altro calcolo?

---

# Separare calcolo e output

```python
def area(base, altezza):
    return base * altezza

risultato = area(3, 4)
print(risultato)
```

Logica e presentazione restano separate.

---

# Più parametri

```python
def costo(prezzo_unitario, quantita):
    return prezzo_unitario * quantita
```

Trace:

```text
12 → prezzo_unitario
3  → quantita
return → 36
```

---

# Predicate

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

Poi:

```python
if eta_valida(eta):
    ...
```

Una domanda booleana può avere un nome.

---

# Senza `return` esplicito

```python
def saluta(nome):
    print("Ciao", nome)
```

La funzione restituisce `None`.

Se serve un valore utilizzabile, rendilo esplicito.

---

# Codice dopo `return`

```python
def doppio(x):
    return x * 2
    print("fine")
```

Dopo `return` la chiamata termina.

---

# Call trace

```python
def differenza(a, b):
    return a - b

x = differenza(10, 4)
y = differenza(x, 3)
```

Completa parametri e return delle due chiamate.

---

# Testare senza framework

```python
def doppio(x):
    return x * 2
```

Casi:

```text
3  → 6
0  → 0
-2 → -4
```

Prima i casi, poi l'esecuzione.

---

# Error Clinic

- chiamata mancante;
- `return` mancante;
- `print` al posto del risultato;
- parametro con nome errato;
- codice dopo `return`.

---

# Activity candidate

- A: call trace;
- B: `print` → `return`;
- C: implementa funzione/predicate;
- D: debug.

P2 verrà materializzato solo quando `2cornot2c#756` è certificato.

---

# Checkpoint

Sai spiegare:

1. definizione vs chiamata?
2. parametro vs argomento?
3. `return` vs `print`?
4. dove va il valore restituito?
5. che cosa succede senza `return`?
6. perché un predicate è utile?

---

# Recap

```text
funzione = responsabilità nominata
```

```text
argomenti → parametri → corpo → return
```

Prossimo modulo: scope locale e composizione.
