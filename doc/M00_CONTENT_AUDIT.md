# Audit contenuti M00 — Problema, algoritmo, programma, input e output

<p align="justify">Revisione editoriale del 16 settembre 2026. L'obiettivo è rendere M00 autonoma per una classe che non ha ancora scritto codice: ogni termine viene introdotto prima di essere riutilizzato, ogni esempio esplicita la domanda a cui risponde e il testo distingue comprensione, progettazione, esecuzione e verifica.</p>

## Criticità rilevate e interventi

<table align="center">
<thead><tr><th>Area</th><th>Criticità</th><th>Impatto</th><th>Intervento applicato</th></tr></thead>
<tbody>
<tr><td>Distinzioni di base</td><td>Problema, algoritmo e programma erano definiti in modo molto breve; il rapporto fra i tre livelli restava implicito.</td><td>Un principiante poteva credere che scrivere un programma fosse già “risolvere” il problema.</td><td>Le definizioni ora spiegano lo scopo di ciascun livello e chiariscono che un programma sintatticamente corretto può implementare un'idea sbagliata.</td></tr>
<tr><td>Input/output/vincoli</td><td>Le etichette ASCII non spiegavano perché un dato appartenesse all'input, né che cosa rendesse valido il calcolo.</td><td>Difficoltà nel distinguere dati utili, dati decorativi e condizioni di validità.</td><td>Nuova figura <code>m00-input-output.svg</code> e spiegazione discorsiva con pagamento sufficiente e unità di misura.</td></tr>
<tr><td>Algoritmo operativo</td><td>La differenza fra “fai il calcolo” e passi osservabili era lasciata al lettore.</td><td>Rischio di produrre istruzioni vaghe non verificabili da un compagno.</td><td>Nuova figura <code>m00-passi-operativi.svg</code> e criterio esplicito: dati, trasformazione e risultato devono essere riconoscibili.</td></tr>
<tr><td>Dati mancanti</td><td>“Calcola l'area” veniva risolto con una risposta corretta ma poco motivata.</td><td>Il principiante poteva interpretare la richiesta di chiarimento come un fallimento.</td><td>Il testo presenta la specifica incompleta come una condizione normale da chiarire, senza inventare dati.</td></tr>
<tr><td>Test</td><td>La parola <em>evidence</em> era inglese e i casi erano elencati senza spiegare quale proprietà verificassero.</td><td>Confusione fra esempio, prova di un caso e controllo di casi diversi.</td><td>Terminologia italiana, spiegazione del motivo di ogni caso e nuova figura <code>m00-test-errori.svg</code> con caso normale, limite e ordine invertito.</td></tr>
<tr><td>Error Clinic</td><td>Le tre categorie di errore erano corrette ma non collegate a una procedura diagnostica.</td><td>Rischio di correggere la formula quando il problema era stato compreso male, o viceversa.</td><td>La figura collega comprensione, algoritmo ed esecuzione alla domanda “a quale livello devo tornare?”.</td></tr>
<tr><td>Attività</td><td>Il micro-lab chiedeva di compilare un modello ma il modello era un blocco ASCII.</td><td>La forma occupava attenzione senza aggiungere un supporto visivo utile.</td><td>Il modello è diventato una tabella HTML con domande e risposta esemplificativa; il lavoro resta scrivibile su carta.</td></tr>
<tr><td>Chiarezza linguistica</td><td>Erano presenti una punteggiatura errata (“primo?”) e formule potenzialmente assolute (“funziona sempre”).</td><td>La domanda diagnostica perdeva precisione.</td><td>Punteggiatura corretta e formulazioni che distinguono evidenza locale da correttezza generale.</td></tr>
</tbody>
</table>

## Figure inserite in M00

<ul>
<li><a href="../assets/python/m00-modello-problema.svg">Dal problema al programma</a>: modello generale riusato nell'apertura e nel recap.</li>
<li><a href="../assets/python/m00-input-output.svg">Input, trasformazione, output e vincoli</a>: esempio del resto e controllo del pagamento.</li>
<li><a href="../assets/python/m00-passi-operativi.svg">Da parole vaghe a passi operativi</a>: confronto fra istruzione vaga e sequenza osservabile.</li>
<li><a href="../assets/python/m00-test-errori.svg">Test diversi e diagnosi degli errori</a>: casi di test e tre livelli della diagnosi.</li>
</ul>

<p align="justify">Le figure condividono canvas, palette, tipografia, frecce e simboli del <a href="../assets/python/visual-system/README.md">Visual System Python</a>. Il testo alternativo esplicita la relazione didattica, così il significato non dipende dal colore o dalla sola immagine.</p>

## Confini didattici mantenuti

<p align="justify">M00 non introduce sintassi Python, flow chart formali, pseudocodice o test automatizzati. Usa solo esempi quotidiani, numeri, ragionamento scritto e una prima distinzione fra livelli dell'errore. Il modulo successivo svilupperà la specifica, il pseudocodice e il trace manuale; anticipare questi strumenti in M00 avrebbe aumentato il carico cognitivo senza migliorare l'obiettivo iniziale.</p>

<p align="justify">La revisione non dichiara che un algoritmo sia corretto perché supera i casi mostrati. Chiede invece di formulare casi diversi e di spiegare che cosa ciascun caso mette alla prova. Questa distinzione prepara il lavoro di testing delle UDA successive.</p>

## Verifiche eseguite

<ul>
<li>controllo HTML, orientamento, link locali e alt text con <code>tests/course_presentation.py</code>;</li>
<li>rigenerazione e controllo byte-for-byte degli SVG con <code>scripts/build_course_diagrams.py --check</code>;</li>
<li>audit e registro figure rigenerati con <code>scripts/build_visual_audit.py</code>;</li>
<li>suite statica completa del corso superata con <code>scripts/run_static_quality.py</code>.</li>
</ul>
