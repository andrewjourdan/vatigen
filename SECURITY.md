# Security Policy

## Supported version

Security fixes apply to the latest version on `main` and the current deployment at https://vatigen.com/. Older commits are not maintained.

## Report a vulnerability

Use [GitHub's private vulnerability reporting form](https://github.com/andrewjourdan/vatigen/security/advisories/new). Do not publish vulnerability details or sensitive information in public issues. If the private form is unavailable, wait until a private reporting channel is available rather than posting exploit details publicly.

Include the affected URL or file, steps to reproduce, expected and observed behavior, and potential impact. Use synthetic examples and remove personal information, credentials, and genetic data from screenshots or attachments.

Reports are reviewed as maintainer availability permits. No response deadline or bounty is promised. Coordinate public disclosure with the maintainer after a fix is available.

## Scope

This is a static concept website with client-side demonstrations. It has no application account system, server-side submission endpoint, or application database. The illustrative codices, sequences, telemetry, and payload estimates do not represent an operational genetic archive or biobank.

The Scriptorium demo processes input in the current browser tab and keeps newly generated codices in memory until the page is reloaded. Do not enter real genetic, medical, or other sensitive personal data. Google Fonts is an external dependency and receives browser requests when the page loads.

Report issues in this repository's code and site configuration here. Report vulnerabilities in GitHub, Cloudflare, or Google Fonts to those providers. Test only resources you own or are authorized to test, without disrupting service or accessing another person's information.

## Maintainer guidance

Never commit passwords, tokens, private keys, or personal data. Keep secret scanning and push protection enabled. Revoke or rotate exposed credentials immediately; deleting a file does not erase Git history.

Render visitor input as text or escape it before inserting it into HTML. Run the site checks before publishing. Preserve HTTPS enforcement and verify Cloudflare response headers after hosting or proxy changes. GitHub Pages does not use `_headers` files; HTTP security headers must be configured at the serving layer.
