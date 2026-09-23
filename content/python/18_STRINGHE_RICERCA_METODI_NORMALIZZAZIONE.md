# M18 — Ricerca, membership, metodi e normalizzazione delle stringhe

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Ricerca e normalizzazione scelgono metodi coerenti con la domanda posta sul testo.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Leggere indici e slice e spiegare l&#x27;immutabilità di str da M17.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
usare <code>in</code> e <code>not in</code>;<br>usare <code>find()</code> quando serve una posizione e interpretare correttamente <code>-1</code>;<br>usare <code>count()</code> quando coincide con il requisito; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Una posizione, un booleano e un conteggio rispondono a domande diverse. Riprendi <a href="17_STRINGHE_INDICI_SLICING_IMMUTABILITA.md">M17 — Stringhe: indici, slicing e immutabilità</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="19_ALGORITMI_TESTO_PARSING_SEMPLICE.md">M19 — Algoritmi su testo e parsing semplice</a>. Algoritmi sul testo combinano cicli, condizioni e funzioni con una politica di normalizzazione dichiarata.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Confronta in e find con un match all&#x27;indice zero e con un testo assente; traccia poi strip e lower.
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
<strong>UDA:</strong> PY2-06 — Stringhe come sequenze e testo<br>
<strong>Baseline:</strong> Python 3.12-compatible</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>usare <code>in</code> e <code>not in</code>;</li>
  <li>usare <code>find()</code> quando serve una posizione e interpretare correttamente <code>-1</code>;</li>
  <li>usare <code>count()</code> quando coincide con il requisito;</li>
  <li>usare <code>lower()</code>, <code>upper()</code>, <code>strip()</code>, <code>replace()</code>, <code>startswith()</code> e <code>endswith()</code>;</li>
  <li>capire che i metodi di <code>str</code> restituiscono nuove stringhe;</li>
  <li>scegliere tra metodo built-in e loop esplicito;</li>
  <li>normalizzare testo in modo consapevole;</li>
  <li>riconoscere alcuni errori tipici nell'uso di <code>find()</code> e <code>strip()</code>.</li>
</ul>

---

## 1. La domanda viene prima del metodo

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">La stringa contiene il carattere <code>@</code>?</p>
</blockquote>

<p align="justify">Se serve soltanto una risposta sì/no:</p>

```python
if "@" in email:
    ...
```

<p align="justify">comunica direttamente l'intenzione.</p>

---

## 2. `in` e `not in`

```python
"py" in "python"      # True
"java" in "python"   # False
"x" not in "python"  # True
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — membership — in e not in:</strong>
La membership verifica l'appartenenza. Nelle stringhe <code>parte in testo</code> è vero quando la sottostringa è presente; <code>not in</code> verifica la sua assenza. Il risultato è booleano, non una posizione.
</p>
</td>
</tr>
</table>

```text
esiste questa sottostringa?
```

<p align="justify">Non restituisce la posizione.</p>

---

## 3. `find()`

```python
posizione = testo.find("@")
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — find():</strong>
<code>find()</code> cerca una sottostringa e restituisce l'indice della prima occorrenza; restituisce <code>-1</code> se non la trova.
</p>
</td>
</tr>
</table>

<p align="justify">Se non viene trovata:</p>

```text
-1
```

<p align="justify">Quindi:</p>

```python
if testo.find("@") != -1:
    ...
```

<p align="justify">è possibile, ma se non serve la posizione <code>in</code> è spesso più leggibile.</p>

---

## 4. Errore classico: `find()` usato come booleano

<p align="justify">Questo è pericoloso:</p>

```python
if testo.find("a"):
    ...
```

<p align="justify">Perché:</p>

<ul>
  <li>se <code>a</code> è in posizione <code>0</code>, il risultato è <code>0</code>, che è falsy;</li>
  <li>se non c'è, il risultato è <code>-1</code>, che è truthy.</li>
</ul>

<p align="justify">Il codice comunica il contrario di ciò che molti beginner immaginano.</p>

---

## 5. `count()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — count():</strong>
<code>count()</code> restituisce il numero di occorrenze non sovrapposte della sottostringa cercata.
</p>
</td>
</tr>
</table>

```python
"banana".count("a")
```

<p align="justify">restituisce <code>3</code>.</p>

<p align="justify">Usalo quando il requisito è davvero:</p>

<blockquote>
<p align="justify">quante occorrenze secondo la semantica standard del metodo?</p>
</blockquote>

<p align="justify">Non riscrivere manualmente una scansione se l'obiettivo non è imparare quell'algoritmo.</p>

---

## 6. Trasformazioni restituiscono nuove stringhe

```python
testo = " Python "
nuovo = testo.strip()
```

<p align="justify"><code>testo</code> non viene modificato in posto.</p>

<p align="justify">La stringa è immutabile.</p>

<p align="justify">Errore tipico:</p>

```python
testo.lower()
print(testo)
```

<p align="justify">Se vuoi conservare il risultato:</p>

```python
testo = testo.lower()
```

<p align="justify">oppure usa una nuova variabile.</p>

---

## 7. `lower()` e `upper()`

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — lower() e upper():</strong>
<code>lower()</code> restituisce una nuova stringa con le lettere convertite in minuscolo; <code>upper()</code> le converte in maiuscolo. La stringa originale resta invariata.
</p>
</td>
</tr>
</table>

```python
nome.lower()
nome.upper()
```

<p align="justify">Utili per confronti/normalizzazioni semplici.</p>

<p align="justify">Esempio:</p>

```python
risposta = input().strip().lower()
if risposta == "si":
    ...
```

<p align="justify">La normalizzazione deve essere una scelta del requisito, non un automatismo.</p>

