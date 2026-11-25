# Data notes

All positions come from one method: a Google search in a normal Chrome window with the location pinned to Gettysburg or York and personalization off. Only regular website results were counted. Mold was recorded to position 30 and radon to position 40.

| File | Rows | What it is |
|---|---|---|
| `rankings_oct19_to_nov17.csv` | 1,718 | Every result on every page for the 26 full checks. One row per result. `page` is the address, cut off at 80 characters. This is the source of truth. |
| `early_positions_sept23_to_oct18.csv` | 269 | Positions of contest sites only, taken from the daily updates. `location_pinned` is "no" before September 30: treat those as rough, they flatter new sites by 10 to 15 positions. No checks from October 5 to 15. |
| `entries_and_final_standings.csv` | 61 | One row per entered site: owner, final position, final points, best position, how many of the 26 checks it was seen on, how many it scored on, and its total if every check had counted. |
| `entered_sites_position_by_check.csv` | 363 | One row per entered site per check it appeared on. |
| `site_comparison.csv` | 54 | What each contest site was made of when copied, next to how it ranked: pages, words, home page words, town pages, articles, profiles in the code, FAQ markup, address, phone. A blank means the site could not be copied. |
| `winner_positions.csv` | 40 | The winning site's best position on every check, early and full. |
| `radon_number_one_positions.csv` | 26 | The radon number one's position on each of the 26 checks. |
| `winner_citations.csv` | 63 | The winner's own list of profiles and listings, in the order of his sheet, grouped, with whether each is named in his site code, whether it ranked, and what we found on November 25. |
| `winner_social_posts.csv` | 82 | Every social post in the winner's log: date, contest week, weekday, platform, title and address. Two TikTok rows repeat an address, as in his sheet. |
| `winner_links.csv` | 11 | His guest posts, press release and cloud pages, with the words used for each link, where it points, and its state on November 25. |
| `winner_blog_posts.csv` | 58 | Every blog post on the winning site with its publish date, title and length. |
| `winner_site_pages.csv` | 119 | Every page of the winning site as copied on October 27: type, title, main heading, words, headings, images, links and markup. |
| `after_contest_check_nov24.csv` | 64 | One follow up check a week after the contest. Not part of the contest record. |

## What the data cannot tell you

It shows what ranked and what each site was made of. It does not prove why. One contest, two searches, one entered site at number one.

Sites that were not on the entry sheet appear in the rankings file as results. No copy of any of them is in this pack.

Owners are shown as first name and last initial.
