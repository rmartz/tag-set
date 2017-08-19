from collections import defaultdict
from itertools import combinations, chain


class TagSet(object):
    count = 0
    sub_counts = None

    def __init__(self):
        self.sub_counts = defaultdict(int)

    def add(self, set):
        self.count += 1
        for v in set:
            self.sub_counts[v] += 1


class TagSetCollection(object):
    tagsets = None

    def __init__(self):
        self.tagsets = defaultdict(TagSet)

    def add_set(self, input):
        # Process all combinations of input of size 1 to one less than
        # len(input)
        powerset = chain.from_iterable(combinations(input, n)
                                       for n in range(len(input)))
        for subset in powerset:
            remainder = input - subset
            self.tagsets(subset).add(remainder)
