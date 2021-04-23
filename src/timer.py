from time import perf_counter
from math import ceil

class Timer:
    def __init__(self):
        self.start = ceil(perf_counter())
        self.end = None

    def end_timer(self):
        self.end = ceil(perf_counter())

    def result(self):
        return self.end - self.start
