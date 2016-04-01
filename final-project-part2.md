---
layout: default
img: prototype
caption: Simple prototype (vitruvian man by Brad Ashburn from The Noun Project)
url: http://www.qmed.com/mpmn/medtechpulse/power-20-minute-prototype
title: Final Project Part 2 "Simple Working Prototype"
active_tab: homework
release_date: 2016-03-28
due_date: 2016-04-08T14:00:00EDT
deliverables:
    -
      description: first part
      due_date: 2016-04-02T23:59:00EDT
    -
      description: second part 
      due_date: 2016-04-08T14:00:00EDT
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
{% if page.deliverables %}
This assignment has multiple deliverables.
{% for deliverable in page.deliverables %}
The {{deliverable.description}} is due before {{ deliverable.due_date | date: "%I:%M%p" }} on {{ deliverable.due_date | date: "%A, %B %-d, %Y" }}.  
{% endfor %}
{% endif %}
</div>


Final Project<span class="text-muted"> : Part 2</span> 
=============================================================

This assignment counts as a deliverable toward your final project.  This assignment will be worth 10% of your final grade and divided into two equally weighted parts.  The goal of this assignment is to select and think through your project idea and setup, talk with a member of the teaching staff about your project and create a simple working prototype of your final project.  This will help to ensure that you are on top of all of the pieces of your project, and that you have a clear picture of how they interact.  This will hopefully allow you to divide the project into pieces that each member of your group can work on independently. 

## Deliverable 1 

### Step 1: Select a Project Idea
You should have received or will be receiving your project idea feedback shorlty. Using this select a project idea and start thinking about specific details on implementing it.

### Step 2: Create a version control repository for your team

