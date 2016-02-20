---
layout: default
img: academic-paper
caption: Science used to use ballpoint pens and it was printed on paper 
title: Homework 6 "Replicate Science"
active_tab: homework
release_date: 2016-02-12
due_date: 2016-02-26T14:00:00EST

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
This assignment is due before class on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

Replicate Science<span class="text-muted"> : Assignment 6</span> 
=============================================================
One of the awesome things about crowdsourcing is that it lets us quickly run scientific experiments.  You're going to practice doing this by reading an academic paper that uses crowdsourcing and trying to replicate its findings.  Good science should be repeatable, so you're helping science by replicating someone else's experiments.  And it's good for your own understanding of crowdsourcing and academic research.  Did you know that your professors secretly spend most of their time doing research?  It's true.  If you think that their lectures sometimes seem underprepared, it's likely because they're in their lab, bringing down lightening from the Gods and cackling like Dr. Frankenstein until their calendar app reminds them to go to the lecture hall.

For this assignment, you can work in teams of 3-4 people.  Your final project will require that you work in groups, so this is a good chance for you to form a group and test out whether you want to work with those people.

You have five options for academic papers that you can replicate:

* [Demographics of Mechanical Turk](readings/downloads/platform/demographics-of-mturk.pdf) by Panos Ipeirotis
* [Exploring Iterative and Parallel Human Computation Processes](readings/downloads/programming/iterative-and-parallel-processing-in-hcomp.pdf) by Greg Little, Lydia B. Chilton, Max Goldman, and Robert C. Miller
* [Labeling Images with a Computer Game](readings/downloads/gwap/ESP.pdf) by Luis von Ahn and Laura Dabbish 
* [Financial Incentives and the Performance of Crowds](readings/downloads/econ/financial-incentives-and-the-performance-of-crowds.pdf) by Winter Mason and Duncan Watts
* [Crowds in Two Seconds: Enabling Realtime Crowd-Powered Interfaces](readings/downloads/hci/adrenaline.pdf) by Michael Bernstein, Joel Brandt, Rob Miller, and David Karger

I have sorted the papers roughly in an order of how difficult they will be to replicate.  Because the difficulty level varies, and because I don't want to read 50 demographic studies of Mechanical Turk, I'm going to award different maximum point values to them based on their difficulties.  You can choose whichever one you want to work on.

* Demographics of Mechanical Turk -- 3 points maximum (4 points max if you run the demographic survey on both MTurk and CrowdFlower and contrast the two)
* Exploring Iterative and Parallel Human Computation Processes -- 5 points maximum
* Labeling Images with a Computer Game -- 5 points maximum 
* Financial Incentives and the Performance of Crowds -- 6 points maximum
* Crowds in Two Seconds: Enabling Realtime Crowd-Powered Interfaces -- 7 points maximum 

Here are the steps and deliverables for this project:

1. Read at least 3 of the academic papers and write a brief summary of each of them.
2. Pick one paper, and write an in-depth summary of its experimental methodology and its findings.
3. Re-create one or more experiments from the paper.  For this step, it's fine to deviate somewhat from the paper's design.  For instance, you can use a different crowdsourcing platform, or a different set of images to collect labels for.  
4. Create a task on CrowdFlower or Mechanical Turk or another crowdsourcing platform, and perform the experiment.  You will submit your task templates, along with any code and other materials that you used.

5. Collect responses from crowd
6. Analyze your findings and say how they are different from the findings in the original paper.
7. Write a report and submit your final materials. 

### 1. Literature review

You should begin this project by reading through 3 of the academic papers.  The goals of this step are for you to get a sense of what constitutes interesting research on crowdsourcing, and for you to see how academic papers describe their experimental designs and how they present their results.  While you are reading the papers, you should try to  estimate of how long it will take you to replicate one or more of the experiments that were presented in the paper.  

After you've read the papers, you should write a 1-2 paragraph summary of what they were about and what their main findings were.  The summary of the paper should be written in your own words, and not copied and pasted from the paper itself.

### 2. Understand the paper's experimental design

Your team should meet and come to a consensus about which paper that you want will reproduce.  You should pick a paper that you find to be interesting, and that you will be able to re-create in less than two weeks. It is not necessary to recreate every finding in a paper, it's fine to pick one or more of the experiments.  

For this part of the homework assignment, you should write a complete description of the experimental methodology described in the paper, and what its findings were.  For the experimental methodology you should: 
1. List the experiments that were run
2. For each experiment, describe the materials that they used (like survey questions, images shown to users, or prompts for user feedback)
3. Describe the crowd: How did the paper's authors recruit experimental subjects?  How many people participated in the experiment?  How much were they paid?
4. For each experiment, summarize the results.   Describe how the authors presented those results: Where they summarized in a table, where they qualitatively analyzed?

