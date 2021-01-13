import pygame
from chess.board import Board
from .constants import *
from base.pause_menu import PauseMenu
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r

from chess.bot import Bot

import datetime

class Game:
    def __init__(self, win, online = False, network = None):
        
        self.win = win
        self.pause_menu = PauseMenu(self.win)
        self._init()
        self.online = online
        self.network = network
        self.top_time = 600
        self.bottom_time = 600
        self.clock = pygame.time.Clock()
        self.dt = 0

    def _init(self):
        self.selected_piece = None
        self.board = Board(WHITE)
        self.valid_moves = []

    def tick(self):
        self.board.draw(self.win)
        if self.selected_piece and self.selected_piece.color == self.board.bottom_color and len(self.valid_moves) > 0:
            self.board.draw_possible_moves( self.win, self.valid_moves)
        self.input()
        if self.board.turn == self.board.top_color:
            self.top_time -= self.dt
            if self.online:
                # self.board = self.network.send("update_moves")
                # self.board = self.network.send("name " + name)
                pass
            else:
                self.bot_move()
        else:
            self.bottom_time -= self.dt
        pygame.draw.rect(self.win, WHITE, (25, 50, 50, 20))
        text_to_screen(self.win, datetime.timedelta(seconds=int(self.top_time)), 30, 51, 12)
        pygame.draw.rect(self.win, WHITE, (25, HEIGHT - 70, 50, 20))
        text_to_screen(self.win, datetime.timedelta(seconds=int(self.bottom_time)), 30, HEIGHT - 69, 12)
        pygame.display.update()
        self.dt = self.clock.tick(30) / 1000  # / 1000 to convert to second

    def input(self):
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            alt_f4 = (event.type == KEYDOWN and event.key == K_F4
            and (pressed_keys[K_LALT] or pressed_keys[K_RALT]))
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = self.convertMouseToPosition(pos)
                self.select_piece(row, col)
            if event.type == QUIT or alt_f4: sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE and not pressed_keys[K_p] or event.key == K_p and not pressed_keys[K_ESCAPE]:
                    if self.pause_menu.pause_menu() == 'Main Menu': return 'Main Menu'

    def reset(self):
        self._init()
        
    def select_piece(self, row, col):
        if self.selected_piece:
            result = self.move(row, col)
            if result == "check":
                print("Cannot move into check.")
            elif result:
                self.selected_piece = None
            else:
                print("Invalid move.")
            
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.board.player_color and piece.color == self.board.turn:
                self.selected_piece = piece
                self.valid_moves = self.selected_piece.get_possible_moves()
                return True
        return False

    def move(self, row, col, override_check=False):
        piece = self.board.get_piece(row, col)
        if self.selected_piece:
            if [row, col] in self.valid_moves or override_check:
                if self.selected_piece.type in UNCHECKABLE_PIECES:
                    threats = self.get_all_threats_piece(self.selected_piece, row, col)
                    if len(threats) > 0:
                        return "check"
                if(piece == 0):
                    self.board.move(self.selected_piece, row, col)
                else:
                    self.board.capture_piece(row, col, self.board.turn)
                    self.board.move(self.selected_piece, row, col)
                self.change_turn()
        else:
            return False
        return True
    
    def change_turn(self):
        if self.board.turn == WHITE:
            self.board.turn = BLACK
        else:
            self.board.turn = WHITE

    def convertMouseToPosition(self, pos):
        x, y = pos
        row = (y - BOARD_PADDING_TOP) // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def get_all_threats_piece(self, selected_piece, row, col):
        threats = []
        # Check for Pawn
        pawn_possibleLocations = [
            [row - 1, col - 1],
            [row - 1, col + 1]
        ]
        for location in pawn_possibleLocations:
            piece = self.board.get_piece(location[0], location[1])
            if piece != 0 and piece != "invalid":
                if piece.type == "pawn" and piece.color != self.selected_piece.color:
                    threats.append(piece)
        # Check for Knight
        knight_possibleLocations = [
            [row + 2, col - 1 ],
            [row + 1, col - 2 ],
            [row + 2, col + 1 ],
            [row + 1, col + 2 ],
            [row - 2, col + 1 ],
            [row - 1, col + 2 ],
            [row - 2, col - 1 ],
            [row - 1, col - 2 ]
        ]
        for location in knight_possibleLocations:
            piece = self.board.get_piece(location[0], location[1])
            if piece != 0 and piece != "invalid":
                if piece.type == "knight" and piece.color != self.selected_piece.color:
                    threats.append(piece)
        # Check for Rook
        rook_possibleLocations = {
            "top": [
                [row - 1, col],
                [row - 2, col],
                [row - 3, col],
                [row - 4, col],
                [row - 5, col],
                [row - 6, col],
                [row - 7, col]
            ],
            "left": [
                [row, col - 1],
                [row, col - 2],
                [row, col - 3],
                [row, col - 4],
                [row, col - 5],
                [row, col - 6],
                [row, col - 7]
            ],
            "right": [
                [row, col + 1],
                [row, col + 2],
                [row, col + 3],
                [row, col + 4],
                [row, col + 5],
                [row, col + 6],
                [row, col + 7]
            ],
            "bottom": [
                [row + 1, col],
                [row + 2, col],
                [row + 3, col],
                [row + 4, col],
                [row + 5, col],
                [row + 6, col],
                [row + 7, col]
            ]
        }
        for direction in rook_possibleLocations:
            blocked = False
            for location in rook_possibleLocations[direction]:
                piece = self.board.get_piece(location[0], location[1])
                if piece != 0 and piece != "invalid" and not blocked:
                    blocked = True
                    if piece.type == "rook" and piece.color != self.selected_piece.color:
                        threats.append(piece)
        # Check for King
        king_possibleLocations = {
            "top": [
                [row - 1, col],
                [row - 2, col],
                [row - 3, col],
                [row - 4, col],
                [row - 5, col],
                [row - 6, col],
                [row - 7, col]
            ],
            "left": [
                [row, col - 1],
                [row, col - 2],
                [row, col - 3],
                [row, col - 4],
                [row, col - 5],
                [row, col - 6],
                [row, col - 7]
            ],
            "right": [
                [row, col + 1],
                [row, col + 2],
                [row, col + 3],
                [row, col + 4],
                [row, col + 5],
                [row, col + 6],
                [row, col + 7]
            ],
            "bottom": [
                [row + 1, col],
                [row + 2, col],
                [row + 3, col],
                [row + 4, col],
                [row + 5, col],
                [row + 6, col],
                [row + 7, col]
            ],
            "corners": [
                [row - 1, col - 1],
                [row - 1, col - 2],
                [row - 1, col - 3],
                [row - 1, col - 4],
                [row - 1, col - 5],
                [row - 1, col - 6],
                [row - 1, col - 7],
                [row - 1, col + 1],
                [row - 1, col + 2],
                [row - 1, col + 3],
                [row - 1, col + 4],
                [row - 1, col + 5],
                [row - 1, col + 6],
                [row - 1, col + 7],
                [row + 1, col - 1],
                [row + 1, col - 2],
                [row + 1, col - 3],
                [row + 1, col - 4],
                [row + 1, col - 5],
                [row + 1, col - 6],
                [row + 1, col - 7],
                [row + 1, col + 1],
                [row + 1, col + 2],
                [row + 1, col + 3],
                [row + 1, col + 4],
                [row + 1, col + 5],
                [row + 1, col + 6],
                [row + 1, col + 7]
            ]
        }
        for direction in king_possibleLocations:
            blocked = False
            for location in king_possibleLocations[direction]:
                piece = self.board.get_piece(location[0], location[1])
                if piece != 0 and piece != "invalid" and not blocked:
                    blocked = True
                    if piece.type == "king" and piece.color != self.selected_piece.color:
                        threats.append(piece)
        # Check for Queen
        queen_possibleLocations = {
            "corners": [
                [row - 1, col - 1],
                [row - 1, col + 1],
                [row + 1, col - 1],
                [row + 1, col + 1]
            ],
            "horizontal": [
                [row, col - 1],
                [row, col + 1]
            ],
            "vertical": [
                [row - 1, col],
                [row + 1, col]
            ]
        }
        for direction in queen_possibleLocations:
            for location in queen_possibleLocations[direction]:
                piece = self.board.get_piece(location[0], location[1])
                if piece != 0 and piece != "invalid":
                    if piece.type == "queen" and piece.color != self.selected_piece.color:
                        threats.append(piece)
        # Check for Bishop
        bishop_possibleLocations = {
            "corners": [
                [row - 1, col - 1],
                [row - 1, col - 2],
                [row - 1, col - 3],
                [row - 1, col - 4],
                [row - 1, col - 5],
                [row - 1, col - 6],
                [row - 1, col - 7],
                [row - 1, col + 1],
                [row - 1, col + 2],
                [row - 1, col + 3],
                [row - 1, col + 4],
                [row - 1, col + 5],
                [row - 1, col + 6],
                [row - 1, col + 7],
                [row + 1, col - 1],
                [row + 1, col - 2],
                [row + 1, col - 3],
                [row + 1, col - 4],
                [row + 1, col - 5],
                [row + 1, col - 6],
                [row + 1, col - 7],
                [row + 1, col + 1],
                [row + 1, col + 2],
                [row + 1, col + 3],
                [row + 1, col + 4],
                [row + 1, col + 5],
                [row + 1, col + 6],
                [row + 1, col + 7]
            ]
        }
        for direction in king_possibleLocations:
            blocked = False
            for location in king_possibleLocations[direction]:
                piece = self.board.get_piece(location[0], location[1])
                if piece != 0 and piece != "invalid" and not blocked:
                    blocked = True
                    if piece.type == "bishop" and piece.color != self.selected_piece.color:
                        threats.append(piece)
        print("Threats: ", threats)
        return threats

    def bot_move(self):
        move = Bot.move(self.board, self)