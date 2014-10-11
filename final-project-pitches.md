---
layout: default
img: brainstorm
caption: Brain designed by <a href="http://www.thenounproject.com/marcusmichaels">Marcus Michaels</a> from the <a href="http://www.thenounproject.com">Noun Project</a>
title: Project Pitches
active_tab: project
---


Project Pitches
=============================================================
Here are the pitches that you came up with for your term projects:

<table class="table"> 
  <tbody>
    {% for questionnaire in site.data.project_pitch %}
    {% assign anchor = questionnaire.name_of_your_project | replace:' ', '-' | replace:"'", '' | replace:'.', ''  | replace:'!', '' | replace:',', '' | replace:'?', ''  | replace:'(', '' | replace:')', '' |  replace:'#', '' %}
   <tr>
      <td>
<div class="panel-group" id="accordion{{ anchor }}">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion{{ anchor }}" href="#{{ anchor }}">
	<b>{{ questionnaire.name_of_your_project }}</b> : 
	{{ questionnaire.give_a_one_sentence_description_of_your_project }} 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">

<b>What problem does it solve?</b> {{ questionnaire.what_problem_does_it_solve }} <br />
<b>What similar projects exist?</b> {{ questionnaire.what_similar_projects_exist }} <br />
<b>What type of project is it?</b> {{ questionnaire.what_type_of_project_is_it }} <br />
<b>Who will be the members of your crowd?</b> {{ questionnaire.who_will_be_the_members_of_your_crowd }} <br />
<b>How will you incentivize them to participate?</b> {{ questionnaire.how_will_you_incentivize_them_to_participate }} <br />
<b>What will they provide and sort of skills do they need?</b> {{ questionnaire.what_will_they_provide_and_what_sort_of_skills_do_they_need }} <br />
<b>How will you ensure the quality of what the crowd provides?</b> {{ questionnaire.how_will_you_ensure_the_quality_of_the_crowd_provides }} <br />
<b>How will you aggregate results across the crowd?</b> {{ questionnaire.how_will_you_aggregate_the_results_from_the_crowd }} <br />
<b>Describe each of the steps involved in your process, and say what parts will be done will be done by the crowd and what parts will be done automatically:</b> {{ questionnaire.describe_each_of_the_steps_involved_in_your_process_what_parts_will_be_done_by_the_crowd_and_what_parts_will_be_done_automatically }} <br />
<b>How will you evaluate whether or not your project is successful?</b> {{ questionnaire.how_will_you_evaluate_if_your_project_is_successful }} <br />
<b>What potential problems do you foresee when implementing your project?</b> {{ questionnaire.what_potential_problems_do_you_foresee_when_implementing_your_project }} <br />


{% assign vimeourl = questionnaire.provide_a_link_to_your_vimeo_video | split:"/" %}
{% for urlpart in vimeourl %}
	{% capture videonum %}{{ urlpart }}{% endcapture %}
{% endfor %} 
<div align="center" class="hidden-sm hidden-xs">
<iframe src="http://player.vimeo.com/video/{{ videonum }}" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <br />
</div>
<div align="center" class="visible-sm visible-xs">
<b>Video profile:</b> <a href="http://player.vimeo.com/video/{{ videonum }}">http://player.vimeo.com/video/{{ videonum }}"</a> <br />
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
 