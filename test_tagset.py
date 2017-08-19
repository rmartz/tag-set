import unittest
from tagset import TagSetCollection


class TestTagSetCollection(unittest.TestCase):
    def setUp(self):
        self.collection = TagSetCollection()

    def test_add_tagset(self):
        self.collection.add_tagset([1, 2, 3])

        self.assertEqual(dict(self.collection.prefixes),
                         {(): set([1, 2, 3]),
                          (1,): set([2, 3]),
                          (2,): set([1, 3]),
                          (3,): set([1, 2]),
                          (1, 2): set([3]),
                          (2, 3): set([1]),
                          (1, 3): set([2])})

        self.assertEqual(dict(self.collection.instances),
                         {(): 1,
                          (1,): 1,
                          (2,): 1,
                          (3,): 1,
                          (1, 2): 1,
                          (2, 3): 1,
                          (1, 3): 1,
                          (1, 2, 3): 1})

    def test_add_multiple_tagsets(self):
        self.collection.add_tagset([1, 2, 3])
        self.collection.add_tagset([2, 3])
        self.collection.add_tagset([1, 2])

        self.assertEqual(dict(self.collection.prefixes),
                         {(): set([1, 2, 3]),
                          (1,): set([2, 3]),
                          (2,): set([1, 3]),
                          (3,): set([1, 2]),
                          (1, 2): set([3]),
                          (2, 3): set([1]),
                          (1, 3): set([2])})

        self.assertEqual(dict(self.collection.instances),
                         {(): 3,
                          (1,): 2,
                          (2,): 3,
                          (3,): 2,
                          (1, 2): 2,
                          (2, 3): 2,
                          (1, 3): 1,
                          (1, 2, 3): 1})

    def test_copy_simple(self):
        """Ensure that TagSetCollection.copy() returns a functional object."""
        copy = self.collection.copy()
        self.assertEqual(self.collection.prefixes, copy.prefixes)
        self.assertEqual(self.collection.instances, copy.instances)

    def test_copy_mutability(self):
        """Ensure that a copied tagset does not alter the original."""
        copy = self.collection.copy()
        copy.add_tagset([1, 2, 3])
        self.assertNotEqual(self.collection.prefixes, copy.prefixes)
        self.assertNotEqual(self.collection.instances, copy.instances)


class TestTagSetCollectionWithData(unittest.TestCase):
    def setUp(self):
        collection = TagSetCollection()
        collection.add_tagset([1, 2, 3])
        collection.add_tagset([2, 3])
        collection.add_tagset([2, 3, 4])

        self.collection = collection

    def test_add_tag(self):
        # Make a copy to use to compare results
        comparison = self.collection.copy()

        # Add a short tagset, and then add 3 to it afterwards
        self.collection.add_tagset([1, 2])
        self.collection.add_tag([1, 2], 3)

        # Add the full set to the comparison TagSetCollection
        comparison.add_tagset([1, 2, 3])

        # Ensure that the resulting structures are the same
        self.assertEqual(self.collection.prefixes, comparison.prefixes)
        self.assertEqual(self.collection.instances, comparison.instances)
