from level import Level
import unittest

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(2,4)

    def test_deck_is_random_when_created(self):
        level2 = Level(2,4)
        self.assertFalse(level2.deck == self.level.deck)
    
    def test_the_right_amount_of_cards_is_in_deck_when_deck_is_created(self):
        self.assertEqual(len(self.level.deck),16)