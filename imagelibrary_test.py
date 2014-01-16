#!/opt/local/bin/python
from imagelibrary import ImageLibrary
from pprint import pprint
from random import choice

try:
	f = open('./testing_dir.path')
	dir = f.readline().rstrip()
except IOError:
	dir = './img/'
print dir

library = ImageLibrary()
library.addDirectory(dir)

pprint(library.tagset.flatten())

# Test a random image
image = choice(library.images)
pprint(image.tags)
pprint(image.GetOdds())