---

## 8. `strip()`

```python
"  ciao  ".strip()
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — strip():</strong>
<code>strip()</code>, senza argomenti, restituisce una nuova stringa rimuovendo i caratteri di spazio, tabulazione e ritorno a capo dai bordi. Non rimuove quelli interni.
</p>
</td>
</tr>
</table>

<p align="justify">Attenzione:</p>

```python
strip(chars)
```

<p align="justify">non significa “rimuovi esattamente questa sottostringa dai bordi”. Il parametro indica un insieme di caratteri da rimuovere alle estremità.</p>

---

## 9. Prefissi e suffissi

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — prefisso e suffisso:</strong>
Un prefisso è una parte iniziale del testo; un suffisso è una parte finale. <code>startswith()</code> e <code>endswith()</code> verificano rispettivamente se il testo inizia o termina con la parte indicata.
</p>
</td>
</tr>
</table>

```python
testo.startswith("http")
testo.endswith(".py")
```

<p align="justify">Quando il requisito parla di prefisso/suffisso, questi metodi esprimono bene l'intenzione.</p>

---

## 10. `replace()`

```python
nuovo = testo.replace("-", " ")
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — replace():</strong>
<code>replace()</code> restituisce una nuova stringa sostituendo le occorrenze indicate con un altro testo.
</p>
</td>
</tr>
</table>

<p align="justify">Domanda:</p>

<blockquote>
<p align="justify">voglio sostituire tutte le occorrenze secondo questa regola oppure sto cercando una trasformazione più specifica?</p>
</blockquote>

---

## 11. Metodo vs algoritmo manuale

<p align="justify">Per imparare un pattern:</p>

```python
def conta_vocali(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.lower() in "aeiou":
            conteggio += 1
    return conteggio
```

<p align="justify">Qui il loop è parte dell'obiettivo didattico.</p>

<p align="justify">Se il problema reale coincide con un metodo standard, il metodo può essere più diretto.</p>

---

## 12. Criterio di scelta

```text
capisco l'algoritmo
+
conosco gli strumenti standard
+
scelgo ciò che comunica meglio l'intenzione
```

<p align="justify">Non vale:</p>

```text
built-in sempre migliore
```

<p align="justify">né:</p>

```text
loop manuale sempre più didattico
```

<p align="justify">Dipende dall'outcome.</p>

---

## 13. Normalizzazione

<p align="justify">Pattern comune:</p>

```python
normalizzato = testo.strip().lower()
```

<p align="justify">Prima chiediti:</p>

<ul>
  <li>voglio ignorare spazi esterni?;</li>
  <li>voglio ignorare maiuscole/minuscole?;</li>
  <li>sto perdendo un'informazione che invece serviva?.</li>
</ul>

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — normalizzazione:</strong>
Normalizzare significa cambiare la rappresentazione per confrontarla/elaborarla in modo coerente.
</p>
</td>
</tr>
</table>

---

## 14. Worked example: risposta sì/no

```python
def risposta_affermativa(testo):
    normalizzato = testo.strip().lower()
    return normalizzato == "si"
```

<p align="justify">Casi:</p>

```text
"si"       → True
" SI "     → True
"no"       → False
"sì"       → dipende dal contratto: è un caso diverso da definire
```

<p align="justify">La specifica deve dire quali forme accetta.</p>

---

## 15. Error Clinic

<ul>
  <li><code>find()</code> usato come booleano;</li>
  <li>risultato di <code>lower()</code>/<code>strip()</code> ignorato;</li>
  <li><code>strip(chars)</code> interpretato come rimozione di sottostringa;</li>
  <li>normalizzazione applicata al dato sbagliato;</li>
  <li>metodo standard riscritto manualmente senza obiettivo didattico;</li>
  <li>confronto case-sensitive quando il requisito richiede normalizzazione.</li>
</ul>

---

## 16. Activity candidate

<ul>
  <li><strong>A — Choose the operation:</strong> membership, posizione, prefisso, normalizzazione, sostituzione;</li>
  <li><strong>B — Controlled Change:</strong> da confronto case-sensitive a confronto normalizzato;</li>
  <li><strong>C — Implement:</strong> semplice validator/normalizzatore;</li>
  <li><strong>D — Debug:</strong> correggi <code>find</code>, metodo non assegnato, strip e normalizzazione.</li>
</ul>

<p align="justify">Nessuna nuova Activity P2 viene materializzata finché il profilo function-behavior non è certificato.</p>

---

## 17. Checkpoint

<p align="justify">Sai spiegare:</p>

<ol>
  <li><code>in</code> vs <code>find()</code>;</li>
  <li>perché <code>find()</code> restituisce <code>-1</code>;</li>
  <li>perché <code>if testo.find(...)</code> è fragile;</li>
  <li>immutabilità e metodi che restituiscono nuove stringhe;</li>
  <li>quando normalizzare;</li>
  <li>metodo built-in vs loop manuale.</li>
</ol>

---

## 18. Sintesi

```text
serve solo sapere se esiste? → in
serve la posizione?          → find
serve contare?               → count se coincide col requisito
serve trasformare?           → metodo che restituisce nuova str
```

<p align="justify">Nel prossimo modulo combineremo loop, funzioni e metodi in veri algoritmi su testo e parsing semplice.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 <code>str</code>;</li>
  <li><em>Think Python / Pensare in Python</em> — strings/searching;</li>
  <li><em>Learning Python / Imparare Python</em> — string methods;</li>
  <li><em>Fluent Python</em> — Unicode correctness come controllo docente;</li>
  <li><code>friedpython</code> pinned come fonte legacy da auditare prima di riuso.</li>
</ul>
