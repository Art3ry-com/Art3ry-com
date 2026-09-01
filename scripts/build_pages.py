#!/usr/bin/env python3
"""build_pages.py — Art3ry static-site page factory.

ONE on-brand template per page type, fed by a JSON spec file, so every landing
and blog page is design-consistent (the Art3ry OS way — no drift, no hand-authored
one-offs). Emits crawlable HTML with OG + JSON-LD, updates sitemap.xml + the blog
index, and adds landing pages to the homepage nav dropdown source list.

Usage:
    python3 scripts/build_pages.py specs.json
    # specs.json = {"audience":[LANDING...], "industry":[LANDING...], "blog":[BLOG...]}
"""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://art3ry.com"

# Shared brand CSS (matches the live homepage + /assistant/ page).
# The design system lives in assets/pages.css, not inline. Bump CSS_V on every
# change to it: /assets/*.css ships max-age=14400, and new HTML paired with
# four-hour-stale CSS renders as garbage.
# Cloudflare Web Analytics. Public site token by design (it is visible in the
# page source of every site using it), so it lives here rather than in .env.
# Manual beacon rather than Automatic setup, per the token Jesse issued.
_ANALYTICS = ("""<!-- Cloudflare Web Analytics -->"""
              """<script defer type="module" src="https://static.cloudflareinsights.com/beacon.min.js" """
              """data-cf-beacon='{"token": "11bbd30f1f234e4a85f719e0e1c87be3"}'></script>"""
              """<!-- End Cloudflare Web Analytics -->""")

CSS_V = "20260831c"
_CSS_LINK = f'<link rel="stylesheet" href="/assets/pages.css?v={CSS_V}">'


_NAV = """<nav>
  <a href="/" class="logo" aria-label="ART3RY home">
    <svg class="logo-mark" viewBox="0 0 26 26" aria-hidden="true">
      <defs><linearGradient id="lm" x1="0" y1="1" x2="1" y2="0">
        <stop offset="0%" stop-color="#E63946"/><stop offset="100%" stop-color="#5B9BFF"/>
      </linearGradient></defs>
      <path d="M1 15 H6 L9 7 L13 21 L16 13 H21" fill="none" stroke="url(#lm)"
            stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="23.2" cy="13" r="2.1" fill="#E63946"/>
    </svg>
    <span class="wordmark">ART<em>3</em>RY</span>
  </a>
  <div class="nav-links"><a href="/services/">The Growth Build</a><a href="/about/">About</a><a href="/blog/">Blog</a></div>
  <a href="/get-started/" class="nav-cta">Work with me &rarr;</a>
</nav>"""

_FOOTER = """<footer>
  <div style="display:flex;flex-direction:column;gap:6px">
    <span class="wordmark">ART<em>3</em>RY</span>
    <p style="font-size:11px">&copy; 2026 ART3RY, LLC &mdash; California</p>
  </div>
  <div class="footer-links">
    <a href="/services/">The Growth Build</a><a href="/about/">About</a><a href="/blog/">Blog</a>
    <a href="/get-started/">Work with me</a>
    <a href="https://jessemoraga.com" target="_blank" rel="noopener">jessemoraga.com</a>
  </div>
  <div><a href="mailto:jesse@jessemoraga.com" style="font-size:12px">jesse@jessemoraga.com</a></div>
</footer>"""

# Phone leak guard — Jesse's cell must NEVER reach a public page (mirrors the the flagship operation rule).
_CELL_DIGITS = "4283688"


def _esc(s: str) -> str:
    return html.escape(s or "", quote=True)


_LINK_RE = re.compile(r"\[([^\]\[]+)\]\((/[A-Za-z0-9\-/]*/)\)")


def _esc_p(s: str) -> str:
    """Escape a paragraph, then re-enable [text](/site-relative/) internal links only.

    Hub-and-spoke content is worthless without in-body internal links, but we still
    never want raw author HTML in a paragraph. So: escape everything first, then
    re-open exactly one construct, and only for paths that start and end with "/".
    No protocol, no host, no attributes -> nothing external, nothing injectable.
    """
    return _LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', _esc(s or ""))


