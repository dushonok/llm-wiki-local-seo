---
title: "AI SEO: Rank Expand Academy"
source: "https://www.skool.com/rank-expand-academy/even-better-than-formspree"
author:
published:
created: 2026-10-21
description: "Get your first AI SEO client in 90 days or your money back. Daily coaching, microsite templates, AI workflows & more. Scale to $10,000+ for $99/mo."
tags:
  - "clippings"
---
Even better than Formspree

I am Replacing Formspree with my own lead endpoint on Cloudflare

And you can too...

If you’re running static sites on Pages, you can

drop Formspree entirely.

~170 lines of Worker writes every lead to a

D1 database first, then emails it.

Why it’s worth the swap:

• A wrong Formspree endpoint still shows a thank-you page.

No error, anywhere. I nearly shipped a site with another

site’s endpoint baked into all the pages.

• You can’t test Formspree. It returns identical responses

for a real form id and a fake one — the only way to verify is

a real lead going through.

• Leads become a database you can

[query.SELECT](http://query.SELECT "http://query.SELECT") count(\*) WHERE site = ?

is what you show a contractor

to rent him the site.

An inbox can’t produce that.

• No per-site manual step. One command provisions a new site.

• Storage outlives notification.

My email path broke mid-build — three

leads came in, all three stored

flagged emailed=0

Formspree would have given me silence!

• Free at microsite scale.

here's the Three files and a setup script:

[https://github.com/bacioni/cloudflare-lead-endpoint](https://github.com/bacioni/cloudflare-lead-endpoint "https://github.com/bacioni/cloudflare-lead-endpoint")

(gitHub repo link)

Two Cloudflare gotchas are documented in there

that aren’t in any docs — they cost me an afternoon.

Youre welcome, Shaggers.