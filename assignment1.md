---
layout: default
img: raised-fist
caption: Workers of the world, unite!
title: Homework 1 "Become a Crowd Worker"
active_tab: homework
release_date: 2016-01-13
due_date: 2016-01-22T14:00:00EST
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

You should be excited about this assignment! You will actually get *paid* to do it! For my 50 HITs, I made a full $1.14. That is a far better return than the terrible stock which I am holding for no good reason. So go! Have fun!

In this assignment you’ll choose at least 50 assignments to complete.  We’re going to do an experiment to compare how much money you make under two conditions.  The first condition is using the MTurk interface, and the second condition is using a productivity tool that your instructor has built, called [Crowd Workers](http://crowd-workers.com/landing). 

1. Sign up for MTurk as a worker [here](https://www.mturk.com/mturk/welcome).  Please do this as early as possible, since it can take 48 hours or more to have your account approved.  Foreign students may have problems signing up since Amazon now requires a Social Security Number. Problems have also arisen when students attempt to set up an Amazon Payments account, which is required by MTurk (this problem can sometimes be resolved by faxing a government ID). <a href = "#faq"> *If you are not able to create an account, follow the instructions here to create a MTurk Sandbox account.* </a>
2. Sign up for Figure Eight as a requester [here](https://make.figure-eight.com/users/new). You won't use this for this assignment directly, but we want everyone signed up early so we can get you set up with Figure Eight credits.
3. Install the [Crowd Workers](http://crowd-workers.com/landing) Google Chrome extension. This will track and help you to analyze the work that you’ve done. Please use the Google Chrome web browser with the Crowd Workers plugin installed for all of this homework assignment.
4. Next, choose at least 50 assignments to complete.  You should pick a goal for yourself.  You can try to make as much money as you can, or you try to make the highest hourly rate that you can. 
  * For the first 25 HITs that you do, use the [search tools provided by Mechanical Turk](https://worker.mturk.com/projects).
     Try to get a sense of the variety of tasks that are available, and the kinds of projects for which Mturk is being used. Once you sign up, you will see that you *can* complete this assignment by transcribing 50 receipts, but is it really worth it? 
  * You may notice that some tasks have pretty strict qualifications. Some of them are based on your amount of tasks completed or your task approval rate. You can see your qualifications [here](https://worker.mturk.com/qualifications/assigned).
  * For your second 25 HITs, use the search tools provided on the [Crowd Workers web service](http://crowd-workers.com/new_work?ordering=-last_submitted,-available&only_favourites=false&min_available=1).
5. There are several tools for better Turking. Please explore a few of these and give us your thoughts.
  * [HITs worth Turking for](http://www.reddit.com/r/HITsWorthTurkingFor/new/?sort=new) 
  * [MTurk Crowd](http://www.mturkcrowd.com)
6. After you have finished working, please answer the following questions about your experience and turn in your answers using [this survey](https://docs.google.com/forms/d/16qS3R6Tc9T807NxHCf_fbS8znBOAjJQVG6NFhyCM_oQ/viewform?usp=send_form). _(We recommend writing the survey answers in a text file on your own computer instead of typing them directly into the Google form, so that you have a copy that you can refer to later)._

**Extra Credit** The Crowd Workers extension you tried is mostly likely the next big thing in crowdsourcing. Right now, it is still a startup in its humble beginnings, being run out of the coffee-cup strewn office of a mere tenure-track professor at an Ivy League university. Help it gain some credibility by leaving a review in the [Google Chrome store](https://chrome.google.com/webstore/detail/crowdworkers/aamdbafophajiecmhbnbakndfgjkfpce/reviews) (we can debate [ethics](http://www.nytimes.com/2013/09/23/technology/give-yourself-4-stars-online-it-might-cost-you.html?_r=0) later). You will get extra credit if you leave a review on the Google Chrome store, or if you the survey to provide us with a thoughtful critique about how to improve the plugin. 

**Extra Credit** We will give extra credit to the student or students who make the most money as a worker.

### Suggested Readings

* [My MTurk (half) Workday](http://www.cs.cmu.edu/~jbigham/posts/2014/half-workday-as-turker.html) by Jeff Bigham
* [Being A Turker](readings/downloads/ethics/being-a-turker.pdf) by David Martin, Benjamin Hanrahan, Jacki O’Neill and Neha Gupta
* [Turkopticon: Interrupting Worker Invisibility in Amazon Mechanical Turk](readings/downloads/ethics/turkopticon.pdf) by Lilly Irani and Six Silberman
* [Crowd-Workers: Aggregating Information Across Turkers To Help Them Find Higher Paying Work](readings/downloads/ethics/crowd-workers.pdf) by Chris Callison-Burch
* [Web Workers, Unite! Addressing Challenges of Online Laborers](readings/downloads/ethics/web-workers-unite.pdf) by Ben Bederson and Alex Quinn
* [A Data-Driven Analysis of Workers’ Earnings on
  Amazon Mechanical Turk](https://www.cs.cmu.edu/~jbigham/pubs/pdfs/2018/crowd-earnings.pdf) by Kotaro Hara, Abigail Adams, Kristy Milland, Saiph Savage, Chris Callison-Burch, and Jeffrey P. Bigham

<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### Survey Questions
</div>
<div class="panel-body" markdown="1">
Below are the questions that you will be asked to answer about your experience as a Crowd Worker.  Please turn in your answers using <a href="https://docs.google.com/forms/d/16qS3R6Tc9T807NxHCf_fbS8znBOAjJQVG6NFhyCM_oQ/viewform?usp=send_form">this form</a>. 

1. Did you successfully sign up as a Worker? If you were unable to sign up as a worker, please give an explanation.
2. Did you successfully sign up for a requester account? If you were unable to sign up as a requester, please give an explanation.
3. If you signed up for Mechanical Turk, what is your Worker ID? You can find it [here](https://www.mturk.com/mturk/dashboard) or [here](http://crowd-workers.com/analytics).
4. How many assignments did you complete? You can look up this information on your [Dashboard](https://www.mturk.com/mturk/dashboard) or on [Crowd Workers](http://crowd-workers.com/analytics).
5. What was your goal when you were working? 
* Make as much money as possible 
* Get a high hourly wage 
* Get through the 50 assignments as quickly as possible 
* Other
6. How much money did you make?
7. How much time did you spend working?
8. Do you think you could make a reasonable wage if Mechanical Turk was your sole source of income? 
* Yes 
* No
9. Did any of your HITs get rejected? You can find out [here](https://www.mturk.com/mturk/dashboard).
* Yes 
* No
10. If you did have a HIT rejected, what reason did the Requester give?
11. What types of tasks did you do, and how did you pick them?
12. What was the highest paying HIT that you completed?  Find it [here](http://crowd-workers.com/analytics?ordering=-reward) and then click on the HIT title, and copy-and-paste a link to the HIT group.
13. What HIT paid you the highest hourly rate?  Sort by "My hourly rate" [here](http://crowd-workers.com/analytics) and then click on the HIT title, and copy-and-paste a link to the HITgroup.
14. Describe the most interesting or weirdest or most fun HIT that you found.  Write a couple of sentences describing it.
15. Which do you think provides a better way of discovering work? 
* Crowd Workers 
* Mechanical Turk 
* Other
16. Why?
17. Would you recommend Crowd Workers to other Turkers? 
* Yes 
* No
18. What would you do to improve the site to make it easier for users to find higher paying work?
19. Did you check out any of the other Turker productivity sites or try any productivity plugins? 
* HITS worth Turking for 
* MTurk Crowd
20. What did you think of the other productivity tools?
21. Extra Credit: Did you Leave a review for Crowd Workers on Google Chrome store? What changes would help improve the Crowd Workers plugin? Were there any bugs you noticed? What was difficult or unintuitive to use? What features would you like to see added?

It is a good idea to write your answers in a file on you own computer, instead of typing them directly into Google, so that you'll have a copy after you press the submit button.  If you type them directly into Google, you won't be able to retrieve them.
</div>
</div>


<div class="panel panel-danger" id="rubric">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 5 points of your overall grade in the course.  The rubric for the assignment is given below.

* 1 point - successfully completing 50 assignments on Mechanical Turk. 
* 1 point - investigating a productivity tool like Crowd Workers or TurkOpticon.
* 3 points - answering the survey questions thoughtfully.
* Extra credit (1 point) - leaving a review of the Crowd Workers extension on Google Chrome store
* Extra credit (1 point) - for the student(s) who make the most money as a worker.  Screenshot or other verification may be requested.

</div>
</div>



<div class="panel panel-info" id="faq">
<div class="panel-heading" markdown="1">
#### FAQ
</div>
<div class="panel-body" markdown="1">
_What should I do if Amazon rejects my application to be a Mechanical Turk worker (or rejects my Amazon Payments account, which has the same effect)?_ 

If you cannot create a Mechanical Turk worker account, [create a Mechanical Turk Sandbox account](<https://workersandbox.mturk.com/>). 

Mechanical Turk's “Sandbox” version is a test version of the Mechanical Turk marketplace. Requesters use it to test out tasks before publishing them. These tasks, despite showing a reward on the site, do not pay any money. Anyone who has an Amazon account can create a Sandbox account, and no SSN information is required.

</div>
</div>