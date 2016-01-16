---
layout: default
img: sudo-make-make-a-sandwich
img_link: http://xkcd.com/149/
title: Term project
active_tab: project
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

<div class="alert alert-info" markdown="span">
Check out these fantastic [final project videos](final-projects.html) from the Fall 2013 class!
</div>

Final Project
=============================================================

The final term project will be a self-designed project created by the students in consultation with the professor and the TA.

## Deliverables

Due October 8th Midterm: In class proposal for project/pitch to class

Progress Update: Individual team meetings with TA+Prof, give concrete progress update

Final: Writeup and demonstration system

Your project should meet the following guidelines:

* Should solve a real world problem
* Should actually use crowdsourcing (it doesn't have to be via MTurk, but that is a good default way to incorporate crowdsourcing)
* Should involve either an HCI or a ML component
* Should explain the choice of incentives and discuss alternative ways of incentivizing workers
* Should contain a quality control component
* Analyze costs, decide whether it is a viable business
* Extra credit: Lay the foundation for a PennApp, Use 99designs to create cool web site
* Bonus Extra credit: Start a business and put your Prof + TA on the board of advisors
* Super extra mega credit: Raise VC funding
* Loss of all credit: Dropping out of school

## Project ideas

Here are a few final project ideas. You are welcome to adapt one of these ideas into your final project, or to come up with your own idea. 
My expectation is that your final project will represent a substantial amount of work, and that it will be something that you're proud of and that you would like to show off to potential employers or to graduate schools.
 
### Crowdsourced Matchmaking

Come up with a human computation algorithm that helps people find a better match in online dating.  Some people have tried to use [machine learning](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) or [crowdsourcing](http://www.youlookgoodtogether.com) to optimize their dating experience on OKCupid.  Can you come up with a better way of matching people up via crowdsourcing?  Maybe you can have the crowd act as Cyrano de Bergerac, feeding users better lines than they could think of themselves.  Maybe you could have people in a social network nominate people who they think would be good matches.

### Translate Children's Books

[The International Children's Digital Library](http://en.childrenslibrary.org) is a collection of children's books from around the the world.  Volunteer translators have translated a subset of their books into different languages.  We could try to translate many more of the books using crowdsourcing.  There could be different tasks for monolingual speakers and bilingual speakers.  Monolinguals could transcribe the text of the books (which is usually embedded in images).  Bilinguals could translate it.  Monolinguals could edit the translations.  


### Crowdsourcing and Creativity
 
Create a human computation algorithm to convert prose into poetry. Your algorithm should model two aspects of poetry rhyme and meter. NLP researchers have been working on text-to-text generation algorithms that can rewrite sentences in many different ways. This software can generate a huge number of alternatives, some of which may fit the constraints of a poem. However, the software is currently poor at determining which of the generated sentences are grammatical versus ungrammatical, and which correctly retain the its original meaning. Your job will be to incorporate humans into the process to make those decisions. Meet with your professor to learn more about the NLP software (it takes quite a lot of effort to learn), and then design a set of MTurk HITs to filter generated sentences down to ones that are poetic, grammatical and mean the same thing as the original prose.
 

### Crowd Workers of the world, unite!
 
The Mechanical Turk interface for workers sucks. Although it lets workers search by value of HIT and maximum duration, it lacks one critical piece of inform: expected hourly rate. Write a web plug in to help workers track their hourly rate. Design a database that records these stats for multiple workers and reports the average hourly rate for different requesters and/or tasks. Possible extensions could track the approval/rejection rate of each requester, the average time from doing a HIT to getting paid for it, and a log of all of the reasons for rejection.
 
  
### Fairness in rejection

Design an adjudication system for work rejected by Mechanical Turk Requesters.  The system should allow Workers to appeal rejections, and should have a mechanism for deciding whether the rejection was fair (in which case it would stand), or unfair (in which case it should be overturned, and the Worker should be paid).  Possible ideas: design a second pass HIT that has other Turkers review the work, and decide whether it is acceptable or not.  As part of this project you should specify what constraints are on the original HIT design to allow easy second pass reviewing and highlighting / explanation of why an assignment was rejected.  You should also quantify the expected increase in costs to Requesters, based on variables like: rejection rate, original reward amount, reviewing cost estimate. 


### Design a system for confederated qualifications
 
Design an implement a method for Mechanical Turk Requesters to share qualification tests and the results of who passed the tests. Write a short paper describing the value of such a system, and comparing it to MTurk's master's qualification. Design a few qualifications of your own that you think would be broadly useful, possibly by reviewing the tasks currently posted on MTurk and generalizing the skill sets that are needed. 



### Cognitive science experiments 
 
Choose some aspect of the cognitive science that can be tested through experiments on human subjects. One of my favorite examples of this is Lera Boroditsky's work testing various aspects of the Sapir–Whorf hypothesis that language influences they way that we think. Read Lera's article on how she used MTurk to test whether [metaphors change the way people reason](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0052961). Choose your own topic (or reimplement several classic experiments). Write a paper discussing your results, discussing whether MTurk provides a representative sample of subjects, and describing how to go about applying for Institutional Review Board approval for cognitive science experiments on MTurk.
 
 
### Behavioral Economics
 
Write a suite of HITs on Mechanical Turk to test behavioral economic theories by implementing a set of games like the "ultimatum game". In this game two people are paired up. (They can communicate with each other, but otherwise they’re anonymous to each other.) They’re given $10 to divide between them, according to this rule: One person (the proposer) decides, on his own, what the split should be (fifty-fifty, seventy-thirty, or whatever). He then makes a take-it-or-leave-it offer to the other person (the responder). The responder can either accept the offer, in which case both players pocket their respective shares of the cash, or reject it, in which case both players walk away empty-handed. See more details in "The Wisdom of Crowds". Note that this requires pairing two people simultaneously or simulating their interactions. 
 
### Speech Recognition Systems

Apple uses speech recognition systems for Siri.  You can develop this technology for new languages.  You need an [open source speech recognition system](http://kaldi.sourceforge.net/about.html) and a bunch of training data.  What sort of data?  Audio files paired with their transcriptions.  Where do you get data?  Crowdsourcing!  You can come up with ways of collecting data.  You could gather data either through transcription of existing audio files, or `elicitation' where people read texts out loud and save recordings of it. You'll need to figure out how to do good quality control, to what extent the quality matters when you're training a speech recognition system for a new langauge.

### Food Truck Tracker

There are a lot of food trucks in Philly.  Some of them are so awesome that they move to different locations on different days.  They announce their whereabouts on Twitter or Facebook.  Do they really expect us to keep track of where they all are?  Why not have the crowd create a map of the current whereabouts of all the food trucks.  How about having the crowd keep track of their menus and prices while you're at it?

### Track the spread of the flu using social media 

Did you know that you can catch the flu from social media?  Well, you can't.  But you can use it as a tool to track the spread of certain diseases.  You could try re-creating one of the publications by [this cool researcher](http://www.cs.jhu.edu/~mdredze/publications.php).  What sorts of health problems do you think social media can give us information about?  
 
### Wikitopics
 
Wikipedia provides hour-by-hour page view statistics for every one of its pages. Write a human computation algorithm that uses these statistics as input to detect trending topics in the news. Use humans to (1) review the trending pages to say whether they describe something newsworthy, (2) cluster them into pages about the same event, and (3) write short summaries of the event that triggered them to become popular. Design good mechanisms for quality control for clustering, and for describing something as newsworthy. Read this paper about [a baseline computational algorithm.](http://www.cis.upenn.edu/~ccb/publications/wikitopics-what-is-popular-on-wikipedia-and-why.pdf)
 
 
### MTurk Prediction Market
 
Prediction markets use collective intelligence to try to predict the outcome of future events. Prediction markets answer questions that have definite, verifiable answers on a particular date (like "Will the government shutdown still be in effect on October 31, 2013?"). They let people buy and sell shares in the outcomes, and track the value of each outcome's shares over time. You should implement a prediction market that sets that value of the shares. You should hire workers on Mechanical Turk to make the predictions. The major design challenge will be to formulate the system so that it incentivizes Turkers to make well-considered predictions instead of random predictions. For instance, you may consider designing a HIT that pays nothing initially, but that gives people up to $10 if all of their predictions are accurate. 
 
### Political Descriptors by Demographic

The words we use to describe politicians and public figures in general depends a lot on their background. Pick one characteristic to keep track of (age, gender, party, country or state of origin, relationship status, time in office, anything), figure out which words correlate most strongly with politicians who possess that characteristic, and use the crowd to assign an intensity and sentiment to some of these words -- maybe even design a HIT that swaps out the names and pronouns of one politician for another and ask the Turker to assess the clarity and cohesion of the article to see how background affects descriptions in the media. 

### Efficacy of Gun Violence Databases

The Guardian recently started publishing an online database of police-involved killings called [The Counted](http://www.theguardian.com/us-news/ng-interactive/2015/jun/01/the-counted-police-killings-us-database). In turn, the FBI announced that it would also be [publishing information](http://www.theguardian.com/us-news/2015/dec/09/fbi-launch-new-system-count-people-killed-police-officers-the-counted) about the deadly use of physical force nationwide. This information is tracked in a lot of places, including gun violence blogs and even in the projects of students who took NETS213 last year. Using the crowd to identify duplicates and supplement details in one place could yield interesting information about which areas are best at reporting violence, which news sources are least accurate, or any other problem you'd like to study. Automatic reconciliation of conflicting data and classification of the type of data would likely require some strong HIT design. 

### Inspiration from others

[Jeffery Bigham](http://www.cs.cmu.edu/~jbigham/) runs a class at CMU. [You can check out his list of suggested final project topics.](http://www.programthecrowd.com/finalproject)


[Open Data Philly](http://opendataphilly.org) has cool data about things in Philly.
