# Deploying art3ry.com — the easy way (no WordPress)

The Art3ry site is a static multi-page site in this repo (home, about,
get-started, blog index + 9 posts, plus `404.html`, `sitemap.xml`, `robots.txt`).
You do **not** need WordPress or any paid plan. Pick one of the two options below.

> ⚠️ **Blocker until then:** art3ry.com is mid-transfer. You can't set its DNS
> until the transfer completes and you control the domain at the new registrar.
> Once it's in your hands, do the steps below (or ping Claude to walk through it).
>
> *Status check 2026-06-09: GitHub Pages is not yet enabled on this repo
> (`art3ry-com.github.io` returns 404) and art3ry.com does not yet serve this
> site — both steps below are still pending.*

---

## Option 1 — GitHub Pages (recommended · free · the page is already here)

**Step 1 — Turn on Pages**
1. Go to this repo → **Settings → Pages**
2. **Source:** *Deploy from a branch*
3. **Branch:** `main`  ·  **Folder:** `/ (root)` → **Save**
4. The **Custom domain** box auto-fills `art3ry.com` (it reads the `CNAME` file
   already committed here). Leave it.

**Step 2 — Point the domain (at wherever art3ry.com's DNS lives)**
Add these four apex `A` records:

```
A   @   185.199.108.153
A   @   185.199.109.153
A   @   185.199.110.153
A   @   185.199.111.153
```

(Optional IPv6 — add if your DNS host supports AAAA:)

```
AAAA  @  2606:50c0:8000::153
AAAA  @  2606:50c0:8001::153
AAAA  @  2606:50c0:8002::153
AAAA  @  2606:50c0:8003::153
```

And one record for the www version:

```
CNAME   www   art3ry-com.github.io
```

**Step 3 — Lock in HTTPS**
Back in **Settings → Pages**, wait a few minutes, then tick **Enforce HTTPS**.
Done — art3ry.com is live and secure.

---

## Option 2 — Just forward the domain (simplest stopgap)

At your registrar, set **domain forwarding**:

```
art3ry.com  →  https://jessemoraga.com/system
```

No hosting, no Pages. It lands on the Art3ry page already live on jessemoraga.com.
Switch to Option 1 whenever you want art3ry.com to be its own standalone site.

---

## Notes
- Site content lives in `index.html` + the per-page `*/index.html` files
  (each page is a self-contained HTML file — edit those to change the site).
- After Pages is live, submit `https://art3ry.com/sitemap.xml` in Google
  Search Console.
- `CNAME` must contain exactly `art3ry.com` — it tells GitHub Pages the custom
  domain. Don't delete it.
- DNS changes can take a few minutes to a few hours to take effect.
- GitHub Pages docs: https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site
