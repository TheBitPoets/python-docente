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

<p align="justify">La domanda non chiede ancora Python, un flow chart o una formula da memorizzare. Chiede di capire una situazione: quali dati conosciamo, quale risultato serve e quale condizione deve essere rispettata perché il risultato abbia senso.</p>

<p align="center"><img src="../../assets/python/m00-modello-problema.svg" alt="Tre pannelli collegati: una richiesta concreta diventa analisi del problema, poi algoritmo e infine programma. Ogni pannello esplicita una domanda diversa." width="960"></p>
<p align="center"><em>Il programma arriva dopo aver chiarito la richiesta e ordinato i passi.</em></p>

<p align="justify">Nel nostro esempio, il prezzo e il pagamento sono i dati di ingresso. Il resto è il risultato che vogliamo comunicare. Il pagamento deve essere almeno uguale al prezzo: se il cliente paga meno, la consegna non descrive più un normale calcolo del resto e dobbiamo decidere come gestire quel caso.</p>

<p align="justify">Una possibile procedura legge i due dati, calcola la differenza e comunica il risultato. Questa procedura è un piccolo <strong>algoritmo</strong>: non è ancora scritto in Python, ma è già abbastanza preciso da poter essere seguito e controllato da un'altra persona.</p>

---

## 2. Problema, algoritmo, programma

## Problema

<p align="justify">È ciò che vogliamo risolvere. Una richiesta come “calcola il resto” sembra semplice, ma diventa realmente utilizzabile solo quando sappiamo quale prezzo e quale pagamento considerare e che cosa fare se il pagamento non è sufficiente.</p>

## Algoritmo

<p align="justify">È una procedura abbastanza precisa da poter essere seguita passo-passo. “Precisa” non significa lunga: significa che ogni passo fornisce le informazioni necessarie a svolgere quello successivo e che il risultato può essere controllato con un esempio.</p>

<p align="justify">Per i nostri primi problemi deve essere:</p>

<ul>
  <li>finita;</li>
  <li>non ambigua al livello necessario;</li>
  <li>eseguibile con i dati disponibili;</li>
  <li>verificabile con esempi concreti.</li>
</ul>

## Programma

<p align="justify">È una descrizione dell'algoritmo in un linguaggio che il computer può eseguire. Un programma può essere scritto senza errori di sintassi e produrre comunque il risultato sbagliato se l'algoritmo o la comprensione della richiesta erano sbagliati.</p>

<p align="center"><img src="../../assets/python/m00-modello-problema.svg" alt="Il percorso dal problema all'algoritmo e al programma, con frecce che indicano un aumento progressivo della precisione." width="960"></p>
<p align="center"><em>La stessa idea viene resa progressivamente più precisa: problema, algoritmo, programma.</em></p>

<p align="justify">Nel corso useremo spesso questa sequenza: capire la richiesta, estrarre i dati, progettare i passi, rappresentarli, scrivere il programma, provarlo e correggerlo. Il programma è quindi una parte del percorso: non sostituisce il ragionamento che viene prima.</p>

---

## 3. Input, output e vincoli

<p align="justify">Restiamo nella situazione della bottiglia: per descrivere bene il problema dobbiamo separare i dati che entrano, l'operazione che li trasforma e il risultato che deve uscire.</p>

<blockquote>
<p align="justify">Una bottiglia costa 2 euro. Un cliente paga con 5 euro. Quanto resto deve ricevere?</p>
</blockquote>

<p align="justify">Gli input sono il prezzo della bottiglia e il pagamento ricevuto. La trasformazione consiste nel calcolare la differenza tra pagamento e prezzo; l'output è il resto da consegnare. C'è anche un vincolo: il pagamento deve essere maggiore o uguale al prezzo. Se il cliente paga meno, non possiamo chiamare la differenza “resto” senza prima decidere come segnalare il pagamento insufficiente.</p>

<p align="center"><img src="../../assets/python/m00-input-output.svg" alt="Il prezzo e il pagamento entrano in una trasformazione; il risultato è il resto e il pagamento sufficiente è un vincolo." width="960"></p>
<p align="center"><em>Input, trasformazione, output e vincolo rispondono a domande diverse.</em></p>

## Informazioni inutili

<p align="justify">Se la consegna aggiunge:</p>

<blockquote>
<p align="justify">Il sensore è di colore blu.</p>
</blockquote>

<p align="justify">il colore probabilmente non serve a calcolare il resto.</p>

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

<p align="justify">Confronta una frase vaga come “fai il calcolo giusto e mostra il risultato” con una sequenza che dichiara esplicitamente i dati, la trasformazione e l'output.</p>

<p align="center"><img src="../../assets/python/m00-passi-operativi.svg" alt="Confronto fra un'istruzione vaga e quattro passi osservabili: acquisire base, acquisire altezza, calcolare il prodotto e mostrarlo." width="960"></p>
<p align="center"><em>Un algoritmo leggibile rende visibili dati, trasformazione e risultato.</em></p>

<p align="justify">La seconda versione è più utile perché rende espliciti dati e trasformazione. Un compagno può controllare se abbiamo letto davvero base e altezza, se abbiamo usato la formula corretta e se il risultato è stato mostrato nel momento giusto.</p>

