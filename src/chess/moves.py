import pygame
from .constants import *

class Moves:
    @staticmethod
    def pawn(board, row, col, moveCount):
        moves = []
        piece = board.get_piece(row, col)
        cornerLeft = board.get_piece(row - 1, col - 1)
        cornerRight = board.get_piece(row - 1, col + 1)
        front1 = board.get_piece(row - 1, col)
        if front1 == 0:
            if moveCount == 0:
                moves.append([row - 1, col])
                front2 = board.get_piece(row - 2, col)
                if front2 == 0:
                    moves.append([row - 2, col])
            elif moveCount > 0:
                moves.append([row - 1, col])
        if cornerLeft != 0 and cornerRight.color != piece.color:
            moves.append([cornerLeft.row, cornerLeft.col])
        if cornerRight != 0 and cornerRight.color != piece.color:
            moves.append([cornerRight.row, cornerRight.col])
        return moves

    @staticmethod
    def rook(board, row, col, moveCount):
        moves = []
        piece = board.get_piece(row, col)
        forward_checked = False
        left_checked = False
        right_checked = False
        # Check Front
        for currentRow in range(row - 1, -1, -1):
            if not forward_checked:
                move = board.get_piece(currentRow, col)
                if move == 0:
                    moves.append([currentRow, col])
                elif move.color != piece.color:
                    moves.append([currentRow, col])
                    forward_checked = True
                else:
                    forward_checked = True
        # Check Right
        for currentCol in range(col + 1, ROWS, 1):
            if not right_checked:
                move = board.get_piece(row, currentCol)
                if move == 0:
                    moves.append([row, currentCol])
                elif move.color != piece.color:
                    moves.append([row, currentCol])
                    right_checked = True
                else:
                    right_checked = True
        # Check Left
        for currentCol in range(col - 1, -1, -1):
            if not left_checked:
                move = board.get_piece(row, currentCol)
                if move == 0:
                    moves.append([row, currentCol])
                elif move.color != piece.color:
                    moves.append([row, currentCol])
                    left_checked = True
                else:
                    left_checked = True
        return moves

    @staticmethod
    def knight(board, row, col, moveCount):
        moves = []
        piece = board.get_piece(row, col)

        topLeft1 = board.get_piece(row - 1, col - 2)
        topLeft2 = board.get_piece(row - 2, col - 1)
        topRight1 = board.get_piece(row - 1, col + 2)
        topRight2 = board.get_piece(row - 2, col + 1)
                
        if topLeft1 == 0 or (isinstance(Piece, topLeft1) and topLeft1.color != piece.color):
            moves.append([row - 1, col - 2])
        if topLeft2 == 0 or (isinstance(Piece, topLeft2) and topLeft2.color != piece.color):
            moves.append([row - 2, col - 1])
        if topRight1 == 0 or (isinstance(Piece, topRight1) and topRight1.color != piece.color):
            moves.append([row - 1, col + 2])
        if topRight2 == 0 or (isinstance(Piece, topRight2) and topRight2.color != piece.color):
            moves.append([row - 2, col + 1])

        # bottomLeft1 = board.get_piece(row + 1, col - 2)
        # bottomLeft2 = board.get_piece(row + 2, col - 1)
        # bottomRight1 = board.get_piece(row + 1, col + 2)
        # bottomRight2 = board.get_piece(row + 2, col + 1)
        # if bottomLeft1 == 0:
        #     moves.append([row + 1, col - 2])
        # if bottomLeft2 == 0:
        #     moves.append([row  + 2, col - 1])
        # if bottomRight1 == 0:
        #     moves.append([row + 1, col + 2])
        # if bottomRight2 == 0:
        #     moves.append([row + 2, col + 1])
        
        return moves

    @staticmethod
    def king(board, row, col, moveCount):
        moves = []
        piece = board.get_piece(row, col)
        
        return moves

    @staticmethod
    def queen(board, row, col, moveCount):
        moves = []
        piece = board.get_piece(row, col)
        return moves


    @staticmethod
    def bishop(board, row, col, moveCount):
        moves = []
        piece = board.get_piece(row, col)
        
        return moves
