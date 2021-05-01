from .gameloop import GameLoop
from .menu import Menu
class Item:
    def __init__(self, item,window):
        try:
            if item == 0:
                item = Menu("main")
            elif item[0] == 3:
                item = Menu("main", item[1])
        except:
            pass
        self.window=window
        self.loop = GameLoop(item,self.window)

    def result(self):
        return self.loop.loop()

    def next(self):
        result = self.result()
        if result is None:
            exit()
        return Item(result,self.window).next()
