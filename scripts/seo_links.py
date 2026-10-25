#!/usr/bin/env python3
"""Internal-link pass (2026-10-24 audit): every service page linked from every page, and each blog
post pointed at the service it is about. Idempotent: rerun after any rebuild.

    python3 scripts/seo_links.py          # rewrite pages in place, print what changed

Why: the crawl found AI Phone Assistant, AI Search and Marketing reachable only from / and /services/
(2 internal links each) while blog posts about missed calls, AI answers and reviews never linked to them.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVICES = [("/services/websites/", "Websites"), ("/services/seo/", "Local SEO"),
            ("/services/ai-search/", "AI Search"), ("/services/ai-phone-assistant/", "AI Phone Assistant"),
            ("/services/lead-follow-up/", "Lead Follow-Up"), ("/services/automation/", "Automation"),
            ("/services/marketing/", "Marketing")]
FOOTER_ANCHOR = ('<a href="/services/">The Growth Build</a><a href="/about/">About</a>'
                 '<a href="/blog/">Blog</a><a href="/california/">California</a>')
FOOTER_SERVICES = "\n    " + "".join(f'<a href="{u}">{n}</a>' for u, n in SERVICES)
# Topic words in a post's slug + title -> the service it should send readers to (first match wins order).
TOPICS = [
    (("phone", "call", "receptionist", "voicemail", "answering", "after-hours", "voice", "ai-employee"), "/services/ai-phone-assistant/"),
    (("ai-search", "chatgpt", "ai-overview", "answer-engine", "show-up-in-ai", "perplexity", "llm"), "/services/ai-search/"),
    (("follow-up", "follow-up", "quote", "lead-response", "5-minute", "speed-to-lead", "no-show"), "/services/lead-follow-up/"),
    (("invoic", "automat", "agent", "workflow", "bookkeep", "paperwork", "scheduling", "software", "saas",
      "operating-system", "gohighlevel", "autopilot"), "/services/automation/"),
    (("review", "marketing", "social", "customers", "ads", "newsletter", "growth", "referral", "charge"), "/services/marketing/"),
    (("seo", "rank", "google", "service-area", "local-search", "maps"), "/services/seo/"),
    (("website", "web-design", "landing", "conversion", "site"), "/services/websites/"),
]
NAMES = dict(SERVICES)
MARK = "<!-- service-link -->"


def pick(slug: str, title: str) -> list[str]:
    hay = f"{slug} {title}".lower().replace(" ", "-")
    out = [svc for words, svc in TOPICS if any(w in hay for w in words)]
    return list(dict.fromkeys(out))[:2] or ["/services/websites/", "/services/lead-follow-up/"]


def service_line(svcs: list[str]) -> str:
    links = " and ".join(f'<a href="{s}" style="color:var(--blue);text-decoration:none">{NAMES[s]}</a>' for s in svcs)
    return (f'{MARK}<section class="section"><p style="text-align:center;color:var(--ink-2);font-size:14px">'
            f'Related service: {links} &middot; <a href="/services/" style="color:var(--blue);'
            f'text-decoration:none">see the full Growth Build &rarr;</a></p></section>\n')


def process(path: Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    before, changes = html, []
    if FOOTER_ANCHOR in html and FOOTER_SERVICES.strip() not in html:
        html = html.replace(FOOTER_ANCHOR, FOOTER_ANCHOR + FOOTER_SERVICES, 1)
        changes.append("footer")
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("blog/") and rel != "blog/index.html":
        slug = rel.split("/")[1]
        title = re.search(r"<title>(.*?)</title>", html, re.S)
        line = service_line(pick(slug, title.group(1) if title else ""))
        html = re.sub(re.escape(MARK) + r".*?</section>\n", "", html, flags=re.S)
        cta = html.find('<section class="section"><div class="cta-strip')
        if cta != -1:
            html = html[:cta] + line + html[cta:]
            changes.append("related")
    if html != before:
        path.write_text(html, encoding="utf-8")
    return changes if html != before else []


def main() -> int:
    n = 0
    for p in sorted(ROOT.rglob("index.html")):
        if ".git" in p.parts or "scripts" in p.parts:
            continue
        ch = process(p)
        if ch:
            n += 1
            print(f"{p.relative_to(ROOT)}: {', '.join(ch)}")
    print(f"{n} pages updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
