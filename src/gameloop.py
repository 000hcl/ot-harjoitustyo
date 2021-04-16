import pygame
from level import Level
from renderer import Renderer
from clock import Clock

#pygame.init()
class GameLoop:
    def __init__(self,mode):
        self.level=Level(mode)
        self.window = pygame.display.set_mode((1000,800))
        self.clock = Clock()
        self.renderer = Renderer(self.window,self.level)

    def loop(self):
        while True:
            if self.__handle_events() == False:
                exit()
            self.renderer.render()
            self.clock.tick()

    def __handle_events(self):
        """
        Handles all pygame events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.level.click_event(mouse_pos)
            if self.level.game_ended():
                return False

if __name__=="__main__":
    gl=GameLoop(1)
    gl.loop()
