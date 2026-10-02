---
type: framework-foundation
client: none
status: active
updated: 2026-10-02
sources_note: "Canonical HTTP→HTTPS section verified live via curl against http://moldremediationgettysburgpa.org/ on 2026-10-01 — not a raw/ capture, see inline traceability note. www vs. non-www section (2026-10-02) is general reasoning parallel to that case — not independently verified against a live site, see inline traceability note."
sources:
  - "raw/framework/1. SEO Fundamentals - Learn Technical SEO - The Beginner's Guide to Technical SEO.md"
  - "raw/framework/1. SEO Fundamentals - Learn Technical SEO - Google Crawling and Indexing  Google Search Central    Documentation.md"
  - "raw/framework/1. SEO Fundamentals - Learn Technical SEO - Technical optimization.md"
---

# Technical SEO Fundamentals

**Purpose:** Theoretical foundation for understanding how search engines crawl, index, and rank websites. This is conceptual knowledge supporting the tactical [[on-site-seo.md]] and [[external-seo-microsite-tactics.md]] guides.

**Audience:** Anyone building or optimizing a site who wants to understand *why* certain technical practices matter.

---

## How Search Engines Work

### The Three-Phase Process

Search engines (Google, Bing) follow a three-step process to make your content discoverable:

1. **Crawling** — A bot (Googlebot) discovers your site by following links from other pages and your sitemap. It reads the HTML, CSS, and JavaScript to understand page structure and content.

2. **Indexing** — Google processes what it crawled and stores information about your pages in a massive index. During this phase, Google:
   - Parses content to understand topics and entities
   - Identifies text, images, videos, and structured data
   - Evaluates page quality, freshness, and relevance
   - May filter out duplicates or low-quality content

3. **Ranking** — When someone searches, Google retrieves indexed pages matching the query and ranks them based on hundreds of signals (relevance, authority, user experience, etc.).

**Key insight:** If your site isn't crawlable or indexable, it won't rank — no matter how good the content is.

---

## Crawlability: Making Your Site Easy to Discover

### What Googlebot Needs

- **Clear site structure** — Logical hierarchy (homepage → categories → pages) makes crawling efficient
- **Internal links** — Links between your own pages guide the crawler to all important content
- **Sitemap** — An XML file listing all your pages (tells Google what exists)
- **Robots.txt** — A file that tells crawlers which parts of your site to crawl (or block)
- **No crawl traps** — Avoid infinite loops, duplicate parameters, or crawl-blocking redirects

### What Blocks Crawling

- JavaScript-only content (older crawlers struggle with heavy JS)
- Nofollow links (tell crawler "don't follow this link")
- Blocked by robots.txt or meta robots tag
- Very deep nesting (pages buried 10+ levels deep rarely get crawled)
- Server errors (500s, timeouts prevent crawling)

### Tool Quirk: Ahrefs Flags the Homepage as "Orphaned"

Ahrefs Site Audit sometimes lists the **homepage itself** as an orphan page (no
internal links found pointing to it). This is almost always a **false positive**,
not a real crawlability problem:

- Ahrefs' crawler starts crawling *from* the homepage (or the sitemap), so its
  orphan-detection logic doesn't always count the homepage as "discovered via a
  link" the way it does for every other page — it's the starting point, not an
  arrival.
- On nearly every site, the homepage already receives internal links via the
  logo/nav on every other page, so there's rarely an actual link-equity gap.

**How to confirm it's a false positive (vs. a real issue):**
1. View source on any non-homepage page and confirm the logo/nav links to `/`
   with a real `<a href>` tag — not JS-only navigation (JS-only nav *would* be a
   real crawlability issue, see "What Blocks Crawling" above).
2. Check Google Search Console → Links → Internal links. If GSC (an independent
   crawler) shows a healthy internal-link count for the homepage, Ahrefs is
   almost certainly a crawl artifact.
3. Check the homepage isn't excluded from the XML sitemap and doesn't carry a
   canonical pointing elsewhere — those *would* be genuine problems worth fixing.

**Bottom line:** don't spend client budget "fixing" a homepage orphan flag from
Ahrefs without confirming via GSC or page source first — it's one of Ahrefs' most
common noisy false positives.

> *Not sourced from a raw capture — general SEO/tool-behavior reasoning. Flagged
> here for traceability (same convention as the note in
> [[external-seo-microsite-tactics.md]]).*

### Tool Quirk (Real This Time): "Canonical from HTTP to HTTPS"

Ahrefs Site Audit also flags pages where the **HTTP** version's canonical tag
points to the **HTTPS** version. Unlike the orphan-homepage flag above, **this
one is usually a real issue, not noise** — check it rather than dismissing it.

