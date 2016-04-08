---
layout: default
img: prototype-2
caption: Working prototype (icon created by Ben Ehmke from The Noun Project)
title: Final Project "Working Prototype"
active_tab: homework
release_date: 2017-04-11
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

The final project is due on Thursday May 5th, 2016.  By that time, your system will need to be fully operational, and you'll have to have collected enough data to do an interesting analysis.  You can either collect data by employing a real crowd, or by having your classmates simulate the crowd.  

For this project, you will finish a working version of your system, so that your classmates can help you as a simulated crowd, with the goal of creating some data that you can use to analyze for your final project.

What you should do to prepare:

* Get a working prototype ready
* Be sure that it is capable of collecting data from the crowd.
* Write a step-by-step README that shows your classmates how to use your system.
* Think about what sort of analysis you want to do.  
	- Do you want to compare your system against an existing non-crowdsourcing method?  
	- Do you want to analyze how accurate the crowd is at making predictions?
	- Do you want to test how well your method could scale in terms of time/money?
* Make sure that your capturing the appropriate information so that you can do your analysis.