---
type: framework
client: none
status: active
updated: 2026-11-20
sources:
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 0. Checklist for Local SEO (AI Overview Readiness) · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 1. Core Business Data (NAP Consistency) · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 2. Google Business Profile Optimization - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 3. Review Profile & Sentiment Signals - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 4. Structured Data (Schema) - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 5. Content & Entity Signals - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 6. Authority & Citations - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 7. Monitoring & Reporting - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/Local SEO Innovation - 2 - Local AI SEO Checklist - 8. Next Steps for Local AI SEO - Local SEO Innovation · AI SEO Rank Expand Academy.md"
  - "raw/framework/GBP ranking driving signals vs interactions on the listing - AI SEO Rank Expand Academy.md"
---

# Local SEO Checklist

Goal: Ensure a business's data ecosystem is robust enough to be included in Google's AI Overviews (not just to rank in Maps or organic).

## 1. Core Business Data (NAP Consistency)

**Objective:** Business information must match everywhere AI pulls from.

**Checklist:**
- ✅ Business Name, Address, and Phone Number are identical across:
  - Google Business Profile (GBP)
  - Website footer & contact page
  - Yelp, Angi, HomeAdvisor, BBB, Facebook, and local directories
- ✅ Primary category in GBP reflects main service (e.g., *Roofing Contractor*)
- ✅ Secondary categories cover other key services (e.g., *Siding Contractor*, *Gutter Installation*)
- ✅ Hours of operation, service areas, and contact info are current

**For service-area-only businesses (no customer-facing address):**
- ✅ Business Name and Phone Number are consistent across platforms
- ✅ Address is omitted from website footer (show only name + phone + service areas)
- ✅ Service areas (regions/territories/neighborhoods/ZIP codes) are listed consistently across **website copy, GBP service-area field, and LocalBusiness schema** — use the same terminology in all three places
- ⚠️ GBP is set up as "service area only" (not a location pin) — office address used for verification only, not displayed publicly
- See "Service-Area-Only Businesses" section in [`on-site-seo.md`](on-site-seo.md) for schema guidance and examples

## 2. Google Business Profile Optimization

**Objective:** Make GBP a "data source" for AI summaries.

> **Verification is the gate, not an optimization.** An unverified GBP has
> essentially no local SEO value: Google flags it "not publicly visible,"
> suppresses it from meaningful Map Pack / Local Pack placement, and blocks
> owner access to Insights, review responses, full edits, and Q&A control. It
> can still be scraped/found (see "GBP Gap Mining" in
> [Community Call 9](../../raw/framework/Community%20Call%209%20-%20🎙️%20The%20Call%20Vault%20·%20AI%20SEO%20Rank%20Expand%20Academy.md),
> lines 26–31 — unverified/missing GBPs are treated as prospecting targets,
> precisely because the business is capturing zero value from them), but for
> the business itself, claim + verify must happen **before** anything else in
> this checklist (photos, categories, posts, reviews) starts contributing to
> ranking or AI Overview inclusion. *Not sourced from a raw call — general
> GBP/SEO knowledge, flagged here for traceability.*

**Checklist:**
- ✅ Business description includes key services + location phrases naturally
- ✅ Every service is listed individually under *Services* tab
- ✅ Service area ZIP codes or neighborhoods added
- ✅ 20+ high-quality photos uploaded (before/after, team, trucks, etc.)
- ✅ Weekly post schedule maintained (project highlights, reviews, promos)
- ✅ Q&A section pre-filled with common customer questions and answers

## 3. Review Profile & Sentiment Signals

**Objective:** Build review volume, velocity, and sentiment that AI models trust.

**Checklist:**
- ✅ Maintain 4.7+ average rating across major platforms
- ✅ Target 1–2 new Google reviews weekly
- ✅ All reviews get personal response within 48 hours
- ✅ Negative reviews addressed professionally (demonstrates accountability)
- ✅ Customers encouraged to mention service type + location in reviews (helps AI link contextually)

## 4. Structured Data (Schema)

**Objective:** Help AI understand who you are, what you do, and where.

**Checklist:**
- ✅ Add `LocalBusiness` schema with:
  - Name, address, phone
  - `@type` (e.g., `RoofingContractor`)
  - Opening hours
  - Service area (`geoCoverage`, `areaServed`)
  - Aggregate rating (from reviews)
- ✅ Include `Service` schema for each core offering (Roof Repair, Gutter Cleaning, etc.)
- ✅ Validate all markup using Google's Rich Results Test

## 5. Content & Entity Signals

**Objective:** Prove local relevance through content AI can reference.

**Checklist:**
- ✅ Each location/service area has optimized landing page
- ✅ "Proof" content exists — project case studies, testimonials, gallery images with location captions
- ✅ Google Map embedded and internal link to GBP
- ✅ Blog covers local events, weather damage trends, seasonal issues in region
- ✅ Content mentions nearby landmarks, ZIP codes, towns to strengthen entity-based associations

## 6. Authority & Citations

**Objective:** Reinforce legitimacy across the web.

**Checklist:**
- ✅ Audit all citations quarterly using tools like BrightLocal or Whitespark
- ✅ Fix duplicates or outdated listings
- ✅ Build niche citations (RoofersGuild, NRCA, Home Services directories)
- ✅ Secure local backlinks (sponsorships, chamber of commerce, community events)

## 7. Monitoring & Reporting

**Objective:** Track visibility as a new KPI.

**Checklist:**
- ✅ Use GSC and incognito mode to monitor rankings
- ✅ Track impressions vs clicks to spot AI-caused CTR drops
- ✅ Log new reviews, Q&A activity, and post performance monthly
- ✅ Adjust on-page and GBP strategy every 90 days based on data

