# AGENTS.md — Local SEO LLM Wiki

This file is the schema for this wiki. It follows the pattern Karpathy describes
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent,
compounding knowledge base rather than RAG-over-static-docs. Read this file in full
before doing anything else in this vault.

## 1. Purpose

This vault is the working memory for local SEO client work: SEO research, local SEO
research, and local SEO optimization (including microsites) with one explicit goal —
**rank a given client's site (or a purpose-built microsite) for given keywords in a
given location.** Every page in `wiki/` should exist because it moves a client's
site or microsite closer to ranking, or because it's reusable knowledge that will
speed up the *next* client.

## 2. The three layers

```
raw/        Immutable source-of-truth. Never edit files here — only add.
wiki/       Distilled, interlinked knowledge. This is what you (the LLM) read
            and write. Every page here should trace back to something in raw/.
templates/  Reusable HTML/CSS/JSON skeletons — the output layer. Content briefs
            written in wiki/ get built into real pages using these.
```

**Rule: never edit or delete anything in `raw/`.** If a raw source turns out to be
wrong or outdated, note that in the relevant wiki page (with a link back to the
stale source) rather than touching the source. If the user wants a raw file
corrected, that's their call, not an automatic action.

**Rule: `wiki/` is the only layer you actively maintain.** Every ingest, query, or
lint pass reads and writes here.

**Rule: `templates/` is structural, not content.** Templates hold skeletons and
schemas (HTML/CSS/JSON). Actual client copy lives in `wiki/` as a content brief
first, then gets built into a page using a template.

## 3. Folder structure

```
raw/
  framework/                General SEO/local SEO reference material you're
                             feeding in: methodology docs, ranking-factor
                             research, on-site structure requirements,
                             link-building guides, checklists.
  clients/
    <client-slug>/           Everything client-specific and unedited:
                             competitor site captures/crawls, keyword & SERP
                             exports (rank trackers, Ahrefs/SEMrush), brand
                             docs, briefs the client gave us.

wiki/
  index.md                  Catalog of every page in the wiki. Kept current
                             on every ingest.
  log.md                    Append-only history of every ingest / query / lint.
  framework/                 Distilled, general-purpose SEO knowledge — not
                             tied to one client. This is what makes every new
                             client faster than the last one.
    on-site-seo.md
    backlinks.md
    local-seo-checklist.md
  clients/
    <client-slug>/
      profile.md             Business info, brand voice/constraints, target
                              locations, goals, target keywords at a glance.
      keywords.md             Keyword targets mapped to location + intent +
                              priority + current status.
      competitors/
        <competitor-slug>.md  One page per competitor analyzed for this client.
      recommendations.md     On-page SEO recommendations / gap analysis for
                              the client's existing site.
      microsites/
        <microsite-slug>.md  Status, target keyword/location, and content
                              brief for a microsite built for this client.

templates/
  pages/       Single-page HTML/CSS skeletons (e.g. a local-service landing page).
  sections/    Reusable section partials (hero, service-area map, reviews, FAQ, NAP block).
  sites/       Whole-microsite skeletons (multi-page structure, nav, sitemap shape).
  schemas/     JSON schemas that a content brief in wiki/ must conform to before
               it can be built into a page (see templates/schemas/microsite-brief.schema.json).
```

`raw/clients/<slug>/` and `wiki/clients/<slug>/` are created the first time that
client is onboarded (see §7). Don't pre-create empty client folders speculatively.

## 4. Slugs and naming

- Client slug: lowercase kebab-case business name, e.g. `acme-plumbing-co`. Use the
  same slug under `raw/clients/`, `wiki/clients/`, and anywhere else the client is
  referenced. Don't rename a slug once created — if the business is renamed, add the
  new name to that client's `profile.md` instead.
- Competitor slug: lowercase kebab-case domain or business name, e.g. `rival-plumbing-co`.
- Microsite slug: lowercase kebab-case `<service>-<location>`, e.g.
  `emergency-plumber-scarborough`.
