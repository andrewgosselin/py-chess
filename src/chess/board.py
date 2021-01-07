import pygame
from .constants import *
from .piece import Piece

class Board:
    def __init__(self, player_color):
        self.board = []
        self.player_color = player_color
        self.top_color = ((player_color == WHITE) if BLACK else WHITE)
        self.bottom_color = player_color
        self.generate_board()
        self.white_captures = []
        self.black_captures = []

    def draw_squares(self, win):
        win.fill(DARKGREY)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHTGREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def generate_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                    if row < 2:
                        self.board[row].append(Piece(row, col, self.top_color, "pawn"))
                    elif row > 5:
                        self.board[row].append(Piece(row, col, self.bottom_color, "pawn"))
                    else:
                        self.board[row].append(0)

    def move(self, piece, row, col):
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
        return self.board[row][col]

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
            y = SQUARE_SIZE * row + SQUARE_SIZE // 2
            pygame.draw.circle(win, BLUE, (x, y), SQUARE_SIZE//2 - 25)
                