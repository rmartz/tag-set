import re, os

def PowerSet(start):
	# Copy the list before we modify it
	arg = list(start)
	return __PowerSet(arg)

def __PowerSet(start):
	if not start:
		yield [ ]
		return

	first = start.pop(0)

	for set in __PowerSet(start):
		yield [first]+set
		yield set

# Creates a set for every item that has every element but itself.
# (e.g, [a,b,c] => [[a, [b,c]], [b, [a,c]], [c, [a,b]]])
def OddManOut(start):
	for key in start:
		value = list(start)
		value.remove(key)
		yield [key, value]

# Copies all the entries in src to dest, overwriting existing ones
def MergeDictionary(dest, src):
	for key, value in src.items():
		dest[key] = value
	return dest

# A generator that finds all files that match a regex in a given directory
def GetFileList(dir, regex):
	p = re.compile(regex)
	for root, subFolders, files in os.walk(dir):
		for file in files:
			if p.match(file):
				yield os.path.join(root,file)

