from powerset import PowerSet

class TagSet:
	count = 0
	
	def __init__(self):
		self.tags = {}
		self.count = 0

def CreateTagSet(tag_sets):
	result = TagSet()
	for tags in tag_sets:
		tags.sort()
		TagSetAdd(result, tags)
	return result

def FlattenTagSet(node, path = []):
	key = ",".join(path)
	tags = ",".join(node.tags)	

	#print("=== '{}' (count: {}): {}".format(key, node.count, tags))
	result = { ",".join(path): node.count}
	for tag, subnode in node.tags.items():
		MergeDictionary(result, FlattenTagSet(subnode, path + [tag]))
	return result

def MergeDictionary(dest, src):
	for key, value in src.items():
		dest[key] = value

def GetTagOdds(root, tags):
	tags.sort()
	result = {}
	
	powerset = PowerSet(tags)

	for set in powerset:
		try:
			base = TagSetSearch(root, set)
		except LookupError:
			continue
		
		for tag, node in base.tags.items():
			odds = (1.0 * node.count) / base.count
			try:
				odds = max(odds, result[tag])
			except KeyError:
				pass
			result[tag] = odds

	return result
	
def TagSetSearch(root, tags):
	node = root
	for tag in tags:
		try:
			node = node.tags[tag]
		except KeyError:
			raise LookupError()
	return node

def TagSetAdd(root, tags):
	powerset = PowerSet(tags)
	for set in powerset:
		node = root
		for tag in set:
			#print tag, id(node), node.count
			try:
				node = node.tags[tag]
			except KeyError:
				node.tags[tag] = TagSet()
				#print("Creating entry {} ({}) in {}".format(tag, id(node.tags[tag]), id(node)))
				node = node.tags[tag]
		node.count += 1

