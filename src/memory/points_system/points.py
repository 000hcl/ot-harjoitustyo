from .timer import Timer
from .counter import Counter

class Points:
    """
    Calculates the points gained from each game.

    Attributes:
        timer: A timer object that tracks the time
            passed in the game.
        counter: A counter object that tracks the
            number of times a valid card has been
            clicked.
        start: The starting amount of points. Depends on
            the difficulty.
        point: The amount of points that is removed
            from the starting amount.
    """
    def __init__(self, mode):
        """
        Constructor that creates a new Points object.

        Args:
            mode: The difficulty of the game.
        """
        self.__timer = Timer()
        self.__counter = Counter()
        if mode == 1:
            self.__point = 10
            self.__start = 1000
        elif mode == 2:
            self.__point = 100
            self.__start = 8000
        else:
            self.__point = 1000
            self.__start = 105000
        self.__result = self.__start

    def update(self):
        """
        Increments the counter by one.
        """
        self.__counter.increase()

    def end(self):
        """
        Stops the timer and calculates the result.
        """
        self.__timer.end_timer()
        timer_result = self.__timer.result()*(self.__point//2)
        counter_result = self.__counter.result()*self.__point
        self.__result -= (timer_result + counter_result)
        if self.__result < 0:
            self.__result = 0

    @property
    def result(self):
        """
        Returns the total points.
        """
        return self.__result
