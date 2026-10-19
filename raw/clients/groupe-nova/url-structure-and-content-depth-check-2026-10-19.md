# Raw capture: URL structure check, broken-link check, and content-depth sample

Captured: 2026-10-19
Method: direct `curl` fetches of live URLs on groupenova.ca (HTTP status, `<title>`,
internal nav links, and a stripped-text sample of main body copy). Triggered by the
user's request to broaden the execution plan to cover website URL fixes and more
locally-relevant content, and their specific claim that
`/en/services-2/interior-design-services/` is broken.

## Broken-link claim: not reproduced via direct fetch — flag for clarification

Direct fetch of `https://groupenova.ca/en/services-2/interior-design-services/`
today returns:
- HTTP status: **200**
- `<title>`: "Interior Design Services – Groupe Nova" (correct, matches the service)
- No "not found" / "nothing found" / 404 markers in the returned HTML

The URL is also correctly linked from the English homepage's own nav menu
(`https://groupenova.ca/en/` contains `href="https://groupenova.ca/en/services-2/
interior-design-services/"` verbatim, alongside the other 3 English service links,
all also returning 200).

**This doesn't match "broken."** Possible explanations this capture can't rule out,
since it's a static HTML fetch with no JS execution and no visual rendering: a
client-side JS error breaking something *within* the page after load, a broken
embedded element (image, form, map) below the fold, a mobile-specific rendering
issue, a transient/intermittent outage at the moment the client checked it, or a
browser-cache artifact on the client's end. Recommend the client reconfirm (ideally
with a screenshot or a description of exactly what "broken" looks like — blank page,
error message, broken layout, broken form/button) before scoping a fix, since a
server-side/markup fix isn't indicated by what's fetchable here.

## URL structure observation

English service URLs all sit under an awkward `/en/services-2/` path segment
(`/en/services-2/kitchen-renovation/`, `/en/services-2/bathroom-renovation/`,
`/en/services-2/basement-renovation/`, `/en/services-2/interior-design-services/`),
vs. the French equivalents under the cleaner `/services/` segment. The `-2` suffix
is a classic WordPress artifact (auto-appended when a second page/post uses a slug
that collides with an existing one) and reads as unpolished/unintentional in a live
URL, even though each individual URL does still carry a descriptive service name
after that segment.

## Content-depth sample: confirms genuinely short unique body copy per service page

Stripped-text sample of `/services/renovation-de-cuisine/`'s main content (tags
stripped, reviews-widget boilerplate included since it's part of what actually
renders on the page):

> Rénovation de cuisine — Transformez votre maison avec notre expertise en
> rénovation résidentielle — [one intro paragraph] — Avantages: [4 short bullet
> points: dedicated project manager, on-site foreman, written detailed quotes,
> durable materials] — Notre processus simple et efficace: [4-step numbered
> process: free on-site consultation, work planning, renovation, delivery/
> follow-up] — [Trustindex reviews widget — same 6 reviews repeated verbatim on
> every page] — "Spécialistes en rénovation de cuisine à Montréal, West-Island,
> Rive-Nord, Rive-Sud et Lanaudière" — [one closing paragraph]

Beyond the reused reviews widget (identical boilerplate across every page, not
unique content), the actual unique body copy on this page is: one intro paragraph,
one 4-item bullet list, one 4-step process graphic, and one closing paragraph — no
FAQ section, no location-specific sub-sections, no "why choose us in [area]"
content, no warranty/materials detail beyond the single "quality materials" bullet.
This pattern (confirmed sampled on this one page, consistent with the generic
WordPress-default framing already documented for titles/meta across all pages in
`site-crawl-and-gbp-check-2026-10-19.md`) supports a content-depth gap distinct from
the metadata gap already flagged — there's genuinely little indexable text for
Google to match against specific, longer-tail local queries.

## No dedicated location landing pages exist anywhere on the site

Per the full sitemap listing in `site-crawl-and-gbp-check-2026-10-19.md`, the only
content pages are the 4 generic services + homepage + about + portfolio — no page
targets a specific city/region (Laval, Rive-Nord, Rive-Sud, Montérégie, Lanaudière)
on its own. The only place those specific town names (Laval, Brossard,
Île-des-Sœurs, Blainville) appear at all is in homepage gallery image captions,
already flagged in `recommendations.md` P2 #14.
