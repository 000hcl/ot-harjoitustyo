from time import perf_counter
from math import ceil

class Timer:
    def __init__(self):
        self.__start = ceil(perf_counter())
        self.__end = None

    def end_timer(self):
        self.__end = ceil(perf_counter())

    def result(self):
        return self.__end - self.__start
