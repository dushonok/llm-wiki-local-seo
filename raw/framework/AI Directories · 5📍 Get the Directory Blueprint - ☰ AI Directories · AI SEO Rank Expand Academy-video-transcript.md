# File-AI Directories - 5 📍 Get the Directory Blueprint

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

There it is.

That's all we need to do.

What we can do for Data4SEO, if it doesn't find this CSV file, it's going to run Data4SEO and pull the listings.

And we open the blueprint folder in cloud code.

And we open the blueprint folder in cloud code.

Open your terminal, go to the folder in cloud, or what I like to do, which is easier, and I need to edit this real quick.

I see I made a mistake here. Sorry. That's it.

This is the prompt, and what I'm going to do is I'm going to create a new session here, and I'm going to give it access to the, let's see, academy demo.

This is the directory blueprint number three. This is the directory blueprint number three. That's the folder I'm giving it access to, trust workspace. So now it has access to the wiki element. It will use that folder to work out of. And I'll just give it the prompt, and then we'll see what it does. It's going to read everything it needs to know for the first couple of steps. And then it's going to say scope. It's going to ask us eight questions. What's the service, the domain name, all this stuff. All right. Which service is it for? Pool builders. I'm going to go off script here and give it the location, see if it can adapt. So it's now pulling the list of maps categories. And that is the one. All right. I could not look up the calendar.

The Data4SEO script found no login in CloudCode. That is what we do want to use, CloudCode, and I'm quite sure that I've set that up. So why is it not? I'm going to remove this Outscraper listing real quick because I want to use Data4SEO rather than Outscraper. I have a domain. Yes. FloridaCustomPoolBuilders.com. All right. Type the brand name exactly as the site should show it. Florida. That's it. I like that it asks me. Do you already have microsites or a business of your own in this niche and state? That is interesting to hand to it. Basically, I would list all of the domains that we have in this cluster or this industry.

and this location and then it will sprinkle those into the directory. Currently, the publisher name is going to be RankExpandAcademy, or just use Sean Buckles in this case.

You can do a persona. That's good. If you have a marketing agency, it's perfectly fine to use your marketing agency, your SEO agency, as the publisher here.

Basically, it is a normal business activity to have directories build these things out. With a microsite, we're a little bit more careful because some people are going to build 100 or 200 or 1,000 even.

All right. Publisher details. The person schema links to publishers' other profiles.

We have rbucklespublishing.com. Publisher. Bio follows. I'm not interested. A photo. You can do a photo of your own, like a headshot. Should we do? Let's do it real quick.

This is going to be interesting. There we go. I look rather tired there, but that's okay.

And then the contact email. It's going to be sean at rankexpand.com. There we go.

Of your own, like a headshot. Should we do? Let's do it real quick. This is going to be interesting.

There we go. I look rather tired there, but that's okay.

And then the contact email. It's going to be sean at rankexpand.com. There we go.

I don't know if it's going to pick up this photo here, but it's interesting to try it.

All right. Record it. I saved the photo. You paste it. Excellent.

None and none just for now.

All right. So basically, we are now starting to follow the blueprint.

So we can follow these steps here. They're going to be the same as in the blueprint.

Inspire sites. Are there any sites that we like?

For now, it's going to take design hints from those sites.

If you feed it a directory that you like, like visually or the way it's set up, you can give that as an example reference here.

It will take it into account.

Here are seven reference directories to choose from.

Just use the default. That's good.

Up next, what we're going to do, we have the scope down now.

And then it's going to pull the data and clean the data for us.

So, yeah, the Data4SEO is not connected.

One, we have to be set up key connectors.

These are nice.

The scope is down.

It's going to look for the way to pull the listings now.

And then once it has that way, it's going to pull the listings and enrich them for us.

I'm very curious if it can solve this.

Yeah, so now Claude basically gives us these steps to follow.

So I'm going to do just that.

The connector does not work here.

I thought it would, but that's too bad.

Because it's using OAuth and we need API access.

But it's easy to set up API access.

So let's do that next.

I'm going to open our Data4SEO dashboard and go to API access.

All right, I can do that.

Data4SEO.

Log in.

Sign in.

And then we need API access.

So there we are.

API access.

And then here are the API credentials right here.

And what we want to do is send by email.

And that's going to give us, I think, let's see.

Yeah, API login.

The API password is not your account password.

So this is the API password.

I'm going to copy that real quick here.

And then I'm going to use the command here.

Let me pull that into here real quick.

And I'm going to copy the values.

So it's going to be.

And I'm going to copy this off screen real quick.

So you need to send it by email if you don't have it visible here.

And it will give you the API key.

And then I cannot show you the full command because I have the password in there.

But I'm going to mock it real quick.

Basically, what I do is I would copy this.

I open Terminal or Shell.

And I paste this and I run it.

It's not going to work because the test password is not working.

And also, I had this issue the other day as well.

So let's take this and give it to Claude.

For the debug.

And so this is a little bit fiddly.

But I promise you, once it's set up, it's going to be a pretty amazing setup to turn these things up.

Yeah, there we go.

The fix is that I need this little path in front of the command.

And that was indeed.

Or I can do this.

Yeah, let's do that.

So then it works in every new terminal.

So I'm just going to set this path here to always work when I say Claude.

Done.

So now it should work.

Let's see.

All right.

So what I did is I copied the command, but then the real one, of course, here.

And now the Claude command did work.

And it gave access and modified a file for me so that I now should have access.

All right.

We should be good.

Let's see if it works.

