"""Presentation contract: HTML, local navigation, canonical orientation and SVG kit."""
from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import format_python_lessons as fmt
import build_course_diagrams as diagrams
import build_visual_audit as audit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img":
            assert attrs.get("alt", "").strip(), "image without alt"
            self.images.append(attrs["src"])
        if tag == "p":
            assert attrs.get("align") in ("justify", "center"), "paragraph alignment missing"
        if tag == "table":
            assert attrs.get("align") == "center", "table alignment missing"


def check_link(path, target):
    parts = urlsplit(target)
    if parts.scheme or parts.netloc:
        return
    dest = (path.parent / unquote(parts.path)).resolve() if parts.path else path
    assert dest.exists(), f"{path.name}: missing {target}"
    if parts.fragment and dest.suffix == ".md":
        source = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", dest.read_text(encoding="utf-8"), flags=re.M | re.S)
        anchors = {audit.anchor(h) for h in re.findall(r"^#{1,6} (.+)$", source, re.M)}
        anchors.update(re.findall(r'<a\s+id=[\"\']([^\"\']+)', source))
        assert unquote(parts.fragment) in anchors, f"{path.name}: missing anchor {target}"


def main():
    lessons = fmt.DEFAULT_LESSONS
    assert len(lessons) == 31
    icons = (128506, 128736, 127919, 128257, 128064, 10145, 128279)
    for path in lessons:
        body = path.read_text(encoding="utf-8")
        assert not fmt.validation_errors(body), (path, fmt.validation_errors(body))
        assert fmt.lesson_layout(body, path) == body, f"not idempotent: {path.name}"
        assert body.count("<!-- COURSE-FRAME:START -->") == 1
        panel = body.split("<!-- COURSE-FRAME:START -->")[1].split("<!-- COURSE-FRAME:END -->")[0]
        assert "&#129517;" in panel
        assert [panel.index(f"&#{icon};") for icon in icons] == sorted(panel.index(f"&#{icon};") for icon in icons)
        visible = fmt.html_outside_fences(body)
        assert not re.search(r"^\s*(?:- |\d+\. |\|)", visible, re.M), path.name
        assert "\x00" not in body
        parser = Links()
        parser.feed(visible)
        for target in parser.links:
            # Existing source/provenance links may be external, but lesson navigation must resolve.
            check_link(path, target)
            assert not any(part in target for part in ("/teacher/", "/solution/", "/hidden_tests/")), target
        for target in parser.images:
            assert not urlsplit(target).scheme
            check_link(path, target)

    # Conversion regressions: code punctuation, table pipes and ordered-list starts.
    assert fmt.inline_html('[`a < b`](example.md)') == '<a href="example.md"><code>a &lt; b</code></a>'
    assert fmt.split_table_row('| `a | b` | unione |') == ['`a | b`', 'unione']
    assert '<ol start="3">' in fmt.normalize('3. terzo\n')
    code = '```python\n# keep this comment\nprint("<tag>", 2 < 3)\n```\n'
    assert fmt.normalize(code) == code

    planned = json.loads((diagrams.VISUAL_ROOT / "figure-index.json").read_text(encoding="utf-8"))
    assert {f['module'] for f in planned} == {f'M{n:02d}' for n in range(31)}
    library = ET.parse(diagrams.VISUAL_ROOT / "components.svg").getroot()
    ids = {node.get('id') for node in library.iter(diagrams.tag('symbol'))}
    inventory = json.loads((diagrams.VISUAL_ROOT / "component-inventory.json").read_text(encoding="utf-8"))
    assert ids == {item['id'] for item in inventory} and len(ids) == 25
    catalog_ids = set()
    for scene in (diagrams.VISUAL_ROOT / 'scenes').glob('catalog-*.scene.svg'):
        catalog_ids.update(n.get('href')[1:] for n in ET.parse(scene).iter(diagrams.tag('use')))
    assert catalog_ids == ids, 'catalog must show every component'
    for figure in planned:
        assert set(figure['components']) <= ids
        check_link(ROOT / 'index.md', figure['lesson_section'])
        if figure['asset']:
            assert (ROOT / figure['asset']).is_file()
    for path, payload in diagrams.planned_outputs():
        assert path.read_bytes() == payload, f'stale SVG: {path}'
        assert not re.search(rb'(?<!\{)\{\w+\}(?!\})', payload), 'malformed visual token'
    for path, expected in audit.outputs().items():
        assert path.read_text(encoding='utf-8') == expected, f'stale audit: {path}'
    print('PASS: 31 HTML lessons, orientation, navigation, 25 SVG objects, catalogs and figure audit')


if __name__ == '__main__':
    main()
