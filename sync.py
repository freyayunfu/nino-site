#!/usr/bin/env python3
"""Copy the HTML out of momo-privacy / momo-support into site/ for GitHub Pages."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
for fn, out in [("momo-privacy", "privacy.html"), ("momo-support", "support.html")]:
    s = (root / "supabase/functions" / fn / "index.ts").read_text()
    html = s[s.index("`<!DOCTYPE") + 1:s.index("`;\n\nDeno.serve")]
    (root / "site" / out).write_text(html.replace('href="./momo-privacy"', 'href="./privacy.html"') + "\n")
    print("wrote", out)
