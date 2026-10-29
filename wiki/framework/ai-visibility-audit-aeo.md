---
type: framework
client: none
status: active
updated: 2026-10-29
sources:
  - "raw/framework/Invisible URLS = AI Visibility + Outreach Targets Prompt · AI SEO Rank Expand Academy.md"
---

# AI Visibility Audit & Outreach Target Mining (AEO Strategy)

**Concept:** Measure where your brand appears (or disappears) in ChatGPT and Gemini answers. Mine the AI's trusted citation sources to build a concrete outreach hit list—the pages that appear repeatedly in AI answers are the ones worth pitching.

**Key Insight:** This is link building, except the "search engine" is an LLM's retrieval layer. Instead of asking "who links to my competitors?", you're asking "which third-party pages does the AI trust when answering questions in my market?"

---

## The Problem This Solves

When people ask ChatGPT or Gemini "best [product] in [market]" or "how do I choose [service]":
- The AI recommends your brand, OR
- Cites your site without naming you, OR
- Omits you entirely

**You have no visibility into which.** This system measures that at scale across your entire market and identifies:
1. Which markets you're winning in AI
2. Which third-party pages the AI reads + trusts most (your outreach targets)
3. The highest-leverage next actions (get mentioned in the pages the AI already cites)

---

## The 5-Step Pipeline

### Step 1: Prompt Generation

Generate realistic user prompts that people actually ask AI models.

**Two intent types per page/market:**

- **Product-intent:** "best X in Y" (e.g., "best ecommerce platform for small businesses")
- **Advisory-intent:** "how do I choose X in Y" (e.g., "how do I choose an ecommerce platform?")

**Why both?** An intermediary (broker/agency/marketplace) wins advisory questions, not "best manufacturer" questions. Match prompts to what your business can actually win.

**Use an LLM to generate prompts** for each page/market combo. This ensures variety and realism.

**Google Search Console Connection (Optional):**
- If you connect GSC, identify your top queries by volume
- Infer which AI prompts will have similar volume
- Map everything from GSC as your prompt seed list

---

### Step 2: LLM Answer Collection (DataForSEO API)

Use DataForSEO's AI Optimization API to collect answers from ChatGPT and Gemini.

**Endpoint:**
```
POST /v3/ai_optimization/{chat_gpt|gemini}/llm_responses/live
```

**Body:**
```json
[
  {
    "user_prompt": "best ecommerce platform for small businesses in 2026",
    "model_name": "gpt-4o-mini",
    "web_search": true
  },
  {
    "user_prompt": "how do I choose an ecommerce platform?",
    "model_name": "gemini-2.0-flash",
    "web_search": true
  }
]
```

**Critical Gotchas (Learned the Hard Way):**

1. **Do NOT include `max_output_tokens`** — this is an invalid field and causes error 40501
2. **Use cheap models for cost control:**
   - ChatGPT: `gpt-4o-mini` (~$0.015/call with web search)
   - Gemini: `gemini-2.0-flash` (~$0.066/call) — Gemini drives ~80% of total cost
   - Budget accordingly: run ChatGPT monthly, Gemini every other month if cost is a constraint

3. **Response structure is nested:**
   - Response → `items[]` → `message` → `sections[]`
   - Parse carefully or you'll miss citations

4. **Gemini citation wrapping:**
   - Gemini citations come as `[vertexaisearch.cloud.google.com/grounding-api-redirect/...]`
   - **You must follow each redirect to resolve the REAL cited URL**
   - Do NOT store the redirect URL; store the resolved destination

---

### Step 3: Classification (3 States Per Answer)

Classify each prompt × model × answer into exactly one of three states:

| State | Definition | Example |
|-------|-----------|---------|
| **RECOMMENDED (Green)** | The answer names your brand as a recommendation | "I'd recommend Shopify for small businesses because..." |
| **CITED, NOT CREDITED (Amber)** | Your domain appears in citations, but AI recommended competitors instead | AI cites your how-to guide but recommends Wix instead |
| **OMITTED (Red)** | Neither your brand nor domain appears | Your competitors are mentioned, but you're absent |

**For every classification, store:**
- Verbatim answer text
- All resolved citation URLs (with redirects followed)
- Which competitors were named
- Model, prompt, date

These are your "receipts"—evidence you can review later.

---

### Step 4: Mine Outreach Targets (The Gold)

Per market, aggregate all resolved citation URLs across every answer collected.

