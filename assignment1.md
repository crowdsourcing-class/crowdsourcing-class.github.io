---
layout: default
img: raised-fist
caption: Workers of the world, unite!
title: Homework 1 "Become a Crowd Worker"
active_tab: homework
release_date: 2021-01-28
due_date: 2021-02-04T23:59:00EST
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
This assignment is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}.
</div>


Become a Crowd Worker <span class="text-muted">: Assignment 1</span> 
=============================================================

The point of the first assignment is to get a the worker's perspective. Crowdsourcing platforms like Mechanical Turk allow us, the programmers, to work with humans as though they are function calls (fulfilling every antisocial CS student's dreams). Since, for the rest of the semester, you will be relying on crowd workers to complete work for you quickly and accurately, you should take this first assignment as an opportunity to understand your workers and the ways you can help them work best for you. Pay attention to what makes tasks interesting and attractive, how much each task pays or what non-financial incetives are effective, and whether you think the compensation is fair. 


We will ask you to turn in a short writeup describing your experience.  As inspiration for your writeup, you should read this essay by Jeff Bigham called ["My MTurk (half) Workday"](http://www.cs.cmu.edu/~jbigham/posts/2014/half-workday-as-turker.html).  


In this assignment you should try to do work on *two* crowd platforms from this list:
* Mechanical Turk
* Zooniverse
* Google Crowdsource
* Figure 8
* Upwork
* Datasaur

You should spend 2-3 hours per platform.    If you work with a partner, you should Zoom together and do the tasks together (rather than divvying up the work). 

You should write up your experience working on the two platforms.  Your writeup should be 2000 words long. You can take screenshots of the tasks that you do to include in your writeup. For each of the platforms, we give some suggested questions to answer in your writeup.  You can submit a PDF of your writeup to [Gradescope]({{page.submission_link}}).




## Mechanical Turk
*Overview:*.  Mechanical Turk is a crowdsourcing website Requesters to hire crowdworkers to perform microtasks in return for micropayments. It is operated under Amazon Web Services, and is owned by Amazon. Employers post jobs known as Human Intelligence Tasks (HITs), named since MTurk was designed for tasks that are easy for people, but that computers are currently unable to do. HITs can be tasks like as identifying content in an image, writing product descriptions, or answering questions. Workers, also known as Turkers or crowdworkers, browse among existing jobs and complete them in exchange for a rate set by the employer.

### How to Sign Up:
1. Sign up for MTurk as a worker [here](https://www.mturk.com/mturk/welcome).  Please do this as early as possible, since it can take 48 hours or more to have your account approved.  Foreign students may have problems signing up since Amazon now requires a Social Security Number. Problems have also arisen when students attempt to set up an Amazon Payments account, which is required by MTurk.
2. Optionally, try installing a MTurk productivity tool like [TurkerView](https://turkerview.com) or [Turkopticon](https://turkopticon.ucsd.edu), or check out the [ITsWorthTurkingFor subreddit](https://www.reddit.com/r/HITsWorthTurkingFor/).

### Questions to address in your writeup:
* How long did it take you to sign up as a worker?
* What is your Worker ID? If you signed up for Mechanical Turk you can look up this information on your Dashboard (<https://www.mturk.com/mturk/dashboard>.
* How many assignments did you complete? You can look up this information on your Dashboard (<https://www.mturk.com/mturk/dashboard>.
* What was your goal when you were working? 
** Make as much money as possible 
** Get a high hourly wage 
** Get through the assignments as quickly as possible 
* How much money did you make?
* How much time did you spend working?
* Do you think you could make a reasonable wage if Mechanical Turk was your sole source of income? 
* Did any of your HITs get rejected? You can find out on your Dashboard (<https://www.mturk.com/mturk/dashboard>.
* If you did have a HIT rejected, what reason did the Requester give?
* What types of tasks did you do, and how did you pick them?
* What was the highest paying HIT that you completed?  
* What HIT paid you the highest hourly rate? 
* Describe the most interesting or weirdest or most fun HIT that you found.  Write a couple of sentences describing it.
* Did you try any of the productivity tools?  What did you think?

## Zooniverse

*Overview:*
Zooniverse is a citizen-science platform in which volunteers around the world contribute to projects sourced from the professional research community. With over 1.6mm registered users, the platform supports research projects by allowing volunteers to perform tasks such as completing surveys and labeling datasets. 

### How to Sign Up:
1. Go to [https://www.zooniverse.org/](https://www.zooniverse.org/) and click on “Register” in the top right corner of the page.
2. Input your personal information to create your Zooniverse account.
3. Go to [https://www.zooniverse.org/projects](https://www.zooniverse.org/projects) and click on any of the available projects to reach its project overview page.
4. Read about your selected project on its project overview page and begin contributing by clicking on “Classify” at the top of the page. Task instructions will be available for your reference. 

### Questions to address in your writeup:
* What projects did you select? Why did you pick them?
* What were the specific tasks that you had to complete?
* Did you find the task instructions easy to follow?
* What are examples of completed projects and publications that you see featured on the platform? 
* How much time did you spend on each project in total, and how long did its idividual tasks take?
* All individuals on Zooniverse participate as volunteers – what do you think incentivizes individuals to contribute through this platform?




## Google Crowdsource
*Overview:*
Google Crowdsource is a platform for contributing to making the AI building blocks in Google products better. Examples of products that integrate AI at Google include Google Translate, Maps, Photos, and Assistant. In Google Crowdsource, you’ll perform small tasks (like writing a caption to an image or recognizing facial expressions). The results will be used to train AI models that help make these products better and improve their performance for a diverse population of users. 

See more information about it at: 
[https://crowdsource.google.com/about/](https://crowdsource.google.com/about/)

### How to Sign Up:
1. Go to [https://crowdsource.google.com/](https://crowdsource.google.com/) and log into a Google account
2. Once logged in, make sure you are on the  [https://crowdsource.google.com/](https://crowdsource.google.com/) main page
3. You should see tasks like “Image Label Verification”, “Handwriting Recognition”, “Facial Expressions” that you can complete. It’s fairly straightforward to click on some of these and try out solving some of these tasks.
4. On the achievements page (https://crowdsource.google.com/achievements), you’ll see what level you are, a summary of your activity, and “badges” you can earn by completing tasks.
5. Please complete Level 1 for 3 badges:
* Earn Level 1 on the Contributor badge (you achieve this by completing 100 tasks total)
Choose any one of the other badges that interest you to get Level 1 on. You can click on badges to see what you need to do in order to earn them.
* Choose any one of the other badges that interest you to get Level 1 on. You can click on badges to see a description of what you need to do in order to earn them.

### Questions to address in your writeup:
* What projects did you select?  Why did you pick them?
* What were the specific tasks that you had to complete?
* Did you find the task instructions easy to follow?
*  How many total contributions did you make on Google Crowdsource? You can find this information on your achievements page.  
* What badges did you earn? What level are you on each badge? What were the requirements for each badge?
* If you were designing badges for Google Crowdsource, can you think of a new badge you would create? Give it a name and a description of what it would take to earn Level 1 for your badge.
* How did you handle ambiguous cases that you were unsure of? Did you make an educated guess or did you skip it?
* How do you like the UI/UX design of Google’s annotation tool, does it allow you to complete your tasks efficiently? What improvements, if any, would you make?
* Do you think Google verifies the reliability/trustworthiness of annotators like you? If you were to design a system that filters out “bad” annotators (spammers, bots, NETS 213 students rushing through to complete the assignment), what would you do?
* Why do you think this platform doesn’t offer money as an incentive like Amazon MTurk?
* Do you think you would contribute to this platform if it weren’t for a grade? Do you think others would?
* Had you heard about Google Crowdsource before? Do you think it’s easy to find for most users? If you worked at Google, how might you encourage people to use the platform?
* Why do you think Google implements a badge system instead of just showing you the total number of tasks completed?
* Describe the most interesting or weirdest or most fun job that you were assigned. Write a couple of sentences describing it.
* Describe the hardest or most ambiguous job that you were assigned. Write a couple sentences describing it.
* For each of the annotation categories, try to name a Google product or service that would benefit from your work.
* Image Label Verification, Image Caption, Handwriting Recognition, Facial Expressions, Landmarks
* Write a review (brief, just a couple sentences) of Google Crowdsource from a user’s perspective. What did you like? What did you hate? What did you find frustrating? What would you like to see improved?




## Figure 8
*Overview:*
Figure 8 (formerly Crowdflower) was acquired by Appen for $300 million in 2019. The Appen Part-Time flexible jobs now offers a variety of crowd work employment options ranging from the micro tasks we have discussed to longer term projects. 

### How to Sign Up:
1. To sign up go to the link [https://appen.com/jobs/](https://appen.com/jobs/) and choose ‘Micro Tasks’. From there you’ll need to make an Appen Contributor Account which takes your info and a Paypal for you to receive your payments. Then after you verify you’ll get into a portal to accept a dummy task which will have you sign up for an Appen Platform account. Note that the Contributor account and the Platform account are different so you can use the same email for both but you have to sign up and verify for both.
2. On the sign up there is also a Projects and a Surveys & Data Collection option but these require applying (similar to applying on MTurk) and to get a feel of the platform it’s easier to quickly sign up for the Micro Tasks platform. 

### Questions to address in your writeup:
* Were you able to easily figure out the signup and two different platforms?
* Did you understand how you find tasks to complete once you’re on the platform?
* Did you find the task instructions easy to follow?
* What do you think of the badge system that Appen uses to allow work to certain workers?
* How many tasks did you complete and what was your reward?
* Did you like the setup of the tasks? 

## Upwork
*Overview:*
Upwork is a platform for a variety of different freelance tasks, it is not specific to crowdsourcing. Services that you can offer include IT, design or crowdsourcing services. Upwork goes both ways – you can either post your skills or apply to projects that are being posted by clients. The platform provides a payment guarantee for freelancers as well as a job board.

### How to Sign Up:
1. Go to https://www.upwork.com/signup/?accountType=client and register. Please select “Work as a Freelancer” during sign-up.
2. After you’ve verified your email address, you’re being asked to fill out your profile. It’s important to do this thoroughly as Upwork is approving you based on this information. When asked about your experience level, you should select “Beginner” unless you have had some previous CS experience.
3. Once your account is being approved, you can start searching for crowdsourcing projects by using the search function in the project section.

### Questions to address in your writeup:
* What was the project that you selected? 
* Were you able to get accepted by the client? 
** If yes: What were the specific tasks that you had to complete?
**  Did you find the task instructions easy to follow?
**  How much time did you spend on this project?
** If you didn’t get selected: Why do you think the client picked someone else? Did you think the selection process was fair?

## Datasaur
*Overview:* Datasaur is a platform for doing linguistic annotation for artificial intelligence. Companies have re-invented the wheel in building their own ad hoc data labeling tools. Datasaur was founded to create high quality annotation interface to reduce the re-invention.  Professor Callison-Burch's lab is using Datasaur to annotate data for one of thier DARPA grants.  If you'd like to help out with this annotation for your project, you can follow [these instructions from TAs Ashley and Becca](https://docs.google.com/document/d/1ha77rColinlURzGMjATMbCs-UMhEC9tHqwnCQMfJcRs/edit?usp=sharing) who are managing the annotation effort.


### Questions to address in your writeup:
* Describe the annotation project that you did.
* What did you learn about goals the project?
* Did you find the task instructions easy to follow?
* How many tasks did you complete?
* Do you want to learn more about semantic role labeling](https://web.stanford.edu/~jurafsky/slp3/19.pdf)?