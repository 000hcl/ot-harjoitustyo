import unittest
from src.memory.points_system.points import Points

class TestPoints(unittest.TestCase):
    def setUp(self):
        self.points_1 = Points(1)
        self.points_2 = Points(2)
        self.points_3 = Points(3)
    
    def test_mode_1_timer_works(self):
        points_b = Points(1)
        self.points_1.end()
        for i in range(100000000):
            pass
        points_b.end()
        self.assertGreater(self.points_1.result,points_b.result)

    def test_mode_2_timer_works(self):
        points_b = Points(2)
        self.points_2.end()
        for i in range(100000000):
            pass
        points_b.end()
        self.assertGreater(self.points_2.result,points_b.result)

    def test_mode_3_timer_works(self):
        points_b = Points(3)
        self.points_3.end()
        for i in range(100000000):
            pass
        points_b.end()
        self.assertGreater(self.points_3.result,points_b.result)

    def test_mode_1_counter_works(self):
        self.points_1.update()
        self.points_1.end()
        self.assertEqual(self.points_1.result, 990)

    def test_mode_2_counter_works(self):
        self.points_2.update()
        self.points_2.end()
        self.assertEqual(self.points_2.result, 7900)

    def test_mode_3_counter_works(self):
        self.points_3.update()
        self.points_3.end()
        self.assertEqual(self.points_3.result, 104000)

    def test_ending_does_not_return_negative_value(self):
        for i in range(1000):
            self.points_1.update()
        self.points_1.end()
        self.assertEqual(self.points_1.result, 0)
