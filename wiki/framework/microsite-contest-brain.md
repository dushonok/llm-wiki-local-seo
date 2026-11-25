---
type: framework
client: none
status: active
updated: 2026-11-25
sources:
  - "raw/framework/⭐The Contest Brain AI Pack - 🚀 The Microsite Contest · AI SEO Rank Expand Academy.md"
  - "raw/framework/Microsite-Contest-Brain/START-HERE.md"
  - "raw/framework/Microsite-Contest-Brain/LLM-INSTRUCTIONS.md"
  - "raw/framework/Microsite-Contest-Brain/BRAIN.md"
  - "raw/framework/Microsite-Contest-Brain/MANIFEST.md"
---

# Microsite Contest Brain (AI Pack)

**What it is:** Rank Expand Academy’s frozen evidence pack from the **$1,000 Microsite SEO Contest** (Sep 15–Nov 18, 2026; **61 entries**, final check **Nov 17, 2026**). Built so an LLM can answer “what did we measure?” — not to re-teach the Playbook or Blueprint.

**Canonical copy in this repo:** `raw/framework/Microsite-Contest-Brain/` (member-only; do not redistribute outside Academy).

**Skool overview (how-to):** `raw/framework/⭐The Contest Brain AI Pack - 🚀 The Microsite Contest · AI SEO Rank Expand Academy.md`

## Precedence (when sources disagree)

| Priority | Source |
|----------|--------|
| 1 | `Microsite-Contest-Brain/BRAIN.md` — **60 numbered facts (F-*)** + **15 rules (R-01–R-15)** |
| 2 | `knowledge/12-corrections-log.md` |
| 3 | `data/*.csv` for positions (26 full checks **Oct 19–Nov 17**) |
| 4 | `knowledge/chapters/*`, handouts, `DECISIONS.md` |
| Last | `daily-updates/*` (nicknames, interim errors) |

**This wiki** defers to the Brain pack on any contest fact. Older wiki notes (e.g. Day 22 case study, Oct 12 parasite snapshot) are context only unless they match `BRAIN.md`.

**Learning order (Academy):** Microsite Playbook → Microsite Empire / Blueprint → **then** Contest Brain.

## Quick load (any chat assistant)

1. New chat or project.
2. Paste `LLM-INSTRUCTIONS.md` as system / project instructions.
3. Upload **`BRAIN.md`** + **`DECISIONS.md`** (~7,400 words together).
4. Ask with **service, town, site age, page count, listings**, and **page-one SERP** (pinned).

Validate with `TEST-QUESTIONS.md`.

## Full load (Cursor / coding agent)

Add the whole folder to the workspace (already under `raw/framework/Microsite-Contest-Brain/`). Point the agent at `START-HERE.md` and `MANIFEST.md` for file routing. Use `tools/PROMPTS.md` for copy-paste starters.

**Minimum files:** `LLM-INSTRUCTIONS.md`, `BRAIN.md`, `DECISIONS.md`.  
**Ranking checks:** `tools/make_search_link.py` + `results-08` chapter (pinned, non-personalized; footer must show town + “Results are not personalized”).

## How the assistant should behave

From `LLM-INSTRUCTIONS.md` (summary):

- **Decision first**, then cite fact numbers (e.g. F-27, R-08).
- Tags: **MEASURED**, **SITE**, **WINNER**, **READING** — do not invent numbers or results.
- **Do not re-teach** Playbook / Blueprint; send members there for build mechanics the contest did not test.
- **Audit flow:** `knowledge/13-pre-launch-checks.md` + scorer separators (F-23): home length, profiles in site code, address, FAQ markup, articles; compare listings to winner (F-27).
- **Reported, not recommended:** winner’s guest posts, cloud link pages, distributed press release, indexing tool (F-45–F-49) — least durable; half of guest posts gone a week after contest (F-46).
- **Never** recommend invented reviews, staff, licenses, fake addresses.
- **Winner’s HTML:** study structure; do not reuse copy. **Radon #1** (Blair’s site) — digest only; never entered, no full copy in pack.

## Example questions

- Is [service] in [town] worth building?
- My site dropped — what does the contest suggest?
- How many listings and which platforms first?
- Should I start a blog?
- Audit my site against contest separates.
- Plan first 30 days like the winner (`DECISIONS.md`, `winner-playbook-*` chapters).

## Contest outcome (final check)

| Result | Detail |
|--------|--------|
| **Winner (entered)** | Zeeshan Y. — **gettysburgmoldremediationpros.com** — mold **#1** — 50 pts |
| **2nd / 3rd** | Cyril G. mold #17; Kate S. mold #19 |
| **Radon** | No entered site top 20; Blair W. **#1 radon** with **absoluteradonmitigationllc.com** — **never entered** (honorable mention only) |

