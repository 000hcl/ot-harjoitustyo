import unittest
from ..memory.game.level import Level

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.easy = Level(1)
        self.medium = Level(2)
        self.hard = Level(3)

    def test_game_end_is_false_in_beginning(self):
        self.assertFalse(self.easy.game_ended())
        self.assertFalse(self.medium.game_ended())
        self.assertFalse(self.medium.game_ended())

    def test_clicking_a_card_increases_points(self):
        current = self.easy.result()
        self.easy.click_event((105, 105))
        self.easy.ending_event()
        new = self.easy.result()
        self.assertLess(new, current)
