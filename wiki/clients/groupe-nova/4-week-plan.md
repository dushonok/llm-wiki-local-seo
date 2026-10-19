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

**Estimates:** the hours below are the owner's own estimates from their
planning spreadsheet ("Group Nova estimates for first 2 weeks", 2026-10-19),
which supersede the earlier wiki estimates (~48.5h). Total: **40.5 hours** —
Week 1 15h, Week 2 7.5h, Week 3 7h, Week 4 11h, ongoing 0h. The sheet prices
this at $1,417.50 "estimated" ($35/h) and $1,300 in its "real" column ($500 /
$250 / $200 / $350 for Weeks 1–4). All website changes are manual edits in Elementor, with the French and English
versions of each page edited separately.

**Sequencing:** the first two weeks are the top-priority fixes — broken
website pages, URL/duplicate-page fixes, on-page SEO, and aligning the GBP with
the website. Keyword research is not priority #1 (the broken page, title tags,
and GBP categories rank higher in impact), so it is split: a short wording
check (1h) in Week 1, right before the titles are written, covering the 4
services in French and English for Montreal plus the homepage phrasing; and the
full services × areas research in Week 4 (4h), which mainly feeds the report
and Phase 2 location pages. A refinement pass (2h) in Week 4 adjusts titles,
meta, and GBP wording if the full research says to.

