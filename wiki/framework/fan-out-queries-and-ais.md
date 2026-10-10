---
type: framework
client: none
status: active
updated: 2026-10-10
sources:
  - "raw/framework/Fan-Out Queries - 🚨 Extract Query Fan Out From ChatGPT (1-minute setup) · AI SEO Rank Expand Academy.md"
  - "raw/framework/Fan-Out Queries - Ranking for Multiple Fan-Out Queries Dramatically Increases Your Chances of Getting Cited in AIOs (173,902 URLs Studied).md"
  - "raw/framework/ChatGPT Query Fanout Analyzer (Bookmarklet) - JC Chouinard.md"
  - "raw/framework/How to see fan-out queries in ChatGPT - written by Perplexity on Oct 10, 2026.md"
  - "raw/framework/Pasted image 20261010085447.png"
  - "raw/framework/Pasted image 20261010085748.png"
---

# Fan-Out Queries and AI Overviews

**Definition:** Fan-out queries are the sub-queries and related searches that LLMs (ChatGPT, Gemini) perform internally when answering a user's original question. They represent how AI breaks down and contextualizes a query before generating its response.

---

## The Data: Why Fan-Out Queries Matter

### Key Finding (173,902 URLs Studied)

Ranking for multiple fan-out queries dramatically increases your chances of being cited in AI Overviews.

**Correlation strength:** 0.77 (very strong positive correlation between fan-out ranking and AIO citations)

---

## Critical Statistics

### 1. Main Query + Fanouts > Main Query Alone

- **51.2%** of AIO citations rank for *both* the main query **and** at least one fan-out query
- **19.6%** of AIO citations rank solely for the main query (no fan-outs)
- **Implication:** You're **161% more likely to get cited if you rank for both**

### 2. Fanouts Alone > Main Query Alone

- **29.2%** of AIO citations rank only for fan-out queries (not the main query)
- **19.6%** of AIO citations rank only for the main query (no fan-outs)
- **Implication:** You're **49% more likely to get cited ranking for fan-outs than for the main query**

### 3. Most AIO Citations Don't Rank in Top 10

- **67.82%** of AIO citations in the study didn't rank in the top 10 at all
- **However:** Among top 3 visible citations, **54.14%** do rank in top 10 (for main or fan-out queries)
- **Implication:** Ranking matters, but AI also draws from sources beyond traditional organic results (reviews, social, industry sources, etc.)

---

## How to Extract Fan-Out Queries

### Method 1: Manual Network Tab Extraction (Perplexity Guide)

**Status: Recommended as of Oct 10, 2026** (Bookmarklet approach no longer reliably working)

The most direct way to extract fan-out queries and citations: manually inspect ChatGPT's backend conversation endpoint via Chrome DevTools Network tab, following the step-by-step troubleshooting guide outlined by Perplexity.

**Why this method:** ChatGPT's `/backend-api/conversation/{id}` endpoint stores both `search_model_queries` (the queries ChatGPT actually ran) and `safe_urls` (all cited sources) in the raw JSON response. This method bypasses the parsing complexity that breaks bookmarklets when ChatGPT updates its message structure.

**High-level process:**
1. Open a ChatGPT conversation with Web Search enabled
2. Submit your target question
3. Open Chrome DevTools → Network tab
4. Filter for the `conversation` request (type: `fetch`, status: 200)
5. Click it and open the Response panel
6. Use `Ctrl + F` to search for `search_model_queries` or `safe_urls`
7. Copy the JSON, extract the values (see Perplexity guide for full details + screenshots)

**Detailed walkthrough:** See `raw/framework/How to see fan-out queries in ChatGPT - written by Perplexity on Oct 10, 2026.md` for the complete Network tab debugging process, including screenshots showing where to look for the data and what each field means.

**What you extract:**
- `search_model_queries.queries[]` — the actual fan-out query/queries ChatGPT generated
- `safe_urls[]` — all URLs ChatGPT cited (filter out `images.openai.com`, `google.com/maps`, `google.com/search`)
- Per-prompt metadata: model slug, request ID, reasoning steps

**Limitation:** one conversation at a time. For aggregating across 30+ queries, either manually run this per-query and compile results, or use DataForSEO for automated/scaled extraction.

