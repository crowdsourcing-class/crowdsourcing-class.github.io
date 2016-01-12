---
layout: default
title: NETS 213 Staff
active_tab: staff
---

<div class="container-fluid">
  <div class="row">
  {% for staff in site.data.staff %}
      <div class="col-lg-4 col-md-6 col-xs-12" style="margin-bottom: 20px; height: 350px;">
        {% if staff.pic %}<img src="assets/img/staff/{{staff.pic}}" class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />
        {% else %}<img src="assets/img/staff/profile-pic.png" class="img-circle" style="height: 100%; width: 100%; max-height: 250px; max-width: 250px"/><br />{% endif %}
	{% if staff.webpage %}<b><a href="{{ staff.webpage }}">{{ staff.name }}</a></b><br />
	{% else %}<b>{{ staff.name }}</b><br />{% endif %}
        {% if staff.extra_title %}<b>{{ staff.extra_title }}</b><br />{% endif %}
        <a href="mailto:{{ staff.email }}">{{ staff.email }}</a><br>
       	{% if staff.office_hours %}<span markdown="1">Office Hours: {{ staff.office_hours }}</span>{% endif %}
      </div>
  {% endfor %}
  </div>
</div>
