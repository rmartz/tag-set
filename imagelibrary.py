from tagsets import TagSet
from iptcinfo import IPTCInfo
from functions import GetFileList
from json import JSONEncoder

class Image:
	tags = None
	path = ''
	library = None

	def __init__(self, library, path):
		self.path = path
		self.library = library

		try:
			info = IPTCInfo(path)
			self.tags = info.keywords
		except Exception:
			# The image doesn't have any IPTC data
			raise RuntimeError()

	def GetOdds(self):
		return self.library.tagset.GetOdds(self.tags)

class ImageLibrary:
	tagset = None
	images = None

	# List of keywords that will be excluded from suggestions
	BlacklistedTags = []

	# List of keywords not to be used for predictions
	IgnoredTags = []

	# List of tags with a common meaning
	GroupedTags = []

	# Should different case represent different tags for predictions?
	CaseSensitive = False

	def __init__(self, CaseSensitive = False, GroupedTags = None, 
                     BlacklistedTags = None, IgnoredTags = None, 
                     Directories = [], Extensions = ['jpeg', 'jpg']):
		self.images = []
		self.tagset = TagSet()
		
		self.CaseSensitive = CaseSensitive
		
		self.BlacklistedTags = ([] if BlacklistedTags is None
		                        else BlacklistedTags)
		self.IgnoredTags = ([] if IgnoredTags is None
		                    else IgnoredTags)
		self.GroupedTags = ([] if GroupedTags is None
		                    else GroupedTags)

		regex = '.*.({})$'.format("|".join(Extensions))
		for dir in Directories:
			self.addDirectory(dir, regex)

	@staticmethod
	def fromJSON(path):
		pass

	def toJSON():
		return ''

	def addDirectory(self, dir, regex = '.*.jp[e]?g$'):
		for file in GetFileList(dir, regex):
			self.addImage(file)

	# This creates a list of tags suitable for use in predictions
	def formatTags(self, tags):
		
		if self.CaseSensitive:
			tags = [str.toLower() for str in tags]
		
		# Remove ignored tags
		# TODO

		# Simplify tag groups
		# TODO

		return tags

	def addImage(self, filename):
		try:
			image = Image(self, filename)
		except RuntimeError:
			# Couldn't create the image
			return
		
		tags = self.formatTags(image.tags)
		self.tagset.add(tags)
		
		self.images.append(image)

