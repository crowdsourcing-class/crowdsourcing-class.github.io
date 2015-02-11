---
layout: default
img: Crowdsourcing_Landscape
img_link: http://www.thinketc.com/wp-content/uploads/2012/05/Crowdsourcing_Landscape.jpg
title: Company profile presentation
active_tab: company-profile
---


Final projects from the students enrolled in NETS 213 in Fall 2014
=============================================================

<table class="table table-striped"> 
  <tbody>
    {% assign id = 0 %}
    {% for questionnaire in site.data.final_projects_2014 %}
    {% assign id = id | plus:1 %}
    {% assign anchor = questionnaire.name_of_your_project | replace:' ', '-' | replace:"'", '' | replace:'.', ''  | replace:'(', '' | replace:')', '' | append:"-" | append:id %}
   <tr>
      <td>
	<div class="hidden-sm hidden-xs">
		<img src="{{ questionnaire.url_to_the_logo_for_your_project }}" width="200" />
	</div>
      </td>
      <td>

<div class="visible-sm visible-xs">
	<img src="{{ questionnaire.url_to_the_logo_for_your_project }}" width="100" />
</div>
<div class="panel-group" id="accordion{{ anchor }}">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion{{ anchor }}" href="#{{ anchor }}">
	{{ questionnaire.give_a_one_sentence_description_of_your_project }} 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">

{% if questionnaire.may_we_have_your_permission_to_feature_your_project_on_the_class_website == "Yes" %}
{% assign vimeourl = questionnaire.provide_a_link_to_your_final_presentation_video | split:"/" %}
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

<b>What problem does it solve?</b> {{ questionnaire.what_problem_does_it_solve }} <br />

<b>What type of project is it?</b> {{ questionnaire.what_type_of_project_is_it }} <br />

<b>Who are the members of your crowd?</b> {{ questionnaire.who_are_the_members_of_your_crowd }} <br />

<b>How did you incentivize the crowd to participate?</b> {{ questionnaire.how_do_you_incentivize_the_crowd_to_participate }} <br />

{% if questionnaire.did_you_perform_any_analysis_comparing_different_incentives_ == "Yes" %}
	<b>If you performed an analysis comparing different incentives, what analysis did you perform?</b> {{ questionnaire.if_you_compared_different_incentives_what_analysis_did_you_perform_}} <br />

{% endif %}
      </div>
    </div>
  </div>
</div>

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 