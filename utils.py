from itertools import combinations, chain


def powerset(source, max_len=None):
    if max_len is None:
        max_len = len(input) + 1
    return chain.from_iterable(combinations(input, n)
                               for n in range(max_len))
