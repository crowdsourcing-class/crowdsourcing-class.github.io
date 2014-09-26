---
layout: default
img: Crowdsourcing_Landscape
img_link: http://www.thinketc.com/wp-content/uploads/2012/05/Crowdsourcing_Landscape.jpg
title: Company profile presentation
active_tab: company-profile
---

Company Profiles
=============================================================



<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Logo</th>
      <th>Company</th>
    </tr>
    {% for questionnaire in site.data.company_profiles %}
   <tr>
      <td>
	<a href="{{ questionnaire.give_a_url_for_the_companys_website }}"><img src="{{ questionnaire.give_a_url_for_the_companys_logo }}" width="200" /></a>
      </td>
      <td>
<div class="panel-group" id="accordion">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion" href="#{{ questionnaire.what_company_are_you_profiling }}">
	{{ questionnaire.give_a_one_sentence_description_of_the_company }} 
        </a>
      </div>
    </div>
    <div id="{{ questionnaire.what_company_are_you_profiling }}" class="panel-collapse collapse">
      <div class="panel-body">
<b>When was it started?</b> {{ questionnaire.when_was_the_company_started }} <br />
<b>Who were the founders</b> {{ questionnaire.who_were_the_founders ]}} <br />
<b>What services does {{ questionnaire.what_company_are_you_profiling }} provide?</b> {{ questionnaire.what_service_does_the_company_provide ]}} <br />
<b>Who uses the services?</b> {{ questionnaire.what_is_an_example_of_how_someone_uses_this_service ]}} <br />
<b>Who are the people who contribute the services?</b> {{ questionnaire.who_are_the_people_who_contribute_services ]}} <br />
<b>How does {{ questionnaire.what_company_are_you_profiling }} incentivize them to contribute, or what is their motivation?</b> {{ questionnaire.how_does_the_company_incentivize_them_to_contribute_or_what_motivates_them_to_participate_: ]}} <br />
      </div>
    </div>
  </div>
</div>

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 