"""Build the figure backlog from lesson-specific presentation records; --check is read-only."""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "assets/python/visual-system"


def anchor(title: str) -> str:
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def outputs() -> dict[Path, str]:
    records = json.loads((ROOT / "config/course-presentation.json").read_text(encoding="utf-8"))["modules"]
    objects = json.loads((KIT / "component-inventory.json").read_text(encoding="utf-8"))
    known = {item["id"] for item in objects}
    figures = []
    rows = []
    for record in records:
        n = record["module"]
        lesson = next((ROOT / "content/python").glob(f"{n:02d}_*.md"))
        text = lesson.read_text(encoding="utf-8")
        headings = re.findall(r"^#{1,2} (.+)$", text, re.M)
        heading = next(h for h in headings if h.startswith(f"{record['section']}. "))
        components = ["tpsi-" + name for name in record["objects"]]
        if set(components) - known:
            raise ValueError(f"Unknown components in M{n:02d}")
        target = lesson.relative_to(ROOT).as_posix() + "#" + anchor(heading)
        figure = {
            "id": f"py-m{n:02d}-01", "module": f"M{n:02d}", "title": record["figure"],
            "lesson_section": target, "purpose": record["visual"], "components": components,
            "priority": "P1" if n in (0, 2, 3, 4, 6, 9, 13, 17, 20, 21, 22, 27, 28, 29) else "P2",
            "status": "prototype-not-in-lesson" if n == 21 else "planned",
            "asset": "assets/python/21-alias-copia.svg" if n == 21 else None,
            "alt_draft": record["visual"], "caption_draft": record["figure"] + ". " + record["visual"],
            "existing_images": len(re.findall(r"<img\b|!\[", text)),
            "existing_text_blocks": len(re.findall(r"^```text\s*$", text, re.M)),
        }
        figures.append(figure)
        rows.append('<tr>' + ''.join(f'<td>{cell}</td>' for cell in [
            f'<a href="../{escape(target, quote=True)}">M{n:02d} — {escape(heading)}</a>',
            escape(record["figure"]), escape(record["visual"]),
            ', '.join(f'<code>{c}</code>' for c in components),
            f'{figure["priority"]}; ' + ('esempio composto, non inserito' if n == 21 else 'da costruire'),
            f'{figure["existing_images"]} immagini; {figure["existing_text_blocks"]} blocchi text',
        ]) + '</tr>')
    # M00 is deliberately richer than the one-figure-per-module baseline:
    # each conceptual boundary gets its own readable replacement for an ASCII sketch.
    m00_extras = [
        ("py-m00-02", "m00-input-output.svg", "Input, trasformazione, output e vincoli", "3. Input, output e vincoli", "tpsi-value,tpsi-function,tpsi-decision", "Il prezzo e il pagamento entrano nella trasformazione del resto; il vincolo controlla se il calcolo è valido."),
        ("py-m00-03", "m00-passi-operativi.svg", "Passi operativi", "5. I passi devono essere operativi", "tpsi-step,tpsi-error", "Confronto fra istruzione vaga e passi osservabili con dati, trasformazione e risultato."),
        ("py-m00-04", "m00-test-errori.svg", "Test e diagnosi degli errori", "6. Un esempio non dimostra tutto", "tpsi-document,tpsi-error,tpsi-terminal", "Casi normale, limite e ordine invertito collegati ai tre livelli della diagnosi."),
    ]
    lesson = next((ROOT / "content/python").glob("00_*.md"))
    for ident, asset, title, section, component_text, purpose in m00_extras:
        components = [f"{part}" for part in component_text.split(",")]
        target = lesson.relative_to(ROOT).as_posix() + "#" + anchor(section)
        figures.append({"id": ident, "module": "M00", "title": title, "lesson_section": target, "purpose": purpose, "components": components, "priority": "P1", "status": "prototype-realized", "asset": f"assets/python/{asset}", "alt_draft": purpose, "caption_draft": title, "existing_images": 4, "existing_text_blocks": 0})

    m01_extras = [
        ("py-m01-02", "m01-specifica.svg", "Specifica come contratto", "1. Una specifica è un contratto da capire", "tpsi-document,tpsi-value,tpsi-decision", "La consegna sui prezzi definisce input e tre output possibili."),
        ("py-m01-03", "m01-decomposizione.svg", "Decomposizione in passi", "2. Decomporre non significa complicare", "tpsi-step", "Cinque passi collegano acquisizione, confronto, scelta e comunicazione."),
        ("py-m01-04", "m01-trace-stato.svg", "Trace e stato", "7. Lo stato cambia nel tempo", "tpsi-value,tpsi-decision", "Il trace mostra come i valori cambiano durante l'esecuzione."),
        ("py-m01-05", "m01-ordine-test.svg", "Ordine dei passi e test", "8. Ordine dei passi", "tpsi-decision", "Il valore viene calcolato prima dell'output e i test coprono i casi principali."),
        ("py-m01-06", "m01-selezione-due-rami.svg", "Selezione semplice: due rami", "4.1 Selezione a più casi: ALTRIMENTI SE", "tpsi-terminator,tpsi-io,tpsi-decision,tpsi-step", "Un confronto sul prezzo sceglie fra due assegnamenti; i rami si ricongiungono dopo FINE SE."),
        ("py-m01-07", "m01-selezione-tre-casi.svg", "Due condizioni, tre casi", "4.1 Selezione a più casi: ALTRIMENTI SE", "tpsi-terminator,tpsi-io,tpsi-decision", "Il secondo confronto fra A e B viene raggiunto solo dal ramo falso del primo; un solo output viene eseguito."),
        ("py-m01-08", "m01-selezione-punteggio.svg", "Punteggio e ordine delle condizioni", "4.1 Selezione a più casi: ALTRIMENTI SE", "tpsi-terminator,tpsi-io,tpsi-decision", "Le soglie 90 e 60 distinguono tre fasce: dopo la prima condizione vera le altre vengono saltate."),
    ]
    for ident, asset, title, section, component_text, purpose in m01_extras:
        components = component_text.split(",")
        target = f"content/python/01_DAL_PROBLEMA_AI_PASSI.md#{anchor(section)}"
        figures.append({"id": ident, "module": "M01", "title": title, "lesson_section": target, "purpose": purpose, "components": components, "priority": "P1", "status": "prototype-realized", "asset": f"assets/python/{asset}", "alt_draft": purpose, "caption_draft": title, "existing_images": 0, "existing_text_blocks": 1})
        animated = asset.startswith('m01-selezione-')
        if animated:
            figures[-1]['animated_asset'] = f"assets/python/{asset.removesuffix('.svg')}-anime.svg"
        rows.append('<tr>' + ''.join(f'<td>{cell}</td>' for cell in [f'<a href="../{escape(target, quote=True)}">M01 — {escape(section)}</a>', escape(title), escape(purpose), ', '.join(f'<code>{c}</code>' for c in components), 'P1; prototipo realizzato', 'animazione e schema fermo' if animated else 'immagine inserita']) + '</tr>')
    audit = '''# Audit delle immagini del corso Python

<p align="justify">Audit del 16 settembre 2026: tutte le 31 lezioni canoniche M00–M30. La lettura di obiettivi, spiegazioni, schemi testuali e attività individua una prima figura principale per ciascun modulo. L'inventario automatico conta i riferimenti a immagini e i blocchi <code>text</code>; questi ultimi comprendono anche output e pseudocodice, non soltanto schemi da sostituire.</p>

<p align="justify"><strong>Esito:</strong> 31 figure pianificate, 25 oggetti SVG disponibili, tre cataloghi e un esempio composto su alias e copia. Le figure pianificate non sono immagini già presenti nelle lezioni. Il lavoro corrente prepara la loro costruzione; la revisione dei contenuti e l'inserimento delle figure definitive costituiscono la fase successiva.</p>

## Fonti effettivamente consultate

<ul>
<li><a href="https://github.com/TheBitPoets/tpsi-quinto-docente/blob/main/content/tpsi5/STYLE_GUIDE.md">TPSI quinto: standard editoriale</a> e <a href="https://github.com/TheBitPoets/tpsi-quinto-docente/blob/main/assets/tpsi5/visual-system/README.md">Visual System</a>, letti tramite il connettore GitHub il 16 settembre 2026.</li>
<li><a href="https://github.com/TheBitPoets/tpsi-quarto-docente/blob/main/doc/VISUAL_AUDIT.md">TPSI quarto: audit</a>, guida editoriale, componenti, token, catalogo e generatori, letti dal checkout locale nella stessa data.</li>
<li><a href="https://github.com/TheBitPoets/2cornot2c/blob/main/README.md#introduzione">2cornot2c: README</a>, letto dal checkout locale per cornice completa, icone e paragrafi allineati.</li>
<li>Le 31 dispense Python e i loro obiettivi sono la fonte delle collocazioni e delle relazioni proposte. I libri elencati nel Content Pack non sono stati consultati per questo audit e non vengono dichiarati confrontati visivamente.</li>
</ul>

## Priorità e grammatica

<p align="justify">P1: modelli in cui flussi, riferimenti o stati possono generare interpretazioni errate. P2: confronti, scelte e sintesi da costruire dopo le figure fondative. Non aggiungere illustrazioni decorative: una figura deve chiarire una relazione precisa. Codice, output, trace table numeriche e checklist restano testo copiabile. Il backlog copre tutti i moduli, ma non pretende di esaurire le eventuali figure necessarie dopo la revisione dei contenuti.</p>

<p align="justify">Distinguere frecce di controllo, ritorno di un risultato e riferimenti fra nomi e oggetti: ogni scena deve dichiararne il significato. Non rappresentare i nomi Python come scatole che contengono direttamente tutti gli oggetti, non attribuire ordine ai set e non rappresentare una copia superficiale come duplicazione ricorsiva. Per i flow chart usare le forme canoniche e indicare sempre i rami della decisione.</p>

## Registro per tutte le lezioni

<table align="center">
<thead><tr><th>Collocazione</th><th>Figura proposta</th><th>Relazione da rendere visibile</th><th>Oggetti</th><th>Priorità e stato</th><th>Inventario attuale</th></tr></thead>
<tbody>
''' + '\n'.join(rows) + '''
</tbody>
</table>

## Figure complementari da valutare nella revisione dei contenuti

<ul>
<li>M02–M03: legenda dei simboli, annidamento e trace sincronizzata con il diagramma.</li>
<li>M04–M05: input testuale → conversione → calcolo; confronto fra stampa e restituzione.</li>
<li>M07–M10: condizioni composte, copertura dei confini, sentinella esclusa dai dati e scelta for/while.</li>
<li>M17–M20: immutabilità, ricerca assente rispetto a indice zero, append rispetto a extend.</li>
<li>M21–M22: seconda figura sulla copia superficiale di strutture annidate e tupla contenente una lista mutabile.</li>
<li>M24–M26: chiave mancante e default; raggruppamento uno-a-molti; apertura, uso e chiusura della risorsa file.</li>
<li>M27–M30: self nella chiamata, indipendenza delle istanze, separazione dominio/I/O e tracciabilità requisito → test.</li>
</ul>

## Collezione e costruzione

<p align="justify">La <a href="../assets/python/visual-system/README.md">collezione grafica</a> contiene i cataloghi e le istruzioni di composizione. Il <a href="../assets/python/visual-system/figure-index.json">registro JSON</a> conserva sezione, scopo, priorità, componenti, bozza di alt/didascalia e stato. La bozza di alt va adattata alla scena effettivamente realizzata prima dell'inserimento. L'<a href="../assets/python/21-alias-copia.svg">esempio M21</a> verifica il riuso di nomi, sequenze e riferimenti, senza sostituire ancora la spiegazione nella dispensa.</p>

<p align="justify">Il <a href="../scripts/build_visual_audit.py">generatore dell'audit</a> legge <code>config/course-presentation.json</code> e le lezioni; rigenera questo documento e il registro. Usare <code>python scripts/build_visual_audit.py --check</code> per rilevare disallineamenti senza scrivere. Le verifiche strutturali non costituiscono approvazione didattica delle figure future.</p>
'''
    return {ROOT / "doc/VISUAL_AUDIT.md": audit, KIT / "figure-index.json": json.dumps(figures, ensure_ascii=False, indent=2) + "\n"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, text in outputs().items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(text, encoding="utf-8", newline="\n")
    if stale:
        print("Audit da rigenerare: " + ", ".join(stale))
        return 1
    print("OK: audit e registro di 31 figure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
