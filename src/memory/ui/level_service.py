from ..game.level import Level

class LevelService:
    """
    Communicates with the level class.

    Attributes:
        level: The level it communicates with.
    """
    def __init__(self, mode):
        """
        Args:
            mode: The difficulty for the level.
        """
        self.__level = Level(mode)

    def deck(self):
        """
        Returns the deck of the level.
        """
        return self.__level.deck

    def click_event(self, mouse_pos):
        """
        When the mouse is clicked, calls
        click_event() for the level too.

        Args:
            mouse_pos: The coordinates of a mouse click.
        """
        self.__level.click_event(mouse_pos)

    def game_ended(self):
        """
        Checks if the game has ended.
        Returns:
            True if the game has ended,
            False otherwise.
        """
        return self.__level.game_ended()

    def ending_event(self):
        """
        Does the necessary things for when
        the game has ended.
        """
        self.__level.ending_event()

    def result(self):
        """
        Returns the points.
        """
        return self.__level.result()
