---
layout: default
img: prototype
caption: Simple prototype (vitruvian man by Brad Ashburn from The Noun Project)
url: http://www.qmed.com/mpmn/medtechpulse/power-20-minute-prototype
title: Final Project | Simple Working Prototype
active_tab: homework
---


<div class="alert alert-info">
  This assignment is due before 11:59pm on Thursday, November 13th.  You must work in groups on this project.  </div>


Final Project<span class="text-muted"> : Part 2</span> 
=============================================================

This week's assignment counts as a deliverable toward your final project.  This assignment will be worth 10% of your final grade.  The goal of this assignment is to create a simple working prototype of your final project.  This will help to ensure that you are on top of all of the pieces of your project, and that you have a clear picture of how they interact.  This will hopefully allow you to divide the project into pieces that each member of your group can work on independently. 

###Step 1: Create a version control repository for your team

You will use [github](https://github.com/) to as a version share code across your group. If you have never used github, there is a good getting started guide [here](https://guides.github.com/activities/hello-world/).  While you're at it, why don't you pick up a [CrowdFlower backpack](https://education.github.com/pack)?

###Step 2: Big picture documentation

Your repository <b>must contain a docs/ directory</b>. It must contain the following: 

* <b>README file</b> explaining the directory structure of your repository and what each script does. Don't worry about insulting our intelligence; even if your names are blaringly obvious, tell us anyway. "The run-quality-control.py script runs our quality control algorithm." Talk to us like we are illiterate babies.

* <b>Flow diagram</b>: You should outline the major components/stages of your project, and how they depend on eachother. Somewhere you must have a <b>aggregation module</b> and a <b>quality control module</b>. This should be more conceptual than technical. We are less concerned with your choice of Java classes and interfaces, but more with the big picutre. When does the crowd touch the data? What has to happen before that? What will happen after that? What is your criteria for determining that the crowd's answers are "good enough" to move on? There are [online tools](http://www.gliffy.com/) for making flow diagrams that might be worth checking out.

* <b>Screen shots / mockups</b> of all interfaces that the crowd will see or that the end-users will see. This includes any HITs you plan to use in your project. There are lots of online [mockup tools](http://www.invisionapp.com/) that you can consider using, although [MS Paint](assets/img/mspaint_vista.jpg) is always a solid option as well.

###Step 3: Gather any materials that you need to start
Your repository <b>must contain a data/ directory</b>. For now, this should contain the following: 

* <b>Raw data input</b> that your project requires. If your project needs inputs like Tweets about HPV, pictures of celebrities wearing stylings threads, or psycholinguistic stimuli, then spend time gathering a set of these inputs. 

Eventually you'll be gathering real data from the crowd.  Before that happens you should create fake data that you can use as input for the initial implementation of your modules. Create a data subsection of your README file that describes the format. Ideally the format will be reusable when you get real data from your workers.  That way you only have to change your input files, and your algorithms can operate as they did before.

* <b>Sample input/output from your QC module</b>. You don't need to have collected all your actual data yet, but you should decide on what the input will look like and what the output will be. You should be able to make a small example file to illustrate how your module works. E.g. if workers are labeling tweets, you can grab 10 tweets and make up labels for three imaginary workers.

* <b>Sample input/output from your aggregation module</b>. Again, you don't need your actual data, but should decide on the input and output format. It is okay if there is some overlap or dependence between these files and the files you give above for the QC module. Just verbosely document in your README and your flow diagram how these modules/data interact. 

###Step 4: Implement a quality control module and an aggregation module

Your repository <b>must contain a src/ directory</b>. It can be organized however best fits your system's architecture, but it should contain the following implementations. Make sure you state clearly in your README where to find each piece. 

* A simple, working version of <b>your quality control module</b>.  This can be a simple majority vote, a 2nd pass HIT, or whatever.  You should also describe what you'll need to do to improve it for the final version of your project.

* A simple, working version of <b>your aggregation module</b>.  This version can operate on your simulated data.  Say what additional work is needed for the final version of your project. 


###Step 5: Answer another questionnaire 

What the hell is up with all of these questionnaires?  [Blame Francis Galton](http://en.wikipedia.org/wiki/Francis_Galton#The_questionnaire).  He also invented Vimeo.

You will be asked to provide similar information to in the brainstorming session, but the focus will be on concreteness. No vague statements like "we will choose the best answer" or "users will answer questions about X". Say exactly <i>how</i> you will determine the best answer and <i>which</i> questions they will answer. You can and should provide links to files in your github repository as necessary. 

You should <b>submit your answers to the questions on [the simple prototype questionnaire](https://docs.google.com/forms/d/1ac9KHIZjyvngeOqa-hQegaV2NXYojEuPKFvAHFr76c8/viewform?usp=send_form).</b>

###Step 6 (optional): Sign up for a meeting with Chris and Ellie. 

There is so much variety in the kinds of projects you have come up with, which is *awesome*. Inevitably, this means you will read through this assignment and the deliverables and start complaining among your group in utter frustration about how terribly these deliverables fit with the project you are planning on building. So don't rant amongst yourselves! Come meet with us! Your project probably fits the structure better than you think it does. You can sign up for a individual meeting with use [here](https://docs.google.com/spreadsheets/d/1w0fl8caGH46590cx7qnaLHS1GHh1toBJXh8tuh5y-fQ/edit?usp=sharing).

###Deliverables

This was a lot of text. Your take-away check list is: 

* Flow diagram of major system components

* Mockups of any user-facing interfaces (crowdworkers and end-users)

* Raw data

* Sample input/output for QC

* Sample input/output for aggregation

* Code for QC

* Code for aggregation 

* A disgustingly clear README telling us where we can find each of the above things

* Questionnaire

This assignment is due by 11:59pm on <b>Thursday, November 13th</b>.  You must work in groups on this project.  You must declare who is in your group when you turn your assignment.  Everyone in your group will receive the same grade on the assignment. 
