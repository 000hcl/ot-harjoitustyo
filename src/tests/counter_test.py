import unittest
from ..memory.points_system.counter import Counter

class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_counter_starts_at_0(self):
        self.assertEqual(0, self.counter.result())

    def test_counter_increases_by_1(self):
        self.counter.increase()
        self.assertEqual(1,self.counter.result())