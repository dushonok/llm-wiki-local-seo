---
type: framework
client: none
status: active
updated: 2026-10-27
sources:
  - "raw/framework/48 - Niches Within Niches - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/49 - The 12-Minute Microsite - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/EMD - Exact match domain with dashes - AI SEO Rank Expand Academy.md"
  - "raw/framework/Domain advice. .com is taken - AI SEO Rank Expand Academy.md"
  - "raw/framework/Community Call 58 - Semantics Over Backlinks, Flat Leasing - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/Bilingual sites Worth it - how to do it - AI SEO Rank Expand Academy.md"
  - "raw/framework/Domains - weird extensions - AI SEO Rank Expand Academy.md"
---

# Niche Selection & Microsite Strategy

**Core Principle:** Go one level deeper. "Locksmith" is a bloodbath. "Car locksmith" or "garage-door locksmith" is open. Same holds for concrete, plumbing, HVAC — find the subniche.

---

## The Niche Selection Framework

### Level 1: Problem

Identify a broad service category:
- Locksmith
- Concrete
- Plumbing
- HVAC
- Tree removal
- Wet room installation

### Level 2: Service Niche

Go deeper within the service:
- Locksmith → **Car locksmith** OR **Garage-door locksmith**
- Concrete → **Decorative concrete** OR **Concrete repair**
- Plumbing → **Water heater repair** OR **Emergency plumbing**
- Tree removal → **Dead tree removal** (not generic "tree removal")
- Wet room → **Wet rooms for elderly** (accessibility angle)

### Level 3: Geographic Niche

Combine service with location:
- Car locksmith in Denver
- Decorative concrete in Austin
- Wet rooms for elderly in Manchester
- Tree removal in suburban Chicago

### The Data Point

One city had **30 competitors** for concrete. The next town over had **3**. Pick the easy geographic niche first. Rankings come in 2–4 weeks at this level.

---

## Why This Works

1. **Lower difficulty** → Easier to rank
2. **Clear intent** → User knows exactly what they need
3. **Better conversion** → Someone searching "car locksmith Denver" is ready to buy
4. **AI loves specificity** → Schema, entity relationships, and contextual signals are clearer

---

## The Microsite Model

### What is a Microsite?

A single-page or 2–3 page site targeting one niche, one location, one service.

**Not:**
- Trying to rank for 50 keywords
- Building a "resource hub"
- Generic content that could apply anywhere

**Yes:**
- One service + one location
- Phone number + contact form
- Voice AI agent or chat
- 50–150 word summary at top (AI Overviews love this)
- Structured data (LocalBusiness + Service schema)

---

## The 12-Minute Microsite Build

**Timeline:** From domain purchase to live site with voice agent: ~12 minutes

**Process:**

