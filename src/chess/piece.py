from .constants import *
import pygame
from .moves import Moves

class Piece:
    def __init__(self, row, col, color, type, direction = "up"):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        self.moveCount = 0
        self.x = 0
        self.y = 0
        self.possibleMoves = []
        self.calculatePosition()
        self.direction = direction
        self.board = None
        if self.color == WHITE:
            color_letter = "w"
        else:
            color_letter = "b"
        self.sprite = pygame.image.load('../assets/chess/pieces/' + color_letter + '_' + self.type + '.png')
        self.sprite = pygame.transform.scale(self.sprite, (SQUARE_SIZE - 15, SQUARE_SIZE - 15))

    def calculatePosition(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = (SQUARE_SIZE * self.row + SQUARE_SIZE // 2) + BOARD_PADDING_TOP

    def draw(self, win, board):
        self.board = board
        rect = self.sprite.get_rect()
        rect.center = (self.x, self.y)
        win.blit(self.sprite, rect)
        #pygame.draw.circle(win, self.color, (self.x, self.y), SQUARE_SIZE//2 - 15)

    def get_possible_moves(self):
        moves = []
        if self.type == "pawn":
            moves = Moves.pawn(self.board, self.row, self.col, self.moveCount)
        elif self.type == "rook":
            moves = Moves.rook(self.board, self.row, self.col, self.moveCount)
        elif self.type == "knight":
            moves = Moves.knight(self.board, self.row, self.col, self.moveCount)
        elif self.type == "bishop":
            moves = Moves.bishop(self.board, self.row, self.col, self.moveCount)
        elif self.type == "king":
            moves = Moves.king(self.board, self.row, self.col, self.moveCount)
        elif self.type == "queen":
            moves = Moves.queen(self.board, self.row, self.col, self.moveCount)
        self.possibleMoves = moves
        print(self.possibleMoves)
        return self.possibleMoves
    
    def is_move_possible(self, row, col):
        if (row, col) in self.possibleMoves:
            return True
        return False

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculatePosition()
        self.moveCount += 1

    def __repr__(self):
        return str(self.color)