Location landing pages and expanded page copy (Rec #19, #20) are not in the
initial scope; they are an optional Phase 2 recommended in the report.

## Week 1 — Audit, fix what's broken, and the on-page basics (15h)

- Technical SEO audit — estimated 5h, of which 3h are already spent (5h;
Rec #1–#20 findings).
- Get access: GBP dashboard, WordPress/Elementor admin, Search Console, and a
full site backup before any edits (1h; Rec #1).
- Build one master business record (name, address, phone, hours, categories,
RBQ licence) and audit the website and Google profile against it, so the GBP
work in Week 2 has a baseline (1h; Rec #2, #3, #5).
- Fix the broken `/en/services-2/interior-design-services/` page in Elementor
(stuck-open phone-selector burying the page) and test on desktop and mobile
(1.5h; Rec #18).
- Fix the duplicate homepage URLs (`/` vs `/accueil/`, `/en/` vs `/en/home/`)
(0.5h; Rec #9).
- Rewrite titles and meta descriptions on all ~16 French and English pages from
the existing keyword table (3h; Rec #6, #7, #8).
- Quick keyword wording check before writing titles: volume and phrasing for
the 4 services in French and English for Montreal, plus the homepage
phrasing (1h; builds on [keywords.md](keywords.md)).
- Rewrite titles and meta descriptions on all ~16 French and English pages
using that check (2h; Rec #6, #7, #8).

## Week 2 — Align the GBP with the website and finish on-page SEO (7.5h)

- Optimize the GBP: categories, services, service areas, description,
attributes, and hours, aligned to the website (1h; Rec #4). The 20+ project
photo upload and the pre-filled Q&A moved to ongoing maintenance.
- Align the website's contact and footer details with the master record and
update the footer service-area list (1.5h; Rec #1, #15).
  - Add descriptive, location-matched alt text to the portfolio and homepage
  images (2h; Rec #13, #14). Compressing the heavy images moved to ongoing
  maintenance.
- Add `LocalBusiness`, `Service`, and `Review` structured data and validate it
(2h; Rec #10).
- Set up the review-request process (short Google review link, FR/EN message
templates, a simple tracking sheet, and a completion-day routine) so reviews
start arriving during the 30 days (1h; Rec #4).

## Week 3 — Directory consistency, English URL cleanup, and mid-point check (7h)

- Correct or claim the main directory listings found in the audit and remove
the old address/phone — known so far: ProfileCanada and aubaine.ca (both
unclaimed, free claim/update flow), plus a LinkedIn page that may show a third
phone number; confirm with the client whether 438-866-6682 is still a live
number (3h; Rec #5, #2). Smaller scraped directories (e.g. studio-lb.fr)
moved to ongoing maintenance.
- Clean up the English `/services-2/` URLs: remove the redirect that sends
`/en/services/` to the French services page, make the English services page
live at `/en/services/` (if the multilingual setup allows the same slug in
both languages; otherwise use a different English slug), 301-redirect
`/en/services-2/` and its four child pages to the new addresses, and update
menus and internal links by hand (2h; Rec #17).
- Re-crawl the site and check redirects, metadata, schema, and mobile display of
the Week 1–2 Elementor edits; fix anything found (2h).

## Week 4 — Full keyword research, refinement, and written report (11h)

- Full keyword research for services × target areas (Montreal, Laval, North
Shore, South Shore, Montérégie, Lanaudière) in French and English: volume,
difficulty, SERP check of local competitors, and a keyword-to-page map; the
Montreal wording is already covered by the Week 1 check (4h; builds on
[keywords.md](keywords.md)).
- Refine titles, meta descriptions, and GBP wording where the research warrants
it (2h).
- Final validation and resubmit the sitemap in Search Console (1h).
- Write the report: findings, corrections made, what remains (including the
low-priority author-archive and HSTS items, handed to ongoing maintenance),
the keyword map, and the recommended Phase 2 roadmap (3h).
- Walk the client through the report (1h).

## Ongoing — after the 4 weeks, not counted in the 40.5h

- Turn off the WordPress author-archive pages and add the HSTS header (0h in
the fixed-price sheet; earlier wiki estimate ~1h for the author archives
including sitemap removal and hiding usernames, ~0.5h for HSTS with a short
max-age; Rec #11, #12).
- GBP photos and Q&A: upload 20+ real before/after project photos and
pre-fill the Q&A with common renovation questions (Rec #4).
- Compress the heavy portfolio images (Rec #16).
- Write the weekly GBP posting plan using the final keyword wording and target
areas, then run weekly posts (Rec #4).
- Clean up the old address/phone on smaller scraped directories (e.g.
studio-lb.fr) beyond the main listings handled in Week 3 (Rec #5).
- Review growth and rank tracking.

## Phase 2 — optional, outside the fixed price (~28h French, ~+14h for English mirrors)

Not in the owner's spreadsheet; the earlier wiki estimate is unchanged. Recommended in the
written report, not included in the initial scope:

- Five dedicated location landing pages (Laval, Montérégie, North Shore, South
Shore, Lanaudière) with real project proof, FAQ, and schema (~17h; Rec #19).
- Expand the thin body copy on the homepage and the four service pages (~10h;
Rec #20).

## Open questions on the estimates

- **Possible duplicate title/meta row.** The sheet has two "rewrite titles and
meta descriptions" rows in Week 1 (3h "from the existing keyword table" and
2h "using that check"). The first predates the keyword wording check; if the
second replaces it, Week 1 is 12h and the total is 37.5h (~$1,310 at $35/h).
Kept both here to match the sheet.
- **GBP optimization at 1h — resolved.** Photos (20+) and pre-filled Q&A
moved to ongoing maintenance, so the 1h now covers only categories,
services, service areas, description, attributes, and hours.

## Day-30 success criteria

- The interior design page works and the duplicate homepage URLs are resolved
(done by end of Week 1); English service URLs are clean (done in Week 3).
- Every page has a unique, location-inclusive title and meta description, and
the site has valid `LocalBusiness`/`Service`/`Review` schema (done by end of
Week 2).
- The GBP is fully aligned with the website, and the old Montbrun address/phone
no longer appears in the directories checked.
- Title wording was checked against keyword data before it was written (Week
1), and a full services × areas keyword map exists and has been used to
refine titles/meta/GBP wording (Week 4).
- The written report is delivered and walked through, with Phase 2 priced.

If Week 1's audit contradicts the confirmed Rue Saint-Denis address, stop and
re-ingest that finding into `recommendations.md` before continuing.
