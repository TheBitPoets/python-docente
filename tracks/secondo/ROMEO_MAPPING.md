# Romeo → Python secondo — mapping selettivo

> Stato: **mapping architetturale DRAFT completato** per la pianificazione Activity. Non certifica ancora l'esecuzione cross-profile del runtime.

## Snapshot auditato

Repository:

```text
TheBitPoets/romeo
```

Snapshot di riferimento:

```text
45e5f7e131802fccc89358a23a25dbed1884bbfa
```

Il commit corrente differisce dal parent funzionale soprattutto per metadata di deploy docs; il mapping deve comunque essere aggiornato esplicitamente prima di importare/adattare una Activity se Romeo evolve.

## Regola fondamentale

Romeo è una **spine applicativa**, non il curriculum Python.

Per ogni concetto:

```text
modello generale / esercizio non-Romeo
→ competenza Python
→ eventuale missione Romeo che rende visibile la stessa competenza
```

Mai:

```text
impara l'API Romeo
= impara Python
```

Ogni outcome core resta raggiungibile senza hardware fisico e con esercizi generali.

---

# Cosa esiste già in Romeo

Il corso Romeo `year 1` contiene Activity utili per:

- REPL;
- chiamate di funzione;
- sequenze;
- condizioni;
- `for`;
- `while`;
- funzioni con parametro;
- simulazione/debug;
- coordinate/missioni;
- capstone procedurale.

Le Activity verificate usano Activity schema 1.0 e, quando simulator-backed, dichiarano:

```text
extensions.thebitlab.runtime.runtime_id = romeo-sim
```

con capability come:

- `headless-run`;
- `deterministic-grade`;
- `artifact-collect`.

La versione attuale del corso Romeo `year 2` tratta networking, HTTP/FastAPI, WebSocket, camera/telepresenza ecc. **Non appartiene al track Python beginner di seconda** e non viene importata.

---

# Legenda di riuso

- **NO** — non usare Romeo nel core del modulo;
- **DEMO** — breve applicazione/visualizzazione docente, non Activity necessaria;
- **ADAPT** — scenario/Activity Romeo esistente è un buon candidato da adattare/allegare dopo verifica;
- **NEW** — creare una nuova Activity Python+Romeo perché quella esistente misura un outcome diverso;
- **OPTIONAL** — enrichment, non requisito core.

Non copiare sorgenti/fixture da Romeo dentro `python-docente` se possiamo riferirci al consumer/runtime canonico.

---

# Mapping modulo per modulo

| Modulo Python | Romeo | Asset/Activity Romeo candidata | Uso |
|---|---|---|---|
| M00 problema/algoritmo | DEMO | scenario robot su griglia, senza runtime | dominio narrativo per scomporre passi |
| M01 algoritmo/pseudocodice | DEMO | percorso semplice | progettare sequenza senza API |
| M02 flow chart selezione | OPTIONAL | nessuna Activity runtime necessaria | rappresentare decisione su missione astratta |
| M03 flow chart loop | OPTIONAL | missione su griglia astratta | progettare ripetizione prima del codice |
| M04 REPL/script/I-O | OPTIONAL/ADAPT | `y1-u03-repl` | solo dopo REPL Python generale; osservare chiamate Romeo |
| M05 espressioni/prime funzioni | ADAPT | `y1-u04-chiamate-funzione`, `y1-u11-velocita` | chiamata/argomento come applicazione, non sostituisce I/O generale |
| M06 bool/if | ADAPT | `romeo-y1-u14-condizioni` | prima missione Romeo naturale su `if` |
| M07 elif/logica composta | NEW/OPTIONAL | scenario derivato | usare solo se esiste vera scelta multi-caso; non forzare `elif` su missione binaria |
| M08 annidamento/validazione | NEW/OPTIONAL | scenario parametrizzato | validare parametro/comando; niente sensori/networking |
| M09 while | ADAPT | `romeo-y1-u16-ciclo-while` | terminazione/contatore visibile |
| M10 for/range | ADAPT | `romeo-y1-u15-ciclo-for` | numero noto di movimenti; ottimo confronto for vs duplicazione |
| M11 pattern loop+if | NEW/ADAPT | missione derivata / parti di `y1-u19-missioni` | conteggio/condizione solo se il dominio la giustifica |
| M12 nested loops | OPTIONAL | griglia/coordinate | solo se una missione 2D naturale evita annidamento artificiale |
| M13 funzioni/return | ADAPT | `romeo-y1-u12-funzioni` | funzione parametrica; integrare outcome `return` con esempi generali perché Romeo movement può essere side-effect based |
| M14 scope/composizione funzioni | NEW/OPTIONAL | missione con più helper | mostrare dipendenze esplicite, niente globali accidentali |
| M15 top-down | ADAPT | `romeo-y1-u19-missioni` | percorso in segmenti verificabili → responsabilità/funzioni |
| M16 test/debug/refactor | ADAPT | `romeo-y1-u17-simulazione`, `y1-u19` | previsione vs traiettoria/eventi; regression thinking |
| M17–M19 stringhe | NO | — | non forzare Romeo |
| M20–M22 liste/tuple/matrici | OPTIONAL | waypoint/step solo se utile | nessuna dipendenza Romeo core |
| M23 set | NO | — | nessun beneficio naturale nel core |
| M24 dict | NO/OPTIONAL | comandi/config solo se semplice | non forzare mapping |
| M25 data modelling | OPTIONAL | lista/tuple di step o waypoint | solo come caso di scelta struttura |
| M26 file/errori | NO | — | file ha domini generali migliori |
| M27 class/instance | DEMO/NEW | `romeo.easy` vs `romeo.robot.Robot` | confronto autentico procedurale → oggetti |
| M28 __init__/state/invariants | DEMO/NEW | `Robot(speed_limit=...)` | API reale mostra init, stato, validazione |
| M29 composition | NEW | `Missione` che riceve/contiene `Robot` | caso canonico di composizione |
| M30 capstone | NEW + scenario reuse | scenario ispirato a `y1-u20-capstone` | capstone OOP, non riuso procedurale diretto |

