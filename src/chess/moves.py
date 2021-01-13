import pygame
from .constants import *


class Moves:
    @staticmethod
    def is_in_board(row, col):
        if row >= 0 and row <= ROWS:
            if col >= 0 and col <= COLS:
                return True
        return False
        
    @staticmethod
    def pawn(board, row, col, moveCount):
        initialTopMoves = [
            [row - 1, col],
            [row - 2, col]
        ]
        topMoves = [
            [row - 1, col]
        ]
        initialBottomMoves = [
            [row + 1, col],
            [row + 2, col]
        ]
        bottomMoves = [
            [row + 1, col],
            [row + 2, col]
        ]
        topCaptureMoves = [
            [row - 1, col + 1],
            [row - 1, col - 1]
        ]
        bottomCaptureMoves = [
            [row + 1, col + 1],
            [row + 1, col - 1]
        ]
        moves = []
        piece = board.get_piece(row, col)
        if piece.direction == "up":
            topBlocked = False
            currentMoves = topMoves
            if piece.moveCount == 0:
                currentMoves = initialTopMoves

            for move in currentMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid":
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        topBlocked = True
            for move in topCaptureMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid":
                    if movePiece != 0:
                        if movePiece.color != board.turn:
                            moves.append(move)

        elif piece.direction == "down":
            bottomBlocked = False
            currentMoves = bottomMoves
            if piece.moveCount == 0:
                currentMoves = initialBottomMoves
            for move in currentMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid":
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        bottomBlocked = True
            for move in bottomCaptureMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid":
                    if movePiece != 0:
                        if movePiece.color != board.turn:
                            moves.append(move)

        return moves

    @staticmethod
    def rook(board, row, col, moveCount):
        topMoves = [
            [row - 1, col],
            [row - 2, col],
            [row - 3, col],
            [row - 4, col],
            [row - 5, col],
            [row - 6, col],
            [row - 7, col]
        ]
        leftMoves = [
            [row, col - 1],
            [row, col - 2],
            [row, col - 3],
            [row, col - 4],
            [row, col - 5],
            [row, col - 6],
            [row, col - 7]
        ]
        rightMoves = [
            [row, col + 1],
            [row, col + 2],
            [row, col + 3],
            [row, col + 4],
            [row, col + 5],
            [row, col + 6],
            [row, col + 7]
        ]
        bottomMoves = [
            [row + 1, col],
            [row + 2, col],
            [row + 3, col],
            [row + 4, col],
            [row + 5, col],
            [row + 6, col],
            [row + 7, col]
        ]
        moves = []
        piece = board.get_piece(row, col)
        if piece.direction == "up":
            leftBlocked = False
            rightBlocked = False
            topBlocked = False
            for move in topMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not topBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        topBlocked = True
            for move in leftMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not leftBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        leftBlocked = True
            for move in rightMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not rightBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        rightBlocked = True
            

        elif piece.direction == "down":
            leftBlocked = False
            rightBlocked = False
            bottomBlocked = False
            for move in bottomMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not bottomBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        bottomBlocked = True
            for move in leftMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not leftBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        leftBlocked = True
            for move in rightMoves:
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not rightBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        rightBlocked = True
        return moves

    @staticmethod
    def knight(board, row, col, moveCount):
        topMoves = [
            [row - 1, col - 2],
            [row - 2, col - 1],
            [row - 1, col + 2],
            [row - 2, col + 1]
        ]
        bottomMoves = [
            [row + 1, col - 2],
            [row + 2, col - 2],
            [row + 1, col + 2],
            [row + 2, col + 1]
        ]
        moves = []
        piece = board.get_piece(row, col)

        if piece.direction == "up":
            for move in topMoves:
                if Moves.is_in_board(move[0], move[1]):
                    movePiece = board.get_piece(move[0], move[1])
                    if movePiece != "invalid":
                        if movePiece == 0:
                            moves.append(move)
                        else:
                            if movePiece.color != board.turn:
                                moves.append(move)
        elif piece.direction == "down":
            for move in bottomMoves:
                if Moves.is_in_board(move[0], move[1]):
                    movePiece = board.get_piece(move[0], move[1])
                    if movePiece != "invalid":
                        if movePiece == 0:
                            moves.append(move)
                        else:
                            if movePiece.color != board.turn:
                                moves.append(move)
        return moves

    @staticmethod
    def queen(board, row, col, moveCount):
        topMoves = [
            [row - 1, col],
            [row - 2, col],
            [row - 3, col],
            [row - 4, col],
            [row - 5, col],
            [row - 6, col],
            [row - 7, col]
        ]
        topLeftMoves = [
            [row - 1, col - 1],
            [row - 2, col - 2],
            [row - 3, col - 3],
            [row - 4, col - 4],
            [row - 5, col - 5],
            [row - 6, col - 6],
        ]
        topRightMoves = [
            [row - 1, col + 1],
            [row - 2, col + 2],
            [row - 3, col + 3],
            [row - 4, col + 4],
            [row - 5, col + 5],
            [row - 6, col + 6],
        ]
        leftMoves = [
            [row, col - 1],
            [row, col - 2],
            [row, col - 3],
            [row, col - 4],
            [row, col - 5],
            [row, col - 6],
            [row, col - 7]
        ]
        rightMoves = [
            [row, col + 1],
            [row, col + 2],
            [row, col + 3],
            [row, col + 4],
            [row, col + 5],
            [row, col + 6],
            [row, col + 7]
        ]
        bottomMoves = [
            [row + 1, col],
            [row + 2, col],
            [row + 3, col],
            [row + 4, col],
            [row + 5, col],
            [row + 6, col],
            [row + 7, col]
        ]
        bottomLeftMoves = [
            [row + 1, col - 1],
            [row + 2, col - 2],
            [row + 3, col - 3],
            [row + 4, col - 4],
            [row + 5, col - 5],
            [row + 6, col - 6]
        ]
        bottomRightMoves = [
            [row + 1, col + 1],
            [row + 2, col + 2],
            [row + 3, col + 3],
            [row + 4, col + 4],
            [row + 5, col + 5],
            [row + 6, col + 6]
        ]
        moves = []
        piece = board.get_piece(row, col)

        topLeftBlocked = False
        topRightBlocked = False
        leftBlocked = False
        rightBlocked = False
        topBlocked = False
        bottomBlocked = False
        bottomLeftBlocked = False
        bottomRightBlocked = False
        for move in topLeftMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not topLeftBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        topLeftBlocked = True
        for move in topRightMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not topRightBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        topRightBlocked = True
        for move in topMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not topBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        topBlocked = True
        for move in leftMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not leftBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        leftBlocked = True
        for move in rightMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not rightBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        rightBlocked = True
        for move in bottomLeftMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not bottomLeftBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        bottomLeftBlocked = True

        for move in bottomRightMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not bottomRightBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        bottomRightBlocked = True  
        for move in bottomMoves:
            if Moves.is_in_board(move[0], move[1]):
                movePiece = board.get_piece(move[0], move[1])
                if movePiece != "invalid" and not bottomBlocked:
                    if movePiece == 0:
                        moves.append(move)
                    else:
                        if movePiece.color != board.turn:
                            moves.append(move)
                        bottomBlocked = True 
        return moves

    @staticmethod
    def king(board, row, col, moveCount):
        moves = []
        
        topMove = [row - 1, col]
        topLeftMove = [row - 1, col - 1]
        topRightMove = [row - 1, col + 1]
        bottomMove = [row + 1, col]
        bottomLeftMove = [row + 1, col - 1]
        bottomRightMove = [row + 1, col + 1]
        leftMove = [row, col - 1]
        rightMove = [row, col + 1]

        piece = board.get_piece(row, col)
        topBlocked = False
        topLeftBlocked = False
        topRightBlocked = False
        leftBlocked = False
        rightBlocked = False
        bottomBlocked = False
        bottomLeftBlocked = False
        bottomRightBlocked = False


        return moves

    @staticmethod
    def bishop(board, row, col, moveCount):
        topLeftMoves = [
            [row - 1, col - 1],
            [row - 2, col - 2],
            [row - 3, col - 3],
            [row - 4, col - 4],
            [row - 5, col - 5],
            [row - 6, col - 6],
        ]
        topRightMoves = [
            [row - 1, col + 1],
            [row - 2, col + 2],
            [row - 3, col + 3],
            [row - 4, col + 4],
            [row - 5, col + 5],
            [row - 6, col + 6],
        ]
        bottomLeftMoves = [
            [row + 1, col - 1],
            [row + 2, col - 2],
            [row + 3, col - 3],
            [row + 4, col - 4],
            [row + 5, col - 5],
            [row + 6, col - 6]
        ]
        bottomRightMoves = [
            [row + 1, col + 1],
            [row + 2, col + 2],
            [row + 3, col + 3],
            [row + 4, col + 4],
            [row + 5, col + 5],
            [row + 6, col + 6]
        ]
        moves = []
        piece = board.get_piece(row, col)
        if piece.direction == "up":
            topLeftBlocked = False
            topRightBlocked = False
            for move in topLeftMoves:
                if Moves.is_in_board(move[0], move[1]):
                    movePiece = board.get_piece(move[0], move[1])
                    if movePiece != "invalid" and not topLeftBlocked:
                        if movePiece == 0:
                            moves.append(move)
                        else:
                            if movePiece.color != board.turn:
                                moves.append(move)
                            topLeftBlocked = True

            for move in topRightMoves:
                if Moves.is_in_board(move[0], move[1]):
                    movePiece = board.get_piece(move[0], move[1])
                    if movePiece != "invalid" and not topRightBlocked:
                        if movePiece == 0:
                            moves.append(move)
                        else:
                            if movePiece.color != board.turn:
                                moves.append(move)
                            topRightBlocked = True

        elif piece.direction == "down":
            bottomLeftBlocked = False
            bottomRightBlocked = False
            for move in bottomLeftMoves:
                if Moves.is_in_board(move[0], move[1]):
                    movePiece = board.get_piece(move[0], move[1])
                    if movePiece != "invalid" and not bottomLeftBlocked:
                        if movePiece == 0:
                            moves.append(move)
                        else:
                            if movePiece.color != board.turn:
                                moves.append(move)
                            bottomLeftBlocked = True

            for move in bottomRightMoves:
                if Moves.is_in_board(move[0], move[1]):
                    movePiece = board.get_piece(move[0], move[1])
                    if movePiece != "invalid" and not bottomRightBlocked:
                        if movePiece == 0:
                            moves.append(move)
                        else:
                            if movePiece.color != board.turn:
                                moves.append(move)
                            bottomRightBlocked = True
                        
        return moves