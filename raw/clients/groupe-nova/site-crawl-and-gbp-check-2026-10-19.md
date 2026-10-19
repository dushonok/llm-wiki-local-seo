# Raw capture: groupenova.ca site crawl + GBP/NAP cross-check

Captured: 2026-10-19
Method: live fetch of groupenova.ca (WordPress + Elementor) homepage, service pages,
portfolio page, about page, robots.txt, wp-sitemap.xml and sub-sitemaps, raw HTTP
response headers, and raw HTML `<head>`/body for title/meta/canonical/hreflang/
schema inspection. Supplementary web search for Google Business Profile data via a
third-party places-data aggregator (exa.ai, which mirrors Google Maps/Places listing
data) and cross-reference of the website's listed address against Yelp/commercial
real-estate listings. No login-gated tools (Google Business Profile dashboard,
Google Search Console, BrightLocal/Whitespark citation audit, Ahrefs/SEMrush) were
available — this capture is limited to what's publicly fetchable/searchable.

## Business identity (from homepage + about page)

- Business: **Groupe Nova** — general contractor, residential renovation
  (entrepreneur général, rénovation résidentielle)
- Services: kitchen renovation, bathroom renovation, basement renovation, interior
  design services (`/services/renovation-de-cuisine/`,
  `/services/renovation-de-salle-de-bain/`, `/services/renovation-de-sous-sol/`,
  `/services/services-de-design/`)
