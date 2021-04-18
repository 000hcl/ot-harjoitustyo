import os
import pygame

dirname = os.path.dirname(__file__)

class Card:
    def __init__(self, nr, x, y):
        self.__face = pygame.image.load(os.path.join(dirname,"assets","card_"+str(nr)+".png"))
        self.__back = pygame.image.load(os.path.join(dirname,"assets","card_back.png"))
        self.__img = self.__back
        self.__shown = False
        self.__x = x
        self.__y = y
        self.__nr = nr

    def flip(self):
        if self.shown:
            self.__img = self.__back
            self.__shown = False
        else:
            self.__img = self.__face
            self.__shown = True
        self.get_card()

    @property
    def nr(self):
        return self.__nr

    @property
    def shown(self):
        return self.__shown

    @property
    def x(self):
        return self.__x

    @property
    def x2(self):
        return self.__x + 80

    @property
    def y(self):
        return self.__y

    @property
    def y2(self):
        return self.__y + 100

    def get_pos(self):
        return (self.__x,self.__y)

    def get_card(self):
        return self.__img
