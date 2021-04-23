from .gameloop import GameLoop
from .menu import Menu
class Item:
    def __init__(self, item,window):
        if item == 0:
            item = Menu("main")
        self.window=window
        self.loop = GameLoop(item,self.window)

    def result(self):
        return self.loop.loop()

    def next(self):
        result = self.result()
        if result is None:
            exit()
        return Item(result,self.window).next()
