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

      </div>
    </div>
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 