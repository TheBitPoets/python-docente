# M15 — Progettazione top-down e responsabilità

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
La progettazione top-down divide una specifica in responsabilità e contratti di funzione controllabili.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Passare dati esplicitamente e comporre funzioni da M13–M14.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
partire da una specifica e individuare sotto-problemi;<br>dare un nome alle responsabilità prima di scrivere i corpi delle funzioni;<br>distinguere acquisizione dati, logica e presentazione; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Separare calcolo e presentazione permette di verificare la logica con dati scelti. Riprendi <a href="14_SCOPE_LOCALE_PASSAGGIO_DATI_COMPOSIZIONE.md">M14 — Scope locale, passaggio dei dati e composizione</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="16_ASSERT_REGRESSION_TEST_REFACTOR.md">M16 — <code>assert</code>, regression test, debug e refactoring</a>. I casi scelti diventano assert e proteggono correzioni e refactoring dalle regressioni.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Proponi le firme del calcolatore di spedizione e annota input e risultato atteso prima dei corpi.
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
  <li>partire da una specifica e individuare sotto-problemi;</li>
  <li>dare un nome alle responsabilità prima di scrivere i corpi delle funzioni;</li>
  <li>distinguere acquisizione dati, logica e presentazione;</li>
  <li>proporre firme di funzioni con parametri e <code>return</code> coerenti;</li>
  <li>descrivere input/output attesi di una funzione;</li>
  <li>formulare pre-condizioni e post-condizioni semplici in linguaggio naturale;</li>
  <li>riconoscere una funzione che fa troppe cose non correlate;</li>
  <li>estrarre una responsabilità comune quando c'è duplicazione significativa;</li>
  <li>costruire un piccolo call graph;</li>
  <li>implementare e verificare una funzione alla volta.</li>
</ul>

---

## 1. Prima il progetto, poi i dettagli

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — progettazione top-down:</strong>
La progettazione top-down parte dal problema complessivo e lo scompone in responsabilità e sotto-problemi, fino a poter implementare e verificare ciascuna parte.
</p>
</td>
</tr>
</table>

<p align="justify">Quando il programma cresce, iniziare subito a scrivere righe può produrre un unico blocco difficile da controllare.</p>

<p align="justify">Processo top-down:</p>

```text
problema complessivo
→ responsabilità
→ funzioni candidate
→ input/output di ciascuna
→ relazioni tra funzioni
→ test
→ implementazione progressiva
```

<p align="justify">Non significa progettare tutto perfettamente prima di provare.</p>

<p align="justify">Significa avere una mappa prima di perdere il controllo dei dettagli.</p>

---

## 2. Esempio: calcolatore di spedizione

<p align="justify">Specifica semplificata:</p>

<blockquote>
<p align="justify">Leggi prezzo, quantità e distanza. Calcola il subtotale, applica uno sconto se previsto, calcola la spedizione e stampa il totale finale.</p>
</blockquote>

<p align="justify">Possibili responsabilità:</p>

```text
calcola_subtotale
calcola_sconto
calcola_spedizione
calcola_totale
```

<p align="justify">Lettura e stampa possono restare nel flusso principale.</p>

---

## 3. Scrivere prima le firme

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — firma di funzione:</strong>
Nel modello introduttivo del corso, la firma di una funzione ne indica il nome e i parametri. Permette di progettare come chiamarla prima di scriverne il corpo.
</p>
</td>
</tr>
</table>

<p align="justify">Prima dei corpi:</p>

```python
def calcola_subtotale(prezzo, quantita):
    ...


def calcola_sconto(subtotale):
    ...


def calcola_spedizione(distanza):
    ...
```

<p align="justify">Questo costringe a chiedersi:</p>

<ul>
  <li>quali dati servono?;</li>
  <li>quale risultato produce la funzione?;</li>
  <li>quale funzione dipende da quale altra?.</li>
</ul>

---

## 4. Responsabilità singola, senza slogan rigidi

<p align="justify">Una buona funzione dovrebbe avere una responsabilità che possiamo nominare chiaramente.</p>

<p align="justify">Domanda utile:</p>

<blockquote>
<p align="justify">Per descriverla devo dire “fa questo <strong>e poi anche</strong> quest'altra cosa non collegata”?</p>
</blockquote>

