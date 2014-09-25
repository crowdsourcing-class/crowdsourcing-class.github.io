---
layout: default
img: Crowdsourcing_Landscape
img_link: http://www.thinketc.com/wp-content/uploads/2012/05/Crowdsourcing_Landscape.jpg
title: Company profile presentation
active_tab: company-profile
---

Company Profiles
=============================================================
table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Logo</th>
      <th>Company</th>
    </tr>
    {% for company in site.data.company_profiles %}
   <tr>
      <td>
	<img src="{{ company.give_a_url_for_the_companys_logo }}" width="200" /> 
      </td>
      <td>
	{{ company.what_company_are_you_profiling }} 
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 