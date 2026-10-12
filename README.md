# Nino public pages

`privacy.html` and `support.html` are the App Store's Privacy Policy and Support URLs.
Supabase Edge Functions rewrite `text/html` to `text/plain` (anti-phishing), so these
live on GitHub Pages; `momo-privacy` / `momo-support` serve a plain-text copy and, once
`PUBLIC_SITE_URL` is set, redirect here. Edit the HTML in the function source
(single source of truth) and re-run `python3 site/sync.py`.
