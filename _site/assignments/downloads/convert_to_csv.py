#!/bin/python

import sys
import csv 

csvfile = open('tweets.csv', 'wb')

csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for line in sys.stdin:
    	csvwriter.writerow(line.strip().split('\t'))

csvfile.close()
