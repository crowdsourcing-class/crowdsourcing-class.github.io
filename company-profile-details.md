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

Here is the schedule for the presentations this term:

<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Date</th>
      <th>Company</th>
    </tr>
    {% for company in site.data.company_profiles %}
   <tr>
      <td>{{ company.what_date_did_you_choose_for_your_inclass_presentation | date: "%b %d" }}</td>
      <td>
	<img src="{{ company.give_a_url_for_the_companys_logo }}" width="200" /> 
        {% else %}{{ company.what_company_are_you_profiling }}{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 