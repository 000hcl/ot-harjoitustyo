import unittest
from ..memory.points_system import timer as t

class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = t.Timer()
        self.timer_2 = t.Timer()

    def test_timer_goes_forward(self):
        self.timer.end_timer()
        for i in range(100000000):
            pass
        self.timer_2.end_timer()
        self.assertGreater(self.timer_2.result(),self.timer.result())