## Per-client application

This checklist gets applied and tracked per client in `wiki/clients/<slug>/recommendations.md` — this page stays generic as a reference framework.

---

# Next Steps by Skill Level

Use these implementation roadmaps based on current SEO maturity. Source: raw/framework/Local AI SEO Checklist - 8. Next Steps for Local AI SEO.

## 🟢 BEGINNER — New to Local SEO

**Goal:** Build a solid foundation so AI Overviews can even recognize your business.

**Immediate Actions:**

1. **Run a NAP audit**
   - Use Google Sheets to list every place your Name, Address, and Phone appear
   - Fix mismatches manually
   - Run these Google searches:
     - "Your Business Name" + "Address"
     - "Your Business Name" + "Phone"
     - "Your Business Name" + "City"
     - "Your Business Name" + "ZIP"
     - "Your Phone Number" (in multiple formats: (410) 555-8721, 410-555-8721, 4105558721)

2. **Claim or update your GBP** — Add all services, categories, and 20+ photos
3. **Ask for your first 10 reviews** — Text happy customers directly after jobs
4. **Add LocalBusiness schema** to your website
5. **Track baseline visibility** — Record rank, review count, GBP insights before/after
6. **Post weekly to GBP** — Highlight recent projects and reviews

## 🟡 INTERMEDIATE — Already Ranking Locally

**Goal:** Strengthen signals that make your business "trustworthy" in AI's knowledge graph.

**Actions to Strengthen Authority:**

1. **Audit structured data** — Add Service schema for each offering and validate it
2. **Expand citations** — Build 10–20 niche citations (NRCA, local chambers, directories)
3. **Entity-content push** — Publish 1–3 blog posts quarterly referencing local events, towns, or case studies
4. **Optimize review sentiment** — Reply to all reviews within 48 hours; encourage reviews mentioning service type + location
5. **Improve GBP engagement** — Add Q&A and 1 new GBP post weekly
6. **Integrate monitoring sheet** — Track GSC impressions, GBP calls, and review velocity
7. **Fix duplicate or outdated citations** — Run quarterly audits

### Map pack: driving signals vs. listing interactions (community, 2026)

**Context:** Local businesses (restaurant thread, but map-pack logic applies to trades) sometimes test **(A) simulated driving / GPS route signals** vs **(B) synthetic listing interactions** (search → profile → directions / call / photos).

**Do first (non-negotiable):**

- Website **categories and services match GBP** (names, scope, descriptions).
- Fill **GBP service descriptions** with context that links entity → site → intent.
- **NAP citations** aligned before chasing geo tricks.

Without alignment, "you can eat all you want—you still won't rank" (Cyril Garitey, REA thread).

**Review replies:** Automate or batch slowly—**suspension risk** can beat marginal gains (Jesse Cunningham). See [[grey-hat-tactics-and-risks.md]].

**Dissent in thread:** Cyril and **SEO NEO** proponents report route simulations work after GBP is right—treat as vendor/grey-zone only; see research counter below.

**Research counter (Michael Elliott, REA — local search / anomaly detection):** Fake drives and listing **CTR-style bots** are an **expensive trap**: possible **3–7 day flicker**, then rank snaps back after the tool stops or Google's **weekly filter sweep**. Spoofed devices (no real location history / Wi‑Fi handoffs) trigger **anomaly flags** → **manual video reverifications** and **weeks locked out of Maps**. Prefer the four levers below over paid signal tools.

**What to do instead (Elliott / live testing — adapt restaurant examples to any niche):**

| Lever | Restaurant example | Home-services transfer |
|-------|---------------------|-------------------------|
| **1. Visual scanner** | Real diner photos of dishes (e.g. QR on tables; ~20 real phone photos/week) — Google tags food visuals | Real **job-site / before-after photos** from customers and techs on GBP (not stock) |
| **2. Hard quantitative data** | Full menu: dish + **exact price**, portions, dietary tags; every native GBP attribute (patio, kids menu, etc.) | GBP **services** with scope and price bands where allowed; every applicable **attribute** filled; no vague "quality work" fluff |
| **3. Landmark anchoring** | On the site URL linked from GBP: directions via **highway exit, parking, cross streets, transit** to stretch spatial radius | Service-area / location pages with **local landmarks** and honest drive directions from known hubs |
| **4. Category stack** | Primary = highest-volume cuisine; **3–4 secondaries** (e.g. Pizza, Caterer, Wine Bar) for extra clusters without cannibalizing main | Primary = core trade; secondaries = logical sub-services (don't stack unrelated categories) |

**Default playbook:** pillars 1–4 in [[five-pillar-local-seo-framework.md]], §3 review velocity/sentiment here, citations—then measure in Insights before any paid geo or interaction service.

## 🔵 ADVANCED — Established SEO / Agencies

**Goal:** Future-proof your ecosystem for AI-driven retrieval and dynamic search changes.

**Strategic Initiatives:**

1. **Build multi-entity connections** — Interlink your GBP, site schema, YouTube, and social profiles using sameAs schema
2. **Implement structured reporting** — Use Looker Studio or Sheets to visualize AI Overview visibility changes (CTR drops, impressions, snippets)
3. **Deploy content clusters** — Create a semantic tree (Service → Subservice → Location → Proof assets)
4. **Automate monitoring** — Use DataForSEO or n8n to track reviews, post performance, and rank changes
5. **Conduct quarterly "AI Inclusion Audit"** — Check which GBP pages and site URLs are surfaced in AI summaries or map snippets
6. **Earn backlinks** from authoritative local or trade sources
7. **Refine tone for AI summaries** — Update business descriptions and schema text to sound concise, factual, and entity-rich (like a Wikipedia snippet)
