#!/usr/bin/python

from tagsets import CreateTagSet, FlattenTagSet, GetTagOdds
from pprint import pprint

library = CreateTagSet( [
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
	[],
	[]
			] )

pprint( FlattenTagSet( library ) )


tests = [
	[],
	['mountain'],
	['snow'],
	['trees','snow'],
	['cars', 'city', 'road'],
	['snow', 'invalid1', 'invalid2']
]
for test in tests:
	pprint(test)
	pprint( GetTagOdds( library, test ) )
