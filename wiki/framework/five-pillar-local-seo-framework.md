---
type: framework
client: none
status: active
updated: 2026-10-28
sources:
  - "raw/framework/The Five Pillar Local SEO Checklist - Rank Expand Academy.md"
---

# The Five Pillar Local SEO Framework

**Foundation:** Built from six weeks of daily ranking checks on 61 brand-new sites and twenty audits of member sites (October 2026).

**Core Finding:** Every site that reached the top 15 did it within 48 hours of a big republish, and every one that held page one had Pillars 2 and 4 complete. Pages alone got sites into the twenties and no further. Profiles alone ranked by themselves while the site stayed on page 3. **The sites that did both are the ones still there.**

---

## How to Use This Framework

1. Open the site in one tab and this checklist in another
2. Work the five pillars in order
3. Tick what passes; each pillar ends with a pass line
4. A site that passes all five is built. A site that fails one has its next job. A site that fails two or more is not ready for profiles yet—fix the on-site pillars first.

---

## Pillar 1: Foundation (5 minutes)

**The boring layer that silently blocks ranking.**

- [ ] **One host:** http, https, www and non-www all land on one address with a 301 redirect
  - Type all four into the browser
  - A third of audited sites served two or four copies (blocker)

- [ ] **Real HTML:** View source on the homepage and find your own paragraphs in it
  - An empty shell that renders in the browser is the biggest handicap a new domain can carry

- [ ] **Domain says the service and the town, in the order people say it**
  - Example: "Roof Repair in Baytown, TX" not "Your Roofing Solution"
  - The extension did not decide anything in the contest. The name did.

- [ ] **Canonical tag on every page pointing at itself**

- [ ] **Sitemap with real last modified dates, not one build date on every URL**

- [ ] **A real 404 page that returns a 404, set to noindex**

- [ ] **Thank you page set to noindex**

- [ ] **Images in WebP or AVIF, each with alt text that describes the picture**
  - Half the images on audited sites had no alt at all (blocker)

**Pass if:** All eight tick. None of these rank you. All of them stop you.

---

## Pillar 2: Entity (5 minutes)

**What the site says about who you are. Google ranks businesses for local searches. The website is evidence.**

- [ ] **Business name, phone, hours and email at the site's own domain, in the footer of every page**
  - Not Gmail. Same spelling everywhere.

- [ ] **A street address only if the business has a real one. Otherwise a declared service area.**
  - Never a placeholder. Two contestants used "123 Baltimore St"
  - Address alone predicted nothing

- [ ] **LocalBusiness schema, or the specific type (RoofingContractor, Plumber, HomeAndConstructionBusiness)**
  - Not plain Organization

- [ ] **areaServed lists the towns actually served**
  - Geo coordinates if there is an address

- [ ] **A sameAs array in the schema, filled with every profile from Pillar 4**
  - Present even if empty at launch
  - **This is the connection line that tells Google where else this business exists**
  - Empty on 18 of 20 audited sites (critical miss)

- [ ] **Name, phone and address identical in schema, footer and every profile**
  - Suite C is not Ste. C
  - Area code matches the market (a 928 number on a Phoenix site and a 747 number on a Mesa site both got flagged this month)

**Pass if:** Every box ticks and the sameAs array exists. A business that claims to exist and cannot prove it fails here.

**Schema Template:** See bottom of this page.

---

## Pillar 3: Pages (10 minutes)

**The architecture that got sites into the top twenty.**

- [ ] **Homepage 1,200 to 2,000 words. H1 is the service and the town, not a slogan.**
  - Example: "Roof Repair in Baytown, TX" not "Protecting What Matters Most"

- [ ] **One or two service pages, 800 to 1,200 words each**
  - What the problem looks like
  - What the work involves
  - A cost section
  - Why you
  - The process
  - A FAQ
  - More services = the next site, not a bigger one

- [ ] **A cost page with real ranges**
  - Sourced numbers beat invented ones
  - Highest intent page on the site. Most skipped.

