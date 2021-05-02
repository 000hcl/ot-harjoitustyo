from .button import Button
from ..game.level import Level

class Menu:
    def __init__(self, mode, text=" "):
        self.__buttons = []
        self.__text = text
        if mode == "main":
            self.__create_main_menu("Latest result: " + self.__text)
        if mode == "difficulty":
            self.__create_difficulty_menu()

    def __create_main_menu(self, text=" "):
        #Leaderboard coming soon
        start = Button("play", "difficulty", 10, 0)
        leaderboard = Button("leaderboard", None, 10, 150)
        exit_button = Button("exit", None, 10, 300)
        self.__add_button(start)
        #self.__add_button(leaderboard)
        self.__add_button(exit_button)
        self.__set_text(text)

    def __set_text(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text


    def __create_difficulty_menu(self):
        easy = Button("easy", 1, 10, 0)
        medium = Button("normal", 2, 10, 150)
        hard = Button("hard", 3, 10, 300)
        self.__add_button(easy)
        self.__add_button(medium)
        self.__add_button(hard)

    def __add_button(self, button):
        self.__buttons.append(button)

    def movement_event(self, mouse_pos):
        for button in self.__buttons:
            button.movement_event(mouse_pos)

    def click_event(self, mouse_pos):
        for button in self.__buttons:
            if button.mouse_is_colliding(mouse_pos):
                action = button.action
                #NEW
                if isinstance(action,str):
                    return Menu(action)
                if action is None:
                    exit()
                return Level(action)

    def buttons(self):
        return self.__buttons
