#!/usr/bin/env python3
"""Fills the shared strip, theme switch, footer and mark into each page.
Run from the repo root after changing tools/*.html. The pages are plain files, so Pages needs no build."""
import re

parts = re.split(r"<!--(STRIP|THEME|FOOTER)-->\n", open("tools/chrome.html.txt", encoding="utf8").read())
blocks = {parts[i]: parts[i + 1].rstrip() for i in range(1, len(parts), 2)}
mark = open("tools/mark.svg.txt", encoding="utf8").read()
mark = re.sub(r"\s*\n\s*", "", mark).replace('class="wwmark"', 'class="wwmark" aria-hidden="true"').replace(' role="img" aria-label="WOODWERD Design"', "")

pages = ("index", "github")
for name in pages:
    html = open(f"tools/{name}.src.html", encoding="utf8").read()
    for key, block in blocks.items():
        html = html.replace(f"<!--{key}-->", block)
    open(f"{name}.html", "w", encoding="utf8").write(html.replace("<!--MARK-->", mark))
print("wrote " + ", ".join(f"{p}.html" for p in pages))
