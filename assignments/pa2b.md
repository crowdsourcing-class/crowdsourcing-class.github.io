<ul id="ProjectSubmenu">
    <li><a class="home" href="../index.html" title="Home">Home</a></li>
    <li><a class="syllabus" href="../syllabus.html" title="Lectures">Lectures</a></li>
    <li><a class="assignments" href="../assignments.html" title="Assignments">Assignments</a></li>
    <li><a class="resources" href="../resources.html" title="Resources">Readings</a></li>
</ul>

<link rel="stylesheet" type="text/css" href="../stylesheet.css" />

# Crowdsourcing and Human Computation

##Programming Assignment 2 : Due Wednesday, September 18

Now that you have data from MTurk, let's take a look at your results. We will make use of [Google Charts API](https://google-developers.appspot.com/chart/interactive/docs/index), probably Google's single greatest contribution to society at large. This will allow us generate fancy looking charts without having to have any artistic vision or skill. 

Download this [brute force python script](downloads/visualize_data.py) and run it like so:

- <code>$ python visualize&#95;.py hits.csv > hit_analysis.html</code>

This will generate some html and javascript for you, and you should be able to open the the html file in your browser. You should see the distribution of the labels you received. Click on the bars to see the tweets that received that label (clicking on the tweet text will scroll advance you through all the tweets). 

<b>Note</b>: The python script assumes that the answers you received from the turkers are the string <code>['strongly negative', 'negative', 'neutral', 'positive', 'strongly positive']</code>. If you saved turkers' answers using some other labeling, you will need to edit lines 26 and 27 to reflect this.

You should turn in:

- A screen shot of your Requester page showing your HITs are posted and/or are in progress
- Your <code>hits.csv</code> file, with your Turkers' answers
- <code>hit_analysis.html</code>, with your visualization of the data
- Some intelligent and/or interesting observation about your data. Are the tweets skewed in one direction? Why do you think that is? Is agreement high? Is it higher for positive tweets than for negative tweets? What are some especially ambiguous tweets? 
