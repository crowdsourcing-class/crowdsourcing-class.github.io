---
layout: default
title: Assignments
active_tab: assignments
---



<table class="table table-striped">
  <tbody>
    {% for page in site.pages %}
      {% if page.url contains assignment %}
        <tr><td>{{page.url}}</td></tr>
      {% endif %}
    {% endfor %}    
  </tbody>
</table>

