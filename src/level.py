from deck import Deck
from points_system.points import Points

class Level:
    def __init__(self, mode):
        self.__deck = Deck(mode).deck
        self.__first_card = None
        self.__second_card = None
        self.__pairs = 0
        self.__points = Points(mode)

    @property
    def deck(self):
        return self.__deck

    def __find_clicked_card(self, x, y):
        """If a mouse button was clicked, find the card that collides
        with the position of the mouse.
        If no card is found, return None"""
        for card in self.__deck:
            c_x1 = card.x
            c_x2 = card.x2
            c_y = card.y
            c_y2 = card.y2
            if x >= c_x1 and x<=c_x2 and y>=c_y and y<=c_y2:
                return card
        return None

    def __flip_or_delete_pair(self):
        """ flip the card that was clicked, if two cards are
        flipped, then remove them.
        """
        if self.__first_card is not None and self.__second_card is not None:
            if self.__first_card.nr is not self.__second_card.nr:
                self.__first_card.flip()
                self.__second_card.flip()
                self.__reset_pair()
            else:
                self.__deck.remove(self.__first_card)
                self.__deck.remove(self.__second_card)
                self.__reset_pair()

    def __check_if_matching(self, card):
        """
        checks if the clicked card matches the other
        one, if it is flipped
        """

        if self.__first_card is None:
            self.__first_card = card
        elif self.__second_card is None:
            self.__second_card = card
        else:
            self.__first_card = card
            self.__second_card = None
        if self.__first_card is not None and self.__second_card is not None:
            if self.__first_card.nr == self.__second_card.nr:
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
    def increase_points(self):
        self.__points.update()

    def ending_event(self):
        self.__points.end()

    def result(self):
        return self.__points.result

    def click_event(self,mouse_pos):
        """
        if a mouse button was clicked,
        do this
        """
        card = self.__find_clicked_card(mouse_pos[0],mouse_pos[1])
        if card is not None and card.shown is False:
            self.__flip_or_delete_pair()
            card.flip()
            self.__check_if_matching(card)
            self.increase_points()
