


def Cache:
	# This determines if we should write from the cache to update the store
	def ShouldCommit(self):
		return CacheLastUpdate() < CacheLastCommit()

	# This determines if we should read from the store to update the cache
	def ShouldLoad(self):
		return StoreLastLoad() < StoreLastUpdate()

	###### Cache / Store interface #####
	def Load(self):
		self.__do_load()
		StoreLastLoadTime = datetime.now()
	
	def Commit(self):
		self.__do_commit()
		CacheLastCommitTime = datetime.now()
	
	def __do_load(self):
		throw NotImplementedError()

	def __do_commit(self):
		throw NotImplementedError()
	
	###### Cache manipulation #####
	def Update(self, key, value):
		self.__do_update(key, value)
		CacheLastUpUpdate = datetime.now()

	def Get(self, key):
		self.__do_get(key)

	def Delete(self, key):
		self.__do_delete(key)
		CacheLastUpUpdate = datetime.now()

	def __do_update(self, key, value):
		throw NotImplementedError()

	def __do_get(self, key, value):
		throw NotImplementedError()

	def __do_update(self, key, value):
		throw NotImplementedError()

	# The time that we last read from the store
	StoreLastLoadTime = None
	def StoreLastLoad(self):
		return self.StoreLastLoadTime

	# The time that the store was last updated by some other process
	def StoreLastUpdateTime(self):
		throw NotImplementedError()

	# The time that we last changed the cache directly
	CacheLastUpdateTime = None
	def CacheLastUpdate(self):
		return self.CacheLastUpdateTime

	# The time that the cache was written to disk
	CacheLastCommitTime = None
	def CacheLastCommit(self):
		return self.CacheLastCommitTime
