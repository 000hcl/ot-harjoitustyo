import pygame

class Renderer:
    def __init__(self, window, level):
        self.__window = window
        self.__level = level

    def __blit_deck(self):
        deck = self.__level.deck
        for card in deck:
            self.__window.blit(card.get_card(),card.get_pos())

    def render(self):
        self.__window.fill((0,0,0))
        self.__blit_deck()
        pygame.display.flip()
