# MDPI Filter website

Public website and documentation for the MDPI Filter project and its planned transition into a broader, explainable research-integrity suite.

## Hosting

The site is intentionally dependency-free and deploys as static files on Cloudflare Pages.

- Framework preset: None
- Build command: `exit 0`
- Build output directory: `.`
- Root directory: repository root
- Production branch: `main`
- Environment variables: none

Pull-request deployments should remain on Cloudflare preview hostnames until a neutral product name and domain are cleared.

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
- hardened or tested preview functionality available only on GitHub;
- planned functionality that is not yet shipped.

It must never describe the absence of a warning as proof that an article, journal, or publisher is reliable.

## Licensing

- Site code: AGPL-3.0-or-later
- Original documentation: CC BY-SA 4.0
- Third-party evidence and imported metadata retain their source-specific licenses and attribution requirements.
