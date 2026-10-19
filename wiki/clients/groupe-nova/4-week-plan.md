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

# 4-week execution plan — groupenova.ca (initial fixed-price scope)

Scoped to what the client requested as the initial fixed-price project: (1)
technical SEO audit and correction of priority issues, (2) Google Business
Profile optimization, (3) consistency of business information across the
website, Google profile, and directories, (4) keyword research for services
and target service areas, and (5) a written report. See
[recommendations.md](recommendations.md) for the numbered findings each
milestone draws on.

**Sequencing (revised 2026-10-19):** the first two weeks are the top-priority
fixes — broken website pages, URL/duplicate-page fixes, on-page SEO, and
aligning the GBP with the website. Keyword research moved to Week 4. Because
of that, Week 1–2 titles/meta/GBP wording are written from the existing
service × area table in [keywords.md](keywords.md) (derived from the site's
own services and the client's stated areas, no volume data). Week 4 research
validates it and includes a short refinement pass (~2h) on titles, meta, and
GBP wording if the data says to change anything.

Location landing pages and expanded page copy (Rec #19, #20) are not in the
initial scope; they are an optional Phase 2 recommended in the report.

**Estimating assumption:** all website changes are meticulous manual edits in
Elementor (no bulk tooling), and the French and English versions of each page
are edited separately.

Total estimated effort: **~55 hours** across 4 weeks (53h before, +2h for the
post-research refinement pass).

## Week 1 — Fix what's broken and the on-page basics (~17h)

- Get access: GBP dashboard, WordPress/Elementor admin, Search Console, and a
  full site backup before any edits (~1h; Rec #1).
- Fix the broken `/en/services-2/interior-design-services/` page in Elementor
  (stuck-open phone-selector burying the page) and test on desktop and mobile
  (~2h; Rec #18).
- Fix the duplicate homepage URLs (`/` vs `/accueil/`, `/en/` vs `/en/home/`)
  (~2h; Rec #9).
- Clean up the English `/services-2/` URL segment: new slugs, 301 redirects,
  menus and internal links updated by hand (~3h; Rec #17).
- Rewrite titles and meta descriptions on all ~16 French and English pages
  from the existing keyword table (~4h; Rec #6, #7, #8).
- Build one master business record (name, address, phone, hours, categories,
  RBQ licence) and audit the website and Google profile against it, so the GBP
  work in Week 2 has a baseline (~5h; Rec #2, #3, #5).

## Week 2 — Align the GBP with the website and finish on-page SEO (~15h)

- Optimize the GBP: categories, services, service areas, description,
  attributes, hours, photos, and Q&A, aligned to the website (~4h; Rec #4).
- Align the website's contact and footer details with the master record and
  update the footer service-area list (~2h; Rec #1, #15).
- Add descriptive, location-matched alt text to the portfolio and homepage
  images, and compress the heavy ones (~3h; Rec #13, #14, #16).
- Add `LocalBusiness`, `Service`, and `Review` structured data and validate it
  (~3h; Rec #10).
- Turn off the WordPress author-archive pages and add the HSTS header
  (~1.5h; Rec #11, #12).
- Set up a review-request process and a simple weekly GBP posting plan
  (~1.5h; Rec #4).

## Week 3 — Directory consistency and mid-point check (~7h)

- Correct or claim the directory listings found in the audit and remove the
  old address/phone — known so far: ProfileCanada and aubaine.ca (both
  unclaimed, free claim/update flow), plus a LinkedIn page that may show a
  third phone number; confirm with the client whether 438-866-6682 is still a
  live number (~5h; Rec #5, #2).
- Re-crawl the site and check redirects, metadata, schema, and mobile display
  of the Week 1–2 Elementor edits; fix anything found (~2h).

## Week 4 — Keyword research, refinement, and written report (~16h)

- Keyword research for services × target areas (Montreal, Laval, North Shore,
  South Shore, Montérégie, Lanaudière) in French and English: volume,
  difficulty, SERP check of local competitors, and a keyword-to-page map
  (~7h; builds on [keywords.md](keywords.md)).
- Refine titles, meta descriptions, and GBP wording where the research
  warrants it (~2h).
- Final validation and resubmit the sitemap in Search Console (~1h).
- Write the report: findings, corrections made, what remains, the keyword map,
  and the recommended Phase 2 roadmap (~5h).
- Walk the client through the report (~1h).

## Phase 2 — optional, outside the fixed price (~28h French, ~+14h for English mirrors)

Recommended in the written report, not included in the initial scope:
- Five dedicated location landing pages (Laval, Montérégie, North Shore,
  South Shore, Lanaudière) with real project proof, FAQ, and schema
  (~17h; Rec #19).
- Expand the thin body copy on the homepage and the four service pages
  (~10h; Rec #20).
- Ongoing review growth, GBP posts, and rank tracking after the 30 days.

## Day-30 success criteria

- The interior design page works, English URLs are clean, and the duplicate
  homepage URLs are resolved (done by end of Week 1).
- Every page has a unique, location-inclusive title and meta description, and
  the site has valid `LocalBusiness`/`Service`/`Review` schema (done by end of
  Week 2).
- The GBP is fully aligned with the website, and the old Montbrun address/phone
  no longer appears in the directories checked.
- A keyword map for services × areas exists, and titles/meta/GBP wording have
  been checked against it.
- The written report is delivered and walked through, with Phase 2 priced.

If Week 1's audit contradicts the confirmed Rue Saint-Denis address, stop and
re-ingest that finding into `recommendations.md` before continuing.
