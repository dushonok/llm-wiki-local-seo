---
type: framework
client: none
status: active
updated: 2026-11-23
sources:
  - "raw/framework/Local SEO Playbook Combo of SEO Book, Schema, etc - Claude Code Building · AI SEO Rank Expand Academy.md"
---

# Local SEO Playbook (Maverick Method + REA stack)

**Purpose:** Single doctrine page — Jesse Cunningham's **Maverick Method** (from the SEO Master Class) fused with Rank Expand local, authority, content, technical, and AI-search layers. Use it as a **config file**: paste relevant sections (plus the master checklist at the end) into Claude Code / your build assistant so output matches community standards, not model defaults.

**Order of a job:** strategy → local → authority → content → technical → AI search → build → distribution → measurement.

**Related:** [[five-pillar-local-seo-framework.md]] (microsite contest pillars), [[on-site-seo.md]], [[directory-strategy.md]], [[citations-strategy.md]], [[ranking-in-ai-overviews-semantics.md]], [[getting-cited-by-ai.md]], [[seo-fundamentals/technical-seo.md]].

---

## 1. Non-negotiables (read first)

Rules that override convenience; most mystery ranking losses trace here.

- **LocalBusiness schema on the homepage only.** **Never AggregateRating on LocalBusiness.**
- **Single-hop 301s only** — map redirects before any DNS flip; 404 on a ranking URL = lost revenue.
- **FAQPage in expanded static HTML** — collapsed FAQs hide keyword-rich copy and may be skipped by AI crawlers.
- **No service × location pages** without enough genuinely unique content to justify indexing.
- **GBP primary category = #1 local lever** — treat as deliberate, seasonal (see §3).
- **Factual, non-promotional tone on spokes** earns AI citations; promotional tone is penalized. Spokes inform; money pages sell.

---

## 2. Maverick Method — five phases

Loop: **Motivation → Action → Validation → Expansion → Repeat.**

### Phase 1 — MOTIVATION

- Classify intent with **DEEPR** before committing a keyword: **D**ecision, **E**ntertainment, **E**ducation, **P**roblem-solving, **R**esearch. Strong pages hit 2–3. Score the current #1 with DEEPR; build where it's thin. Avoid pure competitor-brand purchase intent on new sites.
- **Gaps:** PAA (8–12 questions → headings/FAQs), forums/Reddit/Quora, reviews, DataForSEO for weak-SERP terms.
- **Winnable tier:** ladder from broad → specific; new sites win specific first (use **your** DataForSEO difficulty, not fixed DA bands).
- **Gear:** **Blanket** (~80%, templated, VA/AI-friendly) vs **Sniper** (data-driven one-offs around emerging winners).
- **Spreadsheet hubs:** **T1** spine (structure/authority), **T2** sub-categories, **T3** long-tail — tiers **fluid** per hub.
- **Gap content** (essential but too competitive to rank) and **Bridge content** (links loose hubs) both have roles.

### Phase 2 — ACTION

- **Slug** patterned in hub; **title** &lt;55 chars; **meta** &lt;155; one **H1**; H2/H3 = real searches.
- **First paragraph:** answer in ≤300 chars (snippet play) → reassurance → teaser.
- **Body:** 2–3 sentence chunks; tables/lists; credible **non-competitor** data (.gov, primary sources) with links to the passage.
- **Interlinking:** anchor = keyword variant; **upline/downline** every spoke links up and down the sheet (top wraps to bottom); every T2→T1, T3→T2; add natural links on top. Goal: Wikipedia-style graph back to home.
- **FAQ:** 7+ from PAA; ~300-char answers; **no yes/no openers**; internal links inside answers; expanded + FAQPage schema.

### Phase 3 — VALIDATION

Organic vs branded, rankings/position fluctuation (= Google undecided → strengthen page), CTR, GA4 engagement. Measure **hubs** via patterned slug filters; **n-gram check** in GSC (queries vs on-page phrasing).

### Phase 4 — EXPANSION

Fortify hub winner → avoid cannibalization → related keywords (drop branded/unnatural) → promote winner to T1, ring of T2s = moat.

### Phase 5 — REPEAT

Every quality page + on-point keyword = trust deposit.

---

