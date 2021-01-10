import pygame
from chess.board import Board
from .constants import *
from base.pause_menu import PauseMenu
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r

class Game:
    def __init__(self, win, online = False, network = None):
        
        self.win = win
        self.pause_menu = PauseMenu(self.win)
        self._init()
        self.online = online
        self.network = network

    def _init(self):
        self.selected_piece = None
        self.board = Board(WHITE)
        self.turn = WHITE
        self.valid_moves = []

    def tick(self):
        self.board.draw(self.win)
        if self.selected_piece and len(self.valid_moves) > 0:
            self.board.draw_possible_moves( self.win, self.valid_moves)
        self.input()
        if self.turn == self.board.top_color:
            if self.online:
                # self.board = self.network.send("update_moves")
                # self.board = self.network.send("name " + name)
                pass
            else:
                self.bot_move()
        pygame.display.update()

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
            self.turn = BLACK
        else:
            self.turn = WHITE

    def convertMouseToPosition(self, pos):
        x, y = pos
        print("mouse: ", x, y)
        row = (y - BOARD_PADDING_TOP) // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def bot_move(self):
        print("Bot move")
        self.change_turn()