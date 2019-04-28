---
layout: default
img: prototype-3
caption: Final working system
title: Presentation and Final Report 
active_tab: homework
release_date: 2019-04-26
due_date: 2019-05-08T12:00:00EDT
presentations_start: 2019-05-08T12:00:00EDT
presentations_end: 2019-05-08T14:00:00EDT
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


<div class="alert alert-info" markdown="1">
The final project is due on  {{ page.due_date | date: "%A, %B %-d, %Y" }}. Late days *are not* allowed for this assignment.
</div>


Final Project<span class="text-muted"> : The End</span> 
=============================================================

The end is in sight.  This will be the final deliverable for NETS 213.  This assignment will be worth 20% of your final grade.  The goals of the final deliverables are the following:

* Show off what you did and why it is cool
* Demonstrate how it relates to the course and what you learned
* Analyze your results- is it better than similar/existing approaches? What more could be done?

### Final Video

On the day of the final exam, you will each have 7 minutes to wow everyone with your finished product. We will ask you to do so in a 7 minute video. You all have a lot of work to showcase in those 7 minutes, so you keep it crisp and on-point. Your video should:

1. Motivate the problem you are trying to solve or question you are trying to answer, and why crowdsourcing is an especially good fit for solving/answering it.
2. Give a quick background on related problems. Have others tried to solve the same problem? What makes your approach different/better?
3. Demo your solution/product. If you built an app, show it off in all its glory; if you conducted a scientific study, explain your procedure and demo the crowd-facing components.
4. Describe your method/algorithm. Make sure you address the issues of incentives, quality control, and aggregation. Which components you focus on will differ depending on your project, so you don't have to give each one equal weight. Touch on each one, but focus on the part that was the most challenging or required the most creativity.
5. Discuss your results. Convince us that what you did "worked". What is the take-away? 

Some other tips for making your video awesome: 

* Your video should be able to stand alone; someone with no knowledge of the class should be able to watch it and understand what you did and why it was a worthwhile thing to do. This will make it a more rewarding capstone of your work this semester. 
* Every project is different- focus on what makes yours cool/interesting/exciting/impressive. If yours was engineering-heavy, spend the majority of the time on step (3). If yours was more scientific, you should spend the majority of the video on (5). 
* Show, don't just tell. Demos of working apps or figures of analyzed results are gold. Don't just use your voice-over to read words off of a slide. 

### Final Report

Five minutes is short, and we want you do use your video to showcase what is great about what you did. So to make sure you still get credit for all the obligatory parts, and because it is only fitting, we will have you fill out a detailed final report. The questions that we ask you to address will look familiar - its okay to reiterate points you made on past checkpoints, but highlight what about your original plan changed in your final product. 

The questions we will ask you to answer in your final report are , includes questions about these topics:

* What problem you are solving/question you are answering
* How you attempted to solve/answer it
* How did you address each of the following: incentivization, aggregation, QC
* Did you project work? How do you know so? Analyze some results, discuss some positive outcomes of your project.
* What are the biggest challenges you had to deal with? What changed between your original plan and your final product?
* What are some limitations of your product. If yours is an engineering-heavy project, what would you need to overcome in order to scale (cost/incentives/QC...)? If yours was a scientific study, what are some sources of error that may have been introduced by your method. If you results deviate from previous work, why might that be?

Your final report should do a deeper analysis of the individual components of your project.   You should pick **two** of the sections to do a deeper analysis on. For the two deeper analyses, we ask you to create a graph. Which questions you should pick depends on where the balance of your team's effort went.  Some people are building really complex system that require a lot of engineering.  Other people's focus is on analyzing data.  If your focus is on analysis, then you should generate more in-depth graphs. 


### Final Presentations

The final project presentations will be held during the final exam slot on {{ page.presentations_start | date: "%A, %B %-d, %Y" }} from {{ page.presentations_start | date: "%I:%M%p" }} to {{ page.presentations_end | date: "%I:%M%p" }} in Wu and Chen Auditorium (Levine 101)   We will play your videos and have a short amount of time for you to answer questions from the audience. 




<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### Final report
</div>
<div class="panel-body" markdown="1">
Below are the questions that you should address in your final report.  lease submit your answers in a PDF that you submit to Gradescope. 

You must answer the questions in all of the sections below, but you only need to create graphs for 2 sections.

#### Basic project information 

* Name of your project
* Name of your teammates 
* Give a one sentence description of your project. Please use the name of the project in your description.
* Logo for your project. Create a PNG file, save it in your github repo, give its URL. 
* What problem does it solve?
* What similar projects exist? 
* What type of project is it? 
  * Human computation algorithm
  * Social science experiment with the crowd
  * A tool for crowdsourcing
  * A business idea that uses crowdsourcing
  * Other
* What was the main focus of your team's effort
  * Engineering a complex system
  * Conducting an in depth analysis of data
  * Something in between
* How does your project work? Describe each of the steps involved in your project. What parts are done by the crowd, and what parts will be done automatically.
* Provide a link to your final presentation video.  Give the full path to your Vimeo video, and the password, if it is not public. 

#### The Crowd 

* Who are the members of your crowd?
* For your final project, did you simulate the crowd or run a real experiment?
  * Simulated crowd
  * Real crowd
* If the crowd was simulated, how did you collect this set of data?
* If the crowd was simulated, how would you change things to use a real crowd?
* If the crowd was real, how did you recruit participants?
* How many unique participants did you have?

#### Incentives

