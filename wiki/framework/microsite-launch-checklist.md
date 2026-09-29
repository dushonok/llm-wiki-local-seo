---
type: framework
client: none
status: active
updated: 2026-09-29
sources:
  - "raw/framework/Day 37 of My 90-Day Challenge A Wrong Sitemap Found on a Live Site - AI SEO Rank Expand Academy.md"
---

# Microsite Launch Checklist

**Purpose:** Pre-launch validation checklist for microsites. A real-world case study caught a critical error (wrong domain in sitemap) hours before going live—this checklist prevents similar mistakes.

**When to use:** After your microsite is built and content-complete, but *before* you flip the indexing switch (remove `noindex` tag).

---

## The Case Study: What Went Wrong

A microsite was built correctly in all respects, but the **sitemap listed URLs on the wrong domain** (.ca instead of .com). This is a real example from a live project:

**The Problem:**
- Sitemap had 46 URLs pointing to `.ca` domain (which someone else owned)
- Pages had no canonical tags
- Site was still `noindex`, so no damage was done yet
- But if launched like this, the site would have started with wrong URLs indexed

**Root cause:** The hostname (domain) was never verified in the build checks.

**Result:** New check added to prevent this; sitemap re-generated with correct domain.

**Lesson:** A site can look perfect and still have critical infrastructure errors nobody sees.

---

## Pre-Launch Validation Checklist

### Phase 1: Infrastructure & Domain (Before Content)

- [ ] **Domain/Hostname Verification**
  - [ ] Confirm site is built on the correct domain (not a test domain)
  - [ ] Check DNS records point to correct hosting
  - [ ] Verify domain is purchased and renews on schedule
  - [ ] HTTPS/SSL certificate is active (no warnings)

