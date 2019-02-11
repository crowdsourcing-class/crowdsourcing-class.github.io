---
layout: default
img: ML
caption: Crowdsourcing FTW!
title: Homework 4 "Training a classifier"
active_tab: homework
release_date: 2019-02-12
due_date: 2019-02-19T23:59:00EST
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
This assignment is before {{ page.due_date | date: "%I:%M%p" }}  due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>


Training a classifier<span class="text-muted">: Assignment 4</span> 
=============================================================
Deep learning is transforming the world, and the point of this assignment is to demonstrate that _**you**_ can do deep learning!

The [fast.ai](https://www.fast.ai/) community is making deep learning easier to use and [getting more people from all backgrounds involved](https://www.youtube.com/watch?v=LqjP7O9SxOM&list=PLtmWHNX-gukLQlMvtRJ19s7-8MrnRV6h6) through free online classes like [“Practical Deep Learning for Coders 2019”](https://www.fast.ai/2019/01/24/course-v3/), which was launched at the end of January and covers cutting-edge results in an introductory class.

For example, after following along with the [first lesson](https://course.fast.ai/videos/?lesson=1) for this assignment, you’ll have trained an image classifier that can recognize 12 cat breeds and 25 dog breeds at a state-of-the-art accuracy of around 94%, compared to 59% in 2012!

And next week, we will explore [shortcomings with current image classification approaches](https://www.fast.ai/2019/01/29/five-scary-things/#bias) and how crowdsourcing can help.

![Breeds](https://raw.githubusercontent.com/hiromis/notes/master/lesson1/8.png)

<div class="panel panel-info">
<div class="panel-heading" markdown="1">
#### Detailed Instructions
</div>
<div class="panel-body" markdown="1">
1. [Read the Getting Started section](https://course.fast.ai/#getting-started), which describes the need to access a NVIDIA GPU (Graphics Processing Unit). Thankfully, Google Colab freely provides the use of a NVIDIA K80 GPU for up to 12 hours at a time!
2. [Follow the Colab Setup](https://course.fast.ai/start_colab.html), opening the notebook called "nbs/dl1/lesson1-pets.ipynb". Make sure to change your runtime type to GPU and save a copy of the notebook in your Google Drive, as instructed!
3. [Watch Lesson 1 on image classification](https://course.fast.ai/videos/?lesson=1), following along in your copy of the notebook - it's fun, and you'll learn more!
4. [Answer the following Homework 4 questions on Gradescope]({{page.submission_link}}), where a link to your Colab notebook with all the outputs shown is required.
</div>
</div>


<div class="panel panel-primary" id="questions">
<div class="panel-heading" markdown="1">
#### Questions
</div>
<div class="panel-body" markdown="1">

Below are the questions that you will be asked to answer about this assignment. Please turn in your answers for [Homework 4 on Gradescope]({{page.submission_link}}).

It is a good idea to write your answers in a file on you own computer, instead of typing them directly into Gradescope, so that you'll have a copy after you press the submit button. 

1. What is the link to your Colab notebook?
2. What are two places that you often get data from, and why are they each important?
3. What is “fine-grained classification”, and why is it difficult?
4. What are “labels”, and how do you get them in this dataset?
5. Why shouldn’t images in a dataset have different shapes and sizes?
6. What does it mean to “normalize” images?
7. What is “transfer learning”, and why is it helpful?
8. What is “overfitting”, and how do you try to avoid it?
9. Describe two ways to interpret your model’s performance.
10. Describe the connection between “unfreezing”, “fine-tuning”, and “learning rates”.
</div>
</div>
