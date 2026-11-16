# File-AI Directories · 5 Build Your Directory

In our last step we have set up the scope of the directory and we ran into a couple of issues where we had issues setting up the data for sale MCP. So we found that we need to set it up via API and so we have updated the directory blueprint to do just that. And so we are now at the stage where we're going to build the actual directory. And so we're going to generate the site. And so every directory that we build with the blueprint has the same structure. It follows the same URL structure, page set, etc. It follows our master template which we have here. And that is master reference.

The pool builder site that we built and I have included the entire site as HTML as well now for reference. If you want to stray from that, that is fine. You can make it your own. But this is what we have found out works. So what we're going to do next is we're going to run gate 4. Let's go back to our cloud and we say run gate 4. And we'll see whether or not everything works after the update. So what we have, we have our wiki, we have our template, we have the listings that we created.

I've updated the blueprint. So let's see if it works. So it's currently going through gate 4. And that is checking the cities, how many pages in total. It's just basically setting up a plan to create this website.

Colors from the inspired site. And it ends with a numbered list of decisions to prove and to make with Claude's recommendation. And that is based on our framework. It's going to sort all the data. And then once that's done, we're going to build it with gate 5. So I'll let that run and I'll check back in when it's done.

Right, Claude has our decisions listed. We have the two cities as a demo. It says we have a bunch of thin pages, which we're going to no index. I think that's good practice. Yeah.

Decisions for us. The 11 businesses that do not build pools. Cleaners, plasterers, pool fences, dollars, a paver. Their recommendation is going to be to keep them. I don't agree.

Yeet them. Is that the right word? Three non-pool trades with no stated pool work. Yep. Drop them. Sore confirmed builders, label confirmed builders. All right.

Yes. Four. Website that didn't answer and one for sale domain. Read them again at gate 5. Blank the link on any debt. Still dead. Yep. Agreed.

Tier prices on the feature page. Yeah, I'm going to run with that. That's fine for now. And then buyer's guide on the homepage. Yes.

So how to choose a pool builder. Resource pages at launch. None. Correct. And then city copy for the two cities. Run it on Sonnet. One badge. Well under $1.

Use the content. See the content of a skill. I want those to be pretty good. Still open. Claim form endpoint. Yeah. That's up next. Gate 3 made on the way. The maps entry list accessible. All right. Let's start and build this thing. So we are now at step 2 here. Gate 5. It's going to copy the template file and fill it with our data.

And then it's going to seed and populate the site. 4 to 6 FAQs per city. Write 500 to 800 words. Let's see if it's going to go ahead and write. So we need Node.js or Mark popular for this. If you don't have it already, you probably have if you're working with AI. As there's other tools that need it. But if not, it's easy to ask Claude to walk you through it. It's just a terminal command or Claude can do it for you.

And then we're going to continue to look at it and see what we see. See whether we like it or not. It's going to create a preview site. And that is going to show us exactly what the site will look like when it's deployed. And that is going to help us decide on things like layout, design, content quality, all that stuff. And we can dial that in and rework it to our liking before we deploy the thing.

So let's see what Claude is going to do next. They're going to implement our plan and give us a situation report at the end. While Claude is chipping away, we can take a look at step 4 here.

So if there's something off with a business or with a website, we want to fix the data. Not the page itself. We want to go into the data, update the source, let's say. And then we rebuild the entire site.

And the reason we do that is we don't have a CMS or content management system. And we like it that way. I despise content management systems. People use them out of necessity, I think, if you're working with VA's and stuff. But there are solutions to that.

One thing we're looking into is called Buzz. And that is multiplayer AI. And this is a site. It's by Jack Dorsey, the founder of Twitter. It's a way, it's a Discord, let's say, or a Slack, where you can pull in your agents and you can collaborate with VA's and things. And they can use your machine, virtual machine, or your office computer that's on. And they can use your Claude subscription and things like that. It's super cool.

It's super exciting. I haven't dialed it in completely yet. But back to the question, why rebuild instead of edit? It's faster and easier to rebuild the entire site at this point with AI than it is to run and upkeep CMS. And so we just hit rebuild. It's going to rebuild the entire static site from scratch. And it's very fast. I was very surprised by that. It's taking like under a minute and then it deploys the Cloudflare. And it keeps the site light and up to date and easy to work with. I like that a lot more. It's all automatically pushed to GitHub as well than having a CMS. So that's why we rebuild it. There's just so many advantages of having a static site over the dynamic site, it might be. So let's wait for Claude here. That is the main takeaway of this entire module, basically, is waiting for Claude.

Claude to finish. And then we can, of course, also, come to the end of the meantime. All right, so Claude came back with an update for me. The listings, all processed first built. It's done actually for the different locations. And then it's going to do the bio-skite to save lots of our page.

So here is the content writer, the content engine. We're now surp analysis, content sources, et cetera. The phrase to rank for this is why it pulled from our data. I agree. So let's say yes. And then it will move forward and do all the keyword research. Yes.

The audience. Yes, it's going to be this one. All right, let's see. I'm going to use the SEO content writer skill, which is included in the blueprint. We'll let it run and then we'll evaluate the content quality. And if it's good enough, we're going to proceed and push it live.

