import pygame
from chess.constants import *
from chess.game import Game
from base.main_menu import MainMenu

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")



def main():
    pygame.font.init()

    run = True
    clock = pygame.time.Clock()
    
    # game = Game(WIN)
    menu = MainMenu(WIN)
    
    while run:
        clock.tick(FPS)
        if menu.game_started:
            menu.game.tick()
        else:
            menu.tick()
    pygame.quit()

main()