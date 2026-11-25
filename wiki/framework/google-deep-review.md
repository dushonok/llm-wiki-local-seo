---
type: framework
client: none
status: active
updated: 2026-11-25
sources:
  - "raw/framework/google-deep-review-google-research.md"
---

# Google Deep Review

**What it is:** Public, agentic document review from Google Research — rigorous feedback on long, technical documents (logic, math, claims, consistency, grounding vs prior work). Evolved from **Paper Assistant Tool (PAT)** used in optional pre-submission pilots at STOC, ICML, NeurIPS, ICLR (16,000+ manuscripts). Not a search engine tool and **not** a systematic literature-review / PRISMA product.

**Portal:** https://research.google/deepreview/  
**API (alpha):** https://developers.google.com/deep-review/docs — upload, multi-stage review, Markdown report, PDF-anchored comments; bring your own **Gemini API key** for volume.

## How it works (four stages)

1. **Segmentation** — Splits the doc into logical sections (may overlap; full coverage).
2. **Adaptive budgeting** — More compute on dense sections (e.g. proofs, methodology) than light sections (e.g. intro).
3. **Parallel verification** — Section-focused agents with full-doc context for cross-references.
4. **Synthesis + grounding** — Merges critiques, consistency pass, external grounding / tool use to reduce hallucinated objections.

**Inputs (at launch):** PDF, plain text; multi-file across related docs coming soon.  
**Access:** **2 free document reviews per week** per user; higher limits via Gemini API + Deep Review API.  
**Privacy (Google’s stated policy):** Uploads are **not** used to train Google models; retained **~1 year** for UI display.

**What it is good at:** Cognitively heavy verification (internal consistency, technical claims, comparison to cited work, slide/deck flow, clause/table alignment in legal/finance-style docs per Google’s examples).  
**What stays human:** Novelty, taste, strategy, ethics, final publish/ship decisions.

## Limits (don’t misuse)

- **Discovery ≠ systematic review** — It critiques documents you already have; it does not replace documented search strategy, inclusion criteria, or reproducible screening for evidence synthesis.
- **Alpha API** — No SLA; endpoints may break.
- **Confidentiality** — Client contracts, unreleased financials, or PII-heavy exports are still uploaded to Google’s service under their retention policy — use redacted copies or client approval.
- **Not an SEO oracle** — It does not know your live SERPs, GBP, or GSC; it only stress-tests **what’s in the file**.

## Use cases for this wiki / local SEO practice

### High fit

1. **Pre-delivery QA on long client audits** — `recommendations.md`-style exports (50+ pages): catch contradictory priorities, claims that contradict earlier sections, missing evidence for a bold assertion.
2. **Microsite & content brief review** — Service/location page specs, schema notes, internal linking maps: consistency between H1, FAQ answers, `areaServed`, and GBP category language before build in [[microsite-code-location.md]].
3. **Sales / Upwork proposals** — Stress-test promises (timelines, deliverables, “guarantees”) for internal contradictions before send; aligns with standing proposal-honesty rules.
4. **Competitor / methodology write-ups** — Wiki or client-facing competitor memos where you cite stats and processes; flags unsupported leaps (you still verify sources in `raw/`).
5. **Deck + one-pager pairs** — Google explicitly mentions presentations; good for client kickoff decks vs written SOW.
6. **CI-style checks (later)** — When API is stable: optional gate on generated audit PDFs from an internal script (not ranking data).

### Medium fit

7. **Batch consistency (when multi-file lands)** — Entire microsite copy pack + schema JSON + GBP checklist submitted together for cross-doc NAP/service naming drift.
8. **Training internal SOPs** — Academy playbooks you author for VAs; logical gaps before delegation.

### Low fit / skip

- Keyword volume, SERP snapshots, rank tracking → **DataForSEO** (and existing wiki workflows).
- “Will this rank?” predictions from the model alone.
- Replacing human review of **grey-hat** or policy-edge tactics — tool won’t substitute compliance judgment.

## Related wiki pages

- [[ai-tool-stacks.md]] — Where to slot Deep Review in a QA pass vs generation stack.
- [[ai-overviews-local-search.md]] — Different Google surface (search behavior), not Deep Review.
- [[ranking-in-ai-overviews-semantics.md]] — On-page snippet craft; Deep Review can critique a draft, not replace PAA/DataForSEO research.
- [[local-seo-checklist.md]] — Checklist compliance in a **written** audit Deep Review can sanity-check, not execute.
- [[grey-hat-tactics-and-risks.md]] — Policy judgment stays human; do not outsource ethics calls to the reviewer.

## References

- Google Research portal: https://research.google/deepreview/
- Announcement: https://research.google/blog/analyzing-technical-documents-with-deep-review/
- PAT background paper (linked from blog): *Towards Automating Scientific Review with Google’s Paper Assistant Tool*
- Antigravity pattern: **Teamwork Deep Document Review** via `/teamwork-preview` (Google’s multi-agent pattern inspired by Deep Review)