**Cost:** Free | **Time:** 2–5 minutes per query (once you learn the pattern)

---

### Method 1 (Deprecated): ChatGPT Bookmarklet Tool

⚠️ **No longer recommended as of Oct 10, 2026.** The "ChatGPT Query Fanout Analyzer" bookmarklet by Jean-Christophe Chouinard does not reliably parse the current ChatGPT message structure. While the bookmarklet source code is preserved in `raw/framework/ChatGPT Query Fanout Analyzer (Bookmarklet) - JC Chouinard.md` for reference, use the manual Network tab method (Method 1 above) instead.

Historical context: The bookmarklet worked by calling ChatGPT's internal `/backend-api/conversation/{id}` endpoint and parsing the response JSON to extract queries, citations, and entities. It required one-time browser bookmark setup and then ran with a single click. However, recent ChatGPT updates changed the response message structure in ways the bookmarklet's parser does not handle, so it now fails to extract `search_model_queries` even though the data is present in the endpoint response (as confirmed by the Perplexity troubleshooting guide in raw/framework).

### Method 2: Chrome Extension (Keyword Surfer)

Surfer SEO's free Keyword Surfer extension shows fan-out queries directly in ChatGPT/Gemini interface.

---

## Strategy: Topical Authority Over Fan-Out Chasing

### Why Don't Just Chase Every Fan-Out?

1. **Personalization varies:** Fan-outs differ by user context. Same query gets different fan-outs for different searchers.
2. **Inconsistency across runs:** Only ~27% of fan-outs stay consistent across multiple searches for the same prompt. You'd need to run queries multiple times and cluster results to identify "core" fan-outs.
3. **Never-ending game:** You're always optimizing for a moment in time. Fan-outs shift constantly.

### Better Approach: Build Topical Authority

**Core Idea:** If you build strong content around important topics, you'll naturally have content answering *whatever* questions AIOs want to know—regardless of current fan-outs or who's asking.

**Advantage:** You cover so much ground that your content answers probable fan-outs organically, even as they shift.

**Process:**

1. **Identify your core topic** (e.g., "electric cars," "local plumbing services")
2. **Map semantic clusters** around that topic using tools like Surfer SEO's Topical Map
3. **Identify content gaps** in your current coverage
4. **Prioritize low-difficulty topics first** (often align with fan-outs)
5. **Build out methodically** — easier topics first, then harder ones
6. **Create LLM-friendly content** for each subtopic

### Example: Building Topical Authority

Target: "Best Plumbing Services in Denver"

**Topical clusters to cover:**
- Emergency plumbing (fan-out: "24-hour plumbing Denver")
- Drain cleaning (fan-out: "drain cleaning costs Denver")
- Water heater repair (fan-out: "water heater repair Denver")
- Preventive maintenance (fan-out: "plumbing maintenance tips")
- Sewer line repair (fan-out: "sewer line repair costs")

**Strategy:**
- Start with easiest, highest-search-volume subtopics
- Create dedicated landing pages for each
- Interlink using semantic architecture
- Include entity mentions (neighborhoods, landmark businesses, local associations)
- Build structured data for each service/location combination

---

## How to Implement

### For Your Clients

1. **Audit current rankings**
   - Which queries are you ranking for?
   - Do you rank for main query, fan-outs, or both?

2. **Research fan-outs for key queries**
   - Use ChatGPT bookmarklet or Keyword Surfer
   - Extract 5–10 key fan-outs per main query
   - Look for patterns (recurring themes across fan-outs)

3. **Assess coverage gaps**
   - Does your content address these fan-out topics?
   - Which gaps are easiest (lowest KD)?

4. **Prioritize by difficulty + impact**
   - Start with low-difficulty fan-outs
   - Prioritize high-search-volume subtopics
   - Create content naturally (topical authority, not desperation)

5. **Measure AIO visibility**
   - Track which pages appear in AI Overviews
   - Monitor impressions and CTR in GSC
   - Correlate fan-out ranking + AIO citations over time

---

## Key Takeaway

Ranking for multiple fan-out queries is the strongest empirical indicator of getting cited in AI Overviews. Rather than chasing every possible fan-out, build topical authority around your core offering. This ensures you answer most probable questions—and get cited consistently—even as AI fan-outs evolve.
