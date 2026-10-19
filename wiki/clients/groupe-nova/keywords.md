---
type: keyword-map
client: groupe-nova
status: draft
updated: 2026-10-19
sources: [raw/clients/groupe-nova/site-crawl-and-gbp-check-2026-10-19.md, raw/clients/groupe-nova/engagement-and-estimates-notes-2026-10-19.md]
---

# Keyword map — groupenova.ca

Status legend: `targeted-onpage` (title/meta/H-tag already names this
combination), `gap` (service and location both exist on the site but aren't
paired anywhere in titles/meta/copy/schema), `proof-only` (real completed-
project evidence exists — a gallery caption — but isn't used as an SEO
signal anywhere else).

No rank-tracker/SERP export or search-volume data has been supplied yet for
this client — this table is derived from the site's own service list and the
client's stated service areas, not from keyword-research tooling. Treat
priority as directional until real volume/difficulty data is ingested.

## Core service × primary market

| Keyword | Intent | Priority | Status | Notes |
|---|---|---|---|---|
| rénovation résidentielle Montréal | transactional, local | High | gap | This is the homepage's actual H1 concept ("Rénovation résidentielle clé en main à Montréal et aux alentours") but the `<title>` tag is just "Groupe Nova" — the phrase never reaches the title/meta layer. |
| rénovation cuisine Montréal | transactional, local | High | gap | `/services/renovation-de-cuisine/` title is "RÉNOVATION DE CUISINE – Groupe Nova" — service term present, no location modifier. |
| rénovation salle de bain Montréal | transactional, local | High | gap | Same pattern as above on `/services/renovation-de-salle-de-bain/`. |
| rénovation sous-sol Montréal | transactional, local | High | gap | Same pattern as above on `/services/renovation-de-sous-sol/`. |
| entrepreneur général Montréal | transactional, local | Medium | gap | Matches the GBP category ("General Contractor" per aggregator data) and the "À propos" positioning; not targeted in any title/meta. |

## Secondary markets named in the service-area brief

| Keyword | Intent | Priority | Status | Notes |
|---|---|---|---|---|
| rénovation cuisine Laval | transactional, local | High | proof-only | Homepage gallery caption shows a real completed Laval kitchen project — zero other on-site signal (no title/meta/schema mention of Laval anywhere). |
| rénovation salle de bain Brossard | transactional, local | Medium | proof-only | Real completed project per gallery caption (Brossard = Montérégie/South Shore) — same gap. |
| rénovation Rive-Nord / rénovation Rive-Sud | transactional, local | Medium | targeted-onpage | Covered generically in the `/services/` body copy and footer service-area line, but not reinforced with specific town names or in any title/meta. |
| rénovation Montérégie | transactional, local | Medium | gap | Named in the client brief, not named anywhere on the site (site uses "Rive-Sud" instead). |
| rénovation Lanaudière | transactional, local | Medium | targeted-onpage | Already named explicitly in the footer service-area line — the only brief-matching area term currently on-site. |
| rénovation Blainville / Île-des-Sœurs | local, near-me | Low–Medium | proof-only | Both appear as real completed-project captions on the homepage (gallery) but nowhere else. |
| rénovation Montréal-Est / rénovation West Island | transactional, local | Medium (unverified) | gap | Both are in the website footer's service-area line and in the owner's region list for the retainer ([engagement-and-estimates-notes-2026-10-19.md](../../../raw/clients/groupe-nova/engagement-and-estimates-notes-2026-10-19.md)), but were not in the original brief and have no on-site proof, title, or copy. No volume data yet; the planned Google Ads search-terms report (Feb–March 2027) is the first real data source. |

## Brand / trust terms

| Keyword | Intent | Priority | Status | Notes |
|---|---|---|---|---|
| Groupe Nova avis / Groupe Nova reviews | navigational | Medium | gap | No `AggregateRating`/`Review` schema exists despite a live 5.0/5 Trustindex widget — see `recommendations.md`. |
| entrepreneur rénovation RBQ licencié Montréal | transactional, trust-qualifier | Medium | targeted-onpage | RBQ license number and CCQ/APCHQ badges are visible on-page (with correct alt text on the logos) but not reinforced in any schema (`LocalBusiness` lacking entirely) or title/meta. |

## Gaps to close first (see recommendations.md for the fix)

1. Homepage `<title>` has zero keyword or location signal at all ("Groupe
   Nova") — the single biggest on-page miss on the site's highest-authority
   URL.
2. Every service page title has the service term but no location modifier —
   an easy, high-value title-tag rewrite across 4 pages
   (`renovation-de-cuisine`, `renovation-de-salle-de-bain`,
   `renovation-de-sous-sol`, `services-de-design`).
3. Laval, Brossard, Blainville, and Île-des-Sœurs all have real, provable
   completed-project photos already on the site but are invisible to search
   (no alt text, no titles/meta, no schema `areaServed`) — the fastest path to
   ranking for these specific towns is making existing proof machine-readable,
   not producing new content.
4. "Montérégie" (from the client brief) doesn't appear anywhere on-site; the
   site uses "Rive-Sud" instead. Decide whether to add "Montérégie" explicitly
   alongside "Rive-Sud," since both are independently searched terms in
   Quebec.
