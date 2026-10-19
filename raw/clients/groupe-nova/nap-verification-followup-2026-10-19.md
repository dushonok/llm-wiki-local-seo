# Follow-up verification: NAP/GBP finding from the 2026-10-19 site crawl

Captured: 2026-10-19 (same day, follow-up pass after a self-review request)
Method: re-verification of the P0 NAP/GBP claim in
`site-crawl-and-gbp-check-2026-10-19.md` using additional web searches and
direct page fetches, specifically to check whether the original "website vs.
GBP mismatch" framing was adequately supported. This follow-up found the
original finding was **directionally right but materially oversimplified and
partly wrong in its specifics** — see corrections below.

## What the original capture got right

- The website's own two self-reported identifiers disagree with each other:
  the physical address printed in the contact section (4388 Rue Saint-Denis
  #200, Montreal — a known coworking space, "Montréal Cowork") is a different
  address than the one tied to the exact RBQ licence number the site itself
  prints (RBQ: 5881-0540-01).
- Zero meta descriptions, zero JSON-LD, generic titles, duplicate homepage
  URLs, missing alt text — all independently re-verified with permissive,
  case-insensitive regex against freshly re-fetched raw HTML (not just the
  original capture's parsing). These hold up fully.

## What the original capture got wrong or overstated

1. **"The GBP shows a different address (7657 Rue Montbrun, Saint-Léonard)"
   was stated with more confidence than the evidence supports.** The source
   for that address (exa.ai's places-data mirror) shows **6 reviews, all
   dated between 2022-09-29 and 2023-10-18** — i.e. a snapshot that is at
   least ~3 years stale relative to today (2026-10-19). This is very likely a
   cached/un-refreshed crawl of an old Google Maps listing, not a reflection
   of what the live Google Business Profile shows today. The original
   write-up implied a live/current mismatch; the honest framing is "a stale,
   ~3-year-old cached snapshot of a Google-connected listing shows a
   different address," which is a materially weaker claim.

2. **A genuinely new, higher-confidence data point was missed in the
   original pass**: cross-checking the RBQ licence number the website itself
   prints (5881-0540-01) against an independent licence-citing directory
   (soumissionrenovation.ca, "Dernière vérification le : 2026-08-26" — i.e.
   verified roughly 7 weeks before this capture, far more current than the
   exa.ai snapshot) shows that licence number registered to a *different*
   legal entity and address: **9562-0605 Québec inc., 1-8925 Avenue Millen,
   Montreal, QC H2M 1W6**. This is a **third** distinct address associated
   with the business, and arguably the most trustworthy one found, because
   (a) it's tied to the website's own self-reported RBQ number — a unique,
   government-issued identifier — rather than inferred from review-text
   matching, and (b) the citing directory's "last verified" date is far more
   recent than the exa.ai review dates.
   - Caveat on this point too: the directory profile for 9562-0605 Québec
     inc. does **not** itself display the name "Groupe Nova" anywhere (it has
     no business description filled in) — the link to Groupe Nova is an
     inference from the matching RBQ number, not a verbatim name match. A
     search-result synthesis briefly suggested this directory entry also
     said "à Laval, Montérégie, Montréal, Groupe..." but reading the full
     page directly (not just the snippet) showed that text belongs to a
     different, nearby listing (plomberie&chauffage JR inc) on the same
     directory page — the apparent connection was a search-snippet artifact,
     not real. This was caught and excluded.

3. **A fourth, independently-sourced address appeared that the original
   capture never found**: ProfileCanada.com has a listing for "Groupe Nova -
   Renovation Construction" at **7657 Rue Montbrun, Outremont, QC, H1S 2K3**,
   phone 438-866-6682, that explicitly lists **`www.groupenova.ca`** as the
   website — this is the strongest direct (non-inferred) corroboration found
   that the Rue Montbrun/438-866-6682 identity really is tied to the same
   `groupenova.ca` business, not a coincidentally-named different company.
   Two more directories (studio-lb.fr, aubaine.ca) independently list "Groupe
   Nova" at the same Rue Montbrun address/phone. None of these three carry a
   visible "last verified" date, so their currency relative to today is
   unknown — unlike the RBQ-citing directory above.
   - Note the Rue Montbrun listing is tied to RBQ licence **5797-3208-01**
     (a *different* licence number, held by **9394-3199 Québec inc.**, issued
     2022-07-08) — not the 5881-0540-01 the live website currently prints.
     **Correction to this file's own first draft**: this detail was
     originally (mis)described here as coming from "a direct fetch of its
     RBQ-licence-data mirror page." That's not accurate — a direct WebFetch
     attempt to that exact opengovca.com URL was made and was blocked by
     Cloudflare bot-protection (returned only a "performing security
     verification" page, no content). The actual licence table (NEQ
     1174386863, phone 514-627-0401, issue date 2022-07-08, surety "Intact
     Assurance," deposit $40,000) came from a **search engine's own
     cached/indexed snippet** of that page, returned inline in an earlier
     search call — not from a page I personally loaded and read directly.
     The level of specific, structured detail in that snippet (exact NEQ,
     exact deposit amount, named surety company) makes outright hallucination
     unlikely, but this is still one step removed from direct verification,
     the same category of risk as the search-snippet artifact caught and
     excluded elsewhere in this file. Treat this specific sub-claim (the
     5797-3208-01 / 9394-3199 Québec inc. pairing) as search-engine-cached,
     not independently re-verified by a direct page load.
   - This could mean a prior corporate/licensing arrangement that was
     superseded, or it could mean these are two related-but-formally-distinct
     entities both operating under the same public-facing brand name. This
     capture cannot distinguish between those two explanations — it requires
     the client or a direct RBQ repertory lookup to resolve.
   - A direct fetch of the official RBQ repertory (rbq.gouv.qc.ca) was
     attempted to get an authoritative, current read on both licence numbers,
     but the request failed (404 on the direct-query URL format tried; the
     real repertory is a JS-driven search form, not fetchable by a simple
     GET). Both licence numbers remain unverified against the primary
     government source.

4. No Google Place ID or other directly-queryable Google Maps identifier is
   exposed in the site's static HTML (the Trustindex review widget renders
   server-side without leaking a Place ID/CID in page source), so there is no
   way to check the live, current Google Maps pin for this business without
   either the GBP dashboard or a live, manual Google Maps search — neither
   available to this capture.

## Corrected picture (three-plus addresses, not a clean two-way mismatch)

| Address | Source | Confidence it's tied to groupenova.ca | Currency |
|---|---|---|---|
| 4388 Rue Saint-Denis #200, Montreal (coworking space) | Website's own "Contactez-nous" section | Certain (first-party) | Current (live site, today) |
| 1-8925 Avenue Millen, Montreal (9562-0605 Québec inc.) | Directory citing the website's own RBQ number 5881-0540-01 | High (exact unique licence-number match) but inferred, not a verbatim name match | Recently verified (2026-08-26, per the directory) |
| 7657 Rue Montbrun, Saint-Léonard/Outremont (9394-3199 Québec inc., RBQ 5797-3208-01) | ProfileCanada.com (explicit "Groupe Nova" name + `www.groupenova.ca` website link) + 2 other directories + exa.ai Google-review mirror (same 6 reviews as the site's widget) | High that it's the same brand/business at some point | Stale — reviews stop Oct 2023; directories carry no visible verification date; likely an older location/entity, not necessarily today's live GBP pin |

**Bottom line correction**: the original P0 finding correctly identified that
NAP is inconsistent and needs resolving before GBP optimization proceeds, but
incorrectly presented a clean "website vs. GBP" two-way mismatch with the Rue
Montbrun address asserted as "the current GBP." The reality is messier — at
least three addresses are associated with the brand across different sources
with different ages/confidence levels, and the single most defensible,
highest-confidence discrepancy is the website's own address field (Rue
Saint-Denis) disagreeing with the address tied to the website's own printed
RBQ number (Avenue Millen) — not the website-vs-stale-GBP-snapshot comparison
originally foregrounded. None of this substitutes for the client/user directly
opening the GBP dashboard, which remains the single fastest way to resolve
which address (if any of these) is the one actually live on Google Maps today.