* What motivation does the crowd have for participating in your project?
  * Pay
  * Altruism
  * Enjoyment
  * Implicit work
  * Reputation
  * Other
* How do you incentivize the crowd to participate? Please write 1-3 paragraphs giving the specifics of how you incentivize the crowd. If your crowd is simulated, then what would you need to do to incentivize a real crowd?
* Did you perform any analysis comparing different incentives?
* If you compared different incentives, what analysis did you perform? If you have a graph analyzing incentives, include a link to a PNG file of the graph here.

####  What the crowd gives you

* What does the crowd provide for you?
* Is this something that could be automated?
* If it could be automated, say how. If it is difficult or impossible to automate, say why.
* Did you train a machine learning component from what the crowd gave you?
* If you trained a machine learning component, describe what you did.
* Did you analyze the quality of the machine learning component? For instance, did you compare its quality against crowd workers using an n-fold cross validation?
* If you have a graph analyzing a machine learning component, include a link to a PNG file of the graph here.
* Did you create a user interface for the crowd workers? Answer yes even if it's something simple like a HTML form on CrowdFlower.
* If yes, please give the URL to a screenshot of the crowd-facing user interface. Save the screenshot as a PNG file, and put it in your github repo. Include the full path to your image (prefix with https://github.com/). You can include multiple screenshots, one per line.
* Describe your crowd-facing user interface. This can be a short caption for the screenshot. Alternately, if you put a lot of effort into the interface design, you can give a longer explanation of what you did.

#### Skills

* Do your crowd workers need specialized skills?
* What sort of skills do they need?
* Do the skills of individual workers vary widely?
* If skills vary widely, what factors cause one person to be better than another?
* Did you analyze the skills of the crowd?
* If you analyzed skills, what analysis did you perform? How did you analyze their skills? What questions did you investigate? Did you look at the quality of their results? Did you analyze the time it took individuals to complete the task? What conclusions did you reach?
* Do you have a graph analyzing skills? If you have a graph analyzing skills, include a link to a PNG file of the graph here.


#### Quality Control

* Is the quality of what the crowd gives you a concern?
* How do you ensure the quality of the crowd provides?
* If quality if a concern, then what did you do for quality control? If it is not a concern, then what about the design of your system obviates the need for explicit QC? This answer should be substantial (several paragraphs long).
* Did you analyze the quality of what you got back? For instance, did you compare the quality of results against a gold standard? Did you compare different QC strategies?
* What analysis did you perform on quality?
* What questions did you investigate? What conclusions did you reach?
* Do you have a graph analyzing quality? If you have a graph analyzing quality, include a link to a PNG file of the graph here.


#### Aggregation

* How do you aggregate the results from the crowd?
* Did you analyze the aggregated results?
* What analysis did you perform on the aggregated results? What questions did you investigate? Did you compare aggregated responses against individual responses? What conclusions did you reach?
* Do you have a graph analyzing the aggregated results? If you have a graph analyzing the aggregated results, include a link to a PNG file of the graph here.
* Did you create a user interface for the end users to see the aggregated results? If yes, please give the URL to a screenshot of the user interface for the end user.
Save the screenshot as a PNG file, and put it in your github repo. Include the full path to your image (prefix with https://github.com/). You can include multiple screenshots, one per line.
* Describe what your end user sees in this interface. This can be a short caption for the screenshot. Alternately, if you put a lot of effort into the interface design, you can give a longer explanation of what you did.


#### Scaling Up

* What is the scale of the problem that you are trying to solve?
* Would your project benefit if you could get contributions from thousands of people?
* If it would benefit from a huge crowd, how would it benefit?
* What challenges would scaling to a large crowd introduce?
* Did you perform an analysis about how to scale up your project? For instance, a cost analysis?
* What analysis did you perform on the scaling up?
* What questions did you investigate? What conclusions did you reach?
* Do you have a graph analyzing scaling? If you have a graph analyzing scaling, include a link to a PNG file of the graph here.


#### Project Analysis

* Did your project work? How do you know? Analyze some results, discuss some positive outcomes of your project.
* Do you have a graph analyzing your project? If you have a graph analyzing your project, include a link to a PNG file of the graph here.
* What were the biggest challenges that you had to deal with?
* Where there major changes between what you originally proposed and your final product?
* If so, what changed between your original plan and your final product?
* What are some limitations of your product? If yours is an engineering-heavy project, what would you need to overcome in order to scale (cost/incentives/QC...)? If yours was a scientific study, what are some sources of error that may have been introduced by your method.
* Did your results deviate from what you would expect from previous work or what you learned in the class?
* If your results deviated, why might that be?

#### Technical Challenges

* Did your project require a substantial technical component? Did it require substantial software engineering? Did you need to learn a new language or API?
* If project required a substantial technical component, describe the largest technical challenge you faced.
* How did you overcome this challenge? What new tools or skills were required? Feel free to nerd out a bit, to help us understand the amount of work that was required. 
* Do you have any screen shots or flow diagrams to illustrate the technical component you described? If so, include a link to a PNG file of the graph here.

#### Other info (optional)
* Is there anything else you'd like to say about your project?
* If you have additional information about your project that didn't fit into the above questions, put it here.

</div>
</div>

<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Grading Rubric</h4>
</div>
<div class="panel-body" markdown="1">

This assignment is worth 20 points of your overall grade in the course.  The rubric for the assignment is given below. 

* 5 points for your video
* 5 points for your final report
* 10 points will be allocated based on a hollistic evaluation of your project (video+report), with special attention to how well you address the major themes of the course.
</div>
</div>

