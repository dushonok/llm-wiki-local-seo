# Log

Append-only. One entry per ingest/query/lint action that changed the wiki. Newest
entries at the bottom. Format:

```
## YYYY-MM-DD | ingest|query|lint | short title
One or two sentences: what happened, what changed, what was learned.
Pages touched: [[path/to/page.md]], [[path/to/other.md]]
```

Do not edit or delete past entries — if something was wrong, add a new entry
correcting it rather than rewriting history.

---

## 2026-10-16 | ingest | Service-area-only business (NAP & schema guidance)
Added documentation to [[framework/on-site-seo.md]] and [[framework/local-seo-checklist.md]] explaining how to handle businesses with no customer-facing address. Covers website footer strategy (name + phone only), LocalBusiness schema using `areaServed` instead of `address`, and GBP setup as service-area-only (verification address hidden). Clarifies that service-area-only configuration often ranks better than publishing an office address when business is truly mobile/multi-location-serving. Addresses documentation gap: previous pages assumed physical address requirement; this update distinguishes legitimate service-area businesses (plumbing, HVAC, cleaning, etc.) from location-based retail.
Pages touched: [[framework/on-site-seo.md]], [[framework/local-seo-checklist.md]]

## 2026-10-06 | ingest | Social media profiles as backlink sources
Populated [[framework/backlinks.md]] (was a stub) with social media platform hierarchy for building backlinks and citations. Covers YouTube, Reddit, Instagram, Facebook, TikTok, LinkedIn, trade associations ranked by domain authority × AI citation frequency × implementation ease. Included 12-week mold remediation example, linking architecture with `/profiles` page, niche-specific platform selection, and quarterly audit cadence. Updated [[index.md]] to reflect active status and summary.
Pages touched: [[framework/backlinks.md]], [[index.md]]

## 2026-09-04 | setup | Vault scaffolded
Set up AGENTS.md and the wiki/templates/raw structure per Karpathy's LLM-wiki
pattern, tailored for local SEO agency work (multi-client, shared framework/
layer + per-client subtree). No client or framework content ingested yet.
Pages touched: [[index.md]]

## 2026-09-04 | ingest | AI Overviews and local SEO checklist
Ingested two AI Overviews sources from AI SEO: Rank Expand Academy. Created
[[framework/ai-overviews-local-search.md]] covering how AI Overviews reshape
local intent, CTR, and visibility above map packs. Populated
[[framework/local-seo-checklist.md]] with 7-part checklist for AI Overviews
readiness (NAP, GBP optimization, reviews, schema, content, citations,
monitoring). Updated [[index.md]] to catalog both new framework pages.
Pages touched: [[framework/ai-overviews-local-search.md]], [[framework/local-seo-checklist.md]], [[index.md]], [[log.md]]

## 2026-09-04 | ingest | Detailed checklist sections + skill-level roadmaps
Ingested granular source files breaking down each of the 7 checklist sections,
plus a 3-tier Next Steps guide (Beginner, Intermediate, Advanced). Enhanced
[[framework/local-seo-checklist.md]] with detailed actionable steps for each skill
level, including specific Google search queries for NAP audits and tactical
tools/frequencies for monitoring. Updated sources list to include all 9
detailed raw files.
Pages touched: [[framework/local-seo-checklist.md]], [[log.md]]

## 2026-09-04 | ingest | Getting cited by AI + fan-out queries + on-page structure
Ingested three new sources on AI citation strategy, fan-out query research, and on-page
content structure. Created [[framework/getting-cited-by-ai.md]] documenting 5 moves:
invisible URLs, social mentions, listicles, expired-domain sponsorships, and citation-indexing
profiles page. Created [[framework/fan-out-queries-and-ais.md]] synthesizing data from
173,902 URLs showing 0.77 correlation between fan-out ranking and AIO citations; recommends
topical authority strategy over fan-out chasing. Enhanced [[framework/on-site-seo.md]]
from stub to full 8-step content structure recipe (title, lead-in, answer, H2s, entity
signals) with implementation checklist. Updated [[index.md]].
Pages touched: [[framework/getting-cited-by-ai.md]], [[framework/fan-out-queries-and-ais.md]],
[[framework/on-site-seo.md]], [[index.md]], [[log.md]]

## 2026-09-05 | ingest | AI tool stacks + niche selection strategy from community calls
Ingested 20+ new community call files documenting practical AI/automation stacks and niche
selection tactics. Created [[framework/ai-tool-stacks.md]] synthesizing 11 tool stacks
(Shawn's programmatic pages, dual-AI content, Claude writing tools, WordPress factory,
12-minute microsites, master Git deployment, voice AI, SMS bot, Leadsie onboarding, custom
MCPs, GHL consolidation) with implementation guidance. Created [[framework/niche-selection-strategy.md]]
capturing the "niches within niches" thesis with 3-level niche framework, 12-minute microsite
build process, volume strategy (validation → scaling), research-first mindset, and business
models (lead gen, affiliates, personal volume). Updated [[index.md]] and [[log.md]].
Pages touched: [[framework/ai-tool-stacks.md]], [[framework/niche-selection-strategy.md]],
[[index.md]], [[log.md]]

## 2026-09-11 | query | TLD choice for microsite domains (.com vs .org)
User asked whether `.org` is an acceptable substitute for `.com` on microsite domains.
No existing wiki/raw content addressed TLD choice directly, so answered from general
SEO knowledge (no ranking penalty either way; `.com` marginally better for commercial
trust; `.org` fine when the EMD `.com` string is taken; mixed TLDs across a portfolio
slightly reduce entity-linking footprint). Filed the answer back into
[[framework/niche-selection-strategy.md]] under the domain purchase step, explicitly
flagged as not sourced from a raw call, to keep the wiki traceable.
Pages touched: [[framework/niche-selection-strategy.md]], [[log.md]]

## 2026-09-16 | query | Unverified GBP has no local SEO value
User asked whether an unverified Google Business Profile has any local SEO use.
Answered: essentially none — unverified GBPs are suppressed from meaningful
Map Pack placement, marked "not publicly visible," and blocked from
Insights/review-response/full-edit access; verification is a gate that must
happen before any GBP optimization step contributes to ranking. Connected this
to the existing "GBP Gap Mining" concept in Community Call 9 (unverified GBPs
as prospecting targets, not something to lean on). Added a callout to
[[framework/local-seo-checklist.md]] section 2, flagged as general SEO
knowledge not sourced from a raw call.
Pages touched: [[framework/local-seo-checklist.md]], [[log.md]]

## 2026-09-18 | ingest | Business operations layer (5 pages) from Sep 8 Wisdom files
Created 5 new framework pages covering agency operations, pricing, sales, and client management
(not completed in prior session). Created [[framework/agency-operations-scaling.md]] with 3 shifts
to move from solo operator to systems-based scaling (Loom training libraries, bounded services,
documented systems). Created [[framework/pricing-and-deal-structures.md]] synthesizing 11 pricing
plays (per-lead, retainers, stacking, upfront payment, contracts, hourly design). Created
[[framework/client-selection-filters.md]] with 4 pre-qualification filters (expertise respect,
review count sweet spot, volume capacity, niche leverage). Created [[framework/sales-and-lead-generation.md]]
with 3 approaches when cold outreach stalls (human touch, specific hooks, channel stacking).
Created [[framework/client-retention-strategies.md]] covering relationship building, visible-work
proof, and service intertwining. Updated [[index.md]] with new pages grouped by category.
Pages touched: [[framework/agency-operations-scaling.md]], [[framework/pricing-and-deal-structures.md]],
[[framework/client-selection-filters.md]], [[framework/sales-and-lead-generation.md]],
[[framework/client-retention-strategies.md]], [[index.md]], [[log.md]]

## 2026-09-18 | ingest | Citations strategy + AI reliability pages
Ingested new sources on citations and AI context management. Created [[framework/citations-strategy.md]]
covering citations spectrum (real NAP vs. created address vs. none), strategy by situation,
Wikipedia citation opportunities, and legal considerations; addresses both client sites and R&R
microsites with decision trees. Created [[framework/ai-reliability-and-context.md]] on fixing
context overload with 3 solutions: multi-agent architecture (Paperclip), WikiLLM memory setup,
guardrails + version control; includes implementation tier system and quick wins. Updated [[index.md]].
Pages touched: [[framework/citations-strategy.md]], [[framework/ai-reliability-and-context.md]],
[[index.md]], [[log.md]]

## 2026-09-22 | ingest | EMD domain strategy + citations case study + Fiverr reference list
Ingested new sources on domain strategy, citation implementation, and Fiverr services. Enhanced
[[framework/niche-selection-strategy.md]] with new section on EMD strategy: dashes vs. no-dashes,
noting that google-plumbing.com and google-plumbing.com are functionally equivalent EMDs but dash
variant is trending with top 3 rankings observed. Enhanced [[framework/citations-strategy.md]] with
Hunter Lord's real-world #1-ranking citation case study (115 citations, 2 hrs/day for 3 weeks,
5 citations/day pace, then validated with index checker). Added comprehensive Fiverr citation
services reference list (60 platforms from @mason_fik's packages) to enable gap analysis. Updated
sources fields and log.
Pages touched: [[framework/niche-selection-strategy.md]], [[framework/citations-strategy.md]], [[log.md]]

## 2026-09-22 | ingest | Open Graph & metadata page
User asked how important Open Graph is for local on-page SEO. Answer wasn't sourced from a raw
capture — general SEO knowledge, flagged for traceability (same convention as the GBP-verification
note in [[framework/local-seo-checklist.md]]). Created [[framework/open-graph-and-metadata.md]]:
OG tags are not a Google ranking factor, but matter indirectly for social share CTR, citation/
directory tool fallback text, and AI/LLM summarization fallback; includes recommended minimum
tag set and a priority stack showing OG ranks below schema, content, and NAP consistency. Updated
[[index.md]].
Pages touched: [[framework/open-graph-and-metadata.md]], [[index.md]], [[log.md]]

## 2026-09-23 | ingest | External SEO tactics for fast-ranking microsites
Ingested chat summary synthesizing external SEO strategy for a single-location microsite
(moldremediationgettysburgpa.org, Gettysburg PA). Created [[framework/external-seo-microsite-tactics.md]]
documenting 5 external SEO levers ranked by ROI: expired-domain sponsorships ($20–50), NAP
citations + GBP, AI-citation targeting (invisible URLs via DataForSEO), third-party listicles
($100–500), and social proof (Reddit, YouTube, FB groups + /profiles page). Included detailed
NAP citations process (lock format → claim Data Axle [optional] → 10–20 top-tier directories →
index all → quarterly audit), VA delegation split (what to outsource vs. keep in-house), and
single-location expansion strategy (hub-and-spoke with nearby towns, genuine hyperlocal content).
Added action checklist and key decision points. Updated [[index.md]].
Pages touched: [[framework/external-seo-microsite-tactics.md]], [[index.md]], [[log.md]]

## 2026-09-25 | query | Meta description town lists — state abbreviation or not
User asked whether Services/Service-Area meta descriptions listing towns without the state
("Hanover, Littlestown" vs. "Hanover, PA, Littlestown, PA") hurts SEO. Not tied to a client.
Answer wasn't sourced from a raw capture — general SEO knowledge, flagged for traceability (same
convention as the OG-tags page and the GBP-verification note in `local-seo-checklist.md`). Verdict:
generally fine — meta descriptions aren't a direct ranking signal (mainly affect CTR), and the real
geo/entity signal for rankings + AI Overviews lives in schema/H1/body copy, not the meta description
string. Caveat: town names that collide across multiple states (Hanover, Springfield, etc.) lose
their only disambiguating signal in that snippet if state is dropped entirely — recommend keeping
state at least once per description. Added new "Meta Descriptions: Town Lists" section to
[[framework/on-site-seo.md]]. Updated [[index.md]].
Pages touched: [[framework/on-site-seo.md]], [[index.md]], [[log.md]]

