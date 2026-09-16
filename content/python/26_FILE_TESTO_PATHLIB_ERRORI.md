# M26 — File testo, `pathlib` ed errori esterni prevedibili

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
I file conservano testo oltre l&#x27;esecuzione; percorsi e gestione mirata degli errori delimitano l&#x27;I/O.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Usare stringhe, strutture dati, funzioni e test; distinguere elaborazione e presentazione.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
spiegare perché un dato in memoria scompare quando il programma termina;<br>rappresentare un percorso con <code>pathlib.Path</code>;<br>leggere un intero file testo UTF-8; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Il valore in memoria e il contenuto persistente sono distinti; la logica può essere testata senza accedere al file. Riprendi <a href="25_STRUTTURE_COMBINATE_SCELTA_MODELLO.md">M25 — Strutture combinate e scelta del modello dati</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="27_CLASSI_ISTANZE_ATTRIBUTI_SELF.md">M27 — Classi, istanze, attributi e <code>self</code></a>. Una classe associa dati e comportamento; le istanze mantengono il proprio stato.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Leggi e scrivi un testo UTF-8 nel workspace e prova il caso di file mancante separandolo dalla logica di calcolo.
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
<strong>UDA:</strong> PY2-09 — Persistenza ed errori prevedibili<br>
<strong>Durata:</strong> 3 ore core<br>
<strong>Baseline:</strong> Python 3.12-compatible nel Classroom Environment TheBitLab</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine del modulo dovresti saper:</p>

<ul>
  <li>spiegare perché un dato in memoria scompare quando il programma termina;</li>
  <li>rappresentare un percorso con <code>pathlib.Path</code>;</li>
  <li>leggere un intero file testo UTF-8;</li>
  <li>scrivere un intero file testo UTF-8;</li>
  <li>usare <code>with open(..., encoding="utf-8")</code> quando serve lavorare con una risorsa file;</li>
  <li>iterare sulle righe di un file;</li>
  <li>separare lettura/scrittura dalla logica di elaborazione;</li>
  <li>distinguere un bug da un errore esterno prevedibile;</li>
  <li>gestire in modo mirato almeno <code>FileNotFoundError</code>;</li>
  <li>riconoscere <code>PermissionError</code> come possibile errore esterno;</li>
  <li>mantenere tutti i file dentro il workspace gestito dal corso.</li>
</ul>

---

## 1. Memoria e persistenza

<p align="justify">Durante l'esecuzione:</p>

```python
voti = {"Anna": 8, "Luca": 7}
```

<p align="justify">vive in memoria.</p>

<p align="justify">Quando il processo termina, quella struttura non diventa automaticamente persistente.</p>

<p align="justify">Un file permette di conservare dati tra esecuzioni.</p>

---

## 2. Percorso e contenuto sono concetti diversi

```python
from pathlib import Path

percorso = Path("dati") / "messaggio.txt"
```

<p align="justify"><code>percorso</code> rappresenta <strong>dove</strong> si trova il file.</p>

<p align="justify">Il contenuto è ciò che leggiamo o scriviamo in quel percorso.</p>

<p align="justify">Questa distinzione prepara anche software più grande e testabile.</p>

---

## 3. Workspace del corso

<p align="justify">Nel corso usiamo soltanto percorsi relativi al workspace gestito TheBitLab.</p>

<p align="justify">Esempio:</p>

```text
dati/messaggio.txt
```

<p align="justify">Non scrivere esercizi canonici che dipendono da:</p>

```text
C:\Users\Mario\Desktop\...
/home/mario/...
```

<p align="justify">Il corso deve funzionare allo stesso modo a scuola e a casa.</p>

---

## 4. Leggere tutto il testo con `Path`

```python
from pathlib import Path

percorso = Path("dati") / "messaggio.txt"
testo = percorso.read_text(encoding="utf-8")
print(testo)
```

<p align="justify">Per file piccoli e interamente testuali questa forma è molto leggibile.</p>

---

## 5. Scrivere tutto il testo

```python
from pathlib import Path

percorso = Path("dati") / "risultato.txt"
percorso.write_text("ciao\n", encoding="utf-8")
```

<p align="justify">La scrittura sostituisce il contenuto del file nella forma mostrata.</p>

<p align="justify">Il contratto deve chiarire se vogliamo sostituire o aggiungere dati.</p>

---

## 6. Perché dichiariamo UTF-8

<p align="justify">Un file testo è una sequenza di byte che deve essere interpretata secondo un encoding.</p>

