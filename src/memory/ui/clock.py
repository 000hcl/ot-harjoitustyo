import pygame

class Clock:
    """
    Pygame clock that ensures the fps never goes
    beyond 60 fps.
    """
    def __init__(self):
        """
        Constructor that creates a new clock.
        """
        self.__clock = pygame.time.Clock()

    def tick(self):
        """
        Ticks the clock.
        """
        self.__clock.tick(60)
