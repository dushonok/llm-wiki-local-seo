---
type: framework-foundation
client: none
status: active
updated: 2026-09-26
sources:
  - "raw/framework/1. SEO Fundamentals - Learn Technical SEO - The Beginner's Guide to Technical SEO.md"
  - "raw/framework/1. SEO Fundamentals - Learn Technical SEO - Google Crawling and Indexing  Google Search Central    Documentation.md"
  - "raw/framework/1. SEO Fundamentals - Learn Technical SEO - Technical optimization.md"
---

# Technical SEO Fundamentals

**Purpose:** Theoretical foundation for understanding how search engines crawl, index, and rank websites. This is conceptual knowledge supporting the tactical [[on-site-seo.md]] and [[external-seo-microsite-tactics.md]] guides.

**Audience:** Anyone building or optimizing a site who wants to understand *why* certain technical practices matter.

---

## How Search Engines Work

### The Three-Phase Process

Search engines (Google, Bing) follow a three-step process to make your content discoverable:

1. **Crawling** — A bot (Googlebot) discovers your site by following links from other pages and your sitemap. It reads the HTML, CSS, and JavaScript to understand page structure and content.

2. **Indexing** — Google processes what it crawled and stores information about your pages in a massive index. During this phase, Google:
   - Parses content to understand topics and entities
   - Identifies text, images, videos, and structured data
   - Evaluates page quality, freshness, and relevance
   - May filter out duplicates or low-quality content

3. **Ranking** — When someone searches, Google retrieves indexed pages matching the query and ranks them based on hundreds of signals (relevance, authority, user experience, etc.).

**Key insight:** If your site isn't crawlable or indexable, it won't rank — no matter how good the content is.

---

## Crawlability: Making Your Site Easy to Discover

### What Googlebot Needs

- **Clear site structure** — Logical hierarchy (homepage → categories → pages) makes crawling efficient
- **Internal links** — Links between your own pages guide the crawler to all important content
- **Sitemap** — An XML file listing all your pages (tells Google what exists)
- **Robots.txt** — A file that tells crawlers which parts of your site to crawl (or block)
- **No crawl traps** — Avoid infinite loops, duplicate parameters, or crawl-blocking redirects

### What Blocks Crawling

- JavaScript-only content (older crawlers struggle with heavy JS)
- Nofollow links (tell crawler "don't follow this link")
- Blocked by robots.txt or meta robots tag
- Very deep nesting (pages buried 10+ levels deep rarely get crawled)
- Server errors (500s, timeouts prevent crawling)

---

## Indexability: Getting Your Pages Into Google's Database

### What Google Needs to Index Your Page

- **Unique, sufficient content** — At least 100–150 words of original content (thin pages may not be indexed)
- **Indexable HTML** — Page must be HTML-based (JSON, PDF, images alone won't index in the traditional way)
- **No indexing blocks** — No `noindex` tag, no `robots.txt` block, no `Disallow: /` in robots.txt
- **Crawlable** — Page must be discoverable (see Crawlability section above)

### Indexing Issues

- **Duplicate content** — If Google finds multiple versions of the same content, only one gets indexed (canonical tags help signal which one)
- **Thin content** — Very short pages (under 100 words) may not index
- **Soft 404s** — Pages that return 200 status but contain error messages confuse indexing
- **Noindex by mistake** — A stray `<meta name="robots" content="noindex">` tag blocks indexing

**How to verify indexing:** Search `site:yourdomain.com` in Google to see indexed pages.

---

## Ranking Signals: Why Pages Rank

Once indexed, Google ranks pages based on signals including:

### Relevance Signals
- **Keyword match** — Does the query appear in the title, H1, and body?
- **Topic authority** — Does the page cover the topic deeply?
- **Entity recognition** — Does Google understand the people, places, things mentioned?
- **User intent match** — Is this page the type of result users want (local, commercial, informational)?

### Authority Signals
- **Backlinks** — Links from other sites act as votes of confidence
- **Domain age and history** — Older, stable domains typically rank better than new ones
- **Page freshness** — Recently updated pages may rank higher for current topics

### User Experience Signals
- **Page speed** — Faster pages rank better (mobile and desktop)
- **Mobile-friendliness** — Must render well on phones
- **Core Web Vitals** — Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), First Input Delay (FID)
- **HTTPS/SSL** — Secure sites rank slightly higher

### Content Quality Signals
- **E-E-A-T** — Expertise, Experience, Authoritativeness, Trustworthiness (especially for YMYL topics like health, finance, legal)
- **Originality** — Unique, well-researched content ranks better than paraphrased content
- **Readability** — Clear structure, proper headings, short paragraphs help

---

## Core Technical Best Practices

### Site Structure
- Organize pages into logical categories
- Use clear, descriptive URLs (e.g., `/services/emergency-plumbing` not `/p?id=123`)
- Limit pages to 3 clicks from homepage

### Crawlability & Indexing
- Create and submit an XML sitemap
- Use `robots.txt` to allow crawling of key areas
- Avoid crawl traps (redirects loops, infinite parameter variations)
- Implement canonical tags for duplicate content

### Performance
- Optimize images (compress, lazy-load)
- Minimize CSS/JavaScript
- Use a CDN to serve content faster
- Test with Google PageSpeed Insights and GTmetrix

### Mobile & UX
- Design mobile-first (responsive design)
- Test on actual mobile devices
- Ensure clickable elements are 48x48px minimum
- Avoid intrusive interstitials (pop-ups)

### Security & Trust
- Use HTTPS (SSL certificate)
- Fix mixed-content warnings (HTTP resources on HTTPS page)
- Implement structured data (schema.org markup)
- Display trust signals (contact info, privacy policy, about page)

---

## Structured Data & Schema Markup

**Structured data** uses schema.org markup to tell Google exactly what type of content is on your page. Examples:

- **`Organization`** — Business name, logo, contact info
- **`LocalBusiness`** — Address, phone, hours, reviews
- **`Product`** — Name, price, description, reviews
- **`FAQPage`** — Q&A format that appears in SERP snippets
- **`Article`** — Author, publish date, headline

Structured data doesn't directly rank you higher, but it:
- Helps Google understand your content
- Enables rich snippets (star ratings, images) in search results
- Supports AI Overviews and Knowledge Panels

---

## Relationship to Tactical SEO

This foundation explains **why** the tactical pages matter:

- [[on-site-seo.md]] builds on crawlability + indexing + ranking signals to optimize page content
- [[external-seo-microsite-tactics.md]] focuses on authority signals (backlinks, citations)
- [[getting-cited-by-ai.md]] combines content quality + entity signals + social proof to trigger AI citations

Understanding these fundamentals helps you make better decisions about *which* tactics to prioritize.

---

## Next Steps

- For **tactical on-page optimization,** see [[on-site-seo.md]]
- For **tactical off-page optimization,** see [[external-seo-microsite-tactics.md]]
- For **keyword research fundamentals,** see [[keyword-research.md]]
