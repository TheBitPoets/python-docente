# M20 — Liste: mutabilità, metodi essenziali e iterazione

> **Stato:** draft editoriale controllato  
> **UDA:** PY2-07 — Liste, tuple e dati tabellari  
> **Baseline:** Python 3.12-compatible

## Obiettivi

Alla fine del modulo dovresti saper:

- creare una `list`;
- usare `len()`, indici positivi/negativi e slicing;
- modificare un elemento per indice;
- usare `append`, `extend`, `insert`, `remove`, `pop` con semantica corretta;
- distinguere metodi che modificano la lista da operazioni che producono un nuovo valore;
- evitare il bug `lista = lista.append(...)`;
- iterare direttamente sugli elementi;
- usare indice quando la posizione serve davvero;
- usare `enumerate()` quando servono indice e valore;
- verificare membership con `in`;
- spiegare la differenza fondamentale tra `str` immutabile e `list` mutabile.

---

# 1. Da `str` a `list`

Con una stringa:

```python
testo = "ciao"
```

non puoi fare:

```python
testo[0] = "C"
```

Con una lista:

```python
numeri = [10, 20, 30]
numeri[0] = 99
```

la struttura cambia:

```text
[99, 20, 30]
```

La mutabilità è il nuovo modello mentale dell'UDA.

---

# 2. Creazione e accesso

```python
numeri = [12, 45, 7]
```

```python
len(numeri)
numeri[0]
numeri[-1]
numeri[1:3]
```

Indici e slicing riusano il modello imparato sulle stringhe.

Differenza importante: la lista può essere modificata.

---

# 3. Modifica per indice

```python
numeri = [10, 20, 30]
numeri[1] = 25
```

Ora:

```text
[10, 25, 30]
```

Non è stata creata automaticamente una nuova lista: abbiamo mutato l'oggetto esistente.

---

# 4. `append()`

```python
numeri = [10, 20]
numeri.append(30)
```

Risultato:

```text
[10, 20, 30]
```

`append()` aggiunge **un elemento** in fondo.

---

# 5. Bug fondamentale: metodo mutante + assegnamento

Questo è sbagliato:

```python
numeri = [10, 20]
numeri = numeri.append(30)
```

`append()` modifica la lista e restituisce `None`.

Dopo l'assegnamento:

```text
numeri → None
```

Questo stesso modello tornerà con `sort()`.

---

# 6. `append()` vs `extend()`

```python
x = [1, 2]
x.append([3, 4])
```

produce:

```text
[1, 2, [3, 4]]
```

Invece:

```python
x = [1, 2]
x.extend([3, 4])
```

produce:

```text
[1, 2, 3, 4]
```

Domanda:

> voglio aggiungere **un elemento** che è una lista oppure incorporare **più elementi**?

---

# 7. `insert()`

```python
nomi = ["Anna", "Carlo"]
nomi.insert(1, "Bruno")
```

Usalo quando la posizione è davvero parte del requisito.

Non scegliere `insert()` solo perché esiste.

---

# 8. `remove()` vs `pop()`

```python
valori.remove(7)
```

rimuove la prima occorrenza del **valore** `7`.

```python
ultimo = valori.pop()
```

rimuove e restituisce l'ultimo elemento.

```python
x = valori.pop(2)
```

rimuove e restituisce l'elemento in **posizione** 2.

Valore e posizione non sono la stessa cosa.

---

# 9. Iterazione diretta

Se serve soltanto il valore:

```python
for numero in numeri:
    print(numero)
```

È la forma naturale per molte scansioni.

---

# 10. Iterazione per indice

Se la posizione serve al problema:

```python
for i in range(len(numeri)):
    print(i, numeri[i])
```

Non usare l'indice come rituale.

---

# 11. `enumerate()`

Quando servono insieme indice e valore:

```python
for i, numero in enumerate(numeri):
    print(i, numero)
```

Ora possiamo rileggere `i, numero` come unpacking di una coppia prodotta dall'iterazione.

---

# 12. Membership

```python
7 in numeri
```

restituisce un booleano.

Il modello è identico alla membership nelle stringhe, ma ora gli elementi possono essere valori di tipi diversi secondo il contratto della lista.

---

# 13. Slicing di una lista

```python
prima_parte = numeri[:3]
```

produce una nuova lista superficiale con gli elementi selezionati.

Nel prossimo modulo distingueremo in dettaglio:

```text
alias
vs
copia
```

---

# 14. Worked example: raccolta di N valori

```python
n = int(input())
valori = []

for _ in range(n):
    valori.append(int(input()))
```

Ora i dati rimangono disponibili per più elaborazioni successive.

Questo è diverso da elaborare ogni valore e dimenticarlo subito.

---

# 15. Error Clinic

- `lista = lista.append(x)`;
- `append([a, b])` quando serviva `extend([a, b])`;
- `remove(indice)` pensando che rimuova per posizione;
- indice fuori range;
- iterazione per indice quando la posizione non serve;
- modifica dell'elemento sbagliato.

---

# 16. Confronto da `friedpython`

Gli esercizi legacy 1 e 2 mostrano bene lo stesso attraversamento con:

```text
while + indice
vs
for diretto sugli elementi
```

Nel corso 2026/27 li trattiamo come **confronto di intenzione**, non come due sintassi equivalenti da memorizzare.

Se la posizione non serve, il `for` diretto comunica meglio il problema.

---

# 17. Activity candidate

- **A — Predict mutation:** prevedi lista e return dopo operazioni;
- **B — Controlled Change:** scegli `append/extend/insert/remove/pop` da una specifica;
- **C — Implement:** costruisci una lista da N input e calcola proprietà già note;
- **D — Debug:** metodo mutante assegnato, indice, remove/pop, append/extend.

Nessuna nuova Activity autogradata viene materializzata finché il profilo richiesto non è certificato.

---

# 18. Checkpoint

Sai spiegare:

1. `str` immutabile vs `list` mutabile;
2. `append` vs `extend`;
3. `remove` vs `pop`;
4. perché `lista = lista.append(x)` è un bug;
5. valore vs indice;
6. `for` diretto vs indice vs `enumerate`.

---

# 19. Sintesi

```text
list = sequenza ordinata mutabile
```

```text
metodo mutante
→ cambia l'oggetto
→ spesso restituisce None
```

```text
solo valore → for diretto
indice+valore → enumerate
```

Nel prossimo modulo vedremo che due nomi possono riferirsi **alla stessa lista**: alias, copie e mutazioni diventano quindi fondamentali.

---

# Fonti e riferimenti docente

Materiale originale, con riferimento a:

- documentazione Python 3.12 sulle liste;
- *Think Python / Pensare in Python* — lists/mutability;
- *Learning Python / Imparare Python* — list object coverage;
- `friedpython@cb3f3dc...` auditato in `sources/FRIEDPYTHON_LISTS_TUPLES_AUDIT.md`.
