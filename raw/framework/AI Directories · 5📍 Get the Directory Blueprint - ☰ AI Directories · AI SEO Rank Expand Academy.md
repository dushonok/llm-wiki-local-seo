---
title: "📍 Get the Directory Blueprint - ☰ AI Directories · AI SEO: Rank Expand Academy"
source: "https://www.skool.com/rank-expand-academy/classroom/fc0aa216?md=81a5ac9a5e8440ee888dbbcd2e4eb634"
author:
published:
created: 2026-11-12
description: "A raw scrape is a phone book. This step turns it into a tool. Two things happen here. First the junk comes out. Then every real business gets a set of attribute"
tags:
  - "clippings"
---
#### A raw scrape is a phone book. This step turns it into a tool.

Two things happen here. First the junk comes out. Then every real business gets a set of attributes and a description, so a page about "pool builders in Tampa" can say which ones do fiberglass, which offer financing, which say they are licensed. That is what makes a directory rank and what makes it worth using.

All of it runs inside Claude Code with the Directory Blueprint. You approve each step. You don't need to edit spreadsheets, setup databases, or install a CMS.

## Follow these steps:

1. **Step 1. Download the Directory Blueprint** from the resources below and unzip it. You get a folder with a `CLAUDE.md` file, a `README`, a `wiki` folder, `templates`, `scripts`, `skills` and an `input` folder. Claude creates `output` when it starts.
2. **Step 2. Give it your listings.** Outscraper: put the CSV from Step 3 in the `input` folder, named `listings-raw.csv`. DataForSEO: nothing to add. The Blueprint uses the connection you made in Gear Up, and Claude never asks you to paste a login in the chat.
3. **Step 3. Open the Blueprint folder in Claude Code.** Open your terminal, go to the folder, run `claude`. Then type:
	`Read CLAUDE.md and run Gate 1.`
4. **Step 4. Gate 1, Scope.** Claude asks you eight things, one at a time: the service, the state, the domain from Step 2, the phone numbers of any microsites you own in this vertical, the name that fronts the directory as its publisher, that publisher's details (website, a short bio, a photo, a contact email), one or two websites whose look you want the directory to borrow (any site, any industry, just one you think looks good; if you have none, say so and Claude shows you seven directories to pick from), and where the listings come from. On DataForSEO it then quotes the cost for your state and pulls after you say yes. Answer and approve. The publisher and the inspired site are what stop your directory from looking like every other AI-built site.
5. **Step 5. Gate 2, Clean.** Claude runs the cleaning script and shows you a report: rows in, rows out, why, and the kept rows broken down by what Google calls them. The rules are fixed: only your state, only open businesses, only businesses with at least one review, only names or categories that match your service, no duplicates, and on DataForSEO nothing that has not been updated in a year. From an Outscraper export expect to keep 5 to 6 percent. From a DataForSEO pull expect to keep most of it. If the report says you kept 1 percent from Outscraper, or half from DataForSEO, the service terms are wrong. Tell Claude and it runs again.
	One thing to read closely on DataForSEO: businesses that carry your category as a second label come through too. A fence pull in one state kept a third of its rows as landscapers, handymen and roofers who also build fences. Nothing is dropped for that here. You decide what to do with them in Step 5, listing by listing or as a group, and Claude records every decision in a file so a rerun keeps it.
6. **Step 6. Gate 3, Enrich.** Three parts, and Claude stops for your approval before the expensive one.

First, Claude writes the attribute list for your vertical with you: 8 to 15 things a page can say about a business (for pool builders: inground, fiberglass, gunite, spa, remodel, screen enclosure, financing, licensed, and so on), each with the words on a website that would make it true. If the Maps category is broader than your service, one attribute records whether the business does the core work at all. Approve the list.

Second, Claude reads each business's own website. The Maps pull has almost no text to work from (the description is empty on nearly every row), so the website is where the facts come from. This part is free and takes a few minutes for a state.

Third, the enrichment itself. Claude answers every attribute with true, false, or not enough info, and writes a plain description per business, 50 to 200 words depending on how much the site gave. It never guesses: true needs words on the site that say it, and a checker rejects any answer it cannot trace. "Not enough info" shows on the page as exactly that. Before this part runs, Claude tells you how many listings it is and how much of your Claude plan it will use (about 4,000 tokens a listing; a 400-business state is under two million, a 2,000-business state is about eight million), runs one small batch for you to read, then the rest. It goes city by city and saves as it goes, so if you stop and come back nothing is redone.

## What you have at the end

A folder under `output` with the clean list, the attribute list, the enriched list and a report for each step. That is the whole directory in three files. Everything from here is generated from them.

## When something is off

- **Claude cannot find the CSV.** Outscraper: it is not named `listings-raw.csv` or it is not in `input`.
- **Claude says there is no DataForSEO login.** You connected DataForSEO in claude.ai or the desktop app but not in Claude Code. Run the one Claude Code command from the Gear Up lesson and restart Claude Code.
- **The clean report drops almost everything.** Your service terms do not match how businesses name themselves. Look at a few dropped names and give Claude the words they actually use.
- **Half the websites could not be read.** Some share is normal: sites that block robots, sites that are one big image, dead domains. Those businesses get a short description from the Maps data and mostly "not enough info." If it is more than half, the vertical is one where businesses do not keep websites, and the directory will be thin.
- **Attributes come back mostly "not enough info."** Normal for businesses with few reviews and a thin site. Those listings get a page but do not go in the sitemap at launch. Step 7 covers that.

**Do this now:** run Gates 1 to 3. Read the clean report before you approve it, and read the first enrichment batch before the rest runs. Post your keep rate and your attribute list in the community.

Resources

📍 Directory Blueprint (11-11-26)

[

US Census Bureau population dataset

](https://www.skool.com/rank-expand-academy/us-census-bureau-population-dataset)

I build microsites and directories with Claude Code. I just added a US population dataset to my project: 19,483 incorporated places, with July 2025 population estimates. Now I can ask: “Find Florida cities with 50k-200k people” or “Add populations to these 20 microsite locations.” Useful for shortlisting target cities and enriching your site spreadsheet without looking up each city manually. I'm including the CSV for you to download, just use Claude or Codex and add it to your project, and ask questions in plain English. It's a dataset cleaned up from the US Census Bureau. Let me know if you have any questions on how to use it.

<audio><source type="audio/mpeg"></audio>

<audio><source type="audio/mpeg"></audio>