import unittest
from src.memory.game.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck1=Deck(1)
        self.deck2=Deck(2)
        self.deck3=Deck(3)

    def test_deck_is_random_when_created(self):
        easydeck1 = Deck(1).deck
        easydeck2 = Deck(1).deck
        self.assertFalse(self.deck1.deck == easydeck1 == easydeck2)

    def decks_have_correct_number_of_cards(self):
        self.assertEqual(len(self.deck1.deck),12)
        self.assertEqual(len(self.deck2.deck),20)
        self.assertEqual(len(self.deck3.deck),30)