def _meta(s: str, limit: int = 160) -> str:
    """Trim a meta description to <=limit chars at a word boundary (no SERP cut-off)."""
    s = (s or "").strip()
    if len(s) <= limit:
        return s
    return s[:limit].rsplit(" ", 1)[0].rstrip(" .,;:\u2014-")


def _h1(s: str) -> str:
    # allow a single <br> in the headline; escape the rest, add a space after <br> so
    # crawlers don't read concatenated words.
    parts = (s or "").split("<br>", 1)
    return _esc(parts[0]) + ("<br>\n" + _esc(parts[1].strip()) if len(parts) > 1 else "")


def _head(title, desc, canon, jsonld) -> str:
    t, d = _esc(title), _esc(_meta(desc))
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}">
<link rel="icon" type="image/png" href="/assets/art3ry-logo.png">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}/assets/art3ry-brand.jpg"><meta property="og:site_name" content="ART3RY">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{SITE}/assets/art3ry-brand.jpg">
<script type="application/ld+json">{json.dumps(jsonld, separators=(',', ':'))}</script>
{_CSS_LINK}</head><body>
{_NAV}"""


def _guard(htmlstr: str, where: str) -> str:
    if _CELL_DIGITS in re.sub(r"\D", "", htmlstr):
        raise SystemExit(f"build_pages: ABORT — Jesse's private cell appeared in {where}")
    return htmlstr


def render_landing(spec: dict) -> tuple[str, str]:
    slug = spec["slug"].strip("/")
    canon = f"{SITE}/{slug}/"
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": canon + "#service", "serviceType": "AI assistant",
         "name": spec["title_tag"], "description": spec["meta_description"],
         "provider": {"@type": "Organization", "name": "Art3ry", "url": SITE + "/"},
         "areaServed": {"@type": "Country", "name": "United States"}},
        {"@type": "FAQPage", "@id": canon + "#faq",
         "mainEntity": [{"@type": "Question", "name": f["q"],
                         "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in spec["faq"]]},
    ]}
    steps = "".join(
        f'<div class="step"><div class="n">{_esc(s["n"])}</div><h3>{_esc(s["h3"])}</h3><p>{_esc(s["p"])}</p></div>'
        for s in spec["steps"])
    cards = "".join(
        f'<div class="card"><div class="tag">{_esc(c["tag"])}</div><h3>{_esc(c["h3"])}</h3>'
        f'<div class="say">{_esc(c["say"])}</div><ul>'
        + "".join(f"<li>{_esc(b)}</li>" for b in c["bullets"]) + "</ul></div>"
        for c in spec["scenarios"])
    faq = "".join(f'<div class="q">{_esc(f["q"])}</div><div class="a">{_esc(f["a"])}</div>' for f in spec["faq"])
    body = f"""{_head(spec['title_tag'], spec['meta_description'], canon, jsonld)}
