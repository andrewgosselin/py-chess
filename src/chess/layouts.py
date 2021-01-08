import pygame
from .constants import *
from .piece import Piece

class Layouts:
    @staticmethod
    def normal(top_color, bottom_color):
        layout = [
            [
                Piece(0, 0, top_color, "rook"), 
                Piece(0, 1, top_color, "rook"), 
                Piece(0, 2, top_color, "rook"), 
                Piece(0, 3, top_color, "rook"), 
                Piece(0, 4, top_color, "rook"), 
                Piece(0, 5, top_color, "rook"), 
                Piece(0, 6, top_color, "rook"), 
                Piece(0, 7, top_color, "rook")
            ],
            [
                Piece(1, 0, top_color, "rook"), 
                Piece(1, 1, top_color, "rook"), 
                Piece(1, 2, top_color, "rook"), 
                Piece(1, 3, top_color, "rook"), 
                Piece(1, 4, top_color, "rook"), 
                Piece(1, 5, top_color, "rook"), 
                Piece(1, 6, top_color, "rook"), 
                Piece(1, 7, top_color, "rook")
            ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ],
            [
                Piece(6, 0, bottom_color, "pawn"), 
                Piece(6, 1, bottom_color, "pawn"), 
                Piece(6, 2, bottom_color, "pawn"), 
                Piece(6, 3, bottom_color, "pawn"), 
                Piece(6, 4, bottom_color, "pawn"), 
                Piece(6, 5, bottom_color, "pawn"), 
                Piece(6, 6, bottom_color, "pawn"), 
                Piece(6, 7, bottom_color, "pawn")
            ],
            [
                Piece(7, 0, bottom_color, "rook"), 
                Piece(7, 1, bottom_color, "knight"), 
                Piece(7, 2, bottom_color, "bishop"), 
                Piece(7, 3, bottom_color, "queen"), 
                Piece(7, 4, bottom_color, "king"), 
                Piece(7, 5, bottom_color, "bishop"), 
                Piece(7, 6, bottom_color, "knight"), 
                Piece(7, 7, bottom_color, "rook")
            ],
        ]
        return layout