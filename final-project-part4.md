---
layout: default
img: analysis
caption: Prelimiary Analysis (icon created by Creative Stall from The Noun Project)
title: Final Project part 4 "Preliminary Analysis"
active_tab: homework
release_date: 2017-04-21
due_date: 2016-04-27T23:59:59EDT
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


Final Project<span class="text-muted"> : Part 4</span> 
=============================================================

The final project is due on Thursday May 5th, 2016.  As part of your final deliverables, you'll have to perform some sort of quantitative analysis on your project. Please look over [the questions on the final questionnaire](final-project-part5.html#survey), so that you get a sense of what is expected of you for the final writeup.

In this final project milestone, you will perform a preliminary analysis on the data that you collected from your classmates or through a crowdsourcing platform, if you've already begun collecting real data.

* Do you want to compare your system against an existing non-crowdsourcing method?  For instance, you could compare the quality of non-expert annotations versus expert annotations.
* Do you want to analyze how accurate the crowd is at making predictions?
* Do you want to test how well your method could scale in terms of time/money?

latency for HCI

accuracy for ML

XXX




### What you should do to prepare

* Get a working prototype ready
* Be sure that it is capable of collecting data from the crowd.
* Write a step-by-step README that walks your classmates through how to use your system, including all details about how to access it and what you want them to do. If you are using a crowdsourcing platform to collect your crowd contributions, then you should set up your project to be running on the Mechanical Turk Worker Sandbox. If you are using CrowdFlower, you should launch your HIT to the "Internal Crowd." You can do this by going to "Contributors" and then to the "Channels" tab, and turning off "On-Demand Workforce." Then you can follow the link at the bottom of the dashboard to test your own HIT. 
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
Please fill out [this questionnaire](XXX).  It asks for the following:

* Details about your team members
* Name of your project
* What kind of analysis did you perform? 
 * 
 * 
 * Other:
* Describe what analysis you performed
* Where the results what you expected?
* Include a link to a PNG of figure that shows a visualization of your preliminary analysis (a graph, a chart, a table)
* Write a caption that describes the figure.  Your caption should says how to interpret it, and gives your understanding of what it shows.
* How many data points were included in your analysis? 
* Give a link to the data files that you analyzed
* Give a link to the code, scripts, or spreadsheets that you used to generate the figure 
* What is the command line argument that we would need to run to produce your analysis?
</div>
</div>


<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Grading Rubric</h4>
</div>
<div class="panel-body" markdown="1">

This assignment is worth 5 points of your overall grade in the course.  The rubric for the assignment is given below. 

TBD
</div>
</div>

