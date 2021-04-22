---
layout: default
img: the-visual-display-of-quantitative-information
img_link: http://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142/
caption: Read this book. It will change your life.
title: Homework 8 "Analyze Data"
active_tab: homework
release_date: 2021-04-22
due_date: 2021-05-11T12:00:00EST
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

<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<div class="alert alert-info">
This assignment is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

Analyze Data<span class="text-muted">: Assignment 8 (Optional Extra Credit) </span> 
=============================================================

For this assignment, we will analyze data about MTurkers, and try to see if it helps us better understand who/where/when/how questions about crowd workers in the world. 

Please download the [starter code](assignments/downloads/hw8_2021sp.zip). It contains three csv files as data, and a jupyter notebook **homework8.ipynb** with questions, instructions, and skeleton code. Please do not modify any of the function names or input parameters as they are needed for the autograder.  

<h2>Data</h2>

You are provided with the following csv files in this assignment, make sure to upload them to Google Colab before you begin.

* **crowdworker_survey.csv** -- This file contains almost-clean data collected from a [survey](assignments/downloads/CrowdWorkers_Survey.pdf) taken by crowd workers. For more details, you can check out this [paper](http://www.cis.upenn.edu/~ccb/publications/crowd-workers-demographics.pdf) on how researchers analyze Turker demographics and earnings.

* **clustered\_hourly\_wage.csv** -- This contains hourly wage information for each worker.

* **crowd_tasks.csv** -- This is a random sample of 25,000 tasks from the pool of tasks our survey respondents completed.

<h2>Deliverables</h2>

Please make sure to submit both the **homework8.ipynb** and **homework8.py** files to Gradescope. We will be manually grading all the plots so double-check that they are saved with your notebook.

You can work in pairs, and each pair only needs to submit one ipython notebook. No report is required.

<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Grading Rubric</h4>
</div>
<div class="panel-body" markdown="1">

This extra credit assignment can add up to 3% of you overall course grade. For example, if your final grade is 87%, completing this assignment (and get everything right) can bump up your grade to 90%.