---

# Activity esistenti da riusare/adattare

## `romeo-y1-u14-condizioni` → PY2-03/M06

Attuale outcome Romeo:

```text
scegliere un comportamento in base a un dato
```

Uso Python:

- dopo esercizi generali su boolean/`if`;
- missione breve B/C;
- non usarla per insegnare tutta la logica `elif/and/or` perché la specifica attuale è binaria.

## `romeo-y1-u15-ciclo-for` → PY2-04/M10

Attuale outcome:

```text
ripetere un numero noto di azioni
```

È perfettamente allineata a `for` vs ripetizione manuale.

Possibile adattamento didattico:

1. versione con quattro comandi duplicati;
2. refactor con `for`;
3. spiegazione del perché `for` comunica meglio l'intenzione.

## `romeo-y1-u16-ciclo-while` → PY2-04/M09

Attuale outcome:

```text
usare una condizione e assicurare la terminazione
```

Uso:

- trace contatore;
- individuazione condizione/aggiornamento;
- Debug Clinic ciclo non terminante.

Non deve diventare il principale esempio di validazione input: quello resta generale.

## `romeo-y1-u12-funzioni` → PY2-05/M13

Attuale outcome:

```text
racchiudere una sequenza in una funzione con parametro
```

Ottimo per mostrare estrazione/composizione di una sequenza robotica.

Limite:

- il movimento è soprattutto side effect;
- M13 deve insegnare esplicitamente `return` con esempi generali/non-Romeo.

Quindi Romeo completa, non sostituisce il nucleo delle funzioni produttive.

## `romeo-y1-u17-simulazione` → PY2-05/M16

Attuale outcome:

```text
usare traiettoria, clock ed eventi per il debug
```

È molto utile per rendere il debugging osservabile:

```text
previsione
→ esecuzione
→ traiettoria/event log
→ differenza
→ ipotesi sul bug
→ correzione
```

Uso consigliato anche come ponte a regression thinking.

## `romeo-y1-u19-missioni` → PY2-05/M15–M16

Attuale outcome:

```text
scomporre un percorso in segmenti verificabili
```

È un caso autentico per top-down decomposition.

Adattamento:

- prima piano funzioni/segmenti;
- poi implementazione;
- test/checkpoint di ogni segmento;
- refactor solo dopo comportamento corretto.

## `romeo-y1-u20-capstone` → scenario/reference, non Activity finale OOP diretta

L'Activity esistente misura:

```text
funzioni + cicli + condizioni + missione completa
```

È un buon capstone **procedurale**, ma PY2-10 deve misurare OOP.

Uso corretto:

- riusare/ispirarsi al tipo di missione/scenario;
- creare una nuova Activity F Python OOP;
- passare a `romeo.robot.Robot`;
- introdurre una classe dominio come `Missione` che compone `Robot`;
- mantenere la stessa forza del feedback simulato (traiettoria/eventi/final state).

Non dichiarare l'Activity y1-u20 esistente equivalente al capstone OOP.

---

# Transizione didattica Romeo lungo l'anno

## Fase R0 — dominio astratto

PY2-01:

```text
robot su griglia
```

solo come problema algoritmico.

Nessuna installazione/runtime richiesta.

