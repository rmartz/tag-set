#!/usr/bin/python

from powerset import PowerSet
from pprint import pprint

pprint(PowerSet([ ]))
pprint(PowerSet([ 'a' ]))
pprint(PowerSet([ 'a', 'b' ]))
pprint(PowerSet([ 'a', 'b', 'c' ]))
pprint(PowerSet([ 'a', 'b', 'c', 'd' ]))

