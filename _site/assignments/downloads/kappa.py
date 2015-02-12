import sys

def read_ratings(filename) : 
	ratings = {}
	dist = {}
	for line in open(filename).readlines() : 
		url, r = line.strip().split('\t')
		ratings[url] = r
		if r not in dist : dist[r] = 0.0
		dist[r] += 1
	return ratings, dist

rating1, dist1 = read_ratings(sys.argv[1])
rating2, dist2  = read_ratings(sys.argv[2])
total1 = sum([v for v in dist1.itervalues()])
total2 = sum([v for v in dist2.itervalues()])

Pa = 0.0
Pe = 0.0 

for url in rating1 : 
	if rating1[url] == rating2[url] : Pa += 1

Pa = Pa / total1 

for r in dist1 : 
	Pe += ((dist1[r] / total1) * (dist2[r] / total2))

k = (Pa - Pe) / (1 - Pe)
print "kappa = %f"%k