Write up the experimental methodology in your final report. Once again, you should use your own words.  If you want to reproduce a figure or a table from the paper, that is fine, so long as you attribute it. 

### 3. Plan your experiment

Pick one or more of the experiments that you want to replicate. If the paper described a set of experiments, then you can pick one of them.  For instance, [Financial Incentives and the Performance of Crowds](readings/downloads/econ/financial-incentives-and-the-performance-of-crowds.pdf) performs two studies -- one where they have workers organize traffic cam photos chronologically and another where they have workers perform word puzzles.   Similarly, [Exploring Iterative and Parallel Human Computation Processes](readings/downloads/programming/iterative-and-parallel-processing-in-hcomp.pdf)  had 3 studies, one involving writing image descriptions, one on brainstorming, and one blurry image recognition.   If you are reproducing either of those papers, you only need to pick one of those studies. 

When you create your own version of the paper's experiment, it's fine to deviate somewhat from the paper's design.  For instance, you could use CrowdFlower even if the original paper used Mechanical turk.  Or if the crowd was shown a particular set of images and asked to write captions or label the images, it might not be possible for you to get exactly the same set of images.  It's fine to choose your own.  When you deviate from the setup of the original experiment, you should note why.  You should also briefly explain if you think it might result in a different outcome than the findings of the original paper. 

In this step, you should collect any materials that you'll be presenting to workers (images, prompts, survey questions, etc).  You should save these in a directory and write a README describing them.  You'll submit them along with your final writeup.

### 4. Use a crowdsourcing platform to set up your experiment

Create a task on CrowdFlower or Mechanical Turk or another crowdsourcing platform that you'll use to perform the experiment.  You should write clear instructions on what you'd like the workers to do (and how they will be rewarded, if that's relevant to the experiment).

Please save your instructions, and take a screenshot of your task design, and/or submit an HTML template for it.  If you write any code with it (like for a Javascript alert for the [Crowds in Two Seconds](readings/downloads/hci/adrenaline.pdf)), then also include that code and a README describing what it does.

### 5. Collect responses from crowd

Decide on an appropriate reward amount, and an appropriate number of crowd workers that you need to hire to complete your experiment, and then run it.  You may consider starting with a small-scale pilot version of your experiment to make sure that everything is working properly, and that your instructions are written clearly enough for workers to understand.

In your final write up on your experiment, you should describe how many workers you hired, and how  much you paid them.
If you placed restrictions on who can participate (based on their country or their past approval rate, etc), then document that too.
If you had to remove any workers for giving spammy results, describe what criteria you used to select whom to exclude from your experiment.

### 6. Analyze your findings

Analyze the results of your experiment.  Try to perform the same analysis that the original paper did.  You should also present your results in a similar format (for instance, a similar style of graph).  Are your high-level findings the same as the original paper or different?  If they are different, how so? What do you attribute the differences to?


### 7. Final write-up

Write a final report.  Your final report should be written in markdown format (there's a good tutorial for markdown [here](http://markdowntutorial.com/)), and should be approximately 3,500 words long (~5 pages).  The maximum length is 3,750 words.  If you need more than that, you're welcome to submit a supplemental materials document containing additional figures or analysis, but your main document should be constructed so that it is readable as a standalone report.  

Your paper should include the following information:

* A literature review section
* A description of which paper you chose to replicate
* An in-depth explanation of that paper's experimental design, including all of its experiments
* If you choose one specific experiment from the paper, explain which one you picked and why
* A description of your experimental setup, along with an explanation of any  deviations that you made from the original design
* A description of what crowdsourcing platform you used, a description of the selection criteria you used for workers, how much you paid, and how you decided to reject workers (if applicable).  You should also give a pointer to your task design, which can be in a separate document. 
* An analysis of your results, and a comparison to the findings of the original paper.

You will submit your final report and your other materials via turnin, and you will need to answer a few questions on [this questionnaire](). 

Like before, please turn in your files using turnin: 

<code>$ turnin -c nets213 -p replicate-science -v</code>

Note that turnin only keeps the most recent work that you have sent it, so if you are submitting supplementary documents, they need to be in a directory with your primary report. 

<div class="panel panel-danger" id="rubric">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 5 points of your overall grade in the course.  The rubric for the writeup is given below.

* 1 point - literature review
* 1 point - detailed description of one paper's experimental design and results
* 1 point - a description of your experimental setup, including descriptions of any deviations you made
* 1 point - for successfully executing the experiment on a crowdsourcing platform, and describing how you used the platform
* 1 point - for analyzing your results and comparing them to the original paper
* Extra credit: up to two points extra credit for choosing a more challenging paper
* Point caps: if you replicate the Demographics of Mechanical Turk paper, you point total will be capped at 3 points maximum if you run a demographic survey on one platform, or 4 points maximum if you run the demographic survey on both MTurk and CrowdFlower and contrast the two.
</div>
</div>
