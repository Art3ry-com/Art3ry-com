"""Google-autocomplete keyword pass: business growth / make money / automate.
Same method as the 2026-08-31 run (suggestqueries, a-z expansion, noise filter).
No volume numbers exist in this data; it reflects what people type."""
import json, time, urllib.parse, urllib.request, re, string, collections

SEEDS = [
    "how to grow a small business", "how to grow my business", "how to get more customers",
    "how to get more clients", "how to get more leads", "how to make more money in my business",
    "how to market my small business", "how to scale a small business", "small business growth",
    "why is my business slow", "how to automate my business", "how to automate a small business",
    "ai for small business", "how to use ai in my business", "business automation",
    "how to increase sales small business", "how to advertise my small business",
    "how to get customers without ads",
]
SUFFIX = [""] + [" " + c for c in string.ascii_lowercase]
UA = {"User-Agent": "Mozilla/5.0"}

def suggest(q):
    url = "https://suggestqueries.google.com/complete/search?client=firefox&q=" + urllib.parse.quote(q)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=10) as r:
            return json.load(r)[1]
    except Exception:
        return []

RELEVANT = re.compile(r"business|customer|client|lead|sale|market|revenue|money|profit|automat|ai |grow|scale|advertis|promot|brand|local|google|website|referral", re.I)
NOISE = re.compile(r"\b(minecraft|sims|stardew|gta|roblox|acnh|hay day|bitlife|game|instagram bio|tiktok shop ban|essay|resume|interview|visa|immigration|loan forgiveness|disability|pregnan|divorce|crypto|stock|forex)\b", re.I)

raw = set()
for i, seed in enumerate(SEEDS):
    for suf in SUFFIX:
        for s in suggest(seed + suf):
            raw.add(s.strip().lower())
        time.sleep(0.12)
    print(f"[{i+1}/{len(SEEDS)}] {seed}: total raw {len(raw)}", flush=True)

qualified = sorted(s for s in raw
                   if 4 <= len(s.split()) <= 11 and RELEVANT.search(s) and not NOISE.search(s))

buckets = collections.defaultdict(list)
RULES = [
    ("get-more-customers", re.compile(r"more (customers|clients|leads|sales)|get customers|get clients|find (customers|clients)|attract")),
    ("grow-the-business", re.compile(r"grow|scale|expand")),
    ("automate", re.compile(r"automat|ai ")),
    ("marketing-ads", re.compile(r"market|advertis|promot|social media|facebook|without ads")),
    ("make-more-money", re.compile(r"money|profit|revenue|increase sales|charge")),
    ("slow-business", re.compile(r"slow|struggling|failing|no customers")),
]
for s in qualified:
    for name, rx in RULES:
        if rx.search(s):
            buckets[name].append(s); break
    else:
        buckets["other"].append(s)

out = {"raw": len(raw), "qualified": len(qualified),
       "buckets": {k: v for k, v in sorted(buckets.items(), key=lambda kv: -len(kv[1]))}}
import os, datetime
out_path = os.path.join(os.path.dirname(__file__), f"growth_pass_{datetime.date.today().isoformat()}.json")
with open(out_path, "w") as f:
    json.dump(out, f, indent=1)
print("DONE", out["raw"], out["qualified"], {k: len(v) for k, v in out["buckets"].items()}, flush=True)
