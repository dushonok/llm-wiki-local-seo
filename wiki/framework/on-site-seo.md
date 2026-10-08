---
type: framework
client: none
status: active
updated: 2026-10-08
sources:
  - "raw/framework/On-Page SEO Content Frameworks - How To Structure On-Page SEO Content · AI SEO Rank Expand Academy.md"
  - "raw/framework/Small moves  no moves (website updates) - AI SEO Rank Expand Academy.md"
  - "general SEO knowledge (not raw-sourced) — see traceability note in Meta Descriptions section below"
---

# On-Site SEO — Content Structure

## Core Principle: Structure > Length

On-page SEO is not about writing more — it's about **structuring information correctly**. Search engines and AI systems don't read pages like humans. They scan titles, headings (H1, H2), and page top sections.

**What determines ranking:**
- The *order and grouping of words (semantics)* determines how your content is understood
- The *top section of your page carries the most weight*

Get structure right → rank quickly. Get it wrong → good content still won't perform.

---

## Sidebar: Small Moves > No Moves (Iteration Over Perfection)

> **Real example:** A law firm owner spent a year planning a website redesign. It felt too big, so he shelved it. After getting an unqualified lead, he realized his old copy was attracting the wrong work. Instead of the whole-house rebuild, he made the smallest rewrite possible: clarify "what we do" and "who we serve," rewrite from the visitor's POV (less explaining), keep copy short and tight. Two one-hour sessions over two days. Result: A "cold" inquiry for exactly the work he wanted to grow.
>
> **Key insight:** Small incremental improvements beat waiting for the perfect redesign. Start with the smallest change that points you in the right direction. Iterate. Let future work show you what to optimize next.

**For microsites:** Don't wait for the perfect 10,000-word page. Ship 1,500 words, get traffic data, see which questions the search data reveals, then deepen those sections. The process compounds: small moves → clarity → better positioning → more qualified leads → then optimize deeper.

---

## The On-Page Content Structure Recipe

### 1. Title (≤ 60 characters)

- Clear and keyword-focused
- Aligned with search intent
- Front-load the benefit or answer

**Example:** "Local Plumbing Services in Denver | 24/7 Emergency"

### 2. Lead-In (2–3 sentences)

- Show you understand the problem
- Demonstrate you can solve it
- Set context for what follows

**Purpose:** Build trust and relevance immediately.

### 3. Answer Paragraph (≈ 50 words)

- Direct, factual answer to the main query
- Appears immediately (above the fold)
- No fluff or setup needed

**Why:** Google (and AI) reward pages that answer immediately.

### 4. Enticement / Transition ("Read On")

- Brief sentence encouraging deeper reading
- Creates pathway to detailed sections
- Natural flow to next heading

**Example:** "Here's how our process works and why we're different..."

### 5. H2 #1 – Core Intent Expansion

- Expand the main answer with detail and context
- Introduce supporting evidence or methodology
- Keep focus on primary intent

### 6. H2 #2+ – Supporting Topics & Entities

- Cover related subtopics and questions
- Address People Also Ask (PAA) queries
- Include relevant entities (neighborhoods, related services, alternatives)

### 7. Content Blocks (400–600 words per section)

- Provide depth within each H2 section
- Mention relevant entities and context
- Build semantic authority around topic

### 8. FAQ / PAA Section (Optional)

- Capture additional long-tail intent
- Pre-empt common follow-up questions
- Useful for featured snippets and voice search

---

## What Actually Moves Rankings

**Strong factors:**
- ✅ Semantic alignment in **title + H1 + H2s**
- ✅ Clear answer **at the top of the page**
- ✅ Coverage of **related entities and subtopics**
- ✅ Logical structure that reads like a **table of contents**

