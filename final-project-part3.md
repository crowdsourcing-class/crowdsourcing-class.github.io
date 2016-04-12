---
layout: default
img: prototype-2
caption: Working prototype (icon created by Ben Ehmke from The Noun Project)
title: Final Project part 3 "Working Prototype"
active_tab: homework
release_date: 2016-04-11
due_date: 2016-04-18T23:59:59EDT
---
<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.release_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->


<div class="alert alert-info">
This assignment is before {{ page.due_date | date: "%I:%M%p" }} due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>


Final Project<span class="text-muted"> : Part 3</span> 
=============================================================

The final project is due on Thursday May 5th, 2016.  By that time, your system will need to be fully operational, and you'll have to have collected enough data to do an interesting analysis.  We recommend looking over [the questions on the final questionnaire](final-project-part4.html#survey), so that you get a sense of what is expected of the final project. You should pay attention to what sorts of analyses you can do for your final project. 

For your final project, you can collect data by employing a real crowd, or by having your classmates simulate the crowd.  For this part of the project, you will finish a working version of your system, so that your classmates can help you as a simulated crowd, with the goals of debugging your system before you turn the real crowd loose on it, and/or creating some data that you can use to analyze for your final project.

Your classmates will make contributions before the last day of classes, and will get credit toward their participation grade for their contributions.

### What you should do to prepare

* Get a working prototype ready
* Be sure that it is capable of collecting data from the crowd.
* Write a step-by-step README that walks your classmates through how to use your system, including all details about how to access it and what inputs you need.
* Put together a short video tutorial for a new member of the crowd (like one of your classmates) shows you using the system, and explains to them how you would like them to make contributions to your project
* Think about what sort of analysis you want to do.  
	- Do you want to compare your system against an existing non-crowdsourcing method?  
	- Do you want to analyze how accurate the crowd is at making predictions?
	- Do you want to test how well your method could scale in terms of time/money?
* Make sure that your capturing the appropriate information so that you can do your analysis.




<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### What to submit
</div>
<div class="panel-body" markdown="1">
Please fill out [this questionnaire](https://docs.google.com/forms/d/10kT2rAlzStgj0D6q0FBo4EspBKQQSt4ckRg-30rAnV0/viewform).  It asks for the following:

* Details about your team members
* Name of your project
* A one sentence description of your project.
* A logo for your project (PNG format, stored on github)
* What type of project is it? 
  * Human computation algorithm
  * Social science experiment with the crowd
  * A tool for crowdsourcing
  * A business idea that uses crowdsourcing
  * Other
* Provide a link to your training video for new members of your crowd (Vimeo link, and password details)
* A written step-by-step guide for how your classmates should make contributions to your project. This should include where to access it, and who to contact if it isn't working or if  they have any questions.

</div>
</div>