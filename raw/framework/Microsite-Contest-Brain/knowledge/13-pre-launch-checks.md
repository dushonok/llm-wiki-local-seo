# The pre-launch checks

30 checks in 7 groups, built from the faults found again and again when auditing member microsites during the contest. No site or owner is named.

Use it to audit a site: for each line say pass, fail or cannot tell, and what you looked at. The note under a check says what we actually found on member sites.

## 1. Can Google get in?

- [ ] **No page you want ranked carries a "noindex" tag.** One member site had it on every page and could not work out why nothing was indexed.
- [ ] **robots.txt exists, allows the site and names your sitemap.** A missing file or a leftover "Disallow: /" from the build stops everything.
- [ ] **sitemap.xml lists every page, with dates.**
- [ ] **A page that does not exist shows a real "not found" page with links back into the site.** Several sites returned a blank white page.

## 2. Does every address lead to one place?

- [ ] **http, https, www and non www all end up on one version of the site.** The most common technical miss. On one site the www address did not load at all.
- [ ] **Every page has a canonical tag that points to itself.**
- [ ] **Addresses are clean, with no broken characters and no pages that load at two addresses.** Watch town names with accents, and pages that work both with and without ".html".
- [ ] **No build files are public.** One site had its README, with setup notes and phone numbers, open to anyone.

## 3. Does each page stand on its own?

- [ ] **The home page has about 1,200 words or more.**
- [ ] **Each service page has 800 to 1,200 words, and each one covers a different job.** Do not split one service into four near identical pages.
- [ ] **Each town page has about 800 words and could only be about that town.** If you can swap the town name and it still reads fine, it is too generic.
- [ ] **You have a few strong town pages, not dozens of thin ones.** Eight to ten written properly beat thirty at 400 words.
- [ ] **The home page and your main town page do not share the same main heading.** They end up competing with each other. This showed up on site after site.
- [ ] **Sister sites do not target the same town.**
- [ ] **The site gives real price ranges with a source.** Cost is the most searched question in almost every trade, and many sites said only "it depends".

## 4. Is it honest?

- [ ] **No invented owners, staff, years in business, licenses or reviews.**
- [ ] **No leftover draft notes from the AI.** Search the site for "placeholder", "proposed", "illustrative" and "replace before".
- [ ] **If you pass leads to a contractor, the main copy says so, not only the footer.**
- [ ] **Promises like free estimates and 24/7 service are only there if the contractor agreed to them.**
- [ ] **The business name is spelled the same way everywhere.**

## 5. Will a lead reach you?

- [ ] **You sent a test through every form and it arrived.** One site had forms that looked fine and sent nowhere.
- [ ] **One phone number appears in the page, in the code and on every listing, and you have called it.** One site showed three different numbers depending on how the page was read.
- [ ] **The number is local to the area you serve.**

## 6. Does the code describe the business?

- [ ] **LocalBusiness schema with the name, phone number and area served.** Not "Organization" on its own, and not missing altogether.
- [ ] **FAQ schema on your FAQ sections, and Service schema on service pages.**
- [ ] **Every image has alt text that describes the picture.** Not the keyword repeated on every image.
- [ ] **Every page has its own title and description.**

## 7. After launch

- [ ] **Build your profiles in the first week, with the exact name and number from the site.** See the Profile Checklist.
- [ ] **Check your position the right way, from the town.** See How to Check Your Real Rankings.
- [ ] **Stop editing and give Google a few weeks.** The contest winner did not touch his site for the last three weeks.
