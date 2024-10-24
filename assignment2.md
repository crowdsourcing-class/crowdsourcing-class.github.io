---
layout: default
img: launching-a-start-up
caption: Crowdsource your startup!
title: Homework 2 "Market Research"
active_tab: homework
release_date: 2024-02-05
due_date: 2024-02-31T23:59:00EDT
submission_link: https://www.gradescope.com/courses/885628
deliverables:
    -
      description: writeup
      due_date: 2024-10-29T23:59:00EDT
    -
      description: video 
      due_date: 2024-10-31T23:59:00EDT
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
This homework will look at the wealth of companies and platforms that use crowdsourcing as part of their business. Here's a list of companies and platforms that you could research:

1. Microtask and Freelance Platforms
   * [Amazon Mechanical Turk (MTurk)](https://www.mturk.com/): Marketplace for Human Intelligence Tasks (HITs)
   * [Clickworker](https://www.clickworker.com/): European-based microtask platform
   * [Toloka](https://toloka.ai/): Yandex's platform for data collection and enrichment
   * [Upwork](https://www.upwork.com/): Freelance job marketplace connecting businesses with global talent
   * [Fiverr](https://www.fiverr.com/): Freelance services marketplace
   * [Freelancer](https://www.freelancer.com/): Freelance job marketplace
   * [TaskRabbit](https://www.taskrabbit.com/): On-demand task completion platform
   * [Microworkers](https://www.microworkers.com/): Microtask platform

2. AI Data Creation and Training
   * [Scale AI](https://scale.com/): AI training data platform
   * [Appen](https://appen.com/) (formerly Figure Eight): AI training data and content relevance services
   * [Labelbox](https://labelbox.com/): Data labeling platform for AI
   * [Hive](https://thehive.ai/): AI solutions and data labeling
   * [Sama](https://www.sama.com/) (formerly Samasource): Training data for AI
   * [Snorkel AI](https://snorkel.ai/): Data programming platform using weak supervision
   * [CloudFactory](https://www.cloudfactory.com/): Data processing for AI and automation
   * [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker/groundtruth/): Data labeling for machine learning
   * [Dataloop](https://dataloop.ai/): Combines human and machine intelligence for data annotation
   * [Surge AI](https://www.surgehq.ai/): Network of annotators for AI data labeling
   * [Invisible AI](https://invisible.ai/): Human-in-the-loop processes for high-quality AI training data

3. Prediction Markets and Forecasting
   * [Metaculus](https://www.metaculus.com/): Community forecasting platform
   * [Good Judgment Open](https://www.gjopen.com/): Crowdsourced forecasting of geopolitical events
   * [Kalshi](https://kalshi.com): A prediction market that operates under the approval of the Commodity Futures Trading Commission (CFTC)
   * [PredictIt](https://www.predictit.org/): Online marketplace for event predictions
   * [Polymarket](https://polymarket.com): Prediction market for politics, providing real-time odds for election results

4. Citizen Science and Research
   * [Zooniverse](https://www.zooniverse.org/): Platform hosting various citizen science projects
   * [Foldit](https://fold.it/): Online puzzle game about protein folding
   * [BOINC](https://boinc.berkeley.edu/): Volunteer computing and grid computing platform
   * [EyeWire](https://eyewire.org/): Neuron mapping game
   * [Apple ResearchKit](https://www.apple.com/researchkit/): Platform for building health research apps

5. Crowdsourced Content Creation and Curation
   * [Wikipedia](https://www.wikipedia.org/): Crowdsourced encyclopedia
   * [Quora](https://www.quora.com/): Question-and-answer platform
   * [Stack Overflow](https://stackoverflow.com/): Q&A platform for programmers
   * [Genius](https://genius.com/): Collaborative lyrics annotation platform

6. Distributed Problem-Solving
   * [InnoCentive](https://www.innocentive.com/): Platform for posting and solving challenges
   * [Kaggle](https://www.kaggle.com/): Data science and machine learning competition platform
   * [Topcoder](https://www.topcoder.com/): Competitive programming and design platform

7. Crowdfunding and Financial Services
   * [Kickstarter](https://www.kickstarter.com/): Crowdfunding platform for creative projects
   * [GoFundMe](https://www.gofundme.com/): Crowdfunding platform for various causes
   * [Experiment](https://experiment.com/): Crowdfunding platform for scientific research
   * [Unbound](https://unbound.com/): Crowdfunding publisher for authors
   * [Kiva](https://www.kiva.org/): Microlending platform
   * [Robinhood](https://robinhood.com/): Commission-free stock trading platform

8. Peer-to-Peer Services
   * [Airbnb](https://www.airbnb.com/): Peer-to-peer lodging platform
   * [Uber](https://www.uber.com/): Ride-sharing and delivery platform
   * [Lyft](https://www.lyft.com/): Ride-sharing platform
   * [DoorDash](https://www.doordash.com/): Food delivery platform
   * [Instacart](https://www.instacart.com/): Grocery delivery platform
   * [Postmates](https://postmates.com/): Food and goods delivery platform

9. Crowdsourced Design and Creativity
   * [99designs](https://99designs.com/): Platform connecting clients with graphic designers
   * [Threadless](https://www.threadless.com/): Creative community for art and design
   * [iStockPhoto](https://www.istockphoto.com/): Stock media marketplace

10. Education and Online Learning
    * [Coursera](https://www.coursera.org/): Online education platform
    * [edX](https://www.edx.org/): Online education platform
    * [Duolingo](https://www.duolingo.com/): Language learning app with crowdsourced translations

11. Review and Recommendation Platforms
    * [Yelp](https://www.yelp.com/): Business review platform
    * [TripAdvisor](https://www.tripadvisor.com/): Travel review and booking platform
    * [Amazon Reviews](https://www.amazon.com/): E-commerce platform with user reviews

12. Mapping and Navigation
    * [OpenStreetMap](https://www.openstreetmap.org/): Collaborative mapping project
    * [Waze](https://www.waze.com/): Crowdsourced navigation app


<!--

You are also welcome to profile a [relevant company](http://www.crowdsourcing.org/uploads/CrowdSourcing-Industry-Landscape-v09.jpg) that is not on this list (but please verify your choice beforehand with the instructor). 
-->


This assignment has two deliverables:

1. Answering [the Homework 2 questionnaire on Gradescope]({{page.submission_link}}) about the company or project that you are researching. This is due before {{ page.deliverables[0].due_date | date: "%I:%M%p" }} on {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}.  If you are working with a partner, only one of you needs to submit the questionnaire. **Please save your survey answers in a file on your own computer**, so that you can have a copy to use for your presentation.
2. A presentation video about the company. Several of the best videos will be selected for in-class presentations.  Teams whose videos are selected will receive extra credit. This is due before {{ page.deliverables[1].due_date | date: "%I:%M%p" }}  on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}.  You can submit a link to your video on [the Gradescope presentation form]({{page.submission_link}}).

This assignment can be done in pairs.

## Part 1: Researching a Company 

First, please [sign up for a company or project](https://docs.google.com/spreadsheets/d/1GMaMkncEuwUdGeWZjWlKYMhYpaTy4sIV47mwvm0d_ds/edit?usp=sharing).  Up to two teams can sign up for a company.  If two teams have already signed up for a company that you're interested in then please pick a different company.  If there’s a company that you’d like to research that isn’t on the list, you are welcome to ask the instructor or the TA to ask if it is OK.  Please post your request to Piazza.  

Next, please read the academic paper [Human Computation:
A Survey and Taxonomy of a Growing Field](http://crowdsourcing-class.org/readings/downloads/intro/QuinnAndBederson.pdf).  The paper introduces several dimensions that we'll use to categorize the companies that you'll be doing research -- dimensions like motivation, quality control, aggregation, and so on.  We will ask you to write a short summary of the paper.

You and your partner should research the company together, and then [fill in your answers about it in the Homework 2 questionnaire on Gradescope]({{page.submission_link}}).  Your short answers to these questions on  {{ page.deliverables[0].due_date | date: "%A, %B %-d, %Y" }}.  Remember to save your survey answers on your own computer, so that you can have a copy to use when you do your video profile.



<div class="panel panel-primary" id="survey">
<div class="panel-heading" markdown="1">
#### Questionnaire
</div>
<div class="panel-body" markdown="1">
Below are the questions that you will be asked to answer about the company or project that you are profiling. Please upload a PDF with your answers to [Gradescope]({{page.submission_link}}).

1. Please give a summary of the academic paper [Human Computation:
A Survey and Taxonomy of a Growing Field](http://crowdsourcing-class.org/readings/downloads/intro/QuinnAndBederson.pdf), and how it relates to this assignment.
1. What company are you profiling?
3. What online resources did you use in researching it? Include URLs.
4. Did you use any other resources? Did you conduct any interviews, did you try the company’s service?
5. Give a one sentence description of the company. Be sure to use the name of the company in your sentence.
6. Give a URL for the company’s website
7. Give a URL for the company’s logo
8. When was the company started?
9. Who were the founders?
10. Does it have an interesting origin story?
11. What kind of organization is it? 
  -  Publicly traded company
  -  Privately held company
  -  Non-profit organization
  -  Other
12. If the company type is none of the above, please specify.
13. What service does the company provide?
14. Does this update a previous service or business model, or is it completely new?
15. If it updates something, what does it replace?
16. What other new companies provide services that are similar to your company’s?
17. What is an example of how someone uses this service? What sort of people use the service? If this is a service that you have used, then describe your experience. 
18. Compare the number of users to contributors.
  -  More users than contributors
  -  More contributors than users
  -  Roughly equal numbers
19. Who are the people who contribute services?
20. How does the company incentivize them to contribute, or what motivates them to participate?
21. Is this a service that was previously provided by experts / professionals?
22. Are the contributors experts / professionals?
23. How does the company generate revenue?
24. How does the company ensure the quality of the services it provides?
25. Is its service something that is typically regulated by the government?
26. If so, what are the intents of the regulations and does your company meet those standards?
27. Is a reputation system used by your company?
28. If so, how does it work?
29. If the service is provided by many contributors, how are are their contributions aggregated?
30. Describe the workflow for how the service is advertised, and how the contributors contribute, and what the users get in the end.
31. What is the scale of the services that your company provides, in terms of users?
32. What is the scale of the services that your company provides, in terms of dollars?
33. If your company were to scale up to 10 or 100 times its current size, how well do you think its business model would work? How well would the incentive scheme scale? How about the quality/aggregation model?
34. How do you think AI will affect this company?
35. Have there been any controversies about the company or the service that it provides?
36. Is there anything else you'd like to say about the company?
</div>
</div>


## Part 2: Creating a Video 


You will prepare a short presentation in the form a 5 to 7 minute video presentation about your company. Your presentation should address the following questions:

- What incentives does it offer to get people to participate?
- How does it aggregate the information provided by the crowd?
- What are the quality concerns, and how does the company do quality control?
- How does the company benefit from user contributions?
- Are there any controversies about the company?

Your presentation is due on {{ page.deliverables[1].due_date | date: "%A, %B %-d, %Y" }}. To turn in your video, please upload it to YouTube or Vimeo. Give us the link to your presentation or video using [the Homework 2 presentation form]({{page.submission_link}}). Make sure that your video is publicly viewable or that you give us a password to view it on the web form.



<div class="panel panel-info" id="faq">
<div class="panel-heading" markdown="1">
#### FAQ
</div>
<div class="panel-body" markdown="1">
- **What is the difference between Users and Contributors?**

  Many of you seemed confused about what constitutes a user vs. a contributor. In many crowdsourcing companies, this line is blurry- or nonexistent! Many companies you looked at fit what can be thought of as a "data-mining" model (e.g. Yelp, Foursquare), in which the primary service being provided depends on using data and modeling observed patterns of behavior-- e.g. to target ads or to recommend products. In these cases, the users are the contributors-- everyone who participates provides data, and everyone uses everyone else's data. This is an awesome crowdsourcing model because it is (ideally) self-sustaining and self-incentivizing. The more a person contributes (by providing more data about themselves), the better product they receive (e.g. better recommendations). 

- **How does my company do Aggregation?**

  Many of the companies we look at fit into the "match-making" or "marketplace" model (e.g. Uber, Airbnb, Etsy). This is a very common case in which the company is simply working to match supply with demand, where the suppliers (e.g. drivers, in the case of Uber) and the consumers (riders) are distributed all over, and may have trouble finding one another otherwise. Here, rating systems etc. are one piece of the platform that might require aggregating, but arguably the more interesting aggregation problem is how to match a supplier with a consumer. Is this through preference-based recommendation systems (as in the data-mining model discussed above), through location-based matching, through bidding/price? Making these matches is non-trival, but crucial to making the company function.

- **Does this update a previous service or business model, or is it completely new?**

  For this question, more than a third of you said "completely new." Try to think broadly when you are considering where these crowdsourcing companies fit into the economy as a whole. (Think Silicon Valley's favorite buzzword: "disruption.") Most of these services being provided are not completely new, but they are directly competing with a service that was traditionally supplied by a brick-and-mortar company in a more centralized manner. Uber competes with taxi companies, Airbnb with hotel chains, Coursera with higher education universities. This is part of what makes crowdsourcing so exciting!

- **Is getting venture capital funding is a business model?**

  No. Smart investors don't invest in a company who says their plan for generating revenue is to "get money from investors." When in doubt about the company's business plan, it is probably "ads". :-)

- **How to make a group submission on Gradescope?**

  One group member can submit answers just as you do in previous homeworks. Then at the submitted page where you could see all your answers and points distribution, there is an option on the top right for you to edit group member. You can add your partner there with his or her Gradescope Id inside this course. Both of you with share the same submission and get the same grading. The submission is required to be made by only one team member.

</div>
</div>


<div class="panel panel-danger" id="rubric">
<div class="panel-heading" markdown="1">
#### Grading Rubric
</div>
<div class="panel-body" markdown="1">

The written survey is worth approximately 10% of your overall grade in the course. Please answer the survey questions thoughtfully. Importantly, you must discuss aspects of the company to crowdsourcing, and the themes of the class like aggregation, quality control, machine learning, etc. Extra credit would worth approximately 5% of the overall grade in the course.

</div>
</div>

<!--

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

{% if questionnaire.do_you_mind_if_we_post_a_link_to_your_video_on_the_class_website == "Yes, post it!" %}
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
    {% endfor %}
-->
