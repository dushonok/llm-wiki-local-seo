---
type: framework
client: none
status: active
updated: 2026-09-05
sources:
  - "raw/framework/AI Stacks Members Are Actually Using - 🎙️ The Wisdom's In The Calls · AI SEO Rank Expand Academy.md"
  - "raw/framework/51 - SEO Is Now Prompts and Agents - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
  - "raw/framework/49 - The 12-Minute Microsite - 🎙️ The Call Vault · AI SEO Rank Expand Academy.md"
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
