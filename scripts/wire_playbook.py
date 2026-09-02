#!/usr/bin/env python3
"""Wire the playbook hub-and-spoke links across the site. Idempotent.

Reads scripts/specs_playbook.json (the one source of truth for clusters) and:
  1. injects a marker-delimited "Part of the X playbook" backlink into every
     spoke page (blog posts and landing pages alike),
  2. injects the "Keep reading" block on the spec'd pages that carry one
     (scripts/specs_readnext.json),
  3. injects the playbook library section into /playbook/ (the manifesto keeps
     its copy; this only adds the hub directory before its closing CTA),
  4. injects a playbook banner at the top of /blog/,
  5. verifies every spoke href resolves to a real file, and fails loudly if not.

Run it AFTER any build_pages.py run: the generator rewrites spec'd pages
without these blocks, and this script puts them back. Safe to run twice.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "scripts" / "specs_playbook.json"
READNEXT_SPEC = ROOT / "scripts" / "specs_readnext.json"

B_LINK, E_LINK = "<!-- playbook-link -->", "<!-- /playbook-link -->"
B_LIB, E_LIB = "<!-- playbook-library -->", "<!-- /playbook-library -->"
B_BAN, E_BAN = "<!-- playbook-banner -->", "<!-- /playbook-banner -->"
B_NEXT, E_NEXT = "<!-- readnext -->", "<!-- /readnext -->"

BLURB_MAX = 105


def _page_path(href: str) -> Path:
    return ROOT / href.strip("/") / "index.html"


def _splice(html: str, begin: str, end: str, block: str, anchor_res: list[str], where: str) -> str:
    """Replace an existing begin..end block, else insert before the first anchor
    regex that matches. The block always travels with its markers."""
    full = begin + block + end
    if begin in html:
        pattern = re.escape(begin) + r".*?" + re.escape(end)
        return re.sub(pattern, lambda _: full, html, count=1, flags=re.S)
    for a in anchor_res:
        m = re.search(a, html)
        if m:
            return html[: m.start()] + full + "\n" + html[m.start() :]
    raise SystemExit(f"wire_playbook: no anchor found in {where}")


def link_block(hub_slug: str, hub_name: str) -> str:
    return (
        '<section class="section"><p style="text-align:center;color:var(--ink-2);font-size:14px">'
        f'Part of the <a href="/playbook/{hub_slug}/" style="color:var(--blue);text-decoration:none">'
        f"{hub_name}</a> playbook &middot; "
        '<a href="/playbook/" style="color:var(--blue);text-decoration:none">all playbooks &rarr;</a>'
        "</p></section>"
    )


def library_block(hubs: list[dict]) -> str:
    items = "".join(
        f'<a href="/playbook/{h["slug"]}/" style="display:block;border:1px solid rgba(128,128,128,.28);'
        'border-radius:12px;padding:16px 18px;color:inherit;text-decoration:none">'
        f'<span style="display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;opacity:.65">{h["kicker"]}</span>'
        f'<strong style="display:block;font-size:17px;margin:6px 0 4px">{h["h1"]}</strong>'
        f'<span style="display:block;font-size:13.5px;opacity:.75">{len(h["spokes"])} guides, in reading order</span></a>'
        for h in hubs
    )
    return (
        '<div class="wrap" style="margin:64px auto"><div class="kicker">The Library</div>'
        '<h2 style="margin:8px 0 10px">Every play, expanded into a full playbook</h2>'
        '<p class="lead" style="margin-bottom:22px">Each play above is the short version. These six playbooks hold '
        "every guide on this site, organized, in the order to read them.</p>"
        f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px">{items}</div></div>'
    )


def _page_headline(p: Path) -> str:
    """The destination's own H1, minus any <br>, unescaped for re-escaping."""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", p.read_text(), re.S)
    if not m:
        raise SystemExit(f"wire_playbook: no <h1> in {p}")
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1)))).strip()


def _page_blurb(p: Path) -> str:
    """The destination's own meta description, trimmed to a card-sized line."""
    m = re.search(r'<meta name="description" content="([^"]*)"', p.read_text())
    if not m:
        raise SystemExit(f"wire_playbook: no meta description in {p}")
    d = html.unescape(m.group(1)).strip()
    return d if len(d) <= BLURB_MAX else d[:BLURB_MAX].rsplit(" ", 1)[0] + "…"


