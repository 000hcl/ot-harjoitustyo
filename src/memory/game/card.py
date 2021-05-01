import os
import pygame

dir_name = os.path.dirname(__file__)

class Card:
    """
    This class represents a single card in the game.

    Attributes:
        face: The face of the card, an image loaded based on the card's number.
        back: The back image of the card. This is the same for all cards.
        img: The currently visible side of the card. Can either be face or back.
        shown: Returns True if the face is shown (img==face),
        and false if the back is shown(img==back).
        x = The x-coordinate of the top left corner of the card.
        y = The y-coordinate of the top left corner of the card.
        number = The number of the card. This determines which image is chosen for the face.
    """
    def __init__(self, number, x, y):
        """
        The constructor for the card, which creates a new card.

        Args:
            number: The number of the card, which determines which image is chosen for the face.
            x: The x-coordinate for the top-left corner.
            y: The y-coordinate for the top-left corner.
        """
        self.__face = pygame.image.load(os.path.join(dir_name, "..", "..",
         "assets", "card_" + str(number) + ".png"))
        self.__back = pygame.image.load(os.path.join(dir_name, "..", "..", "assets", "card_back.png"))
        self.__img = self.__back
        self.__shown = False
        self.__x = x
        self.__y = y
        self.__number = number

    def flip(self):
        """
        Flips the card. If the face was shown, the back will be shown after the
        card was flipped.
        The visible image is then returned.
        """
        if self.shown:
            self.__img = self.__back
            self.__shown = False
        else:
            self.__img = self.__face
            self.__shown = True
        self.get_card()

    @property
    def number(self):
        """
        Returns number attribute.
        """
        return self.__number

    @property
    def shown(self):
        """
        Returns shown attribute.
        """
        return self.__shown

    @property
    def x(self):
        """
        Returns x-coordinate of the top-left corner.
        """
        return self.__x

    @property
    def x_2(self):
        """
        Returns x-coordinate of the bottom-right corner.
        """
        return self.__x + 80

    @property
    def y(self):
        """
        Returns y-coordinate of the top-left corner.
        """
        return self.__y

    @property
    def y_2(self):
        """
        Returns y-coordinate of the bottom-right corner.
        """
        return self.__y + 100

    def get_pos(self):
        """
        Returns the coordinates for the top left corner as a tuple.
        """
        return (self.__x,self.__y)

    def get_card(self):
        """
        Returns the visible image of the card.
        """
        return self.__img
