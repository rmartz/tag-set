from tagsets import TagSet
import os, sys

def InitalizeLibrary(dir):
	library = TagSet()

	files = GetFileList(dir)
	for file in files:
		AddFileToTagSet(library, file)
	return library

def GetFileList(dir):
	fileList = []
	for root, subFolders, files in os.walk(dir):
	    for file in files:
		fileList.append(os.path.join(root,file))
	return fileList

def AddFileToTagSet(tagset, filename):
	pass


