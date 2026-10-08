---
type: framework
client: none
status: active
updated: 2026-10-07
sources:
  - "raw/framework/Directory Launched 28 Days Ago - 485 Clicks - AI SEO Rank Expand Academy.md"
  - "raw/framework/Community Call 56 - Directory Blueprint as Force Multiplier - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
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

- [ ] Sitemap submitted to GSC
- [ ] Homepage CMS linkable (points to directory home, not just listings)
- [ ] Form handler working (Formspree or equivalent for listing claims/submissions)
- [ ] Link-flywheel configured (if automating outreach)

### Post-Launch

- [ ] Track indexing velocity in GSC (expect 50%+ indexed within 4 weeks)
- [ ] Monitor click behavior: ensure CTR comes from search intent (not just browse)
- [ ] Test featured listing monetization with 2–3 businesses before hard pitch
- [ ] Quarterly review: add/remove listings based on data freshness, expand categories

---

## Related Pages

- [[external-seo-microsite-tactics.md]] — How to leverage directories for backlinks/citations
- [[niche-selection-strategy.md]] — How to pick niches (applies to both microsites and directories)
- [[citations-strategy.md]] — Citations as a monetization + SEO lever
- [[microsite-launch-checklist.md]] — Pre-launch validation (schema, sitemap, etc.)
- [[on-site-seo.md]] — Content structure (applies to directory homepages and category pages)
