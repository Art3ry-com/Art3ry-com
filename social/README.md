# Art3ry Social — the strategy

Two brands, one funnel. Owned inside the brand repo (this file), NOT inside
`art3ry-os` — the master OS ships the generic scaffold; the actual Art3ry
voice, cadence, and copy live here.

## The two-brand structure

**Jesse (personal brand) = the reach engine.** Personal-brand accounts
out-reach company accounts massively on IG / YouTube / TikTok — the
algorithms reward faces and individuals. Same pattern as Hormozi,
Codie Sanchez, Justin Welsh, Gary Vee.

**@art3ry_usa (company) = the funnel.** Company voice, helpful guides,
funnel to art3ry.com. Modest organic reach; the real value is brand
protection (handle claimed) and the target for Meta Ads later.

**Bridge:** every Jesse post ends with *"the system I built is Art3ry
— link"*. Audience follows the person, transacts with the business.

## The channel map

| Handle                              | Who       | Content                                              |
|-------------------------------------|-----------|------------------------------------------------------|
| `@jesse_moraga` (Instagram)         | Personal  | Operator's face — marketing, systems, BTS            |
| `@JesseMoraga` (YouTube)            | Personal  | Long-form + Shorts. Playbook breakdowns, case studies |
| Jesse Moraga (LinkedIn)             | Personal  | Operator content, Playbook worldview                 |
| `@art3ry_usa` (Instagram)           | Company   | Helpful guides, quick tips, funnel to site           |
| `@art3ry_usa` (TikTok)              | Company   | Company voice, short vertical                        |

**Untouched (stay in their lanes):**
- `Jesse Moraga Guitar` (YouTube — 8 subs, music, separate account)
- Music IG + Music TikTok
- `@centralvalleyprocessservers` — CVPS, the actual proof case study.
  Reference in content ("the company I built the system to run"), don't
  rebrand.

**Off for now:** X, Facebook. Both can flip on later — the
`art3ry-os/modules/social/` scaffold ships all six cockpits ready.

## Voice (governs both brands)

Pulled straight from art3ry.com — same voice on the socials as on the site.
Consistency compounds; a second voice torches trust.

- **Warm operator**, not agency-slick. Lead phrase: *"Growth, done for you."*
- **Numbers over adjectives.** Canonical proof: **Central Valley Process
  Servers — 700+ jobs · zero missed leads · no staff.** Same figures
  everywhere, forever.
- **Anti-dashboard.** *"You run your business. I run everything that makes
  it grow."* Never sell "another tool to log into."
- **Show the leak.** Marketing pain is what an owner *feels*; name the leak
  (leads, money, time, follow-up) then plug it.
- **First person, singular** on Jesse's accounts. "I built the system." Not
  "we." Art3ry is one operator, and that's the whole differentiator.
- **One idea per post.** Hook in the first line / first two seconds.

**Never use:** hype ("10X", "revolutionize"), generic marketing bingo,
"what do you think?" bait, hashtag stacks bigger than five.

## Cadence (start conservative — the queue compounds)

**Priority order if bandwidth is tight:**
1. **`@jesse_moraga` IG** — daily to 3x/wk. Highest ROI.
2. **`@JesseMoraga` YouTube** — 1 long-form/mo to start. Doubles as Shorts source.
3. **Jesse LinkedIn** — auto-crosspost the IG carousels. Near-zero extra work.
4. **`@art3ry_usa` IG + TikTok** — 1–2x/wk. Don't stress volume.

**Miss a day → don't backfill.** Consistency beats catch-up.

## The workflow (log → draft → approve → paste)

1. **Log.** Every day, brain-dump one thing into `/capture` (art3ry-os skill):
   *"just audited a barbershop with 40% missed calls — here's the fix."*
   → blog + platform drafts queued.
2. **Approve.** Jesse is last eyes on every draft. Nothing ships unreviewed.
3. **Paste.** IG/YT/TT/LI are all **manual** — no cheap/reliable auto-post
   API for any of them (this is the intended default; see
   `art3ry-os/modules/social/ONBOARDING.md`). Paste at each platform's
   timing.md window.
4. **Log wins + corrections** — same turn — into that platform's cockpit
   `memory.md` inside `art3ry-os/modules/social/<platform>/`. No repeat
   mistakes.

## What to log every day (the raw material)

At least one of these, every active day:

- **A leak** you saw in a business (yours, a client's, a prospect's) + the fix.
- **A play** from the Playbook running in the real world today.
- **A win** — a number, a moment, a customer's reaction.
- **A framework** — how to *look at* a marketing problem, not "5 tips."

The edge is the operator lens: not *"here's what worked for us"* but
*"here's how to see what's leaking so you'd never miss it again."*

## Files in this folder

- `profiles.md` — bios + descriptions per account (char-counted, paste-ready).
- `launch-posts.md` — the first "we're live" post per account.
- `content-seed.md` — 15 idea starters to prime the queue on day one.
