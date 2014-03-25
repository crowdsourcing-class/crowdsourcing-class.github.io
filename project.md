---
layout: default
img: sudo-make-make-a-sandwich
img_link: http://xkcd.com/149/
title: Final project videos
active_tab: main_page 
---

Final Project
=============================================================

The final term project will be a self-designed project created by the students in consultation with the professor and the TA.

## Deliverables

Due October 8th Midterm: In class proposal for project/pitch to class

Progress Update: Individual team meetings with TA+Prof, give concrete progress update

Final: Writeup and demonstration system

Your project should meet the following guidelines:
- Should solve a real world problem
- Should actually use crowdsourcing (it doesn't have to be via MTurk, but that is a good default way to incorporate crowdsourcing)
- Should involve either an HCI or a ML component
- Should explain the choice of incentives and discuss alternative ways of incentivizing workers
- Should contain a quality control component
- Analyze costs, decide whether it is a viable business
- Extra credit: Lay the foundation for a PennApp, Use 99designs to create cool web site
- Bonus Extra credit: Start a business and put your Prof + TA on the board of advisors
- Super extra mega credit: Raise VC funding
- Loss of all credit: Dropping out of school

## Project ideas

Here are a few final project ideas.  You are welcome to adapt one of these ideas into your final project, or to come up with your own idea.  The general guidelines are listed on the course web site at http://crowdsourcing-class.org/assignments.html  My expectation is that your final project will represent a substantial amount of work, and that it will be something that you're proud of and that you would like to show off to potential employers or to graduate schools.
 
 
### Crowdsourcing and Creativity:
 
Create a human computation algorithm to convert prose into poetry.  Your algorithm should model two aspects of poetry: rhyme and meter.  NLP researchers have been working on text-to-text generation algorithms that can rewrite sentences in many different ways.  This software can generate a huge number of alternatives, some of which may fit the constraints of a poem.  However, the software is currently poor at determining which of the generated sentences are grammatical versus ungrammatical, and which correctly retain the its original meaning.  Your job will be to incorporate humans into the process to make those decisions.  Meet with your professor to learn more about the NLP software (it takes quite a lot of effort to learn), and then design a set of MTurk HITs to filter generated sentences down to ones that are poetic, grammatical and mean the same thing as the original prose.
 
 
### Crowd Workers of the world unite:
 
The Mechanical Turk interface for workers sucks.  Although it lets workers search by value of HIT and maximum duration, it lacks one critical piece of inform: expected hourly rate.  Write a web plug in to help workers track their hourly rate.  Design a database that records these stats for multiple workers and reports the average hourly rate for different requesters and/or tasks.  Possible extensions could track the approval/rejection rate of each requester, the average time from doing a HIT to getting paid for it, and a log of all of the reasons for rejection.
 
 
### Design a system for confederated qualifications:
 
Design an implement a method for Mechanical Turk Requesters to share qualification tests and the results of who passed the tests.  Write a short paper describing the value of such a system, and comparing it to MTurk's master's qualification.  Design a few qualifications of your own that you think would be broadly useful, possibly by reviewing the tasks currently posted on MTurk and generalizing the skill sets that are needed.  
 
 
### Cognitive science experiments: 
 
Choose some aspect of the cognitive science that can be tested through experiments on human subjects.  One of my favorite examples of this is Lera Boroditsky's work testing various aspects of the Sapir–Whorf hypothesis that language influences they way that we think.  Read Lera's article on how she used MTurk to test whether metaphors change the way people reason: http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0052961
Choose your own topic (or reimplement several classic experiments).  Write a paper discussing your results, discussing whether MTurk provides a representative sample of subjects, and describing how to go about applying for Institutional Review Board approval for cognitive science experiments on MTurk.
 
 
### Behavioral Economics:
 
Write a suite of HITs on Mechanical Turk to test behavioral economic theories by implementing a set of games like the “ultimatum game”.  In this game two people are paired up. (They can communicate with each other, but otherwise they’re anonymous to each other.) They’re given $10 to divide between them, according to this rule: One person (the proposer) decides, on his own, what the split should be (fifty-fifty, seventy-thirty, or whatever). He then makes a take-it-or-leave-it offer to the other person (the responder). The responder can either accept the offer, in which case both players pocket their respective shares of the cash, or reject it, in which case both players walk away empty-handed. See more details in "The Wisdom of Crowds".  Note that this requires pairing two people simultaneously or simulating their interactions. 
 
 
### Wikitopics:
 
Wikipedia provides hour-by-hour page view statistics for every one of its pages.  Write a human computation algorithm that uses these statistics as input to detect trending topics in the news.  Use humans to (1) review the trending pages to say whether they describe something newsworthy, (2) cluster them into pages about the same event, and (3) write short summaries of the event that triggered them to become popular. Design good mechanisms for quality control for clustering, and for describing something as newsworthy. Read this paper about a baseline computational algorithm: http://www.cis.upenn.edu/~ccb/publications/wikitopics-what-is-popular-on-wikipedia-and-why.pdf
 
 
### MTurk Prediction Market:
 
Prediction markets use collective intelligence to try to predict the outcome of future events.  Prediction markets answer questions that have definite, verifiable answers on a particular date (like "Will the government shutdown still be in effect on October 31, 2013?").  They let people buy and sell shares in the outcomes, and track the value of each outcome's shares over time.  You should implement a prediction market that sets that value of the shares.  You should hire workers on Mechanical Turk to make the predictions.  The major design challenge will be to formulate the system so that it incentivizes Turkers to make well-considered predictions instead of random predictions.  For instance, you may consider designing a HIT that pays nothing initially, but that gives people up to $10 if all of their predictions are accurate.  
 

