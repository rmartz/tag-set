#!/opt/local/bin/python

from functions import PowerSet, OddManOut
from pprint import pprint

pprint(PowerSet([ ]))
pprint(PowerSet([ 'a' ]))
pprint(PowerSet([ 'a', 'b' ]))
pprint(PowerSet([ 'a', 'b', 'c' ]))
pprint(PowerSet([ 'a', 'b', 'c', 'd' ]))

pprint(OddManOut(['a']))
pprint(OddManOut(['a', 'b']))
pprint(OddManOut(['a', 'b', 'c']))
pprint(OddManOut(['a', 'b', 'c', 'd']))
