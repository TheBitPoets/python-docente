# M14 — Scope locale, passaggio dei dati e composizione

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Ogni chiamata ha il proprio contesto locale e collabora con altre funzioni attraverso valori espliciti.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Definire e chiamare funzioni con parametri e return come in M13.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
capire che parametri e variabili definite dentro una funzione sono locali a quella chiamata;<br>distinguere un nome locale da un nome definito fuori dalla funzione;<br>passare esplicitamente alla funzione i dati di cui ha bisogno; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Il parametro è un nome locale della chiamata, mentre l&#x27;argomento è il valore fornito dal chiamante. Riprendi <a href="13_FUNZIONI_PARAMETRI_RETURN.md">M13 — Funzioni produttive: parametri, argomenti e <code>return</code></a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="15_PROGETTAZIONE_TOP_DOWN_RESPONSABILITA.md">M15 — Progettazione top-down e responsabilità</a>. La progettazione top-down divide una specifica in responsabilità e contratti di funzione controllabili.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Traccia due chiamate della stessa funzione e poi il flusso di dati del calcolo del prezzo finale.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128279;</span> Rimando:</strong>
<a href="../../student/README.md">Indice del percorso studente</a>; <a href="#obiettivi">obiettivi della lezione</a>.
</p>

</details>
</td></tr>
</table>
<!-- COURSE-FRAME:END -->

<blockquote>
<p align="justify"><strong>Stato:</strong> draft editoriale controllato<br>
<strong>UDA:</strong> PY2-05 — Funzioni, decomposizione e testing<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>capire che parametri e variabili definite dentro una funzione sono locali a quella chiamata;</li>
  <li>distinguere un nome locale da un nome definito fuori dalla funzione;</li>
  <li>passare esplicitamente alla funzione i dati di cui ha bisogno;</li>
  <li>evitare variabili globali come scorciatoia per i dati di lavoro;</li>
  <li>usare il risultato di una funzione come input di un'altra;</li>
  <li>far collaborare più funzioni tramite valori espliciti;</li>
  <li>leggere un piccolo call graph;</li>
  <li>seguire il flusso dei dati tra chiamate;</li>
  <li>riconoscere una dipendenza nascosta da stato globale;</li>
  <li>usare variabili intermedie quando rendono più chiaro il flusso.</li>
</ul>

---

## 1. Una chiamata crea il proprio contesto locale

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — contesto locale:</strong>
Ogni chiamata di funzione ha il proprio contesto locale: i parametri e le variabili locali appartengono a quella chiamata. Lo <strong>scope</strong> di un nome è l'ambito in cui quel nome può essere usato.
</p>
</td>
</tr>
</table>

```python
def doppio(numero):
    risultato = numero * 2
    return risultato
```

<p align="justify">Dentro la funzione esistono i nomi:</p>

```text
numero
risultato
```

<p align="justify">Questi nomi servono alla chiamata della funzione.</p>

<p align="justify">Modello beginner:</p>

```text
chiamata
→ parametri locali
→ variabili locali
→ return
→ fine della chiamata
```

<p align="justify">Non serve ancora studiare formalmente la regola LEGB.</p>

---

## 2. Variabile locale fuori dalla funzione

```python
def doppio(numero):
    risultato = numero * 2
    return risultato

print(risultato)
```

<p align="justify">La variabile <code>risultato</code> è stata definita dentro la funzione.</p>

<p align="justify">Il codice esterno non può usarla come se fosse un proprio nome locale/globale già disponibile.</p>

<p align="justify">La funzione comunica verso l'esterno attraverso <code>return</code>.</p>

---

## 3. Passare esplicitamente ciò che serve

<p align="justify">Se una funzione deve usare un prezzo e una quantità:</p>

```python
def costo(prezzo, quantita):
    return prezzo * quantita
```

<p align="justify">Il contratto è visibile nella firma.</p>

<p align="justify">Chi legge sa quali dati servono.</p>

---

## 4. Dipendenza globale nascosta

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — nome globale e dipendenza globale:</strong>
Un nome definito al livello del modulo è globale rispetto alle funzioni del modulo. Una funzione ha una dipendenza globale quando usa un dato esterno alla chiamata invece di riceverlo esplicitamente.
</p>
</td>
</tr>
</table>

<p align="justify">Confronta:</p>

```python
prezzo = 10

def costo(quantita):
    return prezzo * quantita
```

<p align="justify">con:</p>

```python
def costo(prezzo, quantita):
    return prezzo * quantita
```

<p align="justify">La prima funzione dipende da un dato esterno che non compare nella firma.</p>

<p align="justify">La seconda rende la dipendenza esplicita.</p>

<p align="justify">Questo la rende più semplice da:</p>

<ul>
  <li>capire;</li>
  <li>provare con valori diversi;</li>
  <li>testare;</li>
  <li>riusare.</li>
</ul>

---

## 5. Non è un dogma contro ogni nome globale

<p align="justify">Una costante di configurazione/dominio può avere senso:</p>

```python
IVA_PERCENTUALE = 22
```

<p align="justify">ma i dati di lavoro che cambiano da chiamata a chiamata sono spesso meglio passati esplicitamente.</p>

<p align="justify">La domanda è:</p>

<blockquote>
<p align="justify">questa dipendenza è parte chiara del contratto o è nascosta?</p>
</blockquote>

---

## 6. Comporre funzioni

```python
def area_rettangolo(base, altezza):
    return base * altezza


def costo_pittura(area, costo_mq):
    return area * costo_mq
```