## 3. Local SEO layer (beyond the book)

**Whitespark-aligned hierarchy:** **#1 primary category**, **#2 proximity**, **#3 keywords in business title**; **review recency** rising (~#11).

- **Seasonal category switching** (e.g. HVAC furnace vs AC) — document per vertical for VAs.
- **GBP Products** often beats Services visibility — use for service businesses too.
- **Physical address &gt; SAB** for rankings when possible; SAB only when address truly cannot show.
- **Driving-directions signal:** staff using Maps to the location can still help — weigh against [[local-seo-checklist.md]] map-pack section (fake GPS/tools = suspension risk).
- **Citation descriptions** with semantic triples across directories; one **canonical NAP** forever (St. vs Street, Suite vs Ste). Audit top 20–30 citation sources first.

---

## 4. Authority — "claim before you beg"

~80% of valuable local links exist as **unclaimed** listings (regulators, associations, supplier directories). Mine claims first; cold outreach last.

| Tier | Focus |
|------|--------|
| **0 — Entity glue** | Identical NAP/logo everywhere + **sameAs** on Organization schema (see [[seo-fundamentals/technical-seo.md]]) |
| **1 — Claim** | .gov + association "find a pro" directories |
| **2 — Relationship** | Supplier/vendor/preferred-contractor pages |
| **3 — Local** | Chambers, regional directories |
| **4 — Editorial (last)** | Press, HARO-style, podcasts |

**KPI:** track **qualified entities connected/month**, gated by DataForSEO DA/relevance — not raw backlink count.

**Phasing:** 0–30d site + schema + GBP + cluster + Tier 0–3 **claims** (20–30 citations if they're claims, not earned); 30–90d distribution; ongoing 2–5 qualified earned links/month.

**VA outreach pattern:** free PDF companion (expertise-led) with contextual link to service page — no paid/grey links.

**YMYL (e.g. insurance):** association/relationship lanes only; highest E-E-A-T bar.

---

## 5. Content production (workflow sketch)

- Audience + intent in AI first → titles filtered for SEO + hook → DataForSEO questions → stat/promise hook (not fictional story) → **Johnson Box** + **KeyTakeaway** before body → expanded FAQ; grade on content checklist.
- CTAs at defined scroll points; Grammarly/fact-check pass; **Article + FAQPage** JSON-LD; named bylines and first-hand callouts on YMYL.

Cluster builds use blueprint-style entity maps + [[on-site-seo.md]] / semantic authority patterns.

---

## 6. Technical & schema

Centralized validated JSON-LD — not per-page LLM guesses.

- LocalBusiness **homepage only**; no AggregateRating there.
- Article, FAQPage (expanded), Person on YMYL.
- **trailingSlash: never**; single-hop 301s; no thin service×location pages; CWV.
- **Original publish dates** on genuine legacy content: datePublished = original, dateModified = today — never fabricate.

---

## 7. AI search / GEO-AEO

Engines fan queries into sub-queries and retrieve at **passage** level → **clusters + tight internal links** beat one hero article. Factual spokes get cited before commercial pages. Tier 0 **sameAs** graph helps entity resolution — ties to [[getting-cited-by-ai.md]] and [[fan-out-queries-and-ais.md]].

---

## 8. Master build checklist (hand to AI)

**Research:** DEEPR + branded screen-out; 8–12 PAA; tier in spreadsheet; blanket vs sniper; DataForSEO rows.

**Build:** slug/title/meta/H-structure; snippet first graph; interlinks; 7+ FAQs (no yes/no); E-E-A-T byline/callouts.

**Local:** GBP category (+ seasonal plan); Products; canonical NAP; Tier 0 profiles + sameAs; baseline scan (e.g. Local Falcon).

**Technical:** schema rules above; canonicals/redirects; no thin loc×service pages; IndexNow / [[directory-strategy.md#step-7-index-with-omega-indexer|Omega]] where applicable.

**Authority & measure:** authority map; claims before outreach; GSC/GA4; hub slug filters; n-gram CTR; expansion around winners.

---

## Related Pages

- [[ai-reliability-and-context.md]] — Feed this playbook + client wiki into Claude via WikiLLM
- [[client-retention-strategies.md]] — Productized ongoing SEO / WaaS