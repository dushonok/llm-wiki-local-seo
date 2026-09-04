# Templates

Reusable HTML/CSS/JSON skeletons. This layer is structural — it holds no client
copy. Content lives in `wiki/` as a content brief first; a template is what that
brief gets built into.

```
pages/       Single full-page HTML/CSS skeletons (e.g. local-service landing page,
             location page, contact page).
sections/    Reusable section partials to compose a page from (hero, service-area
             map, reviews carousel, FAQ, NAP/contact block, CTA banner).
sites/       Whole-microsite skeletons: multi-page nav structure, sitemap shape,
             shared header/footer — what a full microsite is assembled from.
schemas/     JSON schemas a wiki content brief must conform to before it's built
             into a page. See schemas/microsite-brief.schema.json.
```

## Conventions

- Name files by what they are, not by client: `pages/local-service-landing.html`,
  not `pages/acme-plumbing-landing.html`. Templates are reused across clients;
  client-specific content is injected from the matching `wiki/clients/<slug>/microsites/<slug>.md`
  brief.
- Every template should be able to be filled from a content brief's fields alone —
  if a template needs something a brief doesn't provide, either the brief schema
  is missing a field or the template is asking for something out of scope.
- When you (the LLM) add a new template, note it briefly in `wiki/log.md` and, if
  it changes what a content brief needs to supply, update the relevant schema in
  `schemas/`.
