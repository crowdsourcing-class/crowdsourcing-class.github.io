---
layout: default
img: prototype-3
caption: Final working system
title: Final Project 
active_tab: homework
release_date: 2017-04-11
due_date: 2016-05-05T09:00:00EDT
presentations_start: 2016-05-05T09:00:00EDT
presentations_end: 2016-05-05T011:00:00EDT
questionnaire: https://docs.google.com/forms/d/15pK4Gw_GM8wyUWyzwMG9-UkCevGPK175VXjTNSyJ65M/viewform
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
The final project is due on  {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>


Final Project<span class="text-muted"> : Part 4</span> 
=============================================================

The end is in sight.  This will be the final deliverable for NETS 213.  This assignment will be worth 20% of your final grade.  The goals of the final deliverables are the following:

* Show off what you did and why it is cool
* Demonstrate how it relates to the course and what you learned
* Analyze your results- is it better than similar/existing approaches? What more could be done?

### Final Video

On the day of the final exam, you will each have 5 minutes to wow everyone with your finished product. And, being a recurring theme of the course, we will ask you to do so in a 5 minute video. You all have a lot of work to showcase in those 5 minutes, so you keep it crisp and on-point. Your video should:

1. Motivate the problem you are trying to solve or question you are trying to answer, and why crowdsourcing is an especially good fit for solving/answering it.
2. Give a quick background on related problems. Have others tried to solve the same problem? What makes your approach different/better?
3. Demo your solution/product. If you built an app, show it off in all its glory; if you conducted a scientific study, explain your procedure and demo the crowd-facing components.
4. Describe your method/algorithm. Make sure you address the issues of incentives, quality control, and aggregation. Which components you focus on will differ depending on your project, so you don't have to give each one equal weight. Touch on each one, but focus on the part that was the most challenging or required the most creativity.
5. Discuss your results. Convince us that what you did "worked". What is the take-away? 

Some other tips for making your video awesome: 

* Your video should be able to stand alone; someone with no knowledge of the class should be able to watch it and understand what you did and why it was a worthwhile thing to do. This will make it a more rewarding capstone of your work this semester. 
* Every project is different- focus on what makes yours cool/interesting/exciting/impressive. If yours was engineering-heavy, spend the majority of the time on step (3). If yours was more scientific, you should spend the majority of the video on (5). 
* Show, don't just tell. Demos of working apps or figures of analyzed results are gold. Don't just use your voice-over to read words off of a slide. 

### Final Questionnaire

Five minutes is short, and we want you do use your video to showcase what is great about what you did. So to make sure you still get credit for all the obligatory parts, and because it is only fitting, we will have you fill out [a detailed final questionnaire]({{page.questionnaire}}). The questions will look familiar - its okay to reiterate points you made on past checkpoints, but highlight what about your original plan changed in your final product. 

The questions we will ask, includes questions about these topics:

* What problem you are solving/question you are answering
* How you attempted to solve/answer it
* How did you address each of the following: incentivization, aggregation, QC
* Did you project work? How do you know so? Analyze some results, discuss some positive outcomes of your project.
* What are the biggest challenges you had to deal with? What changed between your original plan and your final product?
* What are some limitations of your product. If yours is an engineering-heavy project, what would you need to overcome in order to scale (cost/incentives/QC...)? If yours was a scientific study, what are some sources of error that may have been introduced by your method. If you results deviate from previous work, why might that be?

The questionnaire has questions asking you to do a deeper analysis of the individual components of your project. You should pick some number of these, and do an analysis. For each of the analysis questions, we ask you to create a graph using [your Google graph skills](assignment9.html). The number of questions you should pick depends on where the balance of your team's effort went.  Some people are building really complex system that require a lot of engineering.  Other people's focus is on analyzing data.  If your focus is on analysis, then you should generate more graphs. 


### Your code

Make sure all of your code is in your github repository. You will need to provide a link to your repository, as well as to specific files, in the questionnaire. Your repository <b>must contain a docs/ directory</b> with the following:

1. <b>README file</b> explaining the directory structure of your repository and what each script does. Be obscenely verbose and clear about where everything is and what it does. If we can't find the code you are talking about, we cannot grade it accurately (or at all). 
2. <b>Flow diagram</b>: You should update the flow diagram from your previous submission to outline the major components/stages of your final product, and how they depend on each other. This should contain somewhere an aggregation module and a quality control module. 
3. <b>Screenshots/figures</b> You should include a short written "demo" of your project in PDF format. For the engineering-heavy projects, this can be simply a walk-through of all of the use-cases of your app. If yours is a more scientific study, your PDB should include your figures and analyses of your results. Your full written discussion will be in the questionnaire, but your PDF writeup is meant to keep all of your visual aides (screenshots, tables, charts, etc.) in one place. Your figures should be clearly labeled and captioned. You can and should point to these figures in your responses in the questionnaire.


### Final Presentations

The final project presentations will be held on {{ page.presentations_start | date: "%A, %B %-d, %Y" }} from {{ page.presentations_start | date: "%I:%M%p" }} to {{ page.presentations_end | date: "%I:%M%p" }} in two locations: in LRSM Auditorium and in Skirkanich Auditorium (Berger Auditorium room 101).  We will play your videos and have a short amount of time for you to answer questions from the audience. 




<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### Questionnaire
</div>
<div class="panel-body" markdown="1">
Below are the questions that you will be asked to answer about your final project.  lease submit your answers via [the questionnaire]({{page.questionnaire}}). We recommend that you **save your survey answers in a file on your own computer**, rather than typing them directly into the Google form, so that you can have a copy to use when you do your video profile.  You won't be able to access your answers from Google after you press submit.

#### Basic project information 

* Name of your project
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
* URL to the flow diagram for your project. Create a PNG file, and save it in your github repo. Include the full path to your diagram here (prefix with https://github.com/).
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
* If you compared different incentives, what analysis did you perform? If you have a graph analyzing incentives, include the HTML for a Google graph here.

####  What the crowd gives you

* What does the crowd provide for you?
* Is this something that could be automated?
* If it could be automated, say how. If it is difficult or impossible to automate, say why.
* Did you train a machine learning component from what the crowd gave you?
* If you trained a machine learning component, describe what you did.
* Did you analyze the quality of the machine learning component? For instance, did you compare its quality against crowd workers using an n-fold cross validation?
* If you have a graph analyzing a machine learning component, include the HTML for a Google graph here.
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
* Do you have a Google graph analyzing skills? If you have a graph analyzing skills, include the HTML for a Google graph here.


#### Quality Control

* Is the quality of what the crowd gives you a concern?
* How do you ensure the quality of the crowd provides?
* If quality if a concern, then what did you do for quality control? If it is not a concern, then what about the design of your system obviates the need for explicit QC? This answer should be substantial (several paragraphs long).
* Did you analyze the quality of what you got back? For instance, did you compare the quality of results against a gold standard? Did you compare different QC strategies?
* What analysis did you perform on quality?
* What questions did you investigate? What conclusions did you reach?
* Do you have a Google graph analyzing quality? If you have a graph analyzing quality, include the HTML for a Google graph here.


#### Aggregation

* How do you aggregate the results from the crowd?
* Did you analyze the aggregated results?
* What analysis did you perform on the aggregated results? What questions did you investigate? Did you compare aggregated responses against individual responses? What conclusions did you reach?
* Do you have a Google graph analyzing the aggregated results? If you have a graph analyzing the aggregated results, include the HTML for a Google graph here.
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
* Do you have a Google graph analyzing scaling? If you have a graph analyzing scaling, include the HTML for a Google graph here.


#### Project Analysis

* Did your project work? How do you know? Analyze some results, discuss some positive outcomes of your project.
* Do you have a Google graph analyzing your project? If you have a graph analyzing your project, include the HTML for a Google graph here.
* What were the biggest challenges that you had to deal with?
* Where there major changes between what you originally proposed and your final product?
* If so, what changed between your original plan and your final product?
* What are some limitations of your product? If yours is an engineering-heavy project, what would you need to overcome in order to scale (cost/incentives/QC...)? If yours was a scientific study, what are some sources of error that may have been introduced by your method.
* Did your results deviate from what you would expect from previous work or what you learned in the class?
* If your results deviated, why might that be?


#### Other info (optional)
* Is there anything else you'd like to say about your project?
* If you have additional information about your project that didn't fit into the above questions, put it here.

</div>
</div>
