---
layout: default
img: launching-a-start-up
caption: Crowdsource your startup!
title: Homework 2 "Market Research"
active_tab: homework
release_date: 2016-01-22
due_date: 2016-02-12T14:00:00EST
deliverables:
    -
      description: written survey
      due_date: 2016-01-29T14:00:00EST
    -
      description: video 
      due_date: 2016-02-12T14:00:00EST
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
[CrowdMed](https://www.crowdmed.com),
[Crowds On Demand](http://crowdsondemand.com),
[Daemo](http://hci.stanford.edu/publications/2015/crowdresearch/daemo-uist.pdf),
[Defined Crowd](https://www.definedcrowd.com/en-us/),
[The Doe Network](http://www.onthemedia.org/story/online-supersleuth/),
[Duolingo](https://www.duolingo.com/),
[EatWith](http://www.eatwith.com),
[eBay buyer/seller ratings](http://pages.ebay.com/help/feedback/scores-reputation.html),
[edX](https://www.edx.org),
[EyeWire](https://eyewire.org/signup),
[Facewatch](http://arstechnica.com/tech-policy/2015/12/pre-crime-arrives-in-the-uk-better-make-sure-your-face-stays-off-the-crowdsourced-watch-list/),
[Field Agent](http://www.fieldagent.net),
[Figure Eight](https://www.figure-eight.com),
[Flattr](https://flattr.com),
[Foursquare](https://foursquare.com),
[Freebase](http://www.freebase.com),
[Freelancer](https://www.freelancer.com/),
[Gems](https://gems.org/whitepaper.pdf),
[Go Fund Me](https://www.gofundme.com/),
[Good Judgment Open](https://www.gjopen.com),
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
[Longitude Prize of 1714](http://www.crowdsourcing.com/cs/2008/05/chapter-7-what.html),
[Lyft](https://www.lyft.com),
[Microworkers](https://microworkers.com),
[Microsoft Prediction Lab](https://www.prediction.microsoft.com/#!/),
[MTurk List](http://www.mturklist.com),
[Netflix prize](https://en.wikipedia.org/wiki/Netflix_Prize),
[OpenStreetMap](http://www.openstreetmap.org/),
[Orchestra](http://orchestra.unlimitedlabs.com),
[Parchment](http://www.parchment.com),
[PatientsLikeMe](http://www.patientslikeme.com),
[Phrase Detectives](http://anawiki.essex.ac.uk/phrasedetectives/),
[Postmates](https://postmates.com),
[PredictWise](http://www.predictwise.com/),
[Premise](http://www.premise.com/),
[Prolific Academic](https://prolific.ac/rp?ref=NS6S9E53),
[PublicStuff](https://www.publicstuff.com),
[Quirky](http://quirky.com),
[Quora](http://www.quora.com),
[Qualtrics](http://www.qualtrics.com/),
[Rotten Tomatoes](http://www.rottentomatoes.com),
[Samasource](http://samasource.org),
[scale](https://www.scaleapi.com),
[scistarter](http://scistarter.com),
[Sesame Credit - is this fake?](http://www.independent.co.uk/news/world/asia/china-has-made-obedience-to-the-state-a-game-a6783841.html),
[Silk Road](http://arstechnica.com/tech-policy/2014/08/dark-net-drug-markets-kept-alive-by-great-customer-service/),
[Stackexchange](http://stackexchange.com/sites),
[Stackoverflow](http://stackoverflow.com),
[Sunshine](http://www.slate.com/blogs/future_tense/2015/03/27/apple_watch_could_make_you_a_walking_weather_station.html),
[SquadRun](https://squadrun.com),
[TaskRabbit](https://www.taskrabbit.com),
[Threadless](https://www.threadless.com/how-it-works/),
[Thumbtack](http://www.thumbtack.com/),
[topcoder](http://www.topcoder.com),
[TurkOpticon](http://turkopticon.ucsd.edu),
[TurkPrime](https://www.turkprime.com),
[TurkServer](http://dash.harvard.edu/bitstream/handle/1/11956911/Parkes_TurkServer.pdf?sequence=1),
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
[Zensors](http://zensors.com/),
[Zombi Lingo (French)](http://zombilingo.org).
You are also welcome to profile a [relevant company](http://www.crowdsourcing.org/uploads/CrowdSourcing-Industry-Landscape-v09.jpg) that is not on this list (but please verify your choice beforehand with the instructor). 



This assignment has two deliverables:

1. Answering [a questionnaire](https://docs.google.com/forms/d/1fxe5cwKqM5M2J6NGAsqC30hvNQ0JX4woJV0zOZhRNsU/viewform?usp=send_form) about the company or project that you are researching. This is due before {{ page.deliverables[0].due_date | date: "%I:%M%p" }} on {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}.  If you are working with a partner, only one of you needs to submit the questionnaire. **Please save your survey answers in a file on your own computer**, so that you can have a copy to use when you do your video profile.
2. A video presentation about the company.  Several of the best videos will be selected for in-class presentations on Fridays.  Teams whose videos are selected will receive extra credit. his is due before {{ page.deliverables[1].due_date | date: "%I:%M%p" }}  on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}.  You can submit a link to your video on [this form](https://docs.google.com/forms/d/1y2ObY-Vvgc-_3r8HG8SyTIP5ofA35xxZcwNl1RJf4nc/viewform).

This assignment can be done individually or in pairs.

First, please [sign up for a company or project](https://docs.google.com/spreadsheets/d/1dmTheLr1zzSzF4ci9hWIPNkO7sTHcXV3quwocPKr95o/edit?usp=sharing).  Please do not pick a company that another team has already signed up for.  If there’s a company that you’d like to research that isn’t on the list, you are welcome to ask the instructor or the TA to ask if it is OK.  

You should independently research the company, and then [fill in your answers about it in this questionnaire](https://docs.google.com/forms/d/1fxe5cwKqM5M2J6NGAsqC30hvNQ0JX4woJV0zOZhRNsU/viewform?usp=send_form).  Your short answers to these questions on  {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}.  Remember to save your survey answers on your own computer, so that you can have a copy to use when you do your video profile.


You will record a short 5 to 7 minute video presentation about your company. Your presentation should address the following questions:

- What incentives does it offer to get people to participate?
- How does it aggregate the information provided by the crowd?
- What are the quality concerns, and how does the company do quality control?
- How does the company benefit from user contributions?
- Are there any controversies about the company?

Your presentation video is due on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}. To turn in your video, please upload it to [Vimeo](https://vimeo.com/). Then give us the link to your video [using this form](https://docs.google.com/forms/d/1y2ObY-Vvgc-_3r8HG8SyTIP5ofA35xxZcwNl1RJf4nc/viewform). Make sure that your video is publicly viewable or that you give us a password to view it on the web form.

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


<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### Survey Questions
</div>
<div class="panel-body" markdown="1">
Below are the questions that you will be asked to answer about the company or project that you are profiling. Please submit your answers via [the questionnaire](https://docs.google.com/forms/d/1fxe5cwKqM5M2J6NGAsqC30hvNQ0JX4woJV0zOZhRNsU/viewform?usp=send_form). We recommend that you **save your survey answers in a file on your own computer**, rather than typing them directly into the Google form, so that you can have a copy to use when you do your video profile.  You won't be able to access your answers from Google after you press submit.

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



<div class="panel panel-danger" id="rubric">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

This assignment is worth 10 points of your overall grade in the course.  The rubric for the assignment is given below.

* 5 points - answering the survey questions thoughtfully.
  - 1 point for clearly describing what role crowdsourcing plays in the company or project
  - 1 point for explaining who makes up the crowd, whether they are experts or non-experts, what incentives the company provides to get them to participate
  - 1 point for explaining any quality issues that arise from the use of crowdsourcing and how the company addresses it
  - 1 point for discussing scalability, or controversial issues
  - 1 point for answering all of survey questions
  - Extra credit (up to 1 point) - for an especially entertaining, exciting or otherwise engaging writeup 
  - Extra credit (up to 1 point) - if you conduct an interview with someone who provides the services, or if you make a substantial contribution to the service yourself. 
* 5 points total for the video
  - 2 point for relevance to the themes of the class
  - 1 point for the narration
  - 1 point for the quality of the audio (we recommend using an external microphone)
  - 1 point for a compelling visual accompaniment  
  - Extra credit (up to 2 points) - if your video is selected for presentation in class, you will receive extra credit.
</div>
</div>
 

<div class="panel panel-info" id="faq">
<div class="panel-heading" markdown="1">
#### FAQ
</div>
<div class="panel-body" markdown="1">
* _What is the difference between Users and Contributors?_  Many of you seemed confused about what constitutes a user vs. a contributor. In many crowdsourcing companies, this line is blurry- or nonexistent! Many companies you looked at fit what can be thought of as a "data-mining" model (e.g. Yelp, Foursquare), in which the primary service being provided depends on using data and modeling observed patterns of behavior-- e.g. to target ads or to recommend products. In these cases, the users are the contributors-- everyone who participates provides data, and everyone uses everyone else's data. This is an awesome crowdsourcing model because it is (ideally) self-sustaining and self-incentivizing. The more a person contributes (by providing more data about themselves), the better product they receive (e.g. better recommendations). 
* _How does my company do Aggregation?_ Many of the companies we look at fit into the "match-making" or "marketplace" model (e.g. Uber, Airbnb, Etsy). This is a very common case in which the company is simply working to match supply with demand, where the suppliers (e.g. drivers, in the case of Uber) and the consumers (riders) are distributed all over, and may have trouble finding one another otherwise. Here, rating systems etc. are one piece of the platform that might require aggregating, but arguably the more interesting aggregation problem is how to match a supplier with a consumer. Is this through preference-based recommendation systems (as in the data-mining model discussed above), through location-based matching, through bidding/price? Making these matches is non-trival, but crucial to making the company function.
* _Does this update a previous service or business model, or is it completely new?_ For this question, more than a third of you said "completely new." Try to think broadly when you are considering where these crowdsourcing companies fit into the economy as a whole. (Think Silicon Valley's favorite buzzword: "disruption.") Most of these services being provided are not completely new, but they are directly competing with a service that was traditionally supplied by a brick-and-mortar company in a more centralized manner. Uber competes with taxi companies, Airbnb with hotel chains, Coursera with higher education universities. This is part of what makes crowdsourcing so exciting! 
* _Is getting venture capital funding is a business model?_ No. Smart investors don't invest in a company who says their plan for generating revenue is to "get money from investors." When in doubt about the company's business plan, it is probably "ads". :-)  
</div>
</div>


#### Examples profiles from last year

<table class="table table-striped" id="examples"> 
  <tbody>
    {% assign id = 0 %}
    {% for questionnaire in site.data.example_company_profiles %}
    {% assign id = id | plus:1 %}
    {% assign anchor = questionnaire.what_company_are_you_profiling | replace:' ', '-' | replace:"'", '' | replace:'.', ''  | replace:'(', '' | replace:')', '' | append:"-" | append:id %}
   <tr>
      <td>
	<div class="hidden-sm hidden-xs">
		<a href="{{ questionnaire.give_a_url_for_the_companys_website }}"><img src="{{ questionnaire.give_a_url_for_the_companys_logo }}" width="200" /></a>
	</div>
      </td>
      <td>

<div class="visible-sm visible-xs">
	<a href="{{ questionnaire.give_a_url_for_the_companys_website }}"><img src="{{ questionnaire.give_a_url_for_the_companys_logo }}" width="100" /></a>
</div>
<div class="panel-group" id="accordion{{ anchor }}">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion{{ anchor }}" href="#{{ anchor }}">
	{{ questionnaire.give_a_one_sentence_description_of_the_company }} 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">

{% if questionnaire.do_you_mind_if_we_post_a_link_to_your_video_on_the_class_website == "Yes, post it! " %}
{% assign vimeourl = questionnaire.paste_in_the_url_of_your_presentation_on_vimeo | split:"/" %}
{% for urlpart in vimeourl %}
	{% capture videonum %}{{ urlpart }}{% endcapture %}
{% endfor %} 

<div align="center" class="hidden-sm hidden-xs">
<iframe src="http://player.vimeo.com/video/{{ videonum }}" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <br />
</div>
<div align="center" class="visible-sm visible-xs">
<b>Video profile:</b> <a href="http://player.vimeo.com/video/{{ videonum }}">http://player.vimeo.com/video/{{ videonum }}"</a> <br />
</div>
{% endif %}

<b>Who were the founders?</b> {{ questionnaire.who_were_the_founders }} <br />

<b>When was it started?</b> {{ questionnaire.when_was_the_company_started }} <br />

<b>Does it have any interesting origin story?</b> {{ questionnaire.does_it_have_an_interesting_origin_story }} <br />

<b>What services does {{ questionnaire.what_company_are_you_profiling }} provide?</b> {{ questionnaire.what_service_does_the_company_provide }} <br />

{% if questionnaire.does_this_update_a_previous_service_or_business_model_or_is_it_completely_new == "Updates a previous model" %}
	<b>If this updates a previous service or business model, what does it replace?</b> {{ questionnaire.if_it_updates_something_what_does_it_replace}} <br />

{% endif %}
<b>Who uses the services?</b> {{ questionnaire.what_is_an_example_of_how_someone_uses_this_service }} <br />

<b>Who are the people who contribute the services?</b> {{ questionnaire.who_are_the_people_who_contribute_services }} <br />

<b>How does {{ questionnaire.what_company_are_you_profiling }} incentivize them to contribute, or what is their motivation?</b> {{ questionnaire.how_does_the_company_incentivize_them_to_contribute_or_what_motivates_them_to_participate_ }} <br />

<b>Is this a service that was previously provided by experts?</b> {% if questionnaire.is_this_a_service_that_was_previously_provided_by_experts__professionals %} Yes. {% else %} No. {% endif %}
<br />

<b>Are the contributors experts/professionals?</b> {% if questionnaire.are_the_contributors_experts__professionals %} Yes. {% else %} No. {% endif %}
<br />

<b>How does {{ questionnaire.what_company_are_you_profiling }} ensure the quality of the services it provides?</b> {{ questionnaire.how_does_the_company_ensure_the_quality_of_the_services_it_provides}} <br />

{% if questionnaire.is_a_reputation_system_used_by_your_company %}
	<b>If {{ questionnaire.what_company_are_you_profiling }} uses a reputation system, how does it work?</b> {{ questionnaire.if_so_how_does_it_work}} <br />

{% endif %}
{% if questionnaire.is_its_service_something_that_is_typically_regulated_by_the_government %}
	<b>If its service is typically regulated by the government, what are the intents of the regulations and does the company meet those standards?</b> {{ questionnaire.if_so_what_are_the_intents_of_the_regulations_and_does_your_company_meet_those_standards }} <br />

{% endif %}
<b>Compare the number of users to contributors:</b> {{ questionnaire.compare_the_number_of_users_to_contributors }} <br />

<b>If its service is provided by many contributors, how are their contributions aggregated?</b> {{ questionnaire.if_the_service_is_provided_by_many_contributors_how_are_are_their_contributions_aggregated_ }} <br />

<b>Describe the workflow for how the service is advertised, how the contributors contribute, and what the users get in the end:</b> {{ questionnaire.describe_the_workflow_for_how_the_service_is_advertised_and_how_the_contributors_contribute_and_what_the_users_get_in_the_end }} <br />

<b>What is the scale of {{ questionnaire.what_company_are_you_profiling }} in terms of users?</b> {{ questionnaire.what_is_the_scale_of_the_services_that_your_company_provides_in_terms_of_users }} <br />

<b>What is the scale of {{ questionnaire.what_company_are_you_profiling }} in terms of dollars?</b> {{ questionnaire.what_is_the_scale_of_the_services_that_your_company_provides_in_terms_of_dollars }} <br />

<b>If {{ questionnaire.what_company_are_you_profiling }} were to scale up to 10-100 times its current size, how well do you think would its business model would work?</b> {{ questionnaire.if_your_company_were_to_scale_up_to_10_or_100_times_its_current_size_how_well_do_you_think_its_business_model_would_work }} <br />

<b>What kind of organization is it?</b> {{ questionnaire.what_kind_of_organization_is_it }} <br />

<b>How does {{ questionnaire.what_company_are_you_profiling }} generate revenue?</b> {{ questionnaire.how_does_the_company_generate_revenue }} <br />

<div class="hidden-sm hidden-xs">
<b>References</b> 
{% assign urls = questionnaire.what_online_resources_did_you_use_in_researching_it | split:"<p>" %}
<ul>
{% for url in urls %}
	<li> <a href="{{ url }}">{{ url }}</a> </li>
{% endfor %} 
</ul>
<br />
</div>
      </div>
    </div>
  </div>
</div>

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
