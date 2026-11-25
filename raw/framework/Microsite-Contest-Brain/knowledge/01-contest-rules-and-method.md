# The contest: rules and how it was measured

## The rules

- **Name:** the Microsite $1,000 SEO Contest, run inside the Rank Expand Academy.
- **Dates:** September 15 to November 18, 2026.
- **The task:** build a brand new microsite and rank it on Google for one or both of two searches.
  - "mold remediation gettysburg pa"
  - "radon mitigation york pa"
- **Eligibility:** the domain had to be registered on or after September 15 and submitted on the official entry sheet by September 20.
- **Entries:** 61 websites from 32 contestants. Two sites were entered after the deadline and could not score.
- **Scoring:** points for each entered site's position in the regular Google results on the final check. 50 points for position 1, then 40, 34, 29, 25, 22, 19, 16, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2 and 1 for positions 2 to 20. Nothing below 20. A contestant's score was the total across their entered sites.
- **The deciding check:** November 17, 2026.
- **Prizes:** $1,000 for first, $500 for second, $250 for third.
- **Release of sites:** under the contest rules, copies of entered sites may be shared with members for study.

## How every ranking was measured

1. A normal Chrome window.
2. A Google search link with the location pinned to the town (Gettysburg or York) and personalization switched off.
3. The footer of the results page had to show the town and the words "Results are not personalized". If it did not, the check was thrown out.
4. Only the regular website results were counted. Ads, the map box, the AI answer, the "people also ask" box and the forums box were skipped.
5. Mold was recorded to position 30. Radon was recorded to position 40.
6. Each site was counted once, at its best page.
7. One page of results was loaded at a time, slowly, about ten page loads per day.

The tool that builds the pinned search link is in `tools/make_search_link.py`.

## Why the method matters

On September 30 the same search was run two ways on the same day.

| Method | Contest sites scoring on mold | Contest points on mold |
|---|---|---|
| Pinned to Gettysburg, not personalized | 2 | 10 |
| Not pinned | 9 | 55 |

A search made from a desk in another town shows new sites 10 to 15 positions higher than someone in the town sees them, because Google ranks real local businesses higher for a local searcher. Every check before September 30 was unpinned and overstated the contest sites.

## What data exists

| Period | What we have | How reliable |
|---|---|---|
| September 23 to 29 | Positions of contest sites only, from the daily updates | Rough. Not pinned. |
| September 30 to October 18 | Positions of contest sites only, from the daily updates | Pinned. No checks from October 5 to 15. |
| October 19 to November 17 | Every result on every page, 26 checks | Complete. This is the data every count in the pack uses. |

Always say "26 full checks, October 19 to November 17" when counting.

## Copies of the sites

On October 24 a copy was taken of every contest site that could be reached. The comparison of sites that scored against sites that did not uses those copies. The winning site was copied on October 26 with 47 pages and on October 27 with 119 pages.
