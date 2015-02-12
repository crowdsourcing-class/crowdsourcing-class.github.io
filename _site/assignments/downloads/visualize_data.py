#!/bin/python

import sys
import csv
import cgi
import operator

#html escape function stolen from http://stackoverflow.com/questions/2077283/substitute-special-characters-with-html-entities-in-python
def escape(t): return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&#39;").replace('"', "&quot;"))

#Compile dictionary {tweet : {number of votes for each label}}
def get_tweet_data_from_csv(csv_path):
	tweet_data = dict()
	for hit in csv.DictReader(open(csv_path)):
		for i in range(0,10): 
			tweetId = '%s-%d'%(hit['HITId'],i)
			#TODO if your tweet labels, in your csv file are not the strings below, you will have to edit this function
			if tweetId not in tweet_data : tweet_data[tweetId] = {
			'strongly positive' : 0, 
			'positive' : 0, 
			'negative' : 0, 
			'neutral' : 0 , 
			'strongly negative' : 0, 
			'text' : escape(hit['Input.tweet%d'%i])
			}
			label = hit['Answer.Q%d'%i]
			tweet_data[tweetId][label] += 1
	return tweet_data 
	
csv_path = sys.argv[1]

tweet_data_dump = get_tweet_data_from_csv(csv_path)
tweet_data = [tweet_data_dump[d] for d in tweet_data_dump]

#highly unelegant code to produce the html/javascript for you

print '<html>'
print '\t<head>'
print '\t<script type="text/javascript" src="https://www.google.com/jsapi"></script>'
print '\t<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js"></script>'
print '\t<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>'
print '\t<script type="text/javascript">'
print ''
print '\tsentiment_data = ['

print "['Sentiment', 'Strongly Negative', 'Negative', 'Neutral', 'Positive', 'Strongly Positive'],"
sng = sum([d['strongly negative'] for d in tweet_data])
ng = sum([d['negative'] for d in tweet_data])
nu = sum([d['neutral'] for d in tweet_data])
ps = sum([d['positive'] for d in tweet_data])
sps = sum([d['strongly positive'] for d in tweet_data])
print "['Count', %d, %d, %d, %d, %d],"%(sng, ng, nu, ps, sps)

print "];"

print '\tvar tweets = {'

scored_tweets = {'strongly_positive' : [], 'positive' : [], 'negative' : [], 'neutral' : [], 'strongly_negative' : []}

for tweet in tweet_data:
	sng = tweet['strongly negative']
	ng = tweet['negative']
	nu = tweet['neutral']
	ps = tweet['positive']
	sps = tweet['strongly positive']
	total = sng + ng + nu + ps + sps
	raw = 0*sng + 25*ng + 50*nu + 75*ps + 100*sps
	score = float(raw)/total
	if sng > 0 : scored_tweets['strongly_negative'].append((tweet['text'], score))
	if ng > 0 : scored_tweets['negative'].append((tweet['text'], score))
	if nu > 0 : scored_tweets['neutral'].append((tweet['text'], score))
	if ps > 0 : scored_tweets['positive'].append((tweet['text'], score))
	if sps > 0 : scored_tweets['strongly_positive'].append((tweet['text'], score))

for label in scored_tweets:
	print '%s : ['%label
	for tweet in scored_tweets[label]:
		print "[['Tweet', 'Value'],['%s',%.03f]],"%tweet
	print '],'

print '\t};'

print '\tvar i = -1;'
print '\tvar tweet_set = tweets.neutral;'
print '        var gauge_options = {'
print '       \t\twidth: 600, height: 180,'
print '       \t\tredFrom: 0, redTo: 40,'
print '       \t\tyellowFrom:40, yellowTo: 60,'
print '       \t\tgreenFrom:60, greenTo: 100,'
print '       \t\tminorTicks: 5'
print '       \t};'
print ''
print '\tgoogle.load("visualization", "1", {packages:["corechart", "gauge"]});'
print '\tgoogle.setOnLoadCallback(drawChart);'
print ''
print '\t$(document).ready(function() { update(); });'
print ''
print '\tfunction drawChart() {'
print '      \t\tvar data = google.visualization.arrayToDataTable(sentiment_data);'
print '\t\tvar options = {'
print '\t\t\ttitle: "Tweet Sentiment for Apple",'
print '\t\t\tcolors : ["red", "#FF6600", "yellow", "#66FF00", "green"],'
print '\t\t};'
print '       \t\tvar chart = new google.visualization.ColumnChart(document.getElementById("chart_div"));'
print '\t\tchart.draw(data, options);'
print '\t\tgoogle.visualization.events.addListener(chart, "select", selectHandler);'
print ''
print '\tfunction selectHandler(e) {'
print '\t\ti = 0'
print ' \t\titem = chart.getSelection()[0];'
print '\t\t'
print ' \t\t sentiment = sentiment_data[0][item.column];'
print ''
print '\t\t if(sentiment == "Strongly Positive"){ tweet_set = tweets.strongly_positive };'
print '\t\t if(sentiment == "Positive"){ tweet_set = tweets.positive };'
print '\t\t if(sentiment == "Neutral"){ tweet_set = tweets.neutral };'
print '\t\t if(sentiment == "Negative"){ tweet_set = tweets.negative };'
print '\t\t if(sentiment == "Strongly Negative"){ tweet_set = tweets.strongly_negative};'
print ''
print '\t\ttweet_data = tweet_set[i]; '
print '\t\t'
print '\t\tvar data2 = google.visualization.arrayToDataTable([tweet_data[0], ["", tweet_data[1][1]]]);'
print '        \t'
print '\t\tvar chart2 = new google.visualization.Gauge(document.getElementById("gauge_div"));'
print '\t\t$("#gauge_span").text(tweet_set[i][1][0]);'
print '        \tchart2.draw(data2, gauge_options);'
print '\t\t'
print '      \t}'
print '\t}'
print ''
print '\tfunction update(){'
print ''
print '\t\ti += 1;'
print ''
print '\t\ttweet_data = tweet_set[i]; '
print '\t\tvar data2 = google.visualization.arrayToDataTable([tweet_data[0], ["", tweet_data[1][1]]]);'
print '\t\t'
print '\t\tvar chart2 = new google.visualization.Gauge(document.getElementById("gauge_div"));'
print '\t\t$("#gauge_span").text(tweet_set[i][1][0]);'
print '        \tchart2.draw(data2, gauge_options);'
print '\t}'
print '      '
print '\t</script>'
print '\t</head>'
print '\t<style type="text/css">'
print '\t\t'
print '\t\tbody {'
print '\t\t\tfont-family : sans-serif;'
print '\t\t\tfont-size: "20pt";'
print '\t\t}'
print '\t\t'
print '\t</style>'
print '\t<body>'
print '\t\t<table>'
print '\t\t<tr><td colspan="2"><div id="chart_div" style="width: 800px; height: 400px;"></div></td></tr>'
print '\t\t<tr>'
print '\t\t\t<td width="60%" align="center">'
print '\t\t\t\t<div id="gauge_div"></div>'
print '\t\t\t</td>'
print '\t\t\t<td width="40%" align="center">'
print '\t\t\t\t<span id="gauge_span" onclick="update()"></span>'
print '\t\t\t</td>'
print '\t\t</tr>'
print '\t\t</table>'
print '\t</body>'
print '</html>'
