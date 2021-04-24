class Counter:
    def __init__(self):
        self.__counter = 0

    def increase(self):
        self.__counter += 1

    def result(self):
        return self.__counter
