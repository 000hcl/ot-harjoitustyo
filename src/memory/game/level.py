from .deck import Deck
from ..points_system.points import Points

class Level:
    """
    Represents a game level or a set of cards laid out.

    Attributes:
        deck: The deck used in the game.
        first_card: The first card flipped over when finding a new pair.
        second_card: The second card flipped over when finding a new pair.
        pairs: The number of pairs made.
        points: The point calculating system.
    """
    def __init__(self, mode):
        """
        Constructor which starts a new game.

        Args:
            mode: Determines the difficulty of the game.
        """
        self.__deck = Deck(mode).deck
        self.__first_card = None
        self.__second_card = None
        self.__pairs = 0
        self.__points = Points(mode)

    @property
    def deck(self):
        """
        Returns the deck.
        """
        return self.__deck

    def __find_clicked_card(self, x, y):
        """If a mouse button was clicked, find the card that collides
        with the position of the mouse.

        Args:
            x: The x-coordinate of the mouse.
            y: The y-coordinate of the mouse.

        Returns:
            The clicked card.
            If no card was clicked, returns None.
        """
        for card in self.__deck:
            c_x1 = card.x
            c_x_2 = card.x_2
            c_y = card.y
            c_y_2 = card.y_2
            if x >= c_x1 and x<=c_x_2 and y>=c_y and y<=c_y_2:
                return card
        return None

    def __flip_or_delete_pair(self):
        """
        if two cards have visible faces, check if they are a pair.
        If they are not a pair, flip both of them over.
        If they are a pair, remove them from the deck.
        In both cases, reset the memorized pair of cards (reset_pair()).
        """
        if self.__first_card is not None and self.__second_card is not None:
            if self.__first_card.number is not self.__second_card.number:
                self.__first_card.flip()
                self.__second_card.flip()
                self.__reset_pair()
            else:
                self.__deck.remove(self.__first_card)
                self.__deck.remove(self.__second_card)
                self.__reset_pair()

    def __set_flipped_pair(self, card):
        """
        Remembers a flipped card.
        """
        if self.__first_card is None:
            self.__first_card = card
        elif self.__second_card is None:
            self.__second_card = card
        else:
            self.__first_card = card
            self.__second_card = None

    def __check_if_matching(self):
        """
        checks if the memorized pair are a matching pair.
        Increases the number of found pairs by one if they match.
        """
        if self.__first_card is not None and self.__second_card is not None:
            if self.__first_card.number == self.__second_card.number:
                self.__pairs += 1

    def __reset_pair(self):
        """
        Resets the two flipped cards that
        were memorized.
        """
        self.__first_card = None
        self.__second_card = None

    def game_ended(self):
        """
        Checks if all pairs have been found.
        """
        end = True
        for card in self.__deck:
            if card.shown is False:
                end = False
        return end

    def __increase_points(self):
        """
        Updates the point calculator.
        """
        self.__points.update()

    def ending_event(self):
        """
        What should be done if the game is over.
        """
        self.__points.end()

    def result(self):
        """
        Returns the point result of the game.
        """
        return self.__points.result

    def click_event(self, mouse_pos):
        """
        If a mouse button was clicked,
        do this.

        Args:
            mouse_pos: The coordinates of the mouse.
        """
        card = self.__find_clicked_card(mouse_pos[0],mouse_pos[1])
        if card is not None and card.shown is False:
            self.__flip_or_delete_pair()
            card.flip()
            self.__set_flipped_pair(card)
            self.__check_if_matching()
            self.__increase_points()
