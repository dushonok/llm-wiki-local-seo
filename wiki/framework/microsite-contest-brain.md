---
type: framework
client: none
status: active
updated: 2026-11-26
sources:
  - "raw/framework/⭐The Contest Brain AI Pack - 🚀 The Microsite Contest · AI SEO Rank Expand Academy.md"
  - "raw/framework/2026-11-26-microsite-contest-brain-moved-to-contest-brain-agent.md"
  - "raw/framework/2026-11-26-contest-brain-agent-remote-github.md"
---

# Microsite Contest Brain (AI Pack)

**What it is:** Rank Expand Academy’s frozen evidence pack from the **$1,000 Microsite SEO Contest** (Sep 15–Nov 18, 2026; **61 entries**, final check **Nov 17, 2026**). Built so an LLM can answer “what did we measure?” — not to re-teach the Playbook or Blueprint.

**Canonical pack (local):** `C:\Projects\contest-brain-agent` — **standalone Cursor workspace / agent**; the pack is **not** stored in this wiki repo anymore (removed 2026-11-26).

**Git remote:** https://github.com/dushonok/contest-brain-agent.git — clone if the machine has no local checkout (`git clone` into `C:\Projects\contest-brain-agent` or your preferred path, then open that folder in Cursor).

**Skool overview:** `raw/framework/⭐The Contest Brain AI Pack - 🚀 The Microsite Contest · AI SEO Rank Expand Academy.md`

**This wiki page** is the map + distilled outcomes. **Contest numbers and rules** live only in the agent repo (`BRAIN.md`).

## Two workspaces

| Workspace | Use for |
|-----------|---------|
| **`C:\Projects\contest-brain-agent`** | “Use Brain” — audits, niche go/no-go, listing plans, F-/R- cites, CSV ranking history |
| **`llm-wiki-local-seo`** | Wiki maintenance, client profiles, deliverables, DataForSEO; link out to Brain agent for contest evidence |

## Precedence (when sources disagree)

Paths below are under `C:\Projects\contest-brain-agent\`.

| Priority | Source |
|----------|--------|
| 1 | `BRAIN.md` — **60 numbered facts (F-*)** + **15 rules (R-01–R-15)** |
| 2 | `knowledge/12-corrections-log.md` |
| 3 | `data/*.csv` (26 full checks **Oct 19–Nov 17**) |
| 4 | `knowledge/chapters/*`, handouts, `DECISIONS.md` |
| Last | `daily-updates/*` |

**This wiki** defers to the Brain pack on any contest fact.

**Learning order (Academy):** Microsite Playbook → Microsite Empire / Blueprint → **then** Contest Brain agent.

## Quick load (any chat assistant)

1. Open workspace **`C:\Projects\contest-brain-agent`**.
2. Paste `LLM-INSTRUCTIONS.md` as system / project instructions.
3. Load **`BRAIN.md`** + **`DECISIONS.md`** (~7,400 words).
4. Ask with **service, town, site age, page count, listings**, pinned **page-one SERP**.

Validate with `TEST-QUESTIONS.md`.

## Using Brain in Cursor (step by step)

### One-time setup

1. **File → Open Folder** → `C:\Projects\contest-brain-agent` (keep this separate from the wiki vault).
2. Project rule (recommended): *Follow `LLM-INSTRUCTIONS.md`; cite F-/R- from `BRAIN.md`; daily-updates lose to corrections log.*
3. **Live microsite HTML** → `C:\Projects\website-launchpad` ([[microsite-code-location.md]]) — open that folder when auditing code, not the Brain repo.

### Every new Brain-agent chat (minimum)

1. New Agent chat **in contest-brain-agent workspace**.
2. @-reference:
   - `LLM-INSTRUCTIONS.md`
   - `BRAIN.md`
   - `DECISIONS.md`
3. Include **service, town/state**, **domain age**, **page count**, **listing count**, pinned SERP if judging a market.
4. Templates: `tools/PROMPTS.md`.

**Sanity check:** `TEST-QUESTIONS.md`.

### Full evidence mode

Open files per `LLM-INSTRUCTIONS.md` routing (paths relative to contest-brain-agent root): `knowledge/13-pre-launch-checks.md`, `05-winner-own-account.md`, `06-winner-off-page-records.md`, `data/rankings_oct19_to_nov17.csv`, `knowledge/12-corrections-log.md`, `winner-site/Winning-Site-LLM-Pack.md` (structure only).

### Pinned ranking checks

`knowledge/chapters/results-08-how-to-check-your-real-rankings.md` + `tools/make_search_link.py`; footer must show town + “Results are not personalized”.

### Wiki agent + Brain agent together

1. Decide in **contest-brain-agent** (Brain output with F-/R- cites).
2. File client deliverables / update vault in **llm-wiki-local-seo** — paste Brain conclusions, do not duplicate the whole pack into `wiki/`.

### What not to do

- Do not expect contest files under `raw/framework/Microsite-Contest-Brain/` in the wiki repo (removed).
- Do not use Day 22 in [[microsite-qa-reference.md]] as final truth.
- Do not recommend winner guest posts / press / cloud pages as Academy advice (report only).

## How the assistant should behave

See `LLM-INSTRUCTIONS.md` in the agent repo (summary unchanged: decision first, cite facts, reported-not-recommended tactics, no invented addresses/reviews).

## Contest outcome (final check)

| Result | Detail |
|--------|--------|
| **Winner (entered)** | Zeeshan Y. — **gettysburgmoldremediationpros.com** — mold **#1** — 50 pts |
| **2nd / 3rd** | Cyril G. mold #17; Kate S. mold #19 |
| **Radon** | No entered site top 20; Blair W. **#1 radon** — **never entered** |

**Queries:** `mold remediation gettysburg pa`, `radon mitigation york pa`.

## Rules snapshot (R-01–R-15)

Full text in agent repo `BRAIN.md` §6. See prior wiki distill: R-01 market filter, R-02 pinned measure, R-03 long homepage, R-08 listing cadence, R-10 stop on-site edits, R-15 real business on harder query, etc.

## Pack layout

See `MANIFEST.md` in `C:\Projects\contest-brain-agent`.

## Wiki pages to pair with Brain

[[five-pillar-local-seo-framework.md]], [[parasite-ranking-data.md]], [[microsite-launch-checklist.md]], [[microsite-qa-reference.md]], [[external-seo-microsite-tactics.md]], [[microsite-code-location.md]]

## Wiki contradictions (Brain wins)

1. **Day 22 case study** — interim only; final winner stats in `BRAIN.md` + corrections log.
2. **Five pillars** — republish shorthand vs **R-10** off-site weekly work.
3. **Oct 12 parasite list** — use Brain `data/` + **R-09**.

## When you say “use Brain” in the wiki repo

The wiki agent should **not** pretend to hold the pack in context. Either:

- Ask you to run the **contest-brain-agent** workspace and paste conclusions, or  
- If both folders are available in one machine session, read **`C:\Projects\contest-brain-agent/BRAIN.md`** explicitly before answering contest-fact questions.

Default load: `LLM-INSTRUCTIONS.md` + `BRAIN.md` + `DECISIONS.md` from that path.