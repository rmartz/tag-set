#!/opt/local/bin/python

from tagsets import TagSet
from pprint import pprint

library = TagSet()

sample_tags = [ 
	['mountain', 'trees', 'river'],
	['mountain', 'trees'],
	['mountain', 'trees'],
	['mountain', 'snow', 'river'],
	['forest', 'trees', 'snow'],
	['trees', 'snow'],
	['city', 'road', 'cars'],
	['city', 'road', 'cars'],
	['city', 'road', 'cars'],
	['mountain', 'road'],
	['zzzz','aaaa'],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

for tags in sample_tags:
	library.add(tags)


pprint( library.flatten() )


tests = [
	[],
	['mountain'],
	['snow'],
	['trees','snow'],
	['cars', 'city', 'road'],
	['cars'],
	['zzzz'],
	['snow', 'invalid1', 'invalid2']
]
for test in tests:
	pprint(test)
	pprint( library.GetOdds(test ) )
