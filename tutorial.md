---
title: NAACL 2015 Tutorial on Crowdsourcing for NLP
layout: default
img: turk-engraving-detail
img_link: http://en.wikipedia.org/wiki/The_Turk
caption: An engraving of the Mechanical Turk, the 18th century chess-playing automaton
active_tab: main_page 
---

Welcome to the NAACL 2015 Tutorial on Crowdsourcing for NLP!  

CrowdFlower has generously offered a $100 credit to all of the tutorial's participants.  Sign up for the credits [on this Google form](https://docs.google.com/forms/d/1aT9eypWdCEeqMIhjgl6oF6W9AICMyoQb42yEI-gjnmQ/viewform?usp=send_form), and then [register for CrowdFlower](https://make.crowdflower.com/users/new) using the same email address.


<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Topic</th>
      <th>Readings</th>
    </tr>
    {% for lecture in site.data.tutorial %}
    <tr>
      <td>
	{% if lecture.profile %}
	Company Profile:  
        {% endif %}
        {% if lecture.slides %}<a href="{{ lecture.slides }}">{{ lecture.title }}</a>
        {% else %}{{ lecture.title }}{% endif %}

	{% if lecture.speaker %}
        {% if lecture.speaker_url %} by <a href="{{ lecture.speaker_url }}">{{ lecture.speaker }}</a>
        {% else %} by {{ lecture.speaker }}{% endif %}
	{% endif %}

	{% if lecture.highlights %}
	  <ul>
	   {% for highlight in lecture.highlights %}	
	   <span class="text-muted"><li>
	   {{ highlight }}
	   </li></span>
          {% endfor %}
        {% endif %}
      </td>
      <td>
        {% if lecture.reading %}
          <ul class="fa-ul">
          {% for reading in lecture.reading %}
            <li>
            {% if reading.optional %}<i class="fa-li fa fa-star"> </i>
            {% else %}<i class="fa-li fa"> </i> {% endif %}
            {% if reading.url %}
            <a href="{{ reading.url }}">{{ reading.title }}</a>
            {% else %}
            {{ reading.title }} 
            {% endif %}
	    {% if reading.author %}
            by {{ reading.author }}
            {% endif %}
            </li>
          {% endfor %}
          </ul>
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
