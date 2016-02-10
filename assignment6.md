---
layout: default
img: bookreport
caption:
title: Homework 6 "Reimplement an Academic Paper"
active_tab: homework
active_tab: homework
release_date: 2016-02-12
due_date: 2016-02-19T14:00:00EST

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
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

Reimplement an Academic Paper<span class="text-muted"> : Assignment 6</span> 
=============================================================
For this week's assignment, you will read an academic paper about crowdsourcing and then replicate its findings. You can either work as a team of up to 3 people to re-create the findings.

You have 4 options for academic papers that you can re-create:
* [The Demographics of MTurk](readings/downloads/platform/demographics-of-mturk.pdf) by Panos Ipeirotis
* [Exploring Iterative and Parallel Human Computation Processes](readings/downloads/programming/iterative-and-parallel-processing-in-hcomp.pdf) by Greg Little, Lydia B. Chilton, Max Goldman, and Robert C. Miller
* [Labeling Images with a Computer Game](readings/downloads/gwap/ESP.pdf) by Luis von Ahn and Laura Dabbish 
* [Financial Incentives and the Performance of Crowds](readings/downloads/econ/financial-incentives-and-the-performance-of-crowds.pdf) by Winter Mason and Duncan Watts
* [Crowds in Two Seconds: Enabling Realtime Crowd-Powered Interfaces](readings/downloads/hci/adrenaline.pdf) by Michael Bernstein, Joel Brandt, Rob Miller, and David Karger

