---
layout: default
img: python
img_link: http://xkcd.com/353/
caption: Hello world!
title: Homework 3 "Python Bootcamp"
active_tab: homework
release_date: 2019-02-05
due_date: 2019-02-12T23:59:00EST
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
This assignment is due before {{ page.due_date | date: "%I:%M%p" }} on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>



<div class="alert alert-info" markdown="span">
Links to tutorials and other Python resources are posted on the [resources page](resources.html).</div>


Python Bootcamp <span class="text-muted">: Assignment 3</span> 
=============================================================
This week we will start writing some code! This assignment is designed to be a crash-course to get you up to speed on the level of Python you will need to know in order to do the remainder of the assignments. It's easiest to learn by doing, so please start early so we can help you get on board. You want to spend the semester focusing on the crowdsourcing and machine learning, not the indenting and semicoloning. 

To start with, download the skeleton file [IPython notebook](assignments/hw3/homework3.ipynb) and upload it to [Google Colab](https://colab.research.google.com). And you can start working from there.

Detailed instructions are given in the skeleton file. Functions that are required for you to implement are in python format. Some examples are embedded as comments for your reference. 

Two deliverables are required for you to upload to Gradescope:
1. IPython notebook **homework3.ipynb** modified with your implementation;
2. The corresponding python **homework3.py** file. 

You can download both files through the drop-down menu of File in the Colab environment.

**Notice:** Please make sure all originally commented examples stay as comments before you make submissions to [Gradescope]({{page.submission_link}}).


<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth is worth approximately 5% of your overall grade in the course. 
</div>
</div>

### Bonus! Bash bootcamp.

Knowing more than one scripting language increases your productivity 1 zillion fold (proven fact). If you breezed through the python bootcamp and are sitting and twiddling your thumbs, try brushing up your bash programming skills by doing the following questions using the [wine.txt](assignments/hw3/wine.txt) file. Many of them can also be done in python. Think about how these operations are conceptually different when you write in bash compared to python. Check out this [cheat sheet](http://crowdsourcing-class.org/bash-commands.html) of bash commands to get you started.

1. How many lines are there in the file?
2. What is the distribution over star ratings?
3. How many reviews contain the word 'a'?
4. How many reviews contain the word 'fruit'?
5. How many reviews contain the word 'mineral'?
6. Make a new file containing the full text of all the reviews, with one word per line. (You don't have to do this in python, but I think that is the easiest way. If you want to try a new command-line tool, check out [sed](http://stackoverflow.com/questions/1853009/replace-all-whitespace-with-a-line-break-paragraph-mark-to-make-a-word-list)). 
7. How many total words appear in your list?
8. How many unique words appear in your list?
9. What are the 10 most common words used across all of the reviews, and how many times is each used?
10. How many times does the word "red" appear? (Be careful of capitalization!)