#!/opt/local/bin/python

from functions import PowerSet, OddManOut,MergeDictionary
from pprint import pprint

def test(function, arg):
	result = []
	for value in function(arg):
		result.append(value)
	return result
def testMany(function, args):
	print "Testing {}:".format(function.__name__)
	for arg in args:
		pprint(test(function, arg))

# Generate a sequence of letters - [[a], [a,b], ...]
alphabet = [map(chr, range(97, 97+n)) for n in range(1,5)]

testMany(PowerSet, alphabet)

testMany(OddManOut, alphabet)

print "Testing MergeDictionary:"
pprint(MergeDictionary({'a': 'good'}, {}))
pprint(MergeDictionary({'a': 'good'}, {'b': 'good'}))
pprint(MergeDictionary({'a': 'bad', 'b': 'good'}, {'a': 'good'}))
