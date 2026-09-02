# Deploying art3ry.com

The site is **live**. Push to `main` and it ships. Everything below is what you
need to know before you do that.

```
you push  →  GitHub Pages rebuilds (~1 min)  →  Cloudflare edge (600s cache)  →  art3ry.com
```

Repo `Art3ry-com/Art3ry-com` · `CNAME` = `art3ry.com` · **74 pages, 64 in the
sitemap** (the ten `/assistant*` pages are parked `noindex`) · no build step, no
npm, no framework. The HTML in this repo is the HTML that ships.

---

## Before you push

**1. Bump the stylesheet version if you touched CSS.**
`/assets/*.css` ships `max-age=14400`. New HTML paired with four-hour-stale CSS
renders as garbage, which has already happened once. Both stylesheets carry a
`?v=` and the generator has `CSS_V` near the top of `scripts/build_pages.py`.
Change the CSS, change the version, in the same commit.

**2. Never regenerate without reading what changed.**
`scripts/build_pages.py` writes real pages and mutates `sitemap.xml`. Run it,
then `git diff`, then decide. It has twice tried to undo deliberate decisions.

**3. The sitemap dates itself from git. Do not hand-edit `<lastmod>`.**
The generator merges rather than replaces, on purpose, and every URL now carries
a `<lastmod>`. The date is **the commit that last changed that page's file**, or
today if the file has pending edits, so a rebuild that produces identical bytes
keeps the old date instead of bumping all 64 and burning crawl budget, and a page
you actually edited moves on its own. A previously published date is never walked
backwards. Because the dates read the working tree, run

```bash
python3 scripts/build_pages.py --sitemap-only
```

**last**, after every page edit, including `wire_playbook.py`.

**4. Run `python3 scripts/wire_playbook.py` after every `build_pages.py` run.**
Marker-delimited blocks the generator does not emit, which a rebuild therefore
strips from any spec'd page: the "Part of the X playbook" backlink on every post
and landing page, the library on `/playbook/`, the banner on `/blog/`, and the
"Keep reading" cards. The wiring script puts them all back, verifies every link
resolves, and is safe to run twice. Cluster membership lives in ONE place,
`scripts/specs_playbook.json`; the "Keep reading" link lists in
`scripts/specs_readnext.json`, which stores **only hrefs**: each card's title and
blurb are read from the destination page at wire time, so retitling a post updates
every card that points at it. Pages the factory does not own keep their
hand-written block and are absent from that spec.

---

## The two stylesheets

| File | Used by | Notes |
|---|---|---|
| `assets/site.css` | the homepage, and only the homepage | hero schematic, scroll reel, trade picker |
| `assets/pages.css` | 65 interior pages | implements the page factory's class contract |

**They are never loaded together.** Both define `.hero`, `.card` and `.section`
and they mean different things. Loading both breaks the page.

Eight hand-built pages (`about`, `services`, `playbook`, `get-started`, `blog`,
and three older posts) still carry their own inline CSS. They share the wordmark
and the type, not the layout.

---

## The page factory

```bash
python3 scripts/build_pages.py scripts/specs_services.json
```

**The spec JSON is the source of truth, not the HTML.** Editing a generated page
without editing its spec means the next build silently reverts your change. That
is exactly how the site's first-person rewrite nearly got undone: the HTML was
fixed and the specs were not.

Spec files: `specs_services.json`, `specs_diagnostic.json`, `specs_playbook.json`,
`specs_hub_1..5.json`, `specs_money_1..3.json`, `specs_pillars.json`,
`specs_fresno.json`: 24 pages in all. The other 50 predate the specs and cannot
be regenerated; edit those by hand and know that the factory will not reproduce
them. `scripts/build_pages.py` takes ONE spec at a time, so a full rebuild is

```bash
for f in scripts/specs_*.json; do python3 scripts/build_pages.py "$f"; done
python3 scripts/wire_playbook.py
python3 scripts/build_pages.py --sitemap-only
```

A blog spec's `title` is the H1 and the schema headline; add `title_tag` when the
SERP line has to be shorter or lead with a different keyword. Without it the two
stay identical.

Guards that will stop a build: Jesse's private cell in any output aborts with a
non-zero exit. Keep it that way.

---

## After you push

```bash
curl -s https://art3ry.com/ | grep -c rig-chips      # 1 = the new homepage is live
curl -sI https://art3ry.com/ | head -3               # 200
```

Pages usually takes under a minute; Cloudflare can hold the old copy for up to
ten. If HTML updated and CSS did not, you forgot step 1.

---

## Domain and DNS

Already configured and working. Do not change these unless something is broken.

- Apex `A` records → `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`
- `CNAME www` → `art3ry-com.github.io`
- `CNAME` file must contain exactly `art3ry.com`. Deleting it drops the custom domain.
- Cloudflare's **managed robots.txt / AI-bot blocking must stay OFF**. `robots.txt`
  deliberately allows GPTBot, ClaudeBot, PerplexityBot and the rest; a managed
  rule overrides it at the edge and silently undoes that.

---

## Do not lose these

- `8fd86baa2e017878e7a2bdc6eb4ffa5a.txt` at the web root — IndexNow key. Filename
  must equal contents.
- Both `google-site-verification` tags in `index.html`. They exist nowhere else;
  deleting either drops a Search Console property.
- The Web3Forms endpoint and key in `get-started/`. It is the only structured lead
  capture on the site, and it **cannot be verified with curl** — Web3Forms 403s
  server calls. Only a real browser submitting the real form proves it works.
- The no-dead-end fallback in `get-started/` (mailto, then copy-to-clipboard, then
  a prompt). It exists because leads were being lost. Do not simplify it.
- `noindex,follow` on the ten parked `/assistant*` pages, and their absence from
  the sitemap. Removing the sitemap entries alone would not de-index them.

---

## Known open

- **Eleven indexable pages carry no JSON-LD at all**: `/blog/`, `/get-started/`,
  `/blog/seo-for-local-business/`, `/blog/ai-phone-intake/`,
  `/blog/automate-invoicing/` and the six `/blog/growth-for-*/` posts. They predate
  the factory, so nothing will add schema to them on a rebuild. Structured data is
  the cheapest remaining on-page win on this site.
