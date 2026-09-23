# M13 — Funzioni produttive: parametri, argomenti e `return`

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Le funzioni formalizzano la trasformazione nominata introdotta in M05: parametri in ingresso e risultato restituito.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Scrivere programmi con input, selezioni e cicli e riconoscere la prima funzione pura di M05.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
definire e chiamare una funzione;<br>distinguere il nome di una funzione dalla sua chiamata;<br>distinguere parametro e argomento; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Stampare un valore lo mostra; restituirlo permette al chiamante di usarlo in altri calcoli. Riprendi <a href="12_CICLI_ANNIDATI_GRIGLIE_COSTO_LAVORO.md">M12 — Cicli annidati, griglie e costo del lavoro</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md">M14 — Scope locale, passaggio dei dati e composizione</a>. Ogni chiamata ha il proprio contesto locale e collabora con altre funzioni attraverso valori espliciti.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Segui la chiamata di area_rettangolo indicando argomenti, parametri e valore restituito; verifica più coppie di misure.
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
  <li>definire e chiamare una funzione;</li>
  <li>distinguere il nome di una funzione dalla sua chiamata;</li>
  <li>distinguere parametro e argomento;</li>
  <li>usare uno o più parametri semplici;</li>
  <li>restituire un valore con <code>return</code>;</li>
  <li>usare il valore restituito in un assegnamento o in un'altra espressione;</li>
  <li>distinguere una funzione che calcola da una funzione che stampa;</li>
  <li>sapere che una funzione senza <code>return</code> esplicito restituisce <code>None</code>;</li>
  <li>scrivere predicate semplici che restituiscono <code>bool</code>;</li>
  <li>verificare una funzione con più casi di test.</li>
</ul>

---

## 1. Dal blocco monolitico a una trasformazione nominata

<p align="justify">Finora possiamo già scrivere programmi con input, selezioni e cicli.</p>

<p align="justify">Il rischio è produrre un unico blocco crescente di codice.</p>

<p align="justify">Una funzione ci permette di dare un nome a una responsabilità:</p>

```python
def area_rettangolo(base, altezza):
    return base * altezza
```

<p align="justify">Il punto non è soltanto evitare righe duplicate.</p>

<p align="justify">Il punto è poter dire:</p>

<blockquote>
<p align="justify">questa parte del programma calcola l'area di un rettangolo.</p>
</blockquote>

---

## 2. Definizione e chiamata non sono la stessa cosa

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — definizione e chiamata di funzione:</strong>
La definizione di una funzione ne stabilisce nome, parametri e corpo. La chiamata ne esegue il comportamento con argomenti concreti.
</p>
</td>
</tr>
</table>

<p align="justify">Definizione:</p>

```python
def doppio(numero):
    return numero * 2
```

<p align="justify">Chiamata:</p>

```python
doppio(5)
```

<p align="justify">La definizione descrive il comportamento. La chiamata lo usa con dati concreti.</p>

<p align="justify">Il nome <code>doppio</code> e l'espressione <code>doppio(5)</code> non sono la stessa cosa.</p>

---

## 3. Parametro e argomento

```python
def doppio(numero):
    return numero * 2
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — parametro:</strong>
Un <strong>parametro</strong> è un nome dichiarato nella definizione di una funzione per ricevere un dato alla chiamata. Nell'esempio il parametro è <code>numero</code>.
</p>
</td>
</tr>
</table>

<p align="justify">Nella chiamata:</p>

```python
doppio(7)
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — argomento:</strong>
Un <strong>argomento</strong> è un valore fornito a una chiamata di funzione. Nell'esempio l'argomento è <code>7</code>.
</p>
</td>
</tr>
</table>

<p align="justify">Modello:</p>

```text
argomento concreto
      ↓
parametro locale
      ↓
corpo funzione
```

---

## 4. Modello della chiamata

<p align="justify">Per:</p>

```python
def somma(a, b):
    return a + b

risultato = somma(2, 3)
```

<p align="justify">possiamo pensare:</p>

