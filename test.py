import unittest
from utils import powerset, percent_difference


class TestPowerset(unittest.TestCase):
    def test_empty_powerset(self):
        vals = []
        result = list(powerset(vals))
        self.assertItemsEqual([()], result)

    def test_simple_powerset(self):
        vals = [1, 2]
        result = list(powerset(vals))
        self.assertItemsEqual([(), (1,), (2,), (1, 2)], result)

    def test_powerset_limit(self):
        vals = [1, 2, 3]
        result = list(powerset(vals, max_len=2))
        self.assertItemsEqual([(), (1,), (2,), (3,), (1, 2), (2, 3), (1, 3)],
                              result)


class TestPercentDifference(unittest.TestCase):
    def test_different(self):
        result = percent_difference(5, 7)
        self.assertAlmostEqual(result, 0.3333333)

    def test_equal(self):
        result = percent_difference(5, 5)
        self.assertEqual(result, 0)

    def test_zero(self):
        result = percent_difference(0, 0)
        self.assertEqual(result, 0)
