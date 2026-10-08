# Wiki Index

Catalog of every page in this wiki, one line each. Update this whenever a page is
added or removed (see AGENTS.md §6, Ingest). Grouped by section.

## framework/seo-fundamentals/
**Theoretical foundations** — Conceptual knowledge about how SEO works. These are reference material that inform the tactical pages below, but are not action items themselves. Useful for onboarding, building mental models, and understanding *why* specific tactics matter.

- [technical-seo.md](framework/seo-fundamentals/technical-seo.md) — How search engines crawl, index, and rank; crawlability, indexability, ranking signals, Core Web Vitals; incl. Ahrefs "homepage flagged as orphan page" false-positive explainer + "Canonical from HTTP to HTTPS" real-vs-noise triage (Cloudflare "Always Use HTTPS" fix, HSTS rollout sub-options incl. No-Sniff/`X-Content-Type-Options` explainer, ranking-impact explainer) + www vs. non-www canonicalization (same redirect/backlink-consolidation logic as HTTP→HTTPS)
- [keyword-research.md](framework/seo-fundamentals/keyword-research.md) — What keyword research is; search volume, intent, difficulty, tools; keyword research process
- [content-optimization.md](framework/seo-fundamentals/content-optimization.md) — How to create content that ranks; relevance, authority, structure; SEO copywriting principles
- [title-tags.md](framework/seo-fundamentals/title-tags.md) — What title tags are; why they matter for ranking and CTR; best practices and common mistakes

## framework/
General SEO/local SEO knowledge, not tied to a client.

### Technical SEO & AI Optimization
- [on-site-seo.md](framework/on-site-seo.md) — Content structure recipe (title, lead-in, answer, H2s, entity signals) that ranks fast; incl. meta-description town-list/state-abbreviation guidance; sidebar on small moves vs. waiting for perfection; diagnostic pattern for legal/boilerplate page outranking the service page (noindex + anchor-text fix); diagnostic pattern for ranking-URL flapping between two of your own pages (keyword cannibalization — de-duplicate overlap, consolidate internal links, strengthen the correct page's signals)
- [microsite-launch-checklist.md](framework/microsite-launch-checklist.md) — Pre-launch validation checklist (domain, sitemap, canonicals, broken links, schema, mobile, GSC setup); real case study of sitemap domain error
- [backlinks.md](framework/backlinks.md) — Social media profiles (YouTube, Reddit, Instagram, Facebook, TikTok) as high-authority backlink sources; platform hierarchy by ROI; implementation process for 12-week backlink stack
- [ai-overviews-local-search.md](framework/ai-overviews-local-search.md) — How AI Overviews reshape local intent and visibility above map packs
- [local-seo-checklist.md](framework/local-seo-checklist.md) — 7-part checklist to optimize for AI Overviews + skill-level next steps (Beginner/Intermediate/Advanced)
- [getting-cited-by-ai.md](framework/getting-cited-by-ai.md) — 5 moves to get cited by ChatGPT/Gemini (invisible URLs, social mentions, listicles, expired domains, profiles page)
- [fan-out-queries-and-ais.md](framework/fan-out-queries-and-ais.md) — Why ranking for fan-out queries boosts AIO citations (0.77 correlation); topical authority strategy
- [external-seo-microsite-tactics.md](framework/external-seo-microsite-tactics.md) — 5 external SEO levers for fast-ranking microsites (expired-domain sponsorships, NAP citations, AI-citation targeting, listicles, social proof); citations process, VA delegation, location-page strategy; safe-vs-risky rebuild framework; real case study (launchwithbryan.com)
- [citations-strategy.md](framework/citations-strategy.md) — Citations spectrum (real NAP vs. created address vs. none); strategy by situation; Wikipedia opportunity engine; legal considerations; Web 2.0 vendors; Brave Browser submission for AI visibility; Parasite List framework (102 platforms tagged Seedable/Listing/Review-driven/Earned); LLM citation sources (Forbes/HARO/PR Newswire tiers); doc-hosting parasites; vendor pricing benchmark; diversification execution playbook
- [directory-strategy.md](framework/directory-strategy.md) — Directories as authority hubs and force multipliers (distinct from microsites); Vincent's careertrainingpath.com case study; Directory Blueprint demo; monetization ($95–$200/year per listing, featured placements, "best XYZ" articles); DataForSEO data sourcing; PBN risk (low for directories); Link-Flywheel automation; image strategy (AI vs. real photos)
- [microsite-qa-reference.md](framework/microsite-qa-reference.md) — 30+ common Q&As on building microsites (keyword research, domain selection, GBP strategy, citations, getting started, cost optimization, hosting); Oct 2026 batch (timeline, Search Console, services/scope, business reuse, selling, phone numbers, doorway pages, international search, anti-spam risk, manual review, experience); microsite contest Day 22 case study (winning strategy: ~50 pages + 15 matching profiles, stable homepage, leave alone)
- [ai-reliability-and-context.md](framework/ai-reliability-and-context.md) — Fixing context overload; multi-agent architecture (Paperclip); WikiLLM memory setup; guardrails + version control
- [open-graph-and-metadata.md](framework/open-graph-and-metadata.md) — OG tags aren't a ranking factor; low-priority polish for social CTR + AI/citation fallback

### Strategy & Operations
- [ai-tool-stacks.md](framework/ai-tool-stacks.md) — 11 practical AI/automation stacks (content generation, site building, lead capture, scaling) from community members
- [niche-selection-strategy.md](framework/niche-selection-strategy.md) — "Niches within niches" framework; 12-minute microsite builds; volume strategy; research-first mindset
- [agency-operations-scaling.md](framework/agency-operations-scaling.md) — Moving from solo doer to system operator; Loom training, boundaries, documentation for delegation
- [pricing-and-deal-structures.md](framework/pricing-and-deal-structures.md) — 11 pricing plays and deal structures (per-lead, retainers, stacking, contracts, hourly design)
- [client-selection-filters.md](framework/client-selection-filters.md) — 4 filters to pick clients that stick (expertise respect, review count, volume capacity, niche leverage)
- [sales-and-lead-generation.md](framework/sales-and-lead-generation.md) — 4 approaches to get clients: human touch, specific hooks, channel stacking, Google Maps prospecting (find businesses with SEO gaps before they post jobs)
- [client-retention-strategies.md](framework/client-retention-strategies.md) — Relationship strength, visible work proof, service intertwining for long-term retention

## clients/

_(none yet — see AGENTS.md §7 for how to onboard a client)_

<!--
Template for a new client block once one exists:

### <client-slug>
- [profile.md](clients/<client-slug>/profile.md) — one-line business summary
- [keywords.md](clients/<client-slug>/keywords.md) — one-line: # of keywords tracked, top priority
- competitors/
  - [<competitor-slug>.md](clients/<client-slug>/competitors/<competitor-slug>.md) — one-line takeaway
- [recommendations.md](clients/<client-slug>/recommendations.md) — one-line: top open recommendation
- microsites/
  - [<microsite-slug>.md](clients/<client-slug>/microsites/<microsite-slug>.md) — one-line: target keyword/location, status
-->
