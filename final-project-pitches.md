---
layout: default
img: brainstorm
caption: Brain designed by <a href="http://www.thenounproject.com/marcusmichaels">Marcus Michaels</a> from the <a href="http://www.thenounproject.com">Noun Project</a>
title: Final Project | Brainstorm 3 Ideas
active_tab: homework
---


Project Pitches
=============================================================
Here are the pitches that you came up with for your term projects:

<table class="table table-striped"> 
  <tbody>
    {% assign id = 0 %}
    {% for questionnaire in site.data.project_pitch %}
    {% assign id = id | plus:1 %}
    {% assign anchor = questionnaire.name_of_your_project | replace:' ', '-' | replace:"'", '' | replace:'.', ''  | replace:'(', '' | replace:')', '' | append:"-" | append:id %}
   <tr>
      <td>
<div class="panel-group" id="accordion{{ anchor }}">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion{{ anchor }}" href="#{{ anchor }}">
	{{ questionnaire.name_of_your_project }} : 
	{{ questionnaire.give_a_one_sentence_description_of_your_project }} 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">

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

<b>What problem does it solve?</b> {{ questionnaire.what_problem_does_it_solve }} <br />

      </div>
    </div>
  </div>
</div>

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 