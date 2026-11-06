# Contributing

Open a focused pull request describing the change and how it was verified. Use Issues for ordinary bugs; report security vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

1. Preview the site with `python3 -m http.server 8000`.
2. Run `python3 scripts/check_site.py` with Python 3 and Node.js installed.
3. Check desktop and mobile layouts and the affected interactions.
4. Keep the domain, canonical URLs, crawler files, and documentation consistent.

Preserve the site's concept disclaimer and clearly distinguish illustrative sequences, telemetry, and estimates from real data. Do not commit personal genetic data, medical data, credentials, or private keys. Treat all visitor input as untrusted and render it safely as text.

Keep workflow permissions minimal and pin external actions to full commit SHAs. Review Dependabot changes before merging. After a change reaches `main`, verify the GitHub Pages deployment and relevant live URLs.
