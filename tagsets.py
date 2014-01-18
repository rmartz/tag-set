from functions import PowerSet, OddManOut, MergeDictionary
import operator

class TagSet:
	count = 0
	tags = None
	
	def __init__(self):
		self.tags = {}
		self.count = 0

	# Adds a set of tags to the library and updates all relevant counts
	def add(self, tags):
		tags = self.__cleanTags(tags)

		# For every tag we have, get the powerset of every other tag,
		#  then create a reference to that tag.
		for tag, remainder in OddManOut(tags):
			for path in PowerSet(remainder):
				self.addTagToPath(path, tag)

		# Add a reference to the root
		self.count += 1

	def addTagToPath(self, path, tag):
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
		tags = self.__cleanTags(tags)
		result = {}
		
		for set in PowerSet(tags):
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
					result[tag] += odds
				except KeyError:
					result[tag] = odds
		# Now that we're done, let's sort our output
		return sorted(result.iteritems(), key=operator.itemgetter(1))

	def __cleanTags(self, tags):
		# We want to:
		# * Sort
		# * Remove duplicates
		
		return list(set(tags))
