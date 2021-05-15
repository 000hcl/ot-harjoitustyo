import unittest
from src.memory.game.level import Level

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.easy = Level(1)
        self.normal = Level(2)
        self.hard = Level(3)

    def test_game_end_is_false_in_beginning(self):
        self.assertFalse(self.easy.game_ended())
        self.assertFalse(self.normal.game_ended())
        self.assertFalse(self.normal.game_ended())

    def test_clicking_a_card_increases_points_easy(self):
        current = self.easy.result()
        self.easy.click_event((105, 105))
        self.easy.ending_event()
        new = self.easy.result()
        self.assertLess(new, current)

    def test_clicking_a_card_increases_points_normal(self):
        current = self.normal.result()
        self.normal.click_event((105, 105))
        self.normal.ending_event()
        new = self.normal.result()
        self.assertLess(new, current)

    def test_clicking_a_card_increases_points_hard(self):
        current = self.hard.result()
        self.hard.click_event((105, 105))
        self.hard.ending_event()
        new = self.hard.result()
        self.assertLess(new, current)
    
    def test_clicking_card_on_normal_decreases_points_more_than_on_easy(self):
        easy_current = self.easy.result()
        self.easy.click_event((105, 105))
        self.easy.ending_event()
        easy_new = self.easy.result()
        easy_result = easy_current - easy_new

        normal_current = self.normal.result()
        self.normal.click_event((105, 105))
        self.normal.ending_event()
        normal_new = self.normal.result()
        normal_result = normal_current - normal_new

        self.assertLess(easy_result, normal_result)
    
    def test_clicking_card_on_hard_decreases_points_more_than_on_normal(self):
        normal_current = self.normal.result()
        self.normal.click_event((105, 105))
        self.normal.ending_event()
        normal_new = self.normal.result()
        normal_result = normal_current - normal_new

        hard_current = self.hard.result()
        self.hard.click_event((105, 105))
        self.hard.ending_event()
        hard_new = self.hard.result()
        hard_result = hard_current - hard_new

        self.assertLess(normal_result, hard_result)

    def test_waiting_decreases_points_easy(self):
        current = self.easy.result()
        for i in range(100000000):
            pass
        self.easy.ending_event()
        new = self.easy.result()
        self.assertLess(new, current)

    def test_deck_is_of_correct_size(self):
        self.assertEqual(len(self.easy.deck), 12)
        self.assertEqual(len(self.normal.deck), 20)
        self.assertEqual(len(self.hard.deck), 30)
    
    def test_clicking_a_card_twice_does_not_decrease_points(self):
        easy2 = Level(1)

        easy2.click_event((105, 105))
        easy2.click_event((105, 105))
        self.easy.click_event((105, 105))
        self.easy.ending_event()
        easy2.ending_event()

        result = self.easy.result()
        result2 = easy2.result()

        self.assertEqual(result, result2)

    def test_clicking_outside_of_card_does_not_decrease_points(self):
        result = self.easy.result()
        self.easy.click_event((0, 0))
        self.easy.ending_event()
        result2 = self.easy.result()
        self.assertEqual(result, result2)
