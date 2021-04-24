from .timer import Timer
from .counter import Counter

class Points:
    def __init__(self, mode):
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
        self.__counter.increase()

    def end(self):
        self.__timer.end_timer()
        timer_result = self.__timer.result()*(self.__point//2)
        counter_result = self.__counter.result()*self.__point
        self.__result -= (timer_result + counter_result)
        if self.__result < 0:
            self.__result = 0

    @property
    def result(self):
        return self.__result
