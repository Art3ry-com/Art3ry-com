#!/usr/bin/env python3
"""Idempotent title / meta-description retarget from the 2026-10-31 Semrush pull.

Each page is pointed at the keyword it can actually win (low difficulty, real
volume, buying intent) instead of its old brand-flavoured wording. Volumes and
difficulty are in 07_ANALYTICS/semrush_2026-10-31.md in the brand repo.
Rewrites <title>, og:title, twitter:title, and the three description tags.
H1s and body copy are untouched. Safe to re-run: a page already on the new
title is skipped.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# path -> (new title, new meta description <=160 chars)
PAGES = {
    "index.html": (
        "Art3ry: AI Receptionist, Local SEO & Lead Follow-Up",
        "Art3ry answers your calls, gets you found on Google and chases every lead until it closes. Built and run for you by one person. Start with a free diagnostic.",
    ),
    "services/ai-phone-assistant/index.html": (
        "AI Receptionist for Small Business: Done for You | ART3RY",
        "An AI receptionist for small business that answers every call, qualifies the caller and hands you a clean lead: name, phone, need. Built and run for you.",
    ),
    "never-lose-a-job-to-voicemail/index.html": (
        "Answering Service for Plumbers, HVAC & Electricians | ART3RY",
        "Answering service for plumbers, HVAC and electricians: every call picked up while your hands are full, the job captured, details texted to you. Done for you.",
    ),
    "blog/after-hours-answering-service/index.html": (
        "After Hours Answering Service for Small Business | ART3RY",
        "After hours answering service that catches the calls voicemail loses. How an always-on AI assistant captures your best jobs without putting you on call.",
    ),
    "blog/missed-call-lead-capture/index.html": (
        "Missed Call Text Back: Automatic Lead Capture | ART3RY",
        "Missed call text back for plumbers and trades: how to reply to, log and book every unanswered call automatically, so a ringing phone never becomes a lost job.",
    ),
    "blog/answering-service-pricing/index.html": (
        "Answering Service Pricing: What It Costs per Month | ART3RY",
        "Answering service pricing explained: per-minute vs per-call plans, why the headline rate is never what you pay, and the questions that reveal the real cost.",
    ),
    "blog/virtual-receptionist-companies-compared/index.html": (
        "Best AI & Virtual Receptionist Services Compared | ART3RY",
        "Virtual receptionist services compared: human, hybrid and AI. What each does well, where each fails, and how to pick the one your business actually needs.",
    ),
    "blog/ai-receptionist-cost-vs-front-desk-hire/index.html": (
        "AI Receptionist Cost: Pricing vs a Front-Desk Hire | ART3RY",
        "AI receptionist cost against a full-time front-desk hire. The salary is only part of it, and the hire still goes home at 5. The honest side-by-side math.",
    ),
    "blog/instant-lead-response-software-5-minute-rule/index.html": (
        "Speed to Lead: The 5-Minute Rule Explained | ART3RY",
        "Speed to lead: respond within 5 minutes and your odds of winning the job jump, wait longer and most go cold. How to hit the rule without living in your inbox.",
    ),
    "blog/hire-an-ai-employee/index.html": (
        "AI Employee: What One Can Do for Your Business | ART3RY",
        "An AI employee handles the back-office work you can't afford a person for. Connected to your email and calendar, working around the clock, with you in control.",
    ),
    "blog/seo-for-local-business/index.html": (
        "Local SEO for Small Business: What Actually Works | ART3RY",
        "Local SEO for small business: how to rank above bigger firms in your city, in the order to do it. Profile, reviews, pages, citations, and what to ignore.",
    ),
    "blog/how-to-rank-on-google-maps/index.html": (
        "How to Rank on Google Maps: Ranking Factors | ART3RY",
        "How to rank on Google Maps: proximity can't be bought, so category, profile completeness, reviews and steady activity are the factors you can win.",
    ),
    "seo-company-fresno/index.html": (
        "Fresno SEO Company: Local SEO for Small Business | ART3RY",
        "Fresno SEO company for small businesses: own local search in Fresno, Clovis and Madera instead of renting ads. Real work, honest pricing, free diagnostic first.",
    ),
    "google-business-profile-optimization/index.html": (
        "Google Business Profile Optimization Service | ART3RY",
        "Google Business Profile optimization, done for you: full setup, categories, photos, reviews and posts, run as part of a growth system. Free diagnostic first.",
    ),
}

TITLE_RE = re.compile(r"<title>([^<]*)</title>")
DESC_RE = re.compile(r'<meta name="description" content="([^"]*)"')


def _variants(raw_escaped: str) -> set:
    """The same string as it may appear in HTML attrs and in JSON-LD."""
    plain = html.unescape(raw_escaped)
    return {
        raw_escaped,
        html.escape(plain, quote=True),
        json.dumps(plain)[1:-1],
        json.dumps(plain, ensure_ascii=False)[1:-1],
    }


def main() -> int:
    for rel, (_t, d) in PAGES.items():
        assert len(d) <= 160, (rel, len(d))
    changed, skipped, missing = [], [], []
    for rel, (new_title, new_desc) in PAGES.items():
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        src = path.read_text(encoding="utf-8")
        tm, dm = TITLE_RE.search(src), DESC_RE.search(src)
        if not tm or not dm:
            missing.append(rel + " (no title/description tag)")
            continue
        old_title, old_desc = tm.group(1), dm.group(1)
        if html.unescape(old_title) == new_title and html.unescape(old_desc) == new_desc:
            skipped.append(rel)
            continue
        out = src
        for old in sorted(_variants(old_title), key=len, reverse=True):
            out = out.replace(old, html.escape(new_title, quote=True))
        for old in sorted(_variants(old_desc), key=len, reverse=True):
            out = out.replace(old, html.escape(new_desc, quote=True))
        path.write_text(out, encoding="utf-8")
        changed.append(rel)
    print(f"changed {len(changed)}, already current {len(skipped)}, missing {len(missing)}")
    for r in changed:
        print("  +", r)
    for r in missing:
        print("  ! missing:", r)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
