# File-AI Directories · 4 Pull Your Listings

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

Thank you.

So, we're going to...

And I'll show you.

Thank you.

Thank you.

I can use the...

It's right there.

going to pull 120,000 rows instead of, let's say, 30,000. I want to set the location next. So the

location here, all of the United States. In our case, we want to do Florida. That's it. And then

the next thing we need to do is leave everything on default, but we want to make sure we don't need

emails. We can pull emails if we want. DataFrash will scrape the emails that are known to it, and

that's going to give you like 50% coverage. So 50% of the listings will have an email address then

with it. When I first set this up, like some of these packs for basically enrichment were auto

selected, and that's going to double or triple your cost. So make sure to check that they're not

selected. And then you can set that limit here. If you want to stay within the free limit, set it to

500 or do all available. And then you say get data. It's going to give you a demo of the data. It's

going to pull. Basically, it's going to say, yeah, this is going to cost you about this much. There are

like 1,500 queries, 15 minutes maybe, and 15 bucks to scrape, which is pretty good. However, DataFrash

returned the same amount of listings, and we actually pulled both and compared them side by side with

AI. Basically the same list, but that's going to cost you like $1.50 or something, or $1 or something.

So then we say confirm. It's going to start to run. Maybe it's going to prompt me because I don't have

enough credit. All right. Send to the task page, and now I can see the progress here. And as you can see,

I already scraped this yesterday, like the day before yesterday, and eventually it turned out to be like

$24. And then I can download the list here as an Excel file or a CSV, which is what I want. And we can go to

our next step where we load this into our blueprint. So we rename it to listings-raw.csv. That's the file

that the blueprint is looking for. And then we drop that into the input folder, which I'll show you in the next

step. That's basically it. And then, yeah, what it costs, yeah, under $1 for DataFrashio. And then

Outscraper, it was $24. So that's the big spread that Outscraper is taking here. Well, you do run

cloud code with some models, so that's going to cost you tokens as well. So there's a little bit more

cost involved, but typically DataFrashio is going to be the cheapest way to do it. So let's go over

some common issues. If the count is tiny, the category can be wrong. The location is, for example,

a city, not a state, and there's just too little data. So check that you don't have a city selected,

for example, here with this setup. You can accidentally say Florida, New York, instead of the state

abbreviation here, and that's going to return way fewer listings, and they're also the incorrect ones.

The count looks huge. You pick a broad category. That's a contractor instead of something specific,

so make sure to double check your category. Rows from neighboring states. That is normal. And then

we will clean up this file. The blueprint will do that for you and then bridge it. A business you

know is missing. Yeah, one in 20 is, so it's not perfect. We can add it by hand, or we can have

the owner claim a listing or create a listing on the directory once it's done. Cloud can't find your

category in DataFrashio. It checks the list for free, and if your service is not on it, it's not a

maps category. So then you can do a plain query, like the free text matching, but I cannot guarantee

how much that will cost. I think it's going to be way, way more expensive also with DataFrashio, but you can

run a small batch and then project how much it's going to cost you and make your own decisions.

All right, so for now, if you use DataFrashio, check your connection in Cloud Code, the way I showed you

with the connector here under your account. Let's see. Settings, connectors. Do you have the DataFrashio

MCP connected? If so, nothing else to do. You're good to go. And then if you do outscraper, run the

pool for your category on state and download the CSV, and then we're done for this step. We can download

the directory in the next step, which is very exciting. Load all of this stuff up and start building our

directory.