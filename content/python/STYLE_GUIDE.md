# Formattazione delle lezioni Python

<p align="justify">Convenzione applicata a tutte le 31 lezioni M00–M30, secondo <a href="https://github.com/TheBitPoets/tpsi-quinto-docente/blob/main/content/tpsi5/STYLE_GUIDE.md">TPSI quinto</a>, <a href="https://github.com/TheBitPoets/tpsi-quarto-docente/blob/main/content/tpsi_quarto/STYLE_GUIDE.md">TPSI quarto</a> e il <a href="https://github.com/TheBitPoets/2cornot2c/blob/main/README.md">README di 2cornot2c</a>. I file restano .md per la piattaforma, ma prosa e impaginazione usano HTML, non marcatori Markdown.</p>

## Testo, titoli e codice

<ul>
<li>Paragrafi: <code>&lt;p align="justify"&gt;</code>; enfasi e codice inline: <code>strong</code>, <code>em</code>, <code>code</code>; collegamenti: <code>a href</code>.</li>
<li>Liste: <code>ul</code> o <code>ol</code> con <code>li</code>. Conservare il numero iniziale delle sequenze interrotte.</li>
<li>Tabelle: <code>&lt;table align="center"&gt;</code> con intestazioni <code>th</code>. Immagini e didascalie: paragrafi centrati.</li>
<li>Titoli Markdown conservati come nei corsi TPSI: un solo H1, sezioni H2 e sottosezioni H3. Il testo dei titoli resta invariato, così rimangono validi gli anchor.</li>
<li>I fenced code block restano fuori dai contenitori HTML e conservano integralmente il sorgente. Dentro un pannello usare <code>pre</code>/<code>code</code> con escape di &amp;, &lt; e &gt;.</li>
<li>Le slide restano nel formato Marp. Runbook, checkpoint, attività e documentazione operativa mantengono i propri contratti: questa normalizzazione riguarda le dispense canoniche.</li>
</ul>

## Definizioni

<p align="justify">Le definizioni usano un riquadro HTML centrato, sempre visibile, con icona libro <code>&amp;#128214;</code> ed etichetta <strong>Definizione — termine:</strong>. La cornice riprende i riquadri didattici di <a href="https://github.com/TheBitPoets/2cornot2c/blob/main/README.md">2cornot2c</a>; icona ed etichetta seguono i <a href="https://github.com/TheBitPoets/tpsi-quinto-docente/blob/main/content/tpsi5/STYLE_GUIDE.md#callout-semantici">callout semantici di TPSI quinto</a>.</p>

<pre><code>&lt;table align="center"&gt;
&lt;tr&gt;
&lt;td&gt;
&lt;p align="justify"&gt;
&lt;strong&gt;&lt;span style="font-size: 1.15em;"&gt;&amp;#128214;&lt;/span&gt; Definizione — termine:&lt;/strong&gt;
Testo breve, autonomo e preciso.
&lt;/p&gt;
&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;</code></pre>

<ul>
<li>Rendere riconoscibile la definizione nel punto in cui il concetto viene introdotto, prima che sia necessario per capire gli esempi.</li>
<li>Usare la stessa forma per definizioni originariamente presenti nella prosa, in citazioni o implicite in un titolo e nello schema immediatamente successivo.</li>
<li>Scrivere una frase comprensibile anche da sola; mantenere esempi, codice, confronti e spiegazioni accanto al riquadro.</li>
<li>Non usare <code>details</code> per nascondere una definizione e non inserire blocchi di codice Markdown dentro la tabella.</li>
<li>Le tabelle di operatori o metodi possono dettagliare una definizione comune, senza un riquadro annidato per ogni riga.</li>
<li>Distinguere una definizione da una consegna, un consiglio, una domanda o un richiamo a un caso concreto: questi mantengono la propria forma.</li>
</ul>

## Orientamento della sezione

<p align="justify">Subito dopo il titolo, una tabella centrata contiene <code>details</code> e un <code>summary</code> con bussola e titolo. Le definizioni e la spiegazione fondamentale restano visibili nel corpo della lezione.</p>

<table align="center">
<thead><tr><th>Icona</th><th>Campo</th><th>Descrizione richiesta</th></tr></thead>
<tbody>
<tr><td>&#129517;</td><td>Orientamento della sezione</td><td>Titolo del pannello espandibile</td></tr>
<tr><td>&#128506;</td><td>Contesto</td><td>Ruolo concreto dell'argomento nel percorso</td></tr>
<tr><td>&#128736;</td><td>Prerequisiti</td><td>Abilità già affrontate, senza anticipazioni imposte</td></tr>
<tr><td>&#127919;</td><td>Obiettivi</td><td>Primi tre obiettivi esistenti e rimando all'elenco completo</td></tr>
<tr><td>&#128257;</td><td>Richiamo</td><td>Concetto da riattivare e collegamento al modulo precedente</td></tr>
<tr><td>&#128064;</td><td>Anticipazione</td><td>Modulo successivo o checkpoint finale</td></tr>
<tr><td>&#10145;</td><td>Prossimo passo</td><td>Una prova specifica da svolgere</td></tr>
<tr><td>&#128279;</td><td>Rimando</td><td>Indice studente e obiettivi cliccabili</td></tr>
</tbody>
</table>

<p align="justify">I testi specifici sono mantenuti in <a href="../../config/course-presentation.json">course-presentation.json</a>. Il normalizzatore aggiorna soltanto la cornice delimitata da <code>COURSE-FRAME</code> e conserva l'HTML già presente. Modificare i testi dell'orientamento nel JSON; gli obiettivi vengono letti dalla lezione.</p>

## Immagini

<p align="justify">Usare la <a href="../../assets/python/visual-system/README.md">collezione SVG</a>, percorsi locali, alt descrittivo e didascalia. Il <a href="../../doc/VISUAL_AUDIT.md">registro dell'audit</a> distingue immagini pianificate, prototipi e inserimento nelle lezioni. Non introdurre dipendenze da font, CSS, script o immagini remoti.</p>

## Verifica

<pre lang="bash"><code>python scripts/format_python_lessons.py --write
python scripts/format_python_lessons.py --check
python scripts/build_course_diagrams.py --check
python scripts/build_visual_audit.py --check
python tests/course_presentation.py
python scripts/run_static_quality.py
git diff --check</code></pre>

<p align="justify">La revisione corrente uniforma la presentazione, conserva codice e contenuti preesistenti e aggiunge l'orientamento. Non costituisce la nuova revisione dei contenuti né modifica i gate di approvazione didattica del corso.</p>
