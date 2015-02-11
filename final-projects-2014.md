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
    {% for questionnaire in site.data.company_profiles %}
   <tr>
      <td>
{{ questionnaire.give_a_one_sentence_description_of_the_company }} 
       </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 