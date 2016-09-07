import csv

def load (fileName):
	dat = []
	with open (fileName, newline='') as csvfile:
		rows = csv.reader (csvfile, delimiter=',', quotechar='"')
		columns = rows.__next__ ()
		i=0
		for c in columns:
			columns [i] = c.strip ()
			i += 1
		
		for r in rows:
			index = 0
			c = {}
			for e in r:
				c [columns [index]] = e.strip ()
				index += 1
			dat.append (c)
	return dat


def groupBy (dat, col):
	ret = {}
	for d in dat:
		if d [col] not in ret:
			ret [d [col]] = []
		ret [d [col]].append (d)
	return ret


def extractNamesWeights (dat, name='Name', weight='Weight'):
	
	names = []
	weights = []
	
	if isinstance (dat, list):
		
		for e in dat:
			names.append (e [name])
			weights.append (float (e [weight]))
	
	return names, weights
