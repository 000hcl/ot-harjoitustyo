from time import perf_counter
from math import ceil

class Timer:
    """
    A timer used in the game. Is a part of the
    points calculator system.

    Attributes:
    start: The time the timer starts.
    end: The time the timer is stopped.
    """
    def __init__(self):
        """
        Constructor that creates a new timer object.
        The start is set upon creation.
        """
        self.__start = ceil(perf_counter())
        self.__end = None

    def end_timer(self):
        """
        Stops the timer.
        Sets the end attribute as the current time.
        """
        self.__end = ceil(perf_counter())

    def result(self):
        """
        Returns the time passed between start
        and end of the timer.
        """
        return self.__end - self.__start