<header class="hero"><div class="wrap"><div class="kicker">The Growth Build</div>
<h1>{_h1(spec['h1'])}</h1><p class="sub">{_esc(spec['hero_sub'])}</p>
<div class="btns"><a href="/get-started/" class="btn-primary">Get your assistant &rarr;</a>
<a href="https://jessemoraga.com" target="_blank" rel="noopener" class="btn-secondary">See it running a real business</a></div></div></header>
<section class="section"><h2>It's this simple</h2><p class="lead">No app to learn. You just talk.</p><div class="steps wrap">{steps}</div></section>
<section class="section"><h2>How it shows up in your day</h2><div class="cards wrap">{cards}</div></section>
<section class="section"><div class="safe"><h2 style="color:#fff;font-size:30px;font-weight:800">Powerful, because it's safe</h2><p>{_esc(spec['safety_line'])}</p></div></section>
<section class="section"><p class="proof">Not a demo — ART3RY runs <a href="https://jessemoraga.com" target="_blank" rel="noopener">a real California field-services company</a>, a real one-person company.</p></section>
<section class="section"><h2>Questions</h2><div class="faq">{faq}</div></section>
<section class="section"><div class="cta-strip wrap"><h2>Hand off the work behind the work.</h2><p>Tell us what's eating your day. We'll wire your assistant to it.</p><a href="/get-started/">Get your assistant &rarr;</a></div></section>
{_FOOTER}{_ANALYTICS}</body></html>"""
    return slug, _guard(body, f"landing:{slug}")


def render_blog(spec: dict) -> tuple[str, str]:
    slug = spec["slug"].strip("/")
    canon = f"{SITE}/blog/{slug}/"
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": canon + "#post", "headline": spec["title"],
         "description": spec["meta_description"], "url": canon,
         "author": {"@type": "Organization", "name": "Art3ry"},
         "publisher": {"@type": "Organization", "name": "Art3ry", "url": SITE + "/"}},
        {"@type": "FAQPage", "@id": canon + "#faq",
         "mainEntity": [{"@type": "Question", "name": f["q"],
                         "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in spec["faq"]]},
    ]}
    secs = "".join(f"<h2>{_esc(s['h2'])}</h2>" + "".join(f"<p>{_esc_p(p)}</p>" for p in s["paragraphs"])
                   for s in spec["sections"])
    faq = "".join(f'<div class="q">{_esc(f["q"])}</div><div class="a">{_esc(f["a"])}</div>' for f in spec["faq"])
    body = f"""{_head(spec['title'] + ' | ART3RY', spec['meta_description'], canon, jsonld)}
<header class="hero" style="padding-bottom:30px"><div class="wrap"><div class="kicker">ART3RY Blog</div>
<h1 style="font-size:clamp(28px,4.4vw,46px)">{_esc(spec['title'])}</h1><p class="sub">{_esc(spec['dek'])}</p></div></header>
<article class="article">{secs}<h2>FAQ</h2><div class="faq" style="max-width:none">{faq}</div></article>
<section class="section"><div class="cta-strip wrap"><h2>Stop doing the work behind the work.</h2><p>ART3RY is the AI assistant that runs it for you.</p><a href="/get-started/">Get your assistant &rarr;</a></div></section>
{_FOOTER}{_ANALYTICS}</body></html>"""
    return slug, _guard(body, f"blog:{slug}")


def render_hub(spec: dict, all_hubs: list[dict]) -> tuple[str, str]:
    """A playbook hub page (/playbook/<slug>/): the pillar that binds one topic
    cluster. Lists every spoke with a one-line reason to read it, points at the
    matching service, and cross-references sibling hubs. Spec: specs_playbook.json,
    which scripts/wire_playbook.py also reads to inject the spoke->hub backlinks."""
    slug = spec["slug"].strip("/")
    canon = f"{SITE}/playbook/{slug}/"
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": canon + "#page", "name": spec["title_tag"],
         "description": spec["meta_description"], "url": canon,
         "isPartOf": {"@type": "WebSite", "name": "Art3ry", "url": SITE + "/"}},
        {"@type": "ItemList", "@id": canon + "#list",
         "itemListElement": [{"@type": "ListItem", "position": i + 1,
                              "name": s["title"], "url": SITE + s["href"]}
                             for i, s in enumerate(spec["spokes"])]},
        {"@type": "BreadcrumbList", "@id": canon + "#crumbs", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "The Growth Playbook", "item": SITE + "/playbook/"},
            {"@type": "ListItem", "position": 2, "name": spec["h1"], "item": canon}]},
    ]}
    intro = "".join(f'<p class="lead" style="margin-bottom:14px">{_esc_p(p)}</p>' for p in spec["intro"])
    cards = "".join(
        f'<div class="card"><div class="tag">{_esc(s["tag"])}</div>'
        f'<h3><a href="{s["href"]}">{_esc(s["title"])}</a></h3>'
        f'<p style="font-size:14.5px;color:var(--ink-2);margin-bottom:10px">{_esc(s["hook"])}</p>'
        f'<a href="{s["href"]}" style="color:var(--blue);font-size:14px;font-weight:600">Read it &rarr;</a></div>'
        for s in spec["spokes"])
    by_slug = {h["slug"]: h for h in all_hubs}
    related = " &middot; ".join(
        f'<a href="/playbook/{r}/" style="color:var(--blue);text-decoration:none">{_esc(by_slug[r]["h1"])}</a>'
        for r in spec.get("related", []) if r in by_slug)
    svc = spec["service"]
    body = f"""{_head(spec['title_tag'], spec['meta_description'], canon, jsonld)}
