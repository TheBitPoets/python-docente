# M04 — rehearsal Classroom Environment reale

> Stato: **READY TO RUN / PHYSICAL EVIDENCE PENDING**  
> Questo runbook non certifica automaticamente il corso e non viene compilato dalla CI.

## Obiettivo

Verificare la prima Activity Python M04 nella box `vm-gui` realmente rilasciata e
osservare separatamente il percorso umano usato da uno studente.

Le evidenze restano distinte:

| Evidenza | Come si ottiene | Cosa dimostra | Cosa non dimostra |
| --- | --- | --- | --- |
| report JSON tecnico | `tests/m04_vm_gui_rehearsal.py` | box/provider/release, Python 3.12, GUI attiva, starter 1/3, modifica 3/3 | launcher normale, usabilità, host scolastico, teacher sign-off |
| record umano | copia di `teacher/M04_CLASSROOM_REHEARSAL_RECORD.md` | ciò che il docente ha realmente osservato | certificazione dei profili non provati |
| teacher sign-off generale | `teacher/TEACHER_SIGNOFF_CHECKLIST.md` | giudizio didattico finale | non sostituisce i gate tecnici |

Un `status: passed` nel report JSON significa soltanto **technical vm-gui
execution PASS**.

## Profili supportati

| Host | Provider | Target | Stato richiesto |
| --- | --- | --- | --- |
| Windows amd64 | VirtualBox | `windows-amd64-virtualbox` | release attiva `1.0.0` |
| macOS Apple Silicon | VMware Fusion | `macos-arm64-vmware` | release attiva `1.0.0` |

Un'esecuzione prova soltanto il profilo indicato nel proprio report. Per
certificare l'intera matrice `vm-gui` attualmente supportata servono entrambi i
profili; un pilot limitato deve dichiarare esplicitamente il solo profilo provato.

## 1. Precondizioni

1. Il branch `agent/course-architecture` di `python-docente` deve essere pulito e
   aggiornato.
2. Il checkout `2cornot2c` usato dall'installer deve essere pulito e sul commit
   indicato da `config/p1-canary-profile.json`.
3. Eseguire prima il percorso normale **Ambiente 2cornot2c → Installa, completa
   o ripara**. Devono esistere `.classroom-box` e `.classroom-provider`.
4. Su macOS avviare almeno una volta VMware Fusion e accettare licenza e
   autorizzazioni.
5. Non usare una box Bento legacy o un provider diverso da quello selezionato
   dall'installer.

Il pin `2cornot2c` attuale è:

```text
736bbfddfb79e431b9dedbfd1d877f06aa8b02b5
```

Controllarlo prima della prova con:

```bash
git -C /percorso/2cornot2c rev-parse HEAD
```

Se il checkout installato è pulito ma si trova su un commit successivo,
annotare prima il branch corrente e portare temporaneamente **quella stessa
directory** sul pin. In questo modo restano associati i marker e lo stato della
VM installata:

```bash
git -C /percorso/2cornot2c status --short --branch
git -C /percorso/2cornot2c switch --detach 736bbfddfb79e431b9dedbfd1d877f06aa8b02b5
```

Non copiare o inventare `.classroom-box` e `.classroom-provider`. Dopo aver
salvato tutte le evidenze, ripristinare il branch annotato con `git switch
<branch>`.

Il rehearsal interrompe subito l'esecuzione se trova modifiche tracciate nei due
checkout, un commit `2cornot2c` diverso dal pin, una box/provider non coerente o
una release diversa da quella attiva.

## 2. Rehearsal tecnico registrato

Creare un nome nuovo per ogni tentativo; un report precedente non viene mai
sovrascritto.

### Windows PowerShell

Eseguire dalla cartella `python-docente` sostituendo il percorso di
`2cornot2c` e il timestamp nel nome del file:

```powershell
python tests/m04_vm_gui_rehearsal.py `
  --platform C:\percorso\2cornot2c `
  --report evidence\m04-vm-gui\windows-amd64-AAAAMMGG-HHMM.json `
  --keep-workspace
