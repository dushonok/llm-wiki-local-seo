---
title: "AI SEO: Rank Expand Academy"
source: "https://www.skool.com/rank-expand-academy/how-i-make-the-posts-and-the-shorts-claude-code-openart"
author:
published:
created: 2026-10-15
description: "Get your first AI SEO client in 90 days or your money back. Daily coaching, microsite templates, AI workflows & more. Scale to $10,000+ for $99/mo."
tags:
  - "clippings"
---
How I make the posts and the shorts (Claude Code + OpenArt)

A few of you asked how I made these, so here's the whole process. Short version: the image posts aren't AI at all. Claude Code builds them in code on top of the client's real photos. The short starts in OpenArt (Seedance makes the walkthrough from the photos), and then Claude Code finishes it.

ONE-TIME SETUP (about 15 minutes)

1\. Claude Code. Install the Claude desktop app and open the Code tab, or use the terminal version. Make one folder per client and open Claude in that folder.

2\. Connect OpenArt to Claude. In a terminal, run:

claude mcp add --transport http --scope user openart [https://mcp.openart.ai/mcp](https://mcp.openart.ai/mcp "https://mcp.openart.ai/mcp")

Then type /mcp inside Claude Code, pick openart and click Authenticate. Sign in with the OpenArt account you want billed. Check it worked by asking Claude: "show my OpenArt account and credits."

3\. Tools. Ask Claude: "Make sure Python, Pillow and ffmpeg are installed on this machine." It installs whatever's missing.

4\. Optional: connect GoHighLevel (Settings > Connectors > HighLevel). Claude can then upload to Media Storage and schedule straight into the Social Planner.

PART 1: THE IMAGE POSTS (made in Claude Code, no AI)

Why not AI? Image models redraw the photo. The client's actual kitchen comes back slightly different, and the text gets misspelled. Built in code, the photo stays exactly as shot and every word is exact. It costs nothing, and re-rendering all 25 takes seconds.

1\. Get the client's real photos into a folder. If they're camera RAW files (.RW2, .CR2, .NEF), ask: "Convert the RAW files in this folder to JPG at 2560px."

2\. Find a design you like. Screenshot a post from a brand in the niche. Mine was a big builder's "How we build" carousel: full-bleed photo, dark fade, serif headline.

3\. Paste this into Claude Code with the screenshot attached:

\---

Here's a screenshot of a post design I like. My client's project photos are in \[folder\]. Their website is \[URL\]. Only use facts from the website.

1\. Plan 25 Instagram posts: 5 Education, 5 Inspiration, 5 Process, 5 Comparison, 5 Trust. Short headlines. Put "COMMENT \[KEYWORD\]" on exactly 5 of them.

2\. Write a Python/Pillow script that renders each post at 1080x1350 in the style of the screenshot: full-bleed photo, dark fade at the bottom, small letter-spaced brand name top-left, a small letter-spaced label, a serif headline with the last word in italic (Source Serif 4 from Google Fonts), a light sans subtitle and a thin white rule. Use the real photos untouched except for cropping. Don't use AI to make or change any image.

3\. Make a 5x5 board of all 25 so I can approve it.

\---

4\. Tweak in plain English. For example: "darker fade, the photos are bright", "break the headline after 'nail'", "use a different photo on 16, that one's blown out". Claude edits the script and re-renders.

5\. Send the board to the client and only finish the posts they approve. Same idea for carousels: 15 carousels x 5 slides, approved on three 5x5 grids with one carousel per row.

PART 2: THE SHORT (OpenArt Seedance, finished in Claude Code)

1\. Pick 6-9 photos of one space in walking order: front door > the room > the details.

2\. Paste this into Claude Code:

\---

Upload these photos to OpenArt in this order: \[list files\]. Make a 13-second vertical walkthrough with Seedance 2.0, image references (element-to-video), 9:16, 480p, using this prompt:

Vertical 9:16 architectural walkthrough of a finished custom home. One continuous, smooth gimbal shot at chest height, slow and steady, like a high-end real estate film. Natural daylight, calm and premium. Strictly NO people, no faces, no bodies, no hands; no on-screen text, no captions, no logos, no watermarks.

Beat 1 (0-2.5s): exterior entry from image 1: \[describe it\]. The camera glides up to the door; the door swings open on its own, revealing warm interior light.

Beat 2 (2.5-6s): through the doorway into \[the room\] from images 2-4: \[materials you can see\]. Gentle forward push.

Beat 3 (6-9s): the camera arcs slowly along \[feature\] from image 5 and turns toward \[feature\] from image 6.

Beat 4 (9-11.5s): slow slide past \[details\] from images 7-9, showing grain and joinery.

Beat 5 (11.5-13s): eases back and settles on a wide hero view, holding still for the last second.

Keep every material, colour and layout faithful to the reference photos. Do not invent rooms, furniture or decor.

\---

3\. Watch it against the photos. If it invents a room or changes the materials, regenerate. Never post a wrong one.

4\. Finish it in Claude Code:

\---

Take the OpenArt video and:

\- upscale it to 1080x1920

\- add 4-5 timed captions in the same style as the posts (label + serif headline, italic last word)

\- add a 2.5-second end card with the logo, website and phone

\- replace OpenArt's audio with \[music.mp3\]

\- export H.264 under 10 MB (the GHL uploader caps files at 10 MB)

Write it as a reusable script, so the next short is one command.

\---

5\. Music: OpenArt's built-in audio comes out soft. I use one track from Pixabay (free for commercial use) under every short, so the account sounds the same each time.

Cost: Seedance 2.0 at 480p is about 455 OpenArt credits for 13 seconds, about 525 for 15. 720p costs a bit more than double. The image posts cost nothing.

RULES I FOLLOW (they've each bitten me once)

\- No AI versions of real people. GPT Image turned the owners into lookalikes. Real people only ever appear in their real photos. Walkthrough shorts have no people at all.

\- No prices, star ratings, review counts, years in business or licences unless they're on the client's own site.

\- OpenArt: generate videos one at a time. A 429 error means wait an hour and start a fresh chat. Check the result in OpenArt's Media tab; "created" isn't proof.

\- Client approves the board or the short before anything is scheduled.

\- Every COMMENT keyword post needs a GHL workflow behind it (comment contains keyword > reply > DM the link). Build it before the first one goes out.

Happy to answer questions in the comments.

[https://openart.ai/suite/share/T1VnWFluWXEzSGJKNmloS1BWZkQ7aHR0cHM6Ly9jZG4ub3BlbmFydC5haS9vcGVuYXJ0LWFpL3Byb2R1Y3Rpb24vMjAyNi0wOS9jcmVhdGUtdmlkZW8vdXNlcl8zSWdOV0ZUWk9pZjN0TnZSTGVyeEZZSEdKMjIvMDIxNzg4Mjg5NjA2ODUyMDAwMDAwMDAwMDAwMDAwMDAwMDBmZmZmYzBhOGIzZWEyZWJiNzVfMTc4ODI4OTkwNzMzMV9iZmIzOTcwZS5tcDQ](https://openart.ai/suite/share/T1VnWFluWXEzSGJKNmloS1BWZkQ7aHR0cHM6Ly9jZG4ub3BlbmFydC5haS9vcGVuYXJ0LWFpL3Byb2R1Y3Rpb24vMjAyNi0wOS9jcmVhdGUtdmlkZW8vdXNlcl8zSWdOV0ZUWk9pZjN0TnZSTGVyeEZZSEdKMjIvMDIxNzg4Mjg5NjA2ODUyMDAwMDAwMDAwMDAwMDAwMDAwMDBmZmZmYzBhOGIzZWEyZWJiNzVfMTc4ODI4OTkwNzMzMV9iZmIzOTcwZS5tcDQ "https://openart.ai/suite/share/T1VnWFluWXEzSGJKNmloS1BWZkQ7aHR0cHM6Ly9jZG4ub3BlbmFydC5haS9vcGVuYXJ0LWFpL3Byb2R1Y3Rpb24vMjAyNi0wOS9jcmVhdGUtdmlkZW8vdXNlcl8zSWdOV0ZUWk9pZjN0TnZSTGVyeEZZSEdKMjIvMDIxNzg4Mjg5NjA2ODUyMDAwMDAwMDAwMDAwMDAwMDAwMDBmZmZmYzBhOGIzZWEyZWJiNzVfMTc4ODI4OTkwNzMzMV9iZmIzOTcwZS5tcDQ")

Here's what it costs the way I do it.

Done the standard way, with every image generated in OpenArt (GPT Image 2, about 42 credits an image), one client's month is:

- 25 singles: 1,050 credits

- 15 carousels x 5 slides: 3,150 credits

- Approval board + grids: about 170 credits

That's about 4,400 credits a month just for the images.

My way: 0 credits. The singles and carousels are built in Claude Code on top of the client's real photos, so nothing goes through OpenArt.

So I put those credits into the shorts instead. The package is 12 shorts a month; I'm giving him 4 extra, so he gets 16. Each short is about 455 credits (Seedance 2.0, 13 seconds, 480p).

The numbers:

- Client pays: $600 a month

- OpenArt: 16 shorts x 455 credits = about 7,280 credits, about $17

- We pull in: about $583 a month

The margin is about 97%: $583 ÷ $600 = 0.972.

That's after the OpenArt credits only, so it doesn't count your Claude subscription, GHL\CRM or anyone's time.
