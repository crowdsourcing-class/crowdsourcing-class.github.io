---
layout: default
img: the-visual-display-of-quantitative-information
img_link: http://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142/
caption: Read this book. It will change your life.
title: Homework 8 "Analyze Data"
active_tab: homework
release_date: 2019-04-04
due_date: 2019-04-11T23:59:00EST
---

<!-- Check whether the assignment is up to date -->
{% capture this_year %}{{'now' | date: '%Y'}}{% endcapture %}
{% capture due_year %}{{page.due_date | date: '%Y'}}{% endcapture %}
{% if this_year != due_year %} 
<div class="alert alert-danger">
Warning: this assignment is out of date.  It may still need to be updated for this year's class.  Check with your instructor before you start working on this assignment.
</div>
{% endif %}
<!-- End of check whether the assignment is up to date -->

<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<script type="text/javascript">
google.load("visualization", "1.1", {packages:["corechart", "geochart", "calendar"]});
google.setOnLoadCallback(drawCharts);
function drawCharts() {
var oldData = google.visualization.arrayToDataTable([
["Gun", "Count"],
["Handgun (Pistol/Revolver)", 503],
["Long gun (Rifle/Shotgun)", 202],
["Machine gun/Assault rifle", 83],
]);
var newData = google.visualization.arrayToDataTable([
["Gun", "Count"],
["Handgun (Pistol/Revolver)", 410],
["Long gun (Rifle/Shotgun)", 189],
["Machine gun/Assault rifle", 51],
]);
var options = {};
var chartDiff = new google.visualization.PieChart(document.getElementById('guns_div'));
var diffData = chartDiff.computeDiff(oldData, newData);
chartDiff.draw(diffData, options);

var data = google.visualization.arrayToDataTable([
['State', 'Number of incidents'],
['AK', 1],
['AL', 17],
['AR', 13],
['AZ', 22],
['CA', 110],
['CO', 61],
['CT', 9],
['DC', 3],
['DE', 3],
['FL', 27],
['GA', 37],
['HI', 1],
['IA', 6],
['ID', 2],
['IL', 148],
['IN', 81],
['KS', 24],
['KY', 11],
['LA', 45],
['MA', 22],
['MD', 28],
['ME', 1],
['MI', 62],
['MN', 57],
['MO', 67],
['MS', 39],
['MT', 13],
['NC', 50],
['ND', 6],
['NE', 2],
['NH', 2],
['NJ', 56],
['NM', 1],
['NV', 5],
['NY', 65],
['OH', 61],
['OK', 23],
['OR', 5],
['PA', 40],
['SC', 59],
['TN', 153],
['TX', 118],
['UT', 7],
['VA', 23],
['VT', 2],
['WA', 14],
['WI', 66],
['WV', 2],
]);
var options = {
region : 'US',
displayMode: 'markers',
resolution: 'provinces',
colorAxis : {colors : ['#FF1919', '#800000']}
};
var chart = new google.visualization.GeoChart(document.getElementById('intentional_div'));
chart.draw(data, options);

var data = google.visualization.arrayToDataTable([
['State', 'Number of incidents'],
['AL', 1],
['AR', 1],
['AZ', 3],
['CA', 12],
['CO', 8],
['DC', 2],
['DE', 1],
['FL', 10],
['GA', 3],
['IA', 4],
['ID', 1],
['IL', 51],
['IN', 12],
['KS', 4],
['KY', 3],
['LA', 1],
['MA', 2],
['MD', 5],
['MI', 11],
['MN', 1],
['MO', 12],
['NC', 7],
['NJ', 7],
['NM', 1],
['NY', 15],
['OH', 8],
['OK', 1],
['OR', 1],
['PA', 13],
['SC', 8],
['SD', 1],
['TN', 11],
['TX', 16],
['UT', 3],
['VA', 3],
['WA', 3],
['WI', 8],
['WV', 1],
['WY', 1],
]);
var options = {
region : 'US',
displayMode: 'markers',
resolution: 'provinces',
colorAxis : {colors : ['#3333FF', '#000066']}
};
var chart = new google.visualization.GeoChart(document.getElementById('unintentional_div'));
chart.draw(data, options);


var data = google.visualization.arrayToDataTable([
['Hour', 'Fatal', 'Nonfatal'],
['1', 96, 142],
['2', 74, 141],
['3', 129, 257],
['4', 43, 48],
['5', 20, 29],
['6', 30, 32],
['7', 30, 25],
['8', 36, 26],
['9', 43, 25],
['10', 116, 84],
['11', 146, 158],
['12', 63, 74],
['13', 67, 66],
['14', 34, 67],
['15', 77, 53],
['16', 36, 96],
['17', 95, 151],
['18', 120, 157],
['19', 103, 191],
['20', 77, 165],
['21', 194, 111],
['22', 82, 142],
['23', 84, 107],
['24', 33, 45],
]);
var view = new google.visualization.DataView(data);
var options = {
title: 'Fatal and Nonfatal shootings by time of day',
curveType: 'function',
legend: { position: 'bottom' }
};
var chart = new google.visualization.LineChart(document.getElementById('time_chart'));
chart.draw(data, options);

var data = google.visualization.arrayToDataTable([
['Race', 'White', 'African Am.', 'Asian/Mid. Eastern', 'Hispanic', 'Other', { role: 'annotation' } ],
['Hispanic', 1.0 , 0, 0, 1.0, 0, ''],
['White', 4.0 , 12.0, 0, 0, 0, ''],
['Other', 0 , 0, 0, 0, 3.0, ''],
['African American', 1.0 , 3.0, 0, 4.0, 0, ''],
['Asian/Mid. Eastern', 0 , 1.0, 9.0, 0, 1.0, ''],
]);
var view = new google.visualization.DataView(data);
var options = {
width: 600,
height: 400,
legend: { position: 'top', maxLines: 3 },
bar: { groupWidth: '75%' },
hAxis : {title : 'Race of shooter'},
vAxis : {title : 'Number of reports by race of victim'},
isStacked: true,
};
var chart = new google.visualization.ColumnChart(document.getElementById("race_div"));
chart.draw(view, options);
};

