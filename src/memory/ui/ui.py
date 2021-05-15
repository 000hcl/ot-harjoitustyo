from .gameloop import GameLoop
from .menu import Menu
from ..file_system.save import Save

class UI:
    def __init__(self, ui, window, save):
        self.board = save

        try:
            if ui == 0:
                ui = Menu("main")
            elif ui[0] == 3:
                self.board.update(int(ui[1]))
                ui = Menu("main", ui[1])

        except:
            pass
        self.window=window
        self.loop = GameLoop(ui,self.window, self.board)

    def result(self):
        return self.loop.loop()

    def next(self):
        result = self.result()
        if result is None:
            exit()
        return UI(result,self.window,self.board).next()