- Positioning: family-run business ("Groupe Nova, c'est d'abord une histoire de
  famille" — started by a tradesman, now run by his son/family), 10+ years
  experience, dedicated project manager + on-site foreman per project, written
  detailed quotes ("soumission détaillée et écrite, sans surprise")
- Licensing: RBQ (Régie du bâtiment du Québec) license **5881-0540-01**, insured.
  Professional association logos displayed with correct alt text: CCQ (Commission
  de la construction du Québec), APCHQ, RBQ.
- Reviews: Trustindex-embedded Google reviews widget shows **5.0/5**, 6 reviews
  visible (Pierre Junior Kabeya, Alexandre Periard-Lorrain, haoeuro, Imtiaz Kassim,
  Carlos Andres Ramirez, paula ceballos)
- Site: WordPress + Elementor, bilingual FR (default) / EN via a language switcher
  (`/en/...` URL prefix), French is the default/primary language (`<html lang="fr-FR">`)

## NAP as published on the website

- Phone: **514-701-9898** (tel:+15147019898)
- Email: Info@GroupeNova.ca
- Address: **4388 Rue Saint-Denis #200, Montreal, QC H2J 2L1**
- Service areas (footer, both homepage and `/services/`): "Zones desservies:
  Montréal, Montréal-Est, West Island, Rive-Nord, Rive-Sud et Lanaudière"

## Google Business Profile — NAP cross-check (⚠️ mismatch found)

Web search for "Groupe Nova rénovation Montréal Google Business Profile reviews
4388 Rue Saint-Denis" surfaced a third-party places-data aggregator (exa.ai) with a
listing that mirrors Google Maps/Places data for this business — confirmed to be
the *same* GBP connected to the website's Trustindex widget because **all 6 reviews
and reviewer names match exactly** between the site's widget and the aggregator's
listing (same text, same order, same star ratings).

That GBP-derived listing shows:

| Field | Website (groupenova.ca) | GBP (via aggregator) | Match? |
|---|---|---|---|
| Name | Groupe Nova | "GROUPE NOVA - Entrepreneur général - Rénovation résidentielle - Construction" | Partial — GBP display name is keyword-stuffed (service terms appended after a dash), which conflicts with Google's GBP guidelines on business naming |
| Address | 4388 Rue Saint-Denis #200, Montreal, QC H2J 2L1 | **7657 Rue Montbrun, Saint-Léonard, QC H1S 2K3** | ✕ Mismatch |
| Phone | 514-701-9898 | **+1 438-866-6682** | ✕ Mismatch |
| Rating/reviews | 5.0/5, 6 reviews (Trustindex) | 5.0/5, 6 reviews | ✓ Same reviews — confirms same connected profile |
| Category | (not stated on site) | General Contractor | — |

Further check: the website's listed address, **4388 Rue Saint-Denis #200,
Montreal, QC H2J 2L1**, independently cross-referenced via Yelp and a commercial
office-leasing listing, is **"Montréal Cowork"** — a third-party shared/coworking
office space in the Plateau-Mont-Royal neighborhood (office-hub.com listing:
"Montréal Cowork, located at 4388 R Saint-Denis... coworking space with seven
listings... starting at CA$0... up to ten people"). This is not a Groupe Nova
office.

This is a two-part finding:
1. **NAP inconsistency**: the address and phone number on the website do not
   match the address and phone number on the connected Google Business Profile.
2. **Address legitimacy risk**: the website's published address is a third-party
   shared coworking space, not a Groupe Nova-operated location. Google's Business
   Profile guidelines prohibit using a virtual office / co-working address a
   business doesn't exclusively, physically occupy as its public GBP location —
   if this address were ever submitted to or matched against the GBP, it would
   put the listing at risk of suspension.

**Caveat**: this is derived from a third-party aggregator's mirror of Google
Places data, not a direct login to the GBP dashboard, which wasn't available to
this capture. The client/user should confirm directly in the GBP dashboard (Google
Business Profile Manager) before executing any address/phone change. Flagged as
the top open item below.

## Site structure (from wp-sitemap.xml and sub-sitemaps)

French (default, no prefix):
- `/` (canonical homepage, lastmod 2026-10-08)
- `/accueil/` (lastmod 2026-09-30) — **separate URL, same "Accueil" content as `/`**
- `/services/` (lastmod 2026-10-07)
- `/services/renovation-de-cuisine/` (lastmod 2026-10-02)
- `/services/renovation-de-salle-de-bain/` (lastmod 2026-10-02)
- `/services/renovation-de-sous-sol/` (lastmod 2026-10-02)
- `/services/services-de-design/` (lastmod 2026-10-02)
- `/realisations/` (portfolio, lastmod 2026-10-07)
- `/a-propos/` (lastmod 2026-10-08)
- `/cookie-policy-ca/` (lastmod 2026-03-05)

English (`/en/` prefix):
- `/en/` (canonical homepage)
- `/en/home/` — **separate URL, same "Home" content as `/en/`**
- `/en/services-2/`, `/en/services-2/kitchen-renovation/`,
  `/en/services-2/bathroom-renovation/`, `/en/services-2/basement-renovation/`,
  `/en/services-2/interior-design-services/`
- `/en/portfolio/`
- `/en/about-us/`

Also present in `wp-sitemap-users-1.xml` (WordPress author-archive sitemap, auto-
generated): `/author/farhan/`, `/author/hector-fabio-009hotmail-ca/` — thin
user-enumeration pages with no content value, indexable by default.

## Canonicalization / redirect checks

- `http://groupenova.ca/` → 301 → `https://groupenova.ca/` ✓
- `https://www.groupenova.ca/` → 301 → `https://groupenova.ca/` ✓
- `https://groupenova.ca/xmlrpc.php` → 403 (already blocked) ✓
- robots.txt: clean, `Disallow: /wp-admin/` only, correctly references
  `Sitemap: https://groupenova.ca/wp-sitemap.xsl`
- Response headers include `X-Content-Type-Options: nosniff`,
  `X-XSS-Protection: 1; mode=block`; **no `Strict-Transport-Security` (HSTS)
  header present**.

## On-page SEO findings (title/meta/canonical/hreflang/schema — fetched via raw HTML)

Checked 11 URLs: `/`, `/accueil/`, `/en/`, `/en/home/`, `/services/`,
`/services/renovation-de-cuisine/`, `/services/renovation-de-salle-de-bain/`,
`/services/renovation-de-sous-sol/`, `/services/services-de-design/`,
`/realisations/`, `/a-propos/`.

### Titles (every single page checked)

| URL | `<title>` |
|---|---|
| `/` | **"Groupe Nova"** |
| `/accueil/` | "ACCUEIL – Groupe Nova" |
| `/en/` | **"Groupe Nova"** (not translated) |
| `/en/home/` | "Home – Groupe Nova" |
| `/services/` | "SERVICES – Groupe Nova" |
| `/services/renovation-de-cuisine/` | "RÉNOVATION DE CUISINE – Groupe Nova" |
| `/services/renovation-de-salle-de-bain/` | "RÉNOVATION DE SALLE DE BAIN – Groupe Nova" |
| `/services/renovation-de-sous-sol/` | "RÉNOVATION DE SOUS-SOL – Groupe Nova" |
| `/services/services-de-design/` | "SERVICES DE DESIGN – Groupe Nova" |
| `/realisations/` | "RÉALISATIONS – Groupe Nova" |
| `/a-propos/` | "À PROPOS – Groupe Nova" |

No title on any page includes a location term (Montréal, Laval, Rive-Nord,
Rive-Sud, Montérégie, Lanaudière). The homepage — the site's highest-authority
URL — has no service keyword either, just the brand name. All other titles are
generic WordPress-default page-name-only titles (ALL CAPS page title + brand),
with no compelling/differentiated copy and no location modifier despite operating
across a large, competitive, multi-region market.

### Meta descriptions

**Zero meta descriptions found on any of the 11 pages checked.** Google will
auto-generate SERP snippets for every page, typically pulling boilerplate or
review-widget text rather than a controlled, keyword-relevant summary.

### Canonical tags

Each URL has a self-referencing `<link rel="canonical">` — correct in isolation,
but this creates the duplicate-homepage problem below rather than fixing it.

### Duplicate homepage (confirmed)

The WordPress "static front page" is set to a Page whose own permalink
(`/accueil/` in French, `/en/home/` in English) remains independently live,
indexed in the sitemap, and self-canonicalized — instead of either not existing
as a separate URL or 301-redirecting/canonicalizing to the root. Result: **four**
near-duplicate "homepage" URLs compete for the same intent:
- `/` (title "Groupe Nova")
- `/accueil/` (title "ACCUEIL – Groupe Nova")
- `/en/` (title "Groupe Nova")
- `/en/home/` (title "Home – Groupe Nova")

Confirmed via the site's own `wp-sitemap-posts-page-1.xml` (lists `/accueil/` and
`/` as two separate `<url>` entries) and `en/wp-sitemap-posts-page-1.xml` (lists
`/en/home/` and `/en/` as two separate entries). H1 text and body content on
`/accueil/` matches the homepage.

### Hreflang

FR/EN alternate tags are correctly implemented and reciprocal on all content
pages checked (services, portfolio, about) — e.g.
`/services/renovation-de-cuisine/` ⇄ `/en/services-2/kitchen-renovation/`. **The
homepage variants do not show hreflang pairing in the same way** — worth fixing
as part of the duplicate-homepage cleanup so the correct canonical FR/EN pair (`/`
⇄ `/en/`) carries the hreflang annotation instead of the duplicate pages.

### Structured data (JSON-LD)

**Zero `application/ld+json` blocks found on any page checked**, including the
homepage. No `LocalBusiness`/`HomeAndConstructionBusiness`/`GeneralContractor`
schema, no `Organization` schema, no `Service` schema for the four listed
services, no `AggregateRating`/`Review` schema (despite the live 5.0/5 Google
reviews widget), no `BreadcrumbList`.

### Open Graph / social meta

No `og:title`, `og:description`, `og:image`, or Twitter Card tags found on the
homepage.

## Image / content signal findings

- Homepage "Nos dernières réalisations" section shows 6 recent-project photos,
  each with a visible text caption naming a specific town: *"Rénovation de
  cuisine à Laval," "Rénovation de salle de bain à Montréal"* (×2), *"Rénovation
  de cuisine à Brossard," "Rénovation de salle de bain à Ile des Soeurs,"
  "Rénovation de salle de bain à Blainville."* **None of these towns (Laval,
  Brossard, Île-des-Sœurs, Blainville) appear anywhere else on the site** — not
  in the footer's "Zones desservies" list, not in any title/meta, not in any
  schema. Every one of the 6 corresponding `<img>` tags has `alt=""` (empty).
- `/realisations/` (the main portfolio/proof page) has 56 images in
  before/after comparison widgets, each paired with a location-named `<h2>`
  caption (e.g. "Rénovation de salle de bain à ..."). **All 56 image `alt`
  attributes are meaningless auto-generated filenames** — e.g. `alt="image00001"`,
  `alt="20230509_201132000_iOS"`, `alt="20240225_162026916_iOS (1)"` — not a
  single one carries the service+location text that's sitting right next to it
  in the visible H2 caption.
- Only the 3 professional-association logo images (CCQ, APCHQ, RBQ) have
  descriptive alt text.
- Hero image uses `.webp` format with `<link rel="preload">` +
  `fetchpriority="high"` — correctly optimized for LCP. Most portfolio/gallery
  images are unresized `.jpg`/`.jpeg` camera originals (some up to 2560×2048px)
  served through a lazy-load placeholder pattern (`data-nsrc` + inline SVG
  placeholder `src`) — acceptable for below-the-fold images but adds page
  weight versus serving resized/WebP versions.

## Service-area consistency check

Website footer states: *"Zones desservies: Montréal, Montréal-Est, West Island,
Rive-Nord, Rive-Sud et Lanaudière."*

Per the user's brief for this engagement, the actual target service areas are:
*"Montreal, Laval, the North Shore, the South Shore, Montérégie, and
Lanaudière."*

These don't name-match exactly: the site uses the generic regional labels
"Rive-Nord"/"Rive-Sud" where the brief names specific sub-regions "Laval" and
"Montérégie." Laval is commonly understood as part of the Rive-Nord region and
Montérégie overlaps with "Rive-Sud" colloquially, but they are also distinct,
independently-searched local terms in Quebec local search (e.g. "rénovation
cuisine Laval" and "rénovation salle de bain Montérégie" are both real, separate
search queries) that the generic regional labels don't capture. Meanwhile, real
project proof already exists in Laval and Brossard (Montérégie) per the
homepage gallery captions above — these specific, provable town names aren't
being used anywhere in copy, titles, meta, or schema.

## Not captured (requires login/paid tools — flag for client/user to provide)

- Google Business Profile dashboard (exact listed address/phone, primary +
  secondary categories, service-area settings, verification status, Q&A, Posts
  history, photo count) — the NAP mismatch above is inferred from third-party
  aggregator data mirroring Google Places, not a direct dashboard login
- Google Search Console (indexing status of `/accueil/` vs `/` and `/en/home/`
  vs `/en/`, impressions/clicks, any manual actions)
- Full citation/directory audit (BrightLocal/Whitespark-style sweep across
  PagesJaunes, Yelp, BBB, Houzz, HomeStars, directories, etc.) beyond the single
  coworking-address cross-reference found above
- PageSpeed Insights / Core Web Vitals field data (only static page-weight/
  format signals were checked, not real Lighthouse/CrUX scores)
- Ahrefs/SEMrush backlink profile or rank tracking
