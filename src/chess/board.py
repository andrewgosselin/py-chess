import pygame
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None

    def draw_squares(self, win):
        win.fill(DARKGREY)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHTGREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
