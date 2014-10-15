import sys
import random

students = [l.strip() for l in open(sys.argv[1]).readlines()]

projects = {}

for line in open(sys.argv[2]).readlines() : 
	team, name, url = line.strip().split('\t')
	if team not in projects : projects[team] = []
	projects[team].append((name,url))


assigned = {}
remaining = projects.keys()

for s in students : 
	teams = 0
	options = [k for k in remaining if not s in k.split(',')]
	if len(remaining) < 3 : remaining = projects.keys()
	while teams < 3 : 
		team = random.choice(list(set(options).intersection(remaining)))
		remaining.remove(team)
		for n,u in projects[team] :
			print '%s\t%s\t%s\t%s'%(s,team,n,u)
		teams += 1



