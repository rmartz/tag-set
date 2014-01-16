from tagsets import TagSet
from iptcinfo import IPTCInfo
from functions import GetFileList

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

	def __init__(self, IgnoreCase = True,
		     BlacklistedTags = None, IgnoredTags = None,
		     Directories = [], Extensions = ['jpeg', 'jpg']):
		self.images = []
		self.BlacklistedTags = ([] if BlacklistedTags is None
		                        else BlacklistedTags)
		self.IgnoredTags = ([] if IgnoredTags is None
		                    else IgnoredTags)

		self.tagset = TagSet(CaseInsensitive = IgnoreCase)

		regex = '.*.({})$'.format("|".join(Extensions))
		for dir in Directories:
			self.addDirectory(dir, regex)

	def addDirectory(self, dir, regex = '.*.jp[e]?g$'):
		for file in GetFileList(dir, regex):
			self.addImage(file)

	def addImage(self, filename):
		try:
			image = Image(self, filename)
		except RuntimeError:
			# Couldn't create the image
			return
		self.tagset.add(image.tags)
		self.images.append(image)
