import sys
import csv
import optparse

def print_labels(file) : 
	for row in csv.DictReader(open(file)) : 
		print row['url'], '\t', row['does_this_article_describe_gun_violence']

def print_qualities(file) : 
	for row in csv.DictReader(open(file)) : 
		if float(row['judgments_count']) > 0 : print '%s\t%s'%(row['worker_id'], row['trust_overall'])

if __name__ == '__main__' : 

	optparser = optparse.OptionParser()
	optparser.add_option("-d", dest="data_file", help="Crowdflower csv file.")
	optparser.add_option("-m", dest="mode", help="Worker quality ('worker') or data quality ('data')")
	
	(opts, _) = optparser.parse_args()

	if opts.mode == 'worker' : print_qualities(opts.data_file)
	elif opts.mode == 'data' : print_labels(opts.data_file)