```text
2 → a
3 → b
corpo → a + b
return → 5
5 → punto della chiamata
risultato → 5
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — return:</strong>
<code>return</code> restituisce un valore al chiamante.
</p>
</td>
</tr>
</table>

---

## 5. `print` non è `return`

<p align="justify">Confronta.</p>

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

<p align="justify">La versione A produce output. La versione B produce un valore utilizzabile dal programma.</p>

<p align="justify">Con B possiamo fare:</p>

```python
x = somma(2, 3)
print(x * 10)
```

<p align="justify">La domanda non è “<code>print</code> è sbagliato?”.</p>

<p align="justify">La domanda è:</p>

<blockquote>
<p align="justify">qual è la responsabilità di questa funzione?</p>
</blockquote>

<p align="justify">Se deve <strong>calcolare</strong>, <code>return</code> è il risultato naturale.</p>

---

## 6. Separare calcolo e presentazione

<p align="justify">Preferiamo spesso:</p>

```python
def area_rettangolo(base, altezza):
    return base * altezza

area = area_rettangolo(3, 4)
print(area)
```

<p align="justify">rispetto a:</p>

```python
def area_rettangolo(base, altezza):
    print(base * altezza)
```

<p align="justify">La prima forma:</p>

<ul>
  <li>rende il calcolo riutilizzabile;</li>
  <li>rende il test più semplice;</li>
  <li>separa logica e interfaccia.</li>
</ul>

---

## 7. Più parametri

```python
def costo(prezzo_unitario, quantita):
    return prezzo_unitario * quantita
```

<p align="justify">Chiamata:</p>

```python
totale = costo(12, 3)
```

<p align="justify">Trace:</p>

```text
prezzo_unitario → 12
quantita        → 3
return          → 36
```

<p align="justify">L'ordine degli argomenti posizionali deve rispettare il contratto della funzione.</p>

---

## 8. Predicate: funzioni che rispondono sì/no

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — funzione predicato:</strong>
Una funzione predicato risponde a una domanda restituendo un booleano. Il suo risultato può essere usato come condizione.
</p>
</td>
</tr>
</table>

<p align="justify">Dopo aver studiato le condizioni, possiamo dare un nome a una domanda booleana:</p>

```python
def eta_valida(eta):
    return 0 <= eta <= 120
```

<p align="justify">Poi:</p>

```python
if eta_valida(eta):
    ...
```

<p align="justify">Un buon nome rende leggibile la decisione.</p>

---

## 9. Funzione senza `return` esplicito

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — None:</strong>
<code>None</code> è il valore usato in Python per rappresentare l'assenza di un valore significativo. Una funzione che termina senza restituire esplicitamente un valore restituisce <code>None</code>.
</p>
</td>
</tr>
</table>

```python
def saluta(nome):
    print("Ciao", nome)
```

<p align="justify">La funzione produce output, ma non contiene un <code>return</code> esplicito.</p>

<p align="justify">Python restituisce comunque:</p>

```python
None
```

<p align="justify">A livello beginner basta ricordare:</p>

<blockquote>
<p align="justify">se una funzione deve produrre un valore utilizzabile, rendilo esplicito con <code>return</code>.</p>
</blockquote>

---

## 10. Codice dopo `return`

```python
def doppio(x):
    return x * 2
    print("fine")
```

<p align="justify">Quando viene eseguito <code>return</code>, la chiamata della funzione termina.</p>

<p align="justify">Il <code>print</code> successivo non viene raggiunto.</p>

<p align="justify">Questo è un buon caso di Error Clinic.</p>

---

## 11. Worked example: quoziente e resto

```python
def quoziente_resto(totale, gruppo):
    quoziente = totale // gruppo
    resto = totale % gruppo
    return quoziente, resto
```

<p align="justify">Per ora il ritorno multiplo viene mostrato come tuple/unpacking <strong>solo come preview controllata</strong> se la classe è pronta.</p>

<p align="justify">Versione core più semplice:</p>

```python
def resto_divisione(totale, gruppo):
    return totale % gruppo
```

<p align="justify">Non anticipiamo tuple se distraggono dall'obiettivo <code>return</code>.</p>

---

## 12. Testare una funzione

<p align="justify">Prima del framework di testing possiamo già progettare casi:</p>

```python
def doppio(x):
    return x * 2
