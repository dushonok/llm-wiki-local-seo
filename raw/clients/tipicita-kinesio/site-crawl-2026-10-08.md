# Raw capture: tipicita-kinesio.com site crawl + local SERP/citation check

Captured: 2026-10-08
Method: live fetch of tipicita-kinesio.com (Wix site) pages, sitemap.xml, robots.txt,
and raw HTML head (title/meta/JSON-LD) via HTTP GET; supplementary web search for
Google Business Profile / directory / competitor signals. No login-gated tools
(Search Console, GBP dashboard, Ahrefs/SEMrush) were available — this capture is
limited to what's publicly fetchable.

## Business identity (from homepage + LinkedIn)

- Practitioner: Emmanuelle Mesnard, trading as "Tipicita"
- Services: **kinésiologie** (kinesiology — alternative/holistic modality using
  muscle-testing, NOT physiotherapy) + **coaching de vie/entreprise** (life/business
  coaching) + astrologie humaniste (remote sessions)
- IMPORTANT: despite the domain containing "kinesio", this is a kinésiologue
  (alternative therapy/coaching) practice, not a kinésithérapeute (physiotherapist).
  French searchers sometimes conflate the two terms.
- Certifications: "Certifiée kinésiologue et coach de vie", 900+ hours training,
  RNCP-certified coach
