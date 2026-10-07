#!/usr/bin/env python3
"""Render blog posts from one or more spec files WITHOUT touching sitemap.xml.

Usage: python3 scripts/build_blog_specs.py scripts/specs_oct_posts_1.json [...]

Thin wrapper over build_pages.render_blog. It additionally allows
[text](https://external) links in paragraphs (rendered rel="noopener", new tab),
which the stock _esc_p deliberately refuses. Run scripts/wire_playbook.py after
to restore the playbook backlink and Keep-reading blocks.
"""
import html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pages as bp

_EXT = re.compile(r"\[([^\]\[]+)\]\((https://[A-Za-z0-9\-._~:/?#@!$&'*+,;=%]+)\)")
_orig = bp._esc_p

def _esc_p(s):
    out = _orig(s)
    return _EXT.sub(lambda m: f'<a href="{html.unescape(m.group(2))}" rel="noopener" target="_blank">{m.group(1)}</a>', out)

bp._esc_p = _esc_p

for f in sys.argv[1:]:
    for spec in json.loads(Path(f).read_text()).get("blog", []):
        slug, page = bp.render_blog(spec)
        out = bp.ROOT / "blog" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print("wrote", out.relative_to(bp.ROOT))
