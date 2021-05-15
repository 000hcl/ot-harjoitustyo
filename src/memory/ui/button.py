import pygame
import os

dir_name = os.path.dirname(__file__)

class Button:
    """
    A menu button.

    Attributes:
        img: The image for the button.
        img_selected: The button image for when the mouse is
            hovering over the button.
        state: The image to be shown in the current situation.
        action: What will happen when the button is clicked.
        x: Top left x-coordinate for the button.
        y: Top left y-coordinate for the button.
        x_2: Bottom right x-coordinate for the button.
        y_2: Bottom right y-coordinate for the button.
    """
    def __init__(self, button_type, action, x, y):
        """
        Constructor for a button object.

        Args:
            button_type: Determines the images for the button.
            action: The button's action.
            x: The top left x-coordinate for the button.
            y: The top left y-coordinate for the button.
        """
        self.__img = pygame.image.load(os.path.join(dir_name, "..", "..", "assets", button_type +".png"))
        self.__img_selected = pygame.image.load(os.path.join(dir_name, '..', "..", "assets", button_type +"_selected.png"))
        self.__state = self.__img
        self.__action = action
        self.__x=x
        self.__y=y
        self.__x_2=x+self.__img.get_width()
        self.__y_2=y+self.__img.get_height()

    @property
    def state(self):
        """
        Returns the current image of the button.
        """
        return self.__state

    @property
    def action(self):
        """
        Returns the action for the button.
        """
        return self.__action

    def __select(self):
        """
        Sets the current shown image to the
        selected image.
        """
        self.__state = self.__img_selected

    def __deselect(self):
        """
        Sets the current shown image to the
        unselected image.
        """
        self.__state = self.__img

    def movement_event(self, mouse_pos):
        """
        Events for when mouse movement is detected.
        """
        if self.mouse_is_colliding(mouse_pos):
            self.__select()
        else:
            self.__deselect()

    def get_pos(self):
        """
        Returns top left coordinates as a tuple.
        """
        return (self.__x, self.__y)


    def mouse_is_colliding(self, mouse_pos):
        """
        Returns True if the given position is inside
        the coordinates of the button.
        """
        x=mouse_pos[0]
        y=mouse_pos[1]
        if (x < self.__x_2 and x > self.__x) and (y > self.__y and y < self.__y_2):
            return True
        else:
            return False
