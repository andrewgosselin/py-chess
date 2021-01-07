import pygame
from chess.constants import *
from chess.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def convertMouseToPosition(pos):
    x, y = pos
    print("mouse: ", x, y)
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()

    game = Game(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = convertMouseToPosition(pos)
                game.select_piece(row, col)

        game.tick()
    pygame.quit()

main()