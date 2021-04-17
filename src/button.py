import sys
print(sys.path)
import pygame
import os

dirname = os.path.dirname(__file__)

class Button:
    def __init__(self, button_type, action, x,y):
        self.__img = pygame.image.load(os.path.join(dirname,"assets", button_type +".png"))
        self.__img_selected = pygame.image.load(os.path.join(dirname,"assets", button_type +"_selected.png"))
        self.__state = self.__img
        self.__action = action
        self.__x=x
        self.__y=y
        self.__x2=x+self.__img.get_width()
        self.__y2=y+self.__img.get_height()

    @property
    def state(self):
        return self.__state

    @property
    def action(self):
        return self.__action

    def __select(self):
        self.__state = self.__img_selected

    def __deselect(self):
        self.__state = self.__img

    def movement_event(self, mouse_pos):
        if self.mouse_is_colliding(mouse_pos):
            self.__select()
        else:
            self.__deselect()

    def get_pos(self):
        return (self.__x, self.__y)


    def mouse_is_colliding(self, mouse_pos):
        """
        Returns True if the given position is inside
        the coordinates of the button.
        """
        x=mouse_pos[0]
        y=mouse_pos[1]
        if (x < self.__x2 and x > self.__x) and (y > self.__y and y < self.__y2):
            return True
        else:
            return False