- [ ] **Town and neighborhood pages about that place**
  - Housing stock, local permit rules, what soil/weather does to this problem
  - If the town name could be swapped and the page still reads true, it fails
  - **The 18-page site with real township detail beat the 116-page site**

- [ ] **FAQPage markup on the home, every service page and every town page**
  - Six questions on a page with no markup is the most common miss

- [ ] **Services hub and service areas hub exist, link to every child, and have an intro**
  - Blueprint minimum: 150-word intro plus links

- [ ] **Outbound links to sources**
  - State agency, city permit page, manufacturer bulletin, EPA, etc.
  - Almost no local sites link out. The ones that held did.

- [ ] **Real photos: jobs, crew, before/after**
  - Not four stock images reused on thirty pages

- [ ] **Footer and template headings are not H2s on every page**

**Pass if:** The H1 carries the keyword, every commercial page has FAQ markup, and at least one town page could only be about that town.

---

## Pillar 4: Footprint (5 minutes to check, 1 week to build)

**Everything from Pillar 2, repeated on websites Google already trusts. This is where every page one result in the contest came from.**

### Primary Profiles (Must-Have for Page One)

- [ ] **Facebook business page** with exact name, phone and website
  - Best position seen: #4

- [ ] **Patch business listing** on the town's Patch site
  - Best: #6, reached page one

- [ ] **MapQuest business listing**
  - Best: #3, highest of any profile

- [ ] **Houzz pro profile** with 3–5 photos
  - Best: #4

- [ ] **BBB free business profile**
  - Best: #8, reached page one

- [ ] **Clutch company profile**
  - Best: #11

- [ ] **YouTube channel** named after the business with one 60-second video
  - Best: #11, the video ranked by itself

- [ ] **One press release** through a syndication service
  - Headline = business + service + town, linking to the site
  - Best: #7, landed on regional TV and newspaper sites

### Secondary Profiles (Lower ROI, but still useful)

- [ ] **Birdeye, Crunchbase, Pinterest, ProvenExpert, Yelp**
  - Cheap, never seen above #18

### Critical Connection

- [ ] **Every live profile URL added to the sameAs array in schema**
  - This is the connection. Without it, profiles rank and the site does not.

### Special Cases

- [ ] **Google Business Profile**
  - Only when the business has a real address or verifiable service area
  - Skip at launch. A directory with a profile never ranked.

### Skip (No ROI)

**Do not build:** LinkedIn, TikTok, Reddit, Quora, Hotfrog, Brownbook, Medium, Substack, Tumblr, Linktree and the forty small free directories. Built by contestants, never seen in the top 40.

**Pass if:** Eight or more of the first nine exist, match the site exactly, link to it, and are in sameAs.

---

## Pillar 5: Ship & Measure (5 minutes to set up, then daily)

**How you work.**

- [ ] **Rankings are checked pinned to the town with personalization off**
  - Checking from your desk shows 10–15 spots better than reality. Every time.
  - Method: See "Pinned Search Method" below

- [ ] **Positions are written down daily. Trends are judged at three weeks, not three days.**

- [ ] **Changes ship in batches**
  - Rebuild, republish, update sitemap dates, check in 48 hours
  - Every top 15 entry in the contest followed a big republish within two days
  - Nobody who trickled moved

- [ ] **The first jump is treated as a test, not a result**
  - Site is left alone for three weeks after a ship
  - Four sites visited the top 10 and left within a week
  - The one on page one was untouched for three weeks

- [ ] **A site stuck in the twenties gets Pillar 2 and Pillar 4 work, not more pages**
  - Nine sites sat in a block at #21–30 for two weeks with the same build and the same result

**Pass if:** You can say where the site ranked yesterday from the town, and what shipped on which date.

---

## Pinned Search Method

Google shows a searcher in the town different results from a searcher at your desk. To see what the customer sees, build a search URL with three things: personalization off, English and US, and the location pinned to the town.

### Step 1: Start with the query

```
https://www.google.com/search?q=roof+repair+baytown+tx&hl=en&gl=us&pws=0
```

`pws=0` turns personalization off. `hl` and `gl` set language and country.