<p align="justify">Nel corso scegliamo esplicitamente:</p>

```text
UTF-8
```

<p align="justify">Non approfondiamo ancora byte/code point/normalizzazione Unicode.</p>

<p align="justify">Il principio è:</p>

<blockquote>
<p align="justify">l'encoding è parte del contratto del file testuale.</p>
</blockquote>

---

## 7. `with open(...)`

<p align="justify">Per capire il context manager:</p>

```python
from pathlib import Path

percorso = Path("dati") / "messaggio.txt"

with percorso.open("r", encoding="utf-8") as file:
    contenuto = file.read()
```

<p align="justify">All'uscita dal blocco <code>with</code>, la risorsa viene chiusa correttamente anche se durante il blocco si verifica un'eccezione.</p>

---

## 8. Iterare sulle righe

```python
with percorso.open("r", encoding="utf-8") as file:
    for riga in file:
        print(riga.rstrip("\n"))
```

<p align="justify">Attenzione: la riga letta può contenere il terminatore di riga.</p>

<p align="justify">Non usare <code>strip()</code> automaticamente se spazi iniziali/finali fanno parte del dato.</p>

---

## 9. Separare I/O e logica

<p align="justify">Preferiamo:</p>

```python
def conta_righe_non_vuote(testo):
    conteggio = 0
    for riga in testo.splitlines():
        if riga.strip() != "":
            conteggio += 1
    return conteggio
```

<p align="justify">poi:</p>

```python
testo = percorso.read_text(encoding="utf-8")
risultato = conta_righe_non_vuote(testo)
```

<p align="justify">La funzione di logica può essere testata senza dipendere dal filesystem.</p>

---

## 10. `FileNotFoundError`

<p align="justify">Se proviamo a leggere un file che non esiste:</p>

```python
percorso.read_text(encoding="utf-8")
```

<p align="justify">Python può generare:</p>

```text
FileNotFoundError
```

<p align="justify">Questo è un errore esterno prevedibile quando il file può legittimamente mancare.</p>

---

## 11. Gestione mirata

```python
try:
    testo = percorso.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File non trovato")
```

<p align="justify">Il blocco <code>try</code> deve essere <strong>piccolo</strong> e circondare l'operazione che può generare quell'errore.</p>

<p align="justify">Non usare:</p>

```python
except Exception:
    pass
```

<p align="justify">per nascondere qualunque problema.</p>

---

## 12. `PermissionError`

<p align="justify">Un altro possibile problema esterno è:</p>

```text
PermissionError
```

<p align="justify">quando il processo non può leggere/scrivere un percorso.</p>

<p align="justify">Nel Classroom Environment ben configurato questo dovrebbe essere raro, ma sapere distinguere “permesso negato” da “bug della funzione di calcolo” è utile.</p>

---

## 13. Bug vs errore esterno

### Bug

```python
risultato = prezzo + quantita
```

<p align="justify">quando serviva una moltiplicazione.</p>

### Errore esterno

```text
file richiesto assente
permesso negato
```

<p align="justify">Non trattarli allo stesso modo.</p>

---

## 14. Worked example: diario di misure

<p align="justify">File:</p>

```text
12
15
9
```

<p align="justify">Funzione di parsing/logica:</p>

```python
def somma_interi_testo(testo):
    totale = 0

    for riga in testo.splitlines():
        if riga.strip() != "":
            totale += int(riga)

    return totale
```

<p align="justify">I/O:</p>

```python
percorso = Path("dati") / "misure.txt"
testo = percorso.read_text(encoding="utf-8")
print(somma_interi_testo(testo))
```

---

## 15. Testare la logica senza file

```python
assert somma_interi_testo("12\n15\n9\n") == 36
assert somma_interi_testo("") == 0
assert somma_interi_testo("5\n\n7\n") == 12
```

<p align="justify">Questa separazione riduce la parte che richiede un vero filesystem.</p>

---

## 16. TheBitLab P4

<p align="justify">Un grading file corretto deve poter fornire:</p>

```text
fixture input controllata
+ workdir scrivibile isolato
+ verifica host-side degli artifact
```

<p align="justify">È il profilo <code>python-filesystem-v1</code> tracciato in <code>2cornot2c#757</code>.</p>

<p align="justify">Il <strong>candidato software P4 è ora provato end-to-end</strong> anche attraverso il normale Student Lab Docker:</p>

