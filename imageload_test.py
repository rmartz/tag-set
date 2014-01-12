#!/opt/local/bin/python
from imageload import ImageLibrary, GetImageList
from pprint import pprint


dir = '.'
pprint(GetImageList(dir))

library = ImageLibrary()
library.load(dir)

pprint(library.tagset.flatten())
