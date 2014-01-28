#!/opt/local/bin/python

from tagsets import TagSet
from pprint import pprint


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
	['Multikey1', 'Multikey2', 'Multivalue', 'Multisubvalue'],
	['Multikey1', 'Multikey2', 'Multivalue'],
	['Singlekey', 'Singlevalue', 'Singlesubvalue'],
	['Singlekey', 'Singlevalue'],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

library = TagSet()
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
	['snow', 'invalid1', 'invalid2'],
	['Multikey1', 'Multikey2'],
	['Singlekey']
]
for test in tests:
	pprint(test)
	pprint( library.GetOdds(test ) )
