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

The current production hostname remains `mdpi-filter.pages.dev` temporarily so existing store privacy-policy URLs stay valid. A cleared Notandia custom domain should later become canonical through a path-preserving redirect migration; do not delete or abandon the old hostname.

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

- functionality currently released in browser stores;
- hardened or tested release-candidate functionality available on GitHub;
- planned functionality that is not yet shipped.

It must never describe the absence of a warning as proof that an article, journal, or publisher is reliable.

## Identity boundary

- Public product name: **Notandia**.
- Transition wording: **Previously MDPI Filter**.
- MDPI may still be named when describing the existing MDPI-detection feature.
- Notandia must be described as independent and unaffiliated with publishers, browser vendors, and data providers.
- Legacy store IDs, add-on IDs, update identities, and the temporary Pages hostname may remain where continuity requires them.

## Licensing

- Site code: AGPL-3.0-or-later
- Original documentation: CC BY-SA 4.0
- Third-party evidence and imported metadata retain their source-specific licenses and attribution requirements.
