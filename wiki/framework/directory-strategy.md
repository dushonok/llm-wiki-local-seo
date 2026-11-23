---
type: framework
client: none
status: active
updated: 2026-11-23
sources:
  - "raw/framework/Directory Launched 28 Days Ago - 485 Clicks - AI SEO Rank Expand Academy.md"
  - "raw/framework/Community Call 56 - Directory Blueprint as Force Multiplier - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 1 ▶️ Start Here - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 2 Pick Your Vertical and Location - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 3 Buy Your Domain - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 4 Pull Your Listings - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 5📍 Get the Directory Blueprint - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 6 Build Your Directory - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/1st lead from directory -making money from directories - AI SEO Rank Expand Academy.md"
  - "raw/framework/First claim on my AI pool directory, under 2 weeks live - AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 8 Get It Indexed - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI Directories · 9 Get Paid - ☰ AI Directories · AI SEO Rank Expand Academy.md"
  - "raw/framework/community call 61 - Scaling AI SEO, Sticky Clients - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
---

# Directory Strategy

**Purpose:** Directories are a distinct strategy from microsites—they aggregate listings, serve as authority hubs, and act as a "force multiplier" for microsite portfolios without the PBN footprint risk of running multiple independent sites.

**Key insight:** A directory builds authority in one place, then distributes that authority down to your own microsites (and client sites) without the exposure of running standalone microsites alone.

---

## What Is a Directory (in Local SEO context)?

