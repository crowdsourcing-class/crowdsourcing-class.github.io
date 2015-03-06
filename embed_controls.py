#!/bin/python
"""
This code takes produces a csv file which contains data for one HIT per line
It takes no parameters, but assumes the existence of tweets.csv, which contains one tweet per line, each of which may be either labeled or unlabeled
It outputs tweets_with_controls.csv, which contains one HIT (10 tweets, including one control) per line
"""
import sys
import csv 
import random

#convenience function to iterate through the tweets in batches of 9
#shamelessly stolen from stackoverflow : http://stackoverflow.com/questions/8290397/how-to-split-an-iterable-in-constant-size-chunks
def batch(iterable, n = 9):
   l = len(iterable)
   for ndx in range(0, l, n):
       yield iterable[ndx:min(ndx+n, l)]

#DictReader returns an iterator object, so we can only iterate through the list once
#We use python's list-compression sytax to save the instances into a list that we can interate repeatedly
data = [d for d in csv.DictReader(open('tweets.csv'))]

#The data you want labeled
unknowns = [d for d in data if not(d['label'])]
#The gold standard data you labeled yourself
knowns = [d for d in data if d['label']]
csvwriter = csv.writer(open('tweets_with_controls.csv','w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#Write a new csv file which will contain 9 tweets to be labeled and one embedded quality control 
#'tweet1'...'tweetn' will be the text of the tweets to be labeled
#'control' will be a number (1 through 10) denoting which of the tweets is the control
#'label' is the correct answer to the gold standard tweet
headers = ['tweet0', 'tweet1', 'tweet2', 'tweet3', 'tweet4', 'tweet5', 'tweet6', 'tweet7', 'tweet8', 'tweet9', 'control', 'label']
csvwriter.writerow(headers)

#Take groups of 9 unlabeled tweets
for i,batch in enumerate(batch(unknowns)):
	tweets = [b['tweet'] for b in batch]
	#grab the next gold standard tweet
	control = knowns[i] 
	#TODO choose a random position for the control
	tweets = [] #TODO construct a list of fields which will fill in the headers defined
	csvwriter.writerow(tweets)

