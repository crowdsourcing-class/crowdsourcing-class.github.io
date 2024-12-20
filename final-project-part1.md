---
layout: default
img: brainstorm
caption: Brain designed by <a href="http://www.thenounproject.com/marcusmichaels">Marcus Michaels</a> from the <a href="http://www.thenounproject.com">Noun Project</a>
title: Final Project Part 1 "Brainstorm 3 Ideas"
active_tab: homework
release_date: 2021-03-19
due_date: 2021-03-25T23:59:00EDT
submission_link: https://www.gradescope.com/courses/233619
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->


<div class="alert alert-info">
This assignment is before {{ page.due_date | date: "%I:%M%p" }} due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

Final Project<span class="text-muted"> : Part 1</span> 
=============================================================

This assignment counts as a deliverable toward your final project.   The goal of this assignment is to generate several ideas that you could refine into your final project.

### Step 1: Form a team

Your final project must be done in a group.  The size of the group can be 4-6 people.  Find some awesome people.  Do you remember what James Surowiecki says about groups?  They're best if they are composed of a diverse set of people.  So maybe you should try to pick out people who aren't already your friends.  Use the [Piazza message board](https://piazza.com/class/kgjibsv4k6zqi?cid=5) to advertise that you're looking for teammates. 

### Step 2: Brainstorm ideas for your project

Your group should meet up and brainstorm ideas for the project.  You can come up with ideas on your own, or use [some of my ideas](#ideas) as a starting point.  Your ideas are probably better than mine.

Here are some different kinds of projects that you could do:

* Come up with a human computation algorithm that solves some cool problem
* Conduct a social science experiment with the crowd or analyze data from social media
* Create tools that improve crowdsourcing platforms for requesters or for workers
* Develop a business idea that uses the crowd like in the companies that we've been profiling


### Step 3: Flesh out 3 ideas

As a group, pick the 3 ideas that you like the most and start fleshing them out.   
Here are some considerations that you should take into account when selecting your shortlist of ideas.  The final version of your project should:

* Solve a real world problem
* Actually use crowdsourcing (it doesn’t have to be via Mechanical Turk, but that is a good default way to incorporate crowdsourcing)
* Include a significant machine learning or human-computer interaction component, or another component that you can analyze quantitatively
* Explain the choice of incentives and discuss alternative ways of incentivizing workers
* Contain a quality control component
* Analyze costs and decide whether your idea is a viable business

Your initial ideas don't have to do all of these things yet, but they should be ideas that you can extend in that way.

### Step 4: Answer questions about the 3 ideas

<div class="panel panel-primary" id="questions">
<div class="panel-heading" markdown="1">
#### Report
</div>
<div class="panel-body" markdown="1">

Below are the questions that you will be asked to answer about this assignment. Please turn in your answers in a PDF for [Final Project: Part 1 on Gradescope]({{page.submission_link}}). 

**Note:** you should answer all questions separately for each of the 3 ideas.

1. What is the name of your project (points for creativity!)
2. Give a one sentence description of your project. (Please use the name of the project in your description.)
3. What problem does it solve? 
4. What similar projects exist? 
5. What type of project is it? 
  * Human computation algorithm
  * Social science experiment with the crowd
  * A tool for crowdsourcing
  * A business idea that uses crowdsourcing
  * Other
6. Who will be the members of your crowd? 
7. How will you incentivize them to participate? 
8. What will they provide, and what sort of skills do they need? 
9. How will you ensure the quality of the crowd provides? 
10. How will you aggregate the results from the crowd? 
11. Describe each of the steps involved in your process. What parts will be done by the crowd, and what parts will be done automatically. 
12. How will you evaluate if your project is successful? 
13. What potential problems do you foresee when implementing your project? 

</div>
</div>


<div class="panel panel-danger" id="rubric">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 7 points of your final project grade.  

* 1 point for successfully forming a team with 4-6 members
* 2 points for each of your 3 project ideas

</div>
</div>


<div class="panel panel-info" id="ideas">
<div class="panel-heading" markdown="1">
#### Project Ideas
</div>
<div class="panel-body" markdown="1">

Here are a few final project ideas. You are welcome to adapt one of these ideas into your final project, or to come up with your own idea. 
My expectation is that your final project will represent a substantial amount of work, and that it will be something that you're proud of and that you would like to show off to potential employers or to graduate schools.
 
### Text Adventure Games (suggested by CCB and Daphne Ippolito)

Long before video games had the amazing graphics they have now, there existed text adventure games like [Zork](http://zorkonline.net) or [The Hitchhiker's Guide to the Galaxy](http://textadventures.co.uk/games/view/3cbedqimquselmanehhzxg/the-hitchhikers-guide-to-the-galaxy). Text adventure games were also known as [Interactive Fiction](https://en.wikipedia.org/wiki/Interactive_fiction). There was a recent paper from Facebook Research that used MTurk to create data to help [Learning to Speak and Act in a Fantasy Text Adventure Game](https://arxiv.org/pdf/1903.03094.pdf).  The Facebook project is probably a better example of a [Multi-User Dungeon (MUD)](https://en.wikipedia.org/wiki/MUD) than interactive finction.   Your project could create data in a similar fashion to the Facebook paper, with some augmentations suggested by CCB and his PhD student Daphne.




### Roll Call

Design a crowdsourced app that can collect the contact information for all legislators in a state and poll their offices to see where each of them stand on a piece of upcoming legislation.  For instance, you could use the app to poll all members of the [PA house](https://en.wikipedia.org/wiki/Pennsylvania_House_of_Representatives) and the [PA senate](https://en.wikipedia.org/wiki/Pennsylvania_State_Senate) about whether or not they would support the [National Popular Vote Interstate Compact](https://en.wikipedia.org/wiki/National_Popular_Vote_Interstate_Compact). 

### Crowdsourced Matchmaking

Come up with a human computation algorithm that helps people find a better match in online dating.  Some people have tried to use [machine learning](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) or [crowdsourcing](http://www.youlookgoodtogether.com) to optimize their dating experience on OKCupid.  Can you come up with a better way of matching people up via crowdsourcing?  Maybe you can have the crowd act as Cyrano de Bergerac, feeding users better lines than they could think of themselves.  Maybe you could have people in a social network nominate people who they think would be good matches.

### Translate Children's Books

[The International Children's Digital Library](http://en.childrenslibrary.org) is a collection of children's books from around the the world.  Volunteer translators have translated a subset of their books into different languages.  We could try to translate many more of the books using crowdsourcing.  There could be different tasks for monolingual speakers and bilingual speakers.  Monolinguals could transcribe the text of the books (which is usually embedded in images).  Bilinguals could translate it.  Monolinguals could edit the translations.  


### Crowdsourcing and Creativity
 
Create a human computation algorithm to convert prose into poetry. Your algorithm should model two aspects of poetry rhyme and meter. NLP researchers have been working on text-to-text generation algorithms that can rewrite sentences in many different ways. This software can generate a huge number of alternatives, some of which may fit the constraints of a poem. However, the software is currently poor at determining which of the generated sentences are grammatical versus ungrammatical, and which correctly retain the its original meaning. Your job will be to incorporate humans into the process to make those decisions. Meet with your professor to learn more about the NLP software (it takes quite a lot of effort to learn), and then design a set of MTurk HITs to filter generated sentences down to ones that are poetic, grammatical and mean the same thing as the original prose.
 
  
### Fairness in rejection

Design an adjudication system for work rejected by Mechanical Turk Requesters.  The system should allow Workers to appeal rejections, and should have a mechanism for deciding whether the rejection was fair (in which case it would stand), or unfair (in which case it should be overturned, and the Worker should be paid).  Possible ideas: design a second pass HIT that has other Turkers review the work, and decide whether it is acceptable or not.  As part of this project you should specify what constraints are on the original HIT design to allow easy second pass reviewing and highlighting / explanation of why an assignment was rejected.  You should also quantify the expected increase in costs to Requesters, based on variables like: rejection rate, original reward amount, reviewing cost estimate. 


### Design a system for confederated qualifications
 
Design an implement a method for Mechanical Turk Requesters to share qualification tests and the results of who passed the tests. Write a short paper describing the value of such a system, and comparing it to MTurk's master's qualification. Design a few qualifications of your own that you think would be broadly useful, possibly by reviewing the tasks currently posted on MTurk and generalizing the skill sets that are needed. 




### Cognitive science experiments 
 
Choose some aspect of the cognitive science that can be tested through experiments on human subjects. One of my favorite examples of this is Lera Boroditsky's work testing various aspects of the Sapir–Whorf hypothesis that language influences they way that we think. Read Lera's article on how she used MTurk to test whether [metaphors change the way people reason](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0052961). Choose your own topic (or reimplement several classic experiments). Write a paper discussing your results, discussing whether MTurk provides a representative sample of subjects, and describing how to go about applying for Institutional Review Board approval for cognitive science experiments on MTurk.
 
 
### Behavioral Economics
 
Write a suite of HITs on Mechanical Turk to test behavioral economic theories by implementing a set of games like the "ultimatum game". In this game two people are paired up. (They can communicate with each other, but otherwise they’re anonymous to each other.) They’re given $10 to divide between them, according to this rule: One person (the proposer) decides, on his own, what the split should be (fifty-fifty, seventy-thirty, or whatever). He then makes a take-it-or-leave-it offer to the other person (the responder). The responder can either accept the offer, in which case both players pocket their respective shares of the cash, or reject it, in which case both players walk away empty-handed. See more details in "The Wisdom of Crowds". Note that this requires pairing two people simultaneously or simulating their interactions. 
 
### Track the spread of the flu using social media 

Did you know that you can catch the flu from social media?  Well, you can't.  But you can use it as a tool to track the spread of certain diseases.  You could try re-creating one of the publications by [this cool researcher](http://www.cs.jhu.edu/~mdredze/publications.php).  What sorts of health problems do you think social media can give us information about?  
 
### Wikitopics
 
Wikipedia provides hour-by-hour page view statistics for every one of its pages. Write a human computation algorithm that uses these statistics as input to detect trending topics in the news. Use humans to (1) review the trending pages to say whether they describe something newsworthy, (2) cluster them into pages about the same event, and (3) write short summaries of the event that triggered them to become popular. Design good mechanisms for quality control for clustering, and for describing something as newsworthy. Read this paper about [a baseline computational algorithm.](http://www.cis.upenn.edu/~ccb/publications/wikitopics-what-is-popular-on-wikipedia-and-why.pdf)
 
### MTurk Prediction Market
 
Prediction markets use collective intelligence to try to predict the outcome of future events. Prediction markets answer questions that have definite, verifiable answers on a particular date (like "Will the government shutdown still be in effect on October 31, 2013?"). They let people buy and sell shares in the outcomes, and track the value of each outcome's shares over time. You should implement a prediction market that sets that value of the shares. You should hire workers on Mechanical Turk to make the predictions. The major design challenge will be to formulate the system so that it incentivizes Turkers to make well-considered predictions instead of random predictions. For instance, you may consider designing a HIT that pays nothing initially, but that gives people up to $10 if all of their predictions are accurate. 
 
### Political Descriptors by Demographic

The words we use to describe politicians and public figures in general depends a lot on their background. Pick one characteristic to keep track of (age, gender, party, country or state of origin, relationship status, time in office, anything), figure out which words correlate most strongly with politicians who possess that characteristic, and use the crowd to assign an intensity and sentiment to some of these words -- maybe even design a HIT that swaps out the names and pronouns of one politician for another and ask the Turker to assess the clarity and cohesion of the article to see how background affects descriptions in the media. 

</div>
</div>
