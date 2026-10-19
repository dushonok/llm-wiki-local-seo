---
type: recommendation
client: groupe-nova
status: active
updated: 2026-10-19
sources:
  - raw/clients/groupe-nova/site-crawl-and-gbp-check-2026-10-19.md
  - raw/clients/groupe-nova/nap-verification-followup-2026-10-19.md
  - raw/clients/groupe-nova/gbp-live-screenshot-note-2026-10-19.md
  - raw/clients/groupe-nova/url-structure-and-content-depth-check-2026-10-19.md
  - raw/clients/groupe-nova/interior-design-page-bug-confirmed-2026-10-19.md
  - raw/clients/groupe-nova/montbrun-citation-verification-2026-10-19.md
---

# Recommendations — groupenova.ca

Scope of this pass, per the engagement brief: (1) technical SEO audit +
correction of priority issues, (2) Google Business Profile optimization, (3)
NAP consistency across website / GBP / directories. Findings below are grouped
by priority, not by category.

## P0 — NAP: one stale duplicate to resolve, plus standard GBP optimization

> **Correction (2026-10-19, confirmed directly by the client, then verified
> by screenshot):** the client confirmed 4388 Rue Saint-Denis #200, Montreal
> is the real GBP address, and then provided a direct screenshot of the live
> Google Maps listing as evidence
> ([gbp-live-screenshot-note-2026-10-19.md](../../../raw/clients/groupe-nova/gbp-live-screenshot-note-2026-10-19.md)).
> This is the strongest evidence tier in this entire engagement — an actual
> visual of the live profile, not a third-party aggregator or a search-engine
> snippet. It confirms address, phone, website, category, and hours all
> match the site exactly, and surfaces one correction of its own: the live
> listing shows **11 reviews**, not the 6 the earlier (stale, 2022–2023-dated)
> aggregator snapshot showed. The earlier recommendation to remove this
> address / convert to a hidden-address service-area business remains
> **retracted**. See
> [nap-verification-followup-2026-10-19.md](../../../raw/clients/groupe-nova/nap-verification-followup-2026-10-19.md)
> for the full prior investigation trail — kept for the record, not because
> its address-identity conclusion stands.

1. **NAP for Rue Saint-Denis is now confirmed consistent between the website
   and GBP — screenshot-verified, no action needed on this address.** Name,
   address, phone, website, and category all match exactly between
   groupenova.ca and the live Google Maps listing. The earlier framing (this
   address is "wrong," "a coworking space, not a real office," or a guideline
   risk requiring removal) is fully retracted. The address evidently already
   satisfies whatever shared/co-working location requirements Google applies
   — it's live, verified-looking (set hours, 11 reviews, correct category),
   and functioning normally, so the "confirm shared-office requirements"
   caveat from the prior draft is dropped; there's nothing here actually
   indicating a problem.

