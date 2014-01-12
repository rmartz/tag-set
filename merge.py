# Copies all the entries in src to dest, overwriting existing ones
def MergeDictionary(dest, src):
	for key, value in src.items():
		dest[key] = value