**How to tell real issue vs. harmless:**
- Check the HTTP URL's actual status code directly (don't trust a browser,
  which auto-upgrades to HTTPS): `curl.exe -I http://yourdomain.com/`.
  - **`301`/`302` → HTTPS already:** harmless. Ahrefs is just reporting the
    canonical tag it saw on the final HTTPS page after following the redirect
    — no action needed.
  - **`200 OK` directly on HTTP:** real issue. The site is serving the full
    page over plain HTTP and relying on the canonical tag *alone* to tell
    Google "please index HTTPS instead." `rel=canonical` is a hint, not an
    enforced rule — Google can still crawl/index the insecure duplicate, it
    wastes crawl budget on two versions of every page, and real users can land
    on the insecure version via a stray link.

**Real example (moldremediationgettysburgpa.org, 2026-10-01):**
`curl.exe -I http://moldremediationgettysburgpa.org/` returned `200 OK`
directly — no redirect — while the page's `<link rel="canonical"
href="https://moldremediationgettysburgpa.org/">` was present. Confirmed real
issue: the site sits behind Cloudflare, which was not configured to force
HTTPS at the edge.

**Fix:**
1. If on Cloudflare: **SSL/TLS → Edge Certificates → "Always Use HTTPS"** → On.
   Cloudflare then 301-redirects all HTTP requests at the edge — no origin
   changes needed.
2. Optionally enable **HSTS** afterward (same settings area) once HTTPS is
   confirmed working everywhere. Cloudflare's HSTS panel has sub-options —
   don't just accept the defaults:
   - **Max Age Header:** start at **6 months**, bump to 12 months later once
     stable. Don't jump to the max value on day one.
   - **Apply HSTS Policy to subdomains (`includeSubDomains`):** safe to enable
     only if *every* subdomain (not just `www`) actually supports HTTPS —
     otherwise it can break a legacy subdomain for any visitor who's cached
     the policy, with no quick undo.
   - **Preload:** leave **off** for most client sites. It submits the domain
     to the browser-vendor HSTS preload list, enforced HTTPS-only on first
     visit with no trust-on-first-use gap — but removal takes months to
     propagate through browser release cycles. Only worth it for sites
     handling sensitive data, and only after `includeSubDomains` has run
     stable for a while.
   - **No-Sniff Header:** adds `X-Content-Type-Options: nosniff`, which tells
     the browser to trust the server's declared `Content-Type` instead of
     "MIME-sniffing" (guessing) the real file type. This closes an older XSS
     vector where a mislabeled uploaded file (e.g. an "image") could get
     reinterpreted and executed as script/HTML. **Not a ranking signal, low
     security priority on its own, but zero risk and zero effort to enable**
     — it only restricts how browsers reinterpret content, so it can't break
     a normal page. Matters most on sites that accept user uploads
     (avatars, forum attachments); barely applies to a static local-service
     microsite with no uploads. Leave it **on** regardless — free hardening,
     unrelated to HTTPS enforcement.
3. Re-run the `curl.exe -I http://...` check — expect a `301` with a
   `Location: https://...` header instead of a direct `200`.
4. The canonical tag doesn't need to change — once the redirect exists, it
   becomes a harmless backup signal rather than the only one.

**Important direction check:** this flag's direction (HTTP → HTTPS) is the
*correct* one. The genuinely alarming version is the reverse —
**"Canonical from HTTPS to HTTP"** — a secure page telling Google to prefer
the insecure URL. That direction should be fixed immediately regardless of
redirect status.

**Does this actually hurt rankings?** Small, but non-zero — it's an unforced
risk rather than an active penalty:
- **HTTPS itself is already a weak ranking signal** (see "User Experience
  Signals" below) — the site already serves HTTPS content, so this specific
  issue isn't "losing" that signal. The problem is the HTTP duplicate being
  *also* reachable, not the absence of HTTPS.
- **Duplicate content dilution:** the canonical tag usually gets respected,
  but it's a *request*, not an enforced rule like a 301. If Google ever
  indexes the HTTP duplicate anyway, any authority pointing at it (see
  backlinks below) gets split instead of consolidated.
- **Crawl budget waste:** Googlebot crawls both the HTTP and HTTPS version of
  every URL to confirm the canonical relationship, instead of crawling the
  canonical version once. Negligible on a small microsite; compounds on
  larger sites, indirectly slowing how fast new/updated pages get indexed.
- **Backlink equity leakage (the biggest practical risk):** if any external
  site has ever linked to the `http://` version, that backlink's authority
  depends entirely on Google correctly following the canonical hint. A 301
  redirect *guarantees* consolidation; a canonical tag alone only requests it.
- **CTR/trust (indirect):** anyone landing directly on the HTTP URL (old
  backlink, bookmark, typed URL) sees an insecure "Not Secure" warning in some
  browsers — hurts trust/CTR, which feeds back into ranking via user-behavior
  signals.

**Bottom line:** not an active ranking penalty today (the canonical is doing
its job as a safety net), but several small, free-to-close leaks — which is
why the 301 redirect fix (Step 1 above) is worth doing even though it's not
urgent.

**PowerShell note:** `curl` is aliased to `Invoke-WebRequest` in PowerShell,
which doesn't support `-I` the way real curl does (it will prompt for a
missing `-Uri` instead of erroring clearly). Use `curl.exe` (the real binary,
bundled since Windows 10 1803+) to get actual curl behavior, or use
`Invoke-WebRequest -Uri "http://..." -Method Head -MaximumRedirection 0`.