### Step 2: Add the location pin

Append `&uule=` followed by a code for the town. The code is built from the canonical place name Google uses (e.g., Baytown, Texas, United States). The format is:
- Fixed prefix: `w+CAIQICI`
- One character encoding the length of the name
- The name in base64 with no padding

**Code:**
```
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
name = "Baytown,Texas,United States"
uule = "w+CAIQICI" + table[len(name)] + base64(name).rstrip("=")
```

**Worked Example for Gettysburg, Pennsylvania** (37 characters, so the length character is the 38th in the table, "l"):
```
&uule=w+CAIQICIlR2V0dHlzYnVyZyxQZW5uc3lsdmFuaWEsVW5pdGVkIFN0YXRlcw
```

### Step 3: Confirm it worked

Scroll to the bottom of the results. The footer must say the town name and "Results are not personalized". If it shows your own city or "Results are personalized", the pin did not take.

**Count organic results only:** Skip ads, the map pack, the AI box and the "Discussions and forums" block. Best URL per domain counts.

### Step 4: Pace it

Ten page loads a day, ten seconds apart, in a normal browser. Faster than that and Google starts asking if you are a robot.

---

## Schema Template

Paste into the head of every page, fill every field, delete nothing. Use the specific business type if one fits (RoofingContractor, Plumber, Electrician, HomeAndConstructionBusiness). Leave out streetAddress and geo if there is no real address; keep areaServed. The sameAs array starts empty and grows as profiles go live.

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "@id": "https://www.example.com/#business",
  "name": "Example Roof Repair",
  "url": "https://www.example.com/",
  "telephone": "+1-281-555-0100",
  "email": "hello@example.com",
  "image": "https://www.example.com/images/crew.jpg",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "12837 Louetta Rd, Suite 1",
    "addressLocality": "Baytown",
    "addressRegion": "TX",
    "postalCode": "77520",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 29.7355, "longitude": -94.9774 },
  "areaServed": [
    { "@type": "City", "name": "Baytown, TX" },
    { "@type": "City", "name": "Mont Belvieu, TX" },
    { "@type": "City", "name": "Highlands, TX" }
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens": "08:00", "closes": "18:00"
  }],
  "sameAs": [
    "https://www.facebook.com/examplebusiness",
    "https://patch.com/texas/baytown/business/listing/000000/example",
    "https://www.mapquest.com/us/texas/example-000000",
    "https://www.houzz.com/pro/examplebusiness",
    "https://www.bbb.org/us/tx/baytown/profile/roofing/example-0000-000",
    "https://clutch.co/profile/example-business",
    "https://www.youtube.com/@examplebusiness"
  ]
}
</script>
```

**Extensions:**
- Service pages add a Service node whose provider is the @id above
- Every page with questions adds a FAQPage node
- Every inner page adds a BreadcrumbList

---

## Score Card

| Pillar | Pass | Next Job If It Fails |
|--------|------|---------------------|
| 1 Foundation | ☐ | Redirects, real HTML, sitemap dates. One afternoon. |
| 2 Entity | ☐ | LocalBusiness schema with sameAs, matching NAP. One afternoon. |
| 3 Pages | ☐ | Keyword H1, FAQ markup, a town page that is about the town. One week. |
| 4 Footprint | ☐ | The first nine profiles, then sameAs. One week, then wait. |
| 5 Ship & Measure | ☐ | Pinned checks daily, ship in batches, hands off for three weeks. |

**Reality Check:** Most sites pass two or three. Almost none pass all five. The ones that pass all five are the ones that hold page one instead of visiting it.

---

## Related Pages

- [[microsite-launch-checklist.md]] — Implementation checklist for launch (complements Pillar 1)
- [[on-site-seo.md]] — Content structure and optimization (details for Pillar 3)
- [[backlinks.md]] — Authority building and profiles (details for Pillar 4)
- [[getting-cited-by-ai.md]] — AI citation strategy (relates to Pillar 2 & 4)
- [[ai-overviews-local-search.md]] — AI Overviews and visibility (relates to all pillars)
