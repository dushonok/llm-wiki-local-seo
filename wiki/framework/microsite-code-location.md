---
type: framework
client: none
status: active
updated: 2026-11-26
sources:
  - "user instruction (2026-11-23): canonical microsite build output path"
  - "raw/framework/2026-11-26-microsite-contest-brain-moved-to-contest-brain-agent.md"
  - "wiki/framework/external-seo-microsite-tactics.md (prior live reviews of launchpad builds)"
---

# Microsite code location (website-launchpad)

**Purpose:** Tell agents where the user's live microsite HTML/builds live so code-vs-wiki reviews use real files, not assumptions.

## Related workspace: Contest Brain agent

**Contest evidence KB:** `C:\Projects\contest-brain-agent` (standalone project — not in this vault). Remote: https://github.com/dushonok/contest-brain-agent.git. See [[microsite-contest-brain.md]]. Use that workspace for “use Brain”; use **website-launchpad** for deployed HTML.

## Canonical path

**Root (Windows):** `C:\Projects\website-launchpad`

Each deployment is usually a **sibling folder** under that root (e.g. `Sewer-Line-Repair-San-Diego-CA`). See [[external-seo-microsite-tactics.md]] for lessons from 2026-10-13 reviews of San Diego and Portland sewer builds.

## When the user asks for a code review

1. Read the site tree they name under `website-launchpad` (or the whole root if unspecified).
2. Cross-check against wiki doctrine: [[microsite-launch-checklist.md]], [[on-site-seo.md]], [[external-seo-microsite-tactics.md]], [[local-seo-playbook-maverick.md]] (and [[ai-reliability-and-context.md]] if the ask is about Claude/build context).
3. Report each gap as **wiki rule → what the code does**.

## Environment notes

- Cloud agents need `website-launchpad` **in the workspace** to read files; if missing, ask the user to add `C:\Projects\website-launchpad` (or the site subfolder).
- Launchpad folders are **not** wiki clients unless `wiki/clients/<slug>/` exists — treat reviews as audits unless onboarded.