<p align="justify">Se sì, forse contiene più responsabilità.</p>

<p align="justify">Non useremo regole meccaniche come:</p>

```text
massimo 10 righe
```

<p align="justify">La dimensione non sostituisce il ragionamento sul significato.</p>

---

## 5. Separare input, logica e output

<p align="justify">Pattern target beginner:</p>

```python
def calcola_sconto(prezzo, percentuale):
    return prezzo * percentuale / 100


def main():
    prezzo = float(input())
    percentuale = float(input())
    sconto = calcola_sconto(prezzo, percentuale)
    print(sconto)

main()
```

<p align="justify">La funzione di logica può essere verificata senza dover simulare tutta l'interfaccia.</p>

<p align="justify"><code>main()</code> qui è soltanto un modo per organizzare il flusso. Il guard <code>if __name__ == "__main__"</code> non è ancora obbligatorio.</p>

---

## 6. Contratto intuitivo

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — contratto di funzione:</strong>
Il contratto descrive quali dati una funzione accetta, quali condizioni assume e quale risultato o comportamento garantisce.
</p>
</td>
</tr>
</table>

<p align="justify">Per una funzione possiamo scrivere:</p>

```text
nome: calcola_sconto
input: prezzo >= 0, percentuale tra 0 e 100
output: importo sconto >= 0
side effect: nessuno
non stampa
```

<p align="justify">Non stiamo ancora introducendo design by contract formale.</p>

<p align="justify">Stiamo rendendo esplicite le aspettative.</p>

---

## 7. Pre-condizione

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — pre-condizione:</strong>
Una pre-condizione descrive ciò che deve essere vero prima di usare correttamente la funzione.
</p>
</td>
</tr>
</table>

<p align="justify">Esempio:</p>

```text
percentuale deve essere tra 0 e 100
```

<p align="justify">La funzione può:</p>

<ul>
  <li>assumere che il chiamante rispetti il contratto in un esercizio controllato;</li>
  <li>oppure validare se la specifica richiede quella responsabilità.</li>
</ul>

<p align="justify">La scelta deve essere esplicita.</p>

---

## 8. Post-condizione

<table align="center">
<tr>
<td>
<p align="justify">
<strong><span style="font-size: 1.15em;">&#128214;</span> Definizione — post-condizione:</strong>
Una post-condizione descrive ciò che deve essere vero sul risultato se la funzione termina correttamente.
</p>
</td>
</tr>
</table>

<p align="justify">Esempio:</p>

```text
calcola_sconto restituisce un valore tra 0 e prezzo
```

<p align="justify">Queste frasi aiutano a progettare i test.</p>

---

## 9. Call graph

<p align="justify">Per il programma di esempio:</p>

```text
main
├─ calcola_subtotale
├─ calcola_sconto
├─ calcola_spedizione
└─ calcola_totale
```

<p align="justify">Un call graph non mostra tutti i dettagli.</p>

<p align="justify">Mostra la struttura delle collaborazioni.</p>

---

## 10. Implementare una funzione alla volta

<p align="justify">Strategia:</p>

```text
1. scegli funzione piccola
2. scrivi casi di test
3. implementa
4. verifica
5. passa alla successiva
6. integra
```

<p align="justify">Questo riduce il numero di cose sconosciute contemporaneamente.</p>

---

## 11. Duplicazione significativa

<p align="justify">Se lo stesso calcolo coerente compare in più punti:</p>

```python
sconto = prezzo * percentuale / 100
```

<p align="justify">può avere senso estrarlo:</p>

```python
def calcola_sconto(prezzo, percentuale):
    return prezzo * percentuale / 100
```

<p align="justify">Non estraiamo una funzione per ogni singola riga solo per aumentare il numero di funzioni.</p>

<p align="justify">Il nome deve rappresentare un concetto utile.</p>

---

## 12. Smell: funzione che fa tutto

```python
def gestisci_ordine():
    # legge input
    # valida
    # calcola
    # stampa
    # ripete
    # decide sconti
    ...
```

<p align="justify">Non è automaticamente sbagliata perché lunga.</p>

<p align="justify">Ma è difficile:</p>