## Fase R1 — API a funzioni

Da PY2-02/03:

```python
from romeo.easy import forward, left, stop
```

Gli studenti vedono una API semplice e leggibile.

## Fase R2 — controllo strutturato

PY2-03/04:

- `if` per scegliere comportamento;
- `for` per ripetizioni note;
- `while` con terminazione;
- composizioni controllate.

## Fase R3 — funzioni utente

PY2-05:

```text
avanza_per(...)
percorri_lato(...)
esegui_segmento(...)
```

Il programma smette di essere una lunga sequenza piatta.

## Fase R4 — debug deterministico

Usare:

- traiettoria;
- clock;
- event log;
- stato finale.

Il simulatore diventa strumento per confrontare previsione e comportamento.

## Fase R5 — dati solo quando servono

PY2-07/08:

Possibili waypoint/step:

```python
passi = [
    ("forward", 2),
    ("left", 90),
]
```

ma soltanto se aiuta il problema.

Non creare Activity Romeo per set/dict solo per "coprire Romeo in ogni UDA".

## Fase R6 — API a oggetti

PY2-10:

confronto:

```python
from romeo.easy import forward
```

vs

```python
from romeo.robot import Robot
robot = Robot(...)
robot.forward()
```

Non per affermare che OOP è sempre migliore, ma per osservare:

- un'istanza concreta;
- stato/configurazione dell'oggetto;
- metodi associati all'entità;
- invarianti/validazione;
- possibilità di passare l'oggetto come collaboratore.

## Fase R7 — composizione/capstone

Candidato:

```python
class Missione:
    def __init__(self, robot, ...):
        self.robot = robot
        ...
```

`Missione` usa/compone un `Robot`.

Non eredita da `Robot`.

---

# Capstone OOP Romeo — contratto candidato

## Outcome

Lo studente deve dimostrare OOP, non soltanto arrivare al target del simulatore.

Evidence minima:

1. modello delle responsabilità;
2. classe `Missione` o equivalente con responsabilità significativa;
3. `Robot` ricevuto come collaboratore;
4. `__init__` con stato utile;
5. almeno 2–3 metodi dominio;
6. una struttura dati soltanto se giustificata dalla missione;
7. almeno un invariante/validazione;
8. test/checkpoint;
9. missione simulata deterministica;
10. spiegazione di composizione vs alternative.

## Grading

Combinazione:

```text
romeo-sim
→ outcome di dominio (trajectory/events/final state)
+
rubric/manual evidence
→ responsabilità, composizione, spiegazione
+
P3 generic object behavior quando disponibile
→ contratti OOP deterministici selezionati
```

Non usare AST/regex per fingere di provare qualità OOP.

---

# Fallback se Romeo non è certificato

Il curriculum non deve fermarsi.

Activity F alternativa con stessi outcome:

- `Studente` + `Registro`;
- `Libro` + `Biblioteca`;
- `Prodotto` + `Inventario`.

Stessa rubrica OOP, diverso dominio.

Quando Romeo torna disponibile/certificato, può essere enrichment o capstone alternativo senza cambiare gli outcome curricolari.

---

# Vincoli di integrazione

## TheBitLab

Prima di assegnare Romeo come Activity core:

- runtime `romeo-sim` install/probe/launch/run certificato nel managed Classroom Environment;
- student/teacher asset separation verificata;
- simulator grading non dipende da hardware;
- stessa esperienza disponibile sui profili dichiarati o fallback equivalente.

Governance piattaforma:

- `python-docente#2`;
- `TheBitPoets/2cornot2c#753/#754`.

## Dipendenze

Non importare:

- networking;
- HTTP/FastAPI;
- WebSocket;
- camera/telepresence;
- eventi avanzati del Romeo year 2.

Questi argomenti appartengono a track successivi.

## Provenienza

Romeo resta repository canonico dei propri runtime/scenari/Activity.

`python-docente` conserva:

- mapping;
- adapter/Activity nuova soltanto dove l'outcome Python differisce;
- riferimenti pinned.

Evitare copie divergenti delle stesse fixture/solution.

---

# Decisione finale del mapping

Romeo entra **fortemente ma selettivamente** in:

```text
PY2-03 selezione
PY2-04 cicli
PY2-05 funzioni/debug/top-down
PY2-10 OOP/capstone
```

Entra soltanto opzionalmente in:

```text
PY2-02 primo codice
PY2-07/08 strutture dati quando una missione lo giustifica
```

Non viene forzato in:

```text
stringhe
set/dict come argomento fine a sé stesso
file I/O
```

Questo soddisfa il criterio: **Romeo rende concreti i concetti senza trasformare Python in un corso di robotica**.