All right.

So it doesn't work yet.

Well, we learned together, right?

Connection will save.

Dataverse will reject the login.

It's correct.

The login and password pair itself is what Dataverse will refuse.

Account password instead of API.

Ah, I made the mistake myself.

Let's fix it.

I use my account password instead of the API password.

Probably.

So I've got to remove the save command.

All right.

Done.

Now we're going to add it again.

We're going to use the right values.

Let's do that.

All right.

So I've reran it.

Wrong password.

Indeed.

Should now be fixed.

I'm getting impatient and I try to go too quickly and then you get this stuff.

All right.

Let's see if it works.

The login works now.

Category lookup.

Both ran.

Nothing has been pulled.

So we have the category here.

State.

2,000 businesses.

Three requests.

It's going to be about less than a dollar.

Excellent.

Yes.

So let's move forward and let's try and build this thing.

So once it has pulled all of the data, it's going to clean the data for us.

So we have the data pulled.

It was about the same as the cost indication.

And we have all of the data here.

Publish a bio contact phone.

Yeah.

I've already built this thing out yesterday.

So I've already built out this site as a demo before.

Please ignore and continue building it as usual for now.

Approve.

So it's going to run gate 2.

It's going to clean the data and it's going to insert attributes to the data.

So basically it's going to tag all of the data points, all of the listings, check candidate name terms against the business names in the raw file, cleaning script.

That can take a while.

It's going to clean any listings that it deems not to be a good fit.

Checked thin and still counts.

Review counts, for example.

And this is like the magic step.

So we now have 1,823 listings left.

So it dropped all of the listings that haven't been updated in 12 months.

So that's an indication that these businesses are no longer active.

Zero reviews dropped.

Name or category match or mismatch dropped.

Duplicates on phone and addresses.

So basically duplicate Google business profiles.

So we have about 90% left.

We have 283 cities in total.

153 have three or more listings.

So that's 1,650 listings left.

402 listings have less than five reviews.

So websites, 1,448 listings have a website.

1,322 have distinct domain names.

So now we're cleaned.

So if we now approve it, we close gate 2, which is a cleaning gate.

And then we go to gate 3, which is enrichment, which is important.

It will write the attribute list for the vertical.

8 to 15 things a page can say about a business.

Inground, fiberglass, gunite, spa, remodel.

So basically, what is this contractor up to?

It's going to read the website of the contractors and check whether it's true or not.

If we have a very broad maps category, it's going to record in one attribute whether the business does the core work at all.

So does this thing build pools, this contractor?

And then it's going to read each business's own website.

The maps pool has almost no text to work from.

The description is empty on nearly every row.

So the website is where the facts come from.

This part is free.

Takes a few minutes per state.

And then the enrichment step itself.

Claude answers every attribute with true or false or not enough info.

And that's going to result in...

I'll show you real quick.

That's going to result in, for example, these.

Yes, true or false.

And then it says, inground pools, we don't have enough info.

Let's see.

It writes a plain description per business, up to 200 words.

It never guesses, so it needs to fact check and verify this stuff.

Then Claude tells you how many listings it is, how much of your Claude plan it will use,

about 4,000 tokens a listing.

So you can run one small batch to read, to see if you like it.

And then it goes city by city if you approve it.

And then after that, you have a folder under output with a clean list, the attribute list,

the enrich list, and a report for each step.

And then we have basically all we need to build the directory.

So I already did this step.

It's going to cost like 70 bucks or something.

It's going to take like 15 minutes, half an hour or two.

It's going to deploy a bunch of agents to read all these websites, do two cities for demo purposes.

I already have the listings done in the demo version previously.

So just to show you what that looks like, it's going to deploy the agents.

And then basically, once that's done, we close out this gate, gate 3.

And then we have a folder under output with a clean list.

And we can build the entire directory.

It's going to build the design, the templating.

So we encountered the no-day-for-seo login.

And the way I solved that is just give Claude the screenshot of the issue.

And it will help you set it up.

The clean report drops almost anything or everything.

Maybe this could be an issue.

Then the category is a mismatch.

Half the websites could not read and not be read by AI.

Yeah, it's normal that it locks out a bunch of websites.

But we want to see like two-thirds.

And then if that's the case, the vertical is one where businesses do not keep websites.

So you'll get a thin directory.

So run these three gates.

And it will give you the output.

Let's see if I can pull that up in the one we already built.

Here's the output.

And there it has listings cleaned.

This is the CSV with all the cleaned listings.

And this is all the stuff it pulled from maps.

Pretty nice.

Nice list.

Working hours, all of this stuff.

Operational.

Location link, which we need for directions.

And then here's the listings enriched, which will give us the descriptions as well from

the website, all that stuff.

Let's see.

Where is it?

Slugs.

That we're going to use.

City slug.

Owned.

Thin or not.

New pool construction.

Inground.

All the attributes that Claude decided we need for the directory.

Here's all the descriptions.

Based on their website and the Google business profile.

All the socials are in here.

So it really does a lot for the 70 bucks.

And so here it is reading the actual websites.

It did five batches.

It costs six bucks.

It's now running the smallest batch as a pilot.

And it basically deploys agents.

And you can run this parallelly.

It's going to read the website in batches.

Like all the agents have a batch of websites, which feeds it up.

Pass on the first try.

I got to run in a second.

And so that is where the enriched data list comes from.

So all of this is very methodical.

And then once that's done, we can actually start and build ArtRack3 in the next step,

which we're going to do in a minute.

Thank you.