<header class="hero" style="padding-bottom:34px"><div class="wrap"><div class="kicker">{_esc(spec['kicker'])} &middot; <a href="/playbook/" style="color:inherit">The Growth Playbook</a></div>
<h1 style="font-size:clamp(30px,4.8vw,50px)">{_h1(spec['h1'])}</h1><p class="sub">{_esc(spec['hero_sub'])}</p></div></header>
<section class="section"><div class="wrap" style="max-width:760px">{intro}</div></section>
<section class="section"><h2>Read it in this order</h2><div class="cards wrap">{cards}</div></section>
<section class="section"><div class="cta-strip wrap"><h2>{_esc(svc['label'])}</h2><p>{_esc(svc['line'])}</p><a href="{svc['href']}">Start with a free diagnostic &rarr;</a></div></section>
<section class="section"><p style="text-align:center;color:var(--ink-2);font-size:14px">Keep going: {related} &middot; <a href="/playbook/" style="color:var(--blue);text-decoration:none">all playbooks &rarr;</a></p></section>
{_FOOTER}{_ANALYTICS}</body></html>"""
    return slug, _guard(body, f"hub:{slug}")


def render_service(spec: dict) -> tuple[str, str]:
    """A growth-as-a-service page (SEO, follow-up, websites, automation...). Sibling
    of render_landing, but service-framed (not assistant-framed) and cross-linked
    up to the /services/ hub."""
    slug = spec["slug"].strip("/")
    canon = f"{SITE}/{slug}/"
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": canon + "#service",
         "serviceType": spec.get("service_type", "Business growth service"),
         "name": spec["title_tag"], "description": spec["meta_description"],
         "provider": {"@type": "Organization", "name": "Art3ry", "url": SITE + "/"},
         "areaServed": {"@type": "Country", "name": "United States"}},
        {"@type": "FAQPage", "@id": canon + "#faq",
         "mainEntity": [{"@type": "Question", "name": f["q"],
                         "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in spec["faq"]]},
    ]}
    steps = "".join(
        f'<div class="step"><div class="n">{_esc(s["n"])}</div><h3>{_esc(s["h3"])}</h3><p>{_esc(s["p"])}</p></div>'
        for s in spec["steps"])
    cards = "".join(
        f'<div class="card"><div class="tag">{_esc(c["tag"])}</div><h3>{_esc(c["h3"])}</h3>'
        f'<div class="say">{_esc(c["say"])}</div><ul>'
        + "".join(f"<li>{_esc(b)}</li>" for b in c["bullets"]) + "</ul></div>"
        for c in spec["scenarios"])
    faq = "".join(f'<div class="q">{_esc(f["q"])}</div><div class="a">{_esc(f["a"])}</div>' for f in spec["faq"])
    body = f"""{_head(spec['title_tag'], spec['meta_description'], canon, jsonld)}
