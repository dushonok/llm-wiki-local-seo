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
