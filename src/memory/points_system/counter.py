class Counter:
    """
    Keeps track of how many times a card has
    been clicked during a game.

    Attributes:
    counter: The number of times a valid card has
    been clicked.
    """
    def __init__(self):
        """
        Constructor that sets the default
        counter to 0.
        """
        self.__counter = 0

    def increase(self):
        """
        Increments the counter by one.
        """
        self.__counter += 1

    def result(self):
        """
        Returns the counter.
        """
        return self.__counter