So here's the SERP analysis. I'm going to take you through the process real quick. Per-page breakdown. Here is the request or the recommended setup for all these pages. Or this is the analysis of the SERP, sorry. Keyword targets, entity, topic checklist, format, opportunities, target. All good.

So here's the custom pool builders. The performance is going to ask for you. I'm going to give it straight away. So the content workflow gave me this outline, which I approved. I think it looks pretty good. I'm just going to let the tools run. And then I gave it a tone of voice, authoritative but approachable, factual and helpful. Article draft. There's the outline. Then I gave it permission to do the fact check and run the final export.

I just push this thing through and I'll bore you with all the details. It really walks you through it. You can go really deep. But what we wanted to do is to just get a pretty good piece of content up. And now we're going to do the Miami City copy. And I'm going to do the same thing. I'm just going to push it through and let it do its thing and say, yep, that looks good. And then we'll see what we'll end up with. We can always rework it later pretty easily. So this is like going above and beyond with the content. You don't need to use the content workflow necessarily, but it will help to rank those hot pages.

Alright, so gate 5 has been completed. Waiting for approval. Let's review it real quick together. Look at the master template unchanged. That's good for now. We built 152 pages simply because this is a demo and I'll include the full site in the course. We have the buyer's guide. 2000 words. And then a part of it is on the homepage. And then we have the city pages with the content writer as well. Audit. Every page has a H1 heading and title. Schema. No internal links are broken. Publish a bio empty claim font. Endpoint. Stellar templates placeholder. We'll use Form 3 for that in a later step.

And the domain already serves the earlier demo. That is correct. I already built out the site to test everything. We don't have any striped links yet for the payments for the featured listings. You can do that. Just give it to Claude. It will integrate. For this build out, we're not going to do it. It's fine to have a listing request and then we do it manually.

I think Blair said that he doesn't have a lot of requests or featured listings. And that's only going to play or be important when the volume is getting pretty high. We never want to solve problems that are not existing yet.

Alright. To look at the build yourself later, double click preview site command in the site folder. Alright, let's do that right now. And then prepare the launch files. Yeah. We're going to review real quick.

And we need to go to, I think it's set output. And then, let's see. Output. Oh, in the site folder. Preview site in the site folder. So right there. Preview site. Command.

And that is the case for Mac OS. And then the BAT file, I believe, right there, is for Windows, I think. Alrighty. So there it is. This is what it's built out. This is the raw output. I built this with you live. It's pretty exciting, isn't it? So we have all these listings here. As you saw, we didn't do anything at all. Pull this stuff itself. Let's take a look at one. We have the reviews here. Get directions. Does it work?

It does. There it is. Isn't that beautiful? Alright, so they built new pools. We have the website here, if it works. Oh, it was denied. Alright, that is probably because I'm in the European Union. That's too bad.

We have socials here already. It automatically pulled those in. Facebook. I'm just clicking to see what I see. I like to do that. Just spot checking. Does everything work? I'm not going to check everything.

What reviews mentioned. Alright, let's take a look at the homepage. So we have the homepage here. I like that it lists the amounts here. We have the canonical here. Index follow. Heading structure. This is a, I love the heading structure. I really tweak the heading structure. I am a big fan of getting the heading structure just right.

Fine, pool builders by city. How listings are better. How to choose a pool builder in Florida. That's this one. So this is the excerpt of the entire article.

This sounds like a lot of homework for the customer. So I would probably try and rewrite this article. It's well written, but I would try and rewrite it in a way that it doesn't feel like we're giving the reader all his homework.

So we have the frequently asked questions. Let's take a look at the schema.

Publisher here. It's a webpage. Here are the Q&A schemas for the frequently asked questions.

Every city in Florida. So here is the city or the state content.

I would say that we want to have subheadings here as well, maybe.

I don't like this necessarily with every city page ranks the business in it by rating and review count with feature placements marked.

So what I just do then is I give this to call and it will see that breadcrumb here.

And I'll just say that I don't like the wording.

That sounds like internal talk. So omit. Then anything else we need to do.

I do like the idea of subheadings there, but maybe not for now.

Then we have all cities here. I don't really like the layout here.

I'm just going to go with the flow here and show you what I would do to get this thing ready to go.

All cities.

And I'll just go over it quick and dirty. I would remove the email here, at least encrypted, so that we don't get spammed to death.

If you put a raw email like that on site, you can be sure to get spammed to death in the footer and maybe on other places on the website.

It shows a raw email we want to encrypt it so that we don't get spammed.

Anything else we like? Clean your listing. Here's the form.

Get featured. Featured page. That looks good.

Pool builders. Here's the entire directory.

This is typically a no-index follow page.

That means it will not be indexed as it competes with the homepage and we might rent the homepage and it has the same basic functionality.

But we do want it to be follow.

That means that Google Scrawlers will use this page to follow all the links and that is a nice index.

It will strengthen the link profile of the site.

So there we go. My nice smug phase there. I like that.

Our listings are added. That is good.

Then let's look at the cities.

Pool village in Florida, far southeast.

