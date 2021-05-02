import pygame
from memory.ui.item import Item
from memory.file_system.save import Save

if __name__ == "__main__":
    window = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Memory")
    board = Save("leaderboard.csv")
    main_menu = Item(0, window, board).next()
