#!/usr/bin/env python3
"""build_california.py - the "Claim California" page set (hub, cities, industries, combos).

Imports the shared head/nav/footer helpers from build_pages.py so the chrome stays
in sync with the rest of the site, and keeps its own render functions + content so
it never edits the shared templates. Does NOT touch sitemap.xml (the lead regenerates
it; run `python3 scripts/build_california.py --urls` to list the URLs).

Content lives in scripts/ca_content/*.py (CITIES, INDUSTRIES, COMBOS). Every page is
hand-written: the renderer only supplies structure, schema and the link graph.

Usage:  python3 scripts/build_california.py [--urls]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pages as bp  # noqa: E402
from ca_content import CITIES, INDUSTRIES, COMBOS, HUB  # noqa: E402

ROOT, SITE = bp.ROOT, bp.SITE
MIN_WORDS = 700
BAD = ("—", "–", "cvps", "central valley process", "process serv", "428-3688", "PS-124")

PROOF = ("The system behind this work is not a pitch deck. More than 700 jobs have run through it, and "
         "the field-services company it operates grew organic traffic 60% in 28 days with zero ad spend. "
         "You can see that business at [jessemoraga.com](https://jessemoraga.com).")

SERVICE_LINKS = [
    ("/services/seo/", "Local SEO and content"),
    ("/services/websites/", "Websites that convert"),
    ("/services/lead-follow-up/", "Lead follow-up"),
    ("/services/automation/", "Automation"),
    ("/google-business-profile-optimization/", "Google Business Profile"),
]

IND = {i["slug"]: i for i in INDUSTRIES}
CITY = {c["slug"]: c for c in CITIES}


def p(txt: str) -> str:
    # the shared _esc_p only opens [text](/internal/) links; allow the one external proof link
    out = bp._esc_p(txt)
    return re.sub(r"\[([^\]]+)\]\((https://jessemoraga\.com)\)",
                  lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', out)


def url(slug: str) -> str:
    return f"/california/{slug}/" if slug else "/california/"


def crumbs(canon, name, parent=None):
    items = [("Home", SITE + "/"), ("California", SITE + "/california/")]
    if parent:
        items.append(parent)
    if name != "California":
        items.append((name, canon))
    return {"@type": "BreadcrumbList", "@id": canon + "#crumbs",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(items)]}


def faq_ld(canon, faq):
    return {"@type": "FAQPage", "@id": canon + "#faq",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def service_ld(canon, pg, area):
    return {"@type": "Service", "@id": canon + "#service", "serviceType": pg["service_type"],
            "name": pg["title"], "description": pg["meta"], "url": canon,
            "provider": {"@type": "Organization", "name": "Art3ry", "url": SITE + "/"},
            "areaServed": area}


def sec(h2, paras, bullets=None):
    body = "".join(f'<p style="margin-bottom:14px">{p(x)}</p>' for x in paras)
    if bullets:
        body += ('<ul style="margin:0 0 14px 20px;line-height:1.7">'
                 + "".join(f"<li>{p(b)}</li>" for b in bullets) + "</ul>")
    return f'<section class="section"><div class="wrap" style="max-width:760px"><h2>{bp._esc(h2)}</h2>{body}</div></section>'


def link_list(items):
    return ('<ul style="margin:0 0 6px 20px;line-height:1.8">'
            + "".join(f'<li><a href="{h}">{bp._esc(t)}</a></li>' for h, t in items) + "</ul>")


def authored_text(pg):
    parts = [pg["sub"]] + pg["lead"]
    for _, ps, bl in pg["secs"]:
        parts += ps + (bl or [])
    for q, a in pg["faq"]:
        parts += [q, a]
    parts += list(pg.get("ind_notes", {}).values())
    return " ".join(parts)


def related_block(pg):
    kind = pg["kind"]
    groups = []
    if kind == "city":
        groups.append(("Nearby California markets", [(url(s), CITY[s]["name"]) for s in pg["nearby"]]))
        groups.append(("The four trades", [(url(i["slug"]), i["short"] + " in California") for i in INDUSTRIES]))
        cb = [(url(c["slug"]), c["title_short"]) for c in COMBOS if c["city"] == pg["slug"]]
        if cb:
            groups.append(("In this city, specifically", cb))
    elif kind == "industry":
        groups.append(("Where this gets built", [(url(c["slug"]), c["name"]) for c in CITIES]))
        cb = [(url(c["slug"]), c["title_short"]) for c in COMBOS if c["industry"] == pg["slug"]]
        if cb:
            groups.append(("A closer look", cb))
        groups.append(("The other trades", [(url(i["slug"]), i["short"]) for i in INDUSTRIES if i["slug"] != pg["slug"]]))
    else:  # combo
        groups.append(("The city page", [(url(pg["city"]), CITY[pg["city"]]["name"] + " overview")]))
        groups.append(("The trade page", [(url(pg["industry"]), IND[pg["industry"]]["short"] + " in California")]))
        sib = [(url(c["slug"]), c["title_short"]) for c in COMBOS if c["slug"] != pg["slug"]][:3]
        groups.append(("More California", sib))
    groups.append(("What I do about it", SERVICE_LINKS + [("/diagnostic/", "Free diagnostic")]))
    inner = "".join(f'<h3 style="margin:18px 0 6px">{bp._esc(t)}</h3>{link_list(l)}' for t, l in groups)
    return (f'<section class="section"><div class="wrap" style="max-width:760px"><h2>Keep going</h2>{inner}'
            f'<p style="margin-top:14px"><a href="/california/">All of California</a></p></div></section>')


def render_page(pg):
    slug, kind = pg["slug"], pg["kind"]
    canon = f"{SITE}/california/{slug}/"
    if kind == "city":
        area = {"@type": "City", "name": pg["name"], "containedInPlace": {"@type": "State", "name": "California"}}
        parent = None
    elif kind == "industry":
        area = {"@type": "State", "name": "California"}
        parent = None
    else:
        area = {"@type": "City", "name": pg["name"], "containedInPlace": {"@type": "State", "name": "California"}}
        parent = (CITY[pg["city"]]["name"], f"{SITE}/california/{pg['city']}/")
    jsonld = {"@context": "https://schema.org",
              "@graph": [service_ld(canon, pg, area), faq_ld(canon, pg["faq"]), crumbs(canon, pg["crumb"], parent)]}
    lead = "".join(f'<p class="lead" style="margin-bottom:14px">{p(x)}</p>' for x in pg["lead"])
    secs = "".join(sec(*s) if len(s) == 3 else sec(s[0], s[1]) for s in pg["secs"])
    if kind == "city":
        notes = "".join(f"<h3 style='margin:16px 0 4px'><a href=\"{url(i['slug'])}\">{bp._esc(i['short'])}</a></h3>"
                        f"<p style='margin-bottom:8px'>{p(pg['ind_notes'][i['slug']])}</p>" for i in INDUSTRIES)
        secs += (f'<section class="section"><div class="wrap" style="max-width:760px">'
                 f'<h2>The four trades, {bp._esc(pg["name"])} version</h2>{notes}</div></section>')
    faq = "".join(f'<div class="q">{bp._esc(q)}</div><div class="a">{bp._esc(a)}</div>' for q, a in pg["faq"])
    body = f"""{bp._head(pg['title'], pg['meta'], canon, jsonld)}