<p align="justify">Non significa che ogni algoritmo debba avere molti passi: significa che i passi essenziali non devono essere nascosti dietro parole vaghe.</p>

---

## 6. Un esempio non dimostra tutto

<p align="justify">Supponiamo di avere un algoritmo che dovrebbe restituire il maggiore tra due numeri.</p>

<p align="justify">Con il caso A = 8 e B = 3 l'algoritmo restituisce 8. È un primo controllo, ma non è sufficiente per dire che la soluzione funziona sempre: abbiamo visto soltanto una disposizione dei dati.</p>

<p align="justify">Per esplorare meglio il comportamento proviamo almeno un caso con l'ordine invertito, un caso in cui i valori sono uguali e un caso con valori negativi. Ogni prova pone una domanda: la soluzione tratta entrambi gli ordini? Sa che il maggiore può essere uguale a entrambi? Confronta correttamente anche numeri sotto zero?</p>

<p align="center"><img src="../../assets/python/m00-test-errori.svg" alt="Tre casi di test per il maggiore fra due numeri: caso normale, valori uguali e ordine invertito. A destra sono distinti errore di comprensione, errore dell'algoritmo ed errore di esecuzione." width="960"></p>
<p align="center"><em>Un esempio riuscito è un'evidenza su un caso, non una dimostrazione generale.</em></p>

<p align="justify">Nel secondo anno costruire casi di test diventerà una normale abitudine di lavoro.</p>

---

## 7. Caso normale, caso limite, controesempio

## Caso normale

<p align="justify">Rappresenta una situazione comune.</p>

<p align="justify">Esempio: età 15 in una verifica <code>età &gt;= 14</code>.</p>

## Caso limite

<p align="justify">È vicino a un confine importante.</p>

<p align="justify">Esempi: 13 e 14 per la soglia 14. Il primo sta appena sotto il confine; il secondo è esattamente sul confine. Possiamo aggiungere 15 per osservare il lato opposto. Il caso limite non è “un caso strano”: è un caso scelto perché una piccola differenza può cambiare il risultato.</p>

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

<p align="center"><img src="../../assets/python/m00-test-errori.svg" alt="La diagnosi separa tre origini dell'errore: richiesta compresa male, algoritmo ordinato male e futura esecuzione che fallisce." width="960"></p>
<p align="center"><em>Prima di correggere, identifica quale livello del ragionamento è in errore.</em></p>

<p align="justify">Questa distinzione ci aiuterà a fare debug senza cambiare cose a caso. Se abbiamo scelto la richiesta sbagliata, modificare una formula non risolve il problema; se l'algoritmo è corretto ma l'esecuzione fallisce, dobbiamo invece cercare il difetto nella traduzione in programma.</p>

---

## 9. Micro-lab senza computer

<p align="justify">Per ciascuna consegna annota, in questo ordine, quali dati entrano, quale risultato deve uscire, quali vincoli devono essere rispettati, quali passi proponi e almeno un caso normale e uno vicino a un confine. Non serve usare parole tecniche perfette: serve lasciare una traccia che un compagno possa seguire senza chiederti che cosa intendevi.</p>

<table align="center">
<thead><tr><th>Domanda</th><th>Esempio sul resto</th></tr></thead>
<tbody>
<tr><td>Quali dati entrano?</td><td>Prezzo e pagamento.</td></tr>
<tr><td>Che cosa deve uscire?</td><td>Il resto, se il pagamento è sufficiente.</td></tr>
<tr><td>Quale vincolo vale?</td><td>Pagamento maggiore o uguale al prezzo.</td></tr>
<tr><td>Come controllo l'idea?</td><td>Provo pagamento uguale, maggiore e insufficiente.</td></tr>
</tbody>
</table>

<p align="justify">Le proposte da analizzare sono:</p>

<ol>
  <li>calcolare il resto;</li>
  <li>decidere se una temperatura supera una soglia;</li>
  <li>trovare il maggiore tra due valori;</li>
  <li>descrivere un percorso di tre mosse su una griglia.</li>
</ol>

<p align="justify">Poi scambia il foglio con un compagno. Il compagno deve poter ricostruire la tua idea e indicare dove manca un dato, un controllo o un passo. Se deve interromperti spesso per chiedere spiegazioni, non è un problema del compagno: è un segnale che la specifica o l'algoritmo sono ancora troppo vaghi.</p>

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
  <li>quale esempio proveresti per primo?</li>
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

<p align="center"><img src="../../assets/python/m00-modello-problema.svg" alt="Il percorso riassuntivo va dalla richiesta alla sua analisi, all'algoritmo e al programma; i test e il debug verificano il risultato del percorso." width="960"></p>
<p align="center"><em>Capire prima, rappresentare poi, eseguire e controllare infine.</em></p>

<p align="justify">Prima di scrivere codice, chiediti: ho capito la richiesta? Ho separato dati, risultato e vincoli? I passi sono osservabili? Ho scelto almeno due casi diversi? Se una risposta è “non ancora”, torna al modello del problema e correggilo. Prossimo modulo: trasformiamo il problema in pseudocodice e impariamo a fare un trace manuale sistematico.</p>