You will use [github](https://github.com/) to as a version share code across your group. If you have never used github, there is a good getting started guide [here](https://guides.github.com/activities/hello-world/).  While you're at it, why don't you pick up a [CrowdFlower backpack](https://education.github.com/pack)?

### Step 3: Big picture documentation

Your repository <b>must contain a docs/ directory</b>. It must contain the following: 

* <b>Flow diagram</b>: You should outline the major components/stages of your project, and how they depend on eachother. Somewhere you must have a <b>aggregation module</b> and a <b>quality control module</b>. This should be more conceptual than technical. We are less concerned with your choice of Java classes and interfaces, but more with the big picutre. When does the crowd touch the data? What has to happen before that? What will happen after that? What is your criteria for determining that the crowd's answers are "good enough" to move on? There are [online tools](http://www.gliffy.com/) for making flow diagrams that might be worth checking out.

* <b>Screen shots / mockups</b> of some core interfaces that the crowd will see or that the end-users will see. This includes any HITs you plan to use in your project. There are lots of online [mockup tools](http://www.invisionapp.com/) that you can consider using, although [MS Paint](assets/img/mspaint_vista.jpg) is always a solid option as well.

* <b>README.md</b> markdown file explaining the major components of your project. This should follow the schematic you created for your final project flow diagram. It should also indiciate what the high level milestones for each component are. To make sure you understand the complexity of your own project, each component should have a point value between (1-4) outlining the amount of work required to implement that section. A project suitable for this class should have between 15 - 20 points overall. In your Project update meeting the staff will help you redistribute point values.

## Deliverable 2

<h3>Step 1: Gather any materials that you need to start</h3>
Your repository <b>must contain a data/ directory</b>. For now, this should contain the following: 

* <b>Raw data input</b> that your project requires. If your project needs inputs like Tweets about HPV, pictures of celebrities wearing stylings threads, or psycholinguistic stimuli, then spend time gathering a set of these inputs. You don't need the whole dataset, but have enough to be able to get a MVP (Minimal Viable Product) of your idea working. 

Eventually you'll be gathering real data from the crowd.  Before that happens you should create fake data that you can use as input for the initial implementation of your modules. Create a data subsection of your README file that describes the format. Ideally the format will be reusable when you get real data from your workers.  That way you only have to change your input files, and your algorithms can operate as they did before.

* <b>Sample input/output from your QC module</b>. You don't need to have collected all your actual data yet, but you should decide on what the input will look like and what the output will be. You should be able to make a small example file to illustrate how your module works. E.g. if workers are labeling tweets, you can grab 10 tweets and make up labels for three imaginary workers.

* <b>Sample input/output from your aggregation module</b>. Again, you don't need your actual data, but should decide on the input and output format. It is okay if there is some overlap or dependence between these files and the files you give above for the QC module. Just verbosely document in your README and your flow diagram how these modules/data interact. 

<h3>Step 2: Implement a quality control module and an aggregation module</h3>

Your repository <b>must contain a src/ directory</b>. It can be organized however best fits your system's architecture, but it should contain the following implementations. Make sure you state clearly in your README where to find each piece. 

* A simple, working version of <b>your quality control module</b>.  This can be a simple majority vote, a 2nd pass HIT, or whatever.  You should also describe what you'll need to do to improve it for the final version of your project.

* A simple, working version of <b>your aggregation module</b>.  This version can operate on your simulated data.  Say what additional work is needed for the final version of your project. 

* Update your README.md file to include which parts of the code deal with QC / Aggregation etc. and how they work.

<b>Note</b>: These modules need not be hooked into your UI yet, but they should be able to pass through your dummy data and populate useful output data. You will explain in your project meeting how the values will be interpreted. Yes, we know, every group will have a very valid reason why their project doesn't <i>have</i> a QC and/or aggregation module, per se. In truth, you probably do. (If your project isn't aggregating at some point and doing QC at some point, you need to take a big step back and think about whether what you proposed is a good fit for this class.) Make your best effort to write some code that captures the essence of the aggretation/QC you will need, and we can discuss the problems and limitations in Part 3.

### Step 3 : Sign up for a meeting with Chris, Ellie, or the TAs. 

There is so much variety in the kinds of projects you have come up with, which is *awesome*. Inevitably, this means you will read through this assignment and the deliverables and start complaining among your group in utter frustration about how terribly these deliverables fit with the project you are planning on building. So don't rant amongst yourselves! Come meet with us! Your project probably fits the structure better than you think it does. You must [sign up for a individual meeting with us](https://docs.google.com/spreadsheets/d/1abxlZeSZjEeOMio91Kj2-8PcPngLxlvp7ppr3ne7r10/edit?usp=sharing). 

You should <b>plan to spend the first 5-7 minutes of your meeting presenting your project.</b> You should start by describing the end goal of your project (e.g. be "sales pitchy"-- what are you doing and why is it worthwhile?), and then walking through the deliverabes and giving a bird's eye view of what you have done, and what remains to do. The rest of your meeting, the Prof/TA will ask you questions about the details of your planned schedule and implementation. You should <b>not</b> treat this as an getting-to-know-you meeting. You don't need to have a working demo, but you should have a solid handle on how you plan to proceed and be prepared to discuss the project concretely and technically. 

### Checklist

This was a lot of text. Your take-away check list is: 

<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Deliverables</h4>
</div>
<div class="panel-body" markdown="1">

* Deliverable 1:

	* Flow diagram of major system components
	* Mockups of any user-facing interfaces (crowdworkers and end-users)
	* README.md with required content

* Deliverable 2: 

	* Raw data
	* Sample input/output for QC
	* Sample input/output for aggregation
	* Code for QC
	* Code for aggregation 
	* A disgustingly clear README telling us where we can find each of the above things
	* Sign up for a project update meeting
</div></div>

This first part of this assignment is due before {{ page.deliverables[0].due_date | date: "%I:%M%p" }}  on {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}. Second part of this assignment is due before {{ page.deliverables[1].due_date | date: "%I:%M%p" }} on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}. You must work in groups on this project.  You must work in groups on this project.  You must declare who is in your group when you turn your assignment.  Everyone in your group will receive the same grade on the assignment. 