- Social proof: 47 Google reviews (5.0/5, per LinkedIn bio and bottin.fr "+ de 40
  votes"), 73 Résalib reviews (per LinkedIn). lesmedecinesdouces.fr third-party
  aggregator shows "5/5 - 44 avis externes" / "18 avis analysés, dernier avis le
  30/06/2026, 100% d'avis 5★, le praticien répond aux avis" — but that listing is
  still tagged to the **old Eysines address** (see Stale citations below).
- LinkedIn: https://linkedin.com/in/emmanuellemesnardtipicita — bio lists
  "Bordeaux · Eysines · Mérignac" as service area, NOT updated to Le Bouscat as of
  capture date.

## The move

- Per /ou-me-trouver page: "Rien ne change dans l'accompagnement que je vous
  propose. Seul le lieu évolue : depuis août 2026, toutes les séances ont lieu au
  cabinet du Bouscat." Cabinets Mérignac and Eysines both explicitly closed.
- Homepage footer: "Au 281 Avenue de la Libération Charles de Gaulle 33110 Le
  Bouscat à partir du 19 Août 2026" — move date: **19 August 2026**, ~7 weeks
  before this capture.
- New address: 281 Avenue de la Libération Charles de Gaulle, Résidence Longchamp
  2000, Bâtiment B, 33110 Le Bouscat. Pedestrian entrance via Avenue du 8 Mai 1945.
  Shares cabinet with Mathilde Babilliot (ostéopathe). Tram D, arrêt Mairie du
  Bouscat, 100m away. Free 1h30 disc parking nearby.

## Site structure (from pages-sitemap.xml, lastmod 2026-10-08)

Core pages (9):
- / (homepage)
- /mon-approche
- /cap-famille (parent-child kinesiology)
- /juste-decision (4-session program)
- /juste-place (7-session program, flagship)
- /seance-astrologie-coaching-a-distance
- /ou-me-trouver (location page)
- /kinesiologie-coaching-bordeaux (flagship single-session service page)
- /blog

Blog (blog-posts-sitemap.xml): 35 posts dating back to **2019-12-16**, with a
cluster of edits on 2026-08-23 and 2026-09-28 (post-move content refresh
activity). Several legacy post URLs/titles are permanently anchored to the old
location:
- /post/mieux-gérer-son-stress-kinesiologie-coaching-bordeaux-merignac
- /post/se-liberer-de-ses-blocages-kinesiologie-coaching-bordeaux-merignac
- /post/gerer-ses-emotions-kinesiologie-coaching-bordeaux-merignac
- /post/kinésiologie-et-coaching-à-bordeaux (image alt text: "kinésiologie et
  coaching à Mérignac")
- /post/accompagnement-holistique-sportifs-haut-niveau-bordeaux-merignac

This confirms the "existing SEO history" — nearly 7 years of blog content, but a
real chunk of it has Mérignac baked into URLs/titles/alt text that will keep
signaling the old location indefinitely unless addressed via redirects/rewrites
or de-prioritization.

## On-page SEO findings (title/meta/schema, fetched via raw HTML)

### Homepage (/)
- `<title>`: "Accueil | Emmanuelle Mesnard-Coach de vie-kinesiologue bordeaux" —
  mentions Bordeaux only, no Le Bouscat.
- meta description: mentions "Bordeaux" only.
- **JSON-LD LocalBusiness schema is STALE**:
  ```json
  {"@context":"https://schema.org/","@type":"LocalBusiness",
   "name":"Emmanuelle Mesnard - Kinesiologue coach de vie - Bordeaux",
   "url":"https://www.tipicita-kinesio.com",
   "address":{"@type":"PostalAddress","addressCountry":"FR",
     "addressLocality":"Eysines","addressRegion":"NAQ","postalCode":"33320"},
   "telephone":"0787147913"}
  ```
  This directly contradicts the visible on-page content (which says Le Bouscat,
  33110) and is the single highest-priority technical finding in this capture.
- A second JSON-LD block (`WebSite` type) has no address data.

### /ou-me-trouver (location page)
- `<title>`: "Kinésiologue et coach de vie au Bouscat | Emmanuelle Mesnard" — good,
  location-targeted.
- meta description: mentions "Bouscat... Bordeaux, Bruges, Caudéran, Eysines et
  Mérignac" — good, location + feeder-suburb targeting.
- **No `application/ld+json` block found on this page at all** — the page most
  relevant to the location move carries zero structured data (no LocalBusiness,
  no FAQPage despite having an on-page Q&A section: "Les cabinets de Mérignac et
  d'Eysines sont-ils fermés ?", "Où se garer près du cabinet ?", "Par où entrer ?").

### /kinesiologie-coaching-bordeaux (flagship service page)
- `<title>`: "Séance kinésiologie coaching à Le Bouscat proche de Bordeaux" —
  already updated for the new location.
- meta description: "...Séance Kinésiologie Coaching à Le Bouscat, proche de
  Bordeaux..." — good.
- URL slug itself still says "-bordeaux" (legacy, not necessarily worth breaking
  with a rename/redirect at this stage).

### /juste-decision
- `<title>`: "Retrouver son pouvoir de décision - Accompagnement conflit" — no
  location at all (not even Bordeaux). Missed location-signal opportunity but
  lower priority (mid-funnel program page, not a top entry point).

### /mon-approche
- `<title>`: "Ma vision et posture d'accompagnante | Emmanuelle Mesnard" — meta
  description says "près de Bordeaux" — no Le Bouscat.

## robots.txt / sitemap health

- robots.txt is standard Wix output: `Allow: /`, blocks PetalBot, crawl-delay for
  dotbot/AhrefsBot, correctly references `Sitemap:
  https://www.tipicita-kinesio.com/sitemap.xml`. No crawl blockers found.
- sitemap.xml is a valid sitemap index (pages / blog-posts / blog-categories).
  pages-sitemap.xml lastmod = 2026-10-08 (today), confirming active recent edits
  consistent with the relocation push.

## Local competitive landscape (Le Bouscat, kinésiologue niche)

Per bottin.fr directory ("4 Kinésiologues au Bouscat") and doqi.fr (lists 5):

| Practitioner | Address | Reviews | Domain |
|---|---|---|---|
| Marion Reynaud | 6 Av. Marius Marchandou, 33110 | 5.0, **+70 votes** | mr-kinesiologue.com |
| **Emmanuelle Mesnard (Tipicita)** | 281 Av. de la Libération Charles de Gaulle, 33110 | 5.0, +40 votes | tipicita-kinesio.com |
| Aude Coué | 20 Av. de la Libération Charles de Gaulle, 33110 (+ second cabinet in Blaye) | 5.0, +40 votes | aude-coue.com |
| Nina Peret | 20 Av. de la Libération Charles de Gaulle, 33110 (same building as Aude Coué) | 5.0, +10 votes | bonjourlebonheur.fr |
| Marine Gabillet | 4 Rue Emile Zola, 33110 | — | (doqi.fr listing only) |

Takeaway: the "kinésiologue Le Bouscat" niche is dense — 5 well-reviewed
practitioners in a small town, several sharing a street (Av. de la Libération
Charles de Gaulle) or even a building. Marion Reynaud currently leads on review
volume. Tipicita is competitive on rating/review count but not the clear leader.

For "coach de vie Le Bouscat" the field is thinner and less specialized (small
single-practitioner directory-only listings: Amandine Bise, Noémie Coach
Vibration, Madonie Heudron — mostly nutrition/PNL adjacent, not direct
coach-de-vie competitors). Live web search on 2026-10-08 placed
tipicita-kinesio.com/ou-me-trouver as the #1 organic result for "coach de vie Le
Bouscat Bordeaux".

## Stale citation found (NAP drift)

lesmedecinesdouces.fr still lists the practitioner at the **old Eysines address**:
"Emmanuelle Mesnard, Coach-de-vie, 76 Av. de la Libération, 33320 Eysines" (5/5,
44 avis externes, dernier avis 30/06/2026 — i.e., still receiving/aggregating
recent reviews under the stale listing).
URL: https://lesmedecinesdouces.fr/coachdevie/eysines/76-av-de-la-liberation/emmanuelle-mesnard/therapeute/avis/

This is a concrete, named example of NAP (Name/Address/Phone) inconsistency
across the citation graph post-move — the same failure mode as the stale
homepage schema above, just off-site instead of on-site.

## Not captured (requires login/paid tools — flag for client/user to provide)

- Google Business Profile dashboard (primary category, service-area setting,
  whether old Eysines/Mérignac listings were merged vs. left duplicate/closed,
  Google Posts history, Q&A, photos)
- Google Search Console (actual impressions/rankings pre- vs. post-move, any
  manual actions, indexing status of /ou-me-trouver)
- Full local-pack/map-pack screenshots for "kinésiologue le bouscat" /
  "kinésiologue bordeaux" — only organic web results were checked
- Ahrefs/SEMrush backlink profile or historical rank tracking
- Full citation audit (Yelp-FR equivalents, PagesJaunes, Doctolib, Resalib profile
  page itself, annuaire-therapeutes sites) beyond the two directories sampled
  above
