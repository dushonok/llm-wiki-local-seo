---
type: framework
client: none
status: active
updated: 2026-10-13
sources:
  - "raw/framework/AI Stacks Members Are Actually Using - 🎙️ The Wisdom's In The Calls · AI SEO Rank Expand Academy.md"
  - "raw/framework/51 - SEO Is Now Prompts and Agents - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/49 - The 12-Minute Microsite - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/AI video - What are you building this week · AI SEO Rank Expand Academy.md"
  - "raw/framework/How I make the posts and the shorts (Claude Code + OpenArt) - Bryan Collins - AI SEO Rank Expand Academy.md"
  - "raw/framework/Reddit Lead Alerts free monitoring tool, telegram bot & automation! · AI SEO Rank Expand Academy.md"
---

# AI Tool Stacks: Practical Combinations That Work

**Core Principle:** Don't buy stacks off the shelf. Stitch cheap APIs and open-source tools together, build custom MCPs (Model Context Protocols), delegate tools instead of tasks, and replace SaaS subscriptions with a single Claude Max plan.

---

## Content & Page Generation

### Stack #1: Programmatic Page Factory (Shawn's Recipe)

**Concept:** Break a page into sections, give each section its own specialized AI tool, then assemble hundreds of optimized pages automatically.

**Process:**
1. Create a custom GPT for each page section (title, intro, answer paragraph, H2, closing, etc.)
2. Each GPT has very specific instructions tuned for that section
3. Feed a location CSV (or run manually)
4. Assemble all outputs into a final page

**Results:** One member produced 300 pages in 1–2 months, reaching 50,000–70,000 pageviews/month at peak.

**Tools:**
- Custom GPTs (one per section)
- Location CSV
- Optional: N8n for workflow automation

---

### Stack #2: Dual-AI Content + Custom Graphics

**Concept:** Two AI models cross-checking each other to fill gaps, plus genuinely custom images per page.

**Process:**
1. Write long-form "monster pages" (4,000–5,000 words, no fluff)
2. Run ChatGPT and Claude against each other to find and fill content gaps
3. Generate custom graphics through Google Gemini's Nano Banana image model
4. Add CTAs (calls or quiz funnels) every few paragraphs

**Tools:**
- ChatGPT and Claude (for content cross-check)
- Google Gemini / Nano Banana (for custom images)

---

### Stack #3: Claude-Based Writing Tool for VAs

**Concept:** Don't train a VA repeatedly. Build judgment into Claude once, then hand them a tool.

**Process:**
1. Encode your content standards into a custom Claude tool
2. Delegate articles, listicles, and image sourcing to VA
3. VA runs everything through the tool
4. System teaches consistency without repeated training

**Tools:**
- Claude (custom writing tool built in interface or Claude Code)

---

## Building Sites at Scale

### Stack #4: Claude Code WordPress Factory

**Concept:** Structured prompts in Claude Code beat credit-heavy UI builders. At scale, it's 10x cheaper.

**Process:**
1. Use Claude Code to vibe-code WordPress themes and plugins (no coding experience needed)
2. Create separate agents for different jobs:
   - Agent 1: Builds pages
   - Agent 2: Adds schema markup
   - Agent 3: Internal linking (reads surrounding content, adds contextual links)
3. Chain Anthropic Skills together
4. Push pages directly to WordPress

**Cost:** ~$200/month Claude Max vs. thousands in platform credits (Lovable, Replit, etc.)

**Tools:**
- Claude Code (on Claude Max plan)
- Anthropic Skills
- WordPress

---

### Stack #5: Static Site Building + Voice Agent (12-Minute Microsite)

**Concept:** Build a complete site with lead capture and phone agent in ~12 minutes.

**Process:**
1. Manus: Generate static HTML from prompt
2. Upload zip to SiteGround / Cloudflare Pages
3. Omega Indexer: Bulk-submit all URLs for indexing
4. Retell AI + Twilio: Add phone number and voice agent (30 seconds setup)
5. Nano Banana: Tweak images for uniqueness
6. LoopNet: Pull real building address for NAP

