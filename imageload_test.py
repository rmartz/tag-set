#!/opt/local/bin/python
from imageload import GetImageList, InitializeLibrary
from pprint import pprint

pprint(GetImageList('.'))

library = InitializeLibrary('.')

pprint(library.flatten())