**Weak factors (don't rely on alone):**
- ❌ Word count alone
- ❌ Keyword density
- ❌ Fluffy intro text

---

## Structure vs. Quality: The Reality Check

**Structure gets you in. Quality keeps you there.**

Structure alone may get initial ranking (Google scans structure first), but over time Google evaluates:
- **Depth** — Do you cover the topic thoroughly?
- **Accuracy** — Is the information correct and up-to-date?
- **Value** — Does this actually help the user/AI answer follow-up questions?

---

## How to Apply This to Local SEO Pages

For location or service pages, structure becomes even more critical because AI Overviews rely on clear entity and contextual signals.

**Structure template for local service page:**

1. **Title:** "[Service] in [City/Neighborhood]"
2. **Lead-in:** Problem statement + unique value (2 sentences)
3. **Answer:** "We provide [service] to [areas] with [key differentiator]" (1–2 sentences)
4. **Transition:** "Here's what sets us apart..."
5. **H2 #1:** "Why Choose [Company] for [Service]?"
6. **H2 #2:** "Service Areas: [Neighborhoods/ZIP codes]"
7. **H2 #3:** "[Service] Process & Timeline"
8. **H2 #4:** "Reviews & Results"
9. **FAQ:** 5–6 common questions specific to service + location

**Entity signals to include:**
- Specific neighborhoods, ZIP codes, landmarks
- Related services (cross-links to other pages)
- Company history/credentials (LocalBusiness schema)
- Customer reviews (aggregate rating schema)

---

---

## Meta Descriptions: Town Lists — State Abbreviation or Not?

> *Not sourced from a raw capture — general SEO knowledge, flagged here for
> traceability (same convention as the GBP-verification note in
> [`local-seo-checklist.md`](local-seo-checklist.md) and the OG-tags page,
> [`open-graph-and-metadata.md`](open-graph-and-metadata.md)).*

**Question:** Services/Service-Area meta descriptions list towns without the
state ("Hanover, Littlestown" instead of "Hanover, PA, Littlestown, PA") — is
that a problem?

**Short answer: generally fine, with one caveat.**

- Meta descriptions are **not a direct Google ranking signal** — Google often
  rewrites/truncates them anyway. Their job is influencing **CTR** in the SERP
  snippet, not indexing or geo-relevance scoring.
- Character budget matters more than repetition: meta descriptions truncate
  around ~155–160 characters. Dropping the repeated ", PA" after every town
  buys room to list more towns or add a stronger CTA — which helps CTR.
- The actual geo/entity signal for rankings and AI Overviews comes from
  elsewhere on the page: H1, body copy, `LocalBusiness`/`Service` schema
  (`areaServed`), URL structure, and GBP service areas (see entity-signals
  guidance above and in `local-seo-checklist.md` §4–5). As long as the state
  appears in those places, the meta description doesn't need to repeat it.

**Caveat — town-name collisions:** if a town name is common across multiple
states (Hanover, Springfield, Franklin, Clinton, etc.), dropping the state
removes the only disambiguating signal in that snippet — a real risk if the
description is read out of context (e.g., surfaced in an AI Overview outside
the local search context). For unambiguous/small town names, this risk is
negligible.

**Recommendation:** keep the state at least once per description (e.g.,
"...serving Hanover, Littlestown & nearby PA towns") rather than dropping it
entirely — cheaper on character budget than repeating "PA" after every town,
but preserves the geo anchor. Always confirm schema/H1/body still carry full
"Town, State" pairs regardless of what the meta description does.

---

## Diagnostic Pattern: Legal/Boilerplate Page Outranking the Service Page

> *Not sourced from a raw capture — general SEO diagnostic reasoning, flagged
> here for traceability (same convention as the other general-knowledge
> sections in this file).*

**Symptom:** Rank tracking shows a legal/boilerplate page (`/complaints-policy`,
`/disclaimer`, `/terms`, `/privacy`, `/accessibility`) as the site's best — or
only — result for *hyperlocal commercial terms*, while the page actually built
for that service/location sits far down the results (e.g., policy page on
page 1 for 7 target terms; the real service pages at #54–#55 for the same
terms).

**Why it happens:** Usually not pure "competition" between the two pages — it's
a signal-mismatch problem:
- **Internal link anchor text** disproportionately points keyword-rich anchors
  at the policy page (e.g., a footer link) while the service pages get generic
  anchor text ("Learn more") or thin internal linking.
- **Service page content is weak** relative to the query — thin, missing
  entity signals (neighborhood/ZIP/landmark), weak title/H1, no schema — so
  Google has little to work with even once the competing page is removed.

**Fix (don't just noindex and stop):**
1. **Noindex the legal/boilerplate pages** — add
   `<meta name="robots" content="noindex, follow">` (not a `robots.txt`
   disallow — that would stop Google from seeing the tag and from passing
   link equity through). These pages have no commercial search demand of
   their own, so there's no downside to deindexing them. Keep them live and
   linked normally; this is an indexing decision, not a visibility/compliance
   one.
2. **Redirect internal-link anchor text** — point the hyperlocal commercial
   anchors that were landing on the policy page toward the actual service
   pages instead.
3. **Rebuild the service pages against the Content Structure Recipe above**
   (title, lead-in, answer paragraph, entity signals, schema) — a page
   ranking #54–55 for its own target term almost always has a content/entity
   gap, not just a cannibalization problem.
4. **Request re-crawl via GSC URL Inspection** for both the noindexed pages
   and the rebuilt service pages to speed up reprocessing.
5. **Monitor rank tracker 2–4 weeks** — noindex + content fixes aren't
   instant; give Google time to re-evaluate which page should rank.

**Takeaway:** noindexing the legal pages is correct and low-risk, but it only
removes a false competitor — it doesn't guarantee the service page wins the
slot unless the anchor-text and content gaps are fixed too.

---

## Diagnostic Pattern: Ranking URL Flapping Between Two Pages (Keyword Cannibalization)

> *Not sourced from a raw capture — general SEO diagnostic reasoning, flagged
> here for traceability (same convention as the other general-knowledge
> sections in this file).*

**Symptom:** Rank tracking shows the ranking URL for a *single target
keyword* switching between two different pages day to day — e.g. an FAQ page
ranks Monday, a location/township page ranks Tuesday, the FAQ page again
Wednesday. Position moves (often worsens) every time the switch happens, even
though the keyword itself hasn't lost relevance.

**Why it happens:** This is different from the legal-page-outranking pattern
above (where one wrong page clearly, persistently wins). Here, Google's
indexing/ranking system has **two of your own pages that both look like
plausible answers** to the same query and hasn't settled on which one to
treat as canonical for it:
- Both pages share overlapping title/H1/body-copy keyword targeting — e.g.
  the FAQ page has a Q&A entry that answers the exact same question the
  township page is built to rank for ("How much does mold remediation cost
  in [Township]?" appearing almost verbatim on both).
- Internal links to that query's topic are split between the two pages
  instead of consistently pointing at one.
- Neither page has a strong enough standalone signal (backlinks, dwell time,
  CTR) to decisively win, so Google keeps re-testing both in a swap pattern —
  this is Google's own uncertainty showing up in the SERP, not something the
  site is doing "right" that's being punished.

**Why the position moves every time it switches:** the two pages don't have
identical authority/relevance scores. Each time Google re-evaluates and picks
the weaker of the two candidates, it ranks lower; when it picks the stronger
one, it ranks higher. The *flapping itself* — not just which page wins — is
what's suppressing average position, because the weaker page is dragging the
average down every other day.

**Fix:**
1. **Decide the one true target page** for that specific query — for a
   hyperlocal commercial term ("mold remediation cost in [Township]"), that
   should almost always be the township/location page, not the FAQ page.
   The FAQ page should serve broader, non-location-specific questions.
2. **De-duplicate the overlapping content.** If the FAQ page has an entry
   that restates the exact question the township page targets, either
   remove/generalize that FAQ entry (drop the township name from it) or
   trim it to a one-line answer that links to the township page for the
   full answer — don't let both pages carry a full, self-contained answer
   to the same hyperlocal query.
3. **Consolidate internal links.** Audit every internal link whose anchor
   text references that township + service combination; point all of them
   at the township page. Don't link that phrase to the FAQ page anywhere.
4. **Add a canonical signal if content must stay similar.** If the overlap
   can't be fully removed (e.g. the FAQ entry has to exist for site-wide FAQ
   schema), do not canonical the FAQ page to the township page unless the FAQ
   page truly has no independent query of its own to serve — canonicalizing
   away a page's own long-tail value is a bigger cost than the overlap. Prefer
   content differentiation over canonicalization here.
5. **Strengthen the township page's standalone signals** per the Content
   Structure Recipe above (clear answer in first ~50 words, entity signals —
   neighborhood/ZIP/landmark — `Service`/`LocalBusiness` schema with
   `areaServed`) so it has a decisive relevance edge over the FAQ page for
   that query, not just a technical nudge.
6. **Check GSC URL Inspection's "Google-selected canonical"** for the query
   in question — it will show which URL Google is currently treating as
   canonical for that content cluster, confirming whether the fix above
   needs to happen on the FAQ page, the township page, or both.
7. **Monitor rank tracker 2–4 weeks** after the fix — like the legal-page
   pattern above, de-cannibalization isn't instant; the flapping should
   settle into one consistent URL once Google re-crawls both pages and the
   signal overlap is gone.

**Takeaway:** URL flapping is Google's own confusion, not a penalty — but it
caps your visible ranking at whatever the *weaker* of the two competing pages
can achieve. Fixing it is about giving Google exactly one unambiguous
candidate per query, not about generating more content.

---

## Implementation Checklist

- ☐ Rewrite title to be ≤ 60 characters, keyword-focused
- ☐ Add 2–3 sentence lead-in showing problem understanding
- ☐ Move answer to paragraph 2 (≈ 50 words)
- ☐ Restructure heading hierarchy (one H1, logical H2/H3 flow)
- ☐ Front-load key entities (location, service type) in top 3 sections
- ☐ Expand core intent under H2 #1 (supporting details)
- ☐ Cover 2–4 supporting topics under H2 #2+
- ☐ Aim for 400–600 words per main section
- ☐ Add FAQ with local/service-specific questions
- ☐ Validate semantic HTML structure
