"""Check that M01 animations execute one branch and skip later conditions."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_flowchart_animations import CASES, NS, execution


def main():
    expected = {
        'm01-selezione-due-rami': [
            ('output-1', 'test-1-true', 'sconto ← 10'),
            ('output-2', 'test-1-false', 'sconto ← 0'),
            ('output-2', 'test-1-false', 'sconto ← 0'),
        ],
        'm01-selezione-tre-casi': [
            ('output-1', 'test-1-true', 'Mostra A: 8'),
            ('output-2', 'test-2-true', 'Mostra B: 8'),
            ('output-3', 'test-2-false', 'Mostra “uguali”'),
        ],
        'm01-selezione-punteggio': [
            ('output-1', 'test-1-true', 'fascia alta'),
            ('output-2', 'test-2-true', 'fascia media'),
            ('output-3', 'test-2-false', 'fascia bassa'),
            ('output-1', 'test-1-true', 'fascia alta'),
            ('output-2', 'test-2-true', 'fascia media'),
        ],
    }
    for name, outcomes in expected.items():
        svg = ET.parse(ROOT / f'assets/python/{name}-anime.svg').getroot()
        frames = [node for node in svg if node.get('class') == 'trace-frame']
        assert len(CASES[name]) == len(outcomes)
        for case_number, (value, (output, edge, message)) in enumerate(zip(CASES[name], outcomes), 1):
            _, steps = execution(name, value)
            sequence = [node for node, _, _ in steps]
            executed = [(node, incoming, text) for node, incoming, text in steps if node.startswith('output-')]
            assert len(executed) == 1 and executed[0][:2] == (output, edge)
            assert message in executed[0][2]
            assert sequence[:3] == ['start', 'read', 'test-1']
            assert sequence[-2:] == ['merge', 'end']
            assert ('test-2' in sequence) == (name != 'm01-selezione-due-rami' and output != 'output-1')
            case_frames = [frame for frame in frames if frame.get('data-case') == str(case_number)]
            assert [frame.get('data-step') for frame in case_frames] == sequence
            # A fresh execution must not retain outlines/arrows from the previous case.
            assert len(case_frames[0]) == 3  # two labels and only the INIZIO outline
            assert all(len([n for n in frame if n.get('stroke-dasharray')]) == 1 for frame in case_frames)
        css = svg.find(NS + 'style').text
        assert 'prefers-reduced-motion: no-preference' in css
        assert '.trace-frame { visibility: hidden; }' in css
        assert not list(svg.iter(NS + 'script'))
    print('PASS: 11 animated executions cover every branch and boundaries 100, 90, 60; one output per case')


if __name__ == '__main__':
    main()
