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

# M05 era una preview. M13 formalizza.

In M05 hai già visto una piccola funzione.

Ora devi capire con precisione:

```text
definizione / chiamata
parametro / argomento
return / print
valore al chiamante
casi di test
```

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

# GUIDED EXPOSURE — predicate

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

Non è necessario padroneggiare i predicate per passare a M14.

---

# GUIDED EXPOSURE — senza `return` esplicito

```python
def saluta(nome):
    print("Ciao", nome)
```

La funzione restituisce `None`.

Se serve un valore utilizzabile, rendilo esplicito con `return`.

`None` qui serve soprattutto a capire un `return` dimenticato.

---

# Codice dopo `return`

```python
def doppio(x):
    return x * 2
    print("fine")
```

Dopo `return` la chiamata termina.

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
- C: implementa funzione;
- D: debug.

P2 è un problema di delivery TheBitLab, non un concetto da studente.

---

# Minimum mastery checkpoint

Sai:

1. definizione vs chiamata?;
2. parametro vs argomento?;
3. `return` vs `print`?;
4. dove va il valore restituito?;
5. usare il return in un'altra espressione?;
6. fare un call trace?;
7. proporre tre casi per una funzione?.

`None`, predicate e tuple preview non fanno parte del gate ordinario.

---

# Recap

```text
funzione = responsabilità nominata
```

```text
argomenti → parametri → corpo → return
```

Prossimo modulo: scope locale e composizione. Da M14 entrerà anche `status/diff` Git G1 come osservazione del refactoring.