<header class="hero"><div class="wrap"><div class="kicker">{bp._esc(pg['kicker'])} &middot; <a href="/california/" style="color:inherit">California</a></div>
<h1>{bp._h1(pg['h1'])}</h1><p class="sub">{bp._esc(pg['sub'])}</p>
<div class="btns"><a href="/diagnostic/" class="btn-primary">Start with a free diagnostic &rarr;</a>
<a href="/get-started/" class="btn-secondary">Tell me what you do</a></div></div></header>
<section class="section"><div class="wrap" style="max-width:760px">{lead}</div></section>
{secs}
<section class="section"><div class="wrap" style="max-width:760px"><p class="proof">{p(PROOF)}</p></div></section>
<section class="section"><h2>Questions</h2><div class="faq">{faq}</div></section>
{related_block(pg)}
<section class="section"><div class="cta-strip wrap"><h2>{bp._esc(pg['cta_h2'])}</h2><p>{bp._esc(pg['cta_p'])}</p><a href="/diagnostic/">Start with a free diagnostic &rarr;</a></div></section>
{bp._FOOTER}{bp._ANALYTICS}</body></html>"""
    return bp._guard(body, f"california:{slug}")


def render_hub():
    canon = f"{SITE}/california/"
    items = [(url(c["slug"]), c["name"]) for c in CITIES] + [(url(i["slug"]), i["title_short"]) for i in INDUSTRIES] \
        + [(url(c["slug"]), c["title_short"]) for c in COMBOS]
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": canon + "#page", "name": HUB["title"], "description": HUB["meta"],
         "url": canon, "isPartOf": {"@type": "WebSite", "name": "Art3ry", "url": SITE + "/"}},
        {"@type": "ItemList", "@id": canon + "#list",
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": SITE + h}
                             for i, (h, n) in enumerate(items)]},
        faq_ld(canon, HUB["faq"]), crumbs(canon, "California")]}
    lead = "".join(f'<p class="lead" style="margin-bottom:14px">{p(x)}</p>' for x in HUB["lead"])
    def cards(rows):
        return "".join(f'<div class="card"><h3><a href="{h}">{bp._esc(t)}</a></h3>'
                       f'<p style="font-size:14.5px;color:var(--ink-2)">{bp._esc(d)}</p></div>' for h, t, d in rows)
    city_cards = cards([(url(c["slug"]), c["name"], c["hub_line"]) for c in CITIES])
    ind_cards = cards([(url(i["slug"]), i["title_short"], i["hub_line"]) for i in INDUSTRIES])
    combo_cards = cards([(url(c["slug"]), c["title_short"], c["hub_line"]) for c in COMBOS])
    secs = "".join(sec(*s) for s in HUB["secs"])
    faq = "".join(f'<div class="q">{bp._esc(q)}</div><div class="a">{bp._esc(a)}</div>' for q, a in HUB["faq"])
    body = f"""{bp._head(HUB['title'], HUB['meta'], canon, jsonld)}
