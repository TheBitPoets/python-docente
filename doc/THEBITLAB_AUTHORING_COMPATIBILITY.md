# Compatibilità con la dashboard docente TheBitLab

## Conclusione

La struttura di `python-docente` **non impedisce** l'authoring tramite dashboard docente.

Il modello scelto è anzi il target desiderato:

```text
repo corso / Course Workspace
  -> Markdown + fonti
  -> Content Pack v1
  -> Course Design
  -> Activity 1.0
  -> dashboard docente
  -> Git diff/review
  -> freeze
  -> Course Bundle release
```

## Capacità già presenti in TheBitLab

La Course Board supporta:

```text
python scripts/course_board_server.py --root <course-workspace>
```

Il parametro `--root` fa sì che la dashboard usi direttamente il repository del corso come data root.

Per `python-docente`, dopo un checkout locale, il flusso di sviluppo sarà concettualmente:

```bash
python <path-2cornot2c>/scripts/course_board_server.py \
  --root <path-python-docente>
```

La UI continua ad essere servita da TheBitLab, mentre i dati mutabili sono quelli del corso:

```text
python-docente/
  doc/course_design.json
  doc/course_designs/
  doc/calendars/
  activities/
  content/
```

## Cosa può modificare oggi la Course Board

Il Course Design corrente può essere:

- aperto;
- modificato;
- salvato;
- duplicato con nome;
- archiviato;
- impostato come corrente;
- associato a calendari scolastici;
- aggiornato con stato/ore/date reali durante l'anno.

La board può inoltre gestire fonti Markdown:

- locali;
- GitHub;
- GitLab;

con preview, commit resolution e provenienza.

## Stato di python-docente

Il branch di progettazione contiene già:

```text
doc/course_design.json
content/python/content-pack.json
activities/python/
```

`doc/course_design.json` contiene:

- track secondo anno;
- 33 settimane;
- 3 ore/settimana;
- UDA e checkpoint;
- sorgenti Markdown esplicite.

Gli `items` delle UDA sono volutamente vuoti nella fase di design. Verranno popolati dalla dashboard o dagli script quando le lesson canoniche diventeranno fonti stabili.

## Content Pack e Course Design

Il Content Pack usa:

```text
thebitlab.content-pack.v1
```

Le sue `sources` sono progettate per essere proiettate deterministicamente nel contratto `CourseDesign.sources`.

Regola di coerenza:

> le fonti indicizzabili dichiarate dal Content Pack e quelle esposte alla Course Board devono rappresentare lo stesso catalogo logico.

Il Content Pack conserva metadati più ricchi di provenance/licenza/ownership; il Course Design conserva la composizione didattica e il catalogo necessario alla board.

## Course Bundle: limite attuale e boundary corretto

La Course Board **non apre ancora un Course Bundle completo come progetto editabile**.

Questo non deve essere risolto rendendo il bundle mutabile.

Regola:

```text
Course Workspace = authoring mutabile
Course Bundle    = release immutabile
```

Per modificare un corso pubblicato si riapre il workspace sorgente del bundle e si produce una nuova release.

Il lavoro piattaforma è tracciato in:

- `TheBitPoets/2cornot2c#755`;
- `TheBitPoets/2cornot2c` PR `#754`;
- `doc/architecture/course-workspace-authoring-roundtrip.md` nel branch di design TheBitLab.

## Git e dashboard

Dashboard e Git non sono due modalità alternative.

```text
dashboard salva file
        ↓
Git vede la modifica
        ↓
diff / review / commit / PR
```

Un coding agent può modificare gli stessi file e la board deve poterli rileggere.

Il round-trip da preservare è:

```text
board -> file -> Git -> file -> board
```

senza conversioni lossy.

## Criterio di accettazione per python-docente

Prima del Content Pack 1.0 approvato verificare realmente:

1. checkout pulito di `python-docente`;
2. avvio Course Board con `--root` sul checkout;
3. apertura di `doc/course_design.json`;
4. indicizzazione delle fonti locali dichiarate;
5. modifica innocua di una UDA;
6. salvataggio;
7. Git diff limitato alla modifica prevista;
8. riapertura della board con contenuto identico;
9. validazione Content Pack/Course Design;
10. ripristino/commit della modifica di test.

Finché questo smoke non viene eseguito non dichiarare il round-trip fisicamente collaudato; l'architettura e il supporto server-side sono però già presenti.