## 2026-09-25 | query + ingest | Local SEO page reviews + microsite builder rebuild strategy
Reviewed moldremediationgettysburgpa.org homepage, `/cost`, and `/service-areas` pages for local
SEO implementation (not logged as a formal client — one-off review, user declined to onboard as a
tracked microsite). Findings: homepage and `/cost` had Service + FAQPage schema added since the
first pass (fixed); open items across pages included missing aggregateRating/review signals, empty
hero image alt text, no `sameAs` social links, no geo coordinates, long meta descriptions, a weak
H1/skipped-heading-level on `/service-areas`, and schema-Offer-names-as-prose making `/cost` copy
read unnaturally. User then asked whether to rebuild already-ranking sites when updating the
microsite builder; shared a builder changelog confirming URLs stay stable (redirects added when
they do change). Added new "Updating a Microsite Builder — Safe vs. Risky Rebuild Changes" section
to [[framework/external-seo-microsite-tactics.md]]: 3-tier risk framework (Tier 1 — schema/alt-text/
meta fixes, ship freely; Tier 2 — same-URL content rewrites, safe but brief re-eval window; Tier 3 —
URL changes, require 301 redirects) plus a staged-rollout recommendation (new sites first, batch +
monitor GSC for already-ranking sites). Updated [[index.md]].
Pages touched: [[framework/external-seo-microsite-tactics.md]], [[index.md]], [[log.md]]

## 2026-09-25 | ingest | Bulk ingest: Community Calls 42–55 (14 new sources)
Ingested 14 community call transcripts (September 2026, Calls #42–55) covering microsite building,
external SEO, AI tooling, scaling, and directory monetization. Added two new sections to 
[[framework/external-seo-microsite-tactics.md]]: (1) "Content Depth & AI Citations" — 150+ words in
hero + multiple sections needed to rank & get cited; EMDs + content depth win together; 1,000–10,000
word pages outrank shorter content; (2) "Directory Authority as a Backlink Engine" — lean WordPress/
Cloudflare directories can monetize listings ($50–200/year premium tiers) and backlink to microsites.
Enhanced sources to include Calls 43, 44, 45, 49, 52, 54, 55. These calls also seed future ingests
into [[ai-tool-stacks.md]] (Claude Fable, DeepSeek, Hermes, OpenRouter, Index Bolt), 
[[niche-selection-strategy.md]] (zero-volume keywords, market validation), [[agency-operations-scaling.md]]
(retention, pricing tiers, portfolio management), and [[pricing-and-deal-structures.md]] (recurring
revenue models, "build first" sales). Deferred those updates to keep ingest focused. Updated timestamp.
Pages touched: [[framework/external-seo-microsite-tactics.md]], [[log.md]]

## 2026-09-26 | ingest | SEO Fundamentals: 3-page foundation layer
Ingested 20+ beginner's guide sources on technical SEO, keyword research, and content optimization
(official material from Google Search Central, Ahrefs, and general SEO industry guides). Created new
subsection [[framework/seo-fundamentals/]] as a separate "theoretical foundations" tier—distinct from
tactical pages to clarify that these are reference/conceptual knowledge, not action items. Created
three new pages: (1) [[framework/seo-fundamentals/technical-seo.md]] — crawlability, indexability,
ranking signals, Core Web Vitals; (2) [[framework/seo-fundamentals/keyword-research.md]] — search
volume, intent, difficulty, tools, keyword research process; (3) [[framework/seo-fundamentals/content-optimization.md]]
— relevance, authority, structure, SEO copywriting, content depth. Each page clearly marks itself
as theoretical foundation and cross-links to related tactical pages for practical application.
Updated [[index.md]] to add new Foundations section and explain the distinction. Rationale: tactical
pages focus on "rank a client's site for a keyword"; foundations answer "why does that work?" Keeping
them separate preserves the operational/reference distinction and prevents wiki dilution when new
tactical calls arrive.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[framework/seo-fundamentals/keyword-research.md]],
[[framework/seo-fundamentals/content-optimization.md]], [[index.md]], [[log.md]]

## 2026-09-28 | query | Upwork proposal for a plumbing-GBP job (cross-wiki request)
A separate Upwork-pitching wiki (C:\Projects\llm-wiki-upwork) asked me to redraft a mock
job pitch ("Local SEO for Plumbing Business," Dallas TX, GBP not ranking for "emergency
plumber Dallas") using this wiki's framework knowledge. Synthesized from
[[framework/local-seo-checklist.md]] (GBP verification-as-gate, GBP checklist items,
schema requirements), [[framework/on-site-seo.md]] (location-page structure recipe —
answer in the first ~50 words), [[framework/ai-overviews-local-search.md]] (AI Overviews
now sit above the map pack for local-intent queries), and [[framework/client-selection-filters.md]]
(confirms plumbing/local services is a niche where SEO is genuinely the ranking lever).
No new client or gap found — existing framework pages already covered this well, so
nothing new was written here. The synthesized pitch itself was written into the other
wiki's `pipeline/2026-09-23-mock-plumbing-dallas.md`, not into this wiki.
Pages touched: [[log.md]] (read-only query against existing framework pages; none modified)

## 2026-09-29 | query + ingest | Flat FAQ text vs. accordion FAQs
User asked why FAQ answers should be flat/visible on the page rather than collapsed in an
accordion. Checked `wiki/index.md` and searched all framework pages — no existing page covered
this. Also checked the two new unfiled clippings sitting at repo root (`Clippings/How to Write
Title Tags for SEO.md`, `Clippings/Small moves no moves (website updates)...md`) — neither
touches FAQ formatting, so no raw source to cite. Answered from general SEO/AI-answer-engine
knowledge (AI/LLM crawlers extract passages from static/rendered HTML; JS-injected-on-click
accordion answers may not exist in the DOM to extract; CSS-only accordions are safer but visible
text is still more reliably picked up for snippets/PAA). User asked to file it, so it was added
to [[framework/seo-fundamentals/content-optimization.md]] under Step 6 (AI Citations) as a new
"FAQ Formatting: Flat vs. Accordion" subsection, explicitly flagged as unsourced/agent-synthesized
per the traceability rule (no `raw/` file backs this claim yet). Also added a checklist line.
Note: the two Clippings files remain un-ingested — not yet moved into `raw/framework/` or filed
into the wiki; flagging for a future ingest pass if the user wants them processed.
Pages touched: [[framework/seo-fundamentals/content-optimization.md]], [[log.md]]

## 2026-09-29 | ingest | 4 new sources: Title Tags, Sitemap QA, Small Moves, Google Maps Prospecting
Ingested 4 new sources covering title-tag fundamentals, pre-launch technical validation, iteration
mindset, and local client prospecting. (1) Created [[framework/seo-fundamentals/title-tags.md]] from
Ahrefs guide on title-tag best practices: keyword placement, length (50–60 chars), CTR impact, common
mistakes across 1M+ domains, process for optimizing. (2) Created [[framework/microsite-launch-checklist.md]]
from real case study (Day 37 Longueuil French-drain site): pre-launch checklist covering infrastructure
(domain/hostname verification, sitemap validation, canonical tags), content & schema, performance,
mobile, GSC setup, GBP alignment, security, analytics, and final launch steps. (3) Enhanced [[framework/on-site-seo.md]]
with sidebar "Small Moves > No Moves" emphasizing iteration over waiting for perfect redesigns; real
example of law firm owner: 1 year of planning shelved → 2 one-hour sessions → qualified leads. (4) Expanded
[[framework/sales-and-lead-generation.md]] with new Approach #4: Google Maps prospecting—finding
businesses with SEO/marketing gaps (reviews, website, local SEO, schema) before they post jobs;
outreach process with real phone scripts; monetization options (retainer, lead share, microsite);
success signals from community (82yo parent closing audits daily, 4 closures in 1 week). Updated
[[framework/seo-fundamentals/]] reference in [[index.md]] to add title-tags; updated [[on-site-seo.md]]
and [[sales-and-lead-generation.md]] sources and descriptions.
Pages touched: [[framework/seo-fundamentals/title-tags.md]], [[framework/microsite-launch-checklist.md]],
[[framework/on-site-seo.md]], [[framework/sales-and-lead-generation.md]], [[index.md]], [[log.md]]

## 2026-10-02 | ingest | 3 new sources: 20 Q&As, Bryan's case study, Web 2.0 vendors
Ingested 3 sources covering community Q&As, real microsite execution, and citation vendor guidance.
(1) Created [[framework/microsite-qa-reference.md]] from "We Answered Every Question You Asked This Week"
community Q&A, capturing 20 practical questions organized by topic: keyword research (zero volume
myth, tool accuracy, product testing, vertical vs. geography), domain setup (EMDs, domain selection,
design consistency), GBP (buying profiles, categories over reviews, keyword names), backlinks (quality
over volume, niche fit), getting started (build first positioning, non-technical approach). Each answer
is field-tested and includes key insights. (2) Enhanced [[framework/external-seo-microsite-tactics.md]]
with "Case Study: Building a Real Microsite" (launchwithbryan.com, New Jersey): <$200 setup (incorporated
business + 50 citations), 400+ pages indexed, 3-step funnel (free offer → GBP education → CRM VSL),
11-email sequence feeding YouTube channel, key insight = the list is the real asset, not the free offer.
(3) Expanded [[framework/citations-strategy.md]] with two new sections: "Web 2.0 & Foundational Links"
(what they are, where to find them on Fiverr using "foundational links" search, vetting vendors via Ahrefs,
cost $20–$100, warnings about PBN farms); "Brave Browser Citations" (why Brave matters since Claude uses
it, manual URL submission process, no cost but adds AI visibility). Updated sources and timestamps for
both pages. Updated [[index.md]] with new page entry and enhanced descriptions.
Pages touched: [[framework/microsite-qa-reference.md]], [[framework/external-seo-microsite-tactics.md]],
[[framework/citations-strategy.md]], [[index.md]], [[log.md]]

## 2026-10-01 | query | Ahrefs "homepage flagged as orphan page" question
User asked whether a homepage flagged as "orphaned" in Ahrefs Site Audit needs internal links. Answered
that yes, homepages should receive internal links structurally (logo/nav), but confirmed this specific
Ahrefs flag is almost always a false positive — Ahrefs' crawler starts at the homepage/sitemap, so its
orphan-detection doesn't count the homepage as "discovered via a link" the way it does other pages.
Gave a 3-step verification process (check logo/nav uses real `<a href>`, cross-check GSC Internal Links
report, confirm homepage is in sitemap with correct canonical). Filed as a new subsection in
[[framework/seo-fundamentals/technical-seo.md]] under Crawlability (general reasoning, not sourced from
a raw capture — flagged inline per the no-unsourced-claims convention). Updated [[index.md]] one-liner.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[index.md]], [[log.md]]

