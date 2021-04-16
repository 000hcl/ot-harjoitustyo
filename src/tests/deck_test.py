import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck1=Deck(1)
        self.deck2=Deck(2)

    def test_deck_is_random_when_created(self):
        easydeck1 = Deck(1).deck
        easydeck2 = Deck(1).deck
        self.assertFalse(self.deck1.deck == easydeck1 == easydeck2)