- Dates: ISO `YYYY-MM-DD` everywhere (frontmatter, log entries, filenames when a date
  is part of the name).

## 5. Page frontmatter

Every page in `wiki/` (except `index.md` and `log.md`) starts with frontmatter:

```yaml
---
type: client-profile | keyword-map | competitor | recommendation | microsite-brief | framework
client: <client-slug> | none
status: draft | active | needs-review | archived
updated: YYYY-MM-DD
sources: [raw/clients/<slug>/..., raw/framework/...]
---
```

`sources` is mandatory whenever the page is derived from something in `raw/` —
this is what keeps the wiki traceable back to source-of-truth instead of becoming
an LLM's unverifiable opinion. A page synthesizing multiple sources lists all of them.

## 6. Operations

### Ingest
Triggered when the user adds something to `raw/` (or pastes/describes something
that should be saved there first) and wants it folded into the wiki.
1. Read the raw source in full.
2. Identify what wiki page(s) it affects — an existing page to update, or a new
   page to create. Prefer updating an existing page over creating a near-duplicate.
3. Discuss the key takeaways with the user before writing, if the source is
   substantial or the implications aren't obvious (e.g. "this competitor capture
   shows they have dedicated location pages for all 12 service areas — should I
   flag this as a gap in acme-plumbing-co's recommendations.md?").
4. Write/update the wiki page(s), with `sources` pointing at the new raw file(s).
5. Update `wiki/index.md` if a page was added.
6. Append an entry to `wiki/log.md`.

### Query
Triggered when the user asks a question.
1. Check `wiki/index.md` for relevant pages before searching blindly.
2. Synthesize an answer from wiki pages, citing which page(s) it came from.
3. If answering required connecting facts that aren't already cross-linked in the
   wiki (e.g. a pattern across three competitor pages), consider whether that
   synthesis is worth filing back as a new or updated wiki page — that's how the
   wiki compounds instead of re-deriving the same answer next time.

### Lint
Run periodically, or when asked ("lint the wiki", "check <client> for gaps"):
1. Look for contradictions between pages (e.g. `keywords.md` targets a keyword
   `recommendations.md` doesn't address).
2. Flag stale pages — `status: active` pages not `updated` in a long time, or pages
   whose `sources` predate a newer raw capture on the same topic.
3. Flag orphan pages — not linked from `index.md` or any other page.
4. Flag missing cross-references — e.g. a competitor page mentioning a keyword that
   isn't in the client's `keywords.md`.
5. Report findings to the user rather than silently "fixing" them, unless the fix
   is unambiguous (e.g. adding a missing index.md entry).

## 7. Onboarding a new client

1. Create `raw/clients/<client-slug>/` and `wiki/clients/<client-slug>/`.
2. Ingest whatever the client/brand brief is into `wiki/clients/<client-slug>/profile.md`.
3. As keyword research, competitor captures, and SERP data come in, ingest each
   into `keywords.md`, `competitors/<slug>.md`, etc.
4. Once there's enough to act on, produce the deliverable the user asked for:
   `recommendations.md` (on-page SEO recs, competitor gap analysis) and/or
   `microsites/<slug>.md` (content brief conforming to
   `templates/schemas/microsite-brief.schema.json`) that a template in `templates/`
   can be built from.

## 8. Deliverables this wiki exists to produce

- On-page SEO recommendations for a client's existing site → `recommendations.md`.
- Competitor gap analysis and local SEO checklists (GBP, citations, NAP) → same file,
  or split into `competitors/` + a checklist section if it gets long.
- Microsite content briefs/outlines that feed `templates/` → `microsites/<slug>.md`,
  conforming to `templates/schemas/microsite-brief.schema.json`.

When producing any of these, always link back to the wiki pages (and ultimately raw
sources) the recommendation is based on — no unsourced claims about a competitor or
a keyword's difficulty.

## 9. Open questions / not yet decided

- Whether framework pages (`wiki/framework/`) get a lint pass for staleness against
  evolving Google algorithm guidance — revisit once there's enough framework content
  to matter.