> *Not sourced from a raw capture — general SEO/tool-behavior reasoning,
> verified live against moldremediationgettysburgpa.org. Flagged here for
> traceability (same convention as the note above).*

### www vs. non-www: Same Canonicalization Problem, Different Pair

**Is having the `www` version "up and running" important?** Not in the sense of
running two live sites — it's the exact same duplicate-content/canonicalization
issue as HTTP vs. HTTPS above, just with `www.yoursite.com` vs. `yoursite.com`
instead. Google doesn't prefer one over the other; it just needs **one** to be
canonical and the other to **redirect** into it, not sit unconfigured or 404.

**How to tell real issue vs. harmless** (same pattern as the HTTP/HTTPS check):
- Check both hostnames' actual status codes directly:
  `curl.exe -I http://www.yourdomain.com/` and `curl.exe -I http://yourdomain.com/`
  (repeat with `https://` once HTTPS is confirmed forced — see above).
  - **One 301/302-redirects to the other:** harmless — canonicalization is
    already enforced at the server/edge level. No action needed.
  - **Both resolve with `200 OK` independently (no redirect either direction):**
    real issue. Two live, crawlable copies of every page exist under different
    hostnames, each eligible to be indexed and linked to separately.
  - **The non-canonical version doesn't resolve at all (DNS error, timeout, or
    a generic "can't connect" instead of a redirect):** also a real issue —
    not a ranking problem, but a broken-link/trust problem for anyone who
    types `www.` out of habit or follows an old `www` backlink.

**Fix:**
1. Pick a canonical version — non-www is the common default for new
   microsites, but either is fine as long as it's consistent everywhere
   (GBP, citations, internal links, sitemap).
2. Configure a 301 redirect from the non-canonical hostname to the canonical
   one. On Cloudflare: **Rules → Redirect Rules** (or a page rule) matching
   the non-canonical hostname, forwarding to the canonical one with the path
   preserved. This is a separate setting from the "Always Use HTTPS" toggle
   used for the HTTP→HTTPS fix above — both redirects need to exist
   independently (http→https *and* www→non-www, or whichever pairing applies).
3. Make sure DNS has a record for **both** hostnames (an `A`/`CNAME` for
   `www`) even though one just redirects — an unconfigured `www` subdomain
   can fail to resolve at all instead of redirecting.
4. Set the canonical tag on every page to the canonical hostname version.
5. Re-run the `curl.exe -I` check on the non-canonical hostname — expect a
   `301`/`308` with a `Location:` header pointing at the canonical version.
6. In Google Search Console, verify **both** hostname properties (or the
   domain-level property, which covers both) so GSC reporting isn't split
   across two "sites" — this is already called out as a launch-checklist item
   in [[microsite-launch-checklist.md]].

**Does this actually hurt rankings?** Same shape of risk as the HTTP/HTTPS
case — not an active penalty, but free-to-close leaks:
- **Duplicate content dilution** if both hostnames get crawled/indexed
  independently instead of consolidating to one.
- **Backlink equity leakage** — any external link built to the "wrong"
  hostname (easy to happen across citations, guest posts, social profiles)
  only consolidates correctly if a 301 exists; a canonical tag alone just
  requests it.
- **Broken-link/trust risk** if the non-canonical hostname doesn't resolve at
  all, rather than redirecting.

**Bottom line:** "is www up and running important" → reframe as "is www→non-www
(or the reverse) **redirecting correctly** important" — yes, for the same
backlink-consolidation and duplicate-content reasons as HTTPS, but it's a
one-time setup task, not something to actively monitor once confirmed working.

