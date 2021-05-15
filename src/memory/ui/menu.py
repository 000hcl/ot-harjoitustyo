from .button import Button
from .level_service import LevelService

class Menu:
    """
    Represents a menu.

    Attributes:
        buttons: A list of buttons for the menu.
        text: Text to be displayed alongside the menu.
    """
    def __init__(self, mode, text=" "):
        """
        Constructs a new Menu object.

        Args:
            mode: Determines what kind of menu to create.
            text: The text to display alongside the menu.
        """
        self.__buttons = []
        self.__text = text
        if mode == "main":
            self.__create_main_menu("Latest result: " + self.__text)
        if mode == "difficulty":
            self.__create_difficulty_menu()

    def __create_main_menu(self, text=" "):
        start = Button("play", "difficulty", 10, 0)
        exit_button = Button("exit", None, 10, 300)
        self.__add_button(start)
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
        """
        Actions to be taken when mouse movement
        has been detected.

        Args:
            mouse_pos: Current coordinates of the mouse.
        """
        for button in self.__buttons:
            button.movement_event(mouse_pos)

    def click_event(self, mouse_pos):
        """
        Actions to take when a mouse click
        has been detected.

        Args:
            mouse_pos: Coordinates of the mouse.
        """
        for button in self.__buttons:
            if button.mouse_is_colliding(mouse_pos):
                action = button.action
                if isinstance(action,str):
                    return Menu(action)
                if action is None:
                    exit()
                return LevelService(action)

    def buttons(self):
        """
        Returns buttons.
        """
        return self.__buttons