1. **Domain purchase** (2 minutes)
   - Namecheap, Porkbun, or similar
   - Cost: $10–15/year
   - **TLD choice:** `.com` is the safer default for user trust/perception on a
     commercial local-service site, but `.org` (or other TLDs) is a fine substitute
     when the exact-match `.com` string is taken — no ranking penalty either way.
     Match the domain string (niche + location) to the EMD strategy first; TLD is
     secondary. Mixing TLDs across a multi-site portfolio also slightly reduces
     footprint/entity-linking risk (see "Domain & Hosting Security" in
     [Community Call #8](../../raw/framework/Community%20Call%208%20-%20🎙️%20The%20Call%20Vault%20·%20AI%20SEO%20Rank%20Expand%20Academy.md)
     on avoiding shared assets across microsites). *Not sourced from a raw call —
     general domain/SEO knowledge, flagged here for traceability.*

2. **Site generation** (3 minutes)
   - Manus (generates static HTML from prompt)
   - OR Claude Code (vibe-code it)
   - Output: ZIP file

3. **Upload & host** (2 minutes)
   - SiteGround or Cloudflare Pages (free for static)
   - Deploy ZIP

4. **Indexing** (2 minutes)
   - Omega Indexer: bulk-submit all URLs to Google
   - Alternative: Manual GSC submission

5. **Voice agent setup** (2 minutes)
   - Twilio (get phone number): 30 seconds
   - Retell AI (voice agent): 30 seconds
   - Connect to GoHighLevel for lead capture

6. **Image customization** (1 minute)
   - Nano Banana: tweak images for local uniqueness

**Cost per site:** $2–5 (hosting, indexing, voice agent) + $10–15 domain = ~$15–20 total

---

## Key Implementation Details

### Content Structure for Microsites

**Essential elements:**
- **100–150 word summary at top** — AI Overviews extract this; include service + location + differentiator
- **LocalBusiness schema** — Name, address, phone, service type, hours, rating
- **Service schema** — What service you offer, areas served, pricing if available
- **Phone number prominent** — Top of page, voice AI connected
- **Contact form** — Aweber or GoHighLevel lead capture
- **Real images** — Nano Banana keeps them locally unique
- **Testimonials or reviews** — If available (or seed with early clients)

### Avoiding Common Mistakes

**❌ Don't:**
- Build 100+ sites without research first
- Use completely generic content across sites
- Ignore NAP consistency (address must be real or from LoopNet)
- Skip schema markup
- Neglect voice agent setup (it's 30 seconds—do it)

**✅ Do:**
- Research the niche first (2–3 competitor sites)
- Research the location (population, search volume, competition)
- Use real addresses (LoopNet for commercial; accurate residential for local services)
- Maintain 100% NAP consistency
- Always add voice agent (converts calls to sales)
- Start with 3–5 sites/week; scale after you see what works

---

## Volume Strategy: From 3 to 300 Sites

### Phase 1: Validation (Weeks 1–4)

**Goal:** Find the winning combination

1. Pick **2–3 niches** (car locksmith, garage doors, water heater repair)
2. Pick **3–5 geographic markets** (different cities, different states)
3. Build **9–15 sites total**
4. Wait 2–4 weeks for data

**Metrics to track:**
- Google Search Console impressions
- Phone calls
- Form submissions
- Where conversions come from

### Phase 2: Scaling (Weeks 5+)

Once you have a niche + location combo that converts:

**Option A: Single-niche at scale**
- One niche (e.g., car locksmith)
- 50–100 different cities
- Build 10–20/week

**Option B: One city, multiple niches**
- Pick the winning city
- 20–30 different services
- Build 5–10/week

**Option C: Master Git branch deployment**
- Create template in GitHub
- Deploy to 100+ domains at once via Cloudflare
- All pull from master; updates auto-deploy

**Cost at scale:**
- $10–15 per domain
- $2–5 per site (hosting + indexing + voice agent)
- **Total:** ~$20 per site
- **Payoff:** 30% rank + convert = profitable at ~$200/lead minimum

### Example Numbers

Mark's actual results:
- **88 live sites** since early June
- **18 calls in one day** from one site
- **2–4 week rankings** typical
- **$2–5 per site** operational cost
- **30% conversion to ranking** threshold for profitability

---

## Domain Strategy: EMD with and Without Dashes

**Recent Insight:** EMD (Exact Match Domain) strategy is evolving. Traditional wisdom favored `chicagoplumbing.com` over `chicago-plumbing.com`, but new data suggests dashes are worth testing.

**How Google Treats Dashes:**
- Google parses dashes as spaces: `chicago-plumbing.com` = `chicago plumbing.com` (same EMD)
- Functionally equivalent for SEO ranking purposes
- Both are valid exact match domains

**The Practical Difference:**

| Factor | Without Dashes | With Dashes |
|--------|---|---|
| User experience | Easier to type on phone | Slightly harder to type |
| Visual appearance | Cleaner looking | Looks slightly less spammy |
| Ranking potential | Same | Same |
| Test results | #1-#3 rankings common | #1-#3 rankings observed (trending) |

**Real Example:** A site ranking #2 for "water damage Edmond OK" uses a dash domain variant.

**The Trend:** Members are seeing dash-based EMDs ranking in top 3, occasionally #1. Worth A/B testing if the non-dash version is taken.

**Secondary TLDs:** `.net` and `.xyz` are also working when `.com` isn't available, but stick with `.com` or `.net` first; avoid oddball TLDs.

**Strategy Note:** The micro focus now is less about "top of page 1" (fewer clicks) and more about AI Overviews and owning other SERP real estate. Domain variation (with/without dashes) is secondary to content structure and citations.

### Non-Traditional TLDs (.solar, .io, etc.)

**What Members Are Trying:**
- `.solar` (for solar companies)
- `.io` (tech/projects)
- `.dev`, `.app`, `.co`, `.xyz` (various niches)

**The Verdict (Early Data):**
- **Pros:** Easier to get short, snappy domain names when .com is unavailable; `.solar` specifically works well for solar/energy niches
- **Cons:** Renewal costs jump significantly year 2+ (year 1 often discounted, then $15–$30+/year); community members report mixed results (some parked unused, Brandon wants more test data)
- **Ranking impact:** No data yet on whether .solar, .io, etc. rank differently than .com/geo-TLDs. Brandon suggests A/B testing if you want to compare.

**Recommendation:**
- Use non-traditional TLDs only if:
  - The .com and geo-TLDs are unavailable
  - The TLD is semantically relevant to the niche (.solar for solar, .dev for developers)
  - You're willing to pay renewal costs (~$15–$30/year after year 1)
  - You're OK testing and gathering data (no clear winner yet)
- For most local service microsites, prefer .com, geo-TLDs (.ca, .uk, .mx), or hyphenated .com first

**Cost Gotcha:**
- Many registrars offer cheap year 1 (.solar at $6/year, for example)
- Year 2+ can jump to $25–$30/year
- Factor this into your microsite unit economics if building at scale

---

## Domain Selection When .COM Is Taken

**Key Finding (from Contest Data):** The .com being taken is not a reason to move on. What matters is whether you can make the *brand name match the keyword*.

### The Real Test: What's the Competition Actually Running?

**Scenario:** Your target .com and .ca (or .org) are both taken.

**Ask:** 
- Is the .com an actual functioning site with traffic/authority? Or just a placeholder?
- Is the .ca (or alternative TLD) site live and strong?
- Or is it a "coming soon" page?

**Real Example:** One niche had the .com going to a poorly-maintained site and the .ca showing "coming soon." That's a winnable market. The site that gets profiles + pages built first wins, not the one that registered the domain first.

### Variant Strategies (All Proven to Rank)

**Option 1: Hyphenated .COM**
- Example: `kitchen-renos-city.com`
- Proven ranking: Sites using hyphenated EMDs are in top 3, occasionally #1
- Psychology: Slightly less polished-looking than unhyphenated, but ranks just as well

**Option 2: .CA (or Geographic-Specific TLD)**
- Example: `kitchenrenoscity.ca` or `city-kitchenrenos.ca`
- Advantage: In Canada, .ca beats .org for local trust every time
- Reorder the words if needed: `kitchenrenos-city.ca` or `city-kitchenrenopros.ca`
- Works just as well as .com for local ranking

**Option 3: .ORG (Last Resort)**
- Works and ranks fine
- **Downside:** Reads psychologically like a nonprofit, even for commercial services
- Use only if .com and geographic TLDs are unavailable

### What NOT to Do

- **Don't use oddball TLDs** (.xyz, .co, .io for local services) — they confuse users and signal lower trust for commercial local work
- **Don't abandon a good niche** because the .com is taken; abandon it only if both the .com AND the alternative TLD are in strong hands

### The Data from the Microsite Contest

Test results across hyphenated .com, .org, .net, and .us showed:
- **No position gained because of the extension alone**
- Every position gained came from the business entity behind the domain:
  - Brand name matching the keyword
  - Phone + address showing up the same way everywhere (NAP consistency)
  - 10–15 profiles all pointing at the site

### Summary

**The question isn't ".com or .org." It's "can you make the brand name the keyword?"**

You can, with any of these:
- Hyphenated .com (proven top-3 performer)
- Geographic TLD variant reordered (e.g., .ca or .uk with words rearranged)
- .org only if nothing else works

**Then execute:** Profiles + pages built first. The site that gets built wins, not the one that registered the domain first.

---

## YMYL Niches & Licensing Requirements

**Key Finding (from Call #58):** YMYL (Your Money or Your Life) niches require special handling. Financial services, insurance, legal, and health-related microsites carry licensing and liability risks.

### Niches to Avoid or Approach Carefully

**High-Risk YMYL Categories:**
- **Financial services** (loans, investment advice, debt management)
- **Insurance** (health, life, auto, home)
- **Legal services** (attorney services, legal advice)
- **Health & medical** (medical advice, treatments, diagnoses)

### Safe Approaches for YMYL

**Option 1: Work Under an Existing License (Recommended)**
- Example for attorneys: Build sites but run them under/powered by an actual attorney
- Example for financial services: Partner with a licensed bank or credit union; site is "powered by" their license
- You build the site; they provide the license and liability coverage
- Business model: Per-lead fee or rev-share from closed deals

**Real Example (Attorneys):** Build a relationship with the largest law firm in the niche. Run a test site "powered by" their firm at a discounted per-lead rate. Cover the smaller towns they don't reach yet. This protects you legally and gives them a scalable channel.

**Option 2: Build as Lead Gen Aggregator (Not Advisor)**
- You don't give advice; you connect leads to licensed professionals
- Example: "Find a lawyer near you" (not "get legal advice")
- This avoids YMYL liability because you're not making the recommendation

**Option 3: Skip It**
- The consensus in the community: most people *should* skip high-risk YMYL niches unless they have a clear licensing path
- The liability risk isn't worth the upside unless you're working under someone else's license

### Mitigating Risk

**If you do work in YMYL:**
- Use clear disclaimers ("not legal/financial/medical advice")
- Work *under* an existing license whenever possible
- Consult your own attorney before launching
- Separate the lead aggregation (yours) from the advice (theirs)
- Maintain clear liability boundaries in your contract

---

## Language & Market Focus

**Key Finding:** Don't build bilingual/hybrid-language sites. Pick one language and own that market completely.

### The Problem with Hybrid Language Sites

**Principle:** A site with language switchers or mixed-language content confuses search engines and dilutes ranking potential. You're splitting authority between two languages instead of dominating one.

**Real Case Study (Texas Home Services Client):**
- **Setup:** English primary site with a Spanish subdirectory (`site.com/es/`)
- **Traffic:** Spanish section was ~5% of overall traffic
- **Best practices applied:** All multilingual SEO best practices followed (hreflang tags, proper structure, etc.)
- **Problem:** The Spanish content was competing against a much larger English site; Spanish search volume was lower than English equivalents, but Spanish *competition* was significantly less (they were targeting the wrong language structure)
- **Solution:** Moved all Spanish content to a Spanish-only domain (`site.es` or similar)
- **Result:** Spanish traffic tripled in a few months

**Why the Spanish-only domain won:**
- Search engines see a single-language, focused domain with clear intent
- No dilution of authority (all signals point to one language)
- Lower competition in Spanish market (fewer competitors are there)
- Users landing on a Spanish-only site have a clear, consistent experience (no confusion about language toggling)

### Strategy: One Language Per Site

**For microsites:**
- English-speaking area? Build one .com or local TLD site in English
- Spanish-speaking area? Build a separate .com.mx or .es or Spanish-localized .com site in Spanish
- Do not build one site with both; build separate, focused sites

**For directories:**
- Same principle applies: a Spanish-only directory ranks better than an English directory with a Spanish section
- Example: If building a directory for Texas where 80% of the service area speaks Spanish, build a Spanish-only directory, not an English directory with Spanish pages/switching
- If you want to serve both markets, build two separate directories (or two separate microsites per location)

**For client sites (like the Texas case):**
- If the client's market is bilingual but one language dominates, pick that language
- If the market is truly 50/50, negotiate with the client to build two separate sites
- If they insist on one site, at minimum: use proper hreflang tags and structure (but expect lower performance in both languages than two separate sites would deliver)

### How to Present This to Clients

**The pitch:** "You'll rank better and capture more leads if we build a Spanish-only site targeting Spanish speakers than if we try to serve both English and Spanish speakers on one site. Spanish search competition is much lighter, and we can own that market completely."

**Why clients often resist:** They think one bilingual site is cheaper. It often is, short-term. But two focused sites outrank one hybrid site, usually within a few months.

**The numbers:** If a Spanish-only site triples traffic (as in the Texas case), the additional revenue typically pays for the second site's cost within 1–2 months. Long-term play wins here.

---

## Tools for Volume Builds

### One-at-a-time builds:
- Manus (static HTML generator)
- Claude Code (vibe-code)
- Cloudflare Pages / SiteGround (hosting)
- Omega Indexer (bulk indexing)
- Retell AI + Twilio (voice agent)

### Bulk/programmatic builds:
- **Hermes agent** + DataForSEO (driven from Telegram)
- **Master Git template** + Cloudflare (auto-deploy to many domains)
- **Claude Code** + Scripts (auto-generate and deploy)

---

## Business Models

### Model 1: Lead Gen (for clients)

- Build microsite for contractor
- Charge per lead (~$50–150/lead)
- Or: commission on jobs booked

**Typical:** 1 site, 5–10 leads/month = $500–1,500/month per client

### Model 2: Affiliate Sites

- Build microsite around product/service
- Amazon Associates, AvantLink, or display ads (Mediavine, Raptive, Zoic)
- Passive income per site

**Typical:** 1,000 pageviews/month = $50–200/month (affiliate); higher with display

### Model 3: Personal Volume Play

- Build 100+ sites yourself
- Keep the best leads, flip the rest to contractors
- Or: Sell sites after they rank (turnkey businesses)

---

## The Research-First Mindset

**Key insight from Call #48:** Research first, then build. Volume without research fails.

**Before you build a site:**

1. **Competition check** — How many competitors in this niche + city?
2. **Search volume** — Use Keyword Surfer, Ahrefs, or SeRanking
3. **SERP analysis** — Who ranks? What's their approach? Can you differentiate?
4. **Keyword research** — Pick specific keywords (not generic "locksmith," but "car locksmith near [city]")
5. **Build for one keyword at a time** — Laser-focused, single-page sites convert better

**Timeline:** Spend 30 minutes researching. Build 10 minutes. Ratio of 3:1 research to build.

---

## Automation & Agents

**Emerging:** Hermes agent platform (agent-driven microsite builds)

- One member running Hermes with local models
- Integrated with DataForSEO for competition research
- Driven from Telegram (text commands to build sites)
- Self-learning (improves over time)

**Cost:** Open-source (Hermes), ~$30–50 DataForSEO/month per active build

This represents the future: agents that research, build, and monitor sites autonomously.

---

## The Bottom Line

**Niche selection > volume**

Better to build 3 highly-targeted sites in 2 weeks than 100 generic ones. The 3 will rank, convert, and teach you the system. Then scale what works.

The move: **Niches within niches. Deep specificity. Measurable wins. Scale the winner.**