## 2026-10-01 | query + ingest | Legal page outranking service page (noindex fix)
User described a site-review finding (no client onboarded for this site; one-off review like the mold
remediation case): `/complaints-policy` was the site's best/only result for 7 hyperlocal commercial
terms, outranking the actual service pages (`/residential-sewer-line-repair` #55, `/pipe-relining` #54).
User proposed noindexing the complaints, disclaimer, terms, privacy, and accessibility pages. Confirmed
this is correct but incomplete — noindex (`noindex, follow`, not robots.txt disallow) removes the false
competitor but doesn't fix the root cause: likely internal-link anchor text pointing at the policy page
instead of the service pages, plus weak content/entity signals on the service pages themselves (a #54-55
rank is a real content gap, not just cannibalization). Filed as a new "Diagnostic Pattern" section in
[[framework/on-site-seo.md]] (general reasoning, not raw-sourced — flagged inline per convention) with
the full fix sequence: noindex → redirect anchor text → rebuild service pages against the content recipe
→ request GSC re-crawl → monitor 2-4 weeks. Updated [[index.md]] one-liner.
Pages touched: [[framework/on-site-seo.md]], [[index.md]], [[log.md]]

## 2026-10-01 | query + ingest | Ahrefs "Canonical from HTTP to HTTPS" — real issue vs. noise, verified live
Follow-up to the homepage-orphan question. User asked about another Ahrefs flag: "Canonical from HTTP to
HTTPS." Explained this one is usually a *real* (if minor) issue, not noise like the orphan flag — it means
the HTTP URL is still live (`200`) and relying on the canonical tag alone instead of a server-level 301
redirect. User's PowerShell `curl -I` failed because `curl` is aliased to `Invoke-WebRequest` there, which
doesn't support `-I` the same way. Ran `curl.exe -I` directly against
http://moldremediationgettysburgpa.org/ (same site as the 2026-09-25 one-off review) and confirmed: `200 OK`
directly on HTTP, no redirect, canonical tag present pointing to HTTPS — real issue, Cloudflare not
configured to force HTTPS at the edge. Filed as a companion "Tool Quirk (Real This Time)" subsection in
[[framework/seo-fundamentals/technical-seo.md]] right after the orphan-homepage note: real-vs-noise triage
steps, the live verified example, the Cloudflare "Always Use HTTPS" fix, the HTTPS→HTTP reverse-direction
warning, and a PowerShell `curl.exe` note. Updated [[index.md]] one-liner.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[index.md]], [[log.md]]

## 2026-10-01 | query + ingest | HSTS sub-options (Max-Age, includeSubDomains, Preload, No-Sniff)
Follow-up to the Cloudflare "Always Use HTTPS" fix above. User asked if HSTS needs other options.
Explained Cloudflare's HSTS panel sub-options: Max-Age (start 6mo, bump to 12mo later — don't max out on
day one), includeSubDomains (only safe if every subdomain supports HTTPS — no quick undo once cached),
Preload (leave off for most client sites — months to remove once browsers pick it up, only worth it for
sensitive-data sites), No-Sniff (safe to leave on, unrelated to HTTPS). Gave a 5-step safe rollout order.
Expanded step 2 of the Cloudflare fix in [[framework/seo-fundamentals/technical-seo.md]] with this
breakdown. Updated [[index.md]] one-liner.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[index.md]], [[log.md]]

## 2026-10-01 | query + ingest | How "Canonical from HTTP to HTTPS" affects rankings
Follow-up to the Cloudflare fix + HSTS sections above. User asked how the HTTP-200-with-canonical-only
issue actually affects Google rankings. Explained it's not an active penalty (canonical tag usually
respected as a safety net) but several small, unforced leaks: duplicate-content dilution if Google ever
indexes the HTTP duplicate anyway, crawl budget waste crawling both versions, backlink equity leakage if
any external link points to the http:// version (canonical only *requests* consolidation, a 301
*guarantees* it), and CTR/trust hit if anyone lands directly on the insecure URL. Added a "Does this
actually hurt rankings?" subsection to the same Canonical HTTP→HTTPS section in
[[framework/seo-fundamentals/technical-seo.md]]. Updated [[index.md]] one-liner.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[index.md]], [[log.md]]

## 2026-10-02 | query + ingest | Is having a www version of the site up and running important?
User asked whether the www version of a site needs to be "up and running." Explained this is the same
canonicalization/duplicate-content problem as the HTTP-to-HTTPS case already documented, just applied
to www vs. non-www hostnames instead: Google doesn't prefer either version, but one must be canonical
and the other must 301-redirect into it (not sit unconfigured or 404). Walked through the curl-based
real-vs-harmless check, the Cloudflare redirect-rule fix (separate from the Always-Use-HTTPS toggle),
DNS requirements for the non-canonical hostname, canonical tag alignment, and GSC property verification
(already referenced in the launch checklist). Added a new "www vs. non-www: Same Canonicalization
Problem, Different Pair" subsection to [[framework/seo-fundamentals/technical-seo.md]], directly after
the existing Canonical HTTP→HTTPS section, following the same structure (check / real example framing
/ fix / ranking-impact / bottom line). Updated frontmatter `updated` date and `sources_note`, and the
[[index.md]] one-liner.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[index.md]], [[log.md]]

## 2026-10-02 | query + ingest | How important is the No-Sniff header (X-Content-Type-Options: nosniff)
Follow-up to the HSTS sub-options note. User asked how important the No-Sniff header is. Explained it's
a security-hardening header (prevents MIME-sniffing XSS where a mislabeled uploaded file could get
reinterpreted as executable script/HTML), not a ranking signal, with zero risk/effort to enable and
most relevant to sites accepting user uploads (barely applies to a static microsite with no uploads) —
leave it on regardless since it's free. Expanded the one-line No-Sniff bullet (within the existing HSTS
sub-options list, under the Canonical HTTP→HTTPS section) in
[[framework/seo-fundamentals/technical-seo.md]] into this fuller explainer. Updated [[index.md]]
one-liner.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[index.md]], [[log.md]]

## 2026-10-07 | ingest | Directory strategy + Q&A refresh + microsite contest findings
Created [[framework/directory-strategy.md]] (new page) covering directories as distinct from microsites:
authority hubs, force multipliers, low PBN risk. Included two sources: Vincent's careertrainingpath.com
case study (28 days live, 7,114 pages indexed, 485 clicks, built with Claude Code, Link-Flywheel for
automated outreach) and Community Call #56 demo (Directory Blueprint: 1,500 listings in 45 min–1.5 hrs
for <$100; monetization via featured listings $95–$200/year, "best XYZ" articles, sales outreach;
DataForSEO for data sourcing; AI vs. real photos for images; PBN risk assessment). Updated
[[framework/microsite-qa-reference.md]] with: 14 new Q&As from Oct 22 Q&A batch (timeline
expectations, Search Console strategy, service scoping, business reuse, phone/GBP handling, doorway
pages, international search, anti-spam updates, WhatConverts manual review, Upwork experience);
and Microsite Contest Day 22 case study (winning strategy: ~50 pages + 15 matching profiles across
trusted platforms, stable homepage, built once and left alone; current leaderboard: 1st place at
mold #10/radon #22, 2nd place at mold #22/radon #34). Updated [[index.md]] with directory-strategy
entry and enhanced microsite-qa-reference description.
Pages touched: [[framework/directory-strategy.md]] (new), [[framework/microsite-qa-reference.md]], [[index.md]], [[log.md]]

## 2026-10-08 | ingest | Parasite List framework + LLM citation sources + vendor pricing benchmark
Ingested 6 new raw sources (5 CSVs + 1 comment-thread markdown, "Public_Parasite_list_v3" series,
Aug 2026 citations) into [[framework/citations-strategy.md]] as new sections, per user's choice to
merge rather than create a new page. Added: "The Parasite List Framework" (102 platforms across 17
categories, tagged by 4 strategy types — Seedable/Listing/Review-driven/Earned — with rank-potential
highlights); "LLM Citation Sources" (Tier-1 media outlets LLMs cite, tiered by probability: Forbes
Councils/HARO/PR Newswire as highest-ROI targets, NYT/WSJ/Bloomberg as low-probability/high-authority);
"Document-Hosting Parasites" (DA-ranked doc hosts: Google Drive, Scribd, SlideShare, etc.); "Vendor
Pricing Reference" (summarized, not full list, per user's choice — two price tiers from a captured
vendor list, ~260 sites, with the caution that a meaningful share of "high DA" sites showed Non-Indexed
at capture time, reinforcing the existing Hunter Lord validation-step guidance); "Execution Playbook"
(5 community tactics: vendor diversification by platform type, anchor-text mix, YouTube embeds in
parasite articles, content-type diversification, Writer's Brief for vendors). Updated frontmatter
sources list, [[index.md]] one-liner, and this log entry. Confirmed via `git status`/`git log` that
the Oct 7 ingest (directory-strategy.md, microsite-qa-reference.md updates) was already committed
(commits 8ca5c67 and 5cb0780) before starting this ingest — avoided re-doing completed work.
Pages touched: [[framework/citations-strategy.md]], [[index.md]], [[log.md]]

## 2026-10-08 | query + ingest | Ranking URL flapping between FAQ page and township page (keyword cannibalization)
User reported, for `moldremediationgettysburgpa.org` (same one-off-reviewed site as the 2026-09-25
and 2026-10-01 entries — not formally onboarded as a tracked client), that the ranking URL for one
query had switched daily all week between the FAQ page and a township page, with position moving
every time it flipped. Diagnosed as keyword cannibalization distinct from the existing legal-page-
outranking pattern: here Google has two of the site's own pages (FAQ + township) both plausibly
answering the same hyperlocal query and hasn't settled on one, with the weaker page dragging average
position down whenever it wins the swap. Fix sequence: pick the township page as the one true target
for hyperlocal queries, de-duplicate/trim the overlapping FAQ entry, consolidate internal link anchor
text onto the township page, prefer content differentiation over canonicalizing the FAQ page away,
strengthen the township page's entity/schema signals per the Content Structure Recipe, confirm via
GSC URL Inspection's Google-selected-canonical, then monitor 2–4 weeks. Filed as a new "Diagnostic
Pattern: Ranking URL Flapping Between Two Pages" section in [[framework/on-site-seo.md]] (general
reasoning, not raw-sourced — flagged inline per convention), sibling to the existing legal-page
diagnostic. Updated [[index.md]] one-liner.
Pages touched: [[framework/on-site-seo.md]], [[index.md]], [[log.md]]

