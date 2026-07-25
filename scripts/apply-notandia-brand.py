from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

SYMBOL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" role="img" aria-labelledby="title desc">
  <title id="title">Notandia</title>
  <desc id="desc">A geometric N with a highlighted note point, representing scholarly context worth noticing.</desc>
  <rect x="64" y="64" width="896" height="896" rx="224" fill="#12263F"/>
  <path d="M292 736V304" fill="none" stroke="#F8FAFC" stroke-width="128" stroke-linecap="round"/>
  <path d="M326 700L704 324" fill="none" stroke="#F8FAFC" stroke-width="128" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M748 414V736" fill="none" stroke="#F8FAFC" stroke-width="128" stroke-linecap="round"/>
  <circle cx="748" cy="286" r="82" fill="#FFC857"/>
</svg>
'''
(ASSETS / "notandia-symbol.svg").write_text(SYMBOL, encoding="utf-8")

old_brand = '<a class="brand" href="/">Notandia</a>'
new_brand = '<a class="brand" href="/"><img src="/assets/notandia-symbol.svg" alt="" width="32" height="32"><span>Notandia</span></a>'
stylesheet = '<link rel="stylesheet" href="/styles.css">'
favicon = '<link rel="icon" href="/assets/notandia-symbol.svg" type="image/svg+xml">\n  <meta name="theme-color" content="#12263F">\n  ' + stylesheet

html_files = sorted(ROOT.glob("*.html")) + sorted((ROOT / "privacy").glob("*/index.html"))
for path in html_files:
    source = path.read_text(encoding="utf-8")
    if old_brand not in source:
        raise RuntimeError(f"Expected brand anchor not found in {path.relative_to(ROOT)}")
    source = source.replace(old_brand, new_brand)
    if 'rel="icon"' not in source:
        if stylesheet not in source:
            raise RuntimeError(f"Stylesheet marker not found in {path.relative_to(ROOT)}")
        source = source.replace(stylesheet, favicon, 1)
    path.write_text(source, encoding="utf-8")

index = ROOT / "index.html"
source = index.read_text(encoding="utf-8")
source = source.replace(
    "Existing Chrome, Edge, Firefox, and Zotero technical identities are retained where required for updates and user-data continuity.",
    "Existing Chrome and Edge store identities are retained for update continuity. Firefox and the next Zotero release use new Notandia identifiers."
)
if "Existing Chrome, Edge, Firefox, and Zotero" in source:
    raise RuntimeError("Stale transition wording remains in index.html")
index.write_text(source, encoding="utf-8")

styles_path = ROOT / "styles.css"
styles = styles_path.read_text(encoding="utf-8")
replacements = {
    "--bg: #f7f8fb;": "--bg: #f6f8fb;",
    "--ink: #172033;": "--ink: #12263f;",
    "--muted: #5c667a;": "--muted: #48627a;",
    "--accent: #3457d5;": "--accent: #315f86;",
    "--accent-soft: #e9edff;": "--accent-soft: #e8f0f6;",
    ".brand { color: var(--ink); font-weight: 800; text-decoration: none; letter-spacing: -0.02em; }": ".brand { display: inline-flex; align-items: center; gap: 10px; color: var(--ink); font-weight: 800; text-decoration: none; letter-spacing: -0.02em; }\n.brand img { width: 32px; height: 32px; flex: 0 0 auto; }",
}
for old, new in replacements.items():
    if old not in styles:
        raise RuntimeError(f"Expected CSS marker missing: {old}")
    styles = styles.replace(old, new, 1)
styles_path.write_text(styles, encoding="utf-8")
