from functions import PowerSet, OddManOut, MergeDictionary

class TagSet:
	count = 0
	
	def __init__(self):
		self.tags = {}
		self.count = 0

	# Adds a set of tags to the library and updates all relevant counts
	def add(self, tags):
		tags.sort()

		# For every tag we have, get the powerset of every other tag,
		#  then create a reference to that tag.
		for tag, remainder in OddManOut(tags):
			powerset = PowerSet(remainder)
			for set in powerset:
				self.addTag(set, tag)
		self.count += 1

	def addTag(self, path, tag):
		node = self.search(path+[tag], create = True)
		node.count += 1

	# Runs through the TagSet to find a given node.
	def search(self, tags, create = False):
		node = self
		for tag in tags:
			try:
				node = node.tags[tag]
			except KeyError:
				if create:
					node.tags[tag] = TagSet()
					#print("Creating entry {} ({}) in {}".format(tag, id(node.tags[tag]), id(node)))
					node = node.tags[tag]
				else:
					raise LookupError()
		return node


	# Flattens the TagSet into a dictionary of {path: count}
	def flatten(self, path = []):
		result = { ",".join(path): self.count}
		for tag, subnode in self.tags.items():
			MergeDictionary(result, subnode.flatten(path + [tag]))
		return result

	# This returns a list of suggested tags and their predicted relevance
	def GetOdds(self, tags):
		tags.sort()
		result = {}
		
		powerset = PowerSet(tags)

		for set in powerset:
			try:
				base = self.search(set)
			except LookupError:
				continue
			
			for tag, node in base.tags.items():
				# Check if this tag was part of our start
				# Don't include it in the output if it's already present
				if tag in tags:
					continue

				odds = (1.0 * node.count) / base.count
				try:
					odds = max(odds, result[tag])
				except KeyError:
					pass
				result[tag] = odds

		return result