- [ ] **Sitemap Validation**
  - [ ] Sitemap exists at `/sitemap.xml`
  - [ ] All URLs in sitemap use the correct domain (no test domains, no `.ca` when you need `.com`)
  - [ ] Sitemap is valid XML (use Google's Sitemap Testing tool or XML validator)
  - [ ] Sitemap submittable to Google Search Console without errors

- [ ] **Canonical Tags**
  - [ ] Every page has a canonical tag
  - [ ] Canonical tag points to the page itself (self-referential)
  - [ ] No cross-domain canonicals (e.g., don't point to someone else's site)
  - [ ] Example: `<link rel="canonical" href="https://yoursite.com/page">`

- [ ] **Robots.txt**
  - [ ] `robots.txt` exists and is valid
  - [ ] Does NOT block the entire site with `Disallow: /` (unless you want noindex)
  - [ ] Allows Googlebot to crawl key pages
  - [ ] Example for live site: `Disallow: /admin` (not `Disallow: /`)

### Phase 2: Content & Schema (During/After Content)

- [ ] **No Broken Links**
  - [ ] Use a crawler (Ahrefs, Screaming Frog, Lighthouse) to check for 404s
  - [ ] Internal links work
  - [ ] External links (citations, resources) are live
  - [ ] Forms submit without errors

- [ ] **Schema Validation**
  - [ ] LocalBusiness schema is present and valid
  - [ ] FAQPage schema is valid (if you have FAQ section)
  - [ ] Service schema is present (if offering services)
  - [ ] Use Google's Rich Results Test to validate all schema
  - [ ] No schema errors or warnings

- [ ] **Meta Tags**
  - [ ] Meta descriptions are unique and under 160 characters
  - [ ] Title tags are unique and 50–60 characters
  - [ ] All pages have meaningful titles/descriptions
  - [ ] Open Graph (OG) tags present (optional but recommended)

- [ ] **Images & Media**
  - [ ] All images have alt text
  - [ ] Images are compressed (use TinyPNG or similar)
  - [ ] No broken image links
  - [ ] Videos load without errors
  - [ ] All media files are copyright-clear

- [ ] **No Duplicate Content**
  - [ ] Check for accidental duplicate pages
  - [ ] No boilerplate content copied across service pages without variation
  - [ ] Pagination and sort parameters don't create duplicate content
  - [ ] Use Ahrefs or Screaming Frog to detect duplicates

- [ ] **Accessibility**
  - [ ] Heading hierarchy is correct (no skipped levels like H1 → H3)
  - [ ] Text has sufficient contrast (readable on mobile)
  - [ ] No auto-playing audio/video
  - [ ] Form labels are properly associated with inputs

### Phase 3: Performance & Mobile (Before Launch)

- [ ] **Page Speed**
  - [ ] Core Web Vitals pass (use PageSpeed Insights)
  - [ ] Largest Contentful Paint (LCP): < 2.5s
  - [ ] Cumulative Layout Shift (CLS): < 0.1
  - [ ] First Input Delay (FID): < 100ms
  - [ ] Page loads in < 3 seconds on 4G mobile

- [ ] **Mobile Rendering**
  - [ ] Site is fully responsive (test on mobile device, not just browser)
  - [ ] Text is readable without zooming
  - [ ] Links/buttons are tappable (48px minimum)
  - [ ] No horizontal scrolling
  - [ ] Viewport meta tag is present

- [ ] **Cross-Browser Testing**
  - [ ] Site renders correctly in Chrome, Firefox, Safari, Edge
  - [ ] No CSS/JavaScript errors in console (use browser DevTools)

### Phase 4: Search Console & Indexing (Pre-Launch)

- [ ] **Google Search Console Setup**
  - [ ] GSC property created and verified
  - [ ] Both www and non-www versions added (or redirects configured)
  - [ ] Sitemap submitted in GSC
  - [ ] URL inspection tool works (no "URL not on Google" errors)

- [ ] **Noindex Check (Before Removing)**
  - [ ] Site currently has `<meta name="robots" content="noindex">` (while in staging)
  - [ ] Confirmed no pages are accidentally noindex'd (check via GSC URL Inspection)
  - [ ] Ready to remove noindex tag before launch

- [ ] **Search Appearance Simulation**
  - [ ] Preview how your site appears in search results (GSC's "Inspect URL" feature)
  - [ ] Title and description display correctly (not truncated)
  - [ ] No warning messages or issues

### Phase 5: Business & Local Signals (Before Launch)

- [ ] **Google Business Profile (GBP)**
  - [ ] GBP is created and verified
  - [ ] NAP (Name, Address, Phone) matches website exactly
  - [ ] Business hours are correct
  - [ ] Service area is defined (if applicable)
  - [ ] GBP is fully filled out (no missing fields)

- [ ] **Local Citations**
  - [ ] Business is listed on top citation platforms (Yelp, BBB, etc.)
  - [ ] NAP is consistent across all citations
  - [ ] No duplicate listings

- [ ] **Contact Information**
  - [ ] Phone number is live and monitored
  - [ ] Email address works
  - [ ] Contact form submits without errors
  - [ ] Call-tracking number (if used) is configured

### Phase 6: Security & Compliance (Before Launch)

- [ ] **HTTPS & SSL**
  - [ ] SSL certificate is installed and active
  - [ ] No mixed-content warnings (all resources are HTTPS)
  - [ ] Certificate is valid for your domain

- [ ] **Privacy & Legal**
  - [ ] Privacy Policy page exists and links from footer
  - [ ] Terms of Service (if applicable) are present
  - [ ] GDPR/CCPA compliance (if handling user data)
  - [ ] Copyright notice is accurate

- [ ] **Forms & Data**
  - [ ] Contact form doesn't send sensitive data via email plain-text
  - [ ] No client data exposed in URLs or source code
  - [ ] Spam protection is configured (reCAPTCHA, honeypot, etc.)

### Phase 7: Analytics & Monitoring Setup (Before Launch)

- [ ] **Google Analytics**
  - [ ] GA4 tracking code is installed
  - [ ] Test event fires (use Real-Time report)
  - [ ] No sampling warnings or data loss

- [ ] **Conversion Tracking**
  - [ ] Goal/event tracking is configured (form submission, call button click)
  - [ ] Attribution is set up correctly
  - [ ] Conversion values are assigned (if using them)

- [ ] **Rank Tracking**
  - [ ] Microsite slug is added to rank tracker (Ahrefs, SEMrush, etc.)
  - [ ] Target keywords are configured
  - [ ] Baseline ranking position is captured (optional but useful)

- [ ] **Call Tracking** (if applicable)
  - [ ] Call-tracking number is configured
  - [ ] Calls are recorded and reportable
  - [ ] Number displays correctly on all pages

### Phase 8: Final Checklist (Day-of-Launch)

- [ ] **Remove Noindex**
  - [ ] Remove `<meta name="robots" content="noindex">` from all pages
  - [ ] Confirm removal via GSC URL Inspection (should say "URL available to Google")

- [ ] **Do a Final Crawl**
  - [ ] Run Screaming Frog or Ahrefs on the live site
  - [ ] Check for any broken links, 404s, or errors
  - [ ] Verify sitemap still valid
  - [ ] Check that all canonicals are correct

- [ ] **Request Indexing** (Optional, speeds up)
  - [ ] Submit homepage URL via GSC "Inspect URL" → "Request Indexing"
  - [ ] Submit sitemap in GSC (often done before, but double-check)
  - [ ] Google typically crawls within 24–48 hours anyway

- [ ] **Go Live**
  - [ ] Flip to live (remove staging environment)
  - [ ] Enable CDN/caching if applicable
  - [ ] Monitor first 24 hours for errors

- [ ] **Post-Launch (First Week)**
  - [ ] Check GSC daily for indexing errors
  - [ ] Monitor Core Web Vitals (PageSpeed Insights)
  - [ ] Check analytics for traffic anomalies
  - [ ] Verify ranking baseline in tracker
  - [ ] Test all forms and CTAs work

---

## Automation & Testing Tools

### Free Tools
- **Google Search Console** — Indexing, sitemap validation, URL inspection
- **Google PageSpeed Insights** — Core Web Vitals, mobile rendering
- **Google Rich Results Test** — Schema validation
- **Screaming Frog (free tier)** — Crawl and check for broken links
- **Lighthouse (built into Chrome)** — Performance, accessibility, SEO
- **W3C Markup Validator** — HTML/XML validation

### Paid Tools
- **Ahrefs** — Comprehensive crawl, schema check, rank tracking
- **SEMrush** — Similar to Ahrefs; site audit features
- **Cloudflare** — Security and performance

---

## Lessons Learned

**From the sitemap case study:**

1. **Infrastructure checks must happen first** — Before design, before content. A beautiful site with a broken sitemap is a failed site.

2. **Hostname must be verified** — Not assumed. The wrong domain in the sitemap is invisible until someone checks it.

3. **Canonicals are critical** — Doubly true if you've ever used a staging domain. Always set canonicals before launch.

4. **Check once, check twice** — An automated crawler (Claude, Fable, your own script) running across the full site catches errors humans miss.

5. **Small moves, consistent progress** — Don't wait for perfect. Fix what you find, launch, monitor. Learn as you go.

---

## Related Pages

- [[on-site-seo.md]] — Content and page optimization (complements this infrastructure checklist)
- [[external-seo-microsite-tactics.md]] — Post-launch tactics (citations, backlinks)
- [[seo-fundamentals/technical-seo.md]] — Why crawlability, indexability, and schema matter
