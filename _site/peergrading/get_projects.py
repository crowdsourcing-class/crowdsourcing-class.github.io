import csv
import sys

#Timestamp,Provide a link to your Vimeo video,Name of your project,Give a one sentence description of your project.,How many teammates are in your group?,Name 1,PennKey username 1,Name 2,Name 3,Name 4,PennKey username 2,PennKey username 3,PennKey username 4,What problem does it solve?,What similar projects exist?,What type of project is it?,Who will be the members of your crowd?,How will you incentivize them to participate?,"What will they provide, and what sort of skills do they need?",How will you ensure the quality of the crowd provides?,How will you aggregate the results from the crowd?,"Describe each of the steps involved in your process. What parts will be done by the crowd, and what parts will be done automatically.",How will you evaluate if your project is successful?,What potential problems do you foresee when implementing your project?

for line in csv.DictReader(open(sys.argv[1])) : 
	name = line['Name of your project']
	url = line['Provide a link to your Vimeo video']
	names = [line['PennKey username 1'], line['PennKey username 2'], line['PennKey username 3'],line['PennKey username 4']]
	print '%s\t%s\t%s'%(','.join(sorted([n.strip().lower() for n in names if not n == ''])),name,url)
