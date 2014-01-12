#!/opt/local/bin/python
from imageload import ImageLibrary, GetImageList
from pprint import pprint

try:
	f = open('./imageload_test.dir')
	dir = f.readline().rstrip()
except IOError:
	dir = '.'
print dir

pprint(GetImageList(dir))

library = ImageLibrary()
library.load(dir)

pprint(library.tagset.flatten())
