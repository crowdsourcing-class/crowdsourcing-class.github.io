---
layout: default
img: python
img_link: http://xkcd.com/353/
caption: Hello world!
title: Homework 3 "Python Bootcamp"
active_tab: homework
release_date: 2021-02-12
due_date: 2021-02-18T23:59:00EST
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



<div class="alert alert-info" markdown="span">
Links to tutorials and other Python resources are posted on the [resources page](resources.html).</div>


Python Bootcamp <span class="text-muted">: Assignment 3</span> 
=============================================================
This week we will start writing some code! This assignment is designed to be a crash-course to get you up to speed on the level of Python you will need to know in order to do the remainder of the assignments. It's easiest to learn by doing, so please start early so we can help you get on board. You want to spend the semester focusing on the crowdsourcing and machine learning, not the indenting and semicoloning. 


## Part 1 (Ungraded): Using Python with Google Colab 

We'll be using Google Colab to write and run our Python programs.  Colab hosts Python Notebooks (also known as Jupyter Notebooks), which are ways combinations of code (Python, naturally) and prose (fancy-pants term for nicely formatted documentation).  They're so good that Nobel-winning economists [use Python Notebooks](https://paulromer.net/jupyter-mathematica-and-the-future-of-the-research-paper/).  Colab is awesome because Google lets you use its GPU computers for free (or $10 per month for an upgraded Pro account).  GPUs will be useful for our machine learning experiments later this semester.

For now, you can start learning the basics of [Python Notebooks and Colab via YouTube](https://www.youtube.com/watch?v=yEIc9z-Ad3k).  Better yet, try out this [Colab Notebook tutorial on Python](https://colab.research.google.com/github/cs231n/cs231n.github.io/blob/master/python-colab.ipynb) which introduces a lot of Python language concepts. 


## Part 2 (Graded): Write Python Code

For this part of the assignment, we'll ask you to implement several Python functions.  These will be automatically graded via a Gradescope autograder.  You can submit your code multiple times.  The autograder will give you a score, and that's the score that you'll get for this homework assignment.  There are no hidden tests.

(By the way, the point totals may vary from homework to homework, but each assignment is worth the same as each other assignment when we compute your final grade.) 

To being, make a copy of [this Google Colab notebook](https://colab.research.google.com/github/crowdsourcing-class/crowdsourcing-class.github.io/blob/master/assignments/hw3/assignment3.ipynb).  From the `File` menu of Colab, pick `Save a copy in Drive`, and you can start working  on the assignment. For a tutorial on Python notebooks, download [this notebook](assignments/hw3/00_notebook_tutorial.ipynb) and walk through it on Colab.

Detailed instructions are given in the skeleton file. Functions that are required for you to implement are in python format. Some examples are embedded as comments for your reference. 

When you're ready to check your solutions, you can upload your **homework3.py** file to [Gradescope]({{page.submission_link}}):  You can get the python code through the drop-down menu of "File" in the Colab environment.

This homework can also be done in pairs. Only one group member is required to submit the work. Both of you will share the same submission and get the same grading.
