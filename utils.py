from itertools import combinations, chain


def powerset(source, max_len=None):
    if max_len is None:
        max_len = len(source)
    return chain.from_iterable(combinations(source, n)
                               for n in range(max_len + 1))


def percent_difference(a, b):
    try:
        return 1.0 * abs(a - b) / ((abs(a) + abs(b)) / 2)
    except ZeroDivisionError:
        # If abs(a) + abs(b) == 0, then a and b must both be 0 and so be equal
        return 0
