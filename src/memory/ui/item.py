from .gameloop import GameLoop
from .menu import Menu
from ..file_system.save import Save
class Item:
    def __init__(self, item, window, save):
        self.board = save
        
        try:
            if item == 0:
                item = Menu("main")
            elif item[0] == 3:
                print(item[1])
                self.board.update(int(item[1]))
                
                item = Menu("main", item[1])
                
        except:
            pass
        self.window=window
        self.loop = GameLoop(item,self.window, self.board)

    def result(self):
        return self.loop.loop()

    def next(self):
        result = self.result()
        if result is None:
            exit()
        return Item(result,self.window,self.board).next()

