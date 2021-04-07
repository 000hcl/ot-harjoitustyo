import pygame
import os

dirname = os.path.dirname(__file__)

class Card:
    def __init__(self, nr: int, x: int=0, y: int=0):
        self.face = pygame.image.load(os.path.join(dirname,"assets","card_"+str(nr)+".png"))
        self.back = pygame.image.load(os.path.join(dirname,"assets","card_back.png"))
        self.img = self.back
        self.shown = False
        self.x = x
        self.y = y
        self.x2 = x+80
        self.y2 = y+100
        self.nr = nr
    
    def flip(self):
        if self.shown:
            self.img = self.back
            self.shown = False
        else:
            self.img = self.face
            self.shown = True
        self.getCard()
    
    def getPos(self):
        return (self.x,self.y)
    
    def getCard(self):
        return self.img

         