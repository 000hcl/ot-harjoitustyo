import pygame

class EventHandler:
    """
    Handles the events for both menu and game
    situations.

    Attributes:
        mode: Determines what events to run.
            Depends on the system.
        system: A LevelService or Menu object.
    """
    def __init__(self, system):
        """
        Constructs a new EventHandler object.

        Args:
            system: A LevelService or Menu object.
        """
        self.__mode = 0
        if system.__class__.__name__ == "LevelService":
            self.__mode = 1
        if system.__class__.__name__ == "Menu":
            self.__mode = 2
        self.__system = system

    def handle_events(self):
        """
        Detects events like mouse movement and clicks,
        and acts accordingly.
        """
        if self.__mode == 0:
            return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if self.__mode == 2:
                    self.__system.movement_event(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.__mode != 0:
                    action = self.__system.click_event(mouse_pos)
                    return action
            if self.__mode == 1:
                if self.__system.game_ended():
                    self.__system.ending_event()
                    result = str(self.__system.result())
                    return (3, result)
