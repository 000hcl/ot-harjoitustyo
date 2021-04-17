from gameloop import GameLoop
from menu import Menu
class Item:
    def __init__(self, item):
        if item == 0:
            item = Menu("main")
        self.loop = GameLoop(item)

    def result(self):
        return self.loop.loop()

    def next(self):
        result = self.result()
        if result is None:
            exit()
        return Item(result).next()
