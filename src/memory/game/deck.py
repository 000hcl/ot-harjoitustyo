import random
from .card import Card

class Deck:
    """
    Represents the deck used in each game. There are three modes: easy, normal, and hard.
    Each deck is composed of a number of Card objects.

    Attributes:
        mode: Determines the size of the deck (and difficulty of the game).
    """
    def __init__(self, mode):
        """
        Constructs a new deck based on the argument given.

        Args:
            mode: Determines the size of the deck (and difficulty of the game).
            1 = easy, 2 = normal else = hard mode.
        """
        if mode == 1:
            height = 3
            width = 4

        elif mode == 2:
            height = 4
            width = 5

        else:
            height = 5
            width = 6

        self.__deck = self.__create_deck(height, width)

    def __create_deck(self, height, width):
        """
        Creates a deck out of Card objects.

        Args:
            height: the height of the x*y card layout
            width: the width of the x*y card layout

        Returns:
            A new deck.
        """
        max_num = height*width//2 + 1
        nums = []
        for num in range(1, max_num):
            nums.append(num)
            nums.append(num)
        random.shuffle(nums)
        deck = []

        counter = 0
        for i in range(width):
            for j in range(height):
                deck.append(Card(nums[counter], 100+100*i, 100+120*j))
                counter += 1
        return deck

    @property
    def deck(self):
        """
        Returns deck.
        """
        return self.__deck
