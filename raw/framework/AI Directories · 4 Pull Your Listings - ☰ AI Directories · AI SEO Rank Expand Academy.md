---
title: "Pull Your Listings - ☰ AI Directories · AI SEO: Rank Expand Academy"
source: "https://www.skool.com/rank-expand-academy/classroom/fc0aa216?md=0c4384753f534f96b8eebc54c70d6151"
author:
published:
created: 2026-11-12
description: "Google Maps is the raw material. This step gets it. There are two ways to get it, and the Blueprint takes either. Both end in the same file with the same column"
tags:
  - "clippings"
---

#### Google Maps is the raw material. This step gets it.

There are two ways to get it, and the Blueprint takes either. Both end in the same file with the same columns.

1. **DataForSEO.** If [DataForSEO](https://try.dataforseo.com/oonolodsna2w "https://try.dataforseo.com/oonolodsna2w") is connected to your Claude Code (the Gear Up lesson, Connect DataForSEO to Claude), the Blueprint pulls the listings for you in Step 4. One category, one state, a few dollars, under a minute.
2. **Outscraper.** No API, no key. You run the scrape on [outscraper.com](https://outscraper.com/refer?referrer=M2E4ZmY5M2UxYTgyNDMzYTg2ZmJmMjIxNDViMGI3Mzk= "https://outscraper.com/refer?referrer=M2E4ZmY5M2UxYTgyNDMzYTg2ZmJmMjIxNDViMGI3Mzk=") and download a CSV. This is the path in Jesse's video.

We ran both on the same category in the same state on the same day (swimming pool contractors, Florida) and matched every business. DataForSEO had 19 of every 20 businesses Outscraper found: 95 percent of the open businesses with reviews, 96 percent of those with five or more. Where both had a business, the record was the same record: phone identical on 99 percent, website on 99.9 percent, review counts within a few percent. Outscraper's extra rows were mostly hotels with pools, state parks and plumbers that Step 4 throws out anyway, plus about one real pool company in twenty that DataForSEO did not have. Cost: $0.89 against about $24.

Our take: DataForSEO when it is connected. Outscraper when it is not, or when you want every last business on day one.

## Way 1: DataForSEO

- **Step 1. Connect DataForSEO to Claude Code.** If you already did it for ⚡ [Chat With Your Keyword Data](https://www.skool.com/rank-expand-academy/classroom/5d44ffd9?utm_campaign=skool_link_classroom&utm_content=e0c04038afe74a28a97dccc4b03256df "https://www.skool.com/rank-expand-academy/classroom/5d44ffd9?utm_campaign=skool_link_classroom&utm_content=e0c04038afe74a28a97dccc4b03256df"), check that you did the Claude Code one, not only the [claude.ai](http://claude.ai/ "http://claude.ai") connector. The Blueprint reads the login from that connection, so it never goes in a file or a chat. A new account needs a $50 top-up; one state uses a few dollars of it.  
	  
	➡️ **Setup steps:** [https://dataforseo.com/help-center/connecting-the-remote-dataforseo-mcp-server-using-oauth](https://dataforseo.com/help-center/connecting-the-remote-dataforseo-mcp-server-using-oauth "https://dataforseo.com/help-center/connecting-the-remote-dataforseo-mcp-server-using-oauth")
- **Step 2. There is nothing to run here.** In Step 4, Claude looks up your category, quotes the exact cost for your state, and pulls only after you say yes. The CSV lands in the right place by itself.
- **Step 3. Know the one catch.** DataForSEO is a database, not a live scrape, so it does not know when a business closes. The Blueprint handles it in Step 4 by dropping any listing not updated in the last year. In Florida that removed 193 rows: 72 closed businesses, 109 gone from Maps, and 12 that were still open. About one listing in a hundred that survives will still be a closed business. The claim page and the correction line in Step 8 catch those.

## Way 2: Outscraper

- **Step 1. Create an Outscraper account** at [outscraper.com](http://outscraper.com/ "http://outscraper.com"). The first 500 records are free, so you can test before you pay.
- **Step 2. Open the Google Maps scraper.** In the dashboard, choose **Google Maps** under Services.
- **Step 3. Set the category.** In the **Categories** field, type the exact Google Maps category from Step 1 and pick it from the list. Use the category, not a free-text search. A free-text search pulls anything that mentions the words. Jesse's receipt: a typical scrape is about $100, and the one time he forgot exact match it was $317 for 119,000 rows, most of them junk.
- **Step 4. Set the location.** In **Locations**, choose your country, then your state. Leave cities blank. You want the whole state in one pull.
- **Step 5. Leave the fields on default.** The default export has everything the Blueprint uses: name, address, phone, website, rating, review count, review tags, the about section, hours, category, coordinates, business status and the location link. That last one is the Maps URL of the listing, and it is what the enrichment reads later. Do not turn on the email or social media add-ons for this pull. The pages never show an email, and the emails you do need come cheaper after cleaning (see Emails below).
- **Step 6. Run it, then download the CSV.** A state takes a few minutes to a couple of hours. Florida pool contractors took about ten minutes; Jesse's 6,245 dog parks nationwide took two hours. A slow pull is not a failed one. When it finishes, download the results as **CSV**, not Excel.
- **Step 7. Rename the file to** `listings-raw.csv`**.** That is the name the Blueprint looks for in Step 4.

## Emails

Neither path needs an email add-on for the pull. No listing page ever shows an email. Step 8 is where they matter: the claim invitation, the badge offer and the follow-up all start with an email to the owner. DataForSEO includes web-sourced emails at no extra cost, about one row in four on the Florida pull. On Outscraper, get them after Step 4 from the cleaned list only: the Blueprint writes the website domain of every kept business to one file, and Outscraper's Emails and Contacts scraper takes that file at $3 per 1,000 domains after 500 free. For a cleaned state that is about $5. On the raw export you would pay for every junk row too. On either path an address gets a domain check and a bounce test before anything goes out, which Step 8 covers.

## What it costs

DataForSEO: a few dollars for one category in one state, and Claude shows the exact number before it pulls. Florida pool contractors, $0.89. Texas roofing contractors, about $3.

Outscraper: $3 per 1,000 rows after the free 500. Florida pool contractors was 8,535 rows, about $24. A big state in a common category can be 20,000 to 40,000 rows, $60 to $120. Most of those rows are junk and Step 4 throws them out: you pay for the raw pull and keep the 5 to 6 percent that are real businesses. That is normal on this path. On DataForSEO you keep most of what you pay for, because it pulls by category and nothing else.

## When something is off

- **The count looks tiny.** The category is wrong or the location was set to a city. Check both and run again.
- **The count looks huge (Outscraper).** You picked a broad category ("Contractor") instead of the specific one, or typed the words instead of picking the category from the list. Go back to Step 3.
- **Rows from neighboring states (Outscraper).** Normal. The Blueprint filters them out.
- **A business you know is missing (DataForSEO).** About one in twenty is. Add it by hand, or let the owner claim it in Step 8.
- **Claude cannot find your category (DataForSEO).** It checks the list for free. If your service is not on it, it is not a Maps category. Back to Step 1.

**Do this now:** DataForSEO, check the connection once (in Claude Code, type `/mcp` and look for dataforseo) and move on to Step 4. Outscraper, run the pull for your category and state and download the CSV. Either way, do not open the file and start cleaning by hand. That is what the next step is for.

<audio><source type="audio/mpeg"></audio>

<audio><source type="audio/mpeg"></audio>