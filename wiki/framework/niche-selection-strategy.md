---
type: framework
client: none
status: active
updated: 2026-09-11
sources:
  - "raw/framework/48 - Niches Within Niches - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/49 - The 12-Minute Microsite - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/EMD - Exact match domain with dashes - AI SEO Rank Expand Academy.md"
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
