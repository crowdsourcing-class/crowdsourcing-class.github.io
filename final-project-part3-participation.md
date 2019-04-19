---
title: "Be the crowd"
layout: default
img: participate
active_tab: homework
release_date: 2019-04-18
due_date: 2019-04-25T23:59:00EDT
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
This assignment is before {{ page.due_date | date: "%I:%M%p" }} due on {{ page.due_date | date: "%A, %B %-d, %Y" }}.  Late days are *not* allowed for this assignment.
</div>


Be The Crowd
=============

All teams now have a working prototype for their final projects.  In this assignment you will act as the crowd for your classmates' projects.  You will spend a total of 2 hours working on other teams' projects.  Here's what you need to do:

1. Go to [this Google spreadsheet](https://docs.google.com/spreadsheets/d/1bvztCuNSc32DRVATHMfUP2DhyzImyx7Wc3ElJzKOtlk/edit?usp=sharing) and find a project to make contributions to.  You should look in the *Currently accepting submissions?* column to be sure that the project you are looking at is currently accepting submissions from the crowd.  (Note: you can edit this column for your own project, set it to *yes* when you're ready.  Set it to *no* if you find a bug and need to stop people from giving you data that you cannot use). 
2. View the training video and read the step-by-step guide for the project.  Both of these are included on the spreadsheet. If anything is unclear, email the project contact and ask them what you should do.  They should update the instructions so that other people don't ask the same question.
3. When you first start working on a project, take a screenshot that shows that project's HIT.  The screenshot must include your computer's clock as well.  Save a link to the screenshot.  Protip: Dropbox will allow you to share screenshots (got to Dropbox > Settings > Import and then click on the "Share screenshots using Dropbox" option).  If you don't have Dropbox, you can save your screenshots in your github account.
4. When you finish working on a project (or stop to take a break), take another screenshot that shows the end of the HIT and includes your computer's clock.  Save a link to the screenshot.
5. Log your time using [this form](https://docs.google.com/forms/d/e/1FAIpQLSfEFxlzUDlYJmN41ke5M2OVuXq5gppbcMqzr4LctHiH8e4BzA/viewform?usp=sf_link).  You can submit this form multiple times for different projects, or multiple times if you work on the same project at different times with breaks in between. The form will ask you for:

* Your PennKey
* The name of the project your worked on
* The time you spend on this project
* How many screens worth of data you worked on
* Links to your screenshots showing you starting to work on the project, and finishing it (these are used to validate the time that you spent)


