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
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://art3ry.com"

# Shared brand CSS (matches the live homepage + /assistant/ page).
_CSS = """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#060810;--bg-card:#090c1b;--bg-raised:#0d1126;--red:#e63946;--red-dim:rgba(230,57,70,.14);--red-glow:rgba(230,57,70,.3);--blue:#3a86ff;--blue-dim:rgba(58,134,255,.12);--border:rgba(255,255,255,.08);--border-red:rgba(230,57,70,.3);--text:#dde1f0;--muted:#6a7490;--mono:ui-monospace,SFMono-Regular,Menlo,monospace}
body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:inherit}
nav{display:flex;align-items:center;justify-content:space-between;padding:20px 40px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(6,8,16,.85);backdrop-filter:blur(12px);z-index:50}
.logo-img{height:46px}
.nav-links{display:flex;gap:26px;font-size:14px;color:var(--muted)}.nav-links a{text-decoration:none}.nav-links a:hover{color:#fff;transition:color .15s}
.nav-cta{font-size:14px;font-weight:600;color:#fff;background:var(--red);padding:10px 18px;border-radius:8px;text-decoration:none;box-shadow:0 0 24px var(--red-glow)}
.wrap{max-width:1060px;margin:0 auto;padding:0 40px}
.hero{text-align:center;padding:84px 40px 56px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:-160px;left:50%;transform:translateX(-50%);width:900px;height:600px;background:radial-gradient(ellipse,var(--red-dim),transparent 62%);pointer-events:none}
.kicker{font-family:var(--mono);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--red);margin-bottom:20px}
h1{font-size:clamp(32px,5.4vw,58px);font-weight:900;line-height:1.05;letter-spacing:-.035em;color:#fff;position:relative}
h1 .b{color:var(--blue)}
.sub{font-size:19px;color:var(--muted);max-width:640px;margin:22px auto 0;line-height:1.6}.sub strong{color:var(--text)}
.btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:32px}
.btn-primary{display:inline-block;background:var(--red);color:#fff;font-weight:700;padding:15px 32px;border-radius:10px;text-decoration:none;box-shadow:0 0 40px var(--red-glow)}
.btn-secondary{display:inline-block;border:1px solid var(--border);color:var(--text);font-weight:600;padding:15px 28px;border-radius:10px;text-decoration:none}
.section{padding:56px 40px}
.section h2{font-size:clamp(25px,3.4vw,36px);font-weight:800;letter-spacing:-.02em;color:#fff;text-align:center;margin-bottom:12px}
.section .lead{color:var(--muted);text-align:center;max-width:640px;margin:0 auto 42px;font-size:16px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.step{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:28px 24px}
.step .n{font-family:var(--mono);font-size:13px;color:var(--red);font-weight:700;margin-bottom:12px}
.step h3{font-size:18px;color:#fff;margin-bottom:8px}.step p{font-size:14.5px;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:30px 26px;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:linear-gradient(90deg,var(--red),var(--blue))}
.card .tag{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:14px}
.card h3{font-size:20px;color:#fff;margin-bottom:12px;letter-spacing:-.01em}
.card .say{font-style:italic;color:var(--text);background:var(--bg-raised);border-left:3px solid var(--red);padding:12px 14px;border-radius:8px;font-size:14.5px;margin-bottom:14px}
.card ul{list-style:none;font-size:14px;color:var(--muted)}.card li{padding:5px 0 5px 22px;position:relative}.card li::before{content:'\\2192';position:absolute;left:0;color:var(--red)}
.safe{background:linear-gradient(180deg,var(--bg-card),var(--bg));border:1px solid var(--border-red);border-radius:20px;padding:42px 40px;text-align:center;max-width:820px;margin:0 auto}
.safe p{color:var(--muted);max-width:600px;margin:10px auto 0;font-size:16px}
.proof{text-align:center;color:var(--muted);font-size:15px}.proof a{color:var(--blue);text-decoration:none}
.faq{max-width:760px;margin:0 auto}.faq .q{font-weight:700;color:#fff;margin:22px 0 6px;font-size:16px}.faq .a{color:var(--muted);font-size:15px}
.article{max-width:740px;margin:0 auto;padding:10px 40px 30px}.article h2{font-size:23px;color:#fff;margin:34px 0 10px;border-left:3px solid var(--red);padding-left:12px}.article p{color:#c7cee0;margin:0 0 15px;font-size:16.5px}
.cta-strip{background:linear-gradient(120deg,var(--red),#b5202d);border-radius:20px;padding:48px 40px;text-align:center;margin:18px auto 64px;max-width:980px}
.cta-strip h2{color:#fff;font-size:clamp(25px,4vw,38px);font-weight:900;margin-bottom:12px}.cta-strip p{color:rgba(255,255,255,.9);margin-bottom:24px}.cta-strip a{display:inline-block;background:#fff;color:var(--red);font-weight:800;padding:16px 38px;border-radius:10px;text-decoration:none}
footer{display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;padding:34px 40px;border-top:1px solid var(--border)}
.footer-links{display:flex;gap:22px;font-size:13px;color:var(--muted);flex-wrap:wrap}.footer-links a{text-decoration:none}.footer-links a:hover{color:#fff}
@media(max-width:768px){.nav-links{display:none}.steps,.cards{grid-template-columns:1fr}.wrap,.section,.hero,.article{padding-left:20px;padding-right:20px}footer{flex-direction:column;text-align:center}}"""

