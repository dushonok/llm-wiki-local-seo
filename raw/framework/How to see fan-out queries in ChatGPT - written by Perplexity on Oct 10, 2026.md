# Me:

Trying a **live network capture** during the response or a different ChatGPT version/session that still writes fan-out metadata to the persisted conversation object.
![[Pasted image 20261010085447.png]]


# Perplexity:
You have a filter problem—not a failed capture. Your Network tab shows **`0 / 107 requests`**, which means Chrome captured 107 requests but your current filter hides every one.

The filter field contains **`service`**. Clear that first. The project files have no relevant troubleshooting material.

## Fix the Network view

1. Click inside the filter box directly under the Network toolbar—the one currently containing `service`.
    
2. Press `Ctrl + A`, then `Backspace`.
    
3. You should immediately see the full request list. The bottom counter should change from:
    
    - `0 / 107 requests`
        
    - to approximately `107 / 107 requests`
        
4. Click **Fetch/XHR** first. If nothing useful appears, also test **Other** and **EventStream** if your Chrome version shows it.
    

Your screenshot confirms:

- **Preserve log** is enabled — good.
    
- **Disable cache** is enabled — fine.
    
- The recorded requests exist — 107 total.
    
- They are simply hidden by the filter text.
    

## Capture a fresh search

The current 107 requests may largely be page assets or prior activity. Once you have cleared the filter:

1. Click the **clear** icon in Network—the circle-with-slash icon next to the red record button.
    
2. Leave the red recording indicator active.
    
3. Keep **Preserve log** checked.
    
4. In ChatGPT, submit a new search-enabled question—not “give 5 more.” Use a standalone, citation-heavy prompt:
    
    > Search the web for the best local SEO agencies in Montréal for home-service businesses. Cite every agency-specific claim and show official site, third-party proof, Google Maps expertise, and pricing where public.
    
5. Wait for the answer, citations, and map to finish loading.
    
6. In Network, try each filter separately:
    
    - `conversation`
        
    - `backend-api`
        
    - `search`
        
    - `sse`
        
    - `eventstream`
        
    - `citation`
        

Do **not** include several filter words at once initially. You want to see what endpoints ChatGPT is actually using.

## Which request to open

Look for an entry that is:

- **Type:** `fetch`, `xhr`, `eventstream`, or sometimes `other`
    
- **Size:** relatively large compared with analytics/assets
    
- **Timing:** starts precisely when you pressed Send
    
- **Name/URL:** contains terms like `conversation`, `backend-api`, `sse`, `responses`, `search`, or a long conversation ID
    

Click it, then use the right-side request pane:

1. Open **Response**. If that is blank, try **Preview**.
    
2. Press `Ctrl + F`.
    
3. Check these one at a time:
    
    - `search_model_queries`
        
    - `search_query`
        
    - `search_result`
        
    - `sources_footnote`
        
    - `supporting_websites`
        
    - `citation`
        
    - `safe_urls`
        
    - `url`
        

## What the result means

|You find|Meaning|
|---|---|
|`search_model_queries`|You have the hidden fan-out queries; copy the full response or save it as HAR|
|`citation`, `sources_footnote`, or `safe_urls`|You can extract the URLs, even if fan-out queries are unavailable|
|Only visible assistant text / no search keys|ChatGPT searched but did not expose the retrieval trace in your browser payload|
|No likely request after clearing and submitting again|ChatGPT may be using a streamed connection; inspect **Other**, **Fetch/XHR**, and any EventStream-style request|

## Your exact next screenshot

After you clear `service`, clear the request list, submit one fresh web-search prompt, and filter by **`conversation`**, take a screenshot showing:

- the Network request list,
    
- the likely request selected, and
    
- the **Response** or **Preview** panel.
    

That will tell us whether the fan-out is being sent live and, if so, exactly where to extract it.

# Me:

here we go - I do not see much
![[Pasted image 20261010085748.png]]
# Perplexity

You found the right request. The row named **`conversation`** with status **200**, type **fetch**, and size **28.0 kB** is the one to inspect. The six `user-…` entries are WebSocket connections and are not the useful place to start.