<ul>
  <li>testare una sola responsabilità;</li>
  <li>riusare un calcolo;</li>
  <li>capire dove correggere un bug.</li>
</ul>

<p align="justify">Questo è il momento di cercare sotto-problemi.</p>

---

## 13. Worked example top-down

<p align="justify">Problema:</p>

<blockquote>
<p align="justify">Calcola il costo finale di una prenotazione con prezzo base, numero persone e sconto percentuale.</p>
</blockquote>

<p align="justify">Piano:</p>

```text
calcola_subtotale(prezzo, persone) → subtotale
calcola_sconto(subtotale, percentuale) → sconto
calcola_finale(subtotale, sconto) → finale
```

<p align="justify">Prima dei corpi, casi di test:</p>

```text
100, 2, 10% → subtotale 200, sconto 20, finale 180
50, 1, 0%   → finale 50
```

---

## 14. Error Clinic

## A — funzione fa input e calcolo

<p align="justify">Una funzione che dovrebbe calcolare il totale legge direttamente <code>input()</code>.</p>

<p align="justify">Domanda: possiamo testarla con dati scelti senza simulare input?</p>

## B — funzione stampa e restituisce lo stesso risultato senza motivo

<p align="justify">Qual è davvero il suo contratto?</p>

## C — dipendenza globale

<p align="justify">La funzione usa un valore esterno invece di riceverlo.</p>

## D — duplicazione

<p align="justify">Lo stesso calcolo appare in tre rami con piccole varianti.</p>

## E — funzione troppo generica

<p align="justify">Nome come:</p>

```text
fai_tutto
processa
gestisci
```

<p align="justify">senza responsabilità comprensibile.</p>

---

## 15. Activity candidate

## A — Decomposition cards

<p align="justify">Dato un problema, raggruppa azioni in responsabilità candidate.</p>

## B — Extract function

<p align="justify">Estrai un calcolo coerente da un programma monolitico.</p>

## C — Top-down design

<p align="justify">Consegna prima:</p>

<ul>
  <li>funzioni;</li>
  <li>parametri;</li>
  <li>return;</li>
  <li>call graph;</li>
  <li>casi di test.</li>
</ul>

<p align="justify">Solo dopo implementa.</p>

## D — Smell/debug

<p align="justify">Riconosci dipendenze globali, duplicazioni e funzioni con responsabilità troppo ampia.</p>

---

## 16. Git G1: `diff` come strumento di refactoring

<p align="justify">Dopo un refactoring:</p>

```text
git diff
```

<p align="justify">può aiutarci a rispondere:</p>

<ul>
  <li>quali righe ho spostato?;</li>
  <li>quali responsabilità ho estratto?;</li>
  <li>ho cambiato anche il comportamento senza volerlo?.</li>
</ul>

<p align="justify">Git resta curriculum separato, ma qui diventa parte naturale del workflow.</p>

---

## 17. Checkpoint

<p align="justify">Sai:</p>

<ol>
  <li>individuare 2–4 responsabilità in un problema;</li>
  <li>proporre firme prima dei corpi;</li>
  <li>separare I/O e logica;</li>
  <li>scrivere un contratto intuitivo;</li>
  <li>distinguere pre/post-condizione;</li>
  <li>disegnare un piccolo call graph;</li>
  <li>spiegare perché una funzione ha una responsabilità coerente.</li>
</ol>

---

## 18. Sintesi

```text
specifica
→ responsabilità
→ firme
→ contratti
→ test
→ implementazione
→ integrazione
```

<p align="justify">Nel prossimo modulo useremo <code>assert</code> per rendere eseguibili molti dei casi di test e useremo i test per proteggere debugging e refactoring.</p>

---

## Fonti e riferimenti docente

<p align="justify">Materiale originale del corso, progettato con riferimento a:</p>

<ul>
  <li>documentazione Python 3.12 — funzioni e controllo del flusso;</li>
  <li><em>Think Python / Pensare in Python</em> — decomposizione, funzioni e debugging;</li>
  <li><em>Learning Python / Imparare Python</em> — reference sulle funzioni;</li>
  <li>principi professionali di separazione delle responsabilità adattati al livello beginner.</li>
</ul>

<p align="justify">Le fonti licensed sono teacher-reference; non costituiscono testo da riprodurre.</p>
