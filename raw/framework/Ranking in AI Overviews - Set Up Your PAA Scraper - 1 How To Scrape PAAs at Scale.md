# File-1 - Ranking in AI Overviews - Set Up Your PAA Scraper - 1 How To Scrape PAAs at Scale

So in this module, I'm going to show you how to set up your own. People also ask scraper. This is an internal template we use. This is a API workflow. You can do this in N8N if you like, but sometimes simpler is better. So this is a Google sheet to keep things simple. Each, this tool will scrape the people also ask for the target keywords. It will go three levels deep. Each keyword will take on average three minutes. It's going to pull like 85 questions. And then we recommend maximum of five keywords per scrape. Otherwise, this thing will run for ages and you'll start wondering whether it's running at all. And it gets messy very quickly if you press this button too often. Ask me how I know. So how to use it? We input the main keyword right here. And then we input language and language code and we just press this button.

And then we can paste the output into the Google block template. This is our internal SOP. And then we can deliver to the client. It runs off an apps script here, which I'll show you in a second how to set this up. First off, you want to set up this template with at least this button here, the target keyword, language and country, and then this output, these columns here. And I've already pressed it. So you'll see it has run here. And the formatting can be off a little bit because it's populating these rows here. But what will happen is we say succulent plans, English, United States. And if we pull the SERP for this, you'll see all of these. It will pull.

And then when I open one, that is level two, considered level two. So opening all of these, the first five, I believe, then all of these questions are level two. And then when I open all of these, more will open. That is level three. And so you see how these things gets pretty heavy pretty quickly. This is why it's 85 questions.

So we press the button here and then it outputs as follows. It gives a timestamp based query. Question as a query. No, question used as query. And then the people also ask phrasing the answer if it can pull it. And I think this is having trouble with the non-parameter as well. This is using data for SEO. Here we have the source title. I want to say this is the title. So I think something's not completely.

Right here because this is the source link as you can see. And the level is switched. So sometimes these APIs switch things up. And then you get exactly this type of stuff.

Source link. And I'll make sure you have access to this template so you can just copy paste it for your use. You'll have to update the Apps Script though. So there we go. It has pulled all of the questions here. This tells you the question, the parent question.

And it pulls all the answers if they are available. And then what you could do is simply copy all of these and then run those through the next workflow which is going to be generating the semantic snippets for your website.

And you can insert those on your pages. But first I'll show you how to set up this template using the Apps Script next.



Spreadsheet: [https://docs.google.com/spreadsheets/d/18RGdsQnyg9fBpfEigOxgjSBCYCJM1COMVXe4ViNRN4Q/edit?gid=1835889859#gid=1835889859](https://docs.google.com/spreadsheets/d/18RGdsQnyg9fBpfEigOxgjSBCYCJM1COMVXe4ViNRN4Q/edit?gid=1835889859#gid=1835889859)