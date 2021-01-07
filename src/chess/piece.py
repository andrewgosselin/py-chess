from .constants import *
import pygame
class Piece:
    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        self.moveCount = 0
        self.x = 0
        self.y = 0
        self.possibleMoves = []
        self.calculatePosition()
        self.board = None

    def calculatePosition(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = (SQUARE_SIZE * self.row + SQUARE_SIZE // 2)

    def draw(self, win, board):
        self.board = board
        pygame.draw.circle(win, self.color, (self.x, self.y), SQUARE_SIZE//2 - 15)

    def get_possible_moves(self):
        moves = []
        if self.type == "pawn":
            cornerLeft = self.board.get_piece(self.row - 1, self.col - 1)
            cornerRight = self.board.get_piece(self.row - 1, self.col + 1)
            front1 = self.board.get_piece(self.row - 1, self.col)
            if front1 == 0:
                if self.moveCount == 0:
                    moves.append([self.row - 1, self.col])
                    front2 = self.board.get_piece(self.row - 2, self.col)
                    if front2 == 0:
                        moves.append([self.row - 2, self.col])
                elif self.moveCount > 0:
                    moves.append([self.row - 1, self.col])
            if cornerLeft != 0:
                moves.append([cornerLeft.row, cornerLeft.col])
            if cornerRight != 0:
                moves.append([cornerRight.row, cornerRight.col])
        self.possibleMoves = moves
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