> *Not sourced from a raw capture — general SEO/canonicalization reasoning,
> directly parallel to the verified HTTP→HTTPS case above. Flagged here for
> traceability (same convention as the notes above).*

---

## Indexability: Getting Your Pages Into Google's Database

### What Google Needs to Index Your Page

- **Unique, sufficient content** — At least 100–150 words of original content (thin pages may not be indexed)
- **Indexable HTML** — Page must be HTML-based (JSON, PDF, images alone won't index in the traditional way)
- **No indexing blocks** — No `noindex` tag, no `robots.txt` block, no `Disallow: /` in robots.txt
- **Crawlable** — Page must be discoverable (see Crawlability section above)

### Indexing Issues

- **Duplicate content** — If Google finds multiple versions of the same content, only one gets indexed (canonical tags help signal which one)
- **Thin content** — Very short pages (under 100 words) may not index
- **Soft 404s** — Pages that return 200 status but contain error messages confuse indexing
- **Noindex by mistake** — A stray `<meta name="robots" content="noindex">` tag blocks indexing

**How to verify indexing:** Search `site:yourdomain.com` in Google to see indexed pages.

---

## Ranking Signals: Why Pages Rank

Once indexed, Google ranks pages based on signals including:

### Relevance Signals
- **Keyword match** — Does the query appear in the title, H1, and body?
- **Topic authority** — Does the page cover the topic deeply?
- **Entity recognition** — Does Google understand the people, places, things mentioned?
- **User intent match** — Is this page the type of result users want (local, commercial, informational)?

### Authority Signals
- **Backlinks** — Links from other sites act as votes of confidence
- **Domain age and history** — Older, stable domains typically rank better than new ones
- **Page freshness** — Recently updated pages may rank higher for current topics

### User Experience Signals
- **Page speed** — Faster pages rank better (mobile and desktop)
- **Mobile-friendliness** — Must render well on phones
- **Core Web Vitals** — Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), First Input Delay (FID)
- **HTTPS/SSL** — Secure sites rank slightly higher

### Content Quality Signals
- **E-E-A-T** — Expertise, Experience, Authoritativeness, Trustworthiness (especially for YMYL topics like health, finance, legal)
- **Originality** — Unique, well-researched content ranks better than paraphrased content
- **Readability** — Clear structure, proper headings, short paragraphs help

---

## Core Technical Best Practices

### Site Structure
- Organize pages into logical categories
- Use clear, descriptive URLs (e.g., `/services/emergency-plumbing` not `/p?id=123`)
- Limit pages to 3 clicks from homepage

### Crawlability & Indexing
- Create and submit an XML sitemap
- Use `robots.txt` to allow crawling of key areas
- Avoid crawl traps (redirects loops, infinite parameter variations)
- Implement canonical tags for duplicate content

### Performance
- Optimize images (compress, lazy-load)
- Minimize CSS/JavaScript
- Use a CDN to serve content faster
- Test with Google PageSpeed Insights and GTmetrix

### Mobile & UX
- Design mobile-first (responsive design)
- Test on actual mobile devices
- Ensure clickable elements are 48x48px minimum
- Avoid intrusive interstitials (pop-ups)

### Security & Trust
- Use HTTPS (SSL certificate)
- Fix mixed-content warnings (HTTP resources on HTTPS page)
- Implement structured data (schema.org markup)
- Display trust signals (contact info, privacy policy, about page)

---

## Structured Data & Schema Markup

**Structured data** uses schema.org markup to tell Google exactly what type of content is on your page. Examples:

- **`Organization`** — Business name, logo, contact info
- **`LocalBusiness`** — Address, phone, hours, reviews
- **`Product`** — Name, price, description, reviews
- **`FAQPage`** — Q&A format that appears in SERP snippets
- **`Article`** — Author, publish date, headline

Structured data doesn't directly rank you higher, but it:
- Helps Google understand your content
- Enables rich snippets (star ratings, images) in search results
- Supports AI Overviews and Knowledge Panels

---

## Relationship to Tactical SEO

This foundation explains **why** the tactical pages matter:

- [[on-site-seo.md]] builds on crawlability + indexing + ranking signals to optimize page content
- [[external-seo-microsite-tactics.md]] focuses on authority signals (backlinks, citations)
- [[getting-cited-by-ai.md]] combines content quality + entity signals + social proof to trigger AI citations

Understanding these fundamentals helps you make better decisions about *which* tactics to prioritize.

---

## Next Steps

- For **tactical on-page optimization,** see [[on-site-seo.md]]
- For **tactical off-page optimization,** see [[external-seo-microsite-tactics.md]]
- For **keyword research fundamentals,** see [[keyword-research.md]]