A directory is a searchable, schema-tagged collection of business listings in a niche or geography. Google trusts directory sites (they're a normal publisher activity), so listings inside directories rank easily, and the directory itself builds topical authority.

**Unlike microsites:**
- Microsites target specific keywords/locations with service-focused content
- Directories aggregate and organize listings (similar to Yelp, Houzz, Clutch, Crunchbase)

**Similar to microsites:**
- Can be built in ~45 minutes to 2 hours (end-to-end, including schema)
- Rank fast because Google recognizes the pattern
- Can be monetized immediately

**Scale framing (AI Directories Playbook):** A microsite is one service in one town. A directory is every business in one service across one state — state hub, city pages, business pages. Built from a Google Maps pull plus the **Directory Blueprint** (Claude Code). No WordPress, no plugin, no database: a folder of static files on free hosting; when data changes, you rebuild the folder.

---

## AI Directories Playbook: Nine-Step Path (Skool course)

**Reference build:** [floridacustompoolbuilders.com](https://floridacustompoolbuilders.com/) (demo state directory; fast on PageSpeed).

### Why build one (three revenue angles)

1. **Warm outreach list** — "You have a listing on my directory. Is it correct?" Often the highest-value outcome; warmer than generic cold SEO pitches.
2. **Vertical coverage** — Microsites in several cities plus one state directory = SERP coverage three ways. List your own microsites like any other business; **no cross-links between your sites**.
3. **Rent top spots** — Premium/featured/best-of placements; many small fees across hundreds of businesses.

**Sales infrastructure (Call #20):** Directories are not microsites — they are **outbound fuel**: branded search, phone-number queries, and "verify your listing" outreach to businesses with weak presence. Funnel verified listings into SEO/featured sales ([[sales-and-lead-generation.md#outbound-stack--buyer-reality-call-20]]).

### When *not* to start here

For similar money you could launch ~10 microsites. Build a directory when you **already own the vertical** or when you want the **call list**, not as a first site.

### Prerequisites

- Claude Code (Microsite Empire setup lesson if new)
- DataForSEO connected to **Claude Code** (not only claude.ai) for cheap listing pulls
- Node.js 20+ (Blueprint build step)

### Cost and timeline

| Item | Typical cost |
|------|----------------|
| Domain (.com at Cloudflare) | ~$10.44/year |
| Listings pull (DataForSEO) | Few dollars/state (e.g. FL pool contractors ~$0.89) |
| Listings pull (Outscraper) | $3/1k rows after 500 free; large states $60–$120 raw (most rows dropped in clean step) |
| Hosting | Free (Cloudflare Pages) |
| Indexing (Omega Indexer) | ~$60 for 800 credits (~1k URLs ~$75); tiered launch can cut first pass (e.g. ~584 URLs ~$44) |
| **First run total** | **Under ~$100 with DataForSEO; under ~$200 with Outscraper** (+ indexing credits) |
| **Ongoing** | ~$10/year domain |

**Time:** Weekend build (mostly Claude running). **Ranking curve:** Same as microsites — indexed month 1, Google settles ~month 3, trust ~month 6. One member: 166 → 887 indexed pages in ~30 days after Blueprint rebuild, with first leads and first "list me" request in the same window.

### Steps 1–9 (course order)

1. Pick vertical + state  
2. Buy domain  
3. Pull listings (DataForSEO via Blueprint in Gate 1, or Outscraper → `listings-raw.csv`)  
4. Enrich (Blueprint Gates 1–3: scope, clean, enrich)  
5. Build (Gates 4–5: plan, generate static site)  
6. Put online (deploy after Gate 5 live check; see **Step 6–7 launch rules** below)  
7. **Index** (Omega Indexer drip — lesson 8)  
8. **Get paid — outreach & claims** (lesson 9, §1–2)  
9. **Get paid — products & Stripe** (lesson 9, §3; rank-and-rent on city pages = later)

Live after step 6; **steps 7–9** are indexing + revenue work.

### Step 6–7 launch rules (lean sitemap)

Do not dump every built URL into the index on day one—Google may index a slice and ignore the rest.

- **In sitemap at launch:** home, state, every city/town page, **strong** business pages.
- **Built but `noindex` at launch:** thin business pages (e.g. under five reviews and/or no description). They still render, interlink, and show **"claim this listing."**
- **Widen later:** claimed listings first, then by review count (`Widen the sitemap` in Claude → re-run Gate 5 → upload). Example from course testing: ~**1,100 / ~1,700** pages in the first sitemap tranche.
- URL list order lives in **`06-launch.md`** (strong pages first) or copy from `sitemap-index.xml` after Claude's live check passes.

### Step 7: Index with Omega Indexer

**Footprint:** Prefer **no Google Search Console** on the directory—same rationale as microsites: do not tie many sites to one Google account. Track **Omega's indexed count** + **Cloudflare analytics**. GSC is allowed if you accept that tradeoff (course note).

**Workflow (lesson 8):**

1. **URL list** — From `06-launch.md` or sitemap; ask Claude for **tiered cost** (`What will indexing cost, and can we put the most important pages first?`): tier 1 = home + state + cities; tier 2 = strongest listings; tier 3 = remainder. One credit = one URL (example: tier 1–2 **584 URLs ~$44** vs full set **~$81**).
2. **Omega** — Dashboard → Campaigns → **+ Create Campaign → Copy & Paste Links** (no file upload).
3. **Dripfeed 7–10 days** — not a one-day blast on a thousand-page launch.
4. **Launch and wait.**
5. **30-day calendar check** — Omega indexed count + Cloudflare visitors. If both move: `Widen the sitemap` → Gate 5 → upload → new Omega campaign. Repeat monthly while metrics grow.

**Omega pricing (community):** Subscription can be cancelled while credits remain; **800 credits ~$60** (~$75/1k). Credits last months. See also [[ai-tool-stacks.md]] and [[external-seo-microsite-tactics.md]] for microsite Omega patterns.

### Step 8: Get paid — calls & claims

**1. Make the calls (day-one monetization, nothing else required)**  
Opening line pattern:

> *"We're connected because you have a listing on my directory, the largest directory of [service] in [state]. Is your listing correct?"*  
> Then: listing not optimized (photos, links)—offer to fix → normal SEO/site conversation.

Community: directories as **#1 source of SEO clients** for some members—the **call**, not passive traffic.

**2. Handle claims**  
Every business page: *"Is this your business? Claim it."* Claiming is **free**.

| Step | Action |
|------|--------|
| Verify | Real local business (not lead-gen); email domain matches site; phone matches listing |
| Speed | **Call same day** — "Saw you claimed your listing, welcome." Community Call #61: several members **call immediately after a free claim** to sell **featured placement** while intent is highest. |
| Update | `Mark <business> as claimed.` → Gate 5 → upload |

**No self-serve logins**—all edits through you (spam control).

### Step 9: Get paid — products, Stripe, own microsites

**Sell by hand:** Stripe Payment Link → they pay → you flip the row → Gate 5 rebuild.

| Product | Price (course starting points) | Notes |
|---------|-------------------------------|--------|
| **Premium listing** | **$97/year** | Their photos, links, map, hours, **"Listed on [directory]"** badge for their site (badge links to their listing page) |
| **Best-of placement** | **$750–$1,200** one-time | Pin on city "best [service] in [city]" + press release package; call list winners first, recall non-winners ~6 months later |
| **Featured slots** | **$29 / $99 / $499** per month | Top card: one city, city group, or whole state; one business per slot per city |

**Setup:** Create Payment Links in Stripe (free account) → paste into Blueprint **featured tiers** file → Gate 5. After sale: tell Claude which business bought which product → Gate 5 → upload.

**Later — sell the leads:** Tracked number or form on ranking **city pages** = rank-and-rent (Microsite Playbook step 4 analog)—**not** a first-month move.

**Your microsites in the directory:** List like any other business—same card, **no cross-links, no badge tricks**. SERP coverage three ways, not a link scheme.

---

## Vertical Selection: Seven Checks

**Scope rule:** One service, one state, one directory. Second state = second domain later.

**If you already have microsites:** Match the directory to the vertical and state you already target (e.g. pool builders in FL cities → Florida pool builders directory).

**From scratch:** Use Niche Finder GPT + Niche Validator (`tool.rankexpand.com/members`, code **NICHECHECK**) on the service plus the state's largest cities — you want a service winnable in **most** cities, not one lucky town. Search `[service] in [state]` / `[service] [state]` — room if results mix national directories and weak locals; skip if one strong statewide directory owns it.

A service that passes all seven is directory-fit; fail two → stay on microsites.

1. **Exact Google Maps category** — Pull uses category, not free text ("swimming pool contractor" yes; "luxury pool designer" no). Read the label under names in Maps.
2. **Category names one trade** — Broad categories leak landscapers/handymen on fence pulls; expect manual sorting.
3. **Comparison shopping** — Pools, roofs, septic, solar, remodels — not midnight locksmiths.
4. **Four-figure+ tickets, weak brand loyalty** — Makes $97 featured listings an easy yes; franchise-heavy states need you less.
5. **Most businesses have websites** — Blueprint reads each site; phone-only listings enrich poorly.
6. **Count band ~200–5,000 reviewed businesses** — Under 200 = thin cities; over 5,000 = heavy Claude token use (e.g. TX roofing 8k+ is a lot for a first build). Ask Claude + DataForSEO to size for ~$0.01.
7. **Real "how to choose" content** — Licenses, permits, materials, seasons — fuels buyer's guide + Step 8 calls ("your listing doesn't show your license yet").

**Low state-level keyword volume is OK** — City terms stack; one listing sale can pay for the site. Wrong vertical costs an afternoon + a few dollars; abort after the **clean report** before enrichment.

---

## Domain Rules (state directories)

1. **.com only** (Cloudflare Registrar ~$10.44/yr, renews at cost; Porkbun similar)  
2. **State + service EMD** — `floridapoolbuilders.com` or `poolbuildersflorida.com`; pick one  
3. **State in name, not a city** — City name = microsite territory  
4. **Never reuse a microsite domain** — Different jobs, different domains  
5. **One directory per domain**

---

## Listings Pull: DataForSEO vs Outscraper

Same-day test (swimming pool contractors, Florida): ~95% overlap on open reviewed businesses; phones/websites ~99%+ match when both had the row. Outscraper extra rows were mostly junk (hotels, parks, misc plumbers). Cost: **~$0.89 vs ~$24** on that pull.

| Path | When to use |
|------|-------------|
| **DataForSEO** (MCP in Claude Code) | Default; pay mostly for real category rows; Gate 1 quotes cost before pull |
| **Outscraper** | No API setup; rename download `listings-raw.csv` |

**DataForSEO caveat:** Database, not live scrape — Blueprint drops listings not updated in ~1 year (~1% closed businesses may slip through; catch on claim/outreach).

**Outscraper rules:** Pick category from dropdown (not free-text search — Jesse's $317 / 119k junk rows lesson). State-wide location, default fields, CSV not Excel, skip email add-ons on pull (emails after clean list ~$3/1k domains).

---

## Directory Blueprint: Gates 1–5

Download Blueprint zip → `input/listings-raw.csv` if Outscraper → open folder in Claude Code → `Read CLAUDE.md and run Gate 1.`

| Gate | What happens |
|------|----------------|
| **1 — Scope** | Service, state, domain, your microsite phones (same vertical), publisher identity, design inspiration URL(s), data source; DataForSEO pull on approval |
| **2 — Clean** | State only, open, ≥1 review, category/name match, dedupe; DataForSEO stale drop; Outscraper often **5–6% kept** — if ~1% kept, category is wrong |
| **3 — Enrich** | 8–15 vertical attributes; scrape each business website; true/false/not enough info + 50–200 word descriptions (no guessing). ~4k tokens/listing; sample batch before full run |
| **4 — Plan** | City pages (≥3 businesses), sitemap inclusion rules, featured slots, design tokens from inspiration site |
| **5 — Build** | Static site via Node; city copy 500–800 words + FAQs from facts; buyer's guide via seo-content skill if DataForSEO connected. Preview with `preview-site.command` / `.bat` — **fix data and re-run Gate 5, never hand-edit HTML** |

Thin "not enough info" listings may wait for sitemap at launch (course Step 7).

---

## Member Results (2026)

**Inbound claim (Brandon Belot, Arizona pool):** [arizonacustompoolcontractors.com](https://arizonacustompoolcontractors.com/) — under two weeks live; owner claimed listing, checked "interested in featured," note: "Better SEO." No cold call. Follow-up: welcome email, paid tiers, claimed badge, Stripe on featured page. Featured slots: rotate owned microsites so spot looks active (avoid obvious cross-linking patterns).

**Outbound → microsite retainer (Remco):** Cold email on incomplete listing (photos, badge, Maps integration) → one-word "yes" reply → phone call → €100/mo per site for hosting/maintenance/SEO/web design; closed **€1,000/mo** for 10 sites (3 new domains + 7 existing EMD cities). Email had **no hard offer** — foot in the door only.

**Listing accuracy email pattern (Remco, translated):** Greet → you're on `{directory}` ({N} `{niche}` businesses) → link → listing incomplete (photos, verification badge, Maps) → offer to complete → "Is the info correct? Reply yes." → sign off.

---

## Case Study: careertrainingpath.com (Vincent Czaplyski)

**Timeline:** Live 28 days, ~1 month of operation  
**Scale:** 7,114 pages indexed (GSC); ~6,620 pages awaiting indexing  
**Traffic:** 485 clicks in 28 days  
**Setup cost:** Under $100 (domain included)  
**Technology:** Astro + Cloudflare (free hosting), built entirely by Claude Code

### How It Works

1. **Automated data ingestion:** Claude Code pulls from API data feeds (e.g., career training programs, course metadata) and populates pages automatically.
2. **Schema + SEO structure:** Every page is tagged with schema; templating is intentional (avoids thin-content penalties).
3. **Dynamic updates:** As data sources refresh, old pages are removed and new ones are added—the site stays current without manual maintenance.
4. **Bulk imagery:** Ideogram API generates relevant images at scale (~1,700 images for ~$200).

### The Link-Flywheel: Automation for Outreach

Claude Code also built a secondary automation layer called the **Link-Flywheel:**

1. **Daily research:** Claude researches 8–10 individuals/organizations that have topical interest in the directory (e.g., journalists, trade associations, university librarians, industry groups).
2. **Personalized outreach:** Each week, the directory sends individually crafted emails from the domain—not asking for a link, but pointing out a mention, contribution, or relevant reference.
3. **Authority building:** Over time, as the domain accumulates sending history and reputation, some targets appreciate the content and link back naturally.
4. **Scale:** Currently sending 3 emails/day on autopilot; cost is nearly zero once set up.

### Secondary Revenue: Ad Platform

Claude also built a backend ad system (currently dormant) that could monetize the directory via:
- Newsletter ads (currently testing)
- Affiliate product placements (e.g., job boards advertising to training programs)
- Featured listing placements (when traffic grows)
- Integration with Mediavine (if traffic ever reaches scale)

### Key Takeaway

Directories can be **built once, left alone, and monetized on multiple axes** without constant content updates or re-ranking games. The infrastructure compounds—link-flywheel brings in backlinks, schema keeps pages indexing, and monetization can layer on top without breaking SEO.

---

## Directory Blueprint: Community Call #56 Demo

During Community Call #56, Shawn demonstrated the **Directory Blueprint** — a boilerplate for building directories end-to-end in 45 minutes to 1.5 hours, fully schema-tagged, for under $100.

### Output Metrics

- **Scale:** ~1,500 Google Maps listings (enriched and schema-tagged)
- **Time:** 45 minutes to 1.5 hours
- **Cost:** Under $100 all-in (domain included)
- **Performance:** Runs at 28 megabytes; scores ~98 on PageSpeed Insights
- **Setup:** Claude Code handles entire build (schema, service tagging, data structure)

### Tech Stack

| Component | Tool | Notes |
|-----------|------|-------|
| Data sourcing | DataForSEO | Pulls Google Maps listing data; chosen over Outscraper (17x cheaper, same accuracy ~1% variation) |
| Form handling | Formspree | Routes "claim this listing" submissions to inbox (current) |
| Payment (future) | Stripe | Likely layer for claimed/premium listing fees |
| Image assets | AI generation (KIE.AI) | ~1,700 unique images for ~$200; alternative: real photos from Facebook/GBP (higher trust for outreach) |
| Analytics/updates | Notion/Airtable → Cloudflare | Pipeline shown in community videos for hosting images and bulk updates |
| Voice (optional) | Vapi + Twilio | Example: one member runs "Alex" voice assistant across all microsites + directory |

### Monetization Strategies

**#1: Featured/Premium Listings**
- Charge businesses to appear in top 3 or featured sections
- Industry standard: ~$95–$200/year per listing
- Implementation: Stripe integration + listing sorting by payment status

**#2: "Best XYZ" Articles**
- Write comparison/listicle articles (e.g., "Best Career Training Programs in [State]")
- Catch citation searches (competing listicles, blog roundups)
- Feeds microsites with backlinks + authority signals

**#3: Direct Sales Outreach**
- Use directory as cold-call opener: "I scraped your competitors into [industry directory]. Three of them are now paying $X/month for featured placement."
- Works especially well for: agency owners, niche SEO/web design firms
- Reported success: one member used this approach to close 3 five-figure retainers in one day

### PBN Footprint Risk: Low

**Key distinction:** Running 10+ **microsites** creates a PBN footprint (Google flags networks of purpose-built, single-keyword sites). Running a **directory** does not.

**Why?** Because directories are normal publisher activity—Yelp, Google Maps, Houzz, Crunchbase, LinkedIn all run directories. Google expects publishers to aggregate listings and make money from them. A directory with:
- Real, enriched data (not thin content)
- Publisher name/branding
- Professional presentation
- Monetization (ads, listings, affiliate)

…looks like a legitimate publisher, not a PBN. You can build authority in a directory, then distribute it down to your own microsites without the exposure risk of owning many independent small sites.

### Data Sourcing: DataForSEO vs. Outscraper

The community tested both against the same query:

| Metric | DataForSEO | Outscraper |
|--------|-----------|-----------|
| Accuracy | ~99% match | ~99% match |
| Cost (for bulk pulls) | 17x cheaper | Baseline |
| Community adoption | All use DataForSEO for research assistant | Some members use Outscraper |

**Decision:** DataForSEO wins for cost + consistency (research assistant + directory building use the same tool, reducing tooling overhead).

### Image Strategy: AI vs. Real Photos

**AI-generated images:**
- Fast: 1,700+ unique images for ~$200 using Ideogram or KIE.AI
- Consistent styling
- Instant at scale

**Real photos (from Facebook/GBP):**
- Higher credibility when reaching out to business owners ("I pulled your real photo")
- Builds rapport in outreach
- Slower: requires VA or manual curation
- Best for: high-touch outreach directories (smaller scale)

**Recommendation by use case:**
- **Monetized directory (10K+ listings):** AI images (speed + cost)
- **Outreach-heavy directory (<1K listings):** Real photos (credibility)
- **Hybrid:** Majority AI, pull real photos for top featured listings

---

## Grounding Accuracy: The Wiki LLM Pattern

During the call, Shawn mentioned how their community uses a **Wiki LLM** to ground Claude's SEO answers in vetted sources. Implementation:

1. **Source-of-truth:** Transcribed community calls, validated research documents
2. **Storage:** A `CLAUDE.md` file in the project repo
3. **Pattern:** Before answering SEO questions, Claude reads `CLAUDE.md` to check if an answer is backed by community data
4. **Result:** Answers come from tested material, not the open internet

This wiki follows the same pattern (see AGENTS.md) — every recommendation links back to `sources:` in the page frontmatter, tracing to raw/ files (call transcripts, competitor captures, etc.). This prevents hallucination and keeps advice grounded in real community results.

---

## How Directories Fit Into a Microsite Strategy

### The Authority Distribution Model

```
Directory (1 domain, high authority)
  ├─ Monetize: featured listings, ads, affiliate
  ├─ Build backlinks: outreach, press, citations
  └─ Link down to →
        Microsite Portfolio (10-100+ domains, each targeting specific keyword/location)
          └─ Link back to directory
```

**Benefit:** The directory builds authority *once*, then:
- Your microsites link to it (legitimizes them)
- The directory links back to featured client microsites (shares authority)
- You monetize the directory separately from the microsites

**Risk reduction:** You're not relying on any single microsite to rank. If one microsite gets penalized, the directory remains healthy.

### Scaling with Directories + Microsites

1. **Phase 1:** Build directory (45 min to 1.5 hrs)
2. **Phase 2:** Link your own 5–20 microsites to directory (with relevant anchor text)
3. **Phase 3:** Monetize directory listings (featured, ads, affiliate)
4. **Phase 4:** Use directory as sales opener for agencies ("Look, I built a directory of your competitors, 3 are paying me now")

---

## Summary Checklist

### Before Building

- [ ] Niche has enough listings: at least 500–1000 viable entries (test with DataForSEO)
- [ ] Monetization path is clear (featured listings, ads, affiliate, or outreach angle)
- [ ] Data source is stable (API or quarterly refreshes, not one-time scrape)
- [ ] Image strategy decided: AI (speed) or real photos (credibility)

### Technical Setup

- [ ] Claude Code configured with directory build brief + project log
- [ ] DataForSEO API key connected (for data pulls)
- [ ] Hosting decision: Cloudflare (free, fast), Vercel, or traditional host
- [ ] Schema validation: every listing page has `LocalBusiness` + category schema
- [ ] PageSpeed: target ~90+; Astro/Cloudflare usually achieve 95–98

### Launch

- [ ] **Lean sitemap** live (strong pages indexed; thin listings noindex but claimable)
- [ ] Claude **live check** passed before Omega campaign
- [ ] **Omega Indexer** campaign: paste URLs, **7–10 day drip**, tier 1–2 first if budget-conscious
- [ ] **Prefer no GSC** on directory (footprint); use Omega + Cloudflare analytics—or GSC if you explicitly accept account linkage
- [ ] Claim form / workflow documented (no public listing login)
- [ ] Stripe Payment Links wired in Blueprint featured tiers (when selling paid products)
- [ ] Link-flywheel configured (if automating outreach)

### Post-Launch

- [ ] **30-day check** on calendar: Omega indexed count + Cloudflare traffic → `Widen the sitemap` if growing
- [ ] Monitor click behavior: ensure CTR comes from search intent (not just browse)
- [ ] Test featured listing monetization with 2–3 businesses before hard pitch
- [ ] Quarterly review: add/remove listings based on data freshness, expand categories

---

## Related Pages

- [[sales-and-lead-generation.md]] — Directory listing outreach email pattern; cold email framework
- [[reddit-mentions-for-ai-inclusion.md]] — Optional visibility layer after directory/microsite work
- [[external-seo-microsite-tactics.md]] — How to leverage directories for backlinks/citations
- [[niche-selection-strategy.md]] — How to pick niches (applies to both microsites and directories)
- [[citations-strategy.md]] — Citations as a monetization + SEO lever
- [[microsite-launch-checklist.md]] — Pre-launch validation (schema, sitemap, etc.)
- [[on-site-seo.md]] — Content structure (applies to directory homepages and category pages)
