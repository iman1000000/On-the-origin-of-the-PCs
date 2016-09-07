import csv

def load (fileName):
	dat = []
	with open (fileName, newline='') as csvfile:
		colMap = {}
		rows = csv.reader (csvfile, delimiter=',', quotechar='|')
		columns = rows.__next__ ()
		
		for r in rows:
			index = 0
			c = {}
			for e in r:
				c [columns [index]] = e
				index += 1
			dat.append (c)
	return dat