**Cost:** ~$2–5 per site + domain registration

**Tools:**
- Manus (static HTML generator)
- SiteGround or Cloudflare Pages (hosting)
- Omega Indexer (indexing automation)
- Retell AI + Twilio (voice agent setup)
- Nano Banana (image customization)
- LoopNet (address data)
- Aweber (lead forms)

---

### Stack #6: The Microsite Master Branch (Volume Deploy)

**Concept:** Deploy 100+ sites at once using a Git master branch of templates.

**Process:**
1. Create master template in GitHub with proper Git structure
2. Push to Cloudflare (automatic deploy)
3. Each domain pulls from same master
4. Updates to template auto-deploy to all sites

**Alternative:** Hermes agent + DataForSEO driven from Telegram for AI-powered bulk builds

**Tools:**
- GitHub
- Cloudflare Pages (free static hosting)
- Hermes (optional, for agent-driven builds)
- DataForSEO (optional, for competition research)

---

## Lead Capture & Client Ops

### Stack #7: Voice AI Front Desk (24/7 Lead Capture)

**Concept:** An AI front desk doesn't sleep. Catches after-hours calls human receptionists miss.

**Value:** One member watched the system book an appointment at 2–3 AM. The bigger insight: the value isn't the voice AI itself, it's the *data it captures* (why people call, why they hang up).

**Tools:**
- Voice-AI agent (Retell AI or similar)
- GoHighLevel (for lead management and follow-up)

---

### Stack #8: SMS-First AI Brain for Contractors (Seth's Build)

**Concept:** AI interface layer over existing tools doesn't replace the CRM—it removes the part users hate.

**Process:**
1. Wire AI agent through Twilio
2. Connect to GoHighLevel + financial data
3. Text project details to the agent
4. Agent runs P&L and job-costing analysis on schedule
5. Know actual margins per job

**Monetization:** Already pitched to 3 contractors at $4,500–6,000 build + hosting fee.

**Tools:**
- Twilio (SMS interface)
- GoHighLevel (CRM + data)
- Custom AI agent

---

### Stack #9: One-Click Client Onboarding (Leadsie)

**Concept:** The fastest onboarding step to fix is *access*. One tool removes the "send me an invite" chain.

**Setup:**
- One email to client
- They answer a few questions
- Single click: you get access to GBP, GA, GSC, Facebook/Meta ads—all in one dashboard

