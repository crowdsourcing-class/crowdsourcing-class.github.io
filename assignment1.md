---
layout: default
img: raised-fist
caption: Workers of the world, unite!
title: Homework 1 "Become a Crowd Worker"
active_tab: homework
release_date: 2019-01-22
due_date: 2019-01-29T23:59:00EST
submission_link: https://www.gradescope.com/courses/36538
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
This assignment is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
</div>


Become a Crowd Worker <span class="text-muted">: Assignment 1</span> 
=============================================================

The point of the first assignment is to get to acquainted with Mechanical Turk from the worker's perspective. The crowdsourcing platform allows us, the programmers, to work with humans as though they are function calls (fulfilling every antisocial CS student's dreams). Since, for the rest of the semester, you will be relying on crowd workers to complete work for you quickly and accurately, you should take this first assignment as an opportunity to understand your workers and the ways you can help them work best for you. Pay attention to what makes tasks interesting and attractive, how much each task pays, and whether you think the compensation is fair. We will ask you to turn in a short writeup describing your experience.

You should be excited about this assignment! You may actually get *paid* to do it! For my 50 HITs, I made a full $1.14. Only 438 more HITs to go before I can go downstairs and buy lunch at the Franklin Table food court. So go! Have fun!

In this assignment you’ll choose at least 50 HITs to complete.  We’re going to do an experiment to compare how much money you make under two conditions.  The first condition is using the MTurk interface, and the second condition is using a productivity tool that your instructor has built, called [Crowd Workers](http://crowd-workers.com/landing). 

1. Sign up for MTurk as a worker [here](https://www.mturk.com/mturk/welcome).  Please do this as early as possible, since it can take 48 hours or more to have your account approved.  Foreign students may have problems signing up since Amazon now requires a Social Security Number. Problems have also arisen when students attempt to set up an Amazon Payments account, which is required by MTurk (this problem can sometimes be resolved by faxing a government ID). <a href = "#faq"> *If you are not able to create an account, follow the instructions in the FAQ section to create a MTurk Sandbox account.* </a>
2. Install the [Crowd Workers](http://crowd-workers.com/landing) Google Chrome extension. This will track and help you to analyze the work that you’ve done. Please use the Google Chrome web browser with the Crowd Workers plugin installed for all of this homework assignment. *This is not required if you are using Sandbox version and do not have access to Crowd Workers.* *If you're using the regular mechanical turk version, please see the <a href = "#faq">FAQ section</a> below to use the Greasy Fork extension as an alternative.*
3. Next, choose at least 50 HITs to complete.  You should pick a goal for yourself.  You can try to make as much money as you can, or you try to make the highest hourly rate that you can. 
  * For the first 25 HITs that you do, use the [search tools provided by Mechanical Turk](https://worker.mturk.com/projects).
     Try to get a sense of the variety of tasks that are available, and the kinds of projects for which Mturk is being used. Once you sign up, you will see that you *can* complete this assignment by transcribing 50 receipts, but is it really worth it? 
  * You may notice that some tasks have pretty strict qualifications. Some of them are based on your amount of tasks completed or your task approval rate. You can see your qualifications [here](https://worker.mturk.com/qualifications/assigned).
  * For your second 25 HITs, use the search tools provided on the [Crowd Workers web service](http://crowd-workers.com/new_work?ordering=-last_submitted,-available&only_favourites=false&min_available=1). *You are not required to use Crowd Workers if you are using Sandbox version and do not have access to Crowd Workers. If Crowd Workers isn't providing you search results, then you may continue using Mechanical Turk's search tools for the second 25 tasks.*
4. There are several tools for better Turking. Please explore a few of these and give us your thoughts.
  * [TurkerView](https://turkerview.com)
  * [HITs worth Turking for](http://www.reddit.com/r/HITsWorthTurkingFor/new/?sort=new) 
  * [MTurk Crowd](http://www.mturkcrowd.com)
5. After you have finished working, please answer the following questions about your experience and turn in your answers using [the Homework 1 survey on Gradescope]({{page.submission_link}}). 

**Note:** The Crowd Workers extension you tried is like totally the next big thing in crowdsourcing. It started with humble beginnings, being run out of the coffee-cup strewn office of a mere tenure-track professor at an Ivy League university. Help it gain some credibility by leaving a review of it in the [Google Chrome store](https://chrome.google.com/webstore/detail/crowdworkers/aamdbafophajiecmhbnbakndfgjkfpce/reviews).

### Suggested Readings

* [My MTurk (half) Workday](http://www.cs.cmu.edu/~jbigham/posts/2014/half-workday-as-turker.html) by Jeff Bigham
* [Being A Turker](readings/downloads/ethics/being-a-turker.pdf) by David Martin, Benjamin Hanrahan, Jacki O’Neill and Neha Gupta
* [Turkopticon: Interrupting Worker Invisibility in Amazon Mechanical Turk](readings/downloads/ethics/turkopticon.pdf) by Lilly Irani and Six Silberman
* [Crowd-Workers: Aggregating Information Across Turkers To Help Them Find Higher Paying Work](readings/downloads/ethics/crowd-workers.pdf) by Chris Callison-Burch
* [Web Workers, Unite! Addressing Challenges of Online Laborers](readings/downloads/ethics/web-workers-unite.pdf) by Ben Bederson and Alex Quinn
* [A Data-Driven Analysis of Workers’ Earnings on
  Amazon Mechanical Turk](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2018/crowd-earnings.pdf) by Kotaro Hara, Abigail Adams, Kristy Milland, Saiph Savage, Chris Callison-Burch, and Jeffrey P. Bigham

  

<div class="panel panel-info" id="faq">
<div class="panel-heading" markdown="1">
#### FAQ
</div>
<div class="panel-body" markdown="1">
- **What should I do if Amazon rejects my application to be a Mechanical Turk worker (or rejects my Amazon Payments account, which has the same effect)?**

	If you cannot create a Mechanical Turk worker account, [create a Mechanical Turk Sandbox account](<https://workersandbox.mturk.com/>). 
	
	Mechanical Turk's “Sandbox” version is a test version of the Mechanical Turk marketplace. Requesters use it to test out tasks before publishing them. These tasks, despite showing a reward on the site, do not pay any money. Anyone who has an Amazon account can create a Sandbox account, and no SSN information is required.
	
	The Crowd Workers extension doesn't work with the workersandbox, so please put  N/A in your survey answers for questions involving Crowd Workers if you do not have access to it.

- **What should I do if Crowdworkers isn't showing information for my completed tasks?**

  An alternative to Crowdworkers is Greasy Fork, which can help get information on your overall hourly wage as well as different requesters' hourly wages. Here are [instructions](https://greasyfork.org/en/help/installing-user-scripts) on how to get a web extension for your browser to load the Greasy Fork script, and here's a [link](https://greasyfork.org/en/scripts/31108-mturk-hourly) to download the script. Once you have the script loaded, you should be able to see hourly wage information on your mechanical turk [dashboard](https://worker.mturk.com/dashboard) page. On the dashboard, click on a given date, and you should be able to see the HIT(s) that you did, what their rewards were, and what their hourly wages are. 

- **After loading Greasy Fork, why are all the hourly wages on the MTurk dashboard listed as N/A?**

  Greasy Fork does not track previous tasks. It will give an associated hourly wage to the tasks you complete after enabling the feature.

</div>
</div>

<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### Survey Questions
</div>
<div class="panel-body" markdown="1">
Below are the questions that you will be asked to answer about your experience as a Crowd Worker.  Please turn in your answers using [the Homework 1 survey on Gradescope]({{page.submission_link}}).

It is a good idea to write your answers in a file on you own computer, instead of typing them directly into Gradescope, so that you'll have a copy after you press the submit button. 

**Note:** Please put N/A in your survey answer for questions involving Crowd Workers if you do not have access to it.

1. Did you successfully sign up as a Worker? 
2. If you were unable to sign up as a worker, please give an explanation.
3. Did you successfully sign up for a requester account? 
4. If you were unable to sign up as a requester, please give an explanation.
5. What is your Worker ID? If you signed up for Mechanical Turk or Mechanical Turk Sandbox, you can look up this information on your Dashboard (<https://www.mturk.com/mturk/dashboard> or <https://workersandbox.mturk.com/dashboard>) or on Crowd Workers (<http://crowd-workers.com/analytics>).
6. How many assignments did you complete? You can look up this information on your Dashboard (<https://www.mturk.com/mturk/dashboard> or <https://workersandbox.mturk.com/dashboard>) or on Crowd Workers (<http://crowd-workers.com/analytics>).
7. What was your goal when you were working? 
* Make as much money as possible 
* Get a high hourly wage 
* Get through the 50 assignments as quickly as possible 
* Other
8. How much money did you make?
9. How much time did you spend working?
10. Do you think you could make a reasonable wage if Mechanical Turk was your sole source of income? 
* Yes 
* No
11. Did any of your HITs get rejected? You can find out on your Dashboard (<https://www.mturk.com/mturk/dashboard> or <https://workersandbox.mturk.com/dashboard>).
* Yes 
* No
12. If you did have a HIT rejected, what reason did the Requester give?
13. What types of tasks did you do, and how did you pick them?
14. What was the highest paying HIT that you completed?  Find it on Crowd Workers [here](http://crowd-workers.com/analytics?ordering=-reward) and then click on the HIT title, and copy-and-paste a link to the HIT group. You can also go through your HITs on the Dashboard to see which one is highest paying.
15. What HIT paid you the highest hourly rate? Sort by "My hourly rate" on Crowd Workers [here](http://crowd-workers.com/analytics) and then click on the HIT title, and copy-and-paste a link to the HITgroup. Please follow the instructions in the FAQ to find this HIT if you used Greasy Fork.
16. Describe the most interesting or weirdest or most fun HIT that you found.  Write a couple of sentences describing it.
17. Which do you think provides a better way of discovering work? What is the reason? If other, please specify.
* Crowd Workers 
* Mechanical Turk 
* Other
18. Would you recommend Crowd Workers to other Turkers? 
* Yes 
* No
19. What would you do to improve the Crowd Worker site to make it easier for users to find higher paying work? If Crowd Workers didn't work for you, what feature would you add to Mechanical Turk to make it easier for workers to find higher paying tasks?
20. Did you check out any of the other Turker productivity sites or try any productivity plugins? 
* HITS worth Turking for 
* MTurk Crowd
21. What did you think of the other productivity tools?
22. Did you Leave a review for Crowd Workers on Google Chrome store? 
23. What did your review say? 
24. If you prefer to give constructive criticism instead of a review, what changes would help improve the Crowd Workers plugin? Were there any bugs you noticed? What was difficult or unintuitive to use? What features would you like to see added?
</div>
</div>


<div class="panel panel-danger" id="rubric">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>

<div class="panel-body" markdown="1">
This assignment is worth approximately 5% of your overall grade in the course. Please answer the survey questions thoughtfully.
</div>
</div>