Your Network filter is currently limiting the view to seven entries, which is fine—the key `conversation` response is visible. The project files don’t include any further relevant tooling guidance.

## Next click: inspect `conversation`

1. Click the bottom row named **`conversation`**.
    
2. A details pane should open on the **right**, **bottom**, or inside the DevTools area.
    
3. Select the **Response** tab.
    
4. Click inside the response body and press `Ctrl + F`.
    
5. Search these exact strings, one at a time:
    

text

`search_model_queries`

text

`search_result`

text

`sources_footnote`

text

`citation`

text

`safe_urls`

text

`url`

Your screenshot is exactly at the point before the needed step: you have selected neither the request nor its response body yet.

## What each outcome means

|In the `conversation` response|Interpretation|Next action|
|---|---|---|
|`search_model_queries`|Hidden fan-out queries are present|Copy the nearby JSON block; that is the usable query list|
|`citation`, `sources_footnote`, or `safe_urls`|Source URLs are stored, even if fan-outs are not|Extract URLs from that section|
|Only assistant text and basic metadata|The answer is saved, but its retrieval trace was removed|Inspect the WebSocket frames next|
|No `conversation` content / Response tab empty|The useful data was delivered through WebSocket streaming|Inspect the `user-…` connections|

## If the `conversation` response has no useful keys

Then inspect a WebSocket connection **before assuming data is unavailable**:

1. Click the first `user-RTp1gk…` row.
    
2. In its detail panel, look for **Messages** or **Frames**.
    
3. Open it.
    
4. Use `Ctrl + F` for:
    
    - `search`
        
    - `query`
        
    - `citation`
        
    - `url`
        
    - `source`
        
    - `result`
        

A connection appearing **Pending** is normal for WebSockets—it can remain open while ChatGPT sends or receives data.

## One correction to the earlier process

The very large timeline values and request count mean you have retained a lot of prior browsing activity, even though the useful conversation fetch is isolated now. For a clean test later:

1. Click the clear icon in Network.
    
2. Submit a brand-new web-search prompt.
    
3. Wait for the completed answer.
    
4. Inspect the new `conversation` fetch immediately.
    

But right now, you do **not** need to restart. Click **`conversation` → Response** and search first.

# Me:
is this what we need?

