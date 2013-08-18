#!/bin/python
"""
This code grades the HITs based on the embedded control tweets. 
It takes as input the csv file containing the submitted HITs.
It outputs hits_graded.csv, which contains the columns 'Approve' and 'Reject', one of which contains an 'X' for each HIT, according to the Turker's performance on controls.
"""
import sys
import csv 
import random

#DictReader returns an iterator object, so we can only iterate through the list once
#We use python's list-compression sytax to save the instances into a list that we can interate repeatedly
hit_data = [d for d in csv.DictReader(open(sys.argv[1]))]

csvwriter = csv.writer(open('hits_graded.csv','w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#Get the headers from the input file. We will use the same headers in the output file. 
headers = hit_data[0].keys()
csvwriter.writerow(headers)

#TODO: You may have used slightly different labelings when you annotated the gold standard tweets and when you recorded the Turkers' answers. You will need to map all the answers into a common notation so you can compare. For example, if you used 0=positive, 1=negative, 2=neutral in the HIT, fill that in here. If you used the same labeling in both cases, then these data structures will be unnecessary. That's okay, just fill them in anyway.

gold_labels = {'YOUR_POSITIVE_LABEL' : 'positive', 'YOUR_NEUTRAL_LABEL' : 'neutral', 'YOUR_NEGATIVE_LABEL' : 'negative'}
mturk_labels = {'YOUR_POSITIVE_LABEL' : 'positive', 'YOUR_NEUTRAL_LABEL' : 'neutral', 'YOUR_NEGATIVE_LABEL' : 'negative'}

#Grade each HIT
#Remember, here 'hit' is a dictionary data structure corresponding to one row of your input CSV. It maps the CSV headers to the corresponding values for each row.
for hit in hit_data:
	correct_control_answer = #TODO get the correct answer for the control from this row of the CSV 
	turker_control_answer = #TODO get the Turker's answer for the control tweet 
	if gold_labels[correct_control_answer] == mturk_labels[turker_control_answer] : 
		print 'Turker answered %s. Expected %s. Approving.' %(turker_control_answer, correct_control_answer)
		#TODO approve the worker by marking the appropriate column in the CSV
	else : 
		print 'Turker answered %s. Expected %s. Rejecting.' %(turker_control_answer, correct_control_answer)
		#TODO reject the worker by marking the appropriate column in the CSV
	csvwriter.writerow([hit[column] for column in headers])


