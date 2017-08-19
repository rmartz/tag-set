from collections import defaultdict
from utils import powerset, percent_difference


class TagSetCollection(object):
    subsets = None
    prefixes = None

    def __init__(self):
        self.instances = defaultdict(int)
        self.prefixes = defaultdict(set)

    def copy(self):
        """Create a new TagSetCollection with the same attributes as self."""
        copy = TagSetCollection()
        # Instances can be copied directly without worry about mutability
        copy.instances.update(self.instances)
        # The prefixes dictionary is mutable, so we need a deep copy
        copy.prefixes.update({
            key: set(value) for key, value in self.prefixes.items()
        })
        return copy

    def add_tagset(self, tags):
        """Add a new full item to the tagset collection."""

        # Since we're adding a whole new tagset, increment the base
        self.instances[()] += 1

        # Sequentially add each tag to the prefix
        prefix = set()
        for tag in tags:
            self.add_tag(prefix, tag)
            prefix.add(tag)

    def add_tag(self, prefix, tag):
        """Add a tag to an item that is already in the collection."""
        prefix = set(prefix)
        for subset in powerset(prefix):
            self.instances[subset + (tag,)] += 1

            remainder = prefix - set(subset)
            self.prefixes[subset] |= remainder | set([tag])
            if remainder:
                self.prefixes[subset + (tag,)] |= remainder

    def remove_tagset(self, tags):
        """Remove a full item from the tagset collection."""
        self.instances[()] -= 1

        prefix = set()
        for tag in tags:
            self.remove_tag(prefix, tag)
            prefix.add(tag)

    def remove_tag(self, prefix, tag):
        """Remove a tag from an item in the tagset collection."""
        for subset in powerset(prefix):
            self.instances[subset + tag] -= 1

            if self.instances[subset + tag] == 0:
                self.prefixes[subset] -= tag

    def get_odds(self, tags):
        """Return the odds each likely tag associates to a prefix."""
        def calculate_prefix(prefix):
            base = self.instances[prefix]
            for tag in self.prefixes[prefix]:
                yield (tag, self.instances[prefix + tag] / base)

        sums = defaultdict(int)
        for subset in powerset(tags):
            odds = calculate_prefix(subset)
            for tag, weight in odds:
                sums[tag] += weight

        # Normalize all odds to fall between 0 and 1
        normal = max(sums.values())
        return {tag: weight / normal for tag, weight in sums.iteritems()}

    def get_significances(self, prefix):
        """Calculate the change in odds potential keys have on a given prefix

        This can be used to determine what keys are most valuable to add to a
        set.
        """
        def calculate_change(base, new):
            # Suffixes can't have more than a prefix, so we can just use that
            keys = base.keys()
            # For every key, get the percent difference between the normalized
            # [0-1] odds
            diffs = (percent_difference(base.get(key, 0), new.get(key, 0))
                     for key in keys)
            # Average the percent difference for all keys
            return sum(diffs) / len(keys)

        base = self.get_odds(prefix)

        for tag in self.prefixes[prefix]:
            new = self.get_odds(prefix + tag)
            yield (tag, calculate_change(base, new))
