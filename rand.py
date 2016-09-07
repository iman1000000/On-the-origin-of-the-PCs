import random

def weightedSelect (elements, weights):
	totalWeight = sum (weights)
	r = random.random () * totalWeight
	index = 0
	for w in weights:
		r -= w
		if r<= 0:
			return elements [index]
		index += 1
	return elements [-1]
