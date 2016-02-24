---
layout: default
img: Francis-Galton
img_link: http://en.wikipedia.org/wiki/Francis_Galton
caption: Francis Galton wrote about the wisdom of crowds in his Nature article Vox Populi 
title: Lectures
active_tab: lectures
---

<div class="alert alert-info" markdown="1">
You can [watch recordings of the lectures](https://ex.cts.isc.upenn.edu/Mediasite/Catalog/Full/f03b307a2f104b5e826eb9620d1db36a21).
</div>




<!-- Create a HTML anchor for the most recent lecture -->
{% assign anchor_created = false %}
{% capture now %}{{'now' | date: '%s'}}{% endcapture %}
<!-- End create a HTML anchor for the most recent lecture -->


The lecture schedule is subject to change as the term progresses.

<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Date</th>
      <th>Topic</th>
      <th>Readings</th>
    </tr>
    {% for lecture in site.data.lectures %}

<!-- Create a HTML anchor for the most recent lecture -->
{% capture lecture_date %}{{lecture.date | date: '%s'}}{% endcapture %}
{% assign lecture_date = lecture_date | plus: 0 %}
{% assign now = now | minus: 14400 %}

{% if anchor_created != true and lecture_date >= now %}
   {% assign anchor_created = true %}
<tr id="now">
   {% else %}
<tr>
{% endif %}
<!-- End create a HTML anchor for the most recent lecture -->
      <td>{{ lecture.date | date: "%A, %B %-d, %Y" }}</td>
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

