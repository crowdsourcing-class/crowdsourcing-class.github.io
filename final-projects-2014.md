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
   <tr>
      <td>
	<img src="{{ questionnaire.url_to_the_logo_for_your_project }}" width="100" />
{{ questionnaire.give_a_one_sentence_description_of_your_project }} 
       </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 