import unittest
from ..memory.game.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(1, 0, 0)

    def test_card_is_not_shown_when_created(self):
        self.assertFalse(self.card.shown)

    def test_card_is_shown_when_flipped(self):
        self.card.flip()
        self.assertTrue(self.card.shown)

    def test_card_is_not_shown_when_flipped_twice(self):
        self.card.flip()
        self.card.flip()
        self.assertFalse(self.card.shown)

    def test_number_matches_card_when_created(self):
        self.assertEqual(1, self.card.number)

    def test_coordinates_match_cards_when_created(self):
        self.assertEqual(0, self.card.x)
        self.assertEqual(0, self.card.y)
        self.assertEqual(80, self.card.x_2)
        self.assertEqual(100, self.card.y_2)

    def test_get_pos_return_correct_values(self):
        self.assertEqual((0, 0), self.card.get_pos())