**Tools:**
- Leadsie ([leadsie.com](http://leadsie.com))

---

## Scaling & Automation

### Stack #10: Custom MCP for DataForSEO (Kate's Build)

**Concept:** MCP is the unlock most people sleep on. Any API you pay for can be wired into Claude in an afternoon.

**Process:**
1. Kate built her own MCP connector to DataForSEO in Claude Code
2. Runs hours of niche brainstorming directly in Claude
3. Pulls real SERP data to validate/ditch ideas
4. No tool-switching—Claude reasoning over live data

**Tools:**
- DataForSEO API
- Claude Code (for custom MCP)

---

### Stack #11: GoHighLevel at Scale (Brandon's Consolidation)

**Concept:** At small scale, specialized tools win. At real scale, one platform wins.

**Process:**
1. Everything in GoHighLevel: CRM, voice agent, phone system, tracking infrastructure
2. Build number pools
3. Drop on microsites
4. Track which site → which call
5. Tighten intake for high-quality leads only

**Tools:**
- GoHighLevel ([gohighlevel.com](http://gohighlevel.com))

---

### Stack #12: Automated Video + Multi-Platform Distribution (Bryan's Build)

**Concept:** Generate video scripts via Claude, create videos via HeyGen API, and distribute across YouTube, Pinterest, and email automatically.

**Process:**
1. Claude generates prompts for video creation
2. HeyGen API 1.0 (via OpenRouter) creates videos with AI avatars (avatars cost pennies)
3. Gamma.app converts presentations to slides with voiceover
4. ElevenLabs generates voiceovers
5. Camtasia syncs audio to slides
6. Auto-publish to YouTube
7. Replit generates Pinterest pins from YouTube thumbnails
8. Upload pins to Pinterest with auto-generated titles/descriptions

**Outputs:**
- YouTube Shorts (90 seconds)
- Long-form YouTube videos (2–3 minutes)
- Pinterest pins with embedded YouTube links
- Scheduled email sequences with video CTAs

**Results (Oct 13, 2026):**
- 85 creatives scheduled via GoHighLevel planner
- 12 YouTube Shorts (3/week)
- 3 long-form videos with HeyGen avatars
- 1 completed YouTube channel
- Pinterest pins driving traffic back to microsites

**Cost:** HeyGen API at pennies-per-video scale. AI avatars eliminate voiceover talent costs.

**Tools:**
- Claude (script generation)
- HeyGen API 1.0 (video creation with AI avatars)
- Gamma.app (presentation slides)
- ElevenLabs (voiceover generation)
- Camtasia (audio-to-video sync)
- OpenArt.ai (graphics for shorts)
- Replit (Pinterest pin generation)
- YouTube API (auto-publish)
- Pinterest API (scheduled posting)

---

## Content Production

### Stack #13: Image Posts + Short Videos (Claude Code + OpenArt + Python)

**Concept (Bryan's Workflow):** Build reusable scripts for client Instagram posts and walkthrough videos. Image posts cost $0 (built in code); video shorts scale to 16/month at ~$17 OpenArt cost. 97% margin after tools.

**The Workflow Has Two Parts:**

---

#### Part 1: Instagram Image Posts (5x5 Grid, No AI Images)

**Why Not AI?** Image models redraw the client's real photos. The kitchen comes back slightly different, and the text gets misspelled. Built in code, the photo stays exactly as shot and every word is exact. Re-rendering all 25 takes seconds. Cost: $0.

**Setup (One-time, ~15 min):**
1. Install Claude desktop app or use terminal version
2. Open folder and start Claude Code session there
3. Ensure Python, Pillow (image library), and ffmpeg are installed (ask Claude to check/install)
4. Optional: Connect GoHighLevel (Settings > Connectors) so Claude can schedule directly

**The Workflow:**
1. Get client's 15–25 real project photos into a folder
2. Screenshot a design you like (e.g., a builder's carousel: full-bleed photo, dark fade, serif headline)
3. Paste into Claude Code with the screenshot and this prompt:

```
Here's a screenshot of a post design I like. My client's project photos are in [folder]. 
Their website is [URL]. Only use facts from the website.

1. Plan 25 Instagram posts: 5 Education, 5 Inspiration, 5 Process, 5 Comparison, 5 Trust. 
   Short headlines. Put "COMMENT [KEYWORD]" on exactly 5 of them.
2. Write a Python/Pillow script that renders each post at 1080x1350 in the style of the 
   screenshot: full-bleed photo, dark fade at the bottom, small letter-spaced brand name 
   top-left, a small letter-spaced label, a serif headline with the last word in italic 
   (Source Serif 4 from Google Fonts), a light sans subtitle and a thin white rule. 
   Use the real photos untouched except for cropping. Don't use AI to make or change any image.
3. Make a 5x5 board of all 25 so I can approve it.
```

4. Tweak: "darker fade, the photos are bright", "break the headline after 'nail'", "use a different photo on 16". Claude edits the script, re-renders.
5. Send 5x5 grid to client for approval, only finish what they approve
6. Same approach for carousels: 15 carousels × 5 slides, approved on three 5×5 grids

**Output:** 25 pixel-perfect posts (or carousels) per month, client-approved

**Cost:** $0

---

#### Part 2: Short Videos (Walkthrough + End Card)

**The Workflow:**
1. Pick 6–9 photos of one space in walking order (front door → room → details)
2. Paste into Claude Code:

```
Upload these photos to OpenArt in this order: [list files]. 
Make a 13-second vertical walkthrough with Seedance 2.0, image references (element-to-video), 
9:16, 480p, using this prompt:

Vertical 9:16 architectural walkthrough of a finished custom home. One continuous, smooth gimbal 
shot at chest height, slow and steady, like a high-end real estate film. Natural daylight, 
calm and premium. Strictly NO people, no faces, no bodies, no hands; no on-screen text, 
no captions, no logos, no watermarks.

Beat 1 (0-2.5s): exterior entry from image 1: [describe]. Door swings open, warm interior light.
Beat 2 (2.5-6s): through doorway into [room] from images 2-4: [materials]. Gentle forward push.
Beat 3 (6-9s): camera arcs slowly along [feature] from image 5 toward [feature] from image 6.
Beat 4 (9-11.5s): slow slide past [details] from images 7-9, showing grain and joinery.
Beat 5 (11.5-13s): eases back, holds wide hero view for last second.

Keep every material, colour and layout faithful to the reference photos. Do not invent rooms, 
furniture or decor.
```

3. Watch against photos. If it invents rooms or changes materials, regenerate. Never post a wrong one.
4. Finish in Claude Code:

```
Take the OpenArt video and:
- upscale it to 1080x1920
- add 4-5 timed captions in the same style as the posts (label + serif headline, italic last word)
- add a 2.5-second end card with logo, website, and phone
- replace OpenArt's audio with [music.mp3]
- export H.264 under 10 MB

Write it as a reusable script, so the next short is one command.
```

5. Music: Use one free track from Pixabay (free for commercial use) under every short so the account sounds consistent

**Output:** 1–4 short videos per month (13–15 seconds each)

**Cost:** ~$17/month for Seedance 2.0 at 480p (455 credits per 13-second video at ~$0.03/credit)

---

#### The Numbers

**Standard way (all AI images):**
- 25 singles at ~42 credits each: 1,050 credits
- 15 carousels × 5 slides at ~42 credits each: 3,150 credits
- Approval boards + grids: ~170 credits
- Total: ~4,400 credits/month (~$88)
- Plus shorts: 16 × 455 credits = ~7,280 credits (~$145)
- **Total standard: ~$233/month for images + shorts**

**Bryan's way:**
- Image posts: $0 (Claude Code, no OpenArt)
- 16 shorts: ~7,280 credits (~$17/month with bulk pricing)
- **Total: ~$17/month**

**The Margin:**
- Client pays: $600/month for 25 image posts + 16 shorts
- Tools cost: ~$17/month
- Margin: ~$583/month = **97%**

(This doesn't include Claude subscription or GHL/CRM costs, but Claude Max at ~$20/month spread across multiple clients is negligible per client.)

---

#### Key Rules (Each Learned Hard)

- **No AI versions of real people.** GPT Image turned owners into lookalikes. Real people only ever in their real photos.
- **No prices, ratings, years in business or licences** unless they're on the client's own site
- **OpenArt: generate one video at a time.** A 429 error means wait an hour, start fresh chat. Check result in OpenArt's Media tab; "created" status isn't proof.
- **Client approves the board or short before anything is scheduled**
- **Every "COMMENT [KEYWORD]" post needs a GHL workflow behind it** (comment contains keyword → reply → DM the link). Build it before the first one goes out.

---

## Lead Sourcing

### Stack #14: Reddit Lead Alerts (Automated Prospect Discovery)

**Concept:** Monitor Reddit 24/7 for people actively asking for help in your niche. Get Telegram alerts when matches are found. Reply with value. Close the deal.

**Why It Works:**
- Pure intent (prospects asking for solutions NOW, not browsing)
- No competition (most agencies don't monitor Reddit actively)
- Relationship starts real (you found them when they asked for help)
- Free (GitHub scheduler + Telegram = $0)
- Scalable (same setup works across multiple subreddits/keywords)

**The Stack:**

1. **GitHub Repository:** [neoswf/reddit-lead-alerts](https://github.com/neoswf/reddit-lead-alerts) (free, open-source)
2. **GitHub Actions Scheduler:** Runs every 30 minutes (free tier covers this)
3. **Telegram Bot:** Sends alerts to your phone (free)
4. **No coding required:** Copy the README into Claude, let Claude handle setup

**What It Monitors:**

- Watches multiple subreddits simultaneously (e.g., r/smallbusiness, r/localseo, r/GoogleMyBusiness, r/[city])
- Catches posts matching your keywords (e.g., "local SEO help," "looking for plumber," "Google Business Profile issue")
- Sends one alert per post (no duplicates even if cross-posted)

**The Alert Includes:**
- Post title
- Excerpt
- Why it matched (which keyword)
- Direct link to thread

**Setup (30 minutes, no coding):**

1. Go to [neoswf/reddit-lead-alerts](https://github.com/neoswf/reddit-lead-alerts)
2. Click "Use this template" → create private copy
3. Create a Telegram bot (free, 2 minutes)
4. Edit the settings file in your browser (add subreddits + keywords)
5. GitHub runs the job automatically every 30 minutes

**Real Example:**

First test caught a UK tree surgery business asking "honest local SEO help" in r/smallbusiness, r/GoogleMyBusiness, and r/localseo. One consolidated alert (no spam of three separate notifications).

**Refining Keywords (Week 1-2):**

First run will catch junk: SEOs asking each other questions, directory sellers, etc. That's normal.

- Give it a week
- Add phrases *real buyers* actually use
- Exclude what brings noise

**Best Subreddits by Niche:**

| Subreddit | Type | Quality |
|-----------|------|---------|
| r/smallbusiness | Owner questions | High intent |
| r/localseo | Targeted local SEO | High intent |
| r/GoogleMyBusiness | GBP-specific | Very high intent |
| r/[city] | Local, hyperlocal | High intent |
| r/[service] (e.g., r/Plumbing) | Niche professionals | Medium intent |
| r/SEO | SEO talk | Low intent (mostly other SEOs) |

**When You Reply:**

- Keep it useful. No pitch.
- Many subreddits ban self-promotion. Read rules first.
- Real value + your link = they'll click

**Rate Limits (Important):**

The tool fetches all subreddits in **one request every 30 minutes** and backs off for an hour if Reddit complains. **Keep this pace.** If lots of users hammer Reddit faster, GitHub gets blocked and breaks for everyone.

**Cost:** Completely free

**Timeline to First Lead:** 3-7 days (depends on subreddit traffic and keyword fit)

---

## The Pattern

Nobody is buying stacks off the shelf. They're:
- ✅ Stitching cheap APIs together
- ✅ Building custom MCPs
- ✅ Vibe-coding their own tools (Claude Code)
- ✅ Delegating tools instead of tasks
- ✅ Replacing SaaS subscriptions with Claude Max

---

## Implementation Approach

**Pick one job** costing you the most time right now:
- Writing & content generation → Stack #1–3
- Building sites & pages → Stack #4–6
- Lead capture & onboarding → Stack #7–9
- Scaling & research → Stack #10–11
- Video + multi-platform distribution → Stack #12

Copy just that one stack. Don't rebuild your whole toolkit. Solve one problem, then move to the next.

---

## Emerging Trend: SEO Now Is Prompts & Agents

The shift: **SEO is less about ranking and more about building prompts and managing agents.**

Key observation from Call #51:
- Justin rebuilt his entire SEO toolstack inside **Hermes** (an agent platform) in one week
- Picks any model per task via OpenRouter (the "grocery store of models")
- Agents self-learn instead of starting over every chat
- One agent: checks backlinks are alive → validates against trusted domains → checks if Google indexed → auto-indexes via Index Bolt

This represents a new meta-layer: instead of "rank for this keyword," the work becomes "design agents that rank for this keyword while learning and improving."

---

## Recommended Resources

- **Hermes Agent Platform:** [hermes-agent.org](http://hermes-agent.org)
- **OpenRouter (model marketplace):** [openrouter.ai](http://openrouter.ai)
- **Index Bolt (indexing at scale):** [indexbolt.com](http://indexbolt.com)
- **DataForSEO (SERP data):** [dataforseo.com](http://dataforseo.com)
- **Claude Code (build agents/tools):** [claude.com/claude-code](http://claude.com/claude-code)
