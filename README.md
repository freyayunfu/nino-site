# Nino public pages

`privacy.html` and `support.html` are the App Store's Privacy Policy and Support URLs.
Supabase Edge Functions rewrite `text/html` to `text/plain` (anti-phishing), so these
live on GitHub Pages; `momo-privacy` / `momo-support` serve a plain-text copy and, once
`PUBLIC_SITE_URL` is set, redirect here. Edit the HTML in the function source
(single source of truth) and re-run `python3 site/sync.py`.

Published from the public repo **freyayunfu/nino-site** (GitHub Pages) at
https://freyayunfu.github.io/nino-site/ — `site/` here is a nested git checkout of
that repo: after `sync.py`, `cd site && git commit -am "…" && git push`.
