import pygame
import os

dirname = os.path.dirname(__file__)

class Button:
    def __init__(self, button_type: str,x,y):
        self.__img = pygame.image.load(os.path.join(dirname,"assets", button_type +".png"))
        #self.imgSelected = pygame.image.load(os.path.join(dirname,"assets", button_type +"_selected.png"))
        self.__x=x
        self.__y=y
        self.__x2=x+self.__img.get_width()
        self.__y2=y+self.__img.get_height()

    @property
    def img(self):
        return self.__img

    def mouse_is_colliding(self,mouse_pos):
        """
        Returns True if the given position is inside
        the coordinates of the button.
        """
        x=mouse_pos[0]
        y=mouse_pos[1]
        if (x > self.__x2 and x < self.__x) and (y > self.__y and y < self.__y2):
            return True
        else:
            return False
