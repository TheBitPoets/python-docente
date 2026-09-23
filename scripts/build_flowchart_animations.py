"""Declarative M01 traces, built from the static SVGs by build_course_diagrams.

No JavaScript, external resources or rendering dependency is embedded in an image.
Each CSS frame shows one executed step; a new case starts with an empty trace.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

NS = '{http://www.w3.org/2000/svg}'
HIGHLIGHT = '#fbbf24'
STEP_SECONDS = 2
CASES = {
    'm01-selezione-due-rami': [120, 80, 100],
    'm01-selezione-tre-casi': [(8, 3), (3, 8), (5, 5)],
    'm01-selezione-punteggio': [95, 75, 40, 90, 60],
}


def execution(name: str, value) -> tuple[str, list[tuple[str, str | None, str]]]:
    """Return input and (node, incoming edge, explanation) in execution order."""
    simple = name == 'm01-selezione-due-rami'
    if simple:
        inputs = f'prezzo: {value}'
        first = value > 100
        first_test = f'{value} > 100'
        branch = '1' if first else '2'
        result = f'Assegna sconto ← {10 if first else 0}.'
    elif name == 'm01-selezione-tre-casi':
        a, b = value
        inputs = f'A: {a}; B: {b}'
        first, second = a > b, b > a
        first_test, second_test = f'{a} > {b}', f'{b} > {a}'
        branch = '1' if first else ('2' if second else '3')
        result = f'Mostra A: {a}.' if first else (f'Mostra B: {b}.' if second else 'Mostra “uguali”.')
    else:
        inputs = f'punteggio: {value}'
        first, second = value >= 90, value >= 60
        first_test, second_test = f'{value} >= 90', f'{value} >= 60'
        branch = '1' if first else ('2' if second else '3')
        result = f'Mostra “fascia {dict(zip("123", ["alta", "media", "bassa"]))[branch]}”.'

    steps = [('start', None, 'Inizia una nuova esecuzione: il percorso precedente si azzera.'),
             ('read', 'start-read', f'Leggi {inputs}.'),
             ('test-1', 'read-test', f'{first_test} → {"VERO" if first else "FALSO"}.')]
    incoming = 'test-1-true' if first else 'test-1-false'
    if not simple and not first:
        steps.append(('test-2', incoming, f'{second_test} → {"VERO" if second else "FALSO"}.'))
        incoming = 'test-2-true' if second else 'test-2-false'
    steps.append((f'output-{branch}', incoming, result))
    steps.append(('merge', f'output-{branch}-merge',
                  'FINE SE: il secondo confronto è stato saltato.' if first and not simple
                  else 'FINE SE: i rami si ricongiungono; gli altri blocchi non vengono eseguiti.'))
    steps.append(('end', 'merge-end', f'Fine di questa esecuzione. {result}'))
    return inputs, steps


def label(parent: ET.Element, x: int, y: int, message: str, size: int = 30):
    node = ET.SubElement(parent, NS + 'text', {
        'x': str(x), 'y': str(y), 'font-size': str(size),
        'font-family': 'Arial, sans-serif', 'fill': '#f8fafc',
    })
    node.text = message


def outline(source: ET.Element, active: bool = False) -> ET.Element:
    node = deepcopy(source)
    node.attrib.pop('id', None)
    node.set('fill', 'none')
    node.set('stroke', HIGHLIGHT)
    node.set('stroke-width', '10' if active else '6')
    if 'marker-end' in node.attrib:
        node.set('marker-end', 'url(#trace-arrow)')
    if active:
        node.set('stroke-dasharray', '18 8')
    return node


def animated_svg(name: str, payload: bytes) -> bytes:
    root = ET.fromstring(payload)
    nodes = {node.get('id'): node for node in root.iter() if node.get('id')}
    root.find(NS + 'title').text += ' — esecuzioni animate'
    root.find(NS + 'desc').text += (
        ' Animazione passo per passo di tutti i rami con input concreti. '
        'Le linee dorate indicano il percorso già eseguito; il bordo tratteggiato '
        'indica il passo corrente. Ogni caso riparte da INIZIO.'
    )
    # Keep the original explanatory text as the no-animation/reduced-motion fallback.
    for node in root.iter(NS + 'text'):
        if node.get('y') in ('148', '1032'):
            node.set('class', 'static-caption')
    definitions = ET.SubElement(root, NS + 'defs')
    marker = ET.SubElement(definitions, NS + 'marker', {
        'id': 'trace-arrow', 'viewBox': '0 0 10 10', 'refX': '9', 'refY': '5',
        'markerWidth': '4', 'markerHeight': '4', 'orient': 'auto',
    })
    ET.SubElement(marker, NS + 'path', {'d': 'M0 0 L10 5 L0 10 Z', 'fill': HIGHLIGHT})
    traces = [execution(name, value) for value in CASES[name]]
    total = sum(len(steps) for _, steps in traces)
    duration = total * STEP_SECONDS
    css = ['.trace-frame { visibility: hidden; }',
           '@media (prefers-reduced-motion: no-preference) {',
           '.static-caption { visibility: hidden; }']
    frame_index = 0
    for case_index, (inputs, steps) in enumerate(traces, 1):
        visited = []
        for step_index, (node_id, edge_id, explanation) in enumerate(steps, 1):
            if edge_id:
                visited.append(nodes['edge-' + edge_id])
            current = nodes['node-' + node_id]
            frame_id = f'trace-{frame_index}'
            frame = ET.SubElement(root, NS + 'g', {
                'id': frame_id, 'class': 'trace-frame',
                'data-case': str(case_index), 'data-step': node_id,
            })
            label(frame, 64, 148, f'CASO {case_index}/{len(traces)}  |  {inputs}  |  PASSO {step_index}/{len(steps)}', 32)
            label(frame, 64, 1032, explanation)
            for previous in visited:
                frame.append(outline(previous))
            frame.append(outline(current, active=True))
            visited.append(current)
            start, end = 100 * frame_index / total, 100 * (frame_index + 1) / total
            # step-end switches exactly at the boundaries, without fades or flashes.
            keys = ([] if frame_index == 0 else ['0% { visibility: hidden; }'])
            keys += [f'{start:.8f}% {{ visibility: visible; }}', f'{end:.8f}% {{ visibility: hidden; }}']
            if frame_index + 1 < total:
                keys.append('100% { visibility: hidden; }')
            css += [f'#{frame_id} {{ animation: frame-{frame_index} {duration}s step-end infinite; }}',
                    f'@keyframes frame-{frame_index} {{ {" ".join(keys)} }}']
            frame_index += 1
    css.append('}')
    ET.SubElement(root, NS + 'style').text = '\n'.join(css)
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='utf-8', xml_declaration=True) + b'\n'


def planned_animations(static_outputs: list[tuple[Path, bytes]]) -> list[tuple[Path, bytes]]:
    return [(path.with_stem(path.stem + '-anime'), animated_svg(path.stem, payload))
            for path, payload in static_outputs if path.stem in CASES]
