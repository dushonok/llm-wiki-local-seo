---
title: "Invisible URLS = AI Visibility + Outreach Targets Prompt · AI SEO: Rank Expand Academy"
source: "https://www.skool.com/rank-expand-academy/invisible-urls-ai-visibility-outreach-targets-prompt?p=21c7ccfe"
author:
published:
created: 2026-10-29
description: "This is based off our conversation in the most recent community call. This is a prompt to build the system for \"Invisible URLs\":  I want you to build an \"AI Vis"
tags:
  - "clippings"
---
14

Invisible URLS = AI Visibility + Outreach Targets Prompt

This is based off our conversation in the most recent community call. This is a prompt to build the system for "Invisible URLs":

I want you to build an "AI Visibility + Outreach Targets" analysis for a website. This is an

AEO (Answer Engine Optimization) system. I'll explain the full concept; build it exactly.

MY INPUTS

\- Website: \[DOMAIN, e.g. [acme.com](http://acme.com/ "http://acme.com")\]

\- Brand name(s) the AI might use: \[BRAND + variants/misspellings\]

\- Direct competitors (domains + brand names): \[LIST\]

\- Markets/categories to test: \[e.g. countries, product lines, or service areas —

this is the grouping dimension for all reporting\]

\-I can give you Google Search Console access if you walk me through it

THE CONCEPT

When real people ask ChatGPT or Gemini questions like "best \[product\] in \[market\]" or

"how do I choose \[service\]", the AI either recommends my brand, cites my site without

naming me, or omits me entirely. I want to measure that at scale, and — the key output —

mine the AI's citations to find WHICH third-party pages the AI reads and trusts when

composing answers. Those repeatedly-cited pages are my outreach hit list: getting my

brand mentioned/inserted in them is the most direct way to start appearing in AI answers.

It's link building, except the "search engine" is an LLM's retrieval layer.

PIPELINE (build in this order)

1\. PROMPT GENERATION: For each page/market/gsc query, generate 2 realistic user prompts with an LLM:

one PRODUCT-intent ("best X in Y") and one ADVISORY-intent ("how do I choose X in Y").

Advisory prompts matter: if my business is an intermediary (broker/agency/marketplace),

we win advisory questions, not "best manufacturer" questions — match prompts to what

the business can actually win.

2\. LLM ANSWER COLLECTION: DataForSEO AI Optimization API —

POST /v3/ai\_optimization/{chat\_gpt|gemini}/llm\_responses/live

body: \[{"user\_prompt": "...", "model\_name": "...", "web\_search": true}\]

Gotchas we learned the hard way:

\- Do NOT send max\_output\_tokens (invalid field, error 40501).

\- Use a cheap non-reasoning model for ChatGPT (gpt-4o-mini ≈ $0.015/call with web

search); Gemini flash runs ≈ $0.066/call — Gemini drives ~80% of total cost, so

budget accordingly (e.g. ChatGPT monthly, Gemini every other month).

\- Response text is nested: items → message → sections.

\- Gemini citations come wrapped as [vertexaisearch.cloud.google.com/grounding-api-redirect/…](http://vertexaisearch.cloud.google.com/grounding-api-redirect/%E2%80%A6 "http://vertexaisearch.cloud.google.com/grounding-api-redirect/…")

— follow each redirect to resolve the REAL cited URL before storing anything.

3\. CLASSIFICATION — exactly 3 states per (page × prompt × model):

\- RECOMMENDED (green): the answer names my brand as a recommendation.

\- CITED, NOT CREDITED (amber): my domain appears in the citations but the answer

doesn't name/recommend me — the AI read my page and recommended competitors.

\- OMITTED (red): neither.

Store the verbatim answer text, all resolved citation URLs, and which competitors

were named — these are the "receipts" for every classification.

4\. OUTREACH TARGETS (the gold): per market, aggregate ALL resolved citation URLs across

every answer and keep URLs cited 3+ TIMES, excluding:

\- my own domain

\- competitor domains (can't pitch them)

What remains = the editorial guides, comparison articles, and listicles the AI

repeatedly trusts for this market. Rank by citation count. Each is a concrete

outreach action: pitch a mention, quote, or inclusion in that page.

5\. REPORTING: group everything by market. Per market show: % winning

(green=1, amber=0.5, red=0), the outreach target list with counts, and per-page

rows expandable to the verbatim receipts. Overall scorecard on top.

STRATEGY LENS (interpret results with this)

\- ChatGPT and Gemini diverge because of SEARCH BACKENDS: Gemini retrieves via Google

(if my SEO is strong there, Gemini cites me), ChatGPT via Bing + aggregator listicles.

A huge ChatGPT-vs-Gemini gap is normal and diagnostic, not a bug: it means the fix is

Bing SEO + getting into the exact listicles ChatGPT cites (the outreach list).

\- Verify an "omitted" isn't a capture bug before believing it (read the receipt).

\- Amber ("cited not credited") is the highest-leverage state: the AI already reads my

page — the content needs clearer brand-forward framing so the AI can credit it.

DELIVERABLES

1\. The collection script (resumable, skip-done, retry-on-failure, sequential/gentle —

never hammer any API or site).

2\. A results store (SQLite or Postgres: prompts table + results table).

3\. The per-market report with % winning, outreach targets, and receipts.

4\. A one-page strategy summary: where we win, where we're invisible, the top 10

outreach targets overall, and the 3 highest-leverage next actions.

Run a small pilot first (one market, ~10 pages, both models), show me the results and

cost, and get my approval before any full run.

15

14 comments![Joshua Parfitt](https://assets.skool.com/f/f3e2d6b7cfcc4c8e9f08b84305deb2a8/fd9ba88b6dfd4d8b92a27f167db365f69d2f999296ef4a7db5a0a53d1a65bfaf-sm.jpg)

Joshua Parfitt[Joshua Parfitt](https://www.skool.com/@joshua-parfitt-5922?g=rank-expand-academy)

• Jul 15

this looks really reslly useful

2[Tom LeeZmuda](https://www.skool.com/@tom-leezmuda-3554?g=rank-expand-academy)

• Jul 15

Posted while doing a live? 🤷

4

View 1 more reply[Shlomi Asaf](https://www.skool.com/@shlomi-asaf-8028?g=rank-expand-academy)

• Jul 15

Thank you, Jesse. I already ran it in the project and am preparing a report based on that for my client. Thank you very much for sharing this with us. It's an amazing technique.

3![Danny Nicholas](https://assets.skool.com/f/aee3678119bb49d0ad75b211a5ec19c1/0ba21e1cfbf448cf8aad7c66e369ae83f4e89f7e276247fd90dc643cddd62530-sm.jpg)

Danny Nicholas[Danny Nicholas](https://www.skool.com/@danny-nicholas-8274?g=rank-expand-academy)

• Jul 15

I waited all week I didn’t know what time the call takes place 🥺

2[Shawn Buckles](https://www.skool.com/@shawnbuckles?g=rank-expand-academy)

🔥

• Jul 15

[@Danny Nicholas](https://www.skool.com/@aee3678119bb49d0ad75b211a5ec19c1?g=rank-expand-academy)

you can find all the dates on the Calendar: [https://www.skool.com/rank-expand-academy/calendar](https://www.skool.com/rank-expand-academy/calendar?utm_campaign=skool_link_post&utm_content=e0c04038afe74a28a97dccc4b03256df "https://www.skool.com/rank-expand-academy/calendar")

0[Jesse Cunningham](https://www.skool.com/@jesse-cunningham?g=rank-expand-academy)

👑

🔥

• Jul 15

And the point to have the Google Search Console hookup is so that you can identify the top queries that have most volume. From there you can make a guess on what queries will have similar volume on AI platforms and map everything from them.

2[Shawn Buckles](https://www.skool.com/@shawnbuckles?g=rank-expand-academy)

🔥

• Jul 16

[@Shlomi Asaf](https://www.skool.com/@af28fd24db644db5b25b4e9482116853?g=rank-expand-academy)

always interesting, but as

[@Blair Witkowski](https://www.skool.com/@ab346ce88d4e48cb932c684753540b53?g=rank-expand-academy)

said, we still need to use our own judgement. These tools can get it wrong too with just as much confidence.

2[Shlomi Asaf](https://www.skool.com/@shlomi-asaf-8028?g=rank-expand-academy)

• Jul 16

completely agree. I see this more as a guidance, mechanism I’ll study to build mine.

But this skill is a general SEO skills collections, with one payed link building service.

2![Geoffrey Roberts](https://assets.skool.com/f/081e5cdafe654514bb4910613e6ea291/d4d79dd6ca7048918bac26645f1a514cd6dc84d32c254dae9c331bbefe5c5b39-sm.jpg)

Geoffrey Roberts

• Jul 17

Still true

2

Drop files here to upload

Invisible URLS = AI Visibility + Outreach Targets Prompt

<audio><source type="audio/mpeg"></audio>

<audio><source type="audio/mpeg"></audio>