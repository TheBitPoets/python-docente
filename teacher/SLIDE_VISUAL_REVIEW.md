# Python secondo — Slide Visual Review

> Stato: **PENDING — da compilare su artifact realmente costruiti**  
> Questa scheda non può essere auto-spuntata da source QA o CI strutturale.

## Build candidate

```text
Source commit SHA: ______________________________
Build id: _______________________________________
Build manifest: dist/slides/python/build-manifest.json
Marp CLI reported: ______________________________
Node reported: __________________________________
Chromium reported: ______________________________
Container digest: sha256:119010dd06f8dd256b47f6479d9d3c83fcbfdcac5f873d0d03db5320f130cf87
Reviewer: _______________________________________
Date: ___________________________________________
```

## Campione minimo obbligatorio

| Modulo | Perché è nel campione | HTML | PDF | PPTX | Esito |
|---|---|---|---|---|---|
| M04 | REPL, codice, primo deck ricco | [ ] | [ ] | [ ] | PENDING |
| M11 | trace, tabelle, stato progressivo | [ ] | [ ] | [ ] | PENDING |
| M18 | testo, metodi, scelte | [ ] | [ ] | [ ] | PENDING |
| M22 | matrici, nesting, diagrammi | [ ] | [ ] | [ ] | PENDING |
| M26 | codice/file/errori | [ ] | [ ] | [ ] | PENDING |
| M30 | capstone, recap, densità finale | [ ] | [ ] | [ ] | PENDING |

Spuntare un formato soltanto dopo aver aperto **l'artifact generato**, non il Markdown sorgente.

---

# Criteri per ogni deck/formato

## Layout

- [ ] nessun testo tagliato o fuori canvas;
- [ ] nessun titolo sovrapposto;
- [ ] margini coerenti;
- [ ] tabelle contenute nella slide;
- [ ] liste non eccessivamente dense;
- [ ] nessuna slide bianca inattesa.

## Codice

- [ ] font leggibile da proiezione;
- [ ] righe non troncate;
- [ ] indentazione visibile;
- [ ] output/trace distinguibili dal codice;
- [ ] nessun blocco troppo lungo per una singola slide.

## Didattica

- [ ] il deck non è una copia compressa della lesson;
- [ ] il modello principale della slide è evidente;
- [ ] MUST MASTER non è confuso con GUIDED/ENRICHMENT;
- [ ] nessun detail teacher/grader interno è visibile;
- [ ] esempi e terminologia sono coerenti con lesson/runbook.

## PDF

- [ ] numero pagine coerente con il manifest;
- [ ] proporzioni 16:9 coerenti;
- [ ] testo/codice nitidi;
- [ ] nessuna differenza sistemica rispetto all'HTML.

## PPTX

- [ ] file apre in Microsoft PowerPoint target;
- [ ] numero slide coerente;
- [ ] font/layout accettabili;
- [ ] immagini/asset presenti;
- [ ] comportamento di editabilità osservato e documentato;
- [ ] nessuna promessa di editabilità superiore a ciò che è stato verificato.

Consumer aggiuntivo facoltativo:

```text
[ ] LibreOffice Impress spot-check
```

---

# Registro problemi

| ID | Modulo/formato | Problema | Sistemico? | Fix nel Markdown/toolchain | Re-review |
|---|---|---|---|---|---|
| VR-01 | | | | | |
| VR-02 | | | | | |
| VR-03 | | | | | |

Se un problema è sistemico (font, overflow, theme, renderer), estendere la review a tutti i deck potenzialmente coinvolti prima del sign-off.

---

# Decisione visual layer

```text
[ ] PASS — campione obbligatorio verificato e nessun blocker aperto
[ ] PASS WITH DOCUMENTED LIMITATIONS — limitazioni PPTX/font note e accettate
[ ] FAIL — correzioni necessarie
```

Note:

```text
____________________________________________________________
____________________________________________________________
____________________________________________________________
```

Questa decisione chiude soltanto il **visual slide layer**. Non equivale a teacher sign-off generale, Content Pack approval o GO classroom.
