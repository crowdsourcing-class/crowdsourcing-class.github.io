---
layout: default
img: Francis-Galton
img_link: http://en.wikipedia.org/wiki/Francis_Galton
caption: Fracis Galton wrote about the wisdom of crowds in his Nature article Vox Populi 
title: Lectures
active_tab: lectures
---

Subject to change as the term progresses.


<div class="container-fluid">
  <div class="row">
      <div class="col-md-2 col-sm-4 col-xs-12">
	<b>Date</b>
      </div>
      <div class="col-lg-5 col-md-4 col-xs-12">
	<b>Topic</b>
      </div>
      <div class="col-lg-5 col-md-4 col-xs-12">
	<b>Readings</b>
      </div>
  </div>
    {% for lecture in site.data.lectures %}
  <div class="row">
      <div class="col-md-2 col-sm-4 col-xs-12">
	{{ lecture.date | date: "%A, %B %-d, %Y" }}
      </div>
      <div class="col-lg-5 col-md-4 col-xs-12">
	{% if lecture.slides %}
		<a href="{{ lecture.slides }}">{{ lecture.title }}</a>
        {% else %}
		{{ lecture.title }}
	{% endif %}
	{% if lecture.speaker %}
		{% if lecture.speaker_url %} 
			by <a href="{{ lecture.speaker_url }}">{{ lecture.speaker }}</a>
		{% else %} 
			by {{ lecture.speaker }}
		{% endif %}
	{% endif %}
	{% if lecture.highlights %}
	<ul>
	   {% for highlight in lecture.highlights %}	
			<span class="text-muted"><li>{{ highlight }}</li></span>
	   {% endfor %}
	</ul>
        {% endif %}
      </div>
      <div class="col-lg-5 col-md-4 col-xs-12">
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
      </div>
  </div>
    {% endfor %}

</div>


