# M00 — Problema, algoritmo, programma, input e output

<!-- COURSE-FRAME:START -->
<table align="center">
<tr><td>
<details>
<summary>&#129517; <strong>Orientamento della sezione</strong></summary>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128506;</span> Contesto:</strong>
Il percorso comincia dalla distinzione fra problema, algoritmo e programma, prima di usare un linguaggio.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128736;</span> Prerequisiti:</strong>
Nessuna esperienza di programmazione: bastano la lettura di una consegna e semplici calcoli.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#127919;</span> Obiettivi:</strong>
distinguere un <strong>problema</strong> da un <strong>algoritmo</strong> e da un <strong>programma</strong>;<br>individuare input, output e vincoli in una consegna semplice;<br>riconoscere informazioni necessarie, inutili o mancanti; <a href="#obiettivi">Tutti gli obiettivi del modulo</a>.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128257;</span> Richiamo:</strong>
Parti da una procedura quotidiana e chiediti quali dati servono e quale risultato deve produrre.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#128064;</span> Anticipazione:</strong>
Il percorso prosegue con <a href="01_DAL_PROBLEMA_AI_PASSI.md">M01 — Dal problema ai passi: specifica, pseudocodice e trace</a>. Una consegna diventa una sequenza di passi verificabile con una traccia manuale.
</p>

<p align="justify">
<strong><span style="font-size: 1.15em;">&#10145;</span> Prossimo passo:</strong>
Analizza il problema del resto: indica input, output, vincolo e un caso che non rispetta il vincolo.
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
<p align="justify"><strong>Stato:</strong> draft / orientamento iniziale<br>
<strong>Collocazione:</strong> prima settimana, integrato nella finestra PY2-01<br>
<strong>Dipendenze:</strong> nessuna; Python e Flowchart Lab non sono prerequisiti</p>
</blockquote>

## Obiettivi

<p align="justify">Alla fine di questo modulo dovresti saper:</p>

<ul>
  <li>distinguere un <strong>problema</strong> da un <strong>algoritmo</strong> e da un <strong>programma</strong>;</li>
  <li>individuare input, output e vincoli in una consegna semplice;</li>
  <li>riconoscere informazioni necessarie, inutili o mancanti;</li>
  <li>descrivere una soluzione come una sequenza finita di passi;</li>
  <li>usare esempi e controesempi per controllare se hai capito il problema;</li>
  <li>distinguere almeno intuitivamente un errore di comprensione, un errore nell'algoritmo e un errore di esecuzione.</li>
</ul>

<p align="justify">Non devi ancora scrivere codice.</p>

---

## 1. Prima del linguaggio viene il problema

<p align="justify">Considera la richiesta:</p>

<blockquote>
<p align="justify">Una bottiglia costa 2 euro. Un cliente paga con 5 euro. Quanto resto deve ricevere?</p>
</blockquote>

<p align="justify">La domanda non chiede ancora Python, un flow chart o una formula da memorizzare.</p>

<p align="justify">Prima dobbiamo capire:</p>

```text
INPUT  → prezzo, denaro ricevuto
OUTPUT → resto
VINCOLO → il pagamento deve essere sufficiente
```

<p align="justify">Una possibile procedura è:</p>

```text
1. leggi il prezzo
2. leggi quanto è stato pagato
3. calcola pagato - prezzo
4. comunica il resto
```

<p align="justify">Questa procedura è un piccolo <strong>algoritmo</strong>.</p>

---

## 2. Problema, algoritmo, programma

## Problema

<p align="justify">È ciò che vogliamo risolvere.</p>

<p align="justify">Può essere espresso in linguaggio naturale e può contenere informazioni incomplete o ambigue.</p>

## Algoritmo

<p align="justify">È una procedura abbastanza precisa da poter essere seguita passo-passo.</p>

<p align="justify">Per i nostri primi problemi deve essere:</p>

<ul>
  <li>finita;</li>
  <li>non ambigua al livello necessario;</li>
  <li>eseguibile con i dati disponibili;</li>
  <li>verificabile con esempi concreti.</li>
</ul>

## Programma

<p align="justify">È una descrizione dell'algoritmo in un linguaggio che il computer può eseguire.</p>

<p align="justify">Il percorso del corso sarà spesso:</p>

```text
problema
→ analisi
→ algoritmo
→ rappresentazione / trace
→ programma
→ test
→ debug
```

<p align="justify">Il programma non sostituisce il ragionamento che viene prima.</p>

---

## 3. Input, output e vincoli

<p align="justify">Prendiamo una seconda consegna:</p>

<blockquote>
<p align="justify">Dati la temperatura attuale e una soglia, indica se la temperatura supera la soglia.</p>
</blockquote>

<p align="justify">Possiamo estrarre:</p>

```text
INPUT
- temperatura attuale
- soglia

OUTPUT
- sì/no: supera la soglia?
```

<p align="justify">Un vincolo potrebbe essere, per esempio, l'unità di misura comune.</p>

## Informazioni inutili

<p align="justify">Se la consegna aggiunge:</p>

<blockquote>
<p align="justify">Il sensore è di colore blu.</p>
</blockquote>

<p align="justify">il colore probabilmente non serve a decidere se la temperatura supera la soglia.</p>

