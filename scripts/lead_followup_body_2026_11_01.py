#!/usr/bin/env python3
"""Idempotent body-copy edit for /services/lead-follow-up/ (2026-11-01).

Adds the two Tier-1 phrases from 07_ANALYTICS/keyword_plan_2026-10-31.md to the
page body, not just the tags: "done for you lead generation" (170/mo, KD 2) and
"automated lead follow up" (140/mo, KD 18). Edits the rendered HTML in place, the
same way seo_retarget_2026_10_31.py and oct_audit_fixes.py do, so no old spec
needs re-running (re-running specs would overwrite hand edits). Safe to re-run:
a page already carrying the phrase is skipped.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "services" / "lead-follow-up" / "index.html"

# old -> new. Exact single-substring replacements, each guarded by its own
# idempotency check so re-running never doubles the phrase.
EDITS = [
    (
        "keep chasing until it books or says no.</p>",
        "keep chasing until it books or says no. This is done for you lead generation, from first reply to booked job.</p>",
    ),
    (
        "Automated follow-up over days and weeks so no lead ever quietly dies in an inbox.",
        "Automated lead follow-up over days and weeks so no lead ever quietly dies in an inbox.",
    ),
]


def main() -> int:
    src = PAGE.read_text(encoding="utf-8")
    changed, skipped = [], 0
    for old, new in EDITS:
        if new in src:
            skipped += 1
            continue
        if old not in src:
            print(f"! pattern not found: {old[:60]!r}")
            return 1
        src = src.replace(old, new, 1)
        changed.append(new[:60])
    PAGE.write_text(src, encoding="utf-8")
    print(f"changed {len(changed)}, already current {skipped}")
    for c in changed:
        print("  +", c)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