![](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/154523337/be955359-44c7-419e-935e-43796fe92d57/image.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYEV5CJOLU4%2F20261010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261010T125627Z&X-Amz-Expires=3291&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIDbwhWu7yTvPA0ereNBlThDraZHWqf3CWb6o3TgkQIlEAiBTsHtBKphvf7RBOb0Lz2adDlQ5wyUn6lfnWw5x98wI9CqABQhVEAEaDDY5OTc1MzMwOTcwNSIMr7mFYIUviB8QGV1mKt0ExP0GzICZWml%2BaDtMcgvCKXgnVTktzCCQ8i%2Bat1YGXAcg02Cq%2BKH61NxQ5m76lunyspHFKkm2NkLp%2F52cYZz5%2B8ZC%2FuHH59eYRScV588M15rMKqNbrP173Z7%2B11KrGzB7tryx%2Fgwz%2BWJ4zvzJVnVJgFWJLdR1f9XD%2BmPhzGTHaDKJ6lxgJKgHDEbgjg8Kz5z0My4PnKqv2z3YmYy74M6aYFKk4F4FDzgi6C52VRECEcd2xl5vwK%2F9qF%2BN9jokBRUR%2BsUNSVerStkVVPHxTtzDby1jTJAF6DDOjUBCQ1enznKl2cR2VA1q7T9Za0WgldwrC15r%2BG9i%2FQeMViyw18LOFO%2BSjdG1t2LppSNRmF3WSD9zOGgg7odhfXdMukp7vEEfkXZIfEI4Sa563XYBxLXcF4ZbwsEHG3XBbGmSLSw6vFdL329fG5McRM5vnYIJPIKDveeGrA2oPSD0zupuy2a5%2BFUcwYNguotnEqfdTKcFZknWCc0UkPMLhDG7mul8membZDPt18GMNBEBPc2tpCuXt1hm1PvYkDI358rNoLiilrtKR1%2B1MPKbadPiaQBusA78iIP5YSsHjWChO40kj6hQVSPO9DbtGhgRKKyXLi0sB2fl0zzmH5%2F2%2BqYsUz%2FB4K9Hn08XmcsBuQ9P07HHUtYzttm34lEJ1ksr6SrU%2Bx%2FIObZg1wBjRJKOU68m1Jdg3TFNd1NGbu4LUPiFJjosRamwsnGpgasu%2F9PoorekcKTtOHGMFz%2FoyqfNtr1Yzb4jsIs3FpHin%2FClgzI0ILhugJGUk4neaSERLWe7KK83PKswg%2Bqo1gY6mQH4880BtSDKTJNqgLmyUECToF746qsy%2Fvb69m9OSjUu4ShwXtDUjlkiYTjJujvmlEkO6Ze5ugF8iOlZl7en8hNNUYNi6XUt8nn6RoN7yrCI9jBgdIpdh5O6QGBssLA6Xsk8T5TeGQ11BB1SmKR1YLWCu74D2DVfD27bjmt5yO%2FSMdXhSHXJauJv5Ulj94as6yLOZxMfW%2BAc4XE%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=d6c6b677375fe4c83dfd1f45ddbcfc82afaaa5b6544abd0f1d02441482f1656d)image.jpg![](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/154523337/5c236f5e-cec8-40cb-9eaf-2d018d07ce62/image-2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYEXRX4SDPV%2F20261010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261010T125627Z&X-Amz-Expires=3291&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDoh6C2aorjAE3HIKbH94hTAhAp92GWsd1F3chVC2wgCAIgGpgL%2B0D3GrTJpmrZJby6wlNyJynsIq2t2o12MKitWWoqgAUIVRABGgw2OTk3NTMzMDk3MDUiDNLvwFxDXxI3egteoirdBNRkRRW%2BRpK11cakg31bukzAP36cYR01%2BAQyNjtN6Pq0c6NWJNSNk6PfGAD6vufz8vqKQSesDYG%2FjnVaDgLgDdAedIwixsMG2lKMtNJBp0sKQID9oxn%2BASqRvucuZYNY5RcqfQ5jdYhrTVm8DMBw8IrA6vLI%2B9kz1oupse5gU%2FwnAs964PoVdXij%2BQylsBZI%2FQIFWSUpVs0d0NxNvgX9ygzoLjPheDM9rsE7Tdg9Zm1O8hM0%2FP%2BREVqoJ%2ByAXE26Lxib7HwTW79owTY1K4fMVOVqGuqgtdLVbNRx6v3CzCNtAjG4JskAcjBrJSAMT%2FrhJv1U1HcWR8cXTZp2XIpKHsHnO1d4kbnz8smUMlygn820%2BgLwjmILiKZfk9tzv4y9Pbh9wQobmtZSdBWkgqlAHJaN9%2BSC7Zp98W9MkZtTBUN2saflyU031n6YazgN5ok2fAOCWicpXHh22n8po8Zs3yrFjDCNKg1XG4vDiqJUVTqhEaFLEoiFg8IeMNqH2a2IOzIn4%2B9%2FqFevLXngAmPR9ZY%2FGFkDiG4kmwL4Tn14QpWSay3SOVO%2FTRkIkViNfypiYNRTTHzYZPeZpZ%2FcZnDvbkZ5g7gRSE%2Bhwo7Ew1Hl6YGhDaD1QYw4%2BctZguHLoMlSwJZ3qNj4MhsrTUWG74Ox02d236Q1YChWKR4ulWYTfGrJANSzfwJYdWOa80um%2FL0WmU5xmHwQaF4KN8iRlE31WFs8%2BXUOzNCF3R78lZFNzFUQ1jsvpDJxylMbWnnh%2FR%2BGDziJOFKE6rIY8slpVQc75xy0wOc6chrq8ExvbqvDMIPqqNYGOpgBo3PiN4F%2BT1tLCaNXIBEP7ZZeGrdkbotg%2BPSDhryaFU2QUwEYkNuaVvFT99YYVJt6KivgSFZGpXYv6JvY5ZQITPj%2FLhKJ5QWxOKc7wCnev0gXJ8JFWF9IEykujjqUpu2i68rYqPAuB9ljnEXFte3ZegOe0gMpxBWYqhu%2B49%2FRqGVxyk2ohF7pUCW3WuLKPF%2BmKUK6V9curSQ%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=ad62ff1c5fbd4523b50cb0cbaec7ba9baaff99cc84f5d6ecf3c8c7039ca1201f)image-2.jpg![](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/154523337/6ea76622-67b9-4696-b1bd-51cf29641e7c/image-3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYEV5CJOLU4%2F20261010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261010T125627Z&X-Amz-Expires=3291&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIDbwhWu7yTvPA0ereNBlThDraZHWqf3CWb6o3TgkQIlEAiBTsHtBKphvf7RBOb0Lz2adDlQ5wyUn6lfnWw5x98wI9CqABQhVEAEaDDY5OTc1MzMwOTcwNSIMr7mFYIUviB8QGV1mKt0ExP0GzICZWml%2BaDtMcgvCKXgnVTktzCCQ8i%2Bat1YGXAcg02Cq%2BKH61NxQ5m76lunyspHFKkm2NkLp%2F52cYZz5%2B8ZC%2FuHH59eYRScV588M15rMKqNbrP173Z7%2B11KrGzB7tryx%2Fgwz%2BWJ4zvzJVnVJgFWJLdR1f9XD%2BmPhzGTHaDKJ6lxgJKgHDEbgjg8Kz5z0My4PnKqv2z3YmYy74M6aYFKk4F4FDzgi6C52VRECEcd2xl5vwK%2F9qF%2BN9jokBRUR%2BsUNSVerStkVVPHxTtzDby1jTJAF6DDOjUBCQ1enznKl2cR2VA1q7T9Za0WgldwrC15r%2BG9i%2FQeMViyw18LOFO%2BSjdG1t2LppSNRmF3WSD9zOGgg7odhfXdMukp7vEEfkXZIfEI4Sa563XYBxLXcF4ZbwsEHG3XBbGmSLSw6vFdL329fG5McRM5vnYIJPIKDveeGrA2oPSD0zupuy2a5%2BFUcwYNguotnEqfdTKcFZknWCc0UkPMLhDG7mul8membZDPt18GMNBEBPc2tpCuXt1hm1PvYkDI358rNoLiilrtKR1%2B1MPKbadPiaQBusA78iIP5YSsHjWChO40kj6hQVSPO9DbtGhgRKKyXLi0sB2fl0zzmH5%2F2%2BqYsUz%2FB4K9Hn08XmcsBuQ9P07HHUtYzttm34lEJ1ksr6SrU%2Bx%2FIObZg1wBjRJKOU68m1Jdg3TFNd1NGbu4LUPiFJjosRamwsnGpgasu%2F9PoorekcKTtOHGMFz%2FoyqfNtr1Yzb4jsIs3FpHin%2FClgzI0ILhugJGUk4neaSERLWe7KK83PKswg%2Bqo1gY6mQH4880BtSDKTJNqgLmyUECToF746qsy%2Fvb69m9OSjUu4ShwXtDUjlkiYTjJujvmlEkO6Ze5ugF8iOlZl7en8hNNUYNi6XUt8nn6RoN7yrCI9jBgdIpdh5O6QGBssLA6Xsk8T5TeGQ11BB1SmKR1YLWCu74D2DVfD27bjmt5yO%2FSMdXhSHXJauJv5Ulj94as6yLOZxMfW%2BAc4XE%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=d1b7b3187d6cb7e17cbb6168dc13a235da142cb2edfb813d7f43933bda42d2c4)image-3.jpg

