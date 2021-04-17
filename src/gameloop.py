import pygame
from renderer import Renderer
from clock import Clock
from eventhandler import EventHandler

class GameLoop:
    def __init__(self, system):
        self.system = system
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = Clock()
        self.renderer = Renderer(self.window, self.system)
        self.event_handler = EventHandler(self.system)

    def loop(self):
        while True:
            event = self.event_handler.handle_events()
            if event is False:
                exit()
            if event is not None:
                return event
            self.renderer.render()
            self.clock.tick()

    def action(self, action):
        if action is None:
            exit()
        else:
            pass
