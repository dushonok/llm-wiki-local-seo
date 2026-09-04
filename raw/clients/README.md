Drop client-specific source material here, in a subfolder per client:
`raw/clients/<client-slug>/`. Use the same slug you'll use under
`wiki/clients/<client-slug>/` (see AGENTS.md §4 for the slug convention).

Typical contents per client:
- Competitor site captures/crawls (saved HTML, screenshots, text dumps)
- Keyword & SERP data exports (rank tracker exports, Ahrefs/SEMrush, SERP screenshots)
- GBP & citation data
- Brand/brief documents the client gave you

Naming: `<what-it-is>-<YYYY-MM-DD>.<ext>`, e.g.
`raw/clients/acme-plumbing-co/rival-plumbing-co-crawl-2026-09-04.html`.

This folder is never edited by the LLM — only added to. Tell Claude to ingest
a new file (AGENTS.md §6) to fold it into that client's wiki pages.
