# M19 — Algoritmi su testo e parsing semplice

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Algoritmi sul testo combinano cicli, condizioni e funzioni con una politica di normalizzazione dichiarata.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare accesso, slicing, ricerca e metodi di stringa da M17–M18.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
combinare funzioni, cicli, selezione e metodi su stringhe;<br>contare caratteri che soddisfano una proprietà;<br>costruire progressivamente una nuova stringa quando serve; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
I casi limite e i risultati attesi vanno scelti prima di confrontare due implementazioni. Riprendi <a href="18_STRINGHE_RICERCA_METODI_NORMALIZZAZIONE.md">M18 — Ricerca, membership, metodi e normalizzazione delle stringhe</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="20_LISTE_MUTABILITA_METODI_ITERAZIONE.md">M20 — Liste: mutabilità, metodi essenziali e iterazione</a>. Le liste mantengono una sequenza modificabile; alcuni metodi cambiano l&#x27;oggetto senza restituire la lista.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Progetta il controllo di un palindromo e verifica stringa vuota, un carattere e testo con spazi secondo la politica scelta.
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
  <li>combinare funzioni, cicli, selezione e metodi su stringhe;</li>
  <li>contare caratteri che soddisfano una proprietà;</li>
  <li>costruire progressivamente una nuova stringa quando serve;</li>
  <li>progettare e testare un palindromo semplice con normalizzazione dichiarata;</li>
  <li>validare pattern testuali elementari senza regex;</li>
  <li>estrarre parti con indici/slicing;</li>
  <li>progettare casi limite su stringa vuota, un carattere, spazi e maiuscole/minuscole;</li>
  <li>distinguere analisi del testo e formattazione dell'output;</li>
  <li>confrontare algoritmo manuale e soluzione basata su metodi;</li>
  <li>usare <code>split()</code> come ponte consapevole verso la prossima UDA sulle liste.</li>
</ul>

---

## 1. Le stringhe riusano tutto ciò che abbiamo imparato

<p align="justify">Un algoritmo su testo combina:</p>

```text
funzioni
+ loop
+ if
+ contatori/accumulatori
+ indici/slice
+ metodi str
+ test
```

<p align="justify">La stringa cambia il dominio del problema, non le regole fondamentali del ragionamento.</p>

---

## 2. Conteggio di caratteri

```python
def conta_cifre(testo):
    conteggio = 0
    for carattere in testo:
        if carattere.isdigit():
            conteggio += 1
    return conteggio
```

<p align="justify">Invariante:</p>

<blockquote>
<p align="justify"><code>conteggio</code> è il numero di caratteri cifra già elaborati.</p>
</blockquote>

---

## 3. Costruire una nuova stringa

<p align="justify">Per piccoli esercizi beginner:</p>

```python
def solo_lettere(testo):
    risultato = ""
    for carattere in testo:
        if carattere.isalpha():
            risultato += carattere
    return risultato
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — accumulatore testuale:</strong>
Un accumulatore testuale conserva il testo costruito finora e viene aggiornato aggiungendo nuovi frammenti. Nell'esempio questo ruolo è svolto da <code>risultato</code>.
</p>
</td>
</tr>
</table>

<p align="justify">Teacher note: per grandi quantità di frammenti esistono strategie più efficienti; non serve complicare ora il modello.</p>

---

## 4. Palindromo: prima l'algoritmo

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — palindromo:</strong>
Un testo è palindromo se si legge allo stesso modo da sinistra a destra e da destra a sinistra, dopo l'eventuale normalizzazione prevista dalla specifica.
</p>
</td>
</tr>
</table>

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Una parola è uguale letta da sinistra a destra e da destra a sinistra?</p>
</blockquote>

<p align="justify">Prima del trucco compatto, ragioniamo sulle posizioni opposte.</p>

<p align="justify">Esempio:</p>

```text
radar
0 ↔ -1
1 ↔ -2
centro
```

<p align="justify">L'obiettivo è capire il confronto, non memorizzare una slice.</p>

---

## 5. Versione con inversione

<p align="justify">Dopo aver compreso l'algoritmo possiamo confrontare:</p>

```python
def palindroma(testo):
    return testo == testo[::-1]
```

<p align="justify">Domande:</p>

<ul>
  <li>è corretta rispetto al contratto?;</li>
  <li>come gestiamo maiuscole?;</li>
  <li>spazi/punteggiatura vanno ignorati?;</li>
  <li>il requisito parla di parola o frase?.</li>
</ul>

<p align="justify">La normalizzazione deve essere definita prima.</p>

---

## 6. Normalizzazione del palindromo

<p align="justify">Esempio di contratto semplice:</p>

<blockquote>
<p align="justify">Ignora spazi ai bordi e differenze maiuscole/minuscole; non rimuovere punteggiatura interna.</p>
</blockquote>

```python
def palindroma(testo):
    normalizzato = testo.strip().lower()
    return normalizzato == normalizzato[::-1]
```

<p align="justify">Se il contratto cambia, cambiano anche i test.</p>

---

## 7. Casi limite

<p align="justify">Per una funzione testuale considera almeno:</p>

```text
""        stringa vuota
"a"       un carattere
"Radar"   maiuscole
" radar " spazi ai bordi
```

<p align="justify">Non esiste una risposta universale per ogni contratto: definisci prima il comportamento atteso.</p>

---

## 8. Parsing semplice con posizioni note

<p align="justify">Codice:</p>

```text
ABC-123
```

<p align="justify">Contratto:</p>

```text
3 lettere
-
3 cifre
```

<p align="justify">Possiamo controllare:</p>

```python
def codice_valido(codice):
    if len(codice) != 7:
        return False
    return codice[:3].isalpha() and codice[3] == "-" and codice[4:].isdigit()
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — parsing posizionale:</strong>
Il parsing interpreta un testo secondo un formato per riconoscerne le parti e ricavarne dati. Nel parsing posizionale usiamo posizioni note, indici e slicing.
</p>
</td>
</tr>
</table>

