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
try:
	while True:
		image = choice(library.images)
		odds = image.GetOdds()
		pprint(image.tags)
		pprint(odds[:10])

		raw_input("Press Enter to continue...")
except KeyboardInterrupt:
	print "Exiting."

