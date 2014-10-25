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
	<b>{{ review.project }}</b> 
        </a>
      </div>
    </div>
    <div id="{{ anchor }}" class="panel-collapse collapse">
      <div class="panel-body">
	<b>Suggestions</b> {{ review.suggestions }} <br />
      </div>
    </div>
  </div>
</div>

      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
 