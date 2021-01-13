import pygame
from .constants import *
from .piece import Piece
from .layouts import Layouts

class Board:
    def __init__(self, player_color):
        self.board = []
        self.player_color = player_color
        if self.player_color == WHITE:
            self.top_color = BLACK
        else:
            self.top_color = WHITE
        self.bottom_color = player_color
        self.turn = WHITE
        self.generate_board()
        self.white_captures = []
        self.black_captures = []

    def draw_squares(self, win):
        win.fill(BLACK)
        pygame.draw.rect(win, DARKGREY, (0, BOARD_PADDING_TOP, COLS * SQUARE_SIZE, ROWS * SQUARE_SIZE))
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHTGREY, (row * SQUARE_SIZE, (col * SQUARE_SIZE) + BOARD_PADDING_TOP, SQUARE_SIZE, SQUARE_SIZE))

    def generate_board(self):
        self.board = Layouts.normal(self.top_color, self.bottom_color)

    def move(self, piece, row, col):
        print("Moved [" + str(piece.row) + ", " + str(piece.col) + "] to [" + str(row) + ", " + str(col) + "]")
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == ROWS or row == 0:
            self.promote(piece)

    def capture_piece(self, row, col, color):
        piece = self.get_piece(row, col)
        if WHITE:
            self.white_captures.append(piece)
        else:
            self.black_captures.append(piece)
        self.board[row][col] = 0

    def get_piece(self, row, col):
        try:
            return self.board[row][col]
        except:
            return "invalid"

    def promote(self, piece):
        pass

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win, self)
               
    def draw_possible_moves(self, win, moves):
        for move in moves:
            row = move[0]
            col = move[1]
            x = SQUARE_SIZE * col + SQUARE_SIZE // 2
            y = (SQUARE_SIZE * row + SQUARE_SIZE // 2) + BOARD_PADDING_TOP
            pygame.draw.circle(win, BLUE, (x, y), SQUARE_SIZE//2 - 25)