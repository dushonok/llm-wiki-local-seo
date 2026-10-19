# Raw capture: broken page CONFIRMED and root-caused via live browser inspection

Captured: 2026-10-19
Method: live browser navigation, accessibility snapshots, screenshots, and CDP
`Runtime.evaluate` calls against `https://groupenova.ca/en/services-2/interior-design-services/`
and comparison pages, prompted by the user providing a screenshot of the actual
broken render (`assets/...image-067358f6-0841-4283-817b-73d4b75df4e3.png` in the
agent's workspace). This supersedes the "doesn't match broken, flagged for
clarification" conclusion in `url-structure-and-content-depth-check-2026-10-19.md`
(that check used `curl`, which only sees raw HTML and cannot see client-side
rendering — the actual bug only shows up in a real browser).

## Confirmed: this is a real, reproducible rendering bug

Reloading `https://groupenova.ca/en/services-2/interior-design-services/` fresh
(twice, independently) reproduces exactly the blank-page symptom in the user's
screenshot: the page shows only a floating announcement-bar sentence ("Groupe
Nova encourages the expertise and products of Quebec and Canada.") and the
sticky phone-number footer bar, with no hero image, heading, body copy, or
contact form visible — even though the page's title, nav, and all body text are
present and correct in the DOM/accessibility tree (heading "Interior Design
Services", the 4-item "Advantages" list, the process/reviews sections, the
footer contact block, etc. all exist with correct text).

## Root cause: the contact form's phone country-code selector loads already expanded

The accessibility snapshot on a fresh load of this specific URL shows the
phone-field's country-selector `combobox` with `states: [expanded]`, immediately
followed by a `listbox` of all 244 country options rendered inline in the page
flow. On every other page checked (English kitchen-renovation, English
bathroom-renovation, French `renovation-de-cuisine`, the English and French
homepages), the equivalent combobox loads `states: [collapsed]` — closed, as
expected — and those pages all render correctly (hero image, heading, and body
copy all visible, confirmed via settled screenshots).

Because this specific page's country selector initializes already-open, its
244-row dropdown list — effectively a full page's worth of vertical space —
pushes into the document flow right after the first form fields, visually
burying the hero section and all body content beneath it. The page isn't
missing content; the content is there, just pushed far down the page behind an
unwanted, fully-expanded country picker that should never be open by default.

Pressing Escape collapses the stuck-open list, but even after that the real
page content still does not reappear — confirmed by screenshot after Escape —
so there is a second layer to this (the hero/body section's own visibility
doesn't recover once the page has rendered in this broken initial state; a
full page reload is needed, not just closing the dropdown).

## A related, second bug: the "Get your free quote" popup has the same stuck-open selector

Interacting with the page further (clicking around, which can trigger
Elementor's auto-popup) surfaced a second, related problem: an auto-opening
lead-generation popup ("Get your free quote," Elementor popup modal
`elementor-popup-modal-1668`) also has its own phone country-selector stuck
wide open the same way, burying its own "Submit" button under the same
244-country list. This suggests the underlying bug is in how the site's phone
input widget (the same component used in both the inline contact form and the
popup form) initializes its country-selector state — on this page/popup
instance it's defaulting to expanded instead of collapsed, while other
instances of the same widget elsewhere on the site initialize correctly. Not
confirmed whether this also affects the popup on other pages (it may be
intermittent/instance-specific) — worth a broader spot-check once a developer
has dashboard/code access.

## Scope: isolated to this one page (not a site-wide outage)

Explicitly re-checked, with fresh navigations and settled (non-premature)
screenshots: English kitchen-renovation, English bathroom-renovation, the
English homepage, and the French `renovation-de-cuisine` page all render
correctly — hero image, heading, and body text all visible as expected. Only
`/en/services-2/interior-design-services/` reproduces the blank-page bug on
every load tested.
