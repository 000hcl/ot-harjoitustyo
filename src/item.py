from gameloop import GameLoop
from menu import Menu
from level import Level
#NOT WORKING
class Item:
    def __init__(self, item):
        if item is 0:
            item = Menu("main")
        self.loop = GameLoop(item)
        if item.__class__.__name__ == "Level":
            self.mode = 1
        if item.__class__.__name__ == "Menu":
            self.mode = 2
        #if item == "main":
        #    self.mode = 0

    def result(self):
        return self.loop.loop()
    
    def next(self):
        #if self.mode == 0:
            #Item(Menu(self.result())).next()
        r = self.result()
        if r is None:
            exit()
        return Item(r).next()