<header class="hero"><div class="wrap"><div class="kicker">{_esc(spec['kicker'])}</div>
<h1>{_h1(spec['h1'])}</h1><p class="sub">{_esc(spec['hero_sub'])}</p>
<div class="btns"><a href="/get-started/" class="btn-primary">Start with a free diagnostic &rarr;</a>
<a href="https://jessemoraga.com" target="_blank" rel="noopener" class="btn-secondary">See it running a real business</a></div></div></header>
<section class="section"><h2>{_esc(spec['what_h2'])}</h2><p class="lead">{_esc(spec['what_lead'])}</p><div class="steps wrap">{steps}</div></section>
<section class="section"><h2>{_esc(spec['inc_h2'])}</h2><div class="cards wrap">{cards}</div></section>
<section class="section"><p class="proof">Not a pitch deck. Every Art3ry service already runs <a href="https://jessemoraga.com" target="_blank" rel="noopener">a real California field-services company</a>, a real one-person company.</p></section>
<section class="section"><h2>Questions</h2><div class="faq">{faq}</div></section>
<section class="section"><p style="text-align:center;color:var(--ink-2);font-size:14px">Part of <a href="/services/" style="color:var(--blue);text-decoration:none">Art3ry growth-as-a-service</a> &middot; <a href="/services/" style="color:var(--blue);text-decoration:none">see all services &rarr;</a></p></section>
<section class="section"><div class="cta-strip wrap"><h2>{_esc(spec['cta_h2'])}</h2><p>{_esc(spec['cta_p'])}</p><a href="/get-started/">Get started &rarr;</a></div></section>
{_FOOTER}{_ANALYTICS}</body></html>"""
    return slug, _guard(body, f"service:{slug}")


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: build_pages.py specs.json"); return 2
    specs = json.loads(Path(argv[0]).read_text())
    written, sitemap_urls = [], []

    for spec in specs.get("audience", []) + specs.get("industry", []):
        slug, page = render_landing(spec)
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT))); sitemap_urls.append(f"{SITE}/{slug}/")

    for spec in specs.get("service", []):
        slug, page = render_service(spec)
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT))); sitemap_urls.append(f"{SITE}/{slug}/")

    hubs = specs.get("hub", [])
    for spec in hubs:
        slug, page = render_hub(spec, hubs)
        out = ROOT / "playbook" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT))); sitemap_urls.append(f"{SITE}/playbook/{slug}/")

    blog_cards = []
    for spec in specs.get("blog", []):
        slug, page = render_blog(spec)
        out = ROOT / "blog" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT))); sitemap_urls.append(f"{SITE}/blog/{slug}/")
        blog_cards.append((spec["title"], f"/blog/{slug}/", spec["meta_description"]))

    # MERGE sitemap.xml: keep every URL already listed AND the <lastmod> banked
    # against it, then add core + everything generated this run. A partial spec must
    # never silently drop existing pages, and a rebuild must never strip lastmod —
    # re-emitting bare <loc> throws away crawl-scheduling signal we cannot recover.
    lastmod: dict[str, str | None] = {}
    order: list[str] = []
    sm_path = ROOT / "sitemap.xml"
    if sm_path.exists():
        for block in re.findall(r"<url>(.*?)</url>", sm_path.read_text(), re.S):
            loc = re.search(r"<loc>(.*?)</loc>", block)
            if not loc:
                continue
            u = loc.group(1)
            if u not in lastmod:
                order.append(u)
            lm = re.search(r"<lastmod>(.*?)</lastmod>", block)
            lastmod[u] = lm.group(1) if lm else lastmod.get(u)

    # /assistant/ is intentionally noindex,follow and out of the sitemap (3fdd684):
    # submitting a noindexed URL sends Google two contradictory instructions.
    core = ["", "services/", "about/", "blog/", "get-started/"]
    for u in [f"{SITE}/{c}" for c in core]:
        if u not in lastmod:
            order.append(u); lastmod[u] = None

    # Only pages actually rewritten this run get a fresh lastmod.
    today = date.today().isoformat()
    for u in sitemap_urls:
        if u not in lastmod:
            order.append(u)
        lastmod[u] = today

    rows = "".join(
        f"  <url><loc>{u}</loc>"
        + (f"<lastmod>{lastmod[u]}</lastmod>" if lastmod.get(u) else "")
        + "</url>\n"
        for u in order
    )
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + rows + "</urlset>\n")
    (ROOT / "sitemap.xml").write_text(sm)

    kept = sum(1 for u in order if lastmod.get(u))
    print(f"build_pages: wrote {len(written)} pages + sitemap ({len(order)} urls, {kept} with lastmod)")
    for w in written:
        print("  ", w)
    # emit blog-card snippets for manual blog-index wiring
    if blog_cards:
        (ROOT / "scripts" / "_blog_cards.json").write_text(json.dumps(blog_cards, indent=2))
        print("   (blog cards -> scripts/_blog_cards.json for the blog index)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
