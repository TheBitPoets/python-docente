# M04 — record umano del rehearsal

> Template immutato: **PENDING / NOT RUN**  
> Copiare questo file in `evidence/m04-vm-gui/` prima di compilarlo.

## Identità dell'evidenza

```text
Data e ora:
Osservatore docente:
Profilo: [ ] Windows amd64 / VirtualBox  [ ] macOS arm64 / VMware
Contesto: [ ] host scolastico reale  [ ] host rappresentativo non scolastico
Commit python-docente:
Commit 2cornot2c:
Release classroom:
Report JSON associato:
SHA-256 del report JSON:
```

Non registrare nomi di studenti, account, hostname, indirizzi o altri dati
personali.

## A. Evidenza tecnica associata

- [ ] il report JSON esiste ed è quello prodotto direttamente dall'harness;
- [ ] `status` è `passed`;
- [ ] target, provider e architettura corrispondono all'host osservato;
- [ ] Python guest è `3.12.x`;
- [ ] sessione grafica e `lightdm` risultano attivi;
- [ ] starter `1/3` e modifica controllata `3/3`;
- [ ] `classroom_ready` resta `false` nel report tecnico.

## B. Percorso normale dello studente

- [ ] ambiente avviato dal launcher/percorso guidato normale;
- [ ] desktop grafico comparso senza comandi di riparazione fuori procedura;
- [ ] file manager utilizzabile;
- [ ] editor utilizzabile e testo leggibile;
- [ ] terminale utilizzabile;
- [ ] workspace condiviso `/lab` visibile;
- [ ] `main.py` apribile e modificabile;
- [ ] salvataggio visibile tra editor, terminale e host;
- [ ] modifica persistita dopo chiusura e riapertura del file;
- [ ] nessun asset `teacher/`, `solution/` o oracolo docente mostrato allo studente.

## C. Esecuzione M04 osservata

- [ ] lo starter è stato eseguito con input `2`, `3` e ha stampato `0`;
- [ ] è stata cambiata soltanto la riga del calcolo;
- [ ] caso `2`, `3` → `5`;
- [ ] caso `0`, `0` → `0`;
- [ ] caso `-4`, `10` → `6`;
- [ ] gli errori, se presenti, erano comprensibili o recuperabili con il runbook.

## D. Osservazione di usabilità

```text
Tempo avvio ambiente:
Tempo apertura workspace/editor:
Tempo completamento modifica e tre prove:
Aiuti necessari:
Punti di esitazione:
Problemi grafici/risoluzione/tastiera:
Problemi di persistenza/cartella condivisa:
Errori o codici mostrati:
```

## E. Decisione limitata a questa evidenza

Selezionare una sola voce:

- [ ] `PASS — technical + human workflow` per questo profilo e contesto;
- [ ] `PASS WITH LIMITATIONS — limited pilot candidate`;
- [ ] `CHANGES REQUIRED`;
- [ ] `BLOCKED / evidence incomplete`.

```text
Limitazioni o blocker:

Correzioni richieste:

Firma/identità del decision owner:
Data:
```

## Boundary obbligatorio

Questa decisione non approva automaticamente il Content Pack, non completa il
teacher sign-off generale e non dichiara `classroom ready` o `GO classroom`.
Un record vale soltanto per il profilo e il contesto realmente osservati.