**Queries:** `mold remediation gettysburg pa`, `radon mitigation york pa`.

## Rules snapshot (R-01–R-15)

Full text in `BRAIN.md` §6. Headlines:

- **R-01** Market filter — pinned page-one read before domain buy.
- **R-02** Always measure pinned, not personalized.
- **R-03** Long homepage ranks (~3,750 words typical scorers; winner ~4,600 at first #1).
- **R-04** Homepage owns main keyword.
- **R-05–R-07** Research → write; unique town pages; `sameAs` / profiles in code + FAQ markup sitewide.
- **R-08** **20–25 listings first days**, then **5–10/week** (winner log **63**; **16** named in visible site code).
- **R-09** Time on platforms that **ranked** in contest, not generic parasites.
- **R-10** Finish site, launch, **stop editing** — weekly work = listings / posts / links.
- **R-11–R-14** Patience on volatility; blog schedule not batch dump; no blog/service overlap; steady social weekdays.
- **R-15** Real business with history beats new brand on harder query (radon case).

## Measured separates (F-23, mold scorers vs non-scorers)

Typical contrasts: **~3,758 vs ~2,083** home words; **profiles in code 5/10 vs 1/10**; street address **6/10 vs 1/10**; FAQ markup most pages **7/10 vs 2/10**; articles/guides **4/10 vs 1/10**.

## Pack layout (see `MANIFEST.md`)

| Area | Contents |
|------|-----------|
| Root | `BRAIN.md`, `DECISIONS.md`, `LLM-INSTRUCTIONS.md`, `TEST-QUESTIONS.md`, `MANIFEST.md` |
| `knowledge/` | Results, winner digests, radon #1 digest, pre-launch checks, corrections, timeline |
| `knowledge/chapters/` | Classroom `results-01`–`11`, `winner-playbook-1`–`8` |
| `data/` | Rankings CSVs, standings, winner listings/posts/links |
| `daily-updates/` | Contest-day narrative (use with caution) |
| `handouts/` | PDF + `.txt` mirrors |
| `winner-site/` | Study copy + `Winning-Site-LLM-Pack.md` (structure only) |
| `tools/` | `make_search_link.py`, `PROMPTS.md` |

## Where contest evidence goes beyond Blueprint

`BRAIN.md` §8 — longer homepage, separately written town pages, more listings in code, FAQ on all page types, blog optional for #1 (six posts enough). Blueprint minimums still stand; contest shows **optional upside**, not contradictions.

## Wiki pages to use with the Brain

| Page | Role |
|------|------|
| [[five-pillar-local-seo-framework.md]] | Operational pillars; contest counts in Brain refine timing/volume |
| [[parasite-ranking-data.md]] | Oct 12 tier snapshot; **R-09** + `data/` for winner’s ranking platforms |
| [[microsite-launch-checklist.md]] | Launch gates; pair with `knowledge/13-pre-launch-checks.md` |
| [[microsite-qa-reference.md]] | Q&A; **Day 22 case study superseded** — see below |
| [[external-seo-microsite-tactics.md]] | Off-page execution; defer listing counts to **R-08** / F-27 |
| [[microsite-code-location.md]] | Audit live builds against Brain rules in Cursor |

## Wiki contradictions resolved (notify: Brain wins)

These older wiki distillations conflict with the pack; **do not cite them for final contest facts**:

1. **`microsite-qa-reference.md` — Day 22 case study** — Interim leaderboard (mold ~#10, “~15 profiles”, “no press releases”, “build and leave alone only”). **Final:** winner **#1 mold**, **47 pages** at first #1 (not “~50 only”), **63 listings**, ongoing off-site work including **press release** (reported not recommended), **119-page batch was an accident** (corrections log Nov 25).
2. **`five-pillar-local-seo-framework.md`** — “Top 15 within 48h of big republish” is contest-era shorthand; Brain **R-10** + corrections emphasize **stop on-site edits** and weekly **listings/links/social**, not mandatory republish.
3. **`parasite-ranking-data.md`** — Built from **Oct 12** thread; Brain has **26 checks through Nov 17** and winner listing logs in `data/`.

When editing those pages for clients, cite **`BRAIN.md` fact/rule IDs** or this page instead of Day 22 narrative.

## Frozen limits

- Evidence: **two PA towns**, **two queries**, **~9 weeks**.
- Rankings **not leads**; one entered #1 ≠ guarantee for next niche.
- Data frozen **Nov 17, 2026** (+ post-contest notes in `knowledge/15-after-the-final-check.md`).

## Related

- Academy Winner’s Playbook (human-readable track) — linked from Skool AI Pack page; mirrored in `knowledge/chapters/winner-playbook-*`.