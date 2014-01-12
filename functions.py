def PowerSet(start):
	# Copy the list before we modify it
	arg = list(start)
	return __PowerSet(arg)

def __PowerSet(start):
	if not start:
		return [ [] ]

	first = start.pop(0)

	subsets = __PowerSet(start)

	result = []
	for set in subsets:
		result.append([first] + set)
	result += subsets

	return result

# Creates a set for every item that has every element but itself.
# (e.g, [a,b,c] => [[a, [b,c]], [b, [a,c]], [c, [a,b]]])
def OddManOut(start):
	result = []
	for key in start:
		value = list(start)
		value.remove(key)
		result.append([key, value])
	return result

# Copies all the entries in src to dest, overwriting existing ones
def MergeDictionary(dest, src):
	for key, value in src.items():
		dest[key] = value
