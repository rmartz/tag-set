#!/usr/bin/python

def PowerSet(start):
	if not start:
		return [ [] ]
	
	first = start.pop(0)
	subsets = PowerSet(start)

	result = []
	for set in subsets:
		result.append([first] + set)
	result += subsets

	return result
