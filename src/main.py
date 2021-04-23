import pygame
from ui.item import Item
if __name__ == "__main__":
    window = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Memory")
    main_menu = Item(0,window).next()