<p align="justify">Un buon programmatore non usa automaticamente ogni dato disponibile: chiede <strong>quale dato serve davvero alla decisione</strong>.</p>

---

## 4. Informazioni mancanti

<p align="justify">Consegna:</p>

<blockquote>
<p align="justify">Calcola l'area.</p>
</blockquote>

<p align="justify">Possiamo farlo?</p>

<p align="justify">Non ancora: manca almeno la forma e mancano le misure necessarie.</p>

<p align="justify">Una specifica insufficiente non si corregge inventando dati.</p>

<p align="justify">Prima si chiarisce il problema.</p>

---

## 5. I passi devono essere operativi

<p align="justify">Confronta:</p>

```text
1. fai il calcolo giusto
2. mostra il risultato
```

<p align="justify">con:</p>

```text
1. acquisisci base
2. acquisisci altezza
3. calcola base × altezza
4. mostra il prodotto
```

<p align="justify">La seconda versione è più utile perché rende espliciti dati e trasformazione.</p>

<p align="justify">Non significa che ogni algoritmo debba avere molti passi: significa che i passi essenziali non devono essere nascosti dietro parole vaghe.</p>

---

## 6. Un esempio non dimostra tutto

<p align="justify">Supponiamo di avere un algoritmo che dovrebbe restituire il maggiore tra due numeri.</p>

<p align="justify">Con il caso:</p>

```text
A = 8
B = 3
```

<p align="justify">ottiene 8.</p>

<p align="justify">È sufficiente per dire che l'algoritmo funziona sempre?</p>

<p align="justify">No.</p>

<p align="justify">Proviamo almeno:</p>

```text
A = 3, B = 8
A = 5, B = 5
A = -2, B = -7
```

<p align="justify">Un caso riuscito è <strong>evidence</strong>, non una dimostrazione generale.</p>

<p align="justify">Nel secondo anno costruire casi di test diventerà una normale abitudine di lavoro.</p>

---

## 7. Caso normale, caso limite, controesempio

## Caso normale

<p align="justify">Rappresenta una situazione comune.</p>

<p align="justify">Esempio: età 15 in una verifica <code>età &gt;= 14</code>.</p>

## Caso limite

<p align="justify">È vicino a un confine importante.</p>

<p align="justify">Esempi:</p>

```text
13
14
```

<p align="justify">per la soglia 14.</p>

## Controesempio

<p align="justify">È un dato che mostra che la nostra soluzione non funziona come pensavamo.</p>

<p align="justify">Cercare controesempi non significa voler “rompere” il lavoro di qualcuno: significa verificarlo seriamente.</p>

---

## 8. Error Clinic: tre errori diversi

## Ho capito male il problema

<p align="justify">La specifica chiede la media, ma io progetto la somma.</p>

<p align="justify">Il programma potrebbe essere eseguito perfettamente e restare comunque sbagliato.</p>

## L'algoritmo è sbagliato

<p align="justify">Ho capito la richiesta, ma ho ordinato male i passi o dimenticato un caso.</p>

## L'esecuzione fallisce

<p align="justify">L'algoritmo può essere corretto, ma un futuro programma può contenere un errore di sintassi, un dato non valido o un altro problema di esecuzione.</p>

<p align="justify">Questa distinzione ci aiuterà a fare debug senza cambiare cose a caso.</p>

---

## 9. Micro-lab senza computer

<p align="justify">Per ciascuna consegna annota:</p>

```text
INPUT
OUTPUT
VINCOLI
PASSI
UN CASO NORMALE
UN CASO LIMITE
```

<p align="justify">Proposte:</p>

<ol>
  <li>calcolare il resto;</li>
  <li>decidere se una temperatura supera una soglia;</li>
  <li>trovare il maggiore tra due valori;</li>
  <li>descrivere un percorso di tre mosse su una griglia.</li>
</ol>

<p align="justify">Poi scambia il foglio con un compagno: deve poter seguire i passi senza chiederti che cosa intendevi.</p>

---

## 10. Diagnostic iniziale

<p align="justify">Il diagnostic non è una verifica con voto.</p>

<p align="justify">Serve a capire da dove parte la classe.</p>

<p align="justify">Domande possibili:</p>

<ul>
  <li>quali dati servono?;</li>
  <li>quale risultato è richiesto?;</li>
  <li>quale passo manca?;</li>
  <li>questo procedimento termina?;</li>
  <li>quale esempio proveresti per primo?.</li>
</ul>

<p align="justify">Non serve conoscere parole tecniche perfette: conta il ragionamento.</p>

---

## Minimum mastery checkpoint

<p align="justify">Prima di proseguire dovresti riuscire a:</p>

<ol>
  <li>spiegare con parole tue problema/algoritmo/programma;</li>
  <li>estrarre input e output da una consegna breve;</li>
  <li>segnalare un'informazione mancante;</li>
  <li>ordinare una sequenza semplice di passi;</li>
  <li>proporre almeno due casi diversi;</li>
  <li>dire perché un solo esempio non garantisce che la soluzione sia corretta.</li>
</ol>

## Recap

```text
capire il problema
→ separare dati e risultato
→ costruire passi eseguibili
→ provare esempi diversi
→ correggere il modello prima del codice
```

<p align="justify">Prossimo modulo: trasformiamo il problema in pseudocodice e impariamo a fare un trace manuale sistematico.</p>
