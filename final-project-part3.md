---
layout: default
img: prototype-2
caption: Working prototype (icon created by Ben Ehmke from The Noun Project)
title: Final Project part 3 "Working Prototype"
active_tab: homework
release_date: 2021-04-02
due_date: 2021-04-27T23:59:59EDT
final_exam_date: 
final_exam_location: Zoom
submission_link: 
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

The final project presentations will happen during the final exam slot.
<!-- on {{ page.final_exam_date | date: "%A, %B %-d, %Y" }} at {{ page.final_exam_date | date: "%I:%M%p" }} in {{page.final_exam_location}}.
-->
By that time, your system will need to be fully operational, and you'll have to have collected enough data to do an interesting analysis.  We recommend looking over [the questions on the final questionnaire](final-project-part5.html#survey), so that you get a sense of what is expected of the final project. You should pay attention to what sorts of analyses you can do for your final project. 

For your final project, you can collect data by employing a real crowd, or by having your classmates simulate the crowd.  For this part of the project, you will finish a working version of your system, so that your classmates can help you as a simulated crowd, with the goals of debugging your system before you turn the real crowd loose on it, and/or creating some data that you can use to analyze for your final project.

Your classmates will make contributions before the last day of classes, and will get credit toward their participation grade for their contributions.

### What you should do to prepare

* Get a working prototype ready.
* Be sure that it is capable of collecting data from the crowd.
* Write a step-by-step README that walks your classmates through how to use your system, including all details about how to access it and what you want them to do. If you are using a crowdsourcing platform to collect your crowd contributions, then you should set up your project to be running on the Mechanical Turk Worker Sandbox.  
* Put together a short video tutorial that shows *you* using the system for a new member of the crowd (like one of your classmates) and explains to them how you would like them to make contributions to your project.
* Think about what sort of analysis you want to do.  
	- Do you want to compare your system against an existing non-crowdsourcing method?  
	- Do you want to analyze how accurate the crowd is at making predictions?
	- Do you want to test how well your method could scale in terms of time/money?
* Make sure that your capturing the appropriate information so that you can do your analysis.

### Submission

<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### What to submit
</div>
<div class="panel-body" markdown="1">
Below are the required things that you will be asked to provide about your project.  Please turn in your answers using [Final Project: Part 3 on Gradescope]({{page.submission_link}}).

1. Name of your project.
2. A one sentence description of your project.
3. A link (or links) to your tasks on Mechanical Turk Worker Sandbox.
4. A link (or links) to your training video for new members of your crowd (Vimeo link, and password details).
5. A written step-by-step README guide for how your classmates should make contributions to your project. This should include where to access it, and who to contact if it isn't working or if they have any questions.
6. A link to your github repo for the code that you use to run your system.
7. A README describing how the code runs, and what kind of analysis you plan to do and how to do it. 
</div>
</div>


<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Grading Rubric</h4>
</div>
<div class="panel-body" markdown="1">

This assignment is worth 7 points of your overall grade in the course.  The rubric for the assignment is given below. 

* 5 points - have a working prototype with sufficient documentation so that the course staff can verify that it's working
  * 2 points - allowing us to make a submission in the way that a member of the crowd would
  * 2 points - successfully implemented features/milestones set in README
  * 1 point - documentation for code relevant to QC, aggregation, and all supporting code
* 1 point - for your training video for new members of your crowd
* 1 point - for clearly written step-by-step instructions on how they can make contributions
</div>
</div>