**Keep only URLs cited 3 or more times**, excluding:
- Your own domain (can't outreach to yourself)
- Competitor domains (can't pitch competitors)

**What remains:** Editorial guides, comparison articles, listicles, and resource pages that the AI repeatedly trusts for this market.

**Rank them by citation count.** This is your outreach hit list.

**Example:**
```
Market: Ecommerce Platforms
Citation counts (3+ only):

1. trustradius.com/products/shopify/reviews — cited 8 times
2. capterra.com/compare/shopify-vs-wix — cited 6 times
3. g2.com/products/shopify — cited 5 times
4. forbes.com/advisor/business/best-ecommerce-platforms — cited 5 times
5. pcmag.com/reviews/ecommerce-software — cited 4 times
6. indiehackers.com/post/best-platform-2026 — cited 3 times
```

Each of these is a concrete outreach action: pitch a mention, quote, or inclusion in that page.

---

### Step 5: Reporting (Per-Market Scorecard)

Create a per-market report with three components:

#### 1. Overall Scorecard
- **% winning** (green=1, amber=0.5, red=0)
- Win rate vs. competitor win rates
- Trend (improving or declining?)

#### 2. Outreach Target List
- URLs ranked by citation count
- Best actions for each (mention, quote, inclusion)

#### 3. Expandable Receipts
- Per-page rows showing:
  - The verbatim answer text
  - All resolved citations
  - Competitors named
  - Model + date

---

## Strategy Interpretation

### ChatGPT vs. Gemini Divergence (Normal, Diagnostic)

**Why they differ:** Different search backends.
- **Gemini:** Retrieves via Google (if your SEO is strong in Google rankings, Gemini cites you)
- **ChatGPT:** Retrieves via Bing + aggregator listicles

**If there's a huge ChatGPT-vs-Gemini gap:**
- It's not a bug; it's diagnostic
- **The fix:** Bing SEO + getting into the exact listicles ChatGPT cites (your outreach list will show these)

---

### Amber ("Cited, Not Credited") is Highest-Leverage

If the AI already reads your page, but recommends competitors instead:
- **The content needs clearer, brand-forward framing**
- The AI can find your insights but doesn't know they're *from* you
- Fix: Rewrite to emphasize your brand/unique POV early
- This often requires zero outreach—just better positioning of what you already have

---

### Verify "Omitted" with Receipts

Before believing you're truly omitted:
- Read the verbatim receipts
- Confirm your brand/domain really doesn't appear
- Sometimes a parsing error makes it look omitted when it isn't

---

## Deliverables

### 1. Collection Script
- Resumable (skip already-done prompts)
- Retry on failure
- Sequential/gentle (never hammer APIs)
- Stores raw responses in SQLite or Postgres

### 2. Results Database
```sql
CREATE TABLE prompts (
  id,
  market,
  intent_type, -- product or advisory
  text,
  created_date
);

CREATE TABLE results (
  id,
  prompt_id,
  model_name, -- gpt-4o-mini or gemini-2.0-flash
  classification, -- RECOMMENDED / CITED_NOT_CREDITED / OMITTED
  answer_text,
  cited_urls[], -- resolved URLs only
  competitors_named[],
  collected_date
);
```

### 3. Per-Market Report
- % winning scorecard
- Outreach targets ranked by citation count
- Expandable receipts showing raw data

### 4. One-Page Strategy Summary
- Where you win (markets with high %)
- Where you're invisible (markets with low %)
- Top 10 outreach targets overall
- 3 highest-leverage next actions

---

## How to Build This (Copyable Prompt)

**Run this prompt in Claude Code to build the system:**

```
I want you to build an "AI Visibility + Outreach Targets" analysis system 
for measuring where a brand appears in ChatGPT and Gemini answers.

INPUTS:
- Website domain (e.g., acme.com)
- Brand names and variants
- Direct competitors (domains + brand names)
- Markets/categories to test

DELIVERABLES:
1. Collection script (DataForSEO AI Optimization API, resumable, handles failures)
2. SQLite/Postgres database schema (prompts + results tables)
3. Per-market report generator (% winning, outreach targets, expandable receipts)
4. Strategy summary (1 page: wins/losses, top 10 targets, next actions)

PIPELINE:
1. Generate 2 prompts per market (product-intent + advisory-intent)
2. Call DataForSEO API for ChatGPT (gpt-4o-mini) + Gemini (gemini-2.0-flash)
3. Classify each answer: RECOMMENDED / CITED_NOT_CREDITED / OMITTED
4. Aggregate citation URLs, keep 3+ counts, exclude own domain + competitors
5. Generate reports grouped by market

GOTCHAS:
- No max_output_tokens (error 40501)
- Follow Gemini redirects to resolve real URLs
- Parse nested response (items → message → sections)
- Verify amber/omitted before believing them
```

---

## Starting Point: Pilot Run

**Before running full scale:**

1. Pick one market (e.g., "Ecommerce Platforms")
2. Generate ~10 prompts (5 product-intent, 5 advisory-intent)
3. Collect answers from both models
4. Show me the results and estimated cost
5. Get approval before scaling to all markets

**Expected pilot cost:** $5–20 depending on model mix (ChatGPT is cheap, Gemini drives costs)

---

## Related Pages

- [[fan-out-queries-and-ais.md]] — Discover fan-out queries to optimize for (offensive strategy)
- [[getting-cited-by-ai.md]] — The 5 tactics to get cited; this audit is a measurement framework for #1-3
- [[ai-overviews-local-search.md]] — How AI Overviews reshape local search visibility
- [[sales-and-lead-generation.md]] — Turn outreach targets into actual pitches

---

## The Bottom Line

You can't improve what you don't measure. This system gives you:
1. **Visibility audit** — Where you stand in AI answers vs. competitors
2. **Outreach blueprint** — The exact pages the AI trusts, ranked by influence
3. **Leverage points** — Amber classifications (cited but not credited) are often the fastest wins

Run a pilot. See where you're invisible. Pitch the pages that already cite you. Measure the impact in your next run.
