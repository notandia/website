from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PAGES = [
    ROOT / "index.html",
    ROOT / "methodology.html",
    ROOT / "privacy.html",
    ROOT / "security.html",
]
REQUIRED_HEADERS = [
    "Content-Security-Policy:",
    "Referrer-Policy:",
    "Permissions-Policy:",
    "X-Content-Type-Options:",
    "X-Frame-Options:",
    "Strict-Transport-Security:",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.scripts: list[str | None] = []
        self.has_title = False
        self.has_description = False
        self.has_canonical = False
        self.has_main = False
        self.html_lang: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_lang = values.get("lang")
        elif tag == "title":
            self.has_title = True
        elif tag == "main":
            self.has_main = True
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        elif tag == "script":
            self.scripts.append(values.get("src"))
        elif tag == "meta" and values.get("name") == "description" and values.get("content"):
            self.has_description = True
        elif tag == "link" and values.get("rel") == "canonical" and values.get("href"):
            self.has_canonical = True


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def resolve_internal_link(page: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith("#") or href.startswith("mailto:"):
        return None
    path = parsed.path
    if not path:
        return None
    if path == "/":
        return ROOT / "index.html"
    if path.startswith("/"):
        return ROOT / path.lstrip("/")
    return page.parent / path


def check_page(page: Path) -> None:
    if not page.is_file() or page.stat().st_size == 0:
        fail(f"required page missing or empty: {page.relative_to(ROOT)}")

    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))

    if parser.html_lang != "en":
        fail(f"{page.name}: expected html lang='en'")
    if not parser.has_title:
        fail(f"{page.name}: missing title")
    if not parser.has_description:
        fail(f"{page.name}: missing meta description")
    if not parser.has_canonical:
        fail(f"{page.name}: missing canonical link")
    if not parser.has_main:
        fail(f"{page.name}: missing main landmark")
    if parser.scripts:
        fail(f"{page.name}: JavaScript is not allowed in the dependency-free foundation")

    for href in parser.links:
        target = resolve_internal_link(page, href)
        if target is not None and not target.exists():
            fail(f"{page.name}: broken internal link {href!r}")


def main() -> None:
    for page in REQUIRED_PAGES:
        check_page(page)

    headers = (ROOT / "_headers").read_text(encoding="utf-8")
    for header in REQUIRED_HEADERS:
        if header not in headers:
            fail(f"_headers missing required directive: {header}")

    if "script-src 'none'" not in headers:
        fail("content security policy must block scripts")
    if not (ROOT / "robots.txt").is_file():
        fail("robots.txt missing")
    if not (ROOT / "sitemap.xml").is_file():
        fail("sitemap.xml missing")

    print("Website verification passed.")


if __name__ == "__main__":
    main()
