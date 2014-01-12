#!/opt/local/bin/python
from imageload import ImageLibrary, GetImageList
from pprint import pprint

try:
	f = open('./testing_dir.path')
	dir = f.readline().rstrip()
except IOError:
	dir = './img/'
print dir

pprint(GetImageList(dir))

library = ImageLibrary()
library.load(dir)

pprint(library.tagset.flatten())
