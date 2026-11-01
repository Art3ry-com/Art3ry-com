#!/usr/bin/env python3
"""Idempotent body-keyword fixes (2026-11-01).

The 2026-10-31 retarget changed titles, but a body-copy audit found 5 target
keywords from keyword_plan_2026-10-31.md that still were not present in their
page's body (a title alone will not rank). This script weaves each phrase
naturally into the body in place, the same way seo_retarget_2026_10_31.py does.
Safe to re-run: a page already carrying the phrase is skipped.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (path, old, new) — exact single-substring replacements. Idempotent.
EDITS = [
    (
        "never-lose-a-job-to-voicemail/index.html",
        "You can&#x27;t answer the phone with your hands in a drain. Art3ry can. Every call, form, and email lands as a clean lead, deduped and pinged to your phone, then the client accepts the quote and the invoice fires automatically and chases it while you sleep.",
        "An answering service for contractors, plumbers, HVAC and electricians: you can&#x27;t answer the phone with your hands in a drain, so Art3ry does. Every call, form, and email lands as a clean lead, deduped and pinged to your phone, then the client accepts the quote and the invoice fires automatically and chases it while you sleep.",
    ),
    (
        "blog/seo-for-contractors/index.html",
        "That is why SEO for a contractor is mostly local SEO.",
        "That is why SEO for contractors and SEO for plumbers are mostly local SEO.",
    ),
    (
        "blog/virtual-receptionist-companies-compared/index.html",
        "Human, hybrid, and AI answering are three different products sold under one name. Choosing well starts with being honest about which of your calls actually need a person.",
        "Human, hybrid, and AI answering are three different products sold under one name. Picking the best AI receptionist for your business starts with being honest about which of your calls actually need a person.",
    ),
    (
        "blog/answering-service-pricing/index.html",
        "Every provider quotes a different unit, which makes comparison almost impossible on purpose. Here is how to translate any quote into what you will actually pay.",
        "Every provider quotes a different unit, which makes comparing answering service pricing and virtual receptionist pricing almost impossible on purpose. Here is how to translate any quote into what you will actually pay.",
    ),
    (
        "blog/ai-appointment-scheduling-software/index.html",
        "A booking link makes the customer do the work. AI scheduling does the work for them, over the phone, in a conversation. That difference matters more for some businesses than others.",
        "An AI scheduling assistant does the work for the customer, over the phone, in a conversation, instead of a booking link that makes them do the work. That difference matters more for some businesses than others.",
    ),
    (
        "blog/ai-appointment-scheduling-software/index.html",
        "AI Appointment Scheduling Software: How It Works | ART3RY",
        "AI Scheduling Assistant: How It Works | ART3RY",
    ),
]


def main() -> int:
    changed, skipped, missing = [], 0, []
    for rel, old, new in EDITS:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        src = path.read_text(encoding="utf-8")
        if new in src:
            skipped += 1
            continue
        if old not in src:
            missing.append(rel + " (old text not found)")
            continue
        src = src.replace(old, new, 1)
        path.write_text(src, encoding="utf-8")
        changed.append(rel)
    print(f"changed {len(changed)}, already current {skipped}, missing {len(missing)}")
    for c in changed:
        print("  +", c)
    for m in missing:
        print("  ! missing:", m)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
