#!/usr/bin/env python3

import data
import rand

character = {}

classes = data.load ('Frequency sheet - Classes.csv')
races = data.load ('Frequency sheet - Races.csv')

names, weights = data.extractNamesWeights (classes)
character ['class'] = rand.weightedSelect (names, weights)

names, weights = data.extractNamesWeights (races)
character ['race'] = rand.weightedSelect (names, weights)

print (character)
