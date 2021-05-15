import pygame
from memory.ui.ui import UI
from memory.file_system.save import Save

if __name__ == "__main__":
    window = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Memory")
    board = Save("leaderboard.csv")
    main_menu = UI(0, window, board).next()