<p align="justify">Uso:</p>

```python
area = area_rettangolo(3, 4)
costo = costo_pittura(area, 8)
print(costo)
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — composizione di funzioni:</strong>
La composizione di funzioni usa il risultato di una funzione come dato di ingresso di un'altra.
</p>
</td>
</tr>
</table>

---

## 7. Variabili intermedie rendono visibile il flusso

<p align="justify">Possiamo scrivere:</p>

```python
costo = costo_pittura(area_rettangolo(3, 4), 8)
```

<p align="justify">ma per un beginner spesso è più leggibile:</p>

```python
area = area_rettangolo(3, 4)
costo = costo_pittura(area, 8)
```

<p align="justify">La forma più corta non è automaticamente la migliore.</p>

---

## 8. Call graph introduttivo

<p align="justify">Per:</p>

```text
main
├─ area_rettangolo
└─ costo_pittura
```

<p align="justify">oppure:</p>

```text
main
→ area_rettangolo
→ costo_pittura
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — call graph:</strong>
Un call graph è uno schema che rappresenta quali funzioni chiamano quali altre.
</p>
</td>
</tr>
</table>

<p align="justify">Non serve ancora un tool speciale: basta uno schema leggibile.</p>

---

## 9. Flusso dei dati

<p align="justify">Esempio:</p>

```text
base, altezza
      ↓
area_rettangolo
      ↓
area
      ↓
costo_pittura + costo_mq
      ↓
costo
```

<p align="justify">Questa vista prepara il design top-down di M15.</p>

---

## 10. Due chiamate, due contesti locali

```python
def doppio(numero):
    risultato = numero * 2
    return risultato

x = doppio(3)
y = doppio(10)
```

<p align="justify">Le due chiamate usano valori diversi per <code>numero</code> e <code>risultato</code>.</p>

<p align="justify">Non esiste un unico <code>numero</code> locale condiviso tra tutte le chiamate.</p>

---

## 11. Worked example: prezzo finale

```python
def applica_sconto(prezzo, percentuale):
    sconto = prezzo * percentuale / 100
    return prezzo - sconto


def aggiungi_spedizione(prezzo, spedizione):
    return prezzo + spedizione
```

<p align="justify">Uso:</p>

```python
scontato = applica_sconto(100, 20)
finale = aggiungi_spedizione(scontato, 5)
print(finale)
```

<p align="justify">Ogni funzione ha una responsabilità e riceve i dati necessari.</p>

---

## 12. Error Clinic

## A — locale usata fuori

```python
def f(x):
    y = x + 1
    return y

print(y)
```

## B — dato globale nascosto

<p align="justify">La funzione usa una variabile esterna modificabile invece di riceverla.</p>

## C — risultato ignorato

```python
applica_sconto(100, 20)
print(100)
```

<p align="justify">Il valore restituito non viene usato.</p>

## D — parametro mancante

<p align="justify">La funzione richiede due dati ma il chiamante ne passa uno.</p>

## E — composizione troppo compressa

<p align="justify">Una lunga espressione annidata rende difficile seguire il flusso. Introdurre variabili intermedie può migliorare la leggibilità.</p>

---

## 13. Activity candidate

## A — Scope trace

<p align="justify">Segna per ogni nome dove nasce e dove può essere usato.</p>

## B — Remove global

<p align="justify">Trasforma una funzione dipendente da stato globale in una funzione con parametri/return espliciti.</p>

## C — Compose

<p align="justify">Costruisci 2–3 funzioni che collaborano su un piccolo calcolo.</p>

## D — Debug

<p align="justify">Correggi locale usata fuori, globale nascosta, parametro mancante o return ignorato.</p>

<p align="justify">Nessuna Activity P2 viene materializzata finché il profilo <code>2cornot2c#756</code> non è certificato.</p>

---

## 14. Git G1: osservare il cambiamento

<p align="justify">Da questa fase del corso Git può iniziare a entrare come workflow trasversale:</p>

```text
git status
→ quali file sono cambiati?

git diff
→ quali righe ho cambiato e perché?
```

<p align="justify">Il focus non è ancora il corso Git completo.</p>

<p align="justify">Usiamo Git per osservare un refactoring o una rimozione di dipendenza globale.</p>

---

## 15. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>che cosa significa variabile locale;</li>
  <li>perché una funzione dovrebbe ricevere esplicitamente i dati che usa;</li>
  <li>perché una globale può nascondere una dipendenza;</li>
  <li>come il <code>return</code> di una funzione alimenta un'altra;</li>
  <li>perché una variabile intermedia può migliorare la leggibilità;</li>
  <li>che cosa rappresenta un piccolo call graph.</li>
</ol>

---

## 16. Sintesi

```text
funzione
→ riceve dati espliciti
→ usa nomi locali
→ produce un risultato
```

```text
return di A
→ input di B
```

```text
dipendenze esplicite
→ codice più comprensibile e testabile
```

<p align="justify">Nel prossimo modulo useremo queste idee per progettare un programma dall'alto verso il basso, prima di implementarne tutti i dettagli.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale del corso, progettato con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — funzioni e naming/scope di base;</li>
  <li><em>Think Python / Pensare in Python</em> — funzioni e composizione;</li>
  <li><em>Learning Python / Imparare Python</em> — scope e funzioni come reference;</li>
  <li>TheBitLab <code>2cornot2c#756</code> — futuro grading function-behavior.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>