```

### macOS Apple Silicon

Eseguire dalla cartella `python-docente`:

```bash
python3 tests/m04_vm_gui_rehearsal.py \
  --platform /percorso/2cornot2c \
  --report evidence/m04-vm-gui/macos-arm64-AAAAMMGG-HHMM.json \
  --keep-workspace
```

L'harness usa automaticamente:

- `.vagrant` per VirtualBox/Windows;
- `.vagrant-vmware` tramite `VAGRANT_DOTFILE_PATH` per VMware/macOS.

Un esito valido termina con `status: passed` e una riga `REPORT:`. Se il comando
fallisce, conservare l'errore nel record umano, ma non creare né rinominare a
mano un JSON come se fosse un PASS.

## 3. Osservazione umana nel percorso studente

Questa fase è manuale perché il suo oggetto è l'esperienza reale, non un altro
test automatico.

1. Chiudere la VM senza distruggerla.
2. Avviarla dal percorso normalmente esposto allo studente:
   - Windows: **Ambiente 2cornot2c → Avvia l'ambiente**;
   - macOS: percorso guidato `./scripts/setup-vm.sh --vmware`.
3. Verificare che il desktop grafico sia visibile e leggibile senza interventi
   tecnici straordinari.
4. Nel file manager aprire
   `/lab/python-docente-m04-vm-gui-rehearsal/main.py`.
5. Verificare che il file sia stato ripristinato dallo script alla riga
   `risultato = 0` e che il solo file del rehearsal visibile sia `main.py`.
6. Aprire un terminale nel desktop della VM ed eseguire:

   ```bash
   cd /lab/python-docente-m04-vm-gui-rehearsal
   python3 main.py
   ```

7. Inserire `2` e `3` su due righe: lo starter deve stampare `0`.
8. Nell'editor cambiare soltanto:

   ```text
   risultato = 0
   ```

   in:

   ```text
   risultato = primo + secondo
   ```

9. Salvare, rieseguire e verificare i tre casi:

   | Input | Output |
   | --- | --- |
   | `2`, `3` | `5` |
   | `0`, `0` | `0` |
   | `-4`, `10` | `6` |

10. Chiudere e riaprire il file dalla cartella condivisa, verificando che la
    modifica sia persistita.
11. Annotare tempi, punti di esitazione, errori, leggibilità e qualunque aiuto
    necessario nel record umano.

Non guidare il partecipante attraverso un percorso diverso da quello previsto
per la classe. Un aiuto necessario non annulla l'evidenza: va registrato perché
può trasformarsi in una correzione del runbook o in un blocker.

## 4. Registrazione

Per ogni host copiare il template senza modificarne l'originale:

```text
teacher/M04_CLASSROOM_REHEARSAL_RECORD.md
→ evidence/m04-vm-gui/<profilo>-<data>-human.md
```

Nel record indicare il report JSON associato e il suo SHA-256. Non inserire nomi
di studenti, account, indirizzi, hostname o altri dati personali.

Calcolo SHA-256:

```powershell
Get-FileHash evidence\m04-vm-gui\<report>.json -Algorithm SHA256
```

```bash
shasum -a 256 evidence/m04-vm-gui/<report>.json
```

## 5. Criterio decisionale

- **Technical profile PASS**: JSON valido, ma record umano ancora assente.
- **Human workflow observed**: record compilato; vale soltanto per host e
  contesto dichiarati.
- **Real school-host evidence**: selezionabile soltanto se la prova è avvenuta
  realmente su una macchina scolastica rappresentativa.
- **Limited pilot candidate**: possibile solo per i profili realmente provati e
  con eventuali limitazioni esplicite.
- **Full classroom GO**: non viene concesso da questo rehearsal. Richiede i gate
  rimanenti, il teacher sign-off generale e una decisione esplicita separata.

La issue `#7` non va chiusa sulla sola base del report JSON tecnico.
