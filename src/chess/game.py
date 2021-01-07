import pygame
from chess.board import Board
from .constants import *


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected_piece = None
        self.board = Board(WHITE)
        self.turn = WHITE
        self.valid_moves = []

    def tick(self):
        self.board.draw(self.win)
        if self.selected_piece and len(self.valid_moves) > 0:
            self.board.draw_possible_moves( self.win, self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()
        
    def select_piece(self, row, col):
        if self.selected_piece:
            result = self.move(row, col)
            self.selected_piece = None
            
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.board.player_color and piece.color == self.turn:
                self.selected_piece = piece
                self.valid_moves = self.selected_piece.get_possible_moves()
                return True
        return False

    def move(self, row, col, override_check=False):
        piece = self.board.get_piece(row, col)
        if self.selected_piece:
            if [row, col] in self.valid_moves or override_check:
                if(piece == 0):
                    self.board.move(self.selected_piece, row, col)
                else:
                    self.board.capture_piece(row, col, self.turn)
                    self.board.move(self.selected_piece, row, col)
                self.change_turn()
        else:
            return False
        return True
    
    def change_turn(self):
        if self.turn == WHITE:
            self.turn = WHITE
        else:
            self.turn = WHITE