Rarely keep their work inside one city, multiple pools.

So I've instructed the blueprint to do all this internal linking to the listings.

It calls out. I think that's good. The more internal links, the better, I think.

Concretism. So this is... It reads a little bit like internal speak, like an analysis of the listings here.

And just to be comprehensive, I don't know how much time you have.

I've all designed in the world. Let's... Let's just address it.

I think the city page's main copy sounds like a technical description of the listings featured.

More internal speak. Rather than helping the consumer.

Also, not great for SEO. Please rewrite and rephrase in a way that addresses the search event. That's what I would say.

So as you can see, I'm just dropping in screenshots and giving my thoughts.

Yeah, this looks good. This description here, it looks nice. What reviewers mentioned, I like that a lot.

People can claim this listing. It will fill in the business name automatically.

What else? I want to take a look at the heading structure here as well.

So something I did is to make sure that the About Mellebouple scandal is shown at the top here, but it is lower on the page. That is just a little CSS trick that we do to optimize for SEO as well as UX.

And then what I like a lot about the blueprint is all of the schema is done automatically and very good.

So we have same as, makes offer, and then all of the services are cited here in the offers, which is, I think, very good.

And I think, and this is an instruction I gave, that we get all the businesses as list items as well in the schema.

What I am seeing here, the aggregate rating stuff. I don't know if that is correct. I'm not seeing the rating.

And the address schema looks off a little bit too.

Please review, attached, schema, printout.

It seems the aggregate rating is not actually, how do you call that, printed as a value.

Also check the address property is used correctly.

Alright, who else?

Check some fill here.

Let's scroll down all the way.

So here's about the licensing.

Common questions, this should be in the schema as well.

I have to go down because all the listings are in the, yeah, there we are, FAQ schema, good.

Poolbuilders near Jacksonville.

So I'm really liking this so far.

I think this looks pretty good.

I'm going to drop the feedback into Claude and see what it does.

And then I'll be pleased and push the theme to index, which is our next step.

So I'll check back in with you one more time once it's processed all my feedback to see what it does.

Alright, so it's processed all of our feedback.

I'm very, always very excited to then take a look.

It's a little bit like Christmas morning when Claude is done.

So let's take a look real quick.

The feature placements marked.

It's gone.

Alright, that's good.

To disclosure sentences elsewhere, it still says paid positions are marked wherever they appear.

Yeah, fine, that's okay.

City links, it's now a full width button.

Take a look.

Every city.

That looks way nicer.

Thank you, Claude.

Email, no email address in the build.

HTML is plain text.

Let's take a look how it works.

The address is reversed and encoded.

A small script puts it back as a working mail tool link for a visitor.

That's exactly what we want.

I'm curious to see...

Well, it does seem like it's still there, though.

I'm curious to see how this works in the age of AI agents, where you can just click the thing.

It still seems to print the raw email.

Schema.

Organization and person.

Schema.

Also printed the address, right?

Good.

Oh, I see.

The business emails are of less concern, as they are already publicly available.

It addressed the listing emails as well.

It's less interesting to us.

Alright.

City copy vote blocks are rewritten for someone searching for a pool builder.

So what to decide first?

Which pool types are built?

Who works in which part of the area?

What the permit involves?

The deck and yard.

Financing and track record.

That is excellent.

How much does a pool cost?

I think you would include a digital figure.

I just like answering how much does it cost and then saying it depends.

I'm going to leave it for now, but I would typically maybe rework that or just omit it.

Just it's a pet peeve of mine.

I don't like that.

So let's take a look at one of the city pages real quick.

So it should address the search intent a little bit better.

We have pool builders in Jacksonville cover a lot of ground.

First and so is where the company works.

That's a little bit stating the obvious, but okay.

That would probably rework this a little bit more if I'm really honing it in.

Jacksonville builders routinely cross county lines.

Yep, that's pretty decent.

And pick a pool type because here you have a real choice.

Scott Pools and Sparse builds only concrete and shotcrete pools.

That way you shoot the concrete up the walls in any shape or size.

Fiberglass.

All right, excellent.

Let's do Miami.

All right, so this is unique content.

That's pretty good.

I'm going to run with it for now.

I'm not too worried about it.

This is a nice overview of 23 more pools.

This is the lowest rated.

All right, so I'm very, very pleased with that.

The raw email sale seems to show.

Let's change that.

All right, excellent.

So I'll push this to Claude for review.

And then once that feedback is done, we are pretty much ready to go.

I like that we have made the attributes that we added during the enrichment process searchable as well.

So I say fiberglass pools near Miami.

And these are the two companies that do that.

That's pretty cool.

It's pretty slick what we can build nowadays, so easily and cheaply.

So basically, we'll be having the site outputted in a second once this is done.

If you have microsites, they should look like other listings.

So that's something to check as well.

And now we are basically ready to roll and put this live.

So if you've built your first directory, open a couple of pages, make some screenshots, share it with us in the community if you like,

so that we can review it, see what we like, what we dislike.

Maybe we can even audit it if you post a link once it's online.

Next up, we're going to put it online and take a look at where we're at.

Next up, we're going to put it online and take a look at where we're at.