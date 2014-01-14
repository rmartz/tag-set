#!/opt/local/bin/python

from tagsets import TagSet
from pprint import pprint


sample_tags = [ 
	['mountain', 'trees', 'river'],
	['Mountain', 'trees'],
	['moUntain', 'trees'],
	['mountain', 'snow', 'river'],
	['forest', 'Trees', 'snow'],
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

library = TagSet(CaseInsensitive = True)
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