## 2026-10-08 | query | Correction — FAQ page linked only from footer, no specific township was given
Follow-up to the ranking-URL-flapping entry above. Two corrections from the user: (1) the FAQ page on
the site in question is linked sitewide only from a generic footer link ("FAQ" anchor text) — no
township-specific internal link is actually pointing at it, so step 3 of the fix ("consolidate
internal links") as originally written doesn't apply; the cannibalization must be driven by on-page
content/schema overlap, not link signals. Revised that step in [[framework/on-site-seo.md]] to check
whether the lever applies before doing it, and added a new step checking whether the overlapping Q&A
carries `FAQPage` schema — if so, that structured-data markup is likely the dominant signal pulling
Google toward the FAQ page, independent of links. (2) Clarified that no specific township was actually
named in the original query — `[Township]` in the diagnostic is a placeholder, not a real value pulled
from this conversation; the site identity (`moldremediationgettysburgpa.org`) was inferred only from
matching the user's local folder name to prior one-off review sessions (2026-09-25, 2026-10-01), not
from new raw data. No real township/URL has been supplied yet to audit directly.
Pages touched: [[framework/on-site-seo.md]], [[log.md]]

## 2026-10-08 | query | Recommended implementation: move overlapping FAQ to township page as small FAQPage-marked-up section
Follow-up to the two entries above. User asked whether the township-specific question causing the
overlap should move to the township page as a small FAQ section with its own `FAQPage` markup.
Confirmed yes, and connected it to two existing pages rather than treating it as a new idea: (1) it
executes steps 2 and 4 of the ranking-URL-flapping diagnostic (removes the duplicate content, moves
the structured-data signal onto the correct page) in one action; (2) it satisfies the existing
hub-and-spoke requirement in [[framework/external-seo-microsite-tactics.md]] ("Single-Location Ranking
+ Surrounding Location Pages") that spoke/township pages need genuine hyperlocal content, not
templated copy, to earn their keep — a real local FAQ block is a low-effort way to add that. Added a
"Recommended implementation" paragraph to the end of the Diagnostic Pattern section in
[[framework/on-site-seo.md]], cross-linking to the hub-and-spoke section and to the FAQ-formatting
flat-vs-accordion guidance in [[framework/seo-fundamentals/content-optimization.md]] (keep the new
block short, flat text, server-rendered if collapsed). No raw source backs this synthesis — flagged
inline per convention.
Pages touched: [[framework/on-site-seo.md]], [[log.md]]

## 2026-10-08 | query + ingest | Formalized permanent content-ownership rule: location-page FAQs vs. sitewide FAQ page
Follow-up to the three entries above. User asked whether every township page should permanently have
its own FAQ section, not just as a one-time fix for the overlap that caused the ranking-URL flapping.
Answered yes — and pointed out this isn't a new policy, it's enforcing something already in the
Structure Template section of [[framework/on-site-seo.md]] (step 9, "FAQ: 5-6 questions specific to
service + location") that wasn't being followed consistently, which is how the overlap happened in the
first place. Formalized an explicit content-ownership rule in the Structure Template section: location/
township pages permanently own all location-specific questions; the sitewide FAQ page is scoped to
universal, non-location questions only; location-page FAQs must be genuinely local, not templated copy
with the town name swapped (cross-linked to the hub-and-spoke requirement in
[[framework/external-seo-microsite-tactics.md]]). Cross-referenced this rule from the Diagnostic
Pattern's "Recommended implementation" note and the Implementation Checklist. Updated [[index.md]]
one-liner. No raw source backs this synthesis — flagged inline per convention.
Pages touched: [[framework/on-site-seo.md]], [[index.md]], [[log.md]]

## 2026-10-08 | ingest | Onboarded new client: tipicita-kinesio (Le Bouscat relocation analysis)
User asked for an analysis of tipicita-kinesio.com — Emmanuelle Mesnard, kinésiologue + coach de vie,
recently moved from Eysines/Mérignac to Le Bouscat (19 Aug 2026). No raw client material existed yet,
so performed a fresh capture: live fetch of all 9 core pages + sitemap/robots.txt + raw HTML
title/meta/JSON-LD, plus web search for GBP/directory/competitor signals. Saved as
[[raw/clients/tipicita-kinesio/site-crawl-2026-10-08.md]]. Full onboarding per AGENTS.md §7: created
profile, keyword map, 3 competitor pages (Marion Reynaud, Aude Coué, Nina Peret — all clustered on/near
the same Le Bouscat street), and recommendations. Key findings: (1) homepage's LocalBusiness JSON-LD
schema is stale — still declares the old Eysines address, directly contradicting visible page content;
(2) the location page (/ou-me-trouver) has zero structured data despite being the most location-relevant
page; (3) a third-party citation (lesmedecinesdouces.fr) still lists the old Eysines address and is
still actively aggregating reviews under it; (4) homepage title/meta don't mention Le Bouscat at all,
unlike the flagship service page and location page which are already correctly updated; (5) the practice
already ranks #1 for "coach de vie le bouscat" (thin competition) but faces 4-5 established, well-reviewed
competitors for "kinésiologue le bouscat" (denser competition, one with ~70 reviews vs. Tipicita's ~40).
Flagged that GBP dashboard, Search Console, and a full citation/backlink audit weren't accessible with
available tools — listed as open items for the client to provide. Updated index.md with new clients/
section.
Pages touched: [[clients/tipicita-kinesio/profile.md]], [[clients/tipicita-kinesio/keywords.md]], [[clients/tipicita-kinesio/competitors/mr-kinesiologue.md]], [[clients/tipicita-kinesio/competitors/aude-coue.md]], [[clients/tipicita-kinesio/competitors/bonjourlebonheur-nina-peret.md]], [[clients/tipicita-kinesio/recommendations.md]], [[index.md]], [[log.md]]

## 2026-10-08 | query | Turned tipicita-kinesio recommendations into a phased 90-day plan
User asked to turn the recommendations into an actionable 90-day plan. Synthesized the 12
recommendations in [[clients/tipicita-kinesio/recommendations.md]] into a new dated execution
tracker, [[clients/tipicita-kinesio/90-day-plan.md]], with 4 phases: Wk1-2 NAP/schema fixes (stale
homepage LocalBusiness schema, GBP address/merge audit, stale lesmedecinesdouces.fr citation) → Wk3-6
on-page location signals + easy schema wins (homepage title/meta, FAQPage schema on /ou-me-trouver,
Review/AggregateRating schema on testimonials) → Wk7-10 content build-out (Caudéran/Bruges paragraphs,
one net-new Le Bouscat-anchored blog post, review-velocity push) → Wk11-13 measure (GSC/live-rank
re-check, full citation audit, GBP insights review). Each task has an owner (Em/Dev/SEO), effort
estimate, and traces back to the specific recommendation number it implements. Added a Day-90 success
criteria checklist and a closing instruction to ingest Week 11-13 results back into recommendations.md
and keywords.md once the plan completes. Updated index.md one-liner.
Pages touched: [[clients/tipicita-kinesio/90-day-plan.md]], [[index.md]], [[log.md]]

## 2026-10-09 | query + ingest | Correction: `Organization`/`sameAs` schema does NOT need to repeat on every page
During a `sameAs`/OpenGraph correctness review of `moldremediationgettysburgpa.org` (same
one-off-reviewed site as prior entries — not a tracked client), incorrectly told the user that
Google parses each page's JSON-LD in isolation and therefore `sameAs` (declared only in the
`Organization` node on the home page) provided no entity-verification benefit on the other 28
pages, recommending it be duplicated onto every page's `LocalBusiness` node. User pushed back
("are u sure?"). Fetched Google's own structured-data documentation
(https://developers.google.com/search/docs/appearance/structured-data/organization) to check
rather than defend the claim from memory, and it says the opposite: *"We recommend placing this
information on your home page, or a single page that describes your organization... You don't
need to include it on every page of your site."* Retracted the recommendation to the user.
Root cause of the error: over-applying a heuristic that's true for per-URL rich-result schema
(e.g. `FAQPage`, which must appear on the specific page to produce a result for that URL) to
`Organization`/`sameAs`, which is a brand-level entity-disambiguation signal Google computes by
crawling the site as a whole, not a per-page rich-result eligibility check. The site's existing
implementation (sameAs once, home-page `Organization` node only) was already correct and needed
no change. Filed the corrected rule, with the Google doc link as direct inline citation, in a new
subsection of [[framework/seo-fundamentals/technical-seo.md]] ("Organization/sameAs placement:
homepage only, not every page"), explicitly distinguishing it from `LocalBusiness`/NAP schema
(which does correctly repeat per page/location page — not the same case). Also corrected the
pre-existing, ambiguously-worded instruction in [[framework/getting-cited-by-ai.md]] Move #2
("Add all social profiles to website pages with sameAs schema") that could be read the same
wrong way, pointing it at the new placement rule instead. Updated frontmatter `sources`
(added the Google doc URL as an external, dated source — exception to the usual raw/-only
convention, justified since this is an authoritative primary source directly cited inline) and
`updated` dates on both pages, and the [[index.md]] one-liners.
Pages touched: [[framework/seo-fundamentals/technical-seo.md]], [[framework/getting-cited-by-ai.md]], [[index.md]], [[log.md]]

## 2026-10-09 | ingest | ChatGPT Query Fanout Analyzer bookmarklet (jcchouinard.com)
User supplied the setup link for the "ChatGPT Bookmarklet Tool" that
[[framework/fan-out-queries-and-ais.md]] Method 1 had referenced only vaguely
("see raw sources for setup link," which pointed nowhere concrete) — closing a
gap flagged in the prior turn's answer about DataForSEO/bookmarklet mechanics.
Saved the full page (including complete bookmarklet JS source, captured
verbatim per the raw/ immutability rule) to
`raw/framework/ChatGPT Query Fanout Analyzer (Bookmarklet) - JC Chouinard.md`.
Rewrote Method 1 in [[framework/fan-out-queries-and-ais.md]] with concrete
setup steps (add as a browser bookmarklet), per-query usage (open a ChatGPT
conversation, click bookmarklet, get a dashboard of fan-out queries +
citations), how it technically works (reads the conversation ID from the URL,
calls ChatGPT's own `/backend-api/conversation/{id}` endpoint with the user's
session token — no external server/tracking), and its key limitation
(one conversation at a time, not an aggregation tool — DataForSEO is still the
only automatable/aggregating option across many queries). Also updated
[[framework/getting-cited-by-ai.md]] Move #1 to cross-reference this as the
free per-query alternative to DataForSEO. Updated `sources` and `updated` on
both wiki pages and the [[index.md]] one-liners.
Pages touched: [[framework/fan-out-queries-and-ais.md]], [[framework/getting-cited-by-ai.md]], [[index.md]], [[log.md]]

## 2026-10-10 | ingest | Perplexity troubleshooting guide + bookmarklet extraction walkthrough
Added detailed troubleshooting guide from Perplexity (complete Network tab walkthrough for extracting
`search_model_queries` and `safe_urls` from ChatGPT's backend conversation endpoint) and two screenshots
showing the actual capture process. User successfully extracted a real `search_model_queries` block
containing the query: "best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites"
and confirmed that ChatGPT's conversation endpoint delivers both query metadata and source-URL data,
even when the current bookmarklet parser does not extract them. Saved:
`raw/framework/How to see fan-out queries in ChatGPT - written by Perplexity on Oct 10, 2026.md`
(full Perplexity chat transcript with step-by-step Network debugging), `Pasted image 20261010085447.png`
(Network tab screenshot with 107 requests visible), `Pasted image 20261010085748.png`
(conversation JSON response showing the `search_model_queries` and `safe_urls` structures). Updated
`sources` frontmatter on both [[framework/fan-out-queries-and-ais.md]] and
[[framework/getting-cited-by-ai.md]] to include these new raw files, and set `updated` to 2026-10-10.
These sources provide the complete technical foundation for how to manually extract fan-out query
metadata and citations from ChatGPT when needed (e.g., single-query or exploratory analysis before
committing to DataForSEO for scale).
Pages touched: [[framework/fan-out-queries-and-ais.md]], [[framework/getting-cited-by-ai.md]], [[log.md]]

## 2026-10-10 | deprecation notice | Bookmarklet approach no longer working; redirect to manual Network tab method
ChatGPT updates to message structure broke the "ChatGPT Query Fanout Analyzer" bookmarklet's parser. While the
bookmarklet source code is preserved in raw/ (per immutability), Method 1 in [[framework/fan-out-queries-and-ais.md]]
is now flagged as "Deprecated (as of Oct 10, 2026)" and rewritten to center on the manual Network tab extraction
process outlined in the Perplexity troubleshooting guide. The manual method works because it directly inspects
ChatGPT's `/backend-api/conversation/{id}` response without parsing assumptions — just search the JSON for
`search_model_queries` and `safe_urls`. Updated [[framework/fan-out-queries-and-ais.md]] with: (1) new Method 1
(manual Network tab, with link to Perplexity's full walkthrough), (2) deprecated Method 1 section explaining
why the bookmarklet no longer works. The underlying extraction mechanism (calling the backend endpoint) remains
valid; only the parser layer broke.
Pages touched: [[framework/fan-out-queries-and-ais.md]], [[log.md]]

## 2026-10-12 | ingest + clarification | GBP creation strategy (Blair's off-record methods)
Created [[framework/gbp-creation-strategy.md]] from Blair's off-record note on two GBP creation methods:
(1) Create via Google Maps UI yourself (for real local businesses missing from Maps, AND for your own
microsites that can't get GBPs otherwise — but use sparingly to avoid burning your Local Person rating);
(2) Clone an existing high-review business with your own address (faster but riskier, works via 2-minute
phone-number change window before Google locks; risky at scale). Clarified per user's feedback that
Method 1 should be used both for real businesses AND for microsites (when necessary), but sparingly —
your Local Person rating on Google Maps is a finite asset that shouldn't be over-used. Page includes
detailed cautions against abuse (mass-creating profiles across 20+ microsites burns your trust rating),
best practices, comparison table, and strategic use cases distinguishing (a) legitimate one-off business
gaps, (b) occasional microsite GBP creation (using up some trust), vs. (c) mass microsite scaling
(don't do this). Moved source file from `raw/` root to `raw/framework/` for proper organization. Updated
[[index.md]] with entry for the new page.
Pages touched: [[framework/gbp-creation-strategy.md]], [[index.md]], [[log.md]]

## 2026-10-12 | ingest | Parasite platform ranking data (real contest results, Oct 12)
Created [[framework/parasite-ranking-data.md]] from microsite contest data showing which parasite/citation
platforms actually ranked in top-50 search results (Tier 1: 27 platforms) vs. which contestants built but
never ranked (Tier 2: 25+ platforms). Tier 1 includes Facebook, Clutch, Houzz, BBB, Manta, YouTube,
press releases, Pinterest, MapQuest, etc. Tier 2 includes LinkedIn company pages, Medium, Substack, Yelp,
TikTok, Reddit, Quora, WordPress.com, Weebly, etc. — surprisingly, many high-DA platforms didn't rank.
Page includes: (1) both tiers with platform type/notes, (2) common ranking factors observed (identical
business name/NAP everywhere, sameAs schema linking, built early + left alone), (3) comparison with the
earlier Parasite List Framework to show the difference between "how to use" categories and "actual ranking
potential" tiers, (4) practical implications for citation strategy, (5) open questions (why Yelp didn't
rank, why press releases did, etc.). This provides empirical validation/contradiction of the earlier
parasite platform taxonomy. Updated [[index.md]] with entry and link to [[citations-strategy.md]] for
the theoretical framework comparison.
Pages touched: [[framework/parasite-ranking-data.md]] (new), [[index.md]], [[log.md]]

## 2026-10-13 | ingest | Multi-tier distribution network case study + video automation stack
Created [[framework/multi-tier-distribution-network.md]] from Bryan Collins' detailed case study of a 4-tier
SEO automation system: Tier 1 (Foundation: Medium + LinkedIn long-form), Tier 2 (Amplification: rotation
across LinkedIn/Notion/YouTube/Artifacts), Tier 3 (Conversion: .repair and .dev error-checker microsites
with triple monetization), Tier 4 (Core: mrgrid.io main site). System publishes 240 pieces of content over
30 days (8/day) across 9 platforms using Claude Sonnet 4 + OpenAI adaptation + Replit automation. Day 1
proof: 102 indexed pages across 5 domains, 3 revenue streams live (direct sales $7–$29, affiliate SNOW
$22 CPA, multi-offer landing pages), fully automated. Detailed keyword strategy example ("PDF Corrupted"
base + 20 modifiers = 20 articles). Key insight: error-solver niche (different from local services) +
multi-platform distribution + affiliate monetization. Also added Stack #12 (Video Automation) to
[[framework/ai-tool-stacks.md]]: Claude → HeyGen API avatars → Gamma slides → ElevenLabs voiceover →
Camtasia sync → YouTube auto-publish → Replit-generated Pinterest pins. Results: 85 creatives scheduled,
12 YouTube Shorts, 3 long-form videos. Moved both raw sources to raw/framework/ for consistent organization.
Updated [[index.md]] with entries for both pages.
Pages touched: [[framework/multi-tier-distribution-network.md]] (new), [[framework/ai-tool-stacks.md]], [[index.md]], [[log.md]]

## 2026-10-13 | query + ingest | Primary-location page is a cannibalization bug - verified live, filed as explicit rule
During code review of two sibling website-launchpad microsite builds (Sewer-Line-Repair-San-Diego-CA
and Sewer-Line-Repair-Portland-OR - one-off reviews, not onboarded as tracked wiki clients), found that
the San Diego build correctly never created a dedicated page for its own primary location (homepage
owns 'Sewer Line Repair in San Diego, CA'), while the Portland build initially shipped
/sewer-line-repair-in-portland-or with an H1 identical to the homepage's, indexable, listed in the
sitemap, and linked from the Service Areas page's town list - direct keyword cannibalization of the
homepage's head term. User fixed it by deleting the page and the list entry. When asked where the
existing wiki rule for this lived, found only the adjacent-but-not-explicit hub-and-spoke guidance in
[[framework/external-seo-microsite-tactics.md]] ('keep the main page as the hub' for *surrounding*
towns) - no line explicitly forbidding a primary-location page existed yet. User then asked a follow-up
design question (option A: omit primary location from all town lists entirely vs. option B: keep it
in nav/Service-Areas/nearby-areas lists but link to the home page instead of a dedicated page) and
chose option B. Confirmed B is sound: it satisfies the existing 'each city page must link back to the
main page' hub-and-spoke requirement with on-topic anchor text, and is better UX than omitting the
primary city once 10+ surrounding towns are listed - with one caveat (don't self-link the primary
location if the home page renders its own inline copy of the same town list). Added a new 'Don't Build
a Separate Page for the Primary Location' subsection to
[[framework/external-seo-microsite-tactics.md]] codifying: never build a /service-in-[primary-city]
page; keep the primary location in visible town lists pointing at '/'; omit/de-link it only on the home
page's own inline copy of the list; areaServed schema should include it regardless. Sourced inline to
the live verification on both builds (flagged per the no-unsourced-claims convention, since this is
general SEO reasoning + live verification rather than a raw framework capture). Updated [[index.md]]
one-liner.
Pages touched: [[framework/external-seo-microsite-tactics.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Onboarded new client: groupe-nova (technical SEO + GBP + NAP audit)
User asked for a local SEO analysis of groupenova.ca — Groupe Nova, residential
renovation general contractor (kitchen/bathroom/basement/design) serving Montreal,
Laval, the North Shore, the South Shore, Montérégie, and Lanaudière — covering
technical SEO, GBP optimization, and NAP consistency. No raw client material
existed yet, so performed a fresh capture: live fetch of the homepage, 4 service
pages, portfolio, about page, robots.txt, and full wp-sitemap.xml tree (FR + EN)
via HTTP, raw HTML `<head>`/body inspection for title/meta/canonical/hreflang/
schema, plus web search cross-referencing a Google Places–mirroring aggregator
against the live site's Trustindex review widget. Saved as
[[raw/clients/groupe-nova/site-crawl-and-gbp-check-2026-10-19.md]]. Created
profile, keyword map, and recommendations per AGENTS.md §7. Key findings: (1)
**NAP mismatch** — the website's address (4388 Rue Saint-Denis #200, Montreal)
and phone (514-701-9898) don't match the connected Google Business Profile
(7657 Rue Montbrun, Saint-Léonard; +1 438-866-6682), confirmed same profile via
identical review text/reviewer names on both; (2) the website's address is
independently confirmed (Yelp + a commercial leasing listing) to be a third-party
coworking space ("Montréal Cowork"), not a Groupe Nova office — a GBP-guideline
risk if ever synced; (3) homepage `<title>` is literally "Groupe Nova" with zero
service/location keyword — the single biggest on-page gap on the site's highest-
authority URL; (4) zero meta descriptions and zero JSON-LD structured data found
on any of 11 pages checked; (5) duplicate-homepage URLs confirmed via the site's
own sitemap (`/` + `/accueil/`, `/en/` + `/en/home/` each serve the same content
as separate indexable URLs); (6) the site's strongest local-proof content — 6
homepage project photos and 56 portfolio before/after images, each already
captioned with a specific town (Laval, Brossard, Île-des-Sœurs, Blainville,
Montréal) — has empty or meaningless auto-generated alt text sitewide, so none
of that location signal is machine-readable; (7) the footer's service-area list
("Rive-Nord"/"Rive-Sud") doesn't name-match the client's stated target areas
("Laval," "Montérégie") despite having real completed-project proof in both.
Flagged GBP dashboard login, Search Console, a full citation sweep, and real
Core Web Vitals data as open items the client/user needs to provide directly.
Updated [[index.md]] with new clients/ section.
Pages touched: [[clients/groupe-nova/profile.md]], [[clients/groupe-nova/keywords.md]], [[clients/groupe-nova/recommendations.md]], [[index.md]], [[log.md]]

## 2026-10-19 | query + ingest | Correction: groupe-nova P0 NAP/GBP finding was overconfident and partly wrong
User asked to review the prior groupe-nova findings for correctness. Re-verified
the P0 NAP/GBP claim (website vs. "GBP" address mismatch) with additional web
searches and direct fetches, since it was the single highest-stakes, lowest-
certainty claim in the original pass (inferred from a third-party aggregator,
not a GBP dashboard login). Found two real problems: (1) the alternate address
(7657 Rue Montbrun, Saint-Léonard) was asserted as "the current GBP" but its
source's newest review is dated October 2023 — a ~3-year-stale cached snapshot,
not confirmed live GBP data; the original write-up overstated currency/
confidence. (2) A better, previously-missed data point existed: the website's
own printed RBQ licence number (5881-0540-01) is tied, per an independently
and recently verified (2026-08-26) licence-citing directory, to a *third*,
different address (1-8925 Avenue Millen, Montreal — "9562-0605 Québec inc."),
making this a genuine first-party self-inconsistency (the website disagreeing
with itself) rather than a speculative third-party cross-check — a stronger
finding than the one originally foregrounded. Also confirmed via
ProfileCanada.com (explicitly names "Groupe Nova" + links `www.groupenova.ca`)
that the Rue Montbrun address really is tied to this business at some point,
under yet another RBQ number (5797-3208-01, a different numbered company) —
so there are now 3 addresses in the picture, not 2, each with different
confidence/currency. One search-synthesis artifact was caught and excluded
during this process (a directory snippet appeared to tie "Groupe Nova" wording
directly to the Avenue Millen listing, but reading the full source page showed
that text belonged to a neighboring, unrelated directory entry). Separately
re-verified the lower-stakes technical findings (meta descriptions, JSON-LD,
duplicate homepage) with fresh, permissive/case-insensitive re-parsing of newly
re-fetched raw HTML — these all held up unchanged. Saved the full verification
trail as
[[raw/clients/groupe-nova/nap-verification-followup-2026-10-19.md]] (raw/ is
append-only — did not edit the original capture file). Rewrote P0 #1-2 in
[[clients/groupe-nova/recommendations.md]] with an inline correction note and
the corrected 3-address table, and updated the address caveat in
[[clients/groupe-nova/profile.md]]. Updated `sources` frontmatter on both pages
to include the new raw file.
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/profile.md]], [[log.md]]

## 2026-10-19 | query | Turned groupe-nova recommendations into a 4-week execution plan
User asked for 3-4 week milestones with priorities and hour estimates. Synthesized
the 15 recommendations in [[clients/groupe-nova/recommendations.md]] (as corrected
earlier the same day) into [[clients/groupe-nova/4-week-plan.md]]: Week 1 - NAP/
citation audit + request GBP access + homepage title/duplicate-homepage fixes (no
GBP-access dependency, 7.5h) -> Week 2 - GBP dashboard optimization (category,
display name, service areas, photos, Q&A) once access confirmed + service-page
metadata (9h) -> Week 3 - LocalBusiness/Service/Review schema + portfolio/homepage
image alt text + service-area wording reconciliation (9h) -> Week 4 - review-
request system, GBP posting cadence, HSTS, image compression, schema validation,
client wrap-up (8.5h). ~34 hours total. Each task cites its source recommendation
number for traceability. Added a Day-30 success-criteria checklist and an explicit
stop-and-re-ingest instruction if the Week 1 citation audit contradicts the
3-address NAP picture documented in recommendations.md. Updated [[index.md]].
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[index.md]], [[log.md]]

## 2026-10-19 | query + ingest | Correction: 4-week-plan.md had a sequencing bug, a schema-placement miss, a citation gap, and a mischaracterized source
User asked to review the 4-week plan for accuracy. Re-verified the hour arithmetic
(recomputed independently — original totals were correct: 7.5+9+9+8.5=34) and the
Rec# citations against the actual recommendations.md text, and found 4 real
issues. (1) **Sequencing bug**: Week 1's original Task 3 bundled "decide SAB
conversion" with "remove the coworking address," but rec P0 #2 explicitly says
the SAB decision needs GBP dashboard confirmation first — and Week 1 only
*requests* GBP access, doesn't guarantee it arrives in time. Split into a Week 1
task (remove the confirmed-false address only — safe now, independently
confirmed via Yelp/commercial-listing data, doesn't need GBP) and a new Week 2
task (decide + finalize the correct address once GBP/citation-audit results are
in). (2) **Schema-placement miss**: the plan had `Service` schema bundled onto
the homepage only; per this wiki's own existing technical-seo.md guidance
(`Organization`/`sameAs` is homepage-only, but per-item rich-result schema like
`FAQPage` must live on the specific page), `Service` schema for 4 distinct
services should live on each service page individually. Split into a homepage
`LocalBusiness`/`Organization` task (2h, reduced from 3h) plus a new per-service-
page `Service` schema task (1h) — net neutral on Week 3's total. Updated rec #9
in recommendations.md to state this explicitly. (3) **Citation gap**: Week 2's
About/Portfolio title+meta task cited only "P1 #7" (meta descriptions) because
rec #6 was scoped only to the 4 named service pages, leaving the title-rewrite
portion uncited — extended rec #6 in recommendations.md to explicitly cover
`/a-propos/` and `/realisations/` too (the raw capture's own title table already
listed both as generic). (4) **Mischaracterized source**: the companion raw file
`nap-verification-followup-2026-10-19.md` claimed the 5797-3208-01/9394-3199
Québec inc. RBQ pairing came from "a direct fetch" of the licence page — it
didn't; my direct WebFetch attempt to that URL was Cloudflare-blocked, and the
actual data came from a search engine's own cached snippet in an earlier call.
Corrected the attribution in that file (same risk category as the snippet
artifact already caught/excluded there, though the data's specificity makes
hallucination unlikely). Net effect: plan total moved from 34h to 34.5h (Week 1
7.5h->7h, Week 2 9h->10h, Week 3 unchanged at 9h). Updated
[[clients/groupe-nova/4-week-plan.md]], [[clients/groupe-nova/recommendations.md]]
(rec #6 and #9 text), [[raw/clients/groupe-nova/nap-verification-followup-2026-10-19.md]],
and [[index.md]].
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[clients/groupe-nova/recommendations.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Client confirmed Rue Saint-Denis IS the real GBP address — P0 NAP finding retracted and narrowed
User stated directly that 4388 Rue Saint-Denis #200, Montreal — the address
the two prior passes had investigated as a possible NAP mismatch/coworking-
space risk — is in fact the real, correct address on Groupe Nova's Google
Business Profile. Client-provided ground truth outranks every public/
third-party source used in the two prior investigation passes, so this
retracts the core claim of the original P0 finding (that this address was
"wrong" or needed removal/SAB conversion). Rewrote P0 in
[[clients/groupe-nova/recommendations.md]] (renumbered 1-5, was 1-4) to: (1)
retract the mismatch/removal claim for Rue Saint-Denis, keeping only a
lower-priority "confirm shared-office GBP requirements" check; (2) reframe
the Saint-Léonard listing (7657 Rue Montbrun, same 6 reviews as the site's
widget but all dated 2022-2023) as now most likely a stale/duplicate GBP
listing needing a merge-or-close action, not evidence of a live address
conflict — same pattern as the tipicita-kinesio precedent; (3) de-prioritize
(not drop) the RBQ-licence-address discrepancy (Avenue Millen) as likely a
legal/registration address distinct from the public NAP, since RBQ
registration and GBP/citation NAP aren't required to match. Renumbered all
downstream P1 (now 6-12, was 5-11) and P2 (now 13-16, was 12-15) items and
fixed every internal cross-reference. Updated the address caveat in
[[clients/groupe-nova/profile.md]]. Rewrote
[[clients/groupe-nova/4-week-plan.md]]: Week 1's "remove the address" task
became a quick informational client-check (3 -> 0.5h), Week 2's "decide
correct address" task became "search for and merge/close the Saint-Léonard
duplicate" (1h), and all Rec# citations were updated to match the new
numbering. New grand total: 34h (was 34.5h) — Week 1 now 6.5h (was 7h), all
other weeks unchanged. Updated [[index.md]] one-liners for both pages.
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/profile.md]], [[clients/groupe-nova/4-week-plan.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Client provided live GBP screenshot — NAP fully screenshot-verified, review count corrected from 6 to 11
Client supplied a screenshot of the live Google Maps listing for "GROUPE NOVA"
(saved to [[raw/clients/groupe-nova/assets/gbp-live-maps-screenshot-2026-10-19.jpg]],
documented in new raw file
[[raw/clients/groupe-nova/gbp-live-screenshot-note-2026-10-19.md]]). This is
the strongest evidence tier in the engagement so far — a direct visual of the
live profile, not a third-party aggregator or search-snippet. It confirms
name, address (4388 Rue Saint-Denis #200, Montreal, QC H2J 2L1), phone
(514-701-9898), website, category (General contractor), and hours all match
the site exactly, fully closing out the address question from the prior two
entries. It also surfaces a correction: the live listing shows **11 reviews**,
not the 6 the earlier (stale, 2022-2023-dated) aggregator snapshot showed.
Updated [[clients/groupe-nova/recommendations.md]]: strengthened the P0 #1
correction note to cite the screenshot, dropped the now-unnecessary "confirm
shared-office requirements" caveat since the live listing shows no sign of a
problem, corrected the review-count figure in the GBP-optimization rec
(still recommending a review-velocity push, just from a more accurate
baseline), and added a note to the Saint-Léonard duplicate rec (P0 #2)
that the screenshot is an encouraging but non-conclusive data point since
that Maps search wasn't targeted at the Saint-Léonard area. Updated
[[clients/groupe-nova/profile.md]] reputation line (6 -> 11 reviews) and
address line (now screenshot-confirmed, not just client-stated). No change
to [[clients/groupe-nova/4-week-plan.md]] — none of its hour estimates or
task scopes depended on the exact review count or needed the dropped caveat.
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/profile.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Broadened scope to website URL fixes + content depth; rewrote 4-week-plan at a more generic level
User asked to broaden the plan beyond NAP/GBP/metadata to also cover website
URL fixes (service-name URLs, a reported broken
`/en/services-2/interior-design-services/` page) and content depth (location
pages, more text on existing pages), rewrite the milestones more generically
(less task-by-task detail), and update estimates. Before writing
recommendations, verified the new claims directly: curled the reported broken
URL (returns HTTP 200, correct title, correctly linked from the English nav —
doesn't match "broken," flagged for client clarification rather than taken at
face value); sampled stripped body text of `/services/renovation-de-cuisine/`
to confirm the content-depth gap is real (unique copy per service page is one
intro paragraph + one 4-item bullet list + one 4-step process graphic + one
closing paragraph, beyond the reused reviews-widget boilerplate); confirmed
via the existing sitemap data that no dedicated location landing pages exist
anywhere on the site. Captured all of this in new raw file
[[raw/clients/groupe-nova/url-structure-and-content-depth-check-2026-10-19.md]].
Added items 17-20 to [[clients/groupe-nova/recommendations.md]] under a new
"Website structure fixes and content depth" section (not renumbering the
existing 1-16 to avoid breaking every existing citation): #17 URL `-2` slug
cleanup, #18 investigate-before-fixing the reported broken page, #19 build
location landing pages for Laval/Montérégie first (real project proof already
exists there) then the remaining 3 areas, #20 expand thin page copy with
FAQ/location-specific content. Fully rewrote
[[clients/groupe-nova/4-week-plan.md]] at a more generic milestone level —
collapsed the prior ~22 numbered sub-tasks into 4-5 bullet themes per week —
and updated the total from ~34h to **~53h** to reflect the two new production
workstreams (location pages, expanded copy), distributed as Wk1 9h / Wk2 10h /
Wk3 18h / Wk4 16h. Updated [[index.md]] one-liners for both pages. Also
delivered the milestones to the user as a plain-text, copy-paste-ready block
per the standing action-plan-output rule and the user's explicit request (no
markdown, brackets, or internal links in that chat-facing version — full
detail/links stay in the wiki page only).
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/4-week-plan.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Broken page claim CONFIRMED and root-caused via live browser check — correction to the previous entry
The previous entry's conclusion on the reported broken
`/en/services-2/interior-design-services/` page ("doesn't match broken, flag
for client clarification") was wrong — it was based on a `curl` fetch, which
only sees raw HTML and can't see client-side rendering. The user then provided
a screenshot of the actual broken render, prompting a live browser
investigation (navigation, accessibility snapshots, screenshots, and CDP
`Runtime.evaluate` calls). Confirmed and root-caused: this page's phone-number
country-code selector loads already expanded (244-country dropdown open by
default) instead of collapsed like every other page's equivalent field, and
that open list visually buries the hero image, heading, and body copy beneath
it — the content is present in the DOM, just pushed down the page behind an
unwanted, fully-expanded country picker. Reproduced on two independent fresh
loads. Explicitly re-checked English kitchen-renovation, English
bathroom-renovation, the English homepage, and French renovation-de-cuisine —
all render correctly, so this is isolated to one page, not a site-wide outage.
Also found a related issue: the site's "Get your free quote" popup shows the
same stuck-open phone-selector behavior in at least one instance, suggesting a
shared root cause in the phone-input widget. Captured the full investigation
in new raw file
[[raw/clients/groupe-nova/interior-design-page-bug-confirmed-2026-10-19.md]].
Rewrote item #18 in [[clients/groupe-nova/recommendations.md]] to reflect the
confirmed bug and root cause, and promoted it to P0 (a dead lead-gen page),
relabeling the section header accordingly. Moved the fix to the top of Week 1
in [[clients/groupe-nova/4-week-plan.md]] and bumped the total from 53h to
54h. Updated [[index.md]]. This is a direct example of why a `curl`-only
technical check can miss real, user-facing bugs — client-side rendering
issues need an actual browser.
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/4-week-plan.md]], [[index.md]], [[log.md]]


## 2026-10-19 | lint | Retracted the "duplicate Saint-Leonard GBP" framing — Montbrun address was never seen on Google Maps
User asked where the 7657 Rue Montbrun / 438-866-6682 "GBP" came from, noting Google Maps shows only the Montreal listing. Traced it: it came from exa.ai's places-data mirror (assumed to be a Google listing because its 6 reviews matched the site's Trustindex widget) plus ProfileCanada, studio-lb.fr and aubaine.ca directory listings (see [[raw/clients/groupe-nova/nap-verification-followup-2026-10-19.md]]). It was never observed on Google Maps itself, so calling it a "GBP duplicate" overstated the evidence. Since the reviews are identical and the live listing now has 11 (a superset), the likelier explanation is the same GBP captured earlier with its old address/phone — i.e. stale third-party citations, not a second Google listing. Rewrote rec #2 in [[clients/groupe-nova/recommendations.md]] accordingly (verify reviewers match, one Maps search for a second listing, fold directory cleanup into the citation audit #5, escalate to a Google merge request only if a second listing is actually found). Updated [[clients/groupe-nova/4-week-plan.md]] (Week 1, Week 2, day-30 criteria) and [[clients/groupe-nova/profile.md]] to match; hours unchanged.
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/4-week-plan.md]], [[clients/groupe-nova/profile.md]], [[log.md]]

## 2026-10-19 | query | Re-scoped groupe-nova 4-week plan to the client's stated fixed-price scope
Client's initial scope: technical SEO audit and priority fixes, GBP optimization, business-info consistency across website/GBP/directories, keyword research for services and service areas, and a written report. Also stated that all website work is manual Elementor editing. Rewrote [[clients/groupe-nova/4-week-plan.md]]: added an explicit keyword-research task (~7h) and a written-report/walkthrough week (~9h in Week 4), raised per-edit estimates for manual Elementor work, and moved location landing pages and copy expansion (Rec #19, #20) out of the 4 weeks into an optional Phase 2 (~28h French, ~+14h English). New total ~53h (was ~54h). No changes to [[clients/groupe-nova/recommendations.md]] numbering.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | ingest | Re-verified old Montbrun address/phone listings; reordered plan (priority fixes first, keyword research to Week 4)
User asked to verify the "old Montbrun address/phone still listed" claim, its severity, and proof links. Fetched the pages directly: ProfileCanada and aubaine.ca both still show 7657 Rue Montbrun + 438-866-6682 today (both unclaimed, auto-generated, no reviews). exa.ai and studio-lb.fr are snippet-level only. New: a LinkedIn company page summary shows a third phone (514-929-1906) and postal code H1S 2K3 (unverified, login wall). Severity rated low-to-medium; open question for the client is whether 438-866-6682 is still a live number. Saved as [[raw/clients/groupe-nova/montbrun-citation-verification-2026-10-19.md]]; updated rec #2 in [[clients/groupe-nova/recommendations.md]]. Also reordered [[clients/groupe-nova/4-week-plan.md]]: broken pages, URL fixes, on-page SEO and GBP alignment now in Weeks 1-2, directories in Week 3, keyword research plus report in Week 4 (+2h refinement pass; total ~55h).
Pages touched: [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | query | Elaborated and re-verified the duplicate-homepage finding (rec #9)
User asked to elaborate on "Fix the duplicate homepage URLs". Re-fetched live: /, /accueil/, /en/, /en/home/ all 200 and self-canonical; hreflang only on the roots; duplicates still in the page sitemaps; no internal links to them from 4 pages sampled. Added the verification, severity (low-to-medium) and fix sequence to rec #9 in [[clients/groupe-nova/recommendations.md]]. No plan hours changed (still ~2h in Week 1).
Pages touched: [[clients/groupe-nova/recommendations.md]], [[log.md]]

## 2026-10-19 | query | Split keyword research in the groupe-nova plan (quick check Week 1, full research Week 4)
User questioned whether keyword research is truly priority #1; concluded it is not (broken page, title tags, GBP categories rank higher). Updated [[clients/groupe-nova/4-week-plan.md]]: added a ~2h Montreal wording check in Week 1 before titles are written, cut full Week 4 research from ~7h to ~5h. Week hours now 19 / 15 / 7 / 14; total unchanged at ~55h.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | query | Explained and re-verified the /services-2/ URL cleanup (rec #17)
User asked what the /services-2/ cleanup is and how important it is. Re-fetched live: all 5 EN service URLs return 200 and are in the EN nav; hreflang correct; /en/services/ 301s to the French /services/ page (the plain slug is held by the French page, which explains the -2). Rated importance low (P2); noted the rename needs a different English slug and a redirect check. Added to rec #17 in [[clients/groupe-nova/recommendations.md]]. Plan not yet changed (suggested moving it from Week 1 to Week 3).
Pages touched: [[clients/groupe-nova/recommendations.md]], [[log.md]]

## 2026-10-19 | query | Moved the English /services-2/ URL cleanup to Week 3
Per user: remove the /en/services/ -> French redirect and redirect /en/services-2/ to /en/services/; move the task to Week 3. Updated [[clients/groupe-nova/4-week-plan.md]] (task moved, ~3h; Week 3 now ~10h) and added the decision and open risk (same-slug-in-both-languages, and whether the redirect is a WordPress auto-guess) to rec #17 in [[clients/groupe-nova/recommendations.md]]. While editing, found the plan file had been hand-edited (a garbled title from a cut/paste, stray characters, and the master-record and broken-page estimates reduced to 1h each); cleaned the stray characters, kept the user's estimates, and recomputed the weekly totals: ~11 / 15 / 10 / 14 = ~50h.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[clients/groupe-nova/recommendations.md]], [[log.md]]

## 2026-10-19 | query | Elaborated author-archive and HSTS items (rec #11, #12); questioned Week 2 placement
User asked to elaborate on disabling author archives/sitemap entries and adding HSTS, and why they are in Week 2. Live check: author archive 200 and in both users sitemaps; /?author=1 redirects to /author/hector-fabio-009hotmail-ca/ (username looks email-derived); no Strict-Transport-Security header. Both rated low importance (not ranking factors); noted they do not meet the 'top priority in the first two weeks' bar and suggested moving them to Week 3. A direct read of /wp-json/wp/v2/users contents was blocked by auto-review and not pursued. Added findings to rec #11 and #12 in [[clients/groupe-nova/recommendations.md]]. Plan not yet changed.
Pages touched: [[clients/groupe-nova/recommendations.md]], [[log.md]]

## 2026-10-19 | query | Moved author-archive and HSTS items to ongoing maintenance
User asked whether rec #11 (author archives/sitemap) and #12 (HSTS) can be handled in ongoing maintenance. Yes: both are low-importance and neither is a ranking issue. Updated [[clients/groupe-nova/4-week-plan.md]]: removed the item from Week 2 (now ~13.5h), added an 'Ongoing maintenance' section (author archives ~1h, HSTS ~0.5h, plus the existing review growth/GBP posts/rank tracking items), and made the written report list them as low-priority remaining items. Plan total now ~48.5h. Caveat noted: the exposed email-like username is a small hygiene issue, so the report should flag it so it is not forgotten.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | query | Split review-request process (Week 2) from GBP posting plan (Week 4)
Per user: kept the review-request process early because review volume (11 reviews on the live GBP) is the main GBP opportunity and reviews take time to accumulate; moved the weekly posting plan to Week 4 so it can use the final keyword wording. Updated [[clients/groupe-nova/4-week-plan.md]]: Week 2 ~13h, Week 4 ~14.5h, total unchanged ~48.5h. Explained to the user how to set up the review-request process (rec #4 in [[clients/groupe-nova/recommendations.md]] has the 1-2 reviews/week target).
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | ingest | groupe-nova plan now uses the owner's own estimates (43h, ~$1,505)
User supplied their planning spreadsheet. Rewrote [[clients/groupe-nova/4-week-plan.md]] to match it: Week 1 15h (adds a 5h technical SEO audit row, 3h already spent), Week 2 8.5h, Week 3 8h, Week 4 11.5h, ongoing 0h; total 43h, about $1,505 (~$35/h). Key changes vs. the prior wiki estimates: GBP optimization 4h to 1h, structured data 3h to 2h, directory cleanup 5h to 4h, URL cleanup 3h to 2h, keyword research 5h to 4h, report 5h to 3h, duplicate homepage fix 2h to 0.5h. Flagged two open questions in the plan: the sheet has two Week 1 title/meta rewrite rows (3h and 2h; if the second replaces the first the total is 40h), and GBP optimization at 1h may be tight given the 20+ photos and Q&A in rec #4. Phase 2 estimates unchanged (not in the sheet). The sheet's author-archive/HSTS row is 0h ongoing.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | query | Moved GBP photos and Q&A to ongoing maintenance
Per user: the 20+ photo upload and Q&A pre-fill from rec #4 moved out of the fixed-price Week 2 GBP row into ongoing maintenance, which resolves the concern that 1h was tight. Updated [[clients/groupe-nova/4-week-plan.md]]; the 43h total is unchanged. Also suggested other candidates for ongoing (image compression, GBP posting plan, long-tail directories) pending the user's decision.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | query | Moved image compression, GBP posting plan and long-tail directories to ongoing
Per user: moved three low-priority items from the fixed-price weeks to ongoing maintenance in [[clients/groupe-nova/4-week-plan.md]]: image compression (rec #16, -0.5h from the Week 2 alt-text row, now 2.5h), the weekly GBP posting plan (rec #4, -0.5h in Week 4, row removed), and smaller scraped directories such as studio-lb.fr (rec #5, -0.5h from the Week 3 directory row, now 3.5h). Weeks now 15 / 8 / 7.5 / 11 = 41.5h (about $1,450 at ~$35/h); ongoing still not counted. The possible-duplicate-title-row scenario is now 38.5h.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | ingest | groupe-nova plan synced to the owner's updated spreadsheet (40.5h)
User supplied the updated sheet ('Group Nova estimates for first 2 weeks'). Synced [[clients/groupe-nova/4-week-plan.md]]: alt text 2.5h to 2h (Week 2 now 7.5h), main directory cleanup 3.5h to 3h (Week 3 now 7h); Weeks 1 and 4 unchanged (15h, 11h). Total 40.5h. The sheet prices it at $1,417.50 'estimated' ($35/h) and $1,300 in a 'real' column ($500 / $250 / $200 / $350 for Weeks 1-4). The sheet's two ongoing rows (author archives/HSTS, GBP posting plan) are 0h. Open items remain: the two Week 1 title/meta rows (if the second replaces the first the total is 37.5h), and the sheet's GBP row text still lists photos and Q&A although the plan moved them to ongoing.
Pages touched: [[clients/groupe-nova/4-week-plan.md]], [[log.md]]

## 2026-10-19 | ingest | Drafted the ongoing monthly support proposal for groupe-nova
User asked for volume, schedule, estimates and deliverables for ongoing monthly support after the audit (service page optimization, FR/EN content incl. local landing pages and blog, quality directory listings, ongoing GBP management, monthly reporting, and replacing CTA buttons with embedded forms). Created [[clients/groupe-nova/monthly-support.md]] (status: draft): unit estimates, a 6-month plan at ~20h/month (126.5h, ~$4,430 at the owner's ~$35/h), lean/recommended/full tiers, monthly rhythm, deliverables, and caveats. It absorbs the earlier optional Phase 2 and the 'ongoing' items parked in [[clients/groupe-nova/4-week-plan.md]]. Flagged that the embedded-forms idea depends on first fixing the country-code phone plugin behind the interior-design-page bug, and that real call counts need a call-tracking number added as a secondary GBP number. Also refreshed the stale 4-week-plan line in [[index.md]].
Pages touched: [[clients/groupe-nova/monthly-support.md]], [[index.md]], [[log.md]]

## 2026-10-19 | update | Reworked groupe-nova monthly support into the $600 x 3 months then $300 structure
Rewrote [[clients/groupe-nova/monthly-support.md]] (replacing the earlier ~20h/month six-month draft) using the owner's estimates sheet at $35/h: pricing structure, estimates table (sheet rows plus four assistant-added items, ~4.5h: tracking baseline, ad thank-you pages and conversion tags, image compression, extra ads reporting), a three-month plan at 51.2h ($1,792 of $1,800), the $300 ongoing plan, and elaborations on local landing pages, Montreal homepage optimization, GBP photo and Q&A additions (Q&A is posted from the public listing and may be reduced by Google), and separate Google Ads landing pages (6 regional pages, noindex, same domain). Added the Google Ads launch (Feb-March 2027) impact and the open client question on service areas (Montreal, Montreal East, West Island, North Shore, South Shore, Lanaudière; Laval/Montérégie unconfirmed). Flagged that the owner's per-page estimates are about a third of the earlier assistant estimates. Updated the matching line in [[index.md]].
Pages touched: [[clients/groupe-nova/monthly-support.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Reviewed changes since the last logged entry and folded the session's decisions into the groupe-nova pages
Review: the git working tree was clean and no file was newer than the previous log entry (the earlier work was already committed), so the new material was the owner's chat statements and estimates sheet that had not yet been saved to `raw/`. Saved them as [[raw/clients/groupe-nova/engagement-and-estimates-notes-2026-10-19.md]]: the retainer scope, the proposed pricing ($600/month for 3 months, then $300/month), the Google Ads plan (launch Feb-March 2027, separate landing pages, one per region), the owner's region list, and the final estimates sheet (12 rows). Updated [[clients/groupe-nova/profile.md]] (new next-phase and Google Ads section, plus the unreconciled service-area lists), [[clients/groupe-nova/keywords.md]] (new Montréal-Est / West Island row, no volume data), [[clients/groupe-nova/recommendations.md]] (update note on #19: location page names and separate noindex ad pages), [[clients/groupe-nova/4-week-plan.md]] (pointers from the Ongoing and Phase 2 sections to monthly-support.md), and [[clients/groupe-nova/monthly-support.md]] (source added). Correction: the region list the owner gave (Montreal, Montreal East, West Island, North Shore, South Shore, Lanaudière) is the website footer's own wording, not a new client statement; the earlier monthly-support wording implied otherwise and was fixed. Open items: the client has not yet been asked about the service-area list; the ads landing page estimates and the four assistant-added items in monthly-support.md are unverified.
Pages touched: [[clients/groupe-nova/profile.md]], [[clients/groupe-nova/keywords.md]], [[clients/groupe-nova/recommendations.md]], [[clients/groupe-nova/4-week-plan.md]], [[clients/groupe-nova/monthly-support.md]], [[index.md]], [[log.md]]

## 2026-10-19 | ingest | Ingested Calls #57–58, domain advice, and Bryan's content production workflow

Saved four raw sources to `raw/framework/`:
- Community Call 57 (Oct 15): AI credit optimization, Shawn's $350 directory (fal.ai image models), tiered link building (GSA/SEO Neo), radon contest niche assessment
- Community Call 58 (Oct 15): when backlinks matter (structure + semantics first, backlinks as fuel), YMYL licensing risks (financial/legal/insurance), flat-rate leasing retention strategy (Brandon: 25+ year clients, +$500/mo per location), engagement tactics (quiz forms, video production)
- Domain advice thread: .com taken → test competing TLD (hyphenated .com, .ca, .org); data from microsite contest shows position gains come from NAP + profiles + brand, not TLD
- Bryan's workflow (Oct 15): image posts via Claude Code + Pillow (no AI images, $0 cost), shorts via OpenArt Seedance 2.0 (~$17/mo for 16/month), 97% margin, reusable scripts

Distribution per user recommendation:

1. **[[wiki/framework/backlinks.md]]**: Added new section "When Backlinks Actually Matter" before "Why Backlinks Matter" (the foundational section). Moved sources timestamp to 2026-10-19. New content:
   - Backlinks are a function of competition, not default; structure + schema + NAP work first
   - Three-tier ladder: (1) Structure + semantics, (2) Citations + social profiles, (3) Backlink building
   - Competition test: 0–3 competitors = Tier 1+2 enough; 10+ = need Tier 3
   - Real example: Jacksonville carpenter ranking in AI Overviews from structure alone

2. **[[wiki/framework/niche-selection-strategy.md]]**: Added two new sections after the existing Domain Strategy section; updated sources timestamp to 2026-10-19:
   - "Domain Selection When .COM Is Taken": Niche is winnable if the .com is poorly-maintained or just a "coming soon" page; real test is whether you can make the brand name the keyword; three variant strategies (hyphenated .com, geo-TLD like .ca reordered, .org last resort); microsite contest data: no ranking gains from TLD alone, only from NAP + profiles + brand
   - "YMYL Niches & Licensing Requirements": High-risk categories (financial, insurance, legal, health); three safe approaches (work under existing license, build as lead-gen aggregator, skip entirely); real example (attorney niches: build relationship with largest firm, run test site "powered by" them at discounted per-lead rate); risk mitigation (disclaimers, separate entity, own attorney consult)

3. **[[wiki/framework/pricing-and-deal-structures.md]]**: Added new Play #12 "Flat-Rate Leasing for 25+ Year Client Retention" before the "Bottom Line" section; updated sources timestamp to 2026-10-19. New content:
   - Brandon's model: same flat rate all year; each new location/service adds ~$500/mo; no seasonal pricing
   - Why it works: long-term retention, effortless scaling, predictable revenue, less admin
   - Real example: 25+ year client started at 1 location, now scales to $5k–8k/mo after adding locations incrementally
   - Implementation: quote flat rate, set expectations, renew at same rate unless client requests additions
   - New closing line: "Build for 25-year relationships, not one-year contracts."

4. **[[wiki/framework/ai-tool-stacks.md]]**: Added new Stack #13 "Image Posts + Short Videos (Claude Code + OpenArt + Python)" before the "The Pattern" section; updated sources timestamp to 2026-10-19 and added Bryan's workflow to sources list. New content:
   - Part 1: Instagram image posts via Python/Pillow (5×5 grid, no AI images, $0 cost, client-approved)
   - One-time setup (15 min): Claude Code, Python, Pillow, ffmpeg, optional GoHighLevel
   - Workflow: client photos + design screenshot → Claude Code generates script → render 25 posts → client approval → schedule
   - Tweaking: plain-English edits to dark fade, headline breaks, photo swaps; Claude re-renders in seconds
   - Part 2: Short videos via OpenArt Seedance 2.0 (13–15 sec walkthrough + end card, 9:16 vertical)
   - Upload photos to OpenArt in order → generate with Seedance 2.0 → upscale + captions + end card in Claude Code → music from Pixabay
   - Numbers: standard way (all AI images) = ~$233/mo; Bryan's way = ~$17/mo for 16 shorts/mo
   - Margin: $600 client fee − $17 cost = $583/mo ≈ 97% margin (before Claude/GHL overhead)
   - Key rules: no AI people lookalikes, no unauthorized pricing/ratings/licensing, one video at a time in OpenArt, client approval before scheduling, GHL workflow for each "COMMENT" post

Updated [[wiki/log.md]] with this entry.
Pages touched: [[wiki/framework/backlinks.md]], [[wiki/framework/niche-selection-strategy.md]], [[wiki/framework/pricing-and-deal-structures.md]], [[wiki/framework/ai-tool-stacks.md]], [[wiki/log.md]]

## 2026-10-27 | query | Main service page cannibalizing microsite home page
User asked how to handle a microsite's main-service page (e.g. locksmithdurhamregion.ca/locksmith) cannibalizing the home page. Answered from the existing primary-location rule and filed a new subsection in [[framework/external-seo-microsite-tactics.md]]: the home page is the main service page; do not build /[service]; if it exists, merge unique content and 301 to /; spend pages on sub-services and non-primary towns. Index line updated.
Pages touched: [[framework/external-seo-microsite-tactics.md]], [[index.md]], [[log.md]]
