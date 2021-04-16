import pygame

class EventHandler:
    def __init__(self,system):
        self.__mode=0
        if system.__class__.__name__=="Level":
            self.__mode=1 
        if system.__class__.__name__=="Menu":
            self.__mode=2
        self.__system=system
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.__mode==1:
                    self.__system.click_event(mouse_pos)
            if self.__mode==1:
                if self.__system.game_ended():
                    return False
        
