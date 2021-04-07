import pygame
import os

dirname = os.path.dirname(__file__)

class Button:
    def __init__(self, button_type: str):
        self.img = pygame.image.load(os.path.join(dirname,"assets", button_type +".png"))
        self.imgSelected = pygame.image.load(os.path.join(dirname,"assets", button_type +"_selected.png"))
        self.display = self.img
    
    