```

<p align="justify">Casi:</p>

<table align="center">
<thead>
<tr>
<th>input</th>
<th>atteso</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>-2</td>
<td>-4</td>
</tr>
</tbody>
</table>

<p align="justify">Poi verifichiamo:</p>

```python
print(doppio(3))
print(doppio(0))
print(doppio(-2))
```

<p align="justify">In M16 passeremo agli <code>assert</code>.</p>

---

## 13. Call trace

```python
def differenza(a, b):
    return a - b

x = differenza(10, 4)
y = differenza(x, 3)
```

<p align="justify">Completa:</p>

<table align="center">
<thead>
<tr>
<th>chiamata</th>
<th><code>a</code></th>
<th><code>b</code></th>
<th>return</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>differenza(10, 4)</code></td>
<td>10</td>
<td>4</td>
<td>?</td>
</tr>
<tr>
<td><code>differenza(x, 3)</code></td>
<td>?</td>
<td>3</td>
<td>?</td>
</tr>
</tbody>
</table>

<p align="justify">Il trace delle chiamate prepara il call graph di M14/M15.</p>

---

## 14. Error Clinic

## A — chiamata dimenticata

```python
x = doppio
```

<p align="justify">vs:</p>

```python
x = doppio(5)
```

<p align="justify">Non approfondiamo ancora le funzioni come oggetti; qui basta riconoscere che manca la chiamata richiesta.</p>

## B — `return` mancante

```python
def doppio(x):
    risultato = x * 2
```

<p align="justify">Il valore viene calcolato ma non restituito.</p>

## C — stampa al posto di risultato

<p align="justify">Una funzione che dovrebbe essere usata in un calcolo stampa invece di restituire.</p>

## D — parametro errato

<p align="justify">Il corpo usa un nome diverso dal parametro definito.</p>

## E — codice dopo `return`

<p align="justify">Codice non raggiungibile nella normale esecuzione di quel ramo.</p>

---

## 15. Activity candidate

## A — Call trace

<p align="justify">Completa parametro/argomento/return per più chiamate.</p>

## B — Controlled Change

<p align="justify">Trasforma una funzione che stampa in una funzione che restituisce e aggiorna il chiamante.</p>

<p align="justify">Per certificare il nuovo profilo P2 è materializzato <strong>un solo canarino controllato</strong>:</p>

```text
py2-activity-b-return-area-001
```

<p align="justify">Lo starter calcola e stampa correttamente l'area ma restituisce implicitamente <code>None</code>; la modifica richiesta sostituisce la stampa con <code>return</code>. Il canarino serve a provare che il grading distingue davvero output e valore restituito.</p>

<p align="justify">Il profilo <code>python-function-v1</code> è attualmente validato come <strong>release candidate TheBitLab 2026.08.1</strong>, ma non viene ancora usato per generare in massa Activity: il lock immutabile stabile deve essere pubblicato prima della promozione.</p>

## C — Implement

<p align="justify">Scrivi funzioni numeriche o predicate con almeno tre casi dichiarati prima del codice.</p>

## D — Debug

<p align="justify">Correggi <code>return</code> mancante, valore ignorato, parametro sbagliato e codice irraggiungibile.</p>

---

## 16. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li>definizione vs chiamata;</li>
  <li>parametro vs argomento;</li>
  <li><code>return</code> vs <code>print</code>;</li>
  <li>dove finisce il valore restituito;</li>
  <li>che cosa accade senza <code>return</code> esplicito;</li>
  <li>perché un predicate che restituisce <code>bool</code> può migliorare la leggibilità;</li>
  <li>come verificare una funzione su più input.</li>
</ol>

---

## 17. Sintesi

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

<p align="justify">Nel prossimo modulo studieremo dove vivono i nomi locali e come far collaborare funzioni passando i dati in modo esplicito.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale del corso, progettato con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — definizione/chiamata di funzioni e <code>return</code>;</li>
  <li><em>Think Python / Pensare in Python</em> — funzioni e modello beginner;</li>
  <li><em>Learning Python / Imparare Python</em> — reference di funzioni e scope;</li>
  <li>TheBitLab <code>2cornot2c#756</code> — profilo P2 function-behavior in release candidate.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>