_NAV = """<nav>
  <a href="/" class="logo"><img src="/assets/art3ry-logo.png" alt="ART3RY" class="logo-img" style="border-radius:4px"></a>
  <div class="nav-links">
    <a href="/assistant/">Assistant</a><a href="/about/">About</a><a href="/blog/">Blog</a>
    <a href="https://centralvalleyprocessservers.com/powered-by-art3ry/" target="_blank" rel="noopener">The Proof</a>
  </div>
  <a href="/get-started/" class="nav-cta">Get started &rarr;</a>
</nav>"""

_FOOTER = """<footer>
  <div style="display:flex;flex-direction:column;gap:6px">
    <div><img src="/assets/art3ry-logo.png" alt="ART3RY" style="height:24px;border-radius:3px"></div>
    <p style="font-size:11px;color:var(--muted)">&copy; 2026 ART3RY, LLC — California</p>
  </div>
  <div class="footer-links">
    <a href="/assistant/">Assistant</a><a href="/about/">About</a><a href="/blog/">Blog</a>
    <a href="/get-started/">Get Started</a>
    <a href="https://centralvalleyprocessservers.com/powered-by-art3ry/" target="_blank" rel="noopener">The Proof</a>
  </div>
  <div><a href="mailto:jesse@art3ry.com" style="font-size:12px;color:var(--muted);text-decoration:none">jesse@art3ry.com</a></div>
</footer>"""

# Phone leak guard — Jesse's cell must NEVER reach a public page (mirrors the CVPS rule).
_CELL_DIGITS = "4283688"


def _esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def _h1(s: str) -> str:
    # allow a single <br> in the headline; escape the rest, add a space after <br> so
    # crawlers don't read concatenated words.
    parts = (s or "").split("<br>", 1)
    return _esc(parts[0]) + ("<br>\n" + _esc(parts[1].strip()) if len(parts) > 1 else "")


