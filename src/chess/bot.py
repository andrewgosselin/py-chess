# Bot code here
import random
from .constants import *
import time
class Bot:
    @staticmethod
    def move(board, game):
        # wait()
        moveable_pieces = []
        for row in range(ROWS):
            if row >= 0 and row <= 1:
                for col in range(COLS):
                    piece = board.get_piece(row, col)
                    if piece != 0 and piece.color == board.top_color:
                        moves = piece.get_possible_moves()
                        if len(moves) > 0:
                            moveable_pieces.append(piece)
        chosen_piece = random.choice(moveable_pieces)
        moves = chosen_piece.get_possible_moves()

        move = random.choice(moves)
        row = move[0]
        col = move[1]
        
        game.valid_moves = moves
        game.selected_piece = chosen_piece
        game.move(row, col)
        game.selected_piece = None