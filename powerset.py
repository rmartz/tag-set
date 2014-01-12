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