<ul>
  <li>fixture di grading teacher-side montata read-only;</li>
  <li>workdir isolato e bounded;</li>
  <li>expected artifact confrontato sul trusted host;</li>
  <li>traversal/path esterni/symlink/subdirectory bloccati nel profilo v1;</li>
  <li><code>FileNotFoundError</code> mantenuto come errore del programma studente;</li>
  <li>output limit e timeout fail-closed;</li>
  <li>report teacher-only redatto prima della vista studente;</li>
  <li>primo consumer reale M26 verde in CI.</li>
</ul>

<p align="justify">Questa evidenza <strong>non equivale ancora a release P4 stabile</strong>. Il candidato deve essere unificato con la toolchain P2 e ricevere una nuova identità/digest immutabile prima della materializzazione P4 più ampia.</p>

---

## 17. Error Clinic

<ul>
  <li>path assoluto specifico del proprio PC;</li>
  <li>encoding omesso;</li>
  <li><code>strip()</code> usato distruggendo spazi significativi;</li>
  <li>file aperto senza context manager quando serve una gestione esplicita;</li>
  <li><code>except Exception</code> troppo ampio;</li>
  <li><code>try</code> enorme che nasconde dove nasce il problema;</li>
  <li>logica mescolata completamente con I/O;</li>
  <li>scrittura che sovrascrive quando il requisito voleva conservare dati precedenti.</li>
</ul>

---

## 18. Activity candidate

<p align="justify">Resta autorizzato <strong>un solo canarino P4</strong>:</p>

```text
py2-activity-b-file-risultato-001
Controlled Change: print(totale) → risultato.txt
```

<p align="justify">Il canarino usa una fixture pubblica piccola per le prove studente e una fixture teacher-side distinta per il grading autorevole. La soluzione deve creare l'artifact richiesto; lo starter calcola e stampa correttamente il totale ma fallisce perché non persiste <code>risultato.txt</code>.</p>

<p align="justify">Le altre forme restano candidate editoriali, non ancora materializzate in massa:</p>

<ul>
  <li><strong>A — Path/contract trace:</strong> percorso, input file, output atteso;</li>
  <li><strong>B — Controlled Change:</strong> il canarino attuale;</li>
  <li><strong>C — Implement:</strong> leggi file testo e applica una funzione già testabile;</li>
  <li><strong>D — Debug:</strong> path, FileNotFoundError, newline, exception troppo ampia;</li>
  <li><strong>E — Mini-persistence:</strong> produce un file risultato con evidence P4/manuale.</li>
</ul>

<p align="justify">Finché P4 non riceve la release/toolchain immutabile unificata con P2, <strong>non creare altre Activity P4 soltanto per aumentare la copertura automatica</strong>.</p>

---

## 19. Cosa NON entra nel core

<ul>
  <li>CSV;</li>
  <li>JSON;</li>
  <li>file binari;</li>
  <li>pickle/serializzazione;</li>
  <li>regex;</li>
  <li>custom exceptions;</li>
  <li><code>else/finally</code> come capitolo;</li>
  <li>filesystem traversal;</li>
  <li>path assoluti host-specific.</li>
</ul>

<p align="justify">Questi restano Stage B/enrichment.</p>

---

## 20. Exit checkpoint M26

<p align="justify">Sai:</p>

<ol>
  <li>memoria vs persistenza;</li>
  <li>percorso vs contenuto;</li>
  <li><code>Path</code> relativo al workspace;</li>
  <li>UTF-8 esplicito;</li>
  <li><code>read_text</code>/<code>write_text</code>;</li>
  <li><code>with open</code> e chiusura della risorsa;</li>
  <li>iterazione righe;</li>
  <li>separazione I/O-logica;</li>
  <li><code>FileNotFoundError</code> mirato;</li>
  <li>bug vs errore esterno.</li>
</ol>

---

## 21. Sintesi

```text
Path
→ file testo UTF-8
→ I/O piccolo e isolato
→ logica testabile separatamente
```

```text
errore esterno prevedibile
→ except specifico e piccolo
```

<p align="justify">Il prossimo blocco è il traguardo finale del secondo anno: <strong>classi, oggetti, stato, invarianti, composizione e capstone OOP</strong>.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale, con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 <code>pathlib</code>, <code>open</code>, text I/O ed eccezioni built-in;</li>
  <li><em>Think Python / Pensare in Python</em> — files/debugging;</li>
  <li><em>Learning Python / Imparare Python</em> — file objects/exceptions;</li>
  <li>audit <code>sources/FRIEDPYTHON_FILES_AUDIT.md</code>;</li>
  <li>TheBitLab <code>2cornot2c#757</code> — P4 filesystem behavior.</li>
</ul>
