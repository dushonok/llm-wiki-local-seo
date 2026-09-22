---
type: framework
client: none
status: active
updated: 2026-09-22
sources:
  - "general SEO/Open Graph knowledge — not sourced from a raw call or capture; flagged here for traceability, same convention as the GBP-verification note in local-seo-checklist.md"
---

# Open Graph & Social Metadata

**Core Principle:** Open Graph (OG) tags are not a Google ranking factor — Google has
confirmed they don't influence organic or local pack rankings. They exist for social
platforms (Facebook, LinkedIn, Slack, Discord, iMessage previews) to render link
previews. Treat them as low-priority polish, not a lever to pull for local rankings.

---

## Where OG tags actually matter

1. **Click-through rate on social shares** — Controls the preview card (image, title,
   description) when a page is shared on Facebook/LinkedIn/texted. Better preview →
   more clicks → more traffic, which can indirectly feed other signals (links,
   mentions) over time.

2. **Citation/directory tool fallback** — Some citation submission tools and directory
   scrapers use OG tags as a fallback for title/description/image when no other
   structured data is present. Missing OG tags can mean a directory listing pulls
   messy fallback text or no image. Relevant to this wiki's citations pipeline —
   see `citations-strategy.md`.

3. **AI crawlers / LLM summarization** — AI Overviews, Perplexity, and ChatGPT search
   sometimes use `og:description` as one input when summarizing a page, especially
   when `<meta name="description">` is absent or weak. It's a secondary signal behind
   actual content and `LocalBusiness` schema, but it's a near-zero-cost addition. Ties
   into this wiki's broader "getting cited by AI" strategy — see
   `getting-cited-by-ai.md`.

## Where OG tags don't matter

- No effect on Google organic rankings.
- No effect on Google Business Profile / Map Pack rankings.
- Not a substitute for `LocalBusiness` schema, title tags, or meta descriptions.

## Priority stack for local on-page SEO

For a local business page, rank effort in this order — OG tags sit near the bottom:

1. Title tag / meta description
2. `LocalBusiness` schema markup (NAP, hours, geo, reviews) — see `local-seo-checklist.md` §4
3. H1/content optimization, city + service targeting
4. Internal linking, NAP consistency
5. Page speed / mobile
6. **Open Graph tags** — social/AI-fallback polish, ~5 minutes of work

## Recommended minimum tag set

Add to every microsite/location page:

```html
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta property="og:image" content="..." />
<meta property="og:type" content="business.business" />
<meta property="og:locale" content="en_US" />
<meta property="og:url" content="..." />
```

## Bottom line

Low effort, no downside, but not a ranking lever. Implement across all microsites as
a standard build-checklist item, but don't spend optimization time here at the
expense of schema markup, citations, or content — those move rankings; OG tags don't.
