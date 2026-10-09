---
type: recommendation
client: tipicita-kinesio
status: active
updated: 2026-10-08
sources: [raw/clients/tipicita-kinesio/site-crawl-2026-10-08.md]
---

# Recommendations — tipicita-kinesio.com (Le Bouscat relocation SEO)

Context: the practice moved from Eysines/Mérignac to Le Bouscat on **19 August
2026**. The site has real existing equity (7 years of blog content, 47 Google +
73 Résalib reviews, 5.0/5 everywhere) that just needs to be correctly
re-anchored to the new location — this is a **location-migration fix**, not a
from-scratch local SEO build.

## P0 — Fix NAP inconsistency (do first, unambiguous, highest impact)

1. **Fix the stale homepage `LocalBusiness` schema.** The homepage's JSON-LD
   still declares `addressLocality: "Eysines", postalCode: "33320"`. This
   directly contradicts the visible page content (Le Bouscat, 33110) and is
   actively telling Google's structured-data parser the business is somewhere it
   no longer is. Update to the Le Bouscat address immediately. This is the
   single highest-leverage fix available — a crawler/algorithm reading schema
   will trust it over body text.
2. **Add `LocalBusiness`/`ProfessionalService` schema to `/ou-me-trouver`.** This
   is the page most relevant to the location query and currently has zero
   structured data. Include: full new NAP, geo coordinates, `areaServed`
   (Bordeaux, Caudéran, Bruges, Eysines, Mérignac, sud Médoc — all already named
   in the page copy), opening hours if available.
3. **Close the known stale external citation.** lesmedecinesdouces.fr still lists
   "Coach-de-vie, 76 Av. de la Libération, 33320 Eysines" and is still actively
   aggregating reviews under that stale listing (last review 30 June 2026). Claim
   the listing and update it, or request removal/merge if it's a duplicate of a
   correct listing elsewhere. Treat this as a sample finding, not a complete
   list — a full citation audit (PagesJaunes, Doctolib, Resalib profile itself,
   other annuaire-thérapeutes sites) wasn't possible with available tools and
   should be done directly (see Open items below).
4. **Audit the Google Business Profile directly** (not accessible to this
   capture — requires GBP dashboard login). Confirm: (a) the primary listing's
   address, hours, and service-area are updated to Le Bouscat; (b) old
   Eysines/Mérignac listings were properly merged or closed via Google's
   "business moved" flow rather than left as duplicate/orphaned profiles, which
   would split review signal and confuse the map pack; (c) a "business moved"
   Google Post was published to reinforce the change to Google and to returning
   searchers.

## P1 — On-page location signal gaps

5. **Rewrite the homepage `<title>` and meta description to include Le Bouscat.**
   Currently: "Accueil | Emmanuelle Mesnard-Coach de vie-kinesiologue bordeaux" —
   mentions Bordeaux only. The homepage is the site's highest-authority page and
   currently carries zero location-migration signal in its most important tag.
   Suggested direction: lead with "Kinésiologue & Coach de vie au Bouscat (près
   de Bordeaux)" to match the already-correct pattern used on `/ou-me-trouver`
   and `/kinesiologie-coaching-bordeaux`.
6. **Mark up the existing Q&A on `/ou-me-trouver` as `FAQPage` schema.** The
   content already exists verbatim ("Les cabinets de Mérignac et d'Eysines
   sont-ils fermés ?", "Où se garer près du cabinet ?", "Par où entrer ?") — this
   is a zero-new-copy, pure-markup win that's also a natural fit for an
   AI-Overview-style citation (direct Q&A format), per
   [local-seo-checklist.md](../../framework/local-seo-checklist.md).
7. **Add `/juste-decision` and `/mon-approche` location mentions.** Neither
   title/meta currently names Bordeaux or Le Bouscat at all (`/juste-decision`
   has no location reference whatsoever). Lower priority than the homepage fix
   since these are mid-funnel pages, but easy to patch opportunistically.
8. **Mark up testimonials with `Review`/`AggregateRating` schema.** The 47
   Google + 73 Résalib five-star reviews are a genuine strength but currently
   appear only as plain-text quotes on the homepage and `/cap-famille`. Adding
   review schema is a low-effort way to make this trust signal machine-readable
   and eligible for rich results.

## P2 — Protect and extend existing equity

9. **Don't break the legacy Mérignac/Eysines blog URLs.** Several posts (e.g.
   `/post/mieux-gérer-son-stress-kinesiologie-coaching-bordeaux-merignac`) have
   the old location baked into the URL and have accrued links/age since 2019–2021.
   Leave the URLs alone; instead add a short, natural in-body mention + internal
   link from each to `/ou-me-trouver` so link equity and topical relevance flow
   to the new location page, and so a reader landing on old content isn't
   confused about where the practice is now.
10. **Build light content for the named feeder suburbs** (Caudéran, Bruges) that
    currently only get a one-line mention inside `/ou-me-trouver`. Even a short
    paragraph each ("depuis Caudéran, comptez X minutes en voiture...") with
    internal links would extend long-tail "near me" coverage without the
    SEO/legal risk of a full separate location page for a town the practice
    doesn't physically operate in.
11. **Lean into `coach de vie le bouscat` over `kinésiologue le bouscat` where
    possible.** Live check (2026-10-08) shows `/ou-me-trouver` already ranking
    #1 for the coach-de-vie variant, in a much less contested field (mostly
    thin directory-only competitor listings). The kinésiologue variant has 5
    established, well-reviewed local competitors, including one
    ([Marion Reynaud](competitors/mr-kinesiologue.md)) with nearly double
    Tipicita's review count. Both terms should stay targeted, but coach de vie
    is the faster, less contested win — see
    [keywords.md](keywords.md).
12. **Watch the geographic cluster.** Tipicita's new address (281 Av. de la
    Libération Charles de Gaulle) is on the exact same street as two
    competitors ([Aude Coué](competitors/aude-coue.md) and
    [Nina Peret](competitors/bonjourlebonheur-nina-peret.md), both at #20). Map-pack
    results for this corridor will likely show all three together — differentiate
    via the combined kinésiologie+coaching positioning and the structured
    multi-session programs (Juste Décision, Juste Place), which none of the
    directory-listed competitors appear to offer.

## Open items — needs direct access this capture couldn't reach

- Google Business Profile dashboard audit (see P0 #4)
- Google Search Console: actual impressions/clicks pre- vs. post-move,
  indexing status of `/ou-me-trouver`, any manual actions
- Full citation audit beyond the two directories sampled (PagesJaunes, Doctolib,
  Resalib's own profile page, other annuaire-thérapeutes sites)
- Backlink profile (Ahrefs/SEMrush) to confirm no high-value external links point
  to the Eysines/Mérignac address pages that should be redirected

If the client/user can provide exports from any of the above (GSC, GBP insights,
Ahrefs), ingest them against this page per AGENTS.md §6 to sharpen these
recommendations from "likely" to "confirmed."
