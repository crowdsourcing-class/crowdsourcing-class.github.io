---
layout: default
img: launching-a-start-up
caption: Crowdsource your startup!
title: Homework 2 "Market Research"
active_tab: homework
release_date: 2016-01-22
due_date: 2016-01-29
deliverables:
    -
      description: written survey
      due_date: 2016-01-29
    -
      description: video 
      due_date: 2016-01-29
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
The {{deliverable.description}} is due before class on {{ deliverable.due_date | date: "%A, %B %-d, %Y" }}.  
{% endfor %}
{% endif %}
</div>


Market Research <span class="text-muted">: Assignment 2</span> 
=============================================================
This week we will be looking at the wealth of companies that use crowdsourcing as part of their business. Here’s a list of companies that you could research:
[538](http://fivethirtyeight.com),
[99Designs](http://99designs.com),
[airbnb](https://www.airbnb.com),
[Amazon reviews/product recommendations](https://www.amazon.com),
[Apple HealthKit/ResearchKit](http://www.apple.com/researchkit/),
[benefunder](http://www.benefunder.org),
[Book Country](http://www.bookcountry.com),
[Buy Amazon Reviews](http://www.buyamazonreviews.com),
[change.org](https://www.change.org),
[CloudFactory](http://www.cloudfactory.com/home),
[Couchsurfing](https://www.couchsurfing.org/),
[coursera](https://www.coursera.org),
[Crowdee](https://www.crowdee.de),
[CrowdFlower](http://www.crowdflower.com),
[CrowdMed](https://www.crowdmed.com),
[Crowds On Demand](http://crowdsondemand.com),
[The Doe Network](http://www.onthemedia.org/story/online-supersleuth/),
[Duolingo](https://www.duolingo.com/),
[EatWith](http://www.eatwith.com),
[eBay buyer/seller ratings](http://pages.ebay.com/help/feedback/scores-reputation.html),
[edX](https://www.edx.org),
[EyeWire](https://eyewire.org/signup),
[Facewatch](http://arstechnica.com/tech-policy/2015/12/pre-crime-arrives-in-the-uk-better-make-sure-your-face-stays-off-the-crowdsourced-watch-list/),
[Field Agent](http://www.fieldagent.net),
[Flattr](https://flattr.com),
[Foursquare](https://foursquare.com),
[Freebase](http://www.freebase.com),
[Freelancer](https://www.freelancer.com/),
[Go Fund Me](https://www.gofundme.com/),
[Google Map Maker](http://appleinsider.com/articles/15/08/25/google-reopens-map-maker-with-new-safeguards-to-block-controversial-edits),
[Global Voices](http://globalvoicesonline.org),
[Iceland’s Crowdsourced Constitution](http://www.slate.com/articles/technology/future_tense/2014/07/five_lessons_from_iceland_s_failed_crowdsourced_constitution_experiment.html),
[Idibon](http://idibon.com),
[IndieGoGo](https://www.indiegogo.com),
[Innocentive](http://www.innocentive.com),
[Instacart](https://www.instacart.com/faq),
[Invisible Boyfriend](https://invisibleboyfriend.com),
[iStockPhoto](http://en.wikipedia.org/wiki/IStock),
[Intrade](http://en.wikipedia.org/wiki/Intrade),
[Iowa Election Markets](http://tippie.uiowa.edu/iem/),
[Kaggle](http://www.kaggle.com),
[Kickstarter](http://www.kickstarter.com),
[Kiva](http://kiva.org),
[leadGenius](https://leadgenius.com),
[Lending Club](https://www.lendingclub.com/public/how-peer-lending-works.action),
[Lyft](https://www.lyft.com),
[Microworkers](https://microworkers.com),
[Microsoft Prediction Lab](https://www.prediction.microsoft.com/#!/),
[MTurk List](http://www.mturklist.com),
[Netflix prize](https://en.wikipedia.org/wiki/Netflix_Prize),
[OpenStreetMap](http://www.openstreetmap.org/),
[Orchestra](http://orchestra.unlimitedlabs.com),
[Parchment](http://www.parchment.com),
[PatientsLikeMe](http://www.patientslikeme.com),
[Postmates](https://postmates.com),
[PredictWise](http://www.predictwise.com/),
[Premise](http://www.premise.com/),
[PublicStuff](https://www.publicstuff.com),
[Quirky](http://quirky.com),
[Quora](http://www.quora.com),
[Qualtrics](http://www.qualtrics.com/),
[Rotten Tomatoes](http://www.rottentomatoes.com),
[Samasource](http://samasource.org),
[Silk Road](http://arstechnica.com/tech-policy/2014/08/dark-net-drug-markets-kept-alive-by-great-customer-service/),
[Stackexchange](http://stackexchange.com/sites),
[Stackoverflow](http://stackoverflow.com),
[Sunshine](http://www.slate.com/blogs/future_tense/2015/03/27/apple_watch_could_make_you_a_walking_weather_station.html),
[SquadRun](https://squadrun.co),
[TaskRabbit](https://www.taskrabbit.com),
[Threadless](https://www.threadless.com/how-it-works/),
[Thumbtack](http://www.thumbtack.com/),
[topcoder](http://www.topcoder.com),
[TurkOpticon](http://turkopticon.ucsd.edu),
[Uber](https://www.uber.com),
[Udacity](https://www.udacity.com),
[Upwork (formerly oDesk)](https://www.upwork.com),
[Ushahidi](http://www.ushahidi.com),
[Waze](https://www.waze.com),
[We the People](https://petitions.whitehouse.gov),
[Wikipedia's AI helper](http://www.wired.com/2015/12/wikipedia-is-using-ai-to-expand-the-ranks-of-human-editors/),
[WorkFusion](http://www.workfusion.com),
[XPRIZE](http://www.xprize.org),
[Yelp](http://www.yelp.com/),
[Zensors](http://zensors.com/).
You are also welcome to profile a [relevant company](http://www.crowdsourcing.org/uploads/CrowdSourcing-Industry-Landscape-v09.jpg) that is not on this list (but please verify your choice beforehand with the instructor). 



This assignment has two deliverables:

1. Answering [a questionnaire](https://docs.google.com/forms/d/1fxe5cwKqM5M2J6NGAsqC30hvNQ0JX4woJV0zOZhRNsU/viewform?usp=send_form) about the company or project that you are researching. This is due before class on {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}.
2. A video presentation about the company.  Several of the best videos will be selected for in-class presentations on Fridays.  Teams whose videos are selected will receive extra credit. his is due before class on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}.

This assignment can be done individually or in pairs.

First, please sign up for a [company or project](https://docs.google.com/spreadsheets/d/1dmTheLr1zzSzF4ci9hWIPNkO7sTHcXV3quwocPKr95o/edit?usp=sharing).  Please do not pick a company that another team has already signed up for.  If there’s a company that you’d like to research that isn’t on the list, you are welcome to ask the instructor or the TA to ask if it is OK.  

You should independently research the company, and then [fill in your answers about it in this questionnaire](https://docs.google.com/forms/d/1fxe5cwKqM5M2J6NGAsqC30hvNQ0JX4woJV0zOZhRNsU/viewform?usp=send_form).  Your short answers to these questions on  {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}.

You will record a short 5 to 7 minute video presentation about your company. Your presentation should address the following questions:

- What incentives does it offer to get people to participate?
- How does it aggregate the information provided by the crowd?
- What are the quality concerns, and how does the company do quality control?
- How does the company benefit from user contributions?
- Are there any controversies about the company?

Your presentation video is due on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}. To turn in your video, please upload it to [Vimeo](https://vimeo.com/). Then give us the link to your video on the survey. Make sure that your video is publicly viewable or that you give us a password to view it on the web form.

If you have managed to make it this far in life without having to sign up for accounts for things on the internet, here are more detailed instructions:





<div class="panel panel-info">
<div class="panel-heading" markdown="1">
#### Instructions for uploading your video to Vimeo
</div>
<div class="panel-body" markdown="1">
1. Go to [Vimeo](https://vimeo.com).
2. Create an account by clicking the enormous blue "JOIN" button. 
3. You will receive and email with a link to verify your account. You have to verify before you can upload videos.
4. Once you are signed in, click "Upload" at the top of the page.
5. Click the "Choose a Video to Upload" button and choose your video
6. Once it is uploading, you can change the privacy settings. If you are soon to be on the job market, be careful. You probably don't want potential employers to know how intelligently and elegantly you are able to analyze and present on the potential market value of technology companies, so maybe don't use your real name.
7. That's it! Fill in the title and tags and what-have-you in the survey to tell us where to find it.
</div>
</div>


<div class="panel panel-primary">
<div class="panel-heading" markdown="1">
#### Survey Questions
</div>
<div class="panel-body" markdown="1">
Below are the questions that you will be asked to answer about the company or project that you are profiling. Please submit your answers via [the questionnaire](https://docs.google.com/forms/d/1fxe5cwKqM5M2J6NGAsqC30hvNQ0JX4woJV0zOZhRNsU/viewform?usp=send_form) 

* What company are you profiling?
* What online resources did you use in researching it?
* Did you use any other resources?
* Did you conduct any interviews, did you try the company’s service?
* Give a one sentence description of the company.
* Give a URL for the company’s website
* Give a URL for the company’s logo
* When was the company started?
* Who were the founders?
* Does it have an interesting origin story?
* What kind of organization is it? 
  -  Publicly traded company
  -  Privately held company
  -  Non-profit organization
  -  Other
* What service does the company provide?
* Does this update a previous service or business model, or is it completely new?
* If it updates something, what does it replace?
* What other new companies provide services that are similar to your company’s?
* What is an example of how someone uses this service?
* What sort of people use the service? 
* If this is a service that you have used, then describe your experience.
* Compare the number of users to contributors.
  -  More users than contributors
  -  More contributors than users
  -  Roughly equal numbers
* Who are the people who contribute services?
* How does the company incentivize them to contribute, or what motivates them to participate?
* Is this a service that was previously provided by experts / professionals?
* Are the contributors experts / professionals?
* How does the company generate revenue?
* How does the company ensure the quality of the services it provides?
* Is its service something that is typically regulated by the government?
* If so, what are the intents of the regulations and does your company meet those standards?
* Is a reputation system used by your company?
* If so, how does it work?
* If the service is provided by many contributors, how are are their contributions aggregated?
* Describe the workflow for how the service is advertised, and how the contributors contribute, and what the users get in the end.
* What is the scale of the services that your company provides, in terms of users?
* What is the scale of the services that your company provides, in terms of dollars?
* If your company were to scale up to 10 or 100 times its current size, how well do you think its business model would work?
* How well would the incentive scheme scale? How about the quality/aggregation model?
* Have there been any controversies about the company or the service that it provides?
* Is there anything else you'd like to say about the company?
</div>
</div>



<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 10 points of your overall grade in the course.  The rubric for the assignment is given below.

* 5 points - answering the survey questions thoughtfully.
* 5 points total for the video
  - 2 point for relevance to the themes of the class
  - 1 point for the narration
  - 1 point for the quality of the audio (we recommend using an external microphone)
  - 1 point for a compelling visual accompaniment  
* Extra credit (up to 2 points) - if your video is selected for presentation in class, you will receive extra credit.
</div>
</div>
 

