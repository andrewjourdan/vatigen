# VATIGEN

The static concept website at [vatigen.com](https://vatigen.com/), exploring an illustrative genetic archive, DNA encoding, quartz storage, and lunar preservation.

VATIGEN is an independent, unregistered business concept. It is not affiliated with or endorsed by the Holy See, Vatican Apostolic Library, or any religious, academic, or space organization. The site is not an operational biobank. Its records, sequences, telemetry, and simulator values are illustrative.

## Repository structure

| File | Purpose |
| --- | --- |
| `index.html` | Page content, styles, illustrative dataset, and client-side demos |
| `CNAME` | GitHub Pages custom domain: `vatigen.com` |
| `.nojekyll` | Publish static files without Jekyll processing |
| `404.html` | Missing-page response with a link home |
| `robots.txt` and `sitemap.xml` | Crawler guidance and canonical homepage |
| `SECURITY.md` | Supported version and private vulnerability reporting |
| `CONTRIBUTING.md` | Change and verification guidance |
| `scripts/check_site.py` | Publishing, navigation, and JavaScript checks |
| `.github/workflows/site-checks.yml` | Checks on pull requests and pushes to `main` |
| `.github/dependabot.yml` | Monthly GitHub Actions dependency updates |
| `.gitignore` | Exclude local files and environment secrets |

## Preview and check

No build step or package installation is required. With Python 3 installed:

```sh
python3 -m http.server 8000
```

Open http://localhost:8000. Stop the server with Ctrl+C. Google Fonts requires a network connection; fallback fonts remain available offline.

With Python 3 and Node.js installed, run:

```sh
python3 scripts/check_site.py
```

Before publishing, also check desktop and mobile layouts, navigation, search and category filters, codex selection, chromosome tabs, storage tiers, payload sliders, phase selection, and Scriptorium preview and minting. Try names and origins containing characters such as `<`, `&`, and quotes; they must remain text.

## Deployment

GitHub Pages publishes the root of `main` at https://vatigen.com/. A push to `main` triggers deployment; confirm its success in [Actions](https://github.com/andrewjourdan/vatigen/actions). Enforce HTTPS is enabled in Settings → Pages.

When changing the domain, keep `CNAME`, the canonical and social URLs in `index.html`, `robots.txt`, and `sitemap.xml` consistent. Add new public standalone pages to the sitemap; section anchors are not separate pages. The custom 404 is a real missing-page response, not a redirect that conceals broken URLs.

## Data and security

The demos run in the browser. Generated codices are held in memory and disappear on reload. There is no application database, account system, or server-side submission endpoint. Do not enter real genetic, medical, or sensitive personal data. Google Fonts is loaded from Google's servers; hosting providers may maintain their own access logs.

Cloudflare is configured for Full (strict) SSL, HTTPS redirects, TLS 1.2 minimum, automatic HTTPS rewrites, HTTP/3, encrypted Client Hello, and one-day HSTS with `nosniff`. HSTS subdomain coverage and preload are disabled. DNSSEC is active through the matching DS record at Squarespace. These settings live outside this repository and must be checked separately from a successful Pages build.

GitHub Pages does not apply a `_headers` file. Configure HTTP response headers such as `X-Content-Type-Options` at Cloudflare. Do not copy another site's restrictive Content Security Policy unchanged: this site currently contains inline styles and JavaScript that such a policy could block.

Secret scanning, push protection, private vulnerability reporting, Dependabot alerts and security updates, grouped security updates, and malware alerts are enabled. Workflows default to read-only permissions; external contributor workflows require approval. The site-check workflow uses a pinned checkout action without persisted credentials, and Dependabot checks action updates monthly.

## Contributions and rights

See [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance guidance and [SECURITY.md](SECURITY.md) for private reporting. No open-source license is granted by this repository. Third-party resources remain subject to their owners' terms.
