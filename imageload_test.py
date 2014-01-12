#!/opt/local/bin/python
from imageload import ImageLibrary, GetImageList
from pprint import pprint
from random import choice

try:
	f = open('./testing_dir.path')
	dir = f.readline().rstrip()
except IOError:
	dir = './img/'
print dir

print "Testing GetImageList"
pprint(GetImageList(dir))

library = ImageLibrary()
library.load(dir)

print "Testing library.load"
pprint(library.tagset.flatten())

print "Testing library.GetOdds"
image = choice(library.images)
pprint(image.tags)
pprint(image.GetOdds())

print "Done"	