def _head(title, desc, canon, jsonld) -> str:
    t, d = _esc(title), _esc(desc)
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:url" content="{canon}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<meta property="og:image" content="{SITE}/assets/art3ry-brand.jpg"><meta property="og:site_name" content="ART3RY">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{SITE}/assets/art3ry-brand.jpg">
<script type="application/ld+json">{json.dumps(jsonld, separators=(',', ':'))}</script>
<style>{_CSS}</style></head><body>
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
<header class="hero"><div class="wrap"><div class="kicker">Your AI Assistant</div>
<h1>{_h1(spec['h1'])}</h1><p class="sub">{_esc(spec['hero_sub'])}</p>
<div class="btns"><a href="/get-started/" class="btn-primary">Get your assistant &rarr;</a>
<a href="https://centralvalleyprocessservers.com/powered-by-art3ry/" target="_blank" rel="noopener" class="btn-secondary">See it running a real business</a></div></div></header>
<section class="section"><h2>It's this simple</h2><p class="lead">No app to learn. You just talk.</p><div class="steps wrap">{steps}</div></section>
<section class="section"><h2>How it shows up in your day</h2><div class="cards wrap">{cards}</div></section>
<section class="section"><div class="safe"><h2 style="color:#fff;font-size:30px;font-weight:800">Powerful, because it's safe</h2><p>{_esc(spec['safety_line'])}</p></div></section>
<section class="section"><p class="proof">Not a demo — ART3RY runs <a href="https://centralvalleyprocessservers.com/powered-by-art3ry/" target="_blank" rel="noopener">Central Valley Process Servers</a>, a real one-person company.</p></section>
<section class="section"><h2>Questions</h2><div class="faq">{faq}</div></section>
<section class="section"><div class="cta-strip wrap"><h2>Hand off the work behind the work.</h2><p>Tell us what's eating your day. We'll wire your assistant to it.</p><a href="/get-started/">Get your assistant &rarr;</a></div></section>
{_FOOTER}</body></html>"""
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
    secs = "".join(f"<h2>{_esc(s['h2'])}</h2>" + "".join(f"<p>{_esc(p)}</p>" for p in s["paragraphs"])
                   for s in spec["sections"])
    faq = "".join(f'<div class="q">{_esc(f["q"])}</div><div class="a">{_esc(f["a"])}</div>' for f in spec["faq"])
    body = f"""{_head(spec['title'] + ' | ART3RY', spec['meta_description'], canon, jsonld)}
<header class="hero" style="padding-bottom:30px"><div class="wrap"><div class="kicker">ART3RY Blog</div>
<h1 style="font-size:clamp(28px,4.4vw,46px)">{_esc(spec['title'])}</h1><p class="sub">{_esc(spec['dek'])}</p></div></header>
<article class="article">{secs}<h2>FAQ</h2><div class="faq" style="max-width:none">{faq}</div></article>
<section class="section"><div class="cta-strip wrap"><h2>Stop doing the work behind the work.</h2><p>ART3RY is the AI assistant that runs it for you.</p><a href="/get-started/">Get your assistant &rarr;</a></div></section>
{_FOOTER}</body></html>"""
    return slug, _guard(body, f"blog:{slug}")


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

    blog_cards = []
    for spec in specs.get("blog", []):
        slug, page = render_blog(spec)
        out = ROOT / "blog" / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT))); sitemap_urls.append(f"{SITE}/blog/{slug}/")
        blog_cards.append((spec["title"], f"/blog/{slug}/", spec["meta_description"]))

    # rewrite sitemap.xml with the full known set (home + core + everything generated)
    core = ["", "assistant/", "about/", "blog/", "get-started/"]
    all_urls = [f"{SITE}/{u}" for u in core] + sitemap_urls
    seen, uniq = set(), []
    for u in all_urls:
        if u not in seen:
            seen.add(u); uniq.append(u)
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{u}</loc></url>\n" for u in uniq) + "</urlset>\n")
    (ROOT / "sitemap.xml").write_text(sm)

    print(f"build_pages: wrote {len(written)} pages + sitemap ({len(uniq)} urls)")
    for w in written:
        print("  ", w)
    # emit blog-card snippets for manual blog-index wiring
    if blog_cards:
        (ROOT / "scripts" / "_blog_cards.json").write_text(json.dumps(blog_cards, indent=2))
        print("   (blog cards -> scripts/_blog_cards.json for the blog index)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