---

## 9. Perché niente regex adesso?

<p align="justify">Le espressioni regolari sono potenti, ma introdurle qui può nascondere:</p>

<ul>
  <li>indici;</li>
  <li>slicing;</li>
  <li>composizione booleana;</li>
  <li>struttura del formato.</li>
</ul>

<p align="justify">Regex appartiene al percorso avanzato/optional dopo che il modello base è stabile.</p>

---

## 10. Analisi vs presentazione

<p align="justify">Preferiamo:</p>

```python
def conta_vocali(testo):
    ...
    return conteggio
```

<p align="justify">poi:</p>

```python
risultato = conta_vocali(testo)
print(risultato)
```

<p align="justify">La funzione di analisi non deve stampare se il suo contratto è produrre un valore.</p>

---

## 11. Metodo vs loop: confronto esplicito

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Quante volte compare <code>a</code>?</p>
</blockquote>

<p align="justify">Versione standard:</p>

```python
testo.count("a")
```

<p align="justify">Versione manuale:</p>

```python
conteggio = 0
for carattere in testo:
    if carattere == "a":
        conteggio += 1
```

<p align="justify">Entrambe possono essere corrette.</p>

<p align="justify">La scelta dipende dall'outcome:</p>

<ul>
  <li>imparare scansione/contatore? → loop;</li>
  <li>esprimere una operazione standard? → metodo.</li>
</ul>

---

## 12. `split()` come ponte verso le liste

```python
parti = "rosso,verde,blu".split(",")
```

<p align="justify">Il risultato non è una stringa.</p>

<p align="justify">È una:</p>

```text
list
```

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — split():</strong>
<code>split()</code> divide una stringa in più parti e le restituisce in una lista. Per ora osserviamo il risultato; nella prossima UDA studieremo liste, mutabilità, alias e metodi.
</p>
</td>
</tr>
</table>

---

## 13. `join()` come preview controllata

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — join():</strong>
<code>separatore.join(frammenti)</code> costruisce una stringa unendo frammenti testuali e inserendo il separatore fra un frammento e il successivo.
</p>
</td>
</tr>
</table>

```python
",".join(parti)
```

<p align="justify">Non serve ancora padroneggiare tutte le regole delle liste. È un ponte concettuale:</p>

```text
stringa → split → più parti
più parti → join → stringa
```

---

## 14. Worked example: normalizzatore di username

<p align="justify">Contratto semplice:</p>

<ul>
  <li>rimuovi spazi ai bordi;</li>
  <li>converti in minuscolo;</li>
  <li>deve avere almeno 3 caratteri;</li>
  <li>deve contenere solo lettere/cifre/underscore.</li>
</ul>

```python
def username_valido(testo):
    nome = testo.strip().lower()
    if len(nome) < 3:
        return False

    for carattere in nome:
        if not (carattere.isalnum() or carattere == "_"):
            return False

    return True
```

<p align="justify">Questo riusa funzioni, loop, <code>if</code>, metodi e <code>return</code>.</p>

---

## 15. Error Clinic

<ul>
  <li>stringa vuota non considerata;</li>
  <li>off-by-one sugli indici;</li>
  <li>normalizzazione incompleta;</li>
  <li>tentativo di mutazione;</li>
  <li>risultato di un metodo ignorato;</li>
  <li>parsing che assume lunghezza senza verificarla;</li>
  <li><code>split()</code> usato senza capire che restituisce una lista.</li>
</ul>

---

## 16. Activity candidate

<ul>
  <li><strong>A — Text trace:</strong> indice/carattere/accumulatore;</li>
  <li><strong>B — Controlled Change:</strong> cambia regola di normalizzazione e aggiorna i test;</li>
  <li><strong>C — Implement:</strong> funzione testuale con contratto e casi limite;</li>
  <li><strong>D — Debug:</strong> off-by-one, immutabilità, metodi, stringa vuota;</li>
  <li><strong>E — Mini-project:</strong> analizzatore/normalizzatore con più funzioni e almeno 5 casi.</li>
</ul>

<p align="justify">Nessuna nuova Activity P2 viene materializzata finché il profilo function-behavior non è certificato.</p>

---

## 17. Exit checkpoint PY2-06

<p align="justify">Dovresti saper:</p>

<ul>
  <li>trattare <code>str</code> come sequenza immutabile;</li>
  <li>usare indici/slicing;</li>
  <li>scegliere iterazione diretta/per indice;</li>
  <li>usare membership e metodi appropriati;</li>
  <li>normalizzare consapevolmente;</li>
  <li>implementare un algoritmo testuale con loop;</li>
  <li>progettare casi limite;</li>
  <li>scrivere funzioni testabili su testo;</li>
  <li>motivare metodo vs loop;</li>
  <li>capire che <code>split()</code> produce una lista.</li>
</ul>

---

## 18. Sintesi

```text
str + loop + if + funzioni + test
→ algoritmi su testo
```

```text
split()
→ ponte verso list
```

<p align="justify">La prossima UDA studierà proprio le liste: come si modificano, come si copiano e perché due nomi possono riferirsi alla stessa struttura.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 <code>str</code>;</li>
  <li><em>Think Python / Pensare in Python</em> — string algorithms;</li>
  <li><em>Learning Python / Imparare Python</em> — strings;</li>
  <li><em>Fluent Python</em> — controllo teacher-side su Unicode/sequence;</li>
  <li><code>friedpython</code> pinned come legacy source pack da auditare prima di riuso.</li>
</ul>