def readnext_block(hrefs: list[str]) -> str:
    """A "Keep reading" card list. The card carries the destination's own H1 and
    meta description, READ FROM that page rather than stored here, so editing a
    post fixes every card pointing at it instead of leaving copies to rot on eight
    other pages. H1 and not <title>: the card promises what the reader will see on
    arrival, and it must not shift every time a title tag is retuned for the SERP."""
    items = "".join(
        f'<li><a href="{h}"><b>{html.escape(_page_headline(_page_path(h)), quote=True)}</b>'
        f'<span>{html.escape(_page_blurb(_page_path(h)), quote=True)}</span></a></li>'
        for h in hrefs)
    return f'<div class="readnext"><div class="readnext-h">Keep reading</div><ul>{items}</ul></div>'


def banner_block() -> str:
    # /blog/ is the dark hand-built index: it defines --muted and --blue, not --ink-2.
    return (
        '<p style="text-align:center;margin:0 auto 34px;max-width:640px;font-size:15px;color:var(--muted)">'
        'New here? The posts below are organized into '
        '<a href="/playbook/" style="color:var(--blue);text-decoration:none;font-weight:600">'
        "six playbooks you can read in order &rarr;</a></p>"
    )


def main() -> int:
    hubs = json.loads(SPEC.read_text())["hub"]

    # 1. verify every spoke resolves before touching anything
    missing = [s["href"] for h in hubs for s in h["spokes"] if not _page_path(s["href"]).exists()]
    if missing:
        print("wire_playbook: MISSING spoke pages, nothing written:", *missing, sep="\n  ")
        return 2
    for h in hubs:
        if not (ROOT / "playbook" / h["slug"] / "index.html").exists():
            print(f"wire_playbook: hub /playbook/{h['slug']}/ not built yet; run build_pages.py first")
            return 2

    # 2. spoke -> hub backlinks
    wired = 0
    cta_anchor = r'<section class="section"><div class="cta-strip'
    for h in hubs:
        block = link_block(h["slug"], h["h1"])
        for s in h["spokes"]:
            p = _page_path(s["href"])
            # not `html`: that name is the stdlib module this file now escapes with.
            page = _splice(p.read_text(), B_LINK, E_LINK, block, [cta_anchor, r"<footer>"], str(p))
            p.write_text(page)
            wired += 1

    # 2b. "Keep reading" blocks. These sit immediately above the playbook backlink,
    # so anchor on it first and fall back the same way the backlink does.
    readnext = json.loads(READNEXT_SPEC.read_text())["readnext"]
    missing_next = [h for hrefs in readnext.values() for h in hrefs if not _page_path(h).exists()]
    if missing_next:
        print("wire_playbook: MISSING readnext targets:", *sorted(set(missing_next)), sep="\n  ")
        return 2
    for slug, hrefs in readnext.items():
        p = ROOT / slug / "index.html"
        if not p.exists():
            print(f"wire_playbook: readnext page {slug} not built yet; run build_pages.py first")
            return 2
        html_txt = _splice(p.read_text(), B_NEXT, E_NEXT, readnext_block(hrefs),
                           [re.escape(B_LINK), cta_anchor, r"<footer>"], str(p))
        p.write_text(html_txt)

    # 3. the library on /playbook/
    pb = ROOT / "playbook" / "index.html"
    pb.write_text(_splice(pb.read_text(), B_LIB, E_LIB, library_block(hubs),
                          [r'<div class="cta-strip">', r"<footer>"], str(pb)))

    # 4. the banner on /blog/
    bi = ROOT / "blog" / "index.html"
    bi.write_text(_splice(bi.read_text(), B_BAN, E_BAN, banner_block(),
                          [r'<div class="blog-grid"', r"<footer>"], str(bi)))

    print(f"wire_playbook: {wired} spoke backlinks wired across {len(hubs)} hubs; "
          f"{len(readnext)} readnext blocks; library + blog banner in place")
    return 0


if __name__ == "__main__":
    sys.exit(main())
