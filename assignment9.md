---
layout: default
img: the-visual-display-of-quantitative-information
img_link: http://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142/
caption: Read this book. It will change your life.
title: Homework 9 | A picture is worth 5,948 HITs
active_tab: homework
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

A Picture is Worth 5,948 HITs<span class="text-muted">: Assignment 9</span> 
=============================================================

We are down to the final two weekly homework assignments. This week and next, we will analyze the data that our workers have extracted, and try to see if it better helps us answer who/where/when/how questions about gun violence in the USA. We'll use the [Google Charts API](https://developers.google.com/chart/) which makes even boring statistics look sexy as all hell.

##Data

You can download the almost-clean data [here](assignments/downloads/gun-database.tsv). It contains 5,948 reports and the strucuted data that our Turkers extracted. The data file contains four columns, described below:

 * Article url-- The url of the article
 * Article title-- The title of the alchemy, extracted using the Alchemy API
 * Full text-- The full text of the article, extracted using hte Alchemy API. (You will use this in next week's assignment.)
 * Json-- The extracted information about the incident, e.g. time, location, shooter name, etc. (You will use this data for this assignment.)
 * Worker-- The worker who extracted the information

You can do this assignment in whatever language you prefer, but word on the street is all the cool kids are using Python. You can load the data into a list using the following code. You should be familiar with [JSON](http://en.wikipedia.org/wiki/JSON) format from our last assignment.

<pre><code>import csv
import json

data = []
for row in csv.DictReader(open('gun-database.tsv'), delimiter='\t'):
  data.append(json.loads(row['Json']))
</code></pre>

Now, <code>data</code> is a python list of all the records in our data. Each record is a dictionary. A single record, for example, might look like this beauty:

<pre><code>>> data[17]
{u'date-and-time': {u'city': {u'endIndex': 162, u'startIndex': 146, u'value': u'New Orleans East'}, u'clock-time': {u'endIndex': 216, u'startIndex': 210, u'value': u'8 p.m.'}, u'time-day': {u'endIndex': 125, u'startIndex': 120, u'value': u'night'}, u'state': u'LA - Louisiana', u'details': {u'endIndex': 252, u'startIndex': 224, u'value': u'14400 block of Peltier Drive'}, u'date': u'2015-11-23'}, u'radio1': {u'The shooter and the victim knew each other.': u'Not mentioned', u'The firearm was used in self defense.': u'Not mentioned', u'The incident was a case of domestic violence.': u'Not mentioned', u'The firearm was used during another crime.': u'Not mentioned'}, u'radio3': {u'The shooting was unintentional.': u'Not mentioned', u'The firearm was owned by the victim/victims family.': u'Not mentioned', u'The shooting was by a police officer.': u'No', u'The shooting was directed at a police officer.': u'No', u'The firearm was stolen.': u'Not mentioned'}, u'radio2': {u'Alcohol was involved.': u'Not mentioned', u'The shooting was a suicide or suicide attempt.': u'No', u'Drugs (other than alcohol) were involved.': u'Not mentioned', u'The shooting was self-directed.': u'No'}, u'victim-section': [{u'victim-was': [u'killed'], u'gender': u'Male', u'age': {u'endIndex': 88, u'startIndex': 77, u'value': u'48-year-old'}, u'race': {u'endIndex': -1, u'startIndex': -1, u'value': u''}, u'name': {u'endIndex': -1, u'startIndex': -1, u'value': u''}}], u'shooter-section': [], u'circumstances': {u'number-of-shots-fired': {u'endIndex': -1, u'startIndex': -1, u'value': u''}, u'type-of-gun': {u'endIndex': -1, u'startIndex': -1, u'value': u''}}}
</code></pre>

Here, the keys correspond to the information we asked the workers to extract in our HIT, and the values correspond the their responses. Since not all articles contain the same information, each record is slightly different (e.g. the list in of shooters in <code>shooter-section</code> might be empty or might contain 10 shooters). In general, each record has seven top-level keys: information about the shooter(s) (names, ages, etc.), information about the victim(s), and information about the time/place, and four keys containing other circumstances surrounding the shooting. 

Each record should be structured like shown below. In the examples, STRING means the answer will be a single string, DICT means the answer will be a dictionary, and LIST means the answer will be a list of dictionaries. For DICTs, you will mostly just be interested in the 'value' field. (You will also see start/end index fields, which tell you the span in the original article where the answer appears. You don't need to use this information.)

<pre><code>>> record = data[17]
>> record.keys()
['date-and-time', 'radio1', 'radio3', 'radio2', 'victim-section', 'shooter-section', 'circumstances']

>> record['date-and-time']
{'city': DICT, 'clock-time': DICT, 'time-day': DICT, 'state': STRING, 'details': DICT, 'date': STRING}

>> record['circumstances'] #Details about the gun/shots
 {'number-of-shots-fired': DICT, 'type-of-gun': DICT}

>> record['radio1'] #Details about the circumstances of the shooting 
{'The shooter and the victim knew each other.': STRING, 'The firearm was used in self defense.': STRING, 'The incident was a case of domestic violence.': STRING, 'The firearm was used during another crime.': STRING}

>> record['radio2'] #More details about the circumstances of the shooting 
{'Alcohol was involved.': STRING, 'The shooting was a suicide or suicide attempt.': STRING, 'Drugs (other than alcohol) were involved.': STRING, 'The shooting was self-directed.': STRING}

>> record['radio3'] #Even more details about the circumstances of the shooting 
{'The shooting was unintentional.': STRING, 'The firearm was owned by the victim/victims family.': STRING, 'The shooting was by a police officer.': STRING, 'The shooting was directed at a police officer.': STRING, 'The firearm was stolen.': STRING}

>> record['shooter-section'] 
[{u'gender': STRING, u'age': DICT, u'race': DICT, u'name': DICT}]


>> record['victim-section']
[{'victim-was': LIST, 'gender': STRING, 'age': DICT, 'race': DICT, 'name': STRING}]

</code></pre>

The best way to get comfortable with the data is just to play around with it. Write some code to parse/print different values from the data until you feel reasonably comfortable manipulating and accessing the data you need. 

<h3>Deduping the data</h3>

As we've discussed before, our method for collecting articles (scraping the [Gun Report blog](http://nocera.blogs.nytimes.com/category/gun-report/?_r=0) and training classifiers for arbitrary news articles) isn't perfect. It is highly likely that we have duplicated articles in our dataset, or multiple different articles reporting on the same incident. So, its probably a good idea to [dedoop](https://www.youtube.com/watch?v=AH-AHEsGJWw) the data. 

There is no fool-proof way of doing this, so we will just use some intuitive rules for merging two records into one. 

1. Write a script to identify records which share the same victim name. 
2. Of records which share a victim, consider them "potential duplicates" if they either share a shooter name or if one of the records' shooters is "unknown". Look at 10-15 of these "potential duplicates" manually. How many of these are follow-on articles which actually add information (e.g. the shooter name was not previously released, but is now known) and how many are actually just redundant (e.g. multiple reports about high-profile shootings like the Zimmerman/Martin case). 
3. Write a script which iterates through the records and attempts to merge records when possible. You can merge records which match on at least two of shooter_name/victim_name/date. A good pseudocode for your de-duplication algorithm might be: 

	<pre><code>records = json.load(open('aggregated-data.json'))
	deduped = empty set of records

	def can_merge(this, that) : return True if this/that share two of shooter/victim/date

	add records[0] to deduped

	for this_record in records : 
	   for that_record in deduped : 
	      if can_merge(this_record, that_record) : 
	         update fields in deduped with new information added by this_record
	      else : 
	         add this_record to deduped
	</code></pre>

4. Save your dedupped records to a new file. You can save an object in json format like this:

	<pre><code>json.dump(deduped, open('deduped-data.json', 'w'))</code></pre>

##The Gun ReReport

Now you have a hopefully fairly clean, de-duplicated set of data to work with. Lets ask some questions, and answer them with some figures. Below are instructions for producing four graphs looking at different aspects of the data. Choose two which you find especially interesting and reproduce them using the Google charts API. Each of the API documentation pages gives you an html template you can use, and its usually just as easy as pasting in your own data into the template. You can open the html templates in any browser to look at your results. 

After you have reproduced two of our figures, produce two more plots, charts, or graphs showing any dimension of the data you want to explore. You will answer [a few questions](https://docs.google.com/forms/d/1m6LFLPzvjRxZTRmaCIayy9oJmQrnppa3riYUgtH0wz0/viewform) afterward. 

###When

First, lets see when shootings happen most often. This will help me decide when are the best times to walk around alone with my wallet in plain view, while texting on my iPhone in the most visibly distracted way. Do do this, we can make a basic [Line Chart](https://developers.google.com/chart/interactive/docs/gallery/linechart).

<div id="time_chart"></div>

###Where

Back when Doug talked to us, he mentioned that intentional shootings might be more common in urban areas, but accidental shootings are very common in rural areas. Does our data reflect this? We can plot our incidents by location using the [Google Geo Chart](https://developers.google.com/chart/interactive/docs/gallery/geochart). Here you can see it plotted by state (since the page loads faster that way...), but its more interesting when plotted by city. Try plotting the number of intentional shootings (left) and unintentional shootings (right) by city. 

<table><tr>
<td><div id="intentional_div" style="width: 400; height: 150px;"></div></td>
<td><div id="unintentional_div" style="width: 400px; height: 150px;"></div></td>
</tr></table>

###Who

Most of the records do not contain data about race. But for those that do, we can see some interesting results. Try using the [stacked bar graph](https://developers.google.com/chart/interactive/docs/gallery/columnchart#StackedColumns) to produce a graph like this one. You are welcome to try looking at this slighly differently- e.g. including information about age or gender instead of or in addition to information about race.

<div id="race_div" style="width: 500px; height: 175;"></div>

###How

The information we collected about "type of gun" is not very structured, but we can still pull out some high-level information. By looking through the records and counting the "type of gun" strings with contain the words "rifle", "shotgun", "pistol", "revolver", and "handgun", we can get a sense of how often each type of gun was used. Using the [Diff Charts API](https://developers.google.com/chart/interactive/docs/gallery/diffchart) we can make it more interesting by comparing how the gun types are different between fatal shootings (inner circle) and non-fatal shootings (outer circle).

<div id="guns_div" style="width: 500px; height: 175;"></div>

###Tell us something cool

Create any two plots you want to display something interesting from the data. One trick for making your graphs instantly more interesting (and for forcing yourself to ask deeper questions) is to always display multiple dimensions at a time. Shootings over time of day? Boring. Fatal vs. non-fatal shootings by time of day and age of shooter? So much more cool!! Keep in mind all of the types of data we collected and try to think of meaningful questions you can ask. E.g. 

- Look at how is the type of gun used varies based on location. Age? Gender?
- Look at a subset of the data- just domestic violence shootings, or self-defense shootings.
- Try looking at the articles' text for a more qualitative analysis; there are great [tools available for building word clouds](https://github.com/Coppersmith/vennclouds). Eg. how is the text of different for intentional vs. unintentional shootings? 
- Extra credit if you link up with an external resource. E.g. can you say anything about shootings in a city as a function of [the average income](http://www.census.gov/compendia/statab/cats/income_expenditures_poverty_wealth/income_and_poverty--state_and_local_data.html) or the city's [spending on law enforcement](http://www.census.gov/compendia/statab/cats/law_enforcement_courts_prisons/criminal_justice_expenditures.html)?

##Deliverables

This assignment is due <b>Monday, November 24</b>. You can work in pairs, but you must declare the fact that you are working together when you turn your assignment. Remember to submit your questionnaire before the deadline.  

1. Your de-duplicated data, in json format.
2. Two figures from our analysis, which you reproduced, as html files.
3. Your own two figures, as html, png, or pdf files.
4. Your answers to the [questionnaire](https://docs.google.com/forms/d/1m6LFLPzvjRxZTRmaCIayy9oJmQrnppa3riYUgtH0wz0/viewform). 

You can turn in your figures using 

	$ turnin -c nets213 -p the-end -v *


Related Projects
================
* [Vox - 11 facts about gun violence in the United States](http://www.vox.com/cards/gun-violence-facts/guns-international-comparison-us-homicide)
* [Vox - Mass shootings since Sandy Hook, in one map](http://www.vox.com/a/mass-shootings-sandy-hook)
* [The Guardian - 994 mass shootings in 1,004 days](http://www.theguardian.com/us-news/ng-interactive/2015/oct/02/mass-shootings-america-gun-violence)
* [The Guardian - The Counted: People Killed by Police in the USA](http://www.theguardian.com/us-news/ng-interactive/2015/jun/01/the-counted-map-us-police-killings#)
* [Mass killings in the United States](http://www.gannett-cdn.com/GDContent/mass-killings/)
* [Mass killings in the USA by Muslims and non-Muslims](assets/img/2015-mass-shootings-visualization.jpg)
