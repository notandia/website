# Notandia website

Public website, methodology, privacy policies, and security documentation for Notandia, previously distributed as MDPI Filter.

## Hosting

The site is intentionally dependency-free and deploys as static files on Cloudflare Pages.

- Framework preset: None
- Build command: `exit 0`
- Build output directory: `.`
- Root directory: repository root
- Production branch: `main`
- Environment variables: none

The canonical production address is `https://notandia.pages.dev`. Both the `notandia` and legacy `mdpi-filter` Cloudflare Pages projects deploy this repository from `main`. Keep the legacy project available so existing store privacy-policy and support URLs remain valid. Host-level redirects belong in Cloudflare Bulk Redirects, not this shared `_redirects` file. Activate them only after the new hostname and all platform privacy pages are verified live. No domain purchase is needed.

## Local preview

```bash
python3 -m http.server 8788
```

Then open `http://localhost:8788`.

## Verification

```bash
python3 scripts/verify_site.py
```

The verifier checks required pages, internal links, security headers, canonical metadata, and that no remote JavaScript is loaded.

## Content boundaries

The website must always distinguish:

- functionality in the published Chrome package and the updated Edge package (maintainer-confirmed on 4 October 2026), with pending Edge listing artwork and description kept separate from package availability;
- subsequent functionality in development source, with validation and release status stated separately for each platform;
- planned functionality that is not yet implemented.

The configurable Notandia interface is available in Chrome as of 3 October 2026. The maintainer confirmed the updated Edge package on 4 October 2026. Firefox 0.1.2 is publicly downloadable at https://addons.mozilla.org/en-US/firefox/addon/notandia/, verified 7 October 2026. Mozilla reports automated screening and tentative approval; later human review remains possible. Zotero has separate releases; store availability does not establish feature parity.

## Evidence and interpretation boundaries

The website must keep these concepts separate:

1. **Publisher identity evidence** — domains, DOI prefixes, and validated compatibility evidence.
2. **User-selected publisher treatment** — context only, badge, highlight, dim, hide, or disabled.
3. **Formal work-level events** — retractions, concerns, corrections, reinstatements, withdrawals/removals, and duplicate-publication findings.

MDPI and Frontiers are built-in profiles in current source, enabled and highlighted by default, and independently deactivable. This is a product default and user preference—not an official statement that every article from either publisher is unreliable.

The website must never describe a publisher watchlist match as an objective quality score or the absence of a warning as proof that an article, journal, or publisher is reliable.

## Privacy boundary

- Publisher profiles and actions are processed locally and stored through browser extension storage.
- Custom profiles are declarative and cannot contain executable scripts or selectors.
- NCBI requests contain only validated DOI, PMID, or PMCID identifiers.
- Crossref integrity requests are off by default and contain only normalized DOI identifiers; direct and reverse update queries are both disclosed.
- Reports omit query strings, fragments, citation text, and DOI lists unless the user explicitly adds them.
- The site and extension use no product analytics or advertising.

## Identity boundary

- Public product name: **Notandia**.
- Transition wording: **Previously MDPI Filter**.
- Chrome uses the Notandia name with its existing store item ID; Edge uses the Notandia name with its existing item ID; artwork and description updates are awaiting approval.
- Firefox 0.1.2 is publicly available on Mozilla Add-ons with Gecko ID `browser-extension@notandia.github.io`; public listing and download verified 7 October 2026. This is automated-screening approval, not a claim that human review has been completed.
- MDPI and Frontiers may be named when describing their built-in publisher profiles.
- Notandia must be described as independent and unaffiliated with publishers, browser vendors, and data providers.
- Legacy store IDs, update identities, and the current Pages hostname may remain where continuity requires them.

## Licensing

- Site code: AGPL-3.0-or-later
- Original documentation: CC BY-SA 4.0
- Third-party evidence and imported metadata retain their source-specific licenses and attribution requirements.
