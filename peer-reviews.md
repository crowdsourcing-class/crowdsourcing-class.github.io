---
layout: default
img: peer-evaluation
caption: Peer Reviews
title: Peer Reviews of Project Pitches
active_tab: project
---


Peer Reviews
=============================================================
Here are the peer reviews of your term project ideas:

<table class="table"> 
  <tbody>
    {% for review in site.data.peer-reviews %}
    {% assign anchor = review.project | replace:' ', '-' | replace:"'", '' | replace:'.', ''  | replace:'!', '' | replace:',', '' | replace:'?', ''  | replace:'(', '' | replace:')', '' |  replace:'#', '' %}
   <tr>
      <td>
<div class="panel-group" id="accordion{{ anchor }}">
  <div class="panel panel-default">
    <div class="panel-heading">
      <div class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion{{ anchor }}" href="#{{ anchor }}">
	<b>{{ review.project }}</b> - {{ review.rank }} 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">
	<b>How relevant is this project to the course?</b> {{ review.relevance }} <br />
	<b>How feasible is it to execute this project by the end of the semester?</b> {{ review.feasibility }} <br />
	<b>How well fleshed out is the plan to incentivize/recruit a crowd for this project?</b> {{ review.incentives }} <br />
	<b>How well fleshed out is the plan to ensure the quality of the crowd's results?</b> {{ review.quality }} <br />
	<b>How well fleshed out is the plan to aggregate the crowd's contribution for this project?</b> {{ review.aggregation }} <br />
	<b>Is it likely that the team will be able to recruit the crowd it needs to execute this project?</b> {{ review.recruitment }} <br />
	<b>How exciting is this project?</b> {{ review.excitement }} <br />
	<b>Suggestions:</b> {{ review.suggestions }} <br />
	<b>Potential Problems:</b> {{ review.problems }} <br />
      </div>
    </div>
  </div>
</div>

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 