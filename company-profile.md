---
layout: default
img: Crowdsourcing_Landscape
img_link: http://www.thinketc.com/wp-content/uploads/2012/05/Crowdsourcing_Landscape.jpg
title: Company profile presentation
active_tab: company-profile
---


Company Profiles
=============================================================
As part of your [market research assignment](assignment2.html), you will give a short 5 to 10 minute presentation on your company.  Your presentation should answer the following questions:

- What incentives does the company offer to get people to participate?
- How does it aggregate the information provided by the crowd?
- What are the quality concerns, and how does the company do quality control?
- How does the company benefit from user contributions?

Here are the companies that you are profiling this term:

<table class="table table-striped"> 
  <tbody>
    {% assign id = 0 %}
    {% for questionnaire in site.data.company_profiles %}
    {% assign id = id | plus:1 %}
    {% assign anchor = questionnaire.what_company_are_you_profiling | replace:' ', '-' | replace:'.', ''  | replace:'(', '' | replace:')', '' | append:"-" | append:id %}
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

{% if questionnaire.does_this_update_a_previous_service_or_business_model_or_is_it_completely_new == "Yes, post it! " %}
{{ questionnaire.paste_in_the_url_of_your_presentation_on_vimeo }} <br />

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

{% if questionnaire.is_there_anything_else_youd_like_to_say_about_the_company | strip_newlines | replace:’ ',''  != "" %}
<b>Anything else?</b> {{ questionnaire.is_there_anything_else_youd_like_to_say_about_the_company }} <br />
{% endif %}

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

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 