</script>

<div class="alert alert-info">
This assignment is before {{ page.due_date | date: "%I:%M%p" }} due on {{ page.due_date | date: "%A, %B %-d, %Y" }}. 
</div>

Analyze Data<span class="text-muted">: Assignment 8</span> 
=============================================================

We are down to the final two weekly homework assignments. This week, we will analyze the data about MTurkers, and try to see if it better helps us answer who/where/when/how questions about crowd workers in the world. 

Please download [here](assignments/downloads/hw8.zip) to start. It contains four csv files as data, and an ipython notebook **HW8.ipynb** with questions, instructions and skeleton code.

<h2>Data</h2>

You will be provided the following csv files in this assignment:

* **crowdworker_survey.csv** -- This file contains almost-clean data collected from a [survey](assignments/downloads/CrowdWorkers_Survey.pdf) taken by crowd workers. For more details, you can check out this [paper](http://www.cis.upenn.edu/~ccb/publications/crowd-workers-demographics.pdf) on how researchers analyze Turker demographics and earnings.

* **clustered\_hourly\_wage.csv** -- This contains hourly wage information for each worker.

* **crowd_tasks.csv** -- This is a random sample of 25,000 tasks from the pool of tasks our survey respondents completed.

* **work\_time\_pay.csv** -- This file contains average task completion time and average pay per task for a subset of workers from the original data in *crowdworker_survey.csv*. 

<h2>Deliverables</h2>

One deliverable is required: **HW8.ipynb** with your implementation and answers. 

You can work in pairs, and each pair only needs to submit one ipython notebook. No report is required, but you should write up answers to the open ended questions as text on the notebook.


<div class="panel panel-danger">
<div class="panel-heading" markdown="1">
<h4>Grading Rubric</h4>
</div>
<div class="panel-body" markdown="1">

This assignment is worth 100 points in total, which will be scaled down to be worth the same as your other homeworks. Sections 2.7 and 3.1-3.2 of the homework are extra credit. You can earn up to 60 points of extra credit (see the notebook for details).
