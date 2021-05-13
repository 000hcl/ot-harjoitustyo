import pygame


pygame.init()
class Renderer:
    def __init__(self, window, system, save):
        self.__save = save
        self.__window = window
        self.__system = system
        self.__mode = 0
        self.__font = pygame.font.SysFont("arial", 30)
        self.__colour = (255, 255, 255)

        if system.__class__.__name__ == "Level":
            self.__mode = 1
        if system.__class__.__name__ == "Menu":
            self.__mode = 2

    def __blit_leaderboard(self):
        text = self.__font.render("Leaderboard: ", True, self.__colour)
        self.__window.blit(text, (400, 100))
        for num in range(10):
            text = self.__font.render(str(self.__save.result[num]), True, self.__colour)
            self.__window.blit(text, (400, 40*(num)+200))

    def __blit_text(self, input):
        text = self.__font.render(input, True, self.__colour)
        self.__window.blit(text, (400, 20))

    def __blit_deck(self):
        deck = self.__system.deck
        for card in deck:
            self.__window.blit(card.get_card(), card.get_pos())

    def __blit_menu_buttons(self):
        buttons = self.__system.buttons()
        for button in buttons:
            self.__window.blit(button.state, button.get_pos())

    def __render_menu(self):
        self.__window.fill((0 ,0, 0))
        self.__blit_menu_buttons()
        self.__blit_text(self.__system.text)
        self.__blit_leaderboard()
        pygame.display.flip()

    def __render_level(self):
        self.__window.fill((10, 10, 10))
        self.__blit_deck()
        pygame.display.flip()

    def render(self):
        if self.__mode == 1:
            self.__render_level()
        if self.__mode == 2:
            self.__render_menu()