2. **Old address/phone (7657 Rue Montbrun, 438-866-6682) is still published
   in third-party sources — treat it as stale citation data to clean up, not
   as a confirmed second Google listing.** Correction (2026-10-19, after the
   client pointed out Google Maps shows only the Montreal GBP): the Montbrun
   address was never seen on Google Maps by this audit. It came from (a)
   exa.ai's places-data mirror, which was assumed to reflect a Google listing
   because its 6 reviews matched the website's Trustindex widget, and (b)
   ProfileCanada (which lists `www.groupenova.ca` with that address/phone) plus
   two other directories (studio-lb.fr, aubaine.ca), none with a visible
   verification date. The "duplicate GBP" framing was an inference stacked on
   an unverified premise. The simpler explanation, given identical reviews:
   it is the same GBP as the live Montreal one, captured by exa.ai at an
   earlier date when it carried the older address/phone (the live listing now
   shows 11 reviews, a superset). If so there is no duplicate — only stale
   copies of the old NAP in third-party directories and aggregators. Action:
   (a) have the client open the live listing's Reviews tab and confirm the
   same reviewers (Pierre Junior Kabeya, Alexandre Periard-Lorrain, etc.)
   appear there; (b) search Google Maps for "Groupe Nova" and the old phone
   number once to rule out a separate listing; (c) fold cleanup of the old
   address/phone on ProfileCanada, studio-lb.fr, aubaine.ca and other
   directories into the citation audit (#5). Only escalate to a Google
   duplicate/merge request if (b) actually surfaces a second listing.

   **Re-verified 2026-10-19 (direct page fetches, see
   [[raw/clients/groupe-nova/montbrun-citation-verification-2026-10-19.md]]):**
   the old details are confirmed live today on two unclaimed directory pages —
   [ProfileCanada](https://www.profilecanada.com/companydetail.cfm?company=826158_Groupe_Nova_-_Renovation_Construction_Outremont_QC)
   (7657 Rue Montbrun, 438-866-6682, links to groupenova.ca) and
   [aubaine.ca](https://aubaine.ca/repertoires/services-metiers/entrepreneurs-construction/groupe-nova-entrepreneur-general-renovation-residentielle-construction-saint-leonard)
   (same address/phone, auto-generated page, 56% complete). Snippet-level
   only (not independently loaded): the
   [exa.ai mirror](https://exa.ai/library/place/2dxh15h1z8c),
   [studio-lb.fr](https://studio-lb.fr/montreal) (phone only), and a LinkedIn
   company page showing a third number (514-929-1906) and the Montbrun postal
   code H1S 2K3 (LinkedIn blocked a direct fetch, so unverified).
   **Severity: low-to-medium.** Not a ranking blocker — these are low-authority,
   unclaimed aggregator pages, and the live GBP/website agree with each other.
   It matters because (1) conflicting NAP on aggregators can feed data
   providers, (2) callers may reach 438-866-6682 — whether that number is still
   live and the client's is unknown and should be asked, since a dead number
   means lost leads — and (3) the LinkedIn page, if accurate, is client-
   editable and a fast fix. Both directory pages offer a free claim/update
   flow. The exa.ai/aubaine name ("GROUPE NOVA - Entrepreneur général -
   Rénovation résidentielle - Construction") differs from the live GBP name
   ("GROUPE NOVA"), consistent with the same listing having been renamed, but
   not proof; the reviewer check in (a) is still the deciding test.

3. **The website's printed RBQ licence number (5881-0540-01) still resolves,
   per an independent directory, to a different address (1-8925 Avenue
   Millen) than the GBP/website address.** This may simply be a legal/
   registration address (e.g. an accountant's office or the numbered
   company's filing address) that's allowed to differ from the public-facing
   operating address — RBQ registration and GBP/citation NAP serve different
   purposes and aren't required to match. Flagged for the client to confirm
   is intentional, but **de-prioritized**: unlike the Rue Montbrun duplicate,
   this isn't a citation/map-pack risk unless that Avenue Millen address is
   *also* showing up in local-SEO-relevant places (directories, GBP, review
   sites) under the Groupe Nova name — which hasn't been found.

4. **Audit the Google Business Profile dashboard directly** to complete
   standard GBP optimization, now that the address question is resolved:
   - Confirm primary category (aggregator shows generic "General Contractor" —
     consider whether a more specific category, e.g. "Home improvement" /
     "Kitchen remodeler" / "Bathroom remodeler," better matches search intent,
     and add secondary categories for the other core services).
   - Fix the GBP display name if it currently reads as the keyword-stuffed
     "GROUPE NOVA - Entrepreneur général - Rénovation résidentielle -
     Construction" (seen via aggregator) — Google's guidelines disallow
     appending services/keywords to the business name field.
   - List kitchen, bathroom, basement, and design services individually under
     the Services tab.
   - Set the service-area field to match the client's actual target list —
     Montreal, Laval, the North Shore, the South Shore, Montérégie, and
     Lanaudière — by name, not the website's current shorthand regional labels
     (see P1 #7 below).
   - Upload 20+ real project photos (before/after kitchen, bathroom, basement
     work — the site already has strong before/after assets to reuse).
   - Start a weekly GBP Posts cadence and pre-fill the Q&A section with common
     renovation questions.
   - The live listing shows **11 reviews** at 5.0/5 (confirmed via the
     client's screenshot — an earlier pass had cited 6, from a since-identified
     stale aggregator snapshot). 11 reviews after 10+ years in business is
     still modest relative to the perfect rating and the business's apparent
     maturity — review **volume** is the opportunity here, not sentiment.
     Start a systematic ask (text/email happy clients at project completion)
     targeting 1–2 new reviews/week; mention service type + location in the
     ask so reviews naturally reinforce location signal.

5. **Run a full NAP citation audit** (PagesJaunes, Houzz, HomeStars, BBB,
   Yelp, Facebook, any renovation-specific directories) to confirm Rue
   Saint-Denis / 514-701-9898 is consistent everywhere, and to specifically
   look for the Saint-Léonard duplicate flagged in #2 above. This wasn't
   possible with available tools beyond the directory cross-references
   already found — flagged as an open item below.

## P1 — Technical SEO: on-page metadata & structured data

6. **Rewrite the homepage `<title>` tag.** It is currently just **"Groupe
   Nova"** — no service keyword, no location, nothing. This is the site's
   highest-authority URL and it's carrying zero search-relevant signal in its
   most important tag. Suggested direction, matching the page's own H1:
   "Rénovation résidentielle clé en main à Montréal | Groupe Nova" (and the
   English equivalent on `/en/`, which currently also just reads "Groupe
   Nova" — untranslated).

7. **Add a location modifier to every service page title, and fix the two
   remaining generic titles on `/a-propos/` and `/realisations/` at the same
   time.** All four service pages (`renovation-de-cuisine`,
   `renovation-de-salle-de-bain`, `renovation-de-sous-sol`,
   `services-de-design`) currently read as generic WordPress defaults — e.g.
   "RÉNOVATION DE CUISINE – Groupe Nova" — service term present, no
   "Montréal"/service-area qualifier at all. The raw capture's title table
   also shows `/a-propos/` ("À PROPOS – Groupe Nova") and `/realisations/`
   ("RÉALISATIONS – Groupe Nova") are equally generic and were checked in the
   same pass — they just weren't called out as their own numbered item in the
   first draft of this list. Low-effort, high-value fix across all 6 pages
   (12 bilingual URLs).

8. **Write a meta description for every page.** Zero pages checked have one
   (11 of 11). Without it, Google auto-generates snippets — usually pulling
   review-widget text or boilerplate rather than a controlled summary that
   could drive CTR. Lead with service + location + a call to action on each
   page.

9. **Fix the duplicate-homepage URLs.** WordPress's "static front page" setup
   leaves the underlying Page's own permalink live and separately indexable:
   `/` and `/accueil/` are two different URLs serving the same homepage
   content (confirmed via the site's own sitemap listing both), and the same
   is true for `/en/` and `/en/home/`. Fix: 301-redirect `/accueil/` → `/` and
   `/en/home/` → `/en/` (or set canonical tags on the duplicate pages to point
   at the root), then confirm the FR/EN hreflang pair is declared on the
   correct canonical URLs (`/` ⇄ `/en/`), not the duplicates.

10. **Add `LocalBusiness`/`GeneralContractor` + `Organization` structured data
    to the homepage, and `Service` schema to each of the 4 service pages
    individually (not bundled only on the homepage).** Zero JSON-LD exists
    anywhere on the site currently — no business schema, no `Service` schema
    for the 4 listed services, no `AggregateRating`/`Review` schema (despite
    the live 5.0/5 Google reviews widget), no `BreadcrumbList`. Per
    [technical-seo.md](../../framework/seo-fundamentals/technical-seo.md)'s
    existing `Organization`/`sameAs`-placement guidance, brand-level entity
    schema belongs on the homepage only — but `Service` schema is a per-item,
    per-page rich-result concern (same logic as `FAQPage`), so each service
    page should carry its own `Service` node describing *that* service, not
    just an aggregate mention on the homepage. Use the confirmed Rue
    Saint-Denis address for the `LocalBusiness` node, plus `areaServed`
    listing Montreal, Laval, Rive-Nord, Rive-Sud, Montérégie, and Lanaudière
    explicitly, consistently, on both the homepage `LocalBusiness` node and
    each page's `Service` node. Validate with Google's Rich Results Test once
    added.

11. **Disable the WordPress author-archive sitemap/pages.** `/author/farhan/`
    and `/author/hector-fabio-009hotmail-ca/` are auto-generated, thin,
    user-enumeration pages currently listed in `wp-sitemap-users-1.xml` — low
    value, and the raw-email-derived slug looks unpolished if anyone clicks
    through. Most SEO plugins (Yoast, Rank Math) have a toggle to remove
    author archives/sitemaps; this isn't a multi-author blog so there's no
    downside to turning them off.

12. **Add the `Strict-Transport-Security` (HSTS) header.** HTTP→HTTPS and
    www→non-www redirects are already correctly configured (both 301 to
    `https://groupenova.ca/`), which is the important part — HSTS is a minor
    additional hardening layer on top of that, not a ranking fix. Low
    priority, easy to add at the host/CDN level.

## P2 — Local content & image signals (fast, because the proof already exists)

13. **Add real alt text to the portfolio before/after images.** `/realisations/`
    — the site's main "proof" content, exactly what
    [local-seo-checklist.md](../../framework/local-seo-checklist.md) §5 calls
    for ("gallery images with location captions") — has 56 images, each
    sitting next to a location-named `<h2>` caption, but every single image's
    `alt` attribute is a meaningless auto-generated filename
    (`alt="image00001"`, `alt="20230509_201132000_iOS"`). Matching each
    image's alt text to its adjacent caption (e.g. "Rénovation de salle de
    bain à Laval — avant/après") is a pure-markup fix, no new photography or
    copy needed, and immediately makes the site's strongest local-proof
    content machine-readable for Google Images and location-based queries.

14. **Same fix on the homepage's 6 recent-project photos.** Each is already
    visibly captioned with a specific town — *Laval, Montréal (×2), Brossard,
    Île-des-Sœurs, Blainville* — but every image has `alt=""`. These are the
    only places on the entire site where Laval, Brossard, Île-des-Sœurs, and
    Blainville appear at all; losing that signal to empty alt text is the
    most easily fixed gap on the site.

15. **Reconcile the footer's service-area list with the client's actual
    target list.** The site currently states "Montréal, Montréal-Est, West
    Island, Rive-Nord, Rive-Sud et Lanaudière," while the engagement brief
    names "Montreal, Laval, the North Shore, the South Shore, Montérégie, and
    Lanaudière" specifically. Laval and Montérégie are real, independently
    searched local terms in Quebec, not just sub-regions of "Rive-Nord"/
    "Rive-Sud" — and the client already has completed-project proof in both
    (Laval kitchen, Brossard/Montérégie bathroom). Recommend naming Laval and
    Montérégie explicitly alongside the existing regional labels, in the
    footer copy, GBP service-area settings, and the new `LocalBusiness`
    schema's `areaServed` (P1 #10) — consistently, in all three places.

16. **Resize/compress the portfolio JPEGs.** Several before/after images are
    unresized camera originals up to 2560×2048px, served via a lazy-load
    placeholder pattern that's correctly implemented for below-the-fold
    content but still adds avoidable page weight. The hero image is already
    correctly optimized (`.webp`, preloaded, `fetchpriority="high"`) — apply
    the same WebP + responsive-size treatment to the gallery. Secondary to the
    metadata/schema fixes above, worth doing in the same pass since it's the
    same image set being touched for alt text.

## P0/P1/P2 — Website structure fixes and content depth (added 2026-10-19, scope broadened per client request)

Item #18 below is P0 (a confirmed dead lead-gen page); #17, #19, #20 are P1/P2
as noted.

17. **Clean up the English service URLs' `/services-2/` segment.** The 4
    English service pages all sit under an awkward `/en/services-2/kitchen-
    renovation/`-style path — the `-2` is a WordPress slug-collision artifact,
    not an intentional URL, while the French equivalents use the cleaner
    `/services/` segment. Each URL still carries a real service name after
    that segment, so this is a polish/consistency fix, not a broken-link
    issue: rename the slug to drop the `-2` and 301-redirect the old URLs
    (updating internal nav links and hreflang pairs to point at the new
    canonical versions) so English URLs read as cleanly as the French ones.

18. **Fix the confirmed broken render on
    `/en/services-2/interior-design-services/` — promoted to P0, this is a
    dead lead-gen page.** A `curl`-based fetch looked fine (HTTP 200, correct
    title), but the client's screenshot plus a live browser check confirmed
    the real bug: this page's phone-number country-code selector loads
    already **expanded** (244-country dropdown list rendered open by
    default), instead of collapsed like every other page's equivalent field.
    That open list visually buries the entire hero image, heading, and body
    copy beneath it, so visitors see an almost-blank page — the content is
    present in the markup, just pushed far down the page behind an unwanted,
    fully-expanded country picker. See
    [interior-design-page-bug-confirmed-2026-10-19.md](../../../raw/clients/groupe-nova/interior-design-page-bug-confirmed-2026-10-19.md)
    for the full root-cause trace. Confirmed isolated to this one URL (the
    English kitchen, bathroom, homepage, and the French kitchen page all
    render correctly) — not a site-wide outage, but this specific page is
    currently unusable for visitors and for the lead form on it. A related
    issue was also observed: the site's "Get your free quote" popup has the
    same phone-selector-stuck-open behavior in at least one instance, which
    points to a shared root cause in the phone-input widget's initialization
    — worth a broader spot-check once there's dashboard/code access. Fix:
    find and correct whatever is forcing this field's default state to open
    (an Elementor widget setting, a stray JS init call, or a broken
    conditional specific to this page/post), then confirm the equivalent
    popup-form field everywhere it appears.

19. **Build dedicated location landing pages for the target service areas
    that don't have one today.** Every content page on the site is generic
    (service-only or brand-only) — nothing targets a specific city/region on
    its own, confirmed via the full sitemap listing in
    `site-crawl-and-gbp-check-2026-10-19.md`. Start with Laval and Montérégie
    (Brossard), since real project photos already exist for both (homepage
    gallery captions, P2 #14) and both are real, independently-searched local
    terms distinct from the generic "Rive-Nord"/"Rive-Sud" footer labels
    (P2 #15). Each page should target a service+location combination (e.g.
    "rénovation de cuisine Laval"), reuse the existing before/after proof
    specific to that area, and carry its own title/meta/schema per the P1
    fixes above. Roll out the remaining areas (Rive-Nord/North Shore,
    Rive-Sud/South Shore, Lanaudière) as a follow-on phase once the first two
    are live and indexing.

20. **Expand the thin unique body copy on the homepage and 4 service pages.**
    Sampled directly on `/services/renovation-de-cuisine/`: beyond the
    reused reviews widget (identical boilerplate on every page), the entire
    unique body copy is one intro paragraph, one 4-item bullet list, one
    4-step process graphic, and one closing paragraph — no FAQ, no
    location-specific sub-sections, no "why choose us in \[area]" content
    (see
    [url-structure-and-content-depth-check-2026-10-19.md](../../../raw/clients/groupe-nova/url-structure-and-content-depth-check-2026-10-19.md)).
    This is a genuine content-depth gap distinct from the metadata gap in P1
    #6–8 — there's little indexable text to match against longer-tail local
    queries. Add a short FAQ section and a location-specific paragraph to
    each service page and the homepage, bilingual (FR+EN).

## Open items — needs direct access this capture couldn't reach

- Google Business Profile dashboard login (now mainly to confirm
  verification status, category, service-area settings, and to execute the
  Saint-Léonard duplicate merge/closure — see P0 #2, #4)
- Google Search Console (indexing status of `/accueil/` vs. `/` and
  `/en/home/` vs. `/en/`, actual impressions/rankings, any manual actions)
- Full citation/directory sweep (PagesJaunes, Houzz, HomeStars, BBB, Yelp,
  Facebook Business Page) — see P0 #5
- Real Core Web Vitals / PageSpeed Insights field data (only static image-
  format/weight signals were checked here, not a live Lighthouse run)
- Ahrefs/SEMrush backlink profile or historical rank tracking

If the client/user can provide exports from any of the above (GBP dashboard
screenshots, GSC data, a citation-tool export), ingest them against this page
per `AGENTS.md` §6 to move these recommendations from "likely" to "confirmed."
