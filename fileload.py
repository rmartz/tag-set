import re, os

def GetFileList(dir, regex):
	p = re.compile(regex)
	for root, subFolders, files in os.walk(dir):
		for file in files:
			if p.match(file):
				yield os.path.join(root,file)

