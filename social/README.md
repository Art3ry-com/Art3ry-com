# Art3ry Social — the strategy

The four platforms Art3ry runs, why these four, and how the daily loop feeds
them. Owned inside the brand repo (this file), NOT inside `art3ry-os` — the
master OS ships the generic scaffold; the actual Art3ry voice, cadence, and
copy live here.

## The four channels (why these, not all six)

| Platform  | Role                                              | Format strength           |
|-----------|---------------------------------------------------|---------------------------|
| Instagram | The visual proof — behind-the-scenes, quick wins  | Reels, carousels          |
| YouTube   | The authority archive — long-form + Shorts        | Case studies, deep dives  |
| TikTok    | The discovery layer — hooky POVs, contrarian      | Short vertical, hooks     |
| LinkedIn  | The operator lens — Playbook worldview            | Text, carousels           |

**Off:** X (spend without conversion at our stage), Facebook (Meta Ads later,
not organic reach). Both can flip on later — the `art3ry-os/modules/social/`
scaffold ships all six cockpits ready.

## Voice (governs all four platforms)

Pulled straight from art3ry.com — same voice on the socials as on the site.
Consistency compounds; a second voice torches trust.

- **Warm operator**, not agency-slick. Lead phrase: *"Growth, done for you."*
- **Numbers over adjectives.** Canonical proof: **700+ jobs · zero missed
  leads · no staff.** Same figures everywhere, forever.
- **Anti-dashboard.** *"You run your business. I run everything that makes
  it grow."* Never sell "another tool to log into."
- **Show the leak.** Marketing pain is what an owner *feels*; name the leak
  (leads, money, time, follow-up) then plug it.
- **First person, singular.** "I run the system." Not "we." Art3ry is one
  operator, and that's the whole differentiator.
- **One idea per post.** Hook in the first line / first two seconds.

**Never use:** hype ("10X", "revolutionize"), generic marketing bingo,
"what do you think?" bait, hashtag stacks bigger than five.

## Cadence (start conservative — the queue compounds)

| Platform  | Target                                        |
|-----------|-----------------------------------------------|
| Instagram | 3 Reels + 2 carousels + daily Stories / wk    |
| YouTube   | 1 long-form + 2 Shorts / wk                   |
| TikTok    | 3–5 short verticals / wk                      |
| LinkedIn  | 3–4 text posts + 1 carousel / wk              |

Miss a day → **don't backfill**. Consistency beats catch-up.

## The workflow (log → draft → approve → paste)

1. **Log.** Every day, brain-dump one thing into `/capture` (art3ry-os skill):
   *"just audited a barbershop with 40% missed calls — here's the fix."*
   → blog + 4 platform drafts queued.
2. **Approve.** Jesse is last eyes on every draft. Nothing ships unreviewed.
3. **Paste.** LI/IG/YT/TT are all **manual** — no cheap/reliable auto-post
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

- `profiles.md` — bios per platform (paste-ready, char-counted).
- `launch-posts.md` — the first "we're live" post per platform.
- `content-seed.md` — 15 idea starters to prime the queue on day one.
