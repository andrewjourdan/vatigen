"""Validate publishing files, navigation targets, and visitor-input rendering."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.anchors = []
        self.canonical = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.anchors.append(attrs["href"][1:])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))
        for attr in ("src", "href"):
            assert not attrs.get(attr, "").startswith("http:"), "Insecure resource URL"


html = (ROOT / "index.html").read_text()
page = Page()
page.feed(html)
assert page.canonical == ["https://vatigen.com/"], "Canonical URL mismatch"
assert all(not a or a in page.ids for a in page.anchors), "Broken section link"
assert (ROOT / "CNAME").read_text().strip() == "vatigen.com", "Custom domain mismatch"
assert (ROOT / ".nojekyll").exists(), "Missing static publishing marker"
assert "Sitemap: https://vatigen.com/sitemap.xml" in (ROOT / "robots.txt").read_text()
tree = ET.parse(ROOT / "sitemap.xml")
urls = [el.text for el in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
assert urls == ["https://vatigen.com/"], "Sitemap mismatch"
fallback = (ROOT / "404.html").read_text()
assert 'href="/"' in fallback and 'content="noindex"' in fallback
for name in ("README.md", "SECURITY.md", "CONTRIBUTING.md"):
    assert (ROOT / name).is_file(), f"Missing {name}"

scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", html, re.S | re.I)
assert scripts, "Missing application script"
for script in scripts:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "site.js"
        path.write_text(script)
        subprocess.run(["node", "--check", str(path)], check=True)

# Exercise the actual shelf renderer with hostile visitor input. The DOM stub
# captures its output without needing network access or a browser dependency.
script = scripts[0]
start = script.index("    function escapeHTML(")
end = script.index("    // --- RENDER ACTIVE CODEX READER ---", start)
renderer = script[start:end]
test = r'''
const assert = require('node:assert/strict');
const vm = require('node:vm');
const payload = '<img src=x onerror="alert(1)">&\'"';
const cards = [];
const context = {
  codices: [{id:'TEST', category:'Global Citizens', title:payload,
    origin:payload, haplogroup:payload, medium:payload}],
  selectedCodex: {id:'TEST'}, activeCategory:'ALL',
  searchInput: {value:''},
  shelfContainer: {innerHTML:'', appendChild(card) { cards.push(card); }},
  document: {createElement() { return {addEventListener() {}}; }},
  renderReader() {}
};
vm.createContext(context);
vm.runInContext(RENDERER + '\nrenderShelf();', context);
assert.equal(cards.length, 1);
assert(!cards[0].innerHTML.includes('<img'), 'Visitor HTML became markup');
assert(cards[0].innerHTML.includes('&lt;img'), 'Visitor text was lost');
assert(cards[0].innerHTML.includes('&amp;'), 'Ampersand was not escaped');
assert(cards[0].innerHTML.includes('&#39;'), 'Quote was not escaped');
context.searchInput.value = 'does-not-match';
cards.length = 0;
vm.runInContext('renderShelf();', context);
assert.equal(cards.length, 0, 'Search filtering failed');
'''.replace("RENDERER", json.dumps(renderer))
subprocess.run(["node", "-e", test], check=True)
print("Passed: publishing files, canonical URL, section links, JavaScript syntax, input safety, search filtering")