<header class="hero"><div class="wrap"><div class="kicker">Growth-as-a-service &middot; California</div>
<h1>{bp._h1(HUB['h1'])}</h1><p class="sub">{bp._esc(HUB['sub'])}</p>
<div class="btns"><a href="/diagnostic/" class="btn-primary">Start with a free diagnostic &rarr;</a></div></div></header>
<section class="section"><div class="wrap" style="max-width:760px">{lead}</div></section>
<section class="section"><h2>By city</h2><div class="cards wrap">{city_cards}</div></section>
<section class="section"><h2>By trade</h2><div class="cards wrap">{ind_cards}</div></section>
<section class="section"><h2>City and trade, together</h2><div class="cards wrap">{combo_cards}</div></section>
{secs}
<section class="section"><div class="wrap" style="max-width:760px"><p class="proof">{p(PROOF)}</p></div></section>
<section class="section"><h2>Questions</h2><div class="faq">{faq}</div></section>
<section class="section"><div class="wrap" style="max-width:760px"><h2>Services behind all of it</h2>{link_list(SERVICE_LINKS)}</div></section>
<section class="section"><div class="cta-strip wrap"><h2>Not sure where you fit?</h2><p>Tell me what you do and where your customers are. I will tell you what I would build first.</p><a href="/diagnostic/">Start with a free diagnostic &rarr;</a></div></section>
{bp._FOOTER}{bp._ANALYTICS}</body></html>"""
    return bp._guard(body, "california:hub")


def validate(pages):
    problems = []
    titles, metas, h1s = {}, {}, {}
    for pg in pages:
        txt = authored_text(pg)
        n = len(txt.split())
        low = txt.lower() + pg["title"].lower() + pg["meta"].lower()
        for b in BAD:
            if b.lower() in low:
                problems.append(f"{pg['slug']}: banned string {b!r}")
        if n < MIN_WORDS:
            problems.append(f"{pg['slug']}: only {n} words")
        if len(pg["title"]) > 62:
            problems.append(f"{pg['slug']}: title {len(pg['title'])} chars")
        if len(pg["meta"]) > 160:
            problems.append(f"{pg['slug']}: meta {len(pg['meta'])} chars")
        for k, d in ((pg["title"], titles), (pg["meta"], metas), (pg["h1"], h1s)):
            if k in d:
                problems.append(f"{pg['slug']}: duplicate with {d[k]}")
            d[k] = pg["slug"]
        for s in re.findall(r"\]\((/[^)]*)\)", " ".join([txt])):
            if not (ROOT / s.strip("/")).exists() and s.strip("/").split("/")[0] != "california":
                problems.append(f"{pg['slug']}: dead link {s}")
    return problems


def all_pages():
    return CITIES + INDUSTRIES + COMBOS


def main(argv=None):
    argv = argv or sys.argv[1:]
    pages = all_pages()
    if "--urls" in argv:
        print(f"{SITE}/california/")
        for pg in pages:
            print(f"{SITE}/california/{pg['slug']}/")
        return 0
    problems = validate(pages)
    if problems:
        print("\n".join(problems)); return 1
    out = ROOT / "california" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_hub(), encoding="utf-8")
    for pg in pages:
        o = ROOT / "california" / pg["slug"] / "index.html"
        o.parent.mkdir(parents=True, exist_ok=True)
        o.write_text(render_page(pg), encoding="utf-8")
        print(f"{len(authored_text(pg).split()):5d} words  /california/{pg['slug']}/")
    print(f"build_california: wrote hub + {len(pages)} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
