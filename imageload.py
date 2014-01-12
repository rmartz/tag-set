from tagsets import TagSet
from iptcinfo import IPTCInfo
import re, os, sys

def InitializeLibrary(dir):
	library = TagSet()

	files = GetImageList(dir)
	for file in files:
		AddFileToTagSet(library, file)
	return library

def GetImageList(dir):
	p = re.compile('.*.jp[e]?g$')
	
	fileList = []
	for root, subFolders, files in os.walk(dir):
	    for file in files:
		if p.match(file):
			fileList.append(os.path.join(root,file))
	return fileList

def AddFileToTagSet(tagset, filename):
	tags = GetImageIPTCKeywords(filename)
	tagset.add(tags)

def GetImageIPTCKeywords(filename):
	info = IPTCInfo(filename)
	if len(info.data) < 3: raise Exception(info.error)

	return info.keywords
