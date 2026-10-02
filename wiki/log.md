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
