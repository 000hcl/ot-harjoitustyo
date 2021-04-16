import pygame
from level import Level
from renderer import Renderer
from clock import Clock
from eventhandler import EventHandler

class GameLoop:
    def __init__(self,mode):
        self.level=Level(mode)
        self.window = pygame.display.set_mode((1000,800))
        self.clock = Clock()
        self.renderer = Renderer(self.window,self.level)
        self.event_handler=EventHandler(self.level)

    def loop(self):
        while True:
            if self.event_handler.handle_events() == False:
                exit()
            self.renderer.render()
            self.clock.tick()

if __name__=="__main__":
    gl=GameLoop(1)
    gl.loop()
