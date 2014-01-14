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

	def __init__(self):
		self.tagset = TagSet(CaseInsensitive = True)
		self.images = []

	def load(self, dir):
		for file in GetFileList(dir, '.*.jp[e]?g$'):
			self.addImage(file)

	def addImage(self, filename):
		try:
			image = Image(self, filename)
		except RuntimeError:
			# Couldn't create the image
			return
		self.tagset.add(image.tags)
		self.images.append(image)