# Perplexity
**Yes—this is the source-URL data we needed.** You successfully opened the actual `conversation` JSON response, and its `safe_urls` array contains the URLs ChatGPT associated with that web-search conversation.

What you have **does not yet show fan-out queries**, but it does give you a retrievable list of source/candidate URLs, which the bookmarklet failed to extract. The project file search found no relevant instructions beyond an unrelated portfolio link.[](https://pplxfilegitgateway-projectfiles-prod-use1.s3.us-east-1.amazonaws.com/projectfiles-prod/gateway-object-store/repos/files-05385fce2e8e8df5791c987861b27c39/lfs/objects/c5/06/c506827529361745008571cd22c6064cb5220f245c5beff60a31bcb724d34178?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ASIA2F3EMEYETTLEWQGY%2F20261010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261010T125625Z&X-Amz-Expires=900&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDVNEKFfL9ljK4jEC%2FGf7v0jC%2FGlcsnmrwsYYYSFudOGQIgRy9xlO%2BpPXHvPy%2BJISE3EVFsMSDDpEajpzB5iViWs9IqpgUIUhABGgw2OTk3NTMzMDk3MDUiDHn1fIbKlTz6R4eRcyqDBSxA6cLvuMVztxy0GOrYpG7pOOS2qPvfUFvbn9CYhG0mKUaD%2Bhk2TcgPmqSTJFApzQhc95zyuDvxfO1hwEQnSMU%2FeZMWGDzyJ4jVJGFH5xIKqYxkqR3GiMOYV7sc%2BRm%2FaUXOU6bBCM5DoAckym5jCfC1lfjL7IT0qKaM1hcc%2F8wyBliG55y9Ig%2BFluUzpjrEypqH6NXUTOXsjnnTIkDwbWxStfCzP9H4JTbXjkV7kBGtX%2B3to69obDk5ronlTz%2BTXqkenmHICGBR%2B7%2BzDFwwwFd7nee%2FbTT5hRc8Lh%2FM30lwIYR%2F2mDAWmG0X6%2FuNHdPVYEAbMsCsk9Mer9oPhgjFub8wufzfyephvX0jnoiZR0l62%2F%2FxmWSQs8eZOmMcJrMcb5tHDxf41FOWWe%2BahqUgjm4YdPDYC713OVUachugrbWQcBtSbg0C9o7e%2F90INLc1Cq7heXIPJ52tuqmfclxW2KurHNpFhZ4mc%2Fp2IX99WgXVJtWbimXR1jdBLGytc9pNAjvxmujsRL4oDKHTzRkGX6C3WtNKy281JFCXD1gqvPPnf%2BUMDs5FPiJ%2FdjlaEIu10XVvOpBPmxOF0XfELjqikjHSuyR2WdhWzCmpY2Ijgn5b%2BpYoO7rnUNUGMWXEDaVp5RtO8mI%2FBQzYuGT8np3gbtIig4V42xYjbshZYp%2BWwtI9fwGD2znyaHecVKfssevRmF7nAUZdzhqRR%2FbToiK5Vkyani2OaUAKboGhmfogpS1AjzGzPxCQM%2Bq1LCgzuHbp83R9GKy9iS7KmvWX7aCkcH3%2BqaMG8DmEDol8tm8dQnKMfCQEU%2F9SLtfP706ckQPAkIzs6l3nsAaBSM8hnH5u1Mjq44w3oio1gY6kAEFfo4HXsPe3Mp0nntWP11FTq0CSNM9m%2Fx16lZFBMPqdzBoontiWh9juljNO6%2BpQyZKHVIUvNikK4iKP6LeW7yz9Dl%2BRiddES02mLsPtnftTS4zKSkH86cA19hT5luAchBZ9P7SfIzrc06zohRqHVVZY1oalXUlnsJf4NViqYCPHx0MqHz8ZvwKce5OXxCq9N4%3D&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=d994303d8c629217fe195181f969c91f2403cf4c9ca707f7eb8bb86095890385)

## What you found

In the `conversation → Response` JSON, you can see:

json

`"safe_urls": [   "https://agency360.com/creation-site-internet/montreal/verdun/",  "https://jtrickl.../ressources/etude-de-cas...",  "https://mylittlebigweb.com/en/web-agency-laval/",  "https://localranking.ca/fr/index.html",  ... ]`

That confirms that ChatGPT’s stored conversation payload contains URLs even though the analyzer did not detect/render them.

Visible examples in your screenshot include:

|URL/domain|Likely role in the answer|
|---|---|
|`localranking.ca`|Agency site mentioned as a local-search option|
|`mylittlebigweb.com`|Agency/service pages, including Laval/Longueuil pages|
|`codemarketing.ca`|Agency site, including Verdun/GBP-related tracking URL|
|`ilumamarketing.com`|SEO service page for Verdun|
|`greni​er.qc.ca`|Local marketing/industry publication or listing|
|`purel​expertmedia.com`|SEO/local-search service page|
|`solutionsm.ca`|Marketing agency service page|
|`numérique.ca`|Local SEO/marketing page|
|Google Maps / Google Search URLs|Search/map result context, not necessarily independent editorial evidence|
|`images.openai.com`|ChatGPT-rendered image assets; ignore for competitor/source analysis|

## What to do next

## 1. Find the actual fan-out query field

While staying in that same **Response** panel, press `Ctrl + F` and test these one by one:

text

`search_model_queries`

text

`search_queries`

text

`query`

text

`search_result`

text

`search`

If Chrome reports **0/0** for all of them, then this conversation response contains URLs but no accessible internal query fan-out. That would be a definitive result for this specific chat.

## Extract the URLs cleanly

The easiest low-tech way:

1. Click inside the Response panel.
    
2. Press `Ctrl + A`.
    
3. Press `Ctrl + C`.
    
4. Paste into a text editor such as VS Code.
    
5. Search for `"safe_urls"`.
    
6. Copy the whole array between the opening `[` and its matching closing `]`.
    
7. Remove the `images.openai.com` entries.
    
8. Deduplicate domains, not just URLs, for your agency landscape list.
    

For a quick browser-console extraction, open the **Console** tab and paste this after copying the JSON response into `raw`:

js

`const data = JSON.parse(raw); const urls = data.safe_urls   .filter(url => !url.includes('images.openai.com'))  .filter(url => !url.includes('google.com/maps'))  .filter(url => !url.includes('google.com/search')); console.log([...new Set(urls)].join('\n'));`

However, DevTools may restrict pasting into Console for safety. If it displays a warning asking you to type `allow pasting`, type exactly that **only after reviewing the code above**. This code merely filters and prints the URLs—it does not send data anywhere or modify your ChatGPT account.

## The important distinction

|Data type|Do you have it?|Where it is|
|---|---|---|
|The user’s prompt|Yes|Conversation JSON / messages|
|ChatGPT answer|Yes|Conversation JSON / messages|
|Search/candidate source URLs|**Yes**|`safe_urls`|
|Clean, citation-only URL list|Partly|Requires filtering `safe_urls`|
|Hidden query fan-outs|Not confirmed|Search the JSON for query-related keys|
|Reason each URL was selected or rank position|Usually no|Not exposed in `safe_urls`|

## Why the bookmarklet missed this

The bookmarklet appears to be searching for more specific, older metadata structures—such as explicit `search_model_queries` or search-result groups. Your conversation uses a newer response format where at least the URL collection is exposed through the top-level `safe_urls` field, but the tool only surfaced model info. That is a parser compatibility gap, not a failure in your browser setup.

So yes: you have proved that the raw conversation data contains source links, and this is now a viable manual extraction path for your local SEO / AI-visibility research.

# Me

here they are:  

"metadata": {  
"search_model_queries": {  
"type": "search_model_queries",  
"queries": [  
"best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites"  
]  
},  
"resolved_model_slug": "gpt-6",  
"reasoning_titles": [  
"Searching best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites"  
],  
"reasoning_title": "Searching best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites",  
"reasoning_status": "is_reasoning",  
"tool_icons": [  
"globe"  
],  
"reasoning_start_time": 1791581317.2468743,  
"cot_version": "v5",  
"request_id": "969d9ceb-2ed7-4b80-882b-17f238f3d2f3",  
"message_type": "next",  
"turn_exchange_id": "6cec8de6-e514-4b4e-ae5e-c888ab21fe92",  
"working_turn_id": "6cec8de6-e514-4b4e-ae5e-c888ab21fe92",  
"model_slug": "gpt-6",  
"default_model_slug": "auto",  
"parent_id": "31e54066-14eb-4f4a-86dd-e8df75efc3fb",  
"can_save": false  
},

# Perplexity

**Yes—this is exactly the hidden query data you were trying to extract.** You have now found a genuine ChatGPT Search fan-out record, and it confirms the search model used a specific expanded query rather than simply submitting your original wording unchanged.

The relevant value is:

text

`best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites`

That appears in:

json

`metadata.search_model_queries.queries`

The project files did not contain related instructions or tooling; they only reference unrelated portfolio resources.

## What your JSON confirms

|Field|Your value|What it tells you|
|---|---|---|
|`search_model_queries.type`|`search_model_queries`|This is the query-fan-out metadata block|
|`queries[0]`|`best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites`|The actual web-search query ChatGPT formed|
|`tool_icons`|`globe`|Web Search was used|
|`reasoning_title`|“Searching best SEO companies…”|The internal search step matched the extracted query|
|`model_slug`|`gpt-6`|The search was performed in that model session|
|`request_id`|`969d9ceb-…`|Identifier for this particular request/turn|
|`turn_exchange_id`|`6cec8de6-…`|Identifier tying the turn activity together|
|`can_save`|`false`|Internal session/persistence setting; not material for your research data|

## The key correction

You said “query fan-out,” but this particular search step has **one** extracted query—not multiple:

json

`"queries": [   "best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites" ]`

A true multi-query fan-out would look like this:

json

`"queries": [   "best local SEO agencies Verdun",  "Verdun Google Maps ranking SEO agency",  "local SEO agency pricing Montreal",  "SEO agency case studies Montreal" ]`

So the extraction mechanism works. In this one turn, ChatGPT chose a single broad expanded query containing the location, service, local/Maps intent, and a preference for official sites.

## Why the bookmarklet showed nothing

The bookmarklet was evidently unable to traverse the newer `gpt-6` message structure to the nested path:

text

`mapping → [message node] → message → metadata → search_model_queries → queries`

It was only detecting model-level information. Yet the raw conversation response clearly contains the data it should have surfaced. This means its parser needs an update—not that ChatGPT prevents extraction in your case.

## How to find every query

In the raw response, use `Ctrl + F` for:

text

`"search_model_queries"`

Each match normally corresponds to one Search event. Expand or copy the whole object around each match, then record:

- The query string(s) in `queries`
    
- The nearby `model_slug`
    
- The corresponding `create_time`
    
- The nearby user prompt, so you know which original prompt caused that search
    
- The relevant `safe_urls` and citations, where present
    

Do **not** assume every query block is unique. Models can re-run, refine, or repeat a query across a response.

## Practical extraction template

Create a sheet with these columns:

|Original prompt|Search event|Extracted query|Model|Source URLs|Notes|
|---|---|---|---|---|---|
|“Recommend and compare…”|1|best SEO companies in Verdun Montreal Quebec local SEO Google Maps official websites|gpt-6|URLs from `safe_urls`|Broad local-agency query|
|“Give 5 more”|1|—|gpt-6|—|Add any subsequent query when found|

This lets you track exactly which queries ChatGPT generated, then compare sources and named brands across prompt variants.

## The next useful test

Use a new conversation, leave **Web search** on, and ask a query designed to require separate research angles:

> Search the web and recommend Montréal local SEO agencies for plumbers. Separately research Google Maps / Google Business Profile expertise, pricing or engagement evidence, plumbing or home-service case studies, and independent reviews. Cite every business-specific claim.

Then repeat your extraction process and search the raw response for `"search_model_queries"`. A request with clearly separate constraints is more likely to show several generated search queries rather than one broad query.

Your original objective is now demonstrably possible: the raw conversation endpoint yields both query metadata (`search_model_queries`) and a source-URL collection (`safe_urls`), even though the current bookmarklet does not parse the new structure correctly.