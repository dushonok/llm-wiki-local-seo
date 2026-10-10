---
type: framework
client: none
status: active
updated: 2026-10-10
sources:
  - "raw/framework/🎙️ The Wisdom's In The Calls - Getting Cited by AI  · AI SEO Rank Expand Academy.md"
  - "https://developers.google.com/search/docs/appearance/structured-data/organization (external, fetched 2026-10-09 — basis for the sameAs placement correction below)"
  - "raw/framework/ChatGPT Query Fanout Analyzer (Bookmarklet) - JC Chouinard.md"
  - "raw/framework/How to see fan-out queries in ChatGPT - written by Perplexity on Oct 10, 2026.md"
  - "raw/framework/Pasted image 20261010085447.png"
  - "raw/framework/Pasted image 20261010085748.png"
---

# Getting Cited by AI

**Core Principle:** Getting mentioned is the new ranking. When someone asks ChatGPT or Gemini who to hire, the AI repeats back what it already sees cited. The work moves to wherever the AI reads.

---

## Move #1: Find the Invisible URLs AI Already Trusts

**Concept:** Discover which third-party pages ChatGPT and Gemini cite most frequently — these are AI's trusted sources that show up zero times on traditional backlink tools.

**Process:**
1. Take top 30 queries from Google Search Console
2. Turn each into a question
3. Check which third-party pages ChatGPT and Gemini cite for each — either via
   DataForSEO (paid, automatable at scale) or, per-query and free, the ChatGPT
   Query Fanout Analyzer bookmarklet (see
   [[fan-out-queries-and-ais.md]] Method 1 for setup/use — exports a citations
   CSV per conversation)
4. Aggregate 250–500 URLs and sort by citation frequency
5. Target URLs cited 10+ times (the "invisible layer")

**Action:**
- Outreach those high-citation URLs for listings ($50–200 per link)
- Build backlink strategy sourced from AI behavior, not domain authority

**Principle:** Stop guessing which links matter. Ask the AI where it reads, then go get listed there.

---

## Move #2: Get Mentioned Where the AI Reads

**Key Channels:**
- **YouTube** — Single biggest factor in AI mentions; #2 cited source after Reddit
- **Facebook Groups (Local)** — Profiles active in local town groups recommending your business get cited in Gemini and ChatGPT
- **Reddit** — #1 cited source; where conversation happens shapes AI answers

**Actions:**
1. Create affiliate YouTube accounts (for services like water treatment, contracting, etc.) cranking out educational content
2. Participate actively in local Facebook groups, recommending your client's business
3. Build Reddit presence in relevant communities
4. Add all social profiles via `sameAs` schema to strengthen entity connections —
   put this on the `Organization` markup on the home page (or About page), not
   duplicated across every page; see the placement rule in
   [[seo-fundamentals/technical-seo.md]]

**Principle:** AI answers are a mirror of public conversation. Put your client's name where the conversation happens.

---

## Move #3: Third-Party Beats Self-Praise (The Persona Listicle)

**Problem:** AI detects self-bought press releases as paid and discounts them.

**Solution:** Publish a listicle on an unrelated third-party site under a separate author persona.

**Example Structure:**
- Title: "Best [Service] in [City]" (e.g., "Best Roofers in Charlotte NC")
- Lead line: Front-load "[service] + [city]" language
- Byline: Author name that's independent-looking (not your brand)
- Content: Treat as third-party verification, not self-promotion

**Why It Works:** AI weights *who's talking*, not just what's said. Independent-looking praise outranks direct self-promotion.

**Cost:** $100–500 per listicle (varies by placement)

---

## Move #4: Expired-Domain Sponsorships (Local Links for $20)

**Process:**
1. Find expired domains of past local 5Ks, charity walks, community events
2. Buy the domain ($20–50 each; ~$5/month hosting)
3. Relaunch the site with basic sponsor listings
4. List your clients as sponsors

**Advantages:**
- Genuinely local backlinks
- Dirt cheap (~$25–55 per link)
- One relaunched event site serves 4–5 clients
- Appears authentic (actual event site, not built for backlinks)

**Related Tactic:** Search `[city] "sponsorships"` for active events and approach directly for legit local links.

**Principle:** Local trust signals don't have to be expensive. They have to be real-looking and genuinely local.

---

## Move #5: The Profiles Page That Indexes Your Citations

**Concept:** Use your own domain's authority to index citations and get them crawled by Google.

**Setup:**
1. Create a `/profiles` page on your client's website
2. Link out to all citations and social profiles from this page
3. Ensure the page is indexed (submit to GSC, internal link from homepage)

**How It Works:**
- Your own domain is trusted, so the /profiles page gets crawled
- Links from this trusted page help index the citations
- Citations become indexed backlinks pointing back to your main site
- Creates a virtuous indexing loop

**Principle:** Your own domain is the most reliable indexing tool you have. Use one page of it to power up everything pointing at you.

---

## Takeaway

The playbook shifts from "buy backlinks from high-DA sites" to "get cited where the AI reads." The five moves above serve one goal: make your client visible to AI systems by:

1. Targeting where AI already trusts
2. Appearing in public conversations
3. Building independent-looking authority signals
4. Getting locally cited authentically and affordably
5. Using your own domain to amplify third-party citations
